# Incident Response and Cyber Resilience — Rapid Course

## Chapter 02 Transitional Expansion Draft: Confirming a Source Preservation Hold

**Editorial status:** **Public transitional English instructional component** of Chapter 02 of the **single principal book**. It is not a fifth chapter, a completed volume, a forensic certification, or a record of a real preservation action.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 02 — Alert triage and evidence preservation](../MANUSCRIPT.md#ch-02).  
**Specific learning gap:** Demonstrate a reviewable **source-retention hold lifecycle** that separates requesting, approving, applying, verifying, reviewing, releasing and expiring a hold, while keeping original-source retention separate from a copied item's retention and without assuming the anchor of R15's 24-hour rule.  
**Preserve the existing chapter:** Sections 2.3 and 2.8, P-A/P-B, E1, T1/T2, VQ2, Q1, MIN2, IM2 and the existing EX014–EX026 exercises and final answers. The new **H2** lab tests a different question: whether a claimed hold has the right source/scope, a reported application, a bounded effect check and a lifecycle record.

> **Source and chronological boundaries:** Harbor Library is fictional. The learner has only R1–R8 at the Round A 09:05 checkpoint; R9–R16 are released in Round B at 09:20; R17–R24 and every later Branch S/P, P1/C1, V1, W1 or MQ3 card are excluded from Round B. The H2 dates, identifiers, oldest-row marker and source-protection checks are **independent invented laboratory data**, not facts discovered about Harbor Library. Neither a retention hold, a completed source copy nor a source deletion event is present in canonical R1–R16.

# Chapter 02 — New Teaching

### 2.H1 A request to preserve data is not the preservation itself

A responder may correctly recognize that useful source records could disappear. They can write an urgent, well-scoped request, obtain a decision from an accountable person and contact the custodian. None of those steps alone establishes that the underlying source has changed its deletion behavior.

This distinction is particularly important when a source's normal retention policy is short. In the fictional Harbor Library case, R15 reports that detailed booking-audit records are deleted after **24 hours unless an authorized copy is retained**. R15 does not say whether the period begins at event time, ingestion time, storage time or another policy anchor. It also does not say that a source-level pause of deletion exists, is enabled, or has been requested. A responder must not add 24 hours to R9's 09:03 event time and publish an exact deletion deadline.

A **preservation request** asks that specified information be protected under the applicable authority and scope. A **source hold**—if supported by a particular system and authorized by the organization—changes or constrains the source's normal removal process for defined objects or intervals. A **collected copy** is an independently identified object held under its own access and retention rules. These are different things, even when the same custodial team manages them.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), especially RS.AN-06 and RS.AN-07, addresses records of investigative actions and the integrity, provenance, collection and retention of incident data. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) describes source-aware collection and preservation from an IT incident-response perspective, not as a legal preservation order. The specific hold lifecycle below is an **original CyberABC teaching model**; the cited sources do not prescribe its exact fields or claim that Harbor Library has such a capability.

### 2.H2 Separate three objects that may be confused

A useful incident note keeps three inventories rather than one ambiguous entry named "evidence saved":

| Object | What it represents | What a positive entry does not prove |
|---|---|---|
| Source record set | Events or data still maintained by the producing system or its governed storage layer | That the events are complete, correct, or immune to every deletion path |
| Source-hold control | A particular mechanism reported as protecting a defined source, selection and time interval | That all records existed before activation, or that the hold covers an unrelated source |
| Collected evidence copy | Bytes, export or image separately preserved at a specified location | That the source's normal deletion was stopped, or that no source row was omitted |

Suppose an authorized copy contains one booking-audit row and a SHA-256 digest matches at two checks. That may support a limited **byte-consistency** claim about the saved copy. It says nothing about whether the original application-audit source is still deleting rows. It also does not show that the copy contains every relevant source event.

Conversely, a confirmed source hold might keep selected records available without authorizing a broad export to the analyst. The custodian still needs permission, source-specific selection and a separate release or transfer procedure before supplying a copy. Protecting a source and collecting a reviewer copy can be complementary, but neither substitutes for the other.

The existing E1 laboratory teaches a digest-based check on a synthetic transcription; MIN2 teaches a restricted working view. H2 does not repeat either. It asks whether the *claimed source-level preservation effect* was actually checked and what remains unproven even after a narrow positive check.

### 2.H3 Start with a decision question for P-A and P-B

At 09:20, the learner can propose two separate information paths. **P-A** concerns booking/application audit data relevant to the B19 edit and the limits of R14's earlier quiet-query summary. **P-B** concerns possible identity details that could clarify whether a session relationship is worth investigating. Their evidence value, custodians, privacy limits and loss concerns differ.

P-A is time-sensitive because R15 describes deletion of detailed booking-audit records after an unspecified 24-hour anchor. P-B may also be urgent, but the canonical record gives **no identity-source retention period**. An analyst should seek P-B availability information in parallel rather than borrow P-A's 24-hour rule and apply it to the identity service.

A proposed P-A preservation card should name which *particular source* is at risk. R9 is characterized as booking audit, while R14 is an application-audit summary. These labels must not be silently merged into one producer, one retention clock or one hold-control namespace. The custodian should confirm whether a mechanism applies to each and whether a separate request or receipt is needed.

The current investigation question might be: "Can we preserve the permitted detailed records needed to assess the B19 operation and its surrounding booking edits before the relevant source becomes unavailable?" A second, separate question asks whether limited identity details can be obtained with appropriate authority. Neither question requires collecting every patron or identity record.

The state of both P-A and P-B at the supplied Round B checkpoint is **proposed**. This supplement does not create a fictitious canonical approval or hold to move either card into a completed state.

### 2.H4 Define source-hold coverage as a contract, not a title

A ticket titled "hold B19 logs" is insufficient to know what would be protected. The receiving custodian needs an unambiguous control target and an authorized selection. A reviewable request should cover at least:

1. **Case and purpose:** Which decision may depend on these records?
2. **Producing source:** Exact storage/service and log or data collection identity, not merely "the logs".
3. **Objects:** Booking IDs, event types or other identifiers within permitted scope.
4. **Time selection:** Begin/end and the field used to interpret time, including whether endpoints are inclusive or exclusive.
5. **Authority:** Who approved the hold request and under which organizational procedure and applicable restrictions?
6. **Custodian:** Who can confirm the source's retention implementation and preserve any permitted copy?
7. **Timing:** Requested start, reported effective start, permitted duration or review date, and any separate operational deadline.
8. **Intended mechanism and effect:** Which deletion or retention operation should be constrained for the defined selection?
9. **Verification:** What non-destructive source/control observations can challenge the claim that the hold is effective?
10. **Unresolved limits:** Existing gaps, unprotected sources, unknown clock anchor and any unavailable oldest relevant row.

The field list is a **teaching contract**, not a legal specification or a promise that every logging system supports object-level holds. Some systems may offer retention settings, export-to-protected-storage workflows, snapshot protection or other mechanisms. They have different semantics, and a team must use the actual organization's approved procedures.

A hold on `booking-audit` is not necessarily a hold on `application-audit` or `identity-detail`. A hold covering 09:10–09:35 cannot establish coverage of a requested 09:00–09:30 interval. A hold covering one booking ID cannot establish coverage of every named object. Scope must be compared, not assumed from the presence of a control identifier.

### 2.H5 Approval and application produce different receipts

Suppose the fictional incident lead approves a P-A request to preserve a narrow source interval. The approval should name exactly what may be preserved and who will carry out the work. It does **not** establish that the custodian enabled a protective mechanism, or that the source supports one.

For a proposed operational workflow, use four initial receipt stages:

**Requested.** A bounded card exists. Its time and source show what was asked for, not that anyone agreed.

**Approved.** A responsible authority grants the defined operation and scope. The authorization may have restrictions, a deadline and a valid decision identifier. An approval for booking audit is not transferable to identity detail.

**Application reported.** The custodian records the applied control or other approved protective action, its target, time, identifier and intended behavior. This is an *operator or system report*, not an independently tested effect.

**Effect checked.** A reviewer assesses the reported source/control state and a bounded source-availability check against the approved selection. The result may support a limited effect claim if the method and sources are credible.

A custodian message saying "done" should therefore be followed by precise questions: done on which producer and collection, for which objects and time interval, using which control identifier, with what reported effective and review times? A positive receipt from the wrong source remains irrelevant to the requested one.

The H2 script models these conditions as structured artificial fields. In a real case, a Boolean `approved=True` would not authenticate an actual person's decision. The team needs organizationally valid decision evidence and source-provided receipts, protected according to the applicable access and retention rules.

### 2.H6 Verify an effect without running an unsafe deletion test

A retention hold is often intended to prevent loss of data. It might appear that the simplest test is to try deleting a protected record. That can be unsafe, destructive, unauthorized or misleading. **This course performs no deletion and does not recommend testing a real hold by deleting incident evidence.**

For a preparation or incident review, the team can instead define **non-destructive** observations approved by the owner and custodian. Examples may include a governed control-status read, an audit entry recording the control's application, confirmation that the relevant retention/deletion job recognizes the protected selection, and a read-only retrieval of a known source row expected to exist.

The quality of those observations depends on what the actual source exposes. A dashboard saying "hold active" could be stale, refer to the wrong collection or omit a secondary deletion path. A successful retrieval of one older row proves that one row was accessible at that check time; it does not prove that all requested records are protected indefinitely.

A meaningful verification report should state the **source and scope checked**, who performed the check, the time and method, the recorded response, which expected row or control state was examined, and what could still invalidate the result.

The H2 fixture uses synthetic flags for an "effect check" and an "oldest relevant row." Those are declarations inside a lab, not independent proof. The lab's strongest result is explicitly called **bounded source hold confirmed in fixture**, never "all deletion stopped in Harbor Library."

### 2.H7 The oldest requested row is a critical but limited sentinel

Why check an older row at all? If the request is intended to protect records already near a retention boundary, inspecting only a recent event may give false reassurance. A source might retain new rows while the oldest relevant data have already been removed.

The custodian should help identify a legitimate **sentinel**: a record expected to exist in the requested interval, with an identifiable source pointer and safe retrieval path. The analyst should not fabricate a row solely to make the test pass. An expected oldest row may be determined from a known record inventory, a reliable prior observation or another authorized source, subject to appropriate validation.

If the oldest relevant item cannot be retrieved, several explanations remain possible. It may have expired *before* the hold became effective; the source may never have generated it; a filter or index may exclude it; the request may target the wrong producer; or the hold may not cover it. The correct state is **unverified coverage of that oldest item**, not automatic proof of malicious deletion or proof that every part of the hold failed.

A custodian should document whether the row existed at the intended source before the request, the retrieval selection used, which storage tier was searched, and whether any source-internal transition occurred between application and check. If the cause cannot be resolved, the hold's claimed historical coverage must remain limited.

A future source-preservation mechanism cannot retroactively recreate data already removed. The team may consider authorized alternate sources or copies, but any resulting reconstruction must be documented separately from the original source hold.

### 2.H8 A hold can be valid now yet have a finite term

A source-protection mechanism may have a defined duration, expiration condition or required review. The record should separate:

- **Requested effective time**: when the incident lead wanted protection.
- **Reported activation time**: when the custodian says the mechanism became effective.
- **Verified check time**: when a bounded source/control observation was actually made.
- **Review-due time**: when the accountable owner must reconsider the need, scope or continuation.
- **End of the stated protection term**: when the recorded authorization or technical term no longer supports an active-hold claim.
- **Release time**: when an authorized release action was recorded, if one occurred.

A stated review date is not always the same as automatic technical expiry. A platform may continue enforcement after an administrative review is overdue, or may terminate enforcement at a lease boundary. The semantics depend on the source and control. The course must not invent them.

In H2, the independent fixture provides a technical `term_end`. If the lab's check time is later than that term, the program returns **TERM_EXPIRED_EFFECT_UNKNOWN**. It does not assert that a row was deleted or that deletion resumed immediately. Actual post-term source behavior requires its own authorized observation.

A valid hold receipt also should say what happens if review cannot be completed. A safe plan may require escalation before expiration, a separately approved renewal, or continuing safeguards as defined by the actual policy. The analyst cannot assume that a prior approval renews itself.

### 2.H9 Release and expiration must not erase the earlier lifecycle

An important archival principle applies even after the preservation reason has ended: **historical decisions and receipts should remain reviewable within the organization's authorized recordkeeping rules**. Closing the active hold state is not permission to rewrite its earlier existence.

A source-hold ledger can therefore append lifecycle entries such as requested, approved, application reported, effect checked, review due, renewed, release approved, release reported, release checked, or term-expired status recorded. Each entry should include the responsible role, event time, source and control identifier, and a reason or decision reference where appropriate.

Do not silently overwrite an earlier `ACTIVE` value with `RELEASED` if doing so destroys information about when protection was reported and what was tested before release. Keep a current summary *and* the historical transitions.

A release receipt is another distinct operational event. Someone may approve the release, the custodian may report that the mechanism was removed, and a reviewer may need to confirm the current source/control state. The release should not be tested by deleting evidence in an unauthorized manner.

The H2 laboratory appends a fictitious `RELEASE_RECORDED` entry while retaining all earlier entries. The result is **RELEASE_RECORDED_RECHECK_REQUIRED**, deliberately avoiding the stronger claim that every deletion behavior after release was measured. The lab performs **no deletion or modification of a source**.

### 2.H10 The copy remains governed separately after a source hold ends

A particular collected copy may remain subject to the organization's evidence-retention rules after a source hold is released. Conversely, a copy may have its own permitted deletion or access conditions while a source-level hold remains active. Those are separate governance and custody decisions.

Consider two fictional ledger objects:

- `source_control_id` records a hold applied to a particular source/interval, with reported activation, review and release states.
- `copy_item_id` records a collected export's identifier, collector, creation time, stored bytes, integrity checks, access owner and copy-retention policy.

They should not share one ambiguous status. A checked digest for `copy_item_id` supports a limited byte-consistency statement, but not a source-control effect. A source-control status does not automatically authorize broad distribution of `copy_item_id` to analysts.

The current book already discusses source/copy/interpretation and a minimized technical-review view. H2 contributes the **lifecycle linkage**: a hold record can point to a separately authorized copy without becoming that copy, and release of one should not silently alter the other's governance.

The AR1 authority-readiness exercise in Chapter 1 may help identify a valid approver under a separate pre-incident process. It does **not** replace the case-specific approval required for P-A or P-B; nor does it provide evidence that a hold was applied during Round B.

### 2.H11 Custodian unavailable: treat nonresponse as an escalation condition

A time-sensitive request may reach an organizational mailbox while the responsible custodian is unavailable. The responder must distinguish a **dispatch attempt**, an acknowledgement by a role, a custodian's confirmation of applicability and an actual application/effect receipt.

If the custodian has not responded, the hold remains **not confirmed**. The incident lead can use the organization's approved escalation route to seek an available, authorized custodian or service owner, explain the potential loss path and preserve existing permitted records. The team must not assume that leaving a voicemail, opening a ticket or copying a supervisor creates an active source hold.

The current R15 notice increases the importance of prompt clarification, but it does not supply a verified countdown from the 09:03 R9 event. A blocked request should record the absence of the custodian, time of attempts, what was asked, any ticket/reference, known evidence already at risk, next authorized contact and next review.

The analyst must not bypass source access controls or execute retention changes using unapproved credentials. An emergency retention procedure, if one exists in a real organization, requires its own documented permission boundary and receipt. This introductory exercise invents no such power.

The H2 `CUSTODIAN_UNAVAILABLE` negative case returns that status rather than fabricating application or verification. It does not prove records were lost or that the custodian was negligent.

### 2.H12 Contrastive example — a wrong "hold complete" message

**Incorrect synthetic Round B conclusion:**

> "R15 says the logs last 24 hours, so the B19 row will disappear at 09:03 tomorrow. P-A has been entered as urgent and someone copied R9 into a text file. The source hold is therefore active, all relevant booking logs are safe, and P-B identity data are covered by the same hold."

Every promotion of evidence in this statement is invalid. The retention anchor is unspecified; a ticket priority does not apply a control; a copy of one item does not stop source deletion; source coverage for all booking records has not been verified; and P-B is a different source with no supplied retention policy or hold receipt.

A source reviewer cannot repair the conclusion by calculating a different timestamp. The missing information is *semantic*: the policy anchor, actual custody/implementation path, scope and effect of a control, and whether the oldest relevant row remains available.

A valid next step would identify the bounded P-A source request, obtain an accountable decision, ask the custodian which mechanism if any can protect it, and document only the receipts actually returned. P-B proceeds as a separate availability inquiry with its own owner and scope.

### 2.H13 Correct example — a complete but explicitly hypothetical hold receipt

**Entirely invented H2 rehearsal, not a Harbor Library event.** On the artificial date 2040-03-15, a team prepares a request for two artificial booking-audit items, `BX-01` and `BX-02`, over an event-time interval from 09:00 inclusive to 09:30 exclusive.

A fictional incident lead is represented as having approved the request at 09:36. The specified application custodian reports applying a source-hold control at 09:40 to `booking-audit-sim` covering those two objects and an enclosing 08:55–09:35 interval. The declared technical term extends to 11:30, with a separate owner review to be scheduled under the teaching contract. At 10:00, a synthetic check reports that the relevant source-protection state was observed and that the expected oldest marker was retrievable in the selected toy source.

A careful fictional conclusion is:

> "Within this bounded independent fixture, the named source-control receipt covers the requested objects and event interval, has the expected custodian and a reported activation, and the declared non-destructive check at 10:00 found the oldest marker available. The check supports only the specified source/objects and observed time. It does not prove that all earlier records existed, that every deletion mechanism is constrained, that any real system was held, or that the separate copy's retention was verified."

This positive example includes source, objects, interval, authority, custodian, effective time, limited term, check method and remaining uncertainty. It is correct because its claims stay within the fictitious evidence contract.

A different result is just as educational. If the receipt covers `identity-detail-sim` instead of `booking-audit-sim`, the program refuses source coverage even if every other field looks valid. If the oldest row cannot be retrieved, the team must investigate historical coverage rather than silently mark the hold complete. If the hold term has elapsed, the earlier positive check cannot establish continued current protection.

### 2.H14 A review decision must be different from a routine expiry

At a stated review time, the owner may decide to maintain, narrow, extend, release or escalate the hold under the organization's actual policy and legal requirements. The custodian may have technical facts about control capabilities, but those facts do not automatically grant authority to make a broader business or legal preservation decision.

A renewal should receive a new recorded decision and control confirmation. It should identify whether the original mechanism continued uninterrupted or whether a gap occurred; the earlier control ID and the new decision ID should both remain in the lifecycle. "Renewed" written in a case note does not prove a platform configuration changed.

A release decision should identify the rationale and responsible authority, the affected source and objects, any continuing preservation obligation, the custodian's reported action and the post-release verification status where applicable. It also must avoid treating source-release permission as permission to delete a separately collected copy.

An expiry record may be derived from comparing time with a declared technical term, but **expiration of a term is not direct observation of actual deletion**. A system could continue retaining data, apply a broader policy or have already lost historical rows. The correct state in an unverified source is "term expired; current effect unknown."

These distinctions make handoffs safer. The next analyst can see which source was protected during what interval, which claims were actually verified, and which new authorization is required before the team changes a preservation control.

### 2.H15 Two different negative source outcomes

A source hold can fail acceptance in at least two important ways:

**Control-path problem.** The requested source or interval is not protected by the reported control, the custodian is wrong, or the application/effect receipt is missing. Here the team should correct the control request or seek a valid custodian explanation, then repeat an authorized non-destructive check.

**Historical-source problem.** The control appears correctly scoped for current protection, but the oldest expected row is absent. Here the team must determine whether the row ever existed at that source, whether it was already removed before application, whether the retrieval path is incomplete, or whether another storage tier is relevant. It cannot conclude immediately that the hold mechanism failed for all future records.

A third category is **unknown coverage**: the source does not expose enough status or row-level evidence to demonstrate the intended protection. In that case the reviewer can report that the custodian's statement was recorded but effect remains unverified, rather than replacing missing proof with an optimistic assumption.

These outcomes are different from VQ2. VQ2 concerns whether a query result supports a claim about event coverage under filters and ingestion watermark. H2 concerns whether an **authorized preservation control** was applied to the intended source and selection, with a reviewable lifecycle. A valid hold does not make a poorly scoped query complete; a valid query does not make a source hold effective.

### 2.H16 Section synthesis — preserve the source, the copy and the decision trail separately

The learner should finish with three defensible habits. First, name the source, authorized objects and interval precisely enough that a custodian can say what is and is not protected. Second, separate requested, approved, applied and verified states, and use non-destructive source observations to bound any effect claim. Third, keep a versioned or append-only lifecycle through review, expiry and release without erasing earlier decisions or equating a protected copy with protected source retention.

For Harbor Library at 09:20, **P-A and P-B remain proposed**. R15 leaves the exact deletion anchor unknown. No fictional H2 positive result, expiry or release may be imported into R1–R16. The pending task is to obtain an authorized, narrowly scoped custodian clarification and document whatever the real source could verify under its actual procedures.

---

## H2 Offline Laboratory — Hold Lifecycle and Source-Coverage Gate

**Environment:** Python 3 standard library, entirely in memory. No file creation, network access, credentials, data collection, retention-setting changes, destructive probes or deletion.  
**Fixture classification:** A separate artificial 2040-03-15 scenario; the source names `booking-audit-sim` and `identity-detail-sim`, objects `BX-01`/`BX-02` and hold receipts are invented. They are **not** R-series records or real P-A/P-B execution evidence.  
**Goal:** Decide whether a described source hold has sufficient **bounded** simulated source/custodian/scope/effect evidence, and refuse broader conclusions when a required step is missing or a term has elapsed.

### Assumptions and observations to predict

A request covers two artificial records in the interval `09:00 ≤ event < 09:30 UTC`. An invented approving role has accepted its scoped source, and the invented application custodian reports applying a control at 09:40 that covers 08:55–09:35. The fixture checks state at 10:00 with an artificial effect-check flag and oldest-row availability flag. Its reported technical term ends at 11:30.

The program verifies *declared consistency* and prints a reason when it refuses acceptance. The Boolean fields are invented teaching assertions, not authenticated approval, actual source protection or proof of deletion prevention.

### Complete Python 3 program

~~~python
from copy import deepcopy
from datetime import datetime

def utc(value):
    return datetime.fromisoformat(
        f"2040-03-15T{value}:00+00:00"
    )

REQUEST = {
    "source": "booking-audit-sim",
    "objects": {"BX-01", "BX-02"},
    "interval": (utc("09:00"), utc("09:30")),
    "custodian": "AppCustodian",
}
RECEIPT = {
    "source": "booking-audit-sim",
    "objects": {"BX-01", "BX-02"},
    "interval": (utc("08:55"), utc("09:35")),
    "custodian": "AppCustodian",
    "active_from": utc("09:40"),
    "term_end": utc("11:30"),
}
BASE = {
    "request": REQUEST,
    "approved": True,
    "approval_source": "booking-audit-sim",
    "receipt": RECEIPT,
    "custodian_available": True,
    "effect_checked": True,
    "oldest_retrievable": True,
    "as_of": utc("10:00"),
    "history": (
        ("REQUESTED", "09:34"),
        ("APPROVED", "09:36"),
        ("APPLIED_REPORTED", "09:40"),
        ("EFFECT_CHECKED", "10:00"),
    ),
    "copy_retained": False,
}

def status(s):
    req, rec = s["request"], s["receipt"]

    if not s["approved"]:
        return "PROPOSED_ONLY"
    if s["approval_source"] != req["source"]:
        return "APPROVAL_NOT_FOR_SOURCE"
    if not s["custodian_available"]:
        return "CUSTODIAN_UNAVAILABLE"
    if rec is None:
        return "APPROVED_APPLICATION_UNCONFIRMED"
    if rec["source"] != req["source"]:
        return "WRONG_SOURCE"
    if rec["custodian"] != req["custodian"]:
        return "WRONG_CUSTODIAN"
    if (
        not req["objects"].issubset(rec["objects"])
        or rec["interval"][0] > req["interval"][0]
        or rec["interval"][1] < req["interval"][1]
    ):
        return "SCOPE_GAP"
    if s["as_of"] < rec["active_from"]:
        return "NOT_YET_ACTIVE"

    # Preserve earlier steps; a release is an appended event.
    if "RELEASE_RECORDED" in [
        kind for kind, _ in s["history"]
    ]:
        return "RELEASE_RECORDED_RECHECK_REQUIRED"
    if s["as_of"] >= rec["term_end"]:
        return "TERM_EXPIRED_EFFECT_UNKNOWN"
    if not s["effect_checked"]:
        return "EFFECT_NOT_VERIFIED"
    if not s["oldest_retrievable"]:
        return "OLDEST_ROW_UNAVAILABLE"

    return "BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE"

def variant(changes):
    row = deepcopy(BASE)
    row.update(changes)
    return row

CASES = [
    ("VALID_BOUND", {}),
    ("PROPOSED_ONLY", {"approved": False, "receipt": None}),
    ("APPROVED_NO_APPLY", {"receipt": None}),
    (
        "COPY_ONLY",
        {"approved": False, "receipt": None,
         "copy_retained": True},
    ),
    (
        "APPROVAL_WRONG_SOURCE",
        {"approval_source": "identity-detail-sim"},
    ),
    (
        "RECEIPT_WRONG_SOURCE",
        {"receipt": {
            **RECEIPT, "source": "identity-detail-sim"
        }},
    ),
    (
        "RECEIPT_SCOPE_GAP",
        {"receipt": {
            **RECEIPT, "objects": {"BX-01"}
        }},
    ),
    (
        "WRONG_CUSTODIAN",
        {"receipt": {
            **RECEIPT, "custodian": "OtherCustodian"
        }},
    ),
    (
        "CUSTODIAN_UNAVAILABLE",
        {"custodian_available": False},
    ),
    (
        "OLDEST_MISSING",
        {"oldest_retrievable": False},
    ),
    (
        "NO_EFFECT_PROBE",
        {"effect_checked": False},
    ),
    (
        "NOT_YET_ACTIVE",
        {"as_of": utc("09:38")},
    ),
    (
        "TERM_EXPIRED",
        {"as_of": utc("11:45")},
    ),
    (
        "RECEIPT_WINDOW_GAP",
        {"receipt": {
            **RECEIPT,
            "interval": (utc("09:10"), utc("09:35"))
        }},
    ),
    (
        "RELEASE_RECORDED",
        {
            "as_of": utc("10:15"),
            "history": BASE["history"] + (
                ("RELEASE_RECORDED", "10:05"),
            ),
        },
    ),
]

for label, changes in CASES:
    print(f"{label}: {status(variant(changes))}")

print(
    "HISTORY_RELEASE:",
    " -> ".join(
        kind for kind, _ in CASES[-1][1]["history"]
    ),
)

assert (
    status(variant({}))
    == "BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE"
)
assert (
    status(variant(CASES[-1][1]))
    == "RELEASE_RECORDED_RECHECK_REQUIRED"
)
~~~

### Exact expected output — executed in Python 3

~~~text
VALID_BOUND: BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE
PROPOSED_ONLY: PROPOSED_ONLY
APPROVED_NO_APPLY: APPROVED_APPLICATION_UNCONFIRMED
COPY_ONLY: PROPOSED_ONLY
APPROVAL_WRONG_SOURCE: APPROVAL_NOT_FOR_SOURCE
RECEIPT_WRONG_SOURCE: WRONG_SOURCE
RECEIPT_SCOPE_GAP: SCOPE_GAP
WRONG_CUSTODIAN: WRONG_CUSTODIAN
CUSTODIAN_UNAVAILABLE: CUSTODIAN_UNAVAILABLE
OLDEST_MISSING: OLDEST_ROW_UNAVAILABLE
NO_EFFECT_PROBE: EFFECT_NOT_VERIFIED
NOT_YET_ACTIVE: NOT_YET_ACTIVE
TERM_EXPIRED: TERM_EXPIRED_EFFECT_UNKNOWN
RECEIPT_WINDOW_GAP: SCOPE_GAP
RELEASE_RECORDED: RELEASE_RECORDED_RECHECK_REQUIRED
HISTORY_RELEASE: REQUESTED -> APPROVED -> APPLIED_REPORTED -> EFFECT_CHECKED -> RELEASE_RECORDED
~~~

### Why the result is deliberately bounded

**VALID_BOUND** is a consistency pass **within the invented fields** only. The script does not prove that any real deletion mechanism was configured or that every source row remains available. **PROPOSED_ONLY**, **APPROVED_NO_APPLY** and **COPY_ONLY** separate a request, approval lacking application evidence and preservation of a different copy; none establishes source protection.

**APPROVAL_WRONG_SOURCE**, **RECEIPT_WRONG_SOURCE**, **RECEIPT_SCOPE_GAP**, **RECEIPT_WINDOW_GAP** and **WRONG_CUSTODIAN** demonstrate distinct identity or coverage mismatches. The checker refuses the path rather than silently broadening scope.

**CUSTODIAN_UNAVAILABLE** means no valid custodian confirmation is available under that scenario, not that a breach occurred or data were lost. **OLDEST_MISSING** flags an unverified historical-coverage question: perhaps the row was already absent or a retrieval filter failed; the script cannot identify why. **NO_EFFECT_PROBE** states that a reported application alone is not a verified effect.

**NOT_YET_ACTIVE** rejects using a future control start as proof of present protection. **TERM_EXPIRED** records the end of the stated technical term without claiming actual source deletion. **RELEASE_RECORDED** leaves the earlier lifecycle steps intact and calls for a separately authorized state check. The final printed sequence is an **append-only teaching history**, not a reconstructed real audit trail.

**Important model limitations:** The fixture checks only the first applicable problem; multiple defects could coexist. An `effect_checked=True` flag does not authenticate a source query or independent protection test. A single oldest-row retrieval does not prove every applicable retention path is stopped. The code does not test actual custody, authority, legal duties, privacy rules, control-status provenance or source completeness; no delete request occurs. The H2 event times and source IDs do not belong to Harbor Library's canonical Round B.

**Required learner artifacts:** Reproduce all sixteen output lines; create a scenario table with the first blocking condition and a safe next request; identify why `COPY_ONLY` does not establish source hold and why `OLDEST_MISSING` does not prove deletion timing; propose a reviewer check for release and expiry that does not erase history or delete data.

**Five-point assessment for this unnumbered lab:** One point each for exact output, correct source/object/interval coverage reasoning, separation of copy from source control, correct treatment of unavailable custodian or oldest row, and expiry/release history with explicit effect limits. The lab is supplemental and adds **no new EX identifier**.

---

## Practical Two-Role Activity — Custodian Packet and Independent Hold Review

**Purpose:** Demonstrate that a second person can distinguish a requested, approved, applied and verified source hold **without relying on the packet author's explanation**.

**Roles:** **Custodian / Packet Author** and **Independent Reviewer**. The incident-lead approval is represented only by a fictional classroom request card. There is no real source custodian, logging system or deletion mechanism involved.

### Step 1 — Freeze the source-hold request

The packet author creates `H2-request-v1` with the fictional source, object IDs, time interval, purpose, proposed approval, custodian, requested hold mechanism, earliest relevant row and expected review terms. Mark the actual custodian acknowledgement, control identifier, effect check and observed oldest-row state **not supplied** until the artificial receipt card is given.

Keep a separate copy-item card, if using one, with its own retention and integrity fields. Do not allow a saved copy to change the source-hold status.

### Step 2 — Prepare and freeze one simulated custodian response

Choose either the valid H2 fixture, the wrong-source fixture or the oldest-missing fixture. The author records which source was reported protected, scope, application time, technical term, control identifier if supplied, check response and which fields remain missing. Save the immutable draft as `H2-custodian-v1`.

The reviewer must not see the author's private reasoning or a corrected answer. The packet may include explicit approved source pointers and the relevant original teaching rules.

### Step 3 — Independent review with no author assistance

The reviewer receives the two frozen cards and must answer:

1. What was **requested**, and was the request approved for that exact source and selection?
2. Which source, objects and interval did the custodian **report** protecting?
3. Does the receipt identify the appropriate custodial role, activation time, duration or review condition?
4. Which **non-destructive** effect observation is provided, and which expected oldest source row was or was not retrieved?
5. Is the current state confirmed for this narrow scope, merely reported, unverified, expired, released, or awaiting escalation?
6. What is the safest next **authorized request**, and what claim remains unsupported?
7. Is there a separately retained copy, and why does it not settle the source-hold question?

The reviewer saves `H2-review-v1` before discussion. Missing fields must remain missing. The reviewer should not claim that a source was deleted or that a hold succeeded solely because the author used reassuring wording.

### Step 4 — Evaluate, then correct with a new version

Compare the frozen response with the request and receipt. Identify whether a discrepancy came from the packet's missing field, the reviewer's interpretation, or an unavailable custodian/source. Retain the original versions. If a change is needed, write `H2-request-v2` or `H2-custodian-v2` and run another separately marked review; do not rewrite the first attempt.

**Pass:** The reviewer locates the source/scope, distinguishes proposed/approved/applied/verified states, recognizes the meaning of the oldest-item check, does not calculate a deadline from R15's unknown anchor, and chooses a safe hold/escalation or recheck.

**Critical fail:** The reviewer calls a proposed request an active hold, treats a copy as evidence that deletion stopped, accepts a wrong-source/wrong-object receipt, assumes an absent oldest row was deleted at an invented time, or authorizes an intrusive test without permission.

**Limit:** This tabletop and the Python output measure only consistency and independent reasoning on synthetic records. They do not prove organizational readiness, actual source preservation, legal compliance or completion of any Harbor Library case action.

---

## Targeted Refinements of Existing Exercises — EX018, EX019, EX022 and EX024

Preserve the original exercise IDs and formats. The current Chapter 02 has thirteen numbered exercises (EX014–EX026); the additions below deepen **four existing exercises** without creating new IDs or changing their 0–2 score rules.

### EX018 — Retention decision

**Additional teaching check:** Keep the original **three-row P-A request** and **two-row P-A/P-B comparison**. Add to the existing custodian-question field the exact source-hold receipt requirements: source namespace, approved booking/object IDs, event interval/time semantics, accountable authority, custodian, reported activation, review/expiry terms, observed effect and an explicit limit. State that a missing oldest requested row requires investigation rather than a fabricated expiry. Do not change P-A or P-B from **proposed** merely because H2 contains a positive artificial run.

**Full credit:** The request remains a proposed authorized next step at 09:20, the R15 policy anchor remains unknown, the P-B retention rule remains unspecified, and neither a source hold nor a copy is claimed performed.

### EX019 — Collection note

**Additional teaching check:** Preserve the original **collection-note table** for E1 and its actual-versus-planned status. Add a **separate named source-hold ledger reference** with its own proposal, authority, reported control, effect check and release/expiry fields. If no source hold was executed, mark these fields **not applicable or not supplied**, rather than repeating E1's copy hash as proof of source preservation.

**Full credit:** Source-control lifecycle and copied-item custody are distinct. The original E1 byte/transformation and access limits remain as written; no source hold, collection time or digest is fabricated.

### EX022 — Handoff

**Additional teaching check:** Preserve the **five-sentence maximum** at 09:20, with case ID, two evidence IDs, competing hypotheses, uncertainty, a proposed authorized next action, owner and 09:35 or earlier review. Within those sentences, say whether P-A/P-B are merely **proposed** and whether there is any confirmed source-hold effect. Do not insert H2's simulated positive result or later R17–R24 evidence.

**Full credit:** The handoff gives a second analyst a clear request to the custodian about the R15 policy anchor and source-hold feasibility, without claiming a completed hold or an exact deletion instant.

### EX024 — Escalation threshold

**Additional teaching check:** Preserve the existing **two hypothetical observation/response pairs**. One trigger may now be a **future custodian-confirmed preservation failure or inability to retrieve the oldest relevant item**, provided it states how the source and selection would be checked, why the risk of evidence loss changes, and which approved escalation route is followed. The other trigger should continue to address verified continuing booking harm or a separate impact signal. Neither trigger may be reported as observed within R1–R16.

**Full credit:** A source-hold failure trigger is distinct from confirmed malicious activity or proven deletion. The incident lead coordinates an authorized preservation alternative, not an automatic disruptive action.

---

## Supplementary Worked Answers — For the Principal Book's Final Appendix

### EX018 — Additional worked reasoning

At 09:20, the P-A card can request an authorized, bounded check of relevant **booking-audit and application-audit sources**, explicitly distinguishing their producers and retention semantics. The three-row table asks (1) which source and interval are involved; (2) what starts R15's 24-hour policy clock and whether the oldest needed row is still retrievable; and (3) who approves, applies, verifies and stores any authorized copy or source control. An effective source-hold receipt, if the custodian later supplies one, would identify its source, object set, interval, authority, custodian, reported start, term/review, effect observation and limit. The P-A/P-B comparison retains separate custodians and unknown P-B retention. **Both requests remain proposed in R1–R16**. The isolated H2 result does not prove Harbor Library preserved any data, and a missing oldest row would require source-coverage investigation, not a fabricated deletion time.

### EX019 — Additional worked reasoning

E1 is a synthetic transcription whose actual local creation time and measured digest belong in the collection note only if the learner actually generated the file. A **separate source-hold ledger reference** could identify a planned control for a named audit producer and record status as *not supplied* because no actual source hold is in the canonical Round B evidence. If a later fictional custodian response were provided, it would require its own control identifier, applicable authority, scope, reported activation, non-destructive check and release/review fields. The E1 digest supports limited consistency of E1's saved bytes; it cannot establish that the underlying source stopped deleting records. A source-hold release entry and a collected-copy retention decision remain different records. The original E1 table format and its source/copy distinctions must be preserved.

### EX022 — Additional five-sentence worked handoff

> At 09:20 UTC, HL-IR-001 concerns Harbor Library room bookings: R9 reports a B19 edit, R10's supplied training plan omits B19, and R11 records a patron concern. Authorized training outside the listed tasks and use of the account beyond approved scope remain competing explanations; R13 lacks details needed for human attribution. R14 provides only a bounded quiet-query summary, while R15 states a 24-hour deletion policy for detailed booking audit whose starting anchor and oldest-row availability remain unknown. The incident lead **proposes** that the application custodian confirm P-A's source, hold or copy feasibility and retention semantics, with P-B identity-detail availability separately proposed; no production copy, source hold or account restriction is established. Review with the incident lead at 09:35 UTC or earlier if a verified new edit or source-loss warning requires a fresh decision.

The five sentences remain an **internal handoff**, not a claim of completed collection. The proposal does not assume a hold mechanism exists or borrow H2's fictional positive status.

### EX024 — Additional worked reasoning

A valid hypothetical preservation trigger is a **later custodian-confirmed failure to protect the specifically requested source or to retrieve the oldest expected row** after an appropriately scoped, authorized check. The application custodian and incident lead verify the source, selection, check time and whether missingness may reflect prior expiry, wrong source or incomplete retrieval; the incident lead promptly considers approved alternative preservation or escalation. That trigger increases urgency and uncertainty about evidence availability, but does not by itself prove a malicious deletion or account compromise. A second trigger can remain a verified new unexplained booking edit or an owner-confirmed harmful mismatch, which brings the service and identity owners into a separate containment decision. **Neither future observation is contained in R1–R16**. Source hold, business harm and attribution must not be conflated.

---

## Synthesis, Navigation and Official Sources

The most important distinction is: **requested is not approved, approved is not applied, applied is not independently verified, a verified narrow hold is not complete source coverage, and a retained copy is not a source hold**. Every stage needs a scoped record and the next accountable person. Unavailable custodians, missing oldest data, expired terms and releases should create traceable limitations and review actions, never fictional evidence or silent deletion.

### Continue studying — chapter 02 of 04 (public supplementary draft)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Course chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03) · [Principal book and worked results](../MANUSCRIPT.md#answers)

**Editorial integration note:** This is a transitional public component of the **one principal English book**. Accepted teaching, the H2 laboratory and the four existing-exercise refinements should be consolidated into `MANUSCRIPT.md` by the maintainer after review. This document creates no new numbered exercise or course skill, does not update A4 page measurement and does not declare completion.

### Primary official sources

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025. Its RS.AN-06 and RS.AN-07 recommendations concern recording investigation actions and collecting/preserving incident data and provenance under organizational policies.
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final), final August 2006. It presents source identification, acquisition planning, collection and integrity validation from an IT perspective; it is not all-inclusive forensic or legal advice.
- [NIST SP 800-92 — Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final), final September 2006. It supplies general principles for logging infrastructures, storage and retention. Its age limits any assumption that it specifies modern source-specific hold controls.

These works support general incident evidence-handling and log-management principles; **none prescribes the H2 simulator, establishes a legal hold, or authenticates the fictional Harbor Library records**. The text, examples, Python script, checks and fixture outputs are original synthetic educational material, not copied source prose. Editorial responsibility belongs solely to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned content follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within the stated limits; third-party works retain their rights. No source deletion, log manipulation or real-system access is performed.
