# Principal book plan — Incident response and cyber resilience / Engineering course / English

**One book for this course and language.** 50 curricular subjects are its chapters. Duration: 5 years; planned effort: approximately 4000 hours. Audience: Security systems designers. Entry knowledge: Calculus, computing, networks and systems engineering. Intended outcome: design, build and validate complex systems under constraints in incident response and cyber resilience.

**Editorial state:** structured outline; manuscript not yet authored. English reference edition.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 1500-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response recommendations within cybersecurity risk management; it supersedes Rev. 2.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, testing and improvement.
- [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) — exercise design and evaluation; a 2006 publication whose applicability must be checked during authorship.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic techniques in response; a 2006 publication whose technical details need current verification.

These are source leads, not a finished chapter bibliography. Cite the relevant primary source beside each factual claim in the authored manuscript and identify any fictional case as synthetic.

## Contents and chapter summaries

<a id="ch-01"></a>

### Chapter 01 — Calculus I

**Stage 1; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use rates and change to reason about time-dependent service and response behavior.

**Concepts and techniques:** Function; derivative; rate; unit; sensitivity.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic incident queue whose arrival rate changes during a service outage.

**Practice and exercises:** Model the rate, identify assumptions and explain where a simple derivative misleads. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

<a id="ch-02"></a>

### Chapter 02 — Discrete mathematics

**Stage 1; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Represent response workflows and authorization constraints as checkable structures.

**Concepts and techniques:** Graph; relation; logic; state; invariant.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional approval graph for several responder roles and systems.

**Practice and exercises:** Formalize valid action paths and find an invalid authorization transition. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

<a id="ch-03"></a>

### Chapter 03 — Physics for computing

**Stage 1; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Connect physical resource limits to computing failures that affect monitoring and recovery.

**Concepts and techniques:** Energy; heat; storage medium; signal; measurement error.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic edge device that drops telemetry during thermal throttling.

**Practice and exercises:** Explain a plausible physical failure chain and propose measurable checks. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

<a id="ch-04"></a>

### Chapter 04 — Programming I

**Stage 1; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build small, inspectable programs that preserve input evidence and expose failures.

**Concepts and techniques:** Variables; function; validation; test; deterministic output.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A local parser for synthetic case-intake records.

**Practice and exercises:** Implement input validation and show that rejected records remain available for review. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

<a id="ch-05"></a>

### Chapter 05 — Engineering communication

**Stage 1; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Document decisions so requirements, evidence and limitations can be reviewed across disciplines.

**Concepts and techniques:** Requirement statement; traceability; diagram; risk note; audience.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional response design brief with vague claims and missing owners.

**Practice and exercises:** Rewrite the brief as testable requirements and present its unresolved assumptions. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

<a id="ch-06"></a>

### Chapter 06 — Calculus II

**Stage 2; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Analyze accumulated workload and recovery trajectories rather than only instantaneous rates.

**Concepts and techniques:** Integral; accumulation; model fit; boundary condition.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic incident backlog with periods of increased intake and staffing.

**Practice and exercises:** Estimate accumulated delay and explain how model assumptions affect capacity planning. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

<a id="ch-07"></a>

### Chapter 07 — Probability and statistics

**Stage 2; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Estimate detection and response performance with uncertainty and sampling limits.

**Concepts and techniques:** Distribution; conditional probability; interval; bias; significance.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fabricated set of alert and case outcomes with uneven severity.

**Practice and exercises:** Compute defensible measures and identify which comparisons are confounded. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

<a id="ch-08"></a>

### Chapter 08 — Computer architecture

**Stage 2; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Explain how hardware and isolation boundaries affect evidence acquisition and service recovery.

**Concepts and techniques:** Processor; memory; firmware; storage; virtualization boundary.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic host with a virtualized workload and a shared storage device.

**Practice and exercises:** Map evidence-bearing components and compare collection costs and risks. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

<a id="ch-09"></a>

### Chapter 09 — Programming II

