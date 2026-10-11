# Principal book plan — Incident response and cyber resilience / Professional course / Deutsch

**One book for this course and language.** 12 curricular subjects are its chapters. Duration: 6 months; planned effort: approximately 360 hours. Audience: Entry-level practitioners. Entry knowledge: Security basics and the relevant system fundamentals. Intended outcome: operate a repeatable workflow and communicate findings in incident response and cyber resilience.

**Editorial state:** structured outline; manuscript not yet authored. English working summaries await translation and review.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

A finished book must contain at least 300 actual A4 pages and 50 substantive exercises with worked results. The current 360-page budget is a plan, not measured pages. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Contents and chapter summaries

<a id="ch-01"></a>

### Chapter 01 — Incident lifecycle and organizational readiness

**Stage 1; 30 planned A4 pages; 5 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Establish how preparation, detection, response and recovery interact in a repeatable organizational workflow.

**Concepts and techniques:** Service inventory; roles; escalation path; logging readiness; backup and communication dependencies.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic multi-service organization with incomplete ownership and telemetry maps.

**Practice and exercises:** Produce a readiness checklist, identify missing dependencies and prioritize two corrective actions. The planned allocation is 5 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

<a id="ch-02"></a>

### Chapter 02 — Authority, scope and response roles

**Stage 1; 30 planned A4 pages; 5 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Make the limits of responder authority operational so urgent work stays reviewable and service owners retain decision rights.

**Concepts and techniques:** Rules of engagement; authorization record; role separation; approval matrix; escalation.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A simulated cloud account alert that could require tenant-level changes outside the analyst's scope.

**Practice and exercises:** Draft a response charter and classify proposed actions as permitted, approval-gated or out of scope. The planned allocation is 5 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

<a id="ch-03"></a>

### Chapter 03 — Alert intake and severity assessment

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Move from raw reports to a documented priority without equating every anomaly with compromise.

**Concepts and techniques:** Intake fields; corroboration; impact and confidence; severity matrix; false-positive handling.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** Synthetic endpoint and identity alerts about the same account with conflicting timestamps.

**Practice and exercises:** Triage the alerts, justify severity, record uncertainty and set an explicit reassessment trigger. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

<a id="ch-04"></a>

### Chapter 04 — Evidence preservation and case records

**Stage 2; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Create a case trail that allows a second responder to reproduce observations without altering the source.

**Concepts and techniques:** Collection plan; source identifiers; hashes where applicable; access log; retention and chain-of-custody limits.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic log export and screenshot with different time zones and incomplete metadata.

**Practice and exercises:** Record provenance, verify a supplied checksum and identify what cannot be concluded from the evidence. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

<a id="ch-05"></a>

### Chapter 05 — Investigation, hypotheses and timeline building

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Turn preserved observations into testable explanations while retaining alternatives and gaps.

**Concepts and techniques:** Hypothesis table; timeline normalization; corroboration; competing explanations; confidence.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fictional account takeover case with identity, application and support-ticket records.

**Practice and exercises:** Construct a normalized timeline, test two hypotheses and list the next least-invasive evidence request. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

<a id="ch-06"></a>

### Chapter 06 — Containment planning and approvals

**Stage 3; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Choose a containment sequence that reduces further harm while respecting availability and authorization.

**Concepts and techniques:** Scope of intervention; blast radius; reversibility; approval; success criterion; rollback.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic credential misuse scenario where disabling one account affects a critical service.

**Practice and exercises:** Compare session revocation, credential rotation and temporary access limits; document owner approval. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

<a id="ch-07"></a>

### Chapter 07 — Eradication and verification

**Stage 4; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Distinguish removing an observed symptom from verifying that the cause and persistence paths are addressed.

**Concepts and techniques:** Root-cause hypothesis; persistence check; control change; validation evidence; residual risk.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fictional unauthorized scheduled task with a second unverified account change.

**Practice and exercises:** Plan eradication in a sandbox, specify post-change checks and record unresolved uncertainty. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

<a id="ch-08"></a>

### Chapter 08 — Recovery, continuity and return to service

**Stage 4; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Return a service safely by checking data, dependencies and monitoring before closure.

**Concepts and techniques:** Restore point; data integrity; service acceptance; staged restart; monitoring; rollback.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic booking database restored from a known snapshot while application logs remain incomplete.

**Practice and exercises:** Prepare a recovery checklist and acceptance record with owners, tests and a fallback decision. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

<a id="ch-09"></a>

### Chapter 09 — Communications, privacy and legal coordination

**Stage 5; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Coordinate accurate notices while separating confirmed facts from assumptions and routing sensitive questions to authorized specialists.

**Concepts and techniques:** Stakeholder map; status update; data minimization; legal hold trigger; message approval.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A fictional incident involving possible exposure of a subscriber contact list.

**Practice and exercises:** Write two audience-specific updates, flag unverified claims and identify privacy or legal review points. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

<a id="ch-10"></a>

### Chapter 10 — Playbook engineering and quality review

**Stage 5; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Turn a response path into a usable playbook whose preconditions, limits and expected evidence are explicit.

**Concepts and techniques:** Trigger; decision branch; owner; safety gate; evidence checkpoint; revision control.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A synthetic compromised-credential playbook missing approval and rollback steps.

**Practice and exercises:** Revise the playbook, walk through a failure case and score it against a quality checklist. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

<a id="ch-11"></a>

### Chapter 11 — Supervised incident simulation

**Stage 6; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Exercise a cross-role workflow under changing evidence without treating a tabletop as a live intervention.

**Concepts and techniques:** Inject control; handoff; clock management; decision log; observer notes; stop condition.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A staged simulated identity and application incident with a communications request.

**Practice and exercises:** Run a supervised tabletop, record decisions and evaluate handoffs against preannounced criteria. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

<a id="ch-12"></a>

### Chapter 12 — Case portfolio and after-action review

**Stage 6; 30 planned A4 pages; 4 planned exercises.** Planned; authored chapter pending.

**Teaching purpose and relevance:** Synthesize several cases into evidence of professional judgment and convert observed weaknesses into owned improvements.

**Concepts and techniques:** Case selection; evidence quality; outcome metric; root-cause caution; corrective-action tracking.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints; they must support conclusions with a bounded case record and identify uncertainties.

**Worked example:** A portfolio of the synthetic alerts, records and tabletop artifacts from earlier chapters.

**Practice and exercises:** Submit an annotated case portfolio, defend one tradeoff and prioritize measurable improvements. The planned allocation is 4 exercises; authored tasks and worked answers remain a separate completion gate.

**Learning sequence:** Builds on Chapter 11 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

## Practical and assessment plan

Practice: run a supervised workflow with evidence checkpoints. Assessment: portfolio of cases, lab rubric and final practical review. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
