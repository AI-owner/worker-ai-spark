# Public Review Work Plan for the Basic Principles for Workers' AI

> **Chinese version:** [阅读中文版](PUBLIC_REVIEW_PLAN.md)

> Document status: Public discussion draft<br>
> Version: v0.2-draft<br>
> Scope: Review of the principles, handling review comments, and collaborative development of evaluation questions<br>
>
> Current implementation stage: Transition from Stage One to Stage Two—the draft procedures are in the current repository; formal review is not open
>
> Formal submissions: Not open
>
> Status updated: 2026-08-25
>
> Formal publication date: Subject to confirmation by the project lead

---

## I. Purpose and Boundaries

The Basic Principles for Workers' AI are currently an early draft. Public review is intended neither to recruit people to endorse the project nor to declare, through a single vote, that the principles represent workers broadly. Its purpose is to establish an open, traceable mechanism for scrutiny that accommodates dissent and ongoing revision.

This plan establishes the following cycle:

> Freeze the version under review → Expert review → Worker scrutiny → Public feedback → Reasoned decisions → Revise the principles → Jointly develop evaluation questions → Pilot evaluations across multiple models → Publish results and limitations → Revise again

This stage prioritizes establishing procedures and conducting a small-scale pilot review of the process. The current repository establishes only acceptance criteria and reproducible protocols for a web entry point and a Hugging Face evaluation prototype. Actual services, accounts, dataset repositories, and public links should be developed after the procedures operate reliably and the project separately confirms the work. This plan does not invent services supposedly already online.

### 1.1 The Original Work Plan’s Five Stages and Current Status

The table below maps only the execution sequence in `测评机制.txt`. It does not replace the long-term project stage numbering in [../../ROADMAP.en.md](../../ROADMAP.en.md); the two numbering systems serve different purposes.

| Original work plan stage | Deliverables or entry conditions | Current status |
| --- | --- | --- |
| Stage One: Complete draft procedures | Overall plan, dual-track rules, submissions and feedback, verification and privacy, question-bank rules | Draft procedures are in the current repository and await the initiator’s final check |
| Stage Two: Public disclosure on GitHub | Commit, review, and publish after the initiator confirms the document scope | Procedural documents are in the current repository and linked from the public index; the publication scope, target remote, and version status await verification by the project lead |
| Stage Three: First pilot review | Privacy responsibilities, a non-public channel, a frozen version, roles, dates, and trial completion of forms are all ready | Not started |
| Stage Four: Broaden invitations after revision | Complete the first revised version, decision records, and process retrospective | Not started |
| Stage Five: Website and Hugging Face prototype | Procedures are stable, Section XIII’s acceptance criteria are met, and the project separately confirms the work | Acceptance specifications are established; no claim is made that actual services are online or published |

This table describes only document states verifiable in the current repository. It does not infer live remote-platform settings or publication facts. Before formal review opens, the project lead should verify and update actual links, dates, target branches, branch protection, and the effective CODEOWNERS status.

---

## II. Basic Principles

### 2.1 Openness and Traceability

Versions of the principles, review rules, anonymized outcomes, major disagreements, and revision records should normally be public. The project records not only support but also representative objections, reservations, and unresolved comments.

### 2.2 Workers’ Agency

Workers are co-authors of the principles and evaluation mechanisms. Experts may examine theoretical, factual, legal, ethical, and technical quality, but cannot replace workers’ judgment about whether scenarios are realistic, language is understandable, and who bears the risks.

### 2.3 Expert Scrutiny

Experts in relevant fields examine concepts, evidence, internal consistency, practicability, evaluability, and potential misuse. Professional standing does not automatically make an opinion correct; its reasoning remains open to challenge.

### 2.4 No Monopoly on Interpretation

The initiator is responsible for early maintenance, but no initiator, expert, worker, institution, or model is an unquestionable final authority.

### 2.5 Multiple Rounds of Revision

Review is not a one-off referendum. Each round should publish its objectives, actual coverage, limitations, and next steps. Simple majority votes must not replace reasoned judgment.

### 2.6 Privacy and Safety

Public text and non-public identity materials must be separated. Collect only the minimum information needed for contact and necessary verification. Identity documents, contact details, non-anonymized labor disputes, and internal workplace materials must never enter the public repository.

### 2.7 Accessibility and Low Barriers

Participation does not require GitHub skills, specialist terminology, or formal qualifications. Before each round formally opens, at least one channel must be available that does not depend on GitHub and supports low-bandwidth use or project-assisted entry. Plain-language text and available assistance must be published; assistants must not make judgments on participants’ behalf. Formal review must not be announced as open without a safe, usable non-GitHub channel.

