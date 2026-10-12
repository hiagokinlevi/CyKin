# Chapter 02 expansion component — Authority as a verifiable workflow

> **Editorial state:** Public integration draft for Chapter 02, professional six-month English edition. Transient component for [the single principal manuscript](../MANUSCRIPT.md#ch-02); not a new volume or a completed lesson. Existing IDs EX006–EX010 remain unchanged.
>
> **Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). See [rights and source boundaries](../../../../../../RIGHTS.md).

## Additional learning outcomes

After this material, a supervised practitioner can translate authority from a verbal role assignment into a decision-specific control; distinguish read access from change authority; validate the transitions proposed → approved → executed → independently verified; record the limits of emergency delegation; and produce an actionable record even when the proper approver is unavailable. Every example is synthetic and requires no live system.

## 1. An incident plan does not confer powers

At 09:04 UTC, CTN support receives fictional card C02: S42 appears unavailable, noticed around 09:00. There is no authoritative state check, cause, confirmed scope or actor. A colleague asks whether to disable the shared-sounding account svc-enroll. This request is a **question**, not an approval. The readiness gaps from C01 remain open. No later identity, endpoint or API cards are available at this point. An ethical and operationally competent responder must resist importing facts from future chapters.

Response roles answer different questions. The **analyst** decides what to recommend and what questions to ask. The **incident lead** prioritizes coordination and keeps a record. The **source custodian** knows the permitted way to obtain a particular dataset. The **service owner** decides what business interruption is tolerable. The **identity owner** controls identity-specific risk. The **change authority** interprets the approved emergency-change procedure. The **operator** performs only the permitted act; an **independent verifier** checks the observable effect. These are functions, not job titles. In a small organization, one person may hold several roles, but the record must retain which decision they exercised, on what basis and within which scope.

A source custodian's ability to read the IdP console does not mean they can lawfully export all sign-ins. An identity operator's ability to disable an account does not mean they have the service owner's acceptance of enrollment disruption. An incident lead may ask for rapid response without independently owning every cloud or privacy decision. The **technical ability** to invoke a command, **organizational permission** to do so, and **evidence sufficiency** for choosing the action are three separate gates.

This distinction is aligned with the integrated, cross-organizational response approach described in [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). NIST does not prescribe CTN's fictional approval roles or convert a severity label into tenant administration privileges. Local policy, law, contracts and approved emergency processes remain binding.

## 2. A bounded action is a tuple, not a verb

"Disable" is not an action specification. A useful action request contains: **case identifier; action identifier and revision; observed trigger with source; exact target and environment; method/class of operation; intended effect; accepted service side effect; limits on time and objects; approving roles; operator; prerequisites; stop condition; rollback method and owner; independent observable checks; preservation obligations; expiry and review trigger**.

For CTN, the target could hypothetically be one known session, one slot's write route, the svc-enroll account, or a tenant-wide policy. Those are radically different scopes. If a tool cannot perform the intended narrow restriction and instead defaults to account-wide disablement, the operator must **reject and resubmit** the request for renewed impact assessment. A software interface is not authorized to silently substitute broader behavior. The case manager should record the reason for mismatch and which approval would be necessary; no action has occurred.

Write the **precondition** as a testable statement. "Bad activity detected" is not reproducible. "An approved source contains a live session identifier tied to a documented continuing prohibited action" is closer, but at C02 the needed session and join do not exist. Therefore a recommendation to revoke a session must remain conditional. A retention-risk preservation request can still proceed through a different, read-only approval route once its data and timing have been defined.

An expiry is not automatically a restoration guarantee. After the maximum duration, the specified control may require an operator to restore settings, reconcile queued work, verify dependent services or await a second decision. A rollback plan should address the concrete configuration or session state and name how to detect incomplete recovery. Disabling a shared automation identity may cancel jobs or invalidate tokens that do not simply resume when re-enabled.

## 3. Model the action lifecycle as a state machine

The most consequential documentation error is to use "done" for approval, execution and verification. Keep the four states separate:

