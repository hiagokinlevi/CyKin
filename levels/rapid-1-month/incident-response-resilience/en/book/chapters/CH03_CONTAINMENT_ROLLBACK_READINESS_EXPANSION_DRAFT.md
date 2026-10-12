# Incident Response and Cyber Resilience — Rapid Course

## Chapter 03 Expansion Draft: Preparing and Verifying Containment Reversal

**Editorial status:** **Public transitional English instructional component** for Chapter 03 of the **single principal book**. This is not a separate fifth chapter, a completed volume, or evidence of a real containment operation.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 03 — Containment, eradication and recovery decisions](../MANUSCRIPT.md#ch-03).  
**Specific learning gap:** How to prepare, authorize, execute and **independently check a bounded reversal of containment** when the intervention harms legitimate service or demonstrably fails its protective purpose.  
**Preserve rather than repeat:** The Chapter 03 W1 write-path probe, G3-DG status gates, MQ3 manual-queue replay, RTE3 recovery timing, the existing four-step action record, and all canonical exercise and answer identifiers. The new **RB3** model below concerns *reversal readiness and post-reversal evidence*, not the underlying write-route implementation or end-to-end service restoration.

> **Scenario and safety boundary:** Harbor Library is fictional. At 09:05 only R1–R8 are available; R9–R16 arrive at the 09:20 Round B review; R17–R24 arrive in Round C before the 09:37 proposal. **No R1–R24 item records the execution or reversal of a containment control at 09:37.** Branch S and Branch P are alternative later Round D cards, while P1/C1 and V1 are separately released later. W1, G3-DG, MQ3 and RTE3 are independent classroom fixtures. **RB3 is yet another isolated synthetic variant**, using a different fictional date, fake configuration IDs, abstract observations and fictional roles. No RB3 event may be attached to the canonical timeline or used to justify an earlier Harbor Library decision.

# Chapter 03 — New Teaching: Reversal of a Harmful or Ineffective Control

### 3.RB1 Containment introduces a second risk that must be managed

Containment is intended to limit a particular harmful path. It can simultaneously interrupt ordinary work, prevent approved users from accessing a necessary function, or fail to block the activity the incident team intended to stop. A team that can enable a control but has no prepared way to reconsider or reverse it may turn a temporary protective measure into a prolonged service problem.

The existing §3.3 compares current-session revocation, a short staff-write pause and observation. It already identifies business costs and possible fallbacks. This expansion addresses the next, distinct question: **if a selected intervention produces unacceptable side effects or fails its expected protection, what evidence and authority are needed to reverse that intervention without silently reintroducing the original risk?**

A reversal can involve restoring an earlier configuration, stopping a temporary restriction, replacing a control with a narrower one, or moving to a separately approved operational mode. The word **rollback** is useful, but not every action can be literally undone. A revoked identity session may need a new, appropriately verified authentication procedure; restoring an old configuration may reintroduce the same vulnerability that containment was intended to address. Undoing an emergency pause may permit writes again without proving that the original suspicious edit path is now safe.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) connects incident response and recovery with risk management throughout an incident. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) addresses planned recovery, testing and improvement. These sources support careful planning and evaluation; the precise **RB3 reversal contract** is an original CyberABC teaching construct, not a mandatory NIST workflow.

### 3.RB2 Write down the purpose of reversal before selecting a command

The phrase "undo the containment" conceals at least two different reasons for taking action.

**Service-harm trigger.** The response team has a reliable, scoped observation that the control disrupted legitimate work beyond the accepted operating limit. For example, a fictional short staff-write pause may unexpectedly interfere with an essential permitted function. The proposed next step is not automatically "remove all protection"; it may be to restore that function under a narrower, separately approved safety condition.

**Protection-failure trigger.** A credible post-action test finds that the targeted harmful activity remains possible in the declared control scope. A responder might reasonably request replacement, correction or withdrawal of an ineffective control. However, reverting without an alternative could make the situation worse. The team needs to compare the present control, proposed reversal and remaining safeguards.

Both triggers need an **observable condition** and a source that could be challenged. "The desk is unhappy" is not the same as a verified failure of the service owner's accepted requirements. "The logs are quiet" is not proof that protection worked if no meaningful attempt or source coverage was established. A negative result can be informative only within the test's inputs and scope.

The intervention decision and the reversal decision are separate. Even if a change was previously approved, its inverse need not be automatically approved. The risk has changed, the available evidence may have changed and the accountable owner must understand the new tradeoff.

At rapid level, the learner should describe the trigger in operational language: **which function or expected protective result failed, how was that observed, and what is the narrowest next decision it justifies?**

### 3.RB3 Establish a verified pre-intervention state, not an idealized past

A useful reversal plan starts **before** applying the original control. It records the last verified configuration or state relevant to the proposed change: the affected component, configuration version, tested legitimate service behavior, observed protective posture, dependencies, owner and source of the baseline record.

The phrase "restore the old settings" is unsafe without a trustworthy target. The old version may be missing, incomplete, incompatible with a newer dependency or already known to permit the harmful behavior. A baseline should be an identifiable, owner-reviewed **candidate for return**, not a promise of correctness.

The baseline card should answer:

| Baseline question | Required evidence or limitation |
|---|---|
| What exact object was checked? | Specific setting, session-control scope or configuration identifier |
| When and where was it checked? | Controlled source, environment and timestamp |
| What legitimate function passed? | Owner-defined permitted operation and measured result |
| What protection was present? | Narrow existing safeguard, if observed; unknown elsewhere |
| What was saved? | Authorized configuration reference or approved restoration procedure |
| What may have changed since? | Dependency or state differences requiring fresh verification |
| Who can approve returning? | Current accountable decision role, separate from the operator |

