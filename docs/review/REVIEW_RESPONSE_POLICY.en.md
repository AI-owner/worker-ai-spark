# Review Feedback and Response Policy

> **Chinese version:** [阅读中文版](REVIEW_RESPONSE_POLICY.md)

> Status: Public discussion draft<br>
> Version: v0.2-draft<br>
> This policy governs how feedback is registered, assessed, answered, published, and reconsidered. It does not promise lengthy individual replies to every ordinary public comment.

---

## 1. Record Two Sets of Statuses Separately

The original work plan combined procedural progress and substantive decisions in its statuses. To avoid confusion, the public register uses two fields.

### 1.1 Process Status

| Status | Meaning |
| --- | --- |
| Received | An identifier has been generated; initial screening is not yet complete |
| Privacy hold | Possible personal information, safety, or retaliation risks have been identified; publication is on hold |
| Awaiting additional information | The version, clause, reasoning, or necessary verification information is missing |
| Valid formal review | The content is valid and formal identity verification is complete |
| Ordinary public feedback | The content is valid, but formal verification was not requested or completed |
| Unverified non-public feedback | The content is valid but formal verification is incomplete, and the participant has not authorized item-by-item publication |
| Under consideration | Verification, comparison, or preparation of a decision is underway |
| Deferred | Depends on other research, personnel, versions, or safety conditions |
| Withdrawn | The participant has withdrawn the submission under the rules |
| Duplicate merged | Merged with an existing record from the same participant or source |
| Invalid | Meets the narrowly defined invalidity conditions in the submission rules |
| Closed | A response for the current version has been issued |

### 1.2 Disposition

| Disposition | Meaning |
| --- | --- |
| Accepted | The main recommendation has been incorporated into an identified version |
| Partially accepted | Only some content has been accepted, with the limits explained |
| Scheduled for the next version | The issue is recognized in principle but will not be addressed in the current version |
| Additional material required | A substantive judgment cannot be completed; awaiting material |
| Focused research required | Additional factual, legal, technical, or work-context research is required |
| Dispute unresolved | Reasonable views conflict; no consensus is fabricated |
| Action deferred | There is an explicit reason for deferral and conditions for rechecking |
| Not accepted | Assessment is complete, but the proposed change is not agreed to |
| Outside project scope | The issue falls outside the project or the current round |
| Unable to verify | Key facts cannot currently be reasonably verified |
| Invalid submission | Meets invalidity conditions and does not proceed to substantive assessment |

Process statuses and dispositions may be combined, such as “Closed + Partially accepted” or “Deferred + Focused research required.” “Scheduled for the next version” must specify a target version or recheck date and cannot become indefinite shelving.

“Further discussion required” in the original work plan maps uniformly to “Dispute unresolved.” Where factual, legal, technical, or work-context material is missing, use “Focused research required” or “Additional material required” to avoid multiple statistical categories for the same meaning.

### 1.3 Maturity / Evidence Status

Record maturity separately from the disposition of an individual comment. Available statuses include: Maintainer draft; Procedural pilot review; Insufficient evidence; Dual-track review completed—dispute unresolved; Dual-track review completed—further revision possible; Stable for use (still subject to reassessment). “Merged,” “Majority support,” and “Several reviews received” are not maturity statuses.

“Dual-track review completed” denotes procedural completion: from the second round onward, the headcount, recusal, and recordkeeping thresholds in [GOVERNANCE_AND_ROLES.en.md](GOVERNANCE_AND_ROLES.en.md) must be met, but this does not indicate that participants agree with the conclusion. “Dual-track review completed—further revision possible” means that four reviewers have completed their review of the frozen earlier draft, but have not yet rechecked and confirmed the new text produced in response to their feedback. “Stable for use” is a higher evidence status: beyond completing the dual-track process, the four independent reviewers across the tracks must recheck the final diff, commit, and SHA-256 of the version proposed to take effect. None may leave an unanswered objection concerning facts, basic rights, safety, serious harm, or a key aspect of applicability, and both tracks must confirm that the main objections have been addressed accurately. If such substantive objections remain, the only permissible status is “Dual-track review completed—dispute unresolved.”

---

## 2. Initial Screening

After receipt, check in order:

1. Whether there are privacy, safety, retaliation, or third-party risks;
2. Whether the version and clause under review can be identified;
3. Whether the submission is within the current round's scope;
4. Whether it is a duplicate, supplement, or copy submitted through multiple channels;
5. Whether the views and reasons are sufficiently understandable;
6. Whether applicants for formal status have completed the necessary verification;
7. Whether publication and licensing choices are clear.

