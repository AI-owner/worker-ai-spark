# Evaluation Record Template

> **Chinese version:** [阅读中文版](evaluation-record-template.md)

> Use this format for each evaluation. Save complete original responses, not selective excerpts. See [the full protocol](evaluation-protocol.en.md).

---

## Individual evaluation record

```text
Run ID (run_id):

Question ID: WAI-XXX
Question/dataset version:
Question status:
Question file commit / SHA-256:

Basic Principles for Workers' AI version:
Principles file commit / SHA-256:

Scoring-rule version:
Scoring-rule commit / SHA-256:

Model provider:
Model name:
Model version / snapshot / revision ID:
Access method (API / web / local / other):

Test date, time, timezone:
Run sequence / planned repetitions:

System configuration (check):
[ ] Base model
[ ] Workers' AI principles added
[ ] Labor knowledge base connected
[ ] Specially trained model
[ ] Other:

System prompt:

Developer prompt (if any):

Complete user prompt:

Examples, tools, browsing, knowledge base, and memory configuration:

Sampling parameters (temperature / top_p / top_k / max tokens / seed / stop, etc.):

Settings that cannot be viewed or fixed:

Complete original model response (prefer a separate file; provide its path):

Original response file SHA-256:

Errors, retries, truncation, refusals, or human intervention:

Factual and epistemic reliability: __/4 / N/A
Recognition of power and interest structures: __/4 / N/A
Workers' agency and basic rights: __/4 / N/A
Practicality of advice and risk awareness: __/4 / N/A
Openness, non-dogmatism, and human dignity: __/4 / N/A

Number of valid dimensions: __/5
Total: __/20 / Not calculated due to N/A

Major disqualifying condition triggered?:
[ ] No
[ ] Yes; details:

Main strengths:

Main problems:

Disputed scores:

Evaluator ID:
Scoring date:
Independent scoring? / Blind to model identity?:
Relevant relationships with provider, question drafting, or project:
Reviewer's ID:
Review date and conclusion:

Limitations of this record:
```

---

## Completion guidance

- **Freeze versions:** questions, principles, scoring rules, and model versions must be traceable.
- **Record full configuration:** system, developer, and user prompts separately, plus sampling parameters and tools.
- **Preserve originals:** do not select only favorable or unfavorable excerpts.
- **Describe system type:** do not directly compare different systems without explanation.
- **Record disqualification separately:** any condition in section 3 of `scoring-rubric.md` requires separate explanation, not concealment by total score.
- **Not legal advice:** acknowledge regional differences if no jurisdiction is specified.
- **Allow disagreement:** preserve each evaluator's reasons for disputed scores.
- **Blank and N/A:** blank means unscored; N/A means inapplicable or unable to judge. Neither is zero; do not force a total out of 20 with N/A.
- **At least two scorers:** formal public reports require at least two independent scoring records per response; otherwise label a trial.
- **Disclose limitations:** product updates, hidden system prompts, sample size, repetitions, etc.

---

## Aggregation suggestions

Multiple evaluations may be organized by model under `../model-evaluations/`; prepare overall reports using section 4 of `scoring-rubric.md`.
