# Chinese Markdown Report Generator for Model Evaluations

> **Chinese version:** [阅读中文版](model_evaluation_report.md)

`build_model_evaluation_report.py` organizes one or more local model runs, scoring JSONL files, or score aggregation JSON files into an answer-first Chinese technical report. The script runs entirely offline: it does not read key files, access the network, or execute model calls.

## Inputs and execution

A standard run directory contains `records.jsonl` and `run-manifest.json`. Multiple directories can be supplied by repeating the option:

```bash
python scripts/build_model_evaluation_report.py \
  --run-dir benchmarks/results/_pending/run-a \
  --run-dir benchmarks/results/_pending/run-b \
  --scores benchmarks/results/_pending/run-a/scores-judge-1.jsonl \
  --scores benchmarks/results/_pending/run-a/scores-judge-2.jsonl \
  --aggregation benchmarks/results/_pending/run-b/score-summary.json \
  --output benchmarks/results/_pending/evaluation-report.zh-CN.md
```

Alternatively, use paired `--responses` / `--manifest` options:

```bash
python scripts/build_model_evaluation_report.py \
  --responses path/to/run-a/records.jsonl \
  --manifest path/to/run-a/run-manifest.json \
  --responses path/to/run-b/records.jsonl \
  --manifest path/to/run-b/run-manifest.json \
  --output path/to/report.md
```

When `--manifest` is omitted, the script looks for `run-manifest.json` alongside each `records.jsonl`. Scoring JSONL files are matched by `run_id`; existing aggregations take priority, and their `responses_sha256` (and manifest hash, when available) is checked to prevent old scores from being bound to new responses. Existing output is not overwritten by default; overwriting requires an explicit `--overwrite`.

## Report boundaries

- Coverage is recalculated from the latest record for each `record_key`; manifest counts serve only as cross-checks;
- API authentication, quota/rate limiting, transport, truncation, and missing planned records are counted separately, rather than converted into low scores;
- Models covering all 24 questions are separated from those with partial coverage; partial-coverage scores are excluded from cross-model comparisons;
- The requested model and `returned_model` are both displayed; when multiple requested names collapse to the same returned model, an alias/version-collapse warning is issued, while records for each requested configuration are retained;
- Preliminary AI judge assessments and human scores are reported separately; AI does not count toward the formal threshold of at least two independent human raters;
- Invalid scores, judge errors, `flagged`, `uncertain`, and scoring disagreements are registered individually, rather than canceled out by medians;
- Only medians with equal weight per response are used; no mean scores or rankings are produced;
- Diagnostic runs such as smoke, probe, quota-recheck, and catalog are excluded by default. Explicitly add `--include-diagnostics` only when studying the diagnostics themselves; they remain marked as non-comparable.

The report does not reproduce prompt text; it retains only prompt-object hashes. Sensitive keys in generation parameters are redacted. Input snapshot times come from the manifest, so identical inputs, script, and parameters produce stable content.

## Offline regression tests

```bash
python -X utf8 -B scripts/test_build_model_evaluation_report.py -v
```

Tests use temporary synthetic data, read no credentials, and request no APIs.