1. **Proposed:** analyst has a recommended object, evidence rationale and request for review; approval and operation fields remain empty.
2. **Approved, not executed:** named authority has granted the precise scope and limit, but the operator has not produced a receipt.
3. **Executed, unverified:** the operator reports a method, target, change version and time; intended effects have not been independently observed.
4. **Verified within scope:** a separate authorized check supports a particular result, with test method, observation window and residual gaps. It never licenses claims about untested routes.

These states are **not** an incident lifecycle. They describe the evidentiary status of one named action. Reject an "approved" transition if the authorizer is unidentified or the scope is ambiguous; a chat message "OK" can be logged but is not automatically a valid control decision. Reject "executed" if the only evidence is a recommendation or a scheduled change. Reject "verified" if a command returned success but no independent observation of its intended effect exists.

Consider a synthetic *nonproduction* action TRAIN-A01 that is **not a CTN main-case action**. This lab demonstrates the state labels without contacting identity systems.

~~~python
action = {
    "id": "TRAIN-A01",
    "target": "svc-enroll",
    "scope": None,
    "approved": False,
    "receipt": False,
    "checked": False,
}
def status(a):
    if not a["scope"] or not a["approved"]:
        return "PROPOSED_ONLY"
    if not a["receipt"]:
        return "APPROVED_NOT_EXECUTED"
    if not a["checked"]:
        return "EXECUTED_UNVERIFIED"
    return "VERIFIED_WITHIN_SCOPE"
print("C2|v0=" + status(action))
action.update(scope="S42 only", approved=True)
print("C2|v1=" + status(action))
action["receipt"] = True
print("C2|v2=" + status(action))
action["checked"] = True
print("C2|v3=" + status(action))
~~~

**Executed output for this exact local fixture:**

~~~text
C2|v0=PROPOSED_ONLY
C2|v1=APPROVED_NOT_EXECUTED
C2|v2=EXECUTED_UNVERIFIED
C2|v3=VERIFIED_WITHIN_SCOPE
~~~

The function validates **presence of flags**, not whether an actual approver is legitimate, an operator was authorized or a check tested every route. It is deliberately insufficient as a production authorization engine. In particular, the example sets approved=True without a signature; this represents a classroom state transition, not a real decision. A sound production workflow would validate decision references, signed identities, allowed targets, expiry, separation of duties and immutable audit records. Students must not treat a passing string from this script as permission to touch any tenant.

Fault injection: remove the scope after setting approved=True. The function returns PROPOSED_ONLY because a flag without a defined target is not an actionable authorization. Now set checked=True without a receipt: the state remains APPROVED_NOT_EXECUTED. These two counterexamples show why the requested sequence matters even during operational pressure.

## 4. Build an authorization matrix for the actual decision

Construct the matrix *per action* rather than per department:

| Action | Recommends | Required decision owner | Performs | Independent evidence |
|---|---|---|---|---|
| Log case and contact service owner | Analyst | Incident lead may coordinate according to local procedure | Analyst/recorder | Ticket receipt, no system change |
| Retrieve a restricted IdP interval | Analyst | Identity/data custodian under applicable access policy | Approved custodian | Selection, source metadata, collection receipt |
| Revoke a precisely identified session | Analyst/identity lead | Identity and affected service owner, plus change process as required | Identity operator | Scoped session-state result and service-impact check |
| Disable shared account | Analyst may raise risk, not execute | Service owner and emergency-change authority plus identity owner | Authorized operator | Exact account state, dependent services and rollback checks |
| Notify learners | Communications team drafts | Authorized communications/privacy decision owner | Designated publisher | Approved message and delivery receipt, if later sent |

C01 does not name an after-hours identity alternate or a fallback for an absent service owner. A matrix that assigns "supervisor" to every cell without a charter supporting that person's delegated authority is noncompliant with the exercise. The appropriate status is **unknown route, escalation pending**. A responder may use the organization's real escalation process if known; the course does not invent an emergency delegation.

