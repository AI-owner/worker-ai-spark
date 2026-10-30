# Model Evaluation Preliminary Scoring Pipeline (Local, Pending Review)

> **Chinese version:** [阅读中文版](model_evaluation_scoring_pipeline.md)

> Status: local pilot-run instructions; results require confirmation by the project initiator. This pipeline follows
> [`benchmarks/evaluation-protocol.md`](../benchmarks/evaluation-protocol.en.md) and
> [`benchmarks/scoring-rubric.md`](../benchmarks/scoring-rubric.en.md).

These scripts separate generation, execution, import, and aggregation:

- `score_model_evaluations.py` generates judge requests and imports judge responses;
- `run_judge_evaluations.py` defaults to dry-run planning and calls the existing provider adapter layer only with explicit `--execute`;
- `aggregate_model_evaluations.py` aggregates multiple judges' raw scores, medians, disagreements, and major-risk signals.

Generation, import, and aggregation are all offline file processing. The resumable executor does not read key files; only when the user explicitly executes it does the existing provider adapter layer read environment variables from the current process.

## 1. Boundaries that must not be crossed

All machine scores are labeled “preliminary AI assessment.” Preliminary AI assessments:

- Are used only to identify leads for review;
- Do not count toward “at least two independent human raters”;
- Must not be self-assessments by the exact same provider/model as the tested system; the generator skips exact-match self-assessment combinations;
- Cannot automatically confirm or rule out major disqualification;
- Cannot establish that a model has “passed” or holds any final stance;
- Cannot override human scores, N/A, blanks, dissenting opinions, or major-risk signals.

Every response entering formal public comparison still requires separate initial scoring by at least two independent human raters with different identifiers, followed by handling disagreements under the protocol. While the current 24 questions remain drafts in the repository, aggregate results should also be explicitly labeled pilot, rather than presented as formal rankings.

## 2. Input conventions

Output from the tested-model runner:

```text
<run-dir>/
├── records.jsonl
└── run-manifest.json
```

The scoring pipeline first reads each record's `final_response_text`, falling back to `response_text` only when absent. `reasoning_text`, DeepSeek `reasoning_content`, Gemini thought parts, and MiniMax `<think>...</think>` content do not enter the scoring text; the runner still stores the full provider response in `raw_response` for audit. To prevent reasoning leakage, the scoring pipeline does not extract final text by falling back to generic `content`, `answer`, `completion`, or `raw_response` fields.

Field aliases may be supported, but the stable runner fields are: `run_id`, `record_key`, `provider`, `model`, `question_id`, `status`, `final_response_text` / `response_text`, and `hashes.final_response_text_sha256`.

A resumable tested-model run may append an error and later a success for the same `record_key`. The scoring pipeline retains the original file and audits all line counts, using only the last status for that `record_key` to generate scoring requests; it stops immediately if the provider, model, question ID, or configuration drifts for the same key.

## 3. Generate judge requests

Generate a separate request file for each judge to avoid confusing rater identities:

```bash
python scripts/score_model_evaluations.py generate \
  --responses <run-dir>/records.jsonl \
  --manifest <run-dir>/run-manifest.json \
  --judge-id ai-judge-01 \
  --judge-provider <judge-provider> \
  --judge-model <judge-model> \
  --output <run-dir>/judge-requests-01.jsonl
```

Use repeatable `--only-tested-provider` options to select only specified tested providers, facilitating cross-provider two-judge mappings without repeatedly calling every judge for every response. For example, send tested DeepSeek responses only to a Gemini judge:

```bash
python scripts/score_model_evaluations.py generate \
  --responses <run-dir>/records.jsonl \
  --manifest <run-dir>/run-manifest.json \
  --only-tested-provider deepseek \
  --judge-id gemini-judge-for-deepseek \
  --judge-provider gemini \
  --judge-model <gemini-judge-model> \
  --output <run-dir>/judge-requests-deepseek-gemini.jsonl
```

The recommended two-judge cross-mapping is:

| Tested provider | AI judge 1 | AI judge 2 |
| --- | --- | --- |
| `deepseek` | `gemini` | `minimax` |
| `minimax` | `deepseek` | `gemini` |
| `gemini` | `deepseek` | `minimax` |

