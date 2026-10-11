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

### 1.10 Common errors and chapter synthesis

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

#### EX002 — First two questions

**Objective:** choose checks that could change the restriction decision. **Inputs:** R1–R6 and the service/authority tables. **Output:** two rows with a precise question, the fact that makes it relevant, the authorized custodian or person to ask, and how either answer changes the decision. One question must test the training explanation; the other must test who used the account or whether edits continue. Record requests rather than saying the interview or log review has already occurred. A score of 2 requires different discriminators and a named approval path for any new identity collection.

#### EX003 — Service dependency

**Objective:** connect an incident signal to service outcomes and evidence owners. **Inputs:** the section 1.2 service map and R1–R8. **Output:** a two-row dependency card with dependency, possible user harm, supplied pointer, missing discriminating evidence and custodian. Choose two dependencies; for each, explain what an authorized check would distinguish. Do not call a potential harm a confirmed outage. A score of 2 needs two different dependencies and a test that could separate a service-state problem from account misuse.

#### EX004 — Scope boundary

**Objective:** apply an authorization boundary to a tempting next action. **Inputs:** the section 1.4 scope statement and R1–R8. **Output:** a short scope decision with proposed action, permitted objects and operations, reason for rejection, contained alternative, and stop or escalation condition. A learner wants to search a real public library website for a matching account name. Explain what the eight supplied records permit instead, and write a hypothetical request for the additional detail if it would matter to the case. A score of 2 explicitly excludes real-site access and names the responsible approver for any future expanded scope.

#### EX005 — Timeline

**Objective:** preserve event order without turning sequence into causation. **Inputs:** R1, R3, R4 and R5. **Output:** a four-row UTC table with record ID, source, time and observed event, followed by an ordering sentence and a separate unsupported-causality sentence. Keep the 09:00 case-open time outside the event table. A score of 2 orders the four events correctly and explains why precedence alone does not identify the human actor or prove why the patron's view changed.

#### EX006 — Role assignment

**Objective:** make recommendation, approval, execution and verification visible. **Inputs:** section 1.3's fictional roles, R7 and the classroom scope. **Output:** a four-row responsibility table for a possible booking outage, preservation of R1–R5, coordination of the next review and a contained restore test. Name the task owner, who approves it under the exercise rules and what would verify completion. Distinguish **planning** a restore test from having performed one. A score of 2 does not delegate an outage decision to the analyst or treat R7 as a tested restore.

#### EX007 — Minimal incident record

**Objective:** open a case that another analyst can continue. **Inputs:** R1–R8 and the 09:00 intake checkpoint. **Output:** exactly seven labeled fields: case ID and open time; service; reporter and source; observed signal with record IDs; current assessment and uncertainty; permitted scope and authority; next question, owner and review time. Related details may share a field. A score of 2 retains the `T-104` help-desk context from section 1.5, distinguishes the report from an independently checked booking state, and does not claim the later 09:05 decision was already executed at 09:00.

#### EX008 — Evidence quality

**Objective:** limit claims to what three different source types actually say. **Inputs:** R6–R8. **Output:** a three-row evidence-limit table with ID and time, narrow supported conclusion, tempting unsupported conclusion, and a follow-up source or test. A score of 2 treats a scheduled activity as distinct from an approved booking change, a completed backup job as distinct from a proven restore, and a summary missing destination detail as distinct from a verified absence of transfer.

#### EX009 — Decision alternatives

**Objective:** justify a proportionate 09:05 decision under uncertainty. **Inputs:** R1–R8 and the section 1.9 gate. **Output:** a two-row option matrix for (A) seeking a temporary restriction of `desk-a` and (B) preserving R1–R8, asking the training owner and reviewing before restriction. Record expected benefit, possible service or delay cost, approver, observable success or failure and a 09:15 review trigger for each. Choose one provisionally and explain what new evidence would reverse it. A score of 2 identifies a separate approval for restriction and does not describe either risk as an already observed event.

#### EX010 — Communication draft