For a service that has been changing during an incident, simply replaying a saved configuration may be inappropriate. A baseline can be **known at capture time** yet not safe to reapply later. The reviewer must check its current applicability and the intervening system changes.

The RB3 lab uses the entirely invented identifier `CFG-GOOD-7` and a Boolean `baseline_verified`. Neither is evidence that a real baseline exists. The positive fixture models the discipline of requiring a known starting reference; it does not check the contents or authenticity of an actual configuration.

### 3.RB4 Define the original intervention as an exact bounded change

A reversal can only be compared with an intervention if the first change is itself traceable. The original action record needs its own proposal, approval, object scope, effective window, operator receipt, expected protection and service impact. Otherwise the team may not know what needs undoing.

Suppose a containment proposal affects only a synthetic `staff-write` service function. A later reversal may legitimately aim to restore only that function. A request to alter `identity` settings at the same time would be an **expanded action**, not an automatic inverse of the original. That expansion requires separate justification and authorization.

The RB3 fixture represents the original control as `CTRL-PAUSE-9` with affected scope `staff-write`. Its fictional prior approval is a declared input. The baseline restoration target is `CFG-GOOD-7`. These labels are not Harbor Library configuration IDs.

An implementation plan should preserve both **what the operator intended to change** and **what was actually reported changed**. A control may be applied partially or to the wrong object. In that situation, executing a generic inverse could affect components the original operation never reached.

The safe preparation step is to identify a precise rollback target and its permitted scope, plus a stop condition if the current state no longer matches the assumptions in the plan. A preapproved recipe for the wrong current environment is not automatically safe.

This is deliberately different from W1, which checks specific write routes under a pause. RB3 does not inject writes, run a gateway test or determine whether W1's legacy route was blocked. It checks whether the **proposed inverse** has a reviewable evidence chain.

### 3.RB5 Approval must name the reversal, its window and its business cost

A rollback request should identify the specific control being reconsidered, the intended target state, the components or functions affected, the justification, the risks reintroduced and the authorization window. An approval for the original pause does not necessarily approve ending that pause, and R21's tolerance statement cannot be used as approval for any live change.

The accountable owner for a service-affecting reversal may be the service owner under the applicable fictional governance rule, coordinated with the incident lead. Identity owners may be needed if the intervention concerns authentication rather than a staff-write setting. The operator applies the change only after the relevant decision; the reviewer checks the result independently.

For a clear approval record, name the **operation**, not merely the ticket: "revert the specified synthetic staff-write control to the reviewed candidate state within the defined window, subject to the stated protective and business checks." The record should include:

- The approved target and exact component/function set.
- The allowed start/end of execution, using an agreed clock.
- The decision owner and the operator.
- The triggering evidence and reason for reversal.
- The business impact expected if the inverse is performed.
- The compensating safeguard that should remain effective.
- The post-reversal verification, reviewer and failure response.
- The planned human reassessment, even if the initial check passes.

A missing or expired approval is a **hold condition**, not a license to treat urgency as permission. If immediate harm creates a real emergency, an organization might have a separately governed emergency change procedure; the training exercise does not invent such powers.

RB3 checks a small fictional approved window, 14:05–14:25 UTC on an entirely invented date. The clock is a consistency input, not a measured Harbor Library outage or recovery objective.

### 3.RB6 Specify a trigger that can be falsified

The team should be able to say what observation would cause a planned reversal to be requested and what observation would show that the trigger did **not** occur.

For a **service-harm trigger**, an owner-approved isolated measurement might show that a previously permitted legitimate task is now unavailable *because of the controlled change*, beyond accepted limits. The analyst should compare the affected service function with its baseline and account for other possible causes. If the function was already unavailable before the intervention, a post-action failure cannot by itself establish that the control caused the problem.

For a **protection-failure trigger**, an approved, bounded post-action check may show that the threat path remains available under the tested scope. The team should not interpret a quiet or incomplete log as a successful block. Equally, an unrelated failure does not prove the targeted protection failed.

A valid trigger record should name:

1. The condition being tested.
2. The source and input of the observation.
3. The time and operating scope.
4. The expected result and observed difference.
5. The custodian or owner confirming the relevant semantics.
6. A limit: what the observation cannot establish about other routes or business outcomes.

The RB3 fixture uses either `SERVICE_HARM` or `PROTECTION_FAILURE` as the artificial trigger kind, with a corresponding training receipt. These are **declared exercise observations**, not detector outputs or events added to R1–R24.

The negative variant `TRIGGER_NOT_OBSERVED` deliberately removes the supporting observation. The validator then refuses to convert a plausible rollback proposal into an executed action.

### 3.RB7 Proposed reversal, approved reversal, executed reversal and checked effect

The same action-state discipline used elsewhere in Chapter 3 applies to the reversal **as a new operation**. A team should not merge the original control ticket with the inverse action and then declare both successful.

| Reversal stage | Narrow supported claim | What must remain blocked |
|---|---|---|
| Proposed | The team identified a bounded inverse candidate and reason | Claim that permission was granted |
| Approved | The appropriate owner accepted scope, timing and risk of the inverse | Claim that the operator executed it |
| Execution reported | A named operator recorded what was changed, target and time | Claim that intended effect occurred |
| Post-state checked | An independent or appropriately authoritative check evaluated the selected result | Claim that the full incident is recovered |
| Human review open | Residual protection/business questions have accountable owners and next decision | Automatic closure without case review |

