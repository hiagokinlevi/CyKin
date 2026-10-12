# Principal book plan — Incident response and cyber resilience / Technologist course / English

**One book for this course and language.** 30 curricular subjects are its chapters. Duration: 3 years; planned effort: approximately 2400 hours. Audience: Technology implementers and administrators. Entry knowledge: Computing foundations and introductory security operations. Intended outcome: integrate services, controls, operations and measurement in incident response and cyber resilience.

**Editorial state:** draft manuscript exists; release A4 validation and review pending. English reference edition. [Read the authored draft](MANUSCRIPT.md).

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 900-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response recommendations within cybersecurity risk management; it supersedes Rev. 2.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, testing and improvement.
- [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) — exercise design and evaluation; a 2006 publication whose applicability must be checked during authorship.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic techniques in response; a 2006 publication whose technical details need current verification.

These are source leads, not a finished chapter bibliography. Cite the relevant primary source beside each factual claim in the authored manuscript and identify any fictional case as synthetic.

## Contents and chapter summaries

These are editorial outlines. Each chapter summary ends with links to the previous position, the course index and the next position; a **draft** link opens authored teaching, while a **plan** link opens another outline.

<a id="ch-01"></a>

### Chapter 01 — Computing systems

**Stage 1; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-01)

**Teaching purpose and relevance:** Build a service-level view of the computing components an incident workflow must protect and restore.

**Concepts and techniques:** Compute roles; storage; service dependencies; change ownership; failure domain.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic municipal appointment service spread across three application hosts.

**Practice and exercises:** Draw its component map and identify which failure can delay response or recovery. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 01 of 30 (outline):** [← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](MANUSCRIPT.md#ch-02)

<a id="ch-02"></a>

### Chapter 02 — Networks and internet services

**Stage 1; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-02)

**Teaching purpose and relevance:** Explain how network services create evidence and operational dependencies for an integrated response service.

**Concepts and techniques:** Routing; DNS; transport; TLS endpoints; service availability; flow records.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional public portal and internal API with separate DNS and gateway owners.

**Practice and exercises:** Trace a request across services and name monitoring points and restoration dependencies. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 02 of 30 (outline):** [← Chapter 01 (draft)](MANUSCRIPT.md#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](MANUSCRIPT.md#ch-03)

<a id="ch-03"></a>

### Chapter 03 — Programming foundations

**Stage 1; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-03)

**Teaching purpose and relevance:** Use small programs to support repeatable case processing while keeping inputs and decisions inspectable.

**Concepts and techniques:** Data types; functions; validation; errors; tests; audit output.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic intake script that rejects incomplete incident forms.

**Practice and exercises:** Specify the parser, test malformed submissions and record rejected cases without losing originals. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 03 of 30 (outline):** [← Chapter 02 (draft)](MANUSCRIPT.md#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](MANUSCRIPT.md#ch-04)

<a id="ch-04"></a>

### Chapter 04 — Data models

**Stage 1; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-04)

**Teaching purpose and relevance:** Represent incident objects consistently across tools and teams so handoffs do not silently change meaning.

**Concepts and techniques:** Case ID; event schema; entity relation; version; provenance; retention.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional case record joined to identity events and service tickets.

**Practice and exercises:** Design a minimal case schema and show how two inconsistent fields are reconciled. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 04 of 30 (outline):** [← Chapter 03 (draft)](MANUSCRIPT.md#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](MANUSCRIPT.md#ch-05)

<a id="ch-05"></a>

### Chapter 05 — Security literacy

**Stage 1; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-05)

**Teaching purpose and relevance:** Connect foundational risk and control ideas to the practical choices an incident service makes.

**Concepts and techniques:** Asset; threat; vulnerability; impact; preventive and detective control; residual risk.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic alert concerning a staff account used by a critical scheduling system.

**Practice and exercises:** Explain the risk claim, its uncertainty and the control evidence needed before escalation. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 05 of 30 (outline):** [← Chapter 04 (draft)](MANUSCRIPT.md#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](MANUSCRIPT.md#ch-06)

<a id="ch-06"></a>

### Chapter 06 — Operating systems and virtualization

**Stage 2; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-06)