**Objective:** communicate useful action without premature attribution. **Inputs:** R1–R8 and the 09:00 intake state, *before* the 09:05 decision. **Output:** exactly two sentences for an internal service-owner audience: the first states observed service signals and uncertainty; the second names a **proposed** next check, its owner and the expected 09:05 decision checkpoint. Do not say preservation, an interview or a restriction has already been approved or performed. A score of 2 gives a source pointer and an unambiguous distinction between planned and completed work.

#### EX011 — Escalation trigger

**Objective:** specify when the initial choice must be reopened. **Inputs:** the R1–R8 snapshot and section 1.9. **Output:** two **hypothetical** observation/response rows with source that would verify the signal, harm or uncertainty affected, decision owner and next action. One trigger should concern continued booking change; the other should concern breadth or service impact. A score of 2 states that neither observation is present at 09:05 and avoids an automatic production action without approval.

#### EX012 — Practice record

**Objective:** make a bounded decision auditable. **Inputs:** R1–R8, the fictional 09:05 checkpoint and section 1.3's authority matrix. **Output:** one decision log with time, action, reason with source IDs, approving role, executing role, evidence-copy scope, rejected alternative, next review time and reversal trigger. The scenario grants classroom permission for the bounded copy; do not describe a production export. A score of 2 states the question to the service owner as **pending** until answered and preserves uncertainty about account control.

#### EX013 — Readiness gap

**Objective:** turn an exercise weakness into a measurable preparation change. **Inputs:** the service map, authority table, R7–R8 and the section 1.8 workshop. **Output:** a three-row gap register with missing capability, consequence and owner; then an improvement ticket with priority rationale, specific change, deadline and a pass/fail drill. A score of 2 names a test that would actually demonstrate the change, such as an owner-and-alternate decision drill or a contained restore rehearsal, rather than merely publishing a policy page.

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

#### Event time, discovery time and collection time are different facts

An event may occur at one time, enter a logging service later and be seen by an analyst later still. In the supplied classroom table, R9 says that an edit was recorded at 09:03 UTC. R15, at 09:14, communicates a retention rule; it does not restart the retention period for R9. Without the actual source's deletion policy, no learner can calculate an exact expiry from those two timestamps. The safe operational question is: **What is the oldest relevant record's retention deadline at its source, and how soon can an authorized custodian preserve a narrow copy?** Escalate that uncertainty instead of writing a fabricated deadline.

When merging records from different systems, retain the original timestamp and its timezone or offset. Add a normalized UTC field separately and record how it was obtained. A timestamp without an offset is ambiguous; a clock that is five minutes slow may reverse apparent order. The case table supplies UTC for teaching, but a real analyst would check source clock configuration and collection delay before claiming a precise cross-system sequence. R13's summary omits device and location detail, so the absence of those fields is a **source limitation**, not a negative finding about the session.

Preservation should also be **proportionate**. For the next Harbor Library decision, a bounded booking-audit interval and the account's relevant sign-in summary may be useful. Exporting all patrons, all departments or unrelated accounts could increase privacy risk without improving the decision. A narrow export can still omit a relevant event; record the selection rule and keep an authorized unmodified original when available. Chapter 2 teaches the logic of a collection request and a copy-integrity check. Production evidence handling belongs to the organization's approved procedures and qualified personnel.

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

### 2.7 Handoff and common errors

A useful handoff lets a second analyst reconstruct the decision without guessing: case ID; current time and timezone; affected service; observed facts with record IDs; live hypotheses; confidence and limits; known service impact; actions completed under which authority; evidence locations; next question; decision owner; review deadline. It should also separate the source's event time from the time the analyst learned of the event.

Common errors are copying only an alert title, silently converting timezones, treating a staff recollection as proof, relying on a log summary that omits key fields or query boundaries, hashing a file without recording which bytes were hashed, or using a high severity label without naming harm and urgency. A careful analyst can be concise: cite the observation, state the limit and identify the next decision. The T1 lab also illustrates a subtle mistake: “I discovered R9 at 09:20” does not mean “R9 occurred at 09:20”; conversely, “R9 occurred at 09:03” does not mean it was available for a 09:05 decision.

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