### 2.8 Protection Against Retaliation and Discrimination

Participants must not be disadvantaged for criticizing the project, choosing anonymity, declining unnecessary verification, withdrawing consent, or using assistance. When materials could expose identities or lead to workplace retaliation, priority must be given to stopping publication and reducing identification risks.

---

## III. Review Scope and Version Freeze

Before each round, the review coordinator must publish a round announcement recording:

- File names and public links for the documents under review;
- Text version number;
- Git commit;
- File SHA-256;
- Review scope and matters outside this round’s scope;
- Start and end dates, expected feedback date, and time zone;
- Target professional fields, industries, and forms of employment;
- Participation channels and privacy-notice version;
- The round’s lead, verification roles, and decision owners;
- Unresolved disputes from the previous version.

If the principles require an urgent correction during review, submissions on affected items must stop, the reasons for the change must be published, and a new version must be frozen. Comments addressing different target versions must not be merged without explanation.

---

## IV. Participation Levels

| Level | Type | Minimum requirements | Public reporting category |
| --- | --- | --- | --- |
| Level One | Ordinary public, pseudonymous, or non-public comments | No identity verification; public channels must contain no sensitive information | Unverified public comments; non-public comments reported only in safe aggregates |
| Level Two | Formal worker review | Contact details, account of work experience, light-touch verification, consent to use | Formally verified workers |
| Level Three | Formal expert review | Contact details, professional experience, background verification, conflict-of-interest declaration | Formally verified experts |
| Level Four | Voluntary public attribution | Completed Level Two or Three verification and item-by-item authorization for publication | Named reviewers |

Identity verification establishes only that the declared category is basically credible. It does not increase the weight of an opinion, establish that the participant represents a group, or imply project endorsement of their views.

Participants with multiple identities should choose one primary review role for each submission. The same person reviewing the same principle in the same round counts toward only one primary track. Perspectives arising from another identity may be included as narrative context, but do not count as a second participant or toward a second track’s headcount. Round summaries should report deduplicated numbers for cross-track participation.

---

## V. Multi-Round Schedule

### 5.1 Round One: Process Pilot Review

The aim is to test whether forms are clear, principles are understandable, public and non-public channels are genuinely separated, verification is overly burdensome, and feedback can be delivered on time, while identifying obvious omissions and ambiguities.

Round One does not pursue a sample-size target or claim broad representativeness. Completion requires:

- Handling valid comments received before the round’s deadline;
- Publishing the actual participant composition and coverage gaps;
- Completing a privacy and process retrospective;
- Publishing item-by-item decisions or explicit reasons for deferral;
- Producing at least one inspectable, limited-scope revised version and publishing before-and-after differences and decision records; if no changes are made, explaining the reasons item by item;
- Establishing the next round’s revision list.

### 5.2 Round Two: Targeted Invitations

Priority invitations should cover artificial intelligence, algorithmic governance, labor relations, trade-union studies, labor law, social security, sociology, political economy, and occupational health and safety, as well as participants with experience in factories, platform work, services, care, logistics, construction, flexible employment, unemployment, retirement, and occupational transitions.

This round focuses on applicability across industries, labor relations, and forms of employment. Its summary must disclose groups still not covered and must not infer overall opinion from a small number of participants.

From Round Two onward, any provision proposed for designation as having “completed dual-track review” or being “suitable for use as a stable text” must receive independent review by at least two formal worker reviewers with relevant experience and two relevant formal expert reviewers, and proceed to a five-person adjudication panel under the [Governance, Roles, and Recusal Rules](GOVERNANCE_AND_ROLES.en.md). Where numbers, track coverage, or independence are insufficient, the only permissible labels are “insufficient evidence,” “dispute unresolved,” or “maintainer draft.” No exemptions are allowed.

### 5.3 Round Three: Open Call for Review

Comments will be invited through GitHub, the project website once online, and other announced channels. People not specifically invited may submit ordinary public comments, apply for formal expert or worker review, contribute evaluation questions, or offer technical, translation, and governance suggestions. Workers may submit true cases they personally experienced, directly know about, or have reasonable factual grounds for, and choose real-name, pseudonymous, anonymous, or internal-only handling. Identity, workplace, contact details, original materials, and substantive text require separate authorization. Leads requiring account concealment, identifying third parties, or potentially triggering retaliation may use only the non-public channels designated in the round announcement. No public channel may be described as anonymous.

