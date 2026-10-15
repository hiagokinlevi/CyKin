# Tabletop 01 — Hospital ransomware: clinical continuity before technical convenience

**Edition:** English · **Exercise ID:** TTX-HR-01 · **Scenario catalog ID:** hospital-ransomware · **Editorial date:** 2026-10-15  
**Status:** Original fictional teaching exercise; technical and human review pending.  
**Audience:** Hospital leadership, clinical operations, nursing, radiology, SOC, infrastructure, recovery, privacy and communications.  
**Format:** Facilitated discussion and written decision artifacts, not a functional test or production playbook.  
**Timing:** 15-minute briefing, 90-minute exercise, 25-minute evaluation/debrief; extend for accessibility or deliberation.  
**Sources and rights:** See [primary references](#primary-references-and-rights). Original exercise text is within the project's [rights policy](../../../RIGHTS.md). The ten-entry web scenario catalog remains the discovery index; this document expands its existing hospital-ransomware entry and is **not** an eleventh incident or a second course book.

## 1. Purpose, scope, and safety contract

**Fictional institution:** Cedar Vale Regional Hospital (CVRH), a 120-bed regional hospital with an emergency department, inpatient wards and radiology. All staff names, case IDs, timestamps, systems, metrics, patient situations and records below are invented classroom fixtures, **not** observed incidents, medical advice or validated real-world outcomes. Do not use patient-identifying data, real infrastructure, extortion portals, malware samples, or production credentials. If live clinical risk appears during a real exercise, stop the exercise and invoke the hospital's actual emergency procedures.

**Starting facts from the catalog:** Appointment scheduling and a shared imaging folder are unavailable; bedside systems appear functional but their dependencies are unverified. At 08:20 a workstation displays an extortion note, two file shares become unreadable, and endpoint alerts disagree with backup-job records about the earliest affected time. Those are observations of a possible ransomware event, **not** proof of initial access, complete spread, integrity of any backup, patient-data theft or a safe bedside network.

**Top priority:** Clinical triage, patient movement, clinical substitutions, transfer/diversion, use of paper orders and acceptance of clinical workflows belong to the **clinical lead** and authorized clinical teams. The cybersecurity incident commander cannot override a clinical safety decision. No participant may instruct staff to disconnect, reboot, scan or reconfigure bedside or imaging equipment on the strength of a tabletop assumption. An equipment change requires clinical safety assessment, a verified dependency map and the device/service owner's approved procedure; where relevant, consult biomedical engineering and vendors. Safety can require delaying an otherwise sensible technical isolation.

### Observable objectives

- **O1 — Clinical safety:** Establish clinical impact, owners and safe interim workflows with explicit stop/escalation triggers.
- **O2 — Detection and evidence:** State observations separately from hypotheses; preserve source, acquisition, hashes, custody and time uncertainty.
- **O3 — Proportionate response:** Compare bounded containment alternatives, with scope, clinical dependencies, authorizers, service cost, verification and rollback.
- **O4 — Data and communications:** Keep possible exfiltration distinct from proven exposure; draft messages with approval and review gates.
- **O5 — Recovery:** Evaluate backup provenance, isolation, integrity, malware risk, RPO/RTO uncertainty, functional clinical checks and staged return.
- **O6 — Improvement:** Produce a prioritized after-action record with owners, dates and a measurable retest.

### NIST alignment without invented mandatory steps

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) is a **CSF 2.0 Community Profile** (2025), not the former Rev. 2 four-phase checklist. Its response lifecycle emphasizes **Detect, Respond and Recover**; **Govern, Identify and Protect** supply broader preparation and risk management, and **Identify/Improvement** receives lessons across functions. [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) describes outcomes, not this exercise's timing, roles, evidence cards, score, or hospital authority charter. The following alignment is this course's teaching design, **not** a NIST-prescribed hospital protocol:

| Exercise activity | CSF 2.0 function(s) | Decision demonstrated |
|---|---|---|
| Confirm service inventory, ownership, delegation, downtime and backup assumptions | Govern, Identify, Protect | Who is authorized; which dependencies and controls are actually known? |
| Compare alerts with clinical reports and clock sources | Detect | What is observed, uncertain or unverified? |
| Preserve evidence, scope isolation and coordinate clinical operations | Respond | Which limited actions are justified and approved? |
| Evaluate candidates, isolated restores, clinical acceptance and monitoring | Recover | Which claims have passed a bounded test, and which have not? |
| Record defects, assignments, retests and metrics | Identify/Improvement, Govern | How will the next exercise falsify a claimed improvement? |

