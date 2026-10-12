# Principal book plan — Cybersecurity / Technical course / English

**One book for this course and language.** 18 curricular subjects are its chapters. Duration: 18 months; planned effort: approximately 1200 hours. Audience: Technical operators. Entry knowledge: Networks, operating systems, scripting and safe lab practice. Intended outcome: diagnose failures, configure controls and verify outcomes in cybersecurity.

**Editorial state:** structured outline; manuscript not yet authored. English reference edition.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 540-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) — a taxonomy of security outcomes and a source for discussing organizational risk; it does not prescribe a single implementation.
- [NIST CSF 2.0 FAQ](https://www.nist.gov/cyberframework/faqs) — explanations of framework components and the Govern function.
- [NIST SP 800-53 Rev. 5 publication and current control-catalog update](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — a flexible security and privacy control catalog. Check the linked newer catalog release before citing specific controls; framework mappings are not automatic equivalences.

These sources guide the English teaching plan. The Harbor Library case is synthetic; factual claims in authored lessons need source-specific citations.

## Contents and chapter summaries

These are editorial outlines. Each chapter summary ends with links to the previous position, the course index and the next position; a **draft** link opens authored teaching, while a **plan** link opens another outline.

<a id="ch-01"></a>

### Chapter 01 — Computing and service architecture

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Establish the system model required to troubleshoot security observations across a service.

**Concepts and techniques:** Component; interface; dependency; failure domain; inventory.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A synthetic library booking application with an API and database.

**Practice and exercises:** Map components and identify which changes could affect both evidence and availability. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 01 of 18 (outline):** [← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (plan) →](PLAN.md#ch-02)

<a id="ch-02"></a>

### Chapter 02 — Networks and protocols

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Interpret traffic and service behavior before labeling a connection suspicious.

**Concepts and techniques:** Addressing; DNS; transport; TLS; flow record; packet limit.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** Sanitized client, gateway and DNS records for the synthetic library.

**Practice and exercises:** Trace one request and name observations that would confirm the path. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 02 of 18 (outline):** [← Chapter 01 (plan)](PLAN.md#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (plan) →](PLAN.md#ch-03)

<a id="ch-03"></a>

### Chapter 03 — Operating systems and identities

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Relate account privileges and host activity to safe control configuration.

**Concepts and techniques:** Process; user; service account; permission; event log.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** Fictional staff workstation records and an application service account.

**Practice and exercises:** Compare expected maintenance activity with an unexplained privilege change. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 03 of 18 (outline):** [← Chapter 02 (plan)](PLAN.md#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (plan) →](PLAN.md#ch-04)

<a id="ch-04"></a>

### Chapter 04 — Scripting and data formats

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use bounded scripts to normalize evidence without hiding malformed inputs.

**Concepts and techniques:** CSV; JSON; parser; validation; checksum; deterministic output.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A small synthetic log bundle with duplicate event IDs.

**Practice and exercises:** Create a normalized view and an error report while preserving raw records. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 04 of 18 (outline):** [← Chapter 03 (plan)](PLAN.md#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (plan) →](PLAN.md#ch-05)

<a id="ch-05"></a>

### Chapter 05 — Security scope and evidence

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Connect written permission to actual collection and configuration steps.

**Concepts and techniques:** Approved asset; allowed command; stop condition; provenance; access log.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A fictional lab authorization that excludes the production booking service.

**Practice and exercises:** Prepare a scoped checklist and identify which proposed steps must be refused. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 05 of 18 (outline):** [← Chapter 04 (plan)](PLAN.md#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (plan) →](PLAN.md#ch-06)

<a id="ch-06"></a>

### Chapter 06 — Assets, services and trust boundaries

**Stage 1; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Find the technical and human boundaries that determine where a control belongs.

**Concepts and techniques:** Asset; data flow; principal; trust zone; owner.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A synthetic library service with resident, staff and administrator paths.

**Practice and exercises:** Draw the trust-boundary diagram and identify one boundary with excessive access. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 06 of 18 (outline):** [← Chapter 05 (plan)](PLAN.md#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (plan) →](PLAN.md#ch-07)

<a id="ch-07"></a>

### Chapter 07 — Security signal sources and data quality

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Evaluate whether telemetry supports the claimed detection or leaves blind spots.

**Concepts and techniques:** Log schema; collection path; retention; completeness; clock.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** Fictional identity, application and network records with one missing source.

**Practice and exercises:** Build a source-quality matrix and prioritize a bounded collection improvement. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 07 of 18 (outline):** [← Chapter 06 (plan)](PLAN.md#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (plan) →](PLAN.md#ch-08)

<a id="ch-08"></a>

### Chapter 08 — Threat, weakness and failure distinctions

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Avoid treating service faults, exploitable weaknesses and confirmed misuse as synonyms.

**Concepts and techniques:** Failure mode; vulnerability; threat; observation; alternative hypothesis.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A synthetic booking outage during a password reset campaign.

**Practice and exercises:** Construct competing explanations and identify the next least invasive check. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 08 of 18 (outline):** [← Chapter 07 (plan)](PLAN.md#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (plan) →](PLAN.md#ch-09)

<a id="ch-09"></a>

### Chapter 09 — Safe configuration and inspection methods

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Inspect a system state and propose changes without risking uncontrolled disruption.

**Concepts and techniques:** Baseline; read-only query; change window; rollback; audit note.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** An isolated training service with an unknown access setting.

**Practice and exercises:** Capture baseline evidence, inspect settings and draft a reversible change. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 09 of 18 (outline):** [← Chapter 08 (plan)](PLAN.md#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (plan) →](PLAN.md#ch-10)

<a id="ch-10"></a>

### Chapter 10 — Access and baseline control configuration

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Configure a narrow control and verify expected behavior for authorized and unauthorized users.

**Concepts and techniques:** Least privilege; access rule; exception; configuration drift; test.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A lab booking-admin role with excess export permission.

**Practice and exercises:** Reduce the role, test allowed tasks and record any broken workflow. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 10 of 18 (outline):** [← Chapter 09 (plan)](PLAN.md#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (plan) →](PLAN.md#ch-11)

<a id="ch-11"></a>

### Chapter 11 — Control testing and evidence quality

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Test whether a control meets its objective rather than inferring success from its presence.

**Concepts and techniques:** Control claim; acceptance test; negative test; evidence; limitation.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A synthetic MFA policy shown as enabled but with an unreviewed exception.

**Practice and exercises:** Design tests and state which results would falsify the effectiveness claim. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 11 of 18 (outline):** [← Chapter 10 (plan)](PLAN.md#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (plan) →](PLAN.md#ch-12)

<a id="ch-12"></a>

### Chapter 12 — Laboratory: map a synthetic service and its controls

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Integrate inventory, trust boundaries, telemetry and control checks in a reproducible lab.

**Concepts and techniques:** Service map; control inventory; test log; gap; authorization.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A provided fictional booking environment with sanitized configuration exports.

**Practice and exercises:** Build the map, run bounded checks and submit evidence-backed findings. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares Chapter 13. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 12 of 18 (outline):** [← Chapter 11 (plan)](PLAN.md#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (plan) →](PLAN.md#ch-13)

<a id="ch-13"></a>

### Chapter 13 — Investigate inconsistent security signals

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Troubleshoot conflicting alerts before escalating a stronger security claim.

**Concepts and techniques:** Rule input; sensor health; time offset; duplicate; false positive.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** Two fictional dashboards disagree about a staff account session.

**Practice and exercises:** Trace source records and explain the uncertainty that remains. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 12 and prepares Chapter 14. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 13 of 18 (outline):** [← Chapter 12 (plan)](PLAN.md#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (plan) →](PLAN.md#ch-14)

<a id="ch-14"></a>

### Chapter 14 — Scripted control checks with bounded inputs

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Automate a repeatable verification while retaining human review and safe failure behavior.

**Concepts and techniques:** Allowlist; idempotence; error path; audit log; manual gate.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A local script checking approved synthetic access rules.

**Practice and exercises:** Run normal and malformed cases and compare its output with manual inspection. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 13 and prepares Chapter 15. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 14 of 18 (outline):** [← Chapter 13 (plan)](PLAN.md#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (plan) →](PLAN.md#ch-15)

<a id="ch-15"></a>

### Chapter 15 — Cross-service control dependencies

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Show that a safeguard in one component can affect another service or fail at an interface.

**Concepts and techniques:** Dependency graph; shared identity; fallback; control inheritance.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A synthetic library and community portal sharing an identity provider.

**Practice and exercises:** Trace the impact of an account-policy change and design a regression test. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 14 and prepares Chapter 16. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 15 of 18 (outline):** [← Chapter 14 (plan)](PLAN.md#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (plan) →](PLAN.md#ch-16)

<a id="ch-16"></a>

### Chapter 16 — Technical documentation and safety

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Write procedures that another operator can reproduce without exceeding scope.

**Concepts and techniques:** Precondition; owner; step; expected output; stop rule; rollback.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A fictional hardening instruction with no validation or recovery plan.

**Practice and exercises:** Revise the procedure and perform a peer walk-through of failure cases. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 15 and prepares Chapter 17. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 16 of 18 (outline):** [← Chapter 15 (plan)](PLAN.md#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (plan) →](PLAN.md#ch-17)

<a id="ch-17"></a>

### Chapter 17 — Laboratory: compare prevention, detection and recovery

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Evaluate a small set of controls together against one service scenario.

**Concepts and techniques:** Preventive rule; alert; response; restore check; tradeoff.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** An isolated library lab with a simulated account misuse and backup snapshot.

**Practice and exercises:** Test the controls in sequence and record their different effects and limits. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 16 and prepares Chapter 18. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 17 of 18 (outline):** [← Chapter 16 (plan)](PLAN.md#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (plan) →](PLAN.md#ch-18)

<a id="ch-18"></a>

### Chapter 18 — Supervised service-security case and handoff

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Demonstrate a complete bounded assessment and a reviewable transfer of findings.

**Concepts and techniques:** Case record; evidence pointer; configuration check; recommendation; handoff.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab. Reproduce collection and control steps in a bounded lab, including failure and rollback evidence.

**Worked example:** A staged synthetic service case with access and availability concerns.

**Practice and exercises:** Submit a technical dossier and defend the proposed safe next actions. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 17 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 18 of 18 (outline):** [← Chapter 17 (plan)](PLAN.md#ch-17) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

## Practical and assessment plan

Practice: build and troubleshoot a reproducible lab. Assessment: practical examinations, troubleshooting log and supervised project. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
