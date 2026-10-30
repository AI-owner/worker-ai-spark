# Evaluation Results

> **Chinese version:** [阅读中文版](README.md)

> This directory stores reproducible raw run packages, complete answers, and per-question scores produced with the evaluation questions. Each package may also include a technical report for that batch; narrative reports spanning batches may still be placed in `../../model-evaluations/`.

---

## Suggested Organization

- Create one directory per batch at `results/<run-id>/` to avoid incorrectly merging different configurations;
- Individual evaluation records follow [../evaluation-record-template.en.md](../evaluation-record-template.en.md);
- Follow [../evaluation-protocol.en.md](../evaluation-protocol.en.md) for execution;
- Overall reports should include the ten items listed in Section IV of `../scoring-rubric.md`, rather than presenting only a leaderboard.

---

## Pre-Submission Checklist

- Have original model answers been saved, without selective excerpts?
- Have question, principle, and rubric versions been frozen and file hashes recorded?
- Have system/developer/user prompts, sampling parameters, tools, and knowledge bases been recorded?
- Is the execution mode described (base model / principles added / knowledge base connected / fine-tuning / other)?
- Are major disqualifications flagged without being obscured by averages?
- Have fabricated laws, institutions, and avenues of remedy been avoided?
- Is privacy respected, with no identifiable personal information uploaded?
- Are invisible system configurations, retries, missing data, and other limitations explained?

---

## Current Status

- [wai-20260825-deepseek-pilot/README.en.md](wai-20260825-deepseek-pilot/README.en.md): a **pilot package pending review**, covering 3 requested DeepSeek models, 24 questions, and two AI blind-rating streams. This is not an official model ranking and has no independent human scores yet. Read the package's [wai-20260825-deepseek-pilot/evaluation-report.en.md](wai-20260825-deepseek-pilot/evaluation-report.en.md) first.
- Interruptions, quota issues, and authentication diagnostics for other providers remain only in the local `_pending/` directory excluded by `.gitignore`; they are not part of the results proposed for upload.
- See [FOLLOW_UP_EVALUATION_PLAN.en.md](FOLLOW_UP_EVALUATION_PLAN.en.md) for resumption points and conditions for proceeding to the next batch.

The evaluation questions are in [../first-batch.en.md](../first-batch.en.md) and [../first-batch.zh-CN.jsonl](../first-batch.zh-CN.jsonl). The project lead must still confirm the publication scope for all results.
