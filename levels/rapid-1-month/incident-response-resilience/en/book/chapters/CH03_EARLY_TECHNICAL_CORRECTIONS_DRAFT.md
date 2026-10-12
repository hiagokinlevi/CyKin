# Chapter 3, §§3.1–3.4 — Early Technical Corrections (DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **Edition:** English, rapid Incident Response. **State:** Proposed, independently tested correction blocks; **not integrated**, **not approved**, and not an additional book or chapter. The [principal manuscript](../MANUSCRIPT.md#ch-03) remains the sole course book.

**Review baseline:** public `MANUSCRIPT.md` SHA-256 `91604bd72435c97f68a89dcd6c16af5b72a4aac80d5d6989338ff503f77af6a9` on `main` commit `fea927012751fff01fb10b029c51c250711588c7`. Keep R1–R8 at the 09:05 checkpoint, R1–R16 at 09:20, and R17–R24 available for the 09:37 decision; do not carry exercise-only W1 or RB3 receipts into any of those releases. The 322-page A4 preflight is a length measurement, not an editorial approval. These blocks are proposals for the maintainer's selective integration, not replacements for the published Python baselines.

## Block A — §3.1: correct the R15 retention-clock description

**Exact placement:** Replace only the opening sentence of §3.1, immediately after `### 3.1 A decision loop rather than a fixed sequence`.

**Input and independently checkable evidence:** R15 reports a 24-hour detailed booking-audit retention rule without its anchor. Chapter 2 §2.8a explicitly warns against deriving an exact deletion instant from R9's event time. The current §3.1 sentence says that the previous triage "identified an audit-retention deadline."

**Consequence:** A reader could mistake evidence-loss urgency for a confirmed countdown and assume the team knows when each item will be removed.

**Replacement sentence:**

> Chapter 2 left B19 unexplained and identified a time-sensitive preservation risk: R15 supplies a 24-hour retention duration for detailed booking-audit records, but not the policy anchor or any verified deletion deadline.

The decision loop immediately following this sentence can remain unchanged. Do not derive a deadline from 09:03, nor extend the booking-audit rule to identity records.

## Block B — §3.3 W1: check required route coverage and legitimate-service behavior separately

**Exact placement:** Immediately after the original W1 `write_pause_claim` line and its interpretation, before `**Practice submission.**`. In the final worked-results appendix, place the accompanying transcript after `### Chapter 3 W1 write-pause verification lab — worked result`. Do not replace or silently alter the five published original output lines.

**Inputs:** The original `PROBES` table, `classify()` function and the W1 scope: W-UI and W-API are the **two named required write routes**; W-QUEUE and W-READ are the two tested legitimate-service functions. Each probe is an independent reset trial. All of these are artificial classroom observations.

**Reproduced original result:** The five published output lines match the complete unmodified program exactly.

**Adversarial finding:** Remove only W-API, leaving W-UI blocked. The original aggregation prints `write_pause_claim: SUPPORTED_FOR_TESTED_PATHS` despite losing a required known route. With `PROBES=[]` it prints the same line because Python's `all([])` is true. Separately, `classify("read", "returned Room 2", "Room 4", "Room 4", "read")` returns `READ_RETURNED_EXPECTED_VALUE` even though the supposed independent state is Room 4. Removing W-QUEUE has no effect on the write-claim line.

**Consequence:** A skipped route can appear to satisfy the stated test scope; a returned read label can be inconsistent with the actual reference state; successful write restriction can be confused with successful legitimate-service operation. These are validation defects inside the toy evaluator, not proof of a real deployed control fault.

**Corrective teaching insertion:** Run this extension **after the two existing complete W1 Python blocks in the same isolated Python session**. It leaves the original data and code untouched.

~~~python
# W1-SCOPE supplemental audit; requires the original PROBES and classify().
EXPECTED = {
    "W-UI": "write", "W-API": "write",
    "W-QUEUE": "queue", "W-READ": "read",
}

