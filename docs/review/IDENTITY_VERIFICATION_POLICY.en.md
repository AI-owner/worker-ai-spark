# Identity Verification Rules for Review Participants

> **Chinese version:** [阅读中文版](IDENTITY_VERIFICATION_POLICY.md)

> Status: Public discussion draft<br>
> Version: v0.2-draft<br>
> Verification is used only to confirm participation categories, establish contact, and prevent duplicate counting. It does not determine whether a view is correct.

---

## I. Scope

Identity verification applies only to applications for:

- Formal worker review;
- Formal expert review;
- Public attribution as a formal reviewer.

Verification may begin only after the project announces a dedicated private channel, using the [Expert Participation Application Form](EXPERT_REVIEW_APPLICATION_FORM.en.md) or the [Worker Participation Application Form](WORKER_REVIEW_APPLICATION_FORM.en.md). A public Issue expressing interest in participating does not trigger identity verification and must not serve as a channel for collecting private supporting materials.

Ordinary feedback that is public, non-public, or unattributed in the body of a document does not require verification. GitHub is not an anonymous channel. People who cannot or do not wish to undergo verification may still participate, but are not counted among formally verified participants. Non-public feedback may be safely aggregated only when re-identification is not possible.

---

## II. Minimum Necessary Information

Verification does not aim to establish a person's legal name. It aims to make a reasonable assessment of whether:

1. The participant broadly meets the criteria for the review category they declare;
2. The project can contact the participant when necessary;
3. The same feedback has not been counted repeatedly under multiple identities.

The project does not need full identity document numbers, home addresses, bank accounts, full employer details, or private information unrelated to the review.

Identity verification must be independent of the content of feedback. Opposing the project, recommending the removal of principles, declining attribution, or giving a very low score must not be grounds for failing verification.

---

## III. Low-Risk Verification for Formal Worker Reviewers

Methods are prioritized from lower to higher risk:

1. Describe the industry, type of work, work processes, and broad work experience;
2. Obtain a referral from an already confirmed participant;
3. Provide a public personal profile that supports the relevant experience;
4. Hold a brief written or live conversation, without retaining audio, video, or the full conversation after verification;
5. Provide thoroughly redacted excerpts from work identification, professional qualifications, contracts, pay records, social insurance records, or work communications;
6. Use another method that the privacy lead confirms is necessary, proportionate, and relatively low-risk.

Completing one of these methods is normally sufficient. Another method may be requested only when the existing information is clearly inconsistent or insufficient, and the reason it is necessary should be explained.

The following must not be requested:

- Complete images of both sides of an identity card;
- Complete employment contracts, payslips, social insurance statements, or bank statements;
- Biometric information such as facial images, fingerprints, or voiceprints;
- Exact residential addresses, account passwords, or financial accounts;
- Business secrets or internal documents whose disclosure is unauthorized;
- Information about colleagues, supervisors, clients, or family members.

Employers, platforms, supervisors, colleagues, or family members must not be contacted for verification unless the participant gives separate, explicit consent after being informed of the specific contact, information involved, risks, and alternatives.

---

## IV. Low-Risk Verification for Formal Expert Reviewers

Normally, one of the following is selected:

- A public university, research institution, employer, or personal profile;
- An ORCID or another public researcher identifier;
- Public papers, books, reports, projects, or records of sustained professional practice;
- Public professional qualification or licensing information;
- Confirmation through an institutional email address, without retaining email content beyond what is needed for contact;
- A referral from a confirmed relevant institution, expert, or participant;
- Other public or low-risk materials that reasonably support the relevant experience.

Verifiers assess only whether the background broadly matches what was declared. They do not judge institutional prestige, theoretical positions, or the correctness of conclusions.

---

## V. Verification Procedure