### 5.4 Subsequent Rounds: Ongoing Review

A new round may be launched when principles change substantially, new AI scenarios or labor risks emerge, important disputes remain unresolved for a prolonged period, evaluation practice reveals that principles cannot be tested, or participants raise significant new issues.

### 5.5 Maturity and Coverage Thresholds

Scores, participant numbers, and likes may trigger further scrutiny but cannot automatically determine adoption or “approval.” From Round Two onward, each substantive provision proposed as stable must separately report valid reviewer numbers, gaps, recusals, and dissent in the worker and expert tracks. It must not be labeled stable if either track has fewer than two relevant independent formal reviewers, major risks remain unresolved, or factual, fundamental-rights, safety, serious-harm, or key-scope objections raised by any independent track reviewer remain unanswered. Where four-person dual-track review is complete but substantive disagreement remains, the only permissible label is “dual-track review completed—dispute unresolved.” This threshold does not establish statistical representativeness or permit a few participants’ views to be presented as the shared opinion of an entire group.

---

## VI. Standard Workflow

1. **Preparation**: Meet opening conditions, freeze the version, and publish the round announcement;
2. **Receipt**: Generate a private random receipt identifier; generate a separate public record identifier only after publication authorization is obtained;
3. **Privacy pre-check**: First check public text for sensitive information or third-party information;
4. **Format review**: Assess scope, completeness, duplication, and whether supplements are needed;
5. **Identity verification**: Conduct light-touch verification through non-public channels only for applicants seeking formal status;
6. **Track classification**: Record expert, worker, and ordinary public comments separately;
7. **Analysis and clarification**: Analyze facts, impacts, risks, coverage, consistency, and testability, requesting supplements when necessary;
8. **Draft decision**: State the outcome, reasons, proposed revision locations, and unresolved questions;
9. **Recusal and reconsideration**: Check conflicts of interest; reconsider major disputes under these procedures;
10. **Individual feedback**: Send decisions or progress updates to contactable formal reviewers;
11. **Public summary**: Publish an anonymized register, separate track summaries, representative dissent, and coverage limitations;
12. **Revision and records**: Amend core files through Pull Requests and update the decision log;
13. **Scheduled deletion**: Execute the deletion schedule for verification materials and contact details;
14. **Retrospective**: Revise forms, rules, and coverage goals for the next round.

---

## VII. Judgment Framework

Review conclusions must not be determined solely by vote counts. Those handling comments should answer at least the following:

- Are the facts, law, or research relied upon reliable, and to which periods and jurisdictions do they apply?
- What benefits, costs, and serious harms could arise for workers?
- Could aggregate averages conceal major risks borne by minority groups?
- Are the work scenarios realistic, and is managerial convenience being confused with workers’ interests?
- Does the proposal conflict with other principles, and how should conflicts be resolved in application?
- Can it be translated into clear AI behavior requirements and repeatable evaluations?
- Could companies, platforms, governments, project maintainers, or other holders of power misuse it?
- Are there lower-risk, more clearly worded alternatives?

Factual errors cannot be retained because a majority supports them. Infrequent concerns involving possible serious harm cannot be ignored because few people raise them. One true experience can reveal a problem, but cannot be generalized to everyone without verification.

---

## VIII. Relationship Between Expert and Worker Comments

- Expert comments examine professional quality and do not replace judgments about scenario realism;
- Worker comments examine comprehensibility, realism, and impacts, and need not first become academic arguments to be recorded;
- The two categories are summarized separately, without a combined overall score;
- Where experts approve but workers find the text confusing or detached from reality, revise its wording or applicability guidance;
- Where workers identify a major issue but professional evidence is insufficient, invite further analysis by relevant experts rather than disregard the issue;
- Where the two categories conflict, publish the conflict, supporting grounds, affected groups, and provisional handling; do not fabricate consensus.

---

## IX. Processing Timeframes

The following are service targets under normal conditions. If volunteer maintenance capacity is insufficient, pauses or delays should be announced in advance:

| Step | Target timeframe |
| --- | --- |
| Receipt acknowledgment and identifier | Within 3 working days |
| Initial privacy and completeness review | Within 7 working days |
| Deadline for supplementary materials | 10 calendar days after notification |
| Progress updates for prolonged processing | At least once every 15 working days |
| Individual feedback on formal comments | Within 30 working days after the round ends |
| Public round summary | Within 15 working days after individual feedback is completed |
| Request for reconsideration | Within 10 working days after delivery or publication of the decision |
| Response to reconsideration request | Within 20 working days after receipt of a complete application |

