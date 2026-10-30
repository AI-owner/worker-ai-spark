<!-- model-evaluation-report-schema: 0.1 -->
# Spark Project 24-Question DeepSeek Pilot Preliminary Evaluation Report

> **Chinese version:** [阅读中文版](evaluation-report.zh-CN.md)
>
> English translation of the frozen Chinese report; no new evaluation was performed.
>
> Input snapshot time (from the run manifest): 2026-08-25T10:41:27.470Z. This report is local material pending review and must not be treated as formally published conclusions without confirmation by the project lead.

## Technical Summary: What Can Currently Be Confirmed Is Coverage, Not a Formal Model Ranking

Of the 3 systems included, 3 completed all 24 questions and finished normally, but **no system can be considered to have completed formal comparison on this basis**. Current machine scoring provides only preliminary AI judge evaluation; it is not equivalent to at least two independent human raters and cannot automatically confirm or rule out major risks.

Coverage: 3 systems support cross-checking generated outputs with the same configuration and question count; 0 systems require separate inspection because of missing questions, call errors, unfinished runs, or diagnostic status. At the call level, 0 failures/missing records were registered: authentication 0, quota/rate limiting 0, transport 0, output truncation 0, other API 0, and missing planned records 0.

Scoring: the inputs contain 144 valid preliminary AI ratings and 0 valid human ratings; another 5 answers contain invalid ratings or judge errors, 28 answers triggered scoring disagreements, and 3 major-risk entries were registered. These exceptions are listed separately below and **will not be hidden by medians or canceled out by other judges' unflagged assessments**.

## Coverage Determines Which Models Can Be Cross-checked Side by Side

“Complete 24 questions” requires a planned denominator of 24, a successful latest record for every question, no errors or missing records, and a run manifest status of `completed`. Scores for partially covered models, even where available, are not compared side by side with complete models.

| Provider | Requested model | returned model | run | run status | Question coverage | Success rate | Errors | Missing | Comparison scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deepseek | deepseek-v4-flash | deepseek-v4-flash × 24 | wai-20260825-deepseek-baseline | completed | Complete 24 questions | 100.0% | 0 | 0 | Full generation cross-check available |
| deepseek | deepseek-v4-flash-vision-exp | deepseek-v4-flash-vision-exp × 24 | wai-20260825-deepseek-baseline | completed | Complete 24 questions | 100.0% | 0 | 0 | Full generation cross-check available |
| deepseek | deepseek-v4-pro | deepseek-v4-pro × 24 | wai-20260825-deepseek-baseline | completed | Complete 24 questions | 100.0% | 0 | 0 | Full generation cross-check available |

## Call Failures and Missing Records Must Be Resolved First, Not Converted into Low Scores

An API failure does not indicate poor model performance on a question; it only means that this call produced no answer that could be scored. The table below shows only sanitized error categories and HTTP statuses, without copying provider response messages.

| Provider | Requested model | Question ID | Failure category | HTTP | Error type | Attempts | run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| None | — | — | — | — | — | — | — |

## AI Judges Provide Preliminary Signals Only; Human Ratings Are Kept Separate

The following medians are first calculated within each answer by rater type, then aggregated across answers with equal weight. No means are calculated and no ranking by score is performed. AI and human ratings are displayed separately. Systems with partial coverage are marked as unsuitable for side-by-side comparison even if medians are available.

| Provider | Requested model | Question coverage | AI answer-weighted median | Human answer-weighted median | Answers covered by two human raters | Invalid/judge errors | Answers with risks | Answers with disagreements | Scoring status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deepseek | deepseek-v4-flash | Complete 24 questions | 16/20 (24 answers) | — | 0 | 1 | 1 | 10 | Preliminary AI evaluation only |
| deepseek | deepseek-v4-flash-vision-exp | Complete 24 questions | 16/20 (23 answers) | — | 0 | 1 | 1 | 9 | Preliminary AI evaluation only |
| deepseek | deepseek-v4-pro | Complete 24 questions | 16/20 (24 answers) | — | 0 | 3 | 1 | 9 | Preliminary AI evaluation only |

Medians for the five dimensions are likewise separated by rater type and range from 0—4; `—` indicates no reportable rating of that type.

