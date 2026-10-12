# Chapter 3 §§3.9–3.13 — Late Technical Corrections (DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **Edition:** English / Rapid Incident Response. **Status:** proposed correction blocks, **not integrated or approved**. This is a temporary public draft for selective incorporation into the sole [principal English manuscript](../MANUSCRIPT.md#ch-03), not an extra lesson or book.

**Frozen review source:** public `main` at `2a7a84bc4577c641b2256154d0fd36c1791af04e`; `MANUSCRIPT.md` SHA-256 `ea98937e3567a3602672cae24be40f2f2cdf5eb5c1aa881c82995095ba1f8e92`. The 333-page A4 preflight and 50 paired numbered exercises/answers remain **draft evidence**, not a complete-book approval. [Editorial completion requirements](../../../../../../BOOK_STANDARD.md) remain applicable.

**Release rule shared by every correction:** R1–R8 at 09:05, R1–R16 at 09:20 and R1–R24 at the canonical 09:37 Chapter 3 decision. The independent G3-DG and MQ3 toy data, as well as any later Branch S/P receipts, may not retroactively establish a canonical approval, execution, effective pause, queue disposition, service acceptance or human attribution. Every code sample below uses only Python standard-library objects in memory; no real service, file, account, transaction or deletion is involved.

## Block A — §3.11 G3-DG: known failed gates must not disappear behind another unknown gate

**Exact insertion location:** After the current §3.11 G3-DG program and its unchanged eleven-line expected output, immediately before the existing **Interpretation and negative control**. Add the seven-line supplemental transcript and explanation within the corresponding teaching/worked-results discussion; do not replace or change the original eleven baseline lines.

**Finding (input → reproduced output):** The complete original G3-DG program produced **11/11 lines identical** to the published `3.11` transcript. However, with `approved=True, executed=True, protective=False, legitimate=None, data=True, audit=True`, the original `gate()` returns `EXECUTED_UNVERIFIED`. It encounters the unknown legitimate-service test before reporting the **known failed protection test**. Similarly, with `data=False, audit=None` and otherwise positive flags, it returns `RECOVERY_CHECKS_PENDING`, suppressing an observed negative data gate. Independently, setting all six flags to `True` returns `BOUNDED_TEST_GATES_PASS` without a signed approval, operator receipt or source test, because the fixture authenticates none of those fields.

**Consequence:** A trainee may incorrectly prioritize missing information over an explicit failed condition, or promote a Boolean exercise assertion to an authentic intervention. A negative gate is not turned into a pass or merely pending by another missing result. Reporting the first blocking condition is useful, but its ordering must never conceal a known failure relevant to a business decision.

**Proposed correction:** In a supplemental *logic-only* checker, reject known `False` protection and service results before treating a different result as `None`; do the same separately for data and audit. Preserve the existing lifecycle distinction between proposal, asserted approval and asserted execution. Even the most favorable outcome must be explicitly labeled as **declared and unauthenticated** until the actual organization supplies verifiable approval, operator, source, time and scope receipts.

**Complete, standalone Python 3 program, independently tested:**

~~~python
def gate_strict(approved, executed, protective, legitimate, data, audit):
    if executed and approved is not True:
        return "INVALID_UNAPPROVED_EXECUTION"
    if approved is not True:
        return "PROPOSED_ONLY"
    if executed is not True:
        return "APPROVED_NOT_EXECUTED"
    if protective is False:
        return "PROTECTION_GATE_FAIL"
    if legitimate is False:
        return "BUSINESS_GATE_FAIL"
    if protective is not True or legitimate is not True:
        return "EXECUTED_UNVERIFIED"
    if data is False:
        return "DATA_GATE_FAIL"
    if audit is False:
        return "AUDIT_GATE_FAIL"
    if data is not True or audit is not True:
        return "RECOVERY_CHECKS_PENDING"
    return "DECLARED_GATES_PASS_NOT_AUTHENTICATED"

CASES = [
    ("ALL_FLAGS_TRUE", (True, True, True, True, True, True)),
    ("PROTECTION_FAIL_SERVICE_UNKNOWN", (True, True, False, None, True, True)),
    ("SERVICE_FAIL_PROTECTION_UNKNOWN", (True, True, None, False, True, True)),
    ("DATA_FAIL_AUDIT_UNKNOWN", (True, True, True, True, False, None)),
    ("AUDIT_FAIL_DATA_UNKNOWN", (True, True, True, True, None, False)),
    ("ALL_CHECKS_UNKNOWN", (True, True, None, None, None, None)),
    ("EXECUTED_WITHOUT_APPROVAL", (False, True, True, True, True, True)),
]
for name, flags in CASES:
    print(f"{name}: {gate_strict(*flags)}")