The order matters. A ticket with a return configuration attached is still a plan. An approval receipt is still not an execution receipt. A command or workflow reporting success may have operated on the wrong object, changed only one dependency or left the actual service in an unexpected state.

RB3 adds a **specific target-matching check**. Its execution receipt must refer to the declared candidate configuration rather than an unrelated version. A variant with an execution receipt for `CFG-UNKNOWN` must fail even if the other synthetic status flags are positive.

After execution, the team needs an observation of the resulting state and two different acceptance checks. Those are discussed next. The presence of a receipt does not replace the effect observation.

This section does not repeat G3-DG's generic decision-gate tutorial. It applies those distinctions to the **risk-bearing inverse operation**, including the verified baseline, trigger and competing post-reversal outcomes.

### 3.RB8 Verify protective behavior **after** rollback, not just restored availability

Removing a disruptive restriction may restore legitimate service while also reintroducing the harmful path that containment was intended to limit. A successful rollback command is therefore not sufficient, and even a successful booking operation may be too narrow.

The post-reversal **protection check** asks: *Under the new, declared operating mode, what prevents or detects the selected unacceptable action, and what bounded observation supports that claim?* The original control may have been removed, so the reviewer cannot simply require the exact same control to remain enabled. Instead, the service owner and security lead must define an **acceptable residual protection condition**, perhaps through a narrower approved safeguard or restricted mode.

A failed protection check means the reversed system cannot be called acceptably protected **for the tested purpose**. It does not always mean the inverse had no technical effect. It can mean that legitimate service resumed but the protective risk is unacceptable.

The RB3 negative case `PROTECTION_REGRESSED` models that outcome. It returns `PROTECTION_NOT_ACCEPTED` even when an execution receipt and a positive legitimate-service check are present. This prevents the seductive conclusion "rollback succeeded because the desk can work again."

Do not interpret this as a universal instruction to keep every harmful control in place indefinitely. The accountable owners must balance risks and may select a different approved containment strategy or restricted service mode. The lesson is to **document and verify that tradeoff**, not to choose the outcome for them.

No real security-control test is performed in RB3. The `protection_check` field is an invented Boolean and cannot establish that a live system is safe.

### 3.RB9 Verify legitimate service after rollback, not merely configuration identity

The inverse operation may report that a previous configuration was restored while the original business problem remains. A dependency may still be unavailable; a required approval workflow may still fail; data may still be wrong; or the configuration switch may not control the user-facing function the team intended to restore.

The post-reversal **legitimate-service check** asks whether the specific owner-approved permitted function works in the declared scope. It should use a relevant positive task and a correct state result, not a generic process-health indicator.

The exact result depends on the intervention. For a fictional staff-write pause, the owner may care whether approved work can resume through the permitted route **after** the separate queue and booking-state conditions are satisfied. For a session revocation, the owner may care whether legitimate staff can authenticate through the approved replacement procedure. Those are different operations; neither is safely "undone" by reversing a single string.

The RB3 variant `LEGITIMATE_SERVICE_DOWN` declares that the post-reversal permitted function still fails. It returns `SERVICE_NOT_ACCEPTED` even though the simulated protective check passes. This demonstrates that protection and business availability are **independent** acceptance conditions.

A configuration equality test also cannot prove full booking-state correctness. An application can run under an old configuration while a booking database still contains unresolved inconsistencies. Later P1/C1 and V1 belong to their own separately released cards, and RB3 never changes their findings.

The correct report is "post-reversal legitimate function not accepted in this fixture," not "the entire library remains down" or "the data were destroyed."

### 3.RB10 A valid reversal can still leave open human decisions

Why not mark everything recovered when both post-reversal checks pass? Because the checks cover only their stated function and scenario. The original incident may have an unresolved cause, untested paths, preservation needs, pending communication decisions and business-state errors that the inverse operation did not address.

A safe reversal record keeps a **human review item explicitly open** with an owner and a next checkpoint. This is not a cosmetic ticket. It can include verifying residual exposure, choosing whether another control is needed, reconciling operations deferred during containment, and deciding whether a restricted mode remains acceptable.

The RB3 positive case returns `BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN`. The final words are intentional: the simulated reversal met two bounded post-state checks, but it is **not incident closure**. A negative case with `human_review_open=False` fails because the teaching contract requires an accountable human reassessment even after technically favorable observations.

The output must not be equated with RTO or RPO attainment. Chapter 3's RTE3 exercise measures scoped interruption-to-acceptance under a different contract; RB3 has no completed service-owner recovery-acceptance timeline. This is a **reversal readiness and verification** model.

A team may legitimately leave a temporary restriction partially active while awaiting review; if so, it must say which service and protective conditions are still in effect. Silent assumption of normal service is not an acceptable outcome.

### 3.RB11 Full wrong example: automatically undoing a harmful pause

**Synthetic classroom contrast; none of these events occurred at Harbor Library's 09:37 checkpoint.**

Imagine a fictional application operator learns that a temporary staff-write control is slowing legitimate booking work. A ticket says the earlier control was "deployed," and someone remembers a configuration called `CFG-GOOD-7`. The operator immediately restores that version and announces: "Rollback succeeded, the service is back, and we can close the incident."

This is **wrong**, even if restoring the old configuration appears to make one staff screen work. The team has not established that the old version is the verified relevant baseline, that reversal was authorized for the precise current state, or that a defined trigger was confirmed. It also has not recorded an execution receipt identifying the exact target, checked whether the protective goal still holds, or obtained the service owner's acceptance of the legitimate user outcome.