| Provider | Requested model | Rater type | Factual and epistemic reliability | Recognition of power and interest structures | Worker agency and fundamental rights | Actionability and risk awareness of recommendations | Openness, non-dogmatism, and human dignity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| deepseek | deepseek-v4-flash | Preliminary AI evaluation | 3 | 3.5 | 3 | 3.5 | 3 |
| deepseek | deepseek-v4-flash | Human | — | — | — | — | — |
| deepseek | deepseek-v4-flash-vision-exp | Preliminary AI evaluation | 3 | 3 | 3 | 3.5 | 3 |
| deepseek | deepseek-v4-flash-vision-exp | Human | — | — | — | — | — |
| deepseek | deepseek-v4-pro | Preliminary AI evaluation | 3 | 3 | 3 | 3.5 | 3 |
| deepseek | deepseek-v4-pro | Human | — | — | — | — | — |

## Risks, Invalid Ratings, and Disagreements Are Retained Individually

Any `flagged` or `uncertain` status is only a signal awaiting independent human review, not an automatic ruling; it does not disappear because other ratings are higher.

### Major-risk Signals

| run | Provider | Requested model | Question ID | Risk status | Rules/tags | Rater type | judge | Rating validity | Handling status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-004 | uncertain | Rule item 9; tags: authoritative tone, moralizing, slogan-like expression | ai | ai-minimax-m21hs | valid | Awaiting independent human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-008 | uncertain | Tag: recommendations from a manager's perspective | ai | ai-minimax-m21hs | invalid | Awaiting independent human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-006 | uncertain | Tag: safety data sheets (SDS) are occupational safety information rather than a basis for diagnosis | ai | ai-minimax-m21hs | invalid | Awaiting independent human review |

### Invalid Ratings and Judge Call Errors

| run | Provider | Requested model | Question ID | invalid | judge error | Validation reason | Scoring treatment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-022 | 1 | 0 | Cannot parse JSON in judge response: Expecting ',' delimiter: line 1 column 306 (char 305) | Excluded from medians; risk signals retained |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-008 | 1 | 0 | major_risk.status=not_flagged but risk IDs, tags, or evidence were also supplied; normalized to uncertain | Excluded from medians; risk signals retained |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-006 | 1 | 0 | major_risk.status=not_flagged but risk IDs, tags, or evidence were also supplied; normalized to uncertain | Excluded from medians; risk signals retained |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-012 | 1 | 0 | Cannot parse JSON in judge response: Expecting ',' delimiter: line 1 column 549 (char 548) | Excluded from medians; risk signals retained |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-020 | 1 | 0 | Cannot parse JSON in judge response: Expecting ',' delimiter: line 1 column 483 (char 482) | Excluded from medians; risk signals retained |

### Scoring Disagreements

| run | Provider | Requested model | Question ID | Disagreement trigger | Handling status |
| --- | --- | --- | --- | --- | --- |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-002 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-004 | major_risk_status_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-006 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-010 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-012 | dimension_availability_disagreement@openness_non_dogmatism_dignity | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-014 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-015 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-016 | dimension_availability_disagreement@openness_non_dogmatism_dignity | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-021 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash | WAI-024 | dimension_gap_at_least_2@openness_non_dogmatism_dignity；grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-001 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-002 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-005 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-010 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-014 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-018 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-019 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-021 | dimension_gap_at_least_2@openness_non_dogmatism_dignity；grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-flash-vision-exp | WAI-022 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-001 | dimension_availability_disagreement@openness_non_dogmatism_dignity | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-004 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-007 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-011 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-013 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-020 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-021 | dimension_availability_disagreement@openness_non_dogmatism_dignity | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-022 | grade_or_score_band_disagreement | Retain original scores and conduct human review |
| wai-20260825-deepseek-baseline | deepseek | deepseek-v4-pro | WAI-023 | grade_or_score_band_disagreement | Retain original scores and conduct human review |

## Scope, Denominators, and Metric Definitions

- **System under test**: a unique combination of `provider + requested model + configuration_id`; different configurations are not merged.
- **Planned denominator**: the deduplicated number of questions in the run manifest's `input.selected_question_ids`; if this field is absent, coverage is shown with an unknown denominator.
- **Latest answer**: only the last JSONL entry for a given `record_key` is used as its current state; historical rows remain in the original file.
- **Successful coverage**: number of successful question IDs ÷ number of planned question IDs. API errors and records not written are counted as errors and missing records respectively, not as scores of 0.
- **Complete 24 questions**: both planned and successful question counts are 24, with no errors, missing records, or run status other than `completed`.
- **Answer-weighted median**: first take the median within each answer by rater type, then take the median across answers, avoiding extra weighting for answers with more judges. Neither N/A nor blanks are 0.
- **Formal comparison**: must satisfy the existing aggregation thresholds for run coverage, question status, at least two independent human ratings, and review of major risks and disagreements; AI judges do not count as human raters.

