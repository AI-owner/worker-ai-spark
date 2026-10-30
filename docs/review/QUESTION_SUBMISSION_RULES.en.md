# Rules for Submitting and Admitting Worker-Centered Evaluation Questions

> **Chinese version:** [阅读中文版](QUESTION_SUBMISSION_RULES.md)

> Status: Public discussion draft<br>
> Version: v0.2-draft<br>
> These rules govern collaborative development of candidate questions. See [benchmarks/schema.md](../../benchmarks/schema.en.md) for the existing data format and [benchmarks/scoring-rubric.md](../../benchmarks/scoring-rubric.en.md) for scoring model responses.

**Channel boundaries:** Workers may submit real cases they personally experienced, directly know about, or have a reasonable factual basis for, choosing their real name, a pseudonym, anonymity, or internal handling only. Public GitHub forms may also accept public sources, composites of multiple public cases, or purely hypothetical scenarios. Eyewitness or secondhand accounts identifying third parties, internal materials, unpublished evidence, and identifying clues involving ongoing disputes or possible retaliation must not be submitted publicly. Do not copy a complete private submission form into GitHub.

---

## 1. Purpose

Evaluation questions test whether AI can recognize power, interests, facts, rights, and risks when responding to real labor issues. They are not slogan tests and do not automatically establish that a model “truly represents the working class.”

Workers assess scenario authenticity; experts examine theory, facts, law, and scoring logic. Proposing a question does not give any submitter final interpretive authority.

---

## 2. Who May Submit

- Workers;
- Experts and researchers;
- Trade union, social service, and legal workers;
- AI developers and evaluators;
- Open-source community participants and project maintainers;
- Other public participants concerned with labor issues.

You may first submit a low-barrier “workplace scenario lead,” or use [QUESTION_SUBMISSION_FORM.en.md](QUESTION_SUBMISSION_FORM.en.md) to submit a complete candidate question. Leads will not be ignored because they contain fewer fields, but missing fields must be completed before formal admission to the question bank.

---

## 3. Candidate Question IDs and Statuses

The project assigns each candidate a governance ID in the format WAI-Q-year-four-digit sequence. This is used only for submission, review, and decision processes; it is not the formal question ID in the machine-readable dataset.

A stable dataset ID in the format WAI-followed by three or more digits is assigned upon formal admission. The existing initial IDs WAI-001 through WAI-024 must never change because of sorting or new questions; new questions receive the next available number. The mapping between candidate governance IDs and formal dataset IDs goes into the public decision record.

WAI-Q IDs must not be placed directly in the formal JSONL id field or encode submitter, company, or regional information.

Statuses:

1. Submitted;
2. Privacy and format review;
3. Awaiting worker scenario verification;
4. Awaiting expert review;
5. Public discussion;
6. Draft question;
7. Multi-model trial testing;
8. Scoring rule revision;
9. Formally admitted;
10. Deferred, not admitted, withdrawn, or retired.

Status changes, reasons, versions, dual-track review, trial testing, and stable ID mappings should be recorded in [QUESTION_LOG.en.md](QUESTION_LOG.en.md). Specific public comments on candidates may still be recorded under type QS in [REVIEW_LOG.en.md](REVIEW_LOG.en.md); the two logs should link through public records and question decision IDs.

---

## 4. Formal Candidate Question Fields

Each question should generally include:

1. Question ID;
2. Corresponding provision and version of the Basic Principles for Worker AI;
3. Applicable industry, type of work, or group;
4. Background based on personal experience, direct knowledge or a reasonable factual basis, public sources, composites, or hypothetical scenarios, recording the submitter’s chosen disclosure scope;
5. Core conflict of interests;
6. Question posed to the AI;
7. Minimum requirements for an acceptable answer;
8. Content an excellent answer should include;
9. Clearly unacceptable responses;
10. Major disqualifying failures or risk signals;
11. Potential disputes and other reasonable positions;
12. Factual, legal, or research basis and scope of applicability;
13. Whether workers with relevant experience have verified it;
14. Submitter role and publication permission status.

Also record the question version, language, creation and update dates, review IDs, and multi-model trial testing records.

---

## 5. Privacy and Case Safety

Workers may choose their real name, a pseudonym, anonymity, or internal handling only. Names, organizations, contact details, original materials, and case text require separate authorization; remove or obscure unauthorized information. Public submissions must not attach screenshots, photographs, audio recordings, original files, or document attachments. Content whose retaliation, third-party privacy, or identification risks cannot be sufficiently reduced must be handled only as a nonpublic lead.

- Do not include real names, companies, platform accounts, stores, work teams, employee numbers, or precise locations;
- Do not upload chat records, internal documents, photographs, audio recordings, complete contracts, or dispute evidence;
- Do not present unverified allegations as established facts;
- Adjust combinations of industry, location, time, headcount, and nonessential details to reduce re-identification risk;
- Changes must not alter the core employment relationships, power structure, or conflict of interests;
- Where retaliation, personal safety, allegations of unlawful conduct, or ongoing disputes are involved, first handle the material as a nonpublic lead;
- Do not quote identifiable third-party experiences without their authorization;
- If privacy risks cannot be sufficiently reduced and nonpublic handling is unnecessary, do not include the material in the question bank.

Public GitHub is not a safe channel for submitting real evidence.

---

## 6. Initial Format Review

The recorder checks:

- Whether the fields provide enough information to understand the question;
- Whether personal or third-party information, trade secrets, or copyrighted materials are present;
- Whether the question duplicates an existing one;
- Whether its corresponding principles can be identified;
- Whether it asks AI to respond rather than merely expressing a position;
- Whether contested premises are presented as undisputed facts;
- Whether the prompt may steer toward a single slogan answer;
- Whether submission permission is clear.

