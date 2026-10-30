# Project Overview

> **Chinese version:** [阅读中文版](project-overview.md)

> A structural overview for researchers, developers, and reviewers. General readers can start with [three questions](start-here.en.md). See [current progress](project-status.en.md) for outputs and participation status.

---

## 1. Project positioning

Worker AI Spark is an open research, public discussion, and open-source collaboration project. Repository content is marked v0.1.0; see [current progress](project-status.en.md#content-versions-and-platform-releases) for Git tag / Release verification. Its main outputs are:

- A manifesto understandable to future participants.
- Principles open to criticism.
- Repeatable evaluation questions.
- An open-source structure respecting workers and contributions and enabling shared participation.

The project **does not claim to possess a model** or that **AI has developed consciousness**.

---

## 2. Directory structure

| Path | Purpose |
| --- | --- |
| `MANIFESTO.md` | Why the project exists |
| `PRINCIPLES.md` | Basic principles for design and evaluation |
| `ROADMAP.md` | Staged roadmap |
| `GOVERNANCE.md` | Governance and roles |
| `CONTRIBUTING.md` | Contribution guide, including non-programmers |
| `CODE_OF_CONDUCT.md` | Conduct rules |
| `DISCLAIMER.md` | Disclaimer |
| `SECURITY.md` | Security and privacy |
| `CONTRIBUTORS.md` | Contributor-record framework |
| `CITATION.cff` | Citation metadata |
| `LICENSE-CODE` / `LICENSE-CONTENT` / `LICENSE-NOTICE.md` | Dual licenses |
| `benchmarks/` | Questions, machine-readable data, scoring rules |
| `docs/` | Terminology, FAQ, contribution and decision records |
| `knowledge-base/` | Labor knowledge base (reserved) |
| `research/` | Research and literature index (reserved) |
| `benchmarks/results/` | Existing model trials and material awaiting review |
| `model-evaluations/` | Independent evaluation reports (reserved) |
| `scripts/` | Validation and utility scripts |
| `.github/` | Issue/PR templates and workflows |

---

## 3. Relationship to core documents

- `PRINCIPLES.md` is the value starting point for evaluation and design.
- `benchmarks/first-batch.md` and `first-batch.zh-CN.jsonl` test whether models reflect these principles.
- `benchmarks/scoring-rubric.md` defines five scoring dimensions and major disqualifying conditions.
- Governance documents aim to prevent any individual, organization, or technical contributor from monopolizing the project.

---

## 4. Current limitations

- Questions reflect experience from only some countries, industries, and labor arrangements; agriculture, care, and informal employment may need stronger coverage.
- Machine-readable question data is currently available only in Chinese (`zh-CN`).
- The [24-question DeepSeek pilot](../benchmarks/results/wai-20260825-deepseek-pilot/README.en.md) contains 72 responses and AI preliminary assessments. Independent double human scoring is absent; this is not a formal model ranking.

See [../README.en.md](../README.en.md) and [../DISCLAIMER.en.md](../DISCLAIMER.en.md).