The more subtle failure is that reversing the control may expose the same path the control had been introduced to restrict. A restored booking interface could be responsive and still permit unintended edits. Conversely, the old configuration may fail to restore the intended function because of another dependency.

A superficially reassuring case note would compound the error by replacing the original proposal and intervention history with one line reading "fully recovered." That prevents a later reviewer from understanding what happened and what the reversible risk actually was.

**Correct handling of this wrong case:** Hold any further unapproved change, preserve the relevant source and configuration history, identify the precise previously verified state, seek the accountable rollback decision, specify both protection and legitimate-service checks, and record open human review. If the first change has already occurred under an unverified route, the team must document that fact and obtain an owner-governed safe next decision. It must not invent a retroactive approval.

### 3.RB12 Full correct example: a reviewed, narrow reversal with residual risk open

**Independent RB3 invented variant, dated 2040-04-10; not canonical Harbor Library evidence.**

A fictitious service owner had an isolated, previously verified candidate configuration `CFG-GOOD-7`, documented for the narrow function `staff-write`. A separately approved classroom control `CTRL-PAUSE-9` later restricted that function. A named training observation `TRIG-SVC-01` reports that the required permitted service activity is now failing under the isolated control and meets the declared **SERVICE_HARM** trigger.

The fictional service owner, `ServiceOwnerSim`, considers a scoped reversal request. The request names only the original `staff-write` function, specifies the approved candidate `CFG-GOOD-7`, explains the loss-of-protection risk, and defines an authorization window of 14:05–14:25 UTC. At 14:12, the invented approval receipt `APP-RB-01` is present in the fixture. The operator's simulated execution receipt is `EXEC-RB-01` for the expected target, and a separate declared post-state observation exists.

The **two different post-reversal checks** are then considered: (1) the selected protective condition remains acceptable in the tested scope under a defined residual safeguard, and (2) the legitimate staff function meets its declared business check. Only if both are supported in the fixture does the validator return `BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN`.

That verdict is deliberately narrow. It does **not** authenticate a real approver, prove the earlier intervention's cause, test every write route, reconcile every pending booking or close the incident. The service owner must still review residual risks, choose any further restriction or monitoring and preserve an auditable next checkpoint.

A second positive scenario changes the trigger to **PROTECTION_FAILURE**, with an independent artificial trigger receipt. It can reach the same bounded result if the new operating mode still meets both acceptance checks. This illustrates that the reason for reconsideration can differ while the authorization and verification discipline remains necessary.

A full report preserves the original baseline reference, intervention approval, trigger, new rollback approval, receipt, two check results and open human-review status as **separate historical entries**.

### 3.RB13 Negative evidence and the need to stop before compounding harm

A failed condition can call for holding a reversal proposal, reassessing an already reported action, or escalating immediately to the appropriate owner depending on when it is discovered.

If **approval is absent**, an operator must not treat the proposal as executable merely because service disruption is costly. If the **scope exceeds** the original control, the extra object needs its own authorization and safe test; it must not be folded into the inverse. If the **trigger was not observed**, the evidence for change is unestablished. The team should recheck the source before deciding that rollback is justified.

If a **proposal lacks an execution receipt**, report proposed/not performed. If an **execution receipt exists without post-state observation**, report execution claimed but effect unverified. A command result is not a service test.

If the **protection check fails after the reversal**, the team may need a revised, owner-approved containment strategy. If the **legitimate-service check fails**, the inverse did not accomplish its business objective in the tested scope, even if protection remains intact. Neither failure licenses uncontrolled trial-and-error changes against production.

An **unknown baseline** or **expired window** is also significant. An inverse plan that was valid against one configuration may no longer be safe when state or dependencies have changed. An expired approval does not silently renew itself because the operator is already familiar with the system.

This is why rollback readiness should be prepared alongside containment, not improvised after a failed intervention. A team needs an authorized response even when its first solution makes conditions worse.

### 3.RB14 A reversal card must preserve history, not overwrite the initial decision

A reviewable reversal card should link three distinct records: the pre-intervention baseline, the original intervention and the proposed or executed reversal. Each has its own evidence and authorization.

A useful field-level record includes:

| Field | Evidence or safe limitation |
|---|---|
| Baseline reference | Configuration/service state ID and time of independent check |
| Intervention reference | Original proposal, approval, scope, actual operator receipt and known effects |
| Reversal trigger | Observed service harm or protection failure and source/confirmation |
| Reversal proposal | Target state, exact objects and intended effect |
| Reversal approval | Named owner, scope, time window, restrictions and receipt |
| Reversal execution | Operator, specific change/target, actual time and receipt, if performed |
| Protection after reversal | Expected blocked/detected harmful behavior, observed result and limit |
| Legitimate service after reversal | Permitted function, expected result, observed result and limit |
| Remaining risk | Untested routes, residual incident cause, business obligations and evidence gaps |
| Next human decision | Named accountable reviewer, trigger and deadline |
| State | Proposed, approved, reported executed, bounded checks passed/failed, or unknown |

In the canonical 09:37 decision, no reversal record exists because no intervention was executed. A future optional synthetic exercise may introduce one, but its identifiers must remain outside R1–R24 and the later Branch S/P story.

The correct practice is to **append** the reversal record as a new dated activity rather than replacing the Round C proposal or asserting that a later action had already happened. This preserves the distinction between history and hindsight.

### 3.RB15 Preparing the next safe action when a reversal fails

What should the learner propose if an RB3 negative case appears?

