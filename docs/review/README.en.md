# Public Review Mechanism

> **Chinese version:** [阅读中文版](README.md)

> Rules version: v0.2-draft<br>
>
> Text currently proposed for review: [Basic Principles for Workers' AI](../../PRINCIPLES.en.md) (the version marked in the file is `v0.1.0`; formal review has not yet opened, and the commit and file hash must be frozen separately before the round starts)
>
> Last updated: 2026-09-06

This directory organizes expert review, worker review, handling of public comments, and collaborative development of evaluation questions from workers' perspectives for the Basic Principles for Workers' AI.

Creating these files does not mean that the principles have “passed review,” or that the project already has a broadly representative expert panel or worker sample. Formal review begins to count only after all opening conditions listed on this page have been met and a round notice has been published.

---

## I. Current Status

**Ordinary comments are welcome; formal review has not yet opened.** See [Current Progress and Participation Channels](../project-status.en.md) for a consolidated account of channels and current outputs; first-time participants can begin with [Start with Three Questions](../start-here.en.md).

Draft rules and templates are complete, but the following arrangements remain outstanding. Therefore, **identity verification materials must not be collected, and public comments must not be counted as formal review**:

- [ ] Announce this round's review coordinator and person accountable for final decisions;
- [ ] Announce a non-public channel that can receive contact details and verification materials;
- [ ] Announce the name/designation and contact details of the personal information processor or responsible person;
- [ ] Confirm storage locations, authorized users, and the person responsible for deletion of non-public materials;
- [ ] Freeze the version number, Git commit, and file hash of the text under review;
- [ ] Announce the round's start and end times, coverage targets, and feedback date;
- [ ] Provide at least one working low-bandwidth or assisted participation channel requiring no GitHub;
- [ ] Decide and disclose the status of `main` branch protection and effective CODEOWNERS; if not enabled, explain responsibility for manual merge checks;
- [ ] Complete small-scale testing of review forms for comprehensibility and privacy risks.

Before these opening conditions are met, participants may still submit ordinary public comments containing no personal information through existing GitHub Issues or the enabled [GitHub Discussions](https://github.com/EastForce/worker-ai-spark/discussions). Neither public channel accepts identity verification materials, and a public submission alone cannot count as formal review. The official email address `worker.ai.spark@gmail.com` is already used for ordinary theoretical submissions and security reports, but has not been configured to receive formal review applications, identity verification, or supporting evidence; submissions to that address do not count as formal review either.

As of 2026-09-06, the public repository's Issue interface does not provide dedicated “Expression of Interest in Expert Review” or “Expression of Interest in Worker Review” templates. Readers wishing to express interest may post a brief note in Discussions without contact details or verification materials. This remains an ordinary public comment and does not constitute a formal application, eligibility verification, selection, formal participation, support, or endorsement.

Remote `main` branch protection and effective CODEOWNERS are **platform states awaiting verification by the responsible person**; repository files alone cannot prove live remote settings. Before formal review opens, the responsible person should verify branch protection rules and effective `.github/CODEOWNERS` on the target remote for the round, record the verification date and results, and disclose them accurately in the round notice. Until verification is complete, do not claim that the platform enforces review requirements for core files.

---

## II. Rules and Policy Documents

| File | Purpose |
| --- | --- |
| [PUBLIC_REVIEW_PLAN.en.md](PUBLIC_REVIEW_PLAN.en.md) | Overall goals, multiple-round arrangements, workflow, and decision principles |
| [GOVERNANCE_AND_ROLES.en.md](GOVERNANCE_AND_ROLES.en.md) | Roles, permissions, conflicts of interest, recusal, and responsibility boundaries |
| [CURRENT_REVIEW_TEAM.en.md](CURRENT_REVIEW_TEAM.en.md) | Public status page for current review preparations |
| [REVIEWER_RECRUITMENT_AND_SELECTION.en.md](REVIEWER_RECRUITMENT_AND_SELECTION.en.md) | Expert invitations, expert/worker applications, selection, capacity, and feedback mechanisms |
| [EXPERT_INVITATION_TEMPLATE.en.md](EXPERT_INVITATION_TEMPLATE.en.md) | Template for invitations to external experts after confirmation by both parties |
| [EXPERT_REVIEW_RULES.en.md](EXPERT_REVIEW_RULES.en.md) | Expert eligibility, review dimensions, and conduct rules |
| [EXPERT_REVIEW_APPLICATION_FORM.en.md](EXPERT_REVIEW_APPLICATION_FORM.en.md) | Expert participation application form for use after a dedicated private channel is enabled |
| [EXPERT_REVIEW_FORM.en.md](EXPERT_REVIEW_FORM.en.md) | Template for selected or invited experts to submit formal review text and accompanying authorizations |
| [WORKER_REVIEW_RULES.en.md](WORKER_REVIEW_RULES.en.md) | Rules for worker participation, use of experiences, and safety protection |
| [WORKER_REVIEW_APPLICATION_FORM.en.md](WORKER_REVIEW_APPLICATION_FORM.en.md) | Worker participation application form for use after a dedicated private channel is enabled |
| [WORKER_REVIEW_FORM.en.md](WORKER_REVIEW_FORM.en.md) | Template for selected or invited workers to submit formal review text and accompanying authorizations |
| [REVIEW_SUBMISSION_RULES.en.md](REVIEW_SUBMISSION_RULES.en.md) | Public/non-public channels, formats, and duplicate-submission rules |
| [REVIEW_RESPONSE_POLICY.en.md](REVIEW_RESPONSE_POLICY.en.md) | Rules for receipt, status, feedback deadlines, decisions, and reconsideration |
| [IDENTITY_VERIFICATION_POLICY.en.md](IDENTITY_VERIFICATION_POLICY.en.md) | Participation tiers, lightweight verification, and boundaries for verification records |
| [PRIVACY_NOTICE.en.md](PRIVACY_NOTICE.en.md) | Collection scope, authorization, retention, deletion, and breach response |
| [QUESTION_SUBMISSION_RULES.en.md](QUESTION_SUBMISSION_RULES.en.md) | Rules for evaluation-question submission, review, pilot testing, and inclusion |
| [QUESTION_SUBMISSION_FORM.en.md](QUESTION_SUBMISSION_FORM.en.md) | Complete candidate evaluation-question template |
| [QUESTION_LOG.en.md](QUESTION_LOG.en.md) | Ledger of candidate-question status, dual-track review, pilot testing, decisions, and stable ID mappings |
| [ROUND_NOTICE_TEMPLATE.en.md](ROUND_NOTICE_TEMPLATE.en.md) | Template for each round's opening notice, channels, capacity, roles, and privacy sign-off |
| [REVIEW_LOG.en.md](REVIEW_LOG.en.md) | Public comment ledger without identity mappings |
| [DECISION_LOG.en.md](DECISION_LOG.en.md) | Reasons, supporting grounds, dissent, and version records for formal changes |
| [ROUND_SUMMARIES/](ROUND_SUMMARIES/) | Coverage, conclusions, dissent, and limitations for each round |

---

## III. Participation Channels and Boundaries

### 3.1 Ordinary Public Comments

Ordinary public comments require no identity verification. Participants may choose to display only their GitHub username, use a pseudonym, or voluntarily disclose their real name. Publishing a name does not authorize publication of an employer, contact details, identity documents, employment verification, complete employment contracts, internal materials, or content identifying third parties.

GitHub is not an anonymous channel. Usernames, timestamps, edit history, notification emails, caches, and forked repositories may retain information for a long time. If sensitive information is posted accidentally, report it immediately through the method in [../../SECURITY.en.md](../../SECURITY.en.md); do not add further details on public pages.

### 3.2 Formal Expert or Worker Review

Formal review consists of two parts:

1. Review text that can be published or published after anonymization;
2. Non-public information used only for contact, category confirmation, and lightweight verification.

The project links the two parts using a non-public random receipt ID. A separate public record ID with no identity-related meaning is generated only after the participant separately consents to publication and a risk check is completed. Identity mapping tables, private receipt IDs, and internal handling comments must not enter the public repository. Comments without completed verification can still participate: with authorization, label them “unverified public comments” or “unverified non-public comments.” Neither may count toward formal expert or formal worker participant totals.

---

## IV. Versions and Identifiers

- Rules documents use vMajor.Minor-status, for example v0.2-draft;
- Each review round must freeze the version, commit, and SHA-256 of PRINCIPLES.md;
- Private receipt IDs use WAI-SUB-round-randomcode, solely for non-public communication between participants and the project; they must not be pasted into GitHub;
- Records authorized for publication separately use WAI-PR-round-type-sequence; where one form covers multiple provisions, append subitems I01, I02, etc.; use I00 for overall comments;
- Types are EX (expert), WK (worker), PB (ordinary public comment), and QS (evaluation question);
- Mappings between internal and external IDs are retained only in restricted records;
- Public IDs and their metadata must not contain or combine to reveal names, employers, email addresses, industries, or other information from which identity could be inferred;
- Comments designated “internal handling only” receive no individual public record and appear only in safe anonymous aggregate statistics.

---

## V. Public Commitments

- Organize expert and worker comments separately, without combining them into one overall score;
- Do not replace assessment of facts, risks, and reasons with a simple majority vote;
- Do not portray individual experiences as the views of an entire industry or all workers;
- Do not downgrade comments because they criticize the project, oppose existing principles, or decline public identification;
- Publish accepted and rejected comments, reservations, and unresolved disputes;
- Identity verification does not imply agreement with a viewpoint or endorsement by the project;
- The rules themselves remain open to review and revision.