~~~

**Exact seven-line supplemental output, executed in isolated Python 3.13.5:**

~~~text
ALL_FLAGS_TRUE: DECLARED_GATES_PASS_NOT_AUTHENTICATED
PROTECTION_FAIL_SERVICE_UNKNOWN: PROTECTION_GATE_FAIL
SERVICE_FAIL_PROTECTION_UNKNOWN: BUSINESS_GATE_FAIL
DATA_FAIL_AUDIT_UNKNOWN: DATA_GATE_FAIL
AUDIT_FAIL_DATA_UNKNOWN: AUDIT_GATE_FAIL
ALL_CHECKS_UNKNOWN: EXECUTED_UNVERIFIED
EXECUTED_WITHOUT_APPROVAL: INVALID_UNAPPROVED_EXECUTION
~~~

**Acceptance limit:** `ALL_FLAGS_TRUE` is still not authenticated approval, proven containment, permission to reopen, or service-owner acceptance. The positive label is only an internally consistent *synthetic input declaration*. Protection, legitimate service, data correctness and attributable audit each require their own scoped evidence, and causal eradication and full recovery are additional questions. The G3-DG exercise is independent of actual R-series decisions and of the separately released recovery lab.

## Block B — §3.13 MQ3: validate receipt identity and key conflicts at intake, not only after simulated application

**Exact insertion location:** Immediately after `3.13`'s original three complete MQ3 Python blocks and their discussion of the two order variants, before the `Chapter 3 exercises` heading. Add the eleven supplemental lines under the existing `MQ3 — Worked result`, preserving the original eleven-line transcript **literally** and keeping both passes explicitly separate.

**Finding (inputs → reproduced outputs):** The original three-block MQ3 program generated **11/11 lines identical** to the final appendix. Its original `simulate()` tracks operation keys **only after** a `SIMULATED_APPLY`, and never rejects duplicate receipt IDs. Two distinct approved operations supplied with the same receipt ID `MQ-01` but keys `KEY-A` and `KEY-Z` are **both** returned as `SIMULATED_APPLY`. Separately, if an operation with `KEY-Z` expects X11 version 4 (but X11 is at version 5), it returns `HOLD_STALE_VERSION`; a later, different operation using that same `KEY-Z` for X12 may return `SIMULATED_APPLY` because the earlier intent was never recorded as applied. The existing order experiment independently proves that processing MQ-01 before MQ-08 yields X10 Room D@v3, while reversing their order yields Room B@v3; a stale check prevents only the later write, not an arbitrary first-choice business decision.

**Consequence:** A learner who interprets the original `applied` dictionary as a **complete intake ledger** may miss repeated receipt IDs and conflicting *unresolved* requests. A code-level success remains only a sequential teaching mutation; it is not durable, exactly-once business execution or an authorized reconciliation of real queue entries.

**Proposed correction:** Show a *distinct receipt/intent intake preflight* before deciding whether to simulate any effect. For a repeated receipt ID, flag the collision even if the operation key differs. For a reused key with conflicting content, flag that conflict even when the earlier request was held or stale. For an identical key and signature, say only **possible retry; prior effect unknown** at intake. Preserve all original entries. This preflight is conservative and cannot by itself prove authorization, decide a business conflict, or guarantee atomicity. Its results must not be merged into the original `simulate()` baseline results.

**Complete, standalone Python 3 program, independently tested:**

~~~python
REQUESTS = [
    ("MQ-01", "KEY-A", "X10", 2, "Room D", True),
    ("MQ-02", "KEY-A", "X10", 2, "Room D", True),
    ("MQ-03", "KEY-B", "X11", 4, "Room E", True),
    ("MQ-04", "KEY-C", "X12", 1, "Room F", False),
    ("MQ-05", "KEY-D", "X99", 0, "Room A", True),
    ("MQ-06", "KEY-A", "X10", 2, "Room Z", True),
    ("MQ-07", "KEY-E", "X11", 5, "Room E", True),
    ("MQ-08", "KEY-F", "X10", 2, "Room B", True),
]

def intake_preflight(requests):
    receipts, intents = {}, {}
    output = []
    for receipt, key, booking, expected, desired, approved in requests:
        signature = (booking, expected, desired)
        if receipt in receipts:
            status = "HOLD_DUPLICATE_RECEIPT_ID"
        elif key in intents and intents[key] != signature:
            status = "HOLD_CONFLICTING_OPERATION_KEY"
        elif key in intents:
            status = "POSSIBLE_RETRY_EFFECT_UNKNOWN"
        else:
            status = "NEW_INTENT_EFFECT_UNKNOWN"
        receipts[receipt] = (key, signature)
        intents.setdefault(key, signature)
        output.append((receipt, status))
    return output

