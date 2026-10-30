# Review Governance, Roles, and Recusal Rules

> **Chinese version:** [阅读中文版](GOVERNANCE_AND_ROLES.md)

> Status: Public discussion draft<br>
> Version: v0.2-draft<br>
> This document supplements [../../GOVERNANCE.en.md](../../GOVERNANCE.en.md); it does not invent a committee that already exists.

---

## I. Current Governance Facts

Under the existing governance documents, during the founding stage the project initiator bears primary responsibility for maintenance and final review of core documents. Public review does not automatically change GitHub repository permissions or turn invitees into project committee members.

Before each round, the people actually filling the following roles, or their public designations, must be announced. If roles are not all filled, overlapping responsibilities and limitations on independence must be disclosed. Expressions such as “committee decision” or “collectively approved” must not be used contrary to the facts.

---

## II. Roles and Authority

| Role | Main responsibilities | Prohibited actions |
| --- | --- | --- |
| Person responsible for final decisions | Make reasoned decisions to revise principles, defer action, or decline proposals; normally the initiator initially | Concealing conflicts of interest, deleting reasonable dissent, or independently declaring their own draft to have passed independent review |
| Round coordinator | Publish announcements, manage timing, coordinate separate review tracks and summaries | Changing the reviewed version or publication authorization without authorization |
| Submission recorder | Generate private random receipt identifiers; create separate public record identifiers after authorization; maintain ledgers and receipts | Entering private identifiers or identity mappings in public ledgers |
| Identity verifier | Examine minimal verification information and record results | Judging whether opinions are correct or disseminating original materials |
| Privacy lead | Manage access, deletion, rights requests, and incident response | Using materials for publicity, profiling, or recruitment |
| Expert-comment organizer | Organize comments, evidence, and conflicts by professional dimensions | Judging real working conditions on workers’ behalf |
| Worker-comment organizer | Organize comments on comprehensibility, realistic scenarios, and impacts | Presenting individual experiences as collective opinions |
| Revision implementer | Amend documents according to decisions and record differences | Independently changing core positions beyond public decisions |
| Reconsideration reviewer | Check procedure, omitted evidence, and conflicts of interest | Solely reconsidering a decision they originally handled |

One person may coordinate, record, and implement revisions, but identity-verification information should be separated from substantive comment processing wherever possible. Where there is only one maintainer, round summaries must explicitly disclose the limitation that “independent reconsideration cannot be provided”; matters involving major conflicts of interest must be deferred until a temporary independent reviewer is found.

If the person responsible for final decisions drafted the clause under review, their merge authority remains governed by [../../GOVERNANCE.en.md](../../GOVERNANCE.en.md), but the decision may only be labeled a “maintainer draft decision.” In the first round, claiming “dual-track process pilot review completed” additionally requires at least one formal worker reviewer and one relevant formal expert reviewer, neither involved in drafting the clause, to confirm separately that their track’s comments were accurately handled and major risks were not ignored. This does not mean the text is stable or representative. The higher thresholds in Section VI apply from the second round onward. These two roles cannot be filled by the same person.

---

## III. Role Registration for Each Round

Copy and complete this table before formal opening:

| Item | Name or public designation | Term/applicable round | Contact details public? | Conflicts of interest | Notes |
| --- | --- | --- | --- | --- | --- |
| Person responsible for final decisions | To be completed | To be completed | To be completed | To be completed |  |
| Round coordinator | To be completed | To be completed | To be completed | To be completed |  |
| Submission recorder | To be completed | To be completed | To be completed | To be completed |  |
| Identity verifier | To be completed | To be completed | No | To be completed | Do not publish private contact details |
| Privacy lead | To be completed | To be completed | To be completed | To be completed |  |
| Reconsideration reviewer | To be completed | To be completed | To be completed | To be completed |  |

Formal review must not be declared open while any “To be completed” entries remain.

---