def w1_gates(probes):
    ids = [row[0] for row in probes]
    if len(ids) != len(set(ids)):
        return ("PROTECTION_UNEVALUABLE_DUPLICATE_ID",
                "SERVICE_UNEVALUABLE_DUPLICATE_ID")
    rows = {row[0]: row for row in probes}
    if any(k not in EXPECTED or row[1] != EXPECTED.get(k)
           for k, row in rows.items()):
        return ("PROTECTION_UNEVALUABLE_UNEXPECTED_PROBE",
                "SERVICE_UNEVALUABLE_UNEXPECTED_PROBE")

    if not {"W-UI", "W-API"}.issubset(rows):
        protection = "PROTECTION_UNEVALUABLE_MISSING_ROUTE"
    elif all(classify(*rows[k][1:]) == "BLOCKED_IN_THIS_TEST"
             for k in ("W-UI", "W-API")):
        protection = "PROTECTION_TESTED_PATHS_PASS_NOT_CAUSAL"
    else:
        protection = "PROTECTION_TESTED_PATHS_FAIL"

    if not {"W-QUEUE", "W-READ"}.issubset(rows):
        service = "SERVICE_UNEVALUABLE_MISSING_FUNCTION"
    else:
        q, r = rows["W-QUEUE"], rows["W-READ"]
        queue_ok = classify(*q[1:]) == "QUEUE_ITEM_RECORDED"
        read_ok = (
            classify(*r[1:]) == "READ_RETURNED_EXPECTED_VALUE"
            and r[2] == "returned Room 2"
            and r[3] == "Room 2"
            and r[4] == "Room 2"
        )
        service = ("SERVICE_TESTED_FUNCTIONS_PASS"
                   if queue_ok and read_ok
                   else "SERVICE_TESTED_FUNCTIONS_FAIL")
    return protection, service

def print_w1_gate(label, probes):
    print(f"{label}: {' | '.join(w1_gates(probes))}")

both = [
    ("W-API", "write", "rejected", "Room 2", "Room 2", "deny")
    if row[0] == "W-API" else row
    for row in PROBES
]
wrong_read = [
    ("W-READ", "read", "returned Room 2", "Room 4", "Room 4", "read")
    if row[0] == "W-READ" else row
    for row in both
]

print_w1_gate("ORIGINAL_W1", PROBES)
print_w1_gate("LEGACY_ROW_MISSING",
              [row for row in PROBES if row[0] != "W-API"])
print_w1_gate("NO_ROWS", [])
print_w1_gate("BOTH_WRITES_BLOCKED", both)
print_w1_gate("WRONG_READ_STATE", wrong_read)
print_w1_gate("QUEUE_ROW_MISSING",
              [row for row in both if row[0] != "W-QUEUE"])
~~~

**Exact supplemental output, independently executed with Python 3:**

~~~text
ORIGINAL_W1: PROTECTION_TESTED_PATHS_FAIL | SERVICE_TESTED_FUNCTIONS_PASS
LEGACY_ROW_MISSING: PROTECTION_UNEVALUABLE_MISSING_ROUTE | SERVICE_TESTED_FUNCTIONS_PASS
NO_ROWS: PROTECTION_UNEVALUABLE_MISSING_ROUTE | SERVICE_UNEVALUABLE_MISSING_FUNCTION
BOTH_WRITES_BLOCKED: PROTECTION_TESTED_PATHS_PASS_NOT_CAUSAL | SERVICE_TESTED_FUNCTIONS_PASS
WRONG_READ_STATE: PROTECTION_TESTED_PATHS_PASS_NOT_CAUSAL | SERVICE_TESTED_FUNCTIONS_FAIL
QUEUE_ROW_MISSING: PROTECTION_TESTED_PATHS_PASS_NOT_CAUSAL | SERVICE_UNEVALUABLE_MISSING_FUNCTION
~~~

**Acceptance distinction:** A test of a named write path requires the specific probe to be present; an absent route is **not measured**, not blocked. Read and queue acceptance are a separate service check, not implied by write-path protection. Even `BOTH_WRITES_BLOCKED` cannot demonstrate the pause *caused* the rejections without a permitted pre-pause baseline, request-linked audit pointers, source-consistent before/after reads and control activation evidence. Queue admission does not establish booking fulfillment, reconciliation capacity or recovery acceptance. The extension itself never runs a write or accesses any service.

## Block C — §3.3 RB3: bind reversal approval, trigger and two post-state checks to recorded times and scope

**Exact placement:** After the RB3 lab's complete original program and before `**Before running:** predict the twenty-two scenario lines`. In the final appendix, place the supplemental results immediately after `### RB3 — Worked result`, without replacing the 22 original published lines.

**Input and reproduced result:** RB3's 22 named cases run without errors and agree literally with their published appendix. The original `evaluate(BASE)` returns `BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN`. The program already distinguishes protection from legitimate-service acceptance via separate Boolean fields.

**Adversarial finding:** Adding a `trigger_time` of 14:20 (after the 14:13 execution), a `post-state/protection check` at 14:10 (before execution), an approval receipt recorded at 14:14 (after execution), or an approval whose actual scope is only `booking-read` does **not** change the original positive result. The original code has no receipt fields for these checks to inspect. An invented Boolean is neither an authenticated receipt nor a timestamped observation.

**Consequence:** The positive decision label cannot independently establish the stated operational ordering or that permission names the exact inverse. The existing disclaimers rightly limit the result, but a reader needs a tested method to **refuse acceptance when essential evidence metadata are missing or inconsistent**, rather than assuming optimistic input fields suffice.