**Stage 2; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Design robust data-processing components that can be tested under error conditions.

**Concepts and techniques:** Structured data; module; exception; property test; provenance.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic event-normalization service receiving malformed and duplicate records.

**Practice and exercises:** Implement or review the module and demonstrate predictable failure behavior. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

<a id="ch-10"></a>

### Chapter 10 — Engineering ethics and safety

**Stage 2; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Embed authorization, privacy and service safety into engineering decisions and tests.

**Concepts and techniques:** Duty of care; least privilege; consent; harm; stop criterion.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional request to isolate a critical care scheduling service.

**Practice and exercises:** Define safety gates and an escalation path before approving a simulated intervention. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

<a id="ch-11"></a>

### Chapter 11 — Networks and protocols

**Stage 3; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Trace communication paths and protocol assumptions relevant to evidence and containment.

**Concepts and techniques:** Routing; DNS; TLS; session; packet loss; time source.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic multi-zone application with a gateway and remote identity service.

**Practice and exercises:** Map the path and identify which logs can support a connection claim. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

<a id="ch-12"></a>

### Chapter 12 — Operating systems

**Stage 3; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Model host state, permissions and logs before designing collection or response agents.

**Concepts and techniques:** Process; service; file permission; event; update; kernel boundary.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional workstation with scheduled tasks and two service accounts.

**Practice and exercises:** Compare expected and anomalous behavior and specify safe observation points. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares Chapter 13. This is an editorial brief, not a completed lesson.

<a id="ch-13"></a>

### Chapter 13 — Data systems

**Stage 3; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Treat databases and storage as sources of evidence and as services needing integrity checks.

**Concepts and techniques:** Transaction; schema; backup; consistency; retention; access control.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic case store and booking database with different recovery points.

**Practice and exercises:** Design integrity checks and order restoration steps under a stated objective. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 12 and prepares Chapter 14. This is an editorial brief, not a completed lesson.

<a id="ch-14"></a>

### Chapter 14 — Software engineering

**Stage 3; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Apply requirements and tests to response tooling so changes do not erase evidence or bypass controls.

**Concepts and techniques:** Interface; version; test; review; deployment; rollback.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional evidence-ingest change that silently drops unknown event fields.

**Practice and exercises:** Write acceptance tests and a release plan that detect the regression. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 13 and prepares Chapter 15. This is an editorial brief, not a completed lesson.

<a id="ch-15"></a>

### Chapter 15 — Security fundamentals

**Stage 3; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Translate threat models and control properties into engineering claims and verification tasks.

**Concepts and techniques:** Asset; adversary capability; control; residual risk; assurance.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic account-compromise scenario spanning several services.

**Practice and exercises:** State security properties and identify evidence that would support each one. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 14 and prepares Chapter 16. This is an editorial brief, not a completed lesson.

<a id="ch-16"></a>

### Chapter 16 — Systems engineering

**Stage 4; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use lifecycle and dependency methods to manage an incident service as a complex system.

**Concepts and techniques:** Stakeholder; requirement; architecture; interface; verification; operations.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional organization deploying one response platform across several teams.

**Practice and exercises:** Build a requirements trace from stakeholder need to acceptance test. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 15 and prepares Chapter 17. This is an editorial brief, not a completed lesson.

<a id="ch-17"></a>

### Chapter 17 — Control and feedback basics

**Stage 4; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Understand when a response control improves the system and when feedback causes instability or blind spots.

**Concepts and techniques:** Feedback loop; delay; threshold; oscillation; observability.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A simulated automated alert-to-containment loop with noisy signals.

**Practice and exercises:** Model the loop and identify a safe human gate and stability measure. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 16 and prepares Chapter 18. This is an editorial brief, not a completed lesson.

<a id="ch-18"></a>

### Chapter 18 — Security architecture

**Stage 4; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Compare trust boundaries and control placement for an evidence-preserving response system.

**Concepts and techniques:** Trust zone; separation; control plane; logging; recovery path.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Two synthetic architectures for the same case-management service.

