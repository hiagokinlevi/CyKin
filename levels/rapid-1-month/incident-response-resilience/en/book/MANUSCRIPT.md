# Incident Response and Cyber Resilience: A One-Month Guided Course

- Language: English (`en`)
- Level: rapid course, one month; approximately 80 hours of planned study
- Editorial state: **draft**. All 4 subject-chapters now have initial teaching text, 50 exercises and worked results. Substantive expansion, detailed exercise specifications, specialist review, editing and A4 page verification remain pending.
- Public access: this draft is available to read and study; it is **not** a complete 300-page book or a qualification.
- Authorship and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi)
- Rights: original maintainer-owned text is dedicated under [CC0 1.0](../../../../../LICENSE); cited sources retain their own rights.

[Course overview](../README.md) · [Four-subject grade](../SUBJECTS.md) · [Subject skills](../SUBJECTS.md) · [Book plan](PLAN.md) · [Practice playbooks](../../../../../playbooks/incident-response-resilience/README.md)

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

### 1.4 Scope, authorization and safety

This book's labs use synthetic records only. In real work, incident authority comes from organizational policy, a contract, employment duties or explicit written approval. The authorization should identify the systems, accounts, data, time window and actions allowed. Investigating a partner's system, collecting personal data, changing access rights or taking a production service offline may require additional approval.

Use the smallest action that answers the immediate question. Reading a prepared copy of a log is different from altering the live source. Exporting a dataset may widen the number of people with access. A screenshot can omit the timestamp or the query that produced it. When evidence could later matter for legal or disciplinary decisions, follow the organization's evidence-handling procedure and obtain specialist guidance. This introductory course teaches a record discipline; it does not certify a forensic process.

For the Harbor Library exercise, the permitted scope is a fictional table of eight records in this chapter. Learners may annotate, sort and reason about the table. They may not attempt to contact a real library, probe a real domain or test a real account.

### 1.5 The first incident record

Open one record before investigating deeply. A practical minimum is:

| Field | Example for the fictional case |
|---|---|
| Case ID | `HL-IR-001` |
| Opened at | `2026-10-11 09:20 UTC` |
| Reporter and channel | Help-desk ticket `T-104` |
| Service and owner | Room booking; service owner pending confirmation |
| Observation | Two booking edits followed a staff-account sign-in outside ordinary hours |
| Assessment | Suspicious; compromise **not confirmed** |
| Scope and authority | Synthetic training data only |
| Evidence pointers | Records `R1`–`R8` below |
| Next question | Were the edits authorized by the staff member? |
| Next review | `2026-10-11 09:45 UTC` |

Use **UTC consistently** in this exercise. If a source uses another timezone, retain its original timestamp and record the conversion, including the offset. Never silently reorder events whose clocks may differ. Give each evidence item an identifier so that a later statement can cite its basis.

### 1.6 Worked example: the unusual sign-in

The following record is synthetic:

| ID | UTC time | Source | Observation |
|---|---|---|---|
| R1 | 08:40 | Identity log | Staff account `desk-a` signed in successfully |
| R2 | 08:42 | Application log | `desk-a` opened the booking dashboard |
| R3 | 08:43 | Application log | Two bookings were changed |
| R4 | 08:48 | Help desk | A patron said a room reservation disappeared |

The team can say that a sign-in preceded two changes and a complaint. It **cannot yet say** that the account was stolen, that the edits caused the complaint, or that data was exfiltrated. A safe next step is to preserve the four record identifiers, ask the service owner whether the edits match scheduled work, and seek the staff member's account activity through an authorized channel. Depending on organizational procedure and new evidence, the incident lead may then authorize additional collection or containment.

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

### 1.8 Common errors and chapter synthesis

- **Confusing suspicion with confirmation.** Use a hypothesis and state what would confirm or weaken it.
- **Skipping the service owner.** A technically plausible action can cause avoidable harm to users.
- **Losing the timeline.** Record source timestamps, timezone and collection time.
- **Expanding scope silently.** Ask before collecting or changing systems outside authority.
- **Treating a backup status as a restoration test.** A successful backup run is one fact, not a recovery guarantee.
- **Treating an absence in incomplete logs as evidence of absence.** State the collection limit.

Readiness is the ability to answer, under pressure, who owns the service, who can approve a decision, where trustworthy evidence can be found, and how a decision will be reviewed. This chapter prepares the alert-triage and evidence-preservation work in Chapter 2.

### Chapter 1 exercises

Work from the Harbor Library records unless an exercise says otherwise. For open answers, use the rubric in the worked results.

#### EX001 — Observation or inference