#### EX017 — What the summary cannot prove

**Objective:** test the limits of negative evidence. **Inputs:** R13, R14 and, for this question only, the optional T1 metadata. **Output:** two short claim/limit pairs and one proposed follow-up query. First assess R14 *without* T1; then state exactly what T1 adds and what it still cannot cover after 09:12. Explain why R13 does not establish that the `desk-a` session came from the expected staff device. A score of 2 distinguishes missing device fields from a negative device finding and names the query's filter and interval.

#### EX018 — Retention decision

**Objective:** prepare a proportionate preservation decision. **Inputs:** R15, R9 and the collection-note fields in section 2.3. **Output:** a three-row request to the custodian stating source and event range, deletion-policy anchor or actual deadline, and collector/authority/storage scope; add a sentence explaining why preservation may precede root-cause knowledge. Do not calculate a precise expiry merely by adding 24 hours to R9's timestamp. A score of 2 identifies both the time-sensitive risk and the privacy boundary.

#### EX019 — Collection note

**Objective:** make an exercise extract reviewable. **Inputs:** the E1 fixture in section 2.5 and R9/R14. **Output:** a collection-note table with case/item ID, source and event range, collector, authority, actual local collection time *if a file was created*, copy location, transformation and limitation. If no file was created, label the note **planned** and leave collection time and digest **not applicable**; do not pretend an export occurred. A score of 2 identifies E1 as a synthetic transcription, distinguishes original book text from the working file and records access scope. A made-up digest is not required.

#### EX020 — Hash claim

**Objective:** bound an integrity claim. **Inputs:** the named E1 bytes, the two digest checks and section 2.5. **Output:** a five-row claim table: two statements the comparison supports and three it does not, each with a one-sentence reason. Specify which file and times were checked rather than saying “the evidence is authentic.” A score of 2 distinguishes copy consistency from source truth, completeness and collection authority.

#### EX021 — Time ordering

**Objective:** separate event order from causal inference. **Inputs:** R9, R10, R12, R15 and R16; use T1 only for the optional final sentence. **Output:** five ordered rows with ID, UTC event time, source and one uncertainty about cause. Mark that R9–R16 reached the learner at 09:20 despite earlier event times. Optionally state which interval T1 leaves uncovered. A score of 2 preserves event/discovery separation and does not treat temporal precedence as authorization or attribution.

#### EX022 — Handoff

**Objective:** allow a second analyst to continue without guessing. **Inputs:** the Round B snapshot R1–R16 and the fictional approval path. **Output:** a five-sentence handoff at 09:20 UTC that includes case ID and service, at least two evidence IDs, a live hypothesis and alternative, one uncertainty, an authorized next action, the custodian or owner, and the 09:35 review or an observable earlier trigger. A score of 2 distinguishes a request or proposal from a completed action.

#### EX023 — Impact check

**Objective:** size possible service harm without exporting unrelated patron data. **Inputs:** R9, R11, R14–R16 and the service map. **Output:** a short query request naming approver, custodian, booking identifiers or short event range, necessary fields, expected result table and privacy/access limit. The table should distinguish an audit edit, an owner-approved state and an unresolved mismatch. A score of 2 does not claim a completed count or that R14 covers the whole period.

#### EX024 — Escalation threshold

**Objective:** define a testable escalation rule. **Inputs:** the 09:20 case state and R15's retention notice. **Output:** two **hypothetical** observation/response pairs, each naming who verifies the new signal, why it raises harm or urgency, who decides on containment and when they reconvene. Do not claim either event happened. A score of 2 uses observable triggers rather than “if things get worse.”

#### EX025 — Correct a faulty note

