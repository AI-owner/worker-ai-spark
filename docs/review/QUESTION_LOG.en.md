# Candidate Evaluation Question Lifecycle Register

> **Chinese version:** [阅读中文版](QUESTION_LOG.md)

> Status: Template established; no candidate question records under this mechanism yet<br>
> Register version: v0.2-draft<br>
> Last updated: 2026-07-31

This register records the public lifecycle of WAI-Q candidate questions, from submission, review, and pilot testing through formal inclusion, deferral, or retirement. It does not record private receipts, identity mappings, original firsthand accounts, third-party information, or unauthorized text.

[REVIEW_LOG.en.md](REVIEW_LOG.en.md) records “how a particular expert, worker, or public comment was handled”; this file records “which stage a candidate question has reached.” Public comments on candidate questions may use the QS type in the former. Question status changes must be recorded separately here, with cross-links through public record or decision numbers.

---

## I. Candidate Question Index

There are currently no candidate question records.

| Candidate number | Public title | Current version | Corresponding principles and version | Safe source type | Current question-bank status | Worker review | Expert review | Multi-model pilot testing | Formal stable ID | Decision number | Updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — | — | — | — | — | — | — |

Field rules:

- **Candidate number**: WAI-Q-year-four-digit sequence number, assigned by the project; contains no submitter, affiliation, or regional information;
- **Safe source type**: Firsthand experience / direct knowledge or reasonable factual grounds / secondhand account / adapted from public materials / synthesis of multiple public cases / hypothetical scenario / internal lead only. Publish only as authorized by the submitter; do not disclose unauthorized identities or identifying details;
- **Current question-bank status**: Submitted / privacy and format review / awaiting worker scenario verification / awaiting expert review / public discussion / draft question / multi-model pilot testing / scoring-rule revision / formally included / deferred / not included / withdrawn / retired;
- **Worker review**: `reviewed (n≥2)` / `insufficient (n=...)`; count only relevant formally verified worker reviewers who did not participate in drafting;
- **Expert review**: `reviewed (n≥2)` / `insufficient (n=...)`; count only relevant formally verified expert reviewers who did not participate in drafting and have no major conflicts;
- **Multi-model pilot testing**: Link a public run_id or state “not started/insufficient”; do not present plans as results;
- **Formal stable ID**: Enter WAI-numeric identifier only after formal inclusion; WAI-Q must not be entered directly as the `id` in formal JSONL;
- **Decision number**: Use WAI-QDEC from Section III of this file and link relevant public comments, Pull Requests, or commits.

---

## II. Status History Template

Copy one section per candidate question. Append new rows for status changes; do not overwrite old rows.

### WAI-Q-YYYY-NNNN: Public Title

| Field | Content |
| --- | --- |
| Current question version | draft-01 |
| Corresponding principles and version / commit |  |
| Public candidate text | Public link; enter “none” if no safe public copy exists |
| Safe source type |  |
| Submission license | CC-BY-SA-4.0 / internal lead only / awaiting confirmation |
| Public submission date |  |
| Current question-bank status |  |
| Current restrictions |  |

| Date | From status | To status | Version | Reasons and changes | Public comment/decision number | Responsible role |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Review and pilot testing:

| Stage | Completion status | Valid participant/run count | Disagreements, coverage gaps, and next requirement | Publicly disclosable record |
| --- | --- | ---: | --- | --- |
| Privacy, safety, copyright, and format checks |  | Not applicable |  |  |
| Scenario verification by relevant workers |  |  |  |  |
| Expert and scoring-logic review |  |  |  |  |
| Public discussion |  |  |  |  |
| Multi-model pilot testing |  |  |  | run_id |
| Independent human scoring and disagreement reconsideration |  |  |  |  |

Do not enter participant names, private seat mappings, WAI-SUB, nonpublic service links, original evidence, or identifiable cases in this section.

---

## III. Candidate Question Decision Template

### WAI-QDEC-YYYY-NNNN

| Field | Content |
| --- | --- |
| Candidate question and version |  |
| Decision date |  |
| Decision outcome | Supplement / merge / advance to draft / formally include / defer / do not include / stop for privacy or safety / withdraw / retire / superseded by a new version |
| Review by two workers | Met / insufficient; count and safe records |
| Review by two independent experts | Met / insufficient; count and safe records |
| Evaluation maintainer seat | Safe display name and recusals |
| Same-institution and conflict-of-interest checks |  |
| Multi-model pilot testing and run_id |  |
| Human scoring disagreements |  |
| Unresolved major risks |  |
| Comments not adopted and unresolved disputes |  |
| Formal stable ID | Complete only upon formal inclusion |
| Corresponding PR / commit |  |

Reasons for the decision, before-and-after changes, and applicability boundaries:

> 

Question drafters must not verify their own questions or participate in adjudicating formal inclusion. A decision must not be described as “formally included” if any formal requirement concerning reviewer counts, disagreements, recusals, pilot testing, or licensing is unmet.

---

## IV. Privacy, Withdrawal, and Publication Boundaries

- Before nonpublic leads become safe public candidate questions, report only aggregate counts that cannot enable re-identification; do not create public records containing their text;
- Publication permission does not remove the need to check re-identification, third-party, copyright, and retaliation risks;
- When an unpublished candidate question is withdrawn, do not publish its original text. Handle already-public content within licensing, privacy, and platform-copying limits;
- Once published, formal IDs do not change with ordering. Preserve mappings and reasons when retiring or replacing questions; do not silently reuse IDs;
- Correct register errors by appending the correction date and an explanation of the impact; do not overwrite history.

---

## V. Per-Round Reporting Definitions

For each round, separately report counts of newly submitted candidate questions, privacy suspensions, questions advanced to draft, completed worker verifications, completed expert reviews, completed pilot tests, formal inclusions, and deferrals/non-inclusions/withdrawals/retirements, together with source, industry, and principle coverage and scoring disagreements. Keep participant and question counts separate. Do not subdivide small nonpublic samples in ways that enable re-identification.