Classify each statement as a direct observation, a reasonable inference requiring confirmation, or an unsupported claim: (a) R4 records a cancellation of B18; (b) desk-a was compromised; (c) R5 reports that B18 disappeared; (d) R7 proves the service can be restored in ten minutes.

#### EX002 — First two questions

Write two questions the response lead should ask before deciding whether to disable `desk-a`. Name the person or evidence source that could answer each.

#### EX003 — Service dependency

Choose two dependencies from the service map. For each, explain one possible user impact and one evidence source that would help distinguish service failure from account misuse.

#### EX004 — Scope boundary

A learner wants to search a real public library website for a matching account name. Explain why that action is outside this lab's scope and propose a safe alternative.

#### EX005 — Timeline

Create a four-event timeline for R1, R3, R4 and R5 in UTC. State one ordering fact and one causal claim that the timeline does not establish.

#### EX006 — Role assignment

Assign the service owner, incident lead, analyst and recovery lead to these tasks: approve a potential booking outage, preserve R1–R5, coordinate the review time, and test whether a backup can restore a copy of the schedule.

#### EX007 — Minimal incident record

Draft a seven-field opening record for `HL-IR-001` using the dataset. Include status and uncertainty without claiming compromise.

#### EX008 — Evidence quality

For R6, R7 and R8, write one useful conclusion and one conclusion the record does **not** support.

#### EX009 — Decision alternatives

Compare “disable `desk-a` now” and “preserve records, verify with the owner and staff member, then decide.” Give one benefit, one cost or risk, and the approval needed for each.

#### EX010 — Communication draft

Write a two-sentence internal status update that is accurate at 09:00 UTC. Do not accuse a person or assert a breach.

#### EX011 — Escalation trigger

Name two new observations that would justify raising urgency, and explain how each changes the risk assessment.

#### EX012 — Practice record

Create a small decision log entry at 09:05 UTC for the authorized action “preserve a copy of R1–R5 and ask the service owner about planned training edits.” Include owner, reason and next review time.

#### EX013 — Readiness gap

Identify three readiness gaps revealed by this exercise. Prioritize one improvement that the organization can make before the next alert and define how it will verify the improvement.

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

### 2.4 Worked example: the second alert

The following records are also fictional and extend Chapter 1. They are the complete input for this chapter's exercises. No live system or external account is involved.

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

### 2.5 Handoff and common errors

A useful handoff lets a second analyst reconstruct the decision without guessing: case ID; current time and timezone; affected service; observed facts with record IDs; live hypotheses; confidence and limits; known service impact; actions completed under which authority; evidence locations; next question; decision owner; review deadline. It should also separate the source's event time from the time the analyst learned of the event.

Common errors are copying only an alert title, silently converting timezones, treating a staff recollection as proof, relying on a log summary that omits key fields, hashing a file without recording which bytes were hashed, or using a high severity label without naming harm and urgency. A careful analyst can be concise: cite the observation, state the limit and identify the next decision.

### Chapter 2 exercises

Use only records R1–R16 and the fictional authority described here. For open answers, compare your reasoning with the worked results at the end of this draft.

#### EX014 — Triage question

Turn the label “suspicious booking edit” into two answerable questions. For each, name a record or owner that could help answer it.

#### EX015 — Hypothesis table

For H1, H2 and H3, identify one supporting record, one limitation or contradiction, and one narrow next check. You may state that a record is weak support.

#### EX016 — Priority without false certainty

Write a provisional priority statement for 09:20 UTC that separates potential harm, time sensitivity and confidence. Include a review trigger.

#### EX017 — What the summary cannot prove

Explain why R13 does not establish that the `desk-a` session came from the expected staff device and why R14 does not prove that no later edit occurred.

#### EX018 — Retention decision

R15 announces a 24-hour deletion period for detailed audit records. List three facts the incident lead should know before approving a narrow export and explain why the export may need to happen before the root cause is known.

#### EX019 — Collection note

Draft a collection note for synthetic item `E1`: the Chapter 2 booking-audit rows R9 and R14. Include source, range, collector, authority, collection time, copy location, transformation and limitation. A made-up digest is **not** required.

#### EX020 — Hash claim

A learner hashes `E1.txt` twice and gets the same SHA-256 value. State two conclusions this supports and three conclusions it does not support.

#### EX021 — Time ordering

Order R9, R10, R12, R15 and R16 by their stated UTC times. Identify one reason that this order alone cannot establish the cause of the `B19` edit.

#### EX022 — Handoff

Write a five-sentence handoff for a second analyst at 09:20 UTC. It must include evidence IDs, a live hypothesis, one uncertainty, authorized next action and the next review time.