**Practice and exercises:** Choose a design under explicit threat and availability constraints. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 17 and prepares Chapter 19. This is an editorial brief, not a completed lesson.

<a id="ch-19"></a>

### Chapter 19 — Identity and cryptography

**Stage 4; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use identity and cryptographic properties to support authentic access and evidence integrity.

**Concepts and techniques:** Authentication; authorization; hash; signature; key lifecycle.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional evidence store with signed manifests and shared administrator access.

**Practice and exercises:** Evaluate which claims signatures support and where role separation remains necessary. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 18 and prepares Chapter 20. This is an editorial brief, not a completed lesson.

<a id="ch-20"></a>

### Chapter 20 — Incident response engineering context and constraints

**Stage 4; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Frame incident response as a system design problem bounded by authority, time, evidence and service continuity.

**Concepts and techniques:** Mission; stakeholder; constraint; risk; regulatory interface; safety.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic public-service organization with limited telemetry and strict uptime needs.

**Practice and exercises:** Produce a context diagram and a prioritized constraint register. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 19 and prepares Chapter 21. This is an editorial brief, not a completed lesson.

<a id="ch-21"></a>

### Chapter 21 — Response system requirements and service objectives

**Stage 5; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Convert broad response aims into measurable properties and acceptance criteria.

**Concepts and techniques:** Functional requirement; service objective; latency; integrity; auditability.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional procurement brief promising rapid response without defined evidence quality.

**Practice and exercises:** Write testable requirements and flag mutually conflicting objectives. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 20 and prepares Chapter 22. This is an editorial brief, not a completed lesson.

<a id="ch-22"></a>

### Chapter 22 — Incident data, telemetry and provenance models

**Stage 5; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Design a data model that preserves origin and transformation history across response tools.

**Concepts and techniques:** Event schema; entity key; timestamp; lineage; retention; integrity.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Synthetic identity, host and cloud events with mismatched identifiers.

**Practice and exercises:** Specify normalization rules and trace one decision back to source records. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 21 and prepares Chapter 23. This is an editorial brief, not a completed lesson.

<a id="ch-23"></a>

### Chapter 23 — Threat and failure analysis for response systems

**Stage 5; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Analyze both adversarial abuse and ordinary failure of response infrastructure.

**Concepts and techniques:** Threat model; fault tree; single point of failure; misuse case; mitigation.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional case platform whose notification service and evidence store share credentials.

**Practice and exercises:** Build threat and failure trees and compare mitigations against service constraints. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 22 and prepares Chapter 24. This is an editorial brief, not a completed lesson.

<a id="ch-24"></a>

### Chapter 24 — Evidence pipeline and decision-support methods

**Stage 5; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Design an evidence path that makes triage recommendations inspectable and reversible.

**Concepts and techniques:** Ingestion; validation; scoring; provenance; human review; rollback.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic alert-ranking pipeline that drops records with unknown fields.

**Practice and exercises:** Specify pipeline checks and test how omissions change a responder's decision. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 23 and prepares Chapter 25. This is an editorial brief, not a completed lesson.

<a id="ch-25"></a>

### Chapter 25 — Design studio: case intake and authorization model

**Stage 5; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Integrate roles, case states and permission gates into a reviewable design artifact.

**Concepts and techniques:** State machine; approval; escalation; access matrix; audit event.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional multi-tenant response service with shared and tenant-specific responders.

**Practice and exercises:** Design the intake state machine and review illegal transitions with peers. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 24 and prepares Chapter 26. This is an editorial brief, not a completed lesson.

<a id="ch-26"></a>

### Chapter 26 — Alternative containment and recovery architectures

**Stage 6; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Compare architectures that trade intervention speed against availability, evidence and rollback.

**Concepts and techniques:** Isolation boundary; failover; blast radius; restore path; residual risk.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Two synthetic designs for containing a compromised identity service.

**Practice and exercises:** Model failure modes and defend a choice against explicit service objectives. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 25 and prepares Chapter 27. This is an editorial brief, not a completed lesson.