**Teaching purpose and relevance:** Map host and virtual-machine boundaries that affect collection, containment and recovery.

**Concepts and techniques:** Process; service; image; snapshot; host isolation; patch state.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic virtualized application with a shared hypervisor and two guest instances.

**Practice and exercises:** Compare guest-only and host-level evidence needs, then plan a reversible lab snapshot. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 06 of 30 (outline):** [← Chapter 05 (draft)](MANUSCRIPT.md#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](MANUSCRIPT.md#ch-07)

<a id="ch-07"></a>

### Chapter 07 — Identity and access foundations

**Stage 2; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-07)

**Teaching purpose and relevance:** Identify who can approve, perform and audit response actions in a multi-service environment.

**Concepts and techniques:** Principal; role; token; privilege; federation; access review.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional on-call rotation with service owners and a cloud administrator.

**Practice and exercises:** Build an access matrix for case review, containment approval and evidence storage. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 07 of 30 (outline):** [← Chapter 06 (draft)](MANUSCRIPT.md#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](MANUSCRIPT.md#ch-08)

<a id="ch-08"></a>

### Chapter 08 — Security architecture basics

**Stage 2; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-08)

**Teaching purpose and relevance:** Introduce trust boundaries and resilient design choices before integrating response controls.

**Concepts and techniques:** Trust zone; dependency; control plane; fail-safe path; design assumption.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic booking platform that shares identity services with another department.

**Practice and exercises:** Mark trust boundaries and compare where a monitoring or containment control belongs. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 08 of 30 (outline):** [← Chapter 07 (draft)](MANUSCRIPT.md#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](MANUSCRIPT.md#ch-09)

<a id="ch-09"></a>

### Chapter 09 — Evidence and measurement

**Stage 2; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-09)

**Teaching purpose and relevance:** Define what counts as defensible evidence and a useful measure of response performance.

**Concepts and techniques:** Provenance; integrity; denominator; timestamp; metric validity; uncertainty.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fabricated incident dashboard with missing case closure dates.

**Practice and exercises:** Audit two metrics, reconstruct denominators and flag unsupported claims. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 09 of 30 (outline):** [← Chapter 08 (draft)](MANUSCRIPT.md#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](MANUSCRIPT.md#ch-10)

<a id="ch-10"></a>

### Chapter 10 — Incident response service model and operating roles

**Stage 2; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-10)

**Teaching purpose and relevance:** Treat response as a managed service with defined customers, authority, handoffs and review points.

**Concepts and techniques:** Service catalog; responder role; escalation; approval; service-level objective.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic organization with SOC, IT operations and a service owner.

**Practice and exercises:** Draft a response service charter and assign responsibility for each major decision. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 10 of 30 (outline):** [← Chapter 09 (draft)](MANUSCRIPT.md#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](MANUSCRIPT.md#ch-11)

<a id="ch-11"></a>

### Chapter 11 — Asset inventory and business-service dependencies

**Stage 3; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-11)

**Teaching purpose and relevance:** Make inventory useful for decisions by linking technical assets to service outcomes and owners.

**Concepts and techniques:** Asset record; dependency graph; criticality; owner; recovery priority.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional health-clinic scheduling service dependent on identity, messaging and backups.

**Practice and exercises:** Build a dependency map and justify the order of preservation and recovery tasks. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 11 of 30 (outline):** [← Chapter 10 (draft)](MANUSCRIPT.md#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](MANUSCRIPT.md#ch-12)

<a id="ch-12"></a>

### Chapter 12 — Evidence flows across identity, endpoint and cloud

**Stage 3; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-12)

**Teaching purpose and relevance:** Connect telemetry from different platforms without treating every event as the same kind of proof.

**Concepts and techniques:** Source schema; collection path; join key; retention; access control.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** Synthetic identity sign-ins, endpoint alerts and cloud audit events for one case.