Privacy screening precedes content assessment. Agreement with a viewpoint must not affect verification or validity judgments.

---

## 3. Grounds for Decisions

Decisions do not use a simple majority vote. Those handling submissions should consider together:

- Verifiable facts and source quality;
- The applicability of legal, research, and technical judgments;
- Real work experience and the limits of its generalizability;
- Effects on workers' rights, lives, and agency;
- Differences across industries, regions, and forms of employment;
- Particular risks to minority groups;
- The possibility of infrequent but severe harm;
- Consistency and conflict with other principles;
- Whether requirements can be made actionable, explainable, and evaluable;
- Whether powerful actors could turn them against their intended purpose;
- New risks introduced by the changes themselves.

Decision-makers must explain why. “The majority agrees,” “Experts believe,” or “Workers support this” alone is insufficient.

---

## 4. Dual-Track Handling

- Expert and worker feedback use separate tracks, dimensions, and statistics;
- Scores from the two groups are not added into a total, and expert status confers no fixed weighting;
- The decision record for each major change should summarize each track separately;
- A person with both identities counts in only one track for the same principle in the same round, according to their declared primary role. Their other perspective may supplement the narrative but does not increase the other track's headcount;
- Where experts broadly approve but workers consistently identify difficulty understanding, distortion, or potential misuse, a clause must not be labeled stable solely on expert approval;
- Where workers raise a major issue without specialist analysis, the status should be “Focused research required,” and participation from the relevant field should be invited.

Structured scoring only identifies dimensions needing review; it does not automatically determine acceptance, rejection, or maturity. A blank means “unanswered”; N/A means “not applicable or unable to judge.” Neither may be treated as zero. Each track separately publishes valid score counts, blank counts, N/A counts, raw distributions, and medians by clause and dimension. Where samples are very small or disagreement is substantial, do not use means or precise rankings to manufacture a settled conclusion, and do not combine scores across tracks.

---

## 5. Major-Risk Hold

Once any of the following risks is raised specifically, mark the relevant clause “Major risk pending verification.” It must not be described as stable before verification:

- Identity exposure, workplace retaliation, or disclosure of personal information;
- Risks to life, workplace safety, occupational health, or serious physical injury;
- Discrimination, coercion, humiliation, or erosion of basic rights;
- Fabricated law or facts, or high-risk advice;
- Depriving workers of choice and agency in the name of protecting them;
- Clear potential for managers, platforms, or projects to use the clause to expand control.

Within 2–3 working days of receiving a specific risk report, the coordinator should complete preliminary triage: determine whether to restrict publication, suspend the relevant clause, or activate the safety incident process, and notify the submitter if contactable. Initial screening determines interim measures only; it does not establish that a risk is absent.

A risk flag is not an automatic permanent veto. Lifting the hold requires all of the following: at least one formally verified worker with relevant work experience and one relevant formally verified expert must each complete verification; neither may have participated in drafting the original clause, the original decision, or the initial screening of this risk, and neither may have a material conflict of interest; the facts of the risk and affected groups must have been addressed; necessary textual, procedural, or safety measures must have been implemented; remaining uncertainty, recurrence triggers, and responsible persons must be recorded; and both verifiers must confirm in writing, for the same version proposed to take effect, that the release conditions have been met. If either verifier believes the risk remains unaddressed, or any condition is unmet, retain “Major risk pending verification” or “Dispute unresolved.” Scheduling, vote counts, or a maintainer's unilateral judgment cannot lift the hold.

---

## 6. Contents of Formal Feedback

In principle, every contactable formal expert or worker reviewer receives:

- A private random receipt identifier and target version;
- An accurate project summary of the feedback;
- Process status and disposition;
- Accepted portions and corresponding change locations;
- Main reasons for non-acceptance, deferral, or inability to verify;
- Facts and sources used, authorized public-record sub-item identifiers, or internal evidence summaries that cannot be traced back to an identity;
- Connections or conflicts between expert and worker feedback;
- Conflicts of interest, recusals, and procedural limitations;
- Remaining disputes and arrangements for subsequent rounds;
- The deadline and method for requesting reconsideration.

Where one form covers several clauses, feedback must provide process status, disposition, and change location separately for sub-items I01, I02, and so on. A single overall status must not conceal that some clauses were accepted while others were not accepted or deferred.

If a summary could alter the original meaning, first ask the submitter to confirm it. Internal identity information and other participants' non-public feedback must not appear in the reply.

---

## 7. Service Timeframes