**Objective:** repair unsupported attribution and scope. **Inputs:** R9, R11, R13 and R8. **Output:** a replacement of at most three sentences with one observed booking fact, one evidence limit and one next authorized check. Then underline or list the three unsupported claims removed from the faulty note. A score of 2 does not equate R8's missing destination detail with proof of no transfer either.

#### EX026 — Reproducible review

**Objective:** challenge an overconfident peer conclusion constructively. **Inputs:** R6, R9, R10 and R12. **Output:** a four-field review note: claim, directly supported facts, missing discriminator for B19, and authorized way to obtain it. Explain what outcome would change your view. A score of 2 preserves the possibility that training explains B17/B18 while leaving B19 unresolved; it does not assume the staff member is lying.

<a id="ch-03"></a>

## Chapter 3 — Containment, eradication and recovery decisions

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Distinguish a temporary containment action from cause removal and verified service recovery.
2. Compare two response options against harm reduction, operational cost, reversibility, authority and evidence loss.
3. Record an approval, fallback condition and next review time for a proposed intervention.
4. Explain why a completed backup job is insufficient to claim recovery readiness.
5. Define a small set of tests that would justify returning a fictional service to normal use.

### 3.1 A decision loop rather than a fixed sequence

The Chapter 2 triage left `B19` unexplained and identified an audit-retention deadline. As evidence changes, the incident lead needs a repeated loop: **observe → assess possible harm → compare authorized options → act → verify effect → reassess**. Containment aims to limit further harm while the cause remains under investigation. Eradication addresses a confirmed cause or persistence mechanism when the team can identify it. Recovery restores useful service under explicit checks and monitoring. These activities can overlap, and an intervention may have to be rolled back if its cost or side effects exceed its benefit.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) treats response and recovery as part of wider cybersecurity risk management. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) addresses recovery from cybersecurity events. The classroom decision table below is a teaching model built for Harbor Library, not a universal playbook or an assertion that NIST mandates these exact steps.

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
| Pause staff booking writes for fifteen minutes | Blocks edits through the staff workflow during investigation. | Staff must use the manual queue; patrons may wait. | Service-owner approval in R21 and an operator who can verify the pause. | Resume writes only after a checked booking state and owner sign-off. |
| Observe without intervention for ten minutes | Preserves normal service and may collect more context. | Unexplained edits could continue and harm more patrons. | Explicit lead decision accepting risk and a rapid review trigger. | Escalate immediately if another edit appears or a patron impact grows. |

The best option depends on current activity, confidence, reversibility and the service owner's tolerance. A **reasoned classroom proposal** is to ask the incident lead and identity owner to authorize session revocation, preserve the available narrow records and have the service owner ready to pause staff writes if edits continue. Another team might choose the short write pause first if the identity session cannot be linked reliably to the edits. The learner must explain the decision, authority and fallback; no fixed option is automatically correct.

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

### 3.4 Eradication requires a supported cause

Revoking a session is a containment action. It is **not proof** that a compromised credential, malicious browser extension, faulty training script or application bug has been removed. Before proposing eradication, the team needs to identify a cause well enough to choose a specific fix and a verification test. Examples of possible fixes include resetting a confirmed compromised credential, removing an identified malicious component, correcting a faulty application change or repairing an authorization rule. None of those causes is established in R1–R24. The case record should therefore say “cause unresolved; eradication plan pending evidence,” while continuing to check whether edits stop.

For example, suppose the session is revoked after 09:37 UTC and a **new** narrow query shows no later edits. That observation is compatible with at least three explanations: the revoked session caused the edits, the real source stopped independently, or the audit query missed later activity. R22, which was recorded at 09:32 UTC, cannot be used to verify a later revocation. Neither query can isolate a root cause. A proposed credential reset would become better supported if authorized identity evidence established credential misuse, but it would still require checking other sessions, tokens and recovery paths. A proposed application fix would require a reproducible software fault and a negative test demonstrating that the same unauthorized change no longer succeeds. The lesson is to match the **fix and its verification** to a supported mechanism.

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

### 3.7 Worked decision record and synthesis