For a missing approval or unauthorized scope, identify the accountable owner and request a corrected, bounded decision. For an unknown baseline, ask the configuration or service custodian to establish a safe candidate and document the comparison. For a missing trigger receipt, obtain a genuine authorized observation rather than inventing the incident. For an execution receipt without independent effect evidence, request the appropriate bounded check before claiming success.

If protection fails after rollback, the next step is not automatically to reinstate the original harmful control. The owner must compare the original intervention, proposed alternative and current service risk. A narrower control, monitored restricted mode or another approved protective action may be appropriate, but the supplied RB3 fixture does not select a real solution.

If legitimate service remains down after rollback, the result should be escalated with the specific failed function and source rather than declared successful because the configuration identifier matches the baseline. Additional fault diagnosis or a separately approved recovery action may be necessary.

For all these cases, preserve current evidence, avoid adding unexplained changes and assign an owner and review trigger. An apparently successful inverse is only one step of managing an incident; unresolved cause, correct booking state and actual user acceptance remain separate tasks.

### 3.RB16 Teaching synthesis and relationship to other Chapter 3 laboratories

**W1** tests whether a proposed write pause actually blocks the stated isolated routes. **G3-DG** distinguishes generic approval, execution and acceptance states. **MQ3** checks duplicate/manual-queue processing decisions. **RTE3** measures scoped time and data recovery evidence. **RB3** instead tests whether a *new inverse of a disruptive or ineffective intervention* has a verified baseline, bounded new authority, observed trigger, exact execution target, independent post-reversal protective and business checks, and explicit human review.

These questions are complementary, not interchangeable. A successful control test is not a safe rollback plan; a successful rollback receipt is not verified protection; a normal-looking service function is not full recovery; and an open review item is not an incident-closure receipt.

A rapid-course learner has met this section's objective when they can decide **whether to hold, propose, verify or escalate a reversal** from a small evidence packet, explain why two independent post-state checks matter, and refuse to insert the synthetic scenario into the canonical 09:37 decision.

---

## RB3 Offline Laboratory — Containment Reversal Readiness and Verification

**Classification:** Independent, entirely synthetic laboratory. All identifiers, times, flags, approvals, execution receipts and post-state results are invented for RB3. Nothing relates to actual Harbor Library operations, R1–R24, Branch S/P or other labs.

**Objective:** Evaluate a proposed inversion of a fictional isolated staff-write containment setting. Accept a narrowly valid rehearsal only when pre-state, prior intervention, new reversal approval, scope, execution window, observed trigger, matching execution receipt and **both** post-reversal outcomes are represented, with a human review remaining open.

**Environment:** Python 3 standard library, in memory. No files, network, accounts, logins, real controls, destructive commands, configuration updates or production access.

### Inputs and expected rule

The fictitious date is 2040-04-10 UTC. The verified pre-state reference is `CFG-GOOD-7`; the prior approved containment reference is `CTRL-PAUSE-9`, affecting only `staff-write`. Reversal requires a separate `ServiceOwnerSim` approval receipt and a 14:05–14:25 UTC window, and the proposed rollback targets that same narrow function. A service-harm or protection-failure observation is needed before an inverse is pursued. The operator's returned target and the separate post-state observation must match the plan.

In this controlled fixture, `protection_check=True` means a **declared** residual protective check passed for the tested scope *after* the inverse. It does not mean the original blocking control remained active. `legitimate_service_check=True` means the declared permitted business check passed. Neither Boolean proves a real system property. A positive result **must retain** `human_review_open=True`.

### Full executable Python 3 program

~~~python
from copy import deepcopy
from datetime import datetime

def utc(value):
    return datetime.fromisoformat(
        "2040-04-10T" + value + ":00+00:00"
    )

BASE = {
    "baseline_ref": "CFG-GOOD-7",
    "baseline_verified": True,
    "intervention_id": "CTRL-PAUSE-9",
    "intervention_approved": True,
    "intervention_scope": {"staff-write"},
    "rollback_target": "CFG-GOOD-7",
    "rollback_scope": {"staff-write"},
    "rollback_owner": "ServiceOwnerSim",
    "rollback_approver": "ServiceOwnerSim",
    "rollback_approval_receipt": "APP-RB-01",
    "authorized_window": (utc("14:05"), utc("14:25")),
    "decision_time": utc("14:12"),
    "trigger_kind": "SERVICE_HARM",
    "trigger_observed": True,
    "trigger_receipt": "TRIG-SVC-01",
    "rollback_proposed": True,
    "execution_receipt": "EXEC-RB-01",
    "executed_target": "CFG-GOOD-7",
    "post_state_observed": True,
    "protection_check": True,
    "legitimate_service_check": True,
    "human_review_open": True,
}

