# Chapter 2 — Late Technical Corrections (DRAFT)

**Integration target:** [English rapid Incident Response manuscript](../MANUSCRIPT.md#ch-02), second half of Chapter 2 (§2.8a–§2.24), plus the EX020–EX026 worked results in the same manuscript.

**Source checkpoint:** public main commit 3424db79763107f7541327b724364f4ed3590000; manuscript blob 8a7d68e748b89d68a2613cb4c8bf97e6408cef54. These are proposed corrections only, not integrated teaching or approval of the chapter or book. All case facts and exercise IDs remain unchanged. At 09:05 the learner has R1–R8; at 09:20 the learner has R1–R16. HOLD2, VQ2, Q1, IM2 and MIN2 are independent fictional fixtures, never new case records.

## Correction A — §2.8b HOLD2: reject future or inconsistent lifecycle evidence

**Exact integration location:** In the complete HOLD2 Python program, inside the existing function named status, insert the following block immediately **after** the existing early return for NOT_YET_ACTIVE and **before** the comment beginning “Preserve earlier steps; a release is an appended event.” Leave the current CASES labels, their existing expected output, and the later release/expiry/effect checks unchanged.

~~~python
    # A historical receipt must not justify a state before it existed.
    if rec["term_end"] <= rec["active_from"]:
        return "INVALID_CONTROL_TERM"

    trail = [(kind, utc(clock)) for kind, clock in s["history"]]
    if (
        not trail
        or any(
            trail[i][1] > trail[i + 1][1]
            for i in range(len(trail) - 1)
        )
        or any(when > s["as_of"] for _, when in trail)
    ):
        return "HISTORY_NOT_AVAILABLE_AS_OF"
~~~

**Additional classroom negative controls, to place after the original HOLD2 assertions** (do not append these to R1–R16):

~~~python
future_release = variant({
    "history": BASE["history"] + (
        ("RELEASE_RECORDED", "10:05"),
    )
})
early_review = variant({"as_of": utc("09:45")})
invalid_term = variant({
    "receipt": {**RECEIPT, "term_end": utc("09:35")}
})
print("FUTURE_RELEASE:", status(future_release))
print("FUTURE_EFFECT_CHECK:", status(early_review))
print("INVALID_TERM:", status(invalid_term))
assert status(future_release) == "HISTORY_NOT_AVAILABLE_AS_OF"
assert status(early_review) == "HISTORY_NOT_AVAILABLE_AS_OF"
assert status(invalid_term) == "INVALID_CONTROL_TERM"
~~~

**Tested output of the added controls (Python 3, isolated fixture):**

~~~text
FUTURE_RELEASE: HISTORY_NOT_AVAILABLE_AS_OF
FUTURE_EFFECT_CHECK: HISTORY_NOT_AVAILABLE_AS_OF
INVALID_TERM: INVALID_CONTROL_TERM
~~~

The existing 16-line HOLD2 transcript is unchanged by this insertion; its positive result remains BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE. This new guard detects a missing chronological prerequisite in the *artificial* receipt. It does not authenticate a real approval, independently confirm protection, verify every deletion path, establish retrospective row existence, or prove any data were deleted. An approval, reported application, verified effect, retained copy, release approval and observed post-release state are separate facts. Never use a future receipt at an earlier review checkpoint.

## Correction B — §2.10 VQ2: do not accept impossible clock metadata

**Exact integration location 1:** Replace the current minute(clock) definition in the complete VQ2 Python program with this validated, still single-day HH:MM helper.

~~~python
def minute(clock):
    if (
        not isinstance(clock, str)
        or len(clock) != 5
        or clock[2] != ":"
        or not (clock[:2] + clock[3:]).isdigit()
    ):
        raise ValueError("expected an HH:MM clock")
    hour, minute_value = int(clock[:2]), int(clock[3:])
    if not (0 <= hour < 24 and 0 <= minute_value < 60):
        raise ValueError("clock out of range")
    return 60 * hour + minute_value
~~~

**Exact integration location 2:** Replace the existing entire VQ2 assess(manifest) function with the following version. It retains the original conditional result for the same fixed scope, but refuses invalid declared clocks before evaluating the watermark.

~~~python
def assess(manifest):
    if manifest is None:
        return "UNKNOWN_MANIFEST"
    try:
        run = minute(manifest["run"])
        watermark = minute(manifest["watermark"])
        start = minute(manifest["start"])
        end = minute(manifest["end"])
    except (KeyError, ValueError, TypeError):
        return "INVALID_CLOCK"
    if start >= end:
        return "INVALID_QUERY_INTERVAL"
    if watermark > run:
        return "INCONSISTENT_METADATA"
    if (
        manifest["source"] != "application-audit"
        or manifest["account"] != "desk-a"
        or manifest["start"] != "09:00"
        or manifest["end"] != "09:12"
    ):
        return "SCOPE_MISMATCH"
    if watermark < end:
        return "INGESTION_NOT_COVERED"
    if manifest["returned"] != ("VQ-01",):
        return "RESULT_NOT_AS_ASSUMED"
    return "CONDITIONAL_IF_ATTESTED"
~~~

**Additional negative control, after the original assertions:**

~~~python
print(
    "BAD_CLOCK:",
    assess({**base, "run": "25:99"})
)
assert assess({**base, "run": "25:99"}) == "INVALID_CLOCK"
~~~

**Tested added output:** 

~~~text
BAD_CLOCK: INVALID_CLOCK
~~~

The original seven VQ2 output lines remain literally unchanged. An accepted manifest continues to mean conditional **only if source metadata and coverage are actually attested**; a purported watermark is not a direct measurement of ingestion completeness. The unit and dates are simplified within one fictitious UTC day; the code is not a general timestamp parser. R14 still lacks a validated query envelope, and R15 still lacks a retention-clock anchor.

## Correction C — §2.23 IM2: derive the negative control from the same classifier

**Exact integration location 1:** In the second IM2 Python block, add this helper **before** def classify(target, current, reports).

~~~python
def compare_one(booking_id, target, current):
    expected = target.get(booking_id)
    observed = current.get(booking_id)
    if expected is None or observed is None:
        return "UNVERIFIED"
    if expected == observed:
        return "MATCH"
    return "MISMATCH"
~~~

**Exact integration location 2:** Still in the second block, within classify's for booking_id in ids loop, replace the lines from expected = target.get(booking_id) through the concluding else assignment of status with this single call:

~~~python
        status = compare_one(booking_id, target, current)
~~~

Keep results[booking_id], counts[status], sorting, printing and return value unchanged.

**Exact integration location 3:** In the third IM2 Python block, replace the manual expression assigning negative_status with:

~~~python
negative_status = compare_one("X04", variant, CURRENT)
~~~

After its original two assertions, add the silent adversarial assertion:

~~~python
assert compare_one(
    "X04", {**TARGET, "X04": CURRENT["X04"]}, CURRENT
) == "MATCH"
~~~

**Tested statuses:**

~~~text
Original X04: MISMATCH
Target removed from variant: UNVERIFIED
Adversarial target equal to current value: MATCH
~~~

The original **nine-line IM2 transcript** in the worked appendix is unchanged, including negative_X04_target_removed: UNVERIFIED. The old negative_status shortcut returned MISMATCH whenever a target was present, even if that target equaled the observed value; it did not test the actual comparison rule. The corrected code uses one comparison contract in the baseline, missing-target variant and adversarial equality variant. These are fictional state comparisons, not verified Harbor Library impact, affected-person counts or evidence of a real owner-approved target.

## Correction D — §2.24 MIN2: reject an empty selection and make the accepted view inspectable

**Exact integration location 1:** In the MIN2 complete program, immediately **after** the EVENTS literal ends and **before** ALLOWED, insert an immutable-content baseline for this scalar-only teaching fixture:

~~~python
SOURCE_SNAPSHOT = [dict(row) for row in EVENTS]
~~~

**Exact integration location 2:** Within def review(label, fields, bookings), insert the following as its **first** conditional, ahead of the existing bookings.issubset(SCOPE) check:

~~~python
    if not bookings:
        print(f"{label}: REJECT_EMPTY_SELECTION selected=0")
        return
~~~

**Exact integration location 3:** After subset is constructed but before the READY print, add:

~~~python
    if not subset:
        print(f"{label}: REJECT_NO_SOURCE_ROWS selected=0")
        return
~~~

**Exact integration location 4:** After the second READY print (bookings=...) and before the review function ends, insert:

~~~python
    return subset
~~~

A projected view can now be assigned to a restricted reviewer variable for inspection. The projection includes only selected keys; a READY message is a toy policy outcome, **not** source authenticity, query completeness, permission from a real custodian, or proof of anonymization.

**Exact integration location 5:** Add these checks after the original MIN2 SOURCE_UNCHANGED assert (the additional test uses a copied source, not a real source or R-series record):

~~~python
assert EVENTS == SOURCE_SNAPSHOT
view = review("VIEW_CHECK", ALLOWED, {"Q11"})
assert view is not None and len(view) == 2
assert all("patron_email" not in row for row in view)
review("EMPTY_REQUEST", ALLOWED, set())
saved_events = EVENTS
try:
    EVENTS = [dict(saved_events[2])]  # only Q12 in this variant
    review("NO_Q11_ROWS", ALLOWED, {"Q11"})
finally:
    EVENTS = saved_events
assert EVENTS == SOURCE_SNAPSHOT
~~~

**Tested additional output:**

~~~text
VIEW_CHECK: READY rows=2 fields=actor_account,booking_id,event_id,event_time,operation
VIEW_CHECK: bookings=Q11
EMPTY_REQUEST: REJECT_EMPTY_SELECTION selected=0
NO_Q11_ROWS: REJECT_NO_SOURCE_ROWS selected=0
~~~

The original **six-line MIN2 worked transcript** remains unchanged. Refusing an empty or absent-source selection prevents a zero-row exercise variant from being called a successful booking-specific review. In a real incident, a validated zero-result query could be meaningful under a documented envelope and collection-health checks, which this program does not implement. A returned view must remain restricted to the approved role and purpose; the fictitious source's unchanged contents are not a real preservation receipt.

## Correction E — EX023 worked result: classify a match, a mismatch and unavailable comparison evidence separately

**Exact integration location:** In the final worked-results appendix, within “EX023 — Worked result,” replace the current paragraph's text beginning “Positive hypothetical result:” and ending “No actual result is supplied in R1–R16.” Retain the preceding approval/custodian request and the subsequent IM2-linked measurement contract and MIN2 extension.

**Replacement teaching text (English):**

**Hypothetical outcome A — verified match within the selected frame:** The owner-approved target and the current authoritative B19 value are present with their applicable versions, time and selection receipts; the values agree under the approved comparison rule. This supports a match for that selected state, not proof that every patron-facing consequence was correct or that the booking edit was authorized.

**Hypothetical outcome B — verified mismatch within the selected frame:** Both trusted comparison values and their relevant versions are available, but the current authoritative B19 value differs from the approved target. This supports a specific state discrepancy for B19, pending owner review of its consequence; it does not identify an attacker or estimate all affected patrons.

**Hypothetical outcome C — unverified comparison:** The approved target, current value, provenance, applicable time or required selection evidence is missing or not trustworthy. Do not label this a clean match or a confirmed mismatch. Request the missing bounded information or keep the result unverified.

In all three branches, the unit is the selected booking ID, not the help-desk ticket or an affected person. The requested view excludes unrelated patron names, newsletter fields and unapproved bookings. **None of these three hypothetical outcomes is observed in R1–R16.**

## Correction F — EX024 worked result: state the actual review trigger in both hypothetical branches

**Exact integration location:** In the final appendix, within “EX024 — Worked result,” insert the following paragraph immediately **after** its two-row table and **before** the sentence beginning “Neither observation is part of R1–R16.”

**Insertion (English):**

**Decision-time acceptance:** For either hypothetical branch, the incident lead must record the verifier, time of the qualifying observation, owner contacted, decision proposed, separate approval status and next review. At the supplied 09:20 checkpoint, 09:35 UTC remains the planned review; if either branch becomes source-verified earlier, reconvene promptly at the time of that verified trigger rather than waiting until 09:35. A confirmed source-preservation difficulty calls for a custodian/owner escalation and a separately authorized alternative, not automatic containment. An unexplained edit or owner-confirmed mismatch calls for a separate, proportionate containment assessment, not an assertion that a control was applied. Neither trigger, decision or operational effect is already observed in the R1–R16 release.

## Correction G — EX025 prompt: supply the faulty note the learner must actually repair

**Exact integration location:** In the Chapter 2 exercise section, immediately **after** the heading “EX025 — Correct a faulty note” and **before** its Objective/Inputs/Output paragraph. Keep ID EX025, the three-sentence output limit, the existing 0–2 rubric and the final worked answer intact.

**Insertion (English):**

**Faulty hypothetical note to repair (exercise text, not an R-series record):**

> “R9 proves an attacker stole the desk-a account. The attacker edited every booking. R8 and R11 prove the patron database was exfiltrated.”

This deliberately defective teaching note makes three unsupported claims: identified attacker/account theft; all-booking scope; and confirmed data exfiltration. Using only R9, R11, R13 and R8, rewrite it in at most three sentences so that reported observations, missing device/location/destination evidence and the proposed authorized next checks remain separate. Then name the three discarded claims. Do not replace the note with a claim that **no** transfer occurred.

The existing EX025 worked answer now has a specific, reproducible faulty input to correct; the learner need not invent the three claims that the answer key tells them to remove.

---

**Boundary for future integration:** No correction in this file changes the canonical 09:05 or 09:20 record release, turns a variant into evidence, confirms a source hold or export, introduces a new exercise ID, authenticates a custodian, or changes the manuscript's draft status. Sources supporting the *general* evidence and privacy principles include [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final), [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) and [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final); none prescribes these particular toy validators or establishes a real hold or privacy permission. Only the draft blocks above are proposed for later manual integration.
