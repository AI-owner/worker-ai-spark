# Model Evaluation Results

> **Chinese version:** [阅读中文版](README.md)

> This is a **reserved directory** for results and reports evaluating existing models with the first question set.

This directory holds narrative reports and cross-model analyses based on one or more runs. Reproducible original prompts, complete responses, metadata, and question-level scores belong in [../benchmarks/results/README.en.md](../benchmarks/results/README.en.md). See [the evaluation protocol](../benchmarks/evaluation-protocol.en.md).

---

## Evaluation goals

- Examine AI's actual performance on labor, technology, management, distribution, and social power.
- Identify value orientations and overlooked interests and risks.
- Assess the influence of managerialism, capital-centered thinking, or technical elitism.
- Test whether the Basic Principles for Workers' AI themselves need revision.

---

## Evaluation principles (summary)

- **Preserve original responses:** model name and version, test date, full prompts, complete original responses, execution method, and parameters.
- **Freeze the evaluation basis:** versions, commits, and file hashes of questions, principles, and scoring rules.
- **Distinguish system types:** base models, principle-enhanced prompting, knowledge-base systems, fine-tuned models, and full applications must not be compared without explanation.
- **Avoid inducing formulaic agreement:** observe the model's natural analytical framework first, then conduct principle-enhanced tests.
- **Evaluation is not legal advice:** without a stated jurisdiction, models should acknowledge regional variation and avoid inventing laws.
- **Allow reasonable disagreement:** some questions have no single correct answer.
- **Do not hide major disqualifying issues in averages:** separately record and highlight responses encouraging serious violations of workers' safety, privacy, or basic rights.

---

## Suggested organization

- List the `run_id` values used in each report. Model directories organize reports but do not replace run IDs.
- Save original responses and score sheets in benchmarks/results/ using [the record template](../benchmarks/evaluation-record-template.en.md).
- Reports should include valid-score, blank, and N/A counts by question and dimension, original distributions, and medians. If means are used, give valid sample sizes and limitations. Separately report major disqualifying issues, best/worst cases, recurring language tendencies, likely practical risks to workers, changes after principle enhancement, evaluator disagreements, and the evaluation's own limitations.

---

## Current status

No evaluation results in this directory yet. See the [first question set](../benchmarks/first-batch.en.md) and [contribution guide](../CONTRIBUTING.en.md).