An acceptable **proposed**, not executed, record is: “09:37 UTC; incident lead requests identity-owner approval to revoke `desk-a`'s current session after preservation of the available narrow records. R17–R18 show an unplanned `B20` edit following the earlier `B19` concern; the goal is to reduce further booking changes. Possible cost: front-desk reauthentication. Service owner approves a fifteen-minute staff-write pause as fallback under R21. Analyst will verify whether new edits occur and report at 09:45 UTC. Root cause and exposure remain unconfirmed.”

This chapter converts the earlier timeline into a bounded decision. Chapter 4 will test the whole response: intake, evidence, authority, proportionate action, recovery criteria and a review of what the team would change before another incident.

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

**Objective:** repair an unsupported closure claim. **Inputs:** R17–R24 and sections 3.3–3.4. **Output:** a three-sentence correction: what a *proposed* session revocation is intended to contain, which actor/cause/path questions remain, and what cause-specific test would be needed before an eradication finding. Explain separately why R22, recorded before 09:37, cannot verify the later proposal. A score of 2 does not assert that the branch revocation happened or that a quiet, narrow query proves cause removal.

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

<a id="ch-04"></a>

## Chapter 4 — Guided incident simulation and after-action review

### Learning outcomes

By the end of this chapter, a learner should be able to:

1. Run a contained response exercise from initial alert through an owner-approved service decision.
2. Produce a case record that separates observations, hypotheses, approvals, actions and results.
3. Test a return-to-service claim against explicit evidence instead of accepting a dashboard status.
4. Give a short, accurate internal update that protects people from premature attribution.
5. Identify a process gap, assign an owner and define a measurable improvement check.

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

### 4.6 After-action review

Close the tabletop with three questions: **What helped us decide? What slowed us down? What will we change and how will we check it?** Separate a one-time case correction from a reusable program improvement. For example, correcting `B19` and `B20` fixes two bookings; naming the booking service owner and rehearsing the approval path improves readiness for the next event. A good improvement ticket has an owner, a deadline and an observable test.

For this case, the team can turn the V1 audit failure into a testable improvement: assign the application and audit owner to find why the synthetic change lacks an actor identifier; require a new controlled test that produces the correct actor and UTC time; and have the response lead review the evidence before retiring any compensating monitoring. The ticket should also state what staff should do while attribution is incomplete. This is a **program control** improvement, distinct from correcting individual bookings. Another ticket could require the recovery lead to repeat an isolated restore and record its duration, source timestamp and booking comparison. An empty “review backups” task is not measurable.

The team should not call the case “resolved” merely because the tabletop ends. In the fictional facts, identity attribution and root cause remain open. The course ends when the learner can hand off that uncertainty safely, describe what evidence would close it and show how the organization will review its response process.

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

**Objective:** make a reversible 09:37 recommendation. **Inputs:** Round C, R17–R21 and the section 3.3 option matrix. **Output:** a decision card with current evidence and uncertainty, chosen proposal, approver and executor, intended benefit, uncovered path, service cost, preservation note, fallback, verification plan and 09:45 review. A score of 2 treats R21 as tolerance rather than execution and does not cite the Branch S/P result before Round D.

#### EX045 — Branch S review

**Objective:** bound what a successful session action actually demonstrates. **Inputs:** Round D **Branch S only**, before P1/C1 or V1; earlier R1–R24 remain available. **Output:** a four-row claim ledger with two supported claims and two unestablished claims, each with branch pointer and limit, plus one authorized next check with scope and owner. A score of 2 limits the “no later edit” observation to the branch query's range and does not claim eradication or correct booking state.

#### EX046 — Branch P review

**Objective:** account for operational effects of the pause. **Inputs:** Round D **Branch P only**, before P1/C1 or V1; R21's tolerance. **Output:** a queue-and-return note with the two pending requests, who holds them, a verification that writes were blocked, an owner-approved resume condition, a signal to keep the restriction, and the next checkpoint. A score of 2 does not mark the two requests fulfilled or the cause resolved and gives an explicit reconciliation step before resumption.

