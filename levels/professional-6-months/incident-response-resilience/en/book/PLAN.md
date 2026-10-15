# Principal book plan — Incident response and cyber resilience / Professional course / English

**One book for this course and language.** The existing 12 curricular subjects remain authored as chapters. Chapters 1–6 contain [Week 1](MANUSCRIPT.md#week-01-day-01), [Week 2](MANUSCRIPT.md#week-02-day-01), [Week 3](MANUSCRIPT.md#week-03-day-01), [Week 4](MANUSCRIPT.md#week-04-day-01), [Week 5](MANUSCRIPT.md#week-05-day-01) and [Week 6](MANUSCRIPT.md#week-06-day-01), each with five applied weekday lessons: 30/130 planned daily lessons are authored, with whole-volume review still pending. Later chapters retain their subject structure pending substantive expansion into the 26-week/130-day curriculum. Duration: 6 months; planned effort: approximately 360 hours. Audience: Entry-level practitioners. Entry knowledge: Security basics and the relevant system fundamentals. Intended outcome: operate a repeatable workflow and communicate findings in incident response and cyber resilience.

**Editorial state:** draft manuscript exists; release A4 validation and review pending. English reference edition.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md)

## Book requirements

The earlier 300-page minimum and 360-page budget are superseded by the current book standard: A4 page count is a measurement, not an authoring target or completion gate. The existing 60 exercise/answer pairs do not by themselves complete the 130-day curriculum. Every chapter needs teaching, definitions, a worked example, practical activity, errors and limits, exercises and a synthesis. The final appendix holds answers keyed to the exercise IDs. Cite verifiable sources, label synthetic cases, and review for technical accuracy, rights and accessibility.

## Primary source starting points

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response recommendations within cybersecurity risk management; it supersedes Rev. 2.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, testing and improvement.
- [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) — exercise design and evaluation; a 2006 publication whose applicability must be checked during authorship.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic techniques in response; a 2006 publication whose technical details need current verification.

These are source leads, not a finished chapter bibliography. Cite the relevant primary source beside each factual claim in the authored manuscript and identify any fictional case as synthetic.

## Contents and chapter summaries

These are editorial outlines. Each chapter summary ends with links to the previous position, the course index and the next position; a **draft** link opens authored teaching, while a **plan** link opens another outline.

<a id="ch-01"></a>

### Chapter 01 — Incident lifecycle and organizational readiness