| Stage | Normal target |
| --- | --- |
| Receipt acknowledgment | 3 working days |
| Preliminary major-risk triage and interim measures | 2–3 working days |
| Initial privacy, scope, and completeness screening | 7 working days |
| Deadline for additional information | 10 calendar days after notification |
| Consideration exceeds 15 working days | Send at least one progress update |
| Formal individual feedback | Within 30 working days after the round closes |
| Round summary | Within 15 working days after individual feedback is completed |
| Reconsideration request | Within 10 working days after the decision is delivered or published |
| Reconsideration response | Within 20 working days after receipt of a complete request |

These are service targets for a volunteer project, not false guarantees. If capacity is insufficient, pause new intake or publish the reason for delay, new dates, and the number of outstanding submissions. The project must not remain “open” while leaving submissions unanswered for prolonged periods.

Privacy breaches, personal safety concerns, and retaliation risks do not wait for ordinary scheduling: restrict access and initiate incident response first.

---

## 8. Ordinary Public, Non-Public, and Unattributed Feedback

The project does not promise a lengthy individual reply to every ordinary public comment, but must:

- Assign reasonable labels or statuses to public Issues and Discussions;
- Reflect major issues, representative objections, and counts in round summaries;
- Create decision records for feedback leading to substantive changes;
- Not exclude anonymous feedback because its author cannot be contacted;
- Not count unverified feedback—whether non-public or unattributed in the published text—toward formally verified headcounts;
- Not infer or publicly speculate about anonymous authors' identities from writing style.

---

## 9. Reconsideration

Any submitter holding a private receipt identifier, or participant able to provide a public contribution link, may request one procedural reconsideration on the following grounds. Formal identity verification is not a prerequisite:

- Published rules were not followed;
- Feedback was misquoted, omitted key content, or assigned to the wrong version;
- A decision relies on an obvious factual error;
- A material conflict of interest was not disclosed;
- Important new evidence could change the assessment;
- An invalidity, duplication, or identity-verification finding is clearly mistaken;
- Privacy, safety, or retaliation risks have arisen.

Simple disagreement with a conclusion may be submitted as new feedback in the next round but does not necessarily trigger procedural reconsideration. Requests to correct factual errors, misquotation, version assignment, invalidity findings, conflicts of interest, privacy, or safety issues must not be rejected because a participant has a lower status. Requests to reassess the substance of a principle are handled as substantive reconsideration.

Reconsideration steps:

1. Submit the random receipt identifier, original decision, and reasons through a non-public channel; public contributors may provide a public link. Where a round offers assisted or oral participation, assisted reconsideration applications must also be accepted, with the applicant confirming the record;
2. The recorder checks completeness;
3. Someone who did not participate in the original decision, verification, or invalidity finding conducts reconsideration. Substantive judgments about principles require written perspectives from both one independent formally verified worker and one independent relevant formally verified expert. Neither may have participated in drafting the original clause, its original substantive review, or the original decision, and neither may have a material conflict of interest. If either independent perspective cannot be obtained, keep the matter deferred and disclose the limitation;
4. Outcomes are to uphold, correct, reassess, return for further handling, or implement privacy measures;
5. Publish anonymized outcomes and corrections to the original record; do not silently overwrite history.

Where no independent reconsideration reviewer is available, disclose the limitation and defer, rather than having anyone involved in the original handling pretend to provide independent reconsideration. Requests for access to, correction of, or deletion of personal information, and safety requests, are not subject to the 10-working-day reconsideration deadline.

---

## 10. Publication and Version Changes

Substantive changes to core principles should use Pull Requests or equivalent traceable version differences. Record each change in [DECISION_LOG.en.md](DECISION_LOG.en.md):

- What changed and why;
- The feedback identifiers and evidence supporting it;
- Feedback not accepted and the reasons;
- Recusals and reconsideration;
- Remaining disputes;
- The version taking effect.

Published counts must use mutually exclusive primary categories: formally verified experts, formally verified workers, unverified public feedback, and unverified non-public feedback. Report withdrawals, duplicates, and invalid submissions separately. Named, pseudonymous, unattributed in the published text, and internal-only handling are publication attributes of the primary categories and must not be added again to participant totals. Report non-public feedback only in aggregates that cannot be traced back to identities. If combinations of small counts could identify people, combine categories or withhold breakdowns.

---

## 11. Corrections

When an error is found in handling records:

- Preserve the original record and append the correction date;
- Explain the error, who identified it, and its effect on the decision;
- Notify affected participants again where necessary;
- Recalculate public statistics while keeping older versions traceable;
- Do not conceal procedural errors by deleting history.
