# Incident Response and Cyber Resilience — Rapid Course
## Chapter 03 Transitional Expansion Draft: Measuring Recovery Time and Evidence of Data Recovery

**Editorial state:** **Public transitional English instructional component** of Chapter 03 of the **single principal book**. This is not a fifth chapter, a separately complete book, a verified operational runbook, or an A4 validation.  
**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 03 — Containment, eradication and recovery decisions](../MANUSCRIPT.md#ch-03).  
**Specific gap addressed:** Measure the elapsed interval from a documented service interruption to **accepted** service, distinguish backup/snapshot age from proved missing accepted operations, and refuse time or loss claims when the required evidence is absent or contradicts the acceptance contract.  
**Existing material preserved:** Sections 3.5 and 3.8; W1 control-path tests, G3-DG decision gates, K1 candidate screening, the P1/C1 and V1 cards, MQ3 queue scenarios, the original 50 exercise identifiers and their final worked answers. The RTE3 laboratory below is **new and independent**.

> **Safety and case provenance:** Harbor Library is entirely fictional. R1–R8 belong to the 09:05 Round A decision; R9–R16 are released at 09:20; R17–R24 enter Round C before the 09:37 decision. Branch S or P appears only in Round D; P1/C1 and V1 follow as separately released cards. W1, G3-DG, K1 and MQ3 are independent classroom variants. **RTE3 is another isolated fixture; its times, accepted-write IDs, restore receipts, comparisons and gate results are invented teaching inputs, never observations from any canonical or prior exercise card.** No activity touches live infrastructure or personal data.

# Chapter 03 — New Teaching: Recovery-Time and Data-Point Evidence

### Learning objectives and instructional fit

After this supplement, a new incident-response learner should be able to explain **which two events bound an outage-to-service-acceptance measurement**, calculate elapsed time from those events when trustworthy timestamps exist, and identify why a short installation or import time is not the same measurement. The learner should also screen snapshot age against a *hypothetical* recovery-point target without presenting age as a count or duration of actually lost business transactions.

The earlier Chapter 03 teaches that R23's backup-job success does not establish recovery readiness. Section 3.5 introduces recovery time and point objectives; Section 3.8 uses K1 to compare candidate timestamps, copy integrity and booking correctness. Those are necessary foundations. The distinct next step is to design a **measurement record from interruption through recovery testing and service-owner acceptance**, so that a responder can say precisely whether an RTO result was measured, merely targeted, or impossible to determine.

The method below uses invented small records and standard-library Python. It deliberately avoids repeating the K1 candidates, using P1's four booking values as synthetic output, simulating a live write pause, or replacing the chapter's separate access-and-audit tests. The aim is to improve reasoning from the evidence the learner actually possesses.

### RTE3.1 Define the unit of service that starts and stops the clock

A statement such as "the system recovered in twelve minutes" is uninterpretable until it identifies *which system function*, the starting event, the stopping event and the source of both times. A server process might restart in twelve minutes while a customer-facing booking workflow remains unavailable. A database might become queryable while staff writes are still blocked. Neither event necessarily proves that the library resumed its accepted reservation service.

For this classroom, define the measured unit as **the owner's approved room-booking service outcome for the scoped exercise**. The measurement starts when that outcome is first documented as interrupted under the agreed exercise rule. It stops only when the scoped functional, booking-data, access and audit acceptance conditions have passed and the designated service owner records an acceptance decision. The owner's decision may include a restricted-mode exception, but the claimed scope must then say *restricted*, not unrestricted recovery.

This is an **operational measurement contract chosen for RTE3**, not a universal formula required by NIST. A different organization may define outage onset, business impact and RTO scope differently in its business impact analysis. [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) provides official contingency-planning context, and the [NIST RTO glossary](https://csrc.nist.gov/glossary/term/recovery_time_objective) ties recovery time objectives to the effect of recovery duration on mission or business processes.

The interval only answers an honest question if both endpoints apply to the **same declared service scope**. A start time for staff booking writes and an end time for the home page are mismatched endpoints. A measured end for one isolated test copy does not prove a live service accepted production requests. Every measurement card should therefore name the function and whether the environment is an isolated training fixture, an authorized rehearsal or a real system under appropriate controls.

### RTE3.2 An RTO target is not an observed recovery duration

An **objective** expresses how quickly a function should recover under an owner-approved plan. A **measurement** reports how long an identified event actually took under a specified method. A **pass/fail comparison** requires both the approved objective and enough evidence for the corresponding measurement. It is improper to report "RTO achieved" merely because someone proposed a target or because a restore command ended within that target.

The current book uses a **hypothetical two-hour RTO** for a planning example. RTE3 retains the same illustrative magnitude: 120 minutes. The classroom accepts it only as a fixture input. It is not established that Harbor Library's real or canonical fictional service owner adopted that target. R7 and R23 supply no actual service-interruption timestamp, final accepted-service time or measured restore duration.

To make measurement defensible, use at least three distinct time concepts. **Interruption time** denotes when the named service outcome became unavailable. **Technical-ready time** records when a restricted copy or component can perform a bounded technical test. **Service-accepted time** records the owner's later decision after the required business and security checks. Detection and recovery-start times are additional useful milestones but are not substitutes for the two contract endpoints.

If the technical environment starts at 10:20 but the service owner accepts the complete scoped service only at 11:10, the recovery interval does not end at 10:20 under RTE3's contract. Those fifty minutes may contain evidence reviews, identity tests, corrections, queue reconciliation and owner decision-making. Ignoring them makes a technical component look faster than the service actually became acceptable to use.

### RTE3.3 Construct a milestone ledger with traceable meanings

A recovery measurement ledger should capture **what each timestamp means and what produced it**, not simply a sequence of clock readings. The following columns form a useful minimum:

| Milestone | Evidence the investigator would need | Limit if only a proposed time is available |
|---|---|---|
| Service interruption | Owner-defined failed business outcome, scope, reporter/source and event time | The cause and onset may remain disputed |
| Incident detection | Monitoring or report that the response team received the signal | Detection is not necessarily the beginning of outage |
| Recovery authorization | Decision owner, approved scope and applicable control conditions | Permission alone does not perform recovery |
| Restoration work started | Operator's trial/operation log and environment | Starting a task does not prove any service capability |
| Technical ready | Named component/isolated copy and bounded functional result | Not automatically accepted service |
| Data correctness checked | Approved expected state, observed state, source version and comparison receipt | A sample may omit unknown objects |
| Access/audit gates checked | Permitted and denied test cases with audit identity and time | Limited results cover only tested roles and paths |
| Service owner accepted | Named owner, decision timestamp, accepted function scope and residual conditions | An unacknowledged suggestion is not acceptance |
| Post-return monitoring | Next review and evidence-backed rollback or escalation trigger | A planned window is not an observed clean period |

A timestamp should be stored together with its timezone, source and uncertainty. RTE3 uses one artificial calendar date and explicit UTC offset in Python solely to avoid ambiguity. In a real collection, time from different systems may need independent clock and ingestion validation. Sorting timestamp strings is not enough to establish that each source observed the same event boundary.

The ledger also needs a **status**, such as planned, performed, verified, failed or unavailable, for every milestone. It is inaccurate to fill a planned 11:10 acceptance slot with a value and later report it as measured if the owner never accepted the service. Preserve the original planned time and mark the actual receipt missing.

### RTE3.4 What counts as an acceptable stopping event?

The end of the recovery interval must be tied to the declared outcome. For a fictional booking service, plausible acceptance gates include:

1. **Data:** the restored or reconciled state matches the relevant owner-approved expected objects, with explicitly bounded coverage.
2. **Authorized operation:** a permitted synthetic staff booking can succeed in the authorized test scope.
3. **Denied operation:** a prohibited synthetic edit is rejected without an unintended state change.
4. **Audit:** the permitted action produces the expected actor and event time within the tested route.
5. **Owner decision:** the accountable service owner records acceptance for the tested operating mode and notes residual restrictions.

These gates are not a substitute for real organization-specific criteria. They are intentionally separate because passing one cannot repair another. The existing V1 fixture reports two limited access outcomes and a blank actor field; that failed audit attribution criterion would prevent an **unrestricted acceptance claim** under the relevant later exercise. RTE3 does not change V1's outcome or pretend that any new booking correction was executed.

Owner acceptance itself should state its boundary. A service may be conditionally accepted for restricted use while a different function remains blocked, but the resulting duration can only be attributed to that **restricted service definition**. Labeling such a measured time as "full booking service restored" would erase the material exception.

An observed technical-ready time is valuable as a phase measurement. It can help a team understand how long platform work took. It is not, by itself, the stopping event of the declared end-to-end service-acceptance measurement.

### RTE3.5 Contrastive worked example: measured service acceptance

**Entirely synthetic RTE3 example, not a Harbor Library event.** Imagine an isolated training service on a fictional date with the following documented teaching milestones:

| Artificial event | UTC time | Interpretation in this fixture |
|---|---|---|
| Scoped booking service interrupted | 09:45 | Declared start of the service-level clock |
| Detection acknowledged | 09:55 | Response team learned of the simulated fault |
| Isolated restoration started | 10:02 | Work began, but no acceptance yet |
| Technical copy ready | 10:20 | Bounded technical readiness, not full service |
| Data comparison complete | 10:50 | One required gate passed in the selected fixture |
| Permitted/denied operations checked | 11:02 | Two access tests completed in the toy scope |
| Actor/time audit checked | 11:06 | Last technical acceptance gate completed |
| Owner acceptance recorded | 11:10 | Declared stopping event for this scope |

The elapsed interruption-to-acceptance interval is **85 minutes**: from 09:45 to 11:10. The technical-ready interval is **35 minutes**, from 09:45 to 10:20. Those values answer different questions. The response detected the disruption after ten minutes, but beginning the interval at 09:55 would conceal those ten minutes of unavailable service under this contract.

Against the illustrative 120-minute target, the **85-minute simulated measurement is within target** for this *defined classroom service and gate set*. It does not establish that Harbor Library met an approved organizational RTO, nor does it prove that every unmodeled booking function was healthy.

Suppose the recovery lead's candidate copy is labeled 09:35 and the interruption occurs at 09:45. The apparent age of the copy at interruption is **ten minutes**. That is a separate data-point screening calculation. Whether accepted writes after 09:35 were recovered must be evaluated from accepted-operation records and restored outcomes, not inferred from the 85-minute recovery duration.

The useful conclusion is precise: "The isolated RTE3 scenario reached owner acceptance after 85 minutes under the listed fixture gates; the copy was labeled ten minutes old at the declared interruption; and data coverage is assessed separately." It is not a claim of full operational recovery.

### RTE3.6 Incorrect example: the eleven-minute import

Consider the following **incorrect** fictional handoff:

> "The copy was imported in eleven minutes. The planned RTO is two hours, so RTO passed. The newest copy was only seven minutes old, so we lost seven minutes of data. There was no reason to wait for the service owner."

The handoff combines three unsupported conversions. Import duration is not necessarily elapsed time from interruption to accepted service. Snapshot age is a gap between two timestamps, not the amount of accepted business work permanently missing. And a successful technical activity does not replace required owner acceptance or security/audit tests.

A **correct** alternative would read:

> "The isolated import step took eleven minutes in the separately supplied exercise. The outage start, tested dependencies, completed acceptance gates and service-owner acceptance time are not all supplied for the full service, so an interruption-to-acceptance result is not measured. The seven-minute snapshot age is a screening value under stated clock assumptions, not proof of seven minutes of lost accepted writes. Further source and owner evidence is needed before a service-level RTO or RPO conclusion."

This alternative is less dramatic but more useful. It tells the next responder exactly which evidence must be requested and which numbers remain defensible.

The distinction applies directly to K1's isolated import durations of 11 and 14 minutes. Those existing numbers describe **only the classroom import-and-read trial**. They do not measure a completed production outage, and they must not be reused as proof that the owner accepted correct Harbor Library booking service.

### RTE3.7 A copy's age screens risk; it does not measure lost transactions

A **recovery point objective (RPO)** describes the point in time to which data must be recovered after an outage under the approved organizational requirement. The [NIST RPO glossary](https://csrc.nist.gov/glossary/term/recovery_point_objective) links the definition to NIST SP 800-34 Rev. 1. The classroom's hypothetical RPO magnitude is **30 minutes**; that is a target, not an operational result.

Snapshot age at interruption can be calculated if the relevant source/copy timestamp and interruption timestamp are known and comparable. For a copy labeled 09:35 and interruption at 09:45, the apparent age is ten minutes. A copy labeled 08:50 is apparently 55 minutes old at 09:45. This arithmetic is often a helpful **initial screen** for choosing further tests.

An age that exceeds 30 minutes weakens the case for relying on the older snapshot **alone**. It does not establish that 55 minutes of accepted business changes were actually lost. Perhaps no approved booking was accepted during part of that interval. Perhaps an independently protected transaction journal can replay later changes. Conversely, a copy only five minutes old can still contain incorrect or inconsistent state.

The correct sequence is: verify copy identity and time basis; identify the last recoverable and acceptable business state; investigate any approved journal/replay sources; compare the recovered state with an authorized ledger of accepted operations; and determine which known accepted operations remain unaccounted for.

K1 itself illustrates why copy age is not sufficient: K-B's digest mismatch blocks its integrity gate, K-C's recent state conflicts with the known approved four-booking target, and K-A's selected matches do not establish completeness of other legitimate work. RTE3 preserves those separate results rather than overwriting them.

### RTE3.8 Distinguish a data-point gap from a proved loss count

Suppose a candidate snapshot is labeled 09:35 and two **fictional accepted writes** are recorded after that time, at 09:38 and 09:42. These teaching operation IDs are `W-A` and `W-B`. If the isolated restored state demonstrably includes both accepted effects, the controlled comparison has **zero known unrecovered writes within those two listed operations**.

That limited count is not a claim that the whole business lost zero data. It requires the supplied accepted-write ledger to be complete *for the declared test frame*. If the ledger itself is incomplete, the analyst cannot set the total loss bound to zero, even when every listed operation is present. Unknown accepted transactions might still exist outside the frame.

If `W-B` is absent from the verified restored state, the exercise has **one known unrecovered accepted operation in its specified set**. That is stronger evidence than mere snapshot age for the missing item. It still does not provide a population-wide count unless the source coverage and business effect are appropriately verified.

The learner should maintain three separate fields: **claimed snapshot time**, **complete or incomplete accepted-operation ledger**, and **restored/verified operation coverage**. Combining them into a single number called "minutes lost" conceals what is known and unknown.

A transaction's timestamp is not automatically the moment it became durable and accepted under every system design. In real recovery, the source owner must define its commit/acknowledgement semantics and correlation keys. Our toy IDs deliberately avoid making that assumption about Harbor Library's live reservation database.

### RTE3.9 When accepted operations are missing, stop the shortcut to RPO success

The most tempting mistake in a recovery report is to declare an RPO pass because the snapshot age is below the target, even though a known accepted operation was not recovered. A data-point screen does not repair a business-state discrepancy.

For an isolated exercise, compare the declared set of accepted operation IDs with the set verified in the restored state. The set difference identifies **known, specifically referenced operations requiring attention**. It cannot identify operations absent from the accepted-write source, and it does not prove that an unrecovered entry was permanently destroyed rather than awaiting a later authorized replay or reconciliation.

If one known accepted write is missing, the recovery lead should record its identifier, source/time semantics, expected state, attempted replay, observed result and owner. The owner then decides whether and how the operation can be reconstructed and how the remaining risk affects service acceptance. An incident responder should not silently discard it merely to make the count zero.

This is particularly important when multiple people are working during a disruption. Manual queue receipts, application acceptance records and transaction journal entries can represent different stages of a request. A manual receipt is not necessarily an accepted booking; a successful HTTP response is not necessarily a proven durable commit. The definition of "accepted operation" needs an owner and source semantics.

RTE3 uses one simple boolean `ledger_complete` for the synthetic scope. In practice, proving coverage requires retention, time-window, source-health, inclusion and reconciliation checks. The boolean is a teaching premise, not an independently authenticated production attestation.

### RTE3.10 What to do when the interruption timestamp is missing

Sometimes a team knows that restoration work started but cannot establish when the essential business service became unavailable. It might have an alert receipt time, a patron complaint or an operator's recollection. Those observations can help reconstruct an interval, but they are not necessarily the actual outage onset.

If the interruption time is absent, the correct result of the elapsed-time calculation is **unknown**. The analyst can record known milestones, for example, "first confirmed bad service observation" and "last documented good service observation," and then seek a bounded source or owner-accepted estimate. A range may be possible in a more advanced analysis; an exact duration must not be fabricated from a convenient timestamp.

Do not replace missing interruption time with detection time without saying the measurement has changed. "Minutes since alert" and "minutes the service was unavailable" are distinct metrics. A service may have been unavailable before the detector noticed it. Conversely, a detector may fire before a business disruption is established.

In the offline lab, `MISSING_INTERRUPTION` sets the start to `None` while retaining a technical-ready time and owner-acceptance receipt from the baseline. The program refuses to compute the outage-to-acceptance interval. Even the age of the snapshot **at interruption** becomes unknown without the reference time.

That result is a successful demonstration of evidence discipline. It is not a failed calculation in the sense of arithmetic error; it correctly declines to report an unsupported measurement.

### RTE3.11 What to do when the acceptance receipt is missing or negative

A recovery team may finish all of its planned technical checks yet lack an owner decision for returning the service to use. The correct status is not "accepted by default." An absent owner receipt is a missing business decision, and the elapsed interval to owner acceptance remains **unmeasured** under RTE3's endpoint contract.

There is a second, stronger case: a required acceptance gate **fails**. Suppose a data comparison explicitly reveals an unacceptable mismatch, or the audit test lacks the required actor field. That is not merely an absent receipt. It is a supplied negative result that blocks the declared full-service acceptance. The team should record the failed criterion, its source, the responsible correction owner and the next test, without manufacturing a later acceptance timestamp.

The lab therefore distinguishes **NO_OWNER_RECEIPT** from **ACCEPTANCE_FAILED**. In the first case, the selected gates pass in the invented fixture but the final owner receipt is absent. In the second, a required gate has failed, so the service cannot be accepted under that contract despite the technical copy's availability.

An accountable owner could separately approve a restricted operating mode with explicit residual risk. That would create a **different measured service scope**, with its own start/stop contract and decision evidence. It does not turn a full-service failure into an unrestricted recovery pass.

No real approval, production restoration or scoped risk exception is supplied by RTE3. All owner flags are artificial program inputs.

### RTE3.12 When clocks disagree, the measurement needs verification

Calculating a duration assumes that the two endpoint times can be compared. A timestamp may have the wrong timezone, a clock offset, an imprecise event definition or an ingestion delay. Merely formatting it as ISO 8601 does not establish accuracy.

A robust technical record distinguishes **producer event time**, **collector time**, **review time** and **decision time**, then documents conversions. Chapter 02 teaches those distinctions for investigation logs. In recovery measurement, the same discipline applies to outage start, copy creation and final acceptance.

RTE3 uses one fictional date and UTC-aware Python timestamps, avoiding ambiguous local clock conversion. It also includes an artificial `clock_verified` flag. When that flag is false, the program refuses the exact age and RTO calculations rather than invent a result. In reality, verification would require evidence about the sources and clocks; a Boolean field is only a classroom stand-in.

If the reported technical-ready time precedes the interruption under the same clock basis, or if the accepted time precedes technical readiness contrary to the defined sequence, the measurement should be marked **internally inconsistent**. The analyst must determine whether the records refer to different scopes or contain timing errors. The script checks some ordering conditions but is not a full forensic clock-reconstruction system.

An owner who receives an inconsistent timeline should not simply choose the timestamp that yields a passing target. Corrections need source pointers, reasoning, version history and reviewer acceptance.

### RTE3.13 Use an evidence matrix rather than one recovery percentage

A single score such as "recovery 95%" can hide the facts a service owner actually needs. At the rapid level, a more useful assessment lists separate questions:

| Recovery question | Result category | What would substantiate it |
|---|---|---|
| Was interruption onset established? | Known / unknown / disputed | Scoped business-failure source and time basis |
| Was technical readiness demonstrated? | Passed / failed / not tested | Controlled component or isolated-copy test |
| Were required data checks completed? | Passed / failed / unknown | Owner-approved expected values and observed restored state |
| Were authorized and denied access tests completed? | Narrow pass / fail / not tested | Bound identities, operations, versions and authoritative state |
| Was usable audit attribution verified? | Passed / failed / unknown | Actual actor and event time in tested audit scope |
| Did the owner accept the declared service? | Accepted / restricted / rejected / pending | Dated accountable decision receipt |
| Is an outage-to-acceptance interval measured? | Elapsed time / unknown with reason | Verified comparable start and accepted endpoints |
| Is the recovery point adequately demonstrated? | Supported for scope / screen only / unknown | Snapshot and replay provenance, accepted operation coverage and correctness |

The matrix avoids turning one satisfied row into a universal pass. A service can be technically ready yet unaccepted because data is wrong. A copy may have a recent timestamp yet be unusable. An accepted restricted service may provide a useful function without meeting every normal operating criterion.

A useful handoff preserves all these statuses and names who owns the unresolved decision. The incident lead should not force a single green/red result when different functions and evidence sources remain in different states.

### RTE3.14 Reproducible measurement contracts support later improvement

A recovery exercise can improve the organization only if the next rehearsal can use the same definitions. Record the version of the measurement contract, objective owner, starting event, stopping event, required gates, source timestamps, missing-data rules, and tests for an unacceptable condition. A second analyst should be able to repeat the calculation and explain why an unknown result stayed unknown.

Useful retrospective measurements include time from detection to recovery authorization, time from restoration work start to technical readiness, and time from technical readiness to owner acceptance. Those are **phase measures**. Their sum does not automatically equal the entire outage unless their endpoints and intervals are continuous and consistent. The end-to-end measurement still uses its separately declared start and stop.

These measures can reveal process gaps. If technical readiness occurs promptly but business acceptance takes much longer, a team might need clearer data targets, approver availability or faster audit verification. It would be premature to blame one role without examining the milestone evidence. The exercise should produce a focused improvement ticket with an owner, a test and a review date.

[NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) describes the role of planned recovery testing and improvement in cyber resilience. RTE3's precise timeline and fixture arithmetic are original examples built to make that principle learnable at the rapid level.

### RTE3.15 Release integrity and conclusion boundaries

The canonical case's release boundary is not relaxed by this supplement. At 09:37, the learner has R1–R24 but **not** the later Branch S/P outcome or the separately released P1/C1 and V1 cards. R23 says the last backup job succeeded and the most recent documented restore test was thirty days earlier. It does not provide an interruption timestamp, accepted-service time or data-loss ledger. No canonical RTO or actual RPO result follows.

The K1 candidate timestamps and import durations belong only to their later classroom replay. P1/C1's four booking-state targets belong to a separate controlled comparison. V1's missing audit actor is a separate supplied test failure. MQ3's requests are invented queue rows. The RTE3 `W-A`/`W-B` events and artificial acceptance milestones may **not** be substituted for any of those records.

The practical success of this section is a student able to make three different statements without confusion: **"The copy is this old under verified timestamp assumptions"; "These specified accepted operations were or were not found in the tested recovered state"; and "The declared service was accepted after this measured interval, if all necessary receipts exist."**

If any input is missing, the conclusion must narrow rather than expand. Unknown timing is not proof of a target miss or target pass; unknown ledger completeness is not zero loss; and unverified service acceptance is not recovery completion.

---

## RTE3 Offline Laboratory — Measure Only What the Receipts Support

**Classification:** Entirely fictional, independent RTE3 exercise. The date, interruption time, snapshot label, W-A/W-B operations, readiness milestone, gate flags and owner receipt have **no relationship to R1–R24, K1, P1/C1, V1, W1, G3-DG, MQ3 or the Branch S/P cards**.

**Goal:** Under a declared 120-minute *hypothetical* RTO and 30-minute *hypothetical* RPO, calculate snapshot age, known uncovered accepted writes in a small certified fixture ledger and elapsed interruption-to-owner-acceptance time **only when justified**. Negative controls must handle a missing interruption timestamp, an old copy, a failed acceptance gate, no owner receipt, a known missing accepted operation, an incomplete ledger and an unverified clock.

**Environment:** Python 3 standard library, no files, network connections, accounts, personal data or service operations. All rows are reset independently.

### Inputs and step-by-step reproduction

The baseline's interruption is the invented 09:45 service failure on 2026-01-15 UTC; the copy is labeled 09:35, technical readiness is 10:20 and owner acceptance is recorded at 11:10. Required toy gates cover data comparison, permitted access, denied unauthorized operation and audit attribution. The declared accepted-operation set after the copy consists only of `W-A` and `W-B`; both are initially represented in the recovered set. A `ledger_complete=True` flag is an explicit **toy premise for that selected ledger**, not proof about all bookings.

Before running, predict the 85-minute accepted-service measurement; then predict which negative variants must refuse an RTO calculation or return unbounded data coverage. Copy the following into an isolated Python 3 session.

~~~python
from datetime import datetime
from copy import deepcopy

RTO_TARGET_MIN = 120
RPO_TARGET_MIN = 30
DAY = "2026-01-15"

def at(clock):
    return None if clock is None else datetime.fromisoformat(
        f"{DAY}T{clock}:00+00:00"
    )

BASE = {
    "interrupted": at("09:45"),
    "copy_at": at("09:35"),
    "technical_ready": at("10:20"),
    "accepted_at": at("11:10"),
    "clock_verified": True,
    "gates": {
        "data": True,
        "authorized": True,
        "denied": True,
        "audit": True,
    },
    "owner_receipt": True,
    "accepted_writes": {"W-A", "W-B"},
    "restored_writes": {"W-A", "W-B"},
    "ledger_complete": True,
}

VARIANTS = [
    ("BASELINE_ACCEPTED", {}),
    ("MISSING_INTERRUPTION", {"interrupted": None}),
    (
        "OLD_COPY",
        {
            "copy_at": at("08:50"),
            "accepted_at": None,
            "owner_receipt": False,
            "ledger_complete": False,
            "gates": {
                "data": None, "authorized": True,
                "denied": True, "audit": True,
            },
        },
    ),
    (
        "ACCEPTANCE_FAILED",
        {
            "accepted_at": None,
            "owner_receipt": False,
            "gates": {
                "data": False, "authorized": True,
                "denied": True, "audit": True,
            },
        },
    ),
    ("NO_OWNER_RECEIPT", {"accepted_at": None, "owner_receipt": False}),
    (
        "KNOWN_MISSING_WRITE",
        {
            "accepted_at": None,
            "owner_receipt": False,
            "restored_writes": {"W-A"},
            "gates": {
                "data": False, "authorized": True,
                "denied": True, "audit": True,
            },
        },
    ),
    (
        "INCOMPLETE_LEDGER",
        {
            "accepted_at": None,
            "owner_receipt": False,
            "ledger_complete": False,
        },
    ),
    ("UNVERIFIED_CLOCK", {"clock_verified": False}),
]

def measure(row):
    i, s, t, a = (
        row[key] for key in
        ("interrupted", "copy_at", "technical_ready", "accepted_at")
    )

    if s is None or i is None or s > i or not row["clock_verified"]:
        age = "UNKNOWN"
    else:
        minutes = int((i - s).total_seconds() // 60)
        age = (
            f"{minutes}m_"
            f"{'WITHIN' if minutes <= RPO_TARGET_MIN else 'OVER'}_"
            f"{RPO_TARGET_MIN}m"
        )

    missing = row["accepted_writes"] - row["restored_writes"]
    if not row["ledger_complete"]:
        data = "UNBOUNDED"
    else:
        data = f"{len(missing)}_KNOWN_UNRECOVERED"

    if i is None:
        rto = "UNKNOWN_INTERRUPTION"
    elif not row["clock_verified"]:
        rto = "UNKNOWN_CLOCK"
    elif t is not None and t < i:
        rto = "INVALID_ORDER"
    elif any(value is not True for value in row["gates"].values()):
        rto = "NO_ACCEPTANCE_GATES"
    elif not row["owner_receipt"] or a is None:
        rto = "NO_OWNER_ACCEPTANCE"
    elif a < i or (t is not None and a < t):
        rto = "INVALID_ORDER"
    else:
        minutes = int((a - i).total_seconds() // 60)
        rto = (
            f"{minutes}m_"
            f"{'WITHIN' if minutes <= RTO_TARGET_MIN else 'OVER'}_"
            f"{RTO_TARGET_MIN}m"
        )

    return f"age={age} unrecovered={data} RTO={rto}"

for label, changes in VARIANTS:
    row = deepcopy(BASE)
    row.update(changes)
    print(label, measure(row))

assert measure(BASE) == (
    "age=10m_WITHIN_30m "
    "unrecovered=0_KNOWN_UNRECOVERED "
    "RTO=85m_WITHIN_120m"
)
~~~

### Exact expected output — independently executed with Python 3

~~~text
BASELINE_ACCEPTED age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=85m_WITHIN_120m
MISSING_INTERRUPTION age=UNKNOWN unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_INTERRUPTION
OLD_COPY age=55m_OVER_30m unrecovered=UNBOUNDED RTO=NO_ACCEPTANCE_GATES
ACCEPTANCE_FAILED age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_ACCEPTANCE_GATES
NO_OWNER_RECEIPT age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_OWNER_ACCEPTANCE
KNOWN_MISSING_WRITE age=10m_WITHIN_30m unrecovered=1_KNOWN_UNRECOVERED RTO=NO_ACCEPTANCE_GATES
INCOMPLETE_LEDGER age=10m_WITHIN_30m unrecovered=UNBOUNDED RTO=NO_OWNER_ACCEPTANCE
UNVERIFIED_CLOCK age=UNKNOWN unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_CLOCK
~~~

### Worked interpretation of every scenario

**BASELINE_ACCEPTED:** The copy is labeled ten minutes before interruption, screening within the 30-minute hypothetical target. Both declared accepted-write IDs are present in the artificial restored set. All named gates and the owner acceptance receipt are supplied, so the calculated exercise interval is **85 minutes**, within its 120-minute hypothetical limit. This is **not proof of zero global loss or a real Harbor Library RTO/RPO pass**.

**MISSING_INTERRUPTION:** Without a defensible start event, the age at interruption and the outage-to-acceptance interval are unknown, even though the toy comparison of listed writes remains unchanged. The program does not substitute technical readiness or detection for the missing start.

**OLD_COPY:** The snapshot-age screen is 55 minutes, beyond the 30-minute hypothetical target. The declared accepted-write ledger is incomplete and the data gate is unknown, so lost data cannot be bounded and full acceptance is not measured. This is **not proof that 55 minutes of bookings were lost**. A separately verified journal or other source could alter the final recoverable point assessment.

**ACCEPTANCE_FAILED:** The copy is apparently ten minutes old and the two declared writes appear restored, yet the separate `data` acceptance gate is explicitly false. The gate could represent a different unacceptable data check not captured by those two operation IDs. The program refuses an RTO pass.

**NO_OWNER_RECEIPT:** The toy technical gates pass but no owner acceptance receipt or end timestamp exists. The stopping event remains unmeasured. Technical completion is not owner acceptance by default.

**KNOWN_MISSING_WRITE:** One of the two specified accepted operations is absent from the restored set, so the fixture identifies **one known unrecovered accepted operation**. This does not imply permanent loss or a complete organization-wide count. Acceptance is blocked pending approved investigation or replay.

**INCOMPLETE_LEDGER:** Every listed operation might appear restored, but the toy accepted-operation ledger is explicitly incomplete. The output `UNBOUNDED` means the exercise cannot bound additional missing accepted operations. An unknown is not a zero-loss finding.

**UNVERIFIED_CLOCK:** Copy age and outage elapsed time remain unknown because the declared clock-check premise is false. The two listed write IDs remain a separate toy comparison; their presence cannot repair the timing deficit.

### Lab limitations, safe negative controls and report template

The script uses artificial UTC-aware timestamps on a single fictional day and Boolean gate values. It does not collect a source, verify that an owner signed anything, reconcile a real database, ensure durable journal replay, test actual access controls, recover a live service or authenticate clock sources. It also assumes no unmodeled interval ambiguity and counts accepted IDs rather than evaluating every business effect.

Additional **optional negative controls** can be performed on a copied fixture: change `accepted_at` to precede `technical_ready`, or set `technical_ready` before `interrupted`. The expected status should be `INVALID_ORDER` when the contradictory condition is reached under the existing gates. Restore the baseline before recording the principal eight-line transcript. These are mathematical-input checks, not extra canonical incident injects.

The student should submit a matrix with scenario, start evidence, snapshot-age screening status, accepted-operation coverage, acceptance-gate status, computed elapsed duration or reason for refusal, and the next specific owner/source request. The successful measurement must state its **scope**, not merely the numbers.

**Lab pass criteria:** Reproduce all eight lines; explain why 85 minutes includes the complete fictional interruption-to-acceptance interval; identify the old-copy screening failure without inventing lost-data duration; explain why `UNKNOWN_INTERRUPTION`, `NO_ACCEPTANCE_GATES` and `NO_OWNER_ACCEPTANCE` are different; and keep RTE3 outside R1–R24, K1, P1/C1 and V1.

---

## Practical Activity — Build a Recovery Evidence Receipt

**Learning goal:** Turn a loose recovery statement into an auditable, owner-reviewable recovery measurement request.

**Inputs:** Use the RTE3 fixture and the pre-existing Chapter 03 objectives for context, but **do not** import the simulated W-A/W-B records into the canonical case.

**Steps:**

1. Write a one-sentence service acceptance scope, including the functions a user must perform and the operating restrictions, if any.
2. State who owns the outage-start definition and what evidence would establish the starting timestamp.
3. Name the planned technical-ready measurement and explain why it does **not** end the service outage under the selected contract.
4. Define four required acceptance gates: booking correctness, permitted action, prohibited action and actor/time audit result. Give each a result state and owner.
5. Name the owner-acceptance receipt and identify what happens if the owner rejects or does not respond.
6. For the data-point question, list claimed snapshot time, interruption time, post-snapshot accepted-operation ledger, restored operations, and the source that would establish completeness.
7. Calculate snapshot age separately from the accepted-service interval when both are supported. If either cannot be calculated, record the missing source and do not substitute a guess.
8. Provide a short handoff with the planned next observation, decision owner and explicit no-production-change boundary.

**Expected artifact:** A Markdown table headed `RTE3 recovery evidence receipt`, followed by one paragraph interpreting an age-only result and one paragraph interpreting a measured acceptance time. State the limitations of every figure. Do not call a copied example a completed test unless the learner executed it.

**Evaluation:** Full credit requires distinguishable start and stop conditions, independently supported acceptance gates, age-versus-loss separation, explicit missing-data states, source attribution and permission boundaries. A paper calculation alone does not prove a restore occurred.

---

## Targeted Refinements to Existing Exercises — Preserve EX033, EX034, EX035

These additions **do not create new exercise IDs** and do not change the existing 0–2 scoring scale. Preserve the book's original Chapter 03 prompts, the separate P1/C1 and V1 card release rules, and the final worked-answer appendix.

### EX033 — Recovery test: add a complete service-time measurement contract

**Additional instruction:** Extend the original one-paragraph isolated-copy plan with a separate, compact measurement card naming (a) the owner-defined *service interruption start* and source, (b) isolated restoration start and technical-ready times, (c) the booking, access and audit gate receipt fields, (d) the owner acceptance timestamp and scope, and (e) the rule for declaring elapsed time **unknown**. The existing B17–B20 target table remains `not tested` until the relevant later card and actual isolated result are supplied.

**For 2 points:** A plan with no actual outage or acceptance timestamps does not report achieved RTO. The learner distinguishes proposed and executed steps, remains within an authorized isolated environment and does not infer an accepted service from a copied test plan.

### EX034 — Backup limit: separate age screening, effective recovery point and proved loss

**Additional instruction:** Keep the existing midnight-to-09:45 arithmetic and hypothetical 30-minute RPO/120-minute RTO. Add three explicit columns: **copy age screen**, **accepted-transaction evidence after the copy**, and **actual restored/verified transaction result**. Ask whether any record proves a specific legitimate write was irrecoverably lost. If the accepted ledger, replay evidence or clock semantics are missing, record **unknown**, not "9 hours 45 minutes of data lost."

**For 2 points:** Correct age arithmetic must be paired with an appropriately limited inference. R23 supplies only a backup-job status and old restore-test record, not interruption, service acceptance, actual recovered point or measured data loss. An isolated import duration alone is not a service-level RTO.

### EX035 — Return-to-service: separate gate result, timing and owner receipt

**Additional instruction:** Retain the original booking-correctness, permitted/denied access and audit acceptance conditions and the conditional Branch P queue gate after its proper release. Add an **acceptance-time evidence row**: actual interruption timestamp/source, last passed mandatory gate, owner acceptance (or rejection) timestamp, scope and outcome. If P1/C1 or V1 reports a failed gate in its later isolated test, explain why no full-service recovery completion time is established by those cards.

**For 2 points:** Do not turn the existing V1 limited access results into a completed restore, turn a blank actor into a pass, treat a pending queue as reconciled, or report a measured RTO without comparable start/end receipts and owner-approved acceptance.

---

## Supplementary Worked Answers — To Be Consolidated in the Principal Book's Final Appendix

### EX033 — Additional worked reasoning

At the canonical 09:37 Chapter 03 decision, R23 reports backup-job success and a restore test documented thirty days earlier; it does **not** supply an interruption time, isolated restoration, accepted target result or owner-accepted service. The correct plan identifies a named candidate copy and recorded time *to be collected*, an authorized isolated environment and the data, access and audit checks required before an owner may accept any returned service. The added measurement card defines a scoped service-interruption event as the intended start, technical readiness as an intermediate milestone, and signed or recorded owner acceptance after required gates as the intended stopping event. Its actual times remain `not measured`. P1's B17–B20 target values may be used **only after its later card release**, and V1 remains a separate isolated-copy access/audit trial. Neither substitutes for a measured full service recovery. A 2-point answer refuses to turn a planned isolated import or a successful backup job into a reported RTO result.

### EX034 — Additional worked reasoning

The original hypothetical midnight copy at 09:45 is **9 hours 45 minutes old**, exceeding the illustrative 30-minute point target by **9 hours 15 minutes** when screened as a stand-alone copy. That arithmetic is not a measurement of accepted booking data actually lost. The actual count and earliest missing accepted time require a defined accepted-write source, verified coverage, any protected replay journal and an authoritative restored-state comparison. A gap in one source might prevent completeness assurance without proving permanent loss; an identified accepted operation missing from a tested recovery candidate is a narrower known discrepancy, not necessarily irrecoverable. R23 does not contain the required event/restore/acceptance times, and K1's separate trial import durations of 11 and 14 minutes do **not** establish a service outage duration. The hypothetical two-hour RTO cannot be marked achieved from these inputs.

### EX035 — Additional worked reasoning

Only after the later P1/C1 and V1 releases, the supplied comparison shows B19/B20 differing from the approved P1 targets while V1 reports limited permitted/denied access tests and a **failed audit actor field**. Those are separately scoped results, and they do not establish full service acceptance. The relevant acceptance-time row therefore states: interruption start/time **not supplied for an actual completed Harbor Library recovery**, required data and audit gates **failed or unverified**, accountable service-owner acceptance **not supplied**, and service-level elapsed recovery **not measurable**. A later restricted-mode proposal would need its own declared service scope, approver, restrictions and accepted decision time; it cannot turn existing failed gates into passes. If Branch P was separately chosen, its two pending queue items remain unresolved until their own owner-approved dispositions are evidenced. RTE3's artificial 85-minute interval is a different exercise and cannot be substituted for a canonical Harbor Library completion time.

---

## Section Synthesis, Navigation and Sources

A recoverable copy, a short import, an owner-approved service and a valid recovery objective are distinct concepts. To measure interruption-to-service-acceptance time, define the user-facing service, verify the start event, keep intermediate readiness tests separate, require all mandatory acceptance evidence and record the owner's decision as the scoped stop event. To discuss the recovery point, screen timestamp age but separately establish what accepted business changes are recoverable, missing, unverified or outside source coverage.

RTE3 is deliberately fictional and offline. Its results do not change the canonical Harbor Library chronology, the separate K1/P1/C1/V1 evidence or the public book's completion status.

### Continue studying — chapter 03 of 04 (supplementary public draft)

[← Chapter 02](../MANUSCRIPT.md#ch-02) · [Course chapter index](../../SUBJECTS.md) · [Chapter 04 →](../MANUSCRIPT.md#ch-04) · [Worked answers](../MANUSCRIPT.md#answers)

**Editorial integration note:** This file is a **transitional public component** of the one principal English book, not an additional numbered chapter. Its new teaching and EX033–EX035 refinements should be reviewed and incorporated into the single `MANUSCRIPT.md` by the maintainer. No index, skill, generated progress report, A4 preflight record or private Engine file is modified by this draft.

### Verifiable official primary sources

- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Final May 2010, updated November 2010; business impact analysis, recovery priorities and objectives.
- [NIST CSRC Glossary — Recovery Time Objective](https://csrc.nist.gov/glossary/term/recovery_time_objective). Official term definition, referring to SP 800-34 and other NIST sources.
- [NIST CSRC Glossary — Recovery Point Objective](https://csrc.nist.gov/glossary/term/recovery_point_objective). Official term definition and source references.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final). Final December 2016; planned recovery, realistic exercises, metrics and improvement.
- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; incident response and recovery within organizational risk management.

These sources support **general technical methods and terminology**, not the invented Harbor Library or RTE3 event times, acceptance gates or exercise results. The teaching is original; no third-party text has been copied. Editorial responsibility belongs only to [hiagokinlevi](https://github.com/hiagokinlevi). Maintainer-owned original CyberABC material follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE), while third-party sources retain their rights. This document does not authorize real service tests or claim that the book is complete.