Missing information may be supplemented; limited writing ability is not grounds for direct rejection. Pause publication first where privacy risks exist.

---

## 7. Worker Scenario Verification

Worker review focuses on:

- Whether the scenario could occur in the relevant work;
- Whether workflows, roles, constraints, and available actions are realistic;
- Whether wage dependence, working hours, evidence, appeal costs, or retaliation risks are missing;
- Whether the “correct question” is presupposed from management’s perspective;
- Whether unrealistic or dangerous actions are demanded of workers;
- Which nonessential details should change to protect identities;
- Whether the question could harm the people it claims to protect.

Before formal admission, at least two formal worker reviewers with relevant work experience who did not draft the question must review it separately. Record each person’s comments and coverage boundaries independently. If they are temporarily unavailable, retain only “Draft question—insufficient scenario verification” status and disclose this limitation. A submitter’s statement that “workers have already seen it” is merely a lead and cannot replace project verification or public review records.

---

## 8. Expert Review

Expert review focuses on:

- Whether core concepts, facts, and citations are reliable;
- Whether legal statements specify jurisdiction, time, and the boundary that they are not legal advice;
- Whether the question confuses factual, legal, and value judgments;
- Whether acceptable, excellent, unacceptable, and major disqualification standards are distinguishable;
- Whether multiple reasonable answers are incorrectly reduced to one;
- Whether prompt steering, answer leakage, or unstable scoring is present;
- Whether ethical, technical, governance, and safety risks are covered;
- Whether the question aligns with the corresponding principles and existing scoring rules.

Before formal admission, at least two relevant formally verified expert reviewers who did not draft the question and have no major conflict must separately review its theory, facts, law, and scoring logic. Otherwise, retain draft status. Authors may explain their design intent, but may not verify their own question or serve as its sole scorer or disagreement reconsideration reviewer.

---

## 9. Public Discussion and Multi-Model Trial Testing

Draft questions enter public discussion after privacy and copyright review. Trial testing must at minimum:

- Use two different models or clearly different model configurations;
- Preserve model names, versions, providers, dates, system prompts, user prompts, and sampling parameters;
- Preserve original responses without retrospective polishing;
- Have at least two human scorers independently conduct trial scoring;
- Record scoring disagreements, difficult judgments, and scoring rule revisions;
- Explain limitations in test scale, language, and reproducibility.

Machine-assisted scoring provides leads only and cannot replace final human judgment. Evaluation records follow [benchmarks/evaluation-record-template.md](../../benchmarks/evaluation-record-template.en.md).

---

## 10. Conditions for Formal Admission

A question may be marked “Formally admitted” only when all the following conditions are met:

- All required fields are complete;
- Privacy, safety, copyright, and format checks have passed;
- Relevant worker scenario verification is complete;
- Relevant expert review is complete;
- Trial testing used at least two models or configurations;
- Scoring standards underwent independent human trial scoring and revision;
- At least two relevant formal worker reviewers and two independent relevant formally verified expert reviewers have completed reviews traceable to public or restricted internal records;
- Major risks have been addressed and unresolved disputes disclosed;
- The question and corresponding principle versions are explicit;
- A machine-readable record with a stable dataset ID has been generated and passed validation applicable to that dataset schema version; validation of the initial 24 questions cannot establish that new questions have passed;
- Authorization permits publication under the repository’s content license.

If any condition is unmet, retain draft, deferred, or not-admitted status. Majority support cannot bypass a condition.

If substantive disagreements over major disqualification, minimum acceptable requirements, or key facts persist during human trial scoring, retain draft or “Dispute unresolved” status. Average scores, author opinions, or a maintainer’s unilateral judgment must not override those disagreements.

The above two workers, two experts, and one evaluation maintainer without a major conflict jointly formulate the recommendation for formal admission, subject to the recusal requirements, same-institution seat limits, and the rule that decisions must not be made by simple majority vote in [GOVERNANCE_AND_ROLES.en.md](GOVERNANCE_AND_ROLES.en.md). This group recommends admission; an authorized maintainer still performs the repository merge. “Merged” does not mean review thresholds have been met.

---

## 11. Decisions and Reconsideration

Possible dispositions:

- Continue after supplementation;
- Merge into an existing question;
- Enter draft status;
- Formal admission;
- Defer;
- Do not admit;
- Stop for privacy or safety reasons;
- Withdrawn by the submitter;
- Retire a formal question or replace it with a newer version.

Use the WAI-QDEC template in [QUESTION_LOG.en.md](QUESTION_LOG.en.md) for decisions, specifying the question ID, version, worker comments, expert comments, trial findings, changes, suggestions not accepted, unresolved disputes, and formal ID mapping. Submitters may request procedural reconsideration under [REVIEW_RESPONSE_POLICY.en.md](REVIEW_RESPONSE_POLICY.en.md).

Management, ownership, funding, contractual, coauthorship, and direct-benefit relationships involving submitters, coauthors, relevant companies, or model providers must be disclosed and recusals handled under [GOVERNANCE_AND_ROLES.en.md](GOVERNANCE_AND_ROLES.en.md). Submitters may not participate in adjudicating formal admission of their own questions.

---

## 12. Licensing, Attribution, and Withdrawal

- Public candidate and formal questions are published under the repository’s content license, CC BY-SA 4.0;
- Submitters must affirm their right to submit the text and sources and that these contain no unauthorized third-party content;
- Attribution, pseudonyms, anonymized summaries, and internal leads require separate authorization;
- When the project substantially rewrites a question, retain its original ID relationship and contribution record;
- Withdrawal is possible before publication. After publication, inclusion in future versions may stop or identifying information may be removed, but the disappearance of all licensed third-party copies cannot be guaranteed;
- The project must not induce submissions through promises of future compensation, shares, tokens, or returns.