## IV. Conflicts of Interest

The following relationships must be proactively declared:

- Direct responsibility for drafting, approving, or signing the reviewed text;
- Management, ownership, employment, funding, contractual, co-authorship, or other organizational relationships with relevant companies, platforms, unions, research institutions, political organizations, funders, commercial products, or question submitters;
- Review outcomes that may directly affect one’s employment, contracts, litigation, project income, or reputation;
- Close relationships or direct disputes with worker participants, submitters, drafters, or decision-makers that could affect independent judgment;
- Other relationships a reasonable observer might consider capable of affecting impartial handling.

Conflicts are classified as:

1. **No known conflict**: Normal participation;
2. **Manageable conflict**: Disclose the relationship; opinions may be offered but cannot constitute the sole basis for a decision;
3. **Major conflict**: Labeled opinions may be submitted, but the person must withdraw from final decisions, identity verification, or reconsideration concerning the matter.

Strong views, criticism of the project, previously expressed preferences, or a theoretical position do not themselves constitute disqualifying conflicts of interest. The factual relationships that may affect independent handling must be disclosed and classified.

---

## V. Recusal Procedure

1. Participants or handlers declare conflicts to the coordinator immediately upon discovering them;
2. The coordinator records the conflict category and proposed restrictions without publishing unnecessary private details;
3. The person challenged may explain the circumstances but cannot decide alone whether to recuse themselves;
4. An unconflicted decision-maker or temporary reconsideration reviewer confirms the approach;
5. If nobody can handle the matter independently, label it “deferred—awaiting independent reconsideration”;
6. The public decision log records the recusal, its procedural effects, and alternative measures.

---

## VI. Adjudication Review Panel and Maturity Thresholds

In the second and third rounds, before describing substantive clauses as having “completed dual-track review” or being “suitable for use as stable text,” form a five-person adjudication review panel for each clause:

- Two formal worker reviewers with relevant experience;
- Two formal expert reviewers in relevant fields;
- One maintainer or person responsible for final decisions without a major conflict.

Members are selected from the round’s candidate pool under publicly announced recruitment criteria, according to relevance, availability, coverage gaps, and conflicts of interest—not agreement with the current draft. Each person may occupy only one seat. Members sharing an institution, funding relationship, or direct management relationship may occupy at most two seats and must not fill an entire track. Clause drafters, question submitters, direct managers, and those directly connected through funding or benefits must recuse themselves from the corresponding review or adjudication seats for that matter. If a member cannot continue, replace them under the same public criteria and record the reason; do not temporarily seek only supporters.

Public records may use seat identifiers conveying no identity information and publish only composition and counts that cannot enable re-identification. Names, organizations, individually linked “verified track” status, and seat associations each require separate authorization. Refusal to disclose identity or verification status does not invalidate comments and must not be used to pressure disclosure. If detailed breakdowns cannot be disclosed safely, publish only aggregate composition confirmed by the recorder and reconsideration reviewer, together with this transparency limitation.

The panel does not decide by simple majority. The two workers and two experts must separately provide their tracks’ conclusions, reasons, and objections; the maintainer provides the repository disposition and responds to both tracks. When all four independent track reviewers have actually completed review and revisions, objections, recusals, and limitations have been recorded, this establishes only “dual-track review completed,” not automatic stability.

To further label the text “stable for use (subject to renewed review),” all four independent track reviewers must re-examine the final diff, commit, and SHA-256 of the proposed effective version. None may leave unanswered objections concerning facts, fundamental rights, safety, serious harm, or key scope of application, and both tracks must confirm that major objections were accurately handled. If review of the frozen old draft is complete but the new text incorporating comments awaits re-examination by all four, the only permissible label is “dual-track review completed—further revision possible.” Non-substantive wording preferences may remain and be disclosed; unresolved substantive disagreements of the kinds above require “dual-track review completed—disputes unresolved.” Insufficient personnel or evidence requires “insufficient evidence”; a maintainer’s merge cannot substitute for review conclusions.

