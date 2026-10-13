These outcomes are different from VQ2. VQ2 concerns whether a query result supports a claim about event coverage under filters and ingestion watermark. HOLD2 concerns whether an **authorized preservation control** was applied to the intended source and selection, with a reviewable lifecycle. A valid hold does not make a poorly scoped query complete; a valid query does not make a source hold effective.

<a id="ir-rapid-ch02-hold2-binding"></a>

#### 2.8a.15a Accept a linked evidence chain, not a collection of reassuring fields

A positive result needs more than a source name and several true flags. It needs agreement between the **request**, the **permission actually granted**, the **reported control**, and the **observation used to assess that control**. The purpose of this check is not to add paperwork: it is to prevent a valid receipt for one operation from answering a different question.

Start with three boundaries. The **requested scope** contains the records needed for the decision. The **reported coverage** describes the objects and event interval the custodian says the control covers. The **authorized scope** is the maximum selection the approving role permitted. For this exercise, require requested scope to fit inside reported coverage, and reported coverage to fit inside authorized scope. Check source, objects and time interval separately. Covering every requested object is not sufficient if the reported operation also includes an unapproved object.

In HOLD2, the requested event window is 09:00–09:30, while the reported control covers 08:55–09:35. The larger interval can be acceptable **only with permission for that larger selection**. The revised fixture supplies an explicit, invented authorization for 08:55–09:35 and BX-01/BX-02. This is additional classroom metadata, not a newly discovered Harbor Library approval. Expanding the receipt to 08:50 or adding BX-99 exceeds that permission even though the original requested records would still be covered. An empty request is rejected: mathematically, an empty set fits inside any set, but it cannot establish which evidence a preservation decision intended to protect.

Next bind the identifiers. The authorization and control receipt both name `HOLD2-REQ-01`; the recorded effect check names `HOLD2-CTRL-01` and the same source. An approval for `OTHER-REQUEST` cannot be reused merely because its source name looks familiar. A result for another control cannot establish this control's effect. These comparisons detect declared inconsistencies; they cannot authenticate the issuer, prevent a forger from changing every field consistently, or establish that the named role was truly appointed.

Then inspect the **meaning and order of lifecycle steps**, not just whether their timestamps increase. The modeled path is request, approval, application reported and effect checked, optionally followed by release recorded. A timestamp-sorted list containing only REQUESTED is not a completed lifecycle. Nor is request, application, approval, check a valid prior-approval path simply because the timestamps increase. Under this fixture's single-application contract, the approval time must agree with its history entry, and the receipt's activation time must agree with APPLIED_REPORTED. A missing step remains missing; do not manufacture a receipt to make the sequence pass. Systems with renewals, multiple applications or different reporting-time semantics need a different documented model.

Finally, identify the observation. `BX-01` is the **declared sentinel** for this exercise; retrieving BX-02 does not answer whether BX-01 remains available. Its selection as the oldest relevant marker is a supplied teaching premise, not something the program derives from a complete source inventory. Even a correctly bound retrieval establishes only that the selected marker was reported accessible at the recorded check. It does not demonstrate that every deletion path is constrained, every historical row existed, or every relevant object remains present.

| Review question | Specific check in the fixture | What remains unproved |
|---|---|---|
| Was this selection permitted? | Requested scope fits reported coverage, which fits the named authorization; role and operation agree | Authentic issuance, current organizational authority and real platform permissions |
| Do the receipts describe one operation? | Request IDs, source, control ID and modeled lifecycle agree | Whether an authentic operator actually performed it |
| Was this the intended observation? | Effect source/control and declared sentinel match | Source completeness, a real protection mechanism or the reason for an absent row |
| Does a later review establish present protection? | `as_of` bounds available history and checks the stated term | Continued effectiveness since the last observation |

