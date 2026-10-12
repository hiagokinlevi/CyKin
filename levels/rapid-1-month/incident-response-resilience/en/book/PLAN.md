# Principal book plan — Incident response and cyber resilience / Rapid course / English

**One book for this course and language.** 4 curricular subjects are its chapters. Duration: 1 month; planned effort: approximately 80 hours. Audience: New learners. Entry knowledge: No prior security role; basic digital literacy. Intended outcome: recognize and explain the core risks; complete one guided task in incident response and cyber resilience.

**Editorial state:** draft manuscript exists; release A4 validation and review pending. English reference edition.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 320-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response recommendations within cybersecurity risk management; it supersedes Rev. 2.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, testing and improvement.
- [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) — exercise design and evaluation; a 2006 publication whose applicability must be checked during authorship.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic techniques in response; a 2006 publication whose technical details need current verification.

These are source leads, not a finished chapter bibliography. Cite the relevant primary source beside each factual claim in the authored manuscript and identify any fictional case as synthetic.

## Contents and chapter summaries

<a id="ch-01"></a>

### Chapter 01 — Incident readiness, roles and authorized scope

**Stage 1; 80 planned A4 pages; 13 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-01)

**Teaching purpose and relevance:** Show that an incident decision depends on prior ownership, service knowledge, evidence readiness and permission; prevent a suspicious signal from becoming an unauthorized investigation.

**Concepts and techniques:** Service dependencies; testable evidence-readiness contract; source lineage and missingness; incident record; observation versus conclusion; decision owner; scoped authorization.

**Depth and method:** At rapid course level, learners will follow a contained worked example. Use a guided case record to distinguish observations, assumptions and the next safe action.

**Worked example:** A synthetic Harbor Library booking service, a proposed D1 evidence contract and an unusual staff sign-in.

**Practice and exercises:** Map dependencies to bounded decision questions and source limits, assign owners and open a case record without treating planned telemetry as collected evidence. The planned allocation is 13 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

<a id="ch-02"></a>

### Chapter 02 — Alert triage and evidence preservation

**Stage 2; 80 planned A4 pages; 13 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-02)

**Teaching purpose and relevance:** Teach a defensible first assessment and a decision-oriented preservation queue that keeps requests, approvals, collected items and verified limits separate.

**Concepts and techniques:** Triage question; event, discovery and ingestion time; query coverage; evidence pointer; preservation priority and loss path; approval and collection states; copy integrity; package provenance; cross-source correlation keys and ambiguous joins; uncertainty and severity.

**Depth and method:** At rapid course level, learners will follow a contained worked example. Use a guided case record to distinguish observations, assumptions and the next safe action.

**Worked example:** Synthetic R9–R16 booking, identity, training and help-desk records with a 24-hour retention notice, plus separate delayed-arrival and overlapping-session replays.

**Practice and exercises:** Build a bounded timeline, rank minimal source requests, distinguish booking from application audit, test quiet-query limits, audit a synthetic evidence package and classify cross-source matches without inferring a human actor. The planned allocation is 13 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

<a id="ch-03"></a>

### Chapter 03 — Containment, eradication and recovery decisions

**Stage 3; 80 planned A4 pages; 12 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-03)

**Teaching purpose and relevance:** Explain how a response choice can reduce harm while risking service disruption, evidence loss or premature closure.

**Concepts and techniques:** Containment options; approval; tested control effectiveness across write routes; eradication evidence; backup candidate provenance, freshness and correctness; isolated restore; rollback and review time.

**Depth and method:** At rapid course level, learners will follow a contained worked example. Use a guided case record to distinguish observations, assumptions and the next safe action.

**Worked example:** The fictional booking service with suspicious staff-account activity, a separate isolated write-pause validation branch, a successful backup job without a recent restore test, and a three-candidate recovery replay.

**Practice and exercises:** Compare bounded actions, test whether a proposed pause blocks its stated write routes, reconcile booking states, screen candidate copies against recovery objectives and define service-acceptance evidence. The planned allocation is 12 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

<a id="ch-04"></a>

### Chapter 04 — Guided incident simulation and after-action review

**Stage 4; 80 planned A4 pages; 12 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-04)

**Teaching purpose and relevance:** Integrate readiness, triage and recovery into one controlled case and show how learning is recorded without claiming an untested return to service.

**Concepts and techniques:** Tabletop inject; decision log; audience-specific and versioned status communication; measurement contract; after-action report; corrective-action closure.

**Depth and method:** At rapid course level, learners will follow a contained worked example. Use a guided case record to distinguish observations, assumptions and the next safe action.

**Worked example:** A synthetic Harbor Library scenario with staged evidence, an unavailable-approver replay and a separate unverified-exposure message replay.

**Practice and exercises:** Complete a guided tabletop and six-artifact case record, compare exercise findings with technical tests, draft bounded messages for different audiences and plan evidence-linked improvements. The planned allocation is 12 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

## Practical and assessment plan

Practice: follow a contained worked example. Assessment: short quiz, observed lab and a small annotated artifact. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