def evaluate(p):
    if not p["baseline_verified"] or not p["baseline_ref"]:
        return "HOLD_BASELINE_UNVERIFIED"
    if not p["intervention_approved"]:
        return "HOLD_PRIOR_INTERVENTION_UNVERIFIED"
    if (
        not p["rollback_approval_receipt"]
        or p["rollback_approver"] != p["rollback_owner"]
    ):
        return "HOLD_APPROVAL_MISSING_OR_WRONG"
    if (
        not p["rollback_scope"]
        or not p["rollback_scope"].issubset(
            p["intervention_scope"]
        )
    ):
        return "HOLD_ROLLBACK_SCOPE_INVALID"
    start, end = p["authorized_window"]
    if not (start <= p["decision_time"] < end):
        return "HOLD_OUTSIDE_APPROVED_WINDOW"
    if (
        not p["trigger_observed"]
        or not p["trigger_receipt"]
        or p["trigger_kind"] not in {
            "SERVICE_HARM", "PROTECTION_FAILURE"
        }
    ):
        return "HOLD_TRIGGER_UNOBSERVED"
    if (
        not p["rollback_proposed"]
        or not p["execution_receipt"]
    ):
        return "PROPOSED_NOT_EXECUTED"
    if (
        p["rollback_target"] != p["baseline_ref"]
        or p["executed_target"] != p["rollback_target"]
    ):
        return "EXECUTION_TARGET_MISMATCH"
    if not p["post_state_observed"]:
        return "EXECUTION_REPORTED_EFFECT_UNVERIFIED"
    if p["protection_check"] is not True:
        return "PROTECTION_NOT_ACCEPTED"
    if p["legitimate_service_check"] is not True:
        return "SERVICE_NOT_ACCEPTED"
    if not p["human_review_open"]:
        return "HUMAN_REVIEW_MISSING"
    return "BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN"

CASES = [
    ("VALID_WITH_OPEN_REVIEW", {}),
    (
        "VALID_AFTER_PROTECTION_TRIGGER",
        {
            "trigger_kind": "PROTECTION_FAILURE",
            "trigger_receipt": "TRIG-PROT-02",
        },
    ),
    ("BASELINE_UNKNOWN", {"baseline_verified": False}),
    (
        "PRIOR_INTERVENTION_UNVERIFIED",
        {"intervention_approved": False},
    ),
    ("APPROVAL_ABSENT", {"rollback_approval_receipt": None}),
    ("WRONG_APPROVER", {"rollback_approver": "AnalystSim"}),
    (
        "SCOPE_EXCEEDED",
        {"rollback_scope": {"staff-write", "identity"}},
    ),
    ("EMPTY_SCOPE", {"rollback_scope": set()}),
    ("WINDOW_EXPIRED", {"decision_time": utc("14:30")}),
    ("TRIGGER_NOT_OBSERVED", {"trigger_observed": False}),
    ("TRIGGER_NOT_SUPPORTED", {"trigger_kind": "RUMOR"}),
    ("PROPOSAL_WITHOUT_EXECUTION", {"execution_receipt": None}),
    ("RECEIPT_WRONG_TARGET", {"executed_target": "CFG-UNKNOWN"}),
    ("RECEIPT_WITHOUT_EFFECT", {"post_state_observed": False}),
    ("PROTECTION_REGRESSED", {"protection_check": False}),
    (
        "LEGITIMATE_SERVICE_DOWN",
        {"legitimate_service_check": False},
    ),
    ("HUMAN_REVIEW_NOT_OPEN", {"human_review_open": False}),
]

for name, changes in CASES:
    candidate = deepcopy(BASE)
    candidate.update(changes)
    print(f"{name}: {evaluate(candidate)}")

assert (
    evaluate(BASE)
    == "BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN"
)
~~~

### Exact expected output — executed with Python 3

~~~text
VALID_WITH_OPEN_REVIEW: BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN
VALID_AFTER_PROTECTION_TRIGGER: BOUNDED_REVERSAL_CHECKED_REVIEW_OPEN
BASELINE_UNKNOWN: HOLD_BASELINE_UNVERIFIED
PRIOR_INTERVENTION_UNVERIFIED: HOLD_PRIOR_INTERVENTION_UNVERIFIED
APPROVAL_ABSENT: HOLD_APPROVAL_MISSING_OR_WRONG
WRONG_APPROVER: HOLD_APPROVAL_MISSING_OR_WRONG
SCOPE_EXCEEDED: HOLD_ROLLBACK_SCOPE_INVALID
EMPTY_SCOPE: HOLD_ROLLBACK_SCOPE_INVALID
WINDOW_EXPIRED: HOLD_OUTSIDE_APPROVED_WINDOW
TRIGGER_NOT_OBSERVED: HOLD_TRIGGER_UNOBSERVED
TRIGGER_NOT_SUPPORTED: HOLD_TRIGGER_UNOBSERVED
PROPOSAL_WITHOUT_EXECUTION: PROPOSED_NOT_EXECUTED
RECEIPT_WRONG_TARGET: EXECUTION_TARGET_MISMATCH
RECEIPT_WITHOUT_EFFECT: EXECUTION_REPORTED_EFFECT_UNVERIFIED
PROTECTION_REGRESSED: PROTECTION_NOT_ACCEPTED
LEGITIMATE_SERVICE_DOWN: SERVICE_NOT_ACCEPTED
HUMAN_REVIEW_NOT_OPEN: HUMAN_REVIEW_MISSING
~~~

### Interpretation and negative controls

The first two cases pass only the **bounded synthetic contract**. One is triggered by invented legitimate-service harm; the other by invented failure of the protective objective. Both leave human review open. Neither authenticates an approval or establishes a real service recovery.

`BASELINE_UNKNOWN` refuses an inverse with no verified pre-intervention candidate. `PRIOR_INTERVENTION_UNVERIFIED` refuses to assume the earlier control had an authorized execution history. `APPROVAL_ABSENT` and `WRONG_APPROVER` distinguish missing or invalid reversal authority. `SCOPE_EXCEEDED` and `EMPTY_SCOPE` reject a broadened or undefined inverse target. `WINDOW_EXPIRED` detects the end of the declared authorization period.