**Practice and exercises:** Design an evidence-flow diagram and identify missing links and privacy constraints. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares Chapter 13. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 12 of 30 (outline):** [← Chapter 11 (draft)](MANUSCRIPT.md#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](MANUSCRIPT.md#ch-13)

<a id="ch-13"></a>

### Chapter 13 — Incident risk scenarios and triage thresholds

**Stage 3; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-13)

**Teaching purpose and relevance:** Set defensible escalation thresholds that account for impact, confidence and response cost.

**Concepts and techniques:** Risk scenario; threshold; severity; false positive; review trigger.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic mass-login alert during a planned migration weekend.

**Practice and exercises:** Define triage rules, test boundary cases and explain when a human must override them. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 12 and prepares Chapter 14. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 13 of 30 (outline):** [← Chapter 12 (draft)](MANUSCRIPT.md#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](MANUSCRIPT.md#ch-14)

<a id="ch-14"></a>

### Chapter 14 — Case intake, scope and ownership methods

**Stage 3; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-14)

**Teaching purpose and relevance:** Turn incoming reports into scoped, accountable cases before action begins.

**Concepts and techniques:** Intake form; unique ID; authorization; owner assignment; initial hypothesis.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional help-desk ticket with incomplete system and reporter details.

**Practice and exercises:** Complete a bounded intake record and route missing facts to the right owner. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 13 and prepares Chapter 15. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 14 of 30 (outline):** [← Chapter 13 (draft)](MANUSCRIPT.md#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](MANUSCRIPT.md#ch-15)

<a id="ch-15"></a>

### Chapter 15 — Guided lab: reconstruct a bounded incident timeline

**Stage 3; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-15)

**Teaching purpose and relevance:** Practice combining technical and operational records into a reviewable case chronology.

**Concepts and techniques:** Time normalization; event linkage; evidence pointer; uncertainty; revision.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic log bundle and service ticket chain with clock offsets.

**Practice and exercises:** Reconstruct the timeline, show disputed ordering and submit a provenance note. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 14 and prepares Chapter 16. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 15 of 30 (outline):** [← Chapter 14 (draft)](MANUSCRIPT.md#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](MANUSCRIPT.md#ch-16)

<a id="ch-16"></a>

### Chapter 16 — Investigation methods across multiple data sources

**Stage 4; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-16)

**Teaching purpose and relevance:** Compare hypotheses using independent sources while keeping the investigation within authorization.

**Concepts and techniques:** Question tree; corroboration; sampling; alternative explanation; stop rule.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional account access anomaly with endpoint, network and cloud records.

**Practice and exercises:** Test two explanations, name the least invasive next check and record limits. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 15 and prepares Chapter 17. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 16 of 30 (outline):** [← Chapter 15 (draft)](MANUSCRIPT.md#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](MANUSCRIPT.md#ch-17)

<a id="ch-17"></a>

### Chapter 17 — Case-management and evidence-storage tooling

**Stage 4; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-17)

**Teaching purpose and relevance:** Specify a tool workflow that preserves case history, access boundaries and retrieval ability.

**Concepts and techniques:** Case state; audit log; retention; evidence manifest; permission model.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A simulated case platform with a shared attachment store and missing role separation.

**Practice and exercises:** Configure or model case states and permissions, then test an unauthorized-access scenario. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 16 and prepares Chapter 18. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 17 of 30 (outline):** [← Chapter 16 (draft)](MANUSCRIPT.md#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](MANUSCRIPT.md#ch-18)

<a id="ch-18"></a>

### Chapter 18 — Containment and recovery control implementation

**Stage 4; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-18)

**Teaching purpose and relevance:** Integrate scoped interventions with service validation and rollback rather than closing on one alert.

**Concepts and techniques:** Session revocation; access rule; restore check; change record; rollback.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** An isolated lab service with a compromised synthetic identity and dependency on a database.

**Practice and exercises:** Implement two reversible controls, measure impact and verify restoration criteria. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 17 and prepares Chapter 19. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 18 of 30 (outline):** [← Chapter 17 (draft)](MANUSCRIPT.md#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](MANUSCRIPT.md#ch-19)

<a id="ch-19"></a>

### Chapter 19 — Detection-to-response monitoring and feedback

**Stage 4; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-19)