**Corrective teaching insertion:** Run this extension in a **fresh RB3-only scratch session** after its complete original program. New receipt metadata below are *additional invented exercise inputs*; they were not supplied by R1–R24 or by W1. This validation is supplemental and does not change the original 22-case fixture or outcomes.

~~~python
# RB3-RECHECK: requires original BASE, evaluate(), utc().
from copy import deepcopy

POSITIVE = "BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN"
RECEIPTS = {
    "approval_ref": "APP-RB-01",
    "approval_owner": "ServiceOwnerSim",
    "approval_scope": {"staff-write"},
    "approval_target": "CFG-GOOD-7",
    "approval_time": utc("14:12"),
    "trigger_time": utc("14:10"),
    "execution_receipt_time": utc("14:13"),
    "post_state_time": utc("14:14"),
    "protection_checked_time": utc("14:15"),
    "service_checked_time": utc("14:16"),
    "review_as_of": utc("14:17"),
}

def rb3_recheck(packet, receipt):
    original = evaluate(packet)
    if original != POSITIVE:
        return original
    required = set(RECEIPTS)
    if (set(receipt) != required or
            any(receipt[key] is None for key in required)):
        return "RECEIPT_METADATA_INCOMPLETE"

    if (
        receipt["approval_ref"] != packet["rollback_approval_receipt"]
        or receipt["approval_owner"] != packet["rollback_owner"]
        or receipt["approval_scope"] != packet["rollback_scope"]
        or receipt["approval_target"] != packet["rollback_target"]
    ):
        return "APPROVAL_NOT_BOUND_TO_TARGET_AND_SCOPE"

    start, end = packet["authorized_window"]
    if not (
        start <= receipt["trigger_time"] <=
        receipt["approval_time"] == packet["decision_time"] <=
        receipt["execution_receipt_time"] == packet["execution_time"] < end
    ):
        return "TRIGGER_APPROVAL_EXECUTION_ORDER_INVALID"

    if not (
        packet["execution_time"] <=
        receipt["post_state_time"] <=
        receipt["protection_checked_time"] <= receipt["review_as_of"]
        and receipt["post_state_time"] <=
        receipt["service_checked_time"] <= receipt["review_as_of"]
    ):
        return "POST_EXECUTION_EVIDENCE_TIME_INVALID"

    return "BOUNDED_RECHECK_WITH_DATED_RECEIPTS_REVIEW_OPEN"

def print_rb3_recheck(label, packet, changes):
    receipt = deepcopy(RECEIPTS)
    receipt.update(changes)
    print(f"{label}: {rb3_recheck(packet, receipt)}")

print_rb3_recheck("DATED_BASELINE", BASE, {})
print_rb3_recheck("UNRECORDED_CHECKS", BASE,
                  {"protection_checked_time": None})
print_rb3_recheck("FUTURE_TRIGGER", BASE,
                  {"trigger_time": utc("14:20")})
print_rb3_recheck("LATE_APPROVAL", BASE,
                  {"approval_time": utc("14:14")})
print_rb3_recheck("WRONG_APPROVED_SCOPE", BASE,
                  {"approval_scope": {"booking-read"}})
print_rb3_recheck("CHECK_BEFORE_EXECUTION", BASE,
                  {"post_state_time": utc("14:11")})
print_rb3_recheck("PROTECTION_FAILED",
                  {**BASE, "protection_check": False}, {})
~~~

**Exact supplemental output, independently executed with Python 3:**

~~~text
DATED_BASELINE: BOUNDED_RECHECK_WITH_DATED_RECEIPTS_REVIEW_OPEN
UNRECORDED_CHECKS: RECEIPT_METADATA_INCOMPLETE
FUTURE_TRIGGER: TRIGGER_APPROVAL_EXECUTION_ORDER_INVALID
LATE_APPROVAL: TRIGGER_APPROVAL_EXECUTION_ORDER_INVALID
WRONG_APPROVED_SCOPE: APPROVAL_NOT_BOUND_TO_TARGET_AND_SCOPE
CHECK_BEFORE_EXECUTION: POST_EXECUTION_EVIDENCE_TIME_INVALID
PROTECTION_FAILED: PROTECTION_NOT_ACCEPTED
~~~

**Evidence boundary:** `DATED_BASELINE` is a newly declared **synthetic supplemental** chain; it demonstrates chronological and scope consistency, not independently authenticated action. A real decision would also require original, trusted approval and control receipts, source-clock semantics, named operators, pre-change baseline provenance, linked request IDs and observed acceptance criteria. The two checks must remain separate: protected operation constrained or otherwise acceptably managed **and** legitimate service functioning in the declared scope. A passed rollback check never means that Harbor Library achieved recovery, eradication, full route coverage or incident closure. An open human reassessment and queue/booking-state obligations remain.

