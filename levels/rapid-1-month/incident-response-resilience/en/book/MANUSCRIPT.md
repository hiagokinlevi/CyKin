These outcomes are different from VQ2. VQ2 concerns whether a query result supports a claim about event coverage under filters and ingestion watermark. HOLD2 concerns whether an **authorized preservation control** was applied to the intended source and selection, with a reviewable lifecycle. A valid hold does not make a poorly scoped query complete; a valid query does not make a source hold effective.

#### 2.8a.16 Section synthesis — preserve the source, the copy and the decision trail separately

The learner should finish with three defensible habits. First, name the source, authorized objects and interval precisely enough that a custodian can say what is and is not protected. Second, separate requested, approved, applied and verified states, and use non-destructive source observations to bound any effect claim. Third, keep a versioned or append-only lifecycle through review, expiry and release without erasing earlier decisions or equating a protected copy with protected source retention.

#### Complete Python 3 program

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
~~~

Before reading the final appendix, predict the original sixteen output lines and the three additional negative-control lines. Explain the first blocking condition for each variant. Compare the actual run with the [HOLD2 worked result](#ir-rapid-ch02-hold2-result).

**Required learner artifacts:** Reproduce the sixteen baseline and three additional output lines; create a scenario table with the first blocking condition and a safe next request; identify why `COPY_ONLY` does not establish source hold and why `OLDEST_MISSING` does not prove deletion timing; propose a reviewer check for release and expiry that does not erase history or delete data. A future lifecycle entry cannot support an earlier `as_of` conclusion; even a consistent fixture does not authenticate a real hold.

**Five-point assessment for this unnumbered lab:** One point each for exact output, correct source/object/interval coverage reasoning, separation of copy from source control, correct treatment of unavailable custodian or oldest row, and expiry/release history with explicit effect limits. The lab is supplemental and adds **no new EX identifier**.

### 2.8c Practical two-role activity — custodian packet and independent review

#### Step 2 — Prepare and freeze one simulated custodian response

Choose either the valid HOLD2 fixture, the wrong-source fixture or the oldest-missing fixture. The author records which source was reported protected, scope, application time, technical term, control identifier if supplied, check response and which fields remain missing. Save the immutable draft as `HOLD2-custodian-v1`.

The reviewer must not see the author's private reasoning or a corrected answer. The packet may include explicit approved source pointers and the relevant original teaching rules.

**Limit:** This tabletop and the Python output measure only consistency and independent reasoning on synthetic records. They do not prove organizational readiness, actual source preservation, legal compliance or completion of any Harbor Library case action.

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
~~~

#### Why the result is deliberately bounded

**VALID_BOUND** is a consistency pass **within the invented fields** only. The script does not prove that any real deletion mechanism was configured or that every source row remains available. **PROPOSED_ONLY**, **APPROVED_NO_APPLY** and **COPY_ONLY** separate a request, approval lacking application evidence and preservation of a different copy; none establishes source protection.

**Important model limitations:** The fixture checks only the first applicable problem; multiple defects could coexist. An `effect_checked=True` flag does not authenticate a source query or independent protection test. A single oldest-row retrieval does not prove every applicable retention path is stopped. The code does not test actual custody, authority, legal duties, privacy rules, control-status provenance or source completeness; no delete request occurs. The HOLD2 event times and source IDs do not belong to Harbor Library's canonical Round B.

### Chapter 2 synthetic-extract lab — worked result
