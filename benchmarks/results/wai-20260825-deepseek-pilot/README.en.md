# DeepSeek 24-Question Pilot Package Pending Review

> **Chinese version:** [阅读中文版](README.md)

> Status: machine runs and two AI blind-rating streams are complete, pending confirmation by the project lead. This is neither an official ranking nor a human-review conclusion.

## Key Findings First

- Each of 3 requested models completed 24 questions, totaling 72/72 successful answers, with no empty answers, truncation, or API errors.
- Scoring used two blind-rating streams: `MiniMax-M2.1-highspeed` and `MiniMax-M3`. After targeted retries, every answer has two valid preliminary AI ratings. The original 5 invalid ratings remain preserved; they were neither overwritten nor included in medians.
- All three models have an equally answer-weighted median AI total score of 16/20; this is insufficient to support a strict ranking.
- There are currently 3 risk signals awaiting human review, 28 answers with scoring disagreements, and 0 human ratings, so the requirements for formal comparison are not met.

For complete coverage, five-dimensional medians, and lists of risks and disagreements, see the [Chinese original report](evaluation-report.zh-CN.md) and its [English translation](evaluation-report.en.md).

## Run Boundaries

- Question bank: the 24 main questions in `benchmarks/first-batch.zh-CN.jsonl`; follow-ups are excluded.
- Models evaluated: `deepseek-v4-flash`, `deepseek-v4-flash-vision-exp`, and `deepseek-v4-pro`.
- Generation configuration: no additional system prompt, `max_tokens=8192`, and DeepSeek thinking explicitly disabled; see `run-manifest.json` for detailed configuration and hashes.
- Evaluation stage: pilot; `formal_comparison_allowed=false`.

## File Descriptions

- `records.jsonl`, `run-manifest.json`: 72 complete answers and the run manifest.
- `package-manifest.json`: scoring status after packaging and key file hashes; `run-manifest.json` retains the original generation-stage `scoring_status=unscored`, without rewriting history.
- `scores-*.jsonl`: normalized preliminary AI ratings; `retry` files contain targeted retries with new rater identifiers.
- `score-summary.json`: equally answer-weighted aggregation and registers of invalid records, risks, and disagreements.
- `evaluation-report.zh-CN.md`: Chinese technical report for human inspection; [English translation](evaluation-report.en.md).

This package was copied and promoted from the local `_pending` review area. Original audit manifests may still record repository-relative paths from generation time; the official aggregation and report were regenerated in this directory. Complete judge requests, scoring prompts, and raw streaming responses remain in the local `_pending` audit area and are excluded from the proposed public package; normalized score files retain their hash bindings and validation status. Pre-upload exact-match checks for credential values and local absolute paths both returned 0. The project lead should still review privacy, content, versions, and publication scope.
