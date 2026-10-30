# Follow-Up Model Evaluation Completion Plan

> **Chinese version:** [阅读中文版](FOLLOW_UP_EVALUATION_PLAN.zh-CN.md)

> Status: local resumption plan; this does not mean the models concerned have completed evaluation, failed, or entered formal comparison.
>
> Updated: 2026-08-25

## I. Current Resumption Points

| Provider | Completed | Local resumption point | Treatment in this round |
| --- | --- | --- | --- |
| DeepSeek | 3 models × 24 questions; two valid preliminary AI rating streams and an aggregate report | None | Promoted to the `wai-20260825-deepseek-pilot/` package pending review |
| MiniMax | `M2`, `M2.1`, `M2.1-highspeed`, and `M2.5` each 24/24; `M2.5-highspeed` 14/24 | Main answers 110/192; DeepSeek-flash judge 96/96 and DeepSeek-pro judge 60/96 for the first four models | Retain in `_pending`; excluded from this public package |
| Gemini | 5 requested configurations each 24/24; first DeepSeek judge stream 120/120, valid under strict import | Main batch: 202 successes, 15 errors, 23 not generated; second MiniMax judge stream 37/120 | Handle complete and partial-coverage configurations separately; not published this round |
| Volcengine | Both credential lines can independently read the model directory | Corrected the local parsing issue that treated the entire file as a single token; requests to 6 chat models with one credential line still return 401 | Verify inference authentication, region, and account permissions first; do not record 401 as model failure |

All counts come from the latest local JSONL records. Do not delete interruption records or raw errors; resume using the original directory and `--resume`.

## II. Resumption Order

1. **MiniMax main answers**: resume `run-20260825-minimax-baseline` with the original 8 models, identical parameters, and run id, first reaching 192/192. Do not introduce another system prompt or change `max_tokens=8192`.
2. **MiniMax scoring**: resume DeepSeek-pro judging of the first four completed models to 96/96. Once main answers are complete, generate DeepSeek-flash and DeepSeek-pro blind-rating requests separately for each of the other four models. Use strict import; invalid ratings may only receive targeted retries under new judge ids.
3. **Gemini complete configurations**: first resume `judge-run-complete24-minimax-m21hs` from 37/120. Once complete, generate a derived complete subset, aggregation, and report only for the 5 configurations with 24/24 coverage. Two provider aliases must not be described as independent underlying models.
4. **Gemini partial configurations**: wait for daily quota recovery, then complete all 24 questions in a new independent run. Do not place scores from 20/24 or 21/24 subsets alongside fully covered models.
5. **Gemma 4 31B**: perform a single-question smoke test using the implemented but not yet empirically tested `--gemini-stream`. Proceed to 24 questions only with normal EOF, a terminating `finishReason`, and nonempty, untruncated output.
6. **Volcengine**: first perform a single-question smoke test using a single credential line. After confirming successful chat-inference authentication, freeze the allowlist of current general-purpose text models. Do not automatically include media, embedding, or historical specialized models.

## III. Requirements for Entering the Public Results Directory

- Every requested model must have 24/24 successes, unique question IDs, and nonempty, untruncated final answers;
- The manifest must close out correctly, with verifiable question bank, prompts, generation parameters, and file SHA-256 hashes;
- At least two cross-provider AI blind-rating streams must each have valid records; AI results may only be labeled preliminary;
- Preserve invalid records, judge errors, risk signals, and disagreements individually and include them in the report;
- Formal comparison additionally requires at least two independent human raters for every answer and completed human review of risks and disagreements;
- Promote from `_pending` only after the project lead gives final confirmation of privacy, facts, model scope, and proposed public files.

## IV. Principles for Resumption Commands

Pass credentials only through environment variables; do not write them into command files, manifests, or the repository. Resumption commands must retain the original input, models, parameters, output directory, and run id, and explicitly add `--resume`. If the runner rejects configuration or hash drift, stop and investigate; do not overwrite the original directory or delete historical records.

## V. Nonblocking Scoring-Pipeline Repairs

The following issues did not affect the promoted DeepSeek package: it was verified to contain exactly two valid judge ratings per answer; its aggregation can be reconstructed verbatim from the listed score files; and its manifest explicitly prohibits formal comparison. Nevertheless, add tests and fix these issues before resuming subsequent batches:

- The aggregator should use a logical scoring key comprising “answer + judge identity + provider + judge model” to prevent a valid retry from the same judge being counted again because it has a new `score_id`;
- The report generator should not trust external aggregation based solely on response-file hashes; it should verify the complete system/answer set and score-file hashes, or recompute derived conclusions on the spot;
- Without a trusted manifest, planned coverage, or `completed` status, the aggregator must fix formal-comparison readiness at `false`.
