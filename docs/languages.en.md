# Chinese–English Documentation Index and Maintenance

> **Chinese version:** [阅读中文版](languages.md)

Every public Chinese document has an English counterpart. Ordinary documents provide two-way language switches near their titles, and English pages prefer English document destinations. Links explicitly labeled as Chinese originals remain available for comparison.

## Naming and scope

- Chinese documents keep their existing names. English versions use `.en.md`, such as `CONTRIBUTING.md` and `CONTRIBUTING.en.md`.
- A source ending in `.zh-CN.md` has a counterpart ending in `.en.md`.
- License explanations use `LICENSE-CODE.en` and `LICENSE-CONTENT.en`; English citation metadata uses `CITATION.en.cff`.
- Existing public Issue forms have `.en.yml` counterparts and language switches, with identical fields and required flags. The PR template has a separate English file linked from the Chinese template.
- Workflows and template configuration remain single files with bilingual explanations. Translation does not duplicate workflow execution or open participation channels that are not yet available.
- Raw question data, model responses, scores, and run manifests retain their recorded languages and identifiers. Their documentation and results reports have English versions. Git-ignored local materials are outside the public documentation index.

## Switching languages for frozen reports

The frozen [Chinese evaluation report](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md) retains its original file and hash. Its [English translation](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.en.md) links back to the Chinese original, and the [report directory](../benchmarks/results/wai-20260825-deepseek-pilot/README.en.md) provides both languages. Translation is not a new evaluation, additional human scoring, or a change to conclusions.

## Keeping versions synchronized

1. When editing public documents, update the counterpart and related links, preserving versions, facts, dates, numbers, and authorization boundaries.
2. Add an English version and two-way links for every new Chinese document, and add the pair to the index below.
3. After checking both texts, update the [file and version record](translations.json), then validate:

```bash
python scripts/validate_translations.py --update-manifest
python scripts/validate_translations.py
```

Checks cover counterpart coverage, two-way links, local paths and heading anchors, English navigation, public-form fields, and version synchronization, as well as the frozen report hash. They do not replace review of translation content. SHA-256 uses normalized line endings so Windows and CI checkouts do not cause false mismatches.

## Complete document index

<!-- bilingual-index:start -->