#### EX047 — Recovery acceptance

**Objective:** decide whether the supplied recovery evidence permits full release. **Inputs:** chosen branch, then the later P1/C1 and V1 cards. **Output:** a four-row return-to-service checklist covering booking correctness, authorized access, denied unauthorized access and actor/time audit visibility. For each, state expected result, current card result, owner and next test or correction; add a provisional service status and rollback trigger. A score of 2 marks B19/B20 mismatched and V1's blank actor as failed criteria rather than calling the book's simulated case recovered.

#### EX048 — Internal update

**Objective:** report the action while preserving uncertainty. **Inputs:** chosen Round D branch at 09:45 UTC, **before** P1/C1 and V1 are released. **Output:** exactly two sentences for an internal service-owner audience, naming the service, a supported observation and reported branch action, current uncertainty, owner and next checkpoint. For Branch P mention the manual queue; for Branch S mention reauthentication. A score of 2 does not assert breach, attacker identity, complete recovery, a validated restore or results from later cards.

#### EX049 — Improvement ticket

**Objective:** turn a case observation into a program improvement with proof of closure. **Inputs:** all four rounds, R23 or V1, and section 4.6. **Output:** one ticket with gap and evidence pointer, accountable owner, due date, bounded change, interim control and pass/fail verification. Choose either stale restore evidence or blank audit actor; do not bundle unrelated work into an untestable “improve security” task. A score of 2 explains why correcting B19/B20 alone would not close the selected program gap.

#### EX050 — Final handoff and self-assessment

**Objective:** give a new responder a complete, auditable state without overstating closure. **Inputs:** all rounds, one chosen branch, P1/C1, V1 and the section 4.5 rubric. **Output:** a one-paragraph handoff naming case and evidence, proposal versus branch-reported action and fictional approvers, current booking and audit failures, unresolved cause, owners, next review and rollback trigger. Add a six-row self-score (0–2 per tabletop output, maximum 12) and name the weakest output to revise. A score of 2 requires a defensible score explanation and no zero for approval or evidence scope; the handoff must distinguish the branch result from unexecuted correction or restore work.

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

### EX017 — Worked result

**R13 claim/limit:** the available summary reports one session in its time range, but contains no device or location field. Missing detail cannot identify a device or person; it is not a finding that the session came from the expected staff device. **R14 without T1:** the summary says no further edits after R9 *within its queried range*, but the exact range and filters are absent from R14 itself. **R14 with exercise-only T1:** the illustrative query concerns `desk-a` booking edits in `application-audit` at `09:00 ≤ event < 09:12 UTC`; it does not cover later times, another account, ingestion delay or a different source. A proposed next check asks the authorized application custodian for a new bounded query beginning at 09:12 and ending at a documented, sufficiently ingested cutoff, with source, account filters and completeness recorded. Even a zero-row result would be limited to that new scope.

### EX018 — Worked result

| Needed fact | Why the lead asks |
|---|---|
| Which booking-audit source, booking IDs and event interval contain the R9/R14 question? | Avoid copying unrelated patron records and make the later conclusion reproducible. |
| What exactly starts the 24-hour R15 deletion clock, and what is the custodian-confirmed last safe collection time? | R15 alone does not establish whether age is measured from event, ingestion, storage or another policy anchor. |
| Who may approve and perform the export, where will the unmodified copy be stored, and who may read it? | Collection must have authority, restricted access and an identifiable custodian. |

The analyst can ask the incident lead to decide promptly because detailed rows may disappear before the cause is established. The request is for a bounded copy and recorded policy answer, not an unapproved bulk export or a fabricated 09:03-plus-24-hours deadline.

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

### EX023 — Worked result