#### EX023 — Impact check

Specify a narrow, authorized impact check that could determine whether other bookings besides `B19` were affected. Name the owner, expected output and one privacy limit.

#### EX024 — Escalation threshold

Choose two new observations that would justify a faster containment decision and explain how each changes either harm or urgency. Do not claim they have happened in the supplied case.

#### EX025 — Correct a faulty note

Rewrite this sentence so that it is evidence-based: “The attacker stole `desk-a`, edited every booking and exfiltrated the patron database; R13 proves it.”

#### EX026 — Reproducible review

Another learner claims that H1 is confirmed by R6 and R10. Give a short counter-review: what those records actually say, what they do not say about `B19`, and what evidence would make the review stronger.

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
| R17 | 09:22 | Training owner | The approved task list did not include `B19` or `B20`; the owner knows of no addendum. |
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

### 3.4 Eradication requires a supported cause

Revoking a session is a containment action. It is **not proof** that a compromised credential, malicious browser extension, faulty training script or application bug has been removed. Before proposing eradication, the team needs to identify a cause well enough to choose a specific fix and a verification test. Examples of possible fixes include resetting a confirmed compromised credential, removing an identified malicious component, correcting a faulty application change or repairing an authorization rule. None of those causes is established in R1–R24. The case record should therefore say “cause unresolved; eradication plan pending evidence,” while continuing to check whether edits stop.

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

### 3.6 Worked decision record and synthesis

An acceptable **proposed**, not executed, record is: “09:37 UTC; incident lead requests identity-owner approval to revoke `desk-a`'s current session after preservation of the available narrow records. R17–R18 show an unplanned `B20` edit following the earlier `B19` concern; the goal is to reduce further booking changes. Possible cost: front-desk reauthentication. Service owner approves a fifteen-minute staff-write pause as fallback under R21. Analyst will verify whether new edits occur and report at 09:45 UTC. Root cause and exposure remain unconfirmed.”

This chapter converts the earlier timeline into a bounded decision. Chapter 4 will test the whole response: intake, evidence, authority, proportionate action, recovery criteria and a review of what the team would change before another incident.

### Chapter 3 exercises

Use the synthetic case only. Each answer should identify evidence, limits and the person who may approve an operational change.

#### EX027 — Three different goals

For session revocation, credential reset and an isolated restore test, identify which is primarily containment, which could be eradication if the cause is confirmed, and which supports recovery verification. State one uncertainty for each.

#### EX028 — Changed assessment

Explain how R17 and R18 change the Chapter 2 assessment. Name one hypothesis they weaken, one they strengthen and one fact they still do not establish.

#### EX029 — Decision matrix

Compare session revocation with the fifteen-minute staff-write pause. Give one benefit, one operational cost, one approver and one verification check for each.

#### EX030 — Risk of observation

If the lead chooses ten more minutes of observation, write a bounded review rule: deadline, new signal that would trigger immediate intervention, and person who owns the decision.

#### EX031 — Evidence before change

List four narrow records or facts to preserve before changing the session, when doing so does not dangerously delay harm reduction. Explain why the team might act first if edits are continuing rapidly.

#### EX032 — Avoid premature eradication

Correct this claim: “We revoked the session, so the incident is eradicated and the attacker is gone.”

#### EX033 — Recovery test

Design an isolated restoration check for the booking data. State the copy used, the expected booking state, a success criterion and a privacy or safety boundary.

#### EX034 — Backup limit

What does R23 establish, and what two additional checks would be needed before calling the booking service recoverable?

#### EX035 — Return-to-service criteria

Write three measurable acceptance checks the service owner could require before ending the staff-write pause.

#### EX036 — Decision record

Draft a six-field decision record at 09:37 UTC for a proposed session revocation. Include evidence IDs, approval owner, expected effect, side effect and next review.

#### EX037 — Residual risk

The booking page loads after the session is revoked. Explain why that alone does not justify closing the case; name two remaining questions.

#### EX038 — Alternative defensible choice

Argue for choosing the short staff-write pause first instead of session revocation. Name the assumptions under which this is reasonable and a condition that would make you change course.

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

**Inputs:** R1–R24, the service map, a case-note template from Chapter 1 and the decision/collection fields from Chapters 2–3. **Timebox:** four rounds of ten to fifteen minutes, then a twenty-minute review. **Outputs:** one case timeline, one hypothesis table, one approved-action record, one recovery test plan, one internal status message and one improvement ticket. Each output may fit on one page; completeness and reasoning matter more than length.

### 4.2 Release the injects in order

