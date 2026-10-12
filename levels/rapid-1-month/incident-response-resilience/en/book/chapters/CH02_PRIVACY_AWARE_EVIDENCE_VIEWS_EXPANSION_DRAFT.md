# CyberABC — Rapid Incident Response and Cyber Resilience
## Chapter 02 Expansion Draft: Privacy-Aware Evidence Selection and Reproducible Review Views

**Editorial status:** **Public transitional draft component** of Chapter 02 of the **single principal English book**, not a separate completed course chapter or verified publication.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 02 — Alert triage and evidence preservation](../MANUSCRIPT.md#ch-02).  
**Specific learning gap:** Determine **which fields a bounded investigation actually needs**, how to provide analysts with a restricted derived view while preserving the source and provenance, and how to detect a projection that either exposes unnecessary information or removes essential correlation data.  
**Do not duplicate:** The existing E1 byte-integrity exercise, T1/T2 query coverage, Q1 session matching, VQ2 quiet-query metadata, IM2 impact counts, preservation-state queue, R1–R16 source table or final worked results. This component adds a **purpose-and-field selection contract**, not another source authentication or hashing lesson.

> **Synthetic case boundary:** Harbor Library is fictional. Only R1–R8 were available at 09:05 and R9–R16 at the 09:20 Round B review. R17–R24 and all later W1, MQ3, P1/C1, V1, K1, Branch S/P and Chapter 4 cards are excluded from Round B. The independent MIN2 fixture below contains fabricated `Q11`/`Q12` booking references, `SYN-*` events and reserved `example.test` addresses. These are **not** canonical R-series observations or copies of real personally identifiable information.

# New Chapter 02 Teaching

### 2.M1 A complete source and a useful analyst view are not the same object

An incident investigation often needs enough information to distinguish competing explanations. That does not mean every analyst needs every field from an application export. A raw system record may contain account labels, booking identifiers, timestamps, request identifiers and additional contact information. Some fields could help answer the immediate incident question; others may reveal personal information unrelated to it.

The existing Chapter 02 already insists on bounded collection and trustworthy source provenance. It explains that byte-identical copies do not prove source completeness and that a quiet query cannot establish absence outside its envelope. This expansion asks a distinct question: **After an authorized source has been identified, which fields may a specific reviewing role receive for a specific question, and how can the transformed view remain reproducible without unnecessarily spreading unrelated information?**

Three objects should be distinguished:

- **Source record:** The original record or authorized copy from its named producer, with its actual selection and collection limits.
- **Working review view:** A derived selection of rows and columns created for a specific decision purpose. It may omit or mask fields, but it must be labeled as a transformation.
- **Decision statement:** The analyst's bounded conclusion drawn from that view, with references to the source or a custodian who can verify any omitted details.

A review view is not a more authentic original just because it looks tidy. It is an analytical product. If it hides a relevant source identifier, the reviewer may lose the ability to verify what was selected. If it exposes every available patron contact field, the team may exceed its stated purpose. Both are quality failures.

[NIST SP 800-122, *Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)*](https://csrc.nist.gov/pubs/sp/800/122/final) provides primary guidance on identifying and protecting PII according to risk and context. It is focused on U.S. federal agencies and does not establish the privacy law or authorization rules governing the fictional Harbor Library. The field-level exercise below is original CyberABC instructional material.

### 2.M2 Begin with a permitted decision question, not a list of available columns

Consider the question available at the 09:20 Round B review:

> "Which recorded operation concerning B19 should the application custodian investigate, and which available account/time identifiers could help test the approved-training explanation?"

This question may require a booking identifier, operation type, timestamp, account label, source name and record ID. It does **not** automatically require a patron's home address, email, telephone number, newsletter membership or unrelated reservations.

The decision purpose comes first. Then the analyst and custodian identify the minimum relevant sources, permitted rows and columns, approval and whether any sensitive field is truly necessary. The need for personal information may change if a different authorized question is posed—for example, notifying a person about a verified service consequence. That later purpose requires its own authority and evidence.

A weak collection plan says, "Export every user detail in case it becomes useful." This gives future unknown questions control over today's data exposure. A stronger plan identifies a current question and the specific fields that could discriminate among current hypotheses, with a way to request more through an authorized owner if the original selection proves insufficient.

The correct goal is **proportionate access without destroying legitimate investigative capability**. It is not simply making every exported file as small as possible. An underspecified view can falsely suggest that two events are unrelated because the join identifier was removed. Conversely, a broad export may include sensitive data with no decision value.

At rapid level, the student should state the question, list each requested field, describe its purpose and identify a permitted alternative if that field cannot be shared.

### 2.M3 Separate record selection from field projection

Two distinct filtering operations commonly occur when preparing evidence for review.

**Row selection** determines *which events or business objects* appear. A proposed Round B selection might concern B17–B19 over an approved interval, rather than every historical booking. The exact source and time filter must be documented. R15's deletion rule creates urgency, but does not specify a deadline anchor or authorize a broader export.

**Field projection** determines *which properties* of those selected rows appear in the working view. One reviewer may need event IDs, booking IDs, timestamps, operation names and account labels. A different role may need an aggregate service-status note rather than technical identifiers. Neither view is an original log.

Both transformations must be recorded. A view's reported row count is meaningless without the selection that produced it. A small number of rows may reflect a narrow scope, a data absence, a wrong filter or a broken collection path. Field projection cannot repair any of those problems.

The selection plan should name the producer, approved query interval, relevant account or booking filters, source clocks, collection/ingestion limitations, collector and reviewer roles. Chapter 02 already develops those concepts for R13/R14, VQ2 and T1/T2. This supplement adds a required second line: **Which exact columns are retained or withheld for the receiving analyst, and which original source custodian can recheck an omitted field if needed?**

A changed selection or projection produces a different analytical artifact and must be versioned, not silently substituted for the first output.

### 2.M4 The minimum view must still answer the question

Removing irrelevant data is valuable only if the remaining view can support a defensible conclusion. Suppose an analyst wants to associate an application change with a reported booking symptom. If the view removes the booking identifier, the analyst may not be able to connect the records. A row with only an operation and time can be insufficient, especially when multiple requests occurred nearby.

A **required correlation field** is a field necessary to compare the selected records under the approved method. Its presence does not make a correlation valid by itself. Two systems may use similarly named IDs with different namespaces or semantics. The existing Q1 laboratory demonstrates that an overlapping time window and account label can leave more than one candidate session. A privacy-aware view must not erase that uncertainty or use masking as an excuse to guess which session was involved.

An application-account label such as `desk-a` can itself be sensitive operational context. It may be appropriate for a restricted technical reviewer but unnecessary for a patron-facing message. The fact that a field is not a full legal name does not make it safe for unlimited distribution.

A field checklist therefore needs two explanations: **why retained** and **why not retained**. For example, keep a stable source event identifier so another reviewer can retrieve the correct raw row through an authorized custodian. Keep an operation type to distinguish edit from view. Omit a contact address if the current question does not need it. If a field's necessity is unknown, pause the release decision and ask the approving role rather than selecting it automatically.

### 2.M5 Pseudonymization is not the same as anonymity

Sometimes a team wants to replace a directly identifying value with a less revealing label. For example, a review table might use an internal case alias instead of a patron contact address, while a restricted custodian maintains the approved mapping. Such a transformation may reduce unnecessary exposure, but it does **not** establish that a person can no longer be identified.

A consistent alias may link a person's activities across multiple rows, even when the person's name is absent. Other available fields—time, booking pattern or account metadata—may allow association with a real individual when combined with additional sources. A pseudonym should therefore still be treated according to its remaining disclosure risks.

Nor is a cryptographic digest of a contact address necessarily an anonymous value. Predictable inputs may be guessable, a shared digest can link repeated activity, and any reversible mapping creates a reidentification route. It would be incorrect to say, "The email was hashed, so the export contains no sensitive data." A secure pseudonymization scheme, if needed, requires a separately approved design, key protection, access control and threat assessment, beyond this introductory exercise.

The MIN2 laboratory deliberately **omits** contact fields rather than generating pseudonyms. It checks that the intended reviewer receives only declared analysis columns and that the source retains its original teaching values unchanged. This is easier to audit and avoids suggesting a toy hashing operation can solve privacy risk.

Anonymity is a much stronger claim than "a visible name has been replaced." Nothing in this chapter's fixture establishes irreversible anonymity.

### 2.M6 Keep the original available under an appropriately controlled procedure

A bounded review view should not overwrite or replace the original record set. An analyst may need to verify whether a transformation omitted a relevant field or merged two events incorrectly. If the original was deleted, that review may no longer be possible.

For a real authorized collection, the relevant custodian should follow organizational retention, access, preservation and evidence-handling rules. The preservation may require restricted access to fields that are not distributed to every analyst. **Protecting the source and minimizing the working copy are complementary**, not contradictory, when they are each justified by their purpose and authority.

This does not mean preserving all personal data indefinitely. The original collection itself must be authorized and proportionate, and retention obligations depend on the organization's rules and applicable requirements. The book does not provide a general legal preservation order or permission to copy unrelated patron data.

In Chapter 02, the E1 exercise already distinguishes a synthetic transcription from an authenticated original and shows that matching SHA-256 values support limited byte consistency. A new working view should have a **transformation manifest** and source pointer; it cannot inherit authenticity merely because its source file had a digest check.

An effective manifest records: source identity, query selection, collection status, reviewer access scope, fields retained, fields deliberately omitted, transformation version, creator and creation time *if actually performed*, and the known limits. A planned transformation with no created output must remain **planned**, with no fabricated timestamp or digest.

### 2.M7 Privacy and investigative value can fail in opposite directions

A review view can fail through **excess** or **insufficiency**.

An excess-field failure occurs when the output includes contact information outside the approved purpose. The analyst may still be able to investigate, but the disclosure is broader than necessary. A missing-key failure occurs when the output omits the booking or event identifier needed for the intended comparison. This may appear more protective at first glance, but it can make the authorized review unreliable.

These failures do not cancel each other. One cannot justify unnecessary contact data simply because the view contains other useful columns. One cannot call an unusable view successful just because it exposes fewer fields.

A third failure occurs when the row filter expands beyond the approved objects. A view may have an entirely appropriate set of columns but include records for an unrelated booking. Field-level restrictions do not automatically justify overbroad row selection.

The negative controls in MIN2 test all three conditions separately: removing the required booking key, adding a contact field and including an unapproved booking ID. The program rejects each variant instead of quietly producing a wider or less useful view.

This is an original data-handling acceptance contract. It does not attempt to determine every possible category of personally identifiable information or replace a full privacy impact assessment.

### 2.M8 Contrastive worked example: "we have only the facts we need"

**Incorrect hypothetical assessment:**

> "For R9, export the full patron profile, all contact details and all newsletter fields. The analyst might need them later. After copying them, delete the original and keep only a masked table; the mask proves the evidence is anonymous and complete."

The first step lacks a specific decision purpose for unrelated contact data. The second risks destroying the source context and provenance. The third converts a superficial masking operation into unsupported claims of anonymity and source completeness. None of those steps is authorized by R9 or the Round B release.

**Defensible decision proposal:**

> "At 09:20, R9 reports a B19 booking edit, while R10–R13 provide limited training, patron-report, recollection and session context. The analyst requests that the application custodian confirm the approved source and select only the records and fields needed to investigate the B19 operation within a bounded interval. A technical review view may retain stable event/booking IDs, event time, operation and appropriate account context, while unnecessary patron contact details remain outside that view. The source and any transformation are preserved only according to the approved collection and access rules. No export or identity finding is claimed completed."

The proposal answers a specific question, names the custodian and leaves missing proof visible. It also prevents the opposite error: removing every identifier and then attributing events through timestamps alone.

### 2.M9 Release boundaries still govern restricted views

A projection cannot make later evidence available earlier. At the 09:05 Round A checkpoint, R9–R16 do not exist in the learner's released set, even though R9 reports an event at 09:03. A review view derived from R9 is therefore **not available** for the Round A decision.

At the 09:20 Round B checkpoint, R1–R16 are available as supplied synthetic cards. The learner can design an authorized review request but must not claim that a custodian delivered unprovided raw fields. R13 lacks device and location detail; privacy minimization does not entitle the learner to fill those fields with guesses. R14's query scope is incomplete; a nicely projected table cannot repair that coverage limitation.

R15 adds a separate urgency to determine source retention, but its 24-hour deletion rule lacks a documented anchor. No projection can compute a defensible exact deadline without that missing policy detail.

The MIN2 rows are exercise-only symbols. They are not the same as the original R-series booking values, and they cannot be used to assert how many Harbor Library patrons were affected. The IM2 exercise addresses a separate counting problem, with its own X-series data and limits; MIN2 addresses how a narrowly scoped *review view* should be constructed and rejected when its field or object policy is violated.

### 2.M10 Different reviewers should not automatically receive identical views

Operational teams contain distinct roles. A technical analyst investigating whether a booking edit and session event might be related may need an account label and source identifier. A service owner deciding whether booking state should be corrected may need booking IDs and approved targets. A communications contact preparing a patron-facing update may need a description of the service consequence, not an internal account name or raw contact list.

A single all-purpose export can encourage unnecessary forwarding between those roles. The better practice is to specify the receiving role and purpose before preparing the view, with explicit escalation when a reviewer needs more.

Do not treat role restriction as a replacement for source integrity. The service owner still needs valid authoritative booking data. The privacy contact may need to assess an allegation through a different approved process. A communications role's lack of raw data must not be "fixed" by inventing missing facts.

The fictional case does not define an organizational data-classification scheme or actual permissions. A course learner can design candidate views and approval questions while leaving operational implementation pending. It would be misleading to name a specific privacy law or notification threshold without the jurisdictional and organizational facts required.

### 2.M11 Source identifiers and account labels retain uncertainty

A source event identifier lets a reviewer ask a custodian for the precise original row. It does not by itself authenticate the producer or prove that the data were complete. A booking ID connects a review row with a business object under that source's semantics; it may not be globally unique across all environments or time periods.

Similarly, an account label says what the source attributed to an account or session context. It does not identify the human operator. In Harbor Library, `desk-a` is an account reference. The absence of device/location detail in R13 remains an unresolved question even if a derived view perfectly retains the account field.

These limits are important because a carefully minimized view may look authoritative. Exact row IDs, tidy column names and consistent aliases can make a table appear complete. A disciplined reviewer asks which producer emitted each field, whether the join identifiers are actually comparable, whether the source query covered the intended interval and what was omitted.

MIN2's `actor_account` column is therefore a fictional correlation candidate, not a human attribution result. Its inclusion is allowed only within the exercise's explicitly defined technical-review policy, not as permission to publish account details widely.

### 2.M12 Record transformation without pretending the source changed

A derived review view is not a modified original source; it is a new analytical artifact. A transformation log should allow another authorized reviewer to repeat the same row selection and field projection if the original is still available under the applicable retention rules.

For a small classroom review, record:

1. The permitted question and receiving role.
2. The approved booking/object scope.
3. The source record count and declared producer.
4. The exact fields retained and omitted.
5. Any normalization of timestamps or identifiers.
6. Whether the required correlation fields remain available.
7. The output row count and any errors.
8. The transformation code/version.
9. The result's limitations and who may resolve missing fields.
10. The fact that no real collection or release occurred.

A report saying only "personal details removed" omits too much. It does not identify which personal details, which source rows, which version or whether the transformed view can answer its intended question. A report saying "privacy protected" is even less testable.

The test should include negative cases. If the policy requires a booking ID and it is removed, the view must fail the task's acceptance condition. If a contact email is added, it must fail the field-minimization gate. If an unrelated booking is selected, it must fail the row-scope gate. Rejecting an unsafe requested view before producing it is a legitimate successful outcome for this exercise.

### 2.M13 An authorized extension is not automatic scope creep

Sometimes the initial view is genuinely insufficient. Perhaps an authorized investigator cannot distinguish two records without a session identifier held in a different source. The right response is not to silently broaden every analyst's access. The investigator should document which decision depends on the missing field, why the current view is insufficient, and which custodian and approver can evaluate a targeted extension.

Such a request may be granted, denied or returned for clarification. Any newly approved selection is a distinct transformation version with its own source and limits. An extension does not imply that the old view was dishonest or that the newly supplied data retroactively existed at an earlier checkpoint.

A useful stopping rule is: if the evidence required for a claim is not inside the authorized current view, **stop that claim** and request additional permission or mark it unresolved. Do not use a field guessed from context to fill a missing column. If the current question can already be answered under its limits, do not collect unrelated information merely to make the record larger.

A practical incident process balances confidentiality, integrity and availability of evidence. Preserving too little can prevent a needed investigation; distributing too much can create another exposure. A well-specified purpose and validation rule keeps both risks visible.

### 2.M14 Section synthesis: minimize the view without minimizing the truth

Evidence work needs two kinds of discipline at once. The source and its provenance must remain trustworthy and correctly scoped, while each review copy should contain only the information required for that receiver's approved question. Neither a complete original nor a minimal view automatically produces a correct causal conclusion.

For Harbor Library at 09:20, the right result is still a bounded investigation proposal, not a completed source export, a confirmed human actor or a population-wide impact count. MIN2 shows how a review can fail because it contains an unnecessary contact field, lacks a join identifier or reaches an unrelated booking.

The transferable beginner skill is to explain **what was included, what was omitted, why both choices matter, and what the reviewer still cannot establish**.

---

## MIN2 Offline Laboratory — Select a Review View Without Losing Correlation

**Status:** Entirely synthetic and isolated. MIN2 is not R1–R16, not a real patron export and not the earlier E1, Q1, VQ2 or IM2 fixture.

**Goal:** Produce only the approved minimal technical-review fields for an approved synthetic booking selection; reject a missing join field, unnecessary contact field and expanded object scope. Preserve the original artificial source rows unchanged.

**Environment:** Python 3 standard library, memory only; no files, external requests, accounts or production data.

**Input meaning:** `Q11` is the only approved booking ID in this exercise. The invented `patron_email` values use reserved `example.test` addresses. The `actor_account` field is a fictitious technical label, not a human identity. A `READY` label does not prove the source is authentic, the selection complete or the query authorized in a real setting.

### Executable Python code

~~~python
EVENTS = [
    {
        "event_id": "SYN-A", "booking_id": "Q11",
        "event_time": "09:03", "operation": "EDIT",
        "actor_account": "staff-x",
        "patron_email": "ava@example.test",
    },
    {
        "event_id": "SYN-B", "booking_id": "Q11",
        "event_time": "09:06", "operation": "VIEW",
        "actor_account": "staff-x",
        "patron_email": "ava@example.test",
    },
    {
        "event_id": "SYN-C", "booking_id": "Q12",
        "event_time": "09:08", "operation": "CANCEL",
        "actor_account": "staff-y",
        "patron_email": "bea@example.test",
    },
]

ALLOWED = {
    "event_id", "booking_id", "event_time",
    "operation", "actor_account",
}
SCOPE = {"Q11"}
REQUIRED = {"event_id", "booking_id", "event_time", "operation"}

def review(label, fields, bookings):
    if not bookings.issubset(SCOPE):
        print(f"{label}: REJECT_SCOPE selected=0")
        return

    extras = fields - ALLOWED
    if extras:
        print(f"{label}: REJECT_EXTRA_FIELD {','.join(sorted(extras))}")
        return

    missing = REQUIRED - fields
    if missing:
        print(f"{label}: REJECT_MISSING_KEY {','.join(sorted(missing))}")
        return

    subset = [
        {key: row[key] for key in sorted(fields)}
        for row in EVENTS
        if row["booking_id"] in bookings
    ]
    print(
        f"{label}: READY rows={len(subset)} "
        f"fields={','.join(sorted(fields))}"
    )
    print(
        f"{label}: bookings="
        f"{','.join(sorted({x['booking_id'] for x in subset}))}"
    )

review("MINIMAL", ALLOWED, {"Q11"})
review("DROP_BOOKING", ALLOWED - {"booking_id"}, {"Q11"})
review("ADD_EMAIL", ALLOWED | {"patron_email"}, {"Q11"})
review("EXPAND_SCOPE", ALLOWED, {"Q11", "Q12"})

print(
    "SOURCE_UNCHANGED:", len(EVENTS),
    "rows; sensitive field retained in synthetic source only"
)
assert len(EVENTS) == 3 and "patron_email" in EVENTS[0]
~~~

### Exact expected output — executed in Python 3

~~~text
MINIMAL: READY rows=2 fields=actor_account,booking_id,event_id,event_time,operation
MINIMAL: bookings=Q11
DROP_BOOKING: REJECT_MISSING_KEY booking_id
ADD_EMAIL: REJECT_EXTRA_FIELD patron_email
EXPAND_SCOPE: REJECT_SCOPE selected=0
SOURCE_UNCHANGED: 3 rows; sensitive field retained in synthetic source only
~~~

### Worked interpretation and negative controls

**MINIMAL** selects two records referencing the permitted synthetic booking Q11. It retains five declared technical-review fields and excludes the contact email. Its `READY` result means only that the field/object policy accepted the requested derived view.

**DROP_BOOKING** fails because removing `booking_id` destroys a required reference for the declared booking-level comparison. Removing more fields is not automatically better if the authorized task becomes impossible.

**ADD_EMAIL** fails because `patron_email` is outside the approved technical-review field set. The fact that the artificial source contains the value does not authorize its distribution to this review role.

**EXPAND_SCOPE** fails because Q12 is not one of the approved objects, even though all requested columns are individually permitted. Field minimization cannot repair an overbroad object selection.

**SOURCE_UNCHANGED** demonstrates that the derived projections did not delete the original teaching field. In a real process, the original would still require its own collection and retention authority; preserving a synthetic in-memory source is not a production custody demonstration.

A crucial limitation is that the code's `ALLOWED` and `SCOPE` sets are **invented input policies**, not permissions obtained from a real organization. The function does not verify source origin, consent, legal basis, logging completeness, identity or whether the view's fields are factually correct. It avoids publishing the fake contact values in the output, but that is not a formal anonymization guarantee.

**Learner submission:** The six output lines, a table classifying the three rejected variants, a proposed transformation manifest and a two-sentence explanation of why the canonical R9/R13 evidence does not supply any real patron-contact collection or attribution proof.

**Assessment:** A full result predicts and reproduces all six lines, distinguishes row scope from column projection, maintains a necessary booking join key, rejects unneeded sensitive fields and states that the source and receipt status remain separate. No network or actual personal data is involved.

---

## Targeted Existing-Exercise Refinements — Keep Original IDs

Keep all existing Chapter 02 exercise IDs and its 0–2 rubric. These four refinements complement the present E1, VQ2, IM2 and source/custody questions, without adding new numbered exercises.

### EX018 — Retention decision and field scope

**Additional task:** Alongside the P-A and P-B proposed requests, identify the specific columns necessary for the next decision and a category of source field that should **not** automatically be distributed to the technical reviewer. Distinguish retention of a permitted source object from permission to distribute every column. Preserve the existing R15 unknown policy anchor and proposal-versus-collection states.

**For full credit:** The request names the business purpose, source selection, custodians, approving role and restricted reviewer scope. No completed export or broad personal-data permission is invented.

### EX019 — Collection note for a transformed review view

**Additional task:** Keep E1's original provenance and state requirements. Add a separate *planned derivative manifest*: original source pointer, approved row interval/objects, fields retained, fields excluded, transformation version and intended recipient. Do not reuse E1's digest as if it authenticated new derived bytes; compute a new digest only if a local file was actually created and measured.

**For full credit:** Source and derived views are explicitly distinguished, and no collection/creation time or digest is fabricated. The original E1 transcript and its existing instructions remain unchanged.

### EX020 — Hash claim and confidentiality

**Additional task:** Keep the existing five-row supported/unsupported hash-claim table. Add one sentence explaining why equal digests of a source copy do not authorize sharing the source's personal fields with a broader team, and why a projected view requires its own recorded transformation and limits.

**For full credit:** Byte consistency remains separate from source authenticity, completeness, permission and confidentiality. No statement that masking or hashing makes information automatically anonymous is accepted.

### EX023 — Impact check and purpose-limited evidence

**Additional task:** Add a field-by-field justification for a proposed restricted booking-impact comparison. Distinguish what the analyst needs to classify a selected booking discrepancy from any contact details needed for separate patron communication. The latter require a different permitted purpose and must not be silently included in the technical comparison.

**For full credit:** The learner still defines the measurement unit and selected frame as taught in IM2, keeps unverified rows visible and does not infer affected people from ticket count or claim a completed comparison from R1–R16.

---

## Supplementary Worked Answers — Final Principal-Book Appendix Placement

### EX018 — Additional worked reasoning

At 09:20, P-A can be proposed to the application custodian for a bounded booking-audit selection relevant to B17–B19 and R14's source-coverage question, while P-B can ask the identity custodian about available session detail under separate approval. A technical review may need source event ID, booking ID, event time, operation type and an appropriate account/session pointer. It does not automatically need a patron contact address, newsletter membership or unrelated booking records. R15 reports a 24-hour deletion policy but not its anchor or exact deadline. Source preservation, requested field selection, reviewer access and actual collection require distinct statuses and authority. No completed export or active retention hold is supplied.

### EX019 — Additional worked reasoning

The original E1 collection note describes a **synthetic transcription** and distinguishes a planned local exercise from a file actually created by the learner. A separate review-view manifest would record the original E1/book source pointer, bounded permitted rows, retained fields, excluded fields, intended analyst role, transformation method and its version. If no derived file was made, the creation time, location and digest remain **not applicable**. If a local file was produced, record its actual creation time and compute its own measured digest if required; the original E1 digest does not attest changed bytes. The derivative remains a working selection, not an authenticated production export or evidence of source completeness.

### EX020 — Additional worked reasoning

Matching E1 SHA-256 values at two actual checks support only a bounded consistency claim about the **specified copied bytes** and method. They do not show that the source was complete, correctly timed, lawfully collected or authorized for broader distribution. A technical reviewer may need a derived view with unnecessary contact fields excluded. The view's field policy, row scope and transformation receipt must be recorded separately from the raw copy's integrity comparison. Neither redaction nor a digest establishes anonymization or human attribution; those require their own substantiation.

### EX023 — Additional worked reasoning

For a bounded booking-impact comparison, the learner should identify the selected booking IDs, source audit pointer, appropriate event interval, current authoritative value, approved target/version, comparison outcome and uncertainty. The permitted analyst view should not automatically include patron email, unrelated newsletter data or additional bookings. A service owner may separately authorize a communications workflow if verified consequences require reaching affected patrons, but that purpose does not retroactively expand the technical review. The canonical R1–R16 set supplies no completed authoritative impact comparison or measured affected-person count. MIN2's Q11/Q12 rows are an independent fictional field-selection exercise and cannot be used to claim an additional Harbor Library mismatch.

---

## Synthesis, Navigation and Primary Sources

A defensible evidence workflow distinguishes **an authorized source**, **a purpose-limited derivative view**, and **a bounded conclusion**. Reviewers need enough identifying fields to reproduce the permitted comparison, but they should not receive unrelated personal data simply because the source contains it. A minimal view that removes a required join key can fail the investigation, while an overly broad view can fail the confidentiality objective. Neither deficiency should be hidden.

At the 09:20 Harbor Library checkpoint, R9–R16 support proposing limited authorized checks, not claiming real collections, reconstructed identities or impacts. MIN2 supplies no canonical incident observation.

### Continue studying — chapter 02 of 04 (public supplementary draft)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Course chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03) · [Worked results](../MANUSCRIPT.md#answers)

**Editorial status:** This is a transient **public component** of the single English principal book. It does not create new exercise IDs or satisfy the final A4, review or source-rights gates.

### Primary sources

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025: risk-managed incident response, coordination and analysis.
- [NIST SP 800-122 — Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)](https://csrc.nist.gov/pubs/sp/800/122/final), final April 2010: context-sensitive identification and protection of PII; scope primarily U.S. federal systems.
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final), final August 2006: source-aware evidence handling guidance and limitations.

All MIN2 records, field-selection policies, code and outputs are original **synthetic teaching material**, not facts authenticated by NIST or evidence collected from a real library. Editorial responsibility belongs exclusively to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer material follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE), subject to third-party rights. No external system is queried, no communication is sent, and no real personal data is accessed.
