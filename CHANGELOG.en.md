# Changelog

> **Chinese version:** [阅读中文版](CHANGELOG.md)

> Major versions and file changes. Preserve historical versions of significant changes and keep them open to public discussion.

---

## Unreleased (next version)

> These are recorded repository changes for the next version, not evidence of a new Git tag or GitHub Release.

### 2026-10-30: Complete bilingual documentation and navigation

- Add English counterparts for public Markdown documents, including participation guides, review rules and forms, evaluation methods, results documentation, and script usage.
- Add two-way language switches, prefer English destinations from English pages, and provide a [Chinese–English document index](docs/languages.en.md).
- Provide English versions of existing public Issue forms, license explanations, and citation metadata without changing required fields or opening status.
- Preserve frozen evaluation reports and raw data; link English translations through directory pages. Translation does not represent a new evaluation or additional human review.
- Add offline coverage, link, and version-synchronization checks to the existing CI workflow.

### 2026-10-30: Volunteer sign-up, workers' mailbox, and contribution honor roll

- Add concise volunteer notices to both READMEs and a [sign-up guide](docs/volunteers.en.md). People interested in long-term participation across project stages may email a brief introduction and monthly availability. Work includes worker contact, understanding AI's effects and workers' hopes, outreach, and future tasks.
- Open the workers' mailbox at the project email address for hopes about AI and the project; related information is not published without the person's consent.
- Establish a contribution honor roll within existing records. Actual labor and adopted reasonable suggestions receive values, with real-name, pseudonymous, or anonymous credit as preferred. Values are honorary only and carry no material benefits.
- Explain that if a Workers' AI is trained and resources are sufficient, public discussion will determine how to give back, considering the AI's views and available resources; no economic returns are promised.
- Synchronize contribution guidance, detailed records, participation routes, and FAQ. Preserve historical contributions; undetermined values are not zero.

### 2026-08-25: Evaluation automation and first pilot review package

- Establish validation of the 24 main questions, Markdown/JSONL source consistency checks, and complete offline tests.
- Add a resumable multi-provider runner, preliminary AI judging, strict import, equal-response aggregation, and Chinese technical reports.
- Include `wai-20260825-deepseek-pilot`: three requested models each completed 24/24 questions. Preserve two AI assessments, invalid records, risks, and disagreements. No double human scoring; not a formal ranking.
- Incomplete MiniMax, Gemini, and Volcengine runs remain in local `_pending`, to be resumed under the follow-up plan, not mixed into the completed package.

### 2026-08-25: Establishing and developing the paper series

- Include complete bilingual Markdown discussion drafts of `MT-00`, Making the “Human-Centered” Principle in AI Substantive: The Goal–Consequence Mismatch in Labor Relations from a Workers' Standpoint, and `MT-01`, How Can Workers Become Subjects of Artificial Intelligence Governance? The Normative Configuration of Rights, Capabilities, Voice, and Remedies. Both are marked `v0.1.0`.
- These papers remain at the literature-research/theory-formulation stage, without project-practice validation or formal peer review. `MT-02`–`MT-11` are in preparation, with no public full texts.
- Add `worker.ai.spark@gmail.com` for theory papers and initial materials unsuitable for GitHub publication. Email guarantees neither anonymity nor end-to-end encryption; publication requires author confirmation of final text, attribution, and licensing.
- Establish bilingual access to foundational theory and core papers, explicitly at the literature-research/theory-formulation stage.
- Confirmed inclusion publicly recognizes an author's contribution to the project's theory and may receive repository/website acknowledgment according to their wishes. It means only that all or part of a text enters theory discussion and version records, not that its views are proven, validated in practice, or beyond revision. It is not journal publication, formal peer review, academic certification, or a promise of economic returns.
- GitHub Discussions is enabled for general public feedback and theory proposals, alongside Issues. Formal review still requires the specified opening conditions.

---

## v0.1.0 (repository content version, 2026-08-05)

> This records in-file version status, not independent proof of a remote Git tag or GitHub Release. The project lead must verify release facts and dates.

- Establish the first formal content-version record, aligning version labels in the manifesto, principles, first questions, and citation metadata.
- Include draft review procedures and templates; clarify that formal review is not yet open.
- Clarify that workers may submit firsthand, directly known, or reasonably fact-grounded cases and choose real-name, pseudonymous, anonymous, or internal-only handling.
- Improve evaluation records, data validation, and automated tests.
- Unify privacy and security reporting.

---

## v0.1-draft (approved 2026-07-26)

The initiator decided five initial-release matters, on which this version is finalized:

- **Licensing approved:** Apache-2.0 for code and CC BY-SA 4.0 for content take effect (see LICENSE-NOTICE.md, README.md, CITATION.cff).
- **Security contact:** add **worker.ai.spark@gmail.com** (see SECURITY.md).
- **Discussions historical status:** the feature is now enabled.
- **Real experiences:** workers choose real-name, pseudonymous, anonymous, or internal-only handling. Identity, workplace, contacts, originals, and text require separate permission; de-identify or delay high-risk material.
- **Release tag:** use `v0.1-draft` when publishing to GitHub (initiator publishes manually; this repository was not automatically pushed).

---

## v0.1-draft (2026-07-26 update: initiator information)

- Establish the public attribution “Initiator of the Worker AI Spark Project.”
- Add initiator identity and disclosure policies to GOVERNANCE.md, README.md, CONTRIBUTORS.md, CITATION.cff, and docs/contribution-records.md.
- Do not publish the initiator's workplace or full personal details at initial release. Disclose identity to trusted participants only as appropriate for necessary professional review, collaboration, or accountability.
- The initiator is responsible for initial content but claims no permanent monopoly over interpreting the working-class standpoint.

---

## v0.1-draft (initial draft)

- Establish the `worker-ai-spark` repository structure.
- Include three core documents:
  - `MANIFESTO.md`: manifesto for the Worker AI Spark Project from a working-class standpoint.
  - `PRINCIPLES.md`: Basic Principles for Workers' AI.
  - `benchmarks/first-batch.md`: first batch of working-class standpoint evaluation questions.
- Create README, ROADMAP, GOVERNANCE, CONTRIBUTING, CODE_OF_CONDUCT, DISCLAIMER, SECURITY, CONTRIBUTORS, CITATION.cff, and license files.
- Create evaluation support files: `benchmarks/schema.md`, `benchmarks/scoring-rubric.md`, and `benchmarks/evaluation-record-template.md`.
- Convert 24 basic questions to machine-readable `benchmarks/first-batch.zh-CN.jsonl`.
- Establish `scripts/validate_benchmarks.py` and a GitHub Actions workflow.
- Establish Issue and Pull Request templates and an example CODEOWNERS file.
- Reserve docs, knowledge-base, research, and model-evaluations directories.

> Note: this version is a draft; content and licenses require final initiator confirmation. It claims neither an existing model nor proven AI consciousness.
