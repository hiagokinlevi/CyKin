# Cybersecurity: A One-Month Guided Course

- Edition: published, 13 October 2026
- Language: English (`en`)
- Course: rapid, one month; approximately 80 hours of planned study
- Status: Twenty English chapters published, with exercises EX001–EX036 and worked results. The rapid-course planning minimum is 20 lessons and there is no maximum. Technical, language, source, and accessibility review are **not complete**. This is not a finished qualification.
- Maintainer: [hiagokinlevi](https://github.com/hiagokinlevi)
- Original text: [CC0 1.0](../../../../../LICENSE), within the [rights notice](../../../../../RIGHTS.md). External sources linked below retain their own rights.

## How to study this book

Read the explanation before attempting an exercise. Work only with the fictional library described here. Keep a short notebook with the facts you observe, the assumptions you make, and the question you would ask next. Compare your responses with the worked results at the end. A plausible alternative can be correct when it identifies its assumptions and supports its decision with evidence.

This is the **one principal book** for the English rapid Cybersecurity course. It incorporates the earlier Security Literacy text. Each published chapter teaches one idea with an example and exercises. Worked results are in the final appendix. The planning minimum for this rapid book is 20 lessons, and there is no maximum. These twenty published chapters meet that minimum and are not a finished qualification.

| Subject-chapter | Authored exercises | Publication |
|---|---:|---|
| 1. Foundations and decisions | EX001–EX005 | Published |
| 2. Scope, permission and safe practice | EX006–EX010 | Published |
| 3. Systems, data and dependencies | EX011–EX015 | Published |
| 4. Guided lab and applied synthesis | EX016–EX020 | Published |
| 5. What may be said about a booking | EX021 | Published |
| 6. A handwritten change is not a correction | EX022 | Published |
| 7. A pending queue during an outage | EX023 | Published |
| 8. A weak procedure is not yet a vulnerability | EX024 | Published |
| 9. A verdict tally is not a severity | EX025 | Published |
| 10. A spoken time is not a printout | EX026 | Published |
| 11. A named sheet does not free the room | EX027 | Published |
| 12. A missing row is not a free room | EX028 | Published |
| 13. Yesterday's naming does not bind today | EX029 | Published |
| 14. A new page answers only its own rows | EX030 | Published |
| 15. Two pages are not one schedule | EX031 | Published |
| 16. A created time does not erase a printed row | EX032 | Published |
| 17. Matching rows are not a cause | EX033 | Published |
| 18. Earlier pages stay in the file | EX034 | Published |
| 19. A booking page does not open the contact list | EX035 | Published |
| 20. The note that can leave the room | EX036 | Published |

<a id="ch-01"></a>

## Chapter 1 — Cybersecurity: foundations and decisions

### Learning outcomes

After this chapter, you should be able to:

1. Describe an asset, a threat, a vulnerability, a control, a risk scenario, and evidence in ordinary language.
2. Explain confidentiality, integrity, and availability with a concrete service example.
3. Separate an observation from an assumption and a recommendation.
4. Describe the six functions of the NIST Cybersecurity Framework (CSF) 2.0 without treating them as a required sequence or a product checklist.
5. Produce a small, reviewable security note without probing a real system.

### 1.1 Start with the service and the people

Security begins with a question: **What needs to keep working, for whom, and what harm would follow if it did not?** The answer gives meaning to the technical details. A server is not valuable merely because it is a server. It matters because it supports a service, stores information, or helps people complete a task. A login page matters because it controls access to something behind it. A backup matters if it can actually restore the service within the time its users need.

Our teaching case is **Harbor Library**, an entirely fictional public library. Residents reserve study rooms through a website. Staff can view reservations, resolve conflicts, and print a daily schedule. The library also keeps a list of patrons who asked to receive event announcements. These are invented details; no real library or personal records are used in this lesson.

Before proposing a security tool, list the service outcomes:

| Service outcome | People affected | Example of harm if it fails | Question to verify |
|---|---|---|---|
| Residents can reserve available rooms | Residents and front-desk staff | A resident travels to a room that was double-booked | How are conflicting reservations prevented? |
| Staff can see an accurate daily schedule | Staff and residents | Staff give a room to the wrong group | What is the authoritative schedule? |
| Event contacts are used only for announcements | Subscribers | Unwanted disclosure or misuse of contact details | Who can export the contact list, and why? |

This table is a first model, not a verified inventory. In a real organization, a service owner would confirm the outcomes and acceptable disruption. For the exercises here, the fictional case is the full scope; do not test an actual website.

### 1.2 Name assets and dependencies

An **asset** is something of value that helps provide or protect a service. It can be information, software, a device, an account, a process, or a person's time and trust. Harbor Library's reservation records are information assets. The booking application, staff accounts, backup copies, and printed schedule are also assets. Their value and handling differ: a printed schedule may be essential during an outage, while a staff account can change reservations and therefore needs strong access controls.

A **dependency** is something a service needs in order to work. The booking page may need an identity service, a database, a network connection, and staff procedures. A dependency does not automatically become a single point of failure; that claim requires evidence about alternatives and recovery. Draw a simple chain before assigning a control:

```text
Resident -> booking page -> reservation store -> staff schedule
                         \-> confirmation message
Staff member -> staff sign-in -> reservation store
```

The arrows mean information or a request moves between parts of the service. They do not prove the implementation is built this way. That distinction matters: a diagram is a hypothesis until an owner or observation confirms it.

### 1.3 Three properties of information

The familiar **confidentiality, integrity, and availability** model describes three different ways a service or its information can be harmed. It is a teaching lens, not an exhaustive list of all harms.

- **Confidentiality** asks who may see information. If the event contact list is sent to an unauthorized recipient, confidentiality is affected even if the booking site remains online.
- **Integrity** asks whether information is correct and changed only in the intended way. If a reservation is silently altered, the schedule can be available but wrong.
- **Availability** asks whether authorized people can use the service when needed. An outage can prevent a resident from booking and staff from checking the schedule even if no information is disclosed.

One event can affect several properties. For example, an account with excessive privileges might export the contact list and change room bookings. Avoid reducing the analysis to one label. State the actual consequence, the people affected, and what is known.

Other concerns may matter too: whether a person's data was collected for a legitimate purpose, whether records can be traced to an authorized action, and whether the library can restore service after a disruption. Later chapters will treat these in more depth.

### 1.4 Distinguish threat, vulnerability, event, and risk

A **threat** is a circumstance or event with potential for harm. The [NIST glossary's threat entry](https://csrc.nist.gov/glossary/term/threat) includes unauthorized access, disclosure, modification, and denial of service among possible impacts. A threat is not proof that an attack occurred.

A **vulnerability** is a weakness that a threat source could exploit or trigger. The [NIST glossary's vulnerability entry](https://csrc.nist.gov/glossary/term/vulnerability) includes weaknesses in systems, procedures, controls, and implementations. A reused staff password is a possible weakness. Whether that weakness exists at Harbor Library is unknown; the case does not assert it.

An **event** is something observed: for example, the fictional schedule became unavailable from 10:00 to 10:20. An event alone does not establish its cause. It might result from maintenance, a software error, a network failure, or malicious activity. An **incident** is an event or series of events judged to require a security response under defined criteria. The course will use the organization's response criteria rather than labeling every error an attack.

A **risk scenario** links a plausible condition to an outcome: “If an unauthorized person changes room reservations, residents may receive incorrect confirmations and staff may allocate rooms incorrectly.” This statement does not assign a probability. It also does not claim that any unauthorized change has happened. To prioritize action, add context: how critical is the service, what controls exist, what evidence supports the scenario, and what uncertainty remains? A number without these inputs would create false confidence.

The six CSF 2.0 functions—**Govern, Identify, Protect, Detect, Respond, and Recover**—offer a common language for discussing these responsibilities. NIST describes them as concurrent and continuous outcomes, not a strict six-step procedure. For Harbor Library, assigning an owner for reservation data is governance; understanding the booking dependency is identification; access restrictions are protection; noticing unexpected changes is detection; containing an account misuse is response; restoring a trustworthy schedule is recovery. A single practical decision can involve more than one function. See the [NIST CSF 2.0 FAQ](https://www.nist.gov/cyberframework/faqs) for the framework's own description.

### 1.5 Controls must answer a specific concern

A **control** is a measure intended to reduce risk or improve an outcome. It may be technical, procedural, or organizational. “Use security software” is too vague to evaluate. “Require staff to use an approved second factor when signing in to the reservation administration page” describes a population, an action, and a boundary. It still needs verification: do all staff accounts follow the rule, can an approved user recover access, and is there a safe exception process?

For personal digital safety, [CISA's Secure Our World guidance](https://www.cisa.gov/secure-our-world) recommends recognizing and reporting phishing, using strong passwords and a password manager, enabling multifactor authentication, and updating software. These are useful starting actions. They do not replace a service-specific analysis. A library could implement all four and still have an untested restore process or an unclear owner for the event contact list.

Think in terms of **prevent, notice, act, and recover**. A control that reduces a chance of misuse may fail or be bypassed. The library therefore also needs a way to recognize abnormal changes, a person who can act, and a procedure to restore correct information. The right combination depends on the service's importance and verified facts. More controls are not automatically better: a procedure that no one owns is unlikely to work under pressure.

### 1.6 Use evidence without overclaiming

Security literacy includes knowing what a statement is based on. A useful working note separates four kinds of sentence:

1. **Observed fact:** “The fictional exercise log records a failed staff sign-in at 09:14.” The evidence is named and its scope is clear.
2. **Reported fact:** “The service owner says the printed schedule is refreshed each morning.” The speaker and time are named; the statement has not yet been independently checked.
3. **Inference:** “If printing occurs only in the morning, staff may not see later reservations during an outage.” This follows from the report but still needs testing.
4. **Recommendation:** “Test a midday outage and compare the printed schedule with the authoritative reservation list.” This proposes a check, not a claim about the present system.

The distinction prevents a common mistake: turning a plausible explanation into a finding. If a page is unavailable once, it is inaccurate to write “The library was attacked.” Instead, record the time, what failed, who observed it, and what logs or owner testimony could help determine the cause. Do not collect or publish patrons' personal information to make a teaching point.

Evidence has limits. A screenshot of a backup job may show that the job was configured. It does not prove a usable copy was produced or that a full service restore will meet the library's needs. A single test at noon does not prove the service is always available. Good notes identify both what the evidence supports and what it cannot establish.

### 1.7 A small guided analysis

Read this **synthetic** record. It is invented for this book, not a real incident:

```text
09:00  Staff print the daily room schedule.
10:05  A resident receives a booking confirmation for Room 2 at 14:00.
11:30  The booking page is unavailable to the front desk for 20 minutes.
11:42  Staff use the printed 09:00 schedule to answer a room question.
12:10  A staff member notices that the 10:05 booking is absent from the printout.
```

What is established? The printout predates the booking, and the later booking is absent from it. The record also says the page was unavailable to the front desk for twenty minutes. It does **not** establish why the page failed, whether residents could use it, or whether anyone accessed the contact list. The first concern is that staff may make a decision from stale information during an outage. A proportionate next action is to ask the service owner how staff should confirm current bookings when the live schedule is unavailable, then test that fallback with synthetic bookings.

A compact analysis note could read:

> In a fictional outage exercise, staff used a 09:00 printout after a 10:05 booking. The printout did not include that booking. The exercise therefore demonstrates a stale-schedule risk for front-desk decisions; it does not establish the cause of the booking-page outage. Confirm the fallback procedure with the service owner and test it with a later reservation.

This is the pattern for the rest of the course: name the service, describe the evidence, limit the conclusion, and propose a safe check. Chapter 2 adds authorization, scope, and stop conditions so that this method can be practiced responsibly.

### Chapter 1 summary

Security vocabulary is useful only when it improves a decision. Name the service and people first, map valuable assets and dependencies, describe the kind of harm, then connect a plausible condition to evidence and a proportionate control. Keep observations, assumptions, inferences, and recommendations distinct. The next chapter shows how to practice this work within an authorized boundary.

### Chapter 1 exercises

Use the fictional case only. Compare your work with the final worked-results appendix.

### EX001 — Asset and dependency map

- **Objective:** Distinguish a service, an asset, and a dependency.
- **Input:** The Harbor Library description in Sections 1.1–1.2.
- **Safe condition:** Work from this text alone; do not browse or test a real library.
- **Task:** Name the booking service, three different assets, and two dependencies. Explain why one asset matters to residents.
- **Expected evidence:** A five-item annotated map or short table.
- **Rubric:** Credit for a clear service outcome, three plausible assets of at least two kinds, two dependencies, and a resident-facing consequence.

### EX002 — Three kinds of harm

- **Objective:** Apply confidentiality, integrity, and availability without conflating them.
- **Input:** The fictional services in Section 1.1.
- **Safe condition:** Invent events; use no real personal information.
- **Task:** Write one distinct scenario for each of the three properties. For each, name the affected people and one fact you would need to check before claiming the event occurred.
- **Expected evidence:** Three labeled scenario statements and three verification questions.
- **Rubric:** Credit for matching the harm to the property, identifying people, and not asserting an unobserved event as fact.

### EX003 — Observation or inference

- **Objective:** Calibrate a conclusion to the available evidence.
- **Input:** The five-line synthetic record in Section 1.7.
- **Safe condition:** Analyze the supplied text only.
- **Task:** Classify these claims as supported, unsupported, or a reasonable inference: (a) a 10:05 booking was absent from the 09:00 printout; (b) an attacker caused the outage; (c) a stale printout could mislead staff; (d) the event contact list was exported. Explain each classification.
- **Expected evidence:** Four classifications and one sentence of reasoning each.
- **Rubric:** Credit for correct limits and an explanation tied to the record.

### EX004 — Control and check

- **Objective:** Propose a proportionate measure with evidence of effectiveness.
- **Input:** The stale-schedule issue in Section 1.7.
- **Safe condition:** Design a paper exercise; do not change a live system.
- **Task:** Propose one fallback procedure for staff during a booking-page outage. Define its owner, trigger, verification step, and one failure mode.
- **Expected evidence:** A four-part procedure plus a sample test with a synthetic booking.
- **Rubric:** Credit for an explicit owner and trigger, a test that can detect stale data, and an honest limitation.

### EX005 — Six-function view

- **Objective:** Use the CSF 2.0 functions as a vocabulary for service decisions.
- **Input:** Harbor Library and the [NIST FAQ](https://www.nist.gov/cyberframework/faqs).
- **Safe condition:** Work with the fictional case only.
- **Task:** Give one Harbor Library example for each of Govern, Identify, Protect, Detect, Respond, and Recover. Explain why completing one function does not finish security work.
- **Expected evidence:** Six short examples and a two-sentence explanation.
- **Rubric:** Credit for examples that match each function, recognize shared responsibility, and avoid treating the functions as a once-only sequence.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 20

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

After this chapter, you should be able to define an allowed study activity, identify who can authorize it, write stop conditions, choose a synthetic data set, and report an observation without collecting unnecessary personal information.

### 2.1 Curiosity needs a boundary

The first chapter used an invented schedule so every reader could practice the method. A public website is different. Being able to open a page does not mean you have permission to probe the system behind it, test accounts, collect records, or disrupt its operation. A training exercise needs a named environment, an owner, permitted actions, and a way to stop. Reading a public document and testing a live service are different activities, even when the learner's intent is educational.

This course uses **synthetic** records and paper exercises by default. A learner may work with a real system only after its owner has authorized the specific activity and the learner understands the organization's rules. This is a practice rule for the course, not legal advice about any jurisdiction. If authorization is unclear, the next step is to ask the owner; it is not to test first and explain later.

The [NIST SP 800-115 testing guide](https://csrc.nist.gov/pubs/sp/800/115/final) describes planning and conducting technical assessments. Its [rules-of-engagement definition](https://csrc.nist.gov/glossary/term/Rules_of_Engagement) emphasizes guidelines and constraints set before a test. This rapid course stays at the level of defining safe scope and reviewing evidence. It does not require active testing of anyone else's systems.

### 2.2 Write an authorization brief

Imagine that Harbor Library's service owner wants staff to rehearse what to do if the room-booking page becomes unavailable. The approved exercise can be entirely offline. A one-page brief should answer seven questions:

| Question | Harbor Library exercise answer |
|---|---|
| Who owns the exercise? | The fictional service owner appoints a front-desk lead. |
| What is in scope? | A paper schedule, invented reservations, and a role-play of a 20-minute outage. |
| What is out of scope? | Live accounts, real residents, the actual booking page, and production data. |
| What may participants do? | Compare printed and synthetic later bookings; record decisions. |
| When does it run? | During a scheduled 30-minute training session. |
| What ends it? | The time limit, an unexpected real-system interaction, or a participant's safety concern. |
| Who receives the result? | The service owner receives a short note with evidence and limitations. |

The brief is specific enough for a beginner to follow. It also prevents the exercise from expanding into an unapproved account or network test. A phrase such as “test the library” is not an adequate scope because it does not identify systems, actions, people, or time.

### 2.3 Decide what information is necessary

Good evidence does not require copying everything available. The exercise needs a booking time, a room identifier, a printout time, and a decision made by staff. It does not need a resident's name, contact details, or account credentials. Replace names with invented labels such as `Resident A` and use artificial booking IDs. This both reduces possible harm and makes the exercise reproducible for other learners.

For a real incident report, preserve required evidence under the organization's approved process; do not independently delete or transform records you have a duty to retain. For a classroom exercise, start with synthetic inputs so the privacy question is simple. The learner should be able to explain why each field in the exercise is present. If a field does not support an objective, remove it.

The following sample has enough information for a schedule comparison:

```csv
booking_id,room,start_time,created_time,status
SYN-001,Room 2,14:00,08:20,confirmed
SYN-002,Room 2,15:00,10:05,confirmed
```

`SYN-` identifies invented records. The sample contains no real identity data. A reader can ask whether a 09:00 printout would include both records without accessing a booking system. It would include only the first if the printout is a snapshot at 09:00; that is an exercise assumption to state explicitly.

### 2.4 Define stop conditions before the exercise

A **stop condition** is an observable reason to pause work and ask for direction. It should be written before an activity begins, when everyone can think clearly. Examples for this paper exercise are: a participant opens a real booking page to “check” the scenario; a sheet contains a real patron name; the exercise begins to interfere with front-desk service; or a result suggests an actual urgent problem that needs the organization's response process. In each case, pause the training, protect the material already collected, and ask the designated owner what to do next.

Stopping is not failure. It is evidence that the team respected its boundary. A good report can state, “The exercise stopped after the team noticed a real patron name in the sample sheet. The sheet was not circulated; the owner replaced it with synthetic data.” That sentence documents both the problem and the safe action without publishing the name.

### 2.5 Report a finding with calibrated language

The goal of an exercise report is to help the owner decide what to check or change. A compact structure is:

1. **Objective and scope:** what was the exercise intended to test, and what was excluded?
2. **Method:** which synthetic inputs and steps were used?
3. **Observation:** what did participants actually see or do?
4. **Interpretation:** what risk or control gap may follow, and what alternative explanation remains?
5. **Recommendation:** what can the owner verify or improve next?
6. **Limitations:** what did the exercise not establish?

For the invented library test, a fair statement is: “In one paper exercise, staff using a 09:00 snapshot did not see a synthetic reservation created at 10:05. The exercise suggests that a static printout is insufficient as the sole source for later bookings during an outage. The exercise did not test the real booking service or establish how a real front desk currently operates.” The sentence is useful because the observation and its limit are both visible.

Avoid dramatic labels such as “critical breach” when no breach has been observed. Avoid a vague recommendation such as “improve security.” Propose a decision the owner can evaluate: define a fallback source for later bookings, mark the printout time, and rehearse the procedure with a later synthetic reservation.

### 2.6 Lab: a bounded tabletop

This lab needs only a text editor or paper. Use the two synthetic CSV rows above and draw a 09:00 printout containing `SYN-001` only. One learner plays the front-desk worker, one the resident asking about Room 2 at 15:00, and one the observer. If working alone, write three short lines for each role. The observer asks whether the worker knows the printout time, notices the missing later booking, and avoids promising a room without a current source.

Run two rounds. In round one, give the worker no fallback instruction and record what happens. In round two, give the worker this rule: “When the booking page is unavailable, mark the age of the printout and place unverified later requests in a pending queue until an approved source or the service owner confirms them.” Record whether the rule changed the decision. Do not infer that the rule will work in every setting. The result demonstrates only how this small scenario behaved under the stated assumptions.

An acceptable lab record has the date of the fictional exercise, role labels, the two synthetic booking IDs, the decision in each round, and a limitation statement. There is no need to create a live account, send a message, or access an external system.

### Chapter 2 summary

An authorized boundary makes a security exercise useful and safe. State the owner, permitted data and actions, excluded systems, timing, stop conditions, and reporting route before starting. Use synthetic records when they can answer the learning question. Report exactly what was observed and what remains unknown. Chapter 3 will add a more complete model of systems, data flows, and dependencies within that boundary.

### Chapter 2 exercises

Keep every activity within the synthetic paper-exercise boundary. Worked results appear at the end of this book.

### EX006 — Write the scope

- **Objective:** Turn a vague activity into an authorized exercise boundary.
- **Input:** The Harbor Library tabletop in Section 2.6.
- **Safe condition:** Use only paper or a text editor and invented records.
- **Task:** Write a six-line brief naming owner, in-scope materials, excluded systems, permitted actions, time window, and recipient of results.
- **Expected evidence:** A brief another learner could follow without guessing the boundary.
- **Rubric:** Credit for all six elements and a clear exclusion of production systems and real residents.

### EX007 — Minimize the data

- **Objective:** Select only information needed to test a learning outcome.
- **Input:** A fictional draft sheet with booking ID, room, start time, created time, resident name, personal phone number, and status.
- **Safe condition:** Do not use or invent realistic personal contact details.
- **Task:** Choose fields for the stale-printout exercise, explain each choice, and remove unnecessary fields.
- **Expected evidence:** A revised synthetic field list and one sentence per retained field.
- **Rubric:** Credit for retaining timing and room evidence while excluding name and phone number.

### EX008 — Stop or continue

- **Objective:** Apply a prewritten stop condition.
- **Input:** Halfway through the paper exercise, a participant proposes opening the real library site to check an answer.
- **Safe condition:** Do not open or test any real service.
- **Task:** State whether to continue, what to record, who decides the next step, and how to finish the learning objective safely.
- **Expected evidence:** A four-part response with an offline alternative.
- **Rubric:** Credit for pausing the proposed live action, notifying the owner, preserving the exercise boundary, and continuing with synthetic data if approved.

### EX009 — Calibrate the report

- **Objective:** Distinguish an observation from an exaggerated claim.
- **Input:** “The old printout did not show `SYN-002`; therefore the real library has a critical security breach.”
- **Safe condition:** Use the supplied fictional case only.
- **Task:** Rewrite the sentence as an observation, interpretation, limitation, and next check.
- **Expected evidence:** Four labeled sentences.
- **Rubric:** Credit for retaining the observed printout gap, removing the unsupported breach claim, and proposing an owner-approved check.

### EX010 — Compare two tabletop rounds

- **Objective:** Assess whether a procedure changes a decision in a controlled exercise.
- **Input:** The two rounds in Section 2.6, including the pending-queue rule in round two.
- **Safe condition:** Role-play without real service data or communication.
- **Task:** Define one observable decision in each round, one criterion for improvement, and two limits on generalizing the result.
- **Expected evidence:** A short comparison table and limitations.
- **Rubric:** Credit for an observable measure, a plausible decision difference, and limits about synthetic data and one-session scope.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 20

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Cybersecurity: systems, data and dependencies

### Learning outcomes

After this chapter, you should be able to:

1. Set a useful boundary for a small service model and name its people, processes, stores, and outside services.
2. Trace one kind of information from creation to use, copying, and disposal without assuming that every copy is current.
3. Distinguish a data flow from a dependency and mark where a change of authority or trust deserves a question.
4. State which parts of a diagram are supplied facts, exercise assumptions, or unanswered questions.
5. Produce a small model and evidence-gap list from synthetic records only.

### 3.1 A model answers a question; it is not the service

The first chapter named Harbor Library's room-booking service. The second limited our practice to invented records. We can now ask a more precise question: **Could a front-desk worker make a correct room decision while the live booking view is unavailable?** A useful model contains the parts needed to answer that question. It need not depict every device the library owns.

A **service boundary** says what the model covers. For this lesson it includes a resident's booking request, the booking view, a reservation store, a staff view, and the staff's fallback printout. The event-announcement list is a separate data set; it belongs in a broader library inventory but is outside the booking-decision path we will trace. That exclusion is deliberate, not a claim that the contact list has no security needs.

NIST's [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29) places inventories of hardware, software and services, representations of authorized network flows, supplier services, asset prioritization, and designated data types in its Asset Management category (`ID.AM`). The framework describes outcomes; it does not prescribe this course's diagram or prove that Harbor Library has any particular implementation. An organization would confirm the model with owners and approved records. Our beginner exercise uses stated assumptions so that the reasoning can be checked without live discovery.

The [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) recommends showing external entities, processes, data stores, flows, and trust boundaries when modeling a system. We borrow these simple labels to understand the service. Threat ranking and application testing belong later in the learning path. For now, the job is to understand what information moves, who depends on it, and where our knowledge ends.

### 3.2 Name the parts and their owners

An **external entity** is a person or system outside the modeled process that interacts with it. A **process** accepts information and performs a task. A **data store** retains information. A **data flow** is movement between them. These labels describe roles in a model, not verified product architecture. One real application could combine several roles; one role could be spread across several services.

| Modeled part | Role in the lesson | Who would confirm it in a real review? | Current evidence |
|---|---|---|---|
| Resident | Requests a room and receives a decision | Service owner and user-facing process owner | Fictional case description |
| Booking view | Receives a request and shows booking information | Application owner | Teaching assumption; no software examined |
| Reservation store | Holds the current booking state for the exercise | Application or data owner | Synthetic booking rows only |
| Staff view | Lets authorized staff consult the schedule | Service owner and staff lead | Teaching assumption |
| Printed schedule | Snapshot used during the tabletop outage | Front-desk lead | Invented 09:00 printout in Chapter 2 |
| Event contacts | Separate information used for announcements | Data owner | Fictional service description; outside this flow |

The “owner” column is a route for verification, not an assertion that one named person holds every responsibility. If the staff view actually reads from a different store, the model must change. If the paper printout is produced every hour rather than once each morning, its freshness risk also changes. A diagram should be revised when evidence disagrees with it.

### 3.3 Follow the information, including copies

Start with the data needed for the decision. In our synthetic exercise, a reservation has an invented ID, room, start time, creation time, and status. A confirmed booking is represented in the reservation store. A staff view may display that state. A printout contains a **snapshot** made at a particular time; it does not automatically receive later changes. This is a temporal property of the paper copy, not a software vulnerability.

Trace each representation explicitly:

| Representation | Why it exists | When it is current for this exercise | Question before relying on it |
|---|---|---|---|
| Synthetic booking row | Describes a reservation for the lesson | At its stated `created_time` | Is its status confirmed or only requested? |
| Staff schedule view | Would support a live room decision | Unknown while the exercise says the view is unavailable | What source feeds it, and when was that source updated? |
| 09:00 printed schedule | Provides an offline reference | Contains bookings known at 09:00 under our stated snapshot assumption | Were later bookings added, changed, or canceled? |
| Pending request queue | Records an unverified decision during the exercise | As current as the worker's entries, but **not** authoritative booking confirmation | Who reconciles it after the service returns? |

The event-contact list has a different purpose from the reservation list. Do not assume that a person who may view a room booking may also export event contacts. Likewise, a backup is a potential recovery resource, not automatically a current booking view. For a real inventory, an owner should identify data types, locations, purpose, access, retention and disposal rules according to the organization's policies. In this exercise, we record only the fields needed for the teaching question and invent no personal identifiers.

The distinction between **source of truth** and **copy** helps prevent an easy mistake. A current authoritative record is the one the service owner designates for a particular decision, subject to its actual integrity and availability. A printed copy may still be useful during an outage, but its timestamp limits what it can establish. “The printout exists” does not imply “the printout reflects all reservations.” “A backup job completed” does not imply “staff can safely use the backup as a live schedule.” Each claim needs separate evidence.

### 3.4 Draw a flow and mark the boundaries

The following is a **text alternative** to a diagram. It is intentionally small. Arrows indicate proposed movement of information, and brackets name roles. They do not claim that a real Harbor Library application has this architecture.

```text
[Resident] --booking request--> [Booking view] --proposed write--> [Reservation store]
     ^                              |                               |
     |                         booking result                   proposed read
     +------------------------------+                               |
                                                                    v
[Staff member] --sign-in and query--> [Staff view] <---------------+
                                         |
                                    09:00 snapshot
                                         v
                                [Printed schedule]
```

The first arrow crosses a boundary between a resident and a service that decides whether a request is valid. The staff sign-in and query cross a different boundary because a worker may have authority to see or change information that a resident cannot. The printed schedule leaves a digital process and becomes a physical copy; its handling and freshness need human procedures. A **trust boundary** marks a change in assumptions or authority that should be examined. It is not, by itself, evidence that authentication, authorization, encryption, or logging is present or absent.

For each arrow, ask three beginner questions: **What moves? Who is allowed to cause or read that movement? What evidence would show that the intended rule is followed?** For the resident request, the answers might be “room and time,” “a resident may request an available room,” and “an owner-approved test with synthetic bookings plus a reviewed application specification.” Those are possible checks, not facts established by our paper exercise. Do not use this diagram as permission to send test requests to a public site.

If a third-party messaging service sends confirmations, add it as an outside service only after confirming that it is actually used. Then ask what data it receives, what the supplier is responsible for, and whether the service can still make a booking decision if messaging is delayed. This is an example of a **conditional dependency**: the answer may differ between “a reservation can be saved” and “a resident receives confirmation.” Keeping those outcomes separate avoids treating every supplier outage as a complete booking outage.

### 3.5 Dependencies change with the outcome

A dependency is needed for a particular outcome under particular conditions. In the proposed live path, the booking view may depend on a reservation store. During the tabletop outage, staff may instead depend on the latest approved fallback source and a rule for pending requests. A component can be important without being the only way to keep working. Do not call the reservation store a “single point of failure” unless the owner has confirmed there is no suitable alternative and has defined what failure means.

To review a dependency, write a conditional sentence: “If **X** is unavailable, **Y** cannot be completed within **Z** time using the approved fallback.” The fictional case does not provide a recovery target `Z`, so leave it as a question for the service owner. Separate effects on residents, staff, and event subscribers. An outage of the front-desk view does not prove that a resident's page is down; Chapter 1's record specifically limited the observed outage to the front desk.

The service model also needs an update rule. A change to the booking workflow, printing schedule, or approved source can invalidate this page. A small inventory entry should therefore record the model's date, author or responsible owner, scope, evidence, open questions, and the trigger for revision. A tidy diagram with no review date can mislead a reader more than a rough diagram with clear uncertainty labels.

### 3.6 Guided lab: a decision from a stale snapshot

Use the **synthetic** rows introduced in Chapter 2:

```csv
booking_id,room,start_time,created_time,status
SYN-001,Room 2,14:00,08:20,confirmed
SYN-002,Room 2,15:00,10:05,confirmed
```

For this lab only, assume a 09:00 printout is a fixed snapshot, includes `SYN-001`, and cannot include `SYN-002` because that booking was created at 10:05. The front-desk view is unavailable from 11:30 to 11:50. At 11:42 someone asks whether Room 2 is free at 15:00. No network or real data is used.

1. Copy the six modeled parts from Section 3.2 onto paper or into a Markdown table. Circle the printed schedule as a copy.
2. Trace `SYN-002` from its 10:05 creation to the reservation store in the *hypothetical* model. Draw a question mark at any unverified step, including whether the staff view would normally show it.
3. Compare the query time, printout time, and booking time. The printout cannot answer the 15:00 availability question under the stated snapshot assumption. Do not turn that conclusion into a claim about a real service.
4. Use the Chapter 2 fallback rule: mark the request **pending**, record the reason, and seek an approved current source or the owner. Do not promise the room from the old paper alone.
5. Write a three-line report: observed exercise fact, decision, and limitation. A model answer is: “The 09:00 synthetic printout omitted a booking created at 10:05. In the tabletop, the worker marked the 15:00 request pending rather than confirming it. The exercise did not inspect a real reservation store or establish how the real library handles outages.”

The expected artifact is a small model plus this report. The outcome is not “we discovered a breach.” The outcome is a defensible decision given limited information. If the owner later supplies a verified hourly paper schedule or an approved offline replica, repeat the analysis with that evidence; do not preserve the original conclusion merely because it appeared in a diagram.

### 3.7 A reviewable model record

Use this Markdown template for a service model. It is intentionally short enough that another learner can challenge it:

```text
Decision being supported:
Service and people affected:
In scope / out of scope:
Entities, processes, and stores:
Data types and their purposes:
Flows and boundaries:
Dependencies and fallback assumptions:
Supplied facts:
Exercise assumptions:
Open questions and owner to ask:
Last reviewed / update trigger:
```

For Harbor Library, “booking created at 10:05” is a supplied synthetic fact; “the printed schedule is a fixed 09:00 snapshot” is an exercise assumption; “what source staff may use during a real outage” is an open question. These categories should remain visible in the final artifact. A learner who writes “the system has no recovery” because this chapter did not mention one has confused **missing evidence** with **evidence of absence**.

Common errors include drawing a detailed architecture from a short narrative, treating every line as a verified network connection, omitting physical copies, confusing a dependency with a failure, and leaving a model unchanged after new information arrives. The remedy is modest: keep the model tied to one decision, label uncertainty, ask its owner, and revise the record when a fact changes. Chapter 4 will use this bounded model to discuss plausible threats and ordinary failure modes without asserting that any one of them occurred.

### Chapter 3 summary

Model the people, processes, stores, and information needed for a defined service decision. Treat data copies and their timestamps explicitly. A flow shows proposed movement; a trust boundary prompts a question about authority; a dependency matters only in relation to a stated outcome. Mark supplied facts, assumptions, and unanswered questions so that the model remains useful when evidence changes.

### Chapter 3 exercises

Use the model and invented records above; do not test a live service. Worked results appear in the final appendix.

### EX011 — Boundary and components

- **Objective:** Define a service model that answers a specific question without inventing implementation details.
- **Input:** The decision question in Section 3.1 and the six modeled parts in Section 3.2.
- **Safe condition:** Use the fictional case only; do not inspect a real library service.
- **Steps:** (1) Write the decision question. (2) Name four parts needed to answer it and classify each as entity, process, store, or copy. (3) Name one related data set that is outside this decision path and explain why. (4) Mark one unverified architectural assumption.
- **Expected evidence:** A scope statement and a four-row component table with one open question.
- **Rubric:** Full credit requires a bounded booking-decision question, appropriate roles, a reasoned exclusion of event contacts, and a visible uncertainty label. A highly detailed but unsupported network diagram does not meet the objective.

### EX012 — Trace the snapshot

- **Objective:** Distinguish the time of a data copy from the time of a later change.
- **Input:** The two CSV rows in Section 3.6, a fixed 09:00 printout, and the 11:42 room question.
- **Safe condition:** Work only with these invented times and IDs.
- **Steps:** (1) Put the four relevant times in order. (2) List which booking IDs the printout can include under the snapshot assumption. (3) State what the printout cannot establish at 11:42. (4) Record the worker's defensible next action.
- **Expected evidence:** A short timeline and a decision note with its assumption.
- **Rubric:** Full credit requires `SYN-001` in the printout, `SYN-002` absent, an explicit snapshot assumption, and a pending or owner-confirmed decision rather than an unsupported promise.

### EX013 — Flow versus dependency

- **Objective:** Tell information movement apart from a condition required for an outcome.
- **Input:** The text diagram in Section 3.4 and the two outcomes “save a reservation” and “send a confirmation.”
- **Safe condition:** Treat the optional messaging supplier as hypothetical; do not contact a vendor or send messages.
- **Steps:** (1) Name two flows shown in the diagram. (2) Write one conditional dependency for each outcome. (3) Explain whether a messaging delay necessarily proves that the reservation was not saved. (4) Name the fact an owner must confirm.
- **Expected evidence:** Two labeled flows, two conditional statements, and one verification question.
- **Rubric:** Full credit requires distinguishing a proposed data path from a required service condition and withholding a claim about the unconfirmed supplier or implementation.

### EX014 — Boundary questions

- **Objective:** Use a trust boundary as a prompt for verification rather than as proof of a control.
- **Input:** The resident-to-booking-view and staff-to-staff-view arrows in Section 3.4.
- **Safe condition:** This is a paper review; do not test accounts or send requests to a live service.
- **Steps:** For each arrow, write (1) what information or action crosses it, (2) who ought to be permitted to initiate it in the fictional scenario, (3) one control question for the owner, and (4) one kind of authorized evidence that could answer that question.
- **Expected evidence:** A two-row table separating expected permission from observed proof.
- **Rubric:** Full credit requires distinct resident and staff authority, specific owner questions, and a statement that the diagram alone does not verify any implementation.

### EX015 — Revise when a fact changes

- **Objective:** Update a model without clinging to an earlier conclusion.
- **Input:** A *new fictional owner report* says the front desk receives an approved offline schedule refreshed at 11:40 and containing `SYN-002`. Its accuracy has not yet been tested.
- **Safe condition:** Do not seek or copy real bookings; reason from this additional invented report.
- **Steps:** (1) Identify which earlier conclusion is weakened. (2) Add the reported offline schedule as a separate representation. (3) Specify a safe synthetic check of its timestamp and content. (4) State the decision if the check succeeds and if it fails, and note one remaining limitation.
- **Expected evidence:** A revised model note with report, test, branch decisions, and limitation.
- **Rubric:** Full credit requires treating the new information as a report, not as independently observed fact; changing the stale-09:00-only conclusion conditionally; and keeping the worker's decision within the approved fallback rule.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 20

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Cybersecurity: guided lab and applied synthesis

### Learning outcomes

After this chapter, you should be able to:

1. Apply a written rule to a synthetic staff action and name the verdict the rule produces.
2. Separate a classification of a recorded proposal from a decision that the real service is safe.
3. Explain why ALLOW, REFUSE, OUT OF SCOPE and STOP answer different questions.
4. State one fact the offline script cannot know.
5. Write a short dossier that keeps the observation, the decision and the limit in separate sentences.

### 4.1 Five labels, four logged actions

Chapters 1–3 left a front-desk worker with a 09:00 paper schedule, two invented bookings, and a rule: do not confirm a later room from that paper, do not open a live site, and do not pull the event-contact list into the booking exercise. Chapter 4 turns that rule into a check a second person can rerun.

The check has five possible labels. Four occur in the four-action log; `UNKNOWN` has a zero count. These are labels for this exercise, not a severity scale.

| Verdict | Question it answers | What it does not answer |
|---|---|---|
| STOP | Did this action leave the paper exercise? | Whether a real site is under attack |
| OUT OF SCOPE | Is this data set outside the booking decision? | Whether the contact list is well protected |
| REFUSE | Does the 09:00 snapshot omit a later booking for that room and start? | Why the booking page was unavailable |
| ALLOW | Does the written rule permit this recorded action? | Whether Room 2 is actually free |
| UNKNOWN | Is the action missing from the rule set? | What the owner would decide after being asked |

A number such as 7.4 would hide which of these questions changed. This chapter does not score the library.

### 4.2 The script reads the exercise assumption

The lab below is standard-library Python. It encodes three assumptions already fixed in this book: the printout time is 09:00, `SYN-002` was created at 10:05 for Room 2 at 15:00, and event contacts are outside the booking path. It does not read the Chapter 3 owner *report* of an 11:40 offline sheet. That report is still unverified, so the script must not treat it as a newer printout.

`REFUSE` fires only when a confirm-from-printout action names a room and start whose booking was created after 09:00. `ALLOW` on mark-pending means the rule accepts a pending queue. `ALLOW` on a confirmation means only that no later booking in this tiny table matches that room and start. A different room can therefore print ALLOW while remaining unknown in the real building.

### 4.3 Worked example: four actions

Use the same rows the script uses.

| Time | Action | Why the rule speaks | Verdict |
|---|---|---|---|
| 11:42 | Confirm Room 2 at 15:00 from the paper | `SYN-002` was created at 10:05, after the printout | REFUSE |
| 11:43 | Export event contacts | Announcement contacts are not the booking decision | OUT OF SCOPE |
| 11:44 | Open the live booking site | The brief forbids production systems | STOP |
| 11:45 | Mark the 15:00 request pending | The fallback rule allows a pending queue | ALLOW |

The 11:44 line classifies a *recorded proposal*. It does not by itself halt a classroom. In a live rehearsal the owner still pauses the people, as Chapter 2 required. The script keeps going so the other three rows stay visible. That difference is a limit of the program, not a softer stop condition.

### 4.4 Lab: classify the synthetic log

Save this program as `lab_dossier.py` and run it with `python3 lab_dossier.py`. Do not point it at a network, a library website, or a file of real patrons. The expected output is fixed for these rows. If your output differs, the rule you ran is not the rule in this chapter.

```python
"""Harbor Library tabletop dossier. Synthetic records only."""

PRINTOUT = "09:00"

BOOKINGS = [
    {"id": "SYN-001", "room": "Room 2", "start": "14:00", "created": "08:20", "status": "confirmed"},
    {"id": "SYN-002", "room": "Room 2", "start": "15:00", "created": "10:05", "status": "confirmed"},
]

ACTIONS = [
    {"time": "11:42", "action": "confirm-from-printout", "room": "Room 2", "start": "15:00"},
    {"time": "11:43", "action": "export-contacts"},
    {"time": "11:44", "action": "open-live-site"},
    {"time": "11:45", "action": "mark-pending", "room": "Room 2", "start": "15:00"},
]


def minutes(clock):
    hour, minute = clock.split(":")
    return int(hour) * 60 + int(minute)


def decide(action):
    kind = action["action"]
    if kind == "open-live-site":
        return "STOP", "live site is outside the paper exercise"
    if kind == "export-contacts":
        return "OUT OF SCOPE", "event contacts are outside the booking decision"
    if kind == "confirm-from-printout":
        later = [
            booking["id"]
            for booking in BOOKINGS
            if booking["room"] == action["room"]
            and booking["start"] == action["start"]
            and minutes(booking["created"]) > minutes(PRINTOUT)
        ]
        if later:
            return "REFUSE", "printout 09:00 omits " + ",".join(later)
        return "ALLOW", "no later booking is recorded for that room and start"
    if kind == "mark-pending":
        return "ALLOW", "pending until an approved current source"
    return "UNKNOWN", "the written rule set does not name this action"


def main():
    print("printout: 09:00; bookings: 2")
    omitted = [booking["id"] for booking in BOOKINGS if minutes(booking["created"]) > minutes(PRINTOUT)]
    print("omitted by printout: " + ",".join(omitted))
    counts = {"STOP": 0, "OUT OF SCOPE": 0, "REFUSE": 0, "ALLOW": 0, "UNKNOWN": 0}
    for action in ACTIONS:
        verdict, reason = decide(action)
        counts[verdict] += 1
        print(f"{action['time']} {action['action']}: {verdict}; {reason}")
    print(
        "STOP {STOP}; OUT OF SCOPE {OUT OF SCOPE}; REFUSE {REFUSE}; ALLOW {ALLOW}; UNKNOWN {UNKNOWN}".format(
            **counts
        )
    )


if __name__ == "__main__":
    main()
```

Exact output, checked with Python 3:

```text
printout: 09:00; bookings: 2
omitted by printout: SYN-002
11:42 confirm-from-printout: REFUSE; printout 09:00 omits SYN-002
11:43 export-contacts: OUT OF SCOPE; event contacts are outside the booking decision
11:44 open-live-site: STOP; live site is outside the paper exercise
11:45 mark-pending: ALLOW; pending until an approved current source
STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0
```

The count line is a tally of these four rows. It is not a risk rating. Changing the 11:42 room to Room 4, which does not appear in `BOOKINGS`, makes that row ALLOW. The new ALLOW means the table has no later booking for Room 4 at 15:00. It does not mean a resident may have the room.

### 4.5 A dossier uses only what the run showed

Write six short sentences and stop. Sentence 1 names the exercise and the 09:00 assumption. Sentence 2 quotes one output line. Sentence 3 states the decision that line supports. Sentence 4 names a verdict that must not be merged with it: exporting contacts is OUT OF SCOPE, not REFUSE, because the contact list was never a booking-time comparison. Sentence 5 says the script did not inspect a reservation store and did not accept the unverified 11:40 report. Sentence 6 names the owner question that is still open: which approved source, if any, may replace the 09:00 paper.

If sentence 5 is blank, the note is not ready to guide a procedure change. A blank limit lets a reader treat a classroom tally as a finding about Harbor Library's real systems, which this book does not have.

### Chapter 4 summary

A written rule can classify a synthetic action the same way twice. STOP, OUT OF SCOPE, REFUSE, ALLOW and UNKNOWN answer different questions. The program's ALLOW is permission under the rows it was given, not evidence that a room is free or that a reported 11:40 sheet exists. The dossier keeps the output, the decision and the limit apart.

### Chapter 4 exercises

Use the program and output in Section 4.4. Do not contact a real library. Worked results are in the appendix.

### EX016 — Read the tally

- **Objective:** Tie one verdict to the row that produced it.
- **Input:** The exact lab output in Section 4.4.
- **Safe condition:** Do not add bookings or open a website.
- **Task:** Name the action that received REFUSE, the booking id the reason cites, and the assumption that makes that id absent from the paper.
- **Expected evidence:** Three items, each taken from the output or the stated 09:00 snapshot.
- **Rubric:** Credit only if the action is the 11:42 confirmation, the id is `SYN-002`, and the assumption is the 09:00 printout rather than an inferred attack.

### EX017 — ALLOW is not availability

- **Objective:** Limit what a matching rule is allowed to mean.
- **Input:** Change only the 11:42 action so the room is Room 4 and the start remains 15:00. Leave every other row as printed.
- **Safe condition:** Edit the synthetic table on paper or in a local copy. Do not query a live system.
- **Task:** State the new verdict for 11:42 and write the sentence a staff member must not say to a resident.
- **Expected evidence:** The verdict plus one prohibited claim.
- **Rubric:** Credit for ALLOW together with a refusal to promise Room 4. An answer that calls the room free fails.

### EX018 — Do not merge the verdicts

- **Objective:** Keep a data-set boundary distinct from a stale-paper comparison.
- **Input:** The 11:43 output line.
- **Safe condition:** Reason from that line only.
- **Task:** Explain why the export is OUT OF SCOPE rather than REFUSE, and name one fact about contact-list protection that this run does not provide.
- **Expected evidence:** A distinction and one explicit unknown.
- **Rubric:** Credit when REFUSE stays attached to the printout comparison and the contact list remains unmeasured.

### EX019 — Script stop versus human stop

- **Objective:** Notice that a classified row is not the same act as pausing people.
- **Input:** The 11:44 STOP line and the Chapter 2 rule that a live-site proposal pauses the exercise.
- **Safe condition:** Do not open a site to illustrate the point.
- **Task:** Say what the program did after printing STOP, what a facilitator should do with the participants, and why those two actions differ.
- **Expected evidence:** Three sentences.
- **Rubric:** Credit if the program continues through 11:45 while the facilitator pauses the people and asks the owner.

### EX020 — Six-sentence dossier

- **Objective:** Report the run without enlarging it.
- **Input:** Section 4.5 and the lab output.
- **Safe condition:** Invent no outage cause, no patron, and no second system.
- **Task:** Write the six sentences. Leave sentence 5 concrete. Do not assign a numeric score.
- **Expected evidence:** Six sentences a classmate can check against the output.
- **Rubric:** Credit when each sentence stays inside the run, the 11:43 line is not redescribed as REFUSE, and the 11:40 report is still unverified.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 20

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — What may be said about a booking

### Learning outcomes

After this chapter, you should be able to:

1. Separate a booking fact the asker needs from a fact about another person.
2. Explain why a true statement can still be the wrong thing to say.
3. Choose a reply that answers the operational question without naming a resident.

### 5.1 Confidentiality is about disclosure, not secrecy of the room

Confidentiality, in the ordinary security sense used in Chapter 1, means that information is not disclosed to someone who should not receive it. The room number on a library door is not confidential. The name of the person who reserved it can be, because the reservation connects a person to a place and a time. Harbor Library's exercise has no privacy statute to apply and no real patrons. The limit still matters: a practice that treats every true fact as sayable will train the wrong habit.

A resident at the desk asks, "Who has Room 2 at 14:00?" The worker can see, in the synthetic table, that `SYN-001` is a confirmed booking for Room 2 at 14:00. The table in this book does not even contain a resident name. Inventing one in order to be helpful would create personal data the exercise removed on purpose in Chapter 2.

### 5.2 Worked example

The operational question hiding inside the spoken question is usually "Can I use Room 2 at 14:00?" That question can be answered from the booking state.

| Asker's words | Fact the worker has | Reply that stays inside the exercise | Reply that leaves it |
|---|---|---|---|
| Who has Room 2 at 14:00? | `SYN-001` confirmed, no name stored | "That slot is already booked. I can't use this sheet to say who." | A made-up name, or a guess from the event list |
| Is Room 2 free at 15:00? | `SYN-002` confirmed after 09:00 | "The current exercise record shows 15:00 as booked. I will not confirm a change from the 09:00 paper." | "It's free" because the paper omitted `SYN-002` |

The second row reuses the stale-paper rule from Chapter 4. The new point is the first row: even a current record does not authorize naming a person who is not in the record.

### 5.3 What this chapter does not decide

It does not decide that every library must hide reservation names, or that a name is always sensitive. A library could have a posted public program that lists a speaker's name because that person agreed to be listed. Harbor Library's booking exercise has no such agreement and no name field. Staff who need a name for a safety reason ask the owner and record why. They do not borrow a name from the announcement contacts, which Chapter 3 left outside the booking path.


### 5.4 Two independent gates: evidence and disclosure authority

A statement can be **true but inappropriate to disclose**, and a statement can be **permitted in principle but unsupported by the available record**. The evidence gate asks whether the claim follows from the available, sufficiently current source. The disclosure gate asks whether this audience, purpose and channel are authorized to receive that category of information. Passing one gate never substitutes for the other. A booking identifier, a slot state and a resident identity are different information categories, even if a later system could connect them.

For the fictional desk interaction, use this sequence:

1. **Identify the question that needs a decision.** A resident asking whether a room can be used needs a slot-state answer. “Who is in that room?” requests a different fact about another person.
2. **Specify the exact claim before speaking.** “Room 2 at 14:00 is booked” does not contain the same assertion as “A named resident booked Room 2.” Do not blend them into an apparently helpful sentence.
3. **List the evidence actually available to the worker.** At 09:00, the fixed synthetic sheet can represent SYN-001, created at 08:20. A front-desk worker facing the stated 11:30–11:50 outage must not pretend to have queried an unavailable live view. The instructor may know more from the full teaching fixture than the role-playing worker knows at the desk.
4. **Apply the scenario's disclosure scope.** The exercise permits a necessary room-state reply. It does not supply identity data, authorization to use event-announcement contacts, consent to identify a resident, or a customer-verification process. In a real library these limits must be confirmed with the responsible owner rather than guessed from a job title.
5. **Use the minimum supported response.** Say the supported slot state without reading out internal booking IDs. If freshness is insufficient, state that the request cannot be confirmed yet and follow the pending procedure rather than pretending the paper is current.
6. **Record and refer exceptions.** Route an identity-specific or staff-only request to the authorized service or data owner. Referral is not evidence that the asker is suspicious, and it is not an approval to release the data.

This is an applied least-disclosure practice, not a universal claim that all room schedules are secret. The [NIST CSF 2.0, PR.AA-05 and PR.DS](https://doi.org/10.6028/NIST.CSWP.29) describe organizational outcomes concerning authorization and data protection. They do **not** prescribe Harbor Library's fictional spoken reply, prove a local law applies, or certify this classroom procedure. Authorization comes from the defined case scope, subject to an owner-approved rule in a real service.

### 5.5 Worked claim ledger: what can the sentence actually prove?

| Proposed sentence | Evidence in the exercise | What the speaker may conclude | Boundary to retain |
|---|---|---|---|
| “Room 2 at 14:00 is booked.” | SYN-001 is confirmed and predates the 09:00 sheet | The recorded 14:00 slot is taken in the stipulated snapshot | Answer with the room state; omit a person's identity |
| “Resident A made the 14:00 booking.” | No person field or verified identifier mapping is provided | Nothing about a particular resident | Do not infer a name from an event list or from SYN-001 |
| “The full synthetic fixture contains a later 15:00 booking.” | SYN-002 is confirmed, created at 10:05 | True of the instructor's supplied fixture | Does not show that the desk worker consulted a live record |
| “The 09:00 printout proves 15:00 is free.” | SYN-002 arose after the fixed printout | Unsupported: the copy is too old to exclude later entries | Do not promise the room; keep the request pending |
| “Nobody has booked anything else.” | Only a bounded room/time example is supplied | Unsupported global absence claim | Do not generalize from one sheet or one missing row |

**Worked interaction A — an identity question.** The resident says, “Who has Room 2 at 14:00?” The worker's reply is: “Room 2 at 14:00 is already booked. This record does not identify the person, so I cannot say who.” The first sentence conveys the operational state the exercise permits. The second prevents a fictional identity being created from an internal row ID. It does not imply the worker has searched every possible system for identity data.

**Worked interaction B — an availability question during the outage.** At 11:42 a resident asks to use Room 2 at 15:00. The stipulated full fixture contains the confirmed 10:05 booking SYN-002, but the desk's 09:00 paper is stale. The worker says: “I cannot confirm availability from this 09:00 paper. I can record your request as pending until an approved current source is checked.” The response is not a vague refusal: it names the source limitation and a next step. It neither promises that the room is free nor pretends the worker has live access.

The two sentences illustrate why **the author's omniscient case narrative is not a participant's authenticated observation**. An analyst studying the full fixture may correctly say that SYN-002 exists in that fixture; the fictional worker may not silently borrow an unavailable source to certify a transaction. The same reasoning prevents misleading statements even when no personal information is involved.

### 5.6 Why correct facts may still be the wrong reply

Consider three different audiences. A visiting resident may need the room state; the example grants no reason to receive another resident's identity. A staff lead may have a legitimate operational need to investigate a booking, but the case does not define an identity-access policy or audit trail for that investigation: refer it to the owner rather than assume managerial title equals blanket access. A hypothetical publicly advertised event may list a consenting speaker, but a published event name does not establish who owns this unrelated synthetic room booking. The announcement-contact data are outside the booking-decision path, as Chapter 3 established.

If a caller says “I booked it myself,” that assertion alone does not authenticate the caller or authorize disclosure. This chapter gives no account-validation procedure. The worker should not demand real identity documents as part of the offline exercise or improvise an identity lookup. If the source is insufficient even for slot state, do not offer false reassurance through softer wording such as “probably available.” Uncertainty is not permission to guess.

Avoid the opposite failure as well: “I cannot say anything” withholds the room-state answer even when the permitted source supports it. A proportionate reply combines **useful operational information**, **restricted disclosure**, and **the current limit of evidence**. The data-minimizing reply is the one that meets the legitimate task with no unnecessary fields, not necessarily the shortest possible sentence.

### 5.7 Independent decision rehearsal

Before reading EX021's worked result, draft two spoken replies: one for the 14:00 identity request, and another for the 15:00 request made during the 11:42 outage. Under each, make a brief three-column ledger: **claim**, **source and cutoff**, **reason for disclosure or withholding**. Test the reply against these negative controls: does it invent a person from SYN-001, reveal an internal ID without purpose, or treat the absence of SYN-002 on an old sheet as proof that 15:00 is unbooked? A sound decision survives all three. State explicitly that these are synthetic records and no real permission scheme or application was tested.

### Chapter 5 summary

A true booking state can be shared when it answers the asker's own question. A person's identity is a different disclosure. This exercise has no names to give, and inventing one is not customer service.

### Chapter 5 exercises

### EX021 — Answer the person in front of you

- **Objective:** Refuse an unnecessary disclosure without hiding the room state.
- **Input:** A resident asks who booked Room 2 at 14:00. The synthetic row is `SYN-001`, confirmed, with no name.
- **Safe condition:** Do not invent a resident and do not open a live site.
- **Task:** Write the reply you would say, and name the fact you deliberately leave out.
- **Expected evidence:** One spoken reply and one withheld item.
- **Rubric:** Credit if the slot is described as booked and no person is named or invented.

- **Independent extension:** For the 14:00 answer, label the source and timestamp, the authorized slot-state claim, and the unsupported identity claim. Contrast the answer with one 15:00 availability sentence at 11:42 using only the stale front-desk paper.
- **Extended assessment:** The 15:00 sentence must not turn a missing row into a free-room decision or pretend that the offline exercise inspected a live system. The original reply plus withheld item remain the core graded artifacts.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 20

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — A handwritten change is not a correction

### Learning outcomes

After this chapter, you should be able to:

1. Tell an authorized refresh of a schedule from a handwritten addition.
2. Explain why making the paper match the desired answer damages the record.
3. State what evidence would be required before a later copy could replace the 09:00 paper.

### 6.1 Integrity is about the record, not the wish

Integrity means the information stays accurate and is changed only in an authorized way. Chapter 3 already warned that a second copy can be stale. This chapter looks at a different failure: a worker who wants to help writes `SYN-002` onto the 09:00 sheet so that a confirmation no longer looks refused. The booking may really exist in the synthetic table. The writing still changes the artifact that was supposed to be the 09:00 snapshot.

After that pen mark, a classmate can no longer see what the paper said at 09:00. The lab in Chapter 4 would also change if someone edited `PRINTOUT` or the booking time so the program printed ALLOW. Both moves adjust the record to the preferred verdict. Neither move is a check.

### 6.2 Worked example

| Action | What is preserved | Verdict for this exercise |
|---|---|---|
| Leave the 09:00 sheet unmarked and mark the 15:00 request pending | The snapshot and the later booking stay distinct | Consistent with Chapter 4 |
| Ask the owner for the reported 11:40 sheet and check its time and the presence of `SYN-002` | The new copy is still only reported until the check passes | The Chapter 3 condition |
| Write `SYN-002` on the 09:00 sheet in pencil | The original snapshot is gone | Not a correction |

The third row is the lesson. Good intent does not restore integrity. If the owner later produces a real 11:40 copy, the penciled sheet cannot serve as that copy, because its time and its author are no longer reliable.

### 6.3 A limit

This chapter does not claim that Harbor Library forbids all handwritten schedules. A designed offline form, with a time, an author and a check, can be an authorized copy. An anonymous pencil mark on yesterday's printout is not that form. The exercise also does not show that anyone at Harbor Library did this. It is a mistake to practice against, using the synthetic sheet only.


### 6.4 Three dimensions of integrity, not one convenient match

A document can be historically accurate yet stale for a current decision. Conversely, a handwritten alteration can happen to match a later database row and still lack authority or provenance. Analyze three questions separately:

- **Historical snapshot:** What did the 09:00 paper actually contain when produced? The synthetic exercise says it contained SYN-001 but could not contain SYN-002, created at 10:05. A later pencil line is not evidence that the line existed at printing time.
- **Current state:** Which reservations exist when a worker needs a decision? The teaching fixture includes SYN-002, but the front-desk view is unavailable in the role-play. The old paper cannot exclude later bookings.
- **Authorized change:** Which approved actor or process issued a replacement, from what source, at what time, with what scope and checks? A volunteer's statement that the sheet “matches the table” does not establish any of those facts.

This is a **provenance** problem: the marked sheet now combines claims from two times of knowledge without a documented boundary. Another reader may mistakenly treat the new handwriting as original 09:00 output. That does not prove sabotage, an attacker, a real outage cause or destruction of all possible historical copies. No independent original photograph or archival copy is supplied; the marked object by itself is no longer an unchanged reference.

The [NIST SP 800-53 Rev. 5, SI-7](https://doi.org/10.6028/NIST.SP.800-53r5) discusses detection of unauthorized modifications to information. The [NIST CSF 2.0 data-security outcomes](https://doi.org/10.6028/NIST.CSWP.29) concern information protection according to organizational risk. Those primary references help explain *why* integrity and authorized modification matter; they do not establish a Harbor Library requirement to use cryptographic hashes, prove a control was implemented, or turn a fictional pencil into an observed incident.

### 6.5 Three artifacts that must not be merged

| Artifact | Status and time basis | Legitimate use in this exercise | What it cannot establish |
|---|---|---|---|
| A: original 09:00 snapshot | Fixed paper record in the supplied case | Explain what the printout knew at 09:00 | Whether a later booking exists |
| B: a separate pending request line | Written for the 11:42 request with Room 2, 15:00, “not confirmed” | Carry an unconfirmed request until review | That a new reservation was accepted |
| C: the proposed 11:40 offline schedule | An owner **reported** a later authorized copy in Chapter 3; it has not yet been checked here | Candidate replacement after owner and content verification | That a verified replacement is already available |

Writing SYN-002 on A neither creates C nor converts B into a booking. Relabeling the old sheet “11:40” is equally misleading because it replaces a source claim instead of obtaining that source. A real organization may have a controlled manual-correction form with a writer, time, reason, independent approval and version history. This course does **not** establish that Harbor Library has one. The correct question is what the owner-approved process requires, not whether any handwriting must always be forbidden.

**Worked reconstruction.** The original paper contains SYN-001. Later, the supplied synthetic table contains SYN-002. During the 11:30–11:50 outage, the volunteer pencils a SYN-002 line onto the 09:00 sheet and says it is now up to date. This may reproduce one correct value from the teaching fixture, but it destroys the marked paper's reliability **as an unaltered 09:00 snapshot**. No approved issuance time, completeness check, source record, or reviewer was added by the pencil. The fact that a later entry exists does not authorize rewriting what an earlier artifact said.

Instead, preserve and label the changed exercise sheet as altered; do not silently erase or disguise the pencil, and do not invent a pristine copy. Record the 15:00 request separately as pending and obtain a new source only through the owner's procedure. This protects the history while permitting service continuity without a fabricated authorization.

### 6.6 A conditional gate for the reported 11:40 copy

Chapter 3 introduced an owner's **report** that a new 11:40 schedule may exist. Before replacing the decision basis, make the following checks explicit:

1. **Authority:** Has the responsible owner identified the offline schedule as an approved source for front-desk decisions? A volunteer's assurance or a penciled timestamp is not enough.
2. **Provenance:** Is this a separate 11:40 copy from the stated issuer, rather than the altered 09:00 sheet? Preserve the older artifact and the claimed origin separately.
3. **Relevant row:** Does the purported later schedule contain SYN-002, Room 2, 15:00, with an interpretable status? A matching ID alone cannot establish everything about availability.
4. **Currency and completeness:** Does its generation and update method support the 10:05 change and the requested decision time? The printed number 11:40 is a claim to check, not independent proof of a complete feed.
5. **Permitted decision:** If the owner accepts the source, what may the worker do with the verified occupied slot? Recognizing an existing booking is not authorization to give it away, identify its holder or alter it.
6. **Failure branch:** If the source, its authority or the relevant state remains uncertain, keep the request pending and escalate. Do not change the test fixture merely to obtain an ALLOW verdict.

**Conditional worked outcomes (not received case evidence).** In branch A, the owner approves the use of a separate 11:40 sheet and a bounded rehearsal confirms it includes SYN-002 as booked. The worker can avoid confirming that occupied slot for somebody else. In branch B, the source cannot be verified, or the relevant row is uncertain. The worker keeps the request pending. Neither hypothetical branch should be described as an actual check performed at Harbor Library.

### 6.7 A valid test does not edit its baseline to pass

The Chapter 4 offline script evaluates a rule using the stipulated PRINTOUT and synthetic bookings. It is a bounded classifier, **not a booking engine** and not proof of who is permitted to change a reservation. If the learner changes PRINTOUT to a later time, deletes SYN-002 or changes the action to obtain ALLOW, the learner is evaluating a **different input**; the original REFUSE decision was not disproved.

An honest negative control preserves the initial fixture, labels a **separate hypothetical variant**, changes exactly one assumption, predicts the new classification and explains which claim that output supports. For example, one might compare the fixed 09:00 paper with a separately verified current source in an imagined follow-up. The new branch may yield a different outcome, but it cannot retroactively turn an unapproved pencil line into an authorized source. Likewise, a program output does not certify a room as free or authorize a real booking.

### 6.8 Worked handoff: observation, inference, decision and open evidence

A defensible classroom note would read:

> “At the 11:42 simulated checkpoint, the supplied 09:00 schedule did not contain SYN-002. A volunteer's penciled SYN-002 line changed that paper after printing, so we label the sheet altered and cannot treat it alone as an unchanged 09:00 snapshot. The proposed 11:40 replacement has not been checked. The Room 2 / 15:00 request remains not confirmed pending an owner-approved current source.”

The **observation** is the mark; the **inference** is the resulting loss of pristine-snapshot provenance; the **decision** is to withhold confirmation; and the **next evidence** is an appropriately verified replacement. This note does not allege intent, identify a patron, invent an owner approval or convert an unseen later record into a fact. The success criterion is a traceable decision history, not a tidier-looking piece of paper.

### Chapter 6 summary

Changing a snapshot so that a rule would have allowed the action destroys the evidence the rule needed. Pending, or a checked later copy, keeps the history. A pencil mark does not.

### Chapter 6 exercises

### EX022 — Spot the alteration

- **Objective:** Reject an edit that manufactures agreement.
- **Input:** The 09:00 sheet lists only `SYN-001`. During the outage a volunteer pencils in `SYN-002`, Room 2, 15:00, and says, "Now the paper matches the table, so we can confirm."
- **Safe condition:** Do not confirm a room and do not alter your own copy into the answer you prefer.
- **Task:** Say what the pencil mark did to the 09:00 record, whether confirmation is now allowed, and what you would keep instead.
- **Expected evidence:** Three judgments.
- **Rubric:** Credit only if the mark is called an alteration, confirmation stays refused on that sheet, and the alternative is a pending request or an owner-checked later copy.

- **Independent extension:** Make a three-row provenance note comparing the 09:00 original, the penciled alteration, and the **reported but unverified** 11:40 replacement. Identify what each can establish and which owner check is missing.
- **Extended assessment:** Credit requires historical-vs-current state separation, a pending request rather than confirmation, and a conditional verification step for any replacement. The alteration cannot be redescribed as a validated 11:40 printout.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 20

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — A pending queue during an outage

### Learning outcomes

After this chapter, you should be able to:

1. Separate "the booking page is down" from "no decision procedure exists."
2. Use a pending queue as a continuity method without pretending the room was confirmed.
3. Apply the same method to a second outage without inventing a new cause.

### 7.1 Availability of what

Chapter 1 named availability as the property that information and the service are there when needed. At 11:30 the booking view is not there. The front desk can still be there. Those are different assets. Calling the whole library "unavailable" would erase the procedure that is still usable: write the request, mark it pending, and wait for an approved current source.

A pending entry needs four fields and nothing personal: time the request was heard, room, requested start, and the words "not confirmed." Adding a resident name would repeat the Chapter 5 mistake. Adding "probably fine" would be a confirmation wearing softer clothes.

### 7.2 Worked example: the next morning

The next morning the view fails again from 09:10 to 09:25. A visitor asks to take Room 2 at 15:00 that day. Nothing in this book says the two outages have the same cause. The worker does not need the cause. The current approved source is still missing, and the 09:00 paper from the earlier exercise is a different day's snapshot, so it cannot confirm today's 15:00.

| Field | Entry |
|---|---|
| Heard | 09:12 |
| Room | Room 2 |
| Start | 15:00 |
| State | not confirmed |

When the view returns, the worker compares the pending line with the current record before anyone tells the visitor the room is theirs. If the current record already has a booking, the visitor is told the slot is booked, still without a name. If it is free, a new booking still requires whatever approval the owner defined. This lesson does not invent that approval step.

### 7.3 Limit

One calm pending slip does not measure how long the library can operate this way, how many requests arrive, or whether the view will return. It also does not explain the outage. Availability work at this level is the safe next action during the gap, not a capacity study.


### 7.4 Define exactly what "pending" commits to

A **booking** and a **request to consider a booking** are separate records of intent. The pending slip in this lesson is a local continuity aid: it records that someone *asked*, not that the library *accepted*. The distinction matters even when the person at the desk is polite and optimistic. Saying "I have written it down" is defensible; saying "You have Room 2" asserts an allocation that the worker has not checked or been authorized to create. An old paper schedule cannot turn one into the other.

In this classroom, use a deliberately small state vocabulary:

| State label | Evidence needed | What the worker can say | What cannot be inferred |
|---|---|---|---|
| **Not confirmed / pending** | A request was heard and written with its time, room and requested start | "I have recorded your request, but the room is not confirmed." | No reservation has been approved merely because the request exists |
| **Current source checked, outcome unknown** | A proposed check is scheduled or started, but no reliable result has been supplied | "We still need the result of an approved current check." | Do not convert an action plan into a completed observation |
| **Slot shown occupied** (conditional teaching branch) | An authorized, sufficiently current source is checked and records a conflicting booking | "That slot is already booked." | Neither the prior request nor the check reveals who booked it |
| **Slot appears available** (conditional teaching branch) | An authorized, sufficiently current source has no relevant conflict within its verified scope | "The checked record has no conflict for that slot." | No new reservation exists until the owner-approved creation/confirmation procedure succeeds |
| **Confirmed** (not reached in this chapter) | Both the source/eligibility checks and the service owner's required booking decision and confirmation evidence | Only then could a worker communicate a confirmed allocation under the approved rule | Neither the exercise nor a paper slip supplies such a receipt |

"Current source checked" and "confirmed" are not synonymous. The hypothetical no-conflict row is deliberately weaker than a booking: availability is one possible **precondition** for confirmation, never proof of the confirmation step. This chapter does not invent an authorized booking button, ownership matrix or reservation receipt. In a real procedure those must be verified with the service owner.

This is an example of a **fail-safe decision default**: when required evidence is absent, retain the noncommittal state rather than claiming success. A pending queue maintains a useful front-desk function without misrepresenting the unavailable booking view. The [NIST Cybersecurity Framework 2.0](https://doi.org/10.6028/NIST.CSWP.29) separates protection, response, recovery and other risk-management outcomes; it does not prescribe this fictional queue or authorize Harbor Library staff to make reservations. The design is a teaching procedure with a clearly limited decision right.

### 7.5 Four clocks must not become one event

The two fictional outages occur on different days. In the first, the provided 09:00 fixed sheet precedes a 10:05 booking and an 11:42 request during an 11:30–11:50 interruption. **The next morning**, a new outage is described from 09:10 to 09:25; a visitor asks at 09:12 for a 15:00 slot *that day*. The 09:00 paper in the drawer is from **the earlier day**. A familiar time-of-day printed on a different day's artifact is not a fresh source.

| Time reference | What the teaching case supplies | Proper interpretation |
|---|---|---|
| Previous day's 09:00 | Fixed paper snapshot in the drawer | Historical context from the earlier day; it does not certify today's schedule |
| Next morning 09:10–09:25 | Described window in which the front-desk view fails again | Availability boundary for the fictional view, **not** evidence of a shared cause |
| Next morning 09:12 | Visitor's question is heard and the pending entry is made | The request's recorded **intake time**, not a reservation creation time |
| Next morning 15:00 | Room/start requested by the visitor | A **future requested slot**, not an observation or approval made at 15:00 |
| After the view returns | A current-source review **should** occur before any new promise | No read result, confirmed booking or completed reconciliation receipt has been supplied |

A useful log keeps **when the request was heard**, **what source was available as of what date and time**, **when a decision was taken**, and **what evidence later justified a changed status** in separate fields when those facts exist. The compact four-field slip records only the intake essentials; the later reconciliation record, *if made under an approved procedure*, would carry the check's source, scope and time. Do not backfill a successful check into the 09:12 note. Do not infer the current booking's creation time from its requested 15:00 start.

One can calculate that the described second outage window spans 15 minutes. That arithmetic is **not** a measured recovery objective, uptime guarantee, full-service disruption time, cause analysis or evidence that the booking state was immediately synchronized at 09:25. The chapter supplies neither a recovery-time target nor a measurement system. The uncertainty to resolve is source authority and freshness at the moment of an actual booking decision.

### 7.6 Worked reconciliation with competing possible outcomes

**Phase A — during the outage.** At 09:12, in the second day's fictional scenario, the worker writes only:

| Heard | Room | Requested start | State |
|---|---|---|---|
| 09:12 | Room 2 | 15:00 today | not confirmed |

This row is an **intake artifact**, not evidence that a second booking exists. It contains no resident name, telephone number or fabricated booking identifier. The worker's spoken statement is: "I have noted the Room 2 request for 15:00 today. It is **not confirmed** until the approved schedule and booking procedure are checked." This both helps the visitor and leaves the claim testable. It is stronger than "probably fine" and more informative than "I can do nothing."

**Phase B — the view is reported available again.** Restoration of a screen does not, by itself, establish that its content is approved and current. The owner should define the authoritative source, the date/room/start comparison, any update delays, who may create a reservation, and what constitutes a confirmation receipt. In this exercise these checks are **required follow-up questions**, not observed technical events.

**Phase C — two explicitly hypothetical branches.** In branch **occupied**, assume an owner-approved current check finds a confirmed booking for Room 2 at 15:00 on the second day. The worker reports only "that slot is booked," preserves the original 09:12 pending request as a historical request record, and follows the owner's disposition process. No occupant name is necessary. In branch **no conflict shown**, assume the approved check finds no booking in its verified scope. The worker still must not tell the visitor "you have it": a separate authorized creation and confirmation step is needed, and its result is **not supplied**. Both branches are instructional conditional examples, not additional case cards or claims about what actually happened.

A careless reconciliation might silently erase the pending line after a screen comes back, leaving no record of what was promised or refused. A second error is to submit the same unconfirmed request repeatedly until some screen shows success. The exercise contains no request ID or idempotency contract, so there is no basis to claim duplicate suppression or exactly-once booking. Two requests for the same room/start also cannot automatically be collapsed into one person's request: no identity or cross-reference evidence is provided. Preserve the minimal queue and give unresolved conflicts to the owner under the approved process.

### 7.7 Distinguish continuity evidence from availability claims

The fact that a person can collect requests shows a **limited manual continuity function**; it does not prove that the online booking service or all library operations are available. The fact that a view returns later does not prove that previously submitted reservations were synchronized. Similarly, a pending slip is useful but does not establish capacity, staff coverage, queue safety, the duration for which the fallback remains usable, or the cause of either interruption. Those would need explicit evidence and, in a real institution, testing with its owners.

An evaluator can test this process safely with the invented slips without accessing production. Give one learner the role of worker, another the source steward, and a third a fictional visitor. Hide the hypothetical current-state card from the worker until the owner explicitly "releases" it. Check whether the worker keeps the intake state unconfirmed, distinguishes previous-day paper from current information, and avoids sharing an identity. Release one of the two conditional cards only after the worker names the required checks; record the proposed disposition **without pretending to execute a booking**.

A falsifier for the lesson's claimed success is simple: if the worker says "confirmed" before a checked current source *and* the separately approved confirmation step, the procedure has failed the learning objective—even if a later record happens to show the room free. The matching later outcome cannot retroactively authorize the earlier promise.

### 7.8 Independent practice: reconcile without inventing a receipt

Before consulting the appendix for **EX023**, reproduce the four-field 09:12 slip. Beside it, write a two-row decision matrix for **occupied** and **no conflict shown** as *hypothetical later findings*. For each row name (1) the necessary owner-approved source check, (2) the narrow spoken response, and (3) what remains unconfirmed. Finish with one sentence explaining why the previous day's 09:00 paper and the new outage's end time at 09:25 cannot independently confirm a booking. These are offline reasoning artifacts, not a live-system test or an instruction to collect personal data.

### Chapter 7 summary

A down page removes one way to see bookings. It does not authorize memory, yesterday's paper, or a verbal yes. A pending line with room, time and "not confirmed" keeps the service honest until a current source exists.

### Chapter 7 exercises

### EX023 — Write the pending line

- **Objective:** Continue service without confirming a room.
- **Input:** At 09:12 the booking view is down. A visitor wants Room 2 at 15:00 today. Yesterday's 09:00 paper is in the drawer.
- **Safe condition:** Do not diagnose the outage and do not use yesterday's paper as today's source.
- **Task:** Fill the four pending fields and state why yesterday's paper is the wrong source.
- **Expected evidence:** The four fields and one exclusion.
- **Rubric:** Credit if the state is "not confirmed," no name is stored, and yesterday's sheet is excluded because it is a different snapshot.

- **Independent extension:** After the four-field entry, distinguish intake time (09:12), the requested slot (15:00), the previous day's 09:00 snapshot, and the described 09:10–09:25 outage. Then write one conditional response for a later **occupied** result and one for a later **no-conflict** result, both subject to owner-approved checks. No branch is a confirmed booking in the supplied story.
- **Extended rubric:** A strong answer preserves a pending record, separates request from confirmation, names the necessary current-source/authority check, and never invents an actual read, an online booking, a resident identity or a completed reconciliation.
- **Check your result:** [EX023 worked answer](#answer-ex023).

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 20

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — A weak procedure is not yet a vulnerability

### Learning outcomes

After this chapter, you should be able to:

1. Use "weakness" for the stale-paper habit without upgrading it to an attack.
2. State the extra evidence a vulnerability claim would require.
3. Refuse a lesson that treats a classroom limitation as an incident report.

### 8.1 The words are not interchangeable

The [NIST Computer Security Resource Center glossary](https://csrc.nist.gov/glossary/term/vulnerability) describes a vulnerability as a weakness that could be exploited or triggered by a threat source. A threat, in the same glossary, is a circumstance or event that could harm operations or assets. An incident is not the same noun as either of those. Chapter 1 already separated threat, vulnerability, event and risk. This chapter applies that split to the only failure the book has actually built: people may treat a 09:00 printout as if it were the live schedule.

That habit is a weakness in the procedure. The book has not exhibited a defect in a booking program, a payload, a stolen account, or a harmed resident. Calling it a vulnerability is only fair if we also say "could be triggered" as a hypothesis and then show the trigger. We cannot show it. The library is fictional, and the outage has no measured cause.

### 8.2 Worked example

| Statement | Class in this book | Why |
|---|---|---|
| The 09:00 paper omits a booking created at 10:05 | Observation | It is in the synthetic table |
| Staff might confirm from that paper | Weak procedure | The exercise was built so that mistake is possible |
| An attacker took the booking page down | Unsupported | No evidence, and Chapter 4 forbids the live site |
| The booking software has a flaw an attacker could use | Not established | No program behavior was tested |
| The outage is a security incident | Not declared | No owner has defined it as one, and the cause is unknown |

The useful decision is procedural. Keep the pending rule, stop pencil edits, and do not name people who are not in the record. Those actions reduce the weakness the exercise can demonstrate. They do not close an incident that was never opened.

### 8.3 What a later lesson would need

A later, more technical course can examine a software flaw when it has an authorized program, a controlled input and an observed result. This rapid lesson stops before that. If a classmate writes "critical vulnerability, score 9.1" on the dossier from Chapter 4, the number is the false precision Chapter 4 already rejected, and the noun is the wrong class. The dossier stays a record of four synthetic verdicts.


### 8.4 A careful definition: a procedure can be a vulnerability, but evidence still matters

There is an important technical distinction within the [NIST vulnerability glossary](https://csrc.nist.gov/glossary/term/vulnerability): vulnerabilities are **not limited to bugs in software**. Weaknesses in system security procedures, internal controls, or implementations can also qualify when they could be exploited or accidentally triggered by a threat source. In other words, "it is a procedure, therefore it cannot be a vulnerability" would be incorrect. The defensible claim about Harbor Library is narrower: this **specific fictional exercise has not established an exploitable or triggerable failure in a verified real procedure**.

A security claim should say *what is weak*, *what event or actor could trigger it*, *what unauthorized or harmful outcome could follow*, and *what evidence connects the steps*. Neither actual attacker exploitation nor a real breach is necessary for all vulnerability analysis; an authorized, repeatable demonstration of a relevant defect under clear preconditions may support a vulnerability finding. However, a classroom model of a possible mistake, with no verified operational process and no reproducible security effect in an in-scope system, supports a **procedural weakness / potential risk scenario**, not an established product flaw or actual incident.

The [NIST threat-source glossary](https://csrc.nist.gov/glossary/term/threat_source) includes circumstances that might *accidentally* trigger a weakness; threat source does not always mean a malicious hacker. Here a staff member relying on a stale page is a possible human-error trigger. That possibility still needs a defensible link to a consequence before claims about impact or severity. Do not equate "a condition could cause harm" with "someone caused harm."

### 8.5 Evidence ladder: observation, hypothesis, finding, incident

Use each label for what the available evidence earns. The ladder is not a mandatory NIST workflow; it is a classroom method for preventing conclusion inflation.

| Label | Minimum justified statement | What remains to be established |
|---|---|---|
| **Supplied observation** | In the synthetic fixture, the 09:00 page does not contain SYN-002, created at 10:05. The view is described as unavailable for a bounded interval. | No real application was inspected and no real actor was observed |
| **Procedural weakness** | A worker who treats an old paper as current **could** make an unsupported booking decision | Whether this is the real organization's approved procedure and whether the bad decision occurs |
| **Risk scenario / hypothesis** | **If** the worker confirms from a stale sheet **and if** later booking state conflicts, a duplicate allocation or miscommunication **might** result | The trigger frequency, real controls, actual impact and likelihood |
| **Potential procedural vulnerability** | A defined control or operating rule **might** be triggerable under the specified conditions | Verified authority/scope, relevant weakness mechanism, reproducible check and credible security consequence |
| **Established vulnerability in an assessed scope** (not achieved here) | A sufficiently evidenced, in-scope weakness can be exploited or triggered, with a bounded impact rationale | Further contextual risk characterization, owners' assessment and any necessary remediation validation |
| **Security incident** (not established here) | An actual event meets applicable response criteria under authorized assessment | Event records, affected scope, organizational decision and the cause if known; the cause may remain uncertain |

An incident may be recognized on evidence of harmful events **without attributing them to an attacker**. Conversely, an outage is not automatically a security incident simply because it is inconvenient; one must apply the organization's incident criteria to the available evidence. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) positions response within cybersecurity risk management but does not decide whether Harbor Library's fictional interruption qualifies. The narrative supplies no verified owner classification or real-system telemetry.

### 8.6 Worked counterfactuals: identify the missing causal link

Start with the statement "The 09:00 sheet omitted a booking entered at 10:05." That is a **synthetic fact** under the fixed-snapshot assumption. Now compare five conclusions:

1. **Supported:** "A static 09:00 copy cannot show changes made at 10:05." The copy's timestamp and the row's creation time support this narrow claim.
2. **Reasonable hazard hypothesis:** "If someone uses that copy as a complete current source, they might promise a slot already booked later." The **if** clauses are essential. The fixture demonstrates a route to an incorrect decision, not a record of actual harm.
3. **Conditional process-vulnerability claim:** "If Harbor Library's approved production procedure actually permits unverified confirmation from stale copies, that control gap could be triggered by an outage and cause conflicts." This specifies a mechanism worth investigating but does **not** establish the premise for a real library.
4. **Unsupported technical cause:** "Attackers exploited a bug to bring down the booking site at 11:30." No bug, execution, attacker, diagnostic log or causal chain has been supplied. A described service interruption does not fill those gaps.
5. **Unsupported impact and priority:** "This was a critical, exploited vulnerability causing twelve bad reservations." Neither twelve affected bookings nor any severity analysis appears in this course. Chapter 4's offline verdict count cannot be promoted to affected people, incidents, or a numeric vulnerability score.

**Worked review of the original EX024 sentence.** "The 11:30 outage was an incident caused by a critical vulnerability in the booking site" incorrectly asserts **classification**, **cause**, **criticality** and **site defect** as facts. An appropriate replacement distinguishes (a) the described outage and fixed-paper timing, (b) the procedural confirmation weakness modeled with synthetic records, and (c) the unproved presence of a software vulnerability, attack or owner-declared incident. This correction does not suggest the weakness is harmless; it keeps the investigation decision honest.

### 8.7 What would an authorized vulnerability assessment require?

An assessment of a *real* procedure cannot be inferred from this fictional ledger. A future, separately authorized review would need a bounded plan with all of the following:

- **Asset and rule:** A named service or process, its actual authorized fallback source and the owner-approved decision rule. Without this, "weak" may simply mean "different from the student's invented policy."
- **Trigger and preconditions:** The exact circumstances under which the source becomes stale or unavailable, whether workers can still issue a confirmation, and which permissions they actually have.
- **Observable control behavior:** A reviewed design, a controlled and permitted test with synthetic data, or appropriately obtained historical records showing whether a wrong confirmation can occur. Distinguish an *attempted* confirmation from a committed reservation and from a communicated promise.
- **Competing explanations and negative control:** Repeat the same decision with a verified current source or a correctly applied pending rule; check whether the alleged failure disappears. A script result alone cannot establish what workers do in production.
- **Impact and confidence:** A credible security or service consequence under the owner's criteria, who could be affected, what is unknown, and what independent evidence would refute the mechanism. No unverified quantities or severity scores.
- **Decision authority:** A designated owner reviews the evidence and determines the bounded finding, severity and remediation. A learner has neither permission nor evidence to scan or modify the live service to settle the question.

The test's **falsifier** must be written before its result is known. For example, if an authorized controlled exercise shows that the approved procedure always holds post-snapshot requests pending until an owner-checked current source and separately authorized confirmation, the hypothesis that the procedure *allows* unverified confirmation is not supported by that test. One controlled success is not proof that all shifts, channels or future failures behave that way. Conversely, a repeated failure in a verified in-scope procedure might support a process vulnerability without any malware or malicious actor.

This is a hypothetical evidence plan, **not authorization to perform a test**. Chapter 2's scope restriction still applies: do not visit or probe real booking systems, collect resident data, run payloads or claim a technical assessment happened.

### 8.8 Independent evidence test and safer finding note

Using only Chapters 1–7, make a four-row matrix with columns **claim**, **evidence supplied**, **missing verification** and **safe decision**. Include: the old paper's missing row; a worker's possible unsupported confirmation; the described 11:30 outage; and an asserted "critical" site flaw. For each, find the first unsupported leap. Then write the three-sentence correction requested by **EX024** and check it against the following rubric: sentence 1 contains only actual synthetic observations and their time basis; sentence 2 names the procedural weakness conditionally; sentence 3 explicitly withholds the stronger cause, vulnerability, incident and severity claims.

An appropriate short finding note is: "This fictional exercise suggests a risk from relying on a fixed paper snapshot after later bookings exist. The student can test whether the pending rule prevents a wrong **proposed** confirmation under the supplied fixture; no production process or harmful outcome was verified. Before any organizational finding, the owner would have to verify the real procedure, trigger, effect and authorization." That is an assessment of **teaching evidence**, not a deployed vulnerability disclosure, incident report or grading of a real library.

### Chapter 8 summary

Harbor Library's exercise shows a stale procedure and the harm that procedure can cause inside the story: a wrong confirmation, a disclosure, or a ruined snapshot. It does not show an exploitable product flaw or an attack. Use the smaller word until the evidence grows.

### Chapter 8 exercises

### EX024 — Choose the smaller word

- **Objective:** Classify the stale-paper problem without inflating it.
- **Input:** A classmate's note says, "The 11:30 outage was an incident caused by a critical vulnerability in the booking site."
- **Safe condition:** Use only facts from Chapters 1–7. Do not investigate a real site.
- **Task:** Replace the note with three sentences: what was observed, what class of problem the exercise supports, and which stronger claim remains unproven.
- **Expected evidence:** Three sentences a reader can check against the book.
- **Rubric:** Credit if the outage stays unexplained, the supported class is a weak procedure, and neither vulnerability nor incident is asserted as fact.

- **Independent extension:** In an evidence matrix, identify the exact trigger, possible harm, verification still needed, and a falsifier for the **hypothesis** that staff can wrongly confirm from stale paper. Explain why a procedural vulnerability could in principle exist without a software bug but has not been proven in this case.
- **Extended rubric:** Full reasoning must distinguish observed synthetic data, a procedural weakness, a potential triggerable vulnerability, and an actual incident or severity assessment. An unsupported CVSS number, attacker, bug, affected-person count or real-world test fails the task.
- **Check your result:** [EX024 worked answer](#answer-ex024).

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 20

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — A verdict tally is not a severity

### Learning outcomes

After this chapter, you should be able to:

1. Read `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0` as four counted labels and one empty remainder.
2. Keep that census separate from adverse impact and from likelihood.
3. Refuse a score, a percentage, or a rank built only from those five numbers.

### 9.1 The program counts labels

Chapter 4's program walks the synthetic log once. Each action receives one label, and that label's counter increases by one. The printed line is a census of this log:

`STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`

Four actions entered. Four decided labels came out, one of each class, and the remainder stayed at zero. Those equal counts belong to the exercise design. The log was written with one action per class so every branch would appear. A later week at a real desk could show forty ALLOW lines and one REFUSE line. That single REFUSE could be the only line on which a resident would have been told that a taken room was free. Equal classroom counts do not make the classes weigh the same.

`UNKNOWN 0` means every action in this log matched a branch of the written rule. The outage still has no tested cause. The reported 11:40 sheet is still unchecked. The library still has open questions. None of those facts was an action in the log, so none of them can move a counter.

### 9.2 Worked example

[NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), as carried in the [CSRC glossary entry for risk](https://csrc.nist.gov/glossary/term/risk), treats risk as a measure of the extent to which a potential circumstance threatens an entity, typically a function of adverse impact and likelihood. Accessed 13 October 2026. The Harbor tally supplies neither input. It does not estimate how often staff would trust a stale printout, and it does not measure the harm of a wrong confirmation. This chapter uses that distinction only. It does not perform a risk assessment, and it does not assign the library a level.

| Sentence a classmate proposed | What the printed line can support | Decision |
|---|---|---|
| "The run labeled one action of each class, and no action was UNKNOWN." | The five counters | Keep, as a count |
| "Half the verdicts were adverse, so the figure is 50 percent." | No impact and no likelihood | Refuse the percentage |
| "ALLOW 1 shows that one room was confirmed free." | The rule found no later booking for that slot | Refuse the availability claim |
| "UNKNOWN 0 shows that the 11:30 outage is understood." | The log had no unmatched action | Refuse the causal claim |
| "Give the library 2.5 and close the exercise." | No scale, and no owner has accepted a current source | Refuse the score and the closure |

The report that survives is the four Chapter 4 decisions, named one by one, plus the statement that impact and likelihood were not measured. Chapter 8 kept the demonstrated problem in the class "weak procedure." This chapter leaves that class where it is.

### 9.3 What the counters leave open

A facilitator can still ask which approved source, if any, may replace the 09:00 paper. That question sits outside the tally. Treating the counters as balanced would hide the pending Room 2 at 15:00 request from Chapter 7. The arithmetic of this log is finished. The booking decision is still open.


### 9.4 What the five counters actually measure

A **counter** is the number of records assigned a specified label under a specified rule and scope. A **denominator** defines the population over which a ratio is calculated. The Chapter 4 Python program has exactly four **synthetic proposed actions** in its ACTIONS list, not four security incidents, four room bookings or four residents. The five possible verdicts classify the written rule's treatment of those proposed actions. The mapping is deterministic for the fixed synthetic inputs; that repeatability is not proof of validity outside the fixture.

| Label | Which recorded proposal produced it | What the counter says | An inference the counter does not permit |
|---|---|---|---|
| STOP = 1 | 11:44, proposed live-site access | One action crossed the classroom authorization boundary | A real intrusion or service breach occurred |
| OUT OF SCOPE = 1 | 11:43, proposed event-contact export | One action concerned data excluded from this booking-time comparison | A contact list was actually exported or compromised |
| REFUSE = 1 | 11:42, confirm Room 2 at 15:00 from the 09:00 paper | The fixed rule found the later SYN-002 booking and refused that proposed confirmation | One resident was harmed, or a technical exploit succeeded |
| ALLOW = 1 | 11:45, mark Room 2 / 15:00 pending | The synthetic fallback rule permits recording an unconfirmed request | A room was reserved or is presently free |
| UNKNOWN = 0 | No action fell outside the five written rule branches | The four inputs were all classified | The cause of the outage, completeness of logs or safety of the procedure is known |

The counts sum to **four**, not five: UNKNOWN is a zero category within a five-label vocabulary. Each proposal receives one verdict for this run. The tally does not prove that all actions staff might take were observed, that the rule is complete for production, or that its categories are ordered by harm. The STOP and OUT OF SCOPE branches are boundaries of the exercise, not measured negative security outcomes.

A ratio can be **arithmetically correct and semantically invalid**. If somebody *defines* the arbitrary set {STOP, REFUSE}, then two of the four entries have those labels, and 2 / 4 = 50% is a correct share of **this selected label grouping**. Nothing in the rule establishes that STOP and REFUSE are both adverse consequences or that the four authored examples represent the frequency of real operational actions. The dashboard's phrase “50 percent adverse” therefore has no validated numerator or meaning as a harm rate. Separately, “25” is not derived from the published output; no risk-score model or scale was defined.

### 9.5 Distinguish a classifier, an event sample, and an assessed risk

**Classification** maps an input to a predefined label. **Risk** concerns a potential circumstance's adverse impact and likelihood, informed by threats, vulnerabilities, controls and the context of the affected organization. **Severity** may refer to the magnitude of consequences, the priority of an event, or a defined scheme's vulnerability rating; those uses are not interchangeable, and each needs explicit criteria. A high count is not necessarily high impact. A high-impact, rare failure might appear once; a harmless and frequently exercised branch might appear hundreds of times. Without a defined outcome and exposure population, **the rate of verdicts is neither a likelihood estimate nor a severity rating**.

[NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) provides a systematic framework for risk assessment, and the [NIST risk glossary](https://csrc.nist.gov/glossary/term/risk) explicitly distinguishes possible adverse impact from likelihood. These references support why the two evidence dimensions matter. They do **not** prescribe a numeric Harbor Library dashboard or imply this fictional laboratory has enough observations for one.

To move from a proposed **risk scenario** to an organizational assessment, the service owner would need at least: a precisely defined harm (for example an unauthorized second confirmation of the same slot), an affected service and decision boundary, credible evidence of triggering conditions, existing control performance, impact criteria, exposure or occurrence evidence, and an approved way to express confidence and uncertainty. A **severity** label additionally needs the governing scale and authority. None of that arrives simply by summing STOP, REFUSE or UNKNOWN.

Treat these quantities as separate fields:

| Quantity | Present in this manuscript? | What would be needed to use it |
|---|---|---|
| Four authored action inputs and five classifier counters | Yes, fixed reproducible fixture | Retain the exact fixture, mapping and run scope |
| Number of actual wrong room confirmations | No | Authorized booking/communication records and relevant verification |
| Number of people harmed | No | Lawful, scoped evidence of an adverse effect; do not invent identities |
| Probability of a future wrong confirmation | No | Relevant exposure model and observed or justified control behavior |
| Impact magnitude, severity threshold or numeric risk score | No | Owner-approved impact definitions, data, method and review |
| Root cause of either fictional outage | No | An authorized investigation and source-supported causal evidence |

The safest conclusion is not “risk is zero.” It is **“risk and severity were not estimated from this exercise.”** The source data are too narrow. An unknown quantity cannot be converted into zero, and an UNKNOWN verdict count of zero cannot substitute for missing organizational evidence.

### 9.6 Contrasting examples and negative controls

**Case A: equal counters, unequal meaning.** In the published four-action log, one REFUSE prevents the simulated worker from confirming a slot already represented by SYN-002 in the full fixture. One OUT OF SCOPE blocks a *different data-purpose proposal*. Neither action is an observed breach, and equal counts do not imply equal consequence. A manager may wish to prioritize correcting stale-paper practice, but even that organizational prioritization would require a named service owner and supporting evidence.

**Case B: different label frequency, same missing risk evidence.** Imagine a **separate hypothetical** offline worksheet with forty mark-pending proposals and one confirm-from-printout proposal. The likely label balance would differ under stated inputs. It still would not provide a real incident frequency, affected-person count or future probability. This is an illustration only; it is **not a second program run**, a changed Chapter 4 tally or an observed library shift.

**Case C: severity claimed from an unmatched count.** UNKNOWN 0 tells us the four written action kinds had branches. A facilitator could add a hypothetical action kind not defined by the rule; it would yield UNKNOWN in a **separate model variant**. That change indicates coverage of the *classifier*, not more harm or a resolved outage cause. No variant is executed or inserted into the published census.

**Negative-control review:** for each candidate statement ask, “If I kept the exact four printed labels but changed the real-world harm, would the statement still be true?” The tally remains true; a harm rate and severity ranking would not be determined. Ask also, “Could a perfectly covered rule set report UNKNOWN 0 while a required human approval or source check remains missing?” Yes: label coverage and operational authority are different questions. These controls challenge the inference, not the source fixture.

### 9.7 Worked replacement for the misleading dashboard

The classmate wrote: “Harbor risk score 25. Two adverse verdicts out of four is 50 percent, so the library is Medium and the exercise can close.”

A checkable replacement preserves the **four-sentence** structure required by EX025:

1. “The fixed four-action Harbor Library exercise returned STOP 1, OUT OF SCOPE 1, REFUSE 1, ALLOW 1 and UNKNOWN 0.”
2. “Grouping two selected labels into 2/4 is arithmetically possible, but this designed set does not measure adverse events or their frequency, so calling 50% a harm or risk rate is unsupported.”
3. “No likelihood evidence, impact criteria, severity thresholds or owner-approved scoring method were supplied; neither risk score 25 nor Medium is established.”
4. “The Room 2 / 15:00 request remains unconfirmed pending an owner-approved current source and the separate booking decision; the reported 11:40 copy is not yet checked.”

This language reports an actual classifier output, distinguishes undefined terminology from valid arithmetic, withholds an unsupported rank and keeps the operational decision open. The classroom verdict REFUSE need not be removed for its purpose to be understood. **No new run, risk assessment or accepted recovery action is claimed.**

### 9.8 Independent practice and self-check

Before opening the [EX025 worked answer](#answer-ex025), produce the four replacement sentences yourself. Add a private-to-the-lesson comparison matrix with columns **claim**, **fixture observation**, **missing organizational evidence**, and **valid next question**. Test the incorrect phrases “25,” “50% adverse,” “Medium,” “UNKNOWN 0 means all is safe,” and “ALLOW means the slot is free.” For each, identify the first unsupported step. Preserve Chapter 4's exact tally and the outstanding pending state. An answer passes if a second reader can distinguish a synthetic counter, a mathematically definable category share, and an unsupported risk inference without assigning another score.

### Chapter 9 summary

The tally is a census of labels on one synthetic log. Equal counts come from the way that log was built. They do not state a severity, a probability, or permission to stop asking which source is current.

### Chapter 9 exercises

### EX025 — Take the score off the dashboard

- **Objective:** Keep the Chapter 4 tally as a count.
- **Input:** A classmate's dashboard says, "Harbor risk score 25. Two adverse verdicts out of four is 50 percent, so the library is Medium and the exercise can close."
- **Safe condition:** Use the printed tally from Chapter 4. Do not invent a second run or open a live site.
- **Task:** Replace the dashboard with four sentences: what was counted, why 50 percent does not follow, why Medium does not follow, and which decision remains open.
- **Expected evidence:** Four sentences a reader can check against the printed line and Chapters 4, 7 and 8.
- **Rubric:** Credit when the tally stays a count of four labels, the percentage and the rank are both refused, and the pending confirmation is still unresolved. A replacement number does not earn credit.

- **Independent extension:** Show why 2 / 4 could equal 50% only for an **explicitly chosen group of labels**, while failing as a harm rate. In a four-column ledger classify each dashboard claim as an arithmetic fact, a semantic assumption, an unsupported risk judgment, or an unresolved operational decision. State which evidence about impact, likelihood, and a defined scoring scale would be needed for an organizational assessment.
- **Negative-control criterion:** The four sentences must preserve the five original counters, leave UNKNOWN 0 distinct from the outage's unknown cause, not invent a real incident count, and keep the 15:00 request pending. No extra numerical score or program run is authorized.
- **Self-check:** Compare with the [EX025 worked answer](#answer-ex025).

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 20

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — A spoken time is not a printout

### Learning outcomes

After this chapter, you should be able to:

1. Classify a repeated clock time as a report rather than as a printout.
2. Name the two checks that would have to succeed before an 11:40 sheet could replace the 09:00 paper.
3. Leave the Chapter 4 run unchanged when the only new item is that report.

### 10.1 The rule reads an artifact, not a recollection

Chapter 4 compares a fixed printout clock with the time a booking was created. The published run uses 09:00. `SYN-002` was created at 10:05, so the paper omits it, and the 11:42 confirmation is REFUSE. A sentence such as "the owner mentioned an 11:40 refresh" contains the words for a later clock. It does not contain the sheet, the rows, or a signature that this object is the approved source.

Those are different inputs. The program cannot see a conversation. If a learner types 11:40 because a facilitator spoke it, the learner has invented the input. Chapter 6 already refused a pencil mark on the 09:00 sheet. This chapter refuses a different substitution: replacing the sheet with talk about a sheet.

Chapter 3 recorded the owner's mention of an 11:40 copy as **reported, not verified**. That label still holds. Repeating the mention in the classroom does not verify it. The Chapter 9 tally also stays as printed. This conversation is not one of the four logged actions, so it cannot clear REFUSE or move UNKNOWN.

### 10.2 Worked example

Two gates have to pass before anyone treats a later sheet as the current source. The exercise owner names **this** sheet as the approved current source. A learner then looks at that sheet and writes down two observations: the time on the sheet is 11:40, and `SYN-002` is printed on it. Hearing that both gates "were probably done" is a third report. It completes neither gate.

| What is in front of the learner | Class | May Room 2 at 15:00 be confirmed from it? |
|---|---|---|
| Facilitator: "I heard the owner say 11:40 includes SYN-002." | Second-hand report | No |
| A sheet timed 11:40 with SYN-002 visible, and no statement from the owner that this sheet is the approved source | Checked artifact, authority open | No |
| The same sheet, after the owner names it and both observations are written down | Approved checked source | Only by the procedure the owner stated |
| A plan to retype 11:40 into the Chapter 4 program | Invented input | No. Do not start that run |

The useful record is short. The 09:00 result stands. The 15:00 request stays not confirmed. The spoken time is filed as a report beside the paper, not on top of it.

### 10.3 What this chapter does not open

Passing both gates in a later exercise would still be one synthetic check. It would not show how often a real desk refreshes its fallback sheet, and it would not explain the outage. This lesson stops at the report. It does not hand the learner an 11:40 sheet, and it does not ask for a new program run.


### 10.4 Four different times can appear in one sentence

An accurate security or operational record distinguishes **event time**, **source creation or snapshot time**, **report time** and **decision time**. A sentence can mention a time without providing evidence for the event purported to occur then. Do not silently turn “someone heard that a newer sheet had an 11:40 heading” into “a verified sheet was issued and authorized at 11:40.” The case supplies a *report of a possible 11:40 refresh*, not its receipt or creation log.

| Time and item | Status in Chapters 3–10 | What it supports | What remains unproved |
|---|---|---|---|
| SYN-001 creation at 08:20 | Synthetic reservation-row fact | Its creation predates the fixed 09:00 paper | Any resident identity |
| 09:00 printout | Fixed synthetic copy used in the Chapter 4 run | The source time and scope of the original comparison | Later updates or complete current availability |
| SYN-002 creation at 10:05 | Synthetic fixture fact | A later confirmed booking exists in the full teaching table | That this later record was on the 09:00 paper |
| 11:30–11:50 view outage | Described first-day interruption | The front-desk view is unavailable in the stated interval | Cause, actor, incident classification or recovery target |
| 11:42 confirm-from-printout proposal | Classified action, not an executed booking | REFUSE under the fixed 09:00 rule | That any real booking was refused or confirmed |
| “11:40 refresh” in the owner's mention | **Reported** time of a proposed other sheet | A candidate source warrants follow-up | That the sheet exists, was inspected, was authorized or contains SYN-002 |

A **spoken time** is testimony about a purported record; a **time printed on an artifact** is an observable attribute of that artifact; a **source-generation or synchronization record** would support a further claim about how that artifact was made. Each is a different evidence layer. The lesson does not provide a certified source-generation receipt, audit chain, signature or independent timestamp validation. Even if a future sheet prints “11:40,” its heading alone would not prove completeness or authority.

The classic log-management concerns of source, timestamp, retention and review are discussed at a high level in [NIST SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final). That publication dates from **2006**; we use its general provenance vocabulary, not dated implementation advice or an assertion that the library has a particular log platform. The four-layer ledger below is an **original classroom evidence method**, not a mandatory NIST form.

### 10.5 Provenance is a chain of claims, not an attractive header

An artifact useful for an operational decision needs a scope: which day, which room and start, what data it represents, when it was produced, which owner approves using it, and which relevant contents were actually checked. The requested current-source question is separate from the authorization to **create** a reservation. The minimum checks from Section 10.2 are:

1. **Owner's identification of the exact source:** The designated exercise owner names **this particular later sheet** as the approved current source for the bounded task. An attendee's recollection of the owner's words does not name a physical artifact now in the worker's possession.
2. **Direct observations from that same artifact:** The worker sees its **11:40 heading** and the relevant **SYN-002** printed row and records those observations. Merely hearing that both appear is not inspection.

These two gates are **necessary for the later-sheet decision within this story**, not sufficient to declare every future schedule fresh, verify a real digital supply chain or authorize a new booking. The follow-on scope checks still matter: is the record for the correct day, does the row specify Room 2 / 15:00 and confirmed status, is this copy allowed for the requested decision, and has any owner-specified cutoff or superseding update intervened? This course does not provide a later update receipt, so no stronger freshness claim can be manufactured.

**Boundary with Chapter 11:** In Chapter 10, none of those direct artifact observations has happened. Chapter 11 will **separately release** a named synthetic page and supply its two visible rows. Do not backdate Chapter 11's evidence into the earlier chapter or reclassify the first four-action run after the fact.

### 10.6 Worked contrast: the same clock under different evidentiary conditions

| Candidate input to the desk decision | Evidence class | Permitted decision in this chapter |
|---|---|---|
| The 09:00 synthetic paper together with its known fixed scope | Original, limited source | The Chapter 4 REFUSE and pending request stand |
| “I heard the owner say 11:40” | Second-hand report, no sheet | Record a lead for checking; do not confirm |
| “The facilitator tells me the sheet contains SYN-002” | Another oral report, without direct inspection | Do not silently convert the report into a verified row |
| A purported 11:40 paper whose heading is visible but has no identified authorized issuer | Observed header, authority and row checks missing | Neither confirmation nor substitution of the old source is justified |
| An owner-identified copy whose 11:40 heading and SYN-002 row are directly checked | **Conditional future teaching case**, not evidence released here | Use only for the bounded decision its owner authorized; inspect status before saying a slot is taken |
| Retyping PRINTOUT = 11:40 in the Chapter 4 Python script | Changed model assumption, not an acquired sheet | Does not verify the real world or erase the original REFUSE |

**Worked counterfactual, not an executed test:** Suppose a learner imagines a new PRINTOUT time of 11:40, while retaining the fixture's 10:05 booking creation. The “later than printout” predicate for SYN-002 would no longer be true, so the classifier *might* change the action's label in a separately declared run. That difference would follow **only from altered input**: the original program did not consume the reported page, and no actual owner approval or booking confirmation would follow. The original tally must remain unchanged. This is not a proposal to run modified code as the public source of truth.

There is also a critical **semantic negative control**: if a valid newly inspected sheet includes SYN-002 as a **confirmed 15:00 reservation**, the correct room-state statement is **“already booked,” not “available.”** An authenticated source can narrow uncertainty while ruling out the very confirmation the visitor seeks. Passing a source-validation gate is not the same as passing a transaction-authorization gate.

### 10.7 Preserve chronology when reporting a new source

Write a small ledger with explicit labels rather than inserting a newer time over an old one:

| Entry | Knowledge status at this chapter | Proper follow-up |
|---|---|---|
| Chapter 4: 09:00 printout and four-action verdicts | Observed **within synthetic fixture** | Preserve the exact inputs, output and tally |
| Chapter 3: owner may have an 11:40 offline refresh | **Reported but unverified** | Ask owner to identify the actual candidate sheet |
| Chapter 10: facilitator repeats what was said | Second-hand report; no new artifact | Do not claim direct inspection or approval |
| Future: named sheet and row verification | **Not performed in this chapter** | Record separate observation, authority, source and outcome if later released |

This record distinguishes **when a statement became known to the learner** from **when its alleged source was made**. Neither timestamp should be silently overwritten. A second retelling is not a second independent source. The owner might later refute the recollection, provide a different sheet, or define narrower authority; until the evidence arrives, those are open possibilities, not findings.

For a current-day request, the pending queue remains a request queue. A manager's spoken approval of a source (if someday authenticated in the case) would **not** by itself authorize a new booking or prove availability: content and transaction rules remain distinct. The no-live-site rule persists throughout the tabletop; do not search or export names as an alternate shortcut.

### 10.8 Independent rehearsal and falsifier

Before the [EX026 worked answer](#answer-ex026), write a three-part response to the classmate's sentence: (a) classify it precisely as a **second-hand report**; (b) state the two checks that **have not** occurred—owner naming the exact candidate sheet and direct observation of the sheet's 11:40 time plus printed SYN-002 row; (c) leave Room 2 at 15:00 **not confirmed**, with the published Chapter 4 REFUSE and tally intact. Add a one-line evidence ledger separating **heard**, **seen**, **approved** and **executed**. The exercise succeeds only if **seen**, **approved** and **executed** are not fabricated.

Use two negative controls. First, substitute a second person's repetition of the 11:40 claim: it remains hearsay, not independent artifact evidence. Second, imagine that a truly inspected approved 11:40 page shows SYN-002 as confirmed: it **blocks** a new 15:00 allocation; it does not retroactively make the 11:42 paper proposal acceptable. Stop at the report in this chapter and leave the later page for Chapter 11.

### Chapter 10 summary

A clock time that arrives in a sentence is testimony about a source. The confirmation rule needs the source. Until the owner names the sheet and the learner records its time and `SYN-002`, Room 2 at 15:00 stays pending and the published tally stays as it was.

### Chapter 10 exercises

### EX026 — File the sentence beside the paper

- **Objective:** Keep a heard refresh time from becoming the printout.
- **Input:** A classmate's note says, "The facilitator heard the owner mention 11:40, so confirm Room 2 at 15:00 and clear the REFUSE."
- **Safe condition:** Stay inside the synthetic exercise. Do not type a new printout time into the Chapter 4 program, and do not open a live site.
- **Task:** Write three parts: the class of the note, the two checks that are still missing, and the booking state you leave in place.
- **Expected evidence:** Three parts a reader can check against Chapters 3, 4 and 7.
- **Rubric:** Credit when the note stays a report, both the owner's naming and the sheet observations are still missing, the 15:00 request stays not confirmed, and the published tally is left unchanged.

- **Independent extension:** Produce a two-row evidence ledger for (1) the 09:00 paper actually used in Chapter 4 and (2) the **reported, unseen** 11:40 sheet. For each, name the source status, time assertion, missing check and authorized next decision. Contrast an oral repetition with a conditional owner-identified, directly inspected page without pretending the latter has been released yet.
- **Negative-control criterion:** A repeated verbal 11:40 must not become a confirmed new source; neither a later heading nor a successful source check could make a slot already occupied by SYN-002 free. Preserve the published REFUSE and complete tally.
- **Self-check:** Compare with the [EX026 worked answer](#answer-ex026).

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 20

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — A named sheet does not free the room

### Learning outcomes

After this chapter, you should be able to:

1. Read a named synthetic 11:40 page that includes `SYN-002` as evidence that Room 2 at 15:00 is already booked.
2. Keep that reading inside this exercise: leave the Chapter 4 tally untouched, and do not turn the page into a rule for later outages.
3. Refuse a person's name and refuse a live-site check when the page itself has answered the slot.

### 11.1 What the named page can decide

Chapter 10 stopped while the 11:40 page was only talk. This lesson changes the table. The exercise owner places one synthetic page in front of you and says that **this page** is the approved current source **for this exercise**. The heading on the page is 11:40. The rows are:

| Booking | Room | Start | Created | Status |
|---|---|---|---|---|
| `SYN-001` | Room 2 | 14:00 | 08:20 | confirmed |
| `SYN-002` | Room 2 | 15:00 | 10:05 | confirmed |

You record two observations from the page, not from memory. The heading clock is 11:40. `SYN-002` is a printed row, with Room 2, start 15:00, created 10:05, and status confirmed. Both observations succeed. The owner's sentence and those two observations are the whole authority for this sitting.

The decision those facts support is narrow. A resident who asks for Room 2 at 15:00 is asking for a slot that this page already lists as a confirmed booking. Staff say the slot is taken. The page has booking identifiers and no personal names, so the spoken answer does not add one. `SYN-002` identifies the synthetic row. It is not a person, and announcing the identifier is unnecessary for the resident's question.

`SYN-001` is a different start time. A booked 14:00 slot does not, by itself, decide 15:00. The 15:00 answer comes from the `SYN-002` row. Mixing the two rows would invent a conflict, or a free hour, that the page does not state.

### 11.2 Worked example

The 09:00 printout and this page are different artifacts, so their labels do not cancel. Chapter 4 refused a confirmation that used the 09:00 printout, because that printout has no `SYN-002` row. This page does have the row. The correct speech from this page is still not "the room is free." It is "the slot is taken." Erasing REFUSE would pretend the earlier program had read this page. It had not. Nobody reruns that program, and nobody types 11:40 into it. The published census remains the census of that older log.

| Classmate's next step | What this page actually settles | Decision |
|---|---|---|
| "Both checks passed, so call Room 2 at 15:00 free." | `SYN-002` is a confirmed 15:00 booking | Refuse. Say the slot is taken |
| "Clear REFUSE on the Chapter 4 tally." | The tally labels the 09:00 run | Leave the printed line unchanged |
| "Treat 11:40 as the fallback for every outage this month." | The owner named one page, once | Refuse the standing rule |
| "Open the live site and see whether production matches." | The exercise supplied a paper page | Stop. The site stays closed |
| "Tell the resident who holds 15:00." | No name is printed | Refuse the name |

The notebook line that matches the page is: Room 2 at 15:00 is already booked on the named 11:40 page; no name is given; the Chapter 4 census stays as printed; the page expires with this exercise.

### 11.3 What one page cannot settle

A single synthetic page cannot show how often a real desk reprints a fallback schedule. It cannot explain why the booking view was unavailable. It cannot authorize a search of a live system. The owner's sentence should be copied into the notebook with its limit attached: named for this exercise, not adopted as the library's outage procedure. When the sitting ends, the next outage is pending again until its own source is named and checked.

The Chapter 4 ALLOW line is also the wrong tool here. In the published four-action log, that label belongs to the 11:45 **mark-pending** proposal; the program separately discusses a hypothetical Room 4 input change that could print ALLOW, but that variant was not the logged ALLOW. Neither label grants a room or overrides the 11:40 page. Room 2 at 15:00 now has a confirmed row on the named page, so calling it free contradicts the source.


### 11.4 A bounded source is evidence, not a universal permission

**Source authorization** answers which artifact may be consulted for a particular question. **Evidence of content** answers what that artifact actually states. **Transaction authority** answers who may commit or change a reservation. These are three independent gates: an approved source may establish that a slot is occupied while still providing no permission to assign it to somebody else.

Chapter 10 ended with the purported 11:40 refresh as *reported but not verified*. Only **at the start of Chapter 11** does the fictional exercise owner place an actual synthetic page on the table and designate *that page* as current **for this sitting**. The learner inspects the heading and its two rows. That changes the evidence available for the **present** room-state question. It does not change what an earlier worker saw at 11:42 while relying on the 09:00 copy, and it is not a standing authorization for future days or outages.

A compact evidence record should preserve six distinctions:

| Field | Evidence released here | What must not be added |
|---|---|---|
| Artifact identity | One particular synthetic paper page placed by the exercise owner | A verified production schedule, API result or permanent offline replica |
| Authority | Owner names **this page for this exercise** | Blanket authorization for all future outages or transactions |
| Stated source time | Visible heading **11:40** on the named page | Independent proof of system synchronization, printing mechanism or later updates |
| Relevant row | `SYN-002`: Room 2, 15:00, created 10:05, confirmed | Name of the resident, cause of a system outage, or evidence of a second reservation |
| Bounded decision | The page shows the Room 2 / 15:00 slot **already booked** | Room 2 is free or may be transferred to this asker |
| Historical result | Chapter 4's 09:00-based **REFUSE** and original tally remain | A rerun, cancellation of REFUSE or correction of the earlier source |

[NIST CSF 2.0, PR.AA-05](https://doi.org/10.6028/NIST.CSWP.29) describes defined, managed and enforced authorizations; it does **not** define the fictional library's approval procedure. The [NIST SP 800-53 Rev. 5, AU-3](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) discusses recording event type, time, source and outcome to support auditability. The page/owner ledger above adapts the *conceptual distinction* between source, time, authorization and result; it is original classroom reasoning, **not** a claim that Harbor Library implemented an NIST audit control or that this one piece of paper meets federal control requirements.

### 11.5 Work the two gates against the exact row

**Input:** the newly released 11:40 page contains two printed synthetic records. `SYN-001` is Room 2 / 14:00 (created 08:20, confirmed); `SYN-002` is Room 2 / 15:00 (created 10:05, confirmed). These are different slots. No names or external systems are provided.

**Gate 1 — is this the source designated for the question?** For *this* sitting, yes: the owner identified the page. This is a role-play grant for reading, not verification of how a real system produces schedules. If the owner had only repeated “a sheet may exist,” as in Chapter 10, this gate would **fail**.

**Gate 2 — what does the chosen page show?** Record the heading 11:40 and inspect the row matching **both** requested fields: Room 2 **and** 15:00. The `SYN-002` row explicitly says `confirmed`. A row with start 14:00 cannot be substituted merely because it names the same room. With that direct observation, the supported answer to “Can I have Room 2 at 15:00?” is **“That slot is already booked.”**

Neither gate is a **booking-creation** gate. Even when the source is approved and the relevant row has been read correctly, staff have not been authorized to make a different resident's booking, disclose a person, modify the printed row, or claim success in a production application. The room-state conclusion is bounded to the paper's scope and the exercise. The page may contain information useful for refusing an unavailable slot without proving its completeness for *other* rooms or times.

**Worked comparison of five proposed decisions:**

| Proposal | Evidence/authority finding | Appropriate statement |
|---|---|---|
| “Both source checks passed, so the room is free.” | The matching row has status **confirmed**, meaning occupied in this fixture | “Room 2 at 15:00 is already booked.” |
| “The heading says 11:40, so it is valid for every future outage.” | Approval is bounded to **this page and sitting** | Later uses need their own approved source and time check |
| “The 14:00 booking tells us what happens at 15:00.” | Room matches but time does **not** | Use `SYN-002`, not `SYN-001`, for 15:00 |
| “A new page means the 09:00-based REFUSE was wrong.” | An old verdict is evaluated against an old fixed snapshot | Preserve the historic REFUSE and original tally |
| “The sheet contains a code, so announce the holder's name.” | `SYN-002` is an invented identifier and the sheet has **no names** | State that the slot is booked without identifying a person |

### 11.6 Preservation of chronology and a meaningful negative control

The Chapter 4 classifier uses `PRINTOUT = "09:00"` and the fixture's later `SYN-002` creation time of 10:05. For its 11:42 **proposed** confirm-from-printout action it outputs REFUSE. The printed four-action tally is **STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0**. In that **fixed** log, ALLOW belongs to the **11:45 mark-pending** proposal. Chapter 4 separately discussed a *hypothetical Room 4 input change*; that was **not** the published 11:45 ALLOW row and produced no replacement tally.

**Negative control A — remove the owner naming.** Keep the same printed page visible but imagine the exercise owner does **not** designate it. The text `SYN-002` remains observable, yet authority to use this page as a decision source is missing. Correct action: keep the current decision pending until the owner approves an appropriate source. Visibility is not authorization.

**Negative control B — preserve the naming but choose the wrong row.** The page remains authorized, but using `SYN-001` (14:00) to answer the 15:00 question violates the room/start match. Correct action: reject the wrong inference and use `SYN-002` for the actual question.

**Negative control C — carry the answer into a later sitting.** The 11:40 page remains unchanged, but the date and authorization scope are different. Correct action: do not automatically reuse the page. Chapter 13 will teach that next-sitting boundary explicitly, and the current lesson must not pre-decide its request.

The point is not to make the reply maximally hesitant: **when owner naming and a matching confirmed row are both supplied in this sitting, “already booked” is a well-supported bounded answer.** The same evidence does not authorize a new allocation, a personal disclosure, an old-log rewrite or an indefinite procedure.

### 11.7 Independent EX027 practice

Before consulting [EX027's worked result](#answer-ex027), write the four sentences requested by the original exercise. Underline which sentence depends on the page's visible `SYN-002` row, which protects the historical 09:00 output, and which limits the owner's authorization to a single sitting. Then build a short two-column **claim versus evidence** card for “booked,” “free,” “re-open REFUSE,” and “monthly fallback.” The correct card must show the actual row fields `Room 2 / 15:00 / confirmed` and preserve the exact five-counter line.

As a second independent check, apply negative controls A and B from Section 11.6 without inventing a new case result. State which **gate** failed and which claim must be withheld. Do not open any live site, create a new booking or reveal a resident name. A learner who says “free” after reading `SYN-002` has interpreted the **opposite** of the evidence.

### Chapter 11 summary

When the owner names this 11:40 page and both observations pass, Room 2 at 15:00 is taken. That answer does not clear the older tally, does not identify a person, and does not become the rule for the next outage.

### Chapter 11 exercises

### EX027 — Take the leap off the page

- **Objective:** Use a named 11:40 page without turning a booked slot into a free room or a monthly rule.
- **Input:** A classmate writes, "Both gates passed, so the room is free, clear REFUSE, and use 11:40 for every outage this month."
- **Safe condition:** Paper only. Leave the Chapter 4 program closed, and leave any live booking site closed.
- **Task:** Write four sentences: what `SYN-002` shows about Room 2 at 15:00, why "free" reverses that row, why the Chapter 4 line stays, and why 11:40 does not govern the next outage.
- **Expected evidence:** Four sentences a reader can check against the page in Section 11.1 and against the published Chapter 4 tally.
- **Rubric:** Credit when the slot stays booked, the tally is left as printed, the monthly rule is refused, and no person's name and no live site appear. A new program run does not earn credit.

- **Independent extension:** Construct an evidence-to-decision card distinguishing (a) owner naming for this sitting, (b) the `11:40` heading and exact `SYN-002` row, (c) the scoped “already booked” reply, and (d) what the page **does not** authorize. Explain why Chapter 10 could not use this artifact before it was released.
- **Negative controls:** Reconsider the decision if the owner had not named the page, and if a learner selected the 14:00 `SYN-001` row for the 15:00 query. Neither control permits “free,” “reservation created,” a personal name, or erasure of the old `REFUSE`.
- **Self-check:** [EX027 worked answer](#answer-ex027).

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 20

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — A missing row is not a free room

### Learning outcomes

After this chapter, you should be able to:

1. Match a room-and-start question to a row on the named 11:40 page.
2. Treat a question with no matching row as silence, not as a free room.
3. Leave the Chapter 4 ALLOW label and the printed census on the 09:00 log.

### 12.1 Authority is not the same claim as completeness

Chapter 11 used the named page for a question the page can answer. `SYN-002` prints Room 2 at 15:00, so that slot is taken. A new resident question now asks for Room 4 at 15:00. The same page is still on the table. Its two rows are still the whole page. Neither row says Room 4.

Naming gave permission to read this object in this exercise. It did not say that two rows are every booking in the building. Those are separate claims. The first claim is about authority. The second would be about completeness, and the owner has not made it.

Search the page by the pair the resident asked for. Room and start must both match. `SYN-001` matches Room 2 at 14:00, so that slot is taken for its own question. It does not answer Room 4. `SYN-002` matches Room 2 at 15:00. It also does not answer Room 4. After both rows are checked, the matching count for Room 4 at 15:00 is zero. Zero matches is silence. Silence supports neither "taken" nor "free."

The spoken reply is therefore limited: "This page does not list Room 4 at 15:00, so I cannot answer from it." Staff record the request as pending. They do not offer the room.

### 12.2 Worked example

A classmate treats the old ALLOW label as if it were the missing row. In **Chapter 4's fixed four-action log**, ALLOW classified the **11:45 mark-pending** proposal; no Room 4 confirmation was logged. A separate Chapter 4 counterfactual explains that changing the 11:42 room input to Room 4 could instead produce ALLOW under the tiny synthetic table, but it was **not executed as the published run** and would not prove vacancy. The 11:40 page is a second artifact. It contains neither a Room 4 row nor any ALLOW verdict. Transplanting that label would invent evidence the printer never produced.

| Proposal | What the two rows support | Decision |
|---|---|---|
| "Room 4 at 15:00 is absent, so offer it as free." | Zero matching rows | Refuse. Absence is silence |
| "Chapter 4 printed ALLOW, so the 11:40 page confirms Room 4." | ALLOW belongs to the 09:00 log | Leave that label where it was printed |
| "Add Room 4 by hand so the page becomes complete." | The page would no longer be the printed object | Refuse. That mark is an alteration |
| "Room 2 at 15:00 must also be reopened, because Room 4 is unclear." | `SYN-002` still matches Room 2 at 15:00 | Keep the taken reading for that pair |
| "Look the gap up on the live booking site." | The exercise supplied this page only | Stop. The site stays outside the exercise |

The note to keep is a count. Rows on the page: 2. Rows matching Room 4 at 15:00: 0. Result for that question: pending. Result for Room 2 at 15:00: still taken, from `SYN-002`. Census of the old log: unchanged.

### 12.3 What silence still leaves open

A pending Room 4 request is not a hidden booking. The page did not show a conflict, and it also did not show a vacancy. Another source, named later and checked for a Room 4 row, would be a new exercise. This lesson does not provide that source. It also does not explain the outage, and it does not measure how often a real desk prints a partial fallback.

The Chapter 4 program stays closed. Its census remains a description of the four logged actions against the 09:00 printout. A question asked of the 11:40 page is not a fifth action in that log, so it cannot change ALLOW, REFUSE, or UNKNOWN.


### 12.4 Source completeness is a separate claim from source approval

An **approved source** is one an authorized owner has named for a particular question and context. A **complete source for a query** contains all relevant records within a defined scope and cutoff, with trustworthy retrieval and update behavior. **Availability** is a property of a slot under that complete and sufficiently current state. **Transaction authorization** permits an identified actor or procedure to create, change or confirm a booking. None of those terms can substitute for another.

The new 11:40 page has a **positive matching row** for Room 2 at 15:00, so the Chapter 11 statement “already booked” follows from its printed evidence **for this sitting**. Room 4 at 15:00 is different: there is **no matching row**. That gives the learner exactly one narrow observation: “No Room 4 / 15:00 entry appears on the two displayed rows.” It does **not** prove the page contains every booking for every room, or that a separate operational booking step succeeded or is allowed.

A useful distinction is **open-world versus closed-world inference**. Under an *explicitly established* closed-world rule for a complete and current dataset, a missing record may support a narrowly scoped absence conclusion. Under an *open-world* or incompletely characterized source—like this two-row classroom page—absence of a matching record is **not evidence of absence from the entire reservation system**. We do not claim the real application uses either database semantics. The teaching problem is that the exercise never supplied an approved completeness statement or synchronization guarantee for **Room 4 at 15:00**.

The [NIST CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29) distinguishes asset/data management and authorized access outcomes, while [NIST SP 800-53 Rev. 5, AC-3 (Access Enforcement)](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) frames enforcement of approved authorizations. These primary standards support treating data-management evidence and permission to act as different control questions; they **do not** certify this synthetic page as complete or establish Harbor Library's booking rules.

### 12.5 A precise predicate for an offer, not a guess

Before a worker could responsibly say “Room 4 is available to book,” the owner would need to define the exact question and the required evidence. In this classroom the prerequisites can be written conceptually (this is **not executable code**):

**Sufficient current scope** AND **no conflicting reservation in that scope** AND **authorization to offer or hold the slot**.

A confirmed transaction would need a **separate authorized booking operation and reliable outcome evidence**. The three prerequisites are not asserted as already satisfied. The original two-row page does **not** establish the first; therefore even a zero-match scan is insufficient. In addition, having a current view with no conflict would not by itself prove the booking was committed or that the owner granted transaction rights.

| Question | Room 2 / 15:00 | Room 4 / 15:00 |
|---|---|---|
| Source named for this sitting? | Yes, the specific 11:40 page | Same page, same limited naming |
| Printed matching row? | Yes: `SYN-002` | No: **zero** of the two rows |
| Conclusion supported directly by this page | The page records a confirmed booking for that slot | Only “no matching row on this page” |
| Can “free” or “offer” be asserted? | **No**: the row contradicts vacancy | **No**: relevant source completeness and transaction permission are not supplied |
| Resident-facing decision | “Room 2 at 15:00 is booked.” | “This page does not establish Room 4's availability; I can record the request as pending.” |

This is an **asymmetric evidence problem**. A positive conflicting booking on the owner-named page provides direct evidence that the slot is taken for the bounded question; a missing row cannot prove a universal negative without evidence that the page covers the entire relevant state. The exercise does not infer that the page is always correct in every real-world circumstance: a future contradictory authorized record would require renewed review, not concealment. In this sitting the positive record is sufficient for the limited “taken” reply the owner defined.

### 12.6 Worked contrasting cases and negative controls

**Case A — the actual two-row page.** Match by both fields: Room 4 **and** 15:00. `SYN-001` is Room 2 / 14:00, so it fails room and time; `SYN-002` is Room 2 / 15:00, so it fails room. Total rows = 2; relevant matches = 0. The result is **no answer about Room 4 availability**, so the request remains pending. Separately, the same page does show Room 2 / 15:00 as booked. No row or outcome was added.

**Case B — hypothetical completeness certification (not issued here).** Imagine the owner later provides a separately authorized source and a verified assurance that it contains every active booking for Room 4 at the relevant date and 15:00 cutoff. If that source shows no conflicting row, the narrow **absence of a conflict in that verified scope** becomes supportable. It still does **not** create or confirm a reservation. This is a conditional inference only: no such certification or later artifact has been supplied in Chapter 12.

**Case C — hypothetical missing synchronization receipt.** Imagine that a purported later page says “complete” but there is no evidence of its cutoff or refresh behavior. A heading is not a completeness test. Keep the request pending. No inferred database defect or real operational outage is declared.

**Negative control 1 — wrong-room substitution.** Copying the `SYN-002` Room 2 / 15:00 row into the Room 4 question is wrong: matching the requested start without matching the room does not establish a Room 4 booking. Conversely, `SYN-001` at 14:00 cannot decide a 15:00 slot merely because it is on the same page.

**Negative control 2 — relabel the prior ALLOW.** Chapter 4's fixed four-action result says **ALLOW** for the **11:45 mark-pending** proposal. Chapter 4 also mentioned a distinct hypothetical Room 4 input substitution that *could* return ALLOW under its narrow fixture rule. Neither ALLOW is a new Room 4 reservation or a fresh 11:40 printout row. The published tally remains **STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0**.

**Negative control 3 — manufacture completeness.** Handwriting an invented Room 4 row or typing an altered printout time into the old script changes the evidence or fixture. It does not verify the original page or create booking authority. The prohibited live-site check is still outside the safe exercise scope.

### 12.7 Evidence ledger and a decision another learner can challenge

Use a five-line ledger for the Room 4 question:

| Field | Entry permitted by the released case |
|---|---|
| **Question** | Is Room 4 available at 15:00 during this sitting? |
| **Source** | Owner-named synthetic 11:40 page, limited to this sitting |
| **Observed match** | Two printed rows, zero matching Room 4 / 15:00 |
| **Unknown** | Whether the page covers every relevant Room 4 booking and whether any offer/transaction is authorized |
| **Decision** | Do not offer the slot. Record the request as **pending** and ask for an approved current and sufficiently complete source and the authorized booking step |

The field **Observed match = 0** is not a vacancy result. This ledger separates *query result* (zero in the inspected subset) from *source coverage* (not established), *business state* (not proven) and *permitted operation* (not approved). If a later source disagrees, preserve this original note as the evidence held at this checkpoint; a different result belongs to a versioned new decision, not to silent alteration of the first artifact.

A false positive for the assessment is a learner who says "Room 4 is free" because the page has zero Room 4 rows. A false negative is a learner who declines to say that Room 2 / 15:00 is **already booked** despite directly inspecting the named `SYN-002` row. The goal is neither indiscriminate refusal nor unjustified certainty: it is the strongest **supported** bounded decision for each exact room/time pair.

### 12.8 Independent EX028 exercise extension

Complete EX028's original four sentences independently before reading [its worked answer](#answer-ex028). Then produce a small four-column comparison—**row count**, **scope/freshness established?**, **slot state supported**, **transaction allowed?**—for Room 2 / 15:00 and Room 4 / 15:00. Specify why the owner naming one page does not establish completeness for Room 4 and why the historical classifier's ALLOW is not an authorization to create a room booking. Finally, evaluate the hypothetical completeness-certification branch from Section 12.6: what **additional** evidence would be necessary, and what business action remains separate even if no conflicting row is shown?

The falsifier is a promise of Room 4 based only on missing rows, a claim that a new booking was executed, an overwrite of the Chapter 4 line, or a claim that Room 2 was freed. This is a paper exercise with no live checks, real patrons or new case observations.

### Chapter 12 summary

On this named page, a question is decided only when a printed row matches its room and its start. Room 4 at 15:00 has no such row. The page is silent, the request stays pending, and the older ALLOW label is not a substitute row.

### Chapter 12 exercises

### EX028 — Do not offer the room the page omits

- **Objective:** Keep a missing row from becoming an offer of a free room.
- **Input:** A classmate says, "Room 4 is not on the approved 11:40 page, so tell the resident it is free at 15:00 and turn ALLOW into that confirmation."
- **Safe condition:** Stay with the two printed rows. Do not write a new row onto the page, and do not launch the booking program again.
- **Task:** Write four sentences: how many rows match Room 4 at 15:00, what you tell the resident, what you do with the ALLOW label, and what remains true of Room 2 at 15:00.
- **Expected evidence:** Four sentences a reader can check against the two-row page and against the Chapter 4 census.
- **Rubric:** Credit when the Room 4 request stays pending, ALLOW stays on the old log, the census is not rewritten, and `SYN-002` still makes Room 2 at 15:00 taken. An offer of a free room does not earn credit.

- **Independent extension:** Supply a two-row comparison of Room 2 / 15:00 and Room 4 / 15:00: match count, what the page positively establishes, what **completeness** is missing, and whether a new transaction was authorized. Name what a hypothetical fully scoped later source could establish **without** treating it as evidence released in this chapter.
- **Negative controls:** Do not turn a zero-match subset into a vacancy, or `ALLOW` from the earlier **11:45 mark-pending** action into a booking. Keep `SYN-002`'s confirmed 15:00 reservation for Room 2 and the earlier tally unchanged.
- **Self-check:** [EX028 worked answer](#answer-ex028).

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 20

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Yesterday's naming does not bind today

### Learning outcomes

After this chapter, you should be able to:

1. Separate a finished exercise's named page from a later outage.
2. Leave today's room request pending when today's owner has not named a source.
3. Keep yesterday's conclusion in yesterday's note.

### 13.1 A naming has a sitting attached

The 11:40 page remains in the exercise folder. Its rows have not been edited. What ended is the sentence that made it the source. That sentence was limited to the sitting in which it was spoken. A new morning, with the booking view described as unavailable at 09:12, is a new decision. The classmate who says "the gates already passed" is quoting a closed exercise.

Until the owner of today's exercise names a source for today, staff have no page they are allowed to read as current. They do not borrow yesterday's speech. They do not tell a resident that Room 2 at 15:00 is taken, and they do not tell the resident it is free. The request is pending. The Chapter 4 census is not a participant in this morning, so it stays printed as it was.

### 13.2 Worked example

| What the classmate relies on | What is actually dated | Decision |
|---|---|---|
| "Both checks passed yesterday." | Those checks belong to the earlier sitting | Do not reuse them |
| "The 11:40 page is still in the folder." | Possession is not today's naming | Leave it filed |
| "Say Room 2 at 15:00 is taken, as before." | No source has been named today | Pending |
| "The 09:00 tally can be cleared because a later page once existed." | The tally describes the old log | Leave the line |

The morning note records 09:12, Room 2, start 15:00, state pending, and the reason "no source named for today." It does not copy a resident's name, and it does not explain the outage.

### 13.3 What this limit does not deny

The earlier page is still a real sheet of the earlier exercise. Filing it is allowed. Reading it as today's authority is not. A later sentence, spoken by today's owner about a named object, would open a different lesson. This chapter does not supply that sentence.


### 13.4 What expires: authority to use a source, not the historical fact

**Source designation** is an authorized owner's decision that a particular record can be used for a particular purpose. In a paper-based exercise that designation needs at least an identifiable **object**, a **decision question**, a **sitting or effective period**, and a person with the authority to make the designation. **Temporal validity** means that the designation still applies when the next decision is made. It differs from a paper's physical survival, a row's historical truth, and the date written in the page heading.

Chapter 11 supplied an owner-named 11:40 sheet for one sitting. Chapter 12 used the same source for another room/time query within that limited context. Both lessons' notes remain true descriptions of the pages they inspected. **At the new morning's 09:12 checkpoint**, the earlier owner naming is no longer an applicable grant for today's booking decision. The page may remain unaltered in the folder while its **authorization for today's purpose is absent**. Nothing in the case says the old page was falsified or that its printed SYN-002 row has disappeared; those would be unsupported additional events.

This distinction separates two clocks: **document time** (11:40 on the earlier sheet) and **authority time** (the period and task for which the owner named it). A document can be preserved indefinitely for audit without being current enough to drive a new booking. Conversely, receiving a newly printed document tomorrow would not automatically give the worker transaction authority. A later decision must use the evidence **available and approved at that later checkpoint**, not a result retrospectively borrowed from a finished sitting.

| Claim about the earlier artifact | Supported at the new 09:12 morning? | Why |
|---|---|---|
| "The 11:40 sheet was named for the earlier sitting." | Yes, as historical classroom evidence | The earlier owner statement belongs in its own record |
| "The page still has SYN-002 from its previous exercise." | Yes, as an observation about the retained historical paper, if read as a file record | It is not proof of today's reservation state |
| "Its printed 11:40 heading extends the approval until someone removes the page." | No | Possession and printed time are not a renewed authorization |
| "The previous Room 2 / 15:00 result was taken **on that earlier named page**." | Yes, as a time-qualified previous conclusion | It does not answer today's independent question |
| "Today's Room 2 / 15:00 is definitely taken—or definitely free." | No | No source has yet been named for today's decision |

The [NIST CSF 2.0 outcomes GV.RR-02 and PR.AA-05](https://doi.org/10.6028/NIST.CSWP.29) distinguish defined responsibilities and managed permissions. These are general security-governance outcomes, **not** a Harbor Library policy and not proof that a particular real-world library uses time-limited paper permissions. The **per-sitting** restriction is supplied by this fictional exercise. We apply the broader lesson that an old, authorized act does not authorize an unrelated later act without checking its scope.

### 13.5 Mechanism: make the new decision from today's evidence set

To avoid stale authorization, build a small **decision checkpoint**. This is an analytical worksheet, not a software transaction protocol:

1. **Name the requested outcome.** A visitor wants Room 2 at 15:00 on **the new day**. The requested start time is not the time of the intake, the time of a source's printout, or a record that any booking succeeded.
2. **Find an applicable source designation.** The old owner named the old 11:40 sheet for an earlier sitting. Today's owner **has not named** any page in Chapter 13. The first gate is therefore **unmet**, irrespective of what is still in the folder.
3. **Do not infer the current slot from archived data.** The earlier SYN-002 row was confirmed on the previously named sheet; the new day may have a different booking state, but this chapter provides no current rows either way. Do not use the historic result as a prediction.
4. **Record the request, not an allocation.** Retain the four allowed intake fields: **heard 09:12; Room 2; requested start 15:00 today; status not confirmed**. That queue entry says a request exists, not that an authorized reservation has been created.
5. **Ask for a new bounded decision basis.** Today's owner would need to identify the current source, the date and slot it covers, any freshness and completeness requirements, and the procedure for communicating or creating a reservation. Those are **questions**, not responses or checks already performed.
6. **Preserve the older record untouched.** File the earlier page and note with the original approval scope and conclusion. If the situation later changes, create a new dated record of the later evidence rather than correcting the former conclusion to match hindsight.

The result is a deliberately **pending** state. Pending is not “free” and not “taken”; it records uncertainty **for today's decision**. Keeping the original note is equally important: otherwise a reviewer could not distinguish what the learner reasonably concluded yesterday from what later evidence showed.

### 13.6 Worked contrasts: the same words in different contexts

**Earlier sitting, evidence already released:** the named 11:40 page displayed SYN-002 as a confirmed Room 2 / 15:00 booking. For that sitting, the allowed bounded spoken answer was “Room 2 at 15:00 is already booked.” The historical record should retain the owner designation, printed source, source-scoped row and decision. It is not a universal rule about Room 2.

**New morning, before any new naming:** a visitor asks at 09:12 for Room 2 at 15:00 on that day while the front-desk view is described as unavailable. A classmate still has the 11:40 paper in the folder. The proper reply is “I cannot confirm today's Room 2 at 15:00 from the earlier sheet. I will record the request as **not confirmed** until the current exercise owner identifies an approved source.” This answer conveys the current operational limit and next step. It neither denies nor grants the room.

**Hypothetical future authorization, not in Chapter 13:** if today's owner later names a **different** source, that source must be inspected for the actual question before a room-state answer can be derived. Naming alone does not produce a matching row or booking transaction. This possibility is intentionally kept conditional: **Chapter 14**, not Chapter 13, releases the subsequent page.

| Temptation | Negative control | Decision to record |
|---|---|---|
| Reuse the older page because it is physically present | Imagine the owner approval restricted to that closed sitting—as the case explicitly says | Do not treat possession as current authorization |
| Say the old SYN-002 “still proves” today's slot is taken | Ask which dated current source supports today's row; none is named | Withhold both “taken” and “free” |
| Remove yesterday's taken conclusion to avoid contradiction with today's pending note | Compare each record's question/date and evidence cutoff | Preserve **both** as distinct, time-scoped records |
| Say “the earlier program ALLOW means a room may be confirmed” | Identify the actual Chapter 4 ALLOW: **11:45 mark-pending**, not a reservation | Leave the program tally exactly as published |
| Reproduce today's new outage cause from the prior episode | Ask for telemetry or an authorized root-cause assessment; none supplied | Do not attribute cause, attack, or common mechanism |

The last two controls also prevent false history: Chapter 4's synthetic classifier remains **STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0**. That previous four-action census is not a measurement of today's outage, and no new action has been appended to its fixture.

### 13.7 Provenance, handoff and the stop condition

A usable **historical record** should say *which sitting and question*, *what page was named*, *what the row showed*, *what was communicated*, and *what was not proved*. A usable **current pending slip** should contain only the minimal request fields and the state “not confirmed.” The two can coexist without collapsing dates or introducing resident identity data. The previous printed sheet need not be destroyed to remove an authorization it never had for today.

**Worked handoff (fictional):** “Previous sitting: owner-designated 11:40 page showed SYN-002 confirmed for Room 2 / 15:00; earlier result was ‘taken’ for that sitting only. New morning, 09:12: Room 2 / 15:00 today requested while the staff view is unavailable. No source has been named by today's owner; request retained as **not confirmed**. Do not use the earlier page as today's basis. Await owner designation and checked current contents before stating room availability, and a separate authorized process before confirming a reservation.”

This is not a statement that a real outage persisted past 09:12, that a new row was created, or that any person approved a transaction. The **stop condition** is reached whenever applicable source authorization or current evidence is missing: do not promise, release identity data, modify old records or improvise a live-site check. Paper-only role-play keeps the method reproducible and safe.

### 13.8 Practice without looking at the answer key

Complete the three original sentences of **EX029** first. Then independently draw a two-entry ledger titled **earlier sitting** and **new morning**. For each entry specify: source designation, page available, evidence about Room 2 / 15:00, legitimate reply, and status of any actual new booking. Test three counterexamples: (a) the folder still contains the old sheet; (b) a participant repeats yesterday's owner's words today; (c) a printed timestamp resembles today's time of day but is from a different date. Every case must preserve today's **pending** request unless today's authorized source is actually named and checked. No new source is released in this chapter.

Compare your record with [the worked EX029 result](#answer-ex029). The expected distinction is not “yesterday was wrong”; it is **“yesterday's conclusion was scoped to yesterday's evidence, and no equivalent evidence has been released for today.”**

### Chapter 13 summary

A page that was named yesterday answers yesterday. Today's outage waits for today's naming. Until that sentence exists, the room request is pending and the old census stays put.

### Chapter 13 exercises

### EX029 — Leave yesterday in yesterday's note

- **Objective:** Stop a closed naming from governing a new morning.
- **Input:** A classmate says, "The 11:40 page passed both checks yesterday, so confirm today's Room 2 at 15:00 from it and retire the pending slip."
- **Safe condition:** Use the exercise folder only. Do not open a booking site, and do not feed the old page into the Chapter 4 program.
- **Task:** Write three sentences: which sitting the naming belonged to, what today's owner has not yet done, and the state of today's request.
- **Expected evidence:** Three sentences a reader can check against the two dates.
- **Rubric:** Credit when yesterday's page stays an earlier artifact, today's request stays pending, and the census is untouched. Confirming the room from the old page does not earn credit.

- **Independent extension:** Write an earlier-sitting versus new-morning provenance table with the applicable owner naming, document date/time, Room 2 / 15:00 evidence, permitted reply and unresolved booking action. Explain why the old paper is still useful as an archive but not as today's approved schedule.
- **Negative controls:** Possession of the 11:40 sheet, repeated words of yesterday's owner, and similar clock times cannot create today's source designation. Keep today's 09:12 request **not confirmed** and the Chapter 4 tally intact.
- **Check your reasoning:** [EX029 worked result](#answer-ex029).

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue studying — chapter 13 of 20

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — A new page answers only its own rows

### Learning outcomes

After this chapter, you should be able to:

1. Apply today's naming to the 11:55 page and to no other object.
2. Read `SYN-003` as a taken Room 4 at 15:00, without offering a person's name.
3. Leave yesterday's pending conclusion and the Chapter 4 census in their own records.

### 14.1 Today's source is a different object

Today's owner now names one synthetic page, headed 11:55, for this exercise only. You check the heading on the paper and you find three printed rows. `SYN-003` is the new row: Room 4, start 15:00, created 11:20, status confirmed. That pair matches a resident who asks for Room 4 at 15:00. Staff say the slot is taken. The identifier is not a person, and no personal name is printed, so none is spoken.

`SYN-002` is also on this page, so Room 2 at 15:00 is taken here as well. Chapter 12's silence applied to a page that had no Room 4 row. This page has the row. The earlier silence is not a veto over a later, named object. It also is not erased from the earlier note. Two sittings can hold two different facts about what their own pages showed.

The 09:00 program is not given `SYN-003`. ALLOW remains a label on that old log. This sitting does not rewrite it into a confirmation or into a refusal.

### 14.2 Worked example

| Question in this sitting | Row on the 11:55 page | Speech |
|---|---|---|
| Room 4 at 15:00 | `SYN-003`, confirmed | Taken. No name |
| Room 2 at 15:00 | `SYN-002`, confirmed | Taken. No name |
| Room 4 at 16:00 | No row | Pending. The page is silent |
| "Clear ALLOW because Room 4 is now listed." | ALLOW is not a row on this page | Refuse the edit |

The 11:40 page stays in the folder as yesterday's artifact. It is not consulted for these answers, because today's owner did not name it.

### 14.3 Limits of the third row

`SYN-003` is an invented booking for this lesson. It does not show that a real library created a reservation at 11:20, and it does not show why the booking view was unavailable. The naming expires when this exercise ends. A month-long rule of "trust 11:55" is not on the page.


### 14.4 A new naming changes the evidence available now, not what happened before

**Current source designation** is the owner's identification of one artifact for a defined sitting and purpose. **Relevant evidence** is what that artifact says about the precise room-and-start query. **Disclosure authority** controls what may be communicated to the visitor; **transaction authority** controls whether anyone may create or modify a reservation. Passing the source designation and reading a row is **not** proof of a new booking operation.

Chapter 13 stopped at 09:12 with **no source named for the new day**, so today's Room 2 / 15:00 request remained not confirmed. **Only in Chapter 14** does today's owner identify a separate synthetic sheet headed **11:55** for this exercise. The sheet carries three rows; the released facts relevant here include **SYN-003 — Room 4, 15:00, created 11:20, confirmed** and **SYN-002 — Room 2, 15:00, confirmed**. Those details are **on the new page**, not added to the old 11:40 sheet. The 11:55 heading is a page attribute; without additional receipts, it does not prove a real-world database sync, printing path, or when any real server operation occurred.

That is a change in the learner's **knowledge and permitted source**, not a retroactive correction to Chapter 12's accurate observation that the earlier **two-row 11:40 page** contained **no Room 4 / 15:00 row**. These records have different objects and decision checkpoints. Preserving both is not contradictory: the earlier note describes the earlier page; the later note describes the newer page.

[NIST CSF 2.0, PR.AA-05 and PR.DS-01](https://doi.org/10.6028/NIST.CSWP.29) address managed authorizations and confidentiality, integrity and availability of stored data. The **page naming, row matching and time-scoped decision rule are synthetic teaching procedures**, not a NIST-prescribed library workflow or evidence of deployed controls.

### 14.5 Mechanism: evaluate each exact question against this artifact

Do not start with a desired answer. Use a short chain that a second learner can inspect:

1. **Select the approved object.** The owner names this specific 11:55 page **for this sitting**. The previously named 11:40 page is an archived source from an earlier exercise, not today's substitute.
2. **State the query exactly.** A room-and-start pair is required; 15:00 and 16:00 are different questions, as are Room 2 and Room 4.
3. **Read matching fields and status.** For Room 4 / 15:00 the new page directly contains **SYN-003**, status **confirmed**. For Room 2 / 15:00 it contains **SYN-002**, also confirmed. Two supported positive matches indicate that **each corresponding slot is already booked on this page**.
4. **Do not invert a positive match.** Reading a confirmed reservation supports “taken,” never “free.” Passing the source-identification gate is not a requester's authorization to take a room.
5. **Treat a missing matching row separately.** The three-row page has **no Room 4 / 16:00 match**. No completeness guarantee for that separate slot was supplied, so the strongest honest statement is “not shown on this sheet,” not “available.”
6. **Communicate minimally.** Give the room-state answer where supported. There is no person's name on the synthetic page; neither **SYN-003** nor **SYN-002** is a resident's name, and no identity should be invented or disclosed.
7. **Keep historical outputs and transaction boundaries.** The earlier pending status, older page observations and Chapter 4's fixed four-action tally stay in their own records. None is rewritten, and no new booking is executed in this lesson.

The **positive-match/absence asymmetry** is central. A matching, owner-named, confirmed row supplies direct evidence of an existing reservation for the named context. A zero-match result supplies only a claim about what was searched in the visible subset. To infer a slot is free from absence, the owner would first have to establish completeness and currentness for that slot **and** the relevant booking rules; an authorized transaction would still be a different step.

### 14.6 Worked comparison, with chronology preserved

| Query or proposed action | Evidence released in Chapter 14 | Supported answer or decision | Unsupported leap |
|---|---|---|---|
| Room 4 / 15:00 | **SYN-003**, Room 4, 15:00, created 11:20, confirmed | “That slot is already booked.” | Naming an unknown holder or offering the booked room |
| Room 2 / 15:00 | **SYN-002** is also printed as confirmed on the named page | “That slot is already booked.” | Dropping the older row because another booking is newer |
| Room 4 / 16:00 | No matching row on the three-row page | “This page does not establish whether that slot is available; the request is pending.” | Claiming all unlisted times are free |
| “Correct Chapter 12 to show SYN-003.” | Chapter 12 used a different, two-row 11:40 page | Keep Chapter 12's accurate record of **what its page showed** | Backdating the newly released row or pencil-editing the old sheet |
| “Change Chapter 4 ALLOW to REFUSE.” | Chapter 4's ALLOW is the **11:45 mark-pending** action in an older 09:00-based classifier | Preserve **STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0** | A new 11:55 page cannot rewrite a closed four-action run |

**Worked interaction — two booked slots:** A visitor asks to use Room 4 at 15:00. The worker checks the **owner-named 11:55 page**, finds a confirmed **SYN-003** match, and says, “Room 4 at 15:00 is already booked.” Another visitor asks about Room 2 at 15:00. **SYN-002** gives the same *taken* conclusion for that different room. Neither reply names a resident, promises a replacement room, or asserts the worker has opened the live site.

**Contrasting silent query:** Someone asks for Room 4 at 16:00. The learner can state only “There is no Room 4 / 16:00 entry on the three rows shown.” This does not certify the whole reservation system is complete for 16:00 or that a booking is authorized. The request stays **not confirmed** until the source owner supplies the required scope and decision authority. Importing the 15:00 row would substitute the wrong start time.

### 14.7 Test the reasoning with three negative controls

**Control A — remove today's naming.** Imagine someone merely hands the learner the sheet without the designated owner's approval. The **visible** row can be described as text on paper, but the right to use it as today's booking-decision source is not established. The learner must not convert inspection into authority by assertion. In the **actual** case, the owner did name the page; the authorized, bounded *taken* replies for its two confirmed rows stand.

**Control B — hide SYN-003 while retaining the other rows.** In an explicitly hypothetical variant with no Room 4 / 15:00 row, the page would become silent about that pair. The learner may not transfer Room 2's SYN-002 result to Room 4 or claim vacancy based on silence. The actual named page **does** show SYN-003; this control tests dependence on the specific row rather than altering the published facts.

**Control C — change only the requested start to 16:00.** The physical 11:55 page and owner designation are unchanged, but the query has changed. No Room 4 / 16:00 match is supplied, so the result changes from supported *taken at 15:00* to *pending for 16:00*. One authorized source can answer some questions and be silent about others. A named page is not necessarily a complete live booking register.

In all three controls, do not rewrite Chapter 12's historic zero-match note; its subject was the older 11:40 page. Do not rerun or alter Chapter 4's classifier. The exercise does not disclose why the front-desk view was unavailable or prove any real service defect, synchronization success or executed room allocation.

### 14.8 A provenance-preserving handoff

Keep two different records rather than combining them:

| Evidence checkpoint | Source scope and observed item | Defensible statement |
|---|---|---|
| Earlier Chapter 12 sitting | Owner-named **11:40** page with two rows, neither for Room 4 / 15:00 | “No Room 4 / 15:00 row appears on this earlier page; availability not determined; request pending.” |
| Current Chapter 14 sitting | Today's owner names **11:55** page, containing confirmed **SYN-003** for Room 4 / 15:00 and confirmed **SYN-002** for Room 2 / 15:00 | “The current named page shows both listed slots as booked; no person identified.” |

There is no need to delete the earlier pending note. It records what the worker could responsibly say **at that earlier checkpoint**. A later, scope-bound conclusion can supersede a pending **operational answer for its own sitting** without retroactively supplying data that the prior sheet did not contain. Keep the old page unchanged so another learner can verify this distinction. A comparison note is not a third printed schedule or an authorization to make one.

### 14.9 Independent EX030 practice and limits

Before opening [the EX030 worked result](#answer-ex030), write the original three sentences: identify the page named **today**, report the **SYN-003** evidence for Room 4 / 15:00, and name the **two historical records** that must remain intact (the Chapter 12 earlier-page note and Chapter 4 classifier output). Then independently fill a three-row decision table for **Room 4 / 15:00**, **Room 2 / 15:00**, and **Room 4 / 16:00** with columns **source**, **matching row**, **room-state statement**, and **what remains unauthorized or unknown**.

Check whether your answer would change incorrectly if you erased yesterday's note, relabeled the fixed ALLOW, inferred a resident from SYN-003, or treated a 16:00 omission as proof of availability. A correct answer preserves the original exercise narrative, acknowledges the later release **only here**, and never claims a real booking, incident diagnosis, or site check occurred.

### Chapter 14 summary

When today's owner names the 11:55 page, Room 4 at 15:00 is taken because `SYN-003` is printed there. That reading does not rewrite yesterday's note or the 09:00 census.

### Chapter 14 exercises

### EX030 — Read the row this page actually has

- **Objective:** Accept a new named page without dragging an older silence or an older label onto it.
- **Input:** A classmate says, "Chapter 12 left Room 4 pending, so `SYN-003` cannot count. Keep the room free and clear ALLOW."
- **Safe condition:** Read the 11:55 page named for this exercise. Do not alter the 11:40 page, and do not start the Chapter 4 program.
- **Task:** Write three sentences: which page is named today, what `SYN-003` shows, and which two records you refuse to edit.
- **Expected evidence:** Three sentences a reader can check against the three-row page.
- **Rubric:** Credit when Room 4 at 15:00 is taken from `SYN-003`, no name is added, yesterday's note is left as yesterday's, and ALLOW stays on the old log.

- **Independent extension:** Compare the three queries on the named 11:55 page: Room 4 / 15:00, Room 2 / 15:00, and Room 4 / 16:00. Record matching row, supported state, disclosure limit, and next decision for any unproven availability. Separately state why the earlier pending record and the original classifier output remain valid historical evidence.
- **Negative controls:** No new source in Chapter 13, no invented resident name from SYN-003, no confirmed 16:00 availability from missing rows, no alteration to 11:40 paper, and no changed historical ALLOW.
- **Check your reasoning:** [EX030 worked result](#answer-ex030).

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue studying — chapter 14 of 20

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Two pages are not one schedule

### Learning outcomes

After this chapter, you should be able to:

1. Choose the named page rather than a blend of pages.
2. Refuse a pencil copy of `SYN-003` onto the 11:40 page.
3. Keep every row of the named page, including rows an older page also showed.

### 15.1 A schedule is the page in front of you

Staff sometimes want the "best" row from each sheet. That wish builds a third schedule. No printer produced it, and the owner did not name it. In this exercise the owner named the 11:55 page. Its three rows stand together. Dropping `SYN-002` because the older page was handled first would hide a row the named page prints. Copying `SYN-003` onto the 11:40 page would change an artifact whose job is to show what yesterday's sheet contained.

The comparison between the pages can be written beside them: the later page adds `SYN-003`; both print `SYN-002`. The comparison is a note. It is not a new master sheet.

### 15.2 Worked example

| Proposed blend | Object that would result | Decision |
|---|---|---|
| Glue `SYN-003` onto the 11:40 page | An altered earlier page | Refuse |
| Drop `SYN-002` and keep only the new row | A partial named page | Refuse |
| Answer from the 11:55 page as printed | The named object | Accept |
| Throw out the 11:40 page so only one sheet remains | A missing earlier record | Refuse. File it |

Room 4 at 15:00 is taken because the named page says so. Room 2 at 15:00 is taken for the same reason. The census of the 09:00 log is not a row in either blend, so it is not updated to match the blend someone wished for.

### 15.3 What a comparison may still say

A facilitator may write that the pages differ by one row. That sentence does not choose a room, does not name a person, and does not declare a cause. The next chapter looks at a different temptation: deleting a printed row because of the clock inside it.

### Chapter 15 summary

Use the page this exercise named, with all of its rows. Do not manufacture a schedule by moving lines between sheets.

### Chapter 15 exercises

### EX031 — Stop the blended schedule

- **Objective:** Keep two artifacts from being merged into a third.
- **Input:** A classmate says, "Copy `SYN-003` onto the 11:40 page, cross out `SYN-002` on the 11:55 page, and answer from the result."
- **Safe condition:** Handle paper already in the exercise. Do not add a line to either page.
- **Task:** Name the page you will read, the two edits you will not make, and the two 15:00 answers those pages' named sheet already supports.
- **Expected evidence:** A short note a reader can check against both pages.
- **Rubric:** Credit when the 11:55 page is read whole, both older and newer sheets stay unmarked, and both 15:00 slots that the named page lists are treated as taken.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue studying — chapter 15 of 20

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — A created time does not erase a printed row

### Learning outcomes

After this chapter, you should be able to:

1. Read a created time as the booking's time and a heading as the page's time.
2. Keep a printed row when its created time is earlier than the page heading.
3. Refuse to push that created time into the finished 09:00 run.

### 16.1 Two clocks, one row

`SYN-003` carries created time 11:20. The page heading is 11:55. A classmate argues that a booking made at 11:20 is "already old" by 11:55 and should be ignored, and also that the same booking is "after 09:00" and should be inserted into the Chapter 4 log so ALLOW becomes REFUSE. Both moves misuse a clock.

The heading says when this sheet presents itself. A row created earlier can still be on a later sheet. That is ordinary. Ignoring the row would pretend the printer left it off. Inserting 11:20 into the 09:00 program would pretend that program had seen `SYN-003`. The published run did not. Its census stays `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`.

On the named 11:55 page, Room 4 at 15:00 remains taken.

### 16.2 Worked example

| Claim about 11:20 | Clock it confuses | Decision |
|---|---|---|
| "11:20 is before 11:55, so drop `SYN-003`." | Created time with page heading | Keep the row |
| "11:20 is after 09:00, so rerun the log." | Created time with an older program | Do not rerun |
| "The heading is later, so the whole page is stale." | A heading is not a verdict by itself | The owner still named this page |
| "Change ALLOW to REFUSE on paper." | A label from another artifact | Leave the label |

The useful line is: created 11:20, page 11:55, row present, slot taken, old log unchanged.

### 16.3 What the clocks still do not show

Nothing in the two times explains the unavailable booking view. Nothing in them measures how often a desk prints. The next chapter asks what a repeated row can prove, which is a smaller claim than a cause.

### Chapter 16 summary

A created time locates a booking. A heading locates a page. A printed row stays printed. The finished 09:00 census is not rewritten to match a clock from a later sheet.

### Chapter 16 exercises

### EX032 — Keep the row the clock was used to attack

- **Objective:** Stop a created time from deleting `SYN-003` or from reopening the old program.
- **Input:** A classmate says, "`SYN-003` at 11:20 is both too old for the 11:55 page and late enough to flip ALLOW to REFUSE."
- **Safe condition:** Compare the clocks on paper. Do not type a time into the booking program.
- **Task:** State what each clock means, whether the row stays, and what happens to ALLOW.
- **Expected evidence:** Three statements a reader can check against `SYN-003` and the published census.
- **Rubric:** Credit when the row stays, Room 4 at 15:00 stays taken on the named page, and ALLOW is not rewritten.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue studying — chapter 16 of 20

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Matching rows are not a cause

### Learning outcomes

After this chapter, you should be able to:

1. State the limited fact when the same synthetic row is on two pages.
2. Refuse to promote that fact into an attack, a vulnerability, or an incident.
3. Leave Chapter 8's class, a weak confirmation procedure, where it was.

### 17.1 What the repeat can carry

Put the 11:40 page beside the 11:55 page. `SYN-002` is on both, with the same room, start, created time, and confirmed status. The careful sentence is that this exercise printed that row on two later sheets. The 11:55 page also has `SYN-003`, which the earlier sheet lacks. Sameness and difference can both be listed. Neither list contains a cause for the unavailable view.

Chapter 8 already refused to call the stale-paper habit a proven software weakness or an incident. A second copy of `SYN-002` does not add the missing demonstration. It does not add an owner's incident declaration. A classmate's word "attack" is a new claim with no new evidence. A classmate's word "safe," drawn from the match, is the opposite overclaim. Matching rows do not measure harm or likelihood, so they also do not revive the score rejected in Chapter 9.

### 17.2 Worked example

| Sentence offered for the pair of pages | Evidence it would need | Decision |
|---|---|---|
| "Both later pages show `SYN-002` for Room 2 at 15:00." | The two sheets | Keep |
| "The match shows the outage was an attack." | A demonstrated hostile action | Reject |
| "The match shows a vulnerability in the booking site." | A demonstrated weakness | Reject |
| "The match shows the library is safe." | An evaluation this exercise did not perform | Reject |
| "Raise the tally's UNKNOWN, because the cause is unknown." | UNKNOWN counts unmatched log actions | Reject. The cause was never one of the four actions |

The class of the exercise problem stays a weak confirmation procedure. The census stays the census of the 09:00 log.

### 17.3 The open cause

Staff can still write "cause not established" under the comparison. That phrase blocks a false ending. It does not assign blame, and it does not authorize a live investigation. The following chapter is about whether the older sheets may be destroyed once a newer sheet exists.

### Chapter 17 summary

Two pages that share `SYN-002` support that shared row and nothing causal. The outage stays unexplained. The older labels of procedure, tally, and score stay in their earlier lessons.

### Chapter 17 exercises

### EX033 — Take the diagnosis off the matching row

- **Objective:** Keep a repeated synthetic row from becoming an attack story or a safety claim.
- **Input:** A classmate writes, "The pages agree on `SYN-002`, therefore the outage was an attack and the exercise can close as safe."
- **Safe condition:** Compare the two synthetic pages. Do not investigate a real site.
- **Task:** Replace the note with the fact the pages support, the two claims you reject, and the class Chapter 8 already allowed.
- **Expected evidence:** Four sentences a reader can check against the pages and Chapters 8 and 9.
- **Rubric:** Credit when the shared row is stated, attack and safety are both refused, the procedure class is unchanged, and the census is unchanged.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue studying — chapter 17 of 20

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Earlier pages stay in the file

### Learning outcomes

After this chapter, you should be able to:

1. File the 09:00 printout, the 11:40 page, and the 11:55 page as separate copies.
2. Explain which comparison is lost if an earlier copy is destroyed.
3. Keep answering the current exercise from the page named for it.

### 18.1 Newer does not mean solitary

A later page can be the one this exercise named. That role does not make the earlier pages garbage. The 09:00 printout is the artifact the published program read. If it disappears, a reader can no longer see why the 11:42 confirmation was refused. The 11:40 page is the artifact that lacked `SYN-003`. If it disappears, yesterday's silence becomes a story instead of a sheet. The 11:55 page remains the named source for the current room answers.

Filing means three labels: time, what the owner did or did not say about each, and a pointer such as "do not merge." Overwriting the 09:00 printout with 11:55 rows would be the same kind of damage as the pencil mark in Chapter 6, done with a whole page instead of a line.

### 18.2 Worked example

| Proposed cleanup | Comparison that would vanish | Decision |
|---|---|---|
| Shred the 09:00 printout | The recorded run's input | Keep and label |
| Shred the 11:40 page | Yesterday's missing Room 4 row | Keep and label |
| Replace both with the 11:55 page | The history of what each sheet showed | Refuse |
| Answer Room 4 from the named 11:55 page while the others stay filed | None | Accept |

No cleanup step reruns the program. The census remains the census of the log that already ran.

### 18.3 Not a retention policy for a real library

This chapter does not set how long Harbor Library, or any real library, must keep paper. It does not cite a statute. The rule is local to the exercise: do not destroy the sheets the reasoning depends on. A real schedule would be an owner's decision with its own authority. That decision is not in the folder.

### Chapter 18 summary

Keep the three sheets, labeled and separate. Use the one named for this exercise when you answer a room. Do not shred or overwrite the others to make the folder look simple.

### Chapter 18 exercises

### EX034 — Stop the cleanup

- **Objective:** Preserve the sheets that make the earlier decisions checkable.
- **Input:** A classmate says, "The 11:55 page is newest. Shred the 09:00 printout and the 11:40 page so the file has one truth."
- **Safe condition:** Stay inside the synthetic folder. Do not destroy or mark any sheet.
- **Task:** For each sheet, give its role and say whether it stays. Then name the sheet you would actually read for Room 4 at 15:00 in this exercise.
- **Expected evidence:** Four short lines a reader can match to the three times.
- **Rubric:** Credit when all three sheets stay, their roles differ, the 11:55 page is the one read for the current Room 4 question, and the census is not rerun.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue studying — chapter 18 of 20

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — A booking page does not open the contact list

### Learning outcomes

After this chapter, you should be able to:

1. Keep a named booking page inside booking questions.
2. Leave event contacts outside that page's authority.
3. Refuse to add names so that an out-of-scope message can be sent.

### 19.1 The boundary does not follow the newest sheet

The 11:43 action asked for event contacts and received OUT OF SCOPE, because those contacts are not part of the room decision. A classmate now says the 11:55 page is current, so the export has become allowed, and staff should tell the contact list that rooms changed. The page contains booking rows. It does not contain the contact list, a permission to export it, or a reason to attach personal names.

Today's naming selects which booking sheet may be read. It does not redraw the exercise boundary from Chapter 2 and Chapter 4. Contacts stay outside. Staff do not open an export, live or invented, and they do not write names onto `SYN-003` in order to have someone to notify.

Room answers already made from the named page remain: Room 2 at 15:00 taken, Room 4 at 15:00 taken, no names spoken.

### 19.2 Worked example

| Request after the 11:55 naming | Relation to the named page | Decision |
|---|---|---|
| "Is Room 4 at 15:00 taken?" | Matches `SYN-003` | Taken. No name |
| "Export the event contacts." | Different collection | Out of scope |
| "Add a name to `SYN-003` so we can call them." | The page has no name field | Refuse the addition |
| "The new page cancels the 11:43 label." | The label described a different question | Keep OUT OF SCOPE on that action |

The tally is still the four-action census. This request is not a fifth logged line, so UNKNOWN does not move.

### 19.3 Notification can be a real job, under a different authority

A library might someday have a lawful way to tell a patron about a room. This exercise does not provide that way. Wanting to be helpful does not move contacts into the booking sheet. The owner would have to name a different activity, with its own limit. Until then, the contact path stays closed.

### Chapter 19 summary

Naming the 11:55 page authorizes reading its booking rows. It does not authorize an event-contact export or a name written onto a row.

### Chapter 19 exercises

### EX035 — Keep the contacts outside

- **Objective:** Stop a new booking page from being treated as permission to export contacts.
- **Input:** A classmate says, "The 11:55 page is the approved source, so export the event contacts and add the matching names to `SYN-002` and `SYN-003`."
- **Safe condition:** Stay with the synthetic booking rows. Do not create a contact list or open a site.
- **Task:** Separate the room answers you may give from the export you may not, and say what happens to the 11:43 label.
- **Expected evidence:** A short split note.
- **Rubric:** Credit when the two 15:00 slots stay taken without names, the export stays out of scope, no name is written on a row, and the census stays as printed.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue studying — chapter 19 of 20

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — The note that can leave the room

### Learning outcomes

After this chapter, you should be able to:

1. Assemble one checkable note from the sheets and the unchanged census.
2. Include the open questions instead of closing the exercise.
3. Reject security, safety, blame, and a standing clock rule as sentences this folder cannot support.

### 20.1 What belongs in the note

A facilitator should be able to test the note without trusting the writer's tone. The note names the three sheets and says which one today's owner named. It answers Room 2 at 15:00 and Room 4 at 15:00 from that named page, with the booking identifiers and without personal names. It quotes the Chapter 4 census as unchanged. It lists what remains unknown: the cause of the unavailable view, whether any real desk reprints a fallback on a particular clock, and the fact that another outage will need its own naming.

Sentences that do not belong: "the library is secure," "the room is free," "the resident is named," "11:55 is the rule for this month," "ALLOW was cleared," "the outage was an attack." Each of those fails against a sheet or against the log.

Meeting the rapid course's planning count of 20 lessons does not close those questions, and it does not award a qualification. Review of sources, language, and technical accuracy remains open.

### 20.2 Worked example

| Line proposed for the leaving note | Check | Keep? |
|---|---|---|
| "11:55 page named for this exercise; three rows." | The naming and the page | Yes |
| "Room 4 at 15:00 taken, `SYN-003`, no name." | That row | Yes |
| "Census unchanged." | The printed line | Yes |
| "Cause not established." | No cause is on any sheet | Yes |
| "Harbor risk is low and the exercise is closed." | No scale and no closure condition | No |
| "Use 11:55 whenever the site fails." | The naming was for this exercise | No |

The note can leave the room. The case cannot be declared finished.

### 20.3 What the twentieth lesson does not finish

Another outage, a real retention rule, or a contact procedure would be further teaching if an owner defined them. They are not implied by reaching lesson 20. Other languages of this course are not published by this English note. Information security is a separate book. Read it when you mean to study that book, not as a substitute for an unanswered Harbor question.

### Chapter 20 summary

The leaving note lists the named sheet, the taken slots, the untouched census, and the open questions. It does not close the case, name a person, free a room, or convert this exercise into a standing rule.

### Chapter 20 exercises

### EX036 — Cut the closing sentence

- **Objective:** Produce a note that a facilitator can check, including what is still open.
- **Input:** A classmate's closing lines say, "All twenty lessons are done, so Harbor is secure, Room 4 is free after all, and 11:55 will be the fallback every morning this month."
- **Safe condition:** Use the synthetic folder and the printed census. Do not add a new sheet or open a site.
- **Task:** Replace that ending with the sheet you rely on, the two 15:00 answers, the census, and one question the folder still cannot answer.
- **Expected evidence:** Five checkable lines.
- **Rubric:** Credit when both named-page slots stay taken, the census is quoted unchanged, at least one real open question remains, and the security claim, the free room, and the monthly rule are all gone. Declaring the book finished does not earn credit.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue studying — chapter 20 of 20

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

## References and source notes

- [NIST, Cybersecurity Framework 2.0 FAQ](https://www.nist.gov/cyberframework/faqs) — six functions and their continuous, outcome-oriented use. Accessed 11 October 2026.
- [NIST CSRC glossary, “threat”](https://csrc.nist.gov/glossary/term/threat) — terminology source. Accessed 11 October 2026.
- [NIST CSRC glossary, “vulnerability”](https://csrc.nist.gov/glossary/term/vulnerability) — terminology source. Accessed 11 October 2026.
- [CISA, Secure Our World](https://www.cisa.gov/secure-our-world) — practical personal security starting actions. Accessed 11 October 2026.
- [NIST SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final) — planning and assessment context. Accessed 11 October 2026.
- [NIST CSRC glossary, “Rules of Engagement”](https://csrc.nist.gov/glossary/term/Rules_of_Engagement) — pre-agreed testing boundaries. Accessed 11 October 2026.
- [NIST, The Cybersecurity Framework 2.0 (NIST CSWP 29)](https://doi.org/10.6028/NIST.CSWP.29) — Asset Management outcomes `ID.AM-01`, `ID.AM-02`, `ID.AM-03`, `ID.AM-04`, `ID.AM-05`, and `ID.AM-07`. Accessed 11 October 2026.
- [OWASP, Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — system-model elements, data flows, and trust boundaries. Accessed 11 October 2026.
- [NIST CSRC glossary, “vulnerability”](https://csrc.nist.gov/glossary/term/vulnerability) — weakness that could be exploited or triggered by a threat source. Accessed 13 October 2026.
- [NIST CSRC glossary, “threat”](https://csrc.nist.gov/glossary/term/threat) — circumstance or event with the potential to harm operations or assets. Accessed 13 October 2026.
- [NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1), through the [CSRC glossary entry for “risk”](https://csrc.nist.gov/glossary/term/risk) — risk as impact together with likelihood. Accessed 13 October 2026. The Harbor tally is not an application of that method.

Harbor Library, its services, event log, and worked decisions are original fictional teaching material. No text or figures from the linked sources are reproduced here. The definitions and framework descriptions are paraphrased and tied to those primary references.

## Final appendix — worked results and assessment notes

These results match EX001–EX036. Equivalent answers earn credit when they keep the same evidence limits. Reaching the 20-lesson minimum is separate from this answer key.

### EX001 — Worked result

The service is room booking and schedule access. Assets include reservation records (information), the booking application (software), and staff sign-in accounts (identity resources). The reservation store and staff sign-in process are dependencies for the staff schedule shown in the sample diagram; their exact design would require verification in a real setting. Reservation records matter to residents because an incorrect or unavailable booking can waste a visit or create a double booking. A response that labels “the internet” as the service without explaining the resident outcome is incomplete.

### EX002 — Worked result

Confidentiality: an unauthorized recipient receives the event contact list; subscribers are affected; check an approved export or delivery record before asserting disclosure. Integrity: a reservation is changed without the resident's request; residents and staff are affected; compare the authoritative record and a change history. Availability: the booking page is unavailable during a reservation window; residents and staff may be affected; check the time, scope, and service monitoring. These are invented scenarios. An answer may use different examples if each property and verification question are clear.

### EX003 — Worked result

(a) is supported by the synthetic record. (b) is unsupported: no cause for the outage is recorded. (c) is a reasonable inference because the printout is older than the booking, but actual wrong allocation is not observed. (d) is unsupported: the contact list does not appear in the event record. The key skill is preserving the boundary between a plausible consequence and a documented event.

### EX004 — Worked result

An acceptable fallback: the front-desk lead owns an outage procedure. When the live schedule has been unavailable for five minutes, staff mark the last printout's time and avoid confirming later bookings from that printout alone. They use an approved, current secondary source if one exists, or record the request and tell the resident that confirmation is pending. In a paper test, add a synthetic booking at 10:05, trigger an outage at 11:30, and check whether staff notice that a 09:00 printout is stale. A failure mode is that the secondary source is also outdated; the owner should verify its update time before relying on it. The precise five-minute trigger is a proposed exercise parameter, not a real policy.

### EX005 — Worked result

Govern: assign an owner for reservation and contact-list decisions. Identify: map the booking service and its dependencies. Protect: restrict staff changes to authorized accounts. Detect: alert a reviewer to unexpected reservation changes. Respond: suspend a confirmed misused account and communicate with the service owner. Recover: restore a trustworthy schedule and verify it with the owner. NIST describes the functions as continuous and concurrent. Mapping one example to each function helps reveal responsibilities; it does not prove that every control works or that risk has vanished.

### EX006 — Worked result

Owner: the fictional library service owner, represented by the instructor. In scope: the two synthetic bookings and an invented 09:00 printout. Excluded: production systems, accounts, and real resident information. Permitted actions: compare records and role-play front-desk decisions. Time: one scheduled 30-minute session. Result recipient: the service owner. An answer that names a real site without specific authorization fails the boundary requirement.

### EX007 — Worked result

Keep booking ID to trace the invented record, room to compare competing use, start time to determine which request matters, created time to test printout staleness, and status to know whether the request is confirmed. Remove resident name and personal phone number: neither is needed for the timing question. A learner may omit status if the scenario clearly says both bookings are confirmed, but should state that assumption.

### EX008 — Worked result

Pause the proposed live check. Record that it was proposed, without opening the site or assigning blame. Ask the designated exercise owner whether a different approved activity is needed. Continue the learning objective offline by using the synthetic booking sheet and printout if the owner confirms that the original exercise remains in scope. An individual's curiosity is not a substitute for the approved boundary.

### EX009 — Worked result

Observation: the 09:00 synthetic printout did not include `SYN-002`, which the sample says was created at 10:05. Interpretation: a static printout could mislead staff about later bookings during an outage. Limitation: the paper exercise did not test the real library or show a breach. Next check: ask the service owner for the approved fallback procedure and test it with a later synthetic booking. The wording keeps the evidence and the conclusion in proportion.

### EX010 — Worked result

In round one, the worker may promise Room 2 at 15:00 from an old printout; record that as the observed decision in the role-play. In round two, the worker marks the printout as stale and puts the request in a pending queue. An improvement criterion is “the worker does not confirm a post-printout booking without a current approved source.” The result is limited by invented data and a single session with a small number of participants. It does not establish real-world reliability; repeat tests and owner review would be needed.

### EX011 — Worked result

The decision question is whether a front-desk worker can make a correct room decision while the live view is unavailable. Resident is an external entity; booking view and staff view are processes; reservation store is a store; the printed schedule is a physical copy. Any four of these roles, correctly explained, satisfy the table. The event-contact list is outside the traced booking path because its purpose is announcements, though it remains relevant to a broader information inventory. One open question is whether the staff view reads the same store shown in the diagram. A good model says “proposed read” until the owner confirms it.

### EX012 — Worked result

At 08:20, `SYN-001` is created; at 09:00, the fixed printout is made; at 10:05, `SYN-002` is created; at 11:42, the room question arrives. Under the stated snapshot assumption, the printout can show `SYN-001` but not `SYN-002`. It cannot establish that Room 2 is free at 15:00. The worker marks the request pending and asks for an approved current source or the owner. If a learner says that the printout might refresh itself, they must explicitly challenge the exercise assumption; they cannot silently use a different scenario.

### EX013 — Worked result

Two flows in the proposed model are a resident's booking request to the booking view and a proposed write from the booking view to the reservation store. To save a reservation in this hypothetical path, the booking process would need a way to persist a valid decision; whether the depicted store is the real mechanism is unverified. To send a confirmation through a hypothetical supplier, that supplier would need to receive the required notification data and accept the delivery task. A delayed message does not by itself prove a failed reservation. Ask the owner whether confirmations are sent through an outside service and whether saving and messaging are coupled. Other answers are acceptable when they state an outcome, dependency, and uncertainty rather than asserting an unobserved implementation.

### EX014 — Worked result

Resident boundary: a room and time request enters the booking view; a resident may request an available room but should not gain staff powers. Ask the owner how requests are validated and what an approved synthetic test or design review shows. Staff boundary: an authenticated worker queries a staff view and may see or change information according to a defined role. Ask which roles may make changes and whether an approved role matrix and reviewed test support that rule. The arrows locate questions; they do not show that access checks exist or work. A claim that encryption or multifactor authentication is present from this drawing alone fails the evidence requirement.

### EX015 — Worked result

The earlier conclusion that only a stale 09:00 paper schedule is available is weakened by the owner's new report. Add “reported approved offline schedule, refreshed 11:40” as a separate copy; mark its authority and freshness as **reported, not verified**. In a paper rehearsal, give the worker a synthetic 11:40 sheet and check that its timestamp is 11:40 and that it includes `SYN-002`. If the owner confirms this as an approved current source and the check succeeds, the worker can use it according to the approved procedure; if the check fails, keep the request pending. One remaining limitation is that a single synthetic check does not establish how reliably the real offline schedule refreshes. The correct model changes conditionally instead of defending the old diagram.

### EX016 — Worked result

The REFUSE line is `11:42 confirm-from-printout`. The reason names `SYN-002`. That id is absent from the paper because the exercise printout is fixed at 09:00 and the booking was created at 10:05. The output does not say an attacker caused the gap.

### EX017 — Worked result

Room 4 at 15:00 has no row created after 09:00, so the rule prints ALLOW and the reason says no later booking is recorded for that room and start. The staff member must not tell a resident that Room 4 is free. ALLOW here means the synthetic table did not contain a conflicting later booking.

### EX018 — Worked result

REFUSE compares a printout time with a booking created later. The 11:43 export never makes that comparison, so the rule returns OUT OF SCOPE. This run does not show who can download the contact list, how long it is kept, or whether a control on it works.

### EX019 — Worked result

After STOP, the program still prints the 11:45 mark-pending line and the final tally. A facilitator pauses the participants, does not let anyone open a site, and asks the exercise owner what happens next. The program is replaying a log; the facilitator is responsible for the people in the room.

### EX020 — Worked result

One acceptable note: The exercise classified four synthetic actions against a 09:00 printout. At 11:42 the program refused confirmation of Room 2 at 15:00 because the paper omits `SYN-002`. The decision is to leave that request pending rather than confirm it from the paper. The 11:43 export is out of scope, not a refused booking. The script did not open a reservation store and did not treat the reported 11:40 sheet as verified. The open question for the owner is which approved source, if any, may replace the 09:00 paper. No numeric score belongs in the note.

### EX021 — Worked result

Say: "Room 2 at 14:00 is already booked. This sheet does not say who, and I will not guess." Leave out any person's name. `SYN-001` identifies a synthetic booking, not a resident, so reading the id aloud is also unnecessary for the asker's question.


**Expanded worked reasoning (EX021).** The slot-state statement passes the evidence gate because SYN-001 is confirmed and predates the 09:00 printout; a person-specific claim fails because no identity or permission is supplied. The short spoken reply in the model answer shares the slot state without revealing even an unnecessary internal ID. For a different request, “May I have Room 2 at 15:00?” at 11:42, a properly bounded response is: “I cannot confirm that from the 09:00 sheet; I can record your request as pending until an approved current source is checked.” The instructor can see SYN-002 in the synthetic full table but the simulated desk worker cannot claim that the unavailable live view was read. Reject “the missing paper row proves the room free,” and reject inferring a resident's name from a booking ID or announcement list. An equivalent reply earns credit when the source, permission and uncertainty boundaries are intact.

### EX022 — Worked result

The pencil mark replaces the 09:00 snapshot with a new, unauthorized line, so the sheet can no longer show what was printed. Confirmation on that altered sheet is still not allowed. Keep the request pending, or wait for a later copy whose time and author the owner can check. Do not treat the pencil as that copy.


**Expanded worked provenance note (EX022).**

| Record | Supplied status | Supported claim | Unsupported leap |
|---|---|---|---|
| Original 09:00 snapshot | Fixed, SYN-001 only | The stipulated state of that historical copy | No later booking could exist |
| Pencil addition | Volunteer wrote SYN-002 during the simulated outage | The sheet was changed after printing | The owner issued an authorized new schedule |
| Reported 11:40 source | Potential later copy described by the owner; not checked here | A verification question exists | The checked replacement is already in hand |

The correct alternative preserves the changed sheet as **altered**, records the 15:00 request as **not confirmed**, and asks for a separate owner-approved later source with verified time, origin, completeness and relevant row. Even a valid later sheet showing SYN-002 as booked does not license giving that slot away. The pencil may coincide with a true later fact, but coincidence does not make it part of the original snapshot. This exercise does not prove malicious conduct or the cause of a real outage.

<a id="answer-ex023"></a>
### EX023 — Worked result

Heard 09:12; room Room 2; start 15:00; state not confirmed. Yesterday's 09:00 paper is a different snapshot, so it cannot show whether today's 15:00 is free. No resident name belongs on the slip, and the outage cause is not part of the entry.


**Worked temporal and reconciliation extension (EX023).** The 09:12 entry records when the visitor **asked** on the second morning; 15:00 is the requested future start. The paper in the drawer belongs to the **previous day** at 09:00, and the second day's described 09:10–09:25 view interruption does not prove that the restored screen is authoritative, synchronized or already checked. The record therefore stays **not confirmed**. In a hypothetical **occupied** branch, *after* an owner-approved sufficiently current check, the response is "Room 2 at 15:00 is booked"; this communicates no resident identity and does not pretend the visitor has a reservation. In a hypothetical **no-conflict** branch, the worker may say only that no conflict was found in the approved checked source; creating or confirming a reservation would require a **separate authorized step and evidence** that the book does not supply. Neither outcome is a received case fact. Keep the pending entry's limited history and refer unresolved questions rather than silently deleting or resubmitting it. **Falsifier:** any answer that says "confirmed" on the strength of a slip, an expired paper or merely the page's return has failed the exercise even if the room later proves free.

<a id="answer-ex024"></a>
### EX024 — Worked result

The exercise observed a 09:00 paper that omitted a later synthetic booking, and a booking view that was described as unavailable, with no tested cause. The supported class is a weak confirmation procedure. A software vulnerability, an attack, and an incident are unproven: no program flaw was demonstrated, and no owner declared an incident.


**Worked evidence matrix and causal boundary (EX024).**

| Claim | Evidence actually supplied | Gap / negative control | Safe judgment |
|---|---|---|---|
| The fixed 09:00 paper omitted a 10:05 booking | The synthetic timeline includes SYN-002, created after printing | No real reservation store was inspected | Supported **only for the classroom fixture** |
| A worker might make a wrong promise from that paper | Hypothetical use of the old snapshot during an interruption | No verified live procedure, worker action or authorized confirmation receipt | Procedural weakness and plausible risk hypothesis |
| The 11:30 view outage happened | The fictional narrative describes a limited front-desk outage | No diagnostic data, linked cause or owner incident classification | Described service unavailability; cause and security classification open |
| A critical site vulnerability caused an attack | No source, exploited weakness, product test or severity method supplied | Would need authorized scope, trigger/impact evidence, negative controls and owner review | Unsupported as fact |

A process **can** be vulnerable under NIST terminology if a verified deficiency can be exploited or triggered with a security-relevant effect; a software defect or observed attacker is **not** a prerequisite for every such finding. What is absent here is evidence that the real process permits the failure and evidence linking it to a real security effect. A proper falsifier is an owner-approved controlled comparison showing that a current-source check and pending rule prevent unsupported confirmation under the same synthetic timing. A single test does not certify all future workflows. The classroom does not establish an incident, rate severity or measure how many people were harmed. The three-sentence core answer above remains valid; this table explains why each stronger noun would require additional proof.

<a id="answer-ex025"></a>
### EX025 — Worked result

The program counted one STOP, one OUT OF SCOPE, one REFUSE and one ALLOW on the four-action log, and left UNKNOWN at zero. Fifty percent would turn two of those labels into a harm rate. The printed line does not measure harm, and it does not measure how often staff would trust the stale paper. Medium names a rank this exercise never defined. The Room 2 at 15:00 request stays pending until an approved current source exists. Chapter 8's weak confirmation procedure is unchanged.


**Expanded worked reasoning and evidence boundary (EX025).** The recorded denominator is **four deliberately authored proposals**, not four observed adverse events. A classroom analyst may compute “two of four labels” only after explicitly choosing the arbitrary grouping (for example STOP plus REFUSE). That 2 / 4 calculation is 50% of that **chosen synthetic label set**; nothing justifies calling those two labels actual harms or interpreting their share as operational frequency, likelihood, risk or severity. STOP names an out-of-bounds proposal, OUT OF SCOPE names an excluded data-purpose proposal, REFUSE names a rule-prohibited paper confirmation, and ALLOW permits recording a **pending** request rather than certifying a free room. UNKNOWN 0 demonstrates classification coverage for these four known action kinds, not causal certainty about the outage. The dashboard's **25** and **Medium** have no defined measurement scale, impact criteria or approved owner judgment. The decision still open is which suitable approved current source would be checked before any separate authorization to book Room 2 at 15:00.

| Dashboard proposition | Basis | Disposition |
|---|---|---|
| One each STOP, OUT OF SCOPE, REFUSE, ALLOW; zero UNKNOWN | Exact Chapter 4 printed log | Retain as reproducible classifier census |
| “Two adverse out of four = 50% harm” | Optional arithmetic grouping, with **adverse** undefined | Reject its harm/risk interpretation; arithmetic alone does not supply meaning |
| “Score 25 / Medium” | No likelihood, impact, severity method or approval | Reject both labels without inventing a replacement number |
| “Exercise can close” | The synthetic pending request remains and the reported later copy is unverified | Retain unresolved owner/source and booking-decision gates |

**Falsifiers and accepted alternatives.** An acceptable four-sentence answer may explicitly acknowledge the mathematical 50% share of a *declared grouping* while refusing the unsupported meaning “50% adverse.” Reject any answer that equates UNKNOWN 0 with no unknown causes, ALLOW with permission to allocate a room, or REFUSE with an actual harmed resident. If real decision and outcome evidence later existed, it would belong to a separately scoped analysis; the old tally itself would not change.

<a id="answer-ex026"></a>
### EX026 — Worked result

The classmate's note is a second-hand report of a clock time. It is not the 11:40 sheet. The owner has not named a sheet as the approved current source, and nobody has recorded that the sheet's own time is 11:40 and that `SYN-002` is printed on it. Room 2 at 15:00 stays not confirmed. The Chapter 4 tally remains `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`.


**Expanded worked evidence ledger (EX026).**

| Source or claim | Evidentiary class and time | What remains missing | Decision |
|---|---|---|---|
| Original 09:00 paper | Actual fixed source **in the synthetic exercise**; SYN-002 created 10:05 is later | A verified approved current replacement for the 15:00 query | Preserve the 11:42 REFUSE and pending request |
| “The owner mentioned a refresh at 11:40,” repeated by a facilitator | Second-hand report of a **purported sheet time**, not direct artifact inspection | Owner naming **this** sheet as approved, and direct record of its **11:40 heading plus SYN-002** row | Record a follow-up request; no source substitution or confirmation |
| A future owner-identified, directly inspected 11:40 sheet | **Hypothetical in Chapter 10**; separate evidence arrives only in Chapter 11 | Its actual limited authority, relevant row/status and any independent booking requirement | Could establish that the 15:00 slot is **already booked** if SYN-002 is confirmed; cannot create a new booking |

The correct three-part reply is: **(1)** the classmate's note is a second-hand report, **(2)** owner approval of an identified physical source and the two observations on that very source are not recorded, and **(3)** Room 2 / 15:00 stays **not confirmed**, with Chapter 4's exact STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0 unchanged. The report contains words about a time, not a source record. The visitor's requested start, the printout's timestamp and the time a booking was created are distinct. A learner who retypes the program's printout time to make REFUSE disappear has changed the fixture without producing evidence. In Chapter 11, separately released evidence may support a new, **bounded** statement that a slot is taken; it cannot backdate knowledge or undo the historical paper classification.

**Negative control.** Repeating the purported 11:40 time from another person fails both gates; a real checked page with SYN-002 confirmed would not justify saying the 15:00 slot is free. Equivalent responses that preserve provenance, time, owner approval and the original four-action run satisfy the task without reproducing this table word for word.

<a id="answer-ex027"></a>
### EX027 — Worked result

`SYN-002` on the named page is a confirmed booking of Room 2 at 15:00, so the resident is told the slot is taken. The word free contradicts that row. The older program still describes the 09:00 printout, and its line stays `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. An 11:40 heading on one classroom page does not set the fallback for later outages. No personal name is spoken, and the live site is not opened.


**Expanded worked source-and-decision record (EX027).**

| Decision component | Direct evidence or boundary | Justified result |
|---|---|---|
| **Source selection** | The exercise owner names **this one** synthetic page for the current sitting | Page may support the limited room-state question, not a month-long procedure |
| **Direct inspection** | Heading `11:40`; `SYN-002`, Room 2, 15:00, created 10:05, `confirmed` | A matching, confirmed **existing** reservation for Room 2 / 15:00 |
| **Resident reply** | Booking record has an ID but **no resident name** | “Room 2 at 15:00 is already booked.” No holder identity is inferred or announced |
| **Historical provenance** | Chapter 4 classified a proposal against the fixed `09:00` printout, before release of this page | Its `REFUSE` and exact five-counter tally remain unchanged |
| **Approval limit** | The owner named this page **only in the current exercise** | No standing refresh rule, new booking, production action or live-site check is authorized |

Four defensible original EX027 sentences are: **(1)** “The owner-named 11:40 page shows `SYN-002` as a confirmed Room 2 booking at 15:00.” **(2)** “Calling that slot free contradicts the row's explicit status.” **(3)** “Chapter 4's `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0` still describes the 09:00-based action log, including REFUSE for the 11:42 proposed paper confirmation; the new page does not rewrite it.” **(4)** “The owner approved this particular source for this sitting, not as a standing monthly or future-outage schedule.”

**Adversarial checks:** without the owner's naming, inspection alone is insufficient for the role-play's authorized decision; relying on `SYN-001` would answer the **14:00** question, not the 15:00 question. Chapter 10 recorded only a **report**, so this source cannot be backdated into its evidence set. The fixed log's printed ALLOW belongs to **mark-pending at 11:45**; a separately discussed Room 4 hypothetical is not that log entry. A new confirmed booking, a resident identity and actual software behavior remain outside this chapter. Answers using equivalent wording earn credit only if all four distinctions survive.

<a id="answer-ex028"></a>
### EX028 — Worked result

The named page prints two rows, and both name Room 2. Room 4 at 15:00 matches neither, so the page says nothing about that request. Staff tell the resident they cannot answer from this page and leave the request pending. They do not offer the room. ALLOW remains the label Chapter 4 printed for the 09:00 log. It is not rewritten as a confirmation on the 11:40 page. The census of that log is still `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. `SYN-002` is still on the page, so Room 2 at 15:00 stays booked.


**Expanded worked query-completeness record (EX028).**

| Pair inspected | Page rows matching both room **and** start | Supported room-state conclusion | Missing evidence before a new booking |
|---|---:|---|---|
| Room 2 / 15:00 | **1**: `SYN-002`, confirmed | **Taken**, on this owner-named synthetic page | No authority to reallocate; no patron identity, live access or new transaction receipt |
| Room 4 / 15:00 | **0** of the two displayed rows | **Unknown availability**: page is silent | Completeness/currentness for the relevant date and slot, conflict checking, owner-approved booking action and a separate confirmation result |

The four required EX028 sentences can read: **(1)** “The named 11:40 page has two rows and **zero** matches for Room 4 at 15:00.” **(2)** “That absence does not prove the page lists all Room 4 bookings, so I cannot offer the room and will leave the request pending.” **(3)** “The Chapter 4 ALLOW was the **11:45 mark-pending** verdict on the original 09:00-based four-action log, not a Room 4 reservation; its exact `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0` stays unchanged.” **(4)** “The same page still shows `SYN-002` confirmed for Room 2 at 15:00, so that different slot is already booked.”

**Conditional test, not a new observation:** if the owner separately provided an authorized, demonstrably complete and current record for Room 4 at the relevant date/time, a zero-conflict finding could be assessed **within that verified scope**; it would not automatically create a booking. An authorized transaction and its outcome would still be required. A supposed conflict cannot be manufactured from another room's row, and a missing row cannot be made into a free-room promise. The exercise has no such complete later record, no real patron data and no completed booking operation.

<a id="answer-ex029"></a>
### EX029 — Worked result

The naming the classmate cites belonged to the earlier sitting. Today's owner has not named a source for the 09:12 outage. Today's Room 2 at 15:00 request stays pending. The 11:40 page remains filed as an earlier sheet. The Chapter 4 census is not rerun.


**Expanded worked provenance and temporal-authority answer (EX029).** The earlier 11:40 page was approved **for the previous sitting only**. It can still be filed as evidence that the then-named page displayed a confirmed SYN-002 booking for Room 2 at 15:00. That statement remains historically bounded; the older physical paper and its heading do **not** constitute a new authorization. At 09:12 on the next morning, the desk view is described as unavailable and today's owner **has not named any current page**. Therefore the new request for Room 2 / 15:00 is **not confirmed**; the worker cannot tell the visitor either “taken” or “free” based on the previous sitting. The correct next action is a minimal pending slip followed by an owner-named and checked current source, with a separate approved transaction if a booking is ever to be made. **No source is released in Chapter 13.**

| Checkpoint | Source and authority | Evidence for the question | Permitted result |
|---|---|---|---|
| Previous sitting | 11:40 synthetic sheet, named only for that exercise | SYN-002, Room 2 / 15:00, confirmed **on that sheet** | Historical bounded “taken” statement; preserve note |
| New morning, 09:12 | The old sheet is archived; today's owner has named **none** | No approved current row for Room 2 / 15:00 on the new date | Record **09:12; Room 2; 15:00 today; not confirmed**; await current evidence |

A usable three-sentence answer is: **(1)** “The 11:40 sheet was named for the earlier sitting, not for this new morning.” **(2)** “Today's owner has not identified an authorized current source for the 09:12 request.” **(3)** “The Room 2 / 15:00 request therefore stays not confirmed, while yesterday's record and the original Chapter 4 tally remain unchanged.” The negative control is any response that treats possession, a repeated story or a printed clock as an active permission grant. No record supplied a confirmed transaction for the new morning.

<a id="answer-ex030"></a>
### EX030 — Worked result

Today's owner named the 11:55 page. `SYN-003` prints Room 4 at 15:00 as confirmed, so the slot is taken and no personal name is added. Chapter 12's silence stays in that chapter's note about the 11:40 page. ALLOW stays on the 09:00 log.


**Expanded worked source-scoped reading (EX030).** Today's owner names the separate **11:55 synthetic sheet for this exercise**. Its **SYN-003** row explicitly records **Room 4 / 15:00**, created **11:20**, status **confirmed**, so the bounded answer is **“Room 4 at 15:00 is already booked.”** The page also contains confirmed **SYN-002** for **Room 2 / 15:00**, which independently supports “taken” for that pair. Neither identifier names a resident and no disclosure of a person's identity is authorized. The page says **nothing** about Room 4 at **16:00**, so the absence of a row does not establish that time is free or authorize a transaction.

| Query | Evidence on owner-named 11:55 page | Supported response | Unsupported inference |
|---|---|---|---|
| Room 4 / 15:00 | SYN-003 confirmed, created 11:20 | Already booked, no person named | Free, transferable, or newly confirmed for the asker |
| Room 2 / 15:00 | SYN-002 confirmed | Already booked, no person named | The older booking row can be discarded |
| Room 4 / 16:00 | No matching row in the three-row visible subset | Availability **unknown**; keep the request not confirmed | Missing means free or a new booking is authorized |

An acceptable original three-sentence answer is: **(1)** “Today's owner named this 11:55 page only for the current sitting.” **(2)** “SYN-003 shows an existing confirmed Room 4 / 15:00 booking, so that slot is taken and no person's name is given.” **(3)** “I will not rewrite the earlier Chapter 12 note of silence on its different 11:40 page or the Chapter 4 tally STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0.” The old ALLOW was for the **11:45 mark-pending** proposal in the fixed Chapter 4 log, not proof of Room 4 availability or a receipt for an executed booking. A new record may provide more evidence for a later sitting **without retroactively changing what the older artifact said**. Do not backdate the new sheet to Chapter 13, manually merge the sheets, claim a live test, or identify fictional patrons.

### EX031 — Worked result

Read the 11:55 page whole. Do not copy `SYN-003` onto the 11:40 page, and do not strike `SYN-002` from the named page. Both 15:00 slots printed on the named page are taken. The sheets stay unmarked.

### EX032 — Worked result

11:20 is when `SYN-003` was created. 11:55 is the page heading. The row is on the named page, so Room 4 at 15:00 stays taken. ALLOW is not flipped. The program is not started again.

### EX033 — Worked result

Both later pages show `SYN-002` for Room 2 at 15:00. That is the supported fact. An attack is not shown. Safety is not shown. The supported class remains a weak confirmation procedure. The census stays the four-label line from the 09:00 log.

### EX034 — Worked result

Keep the 09:00 printout because it is the recorded run's input. Keep the 11:40 page because it shows yesterday's missing Room 4 row. Keep the 11:55 page and use it for the current Room 4 question. Do not shred or overwrite. Do not rerun the census.

### EX035 — Worked result

Room 2 at 15:00 and Room 4 at 15:00 stay taken from the named page, with no names spoken or written. The event-contact export stays out of scope, and the 11:43 label stays OUT OF SCOPE. The census does not gain a fifth action.

### EX036 — Worked result

The note names the 11:55 page for this exercise. Room 2 at 15:00 is taken from `SYN-002`. Room 4 at 15:00 is taken from `SYN-003`. The census remains `STOP 1; OUT OF SCOPE 1; REFUSE 1; ALLOW 1; UNKNOWN 0`. The outage cause is still not established. The security claim, the free room, and the monthly 11:55 rule are removed. Reaching lesson 20 does not finish the book.