[NIST IR 8374 Rev. 1](https://csrc.nist.gov/pubs/ir/8374/r1/final), published June 2026, is the relevant ransomware CSF 2.0 Community Profile. It supports treating extortion, encryption, possible data theft, continuity and restoration as related but **different evidence questions**. It does not authorize a responder to make a medical decision.

## 2. Roles, delegation and explicit limits

At briefing, assign each fictional participant a role; the observer records any substitution. Real-world organizations must replace this classroom charter with their approved authorities.

| Named participant and team | Can decide or approve in this simulation | Cannot infer or authorize |
|---|---|---|
| **Dr. Elena Park — Clinical Command (chief medical officer and clinical lead)** | Clinical triage, patient safety actions, downtime workflows, diversion/transfer decisions and clinical acceptance criteria after consulting treating teams | A firewall change, ransomware attribution or legal breach finding; IT cannot authorize her clinical decisions |
| **Maya Torres, RN — Nursing Operations** | Validate bedside workflows, identify manual medication/order reconciliation needs, report unit-level safety problems to Dr. Park | Declare devices network-independent or approve restoration of all services |
| **Dr. Asha Raman — Radiology and Imaging** | Set radiology critical-use cases, image-to-patient identity reconciliation and radiology clinical test acceptance with Dr. Park | Approve an unsafe technical reconnect or treat a successful login as image integrity |
| **Sofia Grant — Patient Safety and Biomedical Engineering liaison** | Document device dependencies, vendor consultation and hold points for equipment changes; escalate uncertain physical risks | Disconnect bedside equipment solely because an EDR panel says “affected network” |
| **Andre Lewis — Cyber Incident Commander (security)** | Open the simulated incident, coordinate responders and approve a bounded cyber-response proposal only within a signed delegation | Overrule Dr. Park, approve a missing owner action, declare a breach or speak for the hospital |
| **Priya Shah — SOC and Evidence Custodian** | Maintain evidence/release ledgers, request authorized collection, annotate detection limits and custody | Treat request as completed acquisition, or a log gap as no compromise |
| **Theo Nguyen — Infrastructure and Network Operations** | Evaluate and execute **separately approved** workstation/share containment; verify reachability and rollback | Isolate an unverified clinical dependency, or claim an unperformed command succeeded |
| **Lena Brooks — Backup and Recovery** | Select isolated restore candidates for review, verify bytes and run controlled recovery tests after approval | Assert malware-free status from a job-success line or put an isolated image into production |
| **Marcus Ellis — Privacy and Legal Review** | Lead protected-data risk assessment, preservation scope and applicable notification analysis | Assert “no exfiltration” from a small sample; assume every extortion note automatically establishes a reportable breach |
| **Dana Ortiz — Communications** | Draft internal/patient-facing status and publish only after clinical, privacy/legal and executive review as applicable | Promise a restoration time, unaffected patient care or absence of data theft without evidence |
| **Ravi Patel — Hospital Executive Sponsor** | Activate organizational crisis resources, approve extraordinary expenditure and ratify enterprise risk decisions | Replace clinical sign-off or forensic evidence with executive preference |
| **Jordan Reed — Neutral Facilitator/Observer** | Release scenario injects, freeze submissions and apply the published rubric | Invent logs to rescue a decision or coach an answer during scoring |

**Two-key principle:** Technical action approval and clinical safety clearance are different decisions, when the proposed IT action may affect care. Each must name the exact target, operator, time window, patient-care impact, rollback, independent verifier and escalation route. The simulated incident commander provides cyber authorization; Dr. Park owns clinical disposition and signs clinical go/no-go. A hypothetical approval is an exercise artifact, never an operational authorization.

## 3. Setup, participant packet and evidence discipline

The facilitator prepares: printed/readonly inject cards HV-00 through HV-08 (with later cards sealed), a service/dependency map explicitly labeled **outdated**, a blank evidence ledger, decision ledger, clinical downtime log, recovery acceptance sheet, unsent message draft and observer scoring sheet. Only **HV-00** is initially public. Separate teams may share information through the incident commander, but later injects cannot be treated as already known.

**Three clocks must not be conflated:** (1) fictional case/event time (UTC, as recorded by each source); (2) exercise elapsed minute at which the facilitator releases a card; and (3) time a participant writes and freezes a decision. Source clock accuracy is an open question. A later card describing an earlier event **does not** authorize an earlier action. Cards are synthetic supplied observations, not evidence of performed classroom actions.

For each decision, retain: **decision ID; release set; case checkpoint; exercise minute; observed facts; inference with confidence; alternatives and their patient/service costs; named authorizers; proposed/approved/executed/independently-verified status; missing evidence; rollback; clinical stop condition; next review trigger.** Never collapse approval, implementation and effectiveness into one “done.” Evidence requests need dispatch and custodian receipts; copies need acquisition metadata and integrity checks. Keep original submitted decisions visible when later information corrects them.

**Exercise stop card:** “Patient safety concern, real emergency, proposed live command, unclear bedside dependency, disclosure of actual patient information or unapproved patient-facing claim.” Freeze the game, record the concern, and refer to the authorized clinical/emergency/privacy process. No score compensates for an unaddressed safety stop.

## 4. Injects and facilitated rounds

The fixed cards define what the facilitator **supplies**. Participant proposals, optional role-play approvals, simulated implementations and alternative consequences must be recorded separately. Rounds 1–7 use a 90-minute exercise clock; extend if needed. The question at every release is: **What can you responsibly decide now, by whose authority, supported by which card, and what will falsify your conclusion?**

### Prebrief — HV-00 (exercise minute 0; preparation before Detect)

**Provided:** CVRH has a scheduling service **SCH**, shared radiology image folder **IMG**, a mixed clinical/application network, 120 beds and an approved but not recently exercised paper appointment fallback. A 50-day-old diagram indicates some shared infrastructure, but no current signed map verifies bedside device dependencies. The last full cross-unit downtime drill is undocumented. The incident escalation contact list has named owners; that list does not establish they are currently reachable. No class-wide RTO or RPO is approved in the supplied packet.

**Decision request:** Dr. Park and Maya identify which clinical care paths could be harmed by SCH/IMG loss, safe alternatives and immediate stop triggers. Andre asks Priya for evidence preservation owners and Theo for a network dependency check. Ravi confirms crisis delegation rather than assigning clinical decisions to security. **Output:** pre-incident assumptions/unknowns and a role acknowledgment. **Guardrail:** do not write “bedside isolated = safe” or invent a backup recovery promise.

### Round 1 — HV-01 and HV-02 (minutes 10–21; Detect)

**HV-01; fictional event 08:20 UTC:** Help desk ticket says one workstation **WS-17** displays an extortion note; staff cannot read the SCH shared export or IMG folder, two distinct shares. The original screenshot is **not** yet in the case repository; the ticket contains a transcribed description only. No source says data were exfiltrated, the encryption process is still running, or bedside equipment was compromised.

**HV-02; sources differ:** At 08:26, an EDR console reports an encryption-like file-write alert timestamped **08:12** on WS-17; a backup-job status screen labeled **08:15 complete** contains a storage checksum warning at **07:58**. The screens do not share a verified clock reference or scope. The 07:58 warning might reflect staging/integrity trouble, not first malicious activity. A completed job is not a verified clean restore.

**Decisions:** Priya opens **CVRH-IR-001**, requests original EDR/export/job records and UTC offset checks, labels the initial event boundary **unknown**, and protects copies from overwrite. Andre assigns provisional severity based on interrupted patient-related workflows, not the ransom demand's rhetoric. Theo proposes but does **not** execute bounded workstation isolation without approval and service-impact review. Maya starts a clinical impact snapshot with Dr. Park. **Required evidence:** source/collection receipt, exact timestamps and their meanings, checksum warning context, observed accessibility by service, and a review time.

**Conditional branches:** If an owner authorizes a short WS-17 network quarantine **after** checking that it is not clinical equipment, the facilitator may record an **optional classroom decision**, but may not report reduced spread unless a subsequent verification card exists. If teams “wipe to stop it,” record evidence-loss and safety defects; no wipe occurs.

### Round 2 — HV-03 (minutes 22–36; clinical safety and Respond)

**HV-03; 08:33 UTC:** Nursing reports bedside screens are currently displaying observations; the clinical teams have **not** established whether chart routing or results synchronization depends on the affected network. Radiology cannot retrieve one test-image request from IMG. Appointment desks report an interrupted outpatient queue. An urgent fictional imaging consultation is awaiting clinical review; this card does **not** describe a specific patient or dictate a clinical action.

**Decisions:** Dr. Park invokes a clinically governed downtime assessment; Maya documents manual workflow limits and high-risk handoffs; Dr. Raman distinguishes an imaging access failure from certainty that all modalities are down; Sofia checks current device/vendor dependency documentation before any network reconfiguration. The team proposes clinical triage or diversion only through Dr. Park's authority, using actual local policy if this were real. Andre prioritizes containment proposals that do not jeopardize care. **Outputs:** clinical impact table (available/unavailable/unknown), named owner, manual reconciliation control, next check and a written “do not disconnect bedside systems” boundary.

**Conditional branches:** If the team describes a **clinically authorized** manual pathway, mark it “planned” until an observer records it was rehearsed on paper; if clinical leadership cannot validate an urgent-care path, Dr. Park records an escalation/transfer/diversion assessment. Neither the instructor nor IT invents the medical disposition. A green bedside display is **not** evidence of independence.

### Round 3 — HV-04 (minutes 37–51; bounded containment)

**HV-04; 08:46 UTC:** An approved synthetic read-only inventory view lists WS-17 and WS-19 as ordinary administrative workstations and **FS-IMG-02** as the IMG file-share server. A local report suggests that FS-IMG-02 may also carry a radiology queue integration, but the attachment is **a 50-day-old topology diagram**. EDR has high-confidence suspicious events on WS-17, one medium-confidence alert on WS-19 and **no supplied direct encryption observation** on bedside endpoints. There is no supplied proof that disconnecting the entire subnet is safe.

**Decision comparison to record:**
1. **Narrow option:** Owner-authorized quarantine of confirmed administrative workstations, preserving endpoint telemetry; check SCH/IMG reachability and clinical impact after each step.
2. **Share option:** Restrict specific affected server write paths under service-owner and clinical dependency review; preserve source data and available read-only evidence.
3. **Broad option:** Isolate the whole clinical/application segment. It might reduce reachability but risks obscured device dependencies and service interruption, so is **not executable** on this evidence without further mapping and clinical clearance.

Theo supplies proposed targets, changes, rollback and a verification plan. Andre records cyber authorization only if the classroom approver signs its scope. Dr. Park independently governs any patient-impacting step and may refuse. Priya preserves original alerts and configurations before disruptive action where safe. **Negative control:** “No alert from other devices” does not mean they are clean. **Conditional effects:** Bounded containment has no claimed effect until a fictional independent readback is explicitly logged; if the clinical dependency remains unknown, defer broad isolation and prioritize safe alternatives.

### Round 4 — HV-05 (minutes 52–63; backup truth and recovery strategy)

**HV-05; 09:05 UTC:** Lena receives two **candidate** backup records. **B-A:** object timestamp 01:00, isolated-vault inventory ID BA-0100, storage hash cataloged, **no restored content checked yet**. **B-B:** incremental chain labeled 07:45, job status “complete” but an unexplained 07:58 staging checksum warning and **no independent end-to-end readback**. Neither card states when malicious activity began, that a snapshot is malware-free, or that all source transactions are present. A planning note says “aim for same-day scheduling” but is **not** an owner-approved RTO or RPO.

**Decisions:** Lena rejects “latest equals clean”; requests immutable/read-only acquisition of backup metadata and logs; proposes isolated restore of B-A first while investigating B-B's chain, clock semantics and completeness. Priya maintains evidence copies separate from restore artifacts. Dr. Park and Dr. Raman establish minimum clinically meaningful patient/appointment/image identity checks before any return; Ravi records resource priorities without inventing target SLAs. **Acceptance planning:** Define completeness horizon, loss interval with unknown start/end, image-to-patient association, approved test identities, scheduling create/read/change, audit logging, clinical communications, independent surveillance and rollback owner.

**Conditional branches:** An isolated hash match can support byte integrity of a specified object, **not** safety, completeness or absence of malware. A successful job notification cannot pass the restore gate. If neither candidate passes, sustain clinician-approved downtime/transfer decisions and escalate recovery procurement; do not reconnect untested data to meet an unsupported deadline.

### Round 5 — HV-06 (minutes 64–75; privacy, legal and communications)

**HV-06; 09:18 UTC:** A firewall summary shows **38 MB outbound** from one affected administrative workstation to an unfamiliar external endpoint during an uncertain window. This is a network-volume summary without payload classification, recipient verification or PHI inventory. An extortion message claims “we copied patient files.” These facts warrant assessment, **not** an assertion of patient-data theft or a cleared risk. The hospital's jurisdiction and actual data flows must be verified by counsel; CVRH is a fictional U.S. covered-entity training assumption for discussion only.

**Decisions:** Marcus requests lawful, minimum-necessary flow context and data-owner inventory, starts a documented protected-data assessment and determines applicable notification duties and deadlines **only after** facts and law are reviewed. Dana prepares a bounded operational message, routes it through Dr. Park for clinical accuracy and Marcus for privacy/legal accuracy, and records draft/approved/sent/read-back separately. Ravi agrees on a factual executive brief; Andre reports technical uncertainty, not a breach verdict. **Safe draft for approval, not transmission:** “We are managing a technology disruption affecting scheduling and access to some imaging records. Clinical teams are evaluating each care pathway and using approved contingency processes where appropriate. We will provide verified service updates through authorized channels.” Do not promise zero exposure, universal care continuity or an estimated full recovery time.

**Conditional branches:** If later authorized investigation proves impermissible disclosure, Marcus initiates the documented legal/regulatory path; if evidence remains incomplete, preserve the unresolved assessment without publishing “no breach.” For a **U.S. HIPAA** discussion, distinguish the [HHS Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) from an extortion claim: an impermissible use/disclosure analysis and applicable risk assessment or notification determination is needed. Do not imply 38 MB proves PHI was acquired or apply a universal deadline without determining actor, entity, jurisdiction and discovery facts.

### Round 6 — HV-07 (minutes 76–89; isolated restoration and failed clinical gate)

**HV-07; 10:05 UTC:** In an explicitly **isolated classroom restore simulation**, B-A was mounted on a test network after preserving a separate evidence reference. The synthetic SCH test can authenticate and create/read a **test-only** appointment. The IMG test returns a sample image, but its image-to-encounter identifier **does not match** the simulated approved clinical manifest. No production service change was performed. The test record does not establish clean source binaries, B-A completeness or ongoing production containment; monitoring coverage of the isolated candidate is incomplete.

**Decision:** Lena records **NO-GO for clinical connection** because identity association failed, even though SCH passed. Dr. Raman explains why wrong-image association is a patient-safety hazard; Dr. Park confirms no production clinical acceptance. Theo retains isolation and versioned rollback. Priya identifies the evidence and malware checks still required. Maya keeps continuity tasks active. The team logs missing tests and an explicit next gate; it does not silently “fix” HV-07 using future information.

**Conditional branches:** A participant who treats a successful login as full recovery fails the clinical integrity criterion. An alternative candidate may be evaluated in a **new** isolated test with its own version and receipts. If test evidence is insufficient, record **unknown**, not a pass.

### Final facilitator card — HV-08 (after Round 6 freeze, minute 90; optional follow-on)

**HV-08; fictional 10:40 UTC, released only after all HV-07 decisions are frozen:** A separately labeled **B-A-v2 isolated candidate** now passes the supplied test-manifest image-to-encounter linkage and the two specified SCH transactions. A bounded isolated telemetry view reports no *new* encryption-like event in its **30-minute observed window**. The facilitator supplies **no** production reconnect receipt, complete historical malware analysis, comprehensive PHI inventory, validated bedside dependency, or owner-signed RTO/RPO. A narrow isolated pass is not a site-wide claim.

**Recovery decision and boundary:** The team may propose a **staged** return plan with signed clinical criteria (Dr. Park and Dr. Raman), security gate (Andre/Priya), technical implementation authorization (Theo and service owner), independently witnessed production tests and rollback. Do **not** record the service as restored: the supplied data prove an isolated candidate result only. If decision rights, source integrity, reconnection path or clinical handoff are unresolved, clinical continuity measures remain in effect. A hypothetical future production acceptance needs a **new** evidence card, not an inference from HV-08.

## 5. Worked decision contrasts and consequences

**Worked example A — 08:46, a bounded proposal:** “HV-01/02 establish suspected ransomware and unknown onset; HV-04 identifies WS-17 as administrative with a high-confidence signal. Recommend a time-limited WS-17 quarantine **pending** Andre's cyber approval and Theo's endpoint ownership check, with Priya collecting an authorized read-only EDR export first if patient safety allows. Dr. Park/Sofia must verify that the target is not clinically coupled. Measure endpoint network state and unaffected care paths separately; reopen at the next defined check. Do not isolate the full subnet on the obsolete map.” This is a defensible **proposal**, not evidence that quarantine happened or worked.

**Contrast A (unsupported):** “The entire hospital network is infected; disconnect all bedside machines now.” HV-04 does not demonstrate that spread or safety. Corrective action: freeze the proposal, identify missing dependency verification and return authority to the clinical lead.

**Worked example B — 10:05, a failed gate:** “HV-07 supplies a synthetic scheduling pass but one demonstrable image-to-encounter mismatch. Mark the isolated candidate **NO-GO**, retain the test evidence, ask Dr. Raman to define an independent identity-binding retest, and avoid production reconnect. Continue a clinically governed downtime pathway.” This preserves patient-safety reasoning despite pressure for quick availability.

**Contrast B (hindsight):** “HV-08 eventually passes, so the 10:05 approval was correct.” HV-08 was not released at 10:05; revise the decision **after** release, retaining the earlier no-go. A later pass never retroactively repairs a decision's missing evidence.

**Worked example C — suspected data theft:** “HV-06 is a volume observation plus an adversary claim. Open an investigation and privilege-aware data-risk assessment; do not describe either confirmed exfiltration or no PHI exposure to patients. Submit the draft to clinical and legal review.” A small flow is not a clean-room negative control; unexplained traffic is also not proof of which data moved.

### Conditional consequence grid (facilitator may use, never present as observed fact)

| Participant branch | If the required approvals and checks are obtained | If prerequisites fail or are skipped |
|---|---|---|
| Narrow administrative workstation quarantine | Record proposed, approved, simulated-executed and verified as **separate** classroom artifacts; service impact remains bounded to observed checks | Approval or effectiveness is **pending**; do not claim spread stopped |
| Broad network isolation | Consider only after current dependency verification and independent clinical safety sign-off, with reversal and communication plan | Stop; record foreseeable care interruption and an authority defect |
| Keep operating under downtime procedures | Clinical team sets monitoring frequency, identity reconciliation and threshold for escalation | Unverified paper handoffs or image associations remain a safety risk, not accepted recovery |
| Choose newest backup by job-success | Independently test provenance, bytes, content, malicious-change risk and clinically relevant completeness before promotion | Quarantine as candidate; no safe-restoration claim |
| Reconnect B-A based on SCH login | A **new** version must pass image identity, patient-safe workflows, security and production gates | HV-07 is a hard **NO-GO**; record cause and corrective test |
| Send external “no breach” statement | Only a supported, reviewed finding and approval process can justify a final claim | Hold the text; issue a narrower operational statement if approved |

No row guarantees attacker behavior, patient outcome, regulatory decision or a production result. Facilitators who want a changed outcome must write a **separately numbered hypothetical card** after the relevant decision, not silently amend HV-00–HV-08.

## 6. Recovery under uncertainty — explicit go/no-go contract

Before proposing any production connection, assemble a versioned acceptance packet. Each line has **evidence ID, tester, approver, result, test scope, date, residual risk and rollback trigger**. Missing or contradictory evidence is **not evaluated**, never “green by default.”

1. **Clinical continuity and timing:** Dr. Park identifies essential services, safe downtime/transfer plans, status of urgent workflows and reassessment interval. No loss target is fabricated from “same-day” language.
2. **Source and preservation:** Priya preserves relevant original telemetry and suspect-system evidence with custody, time correction and separate copy identifiers, subject to care safety and legal constraints. Evidence preservation and restoration do not mean the same thing.
3. **Candidate provenance and integrity:** Lena proves which backup and chain were used, reads back selected objects, verifies bytes independently and assesses compromise window, coverage and missing data. Hashes demonstrate identity of tested bytes, not benign content.
4. **Isolation and security:** Andre and Theo document permitted target, clean/rebuilt infrastructure rationale, access and credential containment, monitoring coverage, negative checks and residual threats. A short quiet telemetry interval does not prove eradication.
5. **Clinical data association:** Dr. Raman tests that the right image is linked to the right fictional encounter and correct patient/test identity; Maya and clinical owners test handoffs and reconciliation, not merely successful logins.
6. **Scheduling workflow:** Clinically approved test identities verify create, read, modify and audit behavior; compare counts and timestamps against a trusted approved reference, documenting untested routes.
7. **Technical return and rollback:** Theo uses a bounded, authorized promotion plan, independent production verification, stop triggers, monitoring interval, on-call owner and tested reversal. Do not invent a production success receipt.
8. **Explicit acceptance:** Dr. Park signs clinical go/no-go; appropriate service owners sign functional go/no-go; Andre signs the security risk statement; Ravi accepts any enterprise residual risk within authority; Marcus keeps data-risk/notification status separate. One signature cannot stand in for the others.

**Deferral rule:** If bedside dependency remains unknown, the image-identity test fails, an evidence-critical restore cannot be reproduced, or the actual clinical lead refuses, do not connect that candidate. Continue clinically approved alternatives, request missing evidence, and reassess. It is acceptable to finish the tabletop with “service still restricted” and a strong, reproducible decision record.

## 7. Required participant artifacts and templates

Submit **one frozen artifact per relevant round** plus a consolidated closing record. At minimum:

| Artifact | Required fields | Reviewer can falsify it by asking |
|---|---|---|
| **A1 Clinical safety board** | Service, critical workflow, bedside dependency known/unknown, fallback, clinical owner, reconciliation hazard, escalation trigger | Which source proves the equipment is safe to disconnect? |
| **A2 Evidence and release ledger** | HV ID, fictional time, source kind, release minute, collector/request status, chain of custody, hash meaning, missing clock facts | Was a later card cited before it was released? |
| **A3 Option/decision log** | Frozen clock and released cards, observations vs hypotheses, at least two options, risk to patients, exact approval, operator, readback and rollback | Is “approved” being mistaken for “performed and verified”? |
| **A4 Backup and recovery gate** | Candidate/version, provenance, time-window uncertainty, isolated tests and failures, clinical identity result, production approval pending | Which card proves image-to-encounter accuracy? |
| **A5 Communications record** | Audience, status at observation time, claims and uncertainty, clinical/legal/executive reviewer, approved vs unsent status, update trigger | Did an extortion demand become “confirmed patient-data breach” without evidence? |
| **A6 After-action plan** | Reproducible defect, cause/assumption, accountable owner, due date, measurable remediation and retest, status | What will prove that this gap actually closed? |

**Minimal log example:** “D-04 | exercise minute 47 | HV-00 to HV-04 | WS-17 suspicious; FS-IMG-02 dependency unknown | propose WS-17-only quarantine | cyber approval pending / clinical dependency review pending / execution not performed / verification not observed | rollback owner Theo | revisit after dependency review.” Keep the original if later cards change the action.

## 8. Evaluation rubric, calibration and safety gates

Two independent observers score only **frozen, actually submitted** artifacts; they may cite a specific artifact ID and released card. For each criterion: **0 = missing or contradicted; 1 = identifiable but missing an essential owner, evidence, time, limit or test; 2 = reproducible, bounded and appropriately authorized.** The ten criteria yield **0–20** points. A facilitator-skipped card is **not observed** and requires a documented conduct defect; do not award a participant zero for withheld evidence. Record disagreement and reconcile against written evidence, without pretending human review occurred.

| Criterion | Full-credit evidence (2 points) |
|---|---|
| C1 Clinical command | Dr. Park's distinct patient-safety authority, downtime owner and explicit safety stop |
| C2 Dependency uncertainty | Bedside/IMG dependencies remain unknown until source-backed checks; no unsafe disconnect |
| C3 Detection quality | HV-01/HV-02 disagreement handled with source scope, clock meanings and a falsifier |
| C4 Evidence preservation | Requests, receipts, copies and integrity claims distinguished with chain-of-custody limits |
| C5 Containment | Narrow, clinically assessed options with named cyber/service authority, cost, verification and rollback |
| C6 Decision chronology | Decisions freeze released evidence; no retrospective import of HV-07/HV-08 |
| C7 Privacy | HV-06 treated as suspicion, not confirmed PHI acquisition or an automatic clearance |
| C8 Communication | Separate operational and data-risk claims, named approvers, unsent/approved status and update plan |
| C9 Recovery gate | B-A/B-B provenance and unknown clean window, failed HV-07 imaging gate, independent retest and staged acceptance |
| C10 Improvement | Defect, owner, measurable retest and due date tied to observed exercise evidence |

**Noncompensable safety findings:** a proposal to change/disconnect clinical equipment without clinical authority or dependency review; forced production reconnect despite the HV-07 image mismatch; disclosed real patient data; or live technical execution. The facilitator stops the exercise and records **safety gate failed** regardless of numerical total. A 20/20 paper score **does not** prove CVRH or any real hospital can withstand ransomware, meet an RTO, avoid a breach or safely perform a production restoration.

Suggested interpretation for this original classroom rubric: **17–20** strong documented reasoning, **12–16** material gaps, **0–11** rework needed; always report any safety failure and unobserved criterion separately. These thresholds are teaching choices, not NIST certification or clinical accreditation.

## 9. Facilitator worked answers (retain until the corresponding round closes)

These are **acceptable example paths, not mandatory choices**. Another defensible choice passes if it meets the same scope, evidence, authority, safety and verification requirements.

| Round | Defensible answer and why | Unacceptable shortcut / facilitator response |
|---|---|---|
| Prebrief | Treat bedside dependencies and downtime exercise status as unknown; obtain clinical owner and stop criteria; verify authority before action | “Network map is enough.” Ask its age, source and clinical sign-off |
| 1 | Open suspected incident; preserve original EDR and backup records; compare time sources; prioritize clinical impact | “08:12 is first compromise.” Ask what the 07:58 storage warning represents |
| 2 | Dr. Park directs clinical assessment; Maya/Dr. Raman define safe fallbacks and patient/image identity checks; Sofia gates device changes | “Bedside screens work, therefore it is safe.” Ask for dependency proof |
| 3 | Consider WS-17 narrow containment with cyber approval and clinical dependency clearance; keep proposed/approved/executed/verified distinct | “Cut the whole subnet.” Present the unknown shared route and stop card |
| 4 | Treat B-A and B-B as candidates; prefer an isolated, versioned test; define clinical acceptance and data/time uncertainty | “08:15 job complete means clean.” Ask for independent readback and content tests |
| 5 | Investigate potential exfiltration with Marcus; hold categorical claims; Dana drafts a reviewed operational statement | “38 MB equals patient records.” Ask for recipient, payload and data-owner evidence |
| 6 | Fail HV-07 clinical gate for incorrect image linkage, despite passing SCH login; keep isolation and downtime plan | “We can go live for speed.” Require clinical no-go and negative-control analysis |
| Final | HV-08 permits **consideration of a new stage**, not retrospective approval or production restored claim; request separate promotion, verification and clinical acceptance | “Everything is clean for 30 minutes.” Ask what the sensor covered and did not |

**Facilitation method:** Ask each team to state the source IDs, evidence release minute, authorization, competing hypothesis, consequence to care and next trigger. Do not provide a “magic” log or clinician decision not in the card. If a learner chooses a different clinically safe bounded branch, acknowledge it and ask for its verification plan. If someone cites HV-08 to excuse HV-07, preserve the original artifact and score chronology, then allow an openly labeled later correction.

**Example score reconciliation:** C9 receives 1 from observer Jordan and 0 from a second observer when the participant writes “B-A restore passed; release.” On checking A4, the only test cited is SCH login and HV-07's image mismatch is missing. Since the submitted claim is **contradicted**, the reconciled C9 score is **0**, with the unsafe-reconnect condition investigated separately. An oral explanation added after freeze becomes a new artifact, not a rewrite of the scored submission.

## 10. Debrief and measured improvement

Allow 25 minutes and record: **(1)** which patient-care dependencies were assumed rather than verified, **(2)** what the 07:58/08:12 conflict does and does not establish, **(3)** which owner could approve each action, **(4)** whether a clinical stop blocked an attractive cyber action, **(5)** which backup properties were never proved, **(6)** whether an imaging identity mismatch blocked return, **(7)** which message would mislead patients or regulators, and **(8)** how a different shift could audit the frozen decisions. Explicitly separate improved classroom reasoning from real hospital readiness.

| Example after-action item | Accountable team and proposed due date | Retest and success evidence |
|---|---|---|
| **I-01: Unverified bedside-to-network dependency** | Sofia / Biomedical + Theo / Network; 30 days after exercise | Clinical leader witnesses read-only inventory reconciliation and an approved non-disruptive dependency drill; signed diagram/version and exceptions |
| **I-02: Untested SCH/IMG downtime handoff** | Dr. Park, Maya and Dr. Raman; 45 days | Simulation of outpatient scheduling, urgent imaging request and identifier reconciliation; frozen handoff sample with no wrong-image association |
| **I-03: Incomplete backup-chain proof** | Lena / Backup and Priya / Evidence; 30 days | Isolated restore of approved fixtures with source provenance, independent readback, integrity checks, malicious-change controls, measured recovery time and documented residual risk |
| **I-04: Premature external claim risk** | Marcus / Privacy and Dana / Communications; 21 days | Two mock injects (unknown outbound traffic; proven PHI access); reviewed distinct messages and notification-decision evidence, never sent externally |
| **I-05: Decision receipt ambiguity** | Andre / Incident Command; 14 days | A new team can distinguish proposed, approved, simulated-executed, verified and clinically accepted statuses from the same log without verbal repair |

Dates are **suggested fictional improvement targets counted from the exercise date**, not obligations of NIST or of a real hospital. Record actual assignments only in an authorized setting. The scenario is complete as a teaching exercise when A1–A6, scores, safety findings and the action plan are captured; **the fictional incident itself may remain unresolved** and clinical operation may remain restricted.

## 11. Primary references and rights

1. [NIST SP 800-61 Rev. 3 (2025), Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — response-in-risk-management and the updated lifecycle; not a hospital operating procedure.
2. [NIST CSWP 29, Cybersecurity Framework 2.0 (2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — six Functions and outcomes; nonprescriptive.
3. [NIST IR 8374 Rev. 1 (2026), Ransomware Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/ir/8374/r1/final) — ransomware-oriented risk governance, protection, detection, response and recovery.
4. [NIST SP 800-184, Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning and testing; older guidance should be contextualized.
5. [HHS, HIPAA Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) — U.S.-specific covered-entity/breach context, not a determination on these fictional facts.

All participant cards, teams, case details, decision examples, scores and exercise gates are newly authored fictional educational material. External references are **linked and summarized, not copied or relicensed**; maintainers' original content follows [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md). This exercise does not award an academic or clinical credential, guarantee a secure system, establish hospital compliance or replace medical/legal advice.
