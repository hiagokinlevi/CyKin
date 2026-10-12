# Principal book plan — Cybersecurity / Technologist course / English

**One book for this course and language.** 30 curricular subjects are its chapters. Duration: 3 years; planned effort: approximately 2400 hours. Audience: Technology implementers and administrators. Entry knowledge: Computing foundations and introductory security operations. Intended outcome: integrate services, controls, operations and measurement in cybersecurity.

**Editorial state:** structured outline; manuscript not yet authored. English reference edition.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 900-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) — a taxonomy of security outcomes and a source for discussing organizational risk; it does not prescribe a single implementation.
- [NIST CSF 2.0 FAQ](https://www.nist.gov/cyberframework/faqs) — explanations of framework components and the Govern function.
- [NIST SP 800-53 Rev. 5 publication and current control-catalog update](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — a flexible security and privacy control catalog. Check the linked newer catalog release before citing specific controls; framework mappings are not automatic equivalences.

These sources guide the English teaching plan. The Harbor Library case is synthetic; factual claims in authored lessons need source-specific citations.

## Contents and chapter summaries

These are editorial outlines. Each chapter summary ends with links to the previous position, the course index and the next position; a **draft** link opens authored teaching, while a **plan** link opens another outline.

<a id="ch-01"></a>

### Chapter 01 — Computing systems

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Explain how compute components and service dependencies affect the placement of security controls.

**Concepts and techniques:** Process; storage; interface; dependency; failure domain.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic municipal reservation service split across a client, gateway and database.

**Practice and exercises:** Draw a component map and identify two failure paths that require different safeguards. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 01 of 30 (outline):** [← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (plan) →](PLAN.md#ch-02)

<a id="ch-02"></a>

### Chapter 02 — Networks and internet services

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Trace ordinary service traffic so later security decisions have a defensible network model.

**Concepts and techniques:** DNS; routing; TLS endpoint; proxy; service exposure.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional resident portal with a public gateway and private administration network.

**Practice and exercises:** Trace a request through named components and mark what each operator can observe. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 02 of 30 (outline):** [← Chapter 01 (plan)](PLAN.md#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (plan) →](PLAN.md#ch-03)

<a id="ch-03"></a>

### Chapter 03 — Programming foundations

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Read and modify small programs while keeping security assumptions visible.

**Concepts and techniques:** Input validation; state; exception; dependency; test.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** An isolated booking API that rejects malformed reservations but logs too much data.

**Practice and exercises:** Add a bounded validation rule and test both accepted and rejected inputs. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 03 of 30 (outline):** [← Chapter 02 (plan)](PLAN.md#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (plan) →](PLAN.md#ch-04)

<a id="ch-04"></a>

### Chapter 04 — Data models

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Model records and relationships before deciding how to protect or retain them.

**Concepts and techniques:** Schema; identifier; provenance; classification; retention.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic events register linking attendees, volunteers and venue bookings.

**Practice and exercises:** Annotate a schema with sensitivity, owners and minimal retention needs. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 04 of 30 (outline):** [← Chapter 03 (plan)](PLAN.md#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (plan) →](PLAN.md#ch-05)

<a id="ch-05"></a>

### Chapter 05 — Security literacy

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Connect confidentiality, integrity and availability to concrete service outcomes and uncertainty.

**Concepts and techniques:** Asset; harm; threat; weakness; control; residual risk.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional ticketing service with a duplicate booking and an unrelated sign-in warning.

**Practice and exercises:** Write separate risk statements without claiming the two events share a cause. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 05 of 30 (outline):** [← Chapter 04 (plan)](PLAN.md#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (plan) →](PLAN.md#ch-06)

<a id="ch-06"></a>

### Chapter 06 — Operating systems and virtualization

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Identify host and virtual resource boundaries relevant to secure administration.

**Concepts and techniques:** Account; process; patch; image; isolation; snapshot.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A training virtual machine running a public portal and a maintenance service.

**Practice and exercises:** Inventory host privileges and propose an isolated maintenance path. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 06 of 30 (outline):** [← Chapter 05 (plan)](PLAN.md#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (plan) →](PLAN.md#ch-07)

<a id="ch-07"></a>

### Chapter 07 — Identity and access foundations

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Explain how identity assertions become application permissions and where this chain can fail.

**Concepts and techniques:** Principal; authentication; authorization; role; session; review.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional library where volunteers can edit only their own event schedules.

**Practice and exercises:** Create a role matrix and test a denied cross-team edit. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 07 of 30 (outline):** [← Chapter 06 (plan)](PLAN.md#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (plan) →](PLAN.md#ch-08)

<a id="ch-08"></a>

### Chapter 08 — Security architecture basics

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Compare simple control placements against trust boundaries and service goals.

**Concepts and techniques:** Trust zone; defense in depth; reference architecture; exception.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A municipal portal that exposes an administrator endpoint through the same gateway as public pages.

**Practice and exercises:** Sketch two architectures and explain their different operational costs. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 08 of 30 (outline):** [← Chapter 07 (plan)](PLAN.md#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (plan) →](PLAN.md#ch-09)

<a id="ch-09"></a>

### Chapter 09 — Evidence and measurement

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Specify what must be observed to support a security claim before choosing a metric.

**Concepts and techniques:** Claim; observation; denominator; data quality; baseline.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic dashboard reporting a high block rate without total request counts.

**Practice and exercises:** Reconstruct a usable measure and record the uncertainty caused by missing data. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 09 of 30 (outline):** [← Chapter 08 (plan)](PLAN.md#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (plan) →](PLAN.md#ch-10)

<a id="ch-10"></a>

### Chapter 10 — Service-security operating model

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Define ownership and decision routes for a service that crosses several technical teams.

**Concepts and techniques:** Service owner; control owner; escalation; review cadence; dependency.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A community platform shared by application, identity and facilities teams.

**Practice and exercises:** Write a responsibility map for access changes and service restoration decisions. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 10 of 30 (outline):** [← Chapter 09 (plan)](PLAN.md#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (plan) →](PLAN.md#ch-11)

<a id="ch-11"></a>

### Chapter 11 — Asset inventory and ownership

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build a maintainable inventory that links assets to services and accountable owners.

**Concepts and techniques:** Inventory source; discovery gap; business service; lifecycle; owner.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic asset export with retired devices and an unassigned database.

**Practice and exercises:** Reconcile two inventory sources and document ownership gaps. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 11 of 30 (outline):** [← Chapter 10 (plan)](PLAN.md#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (plan) →](PLAN.md#ch-12)

<a id="ch-12"></a>

### Chapter 12 — Data and trust-boundary mapping

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Follow sensitive data through interfaces to expose assumptions that need controls.

**Concepts and techniques:** Data-flow diagram; trust boundary; transfer; storage; exposure.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional residents' application that sends form data to an external notification service.

**Practice and exercises:** Mark crossings and define one verification question for each. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares Chapter 13. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 12 of 30 (outline):** [← Chapter 11 (plan)](PLAN.md#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (plan) →](PLAN.md#ch-13)

<a id="ch-13"></a>

### Chapter 13 — Scenario-based risk prioritization

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Prioritize service-specific risks without treating a score as a substitute for evidence.

**Concepts and techniques:** Scenario; impact; uncertainty; likelihood caveat; dependency.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** Three synthetic threats to a public booking service with different recovery windows.

**Practice and exercises:** Rank options under explicit assumptions and show how the order changes when an assumption changes. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 12 and prepares Chapter 14. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 13 of 30 (outline):** [← Chapter 12 (plan)](PLAN.md#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (plan) →](PLAN.md#ch-14)

<a id="ch-14"></a>

### Chapter 14 — Security assessment workflow

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Sequence authorization, collection, analysis and review for a repeatable service assessment.

**Concepts and techniques:** Scope; collection plan; checkpoint; finding; approval.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional request to assess a community portal during a limited maintenance window.

**Practice and exercises:** Write the assessment runbook and mark excluded systems and stop conditions. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 13 and prepares Chapter 15. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 14 of 30 (outline):** [← Chapter 13 (plan)](PLAN.md#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (plan) →](PLAN.md#ch-15)

<a id="ch-15"></a>

### Chapter 15 — Laboratory: map services, evidence and owners

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Practice joining service architecture, evidence availability and accountability in one lab artifact.

**Concepts and techniques:** Service map; data source; owner; blind spot; evidence pointer.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** An isolated civic-service lab with prepared diagrams, log samples and owner notes.

**Practice and exercises:** Produce a map that links each risk claim to a source and an accountable reviewer. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 14 and prepares Chapter 16. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 15 of 30 (outline):** [← Chapter 14 (plan)](PLAN.md#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (plan) →](PLAN.md#ch-16)

<a id="ch-16"></a>

### Chapter 16 — Control selection across the service lifecycle

**Stage 4; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Choose preventive, detective and recovery measures for the same explicit outcome.

**Concepts and techniques:** Control objective; dependency; residual risk; operating cost.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional portal whose login policy is strong but whose export recovery has never been tested.

**Practice and exercises:** Compare three control packages against a common service-risk scenario. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 15 and prepares Chapter 17. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 16 of 30 (outline):** [← Chapter 15 (plan)](PLAN.md#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (plan) →](PLAN.md#ch-17)

<a id="ch-17"></a>

### Chapter 17 — Security tool integration and configuration

**Stage 4; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Integrate tools around stable data contracts instead of assuming dashboards agree.

**Concepts and techniques:** Connector; schema; privilege; clock; failure behavior.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A training identity feed and alerting service with mismatched user identifiers.

**Practice and exercises:** Map fields, configure a safe connector and verify missing-record behavior. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 16 and prepares Chapter 18. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 17 of 30 (outline):** [← Chapter 16 (plan)](PLAN.md#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (plan) →](PLAN.md#ch-18)

<a id="ch-18"></a>

### Chapter 18 — Control deployment and exception handling

**Stage 4; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Deploy a baseline with ownership, tests and narrowly justified exceptions.

**Concepts and techniques:** Baseline; change window; exception expiry; rollback; acceptance test.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic branch office where a legacy printer cannot use the new access policy.

**Practice and exercises:** Document an exception and test its boundary without weakening unrelated users. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 17 and prepares Chapter 19. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 18 of 30 (outline):** [← Chapter 17 (plan)](PLAN.md#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (plan) →](PLAN.md#ch-19)

<a id="ch-19"></a>

### Chapter 19 — Monitoring outcomes and signal quality

**Stage 4; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Assess whether monitoring observes the outcome that a control is intended to protect.

**Concepts and techniques:** Coverage; precision; false positive; blind spot; escalation threshold.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional alert stream with duplicated account events and silent overnight gaps.

**Practice and exercises:** Measure signal quality and propose a limited collection improvement. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 18 and prepares Chapter 20. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 19 of 30 (outline):** [← Chapter 18 (plan)](PLAN.md#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (plan) →](PLAN.md#ch-20)

<a id="ch-20"></a>

### Chapter 20 — Diagnosing drift and broken assurance

**Stage 4; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Troubleshoot why documented safeguards diverge from deployed and observed behavior.

**Concepts and techniques:** Drift; configuration source; effective policy; retest; owner.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A lab access rule that appears in policy documents but is absent on one service instance.

**Practice and exercises:** Trace the discrepancy, propose a reversible fix and record evidence after retesting. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 19 and prepares Chapter 21. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 20 of 30 (outline):** [← Chapter 19 (plan)](PLAN.md#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (plan) →](PLAN.md#ch-21)

<a id="ch-21"></a>

### Chapter 21 — Cross-service dependency management

**Stage 5; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Account for shared identity, network and data services when changing a local control.

**Concepts and techniques:** Dependency graph; cascading effect; service contract; regression test.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** Two fictional public services that rely on the same identity gateway and backup schedule.

**Practice and exercises:** Predict impacts of a gateway change and design cross-service acceptance checks. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 20 and prepares Chapter 22. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 21 of 30 (outline):** [← Chapter 20 (plan)](PLAN.md#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (plan) →](PLAN.md#ch-22)

<a id="ch-22"></a>

### Chapter 22 — Bounded automation and human approval

**Stage 5; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Automate repeatable checks while keeping consequential changes subject to review.

**Concepts and techniques:** Idempotence; allowlist; dry run; approval; audit trail.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** An isolated script proposing access-policy updates from an approved inventory.

**Practice and exercises:** Exercise normal and malformed inputs and require human approval before simulated application. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 21 and prepares Chapter 23. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 22 of 30 (outline):** [← Chapter 21 (plan)](PLAN.md#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (plan) →](PLAN.md#ch-23)

<a id="ch-23"></a>

### Chapter 23 — Security program metrics and evaluation

**Stage 5; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Evaluate whether controls improve service outcomes rather than counting tool activity.

**Concepts and techniques:** Leading measure; outcome measure; baseline; confounder; review period.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional program that reports fewer alerts after one sensor was removed.

**Practice and exercises:** Critique the dashboard and design a measure that exposes lost visibility. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 22 and prepares Chapter 24. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 23 of 30 (outline):** [← Chapter 22 (plan)](PLAN.md#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (plan) →](PLAN.md#ch-24)

<a id="ch-24"></a>

### Chapter 24 — Applied comparative study of control outcomes

**Stage 5; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Compare two control implementations using a bounded question and reproducible observations.

**Concepts and techniques:** Hypothesis; comparator; sampling; bias; reproducibility.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** Two synthetic sign-in policies tested against the same scripted user tasks.

**Practice and exercises:** Define a protocol, record confounders and explain which conclusion the data cannot support. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 23 and prepares Chapter 25. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 24 of 30 (outline):** [← Chapter 23 (plan)](PLAN.md#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (plan) →](PLAN.md#ch-25)

<a id="ch-25"></a>

### Chapter 25 — Team studio: build a service-security plan

**Stage 5; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Coordinate technical and organizational controls in a reviewable implementation plan.

**Concepts and techniques:** Role assignment; milestone; dependency; acceptance criterion; review.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A team brief for a synthetic municipal permits platform with limited staff time.

**Practice and exercises:** Produce a staged plan and defend priority choices to another team. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 24 and prepares Chapter 26. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 25 of 30 (outline):** [← Chapter 24 (plan)](PLAN.md#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (plan) →](PLAN.md#ch-26)

<a id="ch-26"></a>

### Chapter 26 — Operations handoff and runbooks

**Stage 6; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Transfer a deployed safeguard with clear ownership and failure response.

**Concepts and techniques:** Runbook; alert owner; escalation; maintenance; revision trigger.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional service handed to an on-call team without a tested account-lockout procedure.

**Practice and exercises:** Write and walk through a runbook using a synthetic lockout event. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 25 and prepares Chapter 27. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 26 of 30 (outline):** [← Chapter 25 (plan)](PLAN.md#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (plan) →](PLAN.md#ch-27)

<a id="ch-27"></a>

### Chapter 27 — Deploy and verify a security baseline

**Stage 6; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Demonstrate an end-to-end controlled deployment and observable acceptance tests.

**Concepts and techniques:** Precondition; staged rollout; rollback; negative test; evidence.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A contained web service receiving a new staff access baseline.

**Practice and exercises:** Apply the baseline in the lab, test allowed and denied actions, then record rollback evidence. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 26 and prepares Chapter 28. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 27 of 30 (outline):** [← Chapter 26 (plan)](PLAN.md#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (plan) →](PLAN.md#ch-28)

<a id="ch-28"></a>

### Chapter 28 — Supervised field service review

**Stage 6; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use an authorized field setting to compare a documented control with actual service practice.

**Concepts and techniques:** Consent; observation; interview; sanitization; discrepancy.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A simulated interview with a civic-service operator and sanitized configuration excerpts.

**Practice and exercises:** Prepare the scope, document three observations and return a bounded improvement note. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 27 and prepares Chapter 29. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 28 of 30 (outline):** [← Chapter 27 (plan)](PLAN.md#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (plan) →](PLAN.md#ch-29)

<a id="ch-29"></a>

### Chapter 29 — Capstone: integrate controls and evidence

**Stage 6; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build a coherent security service with linked architecture, controls, telemetry and owner decisions.

**Concepts and techniques:** Integration; acceptance test; evidence trail; residual risk.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic community platform with public access, staff roles and nightly data exports.

**Practice and exercises:** Deliver a working lab configuration and a dossier linking each design claim to evidence. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 28 and prepares Chapter 30. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 29 of 30 (outline):** [← Chapter 28 (plan)](PLAN.md#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (plan) →](PLAN.md#ch-30)

<a id="ch-30"></a>

### Chapter 30 — Capstone: evaluate resilience and residual risk

**Stage 6; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Challenge the capstone with failures and explain the limits of the result.

**Concepts and techniques:** Fault scenario; recovery observation; tradeoff; limitation; improvement.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A planned identity-provider outage during the synthetic capstone review.

**Practice and exercises:** Run the bounded fault trial, document service behavior and prioritize remaining work. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 29 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 30 of 30 (outline):** [← Chapter 29 (plan)](PLAN.md#ch-29) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

## Practical and assessment plan

Practice: implement an end-to-end service with monitored controls. Assessment: integration project, operational evidence and design review. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