| Round | Facilitator reveals | Learner decision | Evidence to retain |
|---|---|---|---|
| A — readiness and intake | R1–R8 and a patron ticket | Identify service owner, authorized scope, observations and first questions. | Case ID, raw record IDs, UTC timeline and uncertainty. |
| B — triage | R9–R16 and the 24-hour retention notice | Update hypotheses, priority and preservation request. | Supporting and contradicting records, collector, authority and deadline. |
| C — response | R17–R24 and the owner's fifteen-minute write-pause tolerance | Compare at least two containment options; obtain a fictional approval and set a review time. | Decision owner, expected effects, side effects, fallback and verification. |
| D — recovery branch | The branch card below, chosen from the team's approved action | Test whether booking state and audit coverage justify limited service or further restriction. | Test result, residual uncertainty, service-owner decision and monitoring trigger. |

The facilitator should not reveal later records early. In a solo session, cover the later rows until each round is complete. If a learner chooses a different defensible action than the worked example, continue with the corresponding branch and state the assumptions rather than forcing the reference answer.

**Branch S: session revocation.** At 09:45 UTC, the identity administrator reports that the current `desk-a` session was revoked under the fictional incident lead's approval. A narrow booking query shows no later edits in its queried range. The staff member must sign in again. `B19` still shows an incorrect room until an owner-approved correction is made. This branch does not establish who used the prior session or that another access path is absent.

**Branch P: staff-write pause.** At 09:45 UTC, the service owner reports that staff writes were paused for fifteen minutes under the fictional approval. The manual queue has two pending booking requests. The booking audit shows no writes in the pause interval, but the cause of `B19` and `B20` remains unresolved. This branch does not prove the account is safe when writes resume.

For either branch, R23 still says the last documented restore test was thirty days earlier. The recovery lead should propose an isolated check of the booking state and a narrow audit check before declaring normal service. The privacy contact should review any new evidence of personal-data access; R24 alone is not clearance.

### 4.3 Worked tabletop: one acceptable path

**Round A.** The learner opens `HL-IR-001`, notes that R1 precedes booking edits, names the service owner as pending, records compromise as a hypothesis and asks whether the edits were training work. **Round B.** R9–R16 add an unexplained `B19` edit and a retention deadline. The fictional lead approves preserving the narrow audit copy and sets a 09:35 review. **Round C.** R17–R18 add an unplanned `B20` edit. The lead and identity owner approve session revocation after the available records are noted; the service owner stands by for a short write pause if edits continue. **Round D.** Branch S reports the revocation and no later edits in a limited query. The learner checks booking correctness, requests a bounded restore test, keeps the cause unresolved and proposes limited monitoring rather than closing the case.

This is one acceptable path. A team that prefers Branch P can pass if it explains the service cost, establishes approval, plans for the manual queue and states how it will decide when writes may resume. The exercise assesses **decision quality under incomplete information**, not agreement with a preselected action.

### 4.4 Score the evidence and the handoff

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

### 4.5 After-action review

Close the tabletop with three questions: **What helped us decide? What slowed us down? What will we change and how will we check it?** Separate a one-time case correction from a reusable program improvement. For example, correcting `B19` fixes a booking; naming the booking service owner and rehearsing the approval path improves readiness for the next event. A good improvement ticket has an owner, a deadline and an observable test.

The team should not call the case “resolved” merely because the tabletop ends. In the fictional facts, identity attribution and root cause remain open. The course ends when the learner can hand off that uncertainty safely, describe what evidence would close it and show how the organization will review its response process.

### Chapter 4 exercises

Use the four rounds and choose either Branch S or Branch P for your final decisions. The worked results give example answers and assessment criteria.

#### EX039 — Role and scope card

Write a five-role card for the incident lead, analyst, service owner, recovery lead and communications contact. For each, name one responsibility; then write the authorized tabletop scope in one sentence.

#### EX040 — Intake artifact

After Round A, write a four-line case intake containing ID, first observation, affected service, uncertainty and next owner question. Cite at least two R-records.

#### EX041 — Evidence chronology

Build a six-event UTC timeline using records from at least three rounds. Mark one apparent relationship that is temporal only, not proven causal.

#### EX042 — Competing explanations

At Round B, compare training, unauthorized account use and a display/synchronization problem. For each, name one record and one missing check.

#### EX043 — Preservation request

Write a narrow preservation request before R15's deadline. Include the owner who approves it, source/time range, collector and storage/access limit.

#### EX044 — Decision checkpoint

At Round C, choose session revocation or the write pause. Justify it using R17–R21, name the approver, expected benefit, side effect, fallback and next review.

#### EX045 — Branch S review