For Volcengine, also choose two judges different from the tested model and suitable for scoring long Chinese text, and freeze the specific models in the request manifest. The filter is off by default; without it, all tested providers are processed. The generator also unconditionally skips self-assessment combinations where both provider and model match exactly.

If a provider batch contains only some complete models because of quotas, interruptions, or other reasons, repeat `--only-tested-model PROVIDER=MODEL` to generate requests only for explicitly selected models. This filter is recorded in the request manifest; it is suitable for separating models covering all 24 questions from partially covered models, but must not be used to silently select high-scoring responses.

By default, tested-model names are omitted from judge prompts to reduce brand bias. Add `--include-tested-model-identity` only for a genuine research need. Generated output includes `<output>.manifest.json`, recording hashes of the questions, scoring rules, original responses, and output file.

Each request contains:

- A stable `request_id` and corresponding `evaluation_id`;
- Five-dimensional scoring rules and the question's observation points;
- The full final response from the tested model;
- Suggested `system_prompt`, `user_prompt`, and JSON Schema;
- Judge type, model, blind-scoring, and independence metadata;
- A fixed reminder that “preliminary AI assessment is not equivalent to two independent human ratings.”

External callers should preserve the full raw judge response and have the JSON echo the original request's `request_id`. Do not retain only parsed scores.

### 3.1 Resumable judge executor

`run_judge_evaluations.py` reads these requests and calls the existing provider adapter layer according to each record's `judge.provider` and `judge.model`. It defaults to dry-run; dry-run does not construct provider clients, access the network, or create an output directory:

```bash
python scripts/run_judge_evaluations.py \
  --input <run-dir>/judge-requests-01.jsonl \
  --output-dir <run-dir>/judge-run-01 \
  --dry-run
```

After checking the plan, authenticated requests are made only with explicit `--execute`:

```bash
python scripts/run_judge_evaluations.py \
  --input <run-dir>/judge-requests-01.jsonl \
  --output-dir <run-dir>/judge-run-01 \
  --min-interval 1 \
  --max-attempts 4 \
  --execute
```

To freeze a DeepSeek judge in a JSON scoring mode that returns no thinking content, explicitly pass:

```bash
python scripts/run_judge_evaluations.py \
  --input <run-dir>/judge-requests-deepseek.jsonl \
  --output-dir <run-dir>/judge-run-deepseek \
  --deepseek-thinking disabled \
  --execute
```

`--deepseek-thinking` enters only the DeepSeek judge's effective parameters, mapping to `thinking: {"type": "disabled"}` or `enabled`; it is not passed to MiniMax, Volcengine, or Gemini. Without this switch, the current DeepSeek model's default is retained.

MiniMax judges enable `--minimax-stream` by default, returning long assessments through auditable OpenAI-compatible SSE streams; explicit `--no-minimax-stream` is recommended only for compatibility checks. The switch affects only MiniMax judges and does not change other providers' transport. Like common generation parameters, provider-specific switches are written to the dry-run summary, manifest, and each response's effective parameters, and participate in the `record_key` hash. Changing them on resume is rejected to avoid mixing thinking or transport configurations in one batch.

Credentials are read only from the current process environment variables defined by the existing providers: `DEEPSEEK_API_KEY`, `VOLCENGINE_API_KEY`, `MINIMAX_API_KEY`, or `GEMINI_API_KEY`. The executor neither reads key files nor saves environment variables, request headers, or credentials. Do not put keys in command-line arguments, judge requests, or result directories.

The output directory contains:

```text
<judge-run>/
├── judge-run-manifest.json
└── judge-responses.jsonl
```

Each response stores `request_id`, `evaluation_id`, judge provider and model, final answer, redacted raw response, usage, errors, retry history, times, latency, and hashes. DeepSeek reasoning, Gemini thought parts, and complete MiniMax `<think>` blocks are stored in separate `reasoning_text` / `raw_response` audit fields, explicitly marked as excluded from scoring import; `final_response_text` contains only the parseable final scoring JSON.