for receipt, status in intake_preflight(REQUESTS):
    print(f"{receipt}: {status}")

VARIANTS = [
    ("DUPLICATE_RECEIPT_ID", [
        REQUESTS[0],
        ("MQ-01", "KEY-Z", "X11", 5, "Room F", True),
    ]),
    ("STALE_THEN_DIFFERENT_SAME_KEY", [
        ("T1", "KEY-Z", "X11", 4, "Room E", True),
        ("T2", "KEY-Z", "X12", 1, "Room F", True),
    ]),
    ("TWO_COMPETING_REQUESTS", [REQUESTS[0], REQUESTS[7]]),
]
for label, rows in VARIANTS:
    print(label + ": " + ",".join(
        f"{receipt}={status}"
        for receipt, status in intake_preflight(rows)
    ))
~~~

**Exact eleven-line supplemental output, executed in isolated Python 3.13.5:**

~~~text
MQ-01: NEW_INTENT_EFFECT_UNKNOWN
MQ-02: POSSIBLE_RETRY_EFFECT_UNKNOWN
MQ-03: NEW_INTENT_EFFECT_UNKNOWN
MQ-04: NEW_INTENT_EFFECT_UNKNOWN
MQ-05: NEW_INTENT_EFFECT_UNKNOWN
MQ-06: HOLD_CONFLICTING_OPERATION_KEY
MQ-07: NEW_INTENT_EFFECT_UNKNOWN
MQ-08: NEW_INTENT_EFFECT_UNKNOWN
DUPLICATE_RECEIPT_ID: MQ-01=NEW_INTENT_EFFECT_UNKNOWN,MQ-01=HOLD_DUPLICATE_RECEIPT_ID
STALE_THEN_DIFFERENT_SAME_KEY: T1=NEW_INTENT_EFFECT_UNKNOWN,T2=HOLD_CONFLICTING_OPERATION_KEY
TWO_COMPETING_REQUESTS: MQ-01=NEW_INTENT_EFFECT_UNKNOWN,MQ-08=NEW_INTENT_EFFECT_UNKNOWN
~~~

**Assessment note:** This preflight does **not** turn `POSSIBLE_RETRY_EFFECT_UNKNOWN` into `DUPLICATE_RETRY` without independently verified effect evidence. It does **not** make the arbitrary processing order acceptable. It neither changes original toy state nor authorizes execution against a real database. A production design would require approved source data, stable key namespace and payload normalization, atomic operation/key-result storage, conditional version checks, durable outcome records, controlled concurrency and source-linked human reconciliation. The original RFC 9110 §9.2.2 reference covers HTTP method idempotency semantics, **not** exactly-once handling of application-specific operation keys. The two *unnamed* later Branch P manual requests have no IDs, signatures, expected versions or approval receipts in the supplied branch card: **MQ3 is not Branch P**.

## Block C — EX036: express required approval as future, never as recorded execution

**Exact insertion location:** Replace only field **4. Approver and executor** in the `EX036 — Worked result` six-field model table. Keep fields 1–3 and 5–6, the conditional RB3 subcard, EX036 identifier, input and rubric untouched.

**Finding:** EX036 asks for a 09:37 **proposed** revocation. The existing row says “Incident lead and identity owner approve; identity administrator executes only after approval.” The adjacent text and `3.10` correctly state that no approval or execution is supplied, but the unqualified present-tense “approve” can be misread as a documented completed decision.

**Consequence:** The worked answer is vulnerable to exactly the proposed→approved upgrade the exercise teaches students to reject.

**Replacement model answer row:**

| Field | Model decision card at 09:37 UTC |
|---|---|
| 4. Approver and executor | **Approval required; no receipt supplied:** the incident lead and identity owner would need to approve the exact named-session action under the fictional policy. Only *after that distinct decision*, the identity administrator could execute it, report the actual target and time, and request scoped independent protective and legitimate-service checks. No approval, execution or verification is established at 09:37. |

**Rubric:** EX036 remains a six-field proposal. Award full credit only when the learner names the decision owners and prospective operator **and** labels the approval/execution/effect receipts as pending. R21 establishes only tolerance for a possible pause, not a distinct approval or applied control.

## Block D — EX038: separate the fixed planning review from fifteen minutes of *effective* containment

**Exact insertion location:** Replace the single sentence in `EX038 — Worked result` that begins “Review with the owner at 09:52 UTC” with the corrective paragraph below. Keep the initial 09:37 proposal, two assumptions, approving role, queue template, conditional narrower alternative, RB3 reversal requirement and the original EX038 scoring rubric.