**Teaching purpose and relevance:** Close the loop between alert production, case decisions and control improvement.

**Concepts and techniques:** Detection coverage; alert quality; response handoff; feedback owner; tuning metric.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional detection rule repeatedly opening duplicate cases.

**Practice and exercises:** Measure duplicate rate, revise the handoff and document the effect on triage time. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 18 and prepares Chapter 20. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 19 of 30 (outline):** [← Chapter 18 (draft)](MANUSCRIPT.md#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](MANUSCRIPT.md#ch-20)

<a id="ch-20"></a>

### Chapter 20 — Troubleshoot incomplete or contradictory case records

**Stage 4; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-20)

**Teaching purpose and relevance:** Diagnose workflow and telemetry defects before drawing stronger conclusions from a case.

**Concepts and techniques:** Missing field; duplicate event; clock skew; ownership gap; repair trace.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic case where the timeline conflicts with a change ticket.

**Practice and exercises:** Trace the inconsistency to its source, repair the record and preserve the original error. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 19 and prepares Chapter 21. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 20 of 30 (outline):** [← Chapter 19 (draft)](MANUSCRIPT.md#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](MANUSCRIPT.md#ch-21)

<a id="ch-21"></a>

### Chapter 21 — Integrate response with service management

**Stage 5; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-21)

**Teaching purpose and relevance:** Coordinate security work with change, incident and continuity processes across the organization.

**Concepts and techniques:** Service ticket; change approval; maintenance window; handoff; acceptance owner.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional containment request during a critical payroll processing window.

**Practice and exercises:** Design the coordination path and document approval, fallback and service acceptance. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 20 and prepares Chapter 22. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 21 of 30 (outline):** [← Chapter 20 (draft)](MANUSCRIPT.md#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](MANUSCRIPT.md#ch-22)

<a id="ch-22"></a>

### Chapter 22 — Automate repeatable evidence and notification tasks

**Stage 5; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-22)

**Teaching purpose and relevance:** Automate bounded support tasks while keeping authority, source records and human decisions explicit.

**Concepts and techniques:** Trigger; idempotence; allowlist; retry; audit log; manual gate.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A local workflow that copies approved synthetic logs and drafts a status message.

**Practice and exercises:** Specify and test failure paths, duplicate runs and the human approval checkpoint. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 21 and prepares Chapter 23. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 22 of 30 (outline):** [← Chapter 21 (draft)](MANUSCRIPT.md#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](MANUSCRIPT.md#ch-23)

<a id="ch-23"></a>

### Chapter 23 — Evaluate response latency and decision quality

**Stage 5; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-23)

**Teaching purpose and relevance:** Assess operational performance without rewarding rushed or unsupported case closure.

**Concepts and techniques:** Time-to-triage; time-to-contain; case quality; sampling bias; confidence.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fabricated month of cases with incomplete timestamps and varied severity.

**Practice and exercises:** Compute qualified metrics and explain how missing cases change the conclusion. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 22 and prepares Chapter 24. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 23 of 30 (outline):** [← Chapter 22 (draft)](MANUSCRIPT.md#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](MANUSCRIPT.md#ch-24)

<a id="ch-24"></a>

### Chapter 24 — Applied methods: compare two incident playbooks

**Stage 5; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-24)

**Teaching purpose and relevance:** Judge whether alternative playbooks lead to safe and auditable decisions in the same scenario.

**Concepts and techniques:** Precondition; branch; evidence checkpoint; rollback; stakeholder impact.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** Two synthetic credential-compromise playbooks with different approval gates.

**Practice and exercises:** Walk both through one case, compare tradeoffs and recommend a documented revision. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 23 and prepares Chapter 25. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 24 of 30 (outline):** [← Chapter 23 (draft)](MANUSCRIPT.md#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](MANUSCRIPT.md#ch-25)

<a id="ch-25"></a>

### Chapter 25 — Team studio: build and critique a response workflow

**Stage 5; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-25)

**Teaching purpose and relevance:** Combine service design, evidence flow, controls and people into one usable operating model.

