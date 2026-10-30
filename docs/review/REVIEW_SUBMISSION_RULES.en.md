# Review Submission Rules

> **Chinese version:** [阅读中文版](REVIEW_SUBMISSION_RULES.md)

> Status: Public discussion draft<br>
> Version: v0.2-draft<br>
> Applies to expert reviews, worker reviews, and general public comments. For evaluation questions, see [QUESTION_SUBMISSION_RULES.en.md](QUESTION_SUBMISSION_RULES.en.md).

---

## I. Distinguish Two Questions First

“How is a submission sent?” and “Has publication of its contents been authorized?” are separate questions:

- Content submitted through GitHub Issues, Discussions, or Pull Requests is public by default;
- Submission through email or a private form does not imply consent to publication;
- Identity information for formal review must remain non-public, while participants may choose full publication, publication after anonymization, or internal processing only for the review text;
- The project must not automatically synchronize non-public originals to GitHub, Hugging Face, or public webpages.

---

## II. Channel Matrix

| Channel | Permitted content | Prohibited content | Counts as formal review? |
| --- | --- | --- | --- |
| GitHub Issue / Discussion | Public comments that have passed a privacy self-check | Contact details, verification materials, sensitive experiences, third-party information | Public submission alone does not count |
| Pull Request | Public text changes and reasons | Any identity or verification materials | A PR alone does not count |
| Official theoretical-submission email | Theoretical papers, research notes, de-identified preliminary materials | Formal review identity-verification materials, high-risk original evidence | Not a formal review channel |
| Public project website form | Public text once launched | Identity documents and sensitive materials | A public form alone does not count |
| Designated non-public channel | Contact information, verification, non-public text, and authorization | Information not normally collected | May count after verification |
| Security reporting channel | Actual or potential privacy and security problems | General discussion and public debate | Not a review channel |

Formal verification materials must not be collected until the non-public channel is announced as “configured” in the [mechanism index](README.en.md).

---

## III. Review Identifiers and Data Separation

### 3.1 Internal and External Identifiers

A random receipt identifier is generated for non-public submissions:

> WAI-SUB-ROUND-RANDOM

It is used only for participant inquiries, supplements, withdrawal, rights requests, and internal deduplication. It must not be published or pasted into GitHub.

A separate public record identifier is generated only after the participant authorizes publication of the text or an anonymized summary and the project checks re-identification risks:

> WAI-PR-ROUND-TYPE-SEQUENCE

Types:

- EX: Expert review;
- WK: Worker review;
- PB: General public comment;
- QS: Evaluation-question comment.

The example WAI-PR-R01-WK-0001 denotes only an authorized public record in the worker track of the first round; it conveys no identity information. Private receipt identifiers and public record identifiers must not be identical, derivable from each other, or appear together on a public page.

When a review form addresses multiple principles or independently decidable issues, append a subitem identifier to each processing unit:

- I00: Only for overall structural comments that cannot be divided further;
- I01, I02…: Individual principles or independent issues;
- Each public ledger row records only one subitem and one disposition;
- Supplements, corrections, and reconsideration of the same subitem do not count as additional participants.

### 3.2 Three Types of Records

1. **Public comment records**: Public record identifier, authorized target version, clause, text or summary, processing status, and public decision;
2. **Private contact and authorization records**: Random receipt identifier, contact details, authorization choices, and expiry date;
3. **Temporary verification records**: Random receipt identifier, verification materials or conversations, verification outcome, and deletion date.

Mappings between internal and external identifiers must not enter the public repository. Content handlers should normally see only the internal random receipt identifier and broad categories necessary for their task. Comments designated “internal processing only” receive no individual public records; round summaries report anonymized aggregate counts and themes only where re-identification is not possible.

---

## IV. Required Fields for Each Comment

General public comments must include at least:

- The reviewed document, version, or identifiable target date;
- Clause identifier or location in the original text;
- Main issue;
- Proposed revision or question the project should answer;
- Whether the reasoning concerns facts, firsthand experience, secondhand accounts, professional judgment, or value judgments;
- Confirmation of a completed privacy self-check.

Formal expert or worker reviews must also use the corresponding review form and provide contact information, verification, and authorization choices in the non-public section.

If one form reviews multiple clauses, the recorder must split it into subitems during initial screening. Submitters need not generate identifiers themselves, but should align each comment with its reasons and recommendations wherever possible.

If the version cannot be determined, the project may help identify it; until confirmed, its status is “awaiting supplementary information” and it must not enter formal statistics.

---

## V. Remove Before Public Submission