## Block D — EX029 worked answer: keep the RB3 extension inside the required two rows

**Exact placement:** Immediately after the existing `**RB3 additional worked reasoning:**` inside `### EX029 — Worked result`. Add these columns to the *same two-option submission*, not a third option or a second independent scenario. Retain the original EX029 ID and common 0–2 rubric.

**Input/evidence:** EX029 expressly requires one two-row decision matrix covering revocation and pause, including pre-intervention baselines, reversal triggers, **separate new approval**, post-inverse protection and legitimate-service checks. The existing worked result explains these in following paragraphs rather than displaying all four dimensions against each option. At 09:37, R19 is a capability statement; R21 is a tolerance statement. Neither is an approval/execution receipt.

**Consequence:** A literal row-by-row assessor cannot verify whether both options contain all required reversal fields without reconstructing the model from separate prose.

**Supplemental answer cells:**

| Original EX029 option | Pre-intervention evidence needed | Hypothetical trigger and separately authorized reversal | Post-reversal protection acceptance | Post-reversal legitimate-service acceptance |
|---|---|---|---|---|
| Current-session revocation | Identified current session and baseline permitted sign-in/function; preserve the relevant identity and booking pointers. | Observed unacceptable denial of legitimate work, or failure to constrain the named session. Incident lead **and identity owner** decide on a new, scoped replacement-authentication or restoration action; the identity administrator reports the actual operation. | Independently establish that the original unacceptable session path remains constrained, or that an explicitly approved alternative safeguard is in effect within the tested scope. | Verify the authorized staff member can authenticate and perform the required permitted booking task, with source and time limits. |
| Fifteen-minute staff-write pause | Known authorized staff-write routes and a verified pre-pause allowed-write baseline, service functions and configuration/state reference; R21 alone authorizes nothing. | Observed write-route bypass or owner-verified unacceptable service disruption. The **service owner**, coordinated with the incident lead, approves a *new* precise reversal/replacement; the application operator reports any execution. | Probe each **named required** write route under the post-reversal operating mode, with request-linked response, authoritative before/after state and source coverage. | Demonstrate permitted read/manual intake as applicable; reconcile each queued request against owner-approved current booking state **before** treating it as an accepted booking or allowing uncontrolled normal writes. |

**Rubric alignment:** A score of 2 still requires the original intended effects, uncovered routes, service costs, approving and executing roles, post-action checks, fallback and one provisional 09:37 choice. These additional columns make the already-required RB3 extension auditable. Do not import W1/RB3 synthetic observations as completed case actions.

## Block E — EX031: make source inputs and retention limits explicit

**Exact placement:** Replace only the `**Inputs:**` clause in `#### EX031 — Evidence before change` and append the note immediately following the first row of `### EX031 — Worked result`. Preserve all four original answer rows and the existing 0–2 rubric.

**Input and evidence:** The original question names R13, R17–R20 and R15, but its answer also explicitly uses R9 (B19 row) and R10 (original training plan). Both are already available by 09:37; the issue is an incomplete **exercise input declaration**, not an unauthorized time jump. The answer's phrase "before R15's retention window removes detail" also risks being read as a measured deletion deadline even though R15 has no documented anchor.

**Replacement exercise input clause:**

> **Inputs:** R9–R10, R13, R15 and R17–R20, all available within R1–R24 at the 09:37 checkpoint; use only the record values actually supplied. R15 states a duration but not its deletion-clock anchor or an exact loss time.

**Supplemental worked-answer qualifier:**

> R9 and R18 are supplied booking-audit observations; identifying them as candidates for a preservation request does not assert that their raw source rows remain retrievable or that the analyst has collected them. R10 is a supplied training-plan observation, not a proof that no later authorized version exists. R15 supports time-sensitive custodian clarification and a narrow authorized request, **not** a calculable deletion instant. R20 describes a restricted comparison copy as available but supplies no itemized values or extra access approval for the learner; the future P1/C1 comparison remains a separate exercise release.

## Source and safety notes applicable to all blocks

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) is the current primary incident-response risk-management reference (2025). [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) supplies primary recovery-planning, testing and improvement context (2016). [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses source-aware IT-forensic practices (2006) and is not a legal or universal technical authorization. Their official publication pages were checked. None prescribes W1, RB3, their toy receipt names or their exact statuses.

All corrected programs are standard-library, in-memory classroom extensions. They issue no real service calls, make no configuration change, do not delete a record and grant no incident-response authority. The original W1 and RB3 outputs remain unchanged; the supplemental outputs were tested in isolated Python runs using the supplied complete original program definitions. New variants remain explicitly noncanonical. The [book completion standard](../../../../../../BOOK_STANDARD.md) still requires full-source, technical, pedagogical, accessibility, rights and edition review; these corrections do not approve Chapter 3 or the manuscript.