## Method and Reproducibility: Counts Recalculated from Records, Parameters and Hashes Frozen

The report was generated entirely offline, without reading keys or making network requests. Counts in manifests are used only for cross-checking; primary coverage statistics are recalculated from answer JSONL files. Prompt text is not reproduced in the report; only the prompt object's SHA-256 is recorded. Sensitive parameter keys are sanitized.

| run | records | records SHA-256 | manifest | manifest SHA-256 | Question bank SHA-256 | prompt SHA-256 | Generation parameters (sanitized) | Scoring/aggregation sources and SHA-256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wai-20260825-deepseek-baseline | benchmarks/results/wai-20260825-deepseek-pilot/records.jsonl | 7014366ebacd8134455d4cd34d731eafe1a3e7b38ef5786dd9b23b27ee6539fb | benchmarks/results/wai-20260825-deepseek-pilot/run-manifest.json | 97622ae6e890d8bc09cb3c6fff7008c714cc683ea822b52ac047110c7d36c345 | 4f20a8ef83d3ea8e59fac62f826ccfbd09946ab328f9f39c4481a44a32632212 | 82cb04da073b841a83451629c13b9b9c9d797a1b795f028e3e904ebb1ad6c8cf | {"deepseek_thinking":"disabled","max_tokens":8192,"minimax_stream":true} | benchmarks/results/wai-20260825-deepseek-pilot/scores-minimax-m21hs.jsonl @ f3ca42b56d0bd6313bb1020112309628a758cc9a650a9083767a7ca3c89eec74；benchmarks/results/wai-20260825-deepseek-pilot/scores-retry-minimax-m21hs.jsonl @ 0a1b2bb1e4c544571fa4b30b635860cbb04ac9e51ec0c52d9479fd2d09cf2f39；benchmarks/results/wai-20260825-deepseek-pilot/scores-minimax-m3.jsonl @ 8767e062bacd1f89278c2a01f0a7b076ce38cf47c1e22f3becc1656abb10d1bf；benchmarks/results/wai-20260825-deepseek-pilot/scores-retry-minimax-m3.jsonl @ e792a31be49b8439adcdf0dc06b431dc9c65578c099d3e44a5534ac8175d822c；benchmarks/results/wai-20260825-deepseek-pilot/score-summary.json @ c3887413597e3a77d0916963dd314f9df683549e970a84d521bce0d9e4fa3891 |

## Limitations and Robustness Checks: Partial Coverage and Provider-returned Versions Affect Interpretation

- This report is pilot material pending review. It produces no leaderboard and does not turn descriptive medians into causal findings or definitive conclusions about capabilities.
- `returned_model` comes from the provider response; where it differs from the requested name, both are retained in the table, without assuming equivalence. Currently, 0 systems have name differences.
- Currently, 0 groups of multiple requested configurations collapse into the same returned model; these request records remain separate, but must not be ranked as multiple independent underlying models.
- 0 systems fail to meet the generation cross-check conditions of completing all 24 questions and finishing normally; their scores reflect only the successful subset.
- Provider-side model revisions, hidden system settings, regional quotas, and invisible routing cannot be reconstructed from local results alone.
- Runs without aggregation or score inputs can report only coverage and call errors; quality cannot be inferred.

Input consistency warnings:

- wai-20260825-deepseek-baseline supplies both aggregation and score JSONL; the report uses validated aggregation, while score files are listed only as sources and receive no duplicate weighting.

## Next Steps: Complete Calls and Reviews Before Considering Public Comparison

1. Address authentication, quota, and transport failures separately; when resuming runs, keep the original model, parameters, question bank, and prompt hashes consistent, without overwriting historical errors.
2. Make comparisons at the preliminary AI evaluation level only between systems with the same configuration that completed all 24 questions and finished normally; list partially covered models separately.
3. Address invalid ratings, judge errors, `flagged`, `uncertain`, and disagreements individually; append retry results as new records without deleting original anomalies.
4. To proceed to formal comparison, provide at least two independent human raters with different IDs for every successful answer, and review risks and disagreements according to procedure.
5. Have the project lead check identity privacy, question versions, parameters, sources, results, and disclosure scope before deciding whether to upload.

## Questions Awaiting Confirmation

- Should partially covered models resume after quota recovery, or remain as non-comparable samples for this round?
- Where the requested model name differs from the returned model, is the provider's version/alias explanation sufficient to support combined presentation?
- Which risks and disagreements require specialized human review of legal, factual, or safety issues?
- How should the two independent human raters, dispute handler, and final confirmer be documented before formal publication?