**Concepts and techniques:** Workflow map; role handoff; interface; failure injection; peer review.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional small enterprise adding cloud and endpoint monitoring to an existing SOC.

**Practice and exercises:** Draft the workflow, run a peer failure review and revise ambiguous ownership. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 24 and prepares Chapter 26. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 25 of 30 (outline):** [← Chapter 24 (draft)](MANUSCRIPT.md#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](MANUSCRIPT.md#ch-26)

<a id="ch-26"></a>

### Chapter 26 — Operational handoff and communications practice

**Stage 6; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-26)

**Teaching purpose and relevance:** Ensure case decisions remain actionable and appropriately scoped when teams or shifts change.

**Concepts and techniques:** Handoff minimum; audience; fact versus hypothesis; status cadence; privacy.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A staged incident crossing an on-call shift and a service-owner briefing.

**Practice and exercises:** Prepare a technical handoff and a plain-language update, then test both for omissions. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 25 and prepares Chapter 27. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 26 of 30 (outline):** [← Chapter 25 (draft)](MANUSCRIPT.md#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](MANUSCRIPT.md#ch-27)

<a id="ch-27"></a>

### Chapter 27 — Deploy and validate an incident case workflow

**Stage 6; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-27)

**Teaching purpose and relevance:** Verify that an implemented workflow preserves evidence, approvals and recoverability under normal and failed paths.

**Concepts and techniques:** Configuration baseline; acceptance test; audit trail; failure test; rollback.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** An isolated case-management sandbox with role-based access and synthetic events.

**Practice and exercises:** Deploy the workflow, test authorized and unauthorized paths, and record acceptance evidence. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 26 and prepares Chapter 28. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 27 of 30 (outline):** [← Chapter 26 (draft)](MANUSCRIPT.md#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](MANUSCRIPT.md#ch-28)

<a id="ch-28"></a>

### Chapter 28 — Field simulation with authorized stakeholders

**Stage 6; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-28)

**Teaching purpose and relevance:** Exercise the integrated service under changing evidence and stakeholder constraints without affecting live systems.

**Concepts and techniques:** Simulation objective; inject; observer rubric; escalation; stop condition.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A synthetic cross-team incident involving a cloud account and a public service.

**Practice and exercises:** Run a tabletop, log decisions and assess handoffs against preagreed criteria. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 27 and prepares Chapter 29. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 28 of 30 (outline):** [← Chapter 27 (draft)](MANUSCRIPT.md#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](MANUSCRIPT.md#ch-29)

<a id="ch-29"></a>

### Chapter 29 — Capstone: integrated response and recovery service

**Stage 6; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-29)

**Teaching purpose and relevance:** Demonstrate a complete designed service from alert intake through safe return to operation.

**Concepts and techniques:** Architecture; case workflow; telemetry; containment; recovery; documentation.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** A fictional regional appointment platform with identity and database dependencies.

**Practice and exercises:** Build the service design, run a bounded simulated case and submit the evidence dossier. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 28 and prepares Chapter 30. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 29 of 30 (outline):** [← Chapter 28 (draft)](MANUSCRIPT.md#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](MANUSCRIPT.md#ch-30)

<a id="ch-30"></a>

### Chapter 30 — Capstone evaluation and improvement dossier

**Stage 6; 30 planned A4 pages; 3 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-30)

**Teaching purpose and relevance:** Evaluate the capstone's claims and turn observed shortcomings into measurable changes.

**Concepts and techniques:** Acceptance result; failure analysis; limitation; improvement owner; reassessment plan.

**Depth and method:** At technologist course level, learners will implement an end-to-end service with monitored controls. Integrate services and teams, then measure whether the implemented workflow meets acceptance criteria.

**Worked example:** The capstone artifacts, observer notes and synthetic service metrics.

**Practice and exercises:** Defend design choices, quantify unresolved risks and prioritize the next release's improvements. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 29 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 30 of 30 (outline):** [← Chapter 29 (draft)](MANUSCRIPT.md#ch-29) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

## Practical and assessment plan

Practice: implement an end-to-end service with monitored controls. Assessment: integration project, operational evidence and design review. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