<a id="ch-27"></a>

### Chapter 27 — Control design for scoped intervention

**Stage 6; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Engineer containment controls that act only within authorization and expose their effects.

**Concepts and techniques:** Policy rule; scope check; approval gate; observability; reversibility.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A lab service with a suspect account and a protected unrelated tenant.

**Practice and exercises:** Specify the control and test that it cannot affect the unrelated tenant. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 26 and prepares Chapter 28. This is an editorial brief, not a completed lesson.

<a id="ch-28"></a>

### Chapter 28 — Implementation of evidence capture services

**Stage 6; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build a collection service that preserves source integrity and records every transformation.

**Concepts and techniques:** Read-only input; manifest; checksum; access log; failure recovery.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** An isolated synthetic event source and evidence storage endpoint.

**Practice and exercises:** Implement a bounded capture path and verify provenance under interrupted transfer. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 27 and prepares Chapter 29. This is an editorial brief, not a completed lesson.

<a id="ch-29"></a>

### Chapter 29 — Measure triage accuracy and response latency

**Stage 6; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Evaluate whether an engineered workflow improves both decision quality and timeliness.

**Concepts and techniques:** Precision; recall; latency distribution; case mix; missing data.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic before-and-after dataset from two triage workflow versions.

**Practice and exercises:** Define the population, compute measures and perform a sensitivity check. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 28 and prepares Chapter 30. This is an editorial brief, not a completed lesson.

<a id="ch-30"></a>

### Chapter 30 — Verification lab: evidence preservation invariants

**Stage 6; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Test properties that must hold even when inputs are malformed or services fail.

**Concepts and techniques:** Invariant; immutable raw copy; idempotence; audit completeness; fault injection.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A lab evidence pipeline receiving duplicate, delayed and corrupted records.

**Practice and exercises:** Write and run invariant tests and explain each failed case. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 29 and prepares Chapter 31. This is an editorial brief, not a completed lesson.

<a id="ch-31"></a>

### Chapter 31 — Implement incident workflow orchestration

**Stage 7; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Coordinate tasks across teams without automating decisions outside delegated authority.

**Concepts and techniques:** Workflow engine; human task; retry; timeout; escalation; audit trail.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic case moving through triage, approval, containment and closure.

**Practice and exercises:** Implement the state transitions and show behavior on approval timeout. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 30 and prepares Chapter 32. This is an editorial brief, not a completed lesson.

<a id="ch-32"></a>

### Chapter 32 — Reliability engineering for response tooling

**Stage 7; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Design response tools to remain usable when dependencies fail during an incident.

**Concepts and techniques:** Availability objective; redundancy; queue; degradation; recovery time.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional alert broker outage during a high-volume case period.

**Practice and exercises:** Measure the failure effect and design a tested degraded operating mode. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 31 and prepares Chapter 33. This is an editorial brief, not a completed lesson.

<a id="ch-33"></a>

### Chapter 33 — Safety and resilience under partial failure

**Stage 7; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Prevent a partial response-system failure from turning a controlled action into broader service harm.

**Concepts and techniques:** Fail-safe state; circuit breaker; isolation; monitoring; manual override.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A lab containment controller that loses contact with its policy service.

**Practice and exercises:** Define safe behavior and test automatic and manual recovery paths. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 32 and prepares Chapter 34. This is an editorial brief, not a completed lesson.

<a id="ch-34"></a>

### Chapter 34 — Integrate identity, endpoint and cloud response

**Stage 7; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Engineer interfaces that connect different control planes while respecting their own authorization and evidence rules.

**Concepts and techniques:** API boundary; permission; event correlation; provider limit; rollback.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic account incident observed in identity, endpoint and cloud logs.

**Practice and exercises:** Build an integration diagram and validate a cross-platform case trace. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 33 and prepares Chapter 35. This is an editorial brief, not a completed lesson.

<a id="ch-35"></a>

