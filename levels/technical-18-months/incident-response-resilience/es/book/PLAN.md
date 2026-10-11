# Principal book plan — Incident response and cyber resilience / Technical course / Español

**One book for this course and language.** 18 curricular subjects are its chapters. Duration: 18 months; planned effort: approximately 1200 hours. Audience: Technical operators. Entry knowledge: Networks, operating systems, scripting and safe lab practice. Intended outcome: diagnose failures, configure controls and verify outcomes in incident response and cyber resilience.

**Editorial state:** structured outline; manuscript not yet authored. English working summaries await translation and review.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 540-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Contents and chapter summaries

<a id="ch-01"></a>

### Chapter 01 — Computing and service architecture

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Establish the service model needed to know what an incident can affect and what a change might break.

**Concepts and techniques:** Components; dependencies; data flows; trust boundaries; failure domains.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic reservation service with an identity provider, database and backup tier.

**Practice and exercises:** Draw the service map, label owners and predict two cascading failures. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

<a id="ch-02"></a>

### Chapter 02 — Networks and protocols

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Connect incident evidence to normal network behavior before interpreting an alert.

**Concepts and techniques:** Addressing; transport; DNS; TLS; packet metadata; network time.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A sanitized packet summary for the synthetic reservation service.

**Practice and exercises:** Trace a client request, identify missing context and select a bounded capture point. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

<a id="ch-03"></a>

### Chapter 03 — Operating systems and identities

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Explain how host state and identities shape both attack hypotheses and safe response choices.

**Concepts and techniques:** Processes; services; accounts; tokens; privileges; host logging.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Synthetic host and identity records for a service account with unusual sign-ins.

**Practice and exercises:** Map privileges, correlate events and separate suspicious behavior from expected maintenance. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

<a id="ch-04"></a>

### Chapter 04 — Scripting and data formats

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Prepare learners to handle evidence with repeatable, inspectable transformations.

**Concepts and techniques:** CSV and JSON parsing; encodings; validation; error handling; deterministic output.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A small synthetic log bundle containing malformed records and duplicate IDs.

**Practice and exercises:** Write or review a bounded parser, preserve raw input and report rejected records. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

<a id="ch-05"></a>

### Chapter 05 — Security scope and evidence

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Turn authorization and evidence integrity into concrete technical constraints.

**Concepts and techniques:** Collection scope; provenance; read-only methods; hashing; access records.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fictional responder request that exceeds the approved host list.

**Practice and exercises:** Build a collection checklist, reject out-of-scope steps and document evidence handling. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

<a id="ch-06"></a>

### Chapter 06 — Response system models and service dependencies

**Stage 1; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Use architecture to plan response actions without assuming that one affected host is isolated.

**Concepts and techniques:** Dependency graph; recovery point; control plane; change window; blast radius.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic identity-provider outage that affects several services.

**Practice and exercises:** Model downstream impact and compare two containment sequences. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

<a id="ch-07"></a>

### Chapter 07 — Event-source mapping and log retention

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Determine which observations can answer a triage question and when they expire.

**Concepts and techniques:** Log schema; collection path; retention; coverage gap; clock source.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fabricated inventory of host, identity and application logs with different retention periods.

**Practice and exercises:** Build an evidence-source matrix and prioritize preservation requests. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

<a id="ch-08"></a>

### Chapter 08 — Identity, host and network failure modes

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Distinguish malicious-looking signals from ordinary system failure and incomplete monitoring.

**Concepts and techniques:** Authentication error; host restart; network loss; telemetry lag; corroboration.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Synthetic simultaneous login failures and packet loss during scheduled maintenance.

**Practice and exercises:** Compare competing failure hypotheses and request the least invasive next observation. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

<a id="ch-09"></a>

### Chapter 09 — Host and network evidence collection methods

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Select collection methods that preserve useful context while limiting change to the system.

**Concepts and techniques:** Snapshot choice; volatile state; network flow; access log; integrity check.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A simulated workstation and gateway with time-limited evidence.

**Practice and exercises:** Choose collection order, capture provenance and state the evidence limitations. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

<a id="ch-10"></a>

### Chapter 10 — Containment control configuration in a lab

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Practice implementing a reversible control and verifying both security effect and service impact.

**Concepts and techniques:** Session revocation; temporary rule; rollback; change log; acceptance test.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** An isolated lab with a compromised synthetic account and a dependent application.