If normal approvers are unavailable and there is an imminent safety or availability issue, the responder should check the locally documented emergency authority and its evidence-recording requirements. The word **emergency** does not waive privacy constraints, legal obligations or least privilege by itself. The professional exercise ends at the authorization boundary, not at an imaginary break-glass action. Record urgency separately from permission.

## 5. Compare interventions against a concrete loss model

At C02, compare A: read-only validation and owner contact; B: one-session restriction; C: broad svc-enroll or tenant-policy change. Evaluate four dimensions, not just "fast/slow."

**Expected harm avoided.** A prevents evidence-free disruption and can clarify service scope, but may leave a damaging action running if one exists. B could terminate an identified active session, but C02 has not identified one. C could block a much larger set of actions, including legitimate enrollment operations, yet the necessary causal link is absent.

**Harm introduced.** A consumes analyst time and could cause a time-sensitive source to expire if preservation is neglected. B may interrupt scheduled work or fail if a different session is used. C may stop writes across multiple dependencies, queue failures or legitimate operator recovery. The broader the control, the larger the planned verification and rollback surface.

**Uncertainty.** For A, authoritative slot state and incident scope remain unknown; its purpose is to reduce precisely those unknowns. For B, session identity and cause are not established. For C, whether the account caused the symptom and whether disabling it would protect S42 are not established.

**Verification.** A can be verified by an owner-approved state result and documented intake; B needs a check of the specific session and enrollment behavior after proper authorization; C needs full dependency acceptance, evidence of scope and a rollback decision. "Console returned success" alone is not verification of user-visible outcomes.

At 09:04, A is the defensible first step. It does not imply that later protective controls will never be warranted. New evidence may alter urgency and the acceptable risk of inaction; each decision should have a new timestamp and evidence basis rather than replacing the earlier record.

## 6. Two worked decision records: one correct, one defective

**Defective example:** "09:04 high severity breach, shared account hacked. Supervisor says disable; account contained successfully." This sentence invents compromise, severity, approval, execution and success. No C02 source supports those assertions. It also hides who accepted service consequences or how the account scope was verified.

**Defensible example:** "09:04 C02 support report received: S42 appears unavailable, first noticed approximately 09:00. Current authoritative S42 state and cause unknown. Analyst proposes bounded read-only verification by application owner, identifies missing service-owner alternate from C01, and requests incident-lead coordination. Broad account restriction was raised by a colleague but remains unapproved and unexecuted; no containment effectiveness claim. Reassess upon owner state evidence or newly validated source signals."

The second statement can be acted on by a supervisor even though it is less dramatic. It distinguishes an observation from an action proposal and does not hide the very gap the organization needs to repair.

When a new evidence card arrives, make a **new version**. V1 is the 09:04 decision. V2 would include the new source and its release time; it must not modify V1 as if future knowledge were always available. Keep the original source reference and earlier scope decision for review. The C02 chapter itself does not release C03–C08, so do not use their data to justify V1.

## 7. Handling the V2 ambiguous approval specimen

The exercise's variant V2 contains the phrase "OK to act." Treat that phrase as a communication artifact in a **separate simulated branch**, not as a fact about the main C02 incident. It lacks target, operation, environment, duration, affected service acceptance, operator and verification. A clarifying message should ask which object, method, conditions and maximum time the supervisor authorizes, how the identity and service owners have approved the effects, who will execute, and who will verify or roll back.

Correct case status: "V2 approval wording insufficient for a scoped disruptive change; approval unresolved, no action executed, no verified effect." If an analyst asks "Does this cover a bounded read-only preservation request?" that can narrow the exchange, but it does not turn the original sentence into blanket permission. If the scenario later produces a clear approval, retain both messages with timestamps and record the later decision as a distinct event.

An incorrectly designed training system might accept any affirmative message and silently populate the approved flag. This is why the simple Python fixture is instructional only. A real workflow must independently check identity, delegated authority, scope, expiry and conflict of duties. The essential human question remains: who owns the potential service harm, and what precisely have they approved?