Assume Branch S. State two claims the branch supports and two claims it does not establish. Propose one next check.

#### EX046 — Branch P review

Assume Branch P. Name the manual-queue cost, a condition for resuming writes and a sign that would keep the restriction in place.

#### EX047 — Recovery acceptance

Create a four-item, observable return-to-service checklist for either branch. One item must concern booking correctness, one access control and one audit visibility.

#### EX048 — Internal update

Write a two-sentence internal status message for 09:45 UTC. Do not assert a breach, attacker identity, complete recovery or a validated backup restore.

#### EX049 — Improvement ticket

Create one after-action ticket for a readiness gap shown by the case. Give it an owner, a due date and a measurable check.

#### EX050 — Final handoff and self-assessment

Provide a one-paragraph handoff listing the chosen branch, evidence cited, completed fictional approvals, unresolved cause, next review and a rollback or escalation trigger. Score your six outputs using the Chapter 4 rubric and identify the weakest one to revise.

## Worked results and assessment rubric

These results are placed after the chapter material as the book's developing answer appendix. A different answer is acceptable when it cites the supplied record, states assumptions and explains authority and potential harm.

### EX001 — Worked result

(a) Direct observation in the application record. (b) Unsupported: compromise is a hypothesis. (c) Direct observation of a **report**, not independent confirmation of everything the patron experienced. (d) Unsupported: R7 states only that a backup job completed.

### EX002 — Worked result

Ask the service owner whether edits to B17 and B18 were authorized training work, using the training plan or change record. Ask the staff member or identity administrator whether `desk-a` was used by the expected person, through the approved contact and account-audit process. Other good questions identify affected bookings or current account activity without exceeding authority.

### EX003 — Worked result

For the identity service, an unauthorized session could permit booking edits; the sign-in and account-change records help test misuse. For the database, incorrect reservations affect patrons; the database audit log and authoritative schedule help test whether the application view is wrong. A strong answer separates possible impact from confirmed impact.

### EX004 — Worked result

The lab authorizes only the provided synthetic table. Searching or testing a real library may expose a third party's data or involve an account outside the learner's authority. Use the fictional `desk-a` records and document the missing fact as a question for the hypothetical authorized response lead.

### EX005 — Worked result

08:40 R1 sign-in; 08:43 R3 B17 edit; 08:44 R4 B18 cancellation; 08:48 R5 patron report. The sign-in preceded the edits. The ordering does not prove that the sign-in was unauthorized or that the R4 cancellation caused every aspect of the patron's report.

### EX006 — Worked result

Service owner: approve or reject a booking outage. Analyst: preserve R1–R5 within scope. Incident lead: coordinate the next review and decision record. Recovery lead: test restoration on an authorized copy. In a small organization one person may hold multiple roles, but approval and execution should remain explicit.

### EX007 — Worked result

One acceptable record has ID `HL-IR-001`; opened at 09:00 UTC; service “room booking”; reporter “help desk R5”; observation “R1 sign-in, R3–R4 edits and R5 report”; status “suspicious, compromise unconfirmed”; authorized scope “synthetic R1–R8 only”; next action “verify whether edits match training and record owner approval.” Include a review time if available.

### EX008 — Worked result

R6 supports that training was scheduled, not that these exact edits were approved. R7 supports that a backup job completed, not that restoration will meet a recovery target. R8 states that this summary has no relevant destination detail, not that no data transfer occurred.

### EX009 — Worked result

Immediate disablement might stop further unauthorized changes but might disrupt legitimate staff work; it requires the designated incident or service authority. Preserve-and-verify protects evidence and reduces needless disruption but may allow harm to continue if compromise is real; it too requires authorized collection and a short review deadline. A good comparison states what new evidence would change the choice.

### EX010 — Worked result

“We are reviewing unusual booking changes associated with `desk-a` and a patron report; the cause and scope are not yet confirmed. The response lead is preserving the available records and checking whether the changes match scheduled training before the next decision at 09:15 UTC.”

### EX011 — Worked result

A fresh booking edit after the staff member denies use of the account would increase confidence of unauthorized activity and urgency. Evidence that multiple accounts made unexpected changes could expand the affected scope. Other defensible triggers include confirmed sensitive-data access, a service outage, or inability to account for continued changes, provided the response explains the evidence.

### EX012 — Worked result

“09:05 UTC — Incident lead approved preservation of synthetic records R1–R5 and a question to the service owner about planned training edits. Reason: preserve the observed sequence and test the leading authorized-work hypothesis without changing production access. Analyst will prepare the copy; next review 09:15 UTC.” The exact names may be fictional; the approval and review time must be explicit.

### EX013 — Worked result