**Proposed request:** the service owner approves a named analyst to compare booking-edit audit rows for the short 08:30–09:20 UTC window with the authoritative booking state and relevant help-desk ticket identifiers, using only booking ID, changed field, old/new value, event UTC time and approved target where available. The application custodian supplies a restricted copy and records the query filter, source and collection time. The expected result schema is `booking ID | audit row | current value | owner-approved value or pending | confirmed mismatch / unresolved`. The learner can already point to B19's R9 edit but cannot supply a final count or approved target from R1–R16. Keep patron names and unrelated bookings out of the classroom output and limit the copy to the approved reviewers.

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

“At 09:37 UTC, revocation of the current `desk-a` session is **proposed** as containment; if approved and later confirmed, it would address only that session. The supplied R1–R24 records do not identify the human operator, establish credential compromise or exclude another session, account or application fault. A cause-specific eradication claim would require an authorized investigation that supports a mechanism, a targeted change such as a credential or software fix, and a test showing that mechanism no longer works under an adequate observation scope.”

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

**3. Action record.** At 09:37 UTC the analyst recommends revoking the current `desk-a` session because R17 and R18 weaken the training explanation and continued edits could harm bookings. The fictional incident lead and identity owner approve the narrow action; the identity administrator executes it in Branch S at 09:45. Expected effect: stop changes through that session. Cost: staff reauthentication. Preserve the available narrow records when it does not prolong harm. Fallback: the service-owner-approved fifteen-minute staff-write pause under R21 if edits continue. The response lead checks a new audit range and staff impact at the next checkpoint. This record distinguishes recommendation, authorization, execution and limited verification.

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
- **Handoff:** a case summary sufficient for another authorized person to continue the work.
- **Hypothesis test:** a planned check that could support or weaken an explanation.
- **Offset:** the explicit difference between a timestamp's local clock representation and UTC, needed for an unambiguous conversion.
- **Retention deadline:** the time after which a source may no longer preserve the needed record.
- **Triage:** the initial assessment of potential harm, urgency, uncertainty and next authorized action.

## Chapter 3 glossary

- **Containment:** a bounded action intended to limit further harm while investigation continues.
- **Eradication:** removal of an identified cause or persistence mechanism, followed by verification.
- **Fallback:** an alternative action prepared if the preferred intervention fails or becomes too costly.
- **Recovery acceptance:** evidence and owner sign-off needed before normal service resumes.
- **Residual risk:** uncertainty or exposure remaining after an action has reduced some harm.
- **Rollback trigger:** an observable condition for reversing a service change or returning to restricted mode.

## Chapter 4 glossary

- **After-action review:** a structured review of decisions, evidence, coordination and improvements after an exercise or event.
- **Branch card:** a fictional inject describing the outcome of a choice in the tabletop.
- **Exercise inject:** a new piece of scenario information released at a planned point.
- **Tabletop:** a discussion-based exercise in which participants reason through decisions without changing a live system.

## References for the authored chapters

1. NIST, [SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*](https://csrc.nist.gov/pubs/sp/800/61/r3/final), April 2025. Used for the integration of response across risk-management activities.
2. NIST, [Cybersecurity Framework 2.0 FAQ](https://www.nist.gov/cyberframework/faqs), section “Framework Components.” Used for the six concurrent and continuous functions.
3. CyberABC, [incident-response practice playbook index](../../../../../playbooks/incident-response-resilience/README.md). This index points to revision-pinned source playbooks; it is supplementary to the book. Source repositories retain their own rights.
4. NIST, [SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*](https://csrc.nist.gov/pubs/sp/800/86/final), August 2006. Used for the limited, authorized evidence-collection lesson in Chapter 2; this introductory exercise is not a substitute for a forensic or legal procedure.
5. NIST, [SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final), December 2016. Used for the Chapter 3 emphasis on planned, verifiable recovery.
6. NIST, [SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*, updated edition](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), November 2010. Used for the distinction between a backup status and a tested recovery plan.
7. NIST, [SP 800-84, *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*](https://csrc.nist.gov/pubs/sp/800/84/final), September 2006. Used for the Chapter 4 design, conduct and evaluation of a tabletop exercise.

All Harbor Library names, accounts, bookings, logs and times are invented for instruction. No real incident or person is described.
