# Incident Response and Cyber Resilience: Professional Practice

- Language: English (`en`); professional course, six months; approximately 360 hours of planned study.
- Editorial state: **draft**. Subjects 1–5 of 12 have authored lessons, 25 numbered exercises and 25 worked results. Subjects 6–12, expansion, technical review, editing and the 300-page A4 gate remain open.
- Audience: new response practitioners working with a supervisor and an organization's approved procedures. Prerequisites: basic security concepts, identity, applications, logs and service ownership.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned text is dedicated under [CC0 1.0](../../../../../LICENSE); external sources retain their rights.
- Educational status: this is a public learning draft, not a completed textbook, credential or authority to operate on real systems.

[Course home](../../README.md) · [All subjects](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Answers](#worked-answers)

## How to study this draft

Read the five chapters in order. Each chapter is one curricular subject. Work the exercises before opening the answer section; every exercise specifies an artifact that another responder could inspect. Keep four columns in your notes: **observation, inference, decision, verification**. A plausible inference is not a collected fact. A proposed action is not approval, execution or a measured result. These distinctions matter more than a dramatic incident narrative.

This course's fictional case is **Cedar Training Network (CTN)**, an invented organization with an enrollment portal. All names, accounts, ticket IDs, timestamps, systems, policies, records and retention windows below are synthetic classroom data. There are no real personal records or reachable services. Record IDs `C01`–`C12` are case cards, not externally sourced facts. A card's *event time*, *ingestion time* and *release time* can differ. Unless a chapter expressly releases a later card, use only the information available at that chapter's checkpoint. Exercise variants marked `V` are separate simulations and do not rewrite the main case.

The recommended starting point for organizational incident-response outcomes is [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). It connects response to cybersecurity risk management; it does not give CTN's analyst the authority to change a production tenant. [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) provides outcome categories rather than this book's case procedure. The exercise worksheets, scoring rubrics, synthetic data and decision gates here are original teaching devices. Older [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) and [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) inform log-management and forensic vocabulary; their dated operational details must be checked against current tools and an organization's rules. In particular, this course does not offer legal chain-of-custody advice.

## Contents

1. [Incident lifecycle and organizational readiness](#ch-01) — define the service, owners, evidence readiness and first handoff.
2. [Authority, scope and response roles](#ch-02) — turn a charter into approval gates and reversible proposals.
3. [Alert intake and severity assessment](#ch-03) — reconcile signals and assign a reviewable priority.
4. [Evidence preservation and case records](#ch-04) — collect bounded copies and document provenance and limits.
5. [Investigation, hypotheses and timeline building](#ch-05) — test competing explanations without inventing an actor.
6–12. Containment planning, eradication, recovery, communications, tabletop validation, improvement and professional capstone: **planned in the [book plan](PLAN.md), not yet authored**.

The five authored subjects each end with five exercises. The [worked-answer appendix](#worked-answers) holds EX001–EX025 in the same book. Its model artifacts are examples of defensible reasoning, not a substitute for the local rubric or authority checks.

<a id="ch-01"></a>

## Chapter 1 — Incident lifecycle and organizational readiness

### Learning outcomes

After this subject, the learner can map a service's dependencies and owners, distinguish preparation from live case actions, write a falsifiable evidence-readiness check, and hand off a bounded gap list. The task is operational: a colleague should be able to use the map during an alert without guessing who owns a log, an approval or a restore.

### 1.1 Start with a service, not an alert product

An alert says that a sensor noticed a condition. A response plan must begin earlier: which service could be harmed, which business outcome matters, where relevant records originate, who may obtain them, who can authorize disruption, and what would make recovery acceptable. The [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) recommendations are organized within cybersecurity risk management, so preparation and improvement belong alongside case handling. For CTN, the service outcome is that a learner can find and enroll in an available class; an identity alert is relevant only through a plausible path to that outcome or to another protected asset.

CTN's invented service map has an enrollment front end, an API that writes slot records, an identity provider (IdP) for staff and automation, a notification queue, a support desk and an object-storage backup. A service map is an **inventory hypothesis** until an owner verifies it. The same warning applies to a diagram's arrows: an arrow labelled “logs to audit store” does not establish that all write paths produce a record, that timestamps use UTC or that a responder can obtain a copy before expiry. At professional depth, the learner is expected to name a proposed test for each such claim and record the result as *untested* until run.

| Dependency | Decision it might support | Custodian to identify | Failure or unknown at handoff |
|---|---|---|---|
| Enrollment API and audit | Which slot changed, by which request ID, at what recorded time? | Application owner | Audit coverage across scheduled and manual writes unverified. |
| IdP | Was an account authenticated, with which session and client fields? | Identity custodian | Account label is not a human identity; detailed-event retention unverified. |
| Support desk | When was a symptom reported and what did the reporter observe? | Support lead | A report does not establish authoritative slot state. |
| Backup and restore copy | Can a known-good slot state be reconstructed in isolation? | Recovery lead | Backup success and restore correctness are distinct claims. |
| Service change record | Was a slot change within approved scope? | Service owner | Approval scope and actual execution can differ. |

The owner map needs a **primary, alternate, contact channel and decision right** for each row. “IT” is not a decision right. An identity custodian may export a bounded log but may lack authority to disable an account; a service owner may approve a short pause but may not personally execute it. If the owner is unavailable, an escalation path must say when to use the alternate. No employee name or contact is required in this public fictional exercise; use role names.

### 1.2 Case card C01: an incomplete readiness inventory

At **08:40 UTC**, CTN's fictional preparation worksheet `C01` lists the six dependencies above. It names the application and recovery leads, but the after-hours identity alternate is blank. It asserts “API audit: 24 hours” without specifying whether that means event age, rolling availability, export queue age or a contract claim. The support desk can open an incident ticket, but the escalation contact for an unavailable service owner is missing. `C01` is a *worksheet discovered before the exercise*, not proof that the controls work. At this chapter checkpoint, no alert, compromise or patron harm has been established.

An evidence-readiness contract turns a source name into a testable question. For example: “If a synthetic change to slot S41 is made through the scheduled job, will an authorized analyst retrieve a record with slot ID, request ID, source event time and collection metadata within 20 minutes?” The test requires a permitted training tenant, a specific input, an expected event and a negative control: an unrelated slot S40 should not appear in the selection. Record the result only after a custodian runs it. If the selected export lacks a request ID, the next action is to revise the proposed correlation method; it is not to join by account name and nearby time as if the key existed.

A minimal contract has six fields: **decision question; expected producer and fields; time basis and retention; authorized custodian and access path; positive and negative rehearsal; failure signal and fallback**. Apply data minimization: if the question concerns slot S41, a full enrollment database export is usually unnecessary. Record whether a copy is proposed, approved, collected or verified. This is a teaching format, not a required NIST form.

### 1.3 A worked readiness handoff

Suppose the learner is the CTN analyst at 08:45 UTC. A defensible handoff says: “Enrollment is the service at risk. The application owner should confirm whether scheduled and manual changes are audited. The identity alternate and service-owner escalation are unknown. The claimed 24-hour audit retention has no verified anchor. No incident is inferred from C01. Before the next drill, the application custodian and identity custodian should run two bounded training events, record collection latency and compare an unrelated-slot control.” This identifies what to do, who can do it, and what remains unknown. “All logs are ready” would be unsupported.

Readiness priorities are based on **decision value and failure consequence**, not an arbitrary count of missing boxes. The missing after-hours identity route matters because a short retention window could close before the owner is reachable. The backup row matters because a completed backup job cannot answer whether slot state is correct or usable. The learner should preserve this distinction when later chapters introduce a live signal and an export deadline.

### Common mistakes and limits

- Treating a planned log source as a collected record. Corrective action: write a rehearsal result or mark coverage unknown.
- Treating a role name as an approval. Corrective action: identify the approving role, specific action, scope and timestamp.
- Assuming every application write path has the same audit fields. Corrective action: test scheduled, manual and alternate routes separately in an authorized lab.
- Claiming a backup can restore service from a job-status screen. Corrective action: require an isolated restore and owner-defined acceptance test.

### Practice: readiness workshop

In a synthetic worksheet, build the five-row map, mark unverified fields and write two tests that could fail. Do not run a production test. Exchange the worksheet with a partner who must tell you which owner to contact and what question to ask without asking for an unbounded data export. The deliverable is an owner-and-evidence handoff, not a speculative incident diagnosis. The next chapter will use this map to decide what the analyst may request when a signal arrives.

### Exercises — subject 1

**EX001 — Service dependency map.** Input: `C01` and the six CTN dependencies above. Produce a table with at least five dependencies, a decision each might support, custodian role and one unverified assumption. Assessment: 0 = missing decision/owner; 1 = map with vague assumptions; 2 = actionable, bounded map that does not claim the source is already verified.

**EX002 — Evidence-readiness contract.** Input: the proposed S41 scheduled-job change and unrelated S40 control. Produce all six contract fields, including expected fields, a 20-minute collection window and a falsifiable failure signal. State that the rehearsal requires a permitted training tenant. Use the EX001 rubric, with 2 requiring a negative control.

**EX003 — Owner escalation.** Input: `C01` has no after-hours identity alternate or service-owner fallback. Write a role-based primary/alternate matrix and the exact unanswered decision if each is unavailable. No personal contacts may be invented. A 2-point result distinguishes collection permission from disruptive-action approval.

**EX004 — Retention ambiguity.** Input: “API audit: 24 hours” in `C01`. Give three plausible meanings, one question to the custodian and a conservative readiness action. A 2-point result does not calculate a deletion deadline from an unanchored claim.

**EX005 — Readiness handoff.** Input: your EX001–EX004 artifacts. Write a 90–140-word shift handoff with service outcome, top two gaps, owners, proposed tests and no incident conclusion. A 2-point result labels tests as proposed and assigns owners.

### Subject synthesis

Readiness is a set of checked service, authority and evidence assumptions. `C01` alone cannot prove either preparedness or an incident. Carry its owner gaps and retention question into Chapter 2; do not silently fill them when the scenario becomes urgent.

<a id="ch-02"></a>

## Chapter 2 — Authority, scope and response roles

### Learning outcomes

The learner can translate an incident charter into action-specific permissions; separate an analyst's recommendation from an approver's decision and an operator's execution; and build a reversible, time-bounded escalation proposal. This chapter does not teach unsupervised tenant administration. Its practical product is a record that lets a supervisor say *yes, no or not yet* to a named action.

### 2.1 Why a role is not a blanket permission

The response lead coordinates priorities and records decisions. A service owner accepts service risk and defines a usable outcome. A custodian may retrieve a source record. An operator may execute a change after the required approval. A privacy or legal contact may advise on notice and handling where needed. One person may hold multiple roles in a small organization, but the case record still needs to say **which decision right** that person exercised. An incident severity label does not grant extra access or authority by itself.

In a cloud environment, actions vary enormously in blast radius. Exporting a bounded sign-in interval, revoking one session, disabling a shared automation account and changing tenant-wide access policy are different decisions. Some preserve service; others can interrupt enrollment for every learner. Before an action is approved, write its **target, purpose, expected effect, maximum duration, dependencies, rollback, verification and owner**. A proposed action becomes executed only when an operator records what actually happened and an independent observer checks the intended result. An approval record is not an execution receipt.

The classroom charter below is an original CTN teaching policy. It is *not* an authorization in any real tenant. In practice, the organization's approved emergency-change process, contractual constraints and jurisdictional duties control. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) emphasizes coordination in risk management, while the precise approval matrix must be established locally.

| Action class | Analyst may do in this fictional exercise | Approval / operator needed in a real organization | Why the boundary matters |
|---|---|---|---|
| Record intake and ask a bounded question | Draft ticket, document source and request authorized read-only review. | Custodian authorizes access to restricted records. | Even read-only data may contain personal or sensitive fields. |
| Preserve selected records | Specify time range, fields and retention reason. | Data/source custodian approves and performs collection under policy. | Bulk export creates unnecessary exposure and provenance risk. |
| Revoke one session | Compare effect and proposed rollback; do not issue a command. | Identity owner and service owner approve; authorized operator executes. | The session may belong to enrollment automation. |
| Disable `svc-enroll` or alter tenant policy | Escalate a risk statement and alternatives. | Emergency-change authority and service owner assess impact; operator acts only within approval. | Broad action can remove a critical write path and affect other services. |
| Notify external learners | Draft an audience-specific holding message. | Communications/privacy decision owner approves content and timing. | An unverified report is not a finding of exposure or outage. |

### 2.2 Case card C02: a report arrives before diagnosis

At **09:04 UTC** the fictional support desk receives `C02`: “Slot S42 appears unavailable in the enrollment portal; reporter first noticed it around 09:00.” The receipt time is known; the reporter's first-noticed time is approximate. There is no verified authoritative slot state, no record of a change and no evidence of who made one. A message from a cloud operations colleague asks, “Should we disable `svc-enroll` now?” The account name does not establish whether a person or scheduled job used it, and `C02` does not even connect the account to the symptom. The professional response is to open a case, preserve the report as a report, identify the service and decision owners, and ask for a bounded investigation. **Do not present disabling the account as an accomplished containment.**

The `C01` map makes the gap visible: the after-hours identity alternate and unavailable-service-owner route are blank. The analyst should not invent a substitute approval. Instead, record the owner gap and activate the organization's actual escalation route if one exists. In this synthetic exercise, the escalation status is “route not supplied; supervisor to determine.” That answer may feel unsatisfying, but it preserves the boundary. A real team should repair that readiness gap before depending on urgent account action.

### 2.3 Write a decision request that can be approved

Imagine a supervisor later considers a single-session revocation. A usable request has two parts. **Evidence basis:** which observed card supports the concern, what remains unknown, and what alternative explanation matters? At the current checkpoint, only `C02` exists, so there is insufficient evidence to name a session. **Proposed control:** which session, who owns the service, expected disruption, duration, monitoring, fallback and independent success check? A blanket “revoke suspicious sessions” lacks a target and a test. Chapter 3 will provide a candidate session field; it still will not identify a malicious human.

The request should be versioned when evidence changes. At 09:04 the recommendation may be “investigate and preserve.” At 09:14 new signals may justify a higher priority and an **approval request**, but the case record should retain the earlier rationale. This distinction protects decision quality: an analyst can explain why a reversible action was reasonable at a particular checkpoint, even if a later finding changes the plan.

A simple action record contains: case ID; proposed action ID; target; initiating observation; intended effect; prerequisite evidence or condition; authorizer and scope; operator; start and expiry; expected observable result; rollback owner; actual execution receipt; verification; and any unresolved effect. Fields for approval and execution start blank. Filling them with a suggested name or assumed outcome would falsify the record.

### 2.4 Compare actions by effect and reversibility

At the C02 checkpoint, consider three choices. **A: bounded read-only triage** checks the service report and seeks the relevant owner. It is proportionate and keeps service available, but it may be too slow if a short retention window is later confirmed. **B: targeted session restriction** might limit ongoing misuse if a specific session is established and approved; it may also interrupt automation and requires a success check. **C: disable the whole account or change tenant policy** can affect all enrollment writes, has a larger rollback burden and is not justified from C02 alone. The ranking is not a universal algorithm: if later evidence shows an imminent high-impact action, the authorized owners may choose a different option. The point is that **impact, evidence, scope and authority** must be named before the choice.

One way to compare options is a four-cell note: expected harm avoided, service harm introduced, remaining uncertainty and falsifiable verification. Do not reduce these to an unexplained numeric score. “Targeted” describes an intended scope; the operator still has to confirm the platform implements the target at that scope. If the platform only supports account-wide disablement, the team must reassess the plan rather than silently broadening it.

### Common mistakes and limits

- Confusing an urgent question with permission to execute. Record a recommendation and the approval gate separately.
- Writing “service owner approved containment” without the exact account, action, duration or acceptable service effect. Ask for bounded approval and retain the decision receipt.
- Treating an account label as an actor. Shared accounts and automation require additional records; even detailed logs can leave human attribution unresolved.
- Planning a rollback as “undo change.” Specify who can perform it and which observable condition triggers it. A rollback might not restore data that was changed while access was restricted.

### Practice: supervised decision meeting

In groups, assign analyst, service owner, identity custodian and recorder roles. Give everyone C01 and C02 only. The analyst presents the symptom and three candidate actions. The custodian describes which restricted source could be requested; the service owner states which enrollment disruption would be tolerable *if* supported; the recorder notes what was decided, what remains pending and the next review trigger. The exercise stops before any change or access to real data. Swap roles and compare the records: disagreement over evidence is useful if each claim names a source and time.

### Exercises — subject 2

**EX006 — Role-and-right matrix.** Input: C01 and C02. For case opening, bounded log retrieval, session revocation, account disablement and learner notification, name the recommending, approving and executing role; mark unknown escalation routes. A 2-point result keeps those responsibilities distinct.

**EX007 — Action request.** Input: the cloud colleague's “disable now” question at 09:04. Draft a proposed action record with target, trigger, service risk, approval, operator, expiry and verification. Fields unsupported by C02 must say *pending*, not contain invented receipts. A 2-point result recommends a bounded first step rather than asserting account misuse.

**EX008 — Option comparison.** Input: choices A, B and C in §2.4. Produce the four-cell comparison for each and select the most defensible first step at 09:04. A 2-point result explains why a later checkpoint might change the selection.

**EX009 — Approval ambiguity.** Fictional variant `V2`: a supervisor writes “OK to act,” without target or duration. Compose the precise clarification request and a one-sentence case status. Do not import V2 into the main C02 decision. A 2-point result leaves action unexecuted and names missing scope.

**EX010 — Decision record.** Input: C01, C02 and your EX006–EX009 work. Write a four-line decision log with observation, inference, action status and next review trigger. A 2-point result distinguishes a proposed preservation request from an approved export.

### Subject synthesis

The decision right belongs to a role and a bounded action, not to the incident label. C02 supports intake and owner escalation, not a tenant-wide change. Chapter 3 will add identity and application signals; revisit the options with the new cards while preserving the 09:04 record as it was.

<a id="ch-03"></a>

## Chapter 3 — Alert intake and severity assessment

### Learning outcomes

The learner can form one case from multiple signals without merging their claims, normalize clock readings with a stated uncertainty, assign a provisional response priority from impact and evidence confidence, and set a review trigger. At this level, triage is an auditable decision, not a prediction that an account was compromised.

### 3.1 Four times and three kinds of claim

An **event time** is when a source says something happened. **Ingestion time** is when a collector accepted the record. **Discovery time** is when a person or detector recognized it as relevant. **Release time** in this training case is when the learner may use the card. A support reporter's recollection is another kind of timestamp: it may be approximate and may refer to when a symptom was *noticed*, not when the underlying cause occurred. Put each time in a separate field and record the source's timezone and clock offset. Do not sort all strings lexically and call the result a causal sequence.

An **observation** is bounded by its producer: an IdP reports a successful sign-in for an account, an application audit reports an edit, a support ticket reports what a person saw. An **inference** joins observations: perhaps the sign-in and edit are related. A **decision** is what the team does under uncertainty: preserve details, check present service state or ask an owner for an approval. The distinction makes an analyst's reasoning testable. If a joined identifier is missing, nearby times can motivate a question; they cannot supply the missing join key.

### 3.2 Case cards C03–C08: contradictory signals

The following cards are **fictional and released in sequence**. At 09:09 the learner receives C03–C05; C06 arrives at 09:10, C07 at 09:12 and C08 at 09:14. The columns avoid mixing event and receipt times. All times below are UTC unless an offset is explicitly stated.

| Card and release | Source and source event time | Ingestion / receipt | Exactly what it supports; notable gap |
|---|---|---|---|
| C03, 09:09 | IdP summary: `svc-enroll` successful sign-in at 08:58; a summary displays session `s-77`. | Collector accepted 09:02. | The IdP labelled a sign-in successful; client and human actor fields are absent from this summary. |
| C04, 09:09 | Endpoint detector: browser process on `runner-03` at raw device clock 08:54. The device clock is measured **four minutes slow** relative to UTC in this synthetic snapshot. | Collector accepted 09:06. | Normalized event estimate is 08:58 UTC. There is no shared session or request ID. A browser on a runner can be benign. |
| C05, 09:09 | Enrollment API audit: slot S42 edit at 09:01, account label `svc-enroll`, request `q-144`; session field blank. | Audit collector accepted 09:07. | An application record reports an edit. It does not prove present slot state, intent or which human, if any, caused it. |
| C06, 09:10 | Maintenance calendar: 08:50 approved change lists slots S40 and S41 only. | Retrieved for case 09:10. | S42 is outside the *visible* approval scope. A later or missing addendum remains possible. |
| C07, 09:12 | Application owner states that `svc-enroll` is used by a scheduled job and sometimes an emergency operator. | Statement recorded 09:12. | The account is shared in this exercise; the statement is not a log of this specific use. |
| C08, 09:14 | Identity custodian says detailed IdP source events for this synthetic window expire at **10:00 UTC**. No export is yet in the case. | Statement recorded 09:14. | Creates a time-sensitive preservation request; it does not mean C03's summary has already been independently verified. |

The C04 conversion is elementary but consequential: a clock that displays 08:54 when UTC is 08:58 is **behind**, so add four minutes to its displayed event time. The normalized estimate coincides with C03's 08:58 sign-in, but the match is not evidence that the browser caused the sign-in. A real analyst would record how the offset was measured and its uncertainty; this exercise supplies only a fixed four-minute measurement, so do not claim subsecond ordering. C05's 09:01 edit happens later by the reported clock, but the missing session field prevents a direct `s-77`–`q-144` join.

### 3.3 Intake before severity

Open a single CTN case with `C02` as a symptom report and C03–C05 as separate sensor records. Intake should capture source, reporter/custodian, event and ingestion times, affected service, exact identifiers, original text or bounded copy reference, classification at this checkpoint, what is unknown, and next owner. Preserve the original card wording; a normalized timeline can be an additional view. If two alerts are clearly the same emitted event, link them; here C03, C04 and C05 have distinct producers and no confirmed correlation key, so keep three provenance lines.

Severity needs **impact**, **confidence**, **time sensitivity** and **decision cost**. CTN uses a classroom priority scale: `P1` = immediate owner-led coordination for an observed major service or safety impact; `P2` = urgent bounded investigation where meaningful harm is plausible or evidence may disappear soon; `P3` = routine review of a limited signal without a time-sensitive gap. These labels are *local teaching choices*, not a NIST severity formula. A team may have a different approved taxonomy. Record the rationale and the checkpoint time so another responder can reproduce the decision.

At **09:14**, a defensible CTN assessment is **P2, provisional**. The reported S42 symptom and recorded edit could affect enrollment, but the authoritative state and scope of impact are unknown. The account is shared, the cross-source join is weak, and an approved change covers other slots but not visible S42. The 10:00 source-expiry statement makes a bounded IdP preservation request urgent even if the probability of malicious activity remains uncertain. The next review triggers are: a custodian-approved detail export, an authoritative S42 state check, further user reports, a verified approval addendum, or the looming expiry. A different label could be defended if the learner cites an actual CTN policy and the same evidence limits; an unreasoned “critical compromise” cannot.

The team should distinguish **urgency of preserving evidence** from **confidence in compromise**. High urgency can coexist with low causal confidence. A useful escalation sentence is: “At 09:14, request authorized export of a narrow IdP window before the stated 10:00 expiry; separately ask the application owner to verify current S42 state. Do not disable `svc-enroll` without scoped service-impact review and approval.” This is a proposal, not proof the records were collected or the owner approved a change.

### 3.4 Handle a possible false positive without closing the case too early

The runner browser in C04 might be normal scheduled automation; the S42 display in C02 might be a stale front-end view; the calendar might omit a later addendum. These are **alternative explanations**, not findings. Closing as false positive requires criteria. For example, if the application owner supplies a scoped approval for S42, the job owner shows a matching `q-144` run with a validated join key, and the authoritative slot state is correct, the team could downgrade or close according to its policy. The current cards do not provide those checks. Conversely, a confirmed unauthorized edit or additional affected slots could raise priority. State a specific observation that would change the assessment, rather than “monitor.”

### Common mistakes and limits

- Ordering C04 before C03 because 08:54 appears earlier than 08:58. Normalize the known four-minute offset and retain uncertainty.
- Joining `s-77` to `q-144` by the account label alone. The application session field is blank; keep the relationship as a hypothesis.
- Treating C06 as proof no S42 approval exists anywhere. It proves only that the retrieved calendar entry lists S40 and S41.
- Letting the expiry claim itself authorize a bulk export. Use the approved custodian path and a bounded window and fields.
- Equating `P2` with a confirmed compromise. Priority governs response effort; it is not a forensic conclusion.

### Practice: timed triage board

In a synthetic workbook, record the case at 09:09, then reveal C06, C07 and C08 in their stated order. After each release, update an observation ledger and write the smallest decision that changes. Keep earlier entries rather than overwriting them. A peer checks whether the 09:09 decision cites only C02–C05 and whether the 09:14 preservation request names the custodian, selected time range and expiry trigger. This simulates a handoff under limited information without connecting to any real tenant.

### Exercises — subject 3

**EX011 — Intake form.** Input: C02–C05 at 09:09. Produce four separate source lines with event and receipt times, source identifiers, service implication, missing fields and one next question. A 2-point result does not join `s-77` and `q-144` as fact.

**EX012 — Clock reconciliation.** Input: C03 and C04. Give C04's normalized UTC estimate, the raw/normalized pair and a two-sentence explanation of what the coincidence with C03 does and does not establish. A 2-point result calculates 08:58 and preserves correlation uncertainty.

**EX013 — Priority decision.** Input: C02–C08 at 09:14 and the classroom P1–P3 rubric. Choose a provisional priority, separately state impact, confidence, expiry-related urgency and a review time or event. A 2-point result can justify P2 without calling the account compromised.

**EX014 — False-positive gate.** Input: C04, C06 and C07. Write two benign explanations, one concerning explanation and the minimum discriminator for each. A 2-point result does not use an uncollected record as evidence.

**EX015 — Shift escalation.** Input: C02–C08. Compose a 90–150-word message to the incident lead with observed facts, one bounded preservation request, an S42 state check, the C01 owner gap and a condition that would change priority. A 2-point result separates these requests from approved or executed actions.

### Subject synthesis

The 09:14 triage record carries uncertainty forward. `P2` is a documented workload decision driven partly by the 10:00 expiry, while account misuse remains unproven. Chapter 4 will test whether a bounded export and a screenshot can be preserved with enough provenance to support later analysis.

<a id="ch-04"></a>

## Chapter 4 — Evidence preservation and case records

### Learning outcomes

The learner can specify a bounded collection request, keep an original separate from an analysis copy, verify byte integrity where bytes are available, reconcile timezones and state the limits of an incomplete custody record. The goal is a repeatable case trail for a second responder, not a declaration that a file or screenshot proves a legal conclusion.

### 4.1 Preservation answers a question

The 09:14 decision asked whether detailed IdP records could distinguish account sessions and clients before a stated 10:00 expiry. The analyst should request a **source, time interval, fields, account or session selectors, purpose, authority and destination**. A reasonable first request is IdP detailed events for `svc-enroll`, 08:50–09:05 UTC, including event ID, source timestamp and timezone, account, session, client, outcome and any export metadata. The custodian decides whether the requested fields and scope are permitted. If the source stores all identities in a shared object, the analyst does not independently broaden collection; the custodian should propose the least-privileged way to satisfy the question.

Preservation is not the same as analysis. A custodian may copy source bytes to an access-controlled evidence store; an analyst may parse a read-only working copy; a reviewer may compare notes. Each should leave a separate receipt: who, what, from where, when, under which approval, with which tool or method and which integrity result. A hash helps detect a later byte change to **the hashed object**, not prove that the source system emitted truthful events or that a screenshot depicts the authoritative state. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses forensic techniques from an IT perspective, and [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log-management planning. This book's record fields and synthetic workflow are instructional examples; the organization's current evidence policy governs a live case.

### 4.2 New cards: one export and one screenshot

Assume the fictional identity custodian obtained case approval at 09:16 for the bounded IdP request. This approval is **part of card C09**, introduced now; it was not available in Chapter 3. At 09:18 the custodian provides `C09`, a UTF-8 CSV export described as sourced from the 08:50–09:05 UTC IdP window. Its readable summary contains two rows: `08:58,svc-enroll,s-77,success,runner-03` and `08:59,svc-enroll,s-78,denied,unknown`. The case intake says “copy received 09:18,” but the supplied screenshot of the export console does not show the export command, object version, original byte count or computed digest. **C09 is useful yet incomplete**. It corroborates that the exported rows have session/client fields, and it offers a possible C03/C04 connection. It cannot by itself establish that the CSV is a complete, unchanged copy of the underlying IdP source or connect either session to application request `q-144`.

At **09:22 UTC**, support supplies `C10`, a screenshot whose display clock reads **11:21 UTC+02:00** and shows S42 as “unavailable.” If that fixed offset is correct, the depicted display time is 09:21 UTC. The support ticket records receipt at 09:22 UTC. The capture device, clock-setting evidence, exact URL, account context and whether the front end was cached are missing. Do not replace those gaps with assumptions. The screenshot supports “someone supplied a picture of an unavailable display,” not “the database slot was unavailable at 09:21.” Its visible time is a *claimed capture/display time*, not the moment the original slot changed.

| Card | Source / stated event or display time | Case receipt | What remains to verify |
|---|---|---|---|
| C09 | IdP rows 08:58 and 08:59 UTC; export procedure not shown. | 09:18 UTC; approval documented 09:16. | Original object identity, complete scope, byte count/digest, custodian's method. |
| C10 | Screenshot display 11:21 UTC+02:00 = 09:21 UTC if clock/offset correct. | 09:22 UTC. | Capture device/time basis, page context, cache status, authoritative S42 state. |

### 4.3 A two-stage collection receipt

The analyst first writes a **request record**: `CTN-IR-014 / IDP-01`, requested by response lead at 09:14, limited to 08:50–09:05 UTC and the fields above, with intended custodian and expiry reason. Once C09 arrives, the analyst writes a **receipt**, not a fictional completed custody form: approved 09:16 by the case's identity authority; copy received 09:18; source described by custodian as IdP detailed export; two visible rows; original object ID, source query and byte-level integrity **not supplied**; use restricted to this case. The action item is to ask the custodian for those missing fields or a newly collected, documented copy while the source remains available. Never change the original CSV to “fix” missing columns. A parsed spreadsheet and a narrative timeline are derivatives, with their own filenames and provenance.

For C10, ask support to preserve the original screenshot file and ticket metadata. Record the displayed timezone and the arithmetic conversion as an *analysis annotation*. If a file is later obtained, compute a digest over that file's bytes, record tool/version and storage location, and compare copies. A cropped or re-encoded image has different bytes; hash equality should not be expected across transformations. The screenshot's content still needs contextual corroboration even when its file integrity is verified.

### 4.4 A safe byte-integrity lab

The next fixture `V4` is **not C09**. It is a local, artificial 34-byte payload that demonstrates reproducible SHA-256 without claiming an IdP export was verified. Run the snippet only in a local Python 3 interpreter; it reads no network or user data.

```python
import hashlib

payload = b"case=CTN-IR-014\nsource=idp-export\n"
print(len(payload))
print(hashlib.sha256(payload).hexdigest())
```

Expected output:

```text
34
1407e98f466990ff5aa4eee42cd30291826490e2c910ee57887824e6946136cc
```

Now change one byte in a **copy** and rerun: the digest should differ. The conclusion is limited to byte integrity of the classroom payload and copied bytes. It does not validate the truth, completeness, collection method or authority of C09. In a live case, a file's digest belongs in a receipt alongside the source identifier and approved collection path; the digest alone is a poor case record.

### 4.5 Evidence packages need an explicit negative claim

A second responder must be able to answer: “Which source did we actually receive, and which conclusion must we *not* draw?” For C09, “two visible rows associate `s-77` with client `runner-03`” is narrower than “the runner made the S42 edit.” For C10, “a supplied screenshot shows unavailable” is narrower than “S42 was unavailable to all learners.” Name negative claims in the package: no verified `s-77` to `q-144` key, no authoritative state, no validated full-source export, and no attribution of a human. These are **limits**, not evidence that the opposite is true.

A preservation queue orders requests by decision value and loss risk. C09's detailed source was stated to expire at 10:00, so its bounded metadata gap is time-sensitive. The C10 file and ticket should also be secured, but the visible screenshot does not replace the authoritative state check. A “collect everything” instruction makes privacy, review and provenance harder without answering a specific question. A narrow first collection may need an approved extension if a discriminator requires it; record that new request rather than retroactively widening the first one.

### Common mistakes and limits

- Calling a checksum a signature or proof of authenticity. A digest detects changed bytes only when a trustworthy baseline and object identity exist.
- Writing “UTC 11:21” for a display labelled UTC+02:00. Subtract two hours, and keep the source clock's verification status.
- Treating a screenshot as an authoritative database state or a CSV summary as a complete export. Preserve both and request the source-specific discriminator.
- Backfilling missing C09 collection fields with guesses. A gap is itself a finding about evidence quality.
- Changing an original file to make analysis easier. Work from a documented copy and keep transformation steps reproducible.

### Practice: peer evidence review

One learner prepares a C09/C10 package with a request, receipt, limitation note and proposed follow-up. A second learner, given only that package, must reconstruct what was actually available at 09:22 and ask a question that would discriminate display-only failure from a changed slot. The first learner scores the answer against the source and time fields, then revises the package. No real logs, accounts or screenshots are necessary; the classroom cards are sufficient.

### Exercises — subject 4

**EX016 — Bounded collection request.** Input: C08 at 09:14, C03 and C05. Write the IdP source, 08:50–09:05 UTC range, selectors, minimum fields, purpose, custodian, approval gate and requested result. A 2-point result does not demand a tenant-wide export or claim execution.

**EX017 — Two receipts.** Input: C09 and C10. Create separate receipt lines with source, event/display time, receipt time, approval where known, object integrity state and one explicit limitation each. A 2-point result distinguishes C09's missing digest from a verified hash of V4.

**EX018 — Hash verification.** Input: the V4 bytes and published SHA-256 above. Run the local snippet or independently recompute the digest, state the 34-byte count and digest, then explain one thing it establishes and two things it does not. A 2-point result gives the exact digest and refuses to authenticate C09 from V4.

**EX019 — Timezone annotation.** Input: C10. Calculate the apparent UTC display time, record the 09:22 receipt separately and write a caveat about the unverified capture clock and cached page. A 2-point result gives 09:21 UTC as *conditional*.

**EX020 — Preservation queue.** Input: C08–C10 and the S42 question. Rank two authorized follow-ups by imminent loss and decision value; identify owner, bounded scope and expected discriminator. A 2-point result asks for C09 collection metadata before expiry and an authoritative S42 state comparison without declaring either result received.

### Subject synthesis

C09 and C10 add detail, but the case remains open: an export has an incomplete provenance record and a screenshot is not the service's source of truth. Chapter 5 will use these bounded observations to build a timeline and test multiple explanations. The analyst must carry the missing fields into the hypothesis table rather than fill them with a story.

<a id="ch-05"></a>

## Chapter 5 — Investigation, hypotheses and timeline building

### Learning outcomes

The learner can build a source-traceable timeline, distinguish temporal coincidence from a causal join, maintain at least two competing explanations, identify a least-invasive discriminator and issue a handoff that a containment planner can use. The chapter teaches a **decision-quality investigation** rather than attribution to a person or a complete forensic reconstruction.

### 5.1 Normalize without losing the source

A timeline is a *derived view*. It should link each entry to the unchanged source card and show event time, confidence in the time basis, case receipt and significance. For C04, keep raw 08:54 and normalized estimate 08:58. For C10, keep the display's 11:21 UTC+02:00 and the conditional 09:21 conversion. For C02, record the reporter's “around 09:00” separately from the 09:04 ticket receipt. Do not turn that recollection into a timestamp precise to the minute or silently move a later-released card into the 09:04 decision.

At 09:22, the strongest joined facts are still limited. C09 gives `s-77` and client `runner-03` within its **supplied** export, while C03 gives a sign-in summary with `s-77`; C04 names `runner-03` but does not provide a session ID. C05's application record names `q-144` and the shared account but has a blank session field. A source-reliable join requires matching identifiers with verified semantics or a tested system relationship. Matching account labels and close times generate a useful hypothesis, not a causal link. The documented C09 provenance gap further limits how confidently one can rely on the CSV as a complete source.

### 5.2 Later cards C11 and C12

At **09:24 UTC**, support provides `C11`: an operator says S42 “might have been included in a late approved change.” No change ticket or addendum is attached. This is a lead to check, not a retroactive amendment to C06. At **09:26 UTC**, the application custodian provides `C12`: a read-only view of the C05 audit record shows request `q-144` with a self-reported job tag `batch-17`. The tag records what the application received; it is not proof the scheduled job actually originated the request. The custodian has not supplied a validated job-run record, session/request join or current S42 database state. These cards are now usable; they were unavailable at prior checkpoints.

| Timeline entry | Source and time basis | What can be said at 09:26 | What cannot yet be said |
|---|---|---|---|
| 08:50 | C06 calendar entry; retrieved 09:10 | Visible approved scope lists S40–S41. | No later S42 addendum exists anywhere. |
| 08:58 estimate | C04 raw 08:54, four-minute slow clock; received 09:09 | Runner browser event is approximately coincident with IdP activity. | Browser process caused the sign-in. |
| 08:58 | C03 summary; C09 supplied detail, received 09:18 | `svc-enroll` sign-in and `s-77` are reported; detail associates client `runner-03`. | A named human used that session or it made `q-144`. |
| 09:00 approximate / 09:04 receipt | C02 support ticket | A user noticed an S42 symptom around 09:00. | The underlying state changed at 09:00. |
| 09:01 | C05 app audit, supplemented by C12 at 09:26 | An S42 edit is reported as `q-144`; a self-reported tag says `batch-17`. | The job ran, the edit was authorized, or S42 is currently unavailable. |
| 09:21 conditional / 09:22 receipt | C10 screenshot | A supplied picture displayed S42 as unavailable. | All users saw that state or its database row matched it. |
| 09:24 | C11 operator statement | A possible addendum is asserted. | An addendum actually exists. |

The apparent ordering of C02's noticed symptom and C05's edit is a useful warning: **a symptom noticed “around 09:00” can be earlier than a recorded 09:01 edit**. This may reflect memory imprecision, earlier unrelated behavior, a time-base problem or more than one event. Do not repair the contradiction by moving C05 or by assigning an unprovided clock offset to the API. Instead, ask for a narrower support interview or a traceable front-end record. Such tension is often where an investigation finds its next good question.

### 5.3 Three competing explanations

Use a hypothesis table, not a single favored story. A hypothesis should specify a mechanism, supporting and contradictory observations, a discriminator that might fail, and what decision it would affect. Confidence is provisional and should not be collapsed into the case priority.

| Hypothesis | Current support | Tension or missing link | Least-invasive discriminator |
|---|---|---|---|
| H1 — scheduled job changed the wrong slot | Shared automation account, runner client in C09, `batch-17` tag in C12. | Tag is self-reported; no validated run record or `s-77`–`q-144` join; visible approval excludes S42. | Ask job owner for a bounded, preserved run record with request ID and approved slot list; verify tag semantics with application owner. |
| H2 — an unauthorized operator used the shared account | C07 says emergency humans can use it; S42 is outside C06's visible scope. | No human attribution, session-to-request link or evidence of intent; C11 suggests an unseen addendum could exist. | Ask identity custodian for approved access trail and service owner for signed change scope; compare only the relevant interval. |
| H3 — the display symptom does not reflect current authoritative slot state | C10 lacks cache and capture context; C02 is a report, not a database read. | C05 records an edit, so a pure display-only story must explain that edit and its effect. | Have service owner authorize a read-only, privacy-limited S42 state comparison and an uncached test view; preserve both results. |

Do not label H1 “confirmed” just because three fields sound consistent. They arise from distinct systems with different semantics, and the decisive join is missing. H2 does not become likely solely because C06 lacks S42; an unseen addendum remains possible. H3 cannot erase C05; it must account for the edit or accept that display and data effects are separate. This is why the **next evidence request** should be chosen for discrimination, not volume.

### 5.4 Choose requests by decision value

At 09:26, a bounded S42 authoritative-state check is likely to change the service-impact assessment and inform any containment plan. It should return the slot's current state, last change ID and time if available, without exporting other learners' records. The service owner or custodian must authorize it. A job-run record keyed by `q-144` could distinguish H1 from some H2 variants; first ask whether the job actually stores trustworthy request IDs. An approved change addendum could resolve the C06/C11 tension but would not, alone, show the application executed only approved slots. An identity access trail could strengthen or weaken H2, but account sharing may still prevent individual attribution.

Each request should have an **expected decision use**. “Please send all logs” has no bounded answer and often creates new privacy and provenance risk. “For `q-144`, provide the source run ID, producer, event time, approved slot list and original record identifier for 08:50–09:05, if available” can fail clearly if no such record exists. That failure is information about visibility, not proof of a particular mechanism.

When evidence conflicts, keep competing versions and a review point. A timeline should not erase C11's unverified claim when C06 shows a narrower visible approval. A second analyst should be able to see the source, release time and reason for each inference. The handoff to Chapter 6 should include a conditional action matrix: if S42 is presently wrong and a continuing write path is observed, ask the appropriate owners to compare containment options; if state is correct and the job record explains `q-144` under approved scope, consider downgrade with documented criteria; if records remain incomplete, preserve the uncertainty and avoid an irreversible broad change. None of those branches is an observed result in the current manuscript.

### 5.5 A worked 09:26 handoff

“CTN-IR-014 remains P2 provisional at 09:26. C05 reports an S42 edit through `q-144`; C12 adds a self-reported `batch-17` tag. C03/C09 report session `s-77` from `runner-03`; C04's corrected browser time coincides but lacks a join key. C06 lists approval only for S40–S41, while C11 claims a possible addendum without evidence. C10 depicts an unavailable page, not authoritative state. C09's object integrity and full collection method remain undocumented. Request owner-approved S42 state check and bounded job-run/addendum records. Do not assert a human actor or execute account-wide containment. Reassess on those results or before any further source expiry.” This is a compact artifact another shift can challenge.

### Common mistakes and limits

- Writing a smooth story that hides contradictions. Preserve the approximate C02 symptom time and the exact C05 event time as separate sources.
- Using a self-reported tag as proof of origin. Verify the producer and join-key semantics.
- Allowing a later statement to rewrite an earlier checkpoint. Version the timeline and note C11's 09:24 release.
- Promising attribution a shared account cannot provide. The team may still establish scope, impact and safe control options without naming a person.
- Demanding a broad export as the next step. Ask the smallest question that changes a decision, under the appropriate approval.

### Practice: hypothesis review board

Three learners defend H1, H2 and H3, each citing source IDs, one tension and a falsifiable next request. A fourth learner acts as recorder and rejects statements that use C11 or C12 before their release, convert missing data into negative evidence, or confuse the source clock with receipt. The board then builds a revised 09:26 handoff. No production access or live investigation is involved.

### Exercises — subject 5

**EX021 — Source-traceable timeline.** Input: C02–C12. Produce at least seven entries with event time or range, raw-to-normalized annotation where needed, case receipt/release, source ID and a limitation. A 2-point result preserves C02's approximate time and C10's conditional conversion.

**EX022 — Join audit.** Input: C03–C05, C09 and C12. Draw supported and unsupported links among `s-77`, `runner-03`, `q-144` and `batch-17`; name the one identifier or producer check needed for a direct join. A 2-point result does not claim `s-77` caused `q-144`.

**EX023 — Hypothesis matrix.** Input: C05–C12. Write H1, H2 and H3 with one supporting observation, one counterpoint and a falsifiable discriminator each. A 2-point result treats the job tag and possible addendum as leads, not findings.

**EX024 — Minimal next request.** Input: the 09:26 record. Choose two requests that most directly affect service impact and causal explanation; specify custodian, scope, approval, expected artifact and possible outcome that would change the plan. A 2-point result avoids bulk export and distinguishes a request from a received result.

**EX025 — Professional handoff.** Input: your EX021–EX024 artifacts. Write a 140–200-word 09:26 handoff with priority and rationale, supported timeline, two unresolved explanations, evidence quality gap, proposed requests, forbidden overclaim and next decision gate. A 2-point result could be used by a supervisor to plan Chapter 6 without inventing an approval.

### Subject synthesis and next step

This five-chapter sequence moves from prepared ownership to bounded authority, triage, preservation and competing explanations. It has **not** performed containment, eradication or recovery. [Chapter 6's plan](PLAN.md#ch-06) introduces containment planning and approvals; its full lesson and exercises still need authorship. Before moving on, a learner should be able to tell another responder what was actually observed, what remains a hypothesis, which source might resolve it and who has the right to act.

<a id="worked-answers"></a>

## Worked answers and assessment notes

These are model results for the **fictional** CTN case. Each exercise's local 0–2 criterion controls scoring. An alternative answer is acceptable when it uses the released cards, names its assumptions, respects authorization and produces the required artifact. A source that is absent is *unknown*, not negative evidence. No model answer below records an action that the case did not perform.

### Subject 1: EX001–EX005

**EX001 — Model service map.** A sufficient table includes (1) API audit → identify slot S42 write/request ID → application custodian → scheduled-route coverage unknown; (2) IdP → sign-in/session fields → identity custodian → detailed retention unknown; (3) support → symptom and receipt → support lead → reporter's observation not verified state; (4) change calendar → approved slot scope → service owner → addendum process unknown; (5) backup → candidate restore copy → recovery lead → last isolated restore unknown. This is a *readiness map*. It does not assert that S42 was changed or that these sources were collected at 08:40. Two points require a decision and a real gap in every row; “IT owns everything” earns at most one.

**EX002 — Model contract.** Decision question: can a responder retrieve a scheduled-job change to S41 within 20 minutes and distinguish it from unrelated S40? Expected producer: API audit, with slot ID, request ID, producer, UTC event time and collection time to verify. Time/retention: ask the custodian how long each event remains and start a 20-minute test clock at the authorized event. Access: application custodian in a permitted training tenant, with no personal enrollment data. Positive test: execute a *synthetic authorized* S41 change and recover its record. Negative control: query the same bounded selector and confirm unrelated S40 is absent; also check whether an alternate write route emits an event. Failure: missing `request_id`, wrong slot, missing event, inaccessible export or collection after 20 minutes. Fallback: retain the failed result, ask the owner for a narrower alternative source, and revise correlation plans. This is a **test plan**, not a successful test report.

**EX003 — Model escalation matrix.** Identity export: primary identity custodian, alternate **missing in C01**, response lead can request but cannot appoint an unauthorized substitute. Account/session restriction: identity owner plus service owner/emergency-change approver decide scope; an authorized identity operator executes; fallback approval route **not supplied**. Service-outage tolerance: service owner decides; after-hours delegate **missing**. Case coordination: incident lead records the owner gap and escalates through the organization's actual supervisor process if available. The unanswered decision is who can approve time-sensitive identity collection or disruption when the primary is absent. A plan that names a made-up person or treats the analyst as approver loses the boundary point.

**EX004 — Model retention clarification.** “24 hours” might mean a rolling window measured from source event time, an export queue lifespan measured from request time, or a contractual maximum that has not been technically checked. Ask the application custodian: “For which exact dataset and anchor event does the 24-hour period begin, and can a permitted test verify availability near the edge?” Conservative action: document the ambiguity, prepare a bounded query and test in a training tenant; do not compute a deletion deadline or declare the source safe for a day.

**EX005 — Model handoff (102 words).** “CTN enrollment depends on the API, IdP, support and recovery services. C01 names an application and recovery lead, but it leaves the after-hours identity alternate and service-owner fallback blank. The asserted API-audit 24-hour window has no defined anchor. The response lead should ask the application custodian to test one synthetic scheduled S41 change and an unrelated S40 control, recording fields and retrieval time. The identity custodian should verify detailed-log retention and its authorized export path. The service owner should assign an emergency delegate and define an isolated restore acceptance test. These are proposed readiness checks; C01 contains no incident observation.” A shorter result can earn two points if it retains all required roles, gaps and status distinctions.

### Subject 2: EX006–EX010

**EX006 — Model rights matrix.** Case opening: analyst recommends/records, incident lead coordinates, no system change. Bounded IdP retrieval: analyst requests, identity custodian approves under policy and performs export; other data owners may be required by local rules. Session revocation: analyst recommends, identity owner and service owner/emergency-change role approve the named session, authorized identity operator executes and verifies. Account disablement: service owner plus emergency-change authority weigh enrollment impact; authorized operator executes only a scoped approval. External learner notification: communications/privacy owner approves content and audience; designated communicator publishes. C01 lacks the after-hours identity alternate and service-owner fallback; mark both *unknown*, rather than assign a fictional person.

**EX007 — Model action request.** `CTN-IR-014 / A-01`: trigger C02 report received 09:04; proposed first action is bounded support validation and owner contact, not disablement. Target S42 symptom and relevant service owner; expected effect better state/context with no service disruption. Account disablement is a **contingent alternative** whose target, time limit, service dependency, rollback and success check must be agreed before approval. Approval = pending; operator = pending; execution time = blank; verification = pending. The cloud colleague's question is not a receipt of any of these steps.

**EX008 — Model comparison.** A, bounded triage: harm avoided = reduces mistaken disruption; harm introduced = analyst time; uncertainty = present S42 state; verify with owner-authorized read-only check. B, targeted session restriction: possible ongoing-use reduction; risk = breaks an automation session; uncertainty = session-to-harm relation; verify by scoped session status and service-health checks after approval. C, account/tenant change: broader possible restriction; risk = all enrollment writes or other services fail; uncertainty = whether shared account caused anything; verify broad policy state, service checks and rollback. At 09:04 select **A** because C02 alone supports a symptom, not an identified malicious session. A newly verified destructive action could change the balance, subject to owner approval.

**EX009 — Model clarification for V2.** “Please identify the exact account or session, permitted action, environment, maximum duration, service impact accepted, operator, rollback owner and approval reference; does your ‘OK’ cover a bounded log request or a disruptive tenant change?” Case status: “V2 supervisor message received; scope insufficient for action; no production change approved or executed.” V2 is separate from C02. “OK to act” should not be stretched to authorize an unspecified tenant-wide edit.

**EX010 — Model four-line log.** Observation: “09:04 support received C02; S42 reportedly unavailable, first noticed around 09:00.” Inference: “Potential enrollment issue; cause and authoritative state unknown.” Action status: “Case opened, service/identity owner contact and bounded preservation request **proposed**; no export, restriction or notification recorded.” Trigger: “Revisit after owner state check, relevant source receipt, new reports or a verified retention deadline.” This preserves what the analyst knew at 09:04.

### Subject 3: EX011–EX015

**EX011 — Model intake lines.** C02: symptom noticed around 09:00, received 09:04, reporter observation only, ask for scoped S42 state. C03: IdP event 08:58, ingested 09:02, released 09:09, `svc-enroll`/`s-77`, no client or human field in summary, ask for authorized detail. C04: endpoint raw 08:54, normalized estimate 08:58, ingested 09:06/released 09:09, `runner-03`, no shared session key, ask whether scheduled browser activity is expected. C05: API edit 09:01, ingested 09:07/released 09:09, S42/`q-144`/`svc-enroll`, blank session, ask application custodian for authoritative state and key semantics. The four lines must remain distinct; a combined “runner session edited slot” line is unsupported.

**EX012 — Model clock calculation.** C04 device displays 08:54 while measured four minutes slow; adding four minutes yields approximately **08:58 UTC**. C03's reported sign-in also occurred at 08:58, so the events are temporally coincident at the given minute precision. Because C04 lacks a session ID and the offset's uncertainty is not specified, coincidence neither proves a shared transaction nor orders the two within that minute.

**EX013 — Model priority decision.** At 09:14 choose classroom **P2 provisional**. Potential impact: an S42 enrollment slot may be wrong, but present state and number of users affected are unknown. Confidence: C05 reports an edit, yet `s-77` has no verified link to `q-144`, and account sharing prevents attribution. Urgency: C08 states detailed events expire at 10:00, so ask the authorized custodian for a bounded export now. Review on the first of export receipt, S42 state, verified approval addendum, further symptoms or a short supervisor checkpoint before 10:00. A justified alternative priority can score two if tied to an explicit local rubric and no compromise claim.

**EX014 — Model gates.** Benign explanation 1: C04 browser is scheduled runner activity; discriminate with a preserved, approved job-run record and known expected process behavior. Benign explanation 2: C06's visible calendar is incomplete; discriminate with a signed S42 addendum and its scope. Concerning explanation: shared account used outside approval to edit S42; discriminate with identity access trail, validated session/request join and change scope. None of these source records is in hand at 09:14, so the labels remain hypotheses. A “false positive” closure would need the organization’s actual closure rule and supporting results.

**EX015 — Model escalation (108 words).** “At 09:14 CTN enrollment remains P2 provisional. Support reported S42 unavailable; the API recorded an S42 edit through `q-144`, while the IdP reported `s-77` and the endpoint showed a roughly coincident runner browser event. No session-to-request join or human attribution exists. C06's visible approval covers S40–S41; an addendum has not been checked. C08 says detailed IdP source data expires at 10:00. Please authorize the identity custodian to preserve only `svc-enroll` events from 08:50–09:05 with source metadata. Ask the application owner for present S42 state. The after-hours identity alternate remains undefined in C01. Reassess after either result or before source expiry; no account change has been approved.”

### Subject 4: EX016–EX020

**EX016 — Model request.** `CTN-IR-014 / IDP-01`, requested 09:14: identity custodian to preserve detailed IdP events for `svc-enroll`, 08:50–09:05 UTC, selecting event ID, original source timestamp/zone, session, client, outcome, account and export/source metadata. Purpose: test whether the summary's session/client fields can be reviewed before C08's 10:00 expiry; limit any other identifiers under custodian policy. Approval gate: identity authority and any applicable case/data owner. Expected result: source object ID, export query, byte count, digest and restricted copy location. At 09:14 these are **requested**, not received. At 09:16 C09 later supplies an approval, but do not use that to backdate the request's status.

**EX017 — Model receipts.** C09: IdP detailed CSV described as 08:50–09:05 source range, two reported events 08:58/08:59, approval at 09:16, case copy received 09:18; object ID, byte count and digest not supplied; completeness and integrity **unverified**. C10: support screenshot displays 11:21 UTC+02:00, conditionally 09:21 UTC; ticket receipt 09:22; original file identity, capture device, clock and cache context unknown; displayed symptom only. V4's digest must not be copied into the C09 receipt. If a later collection fills a field, add a dated supplement, not a silent edit of the original receipt.

**EX018 — Model hash result.** The exact V4 payload has **34 bytes** and SHA-256 `1407e98f466990ff5aa4eee42cd30291826490e2c910ee57887824e6946136cc`. Recomputing this on the stated bytes verifies that the local fixture and published expected digest agree. It does **not** show that C09's CSV has those bytes, was completely collected, or contains true IdP events. A different digest after changing one byte in a copy demonstrates sensitivity to byte changes, not authenticity of an external system.

**EX019 — Model time annotation.** The screenshot's displayed 11:21 with a fixed UTC+02:00 label converts to **09:21 UTC** after subtracting two hours; the support desk received it at **09:22 UTC**. Record raw display, stated offset, conditional conversion and receipt in separate fields. Without capture-device clock evidence and cache context, do not claim that the authoritative S42 state changed at 09:21 or that every viewer saw the same result.

**EX020 — Model queue.** First ask the identity custodian, under the case approval, for the C09 source object ID, exact bounded query, byte count/digest and collection method before the stated 10:00 source expiry; this can determine whether an analysable copy exists. In parallel ask the service/application owner for an approved read-only S42 authoritative-state and last-change check with minimal fields; it can distinguish current state from a displayed symptom. Neither follow-up result has arrived in the case at 09:22. Reasonable ordering can differ if the learner preserves the deadline, authority and discriminator.

### Subject 5: EX021–EX025

**EX021 — Model timeline.** A valid seven-entry core is: C06 approval 08:50 (retrieved 09:10; S40–S41 only); C04 raw 08:54/normalized approximately 08:58 (ingested 09:06, released 09:09; no session); C03 sign-in 08:58 (ingested 09:02, released 09:09; account, not human); C02 noticed around 09:00 (received 09:04; reporter estimate); C05 edit 09:01 (ingested 09:07, released 09:09; `q-144`, blank session); C09 detail rows 08:58/08:59 (received 09:18; missing original-object metadata); C10 displayed 11:21 UTC+02:00, conditional 09:21 UTC (received 09:22; capture clock/cache unverified). Add C11 at 09:24 and C12 at 09:26 if useful. Keep a separate release/receipt column so the 09:04 analyst does not “know” C12.

**EX022 — Model join audit.** Supported **within supplied records**: C03 and C09 both report `s-77`; C09 associates that session with client `runner-03`; C04 independently reports a browser on `runner-03`. C05/C12 bind `q-144` to an S42 edit and a self-reported `batch-17` tag. **Unsupported:** direct `s-77`→`q-144` causal link, C04 process→IdP session, tag→validated job run, or any human attribution. Ask the application/identity custodians whether a trustworthy common session or request ID exists across the relevant sources, and test its semantics on an authorized known-good transaction. If no common key exists, state that a direct join is unavailable.

**EX023 — Model hypotheses.** H1, scheduled-job wrong-slot change: C09 runner client and C12 batch tag support a lead; C06 excludes visible S42 approval and run/request join is absent; request a preserved run record keyed to `q-144` plus approved slot list. H2, unauthorized emergency use: C07 establishes a shared-account possibility and C05 reports an S42 edit; C11 raises an unverified addendum and no human/session join exists; request scoped access trail and signed approval scope. H3, display-only symptom: C10 lacks cache context; C05's reported edit is contrary unless it was authorized, harmless or later reverted; request authoritative S42 state and uncached view comparison. These are competing mechanisms, not mutually exclusive certainties.

**EX024 — Model next requests.** Request 1: service owner authorizes an application custodian to retrieve current S42 state, last change/request ID and a privacy-limited uncached view; if state is incorrect, service impact/containment review rises, while a correct state could narrow the harm claim. Request 2: job/application custodians provide a bounded `batch-17` run record and the semantics connecting its request ID to `q-144`, under case approval; a validated match favors H1, while a missing or mismatched run leaves H1 unproven and H2 open. Ask separately for a C11 addendum if available. Do not claim any of these results has been received.

**EX025 — Model handoff (156 words).** “CTN-IR-014 is P2 provisional at 09:26 because a reported enrollment symptom and C05 S42 edit merit urgent review, while the affected state and actor remain unknown. C03 reports `s-77` at 08:58; C04's corrected runner event is approximately coincident; C09 supplies client `runner-03` but lacks complete collection metadata. C05 reports `q-144` at 09:01. C12's `batch-17` is a self-reported tag, not a validated job run. C06's visible approval covers S40–S41; C11 suggests an addendum without providing one. C10 depicts an unavailable page, not authoritative S42 state. Scheduled-job error and unauthorized shared-account use remain plausible; display/cache behavior may affect the symptom. Ask the service owner for a bounded S42 state check and the job/application custodians for a `q-144` run record and join semantics. Do not attribute a human or disable the shared account on this record. Reassess after authorized results or before further evidence loss.”

## Glossary for the authored subjects

- **Authoritative state:** the owner-designated source used to decide the current service value; it still requires an approved, scoped check.
- **Custodian:** role that can supply or manage a particular record under policy; not automatically the incident approver.
- **Decision gate:** named condition, owner and evidence needed before a proposed action can advance.
- **Event / ingestion / receipt time:** source occurrence, collector acceptance and case-team acquisition, respectively; they can differ.
- **Hypothesis discriminator:** a bounded observation that could change support for competing explanations.
- **Provenance:** recorded source, acquisition method, authority, transformations and integrity information for an artifact.
- **Reversible proposal:** planned intervention with a target, limit, monitor and rollback owner; it is not the executed intervention.

## References and case boundaries

- [NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (2025): current high-level response guidance used for the readiness and coordination framing. CTN's priority scale and worksheets are local teaching inventions.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) (2024): risk-management outcomes; it does not prescribe CTN's action charter.
- [NIST SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final) (2006): log-management concepts; technical implementation details must be checked for present systems.
- [NIST SP 800-86, Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final) (2006): forensic vocabulary from an IT perspective; not a legal standard or complete modern tool procedure.

All C- and V-series records and every worked scenario in this manuscript are fictional. The citations support general concepts and are not evidence that any CTN event occurred.