### Chapter 35 — Design studio: coordinated recovery exercise

**Stage 7; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Design a recovery exercise whose success depends on service and evidence acceptance, not merely uptime.

**Concepts and techniques:** Dependency order; restore point; business owner; test; fallback.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional regional portal with a database, identity service and messaging queue.

**Practice and exercises:** Prepare an exercise plan, simulate a failed restore and revise the sequence. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 34 and prepares Chapter 36. This is an editorial brief, not a completed lesson.

<a id="ch-36"></a>

### Chapter 36 — Performance and scale of event pipelines

**Stage 8; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Assess how throughput, delay and data loss affect response decisions at scale.

**Concepts and techniques:** Arrival rate; backpressure; batching; loss; storage budget.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Synthetic telemetry from multiple services during an incident spike.

**Practice and exercises:** Model capacity and test whether delayed events change case severity. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 35 and prepares Chapter 37. This is an editorial brief, not a completed lesson.

<a id="ch-37"></a>

### Chapter 37 — Operating a response system with auditability

**Stage 8; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Translate a tested design into monitored operations with accountability for changes.

**Concepts and techniques:** Runbook; operator role; change record; service metric; audit log.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A simulated response service with rotating on-call staff and monthly releases.

**Practice and exercises:** Create an operations plan and audit one unauthorized configuration change. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 36 and prepares Chapter 38. This is an editorial brief, not a completed lesson.

<a id="ch-38"></a>

### Chapter 38 — Validate containment and restoration claims

**Stage 8; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Require measurable evidence that a response action achieved its intended security and service outcomes.

**Concepts and techniques:** Acceptance criterion; negative test; monitoring window; residual risk.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic incident in which account access is blocked but a token remains active.

**Practice and exercises:** Design verification tests and document a claim that cannot yet be supported. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 37 and prepares Chapter 39. This is an editorial brief, not a completed lesson.

<a id="ch-39"></a>

### Chapter 39 — Maintainability and change control for playbooks

**Stage 8; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Keep procedures accurate as tools, roles and dependencies change.

**Concepts and techniques:** Version; owner; trigger; regression test; deprecation; review date.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A fictional response playbook whose cloud commands and approval chain are outdated.

**Practice and exercises:** Revise the playbook and create a test and review schedule. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 38 and prepares Chapter 40. This is an editorial brief, not a completed lesson.

<a id="ch-40"></a>

### Chapter 40 — Verification lab: failure injection and recovery

**Stage 8; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Demonstrate how engineered controls behave under planned faults without touching production.

**Concepts and techniques:** Fault injection; stop condition; observation; rollback; reproducibility.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** An isolated workflow service with a simulated evidence-store outage.

**Practice and exercises:** Run a bounded fault test and compare observed behavior with design claims. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 39 and prepares Chapter 41. This is an editorial brief, not a completed lesson.

<a id="ch-41"></a>

### Chapter 41 — Optimize decisions with measured tradeoffs

**Stage 9; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use explicit objectives and uncertainty rather than a single speed metric to choose response policies.

**Concepts and techniques:** Multi-objective choice; sensitivity; constraint; cost of error.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Three synthetic containment policies with different disruption and risk profiles.

**Practice and exercises:** Build a decision table and show where a small assumption change reverses the choice. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 40 and prepares Chapter 42. This is an editorial brief, not a completed lesson.

<a id="ch-42"></a>

### Chapter 42 — Applied research on response-system limits

**Stage 9; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Investigate where the designed system stops supporting reliable conclusions or action.

**Concepts and techniques:** Boundary condition; baseline; experiment; external validity; reproducibility.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic study of case quality under delayed or missing telemetry.

**Practice and exercises:** Formulate a testable limit claim and design a reproducible experiment. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 41 and prepares Chapter 43. This is an editorial brief, not a completed lesson.

<a id="ch-43"></a>

### Chapter 43 — Industry or public-service response practicum

**Stage 9; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Apply engineering methods in an authorized setting with service owners and documented safeguards.

