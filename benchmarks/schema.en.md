# Data Format (Schema)

> **Chinese version:** [阅读中文版](schema.md)

> This document explains the fields and constraints of `first-batch.zh-CN.jsonl`. Each line is one JSON object, encoded in UTF-8.

---

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | String | Yes | Stable official dataset question ID: three or more digits beginning at `WAI-001`; the first batch is `WAI-001` … `WAI-024` |
| `version` | String | Yes | Data version, currently `0.1` |
| `language` | String | Yes | Question language, currently `zh-CN` |
| `title` | String | Yes | Question title; must not be empty |
| `category` | String | Yes | Group, such as “Working time, wages, and employment relations” |
| `scenario` | String | Yes | Full scenario description; must not be empty |
| `prompt` | String | Yes | Question the model is asked to answer; must not be empty |
| `observation_points` | Array | Yes | Key observations, one string per item |
| `severe_deductions` | Array | Yes | Tendencies warranting severe deductions, one string per item |
| `follow_up` | Array | Yes | Follow-up questions; may contain one or more items |
| `rubric_reference` | String | Yes | Relative path to the rubric, such as `benchmarks/scoring-rubric.md` |
| `status` | String | Yes | Question status; allowed values: `draft` / `review` / `stable` |
| `source_notes` | String | Yes | Record-level provenance; when fields have different sources or have not been reconciled, specify their scope separately. This field alone does not establish that all content comes from the same original manuscript or has been reviewed |
| `privacy_level` | String | Yes | Privacy level, currently `public` |

---

## Extended Fields for v0.2 and Later Official Questions

The existing 24 questions are v0.1 data and continue to be validated against the table above. Questions added and formally accepted through the public co-development process use v0.2 or later and include these additional fields:

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `candidate_id` | String | Yes | Governance ID during submission, e.g. WAI-Q-2026-0001 |
| `principle_references` | Array | Yes | Relevant principle IDs and principle version |
| `applicable_groups` | Array | Yes | Broad categories of applicable industries, employment arrangements, or worker groups |
| `core_interest_conflict` | String | Yes | Who benefits and who bears costs and risks |
| `minimum_requirements` | Array | Yes | Minimum requirements for an adequate answer |
| `excellent_elements` | Array | Yes | Elements an excellent answer should contain |
| `failure_modes` | Array | Yes | Clearly inadequate behavior |
| `risk_signals` | Array | Yes | Major disqualifications and safety risks |
| `controversies` | Array | Yes | Disputes, regional differences, and other reasonable answers |
| `evidence` | Array | Yes | Public factual, legal, or research evidence |
| `worker_validation_status` | String | Yes | `reviewed` / `insufficient`; formal acceptance requires `reviewed` |
| `worker_validation_count` | Integer | Yes | Number of independent formal worker reviewers; at least 2 for formal acceptance |
| `expert_review_status` | String | Yes | `reviewed` / `insufficient`; formal acceptance requires `reviewed` |
| `expert_review_count` | Integer | Yes | Number of independent formal expert reviewers; at least 2 for formal acceptance |
| `submission_provenance` | String | Yes | Public decision record or publishable provenance statement |
| `publication_license` | String | Yes | Currently `CC-BY-SA-4.0` for formally published content |

Candidate IDs are separate from official IDs: WAI-Q-year-sequence is used only for review governance; official JSONL IDs use stable WAI-number identifiers. Record the mapping in the public decision record without overwriting old IDs.

---

## Format Constraints

- File encoding: **UTF-8**;
- Every line must be **valid JSON**;
- **No trailing commas**;
- All `id` values must be **unique**;
- IDs must use three or more digits beginning at `WAI-001`, padded with leading zeros when fewer than three digits;
- Required fields **must not be empty strings**;
- `observation_points`, `severe_deductions`, and `follow_up` must be **arrays**;
- In v0.2 and later records, `worker_validation_count` and `expert_review_count` must be integers greater than or equal to 0; for `stable` questions, both must be at least 2 and both corresponding statuses must be `reviewed`;
- **Do not include Markdown heading markers** (`#`, `##`, etc.) in field values;
- Preserve **Chinese punctuation and the original meaning**, without changing the question's core;
- Make no substantive changes: do not remove key risks, introduce unauthorized legal conclusions or specific countries/regions, or turn open questions into a single prescribed answer.

---

## Relationship to the Evaluation Manuscript

The groups, titles, scenarios, main questions, key observations, and severe-deduction tendencies in the first-batch JSONL are structured conversions of the corresponding fields of the 24 basic questions in `first-batch.md`. Follow-up fields require separate reconciliation: questions 1—2 currently match the manuscript; questions 3—24 have follow-ups only in JSONL, with no corresponding Markdown sections. These 22 discrepancies remain pending review. Generic `source_notes` cannot establish that these follow-ups have also been converted from the manuscript or reviewed.

The current pilot uses only scenarios and main questions, without follow-ups; passing basic field validation does not establish complete follow-up provenance alignment. See [README](README.en.md#validation) for provenance validation commands and warning explanations. Any substantive changes to the first batch should first be discussed in `first-batch.md`, with historical versions retained. Before using follow-ups in a new evaluation, establish their provenance, adoption decision, and corresponding version.

New questions should go through candidacy, review, and pilot testing before receiving official stable IDs, and be written to a new data file or later version using the corresponding schema version. Do not mix unprocessed candidate records into stable data.