Three gaps are an unconfirmed service owner, unknown clock synchronization and no recorded restore-test result. Prioritize naming the service owner and alternate, then verify the improvement by having both acknowledge a tabletop scenario and approve or reject a simulated booking outage within the agreed time. Another answer may prioritize clock or recovery testing if it states a measurable check.

### EX014 — Worked result

“Was `B19` part of the authorized training?” can be checked with the training owner and R10, then with any approved exercise addendum. “Are other bookings currently affected?” can be checked by the service owner using a narrow booking-audit comparison. A good answer identifies a source and acknowledges that its absence or silence is not conclusive.

### EX015 — Worked result

H1: R6 and R10 support that some training occurred, but R10 does not list `B19`; ask the training owner for the complete task list. H2: R9 and R12 make unexpected account use plausible, but R12 is a recollection and R13 lacks device detail; ask for the authorized detailed identity record. H3: R11 could describe a display problem, but R9 records an actual application edit; compare the approved booking state and user view. Alternative hypotheses are acceptable if they cite the records and identify a discriminating check.

### EX016 — Worked result

“Prompt review at 09:20 UTC: potential harm includes at least one possibly wrong booking and a second patron report; urgency is raised by R15's short retention period; confidence of compromise remains low to moderate because training explains some edits but not yet `B19`. Preserve authorized records, check impact and training scope, and review at 09:35 UTC or immediately if another unexplained edit appears.” The label is provisional; the reasons and trigger matter more than an arbitrary severity number.

### EX017 — Worked result

R13 is a summary of one session in the available range, without device or location fields; it cannot tie the session to a particular device or person. R14 states that no further edits are *shown within the queried range*. It does not cover later times, a different account, missing records or an incomplete export.

### EX018 — Worked result

The incident lead needs the affected source and time range, the approved collector and access scope, and the deletion deadline or retention mechanism. Also useful are the expected sensitivity of patron data, storage location and access limit. The export may be time-critical because its records could disappear even if the hypothesis remains unresolved. Approval must still follow organizational procedure.

### EX019 — Worked result

“`HL-IR-001/E1`; booking-audit rows R9 and R14 in this chapter; events 09:03–09:12 UTC; copied at 09:20 UTC by the learner analyst under the fictional incident lead's classroom authorization; saved as a local training-only working note; original remains in the Markdown book; rows transcribed without changing stated event times. Limitation: the rows are synthetic and R14 summarizes only its query range. If saved as a file, record a SHA-256 value for its exact bytes and any later check.” A valid note need not invent a digest or imply production evidence.

### EX020 — Worked result

The two readings support that the checked byte sequence produced the same digest at both checks and that no change to this copy was detected by that comparison. They do not prove that the original log was complete, that its clock or contents were correct, or that the export was collected with authority. They also do not prove that another unexamined copy is identical. A digest should be tied to a named file, method and times.

### EX021 — Worked result

R9 09:03; R10 09:04; R12 09:08; R15 09:14; R16 09:16 UTC. R10 is a training-plan record observed at 09:04 in the classroom dataset; the plan may have been written earlier. This order cannot establish whether the `B19` edit was authorized, who performed it or whether it caused the patron's reported display problem.

### EX022 — Worked result

“At 09:20 UTC, case `HL-IR-001` includes a `B19` booking edit in R9, a plan omitting `B19` in R10 and a second patron report in R11. H1 still explains earlier training edits, while H2 remains possible for `B19`; the available identity summary R13 lacks device detail. The incident lead authorized preserving the synthetic records for this exercise and requests a narrow impact and training-scope check in the hypothetical real response. The analyst will record source and collection limits, with no account change yet. Review at 09:35 UTC or immediately if new unexplained edits occur.” Other concise handoffs pass when they include the required elements and do not overstate certainty.

### EX023 — Worked result

The service owner can ask an authorized analyst to compare the application audit for the same short period with the authoritative booking state and relevant help-desk tickets. The output is a count and identifiers of possibly altered bookings, each linked to an audit row and marked confirmed or unresolved. Restrict the review to the necessary fields and people; do not export the entire patron database for this question.

### EX024 — Worked result

A new unexplained edit after 09:20 would raise urgency because harm may still be occurring. A confirmed large set of wrong reservations would raise potential harm and the need for a service-owner decision. A confirmed sensitive-data disclosure would also raise harm, but no supplied record establishes one. A strong answer identifies the new evidence required and the decision owner.

### EX025 — Worked result

“R9 records a `B19` booking edit by `desk-a`, and R11 records a patron's report. The available identity summary R13 does not identify the device or user behind the session. Unauthorized use, broad booking impact and data transfer are unconfirmed; the team will check training scope, booking impact and authorized identity detail.” This version distinguishes observations, hypotheses and missing evidence.