- Identity-document numbers and photographs;
- Telephone numbers, private email addresses, social accounts, and home addresses;
- Bank account numbers, payslips, social-insurance details, and financial information;
- Complete employment contracts, diagnostic materials, or dispute evidence;
- Non-public documents of companies, platforms, unions, or other organizations;
- Identifiable combinations of actual employers, precise locations, employee numbers, rare roles, and exact times;
- Information about colleagues, supervisors, clients, family members, or other third parties;
- Account passwords, access tokens, internal links, or security-vulnerability details;
- Anything participants do not wish to remain public long-term.

Removing names alone is usually insufficient for anonymization. Submitters should check whether combinations of industry, city, work team, dates, events, and unusual experiences still allow identification.

---

## VI. Boundaries for Non-public Submissions

The project does not normally collect complete identity documents, bank cards, biometric information, account passwords, precise addresses, medical information unrelated to review, minors’ identity information, family-member information, or employer trade secrets.

If participants voluntarily send unnecessary materials:

1. The recipient stops forwarding and substantive reading;
2. Records minimal incident information;
3. Asks the participant to use redaction or a lower-risk method;
4. Deletes unnecessary materials promptly under the privacy notice;
5. Starts the security incident process if disclosure has already occurred.

---

## VII. Duplicates, Supplements, and Multiple Identities

- One person may review different principles or submit different comments;
- Only one formal comment counts per person, principle, round, and primary role;
- Supplements, corrections, and evidence updates are appended to the same identifier;
- Identical content submitted through multiple channels is consolidated without counting participants twice;
- Participants who are both experts and workers choose a primary track for each comment; for the same principle and round, they count in only one track. Observations from their other identity may supplement the narrative but do not count as a second participant;
- Multiple accounts, pseudonyms, or organization members must not mass-copy identical text to manufacture proportions;
- Organizational joint statements must report both “one jointly signed text” and reasonably deduplicated participant counts; copied text cannot be treated as independent argument.

Clear duplicates are marked by their record relationships; original public links are not silently deleted. Round summaries report both track-specific counts and deduplicated cross-track participant counts.

---

## VIII. Assisted Entry and Translation

Trusted people may transcribe or translate. Submitters should confirm that the final text reflects their own judgment and that assistants have not independently changed the conclusion.

---

## IX. Submission Licensing and Publication Authorization

- Participants retain the rights they lawfully hold in their original comments;
- Choosing to publish full text or a confirmed anonymized summary requires explicit agreement to publication under the repository’s content license, CC BY-SA 4.0;
- Internal-only content must not be published verbatim or incorporated directly into public text;
- The project may edit to remove personal information, correct formatting, or prepare summaries, but substantive rewriting requires participant confirmation;
- Short phrases from public comments may appear in round summaries within reasonable quotation limits, while avoiding re-identification and citing the comment identifier;
- Unauthorized cases, images, tables, full papers, and third-party materials must not enter the repository.

---

## X. Corrections, Withdrawal, and Late Submissions

- Participants may request corrections using their original contact method or receipt information;
- Unpublished content may be withdrawn before the round closes; withdrawal of never-published comments does not create new public ledger rows and is reflected only in safe aggregate counts;
- Content already published under an open license may have been copied by third parties, so complete withdrawal cannot be guaranteed; privacy, security, or legal risks still require best efforts to de-identify or restrict further dissemination;
- Comments received after a round closes may enter the next round or ongoing review; they must not be backfilled into published counts and conclusions for the closed round;
- After substantive changes to the reviewed text, old comments must not automatically be treated as endorsement of the new version; submitters should be invited to reconfirm, or the historically applicable version should be marked.

---

## XI. Submission Receipts

Contactable submitters should receive:

- A non-public random receipt identifier;
- Receipt date;
- Identified target version and clauses;
- Current process status;
- Whether supplementary information is needed;
- Expected next feedback date;
- How to correct, withdraw, request deletion, and request reconsideration.

Those submitting publicly without other contact details should retain their public link and consult [REVIEW_LOG.en.md](REVIEW_LOG.en.md) and round summaries for results. Private submitters must not post their receipt identifiers publicly to inquire.

---

## XII. Invalidity and Security Handling

Submissions may be marked invalid only for:

- Impersonation, fabricated identity, or invented employment experience;
- Manipulating participant counts through duplicate accounts or mass-produced text;
- Malware, prompt injection, credentials, or other security attacks;
- Harassment, threats, hate, or exposure of others’ private information;
- A wholly unidentifiable review target with no response during the supplementation period;
- Advertising, scams, or spam unrelated to the project.

Disagreement with the project, sharp criticism, recommending deletion, minority opinions, evidence awaiting verification, unconventional writing, or anonymity must not alone invalidate a submission.