**Concepts and techniques:** Scope agreement; stakeholder need; observation; safety; feedback.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A supervised simulation for a fictional public-service operator.

**Practice and exercises:** Produce an approved plan, execute the exercise and record operational feedback. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 42 and prepares Chapter 44. This is an editorial brief, not a completed lesson.

<a id="ch-44"></a>

### Chapter 44 — Engineering capstone: design and build

**Stage 9; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build a response system whose requirements, architecture, interfaces and tests are traceable.

**Concepts and techniques:** Design dossier; implementation; dependency; acceptance test; risk register.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A synthetic multi-service organization needing case intake and evidence preservation.

**Practice and exercises:** Implement the bounded system and submit design-to-test traceability. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 43 and prepares Chapter 45. This is an editorial brief, not a completed lesson.

<a id="ch-45"></a>

### Chapter 45 — Independent review of security and safety claims

**Stage 9; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Invite critical challenge to the capstone before interpreting its trial as success.

**Concepts and techniques:** Claim-evidence matrix; reviewer independence; safety case; defect triage.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** The capstone design dossier and an external peer-review checklist.

**Practice and exercises:** Respond to findings, reproduce failures and amend unsupported claims. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 44 and prepares Chapter 46. This is an editorial brief, not a completed lesson.

<a id="ch-46"></a>

### Chapter 46 — Engineering capstone: trial and iteration

**Stage 10; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Run the capstone under controlled scenarios and revise design based on measured failures.

**Concepts and techniques:** Trial protocol; instrumentation; defect; iteration; change impact.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Several synthetic incidents with differing telemetry and approval delays.

**Practice and exercises:** Execute the protocol, prioritize defects and rerun acceptance tests. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 45 and prepares Chapter 47. This is an editorial brief, not a completed lesson.

<a id="ch-47"></a>

### Chapter 47 — Failure and recovery trial with reproducible data

**Stage 10; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Validate resilience claims using a recorded fault and restoration sequence.

**Concepts and techniques:** Failure mode; seed data; restore point; repeatability; residual risk.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A simulated evidence-store failure during an active incident case.

**Practice and exercises:** Publish the lab inputs, reproduce recovery and compare results with objectives. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 46 and prepares Chapter 48. This is an editorial brief, not a completed lesson.

<a id="ch-48"></a>

### Chapter 48 — Evidence dossier and acceptance tests

**Stage 10; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Assemble verifiable evidence that the built system satisfies each approved requirement.

**Concepts and techniques:** Requirement ID; test result; log artifact; exception; reviewer sign-off.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** Capstone implementation records, test outputs and unresolved defects.

**Practice and exercises:** Build the evidence dossier and flag every requirement without adequate proof. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 47 and prepares Chapter 49. This is an editorial brief, not a completed lesson.

<a id="ch-49"></a>

### Chapter 49 — Engineering thesis on response performance

**Stage 10; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Interpret the capstone's measured performance and limitations as an engineering contribution.

**Concepts and techniques:** Method; baseline; result; uncertainty; generalizability; future work.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** A reproducible evaluation of the student's response workflow.

**Practice and exercises:** Write a thesis that links design decisions to outcomes and openly reports failures. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 48 and prepares Chapter 50. This is an editorial brief, not a completed lesson.

<a id="ch-50"></a>

### Chapter 50 — Final defense of design and measured results

**Stage 10; 30 planned A4 pages; 1 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Defend system choices under technical and operational critique using traceable evidence.

**Concepts and techniques:** Design rationale; safety argument; alternative; evidence; revision.

**Depth and method:** At engineering course level, learners will model tradeoffs, implement controls and test failure modes. Trace requirements through design, implementation, verification and measured failure modes.

**Worked example:** The completed capstone dossier and independent review comments.

**Practice and exercises:** Present the system, answer counterexamples and record required revisions. The planned allocation is 1 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 49 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

## Practical and assessment plan

Practice: model tradeoffs, implement controls and test failure modes. Assessment: design dossier, verification results and engineering thesis. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
