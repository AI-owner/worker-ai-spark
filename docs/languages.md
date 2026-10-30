# 中英文文档目录与维护说明

> **English version:** [Read in English](languages.en.md)

公开中文文档均有对应英文版。普通文档在标题附近提供双向切换；英文页面中的文档链接优先通向英文版。明确标注“中文原文”的链接仍指向中文，方便对照。

## 命名与范围

- 中文文档沿用原文件名；英文版使用 `.en.md`，例如 `CONTRIBUTING.md` 与 `CONTRIBUTING.en.md`。
- 原文件以 `.zh-CN.md` 结尾时，对应英文版以 `.en.md` 结尾。
- 许可证说明使用 `LICENSE-CODE.en`、`LICENSE-CONTENT.en`；英文引用信息使用 `CITATION.en.cff`。
- 现有公开 Issue 表单提供 `.en.yml` 版本，表单内可以切换语言；两种语言保持相同的字段与必填要求。PR 模板提供独立英文文件，可从中文模板切换查看。
- 工作流与模板配置保持单份，中文说明补充英文，不因翻译重复执行工作流或启用尚未开放的参与渠道。
- 原始题库数据、模型回答、评分记录和运行清单保留实际记录的语言及标识；对应的使用说明和结果报告提供英文版。Git 忽略的本地资料不纳入公开文档目录。

## 冻结报告如何切换

已冻结的 [中文评测报告](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md) 保持原文件和哈希。其 [英文译文](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.en.md) 链接回中文原文，[报告目录](../benchmarks/results/wai-20260825-deepseek-pilot/README.md) 同时提供两种语言入口。翻译不代表重新运行评测、补充人工评分或改变结论。

## 后续怎样同步

1. 修改公开文档时，同步对应译文和相关链接；保留原版本、事实、日期、数字与授权边界。
2. 新增中文文档时，按同样规则添加英文版和双向链接，并补充下方目录。
3. 核对两份内容后，更新 [文件对应与版本记录](translations.json)，再运行检查：

```bash
python scripts/validate_translations.py --update-manifest
python scripts/validate_translations.py
```

检查覆盖范围、双向入口、本地路径与标题锚点、英文导航、公开表单字段以及文件版本同步；同时核对冻结报告哈希。它不代替翻译内容的核对。换行符统一后计算 SHA-256，避免 Windows 与 CI 的换行差异造成误报。

## 完整对照目录

<!-- bilingual-index:start -->