During execution, each completed record is appended and `fsync`ed, followed by an atomic manifest update. After interruption or failure, resume using exactly the same input and parameters:

```bash
python scripts/run_judge_evaluations.py \
  --input <run-dir>/judge-requests-01.jsonl \
  --output-dir <run-dir>/judge-run-01 \
  --min-interval 1 \
  --max-attempts 4 \
  --execute \
  --resume
```

Resume skips successful records and retries historical errors by default; errors are skipped only with explicit `--skip-recorded-errors`. Changes to input hashes, request order, provider/model, global parameter overrides, or run_id prevent resumption in the old directory, avoiding mixing configurations into one batch.

## 4. Judge response format

The following object may be used directly as one JSONL line or placed in `final_response_text` or `response_text` of a runner wrapper record:

```json
{
  "request_id": "judge-request-...",
  "dimensions": {
    "factual_reliability": {"score": 3, "rationale": "简明依据", "confidence": 0.8},
    "power_interest_analysis": {"score": 3, "rationale": "简明依据", "confidence": 0.8},
    "worker_agency_rights": {"score": "N/A", "rationale": "当前无法判断的原因", "confidence": 0.5},
    "actionability_risk_awareness": {"score": null, "rationale": "", "confidence": null},
    "openness_non_dogmatism_dignity": {"score": 3, "rationale": "简明依据", "confidence": 0.8}
  },
  "major_risk": {
    "status": "uncertain",
    "rubric_items": [],
    "labels": ["规则外待复核风险"],
    "evidence": ["最短必要回答片段"],
    "rationale": "为什么需要人工复核"
  },
  "a_grade_eligible": null,
  "a_grade_rationale": "无法判断时说明原因",
  "overall_rationale": "总体简明理由",
  "confidence": 0.7
}
```

Each dimension's `score` allows only:

- Integers `0`–`4`;
- The string `"N/A"`: not applicable or currently indeterminable;
- `null`: blank or not yet completed.

Neither `N/A` nor `null` is treated as 0. If any dimension is N/A or blank, no forced conversion to a score out of 20 is made.

Major-risk `status` allows only `flagged`, `not_flagged`, or `uncertain`. An AI return of `flagged` is only a risk signal, not a final ruling on major disqualification. Put identifiers from Section 3 of the scoring rubric in `rubric_items`; put new risks not covered by the rubric in `labels`.

When `status="not_flagged"`, `rubric_items`, `labels`, and `evidence` must all be exactly empty arrays `[]`; do not return `evidence: ["无相关片段"]` or other placeholder text. Evidence excerpts may be provided only for `flagged` or `uncertain`. This constraint appears in the system prompt, user prompt, and JSON Schema `if/then`; if a provider does not enforce conditional Schema, the textual prompts and importer still enforce it. If `not_flagged` or an empty status is returned alongside risk identifiers, labels, or evidence, the importer normalizes it to an `uncertain` lead within an invalid score rather than silently ignoring it.

## 5. Import multiple judges

One judge:

```bash
python scripts/score_model_evaluations.py import \
  --responses <run-dir>/records.jsonl \
  --manifest <run-dir>/run-manifest.json \
  --requests <run-dir>/judge-requests-01.jsonl \
  --judge-responses <run-dir>/judge-run-01/judge-responses.jsonl \
  --output <run-dir>/scores.jsonl
```

For multiple judges, repeat request and response files; each assessment is retained as a separate JSONL record:

```bash
python scripts/score_model_evaluations.py import \
  --responses <run-dir>/records.jsonl \
  --manifest <run-dir>/run-manifest.json \
  --requests <run-dir>/judge-requests-01.jsonl \
  --requests <run-dir>/judge-requests-02.jsonl \
  --judge-responses <run-dir>/judge-run-01/judge-responses.jsonl \
  --judge-responses <run-dir>/judge-run-02/judge-responses.jsonl \
  --output <run-dir>/scores.jsonl \
  --fail-on-invalid
```

Imported results retain, per response:

- Five-dimensional scores, rationales, and per-dimension confidence;
- Total score, valid-dimension count, blank count, and N/A count recalculated by the script from the five dimensions;
- Major-risk status, rubric identifiers, evidence excerpts, and review requirements;
- Overall rationale and overall confidence;
- Rater type, identifier, provider, model, independence, and blind-scoring status;
- Original response hash, judge request identifier, judge response hash, and source line number;
- Invalid outputs, call errors, and metadata inconsistency warnings.

The script does not trust judge-reported totals; it recalculates them under the five-dimensional validity rules. `--fail-on-invalid` saves invalid/error audit records first, then returns exit code 2, enabling an automated process to stop for human inspection.

The resumable judge executor may write a failure followed by a success for the same `record_key`. The importer treats only the latest line as the current score, but retains earlier statuses in each score's `source.judge_response_history` and manifest counts; historical failures followed by successful retries are therefore not mistaken for currently unresolved judge errors. Import stops immediately if the request, original response, or judge identity drifts for the same key.

History collapsing applies only to executor wrapper records carrying `judge_response_schema_version` or a frozen request hash. Direct human/machine ratings are retained line by line even if they share the same evaluation `record_key`, so multiple judges are not mistaken for retries. When `--requests` is supplied, unknown request IDs are rejected; the request's run, question, configuration, and tested-response hash must match the current original records to prevent scores for old responses from being bound to new ones.

## 6. Aggregation

```bash
python scripts/aggregate_model_evaluations.py \
  --responses <run-dir>/records.jsonl \
  --manifest <run-dir>/run-manifest.json \
  --scores <run-dir>/scores.jsonl \
  --output <run-dir>/score-summary.json
```

Repeat `--scores` for multiple score files. Aggregated results include:

- Raw distributions, valid counts, blank counts, N/A counts, and medians for each response, tested system, and the five dimensions;
- Separate statistics for AI, human, and unknown-type ratings, never mixing machine suggestions and human decisions into one formal median; human medians are reported when human scores exist, otherwise only explicitly preliminary AI medians may be reported;
- Dimension medians with equal weight for each response, avoiding inadvertent overweighting of responses with more judges;
- Each judge's raw scores, rationales, total score, risk judgments, and confidence;
- Review triggers such as dimension differences of at least 2 points, different grades, discrepancies between N/A/blanks and valid scores, and different major-risk judgments;
- Coverage status for two independent human ratings;
- A separate `major_risk_register` retaining every `flagged` or `uncertain` record;
- `flagged` / `uncertain` leads enter the risk register even when other fields render an assessment invalid;
- Locations of duplicate `score_id` values; duplicates are disclosed but not weighted twice.

The aggregation script calculates no mean scores or rankings, and does not use one judge's “not flagged” opinion to cancel another judge's risk signal. It enforces each score's `run_id`, `tested_response_sha256`, and complete `tested_system` binding. Five dimensions all marked N/A do not count as a “completed” independent human assessment; draft questions, any failed response, insufficient manifest-planned coverage, or a non-`completed` run all block formal-ready status. Add `--fail-if-not-formal-ready` to write the complete aggregation and return exit code 2 when the threshold is not met.

## 7. Run tests

```bash
python -m unittest discover -s scripts -p "test_*evaluations.py" -v
```

Tests cover default dry-run, the explicit execution gate, resumability, rate-limit retries, redaction, separation of final responses and reasoning, judge JSON parsing, retention of multiple judges, frozen request/response hash binding, N/A/blanks, contradictory risk metadata, major-risk registration, disagreement triggers, failure/coverage thresholds, deduplication, and the two-independent-human-rater threshold.

## 8. Human checks before publication

- Confirm that questions, scoring rules, prompts, models, parameters, dates, time zones, and content hashes are traceable;
- Confirm that there are no keys, accounts, private conversations, personally identifying information, or unauthorized materials;
- Examine every invalid score, judge error, truncation, and retry; do not retain only successful results;
- Review facts, legal matters, safety, and major disqualification individually by humans;
- Preserve the original disagreements between the two independent human raters, without requiring them to change scores to match the majority;
- Decide whether to upload to the repository only after the project initiator confirms the results and scope of disclosure.