`as_of` is an **information cutoff**, not a new observation. Moving it from 10:00 to 10:15 without new source evidence does not create a fresh 10:15 effect check. At the exact 11:30 term boundary, the active-term claim ends under this fixture's exclusive-end convention; the result says that current effect is unknown, not that data were deleted. A recorded release likewise requires a new authorized state check. This program records release history but does not authenticate release permission or perform release; it cannot certify that a release was lawful or technically effective.

These checks implement an original CyberABC teaching contract. [NIST SP 800-61 Rev. 3, RS.AN-06 and RS.AN-07, page 29](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf#page=37) supports recording investigative actions, safeguarding provenance and integrity, and collecting and retaining evidence under organizational procedures. It does not prescribe these identifiers, set comparisons, time limits or result labels. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) also expressly limits its forensic guidance: it is not an all-inclusive investigation procedure or legal advice.

**Apply the reasoning before running Python.** For EX018, keep the three-row P-A request and two-row P-A/P-B comparison; use their existing authority and receipt fields to ask for a request-bound permission, the permitted selection and the matching application/effect record. For EX019, keep E1's collection note separate from any source-control reference. For EX022, retain the five-sentence handoff and its proposed status. For EX024, keep two hypothetical trigger/response pairs: an inconsistent receipt calls for clarification and a new authorized review, not automatic containment or proof of deletion. All unprovided P-A/P-B details remain pending at 09:20. No HOLD2 identifier, timestamp or passing run belongs in R1–R16.

#### 2.8a.16 Section synthesis — preserve the source, the copy and the decision trail separately

The learner should finish with three defensible habits. First, name the source, authorized objects and interval precisely enough that a custodian can say what is and is not protected. Second, separate requested, approved, applied and verified states, and use non-destructive source observations to bound any effect claim. Third, keep a versioned or append-only lifecycle through review, expiry and release without erasing earlier decisions or equating a protected copy with protected source retention.

#### Complete Python 3 program

**Execution contract:** Run this whole listing in a fresh Python 3 session, not after another laboratory that reuses `BASE` or `utc`. It prints 33 lines: the previous sixteen baseline lines, three chronology controls and fourteen additional acceptance controls. All times belong to the artificial UTC date 2040-03-15. The explicit authorization, request/control IDs and sentinel binding are invented additions to HOLD2 only. They do not authenticate an issuer or add a case approval to R1–R16.

~~~python
from copy import deepcopy
from datetime import datetime, timedelta
import re

def utc(value):
    return datetime.fromisoformat(
        f"2040-03-15T{value}:00+00:00"
    )

REQUEST = {
    "id": "HOLD2-REQ-01",
    "sentinel": "BX-01",
    "source": "booking-audit-sim",
    "objects": {"BX-01", "BX-02"},
    "interval": (utc("09:00"), utc("09:30")),
    "custodian": "AppCustodian",
}
RECEIPT = {
    "id": "HOLD2-CTRL-01",
    "request_id": "HOLD2-REQ-01",
    "source": "booking-audit-sim",
    "objects": {"BX-01", "BX-02"},
    "interval": (utc("08:55"), utc("09:35")),
    "custodian": "AppCustodian",
    "active_from": utc("09:40"),
    "term_end": utc("11:30"),
}
AUTHORIZATION = {
    "request_id": "HOLD2-REQ-01",
    "operation": "hold_source",
    "source": "booking-audit-sim",
    "objects": {"BX-01", "BX-02"},
    "interval": (utc("08:55"), utc("09:35")),
    "approver": "IncidentLead",
    "custodian": "AppCustodian",
    "approved_at": utc("09:36"),
    "valid_until": utc("11:30"),
}
BASE = {
    "authorization": AUTHORIZATION,
    "effect_control_id": "HOLD2-CTRL-01",
    "effect_source": "booking-audit-sim",
    "oldest_checked": "BX-01",
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

def input_problem(s):
    """Check the fixed teaching schema; never authenticate a real source."""
    if not isinstance(s, dict) or set(s) != set(BASE):
        return "INVALID_PACKET_SCHEMA"
    for field in ("approved", "custodian_available", "effect_checked",
                  "oldest_retrievable", "copy_retained"):
        if type(s[field]) is not bool:
            return "NON_BOOLEAN:" + field
    for field in ("approval_source", "effect_control_id", "effect_source",
                  "oldest_checked"):
        if not isinstance(s[field], str) or not s[field]:
            return "INVALID_IDENTIFIER:" + field
    objects = (("request", REQUEST), ("authorization", AUTHORIZATION))
    if s["receipt"] is not None:
        objects += (("receipt", RECEIPT),)
    times = [s["as_of"]]
    for name, model in objects:
        item = s[name]
        if not isinstance(item, dict) or set(item) != set(model):
            return "INVALID_OBJECT_SCHEMA:" + name
        for field, value in item.items():
            if isinstance(model[field], str):
                if not isinstance(value, str) or not value:
                    return "INVALID_IDENTIFIER:" + name + "." + field
        selected = item["objects"]
        if (not isinstance(selected, (set, frozenset)) or not selected
                or any(not isinstance(x, str) or not x for x in selected)):
            return "INVALID_OBJECT_SCOPE:" + name
        window = item["interval"]
        if not isinstance(window, tuple) or len(window) != 2:
            return "INVALID_INTERVAL:" + name
        times.extend(window)
    times.extend((s["authorization"]["approved_at"],
                  s["authorization"]["valid_until"]))
    if s["receipt"] is not None:
        times.extend((s["receipt"]["active_from"], s["receipt"]["term_end"]))
    for value in times:
        if (not isinstance(value, datetime) or value.tzinfo is None
                or value.utcoffset() != timedelta(0)
                or value.date().isoformat() != "2040-03-15"):
            return "INVALID_UTC_TIME"
    for name, _ in objects:
        if s[name]["interval"][0] >= s[name]["interval"][1]:
            return "INVALID_INTERVAL:" + name
    if not isinstance(s["history"], tuple):
        return "INVALID_HISTORY_SCHEMA"
    for entry in s["history"]:
        if (not isinstance(entry, tuple) or len(entry) != 2
                or not all(isinstance(x, str) for x in entry)):
            return "INVALID_HISTORY_SCHEMA"
        if not re.fullmatch(r"[0-9]{2}:[0-9]{2}", entry[1]):
            return "INVALID_HISTORY_CLOCK"
        try:
            utc(entry[1])
        except ValueError:
            return "INVALID_HISTORY_CLOCK"
    return None


def status(s):
    problem = input_problem(s)
    if problem is not None:
        return problem
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

    if rec["term_end"] <= rec["active_from"]:
        return "INVALID_CONTROL_TERM"
    trail = [(kind, utc(clock)) for kind, clock in s["history"]]
    if (
        not trail
        or any(trail[i][1] > trail[i + 1][1]
               for i in range(len(trail) - 1))
        or any(when > s["as_of"] for _, when in trail)
    ):
        return "HISTORY_NOT_AVAILABLE_AS_OF"

    authorization = s["authorization"]
    if (authorization["request_id"] != req["id"]
            or rec["request_id"] != req["id"]):
        return "REQUEST_BINDING_MISMATCH"
    if (authorization["source"] != req["source"]
            or authorization["operation"] != "hold_source"):
        return "AUTHORIZATION_TARGET_MISMATCH"
    if (authorization["approver"] != "IncidentLead"
            or authorization["custodian"] != req["custodian"]):
        return "AUTHORIZATION_ROLE_MISMATCH"
    if (not rec["objects"].issubset(authorization["objects"])
            or rec["interval"][0] < authorization["interval"][0]
            or rec["interval"][1] > authorization["interval"][1]):
        return "AUTHORIZED_SCOPE_EXCEEDED"
    if (authorization["approved_at"] > rec["active_from"]
            or authorization["valid_until"] < rec["term_end"]):
        return "AUTHORIZATION_TIME_MISMATCH"
    expected = ("REQUESTED", "APPROVED", "APPLIED_REPORTED", "EFFECT_CHECKED")
    kinds = tuple(kind for kind, _ in trail)
    if kinds not in (expected, expected + ("RELEASE_RECORDED",)):
        return "HISTORY_LIFECYCLE_MISMATCH"
    if trail[1][1] != authorization["approved_at"]:
        return "APPROVAL_TIME_MISMATCH"
    if trail[2][1] != rec["active_from"]:
        return "ACTIVATION_TIME_MISMATCH"
    if (s["effect_control_id"] != rec["id"]
            or s["effect_source"] != rec["source"]):
        return "EFFECT_BINDING_MISMATCH"
    if (req["sentinel"] not in req["objects"]
            or s["oldest_checked"] != req["sentinel"]):
        return "SENTINEL_BINDING_MISMATCH"

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

assert status(future_release) == "HISTORY_NOT_AVAILABLE_AS_OF"
assert status(early_review) == "HISTORY_NOT_AVAILABLE_AS_OF"
assert status(invalid_term) == "INVALID_CONTROL_TERM"

# Additional independent acceptance controls, not R-series events.
CONTROLS = [
    ("EMPTY_OBJECTS", {"request": {**REQUEST, "objects": set()}},
     "INVALID_OBJECT_SCOPE:request"),
    ("REVERSED_INTERVAL", {"request": {**REQUEST,
        "interval": (utc("09:25"), utc("09:05"))}},
     "INVALID_INTERVAL:request"),
    ("TEXT_FALSE", {"approved": "False"}, "NON_BOOLEAN:approved"),
    ("MISSING_APPLICATION", {"history": (
        ("REQUESTED", "09:34"), ("APPROVED", "09:36"),
        ("EFFECT_CHECKED", "10:00"))}, "HISTORY_LIFECYCLE_MISMATCH"),
    ("APPROVAL_AFTER_APPLY", {"authorization": {
        **AUTHORIZATION, "approved_at": utc("09:45")}},
     "AUTHORIZATION_TIME_MISMATCH"),
    ("REUSED_APPROVAL", {"authorization": {
        **AUTHORIZATION, "request_id": "OTHER-REQUEST"}},
     "REQUEST_BINDING_MISMATCH"),
    ("EXTRA_OBJECT", {"receipt": {
        **RECEIPT, "objects": {"BX-01", "BX-02", "BX-99"}}},
     "AUTHORIZED_SCOPE_EXCEEDED"),
    ("WIDER_INTERVAL", {"receipt": {**RECEIPT,
        "interval": (utc("08:50"), utc("09:35"))}},
     "AUTHORIZED_SCOPE_EXCEEDED"),
    ("WRONG_EFFECT_CONTROL", {"effect_control_id": "OTHER-CONTROL"},
     "EFFECT_BINDING_MISMATCH"),
    ("WRONG_SENTINEL", {"oldest_checked": "BX-02"},
     "SENTINEL_BINDING_MISMATCH"),
    ("ACTIVATION_DISAGREES", {"receipt": {
        **RECEIPT, "active_from": utc("09:41")}},
     "ACTIVATION_TIME_MISMATCH"),
    ("NAIVE_REVIEW", {"as_of": datetime(2040, 3, 15, 10)},
     "INVALID_UTC_TIME"),
    ("INVALID_HISTORY_CLOCK", {"history": (("REQUESTED", "25:99"),)},
     "INVALID_HISTORY_CLOCK"),
    ("EXACT_TERM_END", {"as_of": utc("11:30")},
     "TERM_EXPIRED_EFFECT_UNKNOWN"),
]
for label, changes, expected in CONTROLS:
    actual = status(variant(changes))
    assert actual == expected, (label, actual, expected)
    print(f"{label}: {actual}")
~~~

Before reading the final appendix, predict all 33 output lines: sixteen baseline lines, three chronology controls and fourteen acceptance controls. Explain the first blocking condition for each variant. Compare the actual run with the [HOLD2 worked result](#ir-rapid-ch02-hold2-result).

**Required learner artifacts:** Reproduce the 33 output lines; create a scenario table with the first blocking condition and a safe next request; identify why `COPY_ONLY` does not establish source hold and why `OLDEST_MISSING` does not prove deletion timing; compare requested, reported and authorized scope; identify the request/control/sentinel bindings and required lifecycle steps; propose a reviewer check for release and expiry that does not erase history or delete data. A future lifecycle entry cannot support an earlier `as_of` conclusion; even a consistent fixture does not authenticate a real hold.

**Five-point assessment for this unnumbered lab:** One point each for exact output; correct source/object/interval coverage and authorization reasoning; separation of copy from source control; correct treatment of unavailable custodian or a specifically identified oldest row; and complete request-bound lifecycle, expiry/release history and explicit effect limits. Assess the added controls within these same five criteria. The lab adds **no new EX identifier**.

### 2.8c Practical two-role activity — custodian packet and independent review

#### Step 2 — Prepare and freeze one simulated custodian response

Choose the valid HOLD2 fixture or a wrong-source, oldest-missing, reused-approval or wrong-effect-control variant. Record the requested selection, the explicit authorization envelope, request and control IDs, application time, technical term, declared sentinel, check response and missing fields. Keep the complete modeled lifecycle and distinguish an unverified issuer from a structurally matching identifier. Freeze the packet as `HOLD2-custodian-v1`; a positive script result does not replace the receiver's independent reconstruction.

The reviewer must not see the author's private reasoning or a corrected answer. The packet may include explicit approved source pointers and the relevant original teaching rules.

**Limit:** This tabletop and the Python output measure only consistency and independent reasoning on synthetic records. They do not prove organizational readiness, actual source preservation, legal compliance or completion of any Harbor Library case action.

<a id="ir-rapid-ch02-q1-lab"></a>

### 2.9 Contained lab: correlate records without inventing an actor

The earlier labs examined *when* a row became visible and whether a copied file changed. A responder also needs to ask whether records from two systems refer to the **same activity**. An account label, a session identifier and a human identity are different things. If an application audit records `desk-a` but omits its session identifier, several identity sessions for that account could fit the same time. A nearby timestamp cannot choose one by itself. An exact identifier can narrow a candidate relationship, but it still does not identify the person who used the session or establish that the edit was authorized. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) provides high-level log-management background, and [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses investigation across source types. Neither older publication prescribes this book's matching code or claims that an account/time join proves attribution. The following method is an original beginner-level teaching fixture.

<a id="ir-rapid-ch02-hold2-result"></a>

### HOLD2 — Source-hold lifecycle laboratory: worked result

#### Exact expected output — executed in Python 3

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
FUTURE_RELEASE: HISTORY_NOT_AVAILABLE_AS_OF
FUTURE_EFFECT_CHECK: HISTORY_NOT_AVAILABLE_AS_OF
INVALID_TERM: INVALID_CONTROL_TERM
EMPTY_OBJECTS: INVALID_OBJECT_SCOPE:request
REVERSED_INTERVAL: INVALID_INTERVAL:request
TEXT_FALSE: NON_BOOLEAN:approved
MISSING_APPLICATION: HISTORY_LIFECYCLE_MISMATCH
APPROVAL_AFTER_APPLY: AUTHORIZATION_TIME_MISMATCH
REUSED_APPROVAL: REQUEST_BINDING_MISMATCH
EXTRA_OBJECT: AUTHORIZED_SCOPE_EXCEEDED
WIDER_INTERVAL: AUTHORIZED_SCOPE_EXCEEDED
WRONG_EFFECT_CONTROL: EFFECT_BINDING_MISMATCH
WRONG_SENTINEL: SENTINEL_BINDING_MISMATCH
ACTIVATION_DISAGREES: ACTIVATION_TIME_MISMATCH
NAIVE_REVIEW: INVALID_UTC_TIME
INVALID_HISTORY_CLOCK: INVALID_HISTORY_CLOCK
EXACT_TERM_END: TERM_EXPIRED_EFFECT_UNKNOWN
~~~

#### Why the result is deliberately bounded

**VALID_BOUND** is a consistency pass **within the invented fields** only. The script does not prove that any real deletion mechanism was configured or that every source row remains available. **PROPOSED_ONLY**, **APPROVED_NO_APPLY** and **COPY_ONLY** separate a request, approval lacking application evidence and preservation of a different copy; none establishes source protection.

**Important model limitations:** The fixture checks only the first applicable problem; multiple defects could coexist. An `effect_checked=True` flag does not authenticate a source query or independent protection test. A single oldest-row retrieval does not prove every applicable retention path is stopped. The code does not test actual custody, authority, legal duties, privacy rules, control-status provenance or source completeness; no delete request occurs. The HOLD2 event times and source IDs do not belong to Harbor Library's canonical Round B.

#### Interpreting the fourteen acceptance controls

The first three added results reject malformed premises before they can become positive evidence. An empty object set does not express a useful preservation scope; a reversed interval cannot describe the selected event window; and the text `"False"` is not a Boolean false value. Rejecting the packet is not evidence that a source was lost. The safe repair is to obtain a well-defined request, not silently coerce or enlarge it.

MISSING_APPLICATION lacks a required lifecycle step despite its remaining timestamps being ordered. APPROVAL_AFTER_APPLY supplies a permission later than the claimed application. REUSED_APPROVAL points to another request. These are different failures: missing application evidence, a prior-authorization contradiction and a request-binding mismatch. None is repaired by a positive effect flag. Obtain the specific missing or conflicting issuer/custodian record, preserve both versions and keep the action's acceptance unresolved.

EXTRA_OBJECT and WIDER_INTERVAL demonstrate the second side of scope checking. The receipt still covers the requested BX-01/BX-02 interval, but it exceeds the declared authorization. Coverage is not permission. Conversely, the original RECEIPT_SCOPE_GAP and RECEIPT_WINDOW_GAP controls fail the first side: they do not cover everything requested. A defensible review needs both comparisons, not a single subset test.

WRONG_EFFECT_CONTROL rejects a result for another control. WRONG_SENTINEL rejects a different selected marker. ACTIVATION_DISAGREES rejects a control receipt and application-history entry with different activation times under this model's stated semantics. In real work, different times might instead represent execution, receipt or discovery; clarify those meanings rather than overwriting a field to make it agree. The laboratory explicitly models one activation and one post-activation check, not every possible operational lifecycle.

NAIVE_REVIEW lacks the explicit UTC basis required by the fixed-date exercise. INVALID_HISTORY_CLOCK supplies an impossible clock. EXACT_TERM_END reaches the exclusive 11:30 boundary: the earlier check remains in history, but the term no longer supports an active-term assertion. No test attempts deletion or measures post-term source behavior.

**Limits of the positive control:** VALID_BOUND now depends on the explicitly declared authorization, nonempty selection, request/control bindings and complete modeled history as well as the original checks. Its positive label still means consistency of artificial premises, not authenticated approval or actual protection. The program returns the first blocking condition; several defects can coexist. Fixing one reported problem requires rerunning the complete review and does not imply all other fields were tested. `copy_retained` is deliberately irrelevant to a source-hold pass: an E1-style copy cannot repair a wrong control, missing effect check or unavailable sentinel.

**Model application to the existing numbered exercises:** EX018 requests both a selection that covers the decision question and authorization that covers the intended operation; at 09:20, IDs and receipts remain to be obtained. EX019 records only the local E1 creation and checks actually performed, with a separate pending source-control reference. EX022 asks the custodian to clarify those missing facts without saying a hold was applied. EX024 keeps receipt inconsistency separate from substantiated imminent source loss: each needs a named verifier and incident-lead review, not an automatic production action. Preserve the original artifact sizes and common 0–2 rubric; the additional program controls belong to the existing five-point HOLD2 assessment and create no new exercise ID.

### Chapter 2 synthetic-extract lab — worked result