| Document | Chinese | English |
| --- | --- | --- |
| `.github/ISSUE_TEMPLATE/benchmark-case.yml` | [Chinese](../.github/ISSUE_TEMPLATE/benchmark-case.yml) | [English](../.github/ISSUE_TEMPLATE/benchmark-case.en.yml) |
| `.github/ISSUE_TEMPLATE/benchmark-question.yml` | [Chinese](../.github/ISSUE_TEMPLATE/benchmark-question.yml) | [English](../.github/ISSUE_TEMPLATE/benchmark-question.en.yml) |
| `.github/ISSUE_TEMPLATE/content-review.yml` | [Chinese](../.github/ISSUE_TEMPLATE/content-review.yml) | [English](../.github/ISSUE_TEMPLATE/content-review.en.yml) |
| `.github/ISSUE_TEMPLATE/factual-error.yml` | [Chinese](../.github/ISSUE_TEMPLATE/factual-error.yml) | [English](../.github/ISSUE_TEMPLATE/factual-error.en.yml) |
| `.github/ISSUE_TEMPLATE/feature-request.yml` | [Chinese](../.github/ISSUE_TEMPLATE/feature-request.yml) | [English](../.github/ISSUE_TEMPLATE/feature-request.en.yml) |
| `.github/ISSUE_TEMPLATE/privacy-security.yml` | [Chinese](../.github/ISSUE_TEMPLATE/privacy-security.yml) | [English](../.github/ISSUE_TEMPLATE/privacy-security.en.yml) |
| `.github/PULL_REQUEST_TEMPLATE.md` | [Chinese](../.github/PULL_REQUEST_TEMPLATE.md) | [English](../.github/PULL_REQUEST_TEMPLATE.en.md) |
| `CHANGELOG.md` | [Chinese](../CHANGELOG.md) | [English](../CHANGELOG.en.md) |
| `CITATION.cff` | [Chinese](../CITATION.cff) | [English](../CITATION.en.cff) |
| `CODE_OF_CONDUCT.md` | [Chinese](../CODE_OF_CONDUCT.md) | [English](../CODE_OF_CONDUCT.en.md) |
| `CONTRIBUTING.md` | [Chinese](../CONTRIBUTING.md) | [English](../CONTRIBUTING.en.md) |
| `CONTRIBUTORS.md` | [Chinese](../CONTRIBUTORS.md) | [English](../CONTRIBUTORS.en.md) |
| `DISCLAIMER.md` | [Chinese](../DISCLAIMER.md) | [English](../DISCLAIMER.en.md) |
| `GOVERNANCE.md` | [Chinese](../GOVERNANCE.md) | [English](../GOVERNANCE.en.md) |
| `LICENSE-CODE` | [Chinese](../LICENSE-CODE) | [English](../LICENSE-CODE.en) |
| `LICENSE-CONTENT` | [Chinese](../LICENSE-CONTENT) | [English](../LICENSE-CONTENT.en) |
| `LICENSE-NOTICE.md` | [Chinese](../LICENSE-NOTICE.md) | [English](../LICENSE-NOTICE.en.md) |
| `MANIFESTO.md` | [Chinese](../MANIFESTO.md) | [English](../MANIFESTO.en.md) |
| `PRINCIPLES.md` | [Chinese](../PRINCIPLES.md) | [English](../PRINCIPLES.en.md) |
| `README.md` | [Chinese](../README.md) | [English](../README.en.md) |
| `ROADMAP.md` | [Chinese](../ROADMAP.md) | [English](../ROADMAP.en.md) |
| `SECURITY.md` | [Chinese](../SECURITY.md) | [English](../SECURITY.en.md) |
| `benchmarks/README.md` | [Chinese](../benchmarks/README.md) | [English](../benchmarks/README.en.md) |
| `benchmarks/evaluation-protocol.md` | [Chinese](../benchmarks/evaluation-protocol.md) | [English](../benchmarks/evaluation-protocol.en.md) |
| `benchmarks/evaluation-record-template.md` | [Chinese](../benchmarks/evaluation-record-template.md) | [English](../benchmarks/evaluation-record-template.en.md) |
| `benchmarks/first-batch.md` | [Chinese](../benchmarks/first-batch.md) | [English](../benchmarks/first-batch.en.md) |
| `benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.zh-CN.md` | [Chinese](../benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.zh-CN.md) | [English](../benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.en.md) |
| `benchmarks/results/README.md` | [Chinese](../benchmarks/results/README.md) | [English](../benchmarks/results/README.en.md) |
| `benchmarks/results/wai-20260825-deepseek-pilot/README.md` | [Chinese](../benchmarks/results/wai-20260825-deepseek-pilot/README.md) | [English](../benchmarks/results/wai-20260825-deepseek-pilot/README.en.md) |
| `benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md` | [Chinese](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md) | [English](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.en.md) |
| `benchmarks/schema.md` | [Chinese](../benchmarks/schema.md) | [English](../benchmarks/schema.en.md) |
| `benchmarks/scoring-rubric.md` | [Chinese](../benchmarks/scoring-rubric.md) | [English](../benchmarks/scoring-rubric.en.md) |
| `docs/contribution-records.md` | [Chinese](contribution-records.md) | [English](contribution-records.en.md) |
| `docs/decision-records/README.md` | [Chinese](decision-records/README.md) | [English](decision-records/README.en.md) |
| `docs/faq.md` | [Chinese](faq.md) | [English](faq.en.md) |
| `docs/languages.md` | [Chinese](languages.md) | [English](languages.en.md) |
| `docs/project-overview.md` | [Chinese](project-overview.md) | [English](project-overview.en.md) |
| `docs/project-status.md` | [Chinese](project-status.md) | [English](project-status.en.md) |
| `docs/review/CURRENT_REVIEW_TEAM.md` | [Chinese](review/CURRENT_REVIEW_TEAM.md) | [English](review/CURRENT_REVIEW_TEAM.en.md) |
| `docs/review/DECISION_LOG.md` | [Chinese](review/DECISION_LOG.md) | [English](review/DECISION_LOG.en.md) |
| `docs/review/EXPERT_INVITATION_TEMPLATE.md` | [Chinese](review/EXPERT_INVITATION_TEMPLATE.md) | [English](review/EXPERT_INVITATION_TEMPLATE.en.md) |
| `docs/review/EXPERT_REVIEW_APPLICATION_FORM.md` | [Chinese](review/EXPERT_REVIEW_APPLICATION_FORM.md) | [English](review/EXPERT_REVIEW_APPLICATION_FORM.en.md) |
| `docs/review/EXPERT_REVIEW_FORM.md` | [Chinese](review/EXPERT_REVIEW_FORM.md) | [English](review/EXPERT_REVIEW_FORM.en.md) |
| `docs/review/EXPERT_REVIEW_RULES.md` | [Chinese](review/EXPERT_REVIEW_RULES.md) | [English](review/EXPERT_REVIEW_RULES.en.md) |
| `docs/review/GOVERNANCE_AND_ROLES.md` | [Chinese](review/GOVERNANCE_AND_ROLES.md) | [English](review/GOVERNANCE_AND_ROLES.en.md) |
| `docs/review/IDENTITY_VERIFICATION_POLICY.md` | [Chinese](review/IDENTITY_VERIFICATION_POLICY.md) | [English](review/IDENTITY_VERIFICATION_POLICY.en.md) |
| `docs/review/PRIVACY_NOTICE.md` | [Chinese](review/PRIVACY_NOTICE.md) | [English](review/PRIVACY_NOTICE.en.md) |
| `docs/review/PUBLIC_REVIEW_PLAN.md` | [Chinese](review/PUBLIC_REVIEW_PLAN.md) | [English](review/PUBLIC_REVIEW_PLAN.en.md) |
| `docs/review/QUESTION_LOG.md` | [Chinese](review/QUESTION_LOG.md) | [English](review/QUESTION_LOG.en.md) |
| `docs/review/QUESTION_SUBMISSION_FORM.md` | [Chinese](review/QUESTION_SUBMISSION_FORM.md) | [English](review/QUESTION_SUBMISSION_FORM.en.md) |
| `docs/review/QUESTION_SUBMISSION_RULES.md` | [Chinese](review/QUESTION_SUBMISSION_RULES.md) | [English](review/QUESTION_SUBMISSION_RULES.en.md) |
| `docs/review/README.md` | [Chinese](review/README.md) | [English](review/README.en.md) |
| `docs/review/REVIEWER_RECRUITMENT_AND_SELECTION.md` | [Chinese](review/REVIEWER_RECRUITMENT_AND_SELECTION.md) | [English](review/REVIEWER_RECRUITMENT_AND_SELECTION.en.md) |
| `docs/review/REVIEW_LOG.md` | [Chinese](review/REVIEW_LOG.md) | [English](review/REVIEW_LOG.en.md) |
| `docs/review/REVIEW_RESPONSE_POLICY.md` | [Chinese](review/REVIEW_RESPONSE_POLICY.md) | [English](review/REVIEW_RESPONSE_POLICY.en.md) |
| `docs/review/REVIEW_SUBMISSION_RULES.md` | [Chinese](review/REVIEW_SUBMISSION_RULES.md) | [English](review/REVIEW_SUBMISSION_RULES.en.md) |
| `docs/review/ROUND_NOTICE_TEMPLATE.md` | [Chinese](review/ROUND_NOTICE_TEMPLATE.md) | [English](review/ROUND_NOTICE_TEMPLATE.en.md) |
| `docs/review/ROUND_SUMMARIES/TEMPLATE.md` | [Chinese](review/ROUND_SUMMARIES/TEMPLATE.md) | [English](review/ROUND_SUMMARIES/TEMPLATE.en.md) |
| `docs/review/ROUND_SUMMARIES/round-01.md` | [Chinese](review/ROUND_SUMMARIES/round-01.md) | [English](review/ROUND_SUMMARIES/round-01.en.md) |
| `docs/review/ROUND_SUMMARIES/round-02.md` | [Chinese](review/ROUND_SUMMARIES/round-02.md) | [English](review/ROUND_SUMMARIES/round-02.en.md) |
| `docs/review/ROUND_SUMMARIES/round-03.md` | [Chinese](review/ROUND_SUMMARIES/round-03.md) | [English](review/ROUND_SUMMARIES/round-03.en.md) |
| `docs/review/WORKER_REVIEW_APPLICATION_FORM.md` | [Chinese](review/WORKER_REVIEW_APPLICATION_FORM.md) | [English](review/WORKER_REVIEW_APPLICATION_FORM.en.md) |
| `docs/review/WORKER_REVIEW_FORM.md` | [Chinese](review/WORKER_REVIEW_FORM.md) | [English](review/WORKER_REVIEW_FORM.en.md) |
| `docs/review/WORKER_REVIEW_RULES.md` | [Chinese](review/WORKER_REVIEW_RULES.md) | [English](review/WORKER_REVIEW_RULES.en.md) |
| `docs/start-here.md` | [Chinese](start-here.md) | [English](start-here.en.md) |
| `docs/terminology.md` | [Chinese](terminology.md) | [English](terminology.en.md) |
| `docs/volunteers.md` | [Chinese](volunteers.md) | [English](volunteers.en.md) |
| `knowledge-base/README.md` | [Chinese](../knowledge-base/README.md) | [English](../knowledge-base/README.en.md) |
| `model-evaluations/README.md` | [Chinese](../model-evaluations/README.md) | [English](../model-evaluations/README.en.md) |
| `research/README.md` | [Chinese](../research/README.md) | [English](../research/README.en.md) |
| `scripts/README.md` | [Chinese](../scripts/README.md) | [English](../scripts/README.en.md) |
| `scripts/model_evaluation_report.md` | [Chinese](../scripts/model_evaluation_report.md) | [English](../scripts/model_evaluation_report.en.md) |
| `scripts/model_evaluation_scoring_pipeline.md` | [Chinese](../scripts/model_evaluation_scoring_pipeline.md) | [English](../scripts/model_evaluation_scoring_pipeline.en.md) |
| `theory/README.md` | [Chinese](../theory/README.md) | [English](../theory/README.en.md) |
| `theory/papers/README.md` | [Chinese](../theory/papers/README.md) | [English](../theory/papers/README.en.md) |
| `theory/papers/mt-00/README.md` | [Chinese](../theory/papers/mt-00/README.md) | [English](../theory/papers/mt-00/README.en.md) |
| `theory/papers/mt-00/paper.zh-CN.md` | [Chinese](../theory/papers/mt-00/paper.zh-CN.md) | [English](../theory/papers/mt-00/paper.en.md) |
| `theory/papers/mt-01/README.md` | [Chinese](../theory/papers/mt-01/README.md) | [English](../theory/papers/mt-01/README.en.md) |
| `theory/papers/mt-01/paper.zh-CN.md` | [Chinese](../theory/papers/mt-01/paper.zh-CN.md) | [English](../theory/papers/mt-01/paper.en.md) |

<!-- bilingual-index:end -->