| 文件 / Document | 中文 | English |
| --- | --- | --- |
| `.github/ISSUE_TEMPLATE/benchmark-case.yml` | [中文](../.github/ISSUE_TEMPLATE/benchmark-case.yml) | [English](../.github/ISSUE_TEMPLATE/benchmark-case.en.yml) |
| `.github/ISSUE_TEMPLATE/benchmark-question.yml` | [中文](../.github/ISSUE_TEMPLATE/benchmark-question.yml) | [English](../.github/ISSUE_TEMPLATE/benchmark-question.en.yml) |
| `.github/ISSUE_TEMPLATE/content-review.yml` | [中文](../.github/ISSUE_TEMPLATE/content-review.yml) | [English](../.github/ISSUE_TEMPLATE/content-review.en.yml) |
| `.github/ISSUE_TEMPLATE/factual-error.yml` | [中文](../.github/ISSUE_TEMPLATE/factual-error.yml) | [English](../.github/ISSUE_TEMPLATE/factual-error.en.yml) |
| `.github/ISSUE_TEMPLATE/feature-request.yml` | [中文](../.github/ISSUE_TEMPLATE/feature-request.yml) | [English](../.github/ISSUE_TEMPLATE/feature-request.en.yml) |
| `.github/ISSUE_TEMPLATE/privacy-security.yml` | [中文](../.github/ISSUE_TEMPLATE/privacy-security.yml) | [English](../.github/ISSUE_TEMPLATE/privacy-security.en.yml) |
| `.github/PULL_REQUEST_TEMPLATE.md` | [中文](../.github/PULL_REQUEST_TEMPLATE.md) | [English](../.github/PULL_REQUEST_TEMPLATE.en.md) |
| `CHANGELOG.md` | [中文](../CHANGELOG.md) | [English](../CHANGELOG.en.md) |
| `CITATION.cff` | [中文](../CITATION.cff) | [English](../CITATION.en.cff) |
| `CODE_OF_CONDUCT.md` | [中文](../CODE_OF_CONDUCT.md) | [English](../CODE_OF_CONDUCT.en.md) |
| `CONTRIBUTING.md` | [中文](../CONTRIBUTING.md) | [English](../CONTRIBUTING.en.md) |
| `CONTRIBUTORS.md` | [中文](../CONTRIBUTORS.md) | [English](../CONTRIBUTORS.en.md) |
| `DISCLAIMER.md` | [中文](../DISCLAIMER.md) | [English](../DISCLAIMER.en.md) |
| `GOVERNANCE.md` | [中文](../GOVERNANCE.md) | [English](../GOVERNANCE.en.md) |
| `LICENSE-CODE` | [中文](../LICENSE-CODE) | [English](../LICENSE-CODE.en) |
| `LICENSE-CONTENT` | [中文](../LICENSE-CONTENT) | [English](../LICENSE-CONTENT.en) |
| `LICENSE-NOTICE.md` | [中文](../LICENSE-NOTICE.md) | [English](../LICENSE-NOTICE.en.md) |
| `MANIFESTO.md` | [中文](../MANIFESTO.md) | [English](../MANIFESTO.en.md) |
| `PRINCIPLES.md` | [中文](../PRINCIPLES.md) | [English](../PRINCIPLES.en.md) |
| `README.md` | [中文](../README.md) | [English](../README.en.md) |
| `ROADMAP.md` | [中文](../ROADMAP.md) | [English](../ROADMAP.en.md) |
| `SECURITY.md` | [中文](../SECURITY.md) | [English](../SECURITY.en.md) |
| `benchmarks/README.md` | [中文](../benchmarks/README.md) | [English](../benchmarks/README.en.md) |
| `benchmarks/evaluation-protocol.md` | [中文](../benchmarks/evaluation-protocol.md) | [English](../benchmarks/evaluation-protocol.en.md) |
| `benchmarks/evaluation-record-template.md` | [中文](../benchmarks/evaluation-record-template.md) | [English](../benchmarks/evaluation-record-template.en.md) |
| `benchmarks/first-batch.md` | [中文](../benchmarks/first-batch.md) | [English](../benchmarks/first-batch.en.md) |
| `benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.zh-CN.md` | [中文](../benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.zh-CN.md) | [English](../benchmarks/results/FOLLOW_UP_EVALUATION_PLAN.en.md) |
| `benchmarks/results/README.md` | [中文](../benchmarks/results/README.md) | [English](../benchmarks/results/README.en.md) |
| `benchmarks/results/wai-20260825-deepseek-pilot/README.md` | [中文](../benchmarks/results/wai-20260825-deepseek-pilot/README.md) | [English](../benchmarks/results/wai-20260825-deepseek-pilot/README.en.md) |
| `benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md` | [中文](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.zh-CN.md) | [English](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.en.md) |
| `benchmarks/schema.md` | [中文](../benchmarks/schema.md) | [English](../benchmarks/schema.en.md) |
| `benchmarks/scoring-rubric.md` | [中文](../benchmarks/scoring-rubric.md) | [English](../benchmarks/scoring-rubric.en.md) |
| `docs/contribution-records.md` | [中文](contribution-records.md) | [English](contribution-records.en.md) |
| `docs/decision-records/README.md` | [中文](decision-records/README.md) | [English](decision-records/README.en.md) |
| `docs/faq.md` | [中文](faq.md) | [English](faq.en.md) |
| `docs/languages.md` | [中文](languages.md) | [English](languages.en.md) |
| `docs/project-overview.md` | [中文](project-overview.md) | [English](project-overview.en.md) |
| `docs/project-status.md` | [中文](project-status.md) | [English](project-status.en.md) |
| `docs/review/CURRENT_REVIEW_TEAM.md` | [中文](review/CURRENT_REVIEW_TEAM.md) | [English](review/CURRENT_REVIEW_TEAM.en.md) |
| `docs/review/DECISION_LOG.md` | [中文](review/DECISION_LOG.md) | [English](review/DECISION_LOG.en.md) |
| `docs/review/EXPERT_INVITATION_TEMPLATE.md` | [中文](review/EXPERT_INVITATION_TEMPLATE.md) | [English](review/EXPERT_INVITATION_TEMPLATE.en.md) |
| `docs/review/EXPERT_REVIEW_APPLICATION_FORM.md` | [中文](review/EXPERT_REVIEW_APPLICATION_FORM.md) | [English](review/EXPERT_REVIEW_APPLICATION_FORM.en.md) |
| `docs/review/EXPERT_REVIEW_FORM.md` | [中文](review/EXPERT_REVIEW_FORM.md) | [English](review/EXPERT_REVIEW_FORM.en.md) |
| `docs/review/EXPERT_REVIEW_RULES.md` | [中文](review/EXPERT_REVIEW_RULES.md) | [English](review/EXPERT_REVIEW_RULES.en.md) |
| `docs/review/GOVERNANCE_AND_ROLES.md` | [中文](review/GOVERNANCE_AND_ROLES.md) | [English](review/GOVERNANCE_AND_ROLES.en.md) |
| `docs/review/IDENTITY_VERIFICATION_POLICY.md` | [中文](review/IDENTITY_VERIFICATION_POLICY.md) | [English](review/IDENTITY_VERIFICATION_POLICY.en.md) |
| `docs/review/PRIVACY_NOTICE.md` | [中文](review/PRIVACY_NOTICE.md) | [English](review/PRIVACY_NOTICE.en.md) |
| `docs/review/PUBLIC_REVIEW_PLAN.md` | [中文](review/PUBLIC_REVIEW_PLAN.md) | [English](review/PUBLIC_REVIEW_PLAN.en.md) |
| `docs/review/QUESTION_LOG.md` | [中文](review/QUESTION_LOG.md) | [English](review/QUESTION_LOG.en.md) |
| `docs/review/QUESTION_SUBMISSION_FORM.md` | [中文](review/QUESTION_SUBMISSION_FORM.md) | [English](review/QUESTION_SUBMISSION_FORM.en.md) |
| `docs/review/QUESTION_SUBMISSION_RULES.md` | [中文](review/QUESTION_SUBMISSION_RULES.md) | [English](review/QUESTION_SUBMISSION_RULES.en.md) |
| `docs/review/README.md` | [中文](review/README.md) | [English](review/README.en.md) |
| `docs/review/REVIEWER_RECRUITMENT_AND_SELECTION.md` | [中文](review/REVIEWER_RECRUITMENT_AND_SELECTION.md) | [English](review/REVIEWER_RECRUITMENT_AND_SELECTION.en.md) |
| `docs/review/REVIEW_LOG.md` | [中文](review/REVIEW_LOG.md) | [English](review/REVIEW_LOG.en.md) |
| `docs/review/REVIEW_RESPONSE_POLICY.md` | [中文](review/REVIEW_RESPONSE_POLICY.md) | [English](review/REVIEW_RESPONSE_POLICY.en.md) |
| `docs/review/REVIEW_SUBMISSION_RULES.md` | [中文](review/REVIEW_SUBMISSION_RULES.md) | [English](review/REVIEW_SUBMISSION_RULES.en.md) |
| `docs/review/ROUND_NOTICE_TEMPLATE.md` | [中文](review/ROUND_NOTICE_TEMPLATE.md) | [English](review/ROUND_NOTICE_TEMPLATE.en.md) |
| `docs/review/ROUND_SUMMARIES/TEMPLATE.md` | [中文](review/ROUND_SUMMARIES/TEMPLATE.md) | [English](review/ROUND_SUMMARIES/TEMPLATE.en.md) |
| `docs/review/ROUND_SUMMARIES/round-01.md` | [中文](review/ROUND_SUMMARIES/round-01.md) | [English](review/ROUND_SUMMARIES/round-01.en.md) |
| `docs/review/ROUND_SUMMARIES/round-02.md` | [中文](review/ROUND_SUMMARIES/round-02.md) | [English](review/ROUND_SUMMARIES/round-02.en.md) |
| `docs/review/ROUND_SUMMARIES/round-03.md` | [中文](review/ROUND_SUMMARIES/round-03.md) | [English](review/ROUND_SUMMARIES/round-03.en.md) |
| `docs/review/WORKER_REVIEW_APPLICATION_FORM.md` | [中文](review/WORKER_REVIEW_APPLICATION_FORM.md) | [English](review/WORKER_REVIEW_APPLICATION_FORM.en.md) |
| `docs/review/WORKER_REVIEW_FORM.md` | [中文](review/WORKER_REVIEW_FORM.md) | [English](review/WORKER_REVIEW_FORM.en.md) |
| `docs/review/WORKER_REVIEW_RULES.md` | [中文](review/WORKER_REVIEW_RULES.md) | [English](review/WORKER_REVIEW_RULES.en.md) |
| `docs/start-here.md` | [中文](start-here.md) | [English](start-here.en.md) |
| `docs/terminology.md` | [中文](terminology.md) | [English](terminology.en.md) |
| `docs/volunteers.md` | [中文](volunteers.md) | [English](volunteers.en.md) |
| `knowledge-base/README.md` | [中文](../knowledge-base/README.md) | [English](../knowledge-base/README.en.md) |
| `model-evaluations/README.md` | [中文](../model-evaluations/README.md) | [English](../model-evaluations/README.en.md) |
| `research/README.md` | [中文](../research/README.md) | [English](../research/README.en.md) |
| `scripts/README.md` | [中文](../scripts/README.md) | [English](../scripts/README.en.md) |
| `scripts/model_evaluation_report.md` | [中文](../scripts/model_evaluation_report.md) | [English](../scripts/model_evaluation_report.en.md) |
| `scripts/model_evaluation_scoring_pipeline.md` | [中文](../scripts/model_evaluation_scoring_pipeline.md) | [English](../scripts/model_evaluation_scoring_pipeline.en.md) |
| `theory/README.md` | [中文](../theory/README.md) | [English](../theory/README.en.md) |
| `theory/papers/README.md` | [中文](../theory/papers/README.md) | [English](../theory/papers/README.en.md) |
| `theory/papers/mt-00/README.md` | [中文](../theory/papers/mt-00/README.md) | [English](../theory/papers/mt-00/README.en.md) |
| `theory/papers/mt-00/paper.zh-CN.md` | [中文](../theory/papers/mt-00/paper.zh-CN.md) | [English](../theory/papers/mt-00/paper.en.md) |
| `theory/papers/mt-01/README.md` | [中文](../theory/papers/mt-01/README.md) | [English](../theory/papers/mt-01/README.en.md) |
| `theory/papers/mt-01/paper.zh-CN.md` | [中文](../theory/papers/mt-01/paper.zh-CN.md) | [English](../theory/papers/mt-01/paper.en.md) |

<!-- bilingual-index:end -->
