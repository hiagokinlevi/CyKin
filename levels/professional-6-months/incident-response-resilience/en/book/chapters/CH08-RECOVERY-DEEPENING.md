# Chapter 08 supplementary teaching component — Data reconciliation, acceptance gates, and monitored return

> **Editorial status: PUBLIC DRAFT — TRANSITORY COMPONENT, NOT AN ADDITIONAL CHAPTER.** For eventual integration into the single [Chapter 8 professional English manuscript](../MANUSCRIPT.md#ch-08). No canonical chapter, exercise ID or worked answer is replaced by this file. Cedar Training Network (CTN) cards are synthetic educational records; the offline lab touches no external system.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). The scope of original-work dedication and third-party rights is set by [RIGHTS.md](../../../../../../RIGHTS.md).

## Outcomes, initial situation and release discipline

A learner completing this extension can (1) distinguish a valid backup from a correct business recovery target; (2) reconcile a small state set while protecting later authorized transactions; (3) design non-negotiable recovery acceptance criteria; (4) distinguish isolated tests, production authorization, operator action, immediate verification and monitored owner acceptance; (5) identify the recovery boundary of a rollback; and (6) justify the existing EX036–EX040 worked results.

The entry state is **10:07 UTC**, not an already recovered service. By then C24 reports sync-override disabled, but only a short observation interval supports that state. The C21 S42-only hold expires at 10:07 after a documented 10:06 decision not to renew it. C22's unapproved recovery-method issue is still open at this exact instant. The service owner uses read-only monitoring with an escalation trigger for a new unexpected edit. **Do not import C25–C30 into a 10:07 decision record.** Their later release points provide new evidence and separate permissions.

### 8.A A backup is an artifact; the recovery target is a governed statement

Many mistakes in response recovery result from confusing **artifact validity**, **restore feasibility**, **business correctness** and **operational acceptance**. They are four independent questions.

Artifact validity asks whether a received backup corresponds to its expected bytes and metadata. A digest match supports byte consistency with the named baseline, but it cannot prove the backup captured all relevant rows, that the operator selected the correct time, or that the stored information reflects the organization's desired business state. Restore feasibility asks whether the backup can be loaded in a compatible and authorized isolated environment. Business correctness asks whether its values comply with the current approved transaction history. Operational acceptance adds application behavior, security logging, access dependencies, user impact and monitoring.

C26 supplies a documented **08:30** snapshot with a matching digest and an isolated read. The snapshot contains S40=open, S41=open and S42=open. At **10:12**, the current owner-scoped state is S40=reserved, S41=reserved and S42=unavailable. The S40/S41 reservations are legitimate later changes under the approved 08:50 work. Therefore blindly restoring the older snapshot would appear to fix S42 while undoing two authorized reservations. A hash that validates a wrong-business-state artifact cannot transform it into the correct target. An operator must compare the snapshot's age and values with the owner-approved current intent, not merely its filename or creation time.

The business target for this synthetic decision is S40=reserved, S41=reserved, S42=open. This target is not inferred from the most recent timestamp or the analyst's personal preference: the **service owner approves it**. An entry-level practitioner should record source versions and change relationships before proposing to edit values. If the owner cannot confirm which later transactions remain valid, pause and request a bounded reconciliation; do not choose a restore point by visual appeal.

[NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) emphasizes planning, testing and improvement in cybersecurity recovery. The CTN three-slot transaction example and proposed gate are original teaching devices, not NIST-prescribed recovery parameters.

### 8.B Construct a state-difference argument with a loss ledger

For each candidate state, list every field that differs from the approved target. The test is **not** simply “Does S42 appear open?” The candidate that recovers S42 but regresses S40/S41 is a partial and dangerous repair. A useful ledger records target value, baseline version/source, current value, proposed value, business authority, intended preservation and rollback reference.

The three candidate strategies have different failure signatures:

| Strategy at 10:12 | Known effect on supplied three-slot fixture | Main unacceptable or unresolved outcome |
|---|---|---|
| Restore the entire 08:30 snapshot | S42 becomes open; S40/S41 would become open too. | Loss of later authorized S40/S41 reservations; wrong business result. |
| Leave state unchanged | S40/S41 remain reserved; S42 remains unavailable. | The reported enrollment functionality remains wrong. |
| Reconcile only S42 to approved open state | Preserves correct S40/S41 fixture values while targeting S42. | Needs strict version control, an authorized application path, audit tests, service dependency checks and rollback. |

The targeted strategy wins this specific comparison, but it is **not** universally safer than restoration. A real application may have cross-record invariants, queues, enrollment counters, caches, foreign-key relationships or transactional consistency constraints that a single-field adjustment would violate. The professional responder asks the data and application owners how the **logical transaction** is represented and which writes are atomic. A one-row change outside the application may bypass audit hooks and create a new failure. The learning target is an owner-approved, isolated-testable reconciliation—not an instruction to modify a database manually.

A useful dry-run precondition is: “Current S42 version still equals the captured pre-change version; otherwise abort and re-evaluate.” That is analogous to optimistic concurrency control. Without a version check, another legitimate update arriving after the 10:12 snapshot could be silently overwritten. The case does not provide evidence of such a race; the precondition is a **general design safeguard** proposed for a real implementation review, not a historical CTN event.

### 8.C Identity readiness and service readiness are coupled but not identical

At **10:11**, C25 reports a separately approved 10:08 identity-owner/service-owner decision: remove the unapproved recovery method, perform a scoped credential change and revoke s-77. The identity operator reports completion at 10:10; a fresh status check at 10:11 finds **s-77 inactive**. This is a specific identity-track result, not evidence of universal account compromise or universal account safety. It also does not automatically prove approved batch-17 will work with an updated credential path.

Recovery introduces a dependency: restarting scheduled enrollment when the integration credential has changed can produce an avoidable outage or prompt operators to restore an old secret unsafely. Therefore the acceptance contract includes a negative control: legitimate batch-17 must continue through its **approved** authentication path, while suspect access does not regain access merely because the app is restarted. A successful scheduled job is relevant to availability, but not by itself a proof that every unauthorized session is gone. Conversely, s-77 inactive is valuable but cannot substitute for S42 data correctness or audit completeness.

Another dependency is the event trail. The C27 first isolated candidate passes the proposed slot values and manual enrollment function, yet its alternate API-route audit record has a **blank actor field**. If the owner-defined gate requires useful audit actor and request fields, the correct decision is **no-go** even if the visible page works. The test result must remain in the record; an engineer must not silently redefine “good logging” to mean “any log line exists” after seeing a failure.

### 8.D Design the gate before the experiment

An acceptance gate is a contract agreed **before** the outcome is known. For this component, five criteria are mandatory: (1) the three slot values match approved intent; (2) both manual and scheduled routes behave correctly; (3) new audit events include required actor and request identifiers; (4) the original evidence and its provenance remain preserved; and (5) a rollback checkpoint and owner exist. For any absent or failed mandatory criterion, the decision is **stop for review**. A percentage score is useful for diagnosing test coverage, but it must not replace the stop rule.

At **10:16**, C27's first isolated run reveals the missing alternate-route audit actor. It is a **failed acceptance test** despite data correctness and a successful manual path. This is not proof of an exploited vulnerability or malicious tampering; it is a failure against a deliberately declared recovery criterion. At **10:20**, C28 records an application-owner audit-mapping adjustment in isolation and a rerun where slot targets, both service routes, the new audit fields and rollback copy meet the supplied gate. The outcome is **isolated candidate pass**—not an implemented production change.

In real operations a pass in a rehearsal is conditional on the fidelity of the test environment: schema versions, dependency mocks, test identities, feature flags, clock and notification routing may differ from production. Describe what was simulated and what was not. A worker that succeeds against an in-memory stub may still fail with the real queue, credential rotation or network path. The owner decides whether remaining differences permit a guarded production change; this book does not declare that an isolated pass authorizes production automatically.

C29 supplies the missing operational decision as an independent case record: at **10:24** the service owner and incident lead approve a bounded S42 correction and staged restart; at **10:26** the authorized operators report performing it. At **10:30** read-only checks show intended S42/S40/S41 values, approved batch-17 function and useful new audit fields. This is early operational verification over a four-minute window. It is incorrect to relabel C28's isolated result as C29's approval or to promote C29's 10:30 first checks directly to sustained acceptance.

### 8.E Rollback is a transaction to be justified, not a magical undo button

A rollback has its own **trigger, authority, scope, expected effect, evidence and test**. If a C29 staged change produces wrong slot values, a failed legitimate route or a blank new actor field, the owner should stop advancement and ask the designated operator to invoke the approved recovery path. Before rollback, preserve enough evidence of the failed state to diagnose what happened. If the rollback itself would erase more recent legitimate changes, it needs another reconciliation decision rather than blind execution.

Distinguish **configuration rollback** from **business-state rollback**. Restoring a prior configuration may reinstate application behavior without restoring lost reservations. Restoring a prior data snapshot may alter current business state. Neither action can retroactively retract messages already delivered or restore historical logging fields that were never collected. The rollback operator should report the exact version changed, the post-action state and observed business checks. The incident lead should record whether security monitoring and identity controls remain effective after reversal.

C30 adds the owner acceptance that C29 lacked. At **10:45**, a 15-minute monitored interval reports no unexpected S42 edits or scheduled-job failures **in the observed sources**. The service owner accepts **limited return to service** and assigns two more hours of monitoring. Do not rewrite “two hours assigned” as “two hours completed,” or “no unexpected edits observed” as “no other path could ever edit S42.”

There is a valid measurement from the **09:04 support ticket receipt to 10:45 owner acceptance**: 101 minutes. There is no supported claim that CTN met or violated an RTO, because no approved objective is supplied. Similarly, the 08:30 backup's age does not equal actual data loss; the chosen targeted reconciliation deliberately preserves later authorized S40/S41 reservations. Service targets and denominators have to be defined by the service owner before a performance claim is credible.

### 8.F Correct recovery recommendation and a deceptive alternative

**Correct recommendation after C26 and before C27:** “Use the 08:30 snapshot as a preserved reference, not as the immediate full restore. The owner-approved target is S40/S41 reserved and S42 open; the snapshot would erase valid S40/S41 changes. Request permission for an isolated, version-checked S42 reconciliation that preserves other slots and can produce required audit data. Preannounce mandatory two-route, audit, preservation and rollback tests. If any fail, stop and revise the candidate before a separately approved production change.”

**Incorrect recommendation:** “The snapshot digest matches, therefore restore it wholesale. If the webpage works, close recovery and send an all-clear.” A valid digest has no knowledge of the correct business target. A webpage check omits the alternate route, the scheduled job, the required audit field, rollback and monitored acceptance. An “all-clear” also conflates service readiness with unknown human attribution and later privacy assessment. The correct decision is more constrained even though it may require greater coordination.

### 8.G Offline laboratory: candidate mismatch and mandatory gate

**Goal:** compute exact slot mismatches and distinguish a failed acceptance gate from a passing one. **Inputs:** synthetic owner target, 08:30 copy, 10:12 current state, and two isolated acceptance checklists. **Safe execution:** Python 3 only; no file or network access; the gate dictionaries are modeling assumptions. **Evaluation:** the two mismatches and two pass/fail labels must match the recorded output, and the learner must explain why C28 cannot independently authorize production.

~~~python
target = {"S40": "reserved", "S41": "reserved", "S42": "open"}
candidates = {
    "snapshot": {"S40": "open", "S41": "open", "S42": "open"},
    "current": {"S40": "reserved", "S41": "reserved", "S42": "unavailable"},
}
for name, state in candidates.items():
    gaps = [key for key in sorted(target) if state[key] != target[key]]
    print("C8", name, "mismatch:", ",".join(gaps))

checks = {
    "C27": {"data": 1, "manual": 1, "scheduled": 0, "audit": 0, "rollback": 1},
    "C28": {"data": 1, "manual": 1, "scheduled": 1, "audit": 1, "rollback": 1},
}
for name, result in checks.items():
    print("C8", name, "GO" if all(result.values()) else "NO-GO")
~~~

**Executed output:**

~~~text
C8 snapshot mismatch: S40,S41
C8 current mismatch: S42
C8 C27 NO-GO
C8 C28 GO
~~~

The flags are **synthetic summaries** of the specified isolated checks, not measurements of a live application. In particular, the C27 scheduled value 0 means “not established as passing in this modeled gate,” not a newly discovered C27 scheduled-job failure. The C28 “GO” means **isolated gate passes**; it says nothing about authorization or production deployment. The fixture omits concurrency, user permissions, transaction invariants and actual audit content by design. The learner must retain those limits.

### 8.H EX036–EX040: enriched reasoning and answer criteria

These are supplementary rubrics and worked-result explanations for existing IDs only.

**EX036 — candidate ledger extension.** Add a “lost legitimate state” column. Model answer: whole snapshot passes historical-byte consistency but would regress S40/S41; no change preserves those valid reservations but leaves S42 unavailable; targeted S42 reconciliation best matches the owner-approved three-slot target **if** app-level integrity, authorization, two-route audit and rollback gates can be met. A strong answer names a source of possible disagreement (for example, a changed version or cross-record invariant) rather than asserting the single-slot technique always safe.

**EX037 — mandatory gate extension.** The model evaluator records C27's blank alternate-route audit actor as a **failure of mandatory criterion 3**, with other tested features retained as observations. Therefore isolated **no-go**. C28 subsequently supplies a passing isolated retest with both routes, required fields and a rollback copy. Therefore **isolated pass** subject to separate production approval. The student should not average failures away or attribute C29's 10:24 authority to the 10:20 rehearsal.

**EX038 — output extension.** The executed fixture has snapshot mismatches S40,S41 and current mismatch S42. Worked implication: restoring the snapshot would overwrite two legitimate reservations; a bounded change could address the one shown mismatch but cannot be executed solely from a set comparison. Ask the learner to write one concrete stop condition: “If S42's source version differs from the preserved precondition at operation time, stop and obtain a new owner-approved reconciliation.” This is a proposed safety design, not a fact about a CTN race.

**EX039 — acceptance timeline extension.** Require distinct records: 10:24 approved; 10:26 action receipt; 10:30 first production observations; 10:45 fifteen-minute monitoring and limited service-owner acceptance; two additional hours **scheduled**, not finished. Worked trigger: wrong S42 value, changed S40/S41 reservation, failed approved batch-17 route or missing new audit field triggers stop and owner-directed rollback review. An excellent response identifies which person/role must decide, operate and independently check rather than collapsing these into one status line.

**EX040 — handoff extension.** State that the whole C26 restore was unsuitable to the business target, C27 failed a mandatory audit gate, C28 passed only in isolation, and C29/C30 supplied distinct production change and limited return evidence. Carry forward C25's narrow identity observation, the unknown actor, earlier provenance limitations and ongoing monitored review. The 101-minute ticket-to-acceptance interval must be labeled with endpoints and cannot be called an RTO achievement. A full-score handoff lets a second responder identify the next checkpoint and exact reopening conditions without assuming the incident closed.

### Limits, synthesis, and primary sources

The lab is a finite synthetic value comparison. It verifies no real recovery, no production state, no authorization and no regulatory target. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) is a primary planning/testing source for cyber recovery. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) gives broader incident-management context. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides background on provenance and evidence handling, with its older technical scope and explicit legal-advice limits.

**Synthesis:** a valid backup may be the wrong business recovery. A passing isolated test may still be the wrong authorization state. A verified production check may be too short for owner acceptance. Recovery requires the correct target, a declared stop gate, a controlled and witnessed action, then appropriately scoped acceptance and follow-up.

### Continue studying — supplementary component for chapter 08 of 12

[← Chapter 07 (authored draft)](../MANUSCRIPT.md#ch-07) · [Course chapter index](../../SUBJECTS.md) · [Chapter 09 (authored draft) →](../MANUSCRIPT.md#ch-09)

The [principal Chapter 08](../MANUSCRIPT.md#ch-08) retains the original exercise statements, and the [book's worked-answer appendix](../MANUSCRIPT.md#worked-answers) retains canonical answer numbering pending integration.