## 8. EX006–EX010: deeper tasks, rubrics and worked-answer supplements

These tasks **extend** the existing exercises; they preserve the numbered IDs and the canonical 0–2 scoring scheme. A competent answer documents unknown fields instead of manufacturing proof.

**EX006 — Role-and-right matrix.** Objective: distinguish recommendation, authorization, operation and verification for five classes of action. Input: C01 gaps and C02 09:04 symptom. Produce the five-row matrix above with a separate column for missing delegates. Model reasoning: an analyst may create an intake record; a data custodian governs log access; disruptive identity changes need identity and service decision owners; a communication owner must approve external statements. Mark unknown after-hours routes as unknown. Assessment: two points only when the learner identifies which role can say no and when the proposed action must stop.

**EX007 — Action request.** Objective: write a request that cannot accidentally be interpreted as a completed change. Input: "Disable svc-enroll now?" Write action ID, revision, observed trigger, provisional target, proposed first step, risk, approval requirements, operator, expiry rule and verification plan. Model: primary request **bounded state validation and owner contact**; the account-disablement option is conditional. Record approval "pending," execution "not requested," result "not observed." Any filled-in success receipt is unsupported. Two points require explicit pending fields and a bounded alternative.

**EX008 — Option comparison.** Objective: reason about inaction and collateral damage. Input: A, B, C. Create a four-row comparison per option or four columns that make avoided harm, introduced harm, uncertainty and verification visible. Model selection A at 09:04 is justified because C02 only reports a symptom. B and C have unestablished mechanism/target and larger service cost. Two points require naming a later fact that would change the recommendation **without** treating that fact as received.

**EX009 — Approval ambiguity.** Objective: reject implicit expansion of authority. Input: V2 "OK to act." Write a clarification specifying target, environment, exact operation, duration, accepted disruption, approver authority, executor, rollback and check. Model status: "Clarification requested, no approved change, no execution." Two points require keeping V2 out of the C02 source ledger and keeping action unperformed.

**EX010 — Four-line decision record.** Objective: preserve checkpoint chronology. Input: C01/C02 and the proposed matrix. Model line 1 observation: C02 received 09:04, reported symptom, approximate onset. Line 2 inference: potential enrollment issue, current slot state unknown. Line 3 status: bounded investigation proposed, no export/disabling/notification documented. Line 4 review trigger: state check, new approved evidence, observed service harm or documented evidence-expiry warning. A two-point answer is usable as a handoff and contains no later cards.

### Common errors and limits

- **Authority laundering:** saying "incident lead approves" as shorthand for any disruptive service action. Correct by identifying the actual required owners and scoped decision reference.
- **Capability as permission:** knowing a cloud command does not grant the right to run it. Correct through role and policy verification before execution.
- **Optimistic rollback:** assuming re-enabling an account instantly restarts lost tasks or undoes data changes. Correct with post-change acceptance criteria and a named owner.
- **Verification inflation:** claiming tenant containment from a single observable route. Correct by naming exactly what was checked and what remains untested.
- **Variant contamination:** turning V2's ambiguous message into a main-case approval. Correct with scenario labels and separate state histories.

### Sources and scope

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final): authoritative background for integrating response with governance and organizational risk management; it does **not** supply CTN's approval matrix.
- [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20): provides outcome-oriented governance and response categories, not procedural authority to disable identities.
- All case times, action identifiers, state labels, training code and comparison tables above are synthetic instructional constructions.

### Synthesis

At C02, disciplined response means recording a real symptom, declining to invent a malicious actor, and routing precise proposals to legitimate decision owners. Proposal, approval, execution and effect verification are separate evidence states. The next chapter introduces additional signals, which may change the priority but never retroactively create an authorization.

### Continue studying — Chapter 02 of 12 (integration draft)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Chapter index](../../SUBJECTS.md) · [Canonical Chapter 02](../MANUSCRIPT.md#ch-02) · [Chapter 03 →](../MANUSCRIPT.md#ch-03)