Stable status applies only to the precise file version, commit, and SHA-256 specified in the decision record. Any subsequent change that could alter meaning, scope, rights, or risks returns the new version to “maintainer draft” or “awaiting confirmation by all four”; it must not automatically inherit the previous version’s maturity. Even formatting-only or link corrections must explain why meaning is unaffected.

The panel produces review conclusions and recommendations; whether to merge into the GitHub repository remains a separate maintenance-authority decision. Maintainers may merge drafts under existing governance, but must label their actual maturity and must not describe “merged” as “passed independent review.”

The first round tests procedure and is not subject to the five-person panel and representativeness thresholds; if personnel are insufficient, only process pilot review results or maintainer drafts may be published. In later rounds, if the project is too small to form the panel, disclose the capacity gap and leave the corresponding matters unresolved.

---

## VII. Decision Authority and Claims of “Passing Review”

During the founding stage, the initiator or future maintainers retain final review authority over merging core documents under [../../GOVERNANCE.en.md](../../GOVERNANCE.en.md). This authority must be constrained by public reasons, version records, conflict-of-interest recusal, and reconsideration procedures.

“Authorized to merge” does not mean “independent review completed.” Only a maintainer draft or deferred decision may be issued if any of the following applies:

- The decision-maker drafted the relevant clause and lacks dual-track confirmation by an independent worker and independent expert;
- Major risks have not undergone separate checks by workers and relevant experts;
- Reconsideration is needed but nobody uninvolved in the original handling is available;
- Review-track participation or publication authorization is insufficient for the intended public claim.

Different maturity levels require different descriptions:

- **Maintainer draft**: Formal expert and worker review has not been completed;
- **Process pilot review version**: First-round process testing completed, with no claim of representativeness;
- **Targeted-review revised version**: Second round completed, with coverage and gaps disclosed;
- **Open-call revised version**: Third-round public solicitation and reasoned processing completed;
- **Continuously revised version**: Published but still subject to renewed review.

Some endorsements, a majority vote, or participation by prominent experts do not justify expressions such as “unanimously endorsed by workers,” “expert-certified,” or “representing the working class.”

---

## VIII. Evidence and Decision Records

Substantive handling of every review comment must be explained in [DECISION_LOG.en.md](DECISION_LOG.en.md). Major decisions concerning core direction, licensing, or governance structure must also create or link a project-level decision record under [docs/decision-records/](../decision-records/README.en.md): the former answers “how was this review comment handled?” and the latter “why did the project make this major directional decision?” Cross-link them through decision identifiers, Pull Requests, or commits.

- What is or is not being changed;
- Why;
- Which review identifiers, facts, and sources support the decision;
- What the expert and worker comments say separately;
- Which comments were not adopted and why;
- What recusals, reconsideration, or procedural limitations apply;
- What disputes remain;
- Which version the decision applies to.

Decision-makers may disagree with the majority, but must explain the higher-priority facts, rights, serious risks, or consistency considerations supporting their decision.

---

## IX. Participant Conduct Boundaries

All roles must follow [../../CODE_OF_CONDUCT.en.md](../../CODE_OF_CONDUCT.en.md). They must not:

- Require workers to prove their identities publicly;
- Decide identity-verification outcomes based on the content of opinions;
- Privately contact, pressure, or investigate anonymous submitters;
- Publish unauthorized employer, role, or contact information;
- Manipulate counts, delete unfavorable comments, or count duplicate submissions as support from multiple people;
- Promise funding, jobs, legal outcomes, or organizational representation on the project’s behalf.

---

## X. Role Changes

Appointments, removals, permission changes, and access revocations must record dates and applicable rounds. When personnel leave, access to non-public materials must be revoked immediately, and the privacy lead must check that temporary copies they hold have been deleted as required.