**Stage 1; 30 planned A4 pages in the earlier outline; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-01) and [Week 1 daily sequence](MANUSCRIPT.md#week-01-day-01). The daily sequence treats transaction invariants, route-specific evidence, decision rights, clock semantics and reviewable handoff as separate lessons; it reuses EX001–EX005 and their worked answers without claiming the rest of the 130-day course has been authored.

**Teaching purpose and relevance:** Establish how preparation, detection, response and recovery interact in a repeatable organizational workflow.

**Concepts and techniques:** Service inventory; roles; escalation path; logging readiness; backup and communication dependencies.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** A synthetic multi-service organization with incomplete ownership and telemetry maps.

**Practice and exercises:** Produce a readiness checklist, identify missing dependencies and prioritize two corrective actions. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on the entry knowledge and prepares Chapter 02. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 01 of 12 (outline):** [← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](MANUSCRIPT.md#ch-02)

<a id="ch-02"></a>

### Chapter 02 — Authority, scope and response roles

**Stage 1; 30 planned A4 pages in the earlier outline; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-02) and [Week 2 daily sequence](MANUSCRIPT.md#week-02-day-01). The sequence separates decision rights, a versioned action envelope, proportionate controls, ambiguous approval and a time-bounded handoff. It reuses EX006–EX010 and their worked answers.

**Teaching purpose and relevance:** Make the limits of responder authority operational so urgent work stays reviewable and service owners retain decision rights.

**Concepts and techniques:** Rules of engagement; authorization record; role separation; approval matrix; escalation.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** A simulated cloud account alert that could require tenant-level changes outside the analyst's scope.

**Practice and exercises:** Draft a response charter and classify proposed actions as permitted, approval-gated or out of scope. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 01 and prepares Chapter 03. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 02 of 12 (outline):** [← Chapter 01 (draft)](MANUSCRIPT.md#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](MANUSCRIPT.md#ch-03)

<a id="ch-03"></a>

### Chapter 03 — Alert intake and severity assessment

**Stage 2 in the legacy outline; 30 historical planned pages; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-03) and [Week 3, course Days 11–15](MANUSCRIPT.md#week-03-day-01). The sequence teaches provenance-preserving intake, clock correction, provisional priority, hypothesis discrimination and actionable escalation. C02–C08, C3/C3X and EX011–EX015 remain in the single manuscript; the questions and worked extensions were revised together. A separate [Chapter 3 timed-test bank](../../../../../web/question-banks/professional-6-months/incident-response-resilience/en/003.json) contains ten source-pinned original questions and worked explanations; the site supplies the fifth uncertainty choice. These timed questions do not replace EX011–EX015 or create their interactive practice counterparts. Independent human approval is not claimed.

**Teaching purpose and relevance:** Move from raw reports to a documented priority without equating every anomaly with compromise.

**Concepts and techniques:** Intake fields; corroboration; impact and confidence; severity matrix; false-positive handling.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** Synthetic endpoint and identity alerts about the same account with conflicting timestamps.

**Practice and exercises:** Triage the alerts, justify severity, record uncertainty and set an explicit reassessment trigger. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 02 and prepares Chapter 04. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 03 of 12 (outline):** [← Chapter 02 (draft)](MANUSCRIPT.md#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](MANUSCRIPT.md#ch-04)

<a id="ch-04"></a>

### Chapter 04 — Evidence preservation and case records

**Stage 2 in the legacy outline; 30 historical planned pages; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-04) and [Week 4, course Days 16–20](MANUSCRIPT.md#week-04-day-01). The five lessons teach authorization/scope, source-copy-derivative identity, receipts and custody, exact-byte checks, capture context and a bounded investigation handoff. They retain C09/C10 and V4/C4/C4X, add the in-memory W4-BYTES representation control, and revise EX016–EX020 with matching worked extensions. No later case card or additional numbered exercise is supplied. A separate [Chapter 4 timed-test bank](../../../../../web/question-banks/professional-6-months/incident-response-resilience/en/004.json) now adds ten original source-pinned questions; it does not replace EX016–EX020 or certify human approval.

**Teaching purpose and relevance:** Create a case trail that allows a second responder to reproduce observations without altering the source.

**Concepts and techniques:** Collection plan; source identifiers; hashes where applicable; access log; retention and chain-of-custody limits.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** A synthetic log export and screenshot with different time zones and incomplete metadata.

**Practice and exercises:** Record provenance, verify a supplied checksum and identify what cannot be concluded from the evidence. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 03 and prepares Chapter 05. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 04 of 12 (outline):** [← Chapter 03 (draft)](MANUSCRIPT.md#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](MANUSCRIPT.md#ch-05)

<a id="ch-05"></a>

### Chapter 05 — Investigation, hypotheses and timeline building

**Stage 3 in the legacy outline; 30 historical planned pages; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-05) and [Week 5, course Days 21–25](MANUSCRIPT.md#week-05-day-01). The sequence teaches versioned provenance timelines, typed graph edges, bounded join tests, competing hypotheses, discriminator requests and gated handoff. C11/C12, C5/C5X and all existing teaching remain; W5-EDGE adds a six-line offline contract control, with revised EX021–EX025 and worked extensions. No later containment evidence is released.

**Teaching purpose and relevance:** Turn preserved observations into testable explanations while retaining alternatives and gaps.

**Concepts and techniques:** Hypothesis table; timeline normalization; corroboration; competing explanations; confidence.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN enrollment-slot change with identity, application and support records but no direct session-to-request join.

**Practice and exercises:** Construct a normalized timeline, compare three hypotheses and list the next least-invasive evidence request. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 04 and prepares Chapter 06. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 05 of 12 (outline):** [← Chapter 04 (draft)](MANUSCRIPT.md#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](MANUSCRIPT.md#ch-06)

<a id="ch-06"></a>

### Chapter 06 — Containment planning and approvals

**Stage 3 in the legacy outline; 30 historical planned pages; 5 existing exercises.** [Read authored chapter](MANUSCRIPT.md#ch-06) and [Week 6, course Days 26–30](MANUSCRIPT.md#week-06-day-01). The daily sequence teaches a measurable containment property, three-control/service-cost comparison, separate approval/execution/verification, fixed 09:47 expiry, route/service tests and conditional rollback. C13–C19 and C6/V6/C6X remain intact; W6-TIME adds fixed-window adverse controls and W6-MISSING challenges an incomplete inventory. EX026–EX030 and their worked extensions are revised together. A separate [Chapter 5 timed-test bank](../../../../../web/question-banks/professional-6-months/incident-response-resilience/en/005.json) adds ten original questions pinned after the Day 25 navigation update. No later authority or human approval is asserted.

**Teaching purpose and relevance:** Choose a containment sequence that reduces further harm while respecting availability and authorization.

**Concepts and techniques:** Scope of intervention; blast radius; reversibility; approval; success criterion; rollback.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN S42 write-hold proposal, separate approval, execution receipt and one-route check.

**Practice and exercises:** Compare a slot hold, session action and account disablement; record approval scope, expiry, verification and rollback. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 05 and prepares Chapter 07. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 06 of 12 (outline):** [← Chapter 05 (draft)](MANUSCRIPT.md#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](MANUSCRIPT.md#ch-07)

<a id="ch-07"></a>

### Chapter 07 — Eradication and verification

**Stage 4; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-07)

**Teaching purpose and relevance:** Distinguish removing an observed symptom from verifying that the cause and persistence paths are addressed.

**Concepts and techniques:** Root-cause hypothesis; persistence check; control change; validation evidence; residual risk.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN task-to-request link and a separately unapproved recovery-method change with unknown actor.

**Practice and exercises:** Compare task and identity paths, specify positive and negative checks, and record residual uncertainty. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 06 and prepares Chapter 08. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 07 of 12 (outline):** [← Chapter 06 (draft)](MANUSCRIPT.md#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](MANUSCRIPT.md#ch-08)

<a id="ch-08"></a>

### Chapter 08 — Recovery, continuity and return to service

**Stage 4; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-08)

**Teaching purpose and relevance:** Return a service safely by checking data, dependencies and monitoring before closure.

**Concepts and techniques:** Restore point; data integrity; service acceptance; staged restart; monitoring; rollback.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN snapshot that would regress legitimate S40/S41 changes versus a targeted S42 correction with an audit-gate retest.

**Practice and exercises:** Compare restore candidates and complete an owner-approved isolated-test and return-to-service record. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 07 and prepares Chapter 09. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 08 of 12 (outline):** [← Chapter 07 (draft)](MANUSCRIPT.md#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](MANUSCRIPT.md#ch-09)

<a id="ch-09"></a>

### Chapter 09 — Communications, privacy and legal coordination

**Stage 5; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-09)

**Teaching purpose and relevance:** Coordinate accurate notices while separating confirmed facts from assumptions and routing sensitive questions to authorized specialists.

**Concepts and techniques:** Stakeholder map; status update; data minimization; legal hold trigger; message approval.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN internal queue batch with twelve pseudonymous tokens, not-dispatched status and an unresolved gateway gap.

**Practice and exercises:** Draft separate service and privacy status, a scoped referral and an unsent learner update with approval state. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 08 and prepares Chapter 10. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 09 of 12 (outline):** [← Chapter 08 (draft)](MANUSCRIPT.md#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](MANUSCRIPT.md#ch-10)

<a id="ch-10"></a>

### Chapter 10 — Playbook engineering and quality review

**Stage 5; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-10)

**Teaching purpose and relevance:** Turn a response path into a usable playbook whose preconditions, limits and expected evidence are explicit.

**Concepts and techniques:** Trigger; decision branch; owner; safety gate; evidence checkpoint; revision control.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** The fictional CTN P0 decision aid that would disable a shared account, regress valid data and make an unsupported breach claim.

**Practice and exercises:** Revise seven decision gates, walk main and negative-control branches, and score six quality criteria. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 09 and prepares Chapter 11. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 10 of 12 (outline):** [← Chapter 09 (draft)](MANUSCRIPT.md#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](MANUSCRIPT.md#ch-11)

<a id="ch-11"></a>

### Chapter 11 — Supervised incident simulation

**Stage 6; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-11)

**Teaching purpose and relevance:** Exercise a cross-role workflow under changing evidence without treating a tabletop as a live intervention.

**Concepts and techniques:** Inject control; handoff; clock management; decision log; observer notes; stop condition.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** A staged simulated identity and application incident with a communications request.

**Practice and exercises:** Run a supervised tabletop, record decisions and evaluate handoffs against preannounced criteria. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 10 and prepares Chapter 12. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 11 of 12 (outline):** [← Chapter 10 (draft)](MANUSCRIPT.md#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](MANUSCRIPT.md#ch-12)

<a id="ch-12"></a>

### Chapter 12 — Case portfolio and after-action review

**Stage 6; 30 planned A4 pages; 5 planned exercises.** [Read authored draft](MANUSCRIPT.md#ch-12)

**Teaching purpose and relevance:** Synthesize several cases into evidence of professional judgment and convert observed weaknesses into owned improvements.

**Concepts and techniques:** Case selection; evidence quality; outcome metric; root-cause caution; corrective-action tracking.

**Depth and method:** At professional course level, learners will run a supervised workflow with evidence checkpoints. Record approvals, evidence checkpoints and a usable operational handoff.

**Worked example:** A portfolio of the synthetic alerts, records and tabletop artifacts from earlier chapters.

**Practice and exercises:** Submit an annotated case portfolio, defend one tradeoff and prioritize measurable improvements. The planned allocation is 5 exercises; authored tasks and worked answers appear in the linked draft, with review pending.

**Learning sequence:** Builds on Chapter 11 and prepares the worked-answer appendix and final assessment. This is an editorial brief, not a completed lesson.

**Continue studying — chapter 12 of 12 (outline):** [← Chapter 11 (draft)](MANUSCRIPT.md#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

## Practical and assessment plan

Practice: run a supervised workflow with evidence checkpoints. Assessment: portfolio of cases, lab rubric and final practical review. Allocate at least one authored exercise to every chapter and at least 50 in the whole book. Each technical exercise needs a goal, inputs, authorized scope, steps, expected evidence and a worked or rubric-based result. The final book requires a glossary, references and an A4 rendering verified under the [book standard](../../../../../BOOK_STANDARD.md).