Extensions must record the reason, new date, and interim risk controls. Anonymous participants without a receipt channel can consult the public register and round summary for outcomes.

---

## X. Suspension and Escalation

The coordinator should suspend relevant submissions or publication when:

- Non-public channels, access controls, or deletion mechanisms are not ready;
- Public content reveals identity information, trade secrets, or details that could trigger retaliation;
- The target version is unclear or changes substantively during review;
- The sole decision-maker has a major conflict of interest that cannot be resolved through recusal;
- Mass impersonation, duplicate manipulation, harassment, or security incidents occur;
- Available capacity cannot safely handle sensitive materials;
- Legal, ethical, or major personal-safety risks require professional handling.

Handle privacy and security incidents under [../../SECURITY.en.md](../../SECURITY.en.md); do not discuss unresolved vulnerability details in public Issues.

---

## XI. Public Outputs

Each round should normally publish:

- The version reviewed, dates, and actual process;
- Mutually exclusive primary-category counts for formally verified experts, formally verified workers, unverified public comments, unverified non-public comments, and invalid or duplicate submissions; named, pseudonymous, text without attribution, and internal-only handling must be reported separately as non-additive attributes;
- Anonymized distributions of professional fields and types of work;
- Separate summaries of expert and worker comments;
- Adopted, partially adopted, rejected, deferred, and unresolved matters;
- Before-and-after differences, reasons, supporting grounds, and applicable versions;
- Limitations concerning samples, channels, regions, languages, industries, and methods;
- Plans for the next round.

Views, likes, reposts, and brief comments do not count toward formal reviewer numbers.

---

## XII. Changes to These Procedures

This plan is itself a draft. Substantive changes should explain what changed, why, the supporting grounds, comments not adopted, remaining disputes, and the effective version. If changes affect the purposes, publication scope, or retention periods of personal information already submitted, participants must be informed again before processing continues, and renewed consent obtained where legally required.

---

## XIII. Acceptance Criteria for the Future Website and Hugging Face Prototype

### 13.1 Web Entry Point

The website may be marked “online” in the repository only when all of the following are met:

- Basic participation requires no GitHub account and works on low-bandwidth connections and mobile devices;
- Public comments, non-public substantive text, identity verification, and security reports have clearly separated entry points;
- Before the form, users see the actual responsible party, service provider, storage region, purposes, retention periods, rights-request arrangements, and risk notices;
- The site supports reviewing a single principle, saving drafts, assisted completion, and accessibility checks;
- Successful submission provides a private receipt and supports inquiries, corrections, withdrawal, and deletion requests;
- Tests cover accidental sensitive-information submissions, permissions, backups, and scheduled deletion.

The minimum feature list should include: project introduction, principles reading, worker review, expert review, candidate evaluation questions, a non-public channel for leads on true cases, ordinary public comments, non-public/comments without text attribution, review progress, historical versions, comment and question decision records, project contact, and a privacy notice. Channels may launch in phases, but unavailable modules must be clearly marked. A single public form must not collect all types of content together.

The first phase explicitly excludes complex forums, points or ranking systems, real-name communities, automated identity authentication, and automated review adjudication. Before adding these features later, reassess their necessity, discrimination risks, data scope, and participation burden on workers.

Until the criteria are met, the project should state only “planned,” without publishing invented links or collecting identity materials.

### 13.2 Hugging Face or an Equivalent Public Evaluation Prototype

A public dataset or evaluation prototype may be labeled a “reproducible prototype” only when all of the following are met:

- Machine-readable questions pass the applicable schema validation and retain stable question identifiers and mappings to candidate-question decisions;
- Questions, principles, scoring rules, models, prompts, parameters, dates, and original responses are traceable;
- New questions complete the required worker scenario verification, expert and scoring-logic review, and publication permissions;
- Independent scores from at least two human raters, missing values, disagreements, reconsideration, and major risks are recorded separately;
- The data card specifies the sample, language, jurisdiction, privacy, licensing, and the limitation that it cannot determine a “final position”;
- External-platform accounts and publication actions receive separate checks and confirmation from the project lead.

See [benchmarks/evaluation-protocol.md](../../benchmarks/evaluation-protocol.en.md) for detailed operating requirements.

---

## XIV. Project Statement

This project does not claim that the current principles represent the entire working class, or that review by a small number of experts or workers can confer final authority on them. Public review is valuable because it keeps the principles open to scrutiny through workers’ experience, professional research, technical practice, and public discussion.