### EX026 — Worked result

R6 says training was scheduled; R10 says its plan names `B17` and `B18`. Neither record says that `B19` was an approved training task or that the staff member made the R9 edit. The reviewer should seek a complete approved plan or addendum and ask the training owner whether `B19` was included; authorized detailed application and identity records could then help test who performed the edit. Treat the answer as unresolved until those checks are assessed.

### EX027 — Worked result

Revoking the current session is containment: it may limit that session but not another path. A credential reset could help eradicate a **confirmed credential-compromise cause**, but the cause is not yet confirmed and the reset alone may be insufficient. An isolated restore test supports recovery verification; it does not prove that the live service is safe or that bookings are correct.

### EX028 — Worked result

R17 weakens H1 as a full explanation because the approved task list omits `B19` and `B20`; R18 supports concern about further unexplained activity and therefore makes H2 more plausible. Neither record identifies the human or device behind `desk-a`. A good response still allows for an incomplete plan, a mistaken recollection or another system fault until checked.

### EX029 — Worked result

Session revocation may quickly stop the current session, but legitimate staff must reauthenticate; the incident lead and identity owner approve it under the fictional policy, and the analyst checks subsequent booking and identity records. The short write pause may stop edits through the staff workflow regardless of the session, but creates a manual queue; the service owner approves it under R21, and the operator verifies writes are paused and reviews queue entries. Neither check proves root cause removal.

### EX030 — Worked result

“Incident lead accepts ten minutes of observation until 09:47 UTC. Any additional unexplained booking edit, broad patron impact or evidence that audit records are about to disappear triggers immediate review with the service owner and identity administrator.” Other defensible triggers pass if they are observable, time-bound and assigned to an owner.

### EX031 — Worked result

Retain a narrow copy or pointer for R18's booking audit row, the available session summary R13, the approved training list R10/R17 and the current booking-state export R20, recording source and collection limits. If rapid further edits are harming patrons, an authorized containment action may be warranted before every collection finishes; record what was missed and why, rather than silently claiming complete preservation.

### EX032 — Worked result

“The current session was revoked as a containment step. We have not established who made the edits, whether another session or path exists, or what caused the change. Eradication requires a supported cause, a targeted fix and verification that the mechanism no longer operates.” Do not equate a lack of observed new edits in a narrow range with eradication.

### EX033 — Worked result

Use an authorized isolated copy from the last backup, compare `B17`–`B20` with the approved booking source, and test that a synthetic booking can be read and changed only by the intended role. Success means the copied data and access checks meet stated expected results, with differences documented. Do not overwrite the live schedule or disclose patron records in the classroom test.

### EX034 — Worked result

R23 establishes that a backup job succeeded and that the most recent documented restore test was thirty days earlier. The recovery lead should test restoration of a bounded copy and compare the restored bookings with the owner-approved state. It should also verify that access controls and audit records function after restoration. R23 alone supplies none of those results.

### EX035 — Worked result

For example: the owner reviews and corrects each affected `B17`–`B20` state; a synthetic booking made by an authorized test role succeeds while an unauthorized role is denied; and the audit shows the test action with actor and UTC time. Add a monitoring period and an explicit trigger to reapply the pause. “The service works” is too vague to measure.

### EX036 — Worked result

“09:37 UTC; proposal: revoke the current `desk-a` session; basis: unplanned `B20` edit R18 and training-owner statement R17; approvers: incident lead and identity owner; expected effect: stop changes from this session; side effect: staff reauthentication and possible workflow delay; fallback: service-owner-approved short write pause under R21; next review: 09:45 UTC against booking audit and impact check.” A completed-action claim would be incorrect before the branch result is supplied.

### EX037 — Worked result

A loading page proves only that a page responded in that check. The team still needs to know whether booking data is correct and whether unexplained edits have stopped across an adequate observation range. It also lacks a supported root cause and a tested recovery path. Keep the case open or in monitored restricted status under the organization's policy.

### EX038 — Worked result

The write pause is reasonable if the unexplained edits could come through more than the single known session, staff can use the manual queue for fifteen minutes, and the service owner approves the cost. Verify that writes actually stop and that queued requests are reconciled. Change course if patron harm grows, the pause fails, or detailed identity evidence points to a narrower intervention with lower operational cost.

### EX039 — Worked result

