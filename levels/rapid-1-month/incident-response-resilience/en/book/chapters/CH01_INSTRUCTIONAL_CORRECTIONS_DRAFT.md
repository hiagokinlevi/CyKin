# Chapter 01 — Targeted Instructional Corrections (English, Transitional Draft)

**Status:** Public **transitional editorial component** of [Chapter 01](../MANUSCRIPT.md#ch-01) of the single principal English Rapid Incident Response book. This is **not** another chapter, an independent book or a completed technical review.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Source manuscript examined:** Chapter 01 and final worked results EX001–EX013, at the current public edition preceding this correction proposal.  
**Integration rule:** Make only the identified replacements or insertions in the one `MANUSCRIPT.md`. Retain all 13 exercise IDs and required formats. Keep the canonical 09:05 decision strictly within R1–R8, and keep BSL1, PATH1 and AR1 separately labeled as independent teaching fixtures.

## Correction 01 — Source selection in §1.4, “Write scope as an executable boundary”

**Placement:** Replace the paragraph that begins “Suppose a learner wants more device details than R8 contains.” Do not alter the subsequent paragraph explaining why R8 cannot establish the absence of data transfer.

**Replacement teaching text:**

Suppose a learner wants to investigate the device or sign-in origin associated with the reported `desk-a` authentication in **R1**. R1 identifies a successful account sign-in but does not supply a verified device, source-network context or human identity. The correct classroom step is to **propose** an authorization-bound question: “Identity administrator: if separately approved, identify the narrow sign-in source, interval, relevant device or session fields, their producer and timezone, and the method needed to preserve and verify those details.” The learner cannot perform that collection from the supplied R1–R8 table, and cannot access a real identity system on the strength of a classroom exercise. R8 is a **different source**: it is a network summary whose missing **destination detail** prevents a supported statement about data transfer. Device/session context for R1 and destination evidence missing from R8 must not be treated as the same field or the same custodial request.

**Expected interpretation:** An analyst may draft two separately scoped requests with different decision purposes, but the Round A case contains neither requested result. This change corrects the record-to-source mapping without adding R9+ or making an identity finding.

---

## Correction 02 — AR1: bind the simulated decision receipt to the precise request

**Placement:** In §1.3b, **after** the existing complete AR1 Python 3 listing and its fifteen baseline outputs, insert the explanation and supplementary code below. In the final appendix, append the four-line result and interpretation **within** “Chapter 1 AR1 offline laboratory — worked result,” without creating a new numbered exercise or changing the original fifteen baseline lines. The code is an **add-on**: run the published AR1 program first in the same isolated Python 3 session, then the supplementary listing.

### The missing guard and why it matters

The existing AR1 program correctly models the governed register's revocation flag, nonempty object scope, valid delegates, permitted custodian and approved confirmation channel. Its fifteen published results reproduce correctly. However, the core `evaluate` function tests whether a simulated approval item **exists**; it does not test whether the **issuing decision record** binds that item to the *specific* request identifier, operation, source and set of objects.

For example, the original `BASE` proposal requests `TR-01` and includes a fictional generic receipt named `SIM-RECEIPT`. If the request is changed to another otherwise allowed object, `TR-02`, while the same receipt is reused, the original function returns `REHEARSAL_PATH_VALID_NOT_EXECUTED`. This is a **reproducible limitation of the toy validator**. It is not evidence that a real organization approved the second object.

The pre-incident governance lesson should not call that second request approved. The simulated approval record must be associated with a stable request identifier **and** its approved operation, resource, objects and role. The following supplementary check introduces a small, independent *fictional issuer-side record* that the requester cannot silently redefine inside the evaluated card. It does not provide real identity authentication, a digital signature or a valid production permission.

### Supplementary AR1 Python 3 listing — run after the existing complete AR1 program

~~~python
# These are invented issuer-side approval records for the classroom.
# The original AR1 program must have been executed first, so BASE,
# PAUSE, RULES, REGISTRY and evaluate are already defined.
SIMULATED_ISSUED_APPROVALS = {
    ("TRAIN-001", "incident_lead"): (
        "lead-sim", "SIM-RECEIPT",
        "collect_training_audit", "training-audit",
        frozenset({"TR-01"})
    ),
    ("PAUSE-001", "incident_lead"): (
        "lead-sim", "SIM-RECEIPT",
        "pause_staff_writes", "staff-write-route",
        frozenset({"staff-write-route"})
    ),
    ("PAUSE-001", "service_owner"): (
        "alternate-sim", "SIM-RECEIPT",
        "pause_staff_writes", "staff-write-route",
        frozenset({"staff-write-route"})
    ),
}

def evaluate_with_approval_binding(card):
    preliminary = evaluate(card)
    if preliminary != "REHEARSAL_PATH_VALID_NOT_EXECUTED":
        return preliminary

    for role in RULES[card["operation"]]["roles"]:
        item = card["approvals"][role]
        presented = (
            item["principal"], item["receipt"],
            card["operation"], card["resource"],
            frozenset(card["objects"])
        )
        issued = SIMULATED_ISSUED_APPROVALS.get(
            (card.get("request_id"), role)
        )
        if presented != issued:
            return "HOLD_RECEIPT_SCOPE_MISMATCH"
    return preliminary

valid_audit = {**BASE, "request_id": "TRAIN-001"}
valid_pause = {**PAUSE, "request_id": "PAUSE-001"}

reused_receipt = {
    **valid_audit, "objects": {"TR-02"}
}
wrong_reference = {
    **valid_audit, "request_id": "PAUSE-001"
}

for name, card in (
    ("REQUEST_SCOPED_TR01", valid_audit),
    ("REQUEST_SCOPED_PAUSE", valid_pause),
    ("REUSED_RECEIPT_TR02", reused_receipt),
    ("REUSED_REQUEST_ID", wrong_reference),
):
    print(name, evaluate_with_approval_binding(card))

assert (
    evaluate_with_approval_binding(valid_audit)
    == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
)
assert (
    evaluate_with_approval_binding(valid_pause)
    == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
)
assert (
    evaluate_with_approval_binding(reused_receipt)
    == "HOLD_RECEIPT_SCOPE_MISMATCH"
)
assert (
    evaluate_with_approval_binding(wrong_reference)
    == "HOLD_RECEIPT_SCOPE_MISMATCH"
)
~~~

### Exact supplementary output — executed with Python 3

~~~text
REQUEST_SCOPED_TR01 REHEARSAL_PATH_VALID_NOT_EXECUTED
REQUEST_SCOPED_PAUSE REHEARSAL_PATH_VALID_NOT_EXECUTED
REUSED_RECEIPT_TR02 HOLD_RECEIPT_SCOPE_MISMATCH
REUSED_REQUEST_ID HOLD_RECEIPT_SCOPE_MISMATCH
~~~

### Worked explanation

`REQUEST_SCOPED_TR01` and `REQUEST_SCOPED_PAUSE` match their separate invented issuance records. `REUSED_RECEIPT_TR02` changes the object from TR-01 to TR-02, retaining the previously issued classroom receipt; the request remains within the *general* allowed source set, but this **specific approval was not issued for that object**. `REUSED_REQUEST_ID` substitutes a request identifier belonging to a different operation, so the purported approval record cannot match.

This is a **second-layer check**: a full positive teaching result should require both the original role/delegation route check and the request-bound issuance check. The original fifteen outputs remain correct **for what their original program actually checks**; they do not establish this additional property. The issuer records are hardcoded fictional premises; a production design would need an authenticated, governed issuer source and protection against forgery, replay and unauthorized modification. No action is performed by either program.

**Review stop condition:** If a role, receipt or request binding cannot be authenticated in real response work, withhold execution and follow the organization's current authorization/escalation procedure. A teaching-only valid route does not become permission to collect data or change a service.

---

## Correction 03 — EX001 input boundary and four-column worked result

**Placement A — EX001 exercise prompt:** Keep the original four statements, four rows, categories and 0–2 rubric. Replace **only** its input sentence:

> **Inputs:** R1, R3, R4, R5 and R7, all within the R1–R8 Round A release at 09:05. These are the exact source pointers used to examine the four listed statements; do not use R9 or any later case result.

The present prompt lists only R4, R5 and R7, while its worked answer cites R1 and R3 to discuss the compromise hypothesis. Including those two already-released records makes the prompt and gabarito traceable without changing the decision time or the statements.

**Placement B — final “EX001 — Worked result”:** Replace the present three-column table with the four-column table below. The text after the table may retain its valid observation-versus-inference explanation.

| Statement | Classification | Supporting supplied record(s) | Limit — one sentence |
|---|---|---|---|
| (a) “R4 records a cancellation of B18” | Direct observation **of record content** | R4, 08:44 UTC, application log | The row reports cancellation but does not demonstrate why it was authorized or whether a later patron view was correct. |
| (b) “`desk-a` was compromised” | Hypothesis requiring confirmation; **unsupported if asserted as a confirmed finding** | R1 reports an account sign-in, and R3–R4 report booking edits | Those records do not establish unauthorized control, a human actor, intent or a completed compromise investigation. |
| (c) “R5 reports that B18 disappeared” | Direct observation **of a patron report** | R5, 08:48 UTC, help desk | The report is evidence of what was reported, not an independent authoritative booking-state comparison. |
| (d) “R7 proves the service can be restored in ten minutes” | Unsupported conclusion | R7, 08:52 UTC, backup monitor | A completed backup job is not an isolated restore, an elapsed recovery measurement or accepted service correctness. |

**Assessment boundary:** Four rows and **four distinct columns** now correspond to the original required statement, classification, source and one-sentence limit. A defensible two-point answer identifies that (b) is a live hypothesis *but not an established finding*.

---

## Correction 04 — EX003 worked dependency card needs explicit falsifiers

**Placement:** Replace **only the primary table** in “EX003 — Worked result” with the two-row, five-field version below. Keep the original exercise's two-dependency requirement, 0–2 rubric, existing PATH1 extension and explanatory paragraphs where they are not redundant.

| Dependency | Possible user-facing harm | Supplied Round A pointer | Missing discriminator and a negative result that would weaken the concern | Permitted custodian / requesting authority |
|---|---|---|---|---|
| Staff identity service | Unexpected use of a staff account might enable inappropriate booking changes; continuing misuse is unverified. | R1 account sign-in and R2 dashboard access; R3–R4 are recorded edits, not human-attribution proof. | A bounded, approved identity/session-context check might show expected account circumstances; that would weaken one hypothesis of unexpected access **without identifying the human operator or validating each edit's authorization**. | Identity administrator supplies only permitted detail after incident-lead approval; the analyst requests, not collects unilaterally. |
| Reservation database and current booking state | Residents could be shown incorrect room availability or an unsuitable assignment. | R3–R4 report edits and R5 reports a patron concern; no present-state comparison is provided. | An owner-approved comparison that matches the authoritative current B17/B18 values and patron display to the approved target would weaken a **selected state-discrepancy hypothesis**, without proving all rooms or users unaffected. | Service owner approves the target and comparison; application/data custodian supplies a bounded authorized view. |

**Teaching note:** A negative result must challenge a *specified hypothesis in its tested scope*. Neither a routine-looking sign-in nor a selected matching booking establishes the full case cause or population impact. The improved card preserves **two rows**, supplies the missing falsifier and separates the custodian from the missing evidence.

---

## Correction 05 — EX012 decision-record execution state

**Placement:** In “EX012 — Worked result,” retain its existing decision-log table and fields. Replace the **Time and action** and **Approver and executor** model entries only; do not add rows.

| Decision-log field | Corrected model entry |
|---|---|
| Time and action | **09:05 UTC:** the fictional incident lead approves a bounded **classroom-only** copy of synthetic R1–R5. **Actual local-copy execution: not evidenced in the model answer.** A question to the training/service owner about B17/B18 authorization is **proposed; response pending**. |
| Approver and executor | **Approver:** fictional incident lead, for the stated classroom scope only. **Prospective executor:** learner analyst; mark `not performed` until the learner actually creates a local copy and records its true creation time, artifact and scope. The training owner has **not** yet answered the question. |

**Reason for precision:** The existing table states that the analyst “prepares the copy,” which could be misread as completed collection, while its later explanation correctly distinguishes permission from actual local execution. The revised table makes that separation visible **at the first point the model answer is read**. It changes no synthetic R-series event or incident authority.

---

## Correction 06 — EX013 measurable readiness ticket with a real deadline field

**Placement:** Keep the original **three-row gap register** and the exercise's objective, inputs and 0–2 rubric unchanged. Replace the **Priority ticket** and **Verification drill** explanatory paragraph in the “EX013 — Worked result” with the following complete model ticket. The subsequent AR1 extension may remain as additional reasoning.

### Model ticket — verify the owner-and-alternate authority route

| Ticket field | Training model entry |
|---|---|
| Gap | The case-opening materials do not confirm the current service-owner/alternate authority route for a disruptive booking decision. |
| Priority rationale | An unverified approver or expired alternate could delay a necessary decision or induce an unauthorized interruption; this is a **preparedness weakness**, not an observed incident failure. |
| Accountable owner | Fictional incident lead coordinates; designated register steward and service manager own the governed appointment record. |
| Specific change | Publish and review a **versioned governed** role/alternate record with operation/object scope, delegation issuer, validity, revocation, custodian and approved confirmation route. |
| Proposed training deadline | **2026-10-25 UTC**, subject to explicit service-manager acceptance; a real organization's deadline must come from its own plan, not from NIST or this fiction. |
| Positive rehearsal | A current correctly scoped primary or delegated route yields only a fictional **path-valid, not-executed** result. The independent reviewer can reconstruct the decision from the frozen register/request. |
| Negative rehearsal | Expired/revoked delegate, wrong approver, missing receipt or expanded object scope produces **hold**, with a named approved escalation path; no source change or production control is executed. |
| Retained acceptance evidence | Register edition/issuer, frozen request and reviewer response, input/result transcript, review date, named reviewer and any observed limitation. |
| Failure and reopen condition | If an invalid route passes, a valid route cannot be reconstructed, or the tested governing edition changes, leave or reopen the ticket for steward correction and a separately versioned retest. |

**Acceptance:** A reviewed register document **alone** does not close the ticket; the independent positive and negative rehearsal must be reproducible and the responsible owner must accept the observed result. The proposed due date is explicitly a synthetic ticket target, not a fact from R1–R8. A learner may choose a different justified gap from the original three-row register, but must supply the same accountable, measurable change and test logic.

---

## Section Summary and Navigation

The corrections above preserve the chapter's central model: **observed record content is not proof of actor or cause; proposed authority is not real execution; source/copy readiness is not restored business service; and isolated variants are not canonical incident facts**. The four original Python programs' published outputs remain unchanged, and the additional AR1 check strengthens the link between a specific simulated request and its simulated issuer-side decision.

### Continue studying — chapter 01 of 04 (transitional corrections)

[← Course home](../../../README.md) · [Course chapter index](../../SUBJECTS.md) · [Chapter 02 →](../MANUSCRIPT.md#ch-02) · [Chapter 01 principal text](../MANUSCRIPT.md#ch-01) · [Worked answers](../MANUSCRIPT.md#answers)

### Official primary sources and provenance

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025; §2.2–2.3 discusses incident response roles, authorities, policies and procedures in organizational context. NIST does **not** prescribe the exact four-verb CyberABC record or the AR1 simulated approval-binding rule.
- [NIST SP 800-84 — Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final), final September 2006; supports preparation and evaluation of exercises, **not** the particular AR1 scenario IDs or sample deadline.
- [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024; provides high-level governance outcomes and flexibility, **not** a Harbor Library delegation policy.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final), final December 2016; provides recovery planning context but does **not** establish that R7's backup job was a successful restore.

All Harbor Library references, proposed correction examples, AR1 issuance records, receipt strings, dates and expected code results are **original synthetic educational content**. No source here verifies a real human identity, approval, source collection, booking state, transfer or recovery. Editorial responsibility belongs exclusively to [hiagokinlevi](https://github.com/hiagokinlevi). The maintainer's original contributions follow [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within the published limits; third-party source rights remain unaffected. This component is not a book-approval certificate, an A4 verification, or an instruction to act on real systems.
