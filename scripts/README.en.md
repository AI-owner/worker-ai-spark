# Scripts

> **Chinese version:** [阅读中文版](README.md)

> This directory contains scripts used by the project. They currently depend only on the Python standard library, with no third-party packages.

> Run all commands below from the repository root.

---

## validate_benchmarks.py

Validates the basic structure and content of `../benchmarks/first-batch.zh-CN.jsonl`.

**Dependencies**: Python standard library only (no `pip install` required).

**Run**:

```bash
python scripts/validate_benchmarks.py
```

You can also specify the file path explicitly:

```bash
python scripts/validate_benchmarks.py benchmarks/first-batch.zh-CN.jsonl
```

**Checks**:

- Every JSONL line can be parsed;
- Exactly 24 first-batch questions are present;
- IDs are unique and follow the format `WAI-001` … `WAI-024`;
- All required fields are present;
- Array fields (`observation_points`, `severe_deductions`, `follow_up`) have the correct type and are nonempty;
- `language` is `zh-CN`;
- `status` is an allowed value (`draft` / `review` / `stable`);
- Titles, scenarios, and questions are nonempty.

**Output**:

- Success: `Benchmark validation passed.` / `Total cases: 24` / `Errors: 0`;
- Failure: reports the specific line number, question ID, and reason, and exits with a nonzero code.

The script is also run automatically by `.github/workflows/validate-benchmarks.yml` on every push and Pull Request.

---

## validate_benchmark_sources.py

Performs a read-only check of the 24 base-question fields in `benchmarks/first-batch.md` and `benchmarks/first-batch.zh-CN.jsonl`:

```bash
python scripts/validate_benchmark_sources.py
```

The script exits with a nonzero status if titles, groups, scenarios, main questions, key observations, or tendencies warranting severe deductions drift. Follow-up questions are not automatically rewritten; differences are reported question by question as warnings requiring review.

This script and its tests are also included in `.github/workflows/validate-benchmarks.yml`.

Standard-library tests:

```bash
python -B scripts/test_validate_benchmark_sources.py
```

---

## run_model_evaluations.py

The evaluation runner requests model APIs only when `--execute` is explicitly used. MiniMax uses OpenAI-compatible SSE streaming responses by default to avoid interruption of long non-streaming connections for reasoning models:

```bash
python scripts/run_model_evaluations.py run \
  --provider minimax \
  --model minimax=MiniMax-M2.7 \
  --output-dir benchmarks/results/_pending/minimax-run \
  --execute
```

- `--minimax-stream` is the default; `--no-minimax-stream` is only for compatibility checks;
- This switch changes only MiniMax transport, not DeepSeek, Volcengine, or Gemini;
- The command-line `--max-tokens` is a unified abstraction parameter; MiniMax requests map it to `max_completion_tokens`;
- Successful records store redacted SSE chunks in order in `raw_response`, distinguishing `[DONE]` termination from MiniMax's “terminal `finish_reason` + clean EOF” completion; EOF without a termination reason or an abnormal disconnection remains a partial error;
- Chunks from interrupted streams belong only to that attempt's error/retry history and are neither merged with subsequent attempts nor recorded as successful; when the provider returns no usage, an empty object is retained and `usage_missing: true` is set;
- After stream content is merged, only complete MiniMax `<think>...</think>` blocks are separated into `reasoning_text`; unclosed tags are not silently deleted.

Gemini still uses non-streaming `generateContent` by default. For models producing long responses, you can explicitly switch to the official `streamGenerateContent?alt=sse` JSON SSE endpoint:

```bash
python scripts/run_model_evaluations.py run \
  --provider gemini \
  --model gemini=models/gemma-4-31b-it \
  --gemini-stream \
  --max-tokens 8192 \
  --output-dir benchmarks/results/_pending/gemma-stream-run \
  --execute
```

- `--gemini-stream` changes only Gemini transport; `--no-gemini-stream` is the default;
- The API key is still sent only through the `x-goog-api-key` request header, never in the URL or persisted results;
- `raw_response` stores redacted JSON chunks in wire order, HTTP status, protocol, clean-EOF termination, and the final `finishReason`; `modelVersion`, `usageMetadata`, thought parts, and the final answer go into separate auditable fields;
- A stream succeeds only if the primary candidate returns an explicit terminal `finishReason` and the connection ends normally; abnormal disconnections, missing terminal status, or missing final text are errors; `MAX_TOKENS` remains a truncation error;
- `gemini_stream` is included in the run manifest, each request's effective parameters, and the request hash, and must not change on resume, to avoid mixing streaming and non-streaming records in one batch.

Offline regression tests (no keys read and no network requests):

```bash
python -B scripts/test_run_model_evaluations.py
```

---

## run_judge_evaluations.py

The preliminary AI assessment request executor defaults to dry-run and calls a provider only with explicit `--execute`. DeepSeek can freeze its thinking mode with `--deepseek-thinking enabled|disabled`; this value enters only the DeepSeek request's `thinking.type` and is not passed to other providers.

MiniMax judges use `--minimax-stream` by default; `--no-minimax-stream` is available for compatibility checks. These provider-specific switches are written to the manifest, effective parameters, and record hash; `--resume` requires them to match the original batch. See [`model_evaluation_scoring_pipeline.md`](model_evaluation_scoring_pipeline.en.md) for full usage and audit boundaries.

Offline regression tests (no keys read and no network requests):

```bash
python -B scripts/test_run_judge_evaluations.py
```

---

## build_model_evaluation_report.py

Generates a Chinese Markdown technical report from one or more local response runs, scoring JSONL files, or aggregation JSON files. The script recalculates coverage offline, separately displays API failures, complete 24-question and partial models, and preliminary AI assessments and human scores, while retaining invalid scores, risks, and disagreements individually. Both the requested model and `returned_model` are shown; diagnostic runs are excluded from comparison by default.

```bash
python scripts/build_model_evaluation_report.py \
  --run-dir benchmarks/results/_pending/run-a \
  --scores benchmarks/results/_pending/run-a/scores.jsonl \
  --output benchmarks/results/_pending/evaluation-report.zh-CN.md
```

See [`model_evaluation_report.md`](model_evaluation_report.en.md) for complete input conventions and boundaries. Offline regression tests:

```bash
python -X utf8 -B scripts/test_build_model_evaluation_report.py -v
```

## Bilingual documentation checks

Check counterpart coverage, language switches, local links, and version synchronization with the command below. See the [documentation language guide](../docs/languages.en.md) for maintenance steps.

```bash
python scripts/validate_translations.py
```