Incident lead: set priorities and record approvals. Analyst: handle the supplied records and report limits. Service owner: weigh booking disruption and approve a write pause. Recovery lead: design an isolated restore and service check. Communications contact: prepare accurate internal updates and privacy coordination. Scope: reason only from R1–R24 and the two fictional branch cards; make no real system changes. Combining roles is acceptable when decisions remain explicit.

### EX040 — Worked result

“Case `HL-IR-001`; R1 records a `desk-a` sign-in and R3–R4 record booking edits. The affected service is room booking; R5 is a patron report, not proof of compromise. Training may explain some edits but the service owner must confirm the authorized plan. The incident lead will preserve the case note and set a review time.” Four lines with equivalent facts, IDs, uncertainty and an owner question pass.

### EX041 — Worked result

One valid six-event timeline is R1 08:40 sign-in, R4 08:44 cancellation, R9 09:03 `B19` edit, R15 09:14 retention notice, R18 09:24 `B20` edit and R21 09:29 write-pause tolerance. The sign-in came before the edits, but this order does not prove that the sign-in was unauthorized or that it caused each edit. Other six-event selections pass when UTC order and limits are clear.

### EX042 — Worked result

Training: R6 supports scheduled work, but ask the training owner for the complete approved task list. Unauthorized account use: R9 is unexplained, but ask for approved detailed identity evidence before attributing a user. Display/synchronization problem: R11 is compatible with a display symptom, but compare the authoritative booking state and audit because R9 records an edit. The answer should identify what would distinguish the explanations.

### EX043 — Worked result

“Before the 24-hour deadline in R15, the incident lead authorizes the named analyst to preserve booking-audit rows for `B17`–`B20` and the relevant identity summary covering 08:30–09:30 UTC. Record source, export method and collection time; keep an unmodified authorized copy in restricted case storage and analyze a separate working copy. Limit patron details to the fields needed to test the booking question.” Do not claim an export already occurred.

### EX044 — Worked result

One acceptable choice is to seek incident-lead and identity-owner approval to revoke the current session after narrow record preservation. R17–R18 show edits outside the known training tasks; the goal is to stop further changes from that session. Staff reauthentication is a side effect. The service-owner-approved write pause under R21 is a fallback if edits continue; review at 09:45 UTC. Choosing the pause first also passes if its manual-queue cost and verification are addressed.

### EX045 — Worked result

Branch S supports that the specified session was revoked and that no later edit appears in the narrow queried range. It does not establish the user behind the prior edits or rule out another account, session or unqueried period. The next check could compare the approved booking state with `B19` and inspect the authorized detailed identity record.

### EX046 — Worked result

The manual queue accumulates two requests and may delay patrons or create reconciliation work. Resume writes only after the service owner has reviewed booking correctness, confirmed the pause worked, and approved a monitored return. Keep the restriction if unexplained edits resume, the booking state is still inconsistent or the queue cannot be reconciled safely.

### EX047 — Worked result

The owner reviews and corrects the affected booking state against an authoritative source; an authorized synthetic role can make a test booking; an unauthorized synthetic role cannot edit it; and the audit logs the test with correct UTC time and actor. For either branch, define who signs off, how long to monitor and what result would trigger rollback.

### EX048 — Worked result

“At 09:45 UTC we are reviewing unexplained changes to several room bookings and have preserved the available case records under the incident lead's fictional authorization. The selected temporary restriction is in place, but the cause and full impact remain under review; the service owner and response lead will reassess booking correctness and access controls at the next checkpoint.” Substitute the chosen branch explicitly in an actual tabletop submission.

### EX049 — Worked result

“Owner: booking service manager. Due: within 30 days of the exercise. Gap: the service owner and backup-restore evidence were not immediately available. Action: document the primary and alternate owners and run a tabletop approval drill plus an isolated restore check. Verify: both owners respond within the agreed period and the recovery lead records an actual pass/fail result with booking-state comparisons.” One narrower ticket also passes if its check is observable.

### EX050 — Worked result

One acceptable handoff names Branch S, cites R17–R21 and the branch result, states that the fictional lead and identity owner approved revocation, notes that root cause and possible additional access remain unresolved, sets the next audit and booking-state review, and triggers escalation if an unexplained edit recurs. Apply the six-output rubric: for example, timeline 2, hypotheses 2, action 2, recovery 1, status 2, improvement 1 = 10/12, with recovery as the first revision target. Other scores pass only when justified against the rubric and no approval or evidence-scope output scores zero.

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
- **Confidence:** the analyst's assessed support for an explanation, stated with its limits.
- **Digest:** the output of a hash function for a specific byte sequence.
- **Handoff:** a case summary sufficient for another authorized person to continue the work.
- **Hypothesis test:** a planned check that could support or weaken an explanation.
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
