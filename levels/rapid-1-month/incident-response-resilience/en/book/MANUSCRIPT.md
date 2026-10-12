# Incident Response and Cyber Resilience: A One-Month Guided Course

- Language: English (`en`)
- Level: rapid course, one month; approximately 80 hours of planned study
- Editorial state: **draft**. All 4 subject-chapters have initial teaching text, 50 specified exercises and corresponding worked results. Substantive teaching expansion, specialist review, editing and A4 page verification remain pending.
- Public access: this draft is available to read and study; it is **not** a complete 300-page book or a qualification.
- Authorship and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi)
- Rights: original maintainer-owned text is dedicated under [CC0 1.0](../../../../../LICENSE); cited sources retain their own rights.

[Course overview](../README.md) · [Four-subject chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md) · [Book plan](PLAN.md) · [Practice playbooks](../../../../../playbooks/incident-response-resilience/README.md)

[Chapter 1](#ch-01) · [Chapter 2](#ch-02) · [Chapter 3](#ch-03) · [Chapter 4](#ch-04) · [Worked results](#answers)

## How to study this draft

Read a chapter's explanation and worked case before looking at its exercises. Record observations, assumptions, decisions and missing information separately. Use only the fictional systems and records provided here, or an environment you own and are authorized to test. The worked results at the end illustrate acceptable reasoning; an answer that identifies different defensible assumptions may also be valid.

The one-book curriculum has four subjects: (1) incident readiness, roles and authorized scope; (2) alert triage and evidence preservation; (3) containment, eradication and recovery decisions; and (4) a guided simulation with an after-action review. Each subject is one chapter. The current draft contains 50 exercises, with their worked results in the final appendix. The exercise count alone does not satisfy the full publication standard.

| Chapter | Subject | Planned exercises | Written exercises | State |
|---|---|---:|---:|---|
| 1 | Incident readiness, roles and authorized scope | 13 | 13 | Draft; technical and editorial review pending |
| 2 | Alert triage and evidence preservation | 13 | 13 | Draft; technical and editorial review pending |
| 3 | Containment, eradication and recovery decisions | 12 | 12 | Draft; technical and editorial review pending |
| 4 | Guided incident simulation and after-action review | 12 | 12 | Draft; technical and editorial review pending |

<a id="ch-01"></a>

## Chapter 1 — Incident readiness, roles and authorized scope

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Explain why incident response begins before an alert appears and continues after service recovery.
2. Distinguish an observation from an interpretation, a response decision and a confirmed fact.
3. Identify the service owner, response lead, analyst, recovery lead and communications contact for a small incident.
4. Define the scope and authorization for a contained response exercise.
5. Open an incident record with a timeline, evidence pointers, uncertainty and decision ownership.
6. Describe a safe first action when a suspicious signal has not yet been verified.
7. Turn a service dependency map into a bounded evidence-readiness plan without treating a planned log source as a collected fact.

### 1.1 Response is part of risk management

An incident response team does more than react to an alarm. It prepares contacts and authority, recognizes potentially harmful activity, preserves facts, makes proportionate decisions, restores services and learns from the result. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places incident response recommendations throughout cybersecurity risk management as described by the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework/faqs). The framework's Govern, Identify, Protect, Detect, Respond and Recover functions are concurrent and continuous activities. A team should not wait for “Respond” to think about owners, backups, communications or evidence.

There is an important distinction between a **function used to prepare for response** and an **action taken during a particular case**. The model in [NIST SP 800-61 Rev. 3, section 2.1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) places Govern, Identify and Protect in broad preparation and risk management; Detect, Respond and Recover describe the case-facing response activities. Its improvement category connects lessons back to all of them. This is a model for organizing outcomes, not a requirement that every case move through six isolated steps. In Harbor Library, naming an authorized service owner belongs to readiness; checking today's booking edit belongs to investigation; deciding whether to restrict an account belongs to response. An improvement ticket after the exercise may change the owner's contact list before the next case.

A beginner can test readiness with four questions: **What service might be harmed? Which records could show what happened? Who may approve a disruptive action? What result would show that normal service is safe to resume?** A team that cannot answer them has work to do even if its alerting system is excellent. Conversely, answering them does not establish that a particular alert is malicious. The distinction prevents a control inventory from being mistaken for an incident finding.

Consider a small library that provides room reservations online. An alert may say that an administrator account signed in at an unusual hour. That is a **signal** worth examining. It does not by itself prove account compromise. A change to the reservation database may be an **event** with business effect. The team must assess context, evidence and impact before it labels the situation a confirmed **incident**. These are working definitions for this teaching case; an organization should use its own approved classification policy.

The first useful question is: **Which service and people could be harmed, and what is known right now?** A team that records uncertainty can act quickly without pretending to know a root cause. A team that labels every alert “breach” risks needless disruption; a team that dismisses every alert risks delayed containment.

### 1.2 A fictional service map

The course uses **Harbor Library**, a fictional organization. No personal records or real network are involved. Residents reserve study rooms through a website. Front-desk staff can edit bookings. A separate event-newsletter list contains contact addresses. The booking service depends on a web application, an identity service, a database, a nightly backup and a staff help desk.

| Service dependency | Why it matters | Owner to consult | Evidence useful during an incident |
|---|---|---|---|
| Booking application | Residents and staff create or change reservations | Service owner | Request logs and change history |
| Staff identity service | Controls who can edit bookings | Identity administrator | Sign-in records and account changes |
| Reservation database | Holds the current schedule | Data steward | Audit log and backup state |
| Nightly backup | Supports restoration | Recovery lead | Last successful run and restore test |
| Help desk | Receives user reports | Response coordinator | Ticket times and reported symptoms |

This map is incomplete on purpose. It does not say whether the application uses third-party hosting, how clocks are synchronized, or who can approve a service outage. A response team should record those as **readiness gaps** before a crisis. If one dependency fails, the team can then ask the correct owner for evidence and options.

#### From dependency map to evidence-readiness contract

A service map names components and owners; it does **not** show that an investigator could answer a specific question on time. A useful next step is an **evidence-readiness contract**: a short, testable agreement about which source would record an event, what its fields mean, who may retrieve it, how long a useful record can remain available and how a second analyst could reproduce the selection. This is a CyberABC teaching device, not a required form from [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). NIST's incident-response guidance places preparation, service knowledge and response roles within broader risk management; the contract below turns that general orientation into a small fictional library exercise.

Begin with a **decision question**, rather than a product name. The practice records introduced in section 1.7 will include a cancelled booking B18 and the `desk-a` account; treat them as a preview here. “Do we have logs?” is too broad. “Was the B18 cancellation an approved staff action, and did the current booking state reflect it?” separates an activity question from a business-state question. A booking audit could record an edit, but an authoritative state comparison would be needed to confirm what users can book now. Similarly, an identity service could report that the account `desk-a` signed in, while neither the account label nor a timestamp identifies the human at the keyboard. The evidence plan should say what a source can *discriminate* and which tempting conclusion it cannot carry.

For each question, write six fields **before** the incident: (1) the producer and event it is supposed to emit; (2) identifiers that might connect records without silently merging different people or actions; (3) event time, collection time and clock or timezone assumptions; (4) the custodian, approved collection path and access limit; (5) expected retention and failure indicators; and (6) a small authorized rehearsal that could show whether the source actually works. Blank or untested fields remain **unknown**. A diagram that shows a log arrow without these details is an architectural hypothesis, not proof of coverage.

The following is a **proposed D1 design card**, written for an isolated training version of Harbor Library. It is a plan for what owners would test, **not** a new R-series record, a description of the library's actual logging configuration or evidence available at the 09:05 checkpoint. Field names such as `request_id` and `session_id` are candidate design fields; their existence and semantics must be checked before a real correlation.

| Decision question | Proposed source and joining field to verify | Custodian and permitted check | Claim that remains blocked without the check |
|---|---|---|---|
| What booking value changed and what is the current approved value? | Application change record keyed by booking ID and request ID; restricted current-state copy compared with an owner-approved target. | Application custodian provides a bounded audit selection; service owner approves the target and state comparison. | An edit record alone does not prove the present state or whether the change was authorized. |
| Was a staff session associated with that application action? | Identity session record and application record; test whether both use the same session-key namespace and time basis. | Identity administrator and application custodian provide only the permitted fields after incident-lead approval. | A matching account label or nearby time does not identify a human, an intent or a causal link. |
| What user-facing harm is supported? | Help-desk report with its receipt time, plus an authorized comparison of a patron view and approved booking state. | Help desk receives reports; service owner defines a narrow, privacy-aware impact check. | A single report does not measure all affected patrons; a correct database row alone does not prove the display was correct. |
| Could the booking service be restored with correct data? | Backup manifest, candidate copy, isolated restore result and a comparison against the approved schedule. | Recovery lead tests an authorized copy; service owner accepts or rejects the result. | A completed backup job does not demonstrate restore duration, booking correctness or service acceptance. |

The four-row card is a **summary**, not a completed six-field contract. For the first row, a fully specified *proposed test record* would read as follows. Its field names, times and expected observations are invented for a future isolated rehearsal; none is claimed to exist in R1–R8.

| Contract field | Proposed entry to check before relying on it |
|---|---|
| Producer and event | Ask the application custodian whether a booking change, including one made through an alternate write route, emits a distinct audit event. The event name and coverage are unverified. |
| Joining identifiers | Test whether booking ID and request ID are present and unique for this action. Do not join an identity record on username or nearby time alone; any session key needs a demonstrated shared namespace. |
| Time basis | Record the event's original timestamp and timezone, collector receipt time and analyst query time separately. Clock tolerance and delayed-arrival behavior remain unknown until measured. |
| Custody and access | Obtain incident-lead approval for a restricted selection by the application custodian of the synthetic test booking over 09:59–10:03 UTC. Keep the unrelated newsletter list outside scope. |
| Retention and failure signals | Ask the custodian to demonstrate the oldest retrievable test event, collector lag and a visible failure indicator. Until this check, do not write a retention guarantee or call an empty query complete. |
| Falsifiable rehearsal | If an isolated test is approved, predeclare a synthetic edit at 10:00 UTC and an out-of-range control at 10:10 UTC. Expect only the first inside the bounded query; save the exact filter, execution time and any missing-field or collection failure. This is a proposed procedure, not a reported result. |

The four-row decision card is deliberately **two-sided**. It names a source, then names what would still be unknown after seeing it. That prevents the familiar slide from “log exists” to “question answered.” Its first row also distinguishes an *activity record* from a *state-of-the-world record*. If an application audit says B18 was cancelled but the restricted current-state copy is missing, the analyst can report the recorded cancellation and request the state comparison. The analyst cannot certify the live schedule from the audit alone. Its second row anticipates Chapter 2's correlation exercise: even a supplied exact session-key match narrows a record relationship, not the identity or authorization of a person.

**Trace where an observation could be lost.** A missing search result has several different causes. The producer might never emit the event; an emitted event might fail collection; a collected record might arrive after the query; an available record might already have aged out; access controls might deny the selected view; the query might use the wrong booking ID, timezone or time window; or a reviewer might misread a real row. The response to these failures differs. Repeating the same query cannot repair non-emission, and asking for a broad export is not a substitute for fixing a wrong filter. A readiness review therefore records the *last confirmed point* in the path from producer to learner and a named owner for the next check. Do not collapse every empty result into “the system had no activity.”

**Make a rehearsal falsifiable.** In an isolated, explicitly approved training copy, an owner could predeclare one synthetic booking change and one deliberately out-of-range control event. The application custodian would record the test request ID and UTC event time; the collector would record receipt time and source; the analyst would run a bounded query and save the exact filter and run time. The expected result is the in-range change and its agreed fields, with the out-of-range control excluded by the declared interval. If the expected row is missing, the team investigates emission, transport, retention, access and query scope in order. If the out-of-range row appears, the filter or time interpretation needs correction. Passing this small rehearsal shows only that the tested path and interval behaved as stated. It does not prove all future events will be collected, or that the event proves why a person acted.

Rehearsal evidence should include the **negative and failure cases**, not only a successful dashboard screenshot. A copy of a search result without its source, filters and collection boundary may be impossible to reproduce. A source timestamp and an analyst's discovery time should occupy separate fields; otherwise a delayed record can seem to have happened later than it did. The plan should also say how a source error is noticed: for example, a missing expected test event, a delayed collection receipt, a schema change or an expired retention window. Chapter 2 will exercise those distinctions with synthetic records. They belong in readiness because a responder cannot reconstruct a record that was never retained.

**Scope and privacy follow the question.** The booking question does not authorize opening the separate newsletter list. The D1 card names minimal booking and session fields to request, the custodians who could provide them and the approval to seek. If a later, supported observation raises a data-exposure concern, the incident lead and privacy contact can define a new purpose and boundary. Collecting an entire identity history or patron database merely because it is technically accessible would enlarge the case and the number of people exposed to those records. A good evidence plan makes the smallest useful selection reproducible and records what it excluded. The exact retention, access and privacy rules of a real organization must come from its own policy and applicable obligations; this fictional card does not supply them.

After reading the dataset in section 1.7, apply the contract to the **actual Chapter 1 snapshot** without importing D1 as evidence. R1 reports a `desk-a` sign-in, but no device, session-key semantics or person. R3 and R4 record booking edits, but the supplied table does not contain an owner-approved target or a fresh authoritative state comparison. R5 records a patron's report, not a count of all affected users. R6 schedules training, but does not list the approved booking tasks. R7 reports a completed backup job, not an isolated restore. R8 explicitly lacks destination detail, so it cannot establish absence of data transfer. At 09:05 the analyst can open a bounded case, preserve the supplied pointers and ask the named owners for the missing discriminators. The analyst cannot claim that the proposed D1 logging fields or rehearsals were already implemented.

An evidence-readiness contract is useful only if someone owns its **maintenance**. A service change may rename a booking field, split a write path, move a log producer or shorten retention. The owner would then re-run the authorized test and update the contract's source, meaning and collection route. The document should show its last tested scope and next review trigger; an old “green” status without those details is weaker than a current, explicit unknown. This connects Chapter 1's service map to Chapter 2's evidence handling, Chapter 3's control and recovery checks and Chapter 4's after-action improvements. It remains a preparation artifact, not a substitute for case evidence or a completed investigation.

#### Test whether readiness is usable

A response team may possess a policy, a contact list, monitoring software and nightly backups while still being unable to make a safe decision under pressure. The existence of a component says little about whether the team can use it correctly when a particular service is threatened.

A practical readiness claim should have five parts: **capability**, **owner**, **permission**, **test**, and **failure response**. For example, "we have booking logs" is an inventory statement. A verifiable readiness statement is: "the application custodian can, with the incident lead's approval, retrieve booking changes for a specified identifier and time interval; another reviewer can check the source, filters and output; if the expected test row is absent, the custodian investigates collection and retention rather than claiming no activity occurred."

This distinction matters because apparent technical success can hide failed business outcomes. A green web-health indicator may represent a responsive landing page while a reservation write fails. A successful backup-job status does not demonstrate that a restored database contains the correct schedule. A sign-in record establishes that the producing system reported an account event; it does not establish a human identity.

[NIST Cybersecurity Framework 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) describes cybersecurity outcomes across Govern, Identify, Protect, Detect, Respond and Recover. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident-response recommendations with organizational risk management. Neither source authenticates Harbor Library's fictional observations or specifies this exercise's cards. The teaching implication is to examine whether the organization's desired outcomes can actually be demonstrated.

Consider the following contrasting rehearsal results:

| Claimed readiness | Weak evidence | Stronger, still bounded demonstration |
|---|---|---|
| An owner can authorize disruption | An owner name appears in a document | An authorized role accepts or rejects a precisely scoped fictional request with reason and review time |
| Booking changes can be reconstructed | A dashboard exists | A custodian returns a predeclared synthetic edit, source identifier, original time and exact selection; an out-of-range control is excluded |
| Backups support recovery | R7 reports job completion | A separate, authorized isolated restore is compared with an owner-approved booking state; **not performed in Round A** |
| An incident can be handed off | A ticket says "investigating" | A second reviewer independently identifies observations, unknowns, scope, proposed decisions and owners |

Readiness tests should expose their own limitations. Passing one retrieval rehearsal validates the tested path and interval, not every collector, account or future day. A signed approval for one mock change does not establish authority to make any other change.

### 1.3 Roles and decision authority

A small organization may assign several roles to one person, but the decisions remain distinct:

| Role | Main responsibility in this course | Decision that needs an owner |
|---|---|---|
| Service owner | Explains service harm and acceptable interruption | Whether a disruption is tolerable |
| Incident lead | Maintains priorities, scope and decision record | Whether to escalate the response |
| Analyst | Checks signals, gathers authorized evidence and states uncertainty | Which hypothesis the evidence supports |
| Recovery lead | Tests restoration options and dependencies | Whether a proposed recovery step is technically ready |
| Communications or privacy contact | Coordinates accurate notices and data-handling review | What can be said, to whom, and when |

The analyst should not shut down a service merely because a dashboard looks unusual. The service owner may not decide that logs are irrelevant because the service appears available. The incident lead brings the owners and evidence together, records the decision and revisits it as facts change.

A useful **decision record** contains a timestamp, the current situation, available options, the chosen action, the person who approved it, the evidence supporting it, expected effects and a review time. Record rejected options as well when they explain an important tradeoff. A terse record made during the incident is more reliable than a reconstructed story written weeks later.

#### Separate recommendation, approval, execution and verification

One person can perform more than one role in a small team, but four verbs should remain visible in the case record. The **analyst recommends** an action and cites observations. An accountable person **approves** its scope and tradeoff. An operator **executes** the bounded change. A reviewer **verifies** whether the change achieved its objective and records any harm. None of these verbs can be inferred safely from a job title alone. [NIST SP 800-61 Rev. 3, sections 2.2–2.3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) discusses distributed response roles and the need for documented authorities and procedures; the four-verb record below is CyberABC's teaching device for making those authorities observable.

| Fictional proposal | Recommends | Approves under the exercise rules | Executes | Verifies |
|---|---|---|---|---|
| Keep an authorized copy of booking records | Analyst | Incident lead | Analyst | Incident lead checks scope and record pointers |
| Temporarily restrict `desk-a` | Analyst with identity administrator | Incident lead and service owner for service impact | Identity administrator | Analyst checks access result; service owner checks front-desk work |
| Pause room booking writes | Service owner and response lead | Service owner under the simulated emergency rule | Application operator | Service owner checks bookings and queued requests |

These assignments are **fictional exercise rules**. They are not a claim about any real organization's legal authority or an instruction to disconnect a production system. A useful approval says more than “go ahead”: it names the target, action, duration, expected disruption, evidence to preserve, rollback trigger and next review. If an urgent action is needed but the designated approver cannot be reached, the response lead follows the organization's approved escalation policy; the learner must not invent authority from silence.

Consider a recommendation to restrict `desk-a` after R1–R5. The analyst can state a plausible benefit: additional unauthorized edits might stop. The analyst must also state a plausible cost: front-desk staff might lose access during a busy period. Neither benefit nor cost is yet measured. A decision record that says “account compromised; disable immediately” hides both uncertainty and authority. A better provisional record is: “At 09:05 UTC, preserve the supplied records and seek the training owner's confirmation by 09:15; if an unexplained new booking edit appears, reconvene the incident lead, service owner and identity administrator for an approved restriction.” The time and threshold here belong to this synthetic case, not to a universal response policy.

### 1.4 Scope, authorization and safety

This book's labs use synthetic records only. In real work, incident authority comes from organizational policy, a contract, employment duties or explicit written approval. The authorization should identify the systems, accounts, data, time window and actions allowed. Investigating a partner's system, collecting personal data, changing access rights or taking a production service offline may require additional approval.

Use the smallest action that answers the immediate question. Reading a prepared copy of a log is different from altering the live source. Exporting a dataset may widen the number of people with access. A screenshot can omit the timestamp or the query that produced it. When evidence could later matter for legal or disciplinary decisions, follow the organization's evidence-handling procedure and obtain specialist guidance. This introductory course teaches a record discipline; it does not certify a forensic process.

For the Harbor Library exercise, the permitted scope is a fictional table of eight records in this chapter. Learners may annotate, sort and reason about the table. They may not attempt to contact a real library, probe a real domain or test a real account.

#### Write scope as an executable boundary

“Investigate the alert” is too vague to guide safe practice. A useful classroom scope has an **object** (R1–R8), an **allowed operation** (read, annotate and compare), an **excluded operation** (connect to any real service or account), a **time boundary** (the session), an **owner** (the course facilitator or learner for the local copy), and a **stop condition** (the supplied records do not answer the question). A real response plan must also specify the organization and system authority, data handling and escalation route. The classroom scope is deliberately narrower.

Suppose a learner wants more device details than R8 contains. The authorized action is to write a request such as “Identity administrator: if approved, provide the sign-in device and source details for `desk-a` from 08:30 to 09:15 UTC; record the original timezone and collection method.” It is **not** to retrieve them from a real service. A request identifies a missing observation, its custodian, the smallest useful interval and the permission needed. The analyst can continue with the supplied dataset while that hypothetical request remains unanswered.

Scope also affects the strength of a conclusion. If only R1–R8 are in scope, the sentence “No exfiltration occurred” is unsupported. R8 explicitly lacks destination detail, and the learner has no additional network records. A defensible sentence is “The supplied network summary does not permit a conclusion about data transfer.” This is not evasive writing: it tells the next reviewer exactly which kind of evidence is missing.

### 1.5 The first incident record

Open one record before investigating deeply. A practical minimum is:

| Field | Example for the fictional case |
|---|---|
| Case ID | `HL-IR-001` |
| Opened at | `2026-10-11 09:00 UTC` |
| Reporter and channel | Help-desk ticket `T-104` |
| Service and owner | Room booking; service owner pending confirmation |
| Observation | Two booking edits followed a staff-account sign-in outside ordinary hours |
| Assessment | Suspicious; compromise **not confirmed** |
| Scope and authority | Synthetic training data only |
| Evidence pointers | Records `R1`–`R8` below |
| Next question | Were the edits authorized by the staff member? |
| Next review | `2026-10-11 09:15 UTC` |

Use **UTC consistently** in this exercise. If a source uses another timezone, retain its original timestamp and record the conversion, including the offset. Never silently reorder events whose clocks may differ. Give each evidence item an identifier so that a later statement can cite its basis.

### 1.6 Worked example: the unusual sign-in

The synthetic records in section 1.7 provide the single source of case facts for this example. R1 records a `desk-a` sign-in at 08:40 UTC, R3 a change to B17 at 08:43, R4 a cancellation of B18 at 08:44, and R5 a patron report at 08:48. The team can say that the sign-in preceded both edits and the report. It **cannot yet say** that the account was stolen, that either edit caused every aspect of the report, or that data was exfiltrated. A safe next step is to preserve the relevant record identifiers, ask the service owner whether the edits match scheduled work, and request staff-account context through an authorized channel. Depending on organizational procedure and new evidence, the incident lead may then authorize additional collection or containment.

The alternative “disable the account immediately” has a possible benefit if the account is compromised, but it may stop front-desk work and obscure whether the staff member is actively making legitimate changes. The correct decision depends on impact, confidence, authority and available alternatives. Record that reasoning rather than presenting a guess as a universal rule.

### 1.7 A contained practice dataset

Use only these synthetic records for the exercises. They extend the worked example; they are not evidence of a real event.

| ID | UTC time | Source | Observation |
|---|---|---|---|
| R1 | 08:40 | Identity log | `desk-a` signed in successfully |
| R2 | 08:42 | Application log | `desk-a` opened the booking dashboard |
| R3 | 08:43 | Application log | Booking `B17` changed from Room 2 to Room 4 |
| R4 | 08:44 | Application log | Booking `B18` was cancelled |
| R5 | 08:48 | Help desk | Patron reported that `B18` disappeared |
| R6 | 08:50 | Staff calendar | Front-desk training was scheduled for 08:30–09:00 |
| R7 | 08:52 | Backup monitor | Previous night's backup completed successfully |
| R8 | 08:55 | Network summary | No relevant network conclusion; summary lacks destination detail |

R6 is a reason to check whether the edits were part of training; it is not proof that they were. R7 may support recovery planning but does not prove that a restore works. R8 cannot prove absence of data transfer. The lesson is to connect a claim to the evidence that actually supports it.

#### A three-hypothesis reading of the same records

Start with three explanations that are meaningfully different. **H1: authorized training** caused the booking changes. R6 makes this plausible because training was scheduled; R6 does not identify which bookings were meant to change. **H2: someone used `desk-a` without authorization.** R1–R4 are compatible with this, but they contain no proof about who controlled the session. **H3: the patron view and authoritative booking state differ.** R5 suggests a user-visible discrepancy, but R4 records a cancellation in the application audit, so H3 cannot by itself explain every observation. All three are hypotheses, and more than one contributing condition could be present.

The next check should be chosen for its ability to **discriminate** among these explanations at low cost and within scope. Asking the training owner whether B17 and B18 were specified in the training plan may strengthen or weaken H1. Comparing the authoritative booking state with the patron view may test H3. Reviewing a narrowly scoped, approved identity detail record could strengthen or weaken H2. The fact that a check is useful does not itself authorize collecting that record. If permission or data is unavailable, record the limit and revisit the decision with the case owner.

| Claim under review | Supplied support | Missing discriminator | Safe next step in this exercise |
|---|---|---|---|
| The B18 change was planned training | R6 shows training was scheduled; R4 shows the cancellation | The approved training task list | Draft a request to the training owner |
| `desk-a` was misused | R1–R4 establish a session and edits | Authorized user's account of activity and approved identity details | Record the question and the responsible custodian |
| The service can be restored | R7 shows a backup job completed | A tested restore and comparison with an authoritative schedule | Ask the recovery lead for a contained restore-test plan |

This is an example of **evidence discipline**, not a probabilistic verdict. With this small dataset, no defensible numerical probability of compromise can be calculated. A score invented from intuition would add apparent precision without adding evidence.

#### Let the service outcome set the evidence question

An alert title tells a responder what a detector noticed. It does not tell the responder which business result is at risk. For Harbor Library, the meaningful outcome is that residents can see and reserve the intended study rooms and that authorized staff can manage bookings without silently corrupting the schedule.

The existing service map lists a booking application, staff identity service, reservation database, nightly backup and help desk. Each has a different evidentiary purpose. An identity record can help investigate an account's authentication context; an application audit describes a reported operation; an authoritative booking-state check tests what is currently stored; a help-desk ticket records a reported user experience; a backup monitor describes a job. None should be substituted for another merely because its timestamp is convenient.

A beginner should write a **decision-purpose sentence** before requesting evidence:

> "I need to determine whether B17 and B18 were authorized training changes before recommending an access restriction that could interrupt front-desk work."

That sentence fixes the relevant object, suspected harm, alternative explanation and pending decision. It also prevents an unjustified expansion to the unrelated newsletter contact list or all patron accounts.

A useful evidence question has two outcomes, not one. Ask: "What would I conclude if the requested record confirms the hypothesis, and what would I conclude if it contradicts the hypothesis?" If neither result would change the decision, the request may not be the best first use of limited time. This is a decision-value test, not a mathematical score.

For instance, the scheduled training in R6 makes an approved-operation explanation plausible, but R6 does not list B17 or B18 as approved tasks. A bounded request for the dated task list could strengthen or weaken that explanation. A broad network search, by contrast, cannot substitute for the missing task authorization merely because it might produce more data.

#### Keep a claim ledger with falsifiers

A record has a **producer**, a **reported event**, a **timestamp**, and a **scope**. The analyst adds an interpretation. Keeping those elements separate prevents a common logical shortcut: replacing "this source reports X" with "X happened exactly as I imagine it."

Use a claim ledger with five columns:

| Claim | Direct pointer | Type | Limitation | What could change the conclusion? |
|---|---|---|---|---|
| `desk-a` signed in | R1, 08:40, identity log | Record-content observation | No human attribution or device proof | Narrow authorized identity context and validated correlation |
| B18 was cancelled | R4, 08:44, application log | Record-content observation | No approval or present-state confirmation | Approved task list and bounded current-state comparison |
| Training explains the changes | R6 plus R3–R4 | Hypothesis | Calendar entry is not task authorization | Dated complete training task list |
| Service can be restored quickly | R7 | Unsupported finding | Job completion gives neither restore duration nor correctness | Isolated restore test under owner-defined acceptance criteria |
| No data was transferred | R8 | Unsupported finding | Destination detail is absent | Approved, fit-for-purpose network evidence and coverage check |

The "direct pointer" column does not turn a synthetic row into authenticated production evidence. It identifies the exact source *within the exercise* from which a statement was drawn.

A credible conclusion also needs a **falsifier**: an observation that would force the writer to change the current explanation. If the only acceptable evidence is evidence that confirms the favored theory, the analyst is not performing a meaningful test. An approved training plan excluding B18 would weaken the proposed training explanation; a plan including B18 would strengthen it for that edit but still would not establish who operated the session.

When the evidence is incomplete, "unknown" is an informative state. It identifies an unfinished dependency between question and proof. It must not be changed to "false" merely because a field or record is missing. R8 illustrates this directly: the absence of destination detail is not evidence that there was no transfer.

#### Keep the 09:05 information boundary explicit

Incident records use more than one time concept. An event timestamp describes what a producer reported. A case-open time describes when the response record began. A decision time describes when particular information and authority were used. Later discovery is not retroactive access to evidence.

In this exercise the source events R1–R8 have timestamps between 08:40 and 08:55 UTC, the case opens at 09:00, and the first decision checkpoint is 09:05. A good decision note states its **available evidence set** as explicitly as its timestamp:

`case=HL-IR-001; checkpoint=09:05 UTC; available=R1–R8; later sources=not released`

A peer reviewer can now ask whether every claimed fact was available to the decision maker. A later record with an earlier event time must remain excluded from this 09:05 reasoning. Otherwise the review suffers from hindsight bias: judging an earlier action as if the responder already knew facts received later.

Keep hypothetical injects in separate cards. If a trainer says "imagine another edit happens at 09:08," the learner may explain how the decision *would* change, but must not silently append the imagined event to R1–R8. Restoring the baseline after the counterfactual is part of the exercise.

### 1.8 Guided readiness workshop: prepare the first decision

This paper-and-pencil lab turns the eight fictional records into a reproducible case artifact. It requires no software, network connection, account, secret or real person. Work from the table in section 1.7 and the role and scope rules above. The outputs are a service card, an evidence ledger and a decision card. Keep the three artifacts together under the synthetic case ID `HL-IR-001`.

**Step 1 — Define the service and authority.** On the service card, name the room-booking outcome, the identity and database dependencies, the service owner to consult and the person who can approve record collection under the exercise rules. Mark the identity administrator as a potential custodian of additional sign-in details, not as a source already consulted. Record “synthetic R1–R8 only” as the current evidence boundary.

**Step 2 — Build the evidence ledger.** Copy the record IDs and UTC times for R1, R3, R4, R5, R6, R7 and R8. Add one column labelled “what this item directly records” and another labelled “what it does not prove.” For example, R7 directly reports a completed backup job; it does not establish the restored schedule or its recovery time. Do not merge the patron's report with the application audit into a single unqualified fact.

**Step 3 — Set a decision checkpoint.** At the fictional 09:05 UTC checkpoint, propose either (A) preserve the supplied records and verify the training explanation before changing access, or (B) request an approved temporary restriction of `desk-a`. For the chosen option, write its expected benefit, service cost, approving role, observable result and next review time. Also record the rejected option and the evidence that would cause reconsideration. Either choice can be defended if assumptions, urgency and authority are stated; R1–R8 alone do not force a universal answer.

**Step 4 — Run a counterfactual.** Imagine that at 09:08 UTC a newly supplied, verified application record shows another booking edited after the scheduled training window. This is a **fictional inject**, not part of R1–R8. State how it would change your assessment and which approval you would seek. Then remove the inject and return to the actual eight-record dataset. This separation prevents a hypothetical event from silently becoming case evidence.

**Expected evidence:** three labeled artifacts with the case ID, source IDs beside every factual statement, an explicit unconfirmed-cause status, a named approver for any disruptive action, and a next review time. A reviewer should be able to reconstruct the order of events and identify which statements were observations, inferences or proposals without asking the author.

**Assessment rubric:** award one point each for accurate event pointers and UTC ordering, clear separation of fact from hypothesis, explicit current authority and scope, a proportionate option comparison, and a review trigger with owner. A score of 5/5 shows the artifact is internally complete for this introductory exercise; it does **not** certify incident-response competence or prove the fictional case's cause. An omitted scope or approval item must be corrected even if the other four points are present. A worked example appears in the final answer section after EX013.

### 1.9 Build a decision gate from incomplete evidence

An initial response is a series of **bounded decisions**, not a search for certainty before anyone acts. At the 09:05 UTC checkpoint, the Harbor Library analyst has eight supplied records, a scheduled training interval and two booking changes. The records do not say who controlled `desk-a`, whether B17 and B18 were authorized training tasks, or whether a backup could actually restore a correct schedule. These unknowns call for discriminating questions, not invented answers. The decision gate below is an original teaching model for this fictional case. It illustrates the documented roles, authority and review practices discussed in [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final); it is not a NIST-prescribed severity scale.

| Gate field | Entry supported at 09:05 UTC | What would change it |
|---|---|---|
| Observed service effect | R3 records B17 moved; R4 records B18 cancelled; R5 records a patron report about B18. The full patron impact is unknown. | An owner-approved comparison of booking IDs, intended schedule and current state. |
| Competing explanations | R6 makes training plausible; R1–R4 are also compatible with use of `desk-a` outside its intended purpose. | Approved training task list and appropriately authorized identity context. |
| Possible cost of waiting | Another incorrect booking may occur if unauthorized edits continue. This is a **risk**, not an observed new edit. | A verified later audit row or report tied to the booking service. |
| Possible cost of restriction | Front-desk work may be interrupted if `desk-a` is temporarily restricted. The cost has not been measured. | Service owner's account of staffing, alternatives and affected operations. |
| Current authority | Classroom analysis of R1–R8; a disruptive restriction requires a separate approval under section 1.3. | A recorded incident-lead and service-owner decision with target, duration and rollback. |
| Review condition | Reassess at 09:15 UTC or sooner on a verified unexplained edit. | Record the new item and its time of discovery before changing the decision. |

One defensible choice is to preserve the supplied records, ask the training owner about B17/B18 and reconvene at the review time. This avoids an immediate service interruption but accepts the possibility of a further edit. Another defensible choice, if the service owner describes a high impact of continued changes and the approving roles are available, is to seek a temporary account restriction with a defined end and a way for staff to continue essential work. **The analyst's recommendation is not permission to execute either change.** A reviewer should ask what fact would reverse the choice, who can authorize the reversal, and how quickly the resulting harm can be observed.

If the training owner confirms that B17 and B18 were on an approved task list, that weakens the hypothesis that *those two* edits were unauthorized. It does not prove the person controlling the session, nor does it settle any later B19 edit introduced in Chapter 2. If the task list excludes B18 and the owner confirms the list is complete, the training explanation for B18 weakens. If the list is unavailable, the answer is **unknown**, not “training was ruled out.” This distinction between a contradictory observation and a missing observation is fundamental to responsible incident decisions.

To make the gate reproducible, a second analyst should be able to read the same R1–R8 table, recover the same event order, locate the supporting record for each claim and see the approval path. If the second analyst cannot tell whether a sentence is a supplied fact, a hypothesis or a proposed action, rewrite it. Chapter 2 adds evidence preservation and discovery-time discipline to this same case; the later records must not be imported backward into the 09:05 decision.

#### Make the first decision a reproducible handoff

A handoff should allow a second learner to answer six questions without asking the original analyst for undocumented context:

- What service and decision are in scope?
- Which exact record identifiers support the current observations?
- Which hypotheses remain live, and what could disconfirm them?
- What has merely been proposed versus approved or executed?
- Who owns the next question or action?
- What deadline or observed trigger requires renewed review?

Compare two examples.

**Insufficient:** "Suspicious admin activity. Likely breach. Investigating."

**Reviewable:** "At the fictional 09:05 UTC checkpoint of HL-IR-001, R1 shows a `desk-a` sign-in, R3 and R4 report booking edits, and R5 reports a patron complaint. R6 documents scheduled training but not the authorized task list. The analyst has not identified a human actor or established compromise. The incident lead is asked to approve a bounded training-owner check and to review the service impact with the owner by 09:15 UTC; no real access restriction was performed."

The longer message is not better simply because it has more words. Each clause answers a question essential to the next decision. A handoff that confuses a proposed request with a completed collection can be more dangerous than a brief handoff that clearly marks the missing evidence.

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) addresses incident response as an organizational capability involving multiple roles and activities. The six-question handoff above is original CyberABC instructional material, not a mandated NIST form.

<a id="ir-rapid-ch01-claim-lab"></a>

### 1.10 Offline laboratory: evidence-bound claim review

**Goal:** Classify claims against the exact Round A release and demonstrate how a missing source changes a supported teaching statement without changing the canonical incident.

**Inputs:** The eight fictional record identifiers, their existing timestamps and source types, plus six classroom claim cards. No new incident observations are introduced.

**Environment:** Python 3, standard library only. The fixture is in memory, requires no accounts, reads no files, and makes no network requests.

**Before running:** Predict which claims may accurately report the supplied *record contents*, which remain hypotheses, which exceed the source semantics, and which reference an unreleased record. In particular, do not treat "record content available" as "real event authenticated."

~~~python
events = [
    ("R1", "08:40", "identity", "desk-a sign-in"),
    ("R2", "08:42", "application", "dashboard opened"),
    ("R3", "08:43", "application", "B17 moved"),
    ("R4", "08:44", "application", "B18 cancelled"),
    ("R5", "08:48", "helpdesk", "patron report"),
    ("R6", "08:50", "staff_calendar", "training scheduled"),
    ("R7", "08:52", "backup_monitor", "job completed"),
    ("R8", "08:55", "network_summary", "destination detail absent"),
]

assert len(events) == len({row[0] for row in events})
assert [row[1] for row in events] == sorted(row[1] for row in events)

available = {row[0] for row in events}

# Each card is an analytical claim, not another R-series event.
claims = [
    ("C01", {"R1"}, "record"),
    ("C02", {"R3", "R4", "R6"}, "hypothesis"),
    ("C03", {"R1", "R3"}, "actor"),
    ("C04", {"R7"}, "restore"),
    ("C05", {"R8"}, "no_transfer"),
    ("C06", {"R9"}, "record"),
]

def classify(refs, kind, released):
    if not refs <= released:
        return "NOT_IN_RELEASE"
    if kind == "record":
        return "RECORD_CONTENT_ONLY"
    if kind == "hypothesis":
        return "HYPOTHESIS_ONLY"
    return "NOT_ESTABLISHED"

for name, refs, kind in claims:
    print(name, classify(refs, kind, available))

# Negative test: make a temporary incomplete copy of Round A.
# This is not a deletion of canonical R6.
without_r6 = available - {"R6"}
print(
    "NEGATIVE_R6_MISSING",
    classify(claims[1][1], claims[1][2], without_r6),
)
print("EVENTS_IN_ROUND_A", len(events))
~~~

#### Exact expected output

~~~text
C01 RECORD_CONTENT_ONLY
C02 HYPOTHESIS_ONLY
C03 NOT_ESTABLISHED
C04 NOT_ESTABLISHED
C05 NOT_ESTABLISHED
C06 NOT_IN_RELEASE
NEGATIVE_R6_MISSING NOT_IN_RELEASE
EVENTS_IN_ROUND_A 8
~~~

#### Worked interpretation

**C01:** R1 is available. The learner may report that the *synthetic identity record* states a successful `desk-a` sign-in. The output is not an independent authentication of the record or a human attribution.

**C02:** R3, R4 and R6 are all available. The training explanation can be formulated as a hypothesis, but the calendar entry does not authorize the specific edits. The code does not evaluate whether the hypothesis is true.

**C03:** Account and application records exist, but the actor's identity is not established. No field in the supplied release identifies the human operating the session.

**C04:** The reported backup-job completion cannot be converted into a proven restore result. No restore was executed in this fixture.

**C05:** R8 omits destination detail. A claim that no transfer occurred would exceed the source.

**C06:** The claim references R9, outside the Round A release. The code intentionally supplies no content for R9; the future record must not influence the 09:05 assessment.

**Negative test:** Removing R6 from a temporary set makes the training-hypothesis card lack one of its referenced sources. The result changes to `NOT_IN_RELEASE` *for the temporary variant*. No historical event or canonical R6 record has changed.

#### Validation, failure modes and limits

The first two assertions detect duplicate identifiers or unsorted printed timestamps in this literal fixture. They do not verify synchronization of independent real systems. The algorithm deliberately checks source *availability* and a simplified claim class; it does not perform semantic parsing of incident narratives, cryptographic integrity checks, authorization checks or independent source verification.

A learner who obtains the expected output has reproduced the stated classroom logic, not proven that Harbor Library experienced an incident. A learner who edits the Python input must preserve the original transcript and label the changed run as a variant.

**Required artifact:** Submit (a) the exact transcript, (b) a six-row claim ledger with evidence ID, supported wording and limitation, and (c) a two-sentence difference report for the negative test. Pass only when all original Round A facts remain unchanged, unsupported findings stay blocked and the hypothetical source removal is not represented as real evidence loss.

### 1.11 Common errors and chapter synthesis

- **Confusing suspicion with confirmation.** Use a hypothesis and state what would confirm or weaken it.
- **Skipping the service owner.** A technically plausible action can cause avoidable harm to users.
- **Losing the timeline.** Record source timestamps, timezone and collection time.
- **Expanding scope silently.** Ask before collecting or changing systems outside authority.
- **Treating a backup status as a restoration test.** A successful backup run is one fact, not a recovery guarantee.
- **Treating an absence in incomplete logs as evidence of absence.** State the collection limit.

Readiness is the ability to answer, under pressure, who owns the service, who can approve a decision, where trustworthy evidence can be found, and how a decision will be reviewed. This chapter prepares the alert-triage and evidence-preservation work in Chapter 2.

### Chapter 1 exercises

Work from **only R1–R8** and the fictional authority rules in Chapter 1. The case is synthetic. At the 09:00 intake and 09:05 decision checkpoints, do not cite records or interviews released in later chapters, claim a production collection took place, or infer a person's identity from an account label. Write any imagined future signal as **hypothetical**. For each answer: (1) write `HL-IR-001` and the exercise ID; (2) copy the relevant record IDs and UTC times; (3) fill the named output fields; (4) mark each conclusion as observed, inferred, unknown or proposed; (5) name an owner and approval for any new collection or service change; and (6) compare the result with the worked answer at the end of the book. The submitted table, note or decision card is the expected evidence of learning; a label without its supporting record is insufficient.

**Common assessment rubric:** score an exercise **0** if its artifact is missing or presents an unsupported attribution or action as fact; **1** if it answers the question but omits a required source, limit, authority or test; **2** if all named fields are present, the reasoning follows the supplied evidence and the next step is bounded and authorized. The local requirements below specify what earns 2 points. A claimed compromise, successful restore or absence of data transfer based only on R1–R8 must be corrected regardless of the numerical score. No real website, account or patron data is needed.

#### EX001 — Observation or inference

**Objective:** separate the content of a record from an explanation of that content. **Inputs:** R4, R5 and R7. **Output:** a four-row table with statement, classification, supporting record and one sentence describing the record's limit. Classify: (a) “R4 records a cancellation of B18”; (b) “`desk-a` was compromised”; (c) “R5 reports that B18 disappeared”; (d) “R7 proves the service can be restored in ten minutes.” Use the categories direct observation, hypothesis requiring confirmation and unsupported conclusion. A score of 2 requires distinguishing the *fact of a patron report* from independent proof of the patron's full experience.

**Extension:** For each original statement, rewrite any unsupported conclusion into the narrowest defensible wording. Add one source that would be needed to upgrade the claim.

**For full credit:** A 2-point answer must distinguish "R5 records a patron report" from "the booking interface was independently proved incorrect," and "R7 reports backup completion" from "recovery was tested." Merely selecting a label without a limiting sentence earns at most 1.

#### EX002 — First two questions

**Objective:** choose checks that could change the restriction decision. **Inputs:** R1–R6 and the service/authority tables. **Output:** two rows with a precise question, the fact that makes it relevant, the authorized custodian or person to ask, and how either answer changes the decision. One question must test the training explanation; the other must test who used the account or whether edits continue. Record requests rather than saying the interview or log review has already occurred. A score of 2 requires different discriminators and a named approval path for any new identity collection.

#### EX003 — Service dependency

**Objective:** connect an incident signal to service outcomes and evidence owners. **Inputs:** the section 1.2 service map and R1–R8. **Output:** a two-row dependency card with dependency, possible user harm, supplied pointer, missing discriminating evidence and custodian. Choose two dependencies; for each, explain what an authorized check would distinguish. Do not call a potential harm a confirmed outage. A score of 2 needs two different dependencies and a test that could separate a service-state problem from account misuse.

**Extension:** For each of the two chosen service dependencies, distinguish a *possible downstream business harm* from an actual observation. Name one negative test that could weaken the proposed explanation and identify who would be authorized to request it.

**For full credit:** A 2-point answer explicitly connects different technical sources to different decisions. The database's current booking values cannot be inferred directly from R3–R4's edit history.

#### EX004 — Scope boundary

**Objective:** apply an authorization boundary to a tempting next action. **Inputs:** the section 1.4 scope statement and R1–R8. **Output:** a short scope decision with proposed action, permitted objects and operations, reason for rejection, contained alternative, and stop or escalation condition. A learner wants to search a real public library website for a matching account name. Explain what the eight supplied records permit instead, and write a hypothetical request for the additional detail if it would matter to the case. A score of 2 explicitly excludes real-site access and names the responsible approver for any future expanded scope.

#### EX005 — Timeline

**Objective:** preserve event order without turning sequence into causation. **Inputs:** R1, R3, R4 and R5. **Output:** a four-row UTC table with record ID, source, time and observed event, followed by an ordering sentence and a separate unsupported-causality sentence. Keep the 09:00 case-open time outside the event table. A score of 2 orders the four events correctly and explains why precedence alone does not identify the human actor or prove why the patron's view changed.

**Extension:** Add a separate checkpoint note `case opened 09:00; decision 09:05; available R1–R8`. Explain why the case-open and decision times must not be inserted into the four-row source-event chronology as if they were source events.

**For full credit:** A 2-point answer preserves chronology while rejecting human attribution and unsupported causality.

#### EX006 — Role assignment

**Objective:** make recommendation, approval, execution and verification visible. **Inputs:** section 1.3's fictional roles, R7 and the classroom scope. **Output:** a four-row responsibility table for a possible booking outage, preservation of R1–R5, coordination of the next review and a contained restore test. Name the task owner, who approves it under the exercise rules and what would verify completion. Distinguish **planning** a restore test from having performed one. A score of 2 does not delegate an outage decision to the analyst or treat R7 as a tested restore.

#### EX007 — Minimal incident record

**Objective:** open a case that another analyst can continue. **Inputs:** R1–R8 and the 09:00 intake checkpoint. **Output:** exactly seven labeled fields: case ID and open time; service; reporter and source; observed signal with record IDs; current assessment and uncertainty; permitted scope and authority; next question, owner and review time. Related details may share a field. A score of 2 retains the `T-104` help-desk context from section 1.5, distinguishes the report from an independently checked booking state, and does not claim the later 09:05 decision was already executed at 09:00.

#### EX008 — Evidence quality

**Objective:** limit claims to what three different source types actually say. **Inputs:** R6–R8. **Output:** a three-row evidence-limit table with ID and time, narrow supported conclusion, tempting unsupported conclusion, and a follow-up source or test. A score of 2 treats a scheduled activity as distinct from an approved booking change, a completed backup job as distinct from a proven restore, and a summary missing destination detail as distinct from a verified absence of transfer.

#### EX009 — Decision alternatives

**Objective:** justify a proportionate 09:05 decision under uncertainty. **Inputs:** R1–R8 and the section 1.9 gate. **Output:** a two-row option matrix for (A) seeking a temporary restriction of `desk-a` and (B) preserving R1–R8, asking the training owner and reviewing before restriction. Record expected benefit, possible service or delay cost, approver, observable success or failure and a 09:15 review trigger for each. Choose one provisionally and explain what new evidence would reverse it. A score of 2 identifies a separate approval for restriction and does not describe either risk as an already observed event.

**Extension:** Add a falsifier and a business negative check to both original options. State which observation would make the learner reconsider a decision to wait and which observation would indicate an account restriction disrupted legitimate work.

**For full credit:** A 2-point answer requires distinct approval, execution and verification states, not merely a preferred option.

#### EX010 — Communication draft

**Objective:** communicate useful action without premature attribution. **Inputs:** R1–R8 and the 09:00 intake state, *before* the 09:05 decision. **Output:** exactly two sentences for an internal service-owner audience: the first states observed service signals and uncertainty; the second names a **proposed** next check, its owner and the expected 09:05 decision checkpoint. Do not say preservation, an interview or a restriction has already been approved or performed. A score of 2 gives a source pointer and an unambiguous distinction between planned and completed work.

#### EX011 — Escalation trigger

**Objective:** specify when the initial choice must be reopened. **Inputs:** the R1–R8 snapshot and section 1.9. **Output:** two **hypothetical** observation/response rows with source that would verify the signal, harm or uncertainty affected, decision owner and next action. One trigger should concern continued booking change; the other should concern breadth or service impact. A score of 2 states that neither observation is present at 09:05 and avoids an automatic production action without approval.

#### EX012 — Practice record

**Objective:** make a bounded decision auditable. **Inputs:** R1–R8, the fictional 09:05 checkpoint and section 1.3's authority matrix. **Output:** one decision log with time, action, reason with source IDs, approving role, executing role, evidence-copy scope, rejected alternative, next review time and reversal trigger. The scenario grants classroom permission for the bounded copy; do not describe a production export. A score of 2 states the question to the service owner as **pending** until answered and preserves uncertainty about account control.

**Extension:** Record an explicit state for each activity: `proposed`, `approved classroom analysis`, `performed classroom copy` if actually done, or `not performed`. Leave the proposed training-owner answer pending until supplied.

**For full credit:** A 2-point answer never reports a hypothetical request as a completed interview or a production evidence collection.

#### EX013 — Readiness gap

**Objective:** turn an exercise weakness into a measurable preparation change. **Inputs:** the service map, authority table, R7–R8 and the section 1.8 workshop. **Output:** a three-row gap register with missing capability, consequence and owner; then an improvement ticket with priority rationale, specific change, deadline and a pass/fail drill. A score of 2 names a test that would actually demonstrate the change, such as an owner-and-alternate decision drill or a contained restore rehearsal, rather than merely publishing a policy page.

**Extension:** The improvement ticket must include a falsifiable rehearsal with a pass and failure criterion. A fallback-authority drill can test an unavailable primary approver; alternative defensible tickets may test log retrieval or isolated recovery.

**For full credit:** Merely writing or publishing a policy does not satisfy an exercise that asks the learner to demonstrate a capability.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Alert triage and evidence preservation

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Turn a reported alert into a short triage question, without treating its label as a fact.
2. Compare a small set of hypotheses against an evidence table and state what remains unknown.
3. Set an initial priority using potential service harm, time sensitivity and confidence, then set a review time.
4. Prepare a collection note that identifies the source, collector, authority, time and integrity check for a synthetic record.
5. Explain why a matching hash helps detect change to a copy but cannot prove that the original source was truthful.
6. Produce a handoff that another analyst can reproduce from the same supplied records.
7. Normalize a supplied fixed-offset timestamp to UTC and distinguish an event's time from its discovery time and a query's coverage.
8. Explain how a delayed log arrival can change a repeated query without changing the original event time, and audit the limits of a synthetic evidence package.
9. Correlate two synthetic log sources with an explicit join key and time interval, marking ambiguous and unmatched rows without inferring a human actor.
10. Prioritize bounded preservation requests by decision value, possible loss, authority and privacy, without reporting a requested copy as collected evidence.

### 2.1 An alert is a question to investigate

Chapter 1 established owners and a bounded record. Triage now asks what the signal means, what might be affected, how soon a decision is needed and which authorized check would reduce uncertainty. A detector may produce the label “suspicious login,” but that label is neither an identity proof nor a conclusion that the account was compromised. The analyst must retain the detector's raw observation, collection time and rule context while testing alternative explanations.

For Harbor Library, the first two hypotheses are **H1: the booking edits were scheduled training** and **H2: the account was used outside the planned training**. A third possibility, **H3: the patron's report reflects a display or synchronization problem**, reminds us that the reported symptom and the booking changes might have different causes. These hypotheses are teaching devices. They are not exhaustive and should be revised when evidence appears.

| Question | Why it changes triage | First authorized check |
|---|---|---|
| Are bookings still changing? | Ongoing harm may require a faster decision. | Request a current application audit summary from the service owner. |
| Was `desk-a` expected to edit these bookings? | Authorized work can explain part of the timeline. | Ask the training owner for the exercise plan and attendee confirmation. |
| How many patrons are affected? | Scope matters for service and communication decisions. | Compare the approved booking audit with the help-desk queue. |
| Can the logs be trusted and retained? | A short retention window may make delay costly. | Record source, time range, export method and retention deadline. |

The initial action should be the smallest authorized check that could change the next decision. If a new edit is causing immediate harm, the incident lead can seek an urgent containment decision while collection continues. If the signal is stale and service impact is unknown, preserving records and checking the owner may be the more informative first step. Triage and containment can overlap; they are not a rigid sequence.

### 2.2 Prioritize harm, urgency and confidence separately

This book uses an **illustrative classroom matrix**, not a universal severity standard. Keep three judgments separate:

| Dimension | Low example | High example | What to write |
|---|---|---|---|
| Potential harm | One corrected training booking | Many lost bookings or sensitive-data exposure | Who or what may be affected, with uncertainty |
| Time sensitivity | Records retained for weeks; no ongoing changes | Further edits occurring or evidence about to expire | Next decision and its deadline |
| Confidence | One uncorroborated alert | Independent records agree on an unauthorized action | Supporting records and contradictions |

A case can be urgent even when confidence is low: continued edits could affect patrons while the cause remains uncertain. It can be well supported but low urgency after an authorized maintenance test has ended. The incident lead should record a provisional priority and **the condition for changing it**. Harbor Library's opening priority is “prompt review,” because a patron reported harm, yet the available records do not establish compromise or broad impact. This priority is a teaching judgment based on the fictional facts, not a prescribed incident category.

### 2.3 Preserve what supports the next decision

[NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides guidance on incorporating forensic techniques into incident response, including work with different data sources. Its publication page expressly frames the guidance as an IT investigation aid and calls for management and legal consultation on applicable requirements. This rapid course therefore teaches a **minimal reproducibility record**, not a certified forensic collection method or a legal chain of custody.

For each synthetic record that matters, note the source system, the exact time range and timezone, the person who exported or copied it, the permission used, the collection time, where the original remains, where the working copy is stored and how access to it is limited. Record transformations: an export may sort rows, normalize timestamps or omit fields. Preserve the unmodified export when authorized, and analyze a separate working copy. If a source is volatile or automatically deleted soon, tell the incident lead so the collection decision can be prioritized.

An integrity hash can detect whether a particular byte sequence changes between two checks. For example, a team can calculate SHA-256 over a copied file at collection and again before review. A matching value supports that the checked copy has not changed **between those checks**, assuming the method and record are trustworthy. It does not prove the source log was complete, that its clock was correct, that the exporter had permission, or that the events actually happened. A hash of a screenshot says nothing about omitted rows. Explain these limits in the case note.

| Collection-note field | Example for a synthetic classroom export |
|---|---|
| Case and item | `HL-IR-001`, item `E1` |
| Source and range | Booking audit, 08:30–09:15 UTC |
| Collector and authority | Analyst; fictional incident lead's classroom authorization |
| Collected at | 09:18 UTC |
| Method | Export the supplied exercise table as UTF-8 text; keep the original table in this book |
| Copy and access | Local training copy `E1.txt`; learner only |
| Integrity note | SHA-256 of the exact saved bytes, recorded before and after analysis if a file is created |
| Transformation and limitation | No production source; table is invented, and export formatting can change bytes |

This table is a model for an **exercise note**. A real organization needs its approved preservation, retention, privacy and evidence-transfer procedures. Never collect broader data merely to make a training exercise look realistic.

#### Prioritize a preservation request before copying

[NIST SP 800-61 Rev. 3, RS.AN-06 and RS.AN-07](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) addresses the provenance, integrity and restricted access of response records, and the collection and retention of incident data under an organization's procedures. The **preservation queue** below is CyberABC's classroom method for deciding what to request next; it is not a NIST form or a substitute for an organization's policy. The question is not “Which source contains the most data?” It is “Which authorized, minimal observation could change the next decision, and which opportunity to obtain it may be lost?”

Write a separate card for each candidate source. Name the **decision it could change**, the smallest relevant field and interval, its custodian, the known or unknown loss path, the approval needed, the expected handoff artifact and the claim that would remain unproved even after collection. This reuses Chapter 1's proposed evidence-readiness contract, but now the case has a live decision point. A source that may expire soon deserves immediate contact even if the cause is uncertain; a source with no confirmed loss clock may still need a parallel availability check. Do not convert the words “high priority” into an unverified deadline. Conversely, an indefinitely retained document is not automatically less important to the hypothesis: it may simply permit a later request after the fragile source is safeguarded.

The queue has four distinct states: **proposed** means the analyst has written a bounded request; **approved** means the named owner authorized that scope; **collected** means a custodian actually produced or preserved a specified item; **verified** means a reviewer checked the item's selection, recorded bytes or other appropriate integrity properties and limitations. An approval is not a completed collection. A digest is not a source-coverage check. A “retention hold” is itself an operational action that needs a named authority and a confirmed effect; saying one was requested does not show that deletion stopped. For every state change, record the time, actor, source pointer and what remains pending.

When two requests compete for attention, compare them without inventing a numerical risk score:

| Question | What to record | Failure of a shallow answer |
|---|---|---|
| Decision value | Which current choice could change, and what observation would discriminate? | “Useful someday” gives no reason to expose unrelated data now. |
| Loss and delay | What policy, observed failure or owner statement supports the loss concern? Is the policy anchor known? | Adding a stated retention period to an event timestamp may fabricate a deadline. |
| Authority and feasibility | Who can approve, who can retrieve, which selection is feasible, and what if the custodian cannot act? | An analyst's urgency does not grant permission or prove that a source is accessible. |
| Exposure and fidelity | Which people and fields are included, what filters or transformations are applied, and how will an unmodified authorized copy be distinguished from a working view? | A broad export increases exposure; a narrow, undocumented filter can hide relevant rows. |

The first contact may be the incident lead to obtain approval, the source custodian to establish a retention anchor, or both through an approved escalation path. Several requests can proceed **in parallel**; the queue ranks decision and loss concerns, not a fixed order of technical commands. Keep the case record and the protected evidence store separate. A case note may point to an item and its access owner without copying sensitive raw records into a widely read ticket. Record the retention rule for the *collected copy* separately from the source's own deletion rule. If an expected source is unavailable, record who confirmed that, which interval or field is missing and how the next decision must be narrowed. Do not fill the gap with an invented export.

#### Event time, discovery time and collection time are different facts

An event may occur at one time, enter a logging service later and be seen by an analyst later still. In the supplied classroom table, R9 says that an edit was recorded at 09:03 UTC. R15, at 09:14, communicates a retention rule; it does not restart the retention period for R9. Without the actual source's deletion policy, no learner can calculate an exact expiry from those two timestamps. The safe operational question is: **What is the oldest relevant record's retention deadline at its source, and how soon can an authorized custodian preserve a narrow copy?** Escalate that uncertainty instead of writing a fabricated deadline.

When merging records from different systems, retain the original timestamp and its timezone or offset. Add a normalized UTC field separately and record how it was obtained. A timestamp without an offset is ambiguous; a clock that is five minutes slow may reverse apparent order. The case table supplies UTC for teaching, but a real analyst would check source clock configuration and collection delay before claiming a precise cross-system sequence. R13's summary omits device and location detail, so the absence of those fields is a **source limitation**, not a negative finding about the session.

Preservation should also be **proportionate**. For the next Harbor Library decision, a bounded booking-audit interval and the account's relevant sign-in summary may be useful. Exporting all patrons, all departments or unrelated accounts could increase privacy risk without improving the decision. A narrow export can still omit a relevant event; record the selection rule and keep an authorized unmodified original when available. Chapter 2 teaches the logic of a collection request and a copy-integrity check. Production evidence handling belongs to the organization's approved procedures and qualified personnel.

#### Four-clock ledger and learner release

A timestamp is meaningful only when its origin is identified. At minimum distinguish:

- **Event time:** when the source claims an operation took place.
- **Ingestion time:** when a receiving store made that operation's record available.
- **Collection time:** when a specified copy or export was actually acquired.
- **Discovery time:** when the analyst received or recognized the relevant information.

A query also has a **run time**, which is distinct from its selected event-time interval. These clocks may be identical in a simple lab but differ in a real collection pipeline. Ingesting a delayed event later does not move its original event time. Collecting a record tomorrow does not mean its event occurred tomorrow.

The Round B teaching checkpoint supplies a concrete example:

| Record | Printed event/record time | Learner's earliest permitted availability in this chapter | Interpretation |
|---|---|---|---|
| R9 — B19 edit | 09:03 UTC | 09:20 UTC | The printed event is earlier; it was not available to the learner's 09:05 decision |
| R10 — training-plan record | 09:04 UTC | 09:20 UTC | Record time does not prove when the underlying plan was originally approved |
| R15 — retention notice | 09:14 UTC | 09:20 UTC | The notice becomes available at Round B; it gives no collection receipt or deletion anchor |
| R16 — service-owner note | 09:16 UTC | 09:20 UTC | The note states an owner condition, not an executed account or service change |

These are fictional source and release times, not measurements of real ingestion delays. The actual ingestion timestamps of the producing systems are **not supplied**. Calling the difference between printed event time and release time an observed "pipeline ingestion delay" would therefore invent a measurement. At most it is the exercise's **event-to-learner-release interval**.

Time discipline protects decision review: one must assess the 09:05 decision from R1–R8, not from later-released R9 merely because R9 carries a 09:03 event timestamp. In a real case, retain original timezone or UTC offset and document normalization and clock uncertainty. [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) specifies an Internet date-time representation including timezone offsets; it does not guarantee that a source clock is accurate.

### 2.4 Worked example: the second alert

The following records are also fictional and extend Chapter 1. They are the complete input for this chapter's exercises. No live system or external account is involved. **Exercise timing:** the Chapter 1 analyst made the 09:05 decision from the then-supplied R1–R8 snapshot. This chapter releases R9–R16 to the learner at the simulated 09:20 review. Several events in the new table have earlier timestamps; the time an event occurred and the time the analyst received its record are different facts.

| ID | UTC time | Source | Observation |
|---|---|---|---|
| R9 | 09:03 | Booking audit | `desk-a` changed booking `B19` from Room 1 to Room 3. |
| R10 | 09:04 | Training plan | The planned exercise mentions `B17` and `B18`; it does not mention `B19`. |
| R11 | 09:06 | Help desk | A second patron reported that the time on `B19` looked wrong. |
| R12 | 09:08 | Staff interview note | The staff member said they edited `B17` and `B18` during training but did not recall editing `B19`. |
| R13 | 09:10 | Identity summary | The account had one session in the available time range; the summary omits device and location detail. |
| R14 | 09:12 | Application audit | No further booking edits are shown after R9 within the queried range. |
| R15 | 09:14 | Retention notice | Detailed booking audit records are deleted after 24 hours unless an authorized copy is retained. |
| R16 | 09:16 | Service-owner note | The owner requests an impact check before any account change and can approve a short booking-service pause if needed. |

**Step 1: state observations.** R9 records a later edit to `B19`; R10 does not list that booking in the planned exercise; R12 records a person's recollection, not proof that no edit occurred; R14 only covers its queried range. **Step 2: compare hypotheses.** H1 explains `B17` and `B18` better than it explains `B19`. H2 gains support from the unexpected `B19` edit but is still unconfirmed because the staff member could have forgotten or the plan could be incomplete. H3 could help explain a patron display problem but does not by itself explain the application audit record. **Step 3: choose the next authorized check.** Ask the training owner whether any unlisted task involved `B19`, request a narrow impact check for affected bookings, and ask the incident lead to authorize preservation before R15's retention deadline. Set a near-term review time and revisit containment if changes resume or harm expands.

| Case decision at 09:20 UTC | Rationale | Owner | Review trigger |
|---|---|---|---|
| Preserve the supplied booking and identity records in the classroom case note; request an authorized impact check in a real response. | The `B19` edit is not yet explained and detailed audit retention is short. | Incident lead authorizes; analyst records the copy. | Training-owner answer, new booking edit or the next review at 09:35 UTC. |

This decision does **not** clear or accuse the staff member. It states what is known, what can be lost and who may authorize the next action. If the impact check found broad damage, a containment proposal would need to reach the service owner and incident lead promptly; Chapter 3 will compare those options.

#### Worked 09:20 preservation queue

The learner has received R9–R16 at the **simulated 09:20 review**. R9's printed event time is 09:03, but the learner did not have R9 for the earlier 09:05 decision. R15 reports that detailed booking-audit records are deleted after 24 hours unless an authorized copy is retained. It does **not** say whether the clock starts at event creation, ingestion, storage or another policy point; nor does it show that a copy or hold already exists. The queue below is therefore a set of **requests**, not a record of actual collection. It does not add evidence to R9–R16.

| Request and decision value | Loss/coverage question | Owner and proposed minimal scope | State at 09:20 and remaining limit |
|---|---|---|---|
| `P-A`: detailed booking audit for B17–B19, plus R14's application-audit query description; could reconstruct recorded edits and support a separate impact comparison. | R15 names 24-hour deletion, but the policy anchor, oldest available row and exact last safe time are unknown. R14's filter and ingestion coverage are also unspecified. | Incident lead seeks approval; application custodian checks a proposed 08:30–09:20 UTC event window, booking IDs and available raw fields, then records each source, filter, run time and export method. | **Proposed.** No detailed copy, confirmed deadline, complete query or approved booking state has been supplied. |
| `P-B`: identity-session detail relevant to `desk-a`; could test whether an application action shares a session key. | R13 is only a summary without device or location; its source retention and key semantics are unknown. | Incident lead asks identity administrator for availability, retention and a restricted time/field selection. Any cross-source join requires schema and clock checks. | **Proposed.** No person, device, location or actor attribution follows from R13. |
| `P-C`: approved training task list and version; could test whether B19 was actually in scope. | R10 lists B17/B18; the plan's version, approval time and completeness need confirmation. No deletion deadline is supplied. | Training owner supplies only the relevant signed or approved task list and its version history through the approved case route. | **Proposed.** R12's recollection is context, not a substitute for the plan or proof of who edited B19. |
| `P-D`: help-desk report and service comparison; could bound user-facing harm. | R11 is a report, not a measured patron count; the database and displayed view may disagree. | Service owner and help desk plan a restricted B19 comparison, separating the report from a patron-facing check and an approved state. | **Proposed.** No population-wide impact estimate or restored-service claim is supported. |

`P-A` receives prompt attention because the **fictional** retention notice identifies a plausible loss path and the detailed rows could change the next containment or impact decision. The lead should seek a custodian-confirmed policy anchor and a safe collection time immediately. R9 is labeled **booking audit** while R14 is labeled **application audit**; the request must ask whether these are the same producer or two different paths, rather than treating their summaries as one complete log. `P-B` can run in parallel because its retention is unknown, not known to be unlimited. `P-C` and `P-D` remain important to interpretation and harm; they are not discarded merely because the audit may be more volatile. The proposed `P-A` range is deliberately broader than R9's single timestamp yet bounded by the booking question. It is a *request for custodian review*, not an assertion that those filters exist, that the source contains every event, or that the lead has approved exporting patron data.

Suppose the application custodian later returns a restricted file. The analyst would record its actual collection time, the approved selection, source timezone, any transformation, byte count or applicable integrity check, storage/access owner and reviewer. The analyst would also ask for the **query manifest** behind R14's quiet summary: source, booking/account filters, half-open event interval, query run time, ingestion coverage and source-health limitations. Without that manifest, a copied R14 sentence still cannot establish that no edits occurred after R9. If the custodian instead reports that the detailed interval has already expired, the response lead records the failed request and who confirmed it, preserves the remaining source pointers within scope, and changes the claim from “we checked the detailed audit” to “the detailed audit was unavailable for this interval.” Neither branch may be silently backdated to 09:05.

A concise 09:20 handoff can therefore say: “R9 records a B19 edit at 09:03 UTC; R10 omits B19 from the listed training tasks, and R15 reports a 24-hour detailed-audit retention rule whose anchor we have not verified. At 09:20 we **propose** `P-A` to the incident lead and ask the application custodian to confirm availability, selection and the actual policy deadline; no production copy, hold or account restriction is recorded here.” This wording lets the next analyst see both the reason for urgency and the boundary of current evidence. Exercise EX018 asks the learner to make that request independently.

#### Preservation as an authorized transaction

A useful preservation request names *why* a source matters before specifying how much data should be copied. The next question is whether B19 was an approved operation and whether the booking service's current state matches what the service owner expects. This favors bounded booking-change evidence, an approved task-list version and appropriately limited identity details—not a bulk export of all patron records.

For each source request, prepare:

1. **Decision purpose:** what the evidence could change.
2. **Producer and fields:** what system is expected to know, including timestamp and identifier semantics.
3. **Selection:** the smallest defensible time and object range, including explicit exclusions.
4. **Custodian and authority:** who can retrieve the data and who can approve the operation.
5. **Retention question:** whether the source still contains the interval and when it may cease to.
6. **Receipt design:** which exact source, query, object, acquisition time and transformation would be recorded *if* collection happens.
7. **Residual uncertainty:** which causal or completeness claims would remain unproved.

The existing P-A and P-B queue illustrates this. P-A can be addressed promptly because R15 reports a deletion risk for detailed booking audits. P-B can proceed in parallel as an availability inquiry because identity-source retention is unspecified. Neither source should be treated as collected merely because the analyst assigned it priority.

The states **proposed → approved → collected → verified** are not interchangeable. A written request is proposed. An incident-lead authorization covers only its recorded scope. A collected object needs an identifiable receipt. Verification identifies what was checked, such as the exact copied bytes or selection manifest, and what was *not* checked. Privacy restrictions and access controls apply to the collected copy independently of the source's original retention policy.

[NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses forensic work across data sources from an IT incident-response perspective and expressly does not offer legal advice or an all-inclusive procedure. Harbor Library's request card is a beginner teaching method, not a chain-of-custody certification or permission to collect real personal data.

### 2.5 Contained lab: preserve and check a synthetic extract

The lab below is deliberately smaller than a forensic acquisition. It teaches which **bytes** a digest covers and which conclusions still require other evidence. Use a scratch directory on a computer you control, with Python 3 and no network connection. The generated text is invented for this book; it contains no real account, endpoint or patron data. Running the script writes two small files in the current directory, so choose a temporary directory first.

The extract has two rows that **transcribe** R9 and R14. It is a learning fixture assembled from this chapter's table, not an original log from Harbor Library. R14 summarizes the queried audit range; it does not assert that no later edit occurred outside that range. Save and run the following as `fixture.py` inside the scratch directory:

```python
from hashlib import sha256
from pathlib import Path

payload = (
    b"case_id|record_id|time_utc|source|observation\n"
    b"HL-IR-001|R9|2026-10-11T09:03:00Z|booking-audit|desk-a changed B19 from Room 1 to Room 3\n"
    b"HL-IR-001|R14|2026-10-11T09:12:00Z|application-audit|no further edits in the queried range after R9\n"
)
Path("E1.txt").write_bytes(payload)
saved = Path("E1.txt").read_bytes()
print(len(saved), sha256(saved).hexdigest())

altered = saved.replace(b"Room 3", b"Room 4")
Path("E1-modified.txt").write_bytes(altered)
print(len(altered), sha256(altered).hexdigest())
```

**Procedure.** First, predict whether both files will have the same byte length and whether their SHA-256 digests will match. Then run the script and record both output lines. Read `E1.txt` and `E1-modified.txt` to locate the intentional one-byte change. Re-run the first digest on `E1.txt` and compare it with the saved value. Finally write a collection note identifying the exact file, byte count, local collection time, synthetic source, authorized classroom scope, transformation and storage location. If you cannot run Python, reason from the displayed bytes and use the worked result to check your conclusion; software execution is not required to answer the conceptual question.

The byte count is a useful reproducibility check, but equal length is not equal content. A matching digest on `E1.txt` at two checks supports the limited statement that **the bytes checked were the same at those two times**, assuming the digest calculation and recorded values are trustworthy. A differing digest for the deliberately altered copy shows that this check detects that particular edit. Neither result verifies the truth of R9 or R14, completeness of the original query, correctness of a clock, identity of the editor, legal authority or whether data left the service. The example uses SHA-256 as an integrity check, not as proof of authenticity.

**Expected submission:** the two byte counts and digests, one sentence explaining why the hashes differ, a collection note for `E1.txt`, and two explicit limits on the integrity claim. **Rubric:** one point each for correct byte/digest comparison, correctly identified modification, complete source-and-authority note, and limits that distinguish copy integrity from source truth. A score of 4/4 means the classroom task is reproducible, not that a real forensic process has been completed. The exact expected output and a model note are in the final worked-results section after EX026.

### 2.6 Temporal coverage lab: what the analyst knew, and when

A useful timeline has at least two clocks: **event time**, as recorded by a source, and **discovery time**, when the responder received or recognized that record. A third time, **collection time**, marks when a copy was created and should be recorded separately. A query also has a **coverage interval**: the source and filters searched, the beginning and end of the search, and any ingestion delay or missing fields. These fields answer different questions. Sorting on one timestamp without naming which clock it represents can produce a fluent but false case history.

The Harbor Library example makes this visible. The learner's 09:05 decision used R1–R8. R9 records a 09:03 edit but is released to the learner with R9–R16 at the 09:20 review. The later discovery does **not** move the edit forward in time, and the earlier event time does **not** make it legitimate evidence for the 09:05 decision. An analyst should preserve both times so a reviewer can reconstruct what was actually knowable at each checkpoint. This is an original classroom workflow consistent with the source-aware investigation described in [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final); that older guide does not prescribe this book's specific fixture or scoring rule.

**Exercise-only card T1 — illustrative query metadata.** Imagine that a custodian now supplies the missing scope for R14: source `application-audit`; booking-edit events with event times **at or after 09:00 and before 09:12 UTC**; account filter `desk-a`; query run at 09:12 UTC. T1 is **not** one of R1–R16 and must not be used to rewrite the 09:05 decision or to pretend the original R14 supplied its own start and end. Even with T1, the statement “no further edit after R9 in this query” covers only that source, account filter and interval. It says nothing about another account, a delayed record or an edit at 09:13. Without T1, R14's exact interval remains unknown.

The following optional lab runs entirely in memory with Python 3's standard library. It creates no files, sends no network requests and uses only fictional timestamps. R10's `05:04-04:00` text is an **exercise rendering** of its existing 09:04 UTC value, not a new event or a claim about any real location's timezone rules. The offset is explicit; the script does not guess one.

```python
from datetime import datetime, timezone

rows = [
    ("R9", "2026-10-11T09:03:00+00:00", "2026-10-11T09:20:00+00:00"),
    ("R10", "2026-10-11T05:04:00-04:00", "2026-10-11T09:20:00+00:00"),
    ("R15", "2026-10-11T09:14:00+00:00", "2026-10-11T09:20:00+00:00"),
]

for record_id, event_text, seen_text in rows:
    event = datetime.fromisoformat(event_text).astimezone(timezone.utc)
    seen = datetime.fromisoformat(seen_text).astimezone(timezone.utc)
    delay = int((seen - event).total_seconds() // 60)
    print(f"{record_id} event={event:%H:%M} UTC seen={seen:%H:%M} UTC delay={delay} min")
```

**Procedure:** (1) Before running it, convert R10's offset time by hand and predict the three delays. (2) Run the code in an authorized local scratch environment, or calculate the outputs from the shown values if Python is unavailable. (3) Make a three-row table with record ID, original timestamp including offset, normalized UTC event time, discovery time, delay and whether the record was available at 09:05. (4) Draw the coverage interval from T1 as `09:00 ≤ event < 09:12 UTC` and put R9, the T1 end and the 09:20 review on it. (5) Write two sentences: the strongest conclusion supported by R14 with T1, and the next *authorized* check needed to assess activity after 09:12. Keep the R15 retention notice separate from any assumed deletion instant.

**Expected evidence:** R9 is 09:03 UTC and seen 17 minutes later; R10 is 09:04 UTC and seen 16 minutes later; R15 is 09:14 UTC and seen six minutes later. None was in the learner's R1–R8 snapshot at 09:05. With T1, R14 supports only that this narrow query showed no further matching edit before 09:12. The unqueried period after 09:12 is an **evidence gap**, not a verified quiet period. The learner should request a new bounded query or an approved source comparison, record its filter and end time, and check whether logging and ingestion were working. R15 says detailed records are deleted after 24 hours unless copied; it does not give enough deletion-policy detail here to calculate the precise expiry of R9 from its event timestamp alone.

**Assessment rubric:** one point each for correct R10 normalization, three correct event-to-discovery delays, the 09:05 availability boundary, a T1 coverage statement that excludes post-09:12 activity, and a narrow authorized follow-up with retention uncertainty. Five points show the classroom reasoning is reproducible; they do not certify a real evidence acquisition or establish who edited B19. The printed output and a model coverage statement appear after the Chapter 2 synthetic-extract result in the final appendix.

#### A query envelope is narrower than a case conclusion

A log search is a measurement operation over a specified source and filter, not a universal statement about everything that happened. An empty or apparently quiet result is meaningful only in the context of its **query envelope**:

| Envelope field | What a reviewer must know |
|---|---|
| Producer/source | Was the booking audit, application audit or another source queried? |
| Event-time interval | What beginning and end were selected, and was the end exclusive? |
| Identity/booking filters | Which account, booking IDs or operation kinds were included or excluded? |
| Query run time | When did the result reflect the available index? |
| Ingestion completeness | Through which event-time boundary was the relevant source demonstrably indexed? |
| Source health and retention | Were generation, collection and storage functioning during the interval? |
| Returned rows and transformations | Were rows missing, deduplicated, normalized or otherwise transformed? |

R14 is intentionally narrow: it reports no further booking edits after R9 **within its queried range**. Canonical R14 does not provide the complete envelope. R9 is labeled booking audit while R14 is labeled application audit. Treating them as a single fully covering source would silently merge producers without evidence.

This distinction exposes two different kinds of "nothing found." One is **no row matched this particular query at this query time**. The other, much stronger statement would be **the necessary producers were functioning, the selection was correct, the source's relevant events were all collected and indexed, and no qualifying event occurred in the bounded interval**. The former does not establish the latter.

The existing T1 exercise supplies illustrative metadata only when expressly invoked, and T2 demonstrates late arrival. The new VQ2 lab below goes a step further: it asks when the *metadata itself* would be adequate to support even a bounded negative statement. A query that covers the correct event interval but was run before ingestion had caught up is insufficient; so is a query with complete ingestion for the wrong account.

[NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) provides primary guidance on log generation, collection and management. This older publication supports the need to understand those stages; the envelope and acceptance gate are original instructional models, not a NIST query specification.

### 2.7 Delayed log arrival: when a quiet query changes

Section 2.6 established a **query envelope**: source, event-time interval, account filter and time at which a query was run. A fifth field matters when records travel through a collection pipeline: **ingestion time**, when a record becomes available to the queried store. An event may have occurred inside the requested interval yet be absent from a query run before its arrival. The absence is a statement about the store's visible contents at that query time, not a final statement about every event that happened in the interval. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) treats log management as a process of generating, transmitting, storing and using records. It is a 2006 high-level guide, not a specification for the exercise algorithm below. This book's delayed-arrival fixture and scoring rule are original classroom material.

Use four different times or bounds in the case note. The **event time** comes from the producing application and may itself be inaccurate if the source clock is wrong. The **ingestion time** is when the queried store accepted the row; it says nothing by itself about when the analyst read it. The **query run time** is when the analyst or custodian asked the store for matching rows. The **event-time window** describes which event timestamps the query selects. A discovery time records when the result reached the response team. If the store can supply only some of these fields, mark the rest unknown. A later query returning more rows does not automatically mean a new event happened after the earlier query.

The canonical Harbor Library R14 card says only that its available query showed no further booking edits after R9 **within its queried range**. T1 in section 2.6 adds an exercise-only event window and account filter. It does not supply an ingestion-completeness guarantee. At a real response desk, an analyst might request source health, pipeline delay and collector error information from the logging owner, but this beginner exercise supplies no such operating measurements. An empty interval should therefore be written as “no matching row visible in this query as run,” followed by its bounds. It should not be written as “no edit occurred.”

#### Optional T2 replay: a late row in the same event window

T2 is a **separate counterfactual replay**, not a new R-series record and not an amendment to the main case. Reset to the fictional 09:12 query snapshot, then imagine the following four synthetic rows. L1 transcribes R9 for this replay. L2–L4 are invented only to exercise query semantics; do not use them in EX014–EX026, Chapter 3 or the Chapter 4 tabletop unless a question explicitly names T2.

| Replay row | Account | Event UTC | Ingested UTC | Classroom observation |
|---|---|---|---|---|
| L1 | `desk-a` | 09:03 | 09:04 | B19 booking edit, representing R9 in this replay |
| L2 | `desk-a` | 09:10 | 09:18 | B21 booking edit, visible only after delayed ingestion |
| L3 | `helper-b` | 09:11 | 09:11 | B22 booking edit under a different account |
| L4 | `desk-a` | 09:12 | 09:13 | B23 booking edit at the excluded end boundary |

The replay query selects `application-audit` booking edits under `desk-a` with **09:00 ≤ event time < 09:12 UTC**. Its second condition is that the row was ingested **no later than the query run time**. The end boundary is exclusive. Assume all four clocks are correct, all rows belong to the same fictional date and no other filter exists; these are classroom assumptions, not evidence about production logging. First run the mental query at 09:12, then repeat the *same event window and account filter* at 09:20. Before looking at code, predict exactly which L IDs each run returns and which exclusion rule removes each other row.

This optional Python 3 standard-library program performs only the stated filtering in memory. It opens no files, sends no requests and cannot query a real service. Its minute parser is intentionally limited to a single fictional UTC day; it is not a general timestamp-normalization function.

```python
rows = [
    ("L1", "desk-a", "09:03", "09:04"),
    ("L2", "desk-a", "09:10", "09:18"),
    ("L3", "helper-b", "09:11", "09:11"),
    ("L4", "desk-a", "09:12", "09:13"),
]

def minute(utc_hhmm):
    hour, minute_part = map(int, utc_hhmm.split(":"))
    return hour * 60 + minute_part

def visible_at(query_time):
    return [
        row_id for row_id, account, event_time, ingested_time in rows
        if account == "desk-a"
        and minute("09:00") <= minute(event_time) < minute("09:12")
        and minute(ingested_time) <= minute(query_time)
    ]

for query_time in ("09:12", "09:20"):
    print(query_time, ",".join(visible_at(query_time)))
```

**Work the result in three passes.** First apply only the account and event-time filters: L1 and L2 qualify, L3 fails the account filter, and L4 sits exactly at the exclusive end. Then apply the ingestion cutoff: at 09:12 L2 is not yet visible, whereas at 09:20 it is. Finally compare the two results **without changing the event times**. The extra row in the second run is a *late arrival*, not a new post-09:12 event. Its presence would cause the response lead to revisit any conclusion that relied on the first query's apparent quiet period. It would not, by itself, identify who performed the edit or prove malicious intent.

The replay makes a useful operational distinction. A **complete interval** would require credible evidence that the source generated expected events, the transport accepted them, any buffering and retries were accounted for, the queried store indexed them, and the query covered the relevant source and filters through a defensible cutoff. An analyst cannot establish all that from the latest row's timestamp. A logging owner might supply a documented ingestion-lag bound or an independently monitored **watermark**, but the owner would have to state what that watermark means and what failures it excludes. This book supplies neither a watermark nor a service-level promise. A second empty query would remain bounded by its own run time and pipeline state.

**Submission and rubric.** Submit a two-row `query time | returned IDs | reason for every excluded ID` table, a one-sentence correction of the overclaim “nothing happened after R9,” and a request to the fictional application/logging custodian naming the event window, account filter, query run time and ingestion-health question. Score one point each for the 09:12 result, 09:20 result, correct explanations of L3 and L4, recognition that L2's *event* time did not move, and an authorized follow-up that distinguishes query coverage from account attribution. A 5/5 answer is a sound classroom interpretation; it is not verification of a real logging pipeline. The exact output and a worked answer appear in the final appendix after the Chapter 2 temporal-coverage result.

### 2.8 Evidence package audit: integrity is one link in a longer chain

The E1 file in section 2.5 is a **synthetic transcription** of book records R9 and R14. Its SHA-256 value can help a second learner check whether the working bytes changed. To assess a claim about the underlying booking service, a reviewer would still need to know who supplied the source, what query or export produced it, which fields or rows were excluded, what transformations were made, whether the source clock and logging path were functioning, and whether collection was permitted. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses evidence work across data sources but explicitly does not offer an all-inclusive forensic or legal procedure. The exercise below is a training review of a small invented package, not a chain-of-custody certification.

Think of three layers. The **source layer** is an application or identity system and its original records. The **copy layer** is a specific exported byte sequence plus a query or selection manifest. The **analysis layer** is the learner's chronology, hypothesis table and decision note derived from the copy. A digest for the copy can check the copy's bytes at two times. It cannot retroactively create a missing source layer or prove the analysis layer's interpretation. Conversely, a well-written analysis cannot repair a silently truncated export. Give each layer a pointer in the case record so the next reviewer knows what can actually be reopened.

For the E1 classroom file, a minimal **package manifest** might contain the following fields. `Status` matters: a *planned* export and a *collected* copy are different artifacts. The example assumes the learner actually ran `fixture.py`; if they did not, they must label byte count and digest as expected values from the book, not measurements they performed.

| Manifest field | Model entry after the local fixture runs | Limit the reviewer must retain |
|---|---|---|
| Item and status | `HL-IR-001/E1`, learner-created teaching copy | Not a production application export |
| Source and selection | Book section 2.5 payload transcribing R9 and R14; two data rows | R14's original query bounds remain unspecified without optional T1 |
| Authority and operator | Learner's local scratch directory under classroom permission | No permission to collect a real library's records follows |
| Creation and transfer times | Learner's actual local creation time; later handoff time only if a handoff occurs | Do not substitute fictional event time for file creation time |
| Bytes and integrity check | 235 bytes; SHA-256 of `E1.txt` as printed by the fixture | A matching value checks these bytes, not source truth |
| Transformations | UTF-8 teaching text assembled by the listed Python payload | The payload omits source metadata not shown in R9/R14 |
| Location and access | Local named file, restricted to the learner or authorized reviewer | The book provides no real storage-control evidence |
| Supported use | Practice a bounded collection note and an integrity comparison | No attribution, exfiltration or full audit-coverage conclusion |

The second learner should check the manifest against the *actual file and script*, not against a confident sentence in a handoff. Confirm the byte count and digest for the file received, read the two data rows, inspect the source and selection note, then compare the proposed conclusion with the package's stated limit. If the values match but the query selection is unknown, the second learner may say the copy is byte-consistent with the recorded digest; they may not say the queried service had no other edits. If the values differ, retain both copies and their labels in the classroom exercise, stop relying on the disputed copy, and ask which bytes were changed or transferred incorrectly. Never silently overwrite one copy with the other to make the hashes agree.

**Optional peer-audit drill.** Imagine three variants of a package handed to you at the 09:20 review. Variant A contains the expected `E1.txt`, its 235-byte count, digest, script and the manifest above. Variant B contains `E1-modified.txt` but labels it `E1.txt` while retaining the original digest. Variant C contains the exact E1 bytes and digest but omits the source-selection and authority fields. For each variant, write (1) what the byte comparison supports, (2) which claim about R9/R14 remains blocked, (3) what you would ask the sender to supply and (4) whether the package is usable for a classroom *copy-integrity* demonstration versus an operational incident conclusion. This drill is separate from EX014–EX026 and uses no real data.

The acceptance criterion is deliberately narrow. **Variant A** can pass the classroom copy-integrity check if the reviewer repeats the calculation; it still cannot prove R14's underlying query was complete. **Variant B** fails the claimed byte identity, regardless of whether the change was accidental or deliberate; that causal question is not answered by the digest mismatch. **Variant C** can have identical bytes yet fail the provenance and authorization review. A simple five-point rubric awards one point for distinguishing A's two kinds of claim, one for correctly rejecting B's recorded digest match, one for C's missing provenance and authority, one for a specific repair request for each variant, and one for a handoff sentence that labels every unperformed check. A model comparison is given in the final appendix.

When preparing a real handoff, ask the next analyst to **reproduce one consequential claim**: locate its source pointer, re-run or review the approved selection, verify the copy if one exists, and identify the decision that would change if the claim fails. This is a quality check on the team's reasoning. It does not replace specialist evidence handling where legal, privacy, disciplinary or contractual obligations apply. Chapter 3 will use the same separation when it asks whether a successful backup job is also a tested and accepted recovery.

#### Distinguish source, copy and interpretation

A digest can support a byte-consistency comparison for a named object at named checks. It does not prove that the source exporter was authorized, that every relevant event was emitted, that the source clock was correct, or that the copied rows identify a human.

The existing E1 laboratory already proves the narrower mechanism: two equally sized classroom files with one changed byte produce different SHA-256 values. Repeating that code here would not add learning. Instead, audit whether a proposed conclusion relies on one of three independent layers:

| Layer | What it can support | What remains to check |
|---|---|---|
| Source | A producer is designated for the business question | Its authority, schema, health, clocks and coverage |
| Copy | A selected byte sequence and its integrity check are documented | Source selection, permissions, transformations and missing rows |
| Interpretation | The investigator relates records to hypotheses | Identifier meanings, competing explanations and disconfirming evidence |

A perfect digest at the copy layer cannot fill a gap in the source layer. Two files could be byte-identical copies of a truncated export. A complete export might still fail to identify the person behind a shared account label. A reviewer must be able to point to the exact layer checked rather than say vaguely that "the evidence is authentic."

A common false positive is to interpret R13's one-session summary as proof of a particular physical operator. R13 omits device and location details, and session counts alone do not authenticate the person at the keyboard. The existing Q1 exercise intentionally shows how matching identifiers and time windows can remain ambiguous; this proposal does not rewrite Q1 or the canonical R13.

### 2.9 Contained lab: correlate records without inventing an actor

The earlier labs examined *when* a row became visible and whether a copied file changed. A responder also needs to ask whether records from two systems refer to the **same activity**. An account label, a session identifier and a human identity are different things. If an application audit records `desk-a` but omits its session identifier, several identity sessions for that account could fit the same time. A nearby timestamp cannot choose one by itself. An exact identifier can narrow a candidate relationship, but it still does not identify the person who used the session or establish that the edit was authorized. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) provides high-level log-management background, and [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses investigation across source types. Neither older publication prescribes this book's matching code or claims that an account/time join proves attribution. The following method is an original beginner-level teaching fixture.

This is a **separate optional Q1 replay**, not a new R record or a correction to R13. In the canonical Round B evidence, R13 reports one session within its *available range* and lacks device details. Q1 deliberately supplies **two overlapping sessions** for a different synthetic comparison so a learner can see an ambiguous join. Never import Q1 into the 09:20 canonical case decision, cite it as a discovered Harbor Library production fact, or reinterpret R13 as false. Both tables below are invented, contain no patron data and use explicit UTC instants on the same fictional date. The session intervals are half-open: `start <= event < end`, so an event at the printed end time is **outside** that row.

**Card Q1-A — isolated identity-session table.** The snapshot is an exercise table, not an authenticated export. `session_id` values are synthetic labels; no password, token or device identifier is supplied.

| Session | Account | Start UTC | End UTC |
|---|---|---|---|
| `S-A` | `desk-a` | 09:00 | 09:15 |
| `S-B` | `desk-a` | 09:02 | 09:12 |
| `S-C` | `front-b` | 09:00 | 09:20 |

**Card Q1-B — isolated application-edit table.** A blank application `session_id` means the field is **missing from this row**; it is not a statement that no session existed. The booking labels `X1`–`X4` are additional exercise-only identifiers and have no relation to B17–B20.

| Edit | Account label | Event UTC | Application `session_id` | Booking |
|---|---|---|---|---|
| `E-A` | `desk-a` | 09:05 | blank | `X1` |
| `E-B` | `desk-a` | 09:07 | `S-B` | `X2` |
| `E-C` | `desk-a` | 09:18 | blank | `X3` |
| `E-D` | `desk-a` | 09:06 | `S-X` | `X4` |

The **first pass** checks account label and interval. E-A falls inside both S-A and S-B, not S-C because its account differs. E-B falls inside both by time, but its explicit `S-B` key narrows the supplied candidate set to one. E-C has no account-and-interval match: the latest supplied `desk-a` session ends at 09:15. E-D falls inside both `desk-a` intervals by time, yet its explicit `S-X` key matches neither supplied ID. A responder should not silently discard the explicit key and report either S-A or S-B as the source. That would change the meaning of the evidence to make a join succeed.

The **second pass** asks whether the apparent matches deserve trust. The two tables might cover different collection windows, use clocks with different error, or have been filtered on different account identifiers. Q1 does not provide a query manifest, source-clock check, application schema showing that both `session_id` fields share one namespace, or a record of session rotation. E-C's zero matches therefore means **no row matched in this supplied table under this rule**, not that no session existed at 09:18. E-D's key mismatch may point to a missing identity row, a malformed application field or a wrong assumption about key namespaces. Its cause is unknown. Even E-B's one exact-key match does not prove who controlled S-B or why the edit occurred.

#### Reproduce the four classifications locally

The Python 3 standard-library program below keeps the invented rows in memory. It opens no file, makes no network request and alters no source. It validates that supplied session IDs are unique and that every interval has a start before its end; it then prints the candidates under the classroom rule. Use a scratch interpreter or reason through the rows on paper. If you change a fixture, label it a **variant** rather than rewriting Q1's original result.

```python
from datetime import datetime, timedelta

DAY = "2026-10-11T"
SESSIONS = [
    ("S-A", "desk-a", "09:00", "09:15"),
    ("S-B", "desk-a", "09:02", "09:12"),
    ("S-C", "front-b", "09:00", "09:20"),
]
EDITS = [
    ("E-A", "desk-a", "09:05", ""),
    ("E-B", "desk-a", "09:07", "S-B"),
    ("E-C", "desk-a", "09:18", ""),
    ("E-D", "desk-a", "09:06", "S-X"),
]


def utc(clock):
    value = datetime.fromisoformat(DAY + clock + "+00:00")
    if value.utcoffset() != timedelta(0):
        raise ValueError("expected an explicit UTC instant")
    return value


seen = set()
parsed = []
for sid, account, start, end in SESSIONS:
    if sid in seen or utc(start) >= utc(end):
        raise ValueError("duplicate session ID or invalid interval")
    seen.add(sid)
    parsed.append((sid, account, utc(start), utc(end)))

for eid, account, event, explicit_sid in EDITS:
    moment = utc(event)
    window = [sid for sid, owner, start, end in parsed
              if owner == account and start <= moment < end]
    if explicit_sid:
        matches = [sid for sid in window if sid == explicit_sid]
        status = "KEY_AND_WINDOW_MATCH" if matches else "EXPLICIT_KEY_UNMATCHED"
    elif len(window) == 0:
        matches, status = [], "NO_WINDOW_MATCH"
    elif len(window) == 1:
        matches, status = window, "ONE_WINDOW_CANDIDATE"
    else:
        matches, status = window, "AMBIGUOUS_WINDOW_CANDIDATES"
    print(f"{eid}: {status} candidates={','.join(matches) or '-'}")
```

The method has an important asymmetry. An explicit key that fails to match is **not** treated like an absent key. The former is evidence of a mismatch under the assumed schema; the latter simply leaves account/time as a weaker possible relationship. `ONE_WINDOW_CANDIDATE`, if a variant ever produces it, means one row survived this table filter, not a measured probability that the row is correct. The program never emits a person's name or a compromise verdict because neither table supplies that evidence. It also does not check that the tables are complete or that the account labels were populated consistently; those limits belong in the learner's result note.

**Practice task.** Submit a four-row result table with event ID, status, candidate session IDs and one sentence stating what the result **cannot** establish. Then write a bounded custodian request for the missing query range, source-clock quality and shared session-key semantics. Identify the fictional incident lead as the person who must authorize any additional collection under the classroom role boundary; no learner may query a real identity or booking system. Finally, create a variant `Q1-V`: remove only E-B's explicit `S-B` key and predict which classification changes. Do not treat a changed result as a new canonical event.

**Expected evidence:** four classifications matching the printed program output, a limitation for each, a request that names the smallest useful source and fields, and the Q1-V prediction. **Rubric (six points):** one point for correctly identifying both E-A candidates; one for E-B's key-and-window match without human attribution; one for E-C's zero-match limit; one for preserving E-D's explicit-key mismatch; one for a proportionate request including clock, coverage and schema; and one for predicting that E-B becomes ambiguous when its key is removed. A 6/6 score verifies reasoning on this fixture, not the trustworthiness of a real log join. The exact output and model request appear in the final answer appendix after the Chapter 2 evidence-package audit result.

<a id="ir-rapid-ch02-vq2-lab"></a>

### 2.10 Offline laboratory: when is a quiet-query claim defensible?

**Learning purpose:** Check evidence release, query scope, ingestion-coverage metadata and an unknown retention anchor without replaying the existing T1/T2 search or E1 hash laboratory.

**Classification:** Entirely synthetic classroom variant VQ2. This is **not** a new R-series observation, an amendment to R14, a real ingestion watermark or a production collection.

**Environment:** Python 3 standard library, in memory. No files, network operations, credentials or service changes.

#### Input interpretation and acceptance contract

The VQ2 scenarios ask a *hypothetical custodian* whether a claim of no additional matching edit is even conditionally defensible for the **application-audit / desk-a / 09:00 ≤ event < 09:12 UTC** scope.

The fixture includes an artificial returned teaching identifier, `VQ-01`. This is **not** R9, is not authenticated to R9, and must not be merged with canonical Harbor Library events. A hypothetical ingestion watermark claims coverage through a specified event-time boundary. Even a passing result remains conditional on the custodian's attestation that the source, metadata, clock, collection health and query actually mean what the manifest claims.

**Pre-run predictions:**

- The original R14 record has no complete query manifest, so the program cannot certify its scope.
- An early watermark ending at 09:07 cannot establish ingestion completeness for the whole interval ending at 09:12.
- A manifest for another account is irrelevant to a `desk-a`-only claim.
- A watermark later than its own query-run time is internally inconsistent in this simplified fixture.
- A 24-hour retention period without an anchor never yields a valid deletion deadline.

#### Reproducible Python 3 code

~~~python
RELEASE = {"R9": "09:20", "R14": "09:20", "R15": "09:20"}

def minute(clock):
    h, m = map(int, clock.split(":"))
    return 60 * h + m

def can_use(record, decision):
    return minute(RELEASE[record]) <= minute(decision)

print(
    "release:",
    "R9@09:05=" + ("YES" if can_use("R9", "09:05") else "NO"),
    "R9@09:20=" + ("YES" if can_use("R9", "09:20") else "NO"),
)

base = {
    "source": "application-audit",
    "account": "desk-a",
    "start": "09:00",
    "end": "09:12",
    "run": "09:20",
    "watermark": "09:12",
    "returned": ("VQ-01",),
}

variants = [
    ("CANONICAL_R14", None),
    ("EARLY_INGESTION", {**base, "run": "09:12", "watermark": "09:07"}),
    ("HYPOTHETICAL_MANIFEST", base),
    ("OTHER_ACCOUNT", {**base, "account": "helper-b"}),
    ("IMPOSSIBLE_WATERMARK", {**base, "run": "09:12", "watermark": "09:16"}),
]

def assess(manifest):
    if manifest is None:
        return "UNKNOWN_MANIFEST"
    if minute(manifest["watermark"]) > minute(manifest["run"]):
        return "INCONSISTENT_METADATA"
    if (
        manifest["source"] != "application-audit"
        or manifest["account"] != "desk-a"
        or manifest["start"] != "09:00"
        or manifest["end"] != "09:12"
    ):
        return "SCOPE_MISMATCH"
    if minute(manifest["watermark"]) < minute(manifest["end"]):
        return "INGESTION_NOT_COVERED"
    if manifest["returned"] != ("VQ-01",):
        return "RESULT_NOT_AS_ASSUMED"
    return "CONDITIONAL_IF_ATTESTED"

for name, manifest in variants:
    print(f"{name}: {assess(manifest)}")

policy = {"period_hours": 24, "anchor": None}
print("R15_DEADLINE:", "UNKNOWN" if policy["anchor"] is None else "REQUIRES_VALIDATION")

assert assess(variants[2][1]) == "CONDITIONAL_IF_ATTESTED"
assert policy["anchor"] is None
~~~

#### Exact expected output — executed against the displayed fixture

~~~text
release: R9@09:05=NO R9@09:20=YES
CANONICAL_R14: UNKNOWN_MANIFEST
EARLY_INGESTION: INGESTION_NOT_COVERED
HYPOTHETICAL_MANIFEST: CONDITIONAL_IF_ATTESTED
OTHER_ACCOUNT: SCOPE_MISMATCH
IMPOSSIBLE_WATERMARK: INCONSISTENT_METADATA
R15_DEADLINE: UNKNOWN
~~~

#### Annotated results and negative controls

- `release` establishes only **learner availability** of R9: absent at the 09:05 Round A decision and available by the Round B review. The program has no authentic source-ingestion timestamps.
- `CANONICAL_R14` lacks sufficient metadata. The correct conclusion is **unknown query envelope**, not "no edits happened."
- `EARLY_INGESTION` models an under-covered interval: the declared watermark ends before the queried interval does. A result at that point cannot exclude events that had not yet arrived at the store.
- `HYPOTHETICAL_MANIFEST` is **conditional**, not confirmed. It accepts a fully specified classroom envelope and declared ingestion boundary but has no external verification that the declaration is truthful or complete.
- `OTHER_ACCOUNT` is a negative scope control: evidence for `helper-b` cannot establish a `desk-a` negative finding even if other metadata looks complete.
- `IMPOSSIBLE_WATERMARK` rejects contradictory classroom metadata rather than silently treating a future watermark as a real guarantee.
- `R15_DEADLINE` remains **UNKNOWN**. The program intentionally cannot turn a period into a deletion instant while the policy anchor is absent.

**Lab limitations:** The `minute` helper handles only single-day HH:MM timestamps; it is not a timezone or multi-day event parser. It does not authenticate query metadata or establish clock correctness. `VQ-01` is a synthetic result marker, not an application audit of R9. A conditional pass tests the *logic of the stated envelope*; it cannot prove producer completeness, an authorized export or a real incident.

**Required submission:** Provide the seven output lines, a manifest-assessment table naming one uncertainty for each scenario, a two-sentence explanation of why the 09:05 decision cannot cite R9, and a preservation request that leaves R15's exact deletion deadline unknown. Add a proposed falsifier: identify the metadata or new qualifying row that would invalidate your current quiet-query conclusion.

**Pass criteria:** Exact reproducibility; no release-boundary violation; no unsupported retention arithmetic; clear distinction between a declared watermark and authenticated completeness; no merger of VQ2 into R1–R16.

### 2.11 Contrastive 09:20 decision example

**Incorrect handoff:**

> "R9 proves the employee attacked B19 at 09:03. R14 proves no further edits happened, and R15 means we have exactly until 09:03 tomorrow to preserve the logs. The records are hashed, so we can declare the account compromised and close collection."

The sentence makes several unsupported jumps. R9 is an application-related booking record under an account label, not verified human attribution. R14 has unspecified source/query bounds and does not prove a universal quiet period. R15 does not define its retention anchor. No completed export or digest check for the underlying canonical records is supplied. Even a genuine matching digest would not settle authorization or root cause. The analyst also confuses account-compromise confidence with preservation urgency.

**Correct bounded assessment:**

> "At the simulated 09:20 review, R9 reports a B19 change at 09:03 UTC; R10's supplied training plan names B17/B18 but not B19, and R12 records that the staff member does not recall B19. These observations warrant an authorized training-scope and service-impact check without identifying the human operator. R14 describes a quiet result only within its unspecified query range; R15 reports a 24-hour deletion policy whose anchor remains unknown. The incident lead should seek a bounded availability and preservation decision with the application custodian and review the matter by 09:35 UTC, or sooner on a verified new unexplained edit. No production copy, restriction or completed identity investigation is established."

The better version does not avoid making a decision. It makes a *specific, reviewable next decision* without asserting evidence that is not present.

### 2.12 Three-lane handoff for independent review

A handoff is complete when another analyst can trace important claims to sources, identify why an apparently stronger conclusion was rejected, and continue through an authorized next step. Include an exact checkpoint, the original record IDs, owner of the next request, decision status and revisit condition.

A compact handoff has three lanes:

**Evidence lane:** "R9 reports B19 edited; R10 omits B19 from the supplied plan; R11 records a second patron report; R13 lacks device/location detail." These are statements about the supplied records.

**Assessment lane:** "Training remains plausible for B17/B18; B19 authorization and human attribution remain unresolved; overall patron impact is not measured." These are interpretations with limits.

**Action lane:** "Propose P-A; request custodian confirmation of the retention anchor and actual source coverage; ask the service owner to authorize a bounded impact comparison; review at 09:35 or on a verified fresh edit." These are plans, not completed operations.

A receiver should be able to challenge the assessment without questioning whether an unseen action occurred. The handoff should say "requested" when requested, "approved" only when approval is documented, and "collected" only when a collection receipt exists. This discipline also prevents an exercise-only query manifest from being misreported as an operational source observation.

The next chapter may consider containment and recovery decisions, but Chapter 2 cannot pre-authorize those changes or introduce Round C evidence. Its immediate result is a bounded, preservation-aware decision ready for review.

### 2.13 Handoff and common errors

A useful handoff lets a second analyst reconstruct the decision without guessing: case ID; current time and timezone; affected service; observed facts with record IDs; live hypotheses; confidence and limits; known service impact; actions completed under which authority; evidence locations; next question; decision owner; review deadline. It should also separate the source's event time from the time the analyst learned of the event.

Common errors are copying only an alert title, silently converting timezones, treating a staff recollection as proof, relying on a log summary that omits key fields or query boundaries, hashing a file without recording which bytes were hashed, or using a high severity label without naming harm and urgency. A careful analyst can be concise: cite the observation, state the limit and identify the next decision. T1 shows why “I discovered R9 at 09:20” does not mean “R9 occurred at 09:20”; conversely, the 09:03 event time does not mean R9 was available for a 09:05 decision. T2 adds a second trap: repeating an event-time query after delayed ingestion can reveal another row without changing the event's occurrence time. The E1 package audit keeps byte integrity, source provenance and authority separate. Q1 adds a cross-source trap: an account/time overlap is a candidate relationship, while a missing or unmatched session key cannot be repaired by confidently naming a person.

### 2.14 Define the thing you are trying to count

"How many were affected?" is not an answerable technical question until an analyst defines what an *affected unit* is.

A **ticket** is a report submitted to a service channel. A **booking** is an application business object. An **edit event** is a recorded operation. A **patron** is a person or account associated with service use. One person may open multiple tickets, one ticket may discuss several bookings, and one booking may have several audit records. These objects must not be treated as interchangeable.

In Harbor Library, R5 contains a patron report about B18; R11 is a second patron report about B19. R3, R4 and R9 describe booking changes. The supplied chapter does not include a complete current authoritative-state comparison or the population of all bookings. Therefore, at the 09:20 checkpoint, the learner can identify **specific reported concerns and recorded changes**, not an independently measured total of incorrect bookings or affected people.

Before any count, write the **measurement question**:

> "Among the booking IDs included in an authorized, owner-defined comparison interval, how many have a current authoritative value that differs from the approved expected state?"

This is substantially narrower than:

> "How many patrons were harmed by the incident?"

The second question requires additional relationships and harm criteria. A room assignment discrepancy could inconvenience a patron, but whether it caused actual harm, whether multiple patrons were associated with the same room, and whether the issue was corrected before use are all separate facts.

The general incident-response goal is to assess scope and consequences based on available evidence. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places response analysis and decisions within cybersecurity risk management; the measurement contract below is original instructional material, not a prescribed NIST impact score.

### 2.15 Establish four levels of impact claim

It helps beginners to classify claims before attempting to calculate a total.

| Classification | Example claim | What it establishes | What it cannot establish alone |
|---|---|---|---|
| **Reported concern** | A help-desk record says that a booking looked wrong | A report was received | That the authoritative state was incorrect or every symptom occurred as described |
| **Recorded change** | Application audit says a room assignment changed | The producer recorded a change | Whether the change was approved, harmful, durable or visible to a patron |
| **Verified state discrepancy** | An authorized comparison finds a current value differs from an owner-approved target | A mismatch exists for the *tested object and state versions*, under the comparison's trust assumptions | The size of the unexamined population, root cause or human actor |
| **Verified service consequence** | A service owner validates a specific failed reservation outcome | The documented scenario caused an unacceptable outcome within tested scope | Whether all patrons experienced the same effect |

These classifications can apply to the same booking; they are not mutually exclusive replacement labels. A report and an audit event can support investigating one booking, while a later state comparison adds a distinct, stronger claim. The analyst should preserve the original evidence and note which new source justified the upgrade.

A state discrepancy must also have a defensible reference target. "The current room is different from the old room" does not necessarily mean it is wrong: a legitimate staff edit could have been approved. The target needs an owner, version, applicable time and authority. If the target is missing, record the comparison as **unverified**, not automatically a mismatch.

### 2.16 The numerator and denominator have different evidence requirements

A count needs a **numerator**, the items meeting the definition, and a **denominator**, the items in the defined population against which the count could be interpreted.

Suppose a restricted comparison examines five selected booking IDs and finds two confirmed mismatches. A precise statement is:

> "Two of the five selected IDs have a verified mismatch under the supplied comparison rules; the other three require their own status classification."

It would still be incorrect to claim:

> "Forty percent of Harbor Library bookings were corrupted."

The selected five could have been chosen because they were suspicious, reported or otherwise convenient. Without evidence that the five represent the entire relevant population or a valid sampling design, their observed proportion cannot be generalized to every booking.

Selection may be **case-driven** rather than representative. An incident analyst often investigates the most urgent known objects first. That is appropriate for containment and service repair, but it creates a biased basis for estimating prevalence. Case selection and statistical sampling are different activities.

The analyst should separate:

- **Known examined frame:** the exact identifiers selected and why.
- **Comparable items:** selected identifiers for which both approved reference and current values are available.
- **Confirmed mismatches:** comparable items that fail the declared equality or business acceptance check.
- **Unverified items:** records missing one of those comparison prerequisites.
- **Unexamined population:** objects outside the selected frame or with unknown existence or completeness.

Do not silently exclude unknown items from the report just to make the ratio look more favorable. Instead state, for example, "two mismatches, two matches and one unverified item within the five listed comparisons; no population-wide estimate available."

This approach is useful even when no percentage is calculated. Counts expressed with explicit scopes let the next analyst decide whether to broaden the inquiry or correct known business state immediately.

### 2.17 Deduplicating does not mean discarding evidence

A help-desk queue may contain repeated calls, email replies or follow-up tickets about one booking. Deduplication can prevent overcounting *booking identifiers*, but it must not destroy the fact that multiple reports were received.

Consider two fictional tickets referencing the same booking. For the question "How many distinct bookings have a reported concern?" the two tickets correspond to **one booking identifier**. For the question "How much help-desk demand was received?" they remain **two separate contacts**. For the question "How many people were affected?" neither answer is sufficient unless the distinct individuals and relevant outcome are reliably established.

Always preserve the original ticket IDs. A normalized table may group them by booking identifier, but the grouping rule must be explicit and reversible. If a booking ID is absent or misspelled, do not make an automatic identity assumption from a similar time or room number.

A dangerous shortcut is to treat multiple independent reports as multiple verified incidents or to count one booking once for each edit event. Another shortcut is to collapse all reports into one and then claim that only one person was affected. Each changes the unit without informing the reader.

The source/copy/interpretation separation explained in Chapter 02 also applies here. A normalized, deduplicated view is a **derived analytical product**. Keep the source pointers and transformations visible. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log-management processes and the handling of event records at an organizational level. It does not specify the fictional deduplication procedure in this section.

### 2.18 Missing information is an impact result, not a reason to guess

An absent owner-approved target, missing current-state row, incomplete query filter or unreliable source timestamp makes some impact claims **unverified**. This classification does not say the booking is healthy or broken.

A response team must distinguish:

1. **Negative observation:** a defined, functioning, appropriately scoped test produced evidence supporting an absence or expected result within its bounds.
2. **Missing observation:** the record or comparison needed for the test was not supplied or could not be trusted.
3. **Contradictory observation:** a properly conducted comparison produced a result that fails the accepted target.

A query that returns no relevant audit rows while collection health is unknown belongs in the second category for any broad absence claim. A state comparison that explicitly shows a different accepted value may support the third category—but only if the target and current value have adequate provenance.

R14's quiet summary is a reminder: a bounded log query cannot certify that no changes occurred outside its query envelope. R15's 24-hour retention policy adds urgency to preserving the source needed for an impact comparison, but its exact deletion anchor remains unknown. These limits affect what can be measured as well as what can be investigated.

### 2.19 A defensible impact ledger

A useful impact ledger contains one row per selected business object, with separate columns for the sources that describe it. It should not put a free-form narrative in place of a test result.

| Field | Explanation |
|---|---|
| Booking ID | Exact identifier within approved scope |
| Selection reason | Audit edit, help-desk report or owner-defined test frame |
| Related evidence | Pointers to source records and query or collection receipts |
| Approved reference | Expected value, version, approval owner and applicable time |
| Current authoritative value | Observed value, source, time and collection method |
| Comparison state | Match, mismatch or unverified |
| Reported service effect | Reported concern, verified consequence or not assessed |
| Uncertainty | Missing records, source-health limits or conflicting interpretations |
| Next action and owner | Bounded comparison, correction proposal or preservation request |

An analyst should not add patron names or unrelated account details to a shared impact summary when booking identifiers and controlled references are sufficient. The service owner can evaluate business consequences and authorize further checks within the relevant privacy rules. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides source-aware guidance for incorporating forensic techniques into incident response; it does not provide a blanket authorization to collect personal data.

The impact ledger's **selection reason** is especially important. If every row was selected because someone complained, a ratio from those rows cannot estimate how common a problem is among people who did not complain. If the source is a partial application audit, the ledger cannot measure omitted write paths or disappeared records. State the missing part of the frame before recommending a new collection.

### 2.20 Contrastive worked example at the Round B decision

**Plausible but incorrect assessment:**

> "R3, R4 and R9 show three booking edits, and R5 and R11 contain two patron reports. Five patrons were affected, so the incident has a confirmed five-user impact."

This is an invalid unit conversion. The three application changes are not five distinct people. The two help-desk reports are observations of reports, not independent verification of two incorrect authoritative states. R3/R4 may include approved training work. Nothing in the Round B case establishes a complete distinct-patron population or the final approved booking targets.

**Correct bounded assessment:**

> "By the fictional 09:20 Round B review, Harbor Library has source records reporting changes to B17, B18 and B19, plus patron complaints involving B18 and B19. The approved scope and current authoritative state for those bookings have not been fully verified. The incident lead should request a bounded, service-owner-approved comparison of the relevant booking identifiers with the correct target state, preserving its source coverage and retention limitations. No total of affected patrons can yet be established from the supplied material."

This assessment makes a useful decision while refusing a fabricated count. It does not need to delay all protective action until every record is available; urgency, ongoing potential harm and evidence loss remain separate considerations.

### 2.21 Communicate a lower bound without claiming completeness

If an authorized comparison later verifies that two selected booking states are inconsistent with approved targets, the analyst can sometimes state **at least two identified mismatches among the checked items**. That is a lower bound for the known, explicitly identified objects under the test assumptions. It is not the total affected booking count unless the investigated frame is complete.

For a public message, even a correct internal count may be too specific if it exposes other patrons or could be misread as exhaustive. An internal service owner may need booking IDs, approved targets and corrective owners; a patron-facing note may only need to acknowledge a possible room-booking discrepancy and describe the owner-confirmed assistance channel. The communications role must not convert "we have identified two incorrect selected bookings" into "only two bookings were affected."

A review should ask which wording remains true if additional relevant source records arrive later. "Two mismatches were identified in the approved five-object comparison" remains true, assuming that comparison was valid. "Only two bookings were affected" can become false as soon as an additional affected object is found. The first is therefore a more resilient and auditable statement.

### 2.22 Failure modes and acceptance limits

| Failure mode | Misleading conclusion | Safer interpretation |
|---|---|---|
| Repeated tickets for one booking | Each ticket represents a new affected booking | Keep ticket count and distinct booking count separate |
| A booking changed in an audit | The change harmed a patron | Validate authorization, approved expected state and service outcome |
| Five suspicious objects examined | Results describe the full population | State the selected frame and avoid prevalence extrapolation |
| Reference target unavailable | No mismatch was found | Comparison is unverified, not passed |
| Current record absent | Booking was deleted | Query, retention, source or export may be incomplete |
| Matching source and current values | All service outcomes are correct | Check applicable version, time, authorization and user-facing result |
| Two confirmed mismatches in a subset | Exactly two bookings were affected overall | At least two were identified within the declared subset, if trusted |
| No new complaint in the help desk | No further harm occurred | Reporting channels and coverage are incomplete observations |

A beginner has met this section's objective when they can select the correct unit, preserve source and derived identifiers, distinguish confirmed mismatch from missing comparison evidence, and write a decision-ready conclusion without claiming a measured population they never examined.

<a id="ir-rapid-ch02-im2-lab"></a>

### 2.23 Offline laboratory — IM2: Reports, distinct bookings and confirmed mismatches

**Classification:** Independently invented, offline-only teaching fixture. IM2 is **not** an additional Harbor Library R-series release, not an approved production comparison, and not P1/C1 from Chapter 03. Identifiers X01–X05 and X99 are fictitious classroom business objects; T01–T04 are fictitious report references.

**Goal:** Separate ticket count, distinct reported booking IDs, verified mismatches in an examined frame and unverified comparisons. Demonstrate how removing an approved reference changes the strength of a claim without changing the underlying hypothetical current value.

**Environment:** Python 3 standard library, in memory. No file operations, network calls, credentials, database writes or real identities.

**Input assumptions:** The dictionary `TARGET` supplies an artificial owner-designated comparison target; `CURRENT` supplies an artificial current-state view. These values are inputs invented for the exercise, not real owner approvals or authenticated exports. A value `None` means the target is missing. The report tuples are separate source observations; repeated booking references are preserved.

Before running, predict: (a) the number of reports, (b) the number of distinct booking references in those reports, (c) which examined IDs mismatch, and (d) what happens when the reference target for X04 is removed in a *variant*.

~~~python
TARGET = {
    "X01": "Room A",
    "X02": "Room B",
    "X03": "Room C",
    "X04": "Room D",
    "X05": None,
}

CURRENT = {
    "X01": "Room A",
    "X02": "Room C",
    "X03": "Room C",
    "X04": "Room B",
    "X05": "Room A",
}

REPORTS = [
    ("T01", "X02"),
    ("T02", "X02"),
    ("T03", "X05"),
    ("T04", "X99"),
]
~~~

The report list is preserved as four contacts. The classifier below builds a union of IDs, then checks whether each one has both values needed for a comparison. Run the three code blocks together in order in one Python session.

~~~python
def classify(target, current, reports):
    ids = sorted(
        set(target) | set(current) |
        {booking_id for _, booking_id in reports}
    )

    counts = {
        "MATCH": 0,
        "MISMATCH": 0,
        "UNVERIFIED": 0,
    }

    results = {}

    for booking_id in ids:
        expected = target.get(booking_id)
        observed = current.get(booking_id)

        if expected is None or observed is None:
            status = "UNVERIFIED"
        elif expected == observed:
            status = "MATCH"
        else:
            status = "MISMATCH"

        results[booking_id] = status
        counts[status] += 1

    distinct_report_ids = {
        booking_id for _, booking_id in reports
    }

    print(
        "reports:", len(reports),
        "unique_booking_refs:", len(distinct_report_ids)
    )

    for booking_id in ids:
        print(f"{booking_id}: {results[booking_id]}")

    print(
        "counts:",
        ",".join(f"{key}={value}" for key, value in counts.items())
    )

    return results
~~~

The negative control removes a reference from a copy of `TARGET`; it does not change `CURRENT` or edit a booking. Predict the change in claim strength before running this final block.

~~~python
original = classify(TARGET, CURRENT, REPORTS)

# Negative control: remove the approved comparison
# value from a copy, without modifying the baseline.
variant = dict(TARGET)
variant.pop("X04")

negative_status = (
    "UNVERIFIED"
    if variant.get("X04") is None
    else "MISMATCH"
)

print("negative_X04_target_removed:", negative_status)

assert original["X04"] == "MISMATCH"
assert variant.get("X04") is None
~~~

Compare your result with the [IM2 worked transcript and interpretation](#ir-rapid-ch02-im2-result) in the final answer appendix.

### Chapter 2 exercises

Use only records R1–R16 and the fictional authority described here; the exercise-only T1 card is available **only** where a question names it. No answer may claim to have queried a real service, received an unprovided identity detail, proved compromise or completed an export that the learner did not make. For each exercise, cite the relevant record IDs, state the observation before the inference, and give a bounded next action or test. The named output is the artifact to submit; the worked results at the end show acceptable reasoning.

**Common procedure and expected evidence:** (1) Write the exercise ID, case ID and evidence boundary at the top of the response. (2) Read the named input records and copy their IDs and relevant UTC times into the requested table or note. (3) Complete that exercise's output fields, marking unknown facts and unperformed actions rather than filling them with guesses. (4) Add the decision owner or custodian for any proposed collection or service change and a sentence limiting the conclusion. (5) Compare the resulting artifact with its matching worked result in the final appendix. Submit the named table or note with its source pointers and limits; a bare multiple-choice label or unsupported conclusion is not sufficient evidence of learning. No real account, patron record or production log is needed.

Score each numbered exercise **0** when its artifact is absent or asserts an unsupported fact, **1** when it addresses the question but omits a required evidence, scope or limitation field, and **2** when the stated fields are present, reproducible and appropriately authorized. A false claim about who controlled `desk-a`, a fabricated collection time or an invented log query must be corrected regardless of the other fields. This common rubric applies to all thirteen questions; a local instruction below adds required fields for a score of 2.

#### EX014 — Triage question

**Objective:** turn a detector label into testable questions. **Inputs:** R9–R16 and the Chapter 1 service map. **Output:** a two-row table with question, relevant supplied record, authorized owner or source to ask next, and an answer that would change triage. Begin with the label “suspicious booking edit” and avoid using the label as evidence. A score of 2 requires two different discriminating questions and a bounded source for each.

#### EX015 — Hypothesis table

**Objective:** keep competing explanations live. **Inputs:** H1–H3 from section 2.1 and R1–R16. **Output:** three rows, each with a supporting record, a contradiction or limit, a narrow next authorized check and what result would weaken that hypothesis. You may state that a record is weak support. A score of 2 requires at least one check that could genuinely discriminate between explanations rather than simply restating the same log.

#### EX016 — Priority without false certainty

**Objective:** set urgency without inventing a severity fact. **Inputs:** R9–R16 at the 09:20 discovery point. **Output:** a short decision note with separate fields for potential patron harm, retention or ongoing-activity urgency, confidence in the leading hypothesis, provisional priority, decision owner and an observable review trigger. A score of 2 requires a reason for the priority and a deadline or event, not merely a color or number.

**Extension:** Require one sentence explaining why retention urgency can be high while evidence of account compromise remains inconclusive. Identify what would cause the priority to increase and what would justify a less urgent review. Do not turn an unknown deadline into a guessed timestamp.

**For full credit:** The learner identifies R15's possible evidence-loss path, R9/R11's potential booking harm, unresolved attribution, the incident lead's decision authority and the 09:35 review or an earlier verified trigger.

**Additional IM2 discriminator for EX016:** At Round B, distinguish the urgency to preserve R9/R11-related evidence under R15 from confidence in a cause or a measured affected-patron total. The separate IM2 fixture supplies no Harbor Library outcome.

#### EX017 — What the summary cannot prove

**Objective:** test the limits of negative evidence. **Inputs:** R13, R14 and, for this question only, the optional T1 metadata. **Output:** two short claim/limit pairs and one proposed follow-up query. First assess R14 *without* T1; then state exactly what T1 adds and what it still cannot cover after 09:12. Explain why R13 does not establish that the `desk-a` session came from the expected staff device. A score of 2 distinguishes missing device fields from a negative device finding and names the query's filter and interval.

**Extension:** Before using optional T1, describe exactly which fields of R14's query envelope are missing. When using T1, distinguish a bounded event-time filter from an ingestion-completeness guarantee; name the first excluded boundary.

**For full credit:** The learner says that even optional T1 ends before 09:12 and does not authenticate logging completeness, another account or activity at and after 09:12. R13's missing device field remains unknown rather than a negative device finding.

#### EX018 — Retention decision

**Objective:** prepare a proportionate preservation decision. **Inputs:** R9, R13–R15, the collection-note fields in section 2.3 and the worked queue in section 2.4. **Output:** a three-row `P-A` request to the application custodian stating each source and proposed event range, deletion-policy anchor or actual deadline, and collector/authority/storage scope; add one sentence explaining why preservation may precede root-cause knowledge. Then add a two-row comparison of `P-A` with `P-B`: decision each could change, known or unknown loss path, owner, present state and why the second availability check may proceed in parallel. Do not calculate a precise expiry merely by adding 24 hours to R9's timestamp or claim either source was collected. A score of 2 identifies the time-sensitive risk, privacy boundary and proposal-versus-collection distinction for both sources.

**Extension:** Include a specific question that the application custodian must answer about the deletion-policy **anchor** and a separate question about whether the oldest requested row is still retrievable. State the status of P-A and P-B using the exact words `proposed`, `approved`, `collected` or `verified`, without skipping intermediate states.

**For full credit:** A 24-hour rule is a duration, not a confirmed deletion instant; P-A's potential urgency does not authorize a bulk export or establish that a hold took effect.

#### EX019 — Collection note

**Objective:** make an exercise extract reviewable. **Inputs:** the E1 fixture in section 2.5 and R9/R14. **Output:** a collection-note table with case/item ID, source and event range, collector, authority, actual local collection time *if a file was created*, copy location, transformation and limitation. If no file was created, label the note **planned** and leave collection time and digest **not applicable**; do not pretend an export occurred. A score of 2 identifies E1 as a synthetic transcription, distinguishes original book text from the working file and records access scope. A made-up digest is not required.

#### EX020 — Hash claim

**Objective:** bound an integrity claim. **Inputs:** the named E1 bytes, the two digest checks and section 2.5. **Output:** a five-row claim table: two statements the comparison supports and three it does not, each with a one-sentence reason. Specify which file and times were checked rather than saying “the evidence is authentic.” A score of 2 distinguishes copy consistency from source truth, completeness and collection authority.

**Extension:** For one claim that a matching E1 digest supports, name its exact evidence layer (copy). For one claim it cannot support, name the missing source/selection or interpretation layer. Keep the E1 lab's original numbers and bytes unchanged.

**For full credit:** Matching hashes concern chosen bytes; they do not attest producer completeness, collection permission or the person responsible for B19.

#### EX021 — Time ordering

**Objective:** separate event order from causal inference. **Inputs:** R9, R10, R12, R15 and R16; use T1 only for the optional final sentence. **Output:** five ordered rows with ID, UTC event time, source and one uncertainty about cause. Mark that R9–R16 reached the learner at 09:20 despite earlier event times. Optionally state which interval T1 leaves uncovered. A score of 2 preserves event/discovery separation and does not treat temporal precedence as authorization or attribution.

#### EX022 — Handoff

**Objective:** allow a second analyst to continue without guessing. **Inputs:** the Round B snapshot R1–R16 and the fictional approval path. **Output:** a five-sentence handoff at 09:20 UTC that includes case ID and service, at least two evidence IDs, a live hypothesis and alternative, one uncertainty, an authorized next action, the custodian or owner, and the 09:35 review or an observable earlier trigger. A score of 2 distinguishes a request or proposal from a completed action.

**Extension:** Preserve the existing five-sentence maximum. Require three distinct verbal states in those sentences: a direct record observation, an assessment with its limitation, and a next action stated as **proposed** unless actual approval/execution is supplied. Do not imply that an approved classroom exercise is a completed production collection.

**For full credit:** The handoff names R9, R10 or R11 as appropriate, identifies unresolved B19 authorization, keeps R15's deadline uncertain and states the 09:35 review or earlier verified trigger.

#### EX023 — Impact check

**Objective:** size possible service harm without exporting unrelated patron data. **Inputs:** R9, R11, R14–R16 and the service map. **Output:** a short query request naming approver, custodian, booking identifiers or short event range, necessary fields, expected result table and privacy/access limit. The table should distinguish an audit edit, an owner-approved state and an unresolved mismatch. A score of 2 does not claim a completed count or that R14 covers the whole period.

**Extension:** Define a positive result and a negative result for the proposed booking comparison. A positive result must distinguish recorded edits from the current authoritative state; a negative result must explain how a mismatch or missing state affects the confidence of the claim. Record which patron fields remain outside scope.

**For full credit:** The learner cannot supply a measured affected-patron count from R9/R11 alone or treat R14 as complete coverage.

**Additional measurement contract for EX023:** State the unit (distinct booking ID), the selected comparison frame and why it was selected, the owner-approved target/current-state fields, and separate reported concern, recorded edit, verified mismatch and unverified comparison. A case-selected numerator is not a population prevalence estimate. As optional offline practice, use IM2 to show how repeated tickets and missing targets remain visible; never import X01–X99 into the R-series case.

#### EX024 — Escalation threshold

**Objective:** define a testable escalation rule. **Inputs:** the 09:20 case state and R15's retention notice. **Output:** two **hypothetical** observation/response pairs, each naming who verifies the new signal, why it raises harm or urgency, who decides on containment and when they reconvene. Do not claim either event happened. A score of 2 uses observable triggers rather than “if things get worse.”

#### EX025 — Correct a faulty note

**Objective:** repair unsupported attribution and scope. **Inputs:** R9, R11, R13 and R8. **Output:** a replacement of at most three sentences with one observed booking fact, one evidence limit and one next authorized check. Then underline or list the three unsupported claims removed from the faulty note. A score of 2 does not equate R8's missing destination detail with proof of no transfer either.

#### EX026 — Reproducible review

**Objective:** challenge an overconfident peer conclusion constructively. **Inputs:** R6, R9, R10 and R12. **Output:** a four-field review note: claim, directly supported facts, missing discriminator for B19, and authorized way to obtain it. Explain what outcome would change your view. A score of 2 preserves the possibility that training explains B17/B18 while leaving B19 unresolved; it does not assume the staff member is lying.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 04

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Containment, eradication and recovery decisions

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Distinguish a temporary containment action from cause removal and verified service recovery.
2. Compare two response options against harm reduction, operational cost, reversibility, authority and evidence loss.
3. Record an approval, fallback condition and next review time for a proposed intervention.
4. Explain why a completed backup job is insufficient to claim recovery readiness.
5. Define a small set of tests that would justify returning a fictional service to normal use.
6. Screen candidate copies by provenance, integrity, freshness and data correctness without confusing an isolated import time with service recovery time.
7. Test a proposed containment control against the write paths in scope, distinguishing an observed block from a quiet log or an untested path.
8. Compare competing cause hypotheses and specify an authorized test, cause-specific correction and verification limit before claiming eradication.

### 3.1 A decision loop rather than a fixed sequence

The Chapter 2 triage left `B19` unexplained and identified an audit-retention deadline. As evidence changes, the incident lead needs a repeated loop: **observe → assess possible harm → compare authorized options → act → verify effect → reassess**. Containment aims to limit further harm while the cause remains under investigation. Eradication addresses a confirmed cause or persistence mechanism when the team can identify it. Recovery restores useful service under explicit checks and monitoring. These activities can overlap, and an intervention may have to be rolled back if its cost or side effects exceed its benefit.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) treats response and recovery as part of wider cybersecurity risk management. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) addresses recovery from cybersecurity events. The classroom decision table below is a teaching model built for Harbor Library, not a universal playbook or an assertion that NIST mandates these exact steps.

#### Three independent checks for a response control

A response measure may stop a suspicious operation and still create unacceptable harm. Conversely, it may keep the service available while failing to block the concerning activity. The incident lead must not call either result unqualified success.

For the Harbor Library booking service, separate three questions before selecting a control:

**Protection:** What exact unwanted operation should the intervention prevent? A session revocation targets use of the named session; a pause targets staff writes along defined routes. Neither automatically prevents activity through all accounts, APIs, jobs or software defects.

**Legitimate service:** What approved function may the intervention interrupt? Revocation may require staff to authenticate again; a write pause may move booking requests into a manual queue. The service owner must describe the tolerable disruption and how queued work will later be reconciled.

**Verification:** What specific evidence would show that the first two expectations were met? A change ticket marked "executed" is not an effectiveness test. A quiet audit result could mean no request was attempted, the relevant source was unavailable, the query was too narrow, or the control actually prevented a change. A useful test needs a specified target, observable attempt, appropriate source coverage and independently checked business state.

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places response activities within wider cybersecurity risk-management decisions. The three-question contract here is an original teaching method, not a mandatory NIST form. It matters because containment can reduce one risk while increasing another; the record must show both.

### 3.2 The case changes

These additional records are invented. Use them with R1–R16; the timestamps are UTC and the records are the only authorized evidence for this exercise.

| ID | UTC time | Source | Observation |
|---|---|---|---|
| R17 | 09:22 | Training owner | The approved task list named `B17` and `B18` only; the owner knows of no addendum. |
| R18 | 09:24 | Booking audit | `desk-a` changed `B20` from Room 3 to Room 1. |
| R19 | 09:25 | Identity administrator | The current session can be revoked without deleting the account; staff would need to sign in again. |
| R20 | 09:27 | Service-owner export | Current states of `B17`–`B20` are available in a restricted comparison copy. |
| R21 | 09:29 | Service owner | A fifteen-minute pause on staff booking writes is tolerable if front-desk staff use a manual queue. |
| R22 | 09:32 | Booking audit summary | No edit after R18 appears within the summary's queried range. |
| R23 | 09:34 | Recovery lead | The last backup job succeeded, but the most recent documented restore test was thirty days earlier. |
| R24 | 09:36 | Privacy contact | No record currently establishes access to the newsletter list or another personal-data store. |

R17 and R18 make the authorized-training explanation for all edits less plausible and raise concern about ongoing harm. They still do not prove who controlled the session or why the edits occurred. R22 is limited to its range; R24 is a statement about the current evidence, not a finding that no exposure occurred. The lead should update confidence and urgency without converting uncertainty into an accusation.

### 3.3 Compare containment options

At 09:37 UTC, the team considers the following **hypothetical options**. No action has been taken in this text.

| Option | Potential benefit | Cost or side effect | Evidence and authorization needed | Reversal or fallback |
|---|---|---|---|---|
| Revoke the current `desk-a` session | May stop edits from that session quickly. | Legitimate front-desk work pauses until reauthentication; another session or account could remain. | Incident lead and identity owner approval under local policy; preserve narrow session and booking records first where time allows. | Reissue a verified session through approved identity process; monitor the booking audit. |
| Pause staff booking writes for fifteen minutes | Blocks edits through the staff workflow during investigation. | Staff must use the manual queue; patrons may wait. | Service-owner approval is required; R21 states tolerability but does not record approval. An operator must verify any approved pause. | Resume writes only after a checked booking state and owner sign-off. |
| Observe without intervention for ten minutes | Preserves normal service and may collect more context. | Unexplained edits could continue and harm more patrons. | Explicit lead decision accepting risk and a rapid review trigger. | Escalate immediately if another edit appears or a patron impact grows. |

The best option depends on current activity, confidence, reversibility and the service owner's tolerance. A **reasoned classroom proposal** is to ask the incident lead and identity owner to authorize session revocation, preserve the available narrow records and have the service owner ready to pause staff writes if edits continue. Another team might choose the short write pause first if the identity session cannot be linked reliably to the edits. The learner must explain the decision, authority and fallback; no fixed option is automatically correct.

#### Recommendation, approval, execution and verification receipts

A decision is auditable only when each state has its own evidence. The distinction is practical, not linguistic:

| State | Required evidence | Inappropriate upgrade |
|---|---|---|
| Proposed | Analyst's bounded option, supporting observations and expected harm reduction | Calling it approved because it sounds necessary |
| Approved | Named accountable role, target, duration, acceptable service cost and review trigger | Calling it executed because permission was granted |
| Executed | Operator's specific target, actual time, method/version and result receipt | Calling the effect verified because a command returned success |
| Verified | Independent or appropriately authoritative proof of intended protection **and** acceptable legitimate service behavior, in a declared scope | Calling all identities, paths or recovery functions safe |

At 09:37, a proposed session revocation could name `desk-a`'s *identified current session* as its target. The incident lead and identity owner are the proposed approving roles; an identity administrator would operate the change under the fictional rules. The expected protective result is denial of subsequent use of that session. The expected legitimate-service consequence is staff reauthentication. The evidence plan must include both, plus a new bounded booking audit after execution. R19 describes the capability to revoke, not a completed revocation.

For the fifteen-minute pause, R21 provides a business *tolerance statement*, not the necessary approval of the actual target and window. An authorized operator would need the service owner's explicit decision and a means of verifying which staff-write paths are blocked. The manual queue also has an owner and reconciliation obligation. R21 must not be transformed into execution, even when the team favors the pause.

A verified control result has **scope**. If one approved test shows a selected session can no longer authenticate, it does not establish that every previous token was invalidated. If one staff route rejects a write, it does not establish that a legacy route is blocked. The existing W1 fixture examines those route-specific failures independently; this expansion adds the state and acceptance logic that should surround any such test.

#### Make the comparison observable

A response option is an **intervention**, not a verdict about the cause. Compare it with the same questions you would ask of a testable claim: What should change? What might break? How will we notice both effects? Who is allowed to make and reverse the change? A short decision table is more useful than assigning unexplained numerical risk scores:

| Question at 09:37 UTC | Session revocation | Fifteen-minute staff-write pause |
|---|---|---|
| Intended effect | Prevent further edits through the identified current session | Prevent edits through the staff booking workflow |
| What it does not cover | Other active sessions, accounts or an application fault | Read-only exposure, another write path or the cause of the edits |
| Immediate service cost | Staff member must reauthenticate; work may pause | Front desk uses a manual queue and must reconcile requests |
| Evidence needed after action | Identity service confirms revocation; audit is checked for continued edits | Application shows staff writes blocked; queue and audit are checked |
| Reversal condition | A new verified session is allowed under the approved identity process | Owner approves resumption after booking-state and queue checks |

The **no-intervention option** also needs a test and a deadline. “Observe” is a decision to accept possible further booking harm for a limited period in exchange for more information. It is not a neutral default. If the team cannot detect a new edit quickly, an observation window may be less defensible than the table suggests. If the audit is incomplete, “no new edit shown” must be reported with that limitation.

Preserve the narrow records that are likely to matter before a disruptive change *when doing so does not dangerously prolong harm*. The incident lead should record which sources were captured, which could not be captured in time and why. Waiting indefinitely for a perfect evidence set could expose more patrons; acting without an evidence note can make later review harder. A proportionate decision records both costs. The comparison follows the risk-management orientation of [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final); the Harbor Library choices and matrix are original teaching examples.

#### Contained W1 lab: test whether a proposed write pause actually holds

A change ticket saying *pause enabled* records an operator's intention, not the control's effect. A quiet booking audit could mean the pause worked, no one tried to edit, the query omitted a path, or logging failed. To evaluate the proposed pause in section 3.3, define its **claim** before testing: during a bounded interval, staff-originated booking writes through both the ordinary interface and the legacy application route should be blocked, while read access and the approved manual queue remain usable. This is a service-specific classroom requirement, not a universal containment recommendation. A real team would identify all relevant routes with the service owner and test only under its change, privacy and safety rules. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) frames effective response and recovery as part of risk management; the W1 test design and pass criteria are original teaching material, not a NIST procedure.

W1 is a **separate fictional branch**. Its special card W1-A says that, for an isolated training copy only, the fictional service owner and incident lead approve a 09:40–09:55 UTC staff-write pause test with a manual queue. This approval does **not** exist in R1–R24. In particular, R21 says a pause is tolerable; it does not authorize one. W1's later timestamps and observations cannot be cited as facts available to the 09:37 canonical decision or the Chapter 4 tabletop. No learner is to submit a write to a live service, use a real account or infer a real incident outcome from these invented rows.

Before reading the outcomes, put four questions on a test sheet: (1) Did the ordinary interface reject a labeled write and leave the isolated booking value unchanged? (2) Did the legacy route do the same? (3) Was a manual request recorded for later reconciliation rather than applied to the booking state? (4) Did a read-only request still work? Use independent *before/after state* beside the response and audit label. A response string alone can disagree with the resulting state; an absent audit line is not evidence of a block. The fixture supplies one trial per route, so even a clean result would support only those paths, values and times.

**Card W1-B — isolated probe results.** The labels `W-UI`, `W-API`, `W-QUEUE` and `W-READ` are new synthetic records. `Room 2` and `Room 4` are training values unrelated to B17–B20. The queue numbers are pending-item counts, not booking-room values.

| Probe and UTC time | Route and intent | Service response | Independent state before → after | Audit label |
|---|---|---|---|---|
| `W-UI` at 09:42 | Ordinary staff interface, booking write | rejected | `Room 2` → `Room 2` | deny |
| `W-API` at 09:43 | Legacy application route, booking write | accepted | `Room 2` → `Room 4` | allow |
| `W-QUEUE` at 09:44 | Manual queue, record one request | queued | `0 pending` → `1 pending` | queue |
| `W-READ` at 09:45 | Read-only booking lookup | returned `Room 2` | `Room 2` → `Room 2` | read |

Treat each row as a **separate probe with its own reset training state**. W-API's `Room 4` does not become W-READ's starting value; the table is not a continuous production trace. The fixture intentionally makes the ordinary interface block a write while the legacy route changes a value. Therefore the broad claim *all staff writes are paused* fails under the stated W1 scope. It would be incorrect to average the two write outcomes into “50% effective”: the sample is neither random nor representative, and one demonstrated route failure is enough to reject the universal claim for this fixture. The manual queue's one pending item shows it recorded a request in this test, not that capacity, reconciliation or later service acceptance was verified.

**Reproduce a narrow classification.** The following standard-library Python program uses only in-memory invented rows. It does not connect to an application or change a file. It validates unique probe IDs and recognized kinds, then gives state change precedence over the service's claimed denial for write probes. The four status labels are *observations about this fixture*, not a production certification.

First enter the W1 fixture:

```python
PROBES = [
    ("W-UI", "write", "rejected", "Room 2", "Room 2", "deny"),
    ("W-API", "write", "accepted", "Room 2", "Room 4", "allow"),
    ("W-QUEUE", "queue", "queued", "0 pending", "1 pending", "queue"),
    ("W-READ", "read", "returned Room 2", "Room 2", "Room 2", "read"),
]
```

**Check the measurement, not just the classifier.** A `Room 2` → `Room 2` pair is useful only if both reads refer to the same training booking and an authoritative state view, with a recorded read time and a known consistency rule. A cached page could remain unchanged even after a successful write. Likewise, an audit label needs a request or event pointer and a collection cutoff; a delayed `deny` row could describe a different attempt. W1 supplies simplified independent values for the classroom method, but does not provide those production-grade provenance fields. This is why the code names one outcome `BLOCKED_IN_THIS_TEST`, rather than *blocked by the pause*.

A **pre-pause baseline** is another missing control. If the W-UI test identity lacked write permission even before 09:40, a rejection during the pause would not show that the pause caused it. An authorized isolated rehearsal could first demonstrate that the same synthetic identity and route can perform a permitted write, reset the training state, then apply the approved pause and repeat the labeled probe. The test sheet would retain both request IDs, approval, state snapshots and timing. W1 does not supply such a baseline, so do not invent one in the worked result. The W-API state change is still enough to reject the broad pause claim *within the stated W1 fixture*, assuming its supplied independent state is reliable. In a real investigation, the owners would verify that assumption before acting on the comparison.

Then run the classifier in the same scratch Python session. These two labeled listings form one program; the second uses `PROBES` from the first.

```python
def classify(kind, response, before, after, audit):
    if kind == "write":
        if before != after:
            return "WRITE_PATH_NOT_BLOCKED"
        if response == "rejected" and audit == "deny":
            return "BLOCKED_IN_THIS_TEST"
        return "INCONCLUSIVE_WRITE"
    if kind == "queue":
        if (response == "queued" and before == "0 pending"
                and after == "1 pending" and audit == "queue"):
            return "QUEUE_ITEM_RECORDED"
        return "INCONCLUSIVE_QUEUE"
    if kind == "read":
        if (response == "returned Room 2" and before == after
                and audit == "read"):
            return "READ_RETURNED_EXPECTED_VALUE"
        return "INCONCLUSIVE_READ"
    raise ValueError("unknown probe kind")


seen = set()
results = {}
for probe_id, kind, response, before, after, audit in PROBES:
    if probe_id in seen:
        raise ValueError("duplicate probe ID")
    seen.add(probe_id)
    results[probe_id] = classify(kind, response, before, after, audit)
    print(f"{probe_id}: {results[probe_id]}")

write_ids = [probe_id for probe_id, kind, *_ in PROBES if kind == "write"]
claim = "SUPPORTED_FOR_TESTED_PATHS" if all(
    results[probe_id] == "BLOCKED_IN_THIS_TEST" for probe_id in write_ids
) else "NOT_ESTABLISHED"
print(f"write_pause_claim: {claim}")
```

The final `claim` line deliberately says `SUPPORTED_FOR_TESTED_PATHS` even in a hypothetical all-blocked variant. It would still say nothing about undiscovered routes, future time windows, queue capacity or why the earlier anomalous edits occurred. In the printed W1 fixture the output is `NOT_ESTABLISHED`; the legacy-route state change is a concrete failure of the proposed write-pause claim in the isolated test. The incident lead should keep the result as a **failed validation**, ask the service owner to correct or narrow the control design, and require a new authorized test before relying on it. A manual queue may reduce service disruption, but it does not compensate for an uncontrolled write route.

**Practice submission.** Prepare (1) a four-row table of status and source fields; (2) a one-sentence containment claim with its scope and test window; (3) a decision record saying whether to rely on the pause, who must approve a change and how the manual item will be reconciled; and (4) a counterfactual W1-V in which W-UI's response remains `rejected` but its after-state becomes `Room 4`. Predict the new W-UI classification and the overall claim without changing any other field. The model output and a bounded decision appear in the final worked-results appendix. **Seven-point rubric:** one point for each of the four probe classifications, one for rejecting the broad pause claim with the W-API state evidence, one for a bounded owner-approved corrective and reconciliation plan, and one for the W1-V prediction. A 7/7 response demonstrates correct reasoning on W1, not verified containment of a real service.

### 3.4 Eradication requires a supported cause

Revoking a session is a containment action. It is **not proof** that a compromised credential, malicious browser extension, faulty training script or application bug has been removed. Before proposing eradication, the team needs to identify a cause well enough to choose a specific fix and a verification test. Examples of possible fixes include resetting a confirmed compromised credential, removing an identified malicious component, correcting a faulty application change or repairing an authorization rule. None of those causes is established in R1–R24. The case record should therefore say “cause unresolved; eradication plan pending evidence,” while continuing to check whether edits stop.

For example, suppose the session is revoked after 09:37 UTC and a **new** narrow query shows no later edits. That observation is compatible with at least three explanations: the revoked session caused the edits, the real source stopped independently, or the audit query missed later activity. R22, which was recorded at 09:32 UTC, cannot be used to verify a later revocation. Neither query can isolate a root cause. A proposed credential reset would become better supported if authorized identity evidence established credential misuse, but it would still require checking other sessions, tokens and recovery paths. A proposed application fix would require a reproducible software fault and a negative test demonstrating that the same unauthorized change no longer succeeds. The lesson is to match the **fix and its verification** to a supported mechanism.

#### From a plausible story to a falsifiable cause test

An eradication plan begins with a claim about **how** the unwanted change could occur, not with the name of a tool to run. In the fictional Harbor Library case, R17 says the training owner's listed work covered B17 and B18; R18 shows a later B20 edit associated with `desk-a`. That discrepancy deserves investigation, but the account label alone cannot identify the person, device or mechanism. R22's earlier quiet query, R23's backup-job status and R24's unattributed exposure concern do not close the causal gap. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places incident analysis, mitigation and learning within the wider response process. The following test design is CyberABC's classroom adaptation; it is not a finding about an actual service.

Write each candidate explanation so that a different observation could weaken it. A useful hypothesis record has five fields: the mechanism, current supporting evidence, a competing explanation, the least invasive authorized discriminator and a result that would change the decision. The discriminator should point to a defined source, owner, event interval and collection limit. “Look at more logs” lacks a falsifiable question. “Ask the identity custodian for session issuance and revocation events for `desk-a` around the B20 edit, with event IDs and a declared time window” can be answered or marked unavailable. Even a matching session event may identify a credential path without establishing who held the credential.

| Candidate explanation at 09:37 UTC | Supplied support and limit | Authorized discriminator to request | Result that would weaken this explanation |
|---|---|---|---|
| The `desk-a` credential or session was misused. | R18 associates the B20 edit with `desk-a`; the account label is not human attribution. | Identity owner checks bounded session issuance, token use, device association and other active sessions; compare event IDs with the application edit. | A verified edit through a different principal or a reproducible application path that does not require this session. |
| An application authorization fault allowed an out-of-scope write. | An unplanned booking change exists; no supplied test demonstrates a software fault. | Application owner reproduces the B20-type edit in an isolated copy using an explicitly unauthorized synthetic identity and records before/after state and server-side decision. | The same controlled attempt is denied with reliable state and audit evidence, while another cause has independent support. |
| Approved work, an incomplete task list or a workflow mistake explains the edit. | R17 lists B17/B18, so B20 is **not** approved by that supplied list; later authorization details are unknown. | Service owner reconciles the change ticket, task version and separately held approval record against the B20 event. | The authoritative approved scope excludes B20 and no later approved change covers it. |

These are **competing tests**, not three diagnoses. A negative check is meaningful only inside its coverage. If an identity export omits older sessions, it cannot exclude older credential use; if an isolated application test exercises only the current build, it cannot exclude a fault in the earlier build. Record the source version, query interval, filters, clock assumptions and missing fields alongside the result. If a control change has already been made, preserve relevant pre-change evidence and note that a later failed reproduction may reflect the new control rather than the original behavior. A beginner can document these limits without touching a production system.

#### Build a cause-to-fix contract

For each supported mechanism, link **evidence → authorized change → pre-change baseline → post-change test → monitoring → rollback or re-open trigger**. The arrows express a decision sequence, not proof that a change succeeds. Containment can proceed while the mechanism remains uncertain; eradication requires a supported cause and a test tied to that cause. The incident lead may keep multiple hypotheses open and seek specialist help when no safe discriminator exists.

Consider a **conditional credential-misuse branch**. If authorized identity evidence later supports use of a specific compromised session or credential, an identity owner may propose revoking relevant sessions, rotating the credential and reviewing related tokens and recovery paths. Before calling the branch effective, the owner records which sessions and token types are in scope. A controlled synthetic login with the old credential should fail, a newly authorized login should work, and a bounded identity/application audit should show the attempts with usable times and IDs. If another token type or account remains untested, the decision record says so. An empty booking-edit query alone would not prove the old credential became unusable or that no other access path remains. None of these branch observations is supplied by R1–R24.

Consider instead a **conditional application-fault branch**. If an isolated reproduction shows an unauthorized synthetic account can change a booking through a particular server route, the application owner can design a server-side authorization correction for that route and check comparable routes. Keep a record of the failing baseline on the isolated pre-change build, then repeat the *same* labeled request against the corrected build. A credible pass requires a denied response, unchanged authoritative booking state and an audit event tied to the request. Also test that an authorized synthetic account can still carry out its intended work; a fix that disables all booking writes may stop the symptom while failing the service requirement. A rollback trigger is a later unauthorized state change or material service failure during the agreed observation window. W1 in section 3.3 illustrates why route coverage matters, but it is a separate write-pause fixture and is **not** evidence that Harbor Library had this application fault.

The **workflow branch** is different. If a later authoritative record establishes that B20 was approved but missing from R17's supplied task list, the team should correct the approval-to-execution workflow and its audit trail. It should also revise the incident classification. It would be unsound to describe a credential reset as eradication of an attacker that the evidence never established. If the missing record cannot be obtained, classify this explanation as unresolved rather than treating it as confirmed benign activity.

The decision owner should sign a short **verification contract** before any cause-specific change: (1) the exact mechanism claimed; (2) the evidence IDs and their limits; (3) the system and route to change; (4) the approving and executing roles; (5) the expected positive and negative synthetic tests; (6) the audit and state evidence to retain; (7) a bounded monitoring interval; and (8) the condition that reopens the case. A post-change test that was never run is recorded as *planned*, not *passed*. If the mechanism remains uncertain, the honest status is “containment under review; eradication not established.” Recovery may still be considered under temporary safeguards, but section 3.5 requires separate service-acceptance evidence.

Rebuilds, account deletion and broad purges are high-impact actions. They may destroy evidence or create recovery problems. They need the relevant owners, scope and change controls. A beginner should avoid treating “wipe and restore” as a synonym for responsible response.

### 3.5 Verify recovery, not merely activity

The recovery lead needs more than R23's successful backup status. A restore claim should name the copy, time, environment, expected contents and test result. [NIST SP 800-34 Rev. 1, updated edition](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) discusses contingency planning and recovery priorities; this classroom example adapts that idea to a small booking service. A safe test uses an authorized isolated copy, not the live database during an unresolved event.

For Harbor Library, a proposed **return-to-service checklist** is:

1. Compare the approved booking source with R20 and identify which of `B17`–`B20` need owner-reviewed correction. Do not overwrite bookings solely from a patron report.
2. Test that authorized staff can view and create a new synthetic booking in an isolated environment, while an unauthorized test identity cannot edit one.
3. Confirm that a narrow audit query records the test change with a usable timestamp and actor label.
4. Ask the service owner to accept any remaining manual-queue entries and confirm that patrons have a consistent schedule.
5. Set a short monitoring window and an explicit rollback trigger if unexplained edits resume.

If the cause is unresolved, the lead may allow limited service with temporary safeguards and close monitoring, or may keep a restricted mode. The record must state that residual uncertainty. “The page loads” is not evidence that bookings are correct or that unauthorized edits have stopped.

#### Recovery objectives are promises to test, not facts supplied by a backup status

The service owner may define a **recovery time objective (RTO)** for how long a service can remain unavailable and a **recovery point objective (RPO)** for how far back its data can acceptably be restored. [NIST SP 800-34 Rev. 1, section 3.2](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf) distinguishes these objectives in contingency planning. CyberABC applies them here as planning questions for a fictional small service; a particular organization's definitions and approved targets must come from its own business-impact analysis.

As a **hypothetical planning exercise**, imagine the library says room booking should be usable within two hours of an interruption and no more than thirty minutes of accepted booking changes may be lost. Those are *targets*, not demonstrated performance. If the only usable copy were made at midnight and an interruption occurred at 09:45 UTC, that copy alone could omit more than nine hours of changes. It could not demonstrate a thirty-minute recovery point without another protected source or a reconciliation method. The actual R7 and R23 records do not provide a backup timestamp, a restore duration or a validated final schedule. They therefore establish neither objective. A successful restore test also needs the correct data and acceptable access controls; speed alone is insufficient.

Keep **technical restoration** and **service acceptance** separate. The recovery lead can report that a controlled copy starts and passes defined integrity checks. The service owner must still decide whether bookings are correct, manual-queue requests are reconciled and patrons can use the service with known limitations. The privacy contact reviews any newly supported exposure concern; R24 does not close that question. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) emphasizes planning, testing and improving recovery. The tests below are a classroom adaptation, not a claim that a backup, a single successful login or a quiet dashboard proves recovery.

### 3.6 Guided reconciliation and return-to-service lab

This is a **paper or local-text simulation**, with no live database, account or customer data. First choose and justify either proposed containment option from section 3.3. Then use the new exercise-only cards below. They are introduced to test recovery reasoning; they were **not** present in R1–R24 and must not be retroactively cited as evidence available to the 09:37 decision.

**Card P1 — owner-approved target state at 09:40 UTC.** For this lab, the fictional service owner confirms that the planned training changes to B17 and B18 may remain, while B19 and B20 should match the listed room assignments. This is a new fictional approval for the exercise, not an inference from R17.

| Booking | P1 approved target | C1 current restricted comparison copy |
|---|---|---|
| B17 | Room 4 | Room 4 |
| B18 | Cancelled | Cancelled |
| B19 | Room 1 | Room 3 |
| B20 | Room 3 | Room 1 |

**Card V1 — isolated-copy trial of a proposed owner-approved correction.** A synthetic staff test account can create a new test booking, and an unauthorized synthetic account is denied the same edit. The audit record for the authorized test includes a UTC time but has a blank actor identifier. These are supplied observations for the lab, not evidence that the production correction ran and not a test to run against any real service.

**Step 1 — Reconcile state.** Compare P1 and C1 row by row. List each mismatch and identify the owner who may approve a correction. Do not silently overwrite C1 or assume B17/B18 are wrong merely because they changed earlier; P1 explicitly approves their target states. Write a narrow proposed correction for mismatched bookings and a way to verify the resulting state.

**Step 2 — Test access and observability.** Use V1 to mark three claims as supported, contradicted or still untested: authorized staff can create a test booking; an unauthorized test identity cannot edit; the audit identifies the actor for every change. A successful application test does not repair missing audit attribution. Record whether full return-to-service acceptance is justified.

**Step 3 — Account for the chosen branch.** For session revocation, state that the old session's removal must be verified but cannot prove all access paths are closed. For the write pause, account for the two manual-queue requests in Branch P and obtain service-owner sign-off before resuming writes. In both cases identify one monitoring window and one observable rollback or escalation trigger.

**Step 4 — Write an acceptance record.** State what was verified, which claim failed, what remains unknown about the cause, who owns the unresolved audit defect, and the next review time. If you propose limited service despite the failed audit claim, specify the temporary compensating observation and the approving owner. “Recovery complete” is not an acceptable label while the target booking states or audit criteria remain unresolved.

**Expected evidence:** a four-row reconciliation table, a three-claim test assessment, a branch-specific queue or identity note, and a signed-off *proposal* for restricted or restored operation. **Assessment rubric:** one point each for correct mismatch identification, justified correction authority, accurate V1 interpretation, branch-specific service cost, and an honest acceptance state with an owner and review trigger. A five-point response is coherent for this lab; it is not a production recovery certificate. The worked result follows EX038 in the final answer section.

### 3.7 Contained lab: validate a recovery comparison before proposing changes

The paper comparison in section 3.6 assumes that every booking ID appears once, that the owner-approved target and the current copy use the same fields, and that the copy can be traced to a particular point in time. Those assumptions are easy to lose in a spreadsheet or an improvised script. A duplicate ID might cause one row to silently replace another in a dictionary; a missing ID might disappear from an inner join; an extra booking could be mistaken for an approved correction. This lab turns those cases into explicit **failures or review items** before anyone considers changing a booking.

The objective is to produce a deterministic **read-only diff** of the four synthetic P1 and C1 rows. Use only the Python standard library and in-memory text; the script opens no file, connects to no service and does not edit any record. P1 and C1 are released **after** the 09:37 containment decision in the simulation. Their values can inform a later recovery proposal, never the earlier decision. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) recommends planned recovery tests and improvement; the CSV schema, validation rules and output below are CyberABC's original classroom example, not a NIST procedure.

**Inputs:** two miniature CSV strings with exactly `booking_id,state` columns. The `target` string transcribes the owner-approved P1 values; `current` transcribes C1. In an actual authorized recovery, the team would record the approver, copy identifier, source time, collection method and access restriction before trusting a comparison. Those provenance fields are **not** supplied by this toy script and must not be fabricated. The state values are short fictional labels, not patron information.

**Step 1 — Read and validate.** Copy both parts of Listing 3.1, in order, into one local scratch Python 3 session you control. `parse_state` rejects a changed header, a blank or extra field, and a repeated booking ID. A failed input must stop the comparison; using the last duplicate row would make the output depend on input order. The program uses `csv.DictReader` so that the field names, not column position alone, drive interpretation.

**Step 2 — Compare without mutation.** `compare` walks the union of booking IDs. It reports `MATCH`, `MISMATCH`, `MISSING_CURRENT` or `UNEXPECTED_CURRENT`. The two latter categories are built into the method even though the ordinary four-row fixture has neither. An ID absent from C1 is not safely interpreted as “deleted” without checking whether the export filter or collection failed. An extra ID may be an unrelated legitimate booking; it must be reviewed, not overwritten automatically.

**Step 3 — Challenge the input.** The final line appends a second B20 row to the current fixture. The parser should reject it before a diff is printed for that variant. This is a deliberate malformed-input test, separate from the valid P1/C1 comparison. It demonstrates a data-quality failure rather than a new event in the Harbor Library case.

**Listing 3.1, part 1 of 2 — fixture and validated parser.** The next block completes the same program.

```python
import csv
from io import StringIO

TARGET = """booking_id,state
B17,Room 4
B18,Cancelled
B19,Room 1
B20,Room 3
"""

CURRENT = """booking_id,state
B17,Room 4
B18,Cancelled
B19,Room 3
B20,Room 1
"""


def parse_state(label, source):
    reader = csv.DictReader(StringIO(source))
    if reader.fieldnames != ["booking_id", "state"]:
        raise ValueError(f"{label}: unexpected CSV header")
    rows = {}
    for row in reader:
        if None in row or not row["booking_id"] or not row["state"]:
            raise ValueError(f"{label}: incomplete or extra field")
        booking_id = row["booking_id"].strip()
        state = row["state"].strip()
        if not booking_id or not state:
            raise ValueError(f"{label}: blank value")
        if booking_id in rows:
            raise ValueError(f"{label}: duplicate booking ID {booking_id}")
        rows[booking_id] = state
    return rows
```

**Listing 3.1, part 2 of 2 — comparison and run.** Append this block immediately after part 1 before executing.

```python

def compare(target, current):
    counts = {"MATCH": 0, "MISMATCH": 0, "MISSING_CURRENT": 0,
              "UNEXPECTED_CURRENT": 0}
    for booking_id in sorted(set(target) | set(current)):
        if booking_id not in current:
            status = "MISSING_CURRENT"
        elif booking_id not in target:
            status = "UNEXPECTED_CURRENT"
        elif current[booking_id] == target[booking_id]:
            status = "MATCH"
        else:
            status = "MISMATCH"
        counts[status] += 1
        print(f"{booking_id}: {status} target={target.get(booking_id, '-')}",
              f"current={current.get(booking_id, '-')}")
    print("counts:", ", ".join(f"{name}={count}" for name, count in counts.items()))


target = parse_state("target", TARGET)
current = parse_state("current", CURRENT)
compare(target, current)
try:
    parse_state("current", CURRENT + "B20,Room 1\n")
except ValueError as error:
    print("rejected variant:", error)
```

**Expected evidence:** four printed booking statuses, a count summary with two matches and two mismatches, and a separate rejected-duplicate message. Save the output as a classroom note along with the program text; record whether it was run and in which local Python version. The worked output appears in the final answer section. The B19/B20 differences are **proposed correction candidates**, not permission to edit. The service owner must confirm P1's authority and approve a bounded correction; an operator would then act in an authorized environment and a reviewer would compare a **new** state copy. C1 is only one point-in-time snapshot. A matching diff after a later correction would still need access and audit checks, including the failed actor field in V1.

**Assessment:** award one point each for (1) rejecting a duplicate instead of silently choosing a row, (2) identifying B19/B20 as mismatches while retaining B17/B18 as matches, (3) distinguishing missing and unexpected IDs in the method, (4) recording that target approval and copy provenance are external to the script, and (5) proposing an authorized, newly verified correction without claiming it occurred. A passing 5/5 demonstrates sound use of this small comparison, not recovery of a real service. If Python is unavailable, trace the four iterations and duplicate check on paper; the expected statuses and limits are the same.

### 3.8 Guided backup-candidate and isolated-restore lab

Section 3.5 introduced recovery objectives; section 3.6 compared booking states; section 3.7 checked whether the comparison itself silently discarded rows. A recovery lead must join those three kinds of evidence before proposing a return to service. The most recent copy can contain the very error being investigated. An older copy can appear correct for the four displayed bookings while omitting legitimate work. A valid checksum can show that a particular copy matches a recorded digest without showing that its source was trustworthy or that its contents meet the service owner's target. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) provides recovery-planning and testing guidance; the three-candidate gate below is an original, deliberately small classroom method.

This is an **optional exercise-only replay**, introduced after P1/C1 and V1. It does not add an event to R1–R24, does not describe a real Harbor Library backup, and cannot be used to revise the 09:37 containment choice. In this replay, imagine a service interruption at **09:45 UTC** and a candidate review at **09:46 UTC**. The service owner's illustrative targets from section 3.5 are a thirty-minute RPO and a two-hour RTO. Neither target was established by R7 or R23. The candidate descriptions below are supplied solely so a learner can practice deciding what still needs verification. The exercise assumes an approved isolated environment and permission to inspect only synthetic booking IDs; it authorizes no production restore.

**Card K1 — three proposed comparison copies.** A snapshot timestamp is the claimed data point. An isolated import duration is a measured *classroom trial*, not the duration of restoring the production service. The checksum comparison is against a digest recorded with that same candidate; the exercise does not establish independent authenticity of the digest or the snapshot source.

| Candidate | Claimed snapshot time | Trial evidence supplied in K1 | Four-booking observation in isolated copy |
|---|---|---|---|
| `K-A` | 09:00 UTC | Recorded digest matches the inspected bytes; isolated import and four-row read took 14 minutes. | B17/B18 match P1; B19 is Room 1 and B20 is Room 3. No statement is supplied about other bookings or changes after 09:00. |
| `K-B` | 09:20 UTC | The inspected bytes differ from the recorded digest; no import was attempted. | No reliable state comparison is available from this candidate. |
| `K-C` | 09:38 UTC | Recorded digest matches the inspected bytes; isolated import and four-row read took 11 minutes. | B17/B18 match P1; B19 is Room 3 and B20 is Room 1, as in C1. |

The data-point ages relative to the hypothetical 09:45 interruption are **45, 25 and 7 minutes** respectively. The thirty-minute RPO would screen out K-A *as a stand-alone copy* if there were no verified way to recover legitimate changes after 09:00. K-B is within the time target, but its digest mismatch is a **stop-and-investigate** result: a responder cannot replace the recorded digest with one from the observed bytes and call the copy verified. K-C is fresh enough by the timestamp alone, yet its B19/B20 state conflicts with the later owner-approved P1 target. The matching digest does not cure that logical error. These observations do not prove that K-A is clean throughout, that K-B is malicious, or that K-C is unusable for every limited purpose.

#### Four separate gates before a restore proposal

1. **Provenance and permission.** Identify the snapshot identifier, originating system, claimed creation time and clock basis, capture method, recorded digest, custody of the copy, allowed test environment and owner who approved the test. K1 omits most of these details. A custodian should supply them in an actual case; a learner should leave the fields open rather than infer them from the candidate label. Preserve the original candidate and test a controlled working copy.
2. **Copy integrity and usability.** Compare bytes with the previously recorded digest, then attempt a bounded isolated import with error logging and a repeatable test. A match supports only a limited byte-integrity claim; a successful import shows that the tested platform read the copy under the trial conditions. K-B fails the first check and has no second check. Neither K-A's nor K-C's successful import proves that the complete database, dependencies or access controls work.
3. **Data correctness and loss.** Compare the isolated booking state with an owner-approved target and account for legitimate transactions between the snapshot and interruption. P1 approves only B17–B20. K-A matches those four rows but may lack later legitimate bookings; K-C contains the known B19/B20 mismatches. A real reconciliation needs a source for intervening work, its provenance, a conflict rule, and an owner who accepts any unrecoverable gap. If that evidence does not exist, the team reports an **unknown loss bound**, not “zero loss.”
4. **Service acceptance and control.** In a safe test scope, verify authorized and unauthorized actions, actor-labelled audit records, manual-queue reconciliation, dependencies, user-facing behavior and a monitoring/rollback condition. V1 supplies two limited access observations and one failed audit-attribution observation. It does not become a pass because a different copy imported quickly. The service owner and incident lead must decide whether restricted operation with a documented compensating check is acceptable; a full-return claim requires the failed control and other acceptance criteria to be resolved.

These gates can fail independently. A candidate can pass an integrity check and fail the owner's data comparison; another can match four rows and fail freshness; a third can be fresh but have an unverified copy. Writing one label such as “good backup” hides the decision. Use `PASS`, `FAIL` or `UNKNOWN` **per gate**, with the supplied observation beside it. `UNKNOWN` is not an implied pass. Where a source cannot be trusted, the correct next step is to seek a more reliable copy or independent corroboration, not to force the matrix to a single winner.

#### An RPO calculation is only a screening calculation

For this replay, subtract the claimed snapshot time from 09:45: K-A is 45 minutes old; K-B is 25 minutes; K-C is 7 minutes. That arithmetic tests the *age of the stated recovery point*. It does not measure the number of valid bookings lost, the effect of a write queue, whether a snapshot is internally consistent, or how far a restored application would lag once other dependencies are rebuilt. If the clock or source metadata is wrong, even the age calculation is only conditional. An RPO pass needs an acceptable recovered data point under the service owner's rules, not merely a recent filename.

Likewise, **11 or 14 minutes of isolated import** is not an RTO result. The two-hour target concerns usable service after the interruption. A meaningful elapsed time would need a defined start and stop, a tested platform, data and access checks, downstream dependencies, and an acceptance decision. In this fixture, no production restart or owner acceptance occurred. Record the isolated times as component measurements and leave the service-level recovery time **unmeasured**. This avoids an attractive but invalid equation: `import duration = outage duration`.

#### Practice: write a candidate decision card

Create a four-row gate matrix for each candidate, using the gate names above. For each row, state one K1/P1/V1 observation and the reason the result is `PASS`, `FAIL` or `UNKNOWN`. Then write a six-line recommendation: (1) the 09:46 review time and status as *proposal*; (2) whether any candidate independently supports both data-point and correctness claims; (3) which copy, if any, merits a further isolated trial and under whose approval; (4) what records are needed to reconstruct legitimate changes after its snapshot; (5) how the failed V1 actor field and unresolved cause affect acceptance; and (6) the next review trigger and named owner. Do not combine K1 with the canonical case history as though these candidate tests had actually happened.

For a variation, imagine that the only independent transaction journal also contains a gap from 09:10 to 09:18 UTC. Explain why a “replay all missing transactions” plan is no longer verified. Identify the narrowest additional source or service-owner decision that could bound the missing interval. This inject belongs to the exercise only. Removing it returns you to the K1 facts; do not add it to R1–R24 or assert a real journal gap.

**Expected submission:** three candidate matrices, the six-line decision card and a two-sentence variation response. **Assessment rubric (six points):** one point each for correct age arithmetic; treating K-B's mismatch as a failed integrity gate; distinguishing K-A's four-row match from complete or timely recovery; identifying K-C's B19/B20 conflict; keeping isolated import time separate from RTO and V1's audit failure open; and proposing an authorized, reviewable next test without claiming a completed production restore. A 6/6 answer is coherent for this fixture only. The model result follows the Chapter 3 source-reading answer in the final appendix.

#### Return to service is a separate decision

A team can reduce further edits while leaving the service unusable or its booking data wrong. Equally, a restored interface may allow unauthorized changes or fail to produce an attributable audit. The return-to-service owner therefore needs a **paired gate**: acceptable protective behavior and acceptable legitimate business behavior, plus correct state and sufficient observability. A failed mandatory gate means the full acceptance claim is blocked.

Rollback is not simply "reverse the command." It needs a named owner, scope, the state or configuration to restore, the treatment of queued work, and tests for both renewed user service and restored security. If a broad pause must remain temporarily, the service owner should record how manual requests are received, protected from duplicates, later reconciled and reviewed. A risk exception is explicit, time-bounded and approved; it must not be hidden under the label "recovered."

The last exercise of the chapter should therefore leave four distinct artifacts: a response decision with approval state, a causal hypothesis and falsifier, an isolated recovery test request with gate results, and an owner-reviewed service acceptance decision. No one artifact alone proves the others.

### 3.9 Sourced case study: recovery beyond the backup copy

Harbor Library is invented. A useful real-world contrast is the [British Library's own March 2024 review of the October 2023 cyber-attack](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=). The report is the institution's retrospective account, written after investigation; it is **not** a raw event log, a finding about Harbor Library or a template for a one-month course to reproduce. Its exact descriptions are time-bound to the review date. Read the cited pages when using the case and avoid extending the report's conclusions to unexamined systems.

The review reports that attackers encrypted or destroyed a substantial part of the Library's server estate and that the institution had secure copies of its digital collections, yet lacked viable infrastructure on which to restore services promptly (executive summary, pp. 2–3). By December 2023, viable backup sources had been identified for collections and other data, but the report still describes restricted research services and systems needing modification, migration or replacement (pp. 2–3 and 9). A searchable catalogue returned on 15 January 2024 while other functions remained incomplete (pp. 2 and 9–10). These are **reported facts about the British Library**, not evidence about the fictional bookings B17–B20. The teaching inference is that **copy availability, platform readiness, data validation and service acceptance are different checkpoints**. A backup can exist while the environment needed to use it is missing or unsafe.

The same report describes strategic and operational crisis groups coordinating technical response, approving workarounds and communicating during disrupted website and intranet service (section 3, pp. 12–13). This supports a second teaching inference: response records must name decision owners and alternate communications paths, because a status page or ordinary internal channel may itself be unavailable. The British Library's roles and governance are specific to that institution; the incident-lead/service-owner matrix in this course is a **fictional teaching arrangement**, not a claim that the real Library used it.

| Source-based statement | What a learner may infer for recovery planning | What the source does **not** establish for this course |
|---|---|---|
| The British Library reported secure digital-collection copies but damaged restoration infrastructure. | Test both the copy **and** the ability to restore it onto an acceptable platform. | It does not give Harbor Library a usable backup, a measured restore time or an approved P1 booking target. |
| A searchable catalogue returned while other services remained restricted. | Define acceptance separately for each user-facing service; a partial return can be useful and still be incomplete. | It does not prove that a searchable page means all data and access controls are correct. |
| Crisis groups coordinated workarounds and communications. | Record who can authorize a temporary manual process and how staff and users will be updated. | It does not authorize a learner to pause a real booking service or contact real users. |

**Guided source-reading activity:** write a three-row claim ledger with (1) a fact from the British Library report and its page or section, (2) one planning question it raises for the fictional booking service, and (3) one conclusion it cannot support about B17–B20. Include at least one row about restoration infrastructure and one about partial service. Then compare the source date with the time of your own course reading: a 2024 retrospective cannot by itself tell you the Library's current service state. The report also expresses uncertainty about the exact initial intrusion point; do not turn a likely entry point into a certain one. A model ledger appears in the final answer section. This supplementary source analysis is separate from EX027–EX038.

#### Contrast: a decision record at 09:37

**Plausible but incorrect:** "At 09:37 we know B20 was an attack. R21 authorizes a write pause, R22 proves the writes have stopped, and R23 proves recovery is ready. Apply the pause and close the incident after the page loads."

Each asserted upgrade is wrong. R18 reports a B20 change but no human attacker or causal mechanism. R21 says a pause is tolerable, not approved or executed. R22 is a narrow earlier query, not a post-change verification. R23 is a backup/old restore-test status, not a current service-acceptance result. A loading page is not evidence of booking correctness or auditability.

**Defensible 09:37 proposal:** "R17 limits the known approved task list to B17/B18 and R18 reports a further B20 edit under `desk-a`. The incident lead proposes a bounded current-session revocation, subject to identity-owner approval and preservation of feasible narrow sources. The identity administrator will verify execution if approved; the application and service owners will separately assess later edits and front-desk continuity. R21 supports discussing a short manual-queue fallback but gives no execution authority. Root cause, recovery readiness and personal-data exposure remain unresolved; reassess at the named next review or on a verified continuing edit."

This record does not avoid action. It prevents recommendation, approval, execution and success from becoming a single unsupported sentence.

### 3.10 Worked decision record and synthesis

Audit the defensible 09:37 proposal above as four separate receipts. This prevents a well-worded recommendation from being mistaken for a change that happened:

| State | What the supplied case supports | What a later reviewer would need |
|---|---|---|
| Proposed | R17–R18 justify asking to revoke the identified current `desk-a` session. R21 makes a short staff-write pause a possible fallback with a known service cost. | A named decision owner, exact session or write routes, review time and a plan for the manual queue or staff reauthentication. |
| Approved | No R1–R24 record approves either action at 09:37. Tolerating a pause is not authorizing it. | A separately recorded incident-lead and relevant identity- or service-owner approval for the chosen target and interval. |
| Executed | No R1–R24 record states that a session was revoked or staff writes were paused. | Operator receipt with actual target, time, method and any failed or partial steps. |
| Verified | R22 predates the proposal, and its query bounds are incomplete. It cannot show that a later change worked. | A post-action protective test tied to the selected target, a separate check of legitimate booking service, reliable source coverage and a defined failure trigger. |

The proposal should set a 09:45 review or earlier review on a verified new unexplained edit. Root cause and personal-data exposure remain unresolved; the four rows do not claim a production action.

This chapter converts the earlier timeline into a bounded decision. Chapter 4 will test the whole response: intake, evidence, authority, proportionate action, recovery criteria and a review of what the team would change before another incident.

<a id="ir-rapid-ch03-g3-lab"></a>

### 3.11 Offline laboratory: decision and recovery gates

**Purpose:** Validate the logical separation of proposal, approval, execution, protective verification, legitimate service continuity, data correctness and audit attribution. This is a *new independent classroom branch*, not a replay of W1 write-path tests, the P1/C1 booking-value comparison, V1's specific observations or K1 copy selection.

**Environment:** Python 3 standard library; data only in memory. No network, files, credentials or system changes. Every G3 row is a separate reset scenario, not a chronological incident timeline.

**Inputs and meanings:** A value of `True` means the corresponding *fictional test card asserts* that a gate passed in its limited scope; `False` means the card asserts a failed gate; `None` means no test result is supplied. The flags are **not real approval receipts, collection evidence or actual restorations**. `protective` concerns the bounded harmful operation, `legitimate` the required legitimate business function, `data` an isolated owner-approved data check and `audit` sufficient attribution for the tested operation. The model intentionally requires all four for its most favorable limited label.

#### Executable fixture

~~~python
SCENARIOS = [
    ("G3-P", False, False, None, None, None, None),
    ("G3-A", True, False, None, None, None, None),
    ("G3-E", True, True, None, None, None, None),
    ("G3-C", True, True, False, True, True, True),
    ("G3-B", True, True, True, False, True, True),
    ("G3-I", True, True, True, True, None, None),
    ("G3-D", True, True, True, True, False, True),
    ("G3-U", True, True, True, True, True, False),
    ("G3-V", True, True, True, True, True, True),
    ("G3-X", False, True, True, True, True, True),
]

def gate(approved, executed, protective, legitimate, data, audit):
    if executed and not approved:
        return "INVALID_UNAPPROVED_EXECUTION"
    if not approved:
        return "PROPOSED_ONLY"
    if not executed:
        return "APPROVED_NOT_EXECUTED"
    if protective is None or legitimate is None:
        return "EXECUTED_UNVERIFIED"
    if not protective:
        return "PROTECTION_GATE_FAIL"
    if not legitimate:
        return "BUSINESS_GATE_FAIL"
    if data is None or audit is None:
        return "RECOVERY_CHECKS_PENDING"
    if not data:
        return "DATA_GATE_FAIL"
    if not audit:
        return "AUDIT_GATE_FAIL"
    return "BOUNDED_TEST_GATES_PASS"

for ident, *fields in SCENARIOS:
    print(ident, gate(*fields))

# Negative control: invalidate attribution for the favorable test card.
print(
    "NEGATIVE_AUDIT",
    gate(True, True, True, True, True, False),
)
~~~

#### Exact expected output — executed against the displayed fixture

~~~text
G3-P PROPOSED_ONLY
G3-A APPROVED_NOT_EXECUTED
G3-E EXECUTED_UNVERIFIED
G3-C PROTECTION_GATE_FAIL
G3-B BUSINESS_GATE_FAIL
G3-I RECOVERY_CHECKS_PENDING
G3-D DATA_GATE_FAIL
G3-U AUDIT_GATE_FAIL
G3-V BOUNDED_TEST_GATES_PASS
G3-X INVALID_UNAPPROVED_EXECUTION
NEGATIVE_AUDIT AUDIT_GATE_FAIL
~~~

#### Interpretation and negative control

G3-P records only a proposal. G3-A adds a fictional approval but no execution. G3-E claims execution while omitting effectiveness checks; it cannot be described as successful containment. G3-C and G3-B show why the protective and legitimate-service tests are independently necessary. G3-I has both of those bounded passes but no recovery-data or audit result. G3-D fails data correctness. G3-U fails audit attribution. G3-V passes the **declared classroom gates for that one modeled test**, but does not establish root cause, complete route coverage, production authorization or service-owner acceptance. G3-X contains an internally unacceptable claim of execution without approval and is rejected even when all other flags are true.

The negative control changes only the audit flag of the favorable test to `False`. The output becomes `AUDIT_GATE_FAIL`: a missing or failed mandatory attribution check blocks the limited acceptance label even when protection, legitimate service and data appear satisfactory.

**Important algorithmic limit:** This code is a decision-logic demonstration, not an evidence authentication engine. Setting `approved=True` does not supply a real signed approval; setting `executed=True` does not produce an operator receipt. All gates would need independent, scope-appropriate evidence in a real authorized operation. The program also does not estimate probabilities or verify that all paths were tested.

**Learner artifact:** Before running, predict all eleven lines. Afterward, provide a three-column table `scenario | returned state | missing or failed evidence`. Add one sentence explaining why G3-V does not mean "recovery complete," and another showing how G3-D might require a new isolated copy or owner-approved reconciliation rather than an unconditional return. Keep G3 cards outside canonical R1–R24 and the later chapter branches.

**Acceptance rubric (five-point lab, supplementary rather than a new numbered exercise):** one point each for exact output; correct lifecycle separation; independent protective and service gates; distinct data and audit failure interpretation; and an explicit bounded-evidence/canonical-release limitation. Do not claim the classroom `True` inputs were verified production observations.

### Chapter 3 exercises

Use the synthetic case only. R1–R24 are available for all twelve exercises; P1/C1 and V1 are available only where an exercise explicitly calls for the Chapter 3 recovery lab. The Chapter 4 branches are **not** evidence at the 09:37 decision point. R17's 09:22 task list names B17/B18 only; the later B20 edit in R18 is evaluated against that already supplied list, not known to the training owner in advance. For each response, first name its record IDs and decision time; then separate observed fact from inference or proposal; finally name an authorized owner, an observable check and a limit. Submit the requested matrix, note or test plan so a reader can reproduce the reasoning from this book alone. The worked results at the end provide examples, while alternative choices pass when their assumptions and verification are explicit.

Use a compact 0–2 check per exercise: **0** if the requested artifact is missing or asserts an unsupported fact, **1** if the artifact answers the question but omits evidence, authority or an important limit, and **2** if it is evidence-linked, bounded and testable. This is a practice rubric for the draft, not a formal grade. Where a question names several fields, all are required for a 2. A claim of executed action before the branch card or of complete recovery after a failed V1 audit check must be revised even if other fields are present.

#### EX027 — Three different goals

**Objective:** distinguish a control action from a cause fix and a service test. **Inputs:** R17–R23 and sections 3.3–3.5 at 09:37 UTC. **Output:** a three-row table for proposed session revocation, credential reset and isolated restore test, with primary goal, prerequisite authority or evidence, observable success check, and one important limit. Do not claim that any of these actions has occurred. A score of 2 identifies the credential reset as only a *candidate* eradication action if credential compromise is supported, and keeps a test of a copy distinct from live-service acceptance.

#### EX028 — Changed assessment

**Objective:** update hypotheses without rewriting the earlier decision. **Inputs:** R9, R10, R12 and R17–R18. **Output:** a before/after 09:37 assessment note with the earlier unresolved B19 issue, what R17 adds about approved tasks, what R18 adds about B20, the hypothesis weakened, the concern strengthened, and a fact that remains unproved. Record event and availability times separately. A score of 2 does not claim the learner knew R17–R18 at the 09:20 Chapter 2 review or identify the human behind `desk-a`.

#### EX029 — Decision matrix

**Objective:** select a bounded containment proposal. **Inputs:** R18–R21 and the section 3.3 comparison. **Output:** a two-row matrix for session revocation and the fifteen-minute staff-write pause, each with intended effect, path it does not cover, operational cost, approving role, executing role, post-action check and rollback. Add one sentence choosing an option provisionally at 09:37. A score of 2 names R21 as tolerance for a pause, **not** proof that a pause was approved and executed, and verifies the service cost as well as the intended block.

#### EX030 — Risk of observation

**Objective:** make non-intervention an explicit, reviewable choice. **Inputs:** R18, R21–R22 and the 09:37 checkpoint. **Output:** an observation decision card with approver, ten-minute deadline, proposed audit source and interval, query-coverage limit, verified trigger for early intervention, and accepted harm if another edit occurs. State what happens if logging is unavailable or the query is incomplete. A score of 2 does not treat R22's earlier narrow zero result as evidence that the next ten minutes will be quiet.

#### EX031 — Evidence before change

**Objective:** preserve enough context without turning preservation into a reason for unbounded delay. **Inputs:** R13, R17–R20 and R15's retention notice. **Output:** a four-row preservation request naming the source/item, bounded purpose, custodian or approval, and what the item cannot establish. Add a decision rule for when verified ongoing harm justifies an approved containment action before all four requests finish; record any omitted item and reason. A score of 2 calls the records **requests or supplied summaries** unless a new collection actually occurred and avoids bulk patron-data copying.

#### EX032 — Avoid premature eradication

**Objective:** repair an unsupported closure claim by making two causes testable. **Inputs:** R17–R24 and sections 3.3–3.4. **Output:** (1) a three-sentence correction stating what a *proposed* session revocation is intended to contain, which actor/cause/path questions remain, and why eradication is not established; (2) a two-row hypothesis card for credential/session misuse and an application authorization fault, each with supplied support, an authorized discriminator, a result that would weaken it and a conditional fix-verification pair; and (3) one sentence explaining why R22, recorded before 09:37, cannot verify the later proposal. Keep planned tests separate from supplied observations. A score of 2 names at least one positive and one negative synthetic test for a proposed fix, plus a scope or provenance limit; it does not assert that revocation, root-cause testing or a fix happened.

#### EX033 — Recovery test

**Objective:** distinguish restoration planning from a measured result. **Inputs:** R23 and, **after the later lab card is released**, P1; V1 remains a separate access-and-audit trial. **Output:** a one-paragraph isolated-copy test plan plus a four-row B17–B20 expected-state table. Name the copy identifier and timestamp as fields to collect, actual restore start/end as fields to measure, service-owner-approved target, pass/fail/not-tested rule, and privacy boundary. A score of 2 keeps all four rows *not tested* until the restore is performed and never changes a live booking.

#### EX034 — Backup limit

**Objective:** test what a successful backup job can and cannot demonstrate. **Inputs:** R23 and the **hypothetical** two-hour RTO, thirty-minute RPO, midnight-only copy and 09:45 interruption in section 3.5. **Output:** a calculation note with `09:45 − 00:00`, comparison to the thirty-minute target, the missing timing measurement for RTO, and two additional authorized checks before calling the service recoverable. Do **not** assert that the fictional library approved those targets or that the actual backup was made at midnight. A score of 2 shows the arithmetic, separates copy age from actual data-loss measurement and identifies booking-state and elapsed-restore tests.

#### EX035 — Return-to-service criteria

**Objective:** require evidence for a proposed return to service. **Inputs:** P1/C1 and V1 **only after their later release**, plus the section 3.5 checklist. **Output:** three measurable acceptance rows for booking correctness, tested access behavior and audit attribution, each with expected result, current supplied result, owner and action needed. Conclude with a proposed service state, next review and one rollback trigger. A score of 2 marks B19/B20 as mismatched in C1, V1's tested access checks as limited passes, and the blank audit actor as a failure, so it does not declare unrestricted recovery.

#### EX036 — Decision record

**Objective:** keep a response recommendation auditable before execution. **Inputs:** R17–R21 and the 09:37 checkpoint. **Output:** a six-field card covering time and status, evidence and uncertainty, chosen action and scope, approvers/executor, intended effect plus service side effect, and verification/fallback/review. Name the identity owner and incident lead for the proposed revocation; use R21 only for a possible pause fallback. A score of 2 gives an observable post-action test and says **proposed**, not completed.

#### EX037 — Residual risk

**Objective:** distinguish page availability from safe, correct service. **Inputs:** R20, R22–R24 and a **hypothetical** observation that the page loads after an approved revocation; this is not the Chapter 4 branch result. **Output:** a claim/limit note with two unresolved questions, a test and owner for each, and a proposed case status. A score of 2 asks about booking correctness and adequate post-action audit coverage, and does not use R24 to claim that no personal-data access occurred.

#### EX038 — Alternative defensible choice

**Objective:** defend a different containment path without inventing a unique right answer. **Inputs:** R18–R21 and the section 3.3 matrix. **Output:** a pause-first proposal with two assumptions, approving role, manual-queue plan, one immediate effectiveness check, a 15-minute review time and a condition for changing to narrower session action or a longer restriction. A score of 2 states that R21 records tolerance rather than execution, and includes reconciliation and service-owner sign-off before resuming writes.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 04

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Guided incident simulation and after-action review

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Run a contained response exercise from initial alert through an owner-approved service decision.
2. Produce a case record that separates observations, hypotheses, approvals, actions and results.
3. Test a return-to-service claim against explicit evidence instead of accepting a dashboard status.
4. Give a short, accurate internal update that protects people from premature attribution.
5. Identify a process gap, assign an owner and define a measurable improvement check.
6. Draft audience-specific, versioned status messages that separate operational coordination from an unverified exposure report and any formal notification decision.
7. Calibrate a tabletop score against frozen artifacts, resolve reviewer disagreement with evidence and propose a revision without changing the earlier decision record.

### 4.1 Exercise purpose and boundaries

This is a **tabletop simulation**, not an instruction to touch a real account. It uses the fictional Harbor Library records in Chapters 1–3. Learners may write notes, compare options and role-play approvals. They may not contact a real library or use a production system. A solo learner can fill every role; a group should assign an incident lead, analyst, service owner, recovery lead and communications contact. Each role must identify what it can decide and what needs another owner's approval.

[NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) describes designing, conducting and evaluating IT plan exercises. This course uses that general idea to evaluate reasoning and coordination. The exercise does not test actual organizational readiness, because the people, data, systems and consequences are invented.

**Inputs:** R1–R24, the service map, a case-note template from Chapter 1, the decision/collection fields from Chapters 2–3, and the Chapter 3 P1/C1 and V1 cards when the facilitator releases them. **Timebox:** four rounds of ten to fifteen minutes, then a twenty-minute review. **Outputs:** one case timeline, one hypothesis table, one approved-action record, one recovery test plan, one internal status message and one improvement ticket. Each output may fit on one page; completeness and reasoning matter more than length.

### 4.2 Release the injects in order

| Round | Facilitator reveals | Learner decision | Evidence to retain |
|---|---|---|---|
| A — readiness and intake | R1–R8 and a patron ticket | Identify service owner, authorized scope, observations and first questions. | Case ID, raw record IDs, UTC timeline and uncertainty. |
| B — triage | R9–R16 and the 24-hour retention notice | Update hypotheses, priority and preservation request. | Supporting and contradicting records, collector, authority and deadline. |
| C — response | R17–R24 and the owner's fifteen-minute write-pause tolerance | Compare at least two containment options; obtain a fictional approval and set a review time. | Decision owner, expected effects, side effects, fallback and verification. |
| D — recovery branch | The branch card below, then P1/C1 and V1 from Chapter 3 | Test whether booking state and audit coverage justify limited service or further restriction. | Test result, residual uncertainty, service-owner decision and monitoring trigger. |

The facilitator should not reveal later records early. In a solo session, cover the later rows until each round is complete. If a learner chooses a different defensible action than the worked example, continue with the corresponding branch and state the assumptions rather than forcing the reference answer.

**Branch S: session revocation.** At 09:45 UTC, the identity administrator reports that the current `desk-a` session was revoked under the fictional incident lead's approval. A narrow booking query shows no later edits in its queried range. The staff member must sign in again. `B19` still shows an incorrect room until an owner-approved correction is made. This branch does not establish who used the prior session or that another access path is absent.

**Branch P: staff-write pause.** At 09:45 UTC, the service owner reports that staff writes were paused for fifteen minutes under the fictional approval. The manual queue has two pending booking requests. The booking audit shows no writes in the pause interval, but the cause of `B19` and `B20` remains unresolved. This branch does not prove the account is safe when writes resume.

For either branch, R23 still says the last documented restore test was thirty days earlier. After discussing the branch result, reveal P1/C1 and then V1 as **later exercise cards**. P1/C1 shows two booking mismatches that require owner-reviewed correction; V1's isolated-copy test supports the two tested access claims but fails actor attribution in the test audit. Neither card proves that production corrections ran. The recovery lead should propose an isolated check of the booking state and a narrow audit check before declaring normal service. The privacy contact should review any new evidence of personal-data access; R24 alone is not clearance.

### 4.3 Worked tabletop: one acceptable path

**Round A.** The learner opens `HL-IR-001`, notes that R1 precedes booking edits, names the service owner as pending, records compromise as a hypothesis and asks whether the edits were training work. **Round B.** R9–R16 add an unexplained `B19` edit and a retention deadline. The fictional lead approves preserving the narrow audit copy and sets a 09:35 review. **Round C.** R17–R18 add an unplanned `B20` edit. The lead and identity owner approve session revocation after the available records are noted; the service owner stands by for a short write pause if edits continue. **Round D.** Branch S reports the revocation and no later edits in a limited query. P1/C1 then reveals that B19 and B20 are still inconsistent with the approved target. V1's isolated-copy trial has a blank audit actor field. The learner requests owner-approved correction, a bounded restore test and audit remediation, keeps the cause unresolved, and proposes restricted or explicitly approved limited operation with monitoring rather than closing the case.

This is one acceptable path. A team that prefers Branch P can pass if it explains the service cost, establishes approval, plans for the two queued requests and states how it will decide when writes may resume. In either path the later P1/C1 and V1 cards prevent an unsupported “fully recovered” conclusion. The exercise assesses **decision quality under incomplete information**, not agreement with a preselected action.

### 4.4 Run a reproducible handoff drill

The facilitator or solo learner should keep a **release ledger** with three columns: time the fictional event occurred, time the learner received the card and the round in which the card became usable. For example, R9 describes an edit at 09:03 UTC but enters the learner's evidence set only in Round B; P1 describes an owner target at 09:40 and belongs to Round D, after the 09:37 containment proposal. This prevents a polished final answer from quietly using later evidence to justify an earlier decision. The ledger can be written in Markdown alongside the case note and should retain the original record IDs.

At each round, freeze a one-paragraph **state snapshot** before revealing the next card. It should contain (a) what is observed, (b) the current leading and alternative hypotheses, (c) a proposed action or reason to wait, (d) the owner whose approval is required, and (e) a time or event that will trigger review. A learner may revise a hypothesis as new records appear but should leave the earlier snapshot visible. Revisions show how the decision changed; replacing earlier text with hindsight hides a real response skill.

At Round D, write a **claim ledger** before an internal update. A sample for Branch S is:

| Claim | Supplied support | Limit or contradiction | Decision consequence |
|---|---|---|---|
| The selected session was revoked | Branch S identity-owner report | Other sessions and paths are untested | Keep identity scope open and monitor for fresh edits |
| The booking schedule matches the approved target | P1 defines target; C1 gives current state | B19 and B20 differ; no production correction result is supplied | Service owner must approve and verify each correction |
| A test staff role can create a booking | V1 isolated-copy result | It tests one synthetic role, not the live production path | Treat as a bounded positive test only |
| The test audit identifies the actor | V1 includes a timestamp | Actor field is blank, so the claim fails | Assign an audit owner; do not claim full observability |
| The service met a recovery time or point target | R23 reports backup-job success | No completed restore, duration, source timestamp or approved target is supplied | Keep the recovery objective unverified |

This ledger separates **supported**, **contradicted** and **untested** claims. “No later edit appeared” is supported only for the branch's queried range. A missing actor field is an observed failed criterion, not simply an unknown. Those two states call for different follow-ups: broaden an authorized query for the former, repair and retest the audit for the latter.

The handoff must reach a person who was not in the tabletop. Give that person the case ID, last evidence snapshot, chosen branch, approvers, action actually reported by the branch card, checks that passed or failed, access location for the restricted synthetic artifacts, owner of each open item and the next checkpoint. The receiver should be able to answer, without guessing, whether staff writes are currently paused and who may change that status. If a real handoff omitted those two facts, it could cause both unnecessary outage and an unsafe restart.

**Failure inject for review, not for the live round:** suppose a team reports “all bookings correct” after seeing only the V1 access test. Ask which supplied card tests that sentence. V1 does not compare booking states; C1 contradicts the sentence for B19 and B20. A defensible revision is: “The isolated-copy access checks passed, while B19 and B20 remain pending owner-approved correction and the audit actor field failed its test.” This exercise in claim repair is as important as selecting the initial containment action.

### 4.5 Score the evidence and the handoff

Use this simple rubric for each of the six outputs: **0 = absent or unsupported; 1 = present but incomplete; 2 = specific, evidence-linked, authorized and clear about limits**. Maximum score is 12. A passing classroom submission should score at least 9, with **no zero** for approval or evidence scope. This is an editorial practice rubric, not a credential or formal academic grade.

| Output | What a score of 2 requires |
|---|---|
| Timeline | UTC order, record IDs and a note about what order cannot prove. |
| Hypotheses | At least two competing explanations, evidence for and against, and a discriminating next check. |
| Action record | Approver, scope, rationale, expected effect, cost, fallback and review time. |
| Recovery plan | Named test copy, booking correctness, authorization check, audit check and rollback trigger. |
| Status message | Affected service, known facts, uncertainty, owner and next update without blame. |
| Improvement ticket | One gap, accountable owner, due date and verification exercise or metric. |

A learner should also note inaccessible evidence and why it was not collected. Do not award points for inventing device detail, a data breach, an attacker identity or a successful restore that the scenario never supplied.

#### Calibrate a score against the artifact that existed at the checkpoint

A rubric is useful only if two reviewers can apply it to the **same submission**, not to what they remember the learner saying later. [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) describes exercise evaluation against criteria identified before the event. The six-output rubric above and the worked comparison below are original classroom choices. They evaluate a learner's records, not Harbor Library's real readiness.

Freeze each artifact at the end of its round. Give it a version ID such as `A-intake-v1`, `B-hypotheses-v1` or `C-action-v1`, the release round and the source IDs actually available then. A later `D-recovery-v2` may improve the final packet, but it does not rewrite `C-action-v1`. Store a one-line reason for every revision. This matters because the Branch S report of revocation arrives in Round D; it cannot make a Round C proposal into an action already performed at 09:37.

Consider this **invented learner packet L2**, prepared after all cards have been released. Its quoted excerpts are student answers in a separate classroom example, not new R-series observations. Two reviewers independently apply the 0–2 rubric before discussing their scores:

1. **Six-row timeline — reviewers A/B: 2/2; reconciled: 2.** The learner lists R1 08:40/A, R3 08:43/A, R5 08:48/A, R9 09:03/B (received at 09:20), R18 09:24/C and R21 09:29/C, all UTC, and writes: “This order does not identify the human operator.” Source IDs, event versus release times and a causal limit are explicit.
2. **Round B hypotheses — reviewers A/B: 2/2; reconciled: 2.** The learner writes: “R10 may support planned work; R9 leaves B19 unexplained. Misuse remains possible; R13 lacks device detail. Ask the identity owner for a bounded session association check.” Alternatives, limits and a discriminator are present without using R17.
3. **`C-action-v1` — reviewers A/B: 2/1; reconciled: 1.** The learner writes: “Recommend revoking the current session; identity owner consulted; check again at 09:45.” This records a proposal and review, but “consulted” is not incident-lead approval. Staff cost, fallback and the test interval are missing. Branch S cannot repair this frozen Round C artifact.
4. **`D-recovery-v1` — reviewers A/B: 1/0; reconciled: 0.** The learner writes: “V1 passed, so all bookings are correct and the audit identifies the editor.” C1 contradicts booking correctness for B19/B20, and V1's actor field is blank. The conclusion is unsupported, not merely incomplete.
5. **Status — reviewers A/B: 2/2; reconciled: 2.** The learner writes: “Branch S reports one session revoked at 09:45; B19/B20 and audit actor remain open. Service owner and audit owner review at 10:05; cause unknown.” The action, open criteria, owners and checkpoint are bounded.
6. **Improvement — reviewers A/B: 1/1; reconciled: 1.** The learner writes: “Fix the audit actor within 30 days.” A gap and proposed window exist, but no accountable owner, test artifact or interim observation is specified, so closure cannot be checked.

The reconciled sum is **8/12**. It is below the classroom threshold of 9 and has a zero in recovery evidence, so packet L2 does not pass. Reviewers should record their disagreement rather than average `2` and `1` into `1.5`: the rubric permits only 0, 1 or 2. Reviewer A can show a source pointer that satisfies a missing field, or accept Reviewer B's score. Here no such pointer exists. A high total would not excuse an unsupported recovery claim, and a corrected final sentence would not retroactively justify the earlier Round C action.

**How to revise L2.** In `C-action-v2`, keep the 09:37 proposal as a proposal; request the incident lead's approval, add the staff reauthentication cost, a fallback if a verified edit continues and a named 09:45 query with source and interval. If a separate fictional approval is later supplied, record when it arrived. In `D-recovery-v2`, list the P1/C1 comparison as two matches and two mismatches, and mark V1's tested access behavior separately from its failed actor-attribution criterion. Ask the service owner to authorize a correction and the audit owner to fix and retest the field; both remain planned until a result is supplied. In the improvement ticket, name the audit owner, an accepted due date, the interim restricted comparison and a controlled edit whose actor and UTC time a second reviewer can verify. The revised packet can earn a new score when its fields are actually present. It still cannot prove live-system containment or recovery.

**Practice check:** score the six L2 excerpts yourself before reading the reconciled column. For each disagreement, point to the missing or contradicting record and decide whether the correct label is *absent/unsupported*, *incomplete* or *evidence-linked and bounded*. Then write three one-sentence revision requests for the action, recovery and improvement artifacts. The worked comparison above supplies the target scores and the paragraph above supplies acceptable revisions; EX050 asks you to perform the same calibration on your own final handoff. No production system or real personal record is needed.

### 4.6 After-action review

Close the tabletop with three questions: **What helped us decide? What slowed us down? What will we change and how will we check it?** Separate a one-time case correction from a reusable program improvement. For example, correcting `B19` and `B20` fixes two bookings; naming the booking service owner and rehearsing the approval path improves readiness for the next event. A good improvement ticket has an owner, a deadline and an observable test.

For this case, the team can turn the V1 audit failure into a testable improvement: assign the application and audit owner to find why the synthetic change lacks an actor identifier; require a new controlled test that produces the correct actor and UTC time; and have the response lead review the evidence before retiring any compensating monitoring. The ticket should also state what staff should do while attribution is incomplete. This is a **program control** improvement, distinct from correcting individual bookings. Another ticket could require the recovery lead to repeat an isolated restore and record its duration, source timestamp and booking comparison. An empty “review backups” task is not measurable.

The team should not call the case “resolved” merely because the tabletop ends. In the fictional facts, identity attribution and root cause remain open. The course ends when the learner can hand off that uncertainty safely, describe what evidence would close it and show how the organization will review its response process.

### 4.7 What this exercise can measure

An exercise can produce an excellent discussion while leaving a technical control untested. [NIST SP 800-84, sections 4–6](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-84.pdf) distinguishes tabletop exercises, functional exercises and tests. Its 2006 examples need local review before use in a contemporary environment; the distinction between **talking through a plan** and **measuring a system** remains useful here. The Harbor Library tabletop asks participants to reason from supplied records. It does not contact an identity provider, pause writes or restore a database. Its score is evidence about a learner's reasoning in this classroom, not a measurement of a real organization's recovery capability.

Before the first inject, write a **measurement contract**: objective, observable participant behavior, evidence to collect, success threshold and a claim the exercise cannot establish. This prevents a facilitator from deciding after the fact that an engaging discussion must have met every objective. The contract below is specific to the fictional case. Its thresholds are CyberABC classroom choices, not NIST requirements.

| Classroom objective | Observable behavior and evidence | Classroom threshold | Claim this tabletop cannot establish |
|---|---|---|---|
| Bound the first assessment | Round A note separates R1/R3/R4 observations from account-compromise hypothesis and names a missing owner answer. | A second learner can find each supporting record and the unresolved question. | The real `desk-a` account was compromised. |
| Preserve before acting | Round B request names a custodian, narrow source, retention question, approval and status as requested or completed. | The request is submitted before Round C and never represented as a completed export without a receipt. | Detailed production audit was actually preserved. |
| Choose an authorized response | Round C record names a proposed action, distinct approver, service cost, fallback and review trigger. | Another role can tell what was approved, what was only proposed and which action remains blocked. | Session revocation or write pause occurred in a real system. |
| Resist premature recovery | Round D note marks the B19/B20 comparison and V1 actor check as failed criteria. | The service status is qualified and a named owner has a next test. | The live service meets an RTO, RPO or full audit requirement. |

The first two rows are primarily **process evidence**. The last row points toward a separate **technical test plan**. A useful learner answer names the boundary: “We rehearsed who would request a restore and what its acceptance conditions would be; we did not execute or time a restore.” This sentence can be true even if every participant completed the tabletop successfully. Its honesty makes the next test easier to design.

To turn an untested recovery claim into an authorized test, the recovery lead would need a named isolated environment, a specific approved copy, a measured start and end time, expected booking values, an operator, a verifier and a safe stop rule. A service owner would then compare that *test result* with an approved business target. If the test failed, the evidence belongs in the improvement plan. If it passed, it would support only the tested copy and configuration; it would not identify the earlier `desk-a` operator or establish that a later production return would behave identically. The present classroom supplies none of those measured values. R23 is a backup-job statement, and V1 is an isolated-copy access and audit trial with a failed actor field.

An observer must record **what participants did**, not only what they said they would do. For this discussion exercise, the record is the frozen Round A–D notes, the facilitator's release ledger and the six submitted artifacts. If a participant says “we preserved R9,” but the only artifact is a request with no collected copy, record the request as observed and preservation as unverified. If the facilitator accidentally reveals P1 before Round C, record that deviation: the learner's later containment choice may be informed by evidence that the intended exercise withheld. Do not hide a compromised exercise run behind a high numerical score; repeat the affected decision checkpoint under correct release conditions.

**A two-minute review:** for each of the six artifacts, draw two columns labeled *observed in exercise* and *requires another test or source*. Put the approved-action record in the first column if its fictional approvals are recorded. Put restore time, production audit coverage and a real customer impact measurement in the second. If an item appears in both columns, narrow the claim until the columns no longer conflict. This review is optional practice and is not one of EX039–EX050.

### 4.8 A worked after-action report and improvement plan

[NIST SP 800-84, section 4.5 and Appendix A](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-84.pdf) describes evaluation that records exercise background, observations and recommendations. The following **original classroom report** applies that general structure to the Harbor Library model path; it is not a copied NIST template and is not a report from an actual organization. It shows a learner how to connect each proposed improvement to an observation and to a later verification activity. In a real exercise, the report author must obtain the actual facilitator notes and participant feedback rather than infer that the model path occurred.

**Report identity and boundary.** Case `HL-IR-001`; exercise type: facilitated, discussion-only tabletop; scenario: fictional room-booking edits and uncertain use of `desk-a`; rounds A–D; model path: Branch S. Participants are *roles*—incident lead, analyst, service owner, recovery lead, identity administrator and communications contact—rather than named real people. R1–R24, Branch S, P1/C1 and V1 are classroom cards. No production identity action, database correction or customer notice was performed. The report does not estimate actual business loss, compromise probability or restoration duration.

**Predeclared objectives.** O1: open an evidence-bounded case record by the Round A checkpoint. O2: make a narrow preservation request before the Round C response choice. O3: document the authority and verification plan for a reversible containment action. O4: refuse an unconditional normal-service declaration when the later booking comparison or audit test fails. Each objective has an artifact in section 4.7. The six-output score from section 4.5 supplements, but does not replace, these four objective checks.

**Observed model trace.** The worked Round A intake cites R1, R3 and R4 and leaves the service-owner answer pending; that supports O1 for this *model*, not for an unseen student submission. In Round B, the model requests a narrow audit copy before choosing a containment option; R15 makes the retention question urgent, but the record has no collector receipt, so O2 is met as a **request** and preservation remains unverified. At Round C, the model recommends session revocation, names the fictional incident lead and identity owner as approvers, and leaves service-owner authority for a write pause separate; this supports the decision-record part of O3. Branch S later reports revocation at 09:45, but the query covers only its stated range. A learner who writes “all unauthorized access stopped” would fail the verification portion of O3. In Round D, P1/C1 shows two mismatches and V1's actor field is blank, so the model withholds unconditional recovery; O4 is met for the model path. The model does not supply an actual restore-time measurement.

| Observed evidence and limit | Recommended change | Closure proof |
|---|---|---|
| The Round A note leaves the service owner pending. The classroom card does not demonstrate a reachable primary or an authorized alternate. | Confirm both contacts and the types of disruption each may approve. | In a later drill, a reviewer finds both contacts and records their response within the organization's chosen time target. |
| The Round B request cites R15, but no copy receipt exists. Request quality was exercised; collection and integrity were not. | Add custodian response, copy ID, collection time, access restriction and independent check to the preservation procedure. | A controlled training export produces a traceable receipt; a second reviewer locates and verifies the restricted copy. |
| P1/C1 shows B19–B20 mismatches and V1 has a blank actor. Limited access tests passed, but complete return and attribution did not. | Test corrections and audit attribution in an approved isolated environment with named owners and rollback conditions. | A new result compares each selected booking with its approved target and shows the correct actor and UTC time for the controlled edit. |

The table does not claim these improvements have been implemented. A recommendation becomes an **assigned action** only when a named owner accepts it, a due date is recorded and the acceptance evidence is agreed. In the model's improvement plan, the response lead owns the first follow-up meeting; the service manager owns the contact and authority record; the evidence custodian owns the export receipt procedure; and the application/audit owner owns the V1 attribution investigation. Set dates from an actual exercise calendar. A classroom learner can propose “within 30 days of the tabletop” but must label it a proposed deadline until the fictional owner accepts it.

**Independent closure rule.** The person who implements a change should supply the test artifact; a different reviewer should decide whether it meets the predeclared criterion. For the audit issue, a configuration change or a filled ticket is not closure. The reviewer needs a controlled edit with the expected test actor and UTC time, a pointer to the resulting log and a statement of the tested scope. A pass in one isolated environment does not automatically cover every production path. If the test fails or the owner cannot produce the artifact, keep the ticket open and keep any approved interim monitoring in place. This is a classroom quality rule for the plan, not a universal legal or regulatory closure standard.

**What to report to management.** A concise summary can state that the model discussion surfaced a missing initial owner contact, a preservation request without a copy receipt, and two failed recovery acceptance criteria; it can name the proposed owners and next tests. It should also state that no live system was exercised. The report should not say “the incident was contained,” “the backup worked,” “no personal data was affected” or “the cause was found.” Those sentences exceed the supplied cards. The after-action report's function is to guide a better next exercise and test, not to manufacture a resolved case.

### 4.9 Optional replay lab: the service owner cannot be reached

This **separate replay variant** starts from the Round C decision point; it does not alter R1–R24 or the reference Branch S/P cards. Keep your original Round C note, then make a fresh copy labeled `HL-IR-001-REPLAY-F1`. The purpose is to test whether a learner can continue evidence work while withholding an action whose required approver is unavailable. The replay is a discussion only. It does not authorize a real session change, write pause or data collection.

**New card F1, revealed at simulated 09:35 UTC:** the booking service owner is temporarily unreachable, and the response plan lists no confirmed alternate for approving a staff-write pause. The incident lead and identity owner remain reachable for a narrowly scoped session decision under the fictional rules already stated in section 3.3. R21 still describes the owner's *tolerance* for a fifteen-minute pause; it does **not** become an approval because the owner is absent. R17/R18 are available at this Round C point. Branch S/P results, P1/C1 and V1 remain withheld until the ordinary Round D sequence.

**Task:** write two decision records at 09:37. Record A is a bounded recommendation that the reachable incident lead and identity owner could approve or reject for the current `desk-a` session. Record B is a proposed staff-write pause marked **approval pending**, with a reason it might be needed, its service cost, who is being contacted, what evidence can still be reviewed meanwhile and a stop or escalation trigger. Then prepare a one-sentence handoff for the next response lead that says which action, if any, was *reported executed* at 09:37. No execution card exists at this point, so the answer must say none is reported. The objective is not to force Record A to be approved; a learner may defer it with an explicit risk and review time.

**Inputs and authority check:** use R17, R18, R21, the option matrix in section 3.3 and the Chapter 1 role boundary. The incident lead can coordinate an escalation and request a contact check; the identity owner can approve or reject the scoped session action with the incident lead in this fictional exercise. Neither role has been given authority to approve the booking-service write pause alone. The analyst may prepare a reversible option and examine already supplied records; a production audit export would still require its own collection authority and custody record. Do not call a missing reply consent.

**Expected artifacts and rubric:** submit Records A and B plus the one-sentence handoff. Award one point each for (1) preserving the distinction between R21 tolerance and approval, (2) recording the two reachable approvers and a bounded verification for Record A, (3) leaving Record B pending and documenting the affected queue/service cost, (4) naming an allowed next evidence or escalation step with a review trigger, and (5) stating that no 09:37 execution has been reported. A 5/5 response can choose a different defensible risk tradeoff; it cannot invent an alternate owner, use a later branch result or claim that a write pause was already enacted. A model answer appears after the 50 numbered worked results.

**Why replay matters:** if two students choose different proposals yet both respect the same approval boundary, the exercise can distinguish justified decisions from lucky outcomes. If F1 changes the decision, compare the original and replay records field by field: which observation changed, which authority became unavailable, which action was held and which review trigger became more urgent? Only the authority fact changed; the underlying R17/R18 evidence did not. That comparison teaches a reusable response habit without treating a fictional facilitator card as real incident evidence.

### 4.10 Optional communication replay: a request for reassurance and an unverified claim

An incident can have a technically careful case record and still cause harm if its updates promise more than the evidence supports. The operational team may need details about a specific account and booking IDs; patrons need a useful description of the affected service and where to get help. A privacy contact may need the exact origin of a new exposure claim. These audiences do not need identical messages, and an internal coordination note is not automatically a public statement or a formal notification. [NIST SP 800-61 Rev. 3, RS.CO and RC.CO](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) discusses incident reporting, coordination and approved recovery communications. The message cards, word limits and scoring rule here are original teaching devices, not prescribed NIST wording or a determination of any notification duty.

This **separate after-Round-D replay** uses Branch S unless a learner clearly marks a Branch P alternative. The canonical R1–R24, Branch S/P, P1/C1 and V1 retain their meanings. No new card may be used to justify the earlier 09:37 choice. Write only in a local Markdown exercise file; do not send a message to a real person or publish one. The fictional organization has not supplied its legal jurisdictions, contracts, notification thresholds or approved external spokesperson, so the exercise cannot decide that a statutory notice is or is not required. It can identify who must assess that question.

**Card M1, released at simulated 09:50 UTC.** A front-desk supervisor asks the communications contact: “May we tell patrons that bookings are restored and the problem is over?” The request is a question, not evidence that service has returned. Branch S reports a session revocation at 09:45 and a quiet *bounded* booking query. P1/C1 still shows B19 and B20 inconsistent with the approved target, while V1's isolated test has a blank actor field. The record has no owner-approved production correction, no full-service acceptance and no production audit pass. A reassuring sentence would be easy to write and hard to defend.

**Card M2, released at simulated 09:52 UTC.** The communications contact receives a forwarded internal chat sentence: “Someone said the newsletter list was stolen.” It contains no original author, time of alleged access, source system, export record or case reference. It establishes that an **unverified statement was received**, not that data was accessed or exported. R24, recorded at 09:36, says that no record then established access to the newsletter list or another personal-data store. R24 is not a permanent all-clear; M2 is not proof that R24 was wrong. The privacy contact and incident lead should receive a narrowly framed verification request through the fictional approval route, with the original forwarded item preserved as a *report of a claim* and its provenance gap stated.

#### Decide which communication you are drafting

An **incident coordination update** tells the response roles which action was reported, what test failed, who is doing the next check and when the next decision is due. It can include restricted case identifiers if sent through an approved internal channel. A **service status draft** gives patrons a useful description of a booking discrepancy and a safe way to check their own booking, without revealing an account label, unsupported root cause or another patron's information. A **formal incident or privacy notification** is a separate, approval-dependent decision made under applicable procedure by designated roles; the sparse classroom record cannot resolve it. A rumor should be routed for assessment, not quietly appended to a patron message as if verified.

Versioning matters because evidence changes. A 09:37 proposal, a 09:45 reported action and a 09:54 communication draft are three different states. If a team previously sent “all bookings restored,” it should not erase the old version and pretend the assurance was never made. Keep the issued wording, audience, time and approving role; issue a clearly linked correction through the same approved route with the new evidence and a next update. In this exercise there is **no issued earlier message**. A learner may practice correcting an explicitly hypothetical flawed draft, but must not claim that Harbor Library actually made it public.

Use this small **claim-to-message ledger** before drafting:

| Candidate sentence | Supplied evidence by 09:54 | Permitted treatment in this replay |
|---|---|---|
| “The current `desk-a` session was revoked.” | Branch S reports that specific action at 09:45. | May appear in a restricted internal coordination update; do not infer every session was removed. |
| “All bookings are correct.” | P1/C1 contradicts it for B19 and B20; no later correction result is supplied. | Exclude from every status version. Name the pending owner-reviewed comparison internally. |
| “The newsletter list was stolen.” | M2 is an unattributed forwarded claim; R24 was an earlier limited evidence statement. | Record as unverified, request scoped assessment by the privacy contact; do not publish as a finding. |
| “Patrons can check a questionable room booking with the front desk.” | R5 reports a patron booking concern; the manual help route is a proposed classroom service instruction. | Include only if the fictional service owner confirms that the route is available and the communications owner approves the draft. |
| “The incident is over.” | Cause, booking correction, full access scope and V1 audit attribution remain unresolved. | Exclude. Promise a **next update time**, not a resolution time. |

The ledger deliberately distinguishes **false or contradicted**, **unverified**, and **conditionally useful** claims. A sentence may be accurate for one restricted audience but inappropriate in a public draft because it exposes unnecessary operational detail. A status note should tell its reader what to do with the information. “Investigating” alone does not tell a front-desk worker how to handle a disputed booking; “all clear” would be worse. The correct short update states the present limit and the next responsible check.

#### Practice: produce a versioned communication packet

Write four Markdown artifacts, all marked **draft, not sent**. First, a five-row claim ledger based on the table above, adding the record or card ID and the earliest round in which each claim became assessable. Second, a restricted **09:54 internal update** of 80–120 words for the incident lead, service owner, front-desk supervisor and privacy contact. State what Branch S reported, which booking and audit criteria remain open, the status of M2 and who will check each issue. Give a fictional next review at 10:05 UTC; it is a planned checkpoint, not a guaranteed restoration time.

Third, write a **patron-facing holding draft** of 45–80 words for approval by the service and communications owners. It may say that the library is reviewing discrepancies affecting room bookings and will provide an update after verification. It should offer a practical contact route only as a proposed, owner-confirmed route. It should not name `desk-a`, claim that a breach occurred, declare the booking service fully restored or say that no personal data was affected. The student is drafting a possible message, not deciding to publish it.

Fourth, write a **privacy assessment request** of three to five sentences: identify M2 as an unattributed report, mention R24's earlier limited finding, ask what authorized source or custodian could verify newsletter-list access in a bounded period, and name the incident lead/privacy contact as decision partners. Preserve the forwarded wording only in the restricted exercise record; do not copy a real person's message. If the result later supports a breach, route notification assessment to designated decision makers under the organization's actual procedure. If the result does not, record the tested scope and residual gaps rather than announcing universal absence of exposure.

**Branch P variation:** replace the Branch S line in the internal update with the 09:45 service-owner report of a fifteen-minute staff-write pause and two manual-queue requests. At 09:54, the planned pause has **not reached its 10:00 end**; do not say writes resumed. The service owner must reconcile the queue and approve the next state. The patron draft should not promise that ordinary booking writes are available. Keep M2's evidence status unchanged: a different containment branch does not make an unattributed claim true or false.

**Optional correction drill:** suppose a *fictional earlier draft*, not an issued statement, read “All bookings are restored and no customer information was affected.” Mark both clauses unsupported or contradicted, retain it in a version log as `draft-v0`, and produce `draft-v1` linked to P1/C1, V1 and M2. If the sentence **had** already been sent in a real organization, an authorized communications lead would need to assess and issue a correction through the proper channel; the learner cannot decide that process from these synthetic cards.

**Assessment rubric (six points):** one point for a ledger that dates and classifies all five claims; one for an internal update that distinguishes Branch S's narrow action from the unresolved booking and audit checks; one for a patron draft that is useful without premature restoration or breach claims; one for routing M2 to a bounded privacy assessment without treating R24 as a permanent all-clear; one for naming approvals, audience and a 10:05 checkpoint; and one for retaining version history and correctly handling the Branch P or correction variation. A perfect classroom score demonstrates careful wording under these supplied facts. It does not establish that the communications route works in a real incident or that a legal notice is unnecessary. A model packet follows the F1 replay result in the final appendix.

### 4.11 Controlled injects and disciplined replay

An inject is useful when it changes what the team could reasonably decide. Merely adding alarming words does not produce better learning. In the Harbor Library curriculum, each release has a defined question: Round A tests first-response boundaries; Round B tests B19 explanation and preservation urgency; Round C tests protective action versus legitimate service; Round D tests whether reported containment and later recovery checks support service acceptance.

The facilitator should prepare an **inject ledger** with: inject identifier, earliest release, factual content, expected decision affected, permissible source claims, prohibited inferences and fallback instructions when the learner asks for data not supplied. If an identity session detail is absent, a facilitator must not improvise a confirmed device or attacker. The appropriate reply is that the detail is unavailable in the current exercise and could be requested from a fictional custodian under the case's approval path.

A facilitator may ask a student to state the *minimum missing observation* that would change the proposal. At 09:20, a complete approved task-list addendum for B19 is more discriminatory than simply repeating a general suspicion. At 09:37, confirming the exact session-to-write relationship would affect how narrowly the team can target access, while R21's tolerability statement informs the business cost of a broader pause. An inject that resolves neither question should be recognized as context rather than treated automatically as heightened confidence.

Counterfactual branches require a reset. After Branch S, ask how the decision would differ under Branch P, but label the alternative as a **replay** and start from the same frozen Round C card. Otherwise the student may merge the reported revocation of Branch S with the two queued requests of Branch P and invent an impossible case record. A comparison can legitimately say that Branch S places more emphasis on session scope and staff reauthentication, while Branch P places more emphasis on paused writes, queue custody and resumption criteria.

The facilitator also should not reward a student for making a production-like change when the exercise permits only tabletop role-play. Instead, score whether the student specified the approval required, the exact target and a test that would detect both intended effect and legitimate-service harm. An explicit "execution not performed" field is a valid outcome.

### 4.12 Audit the six artifacts as one decision chain

This exercise requires a timeline, hypothesis table, action record, recovery plan, internal status message and improvement ticket. The artifacts are not six independent writing assignments: each has an input and output relationship with the others. A late inconsistency in one may reveal an earlier missing assumption.

**Artifact 1: Timeline.** Include the original source event time, release round and source ID. Its primary job is to prevent the analyst from proving causation merely through ordering or justifying an earlier decision with future evidence. Include a column for whether the item was actually available at the checkpoint. The timeline must not mix application activity with an interview note as if they had identical evidentiary semantics.

**Artifact 2: Hypothesis table.** Keep at least two explanations live, including authorized training and account use outside the approved plan; a display/state discrepancy may coexist with either. For each, identify supporting, conflicting or insufficient evidence and an authorized discriminator. An account label and a staff recollection are not human attribution.

**Artifact 3: Action record.** Separate recommendation, approval, execution and verification. In Round C, R19 says a session *can* be revoked and R21 says a staff-write pause is *tolerable*. Neither row confirms execution. The action record must include the expected protection, one legitimate-service negative check, uncovered routes, decision owner, fallback and review time. If an action is never executed in the round, leave its execution fields pending.

**Artifact 4: Recovery plan.** A plan is not a restore receipt. Before P1/C1 and V1 are released, its expected-state and tested-result fields must be labeled pending. After those separate later cards arrive, B19 and B20 do not match the P1 target, and V1's test audit lacks the actor despite its limited positive and denied-access observations. These failures prevent unrestricted acceptance. A later approved corrective operation and **new** comparison would be needed; nothing in these cards establishes that such a production correction occurred.

**Artifact 5: Status message.** Its audience and publication state matter. The exercise EX048 requests two internal sentences at the 09:45 branch result **before** P1/C1 and V1 are released; those later findings cannot be included. A separate post-D communication exercise can discuss the later mismatches because its evidence boundary is different. Label the two versions accordingly, and never transform a drafted message into a sent notice.

**Artifact 6: Improvement ticket.** A ticket closes a reusable capability gap, not the individual case symptom alone. Correcting B19/B20 addresses selected bookings. Testing the missing V1 audit actor or an outdated restore rehearsal addresses whether the next response can be investigated or recovered safely. A ticket needs a directly accountable owner, due date, test fixture, evidence artifact, pass/fail rule and procedure for a failed retest.

The six documents must agree on unresolved conditions. A status message claiming full recovery is inconsistent with a recovery plan that records failed booking and audit gates. A summary saying a session was revoked at 09:37 is inconsistent with the frozen Round C action proposal and the later 09:45 branch report. An evaluator should treat those as material reasoning defects, not stylistic differences.

### 4.13 Compare the operational liabilities of both branches

Choosing Branch S or Branch P does not change the canonical pre-branch evidence. It changes what the learner must verify and hand off.

For **Branch S**, the reported session revocation is an observed *fictional branch action*, not proof of eradication. The narrow quiet query does not cover every route or time; staff reauthentication is a service effect. The next operator needs the identity-action scope and the process for restoring authorized staff access, while the service owner still needs to resolve incorrect booking state and the later V1 audit failure.

For **Branch P**, a fifteen-minute staff-write pause begins at the reported 09:45 branch checkpoint and creates two pending manual requests. Those requests are not accepted reservations. The service owner must assign custody, confirm each request identifier, assess conflicts with current state and authorize reconciliation before resuming writes. At 09:54 the planned fifteen-minute interval has not yet reached its 10:00 boundary; saying the pause expired and writes resumed would be unsupported. Even after 10:00, the planned end is not a verified resumption receipt.

A comparison worksheet should not ask simply "Which branch stopped the attack?" Neither branch establishes the cause, and an absence of matching audit rows could reflect limited coverage. Instead compare: protection aimed at, known service side effect, business owner, required post-action verification, unresolved routes, correction dependencies and risk of reversal.

A good reversal rule is observable. For Branch S, a verified unexplained booking change after the tested session revocation can trigger reassessment of other paths and proposed controls. For Branch P, an inability to reconcile queued requests or a failed business correctness check can block write resumption. Those are criteria for another decision, not automatic authority for a real intervention.

### 4.14 Control the audience and approval of each message

Different audiences legitimately require different levels of technical detail. The incident lead needs decisions and pending authorities. Front-desk supervisors need permitted operating workarounds. Patrons need an accurate, usable service instruction. The privacy contact needs sufficient provenance to assess an alleged data-access event. These are related messages but not interchangeable disclosures.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) addresses coordination and communications in cybersecurity incident response and recovery. The audience matrix below is an original classroom adaptation; it does not decide legal notification duties.

| Audience | Useful content | Avoid | Approving or coordinating role |
|---|---|---|---|
| Incident lead and technical owners | Case ID, action status, exact evidence, failed acceptance checks, missing fields, next decision | An unexplained "all green" verdict | Incident lead and relevant source owners |
| Front-desk supervisor | Whether ordinary writes are available in the chosen branch, approved temporary workflow and escalation route | Account compromise claims or instructions beyond the supplied approval | Service owner and operational lead |
| Patrons | Potential room-booking discrepancy, practical *owner-confirmed* contact route and time of next update | Account names, other patrons' details, unsupported "fully restored" claims | Communications contact and service owner |
| Privacy contact | Scope and provenance of a specific allegation, sources to request and residual uncertainty | Treating a forwarded rumor as evidence of theft or R24 as permanent clearance | Privacy contact with incident lead |
| External or formal notification audience | Only facts approved under the organization's relevant obligations and procedures | Legal conclusions the exercise lacks jurisdictional and evidentiary basis to make | Designated communications, legal and privacy authorities |

A message is itself a controlled artifact with version, audience, approval, release time and superseded-version links. A draft is not an issued notice. When a fact changes after a message was actually sent, an authorized communications role would need to preserve the original and assess a correction; silently overwriting it destroys the history of what recipients were told. The fictional case supplies no record that an erroneous public message was sent.

### 4.15 Verify improvement closure with a measured test

An improvement ticket is not complete when a team marks a task "done." Completion should mean that the identified capability passed a defined test and a reviewer accepted evidence of the result. Prefer one owner and one verifiable weakness per ticket rather than an unbounded "improve the SOC" assignment.

A suitable ticket has: identifier; evidence pointer; risk statement; accountable owner; deadline; planned change; prerequisites; authorized isolated test; expected positive and negative outcomes; review owner; supporting artifact; and next action on failure. The ticket can remain open despite an implementation claim if the verification result is missing.

**Example — audit attribution**

- **Gap:** V1's isolated authorized booking test has a UTC timestamp but blank actor.
- **Owner:** application/audit owner; incident lead reviews closure.
- **Change:** identify and correct the missing synthetic actor-field propagation in the tested path.
- **Controlled test:** execute one approved fictional staff edit and one denied unauthorized edit in an isolated environment, capturing the application version, expected actor identifier, UTC event time, request key and authoritative state.
- **Pass:** the authorized record contains the expected actor and time and matches the declared write, while the unauthorized attempt is denied with state unchanged; the reviewer can reproduce the selection.
- **Fail:** actor remains empty, denied operation changes state, or source attribution/coverage is insufficient.
- **Interim measure:** a named owner performs restricted comparison and escalation until a passing test and explicit closure decision are recorded.

A failure should create a *new decision*, not force the score to pass. Record whether the defect was caused by the test setup, source mapping or incomplete instrumentation only after evidence supports the classification. A corrective-action ticket may legitimately close with a changed design and documented residual risk, but that is a distinct owner-approved decision—not a fabricated test pass.

For a restore-readiness ticket, require an actual isolated import and owner comparison; the mere presence of a backup file does not close it. For a handoff-readiness ticket, require a blind receiver to identify current branch status, approval state, failed gates and next action without asking the original analyst. The blind handoff is a measured learning task, not proof of future production performance.

### 4.16 Choose metrics that cannot be gamed by easy exercises

Measure outcomes rather than counts of meetings or pages. "All personnel attended training" does not show that an analyst can distinguish an unapproved action from a proposed one. "Ten backup jobs succeeded" does not show that one approved booking dataset can be restored correctly and on time.

Useful metrics for repeated, authorized exercises include the proportion of decision cards with exact source pointers, the share of approvals with separately documented execution status, the rate of handoffs that identify open booking/audit gates, and the percentage of improvement tickets closed by independently checked evidence rather than administrative status. Those metrics require clear denominators and consistent definitions. They should not be turned into a score when the sample is too small or the evidence is incomplete.

The facilitator can also measure **decision latency** from card release to a justified proposal, but speed alone is not success. A student who instantly labels `desk-a` compromised and orders account removal is fast and wrong. Another who accurately cites the evidence, names the approver and proposes a short review may be slower and safer. Record both timeliness and completeness. A high score in a tabletop cannot stand in for a technical test of a network, identity provider or recovery process.

For an improvement rehearsal, predefine an allowed response window and what constitutes an acceptable decision. Record the actual fictional start/end and whether the learner met *both* the time and safety criteria. Do not infer a real organization's response-level agreement or compliance posture from this classroom score.

### 4.17 A valid exercise can end with open conditions

A tabletop may end while the fictional incident remains unresolved. That is a valid learning result when the packet makes open questions actionable.

In Branch S, the narrow revoked-session report does not prove which person previously edited bookings. In Branch P, the pause and manual queue do not prove that writes will be safe after resumption. After P1/C1 and V1, B19/B20 correctness and audit attribution are still failed acceptance criteria in the supplied test record. Neither branch establishes a completed production backup restore, full access coverage or a universal absence of data exposure.

The student should state what would close each open item: source, owner, authorized test, pass/fail outcome and review deadline. A final status may therefore be "tabletop concluded; response handoff and corrective actions open" instead of "incident recovered." That distinction respects both the learner's achievement and the limits of the fictional evidence.

Before handing in the final packet, run a **contradiction review**: Does the status message promise recovery while the data table fails? Does the action card imply approval from R21 alone? Does the final timeline use R9 at 09:05 or R17 at 09:20? Does a privacy message repeat M2 as fact? Does the improvement ticket claim a test passed when only a proposal exists? Resolve these as explicit revisions, preserving earlier snapshots. This final consistency check is often more educational than adding another paragraph of incident narrative.

<a id="ir-rapid-ch04-f4-audit-lab"></a>

### 4.18 Offline laboratory: F4-AUDIT release and assessment gate

**Purpose:** Demonstrate that a six-artifact packet can score well yet fail a critical approval gate, and that a later release cannot repair an earlier frozen decision. This classroom evaluator complements the L2 scoring case, F1 unavailable-approver rehearsal and M1/M2 message activity; it does not substitute for their evidence analysis.

**Environment:** Python 3 standard library, in memory. No network, files, credentials, messages or state changes. All sample scores below are invented teaching input. They are *not* grades given to a real learner.

**Procedure:** Before running, predict which references are in scope for each checkpoint; identify the prohibited future reference and mixed-branch example; then predict whether an improved 11/12 packet would pass if its approval evidence were missing. Run the code and compare the exact transcript.

~~~python
LEVEL = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D_BRANCH": 4,
    "D_TARGET": 5,
    "D_ACCESS": 6,
    "M_REPLAY": 7,
}

RELEASE = {
    **{f"R{i}": "A" for i in range(1, 9)},
    **{f"R{i}": "B" for i in range(9, 17)},
    **{f"R{i}": "C" for i in range(17, 25)},
    "S": "D_BRANCH",
    "P": "D_BRANCH",
    "P1": "D_TARGET",
    "C1": "D_TARGET",
    "V1": "D_ACCESS",
    "M1": "M_REPLAY",
    "M2": "M_REPLAY",
}

def validate(snapshot, refs):
    if "S" in refs and "P" in refs:
        return "BRANCH_CONFLICT"
    unknown = sorted(set(refs) - set(RELEASE))
    if unknown:
        return "UNKNOWN:" + ",".join(unknown)
    future = sorted(
        r for r in refs
        if LEVEL[RELEASE[r]] > LEVEL[snapshot]
    )
    return "FUTURE:" + ",".join(future) if future else "IN_SCOPE"

SAMPLES = [
    ("A-timeline", "A", ("R1", "R4")),
    ("B-hypotheses", "B", ("R9", "R10")),
    ("C-action", "C", ("R18", "R21")),
    ("D-status-S", "D_BRANCH", ("S",)),
    ("D-recovery", "D_ACCESS", ("P1", "C1", "V1")),
    ("D-improvement", "D_ACCESS", ("V1",)),
]

for ident, stage, refs in SAMPLES:
    print(f"{ident}: {validate(stage, refs)}")

NEGATIVES = [
    ("NEGATIVE_FUTURE_BRANCH", "C", ("R18", "S")),
    ("NEGATIVE_PREMATURE_RECOVERY", "D_BRANCH", ("S", "V1")),
    ("NEGATIVE_MIXED_BRANCHES", "D_BRANCH", ("S", "P")),
]

for ident, stage, refs in NEGATIVES:
    print(f"{ident}: {validate(stage, refs)}")

def score(values, approval_ok, scope_ok):
    total = sum(values)
    if not approval_ok or not scope_ok:
        return f"{total}/12 HARD_GATE_FAIL"
    if total >= 9:
        return f"{total}/12 CLASSROOM_THRESHOLD_MET"
    return f"{total}/12 REVISION_REQUIRED"

print("FROZEN_V1:", score((2, 1, 1, 1, 2, 1), True, True))
print("REVISED_V2:", score((2, 2, 2, 1, 2, 2), True, True))
print("NEGATIVE_NO_APPROVAL:", score((2, 2, 2, 1, 2, 2), False, True))
~~~

[Check the exact output and interpretation in the final worked results.](#ir-rapid-ch04-f4-audit-result)

### Chapter 4 exercises

Use the four rounds and choose either Branch S or Branch P for your final decisions. Record **event time and card-release round separately**. Round A has R1–R8, Round B adds R9–R16, Round C adds R17–R24, and Round D first supplies a branch result and only later P1/C1 and V1. Do not cite a later card to justify an earlier action; do not invent a real export, restore, account action or person behind `desk-a`. For each answer, submit the named artifact with case ID, source IDs, current round, observation versus proposal or reported action, decision owner, remaining limit and next review. A solo learner may write all roles, but must still record who would approve and who would verify a change.

**Numbered-exercise rubric:** score **0** for an absent artifact or an unsupported breach, actor, executed action or recovered-service claim; **1** for an artifact that addresses the task but omits a required source, release boundary, authority or verification; **2** for an evidence-linked, authorized and reviewable artifact with every local field below. This is distinct from the six-output tabletop rubric in section 4.5. Each worked result shows one acceptable path; a different branch or conclusion can earn 2 when its assumptions, evidence and constraints are explicit.

#### EX039 — Role and scope card

**Objective:** assign authority before observing the case outcome. **Inputs:** Round A, Chapter 1's role table and synthetic R1–R8. **Output:** a five-row role card for incident lead, analyst, service owner, recovery lead and communications contact; name each responsibility, one approval or escalation boundary and one verifiable output. Add a single sentence defining permitted objects, actions and exclusions. A score of 2 makes clear that neither a learner nor analyst can independently disrupt a real booking service.

#### EX040 — Intake artifact

**Objective:** produce a reproducible first handoff without hindsight. **Inputs:** Round A only, R1–R8 and the 09:00 case-open time. **Output:** exactly four labeled lines covering case/time/service, at least two observed source events, current status and unknowns, and the owner question plus proposed 09:05 checkpoint. Cite record IDs and mark R5 as a patron report. A score of 2 does not cite R9, R17 or a later branch result and does not treat proposed preservation as already performed.

#### EX041 — Evidence chronology

**Objective:** separate source-event time from learner availability. **Inputs:** R1–R24 after Round C; **no** Round D card. **Output:** a six-row table with ID, UTC event time, source, release round and observation, using at least one item from each of Rounds A, B and C. Add one ordering fact and one causal or identity claim that the sequence cannot prove. A score of 2 retains that R9's 09:03 event reached the learner only in Round B, while R17–R18 could not guide the 09:20 decision.

#### EX042 — Competing explanations

**Objective:** maintain discriminating hypotheses at the 09:20 review. **Inputs:** R1–R16 only. **Output:** three rows for authorized training, unauthorized use of `desk-a` and display/state divergence, each with supporting record, contrary or limiting record, narrow authorized check and a result that would weaken it. Do not use R17–R18 or P1/C1; those arrive later. A score of 2 says B19 is unresolved rather than proving one explanation from the account label or a patron report.

#### EX043 — Preservation request

**Objective:** request time-sensitive evidence without a fabricated deadline. **Inputs:** Round B, R9, R14–R15 and Chapter 2's preservation fields. **Output:** a request naming source, booking IDs or bounded event interval, necessary fields, policy-clock question, approving role, collector, restricted storage/access and actual collection status. R15 says detailed audit records are deleted after 24 hours unless copied; ask the custodian what starts that clock rather than calculating an exact expiry from R9 alone. A score of 2 says **requested** until a copy and collection time are documented.

#### EX044 — Decision checkpoint

**Objective:** make a reversible 09:37 recommendation. **Inputs:** Round C, R17–R21 and the section 3.3 option matrix. **Output:** a decision card with current evidence and uncertainty, chosen proposal, approver and executor, intended benefit, uncovered path, service cost, preservation note, fallback, verification plan and 09:45 review. Give separate **proposed, approved, executed and verified** states; mark any state without a receipt *pending*. Include one check for the protective effect and a different check for legitimate staff service. A score of 2 treats R21 as tolerance rather than approval or execution and does not cite the Branch S/P result before Round D.

#### EX045 — Branch S review

**Objective:** bound what a successful session action actually demonstrates. **Inputs:** Round D **Branch S only**, before P1/C1 or V1; earlier R1–R24 remain available. **Output:** a four-row claim ledger with two supported claims and two unestablished claims, each with branch pointer and limit, plus one authorized next check with scope and owner. A score of 2 limits the “no later edit” observation to the branch query's range and does not claim eradication or correct booking state.

#### EX046 — Branch P review

**Objective:** account for operational effects of the pause. **Inputs:** Round D **Branch P only**, before P1/C1 or V1; R21's tolerance. **Output:** a queue-and-return note with the two pending requests, who holds them, a verification that writes were blocked, an owner-approved resume condition, a signal to keep the restriction, and the next checkpoint. A score of 2 does not mark the two requests fulfilled or the cause resolved and gives an explicit reconciliation step before resumption.

#### EX047 — Recovery acceptance

**Objective:** decide whether the supplied recovery evidence permits full release. **Inputs:** chosen branch, then the later P1/C1 and V1 cards. **Output:** a four-row return-to-service checklist covering booking correctness, authorized access, denied unauthorized access and actor/time audit visibility. For each, state expected result, current card result, owner and next test or correction; add a provisional service status and rollback trigger. A score of 2 marks B19/B20 mismatched and V1's blank actor as failed criteria rather than calling the book's simulated case recovered.

#### EX048 — Internal update

**Objective:** report the action while preserving uncertainty. **Inputs:** chosen Round D branch at 09:45 UTC, **before** P1/C1 and V1 are released. **Output:** exactly two sentences for an internal service-owner audience, naming the service, a supported observation and reported branch action, current uncertainty, owner and next checkpoint. For Branch P mention the manual queue; for Branch S mention reauthentication. A score of 2 does not assert breach, attacker identity, complete recovery, a validated restore or results from later cards.

#### EX049 — Improvement ticket

**Objective:** turn a case observation into a program improvement with proof of closure. **Inputs:** all four rounds, R23 or V1, and sections 4.6 and 4.15. **Output:** one ticket with gap and evidence pointer, accountable owner, due date, bounded change, interim control, a positive acceptance observation, a negative failure control, retained test receipt and action if the test fails. Choose either stale restore evidence or blank audit actor; do not bundle unrelated work into an untestable “improve security” task. A score of 2 explains why correcting B19/B20 alone would not close the selected program gap.

#### EX050 — Final handoff and self-assessment

**Objective:** give a new responder a complete, auditable state without overstating closure. **Inputs:** all rounds, one chosen branch, P1/C1, V1 and the section 4.5 rubric and L2 calibration. **Output:** a one-paragraph handoff naming case and evidence, proposal versus branch-reported action and fictional approvers, current booking and audit failures, unresolved cause, owners, next review and rollback trigger. Add a six-row self-score (0–2 per tabletop output, maximum 12), identify the weakest output and write one contested-score note: which artifact a second reviewer might score differently, which exact supplied record or missing field resolves the disagreement, and what revision should be versioned rather than silently replacing an earlier round. A score of 2 requires a defensible score explanation and no zero for approval or evidence scope; the handoff must distinguish the branch result from unexecuted correction or restore work.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 04

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="answers"></a>

## Worked results and assessment rubric

These results are placed after the chapter material as the book's developing answer appendix. A different answer is acceptable when it cites the supplied record, states assumptions and explains authority and potential harm.

### EX001 — Worked result

| Statement | Classification | Source and limit |
|---|---|---|
| (a) R4 records B18 cancelled | Direct observation of the application record | R4, 08:44 UTC, states a cancellation. It does not state why it was made or whether the current patron view matches the audit. |
| (b) `desk-a` was compromised | **Hypothesis requiring confirmation**, phrased as a finding without support | R1, 08:40, records a successful sign-in; R3–R4 record changes. Those events are compatible with unauthorized use but do not identify the person or establish compromise. |
| (c) R5 reports B18 disappeared | Direct observation of a **report** | R5, 08:48, says what the patron reported. It does not independently verify the patron interface or the authoritative schedule. |
| (d) R7 proves a ten-minute restore | Unsupported conclusion | R7, 08:52, reports that a backup job completed. No restore test, duration, data-consistency result or approved recovery target is supplied. |

A strong response distinguishes the *observable wording* of (b) from its epistemic status: the claimed compromise is unsupported **as a fact**, while unauthorized use remains a live hypothesis. Reclassifying it as “confirmed” because an account and edits appear near each other fails the exercise.

**Further reasoning:** A correct answer can report that R4 contains a B18 cancellation and R5 contains a patron report. Neither source independently establishes the reason for the cancellation or the full current display state. "`desk-a` was compromised" is not supported as a finding; "unauthorized use is a hypothesis to investigate" is defensible. R7 reports completion of a previous-night backup job, not a ten-minute recovery. The missing upgrade evidence is an authorized account-context comparison for the actor question and a timed, isolated restore with correct booking-state verification for the recovery claim. The follow-up evidence does not already exist within R1–R8.

### EX002 — Worked result

| Discriminating question | Why now | Custodian and permission | Decision effect |
|---|---|---|---|
| Were B17's move and B18's cancellation specifically approved training tasks? | R3–R4, 08:43–08:44, show edits; R6, 08:50, shows only a scheduled training interval. | Service or training owner checks the dated, approved task list; the incident lead records the request. | An approved list naming both edits weakens an unauthorized-*edit* explanation for those records; a confirmed complete list excluding B18 strengthens concern. |
| Was `desk-a` used by the expected staff member, and is an edit still occurring? | R1, 08:40, names an account but no human; the supplied table stops before the 09:05 checkpoint. | Incident lead seeks a narrowly scoped identity or application check from the authorized administrator; the learner does not query a real service. | An independently checked authorized session could reduce concern; a verified new unexplained edit would raise urgency and prompt a new decision. |

Neither answer is in R1–R8. The lead records a **request**, its owner and the decision time. Interview recollection alone may be useful context but is not an identity proof.

### EX003 — Worked result

| Dependency | Possible user effect | Supplied pointer | Missing discriminator and custodian |
|---|---|---|---|
| Staff identity service | If the account is being misused, further room changes may become possible; no current scope of misuse is established. | R1 sign-in at 08:40 and R2 dashboard access at 08:42. | The identity administrator, with incident-lead approval, checks a narrow session detail and account-change record. Compare to an authorized-user account; a sign-in label alone cannot identify the operator. |
| Reservation database | An incorrect schedule could make a room appear unavailable or assigned differently to a patron. | R3–R4 record edits; R5 reports a symptom. | The service owner requests a bounded comparison of the authoritative schedule, change history and patron view for B17/B18. A database record matching an approved target favors an intended change; a mismatch may indicate a data or display problem. |

Both effects are **possible**. The R5 report supports investigating a visible problem, but the exercise has not measured all users or confirmed the database's current state. Other valid pairs, such as booking application and help desk, must still name a check that distinguishes explanations.

**Further reasoning:** For the identity dependency, R1 identifies a reported sign-in and R2 identifies reported dashboard access. The hypothetical harm is further incorrect staff-authorized-function use, not a measured ongoing attack. An authorized identity-session check could weaken an assumption of unexpected session context, but it must not identify a human without appropriate independent evidence. For the database dependency, R3–R4 report changes and R5 a patron symptom. An owner-approved comparison between authoritative B17/B18 values and an expected schedule could show that current state matches or differs from the owner's target. That comparison is **requested**, not performed. The two paths have different owners and do not settle each other.

### EX004 — Worked result

**Proposed action:** search a real public library site for a matching `desk-a` account. **Boundary:** this chapter authorizes reading, sorting and annotating synthetic R1–R8 during the session; it does not authorize access to a real library, real account or third-party data. **Decision:** reject the proposed search because it would expand both the object and the organization under investigation. **Contained alternative:** use R1 and R2 to state that the account signed in and opened the dashboard, while marking the human operator unknown. Draft a fictional request to the incident lead for the identity administrator to provide the minimum relevant session fields and interval *if* an actual organization approved such collection. **Stop condition:** if the answer requires a field absent from R1–R8, stop at the evidence boundary and record the unresolved question. A public page being reachable does not confer incident-response authority over it.

### EX005 — Worked result

| Record | Source | UTC time | Observed event |
|---|---|---|---|
| R1 | Identity log | 08:40 | `desk-a` sign-in succeeded. |
| R3 | Application log | 08:43 | B17 changed from Room 2 to Room 4. |
| R4 | Application log | 08:44 | B18 was cancelled. |
| R5 | Help desk | 08:48 | Patron reported B18 had disappeared. |

**Ordering fact:** the recorded sign-in precedes the two recorded edits, and the help-desk report follows them. **Causal limit:** temporal order does not prove that the sign-in was unauthorized, that one named person made the edits, or that R4 explains every part of the patron's experience. The 09:00 case-open time belongs to the incident record, not to the four source events. A reviewer should preserve source clocks and UTC conversion information if the underlying systems later become available.

**Further reasoning:** The four event rows are R1 08:40, R3 08:43, R4 08:44 and R5 08:48 UTC. The 09:00 case opening and 09:05 decision are case-workflow timestamps, not additional log events. The sequence supports an ordering statement only. It does not prove that a particular person controlled `desk-a`, that the edits were unauthorized or that the R4 change explains every aspect of R5. The correct handoff names the source for each timestamp and retains the lack of cross-source clock validation in a future real investigation.

### EX006 — Worked result

| Task | Responsible role and authorization | Verification |
|---|---|---|
| Possible booking outage | Analyst and lead may recommend; **service owner** decides whether the disruption is tolerable under the fictional emergency rule; application operator would execute only after approval. | Service owner checks whether booking writes actually stopped and whether essential work has an alternative. No outage is approved in R1–R8. |
| Preserve R1–R5 for the classroom case | Incident lead approves the bounded copy; analyst prepares it from the supplied synthetic table. | Incident lead checks IDs, UTC times, scope and storage note. This is not a production-log export. |
| Coordinate the review | Incident lead names 09:15 UTC or a sooner verified trigger and records who must attend. | Decision record contains the time, owner and unresolved questions. |
| Test a backup restore | Recovery lead designs and, when authorized, performs a contained restore using a copy; the service owner states the expected schedule. | Compare restored booking IDs and values with an authoritative target and measure time. R7 alone is a backup-job status, **not** this verification. |

The table assigns responsibilities within the fictional exercise. A small team may combine human roles while retaining separate approval and result fields.

### EX007 — Worked result

| Seven opening fields | Model 09:00 UTC entry |
|---|---|
| 1. Case ID and opened at | `HL-IR-001`; 2026-10-11 09:00 UTC. |
| 2. Service | Harbor Library room booking; service owner to be confirmed. |
| 3. Reporter and source | Help-desk ticket `T-104`; R5 is a patron **report** at 08:48 UTC. |
| 4. Observed signal and pointers | R1 sign-in at 08:40, R3 B17 edit at 08:43, R4 B18 cancellation at 08:44, R5 report at 08:48. |
| 5. Assessment and uncertainty | Suspicious booking activity; account compromise, approval status of the edits and full user impact **unconfirmed**. R6 notes training but does not resolve those questions. |
| 6. Scope and authority | Current classroom scope: inspect synthetic R1–R8 only; no real-system collection or service change approved. |
| 7. Next question, owner and review | Incident lead asks the service/training owner whether B17/B18 were planned; review the proposed next action at 09:05 UTC. |

This is an **opening** record. A later 09:05 decision can be appended with its own approval and review time. Backdating that decision into the 09:00 entry would distort the case chronology.

### EX008 — Worked result

| Record and time | Supported conclusion | Unsupported conclusion | Follow-up within the exercise model |
|---|---|---|---|
| R6, 08:50 UTC | Front-desk training was scheduled for 08:30–09:00. | B17 and B18 were necessarily approved training edits. | Ask the training owner for the dated task list and approved targets. |
| R7, 08:52 UTC | The previous night's backup job was reported complete. | The booking service can be restored correctly within a given time. | Recovery lead plans a contained restore and value comparison. |
| R8, 08:55 UTC | The supplied network summary has no relevant destination detail. | No data transfer occurred. | Record the missing fields; any further query needs a defined purpose, source, interval and approval. |

Each row preserves a useful observation without upgrading it to a conclusion the source cannot sustain. A missing field is a limit on the claim, not a negative finding.

### EX009 — Worked result

| Option | Expected benefit | Possible cost | Approval and execution | Observable review |
|---|---|---|---|---|
| A: seek temporary restriction of `desk-a` | May stop further edits through that account if it is being misused. | Could interrupt legitimate front-desk work; another path may still exist. | Analyst recommends; incident lead and service owner approve scope and service impact; identity administrator executes. | Check whether access changed and whether essential booking work continues; end or revise the restriction at the recorded review. |
| B: preserve R1–R8, verify B17/B18 with training owner, then decide | Retains the observed sequence and may avoid unnecessary service disruption. | An unauthorized editor could make another change while the team checks. | Incident lead approves the bounded classroom analysis; service owner owns service-impact input. | By 09:15 UTC or sooner on a verified new unexplained edit, compare the owner answer and any authorized new source. |

**Provisional choice:** B under the supplied R1–R8 snapshot, because the training explanation is testable and no continuing change is yet supplied. This is not a universal answer. A verified fresh unexplained edit or high, confirmed service harm could shift the recommendation toward A, but it would still require an explicit approval. R1–R8 neither prove that waiting is harmless nor prove that immediate restriction is necessary.

**Further reasoning:** The provisional option to preserve R1–R8 and ask the training owner about B17/B18 is defensible because the approved task list is a direct discriminator and no later edit is supplied at this checkpoint. Its cost is a possible additional unauthorized edit if misuse is occurring. A verified new unexplained change would trigger prompt reconsideration; it is not currently observed. The alternate request to restrict `desk-a` might reduce misuse through that account, but the response owner would need explicit authority and a plan to test both the suspicious route and legitimate front-desk work. Even after approval, a proposal is not executed until an operator performs it and an appropriate observer verifies the result.

### EX010 — Worked result

“At 09:00 UTC, application records R3–R4 show two booking changes following the R1 `desk-a` sign-in, and help-desk record R5 reports a patron concern; the cause and full service impact remain unconfirmed. The incident lead **proposes** to preserve the supplied records and ask the service owner whether the edits match scheduled training, with an approval decision at 09:05 UTC.”

The first sentence identifies the source and uncertainty. The second describes a proposal, not an action already authorized or completed. Its audience is the internal service owner; a public notification would require a separate approved communications decision.

### EX011 — Worked result

| Hypothetical trigger, **not present in R1–R8** | How it would be verified and why it matters | Owner and next decision |
|---|---|---|
| A later booking-audit row shows a new edit outside a confirmed approved task list. | Application custodian checks the row's source, event time, booking ID and task-list comparison; continued change raises the cost of waiting. | Incident lead promptly reconvenes with service and identity owners to consider a bounded temporary restriction. |
| A service-owner comparison finds several current booking assignments differ from an approved schedule. | Service owner and analyst compare only necessary booking IDs and values; a wider user-facing effect raises potential harm. | Service owner and incident lead reassess service continuity and communication, recording approval before any disruption. |

The exercise asks for **triggers**, not invented case facts. A new signal must be collected or reported within authority and checked before it can support a higher-urgency statement.

### EX012 — Worked result

| Decision-log field | Model entry |
|---|---|
| Time and action | 09:05 UTC: approve a **classroom copy** of synthetic R1–R5 and a question to the service owner about whether B17/B18 were planned training edits. |
| Reason and pointers | R1 sign-in, R3 B17 move, R4 B18 cancellation and R5 patron report establish a sequence; R6 makes training plausible but does not approve the edits. |
| Approver and executor | Fictional incident lead approves the bounded analysis; analyst prepares the copy and records its scope. The service owner receives a **pending** question. |
| Boundary and rejected option | Only R1–R5 are copied; R6–R8 remain available for interpretation. Do not collect a real log or restrict a real account. Immediate `desk-a` restriction is deferred because its service cost and approval have not been resolved. |
| Review and reversal | Reassess at 09:15 UTC or sooner on a verified new unexplained booking edit; consult the lead and service owner before changing access. |

This entry does not claim the service owner has answered, that a production export occurred, or that `desk-a` is compromised. The exact role holders may be fictional, but the decision ownership and status must remain explicit.

**Further reasoning:** At 09:05 the incident lead can authorize a *classroom* copy of the synthetic R1–R5 subset and a proposed question to the training owner. If a learner has not actually made a local copy, the state is "approved exercise; copy not performed," not "collected." If performed, the learner records the real creation time and the actual file or worksheet, without inventing a production export. The training-owner response remains pending. The record should preserve the reason for deferring any account restriction, the service owner to consult and the 09:15 review condition.

### EX013 — Worked result

| Readiness gap | Consequence in this case | Improvement owner |
|---|---|---|
| Service owner and alternate are not confirmed in the opening record. | A booking interruption or account restriction could wait for an unavailable approver. | Incident lead and service manager. |
| Cross-source clock synchronization is not documented. | R1–R8 ordering could be misleading if source clocks differ; the exercise assumes the supplied UTC values. | Identity and application custodians. |
| No recorded restore-test result accompanies R7. | A completed backup job may not yield a correct schedule within an acceptable time. | Recovery lead and service owner. |

**Priority ticket:** within the next readiness cycle, the incident lead records the room-booking service owner, alternate and after-hours contact, plus their decision authority for a simulated outage. **Verification drill:** present both a primary-owner-available and primary-owner-unavailable scenario; require the named decision maker to acknowledge each within the organization's chosen response window and to approve or reject a bounded disruption with reason and review time. Record the two elapsed times and decisions as pass/fail evidence. A published contact page without a successful drill would not close the ticket. A learner may reasonably prioritize clock or restore testing instead if the risk rationale and observable acceptance test are comparably specific.

### Chapter 1 readiness workshop — worked result

**Service card:** case `HL-IR-001`; outcome: residents can see and reserve the correct room; dependencies: staff identity service and booking database; current collection authority: the fictional incident lead permits analysis of R1–R8 only; service owner must be consulted before a booking outage. The identity administrator is listed as the custodian for a *possible* future request, not as someone already interviewed.

**Evidence ledger excerpt:** R1 at 08:40 UTC directly records a successful `desk-a` sign-in; it does not identify the human controlling the session. R4 at 08:44 records B18's cancellation; it does not establish why it was cancelled. R5 at 08:48 records a patron report, not an independently verified account of every symptom. R6 at 08:50 records a scheduled training interval but not the authorized task list. R7 at 08:52 reports a completed backup job but no restore result. R8 at 08:55 has insufficient network detail to support an exfiltration conclusion. A full submission also cites R3 and preserves the original UTC order.

**Decision card at 09:05 UTC:** preserve the supplied records and ask the training owner whether B17 and B18 were planned. Expected benefit: avoid an unnecessary access interruption while testing H1; possible cost: if the account is being misused, another edit could occur before review. The fictional incident lead approves the bounded record analysis; the service owner reviews service impact. Reassess at 09:15 UTC, or sooner if a verified new edit is reported. The rejected immediate-restriction option could reduce further misuse but would disrupt front-desk work and requires explicit service and identity approvals. Neither option is labelled the uniquely correct response.

**Counterfactual kept separate:** if the hypothetical 09:08 edit were verified and outside training, the lead would raise urgency, preserve the new record under an updated scope and seek approval for a temporary account restriction. Once the inject is removed, the original case returns to an unconfirmed cause. The sample earns five rubric points if the full ledger, authority and review trigger are present; a learner who omits the collection boundary must revise it regardless of total score.

**Further reasoning:** An incomplete approver map is resolved by a successful fallback contact and decision rehearsal, not by adding a name to a spreadsheet alone. A meaningful test presents an unavailable primary approver, records when the alternate receives the fictional case, and checks whether an authorized decision with scope and review time is recorded within a locally defined target interval. A logging-readiness gap requires retrieving the predeclared synthetic row and excluding an out-of-range control with saved filters. A recovery-readiness gap requires a separate contained restore and owner-approved booking-state comparison. Neither task is proven by R7's backup-job report. The improvement ticket should state what result constitutes failure and which owner must respond.

### EX014 — Worked result

| Answerable question | Supplied starting point | Authorized next source | Result that changes triage |
|---|---|---|---|
| Was B19 an approved training task? | R9 shows an edit; R10 lists B17/B18 but not B19 | Training owner and a dated, approved task list or addendum | A valid addendum including B19 would strengthen H1; a complete list excluding it would weaken H1 further |
| Are bookings beyond B19 inconsistent with an owner-approved state? | R11 is a patron report; R16 requests an impact check | Service owner authorizes a narrow booking-audit and schedule comparison | Additional confirmed mismatches would increase potential harm and urgency |

The first question tests authorization; the second tests scope. Neither a missing addendum nor an empty narrow query proves the opposite claim without checking source completeness and coverage.

### EX015 — Worked result

| Hypothesis | Support | Contradiction or limit | Narrow authorized check | Result that weakens it |
|---|---|---|---|---|
| H1: training explains the edits | R6 records training; R10 names B17/B18 | R10 omits B19; R12 does not recall that edit | Training owner confirms the complete approved task list and addenda | A complete approved list still omits B19 |
| H2: account used outside the plan | R9 records B19 changed under `desk-a` | R13 omits device and location; R12 is a recollection, not identity proof | Incident and identity owners authorize narrowly scoped session detail | A documented authorized B19 task with consistent identity evidence would weaken this explanation, though not prove every edit was safe |
| H3: patron display and stored state diverge | R11 reports a wrong-looking time | R9 is an application audit edit; a display fault alone does not explain it | Service owner compares patron view, authoritative state and edit history for B19 | Both views show the same incorrect underlying value, weakening a *display-only* explanation |

The hypotheses need not be mutually exclusive. A good answer identifies what each check can and cannot settle.

### EX016 — Worked result

“**Decision owner:** incident lead. **Checkpoint:** 09:20 UTC. **Potential harm:** B19's recorded edit and R11's patron report could affect room use; broader impact has not been measured. **Time sensitivity:** R15 reports 24-hour retention of detailed audit records and a new edit could add harm. **Confidence:** training plausibly explains B17/B18 but does not yet explain B19; account misuse remains a hypothesis, not a finding. **Priority:** prompt, bounded review. **Next action:** seek approved preservation and a service-owner impact check. **Review:** 09:35 UTC or immediately on a verified new unexplained edit.” The reasons and trigger matter more than an arbitrary severity number; “low to moderate” can be replaced by a qualitative uncertainty statement if it is justified.

**Further reasoning:** At 09:20, R9 supports investigating an unexplained B19 edit and R11 supports investigating a reported patron effect. Neither supplies a total impact count. R15 introduces an independent reason for prompt action: detailed booking audit material may be lost under a 24-hour deletion policy. Because the anchor and actual source availability are unknown, the priority note should request an immediate custodian check without publishing an exact expiry. The leading unauthorized-use explanation remains a hypothesis. "Prompt, bounded review" is defensible; a verified fresh unexplained edit or owner-confirmed broader booking damage would justify reassessment sooner than 09:35. A later complete approved task addendum could weaken the authorization concern for B19, but would not remove the need to assess record preservation.

**IM2-linked reasoning:** R9 reports a B19 edit and R11 a patron concern, while R15 makes source availability time-sensitive without establishing the deletion anchor. There is no authorized target/current-state comparison or complete patron population in R1–R16. Preserving the bounded source can be urgent even when confidence in account compromise and quantified service impact is low. If a later owner-approved state check finds a mismatch, reassess potential harm; if a validated approved change explains B19, weaken the unauthorized-use hypothesis. Neither conditional outcome has occurred in Round B.

### EX017 — Worked result

**R13 claim/limit:** the available summary reports one session in its time range, but contains no device or location field. Missing detail cannot identify a device or person; it is not a finding that the session came from the expected staff device. **R14 without T1:** the summary says no further edits after R9 *within its queried range*, but the exact range and filters are absent from R14 itself. **R14 with exercise-only T1:** the illustrative query concerns `desk-a` booking edits in `application-audit` at `09:00 ≤ event < 09:12 UTC`; it does not cover later times, another account, ingestion delay or a different source. A proposed next check asks the authorized application custodian for a new bounded query beginning at 09:12 and ending at a documented, sufficiently ingested cutoff, with source, account filters and completeness recorded. Even a zero-row result would be limited to that new scope.

**Further reasoning:** Canonical R14 states only that its query showed no further edits after R9 within the queried range; its exact start, end, filters, run time and ingestion coverage are not supplied. Optional T1, when explicitly invoked, introduces `application-audit`, account `desk-a` and `09:00 ≤ event < 09:12 UTC`. It does not cover 09:12 itself, later events, another account or delayed ingestion. To investigate later activity, request a newly bounded query with a documented source, filter, interval, run time, collection status and ingestion-health check. R13's one-session summary lacks device and location details. It does not show that the session was on an expected device, and it cannot establish human attribution. A strong answer preserves both the narrower negative-query result and its untested assumptions.

### EX018 — Worked result

| Needed fact | Why the lead asks |
|---|---|
| Which booking-audit source supports R9, which application-audit source produced R14, and which booking IDs and event interval would be selected from each? | Avoid silently merging source paths, copying unrelated patron records or reporting an unrepeatable quiet query. |
| What exactly starts the 24-hour R15 deletion clock, and what is the custodian-confirmed last safe collection time? | R15 alone does not establish whether age is measured from event, ingestion, storage or another policy anchor. |
| Who may approve and perform the export, where will the unmodified copy be stored, and who may read it? | Collection must have authority, restricted access and an identifiable custodian. |

The analyst can ask the incident lead to decide promptly because detailed rows may disappear before the cause is established. The request is for a bounded copy and recorded policy answer, not an unapproved bulk export or a fabricated 09:03-plus-24-hours deadline.

| Comparison at 09:20 | Decision value and loss path | Owner, state and limit |
|---|---|---|
| `P-A` booking and application audits | Could test the B19 edit and R14's quiet-query coverage, if the sources and selection are distinguished. R15 reports a 24-hour deletion rule, but its start point and actual source availability remain unknown. | Incident lead seeks approval; application custodian confirms each source, a narrow selection and policy. **Proposed**, not collected; no current-state or completeness proof. |
| `P-B` identity detail | Could test whether a session key connects records, if both sources share its meaning. R13 omits device/location and no identity-source retention period is supplied. | Incident lead asks identity administrator about availability and minimal fields in parallel. **Proposed**, not collected; no human attribution. |

The comparison does not mean that only `P-A` matters or that urgency authorizes a bulk identity export. A valid answer may choose a different order if it names a documented loss condition and approval path; it must leave unsupported source coverage and actor identity unresolved.

**Further reasoning:** A complete P-A request asks which producer emitted the R9 booking audit and which produced R14's application-audit summary before proposing that their rows be joined. It names B17–B19, a bounded event range, minimum necessary fields and the application custodian. The custodian must establish **what starts** R15's 24-hour clock and whether the oldest relevant detailed row is still accessible. The incident lead owns approval, and the retained object would need its own source, method, access and collection receipt. At the supplied 09:20 state, P-A and P-B remain **proposed**; P-B can investigate identity-detail availability and its unknown retention in parallel. Neither request is an approved export, an effective hold or a verified copy. The inability to compute a deadline is an explicit result, not a reason to defer contacting the custodian.

### EX019 — Worked result

| Collection-note field | Model entry before a learner runs the optional fixture |
|---|---|
| Case/item and state | `HL-IR-001/E1`; **planned classroom transcription**, not a completed export |
| Source and event range | Synthetic book records R9 at 09:03 UTC and R14 at 09:12 UTC; R14's underlying query interval is unspecified unless the separate T1 card is explicitly used |
| Collector and authority | Learner analyst, within the fictional incident lead's classroom scope for supplied records only |
| Collection time and location | **Not applicable until a file is actually created**; then record the learner's real local time, file path and access restriction |
| Transformation and original | Fixture transcribes two rows as UTF-8 text; the book table is the retained source of the classroom transcription |
| Limitation | No production log was acquired; a saved file cannot prove the source system's completeness, clock or identity attribution |

If the learner ran `fixture.py`, replace the planned state with **completed local fixture**, record the actual creation time and scratch path, and attach the measured 235-byte SHA-256 value from the lab. Never invent a 09:20 collection time simply because the scenario's discovery checkpoint was 09:20.

### EX020 — Worked result

| Claim | Supported? | Reason |
|---|---|---|
| The named `E1.txt` produced equal SHA-256 values at the two recorded checks | Yes, if the learner actually measured and retained both values | This is the direct comparison of the checked bytes under the stated method. |
| No byte change was detected in that named copy between the checks | Yes, within the hash method and trustworthy-check assumptions | Equality supports a limited consistency finding, not a broader provenance claim. |
| The original application log was complete and true | No | E1 is a transcription; the digest cannot reveal omitted or false source rows. |
| The source clock and actor identity were correct | No | A digest has no independent clock or identity context. |
| The export or collection had organizational authority | No | Permission is a decision record, not a property of the digest. |

Specify the file, method and check times. Two matching values copied from the same mistaken note would not become proof of authenticity.

**Further reasoning:** If the learner actually created E1 and repeated the stated SHA-256 checks, the equality supports consistency of the **named copy bytes** at those checks, subject to method and record trust. The modified E1 variant with a different digest establishes only that the modified teaching bytes differ from those of E1. The **source layer** is not authenticated by the digest: E1 was transcribed from the synthetic R9/R14 table, and the underlying canonical R14 query manifest is incomplete. The **interpretation layer** also remains uncertain: none of the copied bytes proves who controlled `desk-a` or whether B19 was authorized. A 2-point answer must name the file and distinguish copy consistency from provenance, complete coverage and permission; generic claims that the evidence is "verified authentic" fail that boundary.

### EX021 — Worked result

| Order | Record and supplied UTC time | Source |
|---:|---|---|
| 1 | R9, 09:03 | Booking audit: B19 edit |
| 2 | R10, 09:04 | Training plan: B17/B18 named |
| 3 | R12, 09:08 | Staff interview note |
| 4 | R15, 09:14 | Retention notice |
| 5 | R16, 09:16 | Service-owner note |

These are **record event or observation times** in the fictional dataset. The learner first receives R9–R16 at the simulated 09:20 review. R10's timestamp is the time of the supplied plan record, not proof that the plan itself was first written after R9. Ordering cannot establish who made the B19 edit, whether it was authorized or whether it caused the patron's report. If optional T1 is used, its interval ends before 09:12; it supplies no coverage of later activity.

### EX022 — Worked result

“At 09:20 UTC, `HL-IR-001` concerns the room-booking service: R9 records B19 edited and R11 records a second patron report. H1 can explain the earlier training edits, while H2 remains possible for B19 because R10 omits it and R13 gives no device detail. The fictional incident lead authorizes classroom preservation of supplied records and asks the service owner to approve a **proposed**, narrow real-world impact check; no production account or data change has occurred. The analyst will ask the training owner about any approved B19 addendum and record source and query limits. Review with the incident lead at 09:35 UTC or sooner if another verified unexplained edit appears.” A handoff must tell the receiver what was approved, what remains only a request and what would change the next decision.

**Further reasoning:** At 09:20 UTC, case HL-IR-001 concerns Harbor Library room bookings: R9 reports a B19 edit, while R11 records a second patron complaint. The supplied training plan in R10 names B17/B18 but not B19, so authorized training and use outside the plan remain competing explanations; the operator is not identified by R13. R14's quiet query does not establish complete subsequent activity, and R15 reports a 24-hour detailed-audit deletion policy without a verified anchor or deadline. The incident lead **proposes** a bounded P-A availability/preservation request through the application custodian and a service-owner impact check; no production copy, hold or account restriction is claimed completed. Review at 09:35 UTC or earlier on a verified unexplained booking change.

The five sentences label the evidence, assessment, unanswered questions, proposed action and review trigger. A classroom preservation authorization, if separately recorded, must not be misreported as a production export.

### EX023 — Worked result

**Proposed request:** ask the service owner to approve a named analyst to compare booking-edit audit rows for the short 08:30–09:20 UTC window with the authoritative booking state and relevant help-desk ticket identifiers, using only booking ID, changed field, old/new value, event UTC time and approved target where available. If approved, the application custodian would supply a restricted copy and record the query filter, source and collection time. The expected result schema is `booking ID | audit row | current value | owner-approved value or pending | confirmed mismatch / unresolved`. The learner can already point to B19's R9 edit but cannot supply a final count or approved target from R1–R16. Keep patron names and unrelated bookings out of the classroom output and limit the copy to the approved reviewers.

**Further reasoning:** A well-scoped request proposes comparing the B19 audit row, any approved relevant booking targets, the current authoritative state and the patron-facing information needed to evaluate R11. The service owner would approve the business comparison; the application custodian would then confirm the exact source and selection. **Positive hypothetical result:** an authorized read shows the owner-approved B19 value reflected correctly in current authoritative state for the tested item; this narrows one state question but does not establish every patron view or the actor's identity. **Negative hypothetical result:** the current state is missing, conflicts with the approved target, or cannot be compared because the target or source is unavailable; the learner must record a mismatch or unresolved state, not invent a full impact count. The requested view excludes unrelated patron names, the newsletter list and unapproved bookings. No actual result is supplied in R1–R16.

**IM2-linked measurement contract:** Count distinct selected booking IDs only after declaring the owner-approved target, source version, current authoritative state and comparison time. Keep the reason each row was selected. B17–B19 may form a bounded inquiry frame, but R1–R16 have no completed authoritative comparison. Proposed result columns are `booking ID | audit pointer | report pointer | approved target/version | current value/time | match/mismatch/unverified | limit`. A mismatch for one valid tested row is not an estimate of affected patrons. In the **separate invented IM2 exercise**, six encountered IDs yield two matches, two mismatches and two unverified classifications; four reports reference three distinct booking IDs. X04 has no report but is a mismatch under the fictional comparison; X05 has a report but lacks a target. Removing X04’s target changes its label to unverified without repairing any state. These are classroom outcomes only.

<a id="ir-rapid-ch02-im2-result"></a>

### IM2 — Worked result

**Exact expected output, executed with the fixture:**

~~~text
reports: 4 unique_booking_refs: 3
X01: MATCH
X02: MISMATCH
X03: MATCH
X04: MISMATCH
X05: UNVERIFIED
X99: UNVERIFIED
counts: MATCH=2,MISMATCH=2,UNVERIFIED=2
negative_X04_target_removed: UNVERIFIED
~~~

#### Worked interpretation

Four report rows refer to only three distinct booking IDs: X02 appears twice, while X05 and X99 each appear once. This is **not** a count of distinct people. Report count and distinct business-object count answer different questions.

The examined comparison contains two matches, X01 and X03. X02 and X04 are mismatches under the declared synthetic target/current inputs. X05 is unverified because its target is missing, even though a current value exists. X99 is unverified because neither the target nor the current comparison row is supplied; a report references it, but the ledger has no authoritative state for it.

The laboratory demonstrates a nonreported mismatch: X04 is a mismatch in the supplied comparison even though no help-desk ticket in `REPORTS` references X04. Conversely, a reported concern about X05 does not by itself prove that the current value is incorrect. This is why a report-only sample cannot reliably characterize every state discrepancy.

The negative variant removes only X04's reference value. Its classification becomes `UNVERIFIED` rather than `MISMATCH`. No simulated current booking state changed. The shift is caused by weakened **evidence**, not by an automatically repaired business condition. Restore the original target after the variant and retain both results distinctly.

The defensible classroom statement is: "Of six identifiers encountered across these small supplied sources, two match, two mismatch and two cannot be evaluated; four reports cover three distinct booking references. These numbers characterize only the IM2 fixture, not Harbor Library's complete bookings or patrons."

#### Reproducibility and limitations

The code checks exact string equality, not room availability rules, approved changes, person-to-booking relationships, clock normalization or database consistency. `None` is a local missing-value convention; a real schema must distinguish missing, null, deleted and legitimately empty state according to producer semantics.

A production analyst would require source identifiers, selection manifest, approval owner, effective target version, authoritative current-state timestamp and privacy/access controls before treating the comparison as evidence. The toy script supplies none of those provenance receipts, and its computed results must never be called a measured incident impact.

**Required learner artifacts:** Copy the nine-line output; produce a six-row impact ledger with evidence status and source limitations; explain in two sentences why "four affected patrons" is unsupported; and report exactly what changed in the negative test. A response fails if it equates report count with affected people, silently discards X99, claims all bookings were examined or treats the variant as a correction.

### EX024 — Worked result

| Hypothetical new observation | Who verifies it and why it changes triage | Decision response |
|---|---|---|
| A fresh booking-audit row after the 09:20 review shows a new unexplained edit | The application custodian confirms the row, source clock and booking impact; ongoing change raises urgency. | Incident lead reconvenes immediately with the identity and service owners to compare containment options. |
| A bounded owner-approved comparison finds several currently incorrect room assignments | The service owner and analyst verify identifiers against an authoritative schedule; confirmed scope raises potential patron harm. | Incident lead and service owner promptly reconsider write restrictions and patron-service communication. |

Neither observation is part of R1–R16. A confirmed sensitive-data disclosure would also raise harm, but no supplied record establishes one. The triggers are evidence requirements, not predictions.

### EX025 — Worked result

“R9 records a B19 booking edit under `desk-a`, and R11 records a patron's report. R13 omits device and location detail, while R8 lacks destination detail; neither establishes who controlled the session or whether information was transferred. The incident lead will seek a service-owner impact comparison and authorized identity details before revising scope or attribution.” Removed unsupported claims: a named **attacker stole** the account; **every** booking was edited; and the patron database was **exfiltrated**. The correction does not replace those false positives with an equally unsupported claim that no transfer occurred.

### EX026 — Worked result

| Review field | Model note |
|---|---|
| Peer claim | “R6 and R10 confirm H1 for all edits.” |
| Directly supported | R6 says training was scheduled; R10 lists B17 and B18 in the plan. R9 separately records a B19 edit; R12 reports that the staff member does not recall it. |
| Missing discriminator | A complete approved task list or dated addendum naming B19, plus a narrow authorized check of the account and application edit context. |
| Possible update | A valid pre-existing B19 addendum would strengthen H1 for that edit, though identity still needs checking; a confirmed complete plan excluding B19 would weaken H1 for B19. |

Treat the conclusion as unresolved until the owner and record checks are assessed. A constructive review explains how to change the conclusion; it does not accuse the staff member because recollection and audit attribution can both have limits.

### Chapter 2 synthetic-extract lab — worked result

The script writes **235 bytes** to each file. The SHA-256 digest for `E1.txt` is `dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37`; the digest for `E1-modified.txt` is `15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d`. The strings have equal byte length because the single ASCII digit `3` was replaced with `4`; their different digests show the modified copy is not byte-identical to the saved original. Learners should calculate the values locally rather than trust a copied answer.

A model note is: “`HL-IR-001/E1`; synthetic classroom extract transcribed from book records R9 and R14; event times 09:03 and 09:12 UTC; learner-created local file `E1.txt` in a scratch directory at the learner's actual collection time; classroom authorization permits only this supplied material; 235 bytes written by `fixture.py` without a live source; SHA-256 digest recorded above; working copy stored locally and deleted after the exercise.” The collection time should be the learner's actual time, not an invented 09:18 UTC. The output is **not** an original application log, and R14 covers only its queried range. Matching digests after a repeat check support byte consistency of the checked copy; they do not prove authorized account use, complete source records or the cause of B19's change.

### Chapter 2 temporal-coverage lab — worked result

The optional Python script prints the following three lines for the supplied fixture:

```text
R9 event=09:03 UTC seen=09:20 UTC delay=17 min
R10 event=09:04 UTC seen=09:20 UTC delay=16 min
R15 event=09:14 UTC seen=09:20 UTC delay=6 min
```

R10's original exercise text is `2026-10-11T05:04:00-04:00`; adding the explicit four-hour offset yields `09:04 UTC`. The three delays are `09:20 − 09:03 = 17`, `09:20 − 09:04 = 16` and `09:20 − 09:14 = 6` minutes. The event-time order is R9, R10, R15; the learner receives all three only with the Round B release at 09:20. None can justify the learner's 09:05 decision retroactively.

With exercise-only T1, the strongest negative statement is: “The specified `application-audit` query for `desk-a` booking edits in `09:00 ≤ event < 09:12 UTC` showed no further matching edit after R9.” R14 *without* T1 lacks those exact bounds. Neither version proves that no edit occurred after 09:12, through another account or in an unexamined source. A bounded request to the authorized application custodian should specify source, account filters, the new interval, an ingestion/completeness check, collector and collection time. R15 calls for a prompt retention decision; the exact deletion instant depends on policy detail not supplied here. A full-credit answer records these limits rather than filling gaps with confident words.

### Chapter 2 delayed-arrival T2 replay — worked result

The optional in-memory program prints:

```text
09:12 L1
09:20 L1,L2
```

Both runs use the same account filter and **09:00 ≤ event < 09:12 UTC** window. L1 qualifies in both. L2's event time is 09:10, so it belongs to that window, but its 09:18 ingestion time makes it invisible at the 09:12 query cutoff and visible at 09:20. L3 is excluded because its account is `helper-b`, even though its event and ingestion times are inside the interval. L4 is excluded because 09:12 is the *exclusive* end; its later ingestion time is not the reason it fails this particular selection.

The strongest correction is: “At 09:12, the specified query showed no other visible matching edit after L1; this did not establish that the event-time interval was complete.” In the T2 replay, the repeated query would later reveal L2 and require a fresh assessment, but **L2 is not a canonical Harbor Library case fact**. The next request is to the fictional application/logging custodian: “Please confirm the exact source, `desk-a` account filter, half-open event interval, each query's run and ingestion cutoff, and whether collection or indexing lag could leave relevant rows unseen; provide a scoped follow-up result under the incident lead's approval.” The custodian's reply, not the newest event timestamp alone, would determine what completeness claim is defensible. None of the four L rows establishes the human operator or intent.

### Chapter 2 evidence-package peer audit — worked result

| Variant | Byte and manifest finding | Defensible classroom use | Blocked claim and repair request |
|---|---|---|---|
| A: expected E1 bytes and full manifest | If recalculated, 235 bytes and the recorded SHA-256 match the learner's copy; the script explains the teaching transformation. | Demonstrate consistency of the checked synthetic copy and discuss its stated limits. | It cannot prove R14's source query was complete. Ask for an authorized source/export record and exact selection metadata before making an operational coverage claim. |
| B: modified bytes labeled E1 with the original digest | A repeat digest would differ from the recorded E1 value. The copied label does not repair the mismatch. | Use as a deliberate failure example after labeling both variants accurately. | Do not rely on the disputed file for an incident claim. Ask the sender for the original file, creation and transfer steps, and an explanation of which bytes changed; retain both versions in this exercise. |
| C: exact E1 bytes but no selection or authority | The digest can still match, but it answers only the byte-comparison question. | Demonstrate why integrity is distinct from provenance and permission. | Do not assert complete source coverage or authorized collection. Ask for the source, selection rule, operator, scope and authority record. |

A handoff that preserves these limits can say: “We can reproduce the digest of the supplied synthetic E1 bytes; we have not verified an original application export, its query completeness, a real collector's authority or the identity behind `desk-a`.” This is a better answer than “the evidence is authentic” because the latter does not identify *which* link was checked. The peer-audit drill is supplemental; it does not increase the count of 50 numbered exercises.

### Chapter 2 Q1 correlation lab — worked result

The unmodified Python fixture in section 2.9 prints exactly:

```text
E-A: AMBIGUOUS_WINDOW_CANDIDATES candidates=S-A,S-B
E-B: KEY_AND_WINDOW_MATCH candidates=S-B
E-C: NO_WINDOW_MATCH candidates=-
E-D: EXPLICIT_KEY_UNMATCHED candidates=-
```

| Edit | Why the supplied rule gives that result | What it does **not** establish |
|---|---|---|
| E-A | At 09:05, `desk-a` has overlapping S-A (09:00–09:15) and S-B (09:02–09:12); the application row has no session key. | It does not choose a session, let alone identify a human. “Two candidates” is not a 50/50 probability estimate. |
| E-B | At 09:07, both `desk-a` windows include the event, but the application supplies `S-B`, which survives the exact-key check in this fixture. | A matching row does not prove the account's user, intent, source authenticity or authorization. |
| E-C | At 09:18, neither supplied `desk-a` interval covers the event. S-C covers that time but belongs to `front-b` and is excluded by the account rule. | No match in Q1 does not prove no session existed; the table may omit a session, have different coverage or use an incorrect clock. |
| E-D | At 09:06, both `desk-a` windows cover the time, but neither has the explicit `S-X` key. The method refuses to fall back silently to account/time. | It does not prove the application row is fraudulent; the source, field mapping or export may be incomplete or inconsistent. |

**Bounded request:** “Incident lead: please authorize the identity and application custodians to provide the source identifiers, query filters and actual event/collection ranges for the Q1 teaching interval, plus a documented check of each source clock and whether both `session_id` fields use the same namespace. If a real case required it, request only the session and application rows relevant to the edit interval under the organization's approved collection and privacy rules. Record any omitted range or transformation, and return an evidence pointer rather than declaring the account's human operator.” In this book Q1 is already the entire permitted fixture; the sentence models the *fields to request*, not an instruction to contact a real custodian.

**Q1-V key-removal variation:** replace E-B's explicit `S-B` with a blank field while leaving all other rows unchanged. Its 09:07 `desk-a` event then has two account-and-time candidates, S-A and S-B, so it becomes `AMBIGUOUS_WINDOW_CANDIDATES candidates=S-A,S-B`. E-A, E-C and E-D keep their original classifications. The changed label comes from weaker correlation information, not from a newly discovered attacker or edit. If a student instead renames S-X to S-A, that is a **different** variant and must be labeled separately; the Q1-V task changes only one E-B field.

Award the six rubric points only when the candidate sets, limits, authorized request and variant are all present. The table and code use the same half-open interval rule, so an event exactly at S-A's 09:15 end would not match S-A. A reviewer who uses an inclusive end, silently discards E-D's explicit key or reads R13's canonical one-session summary into Q1 has changed the stated exercise input and must revise the answer. This lab is supplementary; the book still contains exactly 50 numbered exercises.

### EX027 — Worked result

| Proposed action | Primary goal | Prerequisite | Observable check | Limit |
|---|---|---|---|---|
| Revoke current `desk-a` session | **Containment:** reduce the ability of that session to make further edits. | Incident-lead and identity-owner approval under the exercise policy; retain narrow records when safe. | Identity administrator confirms the specific session ended; analyst checks a defined later booking-audit interval. | Other sessions, accounts and a non-identity cause may remain. |
| Reset a credential | **Possible eradication** only if authorized evidence supports credential compromise as a cause. | Identify the credential and mechanism, approval from the identity owner, and a plan for dependent sessions or tokens. | Confirm the old credential no longer authenticates and check related paths under approved scope. | A reset does not repair an application fault and may not invalidate every existing session. |
| Restore a booking copy in an isolated environment | **Recovery verification** of a particular copy and procedure. | Recovery-lead test authorization, a copy identifier, an expected owner-approved target and isolated environment. | Compare restored B17–B20 values and measure time and access/audit behavior. | A successful test of a copy is not proof that the live schedule is correct or safe to reopen. |

At 09:37 these are classifications and proposed checks, **not executed events**. R23 reports a prior backup success but gives no current restore result.

### EX028 — Worked result

**Before the new release:** at the 09:20 Chapter 2 review, R9 showed a 09:03 B19 edit, R10 named B17/B18 in the training plan, and R12 supplied a staff recollection. B19 remained unexplained; H1 could plausibly explain the earlier planned edits but did not cover every known item. **New at 09:37:** R17, recorded 09:22, says the approved task list named B17/B18 only and no addendum was known. R18, recorded 09:24, adds a B20 edit under `desk-a`. The new edit falls outside the known task list and raises concern about continued booking changes. H1 as a **complete explanation of all four bookings** weakens; H2, account use outside the plan, gains plausibility. Neither R17 nor R18 identifies the human, device, mechanism or root cause. An unrecorded authorized change, a faulty process or a source error remains possible until checked. Event time is not the time the learner knew the item; do not justify the earlier 09:20 decision retroactively.

### EX029 — Worked result

| Option | Intended effect and uncovered path | Operational cost | Approval and executor | Verification and reversal |
|---|---|---|---|---|
| Revoke current `desk-a` session | Stop edits through that session; other sessions and non-identity paths remain possible. | Expected staff reauthentication and possible desk delay. | Incident lead and identity owner approve; identity administrator executes a named-session action. | Administrator confirms revocation; analyst checks a new, bounded audit interval and service owner checks desk impact. A verified staff member can reauthenticate through the approved process if service work must resume. |
| Pause staff booking writes for fifteen minutes | Stop the staff write workflow; does not settle cause, read exposure or an alternate write path. | Manual queue and potential patron delay. | R21 records service-owner **tolerance**; owner must still approve the actual pause and application operator executes it. | Operator verifies write block in the approved scope; owner inspects queue and booking state before approved resumption. |

**Provisional 09:37 choice:** request session revocation first because it targets a narrower active path and preserves other staff workflows, with the short pause ready if a verified edit continues. A pause-first answer also passes if it justifies why the session link is too weak and plans the manual queue. Neither choice proves who caused the edits.

### EX030 — Worked result

**Decision card, 09:37 UTC:** the fictional incident lead accepts a ten-minute observation window through **09:47 UTC**, after consulting the service owner about possible booking harm. The application custodian is asked to run a bounded query for staff booking edits from 09:37 to 09:47 UTC, recording source, filters, event-time bounds, ingestion cutoff and actual collection time. R22's narrow earlier summary does not cover this proposed interval. A verified new unexplained booking edit, a service-owner-confirmed impact increase, or unavailable/incomplete logging ends the observation choice early and triggers an immediate lead review of revocation versus write pause with the identity and service owners. The accepted downside is that another wrong booking may occur while the team waits. If the query cannot run or ingestion lags beyond the review, the team must **not** report “no later edits”; it must decide under explicit reduced visibility. An unverified quiet dashboard is not a verification result.

### EX031 — Worked result

| Narrow item to preserve or request | Purpose | Custodian and authority | Limit |
|---|---|---|---|
| R18 B20 booking-audit row and related B19 R9 row | Preserve the two edit times, IDs and values before R15's retention window removes detail. | Incident lead authorizes a bounded request to the application custodian; actual export status and collection time must be recorded. | Audit account label does not prove the human operator. |
| R13 current-session summary and an approved detail request | Reconstruct the specific session considered for revocation. | Identity administrator under incident-lead and identity-owner scope. | R13 itself lacks device and location detail; do not invent those fields. |
| R10 plan plus R17 training-owner statement | Compare approved tasks with B19/B20 and retain the provenance of the owner's answer. | Training owner supplies the authorized plan; analyst records its date and completeness question. | A plan may be incomplete or superseded; R17 says no addendum is *known*, not that one is impossible. |
| R20 restricted booking-state comparison copy | Check current B17–B20 state before any correction. | Service owner controls the copy and grants necessary access to the analyst. | The supplied R20 note does not provide row values; do not substitute later C1 values into the 09:37 record. |

If a verified sequence of harmful edits is continuing and waiting for all four requests would prolong harm, the lead seeks approved containment promptly. The case note then lists which items were preserved, which were merely requested, which could not be obtained in time and why. A bulk patron export is not necessary to answer the narrow booking question.

### EX032 — Worked result

**Correction:** “At 09:37 UTC, revocation of the current `desk-a` session is **proposed** as containment; if approved and later confirmed, it would address only that session. The supplied R1–R24 records do not identify the human operator, establish credential compromise or exclude another session, account or application fault. Eradication is not established until an authorized, cause-specific change is tested with reliable state and audit evidence.”

| Hypothesis | Supplied support and limit | Authorized discriminator and weakening result | Conditional fix and verification |
|---|---|---|---|
| Credential or session misuse | R18 associates the B20 edit with `desk-a`; R17's task list does not approve B20. Neither record attributes a person or proves credential theft. | Identity owner requests bounded session and token events matched by IDs to the B20 edit. A verified different principal or a route that works without the session would weaken this claim. Missing older-session events limit a negative result. | **Only if supported:** owner-approved credential/session changes, then a synthetic old-credential attempt that fails, a legitimate new-credential attempt that succeeds, and audit/state evidence with the relevant time window. Other tokens remain a separate check. |
| Application authorization fault | B20 changed outside the supplied task list, but R1–R24 contain no reproducible application-fault test. | Application owner attempts the same kind of edit with an unauthorized synthetic identity in an isolated pre-change copy. A reliable denial with unchanged state would weaken this mechanism for that build and route, not all builds and routes. | **Only if reproduced:** a scoped server-side fix, repeat of the failing request that is now denied with unchanged state and linked audit, plus an authorized synthetic edit that still succeeds. Monitor other routes and re-open on an unexplained state change. |

R22 was recorded at 09:32 UTC, before the proposed 09:37 revocation. Its unspecified queried range cannot verify a later action, and a zero result within a narrow range would not distinguish cause removal from a missed edit. A learner may write a *conditional* “after approval and execution” note but must not turn the later Chapter 4 branch into evidence at this checkpoint.

### EX033 — Worked result

**Plan:** after P1 is released, the recovery lead requests permission to restore an identified backup into an isolated environment. Record copy ID, source timestamp, actual restore start/end, tool and access scope; none is supplied by R23. Use P1 as the service-owner-approved comparison target, preserving original copy and test results. Limit classroom output to booking IDs and room/cancellation values; do not change live bookings or disclose patron fields. A pass requires an actual measured restore with every target row correct, recorded time, acceptable access checks and an auditable result. Until then the state is *not tested*.

| Booking | P1 expected state | Restored observation | Current result |
|---|---|---|---|
| B17 | Room 4 | Not supplied | Not tested |
| B18 | Cancelled | Not supplied | Not tested |
| B19 | Room 1 | Not supplied | Not tested |
| B20 | Room 3 | Not supplied | Not tested |

After a real isolated restore within the fictional approved scope, fill the observed column and mark each row pass or fail. Then test one authorized and one denied **synthetic** edit and check the audit's UTC time and actor. V1 is a separate supplied isolated-copy trial whose actor field is blank; it is not a completed backup restore. A plan alone cannot establish that the service is recoverable or that a later production correction ran.

### EX034 — Worked result

R23 establishes that a backup job succeeded and that the most recent documented restore test was thirty days earlier. In the **hypothetical** section 3.5 example, a midnight copy is 9 hours 45 minutes old at 09:45. If it were the only recoverable data source, its age exceeds the illustrative thirty-minute RPO by 9 hours 15 minutes; it cannot by itself demonstrate that target. The two-hour RTO cannot be assessed from R23 because no restore duration or successful service-acceptance time is supplied. The recovery lead must perform an authorized isolated restore, compare the restored data with P1 or another approved target, and measure elapsed time and access/audit checks. A successful backup job does not replace either check.

### EX035 — Worked result

| Acceptance check | Expected result | Current supplied state | Owner and next action |
|---|---|---|---|
| Booking correctness | New restricted comparison copy matches P1 for B17–B20 after approved correction. | **Fail/pending:** C1 matches B17/B18 but B19 and B20 are reversed against P1. | Service owner approves bounded correction; authorized operator acts; analyst checks a **new** copy. |
| Access behavior | Approved synthetic staff role can edit; tested unauthorized role is denied. | **Limited pass in isolated copy:** V1 reports both observed outcomes, but not every account or live path was tested. | Identity and application owners define the acceptable production-scope verification before full release. |
| Audit visibility | Authorized test change is recorded with correct actor and UTC time. | **Fail:** V1 has a UTC time but blank actor. | Application/audit owner repairs attribution and reruns the test; incident lead records interim monitoring. |

**Proposed status:** do not declare unrestricted return to service. The service owner and incident lead may consider a time-limited restricted mode with a compensating check, named owner and near-term review, but the failed booking and audit criteria remain open. An unexplained new edit or failed manual-queue reconciliation triggers renewed restriction or escalation. A loading page or backup-success label does not override these observable failures.

### EX036 — Worked result

| Field | Model decision card at 09:37 UTC |
|---|---|
| 1. Time and status | 09:37 UTC, **proposal; not executed**. |
| 2. Evidence and uncertainty | R17's approved list names B17/B18; R18 shows B20 changed at 09:24. Account operator and cause unknown. |
| 3. Chosen action and scope | Revoke only the identified current `desk-a` session; preserve narrow available records if doing so does not delay harm reduction. |
| 4. Approver and executor | Incident lead and identity owner approve under fictional policy; identity administrator executes only after approval. |
| 5. Intended effect and side effect | Try to stop edits through that session; legitimate staff may need to reauthenticate and booking work may slow. |
| 6. Verify, fallback and review | Check a specific identity revocation result, later bounded booking audit and desk impact at 09:45 UTC. If a verified edit continues, seek service-owner approval for a fifteen-minute write pause under R21's stated tolerance. |

R21 does **not** mean the fallback has already been implemented. Before any Chapter 4 branch result is released, a completed-action sentence is unsupported.

### EX037 — Worked result

**Claim:** the booking page loads after a hypothetical approved session revocation. **Limit:** a page response tests availability at one moment; it says nothing by itself about schedule correctness, authorization of edits or the completeness of later audit coverage. **Question 1, booking state:** are B17–B20 consistent with a service-owner-approved target? The service owner authorizes a restricted comparison and owns any correction; R20 says a copy is available but does not supply the row values at 09:37. **Question 2, continued change:** did an approved, sufficiently ingested audit query after the intervention show any new unexplained edit? The application custodian records source, interval, filters and cutoff; R22 is earlier and cannot answer. **Proposed status:** keep the case open with a named review and possible restricted service. R24 says no current record establishes access to another personal-data store, but it cannot close an exposure question by proving absence.

### EX038 — Worked result

**Pause-first proposal at 09:37 UTC:** assume the observed B19/B20 edits may not be limited to the one current session, and assume front-desk staff can safely record new requests in the manual queue for fifteen minutes. R21 supports the owner's tolerance for that cost, **not** a completed pause. Ask the service owner to approve a named fifteen-minute write restriction; the application operator implements it under that approval. Verify immediately in the approved test scope that staff booking writes are blocked while the manual queue captures requests, then inspect a new bounded audit interval. Review with the owner at 09:52 UTC, account for every queued request against an approved schedule and get explicit sign-off before resuming writes. If the block does not work, patron harm becomes unacceptable, or authorized identity evidence identifies a narrower safe action, the incident lead and service owner should reconsider revocation or a different control. The pause reduces one class of harm while leaving cause and other paths unresolved.

### Chapter 3 reconciliation lab — worked result

**Row-by-row comparison:** B17 and B18 already match the P1 approved target. B19 is Room 3 in C1 but should be Room 1; B20 is Room 1 in C1 but should be Room 3. The service owner must approve those two bounded corrections against the authoritative schedule before an authorized operator makes them. The analyst should retain the pre-correction C1 values, record the approval and later compare a new restricted copy with P1. The lab does not imply that a correction has actually been executed.

**V1 claims:** The supplied test supports that an authorized synthetic staff account can create a booking and that the tested unauthorized identity cannot perform the same edit. It **contradicts** the claim that this test's audit record identifies the actor, because the actor field is blank. These two access checks do not cover every identity or access path. An audit timestamp alone does not make the change attributable.

**Branch and acceptance:** In Branch S, confirm the old session was revoked and monitor for new changes, but keep other sessions and the unresolved cause on the case record. In Branch P, the service owner must reconcile both queued requests before approving resumed staff writes. An acceptable proposal is *restricted or conditionally monitored service*, with the service owner and incident lead recording whether a temporary compensating check can cover the missing actor field while the application/audit owner repairs it. Set a named next review and reapply a restriction or escalate if an unexplained edit recurs. Neither branch, P1 nor V1 alone establishes full recovery. Award the five rubric points only if the row mismatches, correction authority, V1 limitation, branch cost and honest acceptance state are all explicit.

### Chapter 3 CSV comparison lab — worked result

Executing the complete Python 3 fixture in section 3.7 with the supplied strings prints:

```text
B17: MATCH target=Room 4 current=Room 4
B18: MATCH target=Cancelled current=Cancelled
B19: MISMATCH target=Room 1 current=Room 3
B20: MISMATCH target=Room 3 current=Room 1
counts: MATCH=2, MISMATCH=2, MISSING_CURRENT=0, UNEXPECTED_CURRENT=0
rejected variant: current: duplicate booking ID B20
```

The comparison performs **no repair**. It says B17 and B18 match the P1 target in this transcription; B19 and B20 do not. `MISSING_CURRENT=0` and `UNEXPECTED_CURRENT=0` are statements about the four supplied CSV rows, not proof that the live database has no missing or extra bookings. Appending a duplicate B20 is rejected because two rows with the same key would make a naive last-write-wins comparison order-dependent. The program's header and field checks defend the classroom fixture against simple malformed input; they do not authenticate a source, establish owner approval or handle a production CSV dialect and all possible data errors.

A responsible next artifact is a **request** for the service owner to confirm the approved P1 target and authorize correction of B19/B20 only. Record the C1 copy's provenance, the planned operator and a new post-change comparison. Keep the cause, other bookings and V1's failed actor attribution open. If the malformed variant is tested, label its rejection as a validation result, never as a fifth Harbor Library booking event.

### Chapter 3 real-case source reading — worked result

| Reported fact and location in the [British Library review](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=) | Harbor Library planning question | Unsupported leap to avoid |
|---|---|---|
| The British Library reported secure collection copies but an infrastructure obstacle to restoration (executive summary, pp. 2–3). | Does the recovery lead have an isolated platform on which a named booking copy can actually be restored and timed? | “R7 says Harbor Library can restore within ten minutes.” R7 has no restore measurement. |
| The British Library reported partial catalogue return while other research services remained restricted (pp. 2 and 9–10). | Which room-booking functions must work, with correct B17–B20 state, before the service owner accepts a limited return? | “A loaded booking page means all Harbor bookings and controls are correct.” |
| The British Library described crisis groups approving workarounds and coordinating communications (section 3, pp. 12–13). | Who approves a manual booking queue, who reconciles it and how will users receive a bounded update if ordinary channels fail? | “The fictional analyst has authority to pause a real service.” The two organizations' authorities are separate. |

The report is dated **8 March 2024** and discusses an incident in **October 2023**. Its findings must be read as a dated institutional account, not a live service dashboard or an independent forensic dataset. A good answer names both the supported fact and the decision it motivates without importing British Library facts into R1–R24. The exact initial intrusion point remains uncertain in the report; a learner who states a definitive entry mechanism from this source must revise the claim.

### Chapter 3 backup-candidate lab — worked result

This model uses K1 only as an optional replay **after** P1/C1 and V1. Each `PASS` below is restricted to the stated check; it is not a certificate for the entire candidate. A real assessor would ask for the missing provenance before relying on the listed snapshot times or digests.

| Candidate | Gate | Result and supplied reason |
|---|---|---|
| K-A | Provenance and permission | `UNKNOWN`: K1 supplies a time and local digest comparison, but no independent source or capture chain. The exercise permits only isolated classroom inspection. |
| K-A | Copy integrity and usability | `PASS` for the **supplied limited trial**: digest matched and a four-row isolated import was read in 14 minutes. Other tables and dependencies are untested. |
| K-A | Data correctness and loss | `FAIL` as a stand-alone thirty-minute recovery point: 09:45 minus 09:00 is 45 minutes. B17–B20 match P1, but legitimate post-snapshot work and all other bookings are unaccounted for. |
| K-A | Service acceptance and control | `UNKNOWN`, with a known failed audit criterion from V1: no full service test, owner acceptance or attributable actor record is supplied. |
| K-B | Provenance and permission | `UNKNOWN`: a 09:20 timestamp alone cannot establish source authority or approval. |
| K-B | Copy integrity and usability | `FAIL`: inspected bytes differ from the recorded digest; no isolated import was attempted. Cause of the mismatch remains unknown. |
| K-B | Data correctness and loss | `UNKNOWN`: 25-minute nominal age meets the time screen, but no trusted booking comparison or valid import is available. |
| K-B | Service acceptance and control | `UNKNOWN`: no K-B service trial, owner acceptance or repaired V1 actor field is supplied. |
| K-C | Provenance and permission | `UNKNOWN`: the matching digest does not independently establish when or by whom the snapshot was captured. |
| K-C | Copy integrity and usability | `PASS` for the **supplied limited trial**: digest matched and a four-row isolated import was read in 11 minutes; completeness is untested. |
| K-C | Data correctness and loss | `FAIL` for return in its supplied state: seven-minute nominal age meets the time screen, but B19 and B20 conflict with P1. A later authorized correction and all other changes still need verification. |
| K-C | Service acceptance and control | `UNKNOWN`, with V1's failed actor-attribution criterion open; the 11-minute trial is not a service-level RTO measurement. |

**Six-line decision card, 09:46 UTC, proposed:**

1. Status: K1 is an exercise-only candidate review; no production restore, correction or service acceptance has occurred.
2. No candidate independently demonstrates both an acceptable data point and owner-approved correct data: K-A is old, K-B fails the digest check, and K-C contains B19/B20 mismatches.
3. The recovery lead requests service-owner and system-custodian approval to inspect K-A and K-C provenance and repeat a fuller isolated trial; K-B is held unchanged for mismatch investigation, not “fixed” by replacing its recorded digest.
4. The service owner and analyst request an authorized, independently sourced transaction history or manual-queue record to account for legitimate work since the chosen snapshot, plus a post-correction comparison with P1. If it is unavailable, the loss bound stays unknown.
5. V1's blank actor field and the unconfirmed cause prevent a claim of full controlled return. A restricted-service proposal would need an explicit compensating observation, approval, named owner and review limit.
6. The incident lead sets the next review when provenance, reconciliation and audit-attribution results are available, or sooner if unexplained edits or patron harm recur; the service owner decides whether the remaining service risk is acceptable.

The hypothetical two-hour RTO remains **unmeasured**: 14 and 11 minutes describe isolated imports and four-row reads, not a production service's accepted return after the 09:45 interruption. For the variation, a 09:10–09:18 journal gap prevents claiming complete replay of K-A's post-snapshot changes or complete validation of a later candidate. Request a separately retained booking audit or manual queue with known coverage for that interval; if none exists, document the gap and ask the service owner to make a bounded decision about the unresolved data rather than asserting zero loss. The variation does not change K1 or the canonical R records.

### Chapter 3 W1 write-pause verification lab — worked result

The unmodified in-memory program in section 3.3 prints:

```text
W-UI: BLOCKED_IN_THIS_TEST
W-API: WRITE_PATH_NOT_BLOCKED
W-QUEUE: QUEUE_ITEM_RECORDED
W-READ: READ_RETURNED_EXPECTED_VALUE
write_pause_claim: NOT_ESTABLISHED
```

| Probe | Observable basis | Limit of the classification |
|---|---|---|
| W-UI | The response is `rejected`, the independent state remains `Room 2`, and the audit label is `deny`. | One test of the ordinary interface during W1's time window does not establish every ordinary-interface request, future period or other write route is blocked. |
| W-API | The independent value changes from `Room 2` to `Room 4`; the service also reports `accepted` and the audit says `allow`. | This is a demonstrated failure **inside the fictional fixture**. It does not show what would happen on a real library service, and it does not identify the cause of earlier R-series edits. |
| W-QUEUE | The pending count rises from zero to one and the response/audit say `queued`/`queue`. | A recorded item has not been reconciled into the booking state; one item does not measure capacity or patron wait time. |
| W-READ | The lookup returns the expected `Room 2` value with no state change and a `read` audit label. | One successful read does not establish that all required read functions or users remain available. |

**Model claim:** “Under the separately approved W1 isolated-copy trial from 09:40 to 09:55 UTC, the ordinary write path blocked the one W-UI probe, but the legacy route changed a booking value at 09:43. The proposed control therefore did not establish a staff-write pause across its stated two-route scope.” This is narrower and more useful than “the pause failed everywhere,” which is not shown. A quiet R22 query, collected before W1, would add no evidence that W1 blocked an edit. R21's tolerance statement is also not W1's special approval card.

**Model decision and handoff:** do not call containment achieved or lift a monitoring requirement on the strength of W1. The fictional incident lead records W-API's before/after values, the response, audit label, test window, isolated environment and approvers, then asks the service owner and application owner to inspect the legacy-route control boundary. A revised control needs a new authorized trial on both known write routes and an explicit failure or rollback condition. The front desk keeps the manual item in its restricted queue; the service owner reconciles it against the approved booking target before normal writes resume. If a real service had other write routes, they would enter a separately scoped route inventory and test plan; W1 does not certify their absence. The containment choice in the canonical R1–R24 case remains unresolved until its own authorized branch outcome is supplied.

**Optional measurement-design answer:** to attribute W-UI's rejection to the proposed pause, the team would need a permitted pre-pause baseline on the *same authorized synthetic route and identity*, a reset state, a recorded change time and a repeated labeled probe under the approved pause. The state reads should name the same booking and authoritative store; the response and audit rows should be linked by request ID and bounded collection times. These checks were not supplied in W1. Therefore the observed W-UI result is a narrow tested block, not proof of causal effectiveness. The W-API changed value independently prevents a two-route containment claim in the fixture.

**W1-V counterfactual:** change only W-UI's after-state to `Room 4`, leaving its response `rejected` and audit label `deny`. The program classifies it as `WRITE_PATH_NOT_BLOCKED` because an observed value change outranks an asserted rejection. W-API remains a second `WRITE_PATH_NOT_BLOCKED`; W-QUEUE and W-READ keep their original results, and `write_pause_claim` remains `NOT_ESTABLISHED`. The conflict between W-UI's response/audit and resulting state calls for a provenance or control-path check, not a silent decision to trust the denial. W1-V is an exercise variant and does not alter the printed W1 fixture.

Award the seven rubric points only when the four classifications, scoped failure claim, corrective handoff and variant are present. A learner who treats the `rejected` response alone as proof, averages the write outcomes, calls a queued request a completed booking, or imports W1's 09:40 approval into R21 must correct the result. W1 is supplementary; the book still has exactly 50 numbered exercises with matching answers.

### EX039 — Worked result

| Role | Round A responsibility | Approval or escalation boundary | Verifiable output |
|---|---|---|---|
| Incident lead | Set the first decision time and case scope. | Approves classroom record handling; seeks the owner for disruptive service decisions. | `HL-IR-001` decision log with 09:05 checkpoint. |
| Analyst | Separate R1–R8 observations from hypotheses. | May recommend but cannot independently change a real account or booking service. | Evidence ledger with source IDs, UTC times and missing fields. |
| Service owner | Explain patron impact and acceptable interruption. | Decides whether a simulated service interruption is tolerable. | Recorded decision and review trigger. |
| Recovery lead | Plan how to test a backup and booking state. | Needs approval for a contained restore; cannot call R7 a successful restore test. | Test plan with expected data and measured-result fields. |
| Communications contact | Prepare an accurate internal update. | Escalates privacy or external-notice questions to authorized contacts. | Status draft that states cause and impact are unconfirmed. |

**Scope sentence:** “In this tabletop, read and annotate only the synthetic records released in the current round, role-play approvals, and write artifacts; do not contact a real library, access a real account or change a production service.” Combining human roles is acceptable only if approval and verification remain visible.

### EX040 — Worked result

1. **Case, time and service:** `HL-IR-001`, opened 09:00 UTC; Harbor Library room booking.
2. **Observed signals:** R1 at 08:40 records a `desk-a` sign-in; R3 and R4 at 08:43–08:44 record B17/B18 edits; R5 at 08:48 is a patron **report**.
3. **Assessment and limit:** booking changes warrant review; R6 shows scheduled training but compromise, approval of those edits and full patron impact are unconfirmed.
4. **Next owner question:** incident lead proposes asking the service/training owner whether B17/B18 were approved and setting a 09:05 decision checkpoint.

The line count and source pointers matter because a receiving analyst must distinguish source events from the first decision. No Round B record or 09:05 approval belongs in this Round A artifact.

### EX041 — Worked result

| ID | UTC source time | Source and observation | Learner release |
|---|---|---|---|
| R1 | 08:40 | Identity log: `desk-a` signed in. | Round A, first decision at 09:05. |
| R4 | 08:44 | Application log: B18 cancelled. | Round A. |
| R9 | 09:03 | Booking audit: B19 edited. | Round B, learner's 09:20 review. |
| R15 | 09:14 | Retention notice: detailed records kept 24 hours unless copied. | Round B. |
| R18 | 09:24 | Booking audit: B20 edited. | Round C, before 09:37 decision. |
| R21 | 09:29 | Service owner: fifteen-minute staff-write pause is tolerable with a manual queue. | Round C. |

**Ordering:** R1 is earlier than the supplied booking edits. **Limit:** the order does not prove who used the account or that the sign-in caused every edit. R9's event time is earlier than the learner's 09:20 receipt; it is not legitimate evidence for the prior 09:05 decision. R17–R18 cannot be imported into Round B. Other six-event selections pass if they preserve these boundaries.

### EX042 — Worked result

| Round B explanation | Supplied support | Contrary fact or limit | Discriminating authorized check and weakening result |
|---|---|---|---|
| Approved training explains all edits | R6 scheduled training; R10 names B17/B18 tasks. | R9 records B19 changed and R10 does not name B19. | Training owner checks complete approved task list and dated addenda; a confirmed complete list excluding B19 weakens the *all-edits* explanation. |
| `desk-a` was used outside its approved purpose | R9 shows B19 edited under the account; R12 reports staff did not recall it. | R13 has no device detail; recollection does not prove identity. | Incident and identity owners authorize a narrow session check; a valid documented B19 task with consistent context would weaken this hypothesis. |
| Patron display differs from authoritative state | R11 reports a wrong-looking booking time. | R9 is an application audit edit; a display-only fault may not explain it. | Service owner compares patron view, approved target and current booking state for B19; matching views of an incorrect underlying value weaken a *display-only* explanation. |

All three remain live at 09:20. R17's later task-list statement and R18's B20 edit are deliberately excluded. A hypothesis table should say what observation would change it, not merely repeat its label.

### EX043 — Worked result

**Round B preservation request, status: requested.** The incident lead asks the application custodian to preserve booking-audit rows for B17–B19 in a bounded 08:30–09:20 UTC event interval, retaining booking ID, field change, account label, original UTC time and any source metadata needed to interpret the rows. B20 is **not yet known** at Round B, so it does not belong in this initial request. The lead asks the identity administrator for a separately authorized narrow `desk-a` session summary where needed. The named collector records the actual query, source, collection time, approved copy location and access list; only necessary fields enter the restricted case storage, and analysis uses a working copy. R15's 24-hour notice makes the request urgent, but the custodian must confirm what starts the deletion clock and the last safe collection time. Until the copy exists, neither a digest nor a completed export can be claimed. A later Round C request may expand to B20 under a new scope and approval.

### EX044 — Worked result

**Round C decision card, 09:37 UTC; status: proposed.** R17's approved list names B17/B18 only and R18 records a later B20 edit under `desk-a`; account operator and cause remain unknown. The analyst recommends revoking only the identified current `desk-a` session after noting which narrow audit and session records can be preserved without prolonging harm. Fictional incident lead and identity owner approve the proposed identity action; the identity administrator would execute it. Intended benefit: stop edits through that one session. Uncovered paths: other sessions, accounts or an application fault. Service cost: staff reauthentication and possible desk delay. If a verified unexplained edit continues, ask the service owner to approve a fifteen-minute staff-write pause; R21 records tolerance, not execution. Verify actual revocation, a later bounded booking query and front-desk impact at 09:45 UTC. A pause-first choice also passes if it names an operator, queue and reversal check. Neither branch card has been supplied at the decision point.

**State receipts for this worked path:** proposed and fictionally approved at the Round C checkpoint; **execution pending** and **verification pending** until a later card reports them. The protective check is a new, owner-authorized query whose source, filter and interval are recorded. The separate legitimate-service check asks the desk supervisor whether approved staff can reauthenticate and continue the permitted workflow. Neither check establishes all-path eradication. The optional F1 replay has a different authority fact and must retain its own approval-pending state; do not merge it with this worked path.

### EX045 — Worked result

| Claim after Branch S, before P1/C1 and V1 | Supported? | Basis and limit |
|---|---|---|
| The specified current `desk-a` session was revoked at 09:45. | Yes, as a **fictional branch report**. | Identity administrator's Branch S card; it does not cover every session. |
| The branch's narrow booking query showed no later matching edit. | Yes, within the query's **unspecified range**. | Branch S card; exact source, filter, ingestion cutoff and later period still need recording. |
| The human behind the earlier edits was identified. | No. | Neither the branch action nor R1–R24 identifies the human. |
| All booking values are correct and no other edit path exists. | No. | Branch S itself says B19 remains incorrect; another account, session or source could still matter. |

**Next check:** the service owner authorizes a restricted comparison of B19's current state with an approved target, while the application custodian documents the query range and retention limit. Do not borrow the later P1/C1 rows to answer this pre-card review. No supported claim of eradication follows from a narrow quiet query.

### EX046 — Worked result

**Branch P queue-and-return note at 09:45 UTC:** the fictional service owner reports staff writes paused for fifteen minutes and a manual queue with **two pending requests**. The front-desk lead keeps request IDs, received times and desired bookings in restricted exercise notes; neither request is marked fulfilled. The application operator verifies the write block in its approved scope, and the analyst records the pause interval and audit query bounds. Before the planned 10:00 review, the service owner checks booking correctness against an approved target, assigns an operator to reconcile each queued request, and decides whether to resume writes with monitoring. A verified unexplained edit during the pause, inability to reconcile the queue or an unresolved booking-state mismatch keeps the restriction in place and returns the issue to the incident lead. The branch's no-write observation within the pause interval does not prove the account is safe after reopening. P1/C1 and V1 have not yet been released for this answer.

### EX047 — Worked result

| Observable acceptance item | Expected result | Supplied result after later cards | Owner and next step |
|---|---|---|---|
| Booking correctness | A **new** restricted comparison after approved correction matches P1 for B17–B20. | **Fail/pending:** C1 matches B17/B18, but B19 and B20 differ from P1; no production correction result exists. | Service owner approves B19/B20 correction; authorized operator acts; analyst checks a new copy. |
| Authorized access | A permitted staff role creates a synthetic test booking in approved scope. | **Limited pass:** V1 reports this in an isolated copy only. | Identity and service owners define an acceptable later production-scope test. |
| Denied unauthorized access | A tested unauthorized role cannot edit the synthetic booking. | **Limited pass:** V1 reports denial for that one synthetic identity and path. | Identity owner verifies the intended access policy and other relevant paths. |
| Audit visibility | Authorized test change has correct UTC time **and actor**. | **Fail:** V1 has UTC time but blank actor. | Application/audit owner repairs and retests attribution. |

**Provisional service state:** restricted or explicitly approved limited operation only, with owner and next review recorded; the cards do not support unconditional release. An unexplained new booking edit or unreconciled manual-queue item is a rollback/escalation trigger. The chosen branch changes the operational cost, not the failed P1/C1 and V1 evidence.

### EX048 — Worked result

**Branch S, exactly two sentences:** “At 09:45 UTC, Harbor Library is reviewing unexplained room-booking edits in R9 and R18, and the identity administrator reports that the specified `desk-a` session was revoked under the fictional approval; the staff member must reauthenticate. The incident lead and service owner will review booking correctness and the bounded audit at the next checkpoint, while the cause and wider impact remain unconfirmed.”

**Branch P, exactly two sentences:** “At 09:45 UTC, Harbor Library is reviewing unexplained room-booking edits in R9 and R18, and the service owner reports a fifteen-minute staff-write pause with two requests waiting in a manual queue. The incident lead and service owner will check booking state and reconcile the queue before deciding whether to resume writes, while the cause and wider impact remain unconfirmed.”

Neither update uses P1/C1 or V1, which the facilitator reveals later, or claims a completed restore. A real external update would require its own authorized review.

### EX049 — Worked result

**Ticket IR-IMPROVE-01.** **Gap and source:** V1's isolated-copy audit record contains a UTC time but a blank actor; this prevents attribution for the tested authorized change. **Owner:** application/audit owner, with incident lead accepting the result. **Due:** within 30 days of the tabletop. **Change:** trace where the actor field is lost in the synthetic test path, correct the audit mapping and document the field requirement. **Interim control:** keep the case in an approved restricted or monitored mode, with named reviewer and bounded change comparisons until the test passes. **Verification:** repeat a controlled authorized edit and a denied unauthorized edit; pass only if the authorized change's audit row includes the expected actor and UTC time, the denial is observed, and the incident lead records the evidence and scope. Correcting B19/B20 addresses particular booking values; it does **not** repair this program-level attribution defect. A different single-gap ticket for R23's stale restore test passes if it includes a dated isolated restore, measured duration, copy timestamp, booking comparison and named acceptance.

Retain the test input, application version, expected actor, request key, authoritative state, emitted audit row and reviewer receipt. The negative control fails if an unauthorized synthetic edit changes state or a deliberately omitted actor is still accepted. A failed or missing test leaves the ticket open and triggers a revised owner-approved investigation; a marked-complete implementation task is not proof that the control passed.

### EX050 — Worked result

**Handoff paragraph, Branch S:** “`HL-IR-001` concerns Harbor Library room booking: R17 limits the approved training list to B17/B18, R18 records B20 changed at 09:24, and the fictional incident lead and identity owner approved the current-session revocation reported by Branch S at 09:45. The branch's narrow query showed no later matching edit in its range, but did not identify the prior operator or rule out another path. Later P1/C1 cards show B19/B20 still differ from the service-owner target, and V1's isolated test has a blank audit actor despite its limited access successes; no production correction or backup restore result is supplied. The service owner owns booking correction, queue or access acceptance and a documented restricted-service choice; the application/audit owner owns actor-field repair; the response lead reconvenes at the next named checkpoint, sooner if a verified unexplained edit appears, and records approval before any rollback or further restriction.”

| Six-output self-score | Score / 2 | Reason or revision |
|---|---:|---|
| Timeline | 2 | IDs, UTC source times and release rounds retained. |
| Hypotheses | 2 | Training and outside-plan use compared with a missing identity discriminator. |
| Action record | 2 | Fictional approvers, narrow scope, effect, cost and fallback stated. |
| Recovery plan | 1 | P1/C1 and V1 failures identified; add a copy ID, measured restore time and approval for a later isolated test. |
| Status message | 2 | Branch action and uncertainty reported without blame. |
| Improvement ticket | 1 | Audit repair owner and test named; add a specific due date and interim check if absent. |

**Total:** 10/12 for this *example*; recovery plan is the first artifact to revise. The self-score does not turn an untested restore into a pass. A different branch can earn the same score when its queue, approvals and return condition are handled explicitly. A submission with zero for approval or evidence scope fails the section 4.5 gate regardless of its total.

**Contested-score note:** a second reviewer might give the recovery plan 0 rather than 1 if “restore complete” appeared in the submitted plan; R23 contains only a backup-job report, not a restore result. In this model packet the handoff explicitly says no restore result is supplied and identifies P1/C1 and V1 failures, so **1** is defensible for an incomplete plan. The learner should save a `recovery-plan-v2` with a proposed copy ID field, measured start/end fields, service-owner target, negative access test and rollback rule. Those fields remain planned until an isolated test supplies their results. Do not edit the earlier `C-action-v1` to include the later Branch S outcome.

### Chapter 4 F1 replay lab — worked result

**Record A — current-session option, 09:37 UTC, replay only.** “R17 limits the approved training plan to B17/B18 and R18 records a B20 edit outside that plan. I recommend that the fictional incident lead and identity owner consider revoking the *current* `desk-a` session after a bounded preservation check of the supplied records. The intended benefit is to stop further changes through that session; the cost is staff reauthentication, and other sessions or paths remain untested. Approval is **requested**, not presumed. The identity administrator would report execution only after both fictional approvers agree; the response lead would then check a newly authorized audit range and staff impact at the next checkpoint. An unexplained fresh edit or inability to verify the session result triggers reassessment.” This is a proposal at 09:37, even if the original Branch S card later reports an action in a different run.

**Record B — booking-write pause, 09:37 UTC, replay only.** “R21 states that the service owner could tolerate a fifteen-minute pause, but F1 says that owner cannot be reached and no alternate is confirmed. A pause may protect bookings if new unexplained edits continue; it would also delay staff requests and create a queue needing ownership and reconciliation. Approval is **pending**. The response lead asks the service manager to verify the authorized alternate and contact route, keeps the analyst on the already supplied synthetic records and names the next review at 09:45 or immediately upon a verified new edit. The team does not execute the pause on the strength of the tolerance statement alone.” If an alternate is later identified, the team must record their scope of authority and actual decision before any simulated execution card could be treated as evidence.

**Handoff sentence:** “At the 09:37 replay checkpoint, a scoped session action is proposed to the incident lead and identity owner, the staff-write pause awaits a verified service-owner approval route, and **no action has been reported executed**; review again at 09:45 or on a verified fresh edit.” This sentence distinguishes three different states—proposal, approval pending and reported execution—without relying on any Round D card.

**Rubric check:** R21 is not treated as approval (1); Record A names both fictional approvers and a bounded result check (1); Record B retains the service cost and pending authority (1); escalation and a review trigger are specified (1); the handoff states no execution at 09:37 (1). **Model score: 5/5.** A learner who recommends waiting on both options can also receive 5/5 if the record explains the residual booking risk, identifies who can decide, and fixes a prompt review time. A learner who uses the 09:45 Branch S result to justify the 09:37 proposal loses the evidence-timing point because that result was unavailable then.

### Chapter 4 communication replay — worked result

The following packet is **draft, not sent**, for the optional M1/M2 replay after Round D. It uses Branch S. No message in this example is an actual Harbor Library or British Library communication. The 10:05 checkpoint is a proposed classroom review, not a predicted restoration time.

| Claim considered at 09:54 UTC | Earliest usable evidence | Classification and treatment |
|---|---|---|
| Current `desk-a` session revoked | Branch S, released in Round D; action reported for 09:45 | **Supported narrowly** for an internal message. Other sessions and paths remain untested. |
| All bookings correct | P1/C1, released after the branch card in Round D | **Contradicted** for B19/B20; no subsequent correction result. Exclude the assurance. |
| Newsletter list stolen | M2 forwarded claim received at 09:52 in the optional replay; R24 was available in Round C at 09:36 | **Unverified**. M2 has no originating source; R24 did not establish access at its earlier checkpoint and cannot clear all future evidence. Refer for bounded assessment. |
| Front desk can check disputed bookings | R5 patron report in Round A; M1 request at 09:50 in the optional replay | **Conditional service instruction**. Ask the service owner to confirm staffing and route before the communications owner approves a patron draft. |
| Incident over | P1/C1, V1 and unresolved cause in Round D | **Unsupported**. Do not issue a closure statement; set the next review. |

**Restricted internal update, `draft-internal-v1`, prepared 09:54 UTC for the fictional response roles:**

> Branch S reports that the specified `desk-a` session was revoked at 09:45; its subsequent booking query was limited to the recorded range and does not clear other access paths. P1/C1 still identifies B19 and B20 as mismatches, and V1's isolated test has a blank audit actor field. The service owner and recovery lead should review the booking target and an authorized correction test; the application owner should investigate attribution. M2 is an unattributed forwarded claim about the newsletter list, not evidence of access. The incident lead and privacy contact will request a scoped source check. No full-service return has been approved. Next decision review: 10:05 UTC, or sooner on a verified new edit.

The internal version includes account and booking identifiers because its audience is restricted to response roles and the synthetic case. It attributes the revocation to the Branch S report, not to an independent production verification. “No full-service return has been approved” describes the supplied exercise record, which lacks such an approval; it is not a claim about any real library.

**Patron-facing holding message, `draft-patron-v1`, approval pending with the fictional service and communications owners:**

> We are reviewing discrepancies in some room-booking information. If your booking appears incorrect, please ask the front desk to check it. We are verifying the affected records and will update this notice when the next service status is confirmed. Thank you for your patience while we check the bookings.

Before any real public message, the owners must confirm that the front-desk route is staffed and approved or replace it with one that is. The draft avoids an account label, a purported cause, an unsupported data-exposure conclusion and a precise restoration promise. It is a teaching example, not a recommendation to publish that exact wording.

**Privacy assessment request, `draft-privacy-v1`, restricted:** “M2 is a forwarded internal sentence alleging newsletter-list theft, with no originating author, time, source or export record. R24 stated only that the evidence then available at 09:36 did not establish access to the newsletter list or another personal-data store. Incident lead and privacy contact: please identify the authorized custodian of newsletter access and export records and approve a bounded check covering the incident interval with source and collection metadata. Record any finding, coverage gap and next review before deciding whether a separate notification assessment is needed.” This is a request, not a conclusion about breach status or notification obligations.

**Branch P replacement line:** “At 09:45, Branch P reports a service-owner-approved fifteen-minute staff-write pause; two booking requests are in the manual queue. At 09:54, the pause is still within its planned interval, and the service owner must reconcile the queue and decide whether writes may resume.” The rest of the update still keeps the P1/C1 discrepancies, V1 failure and M2 report open. The patron version would omit any implication that normal booking writes are available.

**Correction practice:** retain the fictional overconfident sentence as `draft-v0`, labelled *never issued in this exercise*. In `draft-v1`, replace “all bookings are restored” with “P1/C1 still shows B19/B20 mismatches pending owner review” for the restricted audience, and replace “no customer information was affected” with “an unattributed exposure claim is being assessed; the supplied record has not established its truth.” Record the source card, preparation time, intended audience and approving role beside the revision. If the earlier sentence had actually been issued, the response team would need its own authorized correction decision and an auditable link between versions; this model does not claim one occurred.

**Rubric check:** the ledger records five bounded claims and release points (1); the internal draft reports narrow action and open checks (1); the patron draft avoids false reassurance while offering conditional help (1); the privacy request treats M2 and R24 correctly (1); audiences, pending approvals and 10:05 review are named (1); the Branch P and correction variations preserve state and version history (1). **Model score: 6/6.** The score describes this synthetic packet only. Another short message can pass if it states the same facts, authority and limits without unnecessary case details.

<a id="ir-rapid-ch04-f4-audit-result"></a>

### Chapter 4 F4-AUDIT laboratory — worked result

~~~text
A-timeline: IN_SCOPE
B-hypotheses: IN_SCOPE
C-action: IN_SCOPE
D-status-S: IN_SCOPE
D-recovery: IN_SCOPE
D-improvement: IN_SCOPE
NEGATIVE_FUTURE_BRANCH: FUTURE:S
NEGATIVE_PREMATURE_RECOVERY: FUTURE:V1
NEGATIVE_MIXED_BRANCHES: BRANCH_CONFLICT
FROZEN_V1: 8/12 REVISION_REQUIRED
REVISED_V2: 11/12 CLASSROOM_THRESHOLD_MET
NEGATIVE_NO_APPROVAL: 11/12 HARD_GATE_FAIL
~~~

**Interpretation of the reproduced result:** The first six rows confirm only that each displayed reference is *permitted in that stage*, not that the artifact's interpretation is correct. The first negative control rejects Branch S as evidence in Round C. The second rejects V1 at the first Branch S release; P1/C1 and V1 must enter later. The third detects mutually exclusive Branch S and P reports incorrectly combined as one case path.

The frozen example totals 8/12, below the declared classroom threshold. The revised example totals 11/12 and meets the *numeric classroom* threshold if the explicit approval and evidence-scope checks also hold. Removing the approval evidence yields `HARD_GATE_FAIL` even though the score remains 11/12. The program does not decide whether a source is authentic, whether an action was truly approved or whether a recovery criterion passed: `approval_ok` and `scope_ok` are assumed input flags to be justified by a human reviewer with evidence.

**Negative test:** Change `("D-status-S", "D_BRANCH", ("S",))` to include `"V1"` and observe `FUTURE:V1`. Restore the original tuple before interpreting the baseline results. A correct result proves only that the classroom release rule was enforced by the script, not that a real system is secure.

**Required learner artifacts:** the exact twelve-line transcript; a six-row artifact table with checkpoint, references, proposed score, evidence pointer and one missing field; a short explanation of the approval hard gate; and a versioned correction of one deliberately premature claim. The learner must not modify actual incident records or contact an outside system.

**Assessment:** Award one point each for exact transcript, correct future/mixed-branch reasoning, separation of score from critical gate, versioned non-backdating correction and explicit explanation that a tabletop score does not verify production containment/recovery. The lab is supplemental; no new numbered exercise ID is created.

---

### Chapter 4 tabletop — six-artifact model submission

This **model submission** uses Branch S. It is a classroom example assembled from the supplied records and cards; the named approvals and actions below occur only in the fictional branch. Copy its structure for the Branch P alternative, not its conclusions.

**1. Timeline with evidence availability.** R1: 08:40 UTC, `desk-a` sign-in; R3: 08:43, B17 edit; R4: 08:44, B18 cancellation; R9: 09:03, B19 edit, *revealed to the learner in Round B*; R15: 09:14, notice that detailed booking audit is retained for only 24 hours unless copied; R18: 09:24, B20 edit, *revealed in Round C*; Branch S: 09:45, specified session revoked. P1 describes an owner target at 09:40 and is disclosed in Round D; it cannot justify the 09:37 containment proposal. R1's earlier time does not prove who made R3, R4, R9 or R18.

**2. Hypothesis table.**

| Explanation | Support in the supplied record | Contradiction or limit | Next authorized discriminator |
|---|---|---|---|
| Scheduled training explains all edits | R6 records training; R12 says the staff member edited B17/B18 | R10 and R17 do not include B19/B20 in approved tasks | Ask the training owner for the complete approved plan and any addendum |
| An unauthorized user controlled a session | R9 and R18 are outside the known plan; R1 shows a session | No supplied record identifies the human or rules out an application error | Request narrowly scoped identity detail under incident and identity-owner authority |
| Booking display differs from stored state | R5 and R11 are patron reports of booking problems | R9 and R18 are application audit edits; a display issue does not explain them alone | Compare owner-approved target P1 with a fresh restricted application copy |

These explanations need not be mutually exclusive. Their table entries are hypotheses, not findings of compromise, exposure or root cause.

**3. Action record.** At 09:37 UTC the analyst recommends revoking the current `desk-a` session because R17 and R18 weaken the training explanation and continued edits could harm bookings. The fictional incident lead and identity owner approve the narrow action; the identity administrator executes it in Branch S at 09:45. Expected effect: stop changes through that session. Cost: staff reauthentication. Preserve the available narrow records when it does not prolong harm. Fallback: seek separate service-owner approval for a fifteen-minute staff-write pause if edits continue; R21 alone records tolerance, not approval. The response lead checks a new audit range and staff impact at the next checkpoint. This record distinguishes recommendation, authorization, execution and limited verification.

**4. Recovery plan and result field.** The recovery lead proposes an authorized isolated copy and a named source timestamp, compares B17–B20 against P1, tests one allowed and one denied synthetic edit, checks whether the audit includes both UTC time and actor, and records duration and data freshness against any owner-approved recovery targets. The **current result field is incomplete**: P1/C1 shows B19 and B20 do not match; V1's isolated-copy access checks pass within their scope but actor attribution fails; R23 gives no completed restore result. The service owner cannot sign an unconditional return to normal booking writes from these cards. A future owner-approved correction and retest would require a *new* result record. An unexplained fresh edit triggers immediate reassessment of the restriction.

**5. Internal update.** “At the 09:45 UTC checkpoint, the specified `desk-a` session has been revoked under the exercise approval, and we are checking affected room bookings; the cause and full access scope remain unconfirmed. The service owner and response lead will review B19/B20 against the approved target and the audit-attribution defect before deciding whether booking writes can resume normally.” The update describes the branch action while leaving later verification separate.

**6. Improvement ticket.** “Owner: booking application/audit owner, with the response lead reviewing evidence. Due: within 30 days of this tabletop. Gap: the V1 isolated-copy test recorded a UTC time but no actor identifier. Action: identify the missing attribution path, correct it through the approved change process and run a controlled allowed edit. Acceptance: the resulting audit record contains the correct test actor and UTC time, and a reviewer can link it to the controlled action; document a compensating monitoring owner until that check passes.” This ticket addresses a reusable control gap; it does not claim that the fictional live incident has been resolved.

The model earns full credit only if the learner's own six artifacts preserve the same evidence boundaries and state which checks remain unperformed. A polished handoff with an invented successful restore or an unrecorded approval fails the relevant rubric row even if its prose is clear.

## Chapter 1 glossary

- **Alert:** a signal that a rule or person has flagged for assessment.
- **Artifact:** a record or object produced during investigation or response.
- **Authorization:** the permission and scope under which a response action may be taken.
- **Evidence pointer:** a stable identifier that lets a reviewer locate the underlying record.
- **Hypothesis:** an explanation to test, not a confirmed cause.
- **Incident record:** the shared account of observations, decisions, owners and timing.
- **Service owner:** the person accountable for the service's business outcome and tradeoffs.

## Chapter 2 glossary

- **Collection note:** a record of how, when, where and under whose authority an item was obtained or copied.
- **Coverage interval:** the time span and filters a query or source actually examined; a negative result applies only within that scope.
- **Confidence:** the analyst's assessed support for an explanation, stated with its limits.
- **Digest:** the output of a hash function for a specific byte sequence.
- **Discovery time:** when the analyst received or recognized a record, distinct from the event time recorded by its source.
- **Ingestion time:** when a record became available to the queried store; it may be later than the recorded event time.
- **Handoff:** a case summary sufficient for another authorized person to continue the work.
- **Hypothesis test:** a planned check that could support or weaken an explanation.
- **Offset:** the explicit difference between a timestamp's local clock representation and UTC, needed for an unambiguous conversion.
- **Package manifest:** the item, source, selection, authority, transformation, byte check, access and limits needed to review a particular copy.
- **Query run time:** the time a search was executed against a store, distinct from event, ingestion and analyst discovery times.
- **Retention deadline:** the time after which a source may no longer preserve the needed record.
- **Triage:** the initial assessment of potential harm, urgency, uncertainty and next authorized action.

- **Comparison frame:** the explicitly selected business objects to which a count applies; a case-selected frame is not a population sample.
- **Impact unit:** the object being counted, such as a ticket, booking, edit or person; different units cannot be interchanged.
- **Unverified comparison:** a selected object for which the approved target or current authoritative value is unavailable.

## Chapter 3 glossary

- **Containment:** a bounded action intended to limit further harm while investigation continues.
- **Control effectiveness:** the observed effect of a proposed safeguard within a named scope and test window; an enabled setting or quiet log alone does not establish it.
- **Eradication:** removal of an identified cause or persistence mechanism, followed by verification.
- **Fallback:** an alternative action prepared if the preferred intervention fails or becomes too costly.
- **Provenance:** the recorded origin, collection context and authority of a data copy or claim.
- **Reconciliation:** comparison of a current state with an approved target, identifying matches and exceptions before any authorized change.
- **Recovery acceptance:** evidence and owner sign-off needed before normal service resumes.
- **Residual risk:** uncertainty or exposure remaining after an action has reduced some harm.
- **Rollback trigger:** an observable condition for reversing a service change or returning to restricted mode.

## Chapter 4 glossary

- **After-action report:** a documented account of exercise scope, observations, limits and proposed improvements; a model classroom report is not an operational incident finding.
- **After-action review:** a structured review of decisions, evidence, coordination and improvements after an exercise or event.
- **Branch card:** a fictional inject describing the outcome of a choice in the tabletop.
- **Closure proof:** the predeclared artifact and independent check required to close an improvement action.
- **Exercise inject:** a new piece of scenario information released at a planned point.
- **Measurement contract:** an objective, observable behavior, evidence source, threshold and explicit limit set before an exercise round.
- **Tabletop:** a discussion-based exercise in which participants reason through decisions without changing a live system.

## References for the authored chapters

1. NIST, [SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*](https://csrc.nist.gov/pubs/sp/800/61/r3/final), April 2025. Used for the integration of response across risk-management activities.
2. NIST, [Cybersecurity Framework 2.0 FAQ](https://www.nist.gov/cyberframework/faqs), section “Framework Components.” Used for the six concurrent and continuous functions.
3. CyberABC, [incident-response practice playbook index](../../../../../playbooks/incident-response-resilience/README.md). This index points to revision-pinned source playbooks; it is supplementary to the book. Source repositories retain their own rights.
4. NIST, [SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*](https://csrc.nist.gov/pubs/sp/800/86/final), August 2006. Used for the limited, authorized evidence-collection lesson in Chapter 2; this introductory exercise is not a substitute for a forensic or legal procedure.
5. NIST, [SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final), December 2016. Used for the Chapter 3 emphasis on planned, verifiable recovery.
6. NIST, [SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*, updated edition](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), November 2010. Used for the distinction between a backup status and a tested recovery plan.
7. NIST, [SP 800-84, *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*](https://csrc.nist.gov/pubs/sp/800/84/final), September 2006. Used for the Chapter 4 design, conduct and evaluation of a tabletop exercise.
8. British Library, [*Learning Lessons from the Cyber-Attack: British Library Cyber Incident Review*](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=), 8 March 2024. Primary institutional account used for the separate real-world source-reading activity in Chapter 3. Its text and findings are cited, not copied or relicensed.
9. NIST, [SP 800-92, *Guide to Computer Security Log Management*](https://csrc.nist.gov/pubs/sp/800/92/final), September 2006. Background on log-management processes for Chapter 2. Its age and high-level scope are stated beside the original delayed-arrival exercise; it does not prescribe the fictional fixture or its query algorithm.

All **Harbor Library** names, accounts, bookings, logs and times are invented for instruction. The **British Library** case is a separately cited real incident. Its reported facts do not describe or validate the fictional Harbor Library scenario.