`TRIGGER_NOT_OBSERVED` and `TRIGGER_NOT_SUPPORTED` block action based on a missing observation or a kind of signal not defined in the teaching contract. `PROPOSAL_WITHOUT_EXECUTION` has no operator receipt and remains a proposal. `RECEIPT_WRONG_TARGET` detects that a reported execution does not match the planned configuration. `RECEIPT_WITHOUT_EFFECT` is especially important: an execution receipt exists, but the resulting technical state was not checked, so success cannot be claimed.

`PROTECTION_REGRESSED` represents a case where the expected protection is unacceptable after reversal despite the simulated operation. `LEGITIMATE_SERVICE_DOWN` represents the opposite risk: protection may remain acceptable, but legitimate service still fails. Both require a new, owner-governed decision rather than silent closure. `HUMAN_REVIEW_NOT_OPEN` blocks a "completed" verdict with no accountable residual-risk review.

**What the script does not prove:** Its identifiers, Boolean approvals, scopes, times, trigger receipts and verification flags are invented. The code does not read or write configuration, authenticate an owner, inspect a security control, test booking routes, measure recovery time or handle an actual incident. It reports the first applicable condition; other failures may coexist. A favorable result is **not** authorization to reverse a control or proof of full recovery.

**Required learner artifact:** Reproduce the seventeen output lines. Create a three-column matrix `scenario | first failed condition | safe next owner-request`. Explain why an execution receipt without effect verification is inadequate, and why passing the legitimate-service test without passing the protection test does not constitute acceptable rollback. Identify one fact an actual operator would have to measure for each Boolean post-state check.

**Acceptance criteria:** A full lab result reproduces every line, distinguishes prior intervention from separate reversal approval, rejects scope and time violations, correctly explains both post-reversal gates and keeps the human review open. A response fails if it treats the toy result as a real control operation, calls an unapproved inverse executed or equates a successful inverse with resolved root cause or complete recovery.

---

## Two-Role Practical Exercise — Frozen Reversal Packet and Independent Decision

**Roles:** **Reversal Packet Author** and **Independent Reviewer**. The roles are fictional classroom assignments; no participant receives real production privileges.

**Objective:** Test whether another learner can determine from a sealed record whether a proposed reversal has a verified baseline, justified trigger, correct approver and scope, actual execution receipt and two independent post-reversal results **without asking the author for undocumented context**.

### Procedure

1. **Choose the fixture.** Use the artificial `VALID_WITH_OPEN_REVIEW` case or one negative RB3 variant. Do not use R1–R24 as executed rollback evidence. State the fictional date and scope.
2. **Author prepares the packet.** Include baseline reference and its asserted check, intervention reference and prior approval status, trigger observation, proposed inverse target and objects, required owner, approval window, receipt status, post-state protection and legitimate-service results, and review owner.
3. **Freeze the packet.** Save `RB3-packet-v1`. Do not edit it during the receiver phase. The packet is a classroom document, not a runbook for real action.
4. **Reviewer works independently.** Without verbal or written hints from the author, produce `RB3-review-v1` that states whether the reversal may remain proposed, whether it is reported executed, whether each post-state gate has evidence, and which approval or source is still needed.
5. **Reviewer identifies the next safe step.** For a missing approval, request the proper owner decision. For missing execution verification, request a bounded post-state check. For a failed protection or service result, request a new owner-governed action while documenting risk.
6. **Freeze the review.** Compare it with the declared fixture and the Python output. Record whether a disagreement came from a missing packet field, an unsupported inference or a misunderstood decision state.
7. **Retest with versioning.** If needed, publish a clearly labeled `RB3-packet-v2` with corrected fields and obtain a new reviewer response. Preserve the first failed answer and its reason.

**Required evidence package:** Both frozen versions, a source-reference table, named approving role, justified trigger, scope and window check, execution/effect status, two gate results and next human decision. The reviewer must never use silence to infer permission.

**Pass:** The reviewer rejects invalid or incomplete routes, accurately reports the limited positive case and identifies its unresolved human-review work. **Critical fail:** the reviewer authorizes real changes, promotes a proposal to execution, restores an unverified baseline, ignores a failed protection gate, or reports full incident recovery from a bounded rollback result.

**Limit:** Passing the two-role tabletop does not demonstrate reliability of a real rollback mechanism. It tests an independent person's understanding of a fictional control-decision packet.

---

## Targeted Existing-Exercise Refinements — EX029, EX036 and EX038 Only

These additions **do not change** the existing exercise IDs, the number of book exercises or their required output formats. Keep the existing 0–2 evaluation rubric and the canonical 09:37 decision boundary.

### EX029 — Decision matrix (original **two rows**)

**Additional requirement:** Within the existing two-row comparison for session revocation and the fifteen-minute staff-write pause, add for each option (a) the pre-intervention state that would have to be verified, (b) an observable **service-harm or protection-failure trigger** that would justify seeking reversal, (c) the accountable approver of that *new reversal decision*, and (d) separate protection and legitimate-service checks after a reported inverse. Do not create a third row, reuse W1 probe outcomes as canonical facts or claim the option was executed at 09:37.

**2-point refinement:** Both original intended effects and service costs remain explicit, with R21 labeled tolerance only. The reversal is a separately approved proposal with exact target and review conditions; a hypothetical fallback does not prove recovery.

### EX036 — Decision record (original **six fields**)

**Additional requirement:** Keep the original six-field card for the 09:37 **proposal**. In field 6 (verification/fallback/review), add a short **conditional reversal subcard**: last verified configuration reference to obtain, observable trigger, scope and window to request, authority needed, operator/effect receipt to require, post-reversal protection and legitimate-service checks, and the accountable human-review item. Use `pending/not supplied` for every rollback execution or test not contained in R17–R24.