**Finding (input → reproduced result):** EX038's supplied canonical state at **09:37** is *pause proposed*, without application start receipt. Adding fifteen minutes to the **proposal** gives **09:52**, a reasonable **scheduled review time**, but **not proof** that a fifteen-minute effective pause ended then. If a later artificial approved-and-applied control were reported as starting at 09:42, the nominal end of its fifteen-minute interval would be 09:57; the lead could still review at 09:52 while the pause is active. The separately released Branch P describes its own reported start at 09:45 and nominal end at 10:00; neither time is knowable as an executed fact at the canonical 09:37 checkpoint.

**Consequence:** Students may confuse a review appointment with a control's verified activation/expiration, prematurely resume booking writes or represent queued requests as accepted without reconciliation. A duration is not a control-status observation, and reaching the expected end is not sufficient authority for automatic resumption.

**Replacement model-answer paragraph:**

> At 09:37 UTC, the incident lead **proposes**, but has not approved or applied, a fifteen-minute staff-write pause under the service owner's separate decision. Schedule a **planning and decision-status review at 09:52 UTC**, or sooner if verified new harm or a control failure requires attention. That meeting time does **not** certify fifteen minutes of effective protection. If a future authorized operator supplies a trustworthy, source-linked actual activation time, calculate the proposed fifteen-minute end from **that effective start**; record approval, targeted write routes, independent block verification, manual-queue continuity, expiry semantics and the next owner decision separately. Do not treat the calculated end as evidence that the control expired, that writes resumed or that pending manual requests were correctly applied. Any resumption requires current-state, queue, access and audit checks and explicit service-owner authorization.

**Complete, standalone Python 3 contrast to reproduce the timing distinction:**

~~~python
from datetime import datetime, timedelta

def time(clock):
    return datetime.strptime(clock, "%H:%M")

def timing(proposal_at, applied_at, minutes=15):
    review = (time(proposal_at) + timedelta(minutes=minutes)).strftime("%H:%M")
    if applied_at is None:
        return f"planning_review={review} effective_end=UNKNOWN_NO_EXECUTION_RECEIPT"
    if time(applied_at) < time(proposal_at):
        return f"planning_review={review} effective_end=INVALID_PRE_PROPOSAL_TIME"
    end = (time(applied_at) + timedelta(minutes=minutes)).strftime("%H:%M")
    return f"planning_review={review} conditional_effective_end={end}"

for label, start in [
    ("ONLY_PROPOSED", None),
    ("IMMEDIATE_IF_RECEIPTED", "09:37"),
    ("DELAYED_IF_RECEIPTED", "09:42"),
]:
    print(label, timing("09:37", start))
~~~

**Exact three-line output, executed in isolated Python 3.13.5:**

~~~text
ONLY_PROPOSED planning_review=09:52 effective_end=UNKNOWN_NO_EXECUTION_RECEIPT
IMMEDIATE_IF_RECEIPTED planning_review=09:52 conditional_effective_end=09:52
DELAYED_IF_RECEIPTED planning_review=09:52 conditional_effective_end=09:57
~~~

**Limit:** The string passed as `applied_at` is a *hypothetical input*, not an authenticated application receipt. `IMMEDIATE_IF_RECEIPTED` and `DELAYED_IF_RECEIPTED` are **counterfactual classroom variants**, not R-series or Branch P events. A real pause might activate late, cover fewer routes than expected, extend after a technical term or cease without safe service resumption. A 09:52 planning review is defensible even if the pause never begins, because it asks whether the plan is still valid—not whether the protective effect completed.

## Source, rights and safety boundaries for these corrective blocks

The [British Library's 8 March 2024 cyber-incident review](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=) was independently read against its printed **pp. 2–3, 9, 12–13**, including screenshots of the primary PDF. Page 2 supports the digital-collection copies, infrastructure difficulty and dated partial catalogue return; page 9 supports the identified backup sources and ongoing restrictions; page 12 supports Gold/Silver decision-making, workarounds and communications. The §3.9 source-reading exercise and worked ledger correctly treat those as *historical institutional statements*, not Harbor Library incident events. No replacement of the verified report-derived text is proposed. The original report and any external wording retain their rights; these correction blocks paraphrase only necessary facts and supply original code and pedagogy under [RIGHTS.md](../../../../../../RIGHTS.md).

The official [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) and [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) pages were checked. They supply primary background, not a mandate or certification for G3-DG or MQ3 statuses. Existing §3.11/§3.13 internal lab and worked-result anchors resolve in the current manuscript. EX037's supplied limitation on a page-load observation and absence of proof of exposure was consistent with its answer and needs no corrective text.

**Publication-status boundary:** These four correction blocks do not approve Chapter 3, restore a service, validate actual incident authority or satisfy the complete-volume gate. All test executions were isolated and did not alter a live system, the canonical manuscript or any private operational repository.