**Practice and exercises:** Configure a scoped control, test expected and unexpected effects, then roll it back. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

<a id="ch-11"></a>

### Chapter 11 — Clock-offset and record-integrity verification

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Prevent timeline errors from being mistaken for adversary behavior.

**Concepts and techniques:** UTC normalization; offset; drift; checksum; immutable copy.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Three synthetic logs with differing time zones and one altered export.

**Practice and exercises:** Normalize timestamps, verify integrity and annotate uncertainty in event order. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

<a id="ch-12"></a>

### Chapter 12 — Laboratory: ingest and preserve synthetic incident records

**Stage 2; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Integrate intake, parsing and preservation into a repeatable small laboratory.

**Concepts and techniques:** Input manifest; schema check; raw copy; normalized view; audit trail.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A supplied synthetic bundle of identity, host and application records.

**Practice and exercises:** Ingest the bundle, produce a preservation manifest and reconcile parse failures. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares Chapter 13. This is an editorial brief, not a completed lesson.

<a id="ch-13"></a>

### Chapter 13 — Troubleshooting conflicting alerts and missing telemetry

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Diagnose why detections disagree before escalating a claim.

**Concepts and techniques:** Detection rule assumption; dropped event; duplicate signal; sensor health.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Two fictional alerts disagree about whether an account reached a protected service.

**Practice and exercises:** Inspect rule inputs, document the coverage gap and revise confidence. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 12 and prepares Chapter 14. This is an editorial brief, not a completed lesson.

<a id="ch-14"></a>

### Chapter 14 — Scripted triage with bounded inputs and audit logs

**Stage 3; 30 planned A4 pages; 3 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Automate repetitive analysis without hiding assumptions or changing source evidence.

**Concepts and techniques:** Input allowlist; idempotence; output log; exception path; review point.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A local script processing the prior synthetic case records.

**Practice and exercises:** Run the script against normal and malformed inputs; compare its output with a manual sample. The planned allocation is 3 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 13 and prepares Chapter 15. This is an editorial brief, not a completed lesson.

<a id="ch-15"></a>

### Chapter 15 — Cross-service incident timeline integration

**Stage 3; 30 planned A4 pages; 2 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Build a defensible incident narrative from several partial system views.

**Concepts and techniques:** Event join; entity mapping; causal caution; confidence; missingness.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Synthetic identity, application and support-desk events for one possible takeover.

**Practice and exercises:** Create a cross-service timeline and mark disputed transitions and unresolved questions. The planned allocation is 2 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 14 and prepares Chapter 16. This is an editorial brief, not a completed lesson.

<a id="ch-16"></a>

### Chapter 16 — Technical documentation and safety

**Stage 3; 30 planned A4 pages; 2 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Package technical decisions so another operator can reproduce and safely continue the work.

**Concepts and techniques:** Runbook precondition; stop condition; rollback; evidence pointer; handoff.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fictional containment procedure with no owner or rollback check.

**Practice and exercises:** Revise the runbook and perform a peer walk-through of failure cases. The planned allocation is 2 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 15 and prepares Chapter 17. This is an editorial brief, not a completed lesson.

<a id="ch-17"></a>

### Chapter 17 — Laboratory: compare containment and restoration options

**Stage 3; 30 planned A4 pages; 2 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Evaluate alternative response plans against measured availability and evidence constraints.

**Concepts and techniques:** Control comparison; service acceptance; restore test; residual risk.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** An isolated service whose account and database show different signs of compromise.

**Practice and exercises:** Test two containment paths and one restoration path; record tradeoffs and acceptance evidence. The planned allocation is 2 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 16 and prepares Chapter 18. This is an editorial brief, not a completed lesson.

<a id="ch-18"></a>

### Chapter 18 — Supervised technical incident case and handoff

**Stage 3; 30 planned A4 pages; 2 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Demonstrate a complete bounded technical response with a reviewable transfer of responsibility.

**Concepts and techniques:** Case chronology; evidence manifest; approval log; remediation check; handoff rubric.

**Depth and method:** At technical course level, learners will build and troubleshoot a reproducible lab; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A staged synthetic incident spanning identity, host and application logs.

**Practice and exercises:** Submit a case dossier, defend the chosen action and hand it to a second responder. The planned allocation is 2 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 17 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

## Practical and assessment plan

Practice: build and troubleshoot a reproducible lab. Assessment: practical examinations, troubleshooting log and supervised project. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