**2-point refinement:** The historical action remains a proposal, the new inverse is not silently authorized, and later branch or RB3 exercise observations never enter the canonical 09:37 decision.

### EX038 — Alternative defensible choice (pause-first with an **empty queue ledger**)

**Additional requirement:** Retain the original pause-first proposal, its two assumptions, service-owner approval requirement, queue plan, immediate effectiveness check, 15-minute review and conditional alternative. Keep the **queue-ledger template empty** at 09:37. Add a **reversal-readiness clause**: if the pause blocks essential authorized work or fails its protective purpose in a *future separately verified test*, what exact owner decision and bounded post-reversal checks would be required before changing that control? Do not use Branch P's later two pending requests or MQ3's synthetic rows as an observed 09:37 queue.

**2-point refinement:** R21 remains a tolerability statement; the proposed pause and any later reversal have independent authorization and verification. The ledger format stays empty and unchanged, and resumption remains conditional on booking/queue review and owner sign-off.

---

## Supplementary Worked Answers — Final Principal-Book Appendix Placement

### EX029 — Additional worked reasoning

The two-row decision matrix still compares a proposed current-session revocation and a proposed fifteen-minute staff-write pause at 09:37. For revocation, the baseline would include the identified current session and the permitted reauthentication path; a verified legitimate-work failure could justify asking the incident lead and identity owner for a narrowly approved new authentication or access-restoration decision. A simple "unrevoke" claim is not automatically technically meaningful. Check that the selected protective constraint remains appropriate and that authorized staff can perform the required task within the approved scope.

For the write-pause option, obtain a verified pre-change route/configuration reference and owner-defined legitimate operating condition; R21 says the interruption is tolerable but **does not approve** the pause. If a later independent test reported unacceptable service harm or protective ineffectiveness, the service owner would have to authorize a bounded reversal or replacement control with a named window and operator. A reported inverse must be followed by separate evidence that the appropriate protection remains and that legitimate booking service works, plus continued queue and booking-state obligations. At 09:37 neither initial action nor reversal has been executed. RB3's positive laboratory result is unrelated synthetic data, not a missing case receipt.

### EX036 — Additional worked reasoning

The six-field card remains: **(1)** 09:37 proposal/not executed; **(2)** R17's confirmed training scope and R18's B20 edit, with actor/cause unknown; **(3)** named-current-session restriction proposal; **(4)** incident lead and identity owner approvals needed, identity administrator prospective executor; **(5)** intended protection and possible staff reauthentication cost; **(6)** proposed bounded identity/booking verification, a possible pause fallback and a 09:45 review trigger. The conditional RB3 subcard fits **inside field 6**, not as a new seventh field. It identifies the baseline and approval details to collect *before* any action, the service-harm or protection-failure signal that might trigger a **new** reversal request, the owner of that decision, a target- and time-scoped execution receipt, both post-state checks, and an open human review. Every result that is not supplied remains `pending`. No Branch S/P or RB3 execution is backdated to the 09:37 R-series case.

### EX038 — Additional worked reasoning

A pause-first proposal is defensible if the team explains that the account-to-edit path is uncertain and the service owner could tolerate a short interval of manual intake under appropriate approval. R21 **does not** authorize or execute that pause. The plan names a service-owner decision, application operator, protective test, legitimate service/queue cost, next review and a possible alternative if the control fails.

At 09:37 the proposed queue ledger stays empty, with its schema unchanged: `receipt ID | booking/action | claimed time | approval | expected version | prior effect | disposition | owner`. If a **future independent** source establishes that the pause prevents essential permitted work or fails to block its intended path, the incident lead and service owner should evaluate a new bounded reversal or replacement under separate scope, approval and verification. A rollback is not automatically safe merely because it ends the pause: a post-reversal check must test remaining protection and legitimate booking behavior, while queue reconciliation and data correctness stay with the service owner. The later Branch P and MQ3 records are unavailable to the canonical 09:37 decision.

---

## Section Synthesis, Navigation and Primary Sources

Reversal readiness is the ability to show what the service was like **before** containment, why the chosen control may need to change, what new authority is required, what the operator actually reported doing, and whether the result meets **both protection and legitimate-service criteria**. A checked inverse remains bounded; it does not prove that the whole incident is resolved, that every earlier edit was understood, or that the service owner accepted full recovery.

### Continue studying — chapter 03 of 04 (public supplementary draft)

[← Chapter 02](../MANUSCRIPT.md#ch-02) · [Course chapter index](../../SUBJECTS.md) · [Chapter 04 →](../MANUSCRIPT.md#ch-04) · [Principal book and worked answers](../MANUSCRIPT.md#answers)

**Editorial integration:** This is a **transitional public component** of the one principal English book. Accepted teaching, RB3, the three original-exercise refinements and their worked answers belong in the existing `MANUSCRIPT.md` after independent review. The file adds no new chapter, exercise ID or course skill and does not establish 300 verified A4 pages.

### Verifiable primary references

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025. It supports incorporating incident response, coordination and recovery decisions into broader risk management; it does **not** prescribe the RB3 simulator.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final), final December 2016. It addresses recovery planning, realistic testing, prioritization and improvement; it does **not** report RB3's test results.
- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), updated November 2010. It provides contingency planning and restoration context; its public examples should not be mistaken for Harbor Library's configuration.

All RB3 identifiers, times, permissions, reported executions, test flags and scenario outcomes are original **synthetic** educational constructions. Third-party rights remain with their sources. Editorial responsibility belongs solely to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned material follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within their limits. The exercises neither access nor modify real infrastructure.