1. **Inform**: Provide the current privacy notice, purposes, material options, retention periods, and rights;
2. **Choose**: The participant selects the lowest-risk method that is sufficient;
3. **Receive**: Create a mapping between participant_id and a random submission_id through a non-public channel;
4. **Verify**: An authorized verifier reviews the minimum information necessary;
5. **Record**: Record only the result, method category, date, verifier role, and deletion deadline;
6. **Separate**: Content handlers receive the private submission_id and a “verified/unverified” status and, as a rule, do not access the original materials;
7. **Delete**: Delete original materials in accordance with [PRIVACY_NOTICE.en.md](PRIVACY_NOTICE.en.md);
8. **Notify**: Communicate the result, the minimum additional information needed, and how to request reconsideration.

---

## VI. Verification Results

| Result | Meaning |
| --- | --- |
| Verified—worker | The declared category of work experience is broadly supported |
| Verified—expert | The declared relevant professional background is broadly supported |
| Additional information pending | Existing information is insufficient or inconsistent; no conclusion has been reached |
| Verification incomplete | The participant did not respond, withdrew, or chose not to continue |
| Verification unsuccessful | Specific reasons indicate that the declared category is not supported or that impersonation is involved |

“Verification incomplete” does not mean the information is false. The feedback becomes ordinary public or non-public participant feedback. “Verification unsuccessful” must be accompanied by reasons that can be reviewed; subjective suspicion alone is insufficient.

---

## VII. Limits on Verification Records

By default, verification results are included only in anonymous aggregate statistics, with no individual disclosure. Only when participants separately consent to disclosure of the relevant metadata, their feedback is also authorized for publication, and the combined information cannot lead to re-identification may the public register record:

- A separately generated public record identifier;
- The expert, worker, or unverified track authorized for public disclosure;
- Broad conflict-of-interest categories that are authorized for disclosure and necessary.

Individual verification completion dates, verification methods, private receipt identifiers, and information that could link a GitHub account to non-public identity materials must not be disclosed.

Minimal non-public records may include:

- The mapping between participant_id and submission_id;
- Contact information;
- Verification method category;
- Verified, additional information pending, or unsuccessful status;
- Verification date and verifier;
- Consent version;
- Date of deletion of original materials.

If a public record identifier exists, it is linked to submission_id only in a restricted mapping.

Real names, employers, or job roles may be recorded only when the participant has given separate, explicit authorization for each relevant item, the feedback is also authorized for publication, and a re-identification risk check has been passed. Private email addresses, supporting-evidence links, private receipts, and verification process notes must not enter the public register.

---

## VIII. Access and Separation of Responsibilities

- Only registered verifiers and the privacy lead may access original verification materials;
- Decision-makers must not receive access if they do not need to see identity information;
- Access should be logged with the date, person, purpose, and file category;
- Permissions should be revoked promptly when a person leaves a role or a review round ends;
- A “private Git repository” must not be treated as the default safe option for storing identity evidence;
- Verification materials must not be copied into personal messaging tools, public cloud drives, training data, or other unapproved services;
- Verifiers must not use the materials outside the review for publicity, profiling, screening, or personal contact.

When there is only one maintainer, the inability to fully separate responsibilities should be publicly disclosed, and preference should be given to public background information or inspection without retention.

---

## IX. Additional Information and Reconsideration

A request for additional information should explain:

- Which information is insufficient;
- Why it is necessary to confirm the category;
- Available low-risk alternatives;
- The response deadline;
- How the feedback will be classified if no additional information is provided.

Participants may request reconsideration of unsuccessful verification, misclassification, or a determination that they are a duplicate participant. Reconsideration must not consist solely of the original verifier repeating their initial judgment. If no one can conduct an independent reconsideration, the status remains “additional information pending/on hold,” and the capacity limitation is disclosed.

---

## X. Minors

At the current stage, the project does not conduct formal identity verification for anyone under 18 or collect their identity materials. If the project needs to involve minors in the future, it should establish separate rules for guardian consent, tailored notices, safety assessments, information processing, and withdrawal before receiving submissions.

---

## XI. What Verification Does Not Mean

Verification does not mean that:

- The project agrees with all of the participant's views;
- The feedback automatically receives greater substantive weight;
- The participant represents an entire industry, the expert community, or the working class;
- The project endorses the participant's personal conduct, their employer's positions, or their other public views;
- The project has confirmed every detail of their legal identity, employment relationship, or professional qualifications.
