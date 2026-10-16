# TableTop 05 — Suspicious data export: an account event is not a finding about a person

**Edition:** English · **Exercise ID:** TTX-IDE-05 · **Catalog scenario ID:** `insider-data-export` · **Editorial date:** 2026-10-15  
**Editorial status:** Original fictional defensive exercise; independent technical, privacy and human review pending.  
**Format:** Facilitated paper-only discussion: 15-minute briefing, 90-minute staged exercise, 25-minute debrief. No active data transfer, interrogation, endpoint investigation, real account access or live report generation.  
**Scope:** This document deepens the fifth entry in [the existing ten-scenario catalog](../../../web/tabletop/scenarios.json); it does not duplicate or modify that catalog. Return to the [incident-response playbook index](../README.md). See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Fictional setting, uncertainty and learning objectives

**All people, organizations, customers, account identifiers, destinations, jobs, time stamps, observations, communications and outcomes in this exercise are synthetic.** They are not real employee or customer records and have no evidentiary standing outside the classroom. The packet contains no customer names, email addresses, identifiers usable for access, actual records, secrets, extraction commands, data movement instructions or operational test endpoints. Do not access employee communications or HR files, send data, trigger exports, contact actual recipients, change live permissions or conduct surveillance during the tabletop. Use only the released cards.

Fictional **Elmwick Service Cooperative (ESC)** provides customer assistance and account reporting. Its reporting application maintains **customer-service dataset CDS-9**, whose fields include simulated account-service attributes. One staff account **staff-tm** is associated in the access register with employee **Talia Mercier**, an authorized reporting analyst. An unusually large **84,200-row** export job runs **outside the customary reporting window**, references destination handle **DST-771**, and is tagged with staff-tm. Talia says she *may* have been working on an authorized quarterly analysis, but cannot immediately recall the specific job or approved destination. This is neither an admission nor a reliable denial.

The initial audit proves an export **job record** and a **destination identifier**; its schema does not name the human who initiated the job or demonstrate a subsequent recipient download. “Insider” describes a possible organizational-access risk, **not** a finding of employee misconduct or intent. Several competing causes remain plausible: approved work poorly documented, scheduled automation acting within a staff account's privileges, mistaken configuration, external misuse of an account, or deliberate misuse. None is assumed equally likely, and none becomes a personnel conclusion without relevant evidence and a fair process.

### Six distinctions that must survive every round

1. **Account:** `staff-tm` is an application identity label. It identifies a credential/account context, not the person at a keyboard.
2. **Account holder:** Talia is listed as owner of that account. Employment ownership is not proof she initiated an event.
3. **Initiator:** the person, job scheduler, delegated identity or other process that caused the run. The job audit omits that field; attribution is **unknown**.
4. **Authorization:** the specific approved purpose, source fields, row set, destination, receiving role, period and independent approver. General reporting access is not approval for every export.
5. **Transfer and receipt:** job creation, source-side package generation, gateway acceptance, actual delivery and recipient **download** are distinct events, each requiring its own trace and coverage.
6. **Intent:** malice, negligence, mistake or permissible work cannot be established from an account tag, off-hours timestamp, a destination handle, or an employee's uncertain recollection.

**O1 — Governance:** Allocate data ownership, cyber response, IAM, employee-relations and privacy authority without silently transferring them to SOC or executives.  
**O2 — Evidence:** Build source-typed chronology, distinguish job state from network delivery and human attribution, preserve minimal reliable records with time and coverage limits.  
**O3 — Proportionate response:** Obtain **data-owner approval** before pausing the next scheduled export; separately verify implementation, business effects and permitted reporting continuity.  
**O4 — Purpose and destination:** Test competing hypotheses with approval records, destination authorization, minimized dataset scope and independently reviewed access evidence.  
**O5 — Recovery:** Restore only a purpose-limited extract after its fields, audience, retention, timing, approvals and independent controls have been validated.  
**O6 — Due process and improvement:** Avoid accusatory communications, prevent unnecessary employee/customer-data collection, maintain a documented fair assessment path and record measurable corrective actions.

### Mapping to NIST without manufacturing a personnel procedure

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (final April 2025) integrates response into [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final): **Govern, Identify and Protect** cover risk ownership, permitted processing, access and logging readiness; **Detect, Respond and Recover** cover detection, coordinated investigation, proportionate containment and validated restoration, with improvement throughout. This is **not** the former Rev. 2 four-stage flow. The exercise's role assignments, scoring, timing, HR process and approval gates are **original teaching adaptations**, not NIST or statutory mandates.

| Exercise activity | CSF 2.0 function(s) | Evidence-aware decision |
|---|---|---|
| Approved purposes, data inventory, destination register, least privilege, retention and HR/privacy boundaries | Govern, Identify, Protect | Who may authorize a particular processing operation? |
| Identify off-hours job, account context, requested destination and telemetry gaps | Detect | What was observed, and what is not proved? |
| Preserve scoped logs; approve and check scheduled-job hold; investigate initiating mechanism fairly | Respond | How to reduce risk without assuming misconduct or destroying evidence? |
| Verify minimum permissible fields, destination ownership/access, recipient obligations and bounded report tests | Recover | What can be restarted under the data owner's authority? |
| Assess logs, access workflow and employee privacy with an independent reviewer | Identify/Improvement, Govern | How will a later drill falsify the claim a control works? |

[NIST Privacy Framework 1.0](https://www.nist.gov/privacy-framework/privacy-framework) is a **voluntary** privacy-risk-management framework, not a universal employment rule or a determination of legal notice duties. [NIST SP 800-53 Rev. 5, updated publication](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) contains customizable security and privacy control families for access, audit, personnel and data processing; applying any controls here is a **scenario design choice**. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) gives older, contextual forensic guidance and is **not** a legal procedure or authorization to inspect personal content.

## 2. Teams, named people and separated decision rights

Each person and delegation below is fictitious. Real organizations must apply current policy, lawful process, contracts and jurisdiction-specific counsel. Two different signatures or perspectives remain distinct even if one learner plays multiple roles; a line manager's suspicion cannot bypass HR/privacy governance.

| Participant and team | Authorized classroom decisions | Not authorized to conclude or do |
|---|---|---|
| **Dr. Sanaa Whitcomb — Customer Data Owner** | Define lawful business reporting purpose, approve/deny the *specific scheduled export pause* and permitted future extract; sign final field/destination/access acceptance | Attribute a job to a person, inspect personnel records, or infer an external download |
| **Lucien Arora — Reporting Product Owner** | Explain job scheduling, dependencies, service effect, expected controls and reporting continuity; document operator versus scheduler uncertainties | Grant blanket export permission or call a queued report delivered |
| **Bruna Kepler — IAM and Application Access** | Inventory staff, service, delegated and destination privileges; implement separately approved scoped session/job access safeguards with readback | Impose broad employment sanctions or declare human initiator from account tag |
| **Eliot Navarro — SOC Incident Commander** | Open/triage case, authorize bounded investigative requests within policy, coordinate a proportional containment proposal | Accuse Talia, publish investigation details or order unauthorized employee monitoring |
| **Farah Wexler — Forensic Evidence Custodian** | Preserve minimized source audits, access/approval records and integrity/retention receipts; distinguish original, copy and derivative | Collect bulk customer contents or personal communications solely to satisfy curiosity |
| **Daria Quinn — People Operations / Employee Relations** | Arrange a non-accusatory factual clarification, fair notice/opportunity to respond as applicable, impartial handling and restricted case access | Decide guilt or impose a sanction from one suspicious account event; overrule counsel |
| **Helena Fong — Legal and Privacy Counsel** | Review authority, scope, confidentiality, retention, employment due-process safeguards and any later reporting question under applicable law | Declare a reportable breach or universally applicable employment-law consequence from synthetic facts |
| **Osman Doyle — Destination and Data Platform Steward** | Resolve DST-771 in the approved destination register, check specific transport/recipient access evidence and recipient-use conditions | Equate accepted gateway manifest with person receiving/downloading a dataset |
| **Willa Saye — Reporting Continuity Lead** | Maintain minimum permissible internal analytics through a controlled alternate report and record operational loss from the hold | Override data-owner approval or restore broad exports for a deadline |
| **Cora Mizuno — Communications** | Draft scope-limited internal/recipient messages and record independent review, approval and delivery statuses | Call a colleague dishonest, or claim customer data were stolen or safely received |
| **Magnus Bellamy — Executive Sponsor** | Allocate resources, authorize organizational escalation and accept bounded residual business risk within charter | Substitute for the data owner, HR/counsel due process or independent technical check |
| **Pearl Rivers — Neutral Facilitator and Observer** | Release synthetic injects, timestamp and freeze participant artifacts, score by published rubric and report scenario defects | Add logs to vindicate a favored decision or retrospectively revise a participant answer |
| **Talia Mercier — Account Holder / Witness (role-play only)** | Explain recollection and business context voluntarily via an HR-reviewed, neutral interview; offer records through authorized channels | Certify attribution by memory, approve her own processing request or be deemed at fault without corroboration |

**Authority contract:** Data owner authorizes processing/hold, application owner plans service impact, IAM executes reviewed access action, SOC frames evidence, forensic custodian preserves source, platform steward verifies technical destination, employee relations/legal govern fair fact gathering, executive manages organizational risk. Approval, operator receipt, effect readback and independent reviewer acceptance are **different events**. No person may transform a technical suspicion into a disciplinary finding by fiat.

## 3. Facilitator rules, release contract and privacy protections

The exercise uses sealed synthetic cards **ID-00 through ID-10**. Initially release only **ID-00**. The facilitator records **three different clocks**: source event time (UTC) printed on each record, the elapsed exercise minute when the card became available, and the minute a participant froze the decision. A later card describing an earlier event is **not available** to justify an earlier decision. Preserve every earlier snapshot and annotate later corrections as new records; never silently rewrite an unsafe or overconfident answer.

**Participant packet:** blank data-purpose register, job/destination ledger, source/acquisition sheet, bounded access matrix, pause authorization form, neutral employee-relations question set, recovery acceptance sheet, independent observer rubric and communications draft. Packet fixtures show **symbolic** account/destination IDs and aggregate counts only; no real customer rows or personnel files are needed.

**Required decision row:** `decision ID | source/event UTC | release minute | freeze minute | ID cards available | observations and limits | at least two hypotheses | exact job/data/destination scope | customer/employee/business costs | required authorizer | proposed/approved/simulated-applied/independently-verified statuses | next evidence request and trigger`.

**Evidence discipline:** Keep original log/source IDs distinct from read-only exports, hashes and analyst derivatives. Log request **is not** collection; SHA-256 equality of a selected audit-copy byte set proves only identity of those bytes, not the author's intent or audit completeness. Legal/privacy review sets purpose, access need, minimization and retention. Use restricted case access, neutral language and non-accusatory questions. Do not search personal devices, social accounts, conversations or mail without separately established authorization and proportional review.

**Stop card:** Stop the simulation if participants propose a real export, unapproved employee surveillance, posting a real customer's record, password use, exfiltration testing, mass disciplinary action, live account disablement, a legal conclusion without facts, or contact with a real external recipient. No classroom branch supplies actual privileges or a real employment finding.

## 4. Progressive injects and frozen decisions

The **90-minute exercise clock** is independent of fictional UTC case time. The observer must document that a complete artifact is frozen **before** the next card appears.

| Exercise minute | Release | Fictional event UTC | Primary question |
|---:|---|---|---|
| 0–7 | **ID-00** | 17:00 previous business day | Data-purpose baseline and authorized schedule |
| 8–18 | **ID-01** | 22:14–22:19 previous evening | Job vs account identity vs destination |
| 19–28 | **ID-02** | 08:48 next morning | Holder statement and neutral hypotheses |
| 29–40 | **ID-03** | 09:03–09:09 | Owner-approved pause and business consequence |
| 41–52 | **ID-04** | 22:10–22:23 historical; released late | Source/coverage and pipeline joins |
| 53–61 | **ID-05** | 09:34 | Read-only preservation and job hold readback |
| 62–70 | **ID-06** | 09:47 | Delegation, scheduler and identity limits |
| 71–78 | **ID-07** | 10:02 | Destination mapping and delivery gaps |
| 79–85 | **ID-08** | 10:19 | Authorized purpose/dataset contrast |
| 86–90 | **ID-09** | 11:05 | Isolated minimum extract test, no production restart |
| After final freeze | **ID-10 (optional)** | 11:40 | Separate future approval/readback, no retroactive repair |

### Prebrief — ID-00: approved use is specific (minute 0)

**Fictional 17:00 signed baseline:** Dataset **CDS-9** is available through an audited reporting service to an analyst account **staff-tm**, associated with Talia. Normal internal dashboards run at **09:00–17:00** business hours. A **monthly aggregate** extract has approved workflow **APR-AGG-12**, with up to **1,200 aggregated result rows** and **six nonidentifying reporting fields**, to internal approved destination **DST-214**. This is a *scope-specific* approval; it is **not** consent to export the raw CDS-9 customer rows elsewhere. Staff-tm can request export jobs but service scheduler and delegation rights are **not yet inventoried**. A supervisor's broad expectation of quarterly analysis does not define exact data, purpose or recipient.

A change in staff workflow could require after-hours processing, but no such exception is supplied yet. Data owner Sanaa must sign changes, platform steward Osman validates the destination and receiving permissions, Lucien owns availability/continuity. **Decision:** name the approved baseline, data categories, who could authorize a raw export, logs to preserve, and why a large off-hours event would be triaged without equating it to intentional misuse.

### Round 1 — ID-01: job logged, initiator and recipient unknown (minutes 8–18; Detect)

**Synthetic audit summary, previous evening:** At **22:14 UTC**, audit entry **J01** associates export job **JOB-880** with account **staff-tm** and dataset **CDS-9**, with destination identifier **DST-771**. At **22:18**, **J02** reports "export package prepared" and an **estimated 84,200 customer-service rows** from a broad source view. At **22:19**, **J03** reports "handoff enqueued" to destination service handle DST-771. **J01–J03 supply no actor/initiator field, authorization ID, recipient acknowledgment, external download receipt, or proof that the receiving party viewed any data.** The job is outside the usual time window and substantially larger than APR-AGG-12's 1,200 aggregates.

**Action and decision:** Eliot opens **ESC-IR-005** as **suspicious export activity requiring verification**, not as proved insider theft. Farah requests access-restricted source audit and logging coverage; Bruna checks scheduler and token/delegation inventory; Sanaa compares approved purpose/fields/destinations before choosing containment; Osman checks DST-771 ownership and delivery semantics. **Do not** contact or discipline Talia on the basis of an account label. Snapshot J01/J02/J03 separately: job record exists, package generation reported, handoff queued; actual receipt and download are not evidenced.

**Option A:** keep all future scheduled exports running pending a verified owner decision, accepting potential exposure risk. **Option B:** urgently seek authorization for a scoped pause of **JOB-880 recurring schedule**, with monitoring and safe internal reporting fallback. Either choice must state time/owner/service cost, but acting on the pause **without data-owner approval** fails the decision-rights gate.

### Round 2 — ID-02: the holder recalls a possible legitimate task (minutes 19–28)

**Fictional 08:48 UTC neutral statement (witness role-play):** Talia says, “I may have prepared a quarterly analysis, but I cannot confirm the exact job, export fields or destination from memory.” Her reporting calendar includes a quarterly review the next week, with **no attached destination authorization**. She does not say she intentionally sent customer rows; she also does not supply evidence excluding her account from the job. This statement is **uncertain witness context**, not an admission, denial, clearance or employment finding.

**Decision:** Daria and Helena prepare an appropriately scoped, unbiased fact-gathering process under applicable workplace and privacy protections. They avoid accusatory leading questions; preserve what the witness actually said; make clear that memory uncertainty is not proof of intent. Eliot keeps H1 approved-but-undocumented work, H2 scheduled/delegated execution, H3 mistaken configuration, H4 unauthorized account use, and H5 deliberate misuse as competing hypotheses rather than verdicts. Business relevance of a quarterly meeting may warrant checking task approvals, not surveillance or early HR sanctions.

**Alternative:** Do not request personal chats or full mailbox export automatically. First seek approved workflow/ticket metadata and administrative job origin within the event scope. Any need to expand to communications or personnel evidence requires separate legally reviewed authority, minimization and access controls.

### Round 3 — ID-03: data owner pauses the next scheduled export (minutes 29–40; Respond)

**Fictional 09:03:** Sanaa is reachable as **CDS-9 data owner** and reviews a **specific request** to suspend the next planned recurrence of JOB-880 while resolving purpose and destination. The service has two distinct reporting routes: scheduled raw export associated with JOB-880 and an approved internal aggregate dashboard **APR-AGG-12**. At 09:09 Sanaa signs **HOLD-OWNER-09** covering **future JOB-880 recurring raw export only** for a four-hour review window, with business rationale, explicit renewal owner and return conditions. It does **not** revoke the employee's whole account, stop the aggregate dashboard or establish that any previous delivery was prevented. Bruna is named implementation owner; Lucien/Willa are assigned continuity checks.

**Decision:** Eliot/Sanaa compare narrow hold, broader reporting shutdown and continued monitoring with no pause. The **narrow authorized future-job pause** protects the specific high-risk route while preserving permitted aggregate reporting. Bruna records **approved, execution pending**, requests a specific scheduler-state readback and verifies alternate routes rather than claiming protection by approval alone. Willa records possible delayed quarterly analysis; she cannot waive Sanaa's decision.

**Negative control:** A successful data-owner hold decision at 09:09 is **not** evidence that JOB-880 was paused, that already-enqueued data were recalled, or that every export mechanism was blocked.

### Round 4 — ID-04: limited source audit, actor is still unproved (minutes 41–52)

**Fictional forensic read-only export delivered 09:21, but released to learners only now.** It covers reporting audit for tenant **ESC-RPT**, the **previous evening 22:10–22:23 UTC**, plus selected identity events. Source clock is documented UTC with ingestion delay of up to two minutes; the card does not cover all devices, prior persistent sessions, personally held devices or destination-side use. The following records are **synthetic event facts, not executable data-export methods**:

| ID | Event / ingest UTC | Identity recorded | Source and action | State / limit |
|---|---|---|---|---|
| **J00** | 22:10 / 22:11 | staff-tm | IdP session refresh logged | Session linked to account; no person or originating device identified |
| **J01** | 22:14 / 22:15 | staff-tm | Reporting API JOB-880 request | No `initiated_by` or verified initiator; dataset CDS-9 and DST-771 |
| **J02** | 22:18 / 22:19 | reporting-worker | Source-side export package prepared | Count 84,200 estimated rows; no payload provided |
| **J03** | 22:19 / 22:20 | reporting-worker | Destination handoff queued | Queue state, not external receipt or download |
| **J04** | 22:21 / 22:22 | scheduler-service | Schedule record checked | Shows recurrence enabled at that source checkpoint; causation for J01 unknown |
| **J05** | 22:22 / 22:23 | staff-tm | Dashboard read in separate report path | Doesn't authenticate person, correlate to job initiator or prove download |

**Decision:** Farah preserves **source/export/derivative** IDs, collector, source kind, event/ingest clocks, narrow time scope, integrity/readback status, privacy access scope and original server retention. Ask for **request correlation ID, scheduler initiation provenance, approved ticket lineage and any delegated grant** where available. Do not infer “Talia was online and clicked export” from J00/J05. A refresh or job associated with a staff account is compatible with a token, scheduler or human action; the source omits the discriminating field.

**Worked distinction:** J02's successful package-preparation record supports **source-side creation**; J03's enqueued handoff supports **a pending transport state**, not recipient receipt. No item in ID-04 reports a destination-side download. A reported row count is an estimate of the package's scope, not proof all those rows reached an outsider.

### Round 5 — ID-05: verified hold and privacy-preserving evidence copy (minutes 53–61)

**Fictional 09:34:** Bruna's approved scheduler operation **OP-HOLD-21** states that JOB-880's *scheduled recurrence* was paused at 09:22 within the HOLD-OWNER-09 window. Independent application readback **STATE-0930** at 09:30 confirms that specific schedule disabled; **APR-AGG-12 remains enabled**. Farah's read-only copy request **REQ-AUD-1** receives bounded **ACQ-0932** at 09:32 with collector, source scope, audit rows J00–J05, acquisition UTC and access restrictions. A **separate** digest readback receipt **HASH-0933** confirms byte equality **for that acquired audit copy** at 09:33; this does not establish completeness of all identity/recipient records or truth of every record's assertion. No data content is copied for the class.

**Decision:** Declare only the **specific recurrence pause** verified for its scope; no claim about previous 22:19 handoff, alternative manual exports or unseen schedules. Sanaa schedules a review before the four-hour hold expires. Willa monitors internal aggregate reporting and any business need for an exception. Helena sets a retention/restricted access plan and prevents excessive employee/customer content collection. Farah keeps the independent audit copy separate from original source and derivative investigation notes.

**Alternate condition:** If a target schedule state's readback were missing, mark pause effectiveness **pending** and escalate through owner-authorized controls; do not disguise “approved” as “applied.”

### Round 6 — ID-06: delegation clues do not identify the person (minutes 62–70)

**Fictional 09:47 access inventory:** An IAM policy snapshot **ACL-47** associates staff-tm with application export permission; the reporting system also permits a delegated **scheduler-service** to request export work through staff-scoped jobs. The record of when the delegation was originally granted is incomplete. The source's **initiator field remains unavailable** for J01. A separate allowed analyst-access review lists Talia as the current account holder, but offers no confirmed workstation/device binding for 22:14. Daria/Helena have not established an employment misconduct record or approved any broadened investigation.

**Competing hypotheses to score:** H1 Talia submitted an approved task manually; H2 scheduled job ran under inherited account context; H3 another permitted delegate initiated it; H4 credentials or sessions were misused; H5 unauthorized purposeful export. All remain hypotheses unless a reliable request origin and approval/destination evidence discriminate. An unknown delegation history is a reason for **more bounded technical inquiry**, not retroactive blame.

**Decision:** Bruna reviews effective rights and narrows future raw export privileges only with Sanaa's consent and impact plan; Farah requests policy revision history, scheduler request trace and relevant source clock checks. Daria protects neutrality and opportunity to clarify once facts are available; Helena approves only necessary investigation depth. **Do not** automatically disable all staff access or publish Talia's name in an incident bulletin.

### Round 7 — ID-07: destination acceptance and download remain different (minutes 71–78)

**Fictional 10:02 platform report:** Osman resolves **DST-771** to a managed **transfer landing service**, not an identified human recipient. Destination registry **DEST-REG-14** shows it was created for a vendor-integration trial but is **not approved** for CDS-9 raw customer data. Its access-control register lists a service receiving role, not the person who might later download data. A limited gateway event **G01** at **22:24** shows the *service accepted a delivery manifest identifier* linked to JOB-880. The gateway does **not** attest that 84,200 full rows were written, decrypted, opened or downloaded by any recipient; destination object read/download logs for the relevant time are **not supplied**. Service-to-service delivery may occur without a person viewing anything, and manifest acceptance may precede actual object transfer.

**Decision:** Mark **destination use not approved for this dataset** in the supplied register; the scope of any actual off-platform data transfer/receipt remains **unknown**. Osman and Farah request independently authorized destination-side object creation/read audit (if retained and lawful), delivery acknowledgement with exact identifier, receiving-service permissions and source/destination size or completeness receipts. Isabel/Helena assess risk without asserting disclosure to an external person or wrongdoing by Talia. Sanaa decides whether any future CDS-9 sharing can be permitted; the earlier approved internal DST-214 does not grant DST-771 authorization.

**Negative control:** “G01 accepted manifest” is not equal to “recipient downloaded customer data,” and “not approved for CDS-9” is an authorization gap, not proof of motive.

### Round 8 — ID-08: a narrow approved purpose, not a blanket job clearance (minutes 79–85)

**Fictional 10:19 fully scoped owner register review:** Sanaa, with Lucien and Helena, supplies signed approved processing record **APR-AGG-12**: weekly/monthly internal service metric aggregates, up to 1,200 grouped rows, six specifically approved nonidentifying columns, destination **DST-214**, recipients restricted to internal reporting role **RPT-INTERNAL**, retention **30 fictional days**, and an owner/reviewer. The register is represented as **complete for the approved CDS-9 workflows currently visible to this owner for the incident period**, but does **not** establish that no private authorization exists anywhere outside the supplied governance process. No corresponding owner decision authorizing the **84,200-row raw CDS-9 export to DST-771** is present in this complete scoped register.

**Decision:** Classify JOB-880 as **unreconciled with the established approved-purpose register**, rather than finding Talia personally at fault. Keep the narrow recurrence pause while validating origin, intent, recipient use, any documented exceptional approval outside the source and actual data disclosure facts. Willa proposes continuity using the **approved, minimal aggregate report**, not automatically releasing JOB-880. Counsel retains the risk assessment and any jurisdiction-specific reporting question as open pending facts.

**Worked limit:** Lack of a matching approval in a defined authoritative register supports a **specific control exception**, not proof of dishonesty, intent or criminal activity. A future genuine approval would have its own time and scope; it could not retroactively establish that the earlier export to DST-771 was permitted unless valid documented authority and policy actually support that interpretation.

### Round 9 — ID-09: isolated permitted extract, independent acceptance still gated (minutes 86–90)

**Fictional 11:05 classroom-isolated fixture:** Data owner Sanaa and reporting lead Lucien review a proposed **RPT-AGG-NEW** report derived from **synthetic grouped facts only**, with the exact **six approved fields**, at most **1,200 aggregate rows**, destination **DST-214**, internal receiving role **RPT-INTERNAL** and the named retention setting. In an *isolated, paper-described mock test*, schema/row limit and an internal role-read test are **reported pass**; a negative control reports that a role outside RPT-INTERNAL is **denied** in that fixture. Farah records no live job execution and no real customer data used. The test does **not** prove production output, actual destination receipt, comprehensive authorization of other routes, or remediation of JOB-880's origin. An unsigned production restart would be premature.

**Decision:** Sanaa can endorse the **limited candidate** with Helena's privacy review and Lucien's business checks. Bruna/Osman propose a new exact-scoped production change envelope, independently reviewed destination and post-change readback, and an expiry/reassessment of HOLD-OWNER-09. Until those distinct approvals and production outcomes exist, report **the sensitive scheduled raw export held**, and **the minimal isolated report candidate tested**. Do not turn a successful test into evidence that unauthorized recipient access never occurred.

### Optional ID-10 — future evidence after all decisions are frozen

**Fictional 11:40, not part of the canonical case:** A facilitator may add a **separately numbered** source receipt from an independently verified report rollout, accepted by Sanaa and Helena, confirming the specified minimal fields and internal-only destination for a bounded production interval. That would support only the named approved extract and interval; it cannot prove who initiated JOB-880 or whether DST-771 ever received/downloaded the earlier raw package. Never cite this later receipt to repair the ID-07/ID-08 participant decisions.

## 5. Worked evidence and claim matrix

The six critical distinctions can be tested using only the printed cards. **No script, executable export, network request or identity access is required or represented as run.**

| Proposition | Supported observation and source | What it cannot establish |
|---|---|---|
| A staff-associated account appears in a job audit | J01 staff-tm / JOB-880, ID-01 and ID-04 | That Talia or any particular person started it |
| Source package was prepared | J02; estimated 84,200 source rows | That a recipient obtained or inspected all rows |
| A destination handle was used in routing | J03 enqueued and later G01 accepted manifest | That full data were transferred, delivered, downloaded or read |
| Data owner approved a broad export | **No such receipt** in supplied complete scoped owner register, ID-08 | That an employee acted maliciously or that no hidden authorization could ever exist |
| Future recurrence is paused | HOLD-OWNER-09 + OP-HOLD-21 + STATE-0930 | That yesterday's handoff was undone or all alternate routes blocked |
| Staff account was used outside business hours | J00/J01 source times | Identity of initiator, workstation, intent or valid exception |
| Destination has a service role | DEST-REG-14 service identity mapping | That a named human downloaded anything |
| Minimal candidate passed isolated checks | ID-09 synthetic fixture | That production ran, or past impact has been cleared |

**Reproducible control calculations:** An approved aggregate of up to **1,200 rows** and **six columns** is a different scope from **84,200 raw customer-service rows**. The difference in counts is **83,000 rows**, but this arithmetic is only a *size contrast*: the row types/semantics differ, so it is **not** a number of records definitively disclosed. The destination **DST-214** is an approved internal target; **DST-771** is a different service handle and not approved for raw CDS-9 in the scoped register. Neither row count nor handle proves what any recipient downloaded. Time difference between J01 (22:14) and J03 (22:19) is **five minutes**, not recipient dwell time or exfiltration duration.

**Negative controls to apply independently:**

- **NC-1:** Staff account is not a human initiator.
- **NC-2:** Off-hours use and uncertain recollection are not intent.
- **NC-3:** General reporting permission is not approval for an exact raw dataset and destination.
- **NC-4:** Job completed or package prepared is not transmission or recipient download.
- **NC-5:** G01 gateway manifest accepted is not complete object transfer or a recipient read.
- **NC-6:** A pause approved at 09:09 is not active until an independent scheduler readback, and does not recall past queued work.
- **NC-7:** A narrow audit query without destination download events is **unknown** unless destination logging coverage/completeness is established.
- **NC-8:** An isolated aggregate report passing six-field tests is not a proven safe production release.
- **NC-9:** No matching approval in the scoped register is a control exception, not a guilt finding.
- **NC-10:** Employee communications/personal-device acquisition is not automatically warranted by a suspicious job.

## 6. Proportionate containment, investigation alternatives and conditional consequences

The instructor treats each choice as a **proposal** unless the packet supplies a separately sourced, time-stamped action/verification receipt. No facilitated dialogue creates a real system action.

| Option | Authority, useful evidence and proportionality | Conditional consequence / common failure |
|---|---|---|
| **A: Pause JOB-880 recurrence only** | Sanaa's signed request, Bruna's scoped scheduler action and independent STATE-0930 | Prevents that specified future recurrence; not yesterday's job or all exports |
| **B: Disable staff-tm completely** | Separate IAM authorization, business impact and credible continuing account misuse evidence needed | Unjustified on account tag alone; interrupts legitimate reporting and risks prejudgment |
| **C: Freeze all reporting outputs** | Requires strong documented data risk, Sanaa/Lucien/Willa continuity approval and alternative service | Can harm customer assistance; broader than supplied evidence presently requires |
| **D: Continue without pause or review** | Would need an explicit owner decision accepting an assessed risk and monitoring plan | May allow recurrence of unresolved large export; not a safe default |
| **E: Preserve minimal audit and register records** | Farah/Helena restricted, specific source/query and purpose; record custody and retention | Avoid copying raw customer data, employee conversations and speculative dossiers |
| **F: Perform broad personal surveillance** | Requires separate lawful necessity, scope and employment/privacy approvals not supplied | Reject; presumed guilt and disproportionate intrusion |
| **G: Contact DST-771 operator** | Osman through pre-established service owner channel, counsel-approved disclosures | May clarify service-side logging; does not guarantee a human recipient attestation |
| **H: Restore narrow RPT-AGG-NEW** | Verified purpose, fields, DST-214 owner/access, Sanaa approval, Helena review, independent change/test readback | Isolated pass alone does not authorize production release |
| **I: Publicly call the employee a thief** | No evidence or decision authority supports this | Stop; preserves neither fairness nor technical accuracy |

**Decision exercise C-05:** Two responders disagree: one wants to immediately disable Talia's entire account to “stop the insider,” another wants only a scheduled export pause. A defensible reviewer begins with source/impact: no initiator, device or malicious action is proven; the specific future job has a data-owner authorizable control and an internal fallback. Select the narrow pause with readback and escalation triggers unless new evidence justifies a broader, independent IAM intervention. Record review date, potential alternate export routes and employee privacy safeguards. This is not immunity from investigation; it is proportionality under uncertainty.

**Counterfactual:** If a newly verified destination download later proves specific rows were accessed by an unauthorized receiving role, the data owner, privacy counsel and SOC reassess containment, recipient notice, lawful actions and risk. That **new evidence** must receive a new card/time/source; do not claim it exists in the original exercise.

## 7. Safe evidence preservation and employment due process

**This section is a governance/analysis checklist, not an investigation authorization or a jurisdiction-specific employment-law rule.**

1. **Authorize scope first:** Record the security question: how did JOB-880 arise, was the raw CDS-9 operation permitted, what left which boundary, and what recipient access occurred? Separate technical access need from personnel management.
2. **Preserve minimal original sources:** Obtain existing app, IAM, schedule, destination registry, gateway and approval audit records from authorized custodians. Prefer metadata and counts rather than raw customer contents; if original content becomes genuinely necessary, require a distinct reviewed purpose and protection plan.
3. **Mark provenance and custody:** Source identifier, collector and permission, event versus ingestion UTC, query boundaries, immutable copy identifier, hashing/readback status and restricted storage. A recorded request is not a completed acquisition; byte equality is not log completeness.
4. **Protect customers and employee privacy:** Restrict access by need, separate case roles from line management, define retention/legal hold, use neutral terminology, and prevent unnecessary copying or dissemination of sensitive information.
5. **Verify origin without blaming the holder:** Seek scheduler execution trace, delegation/service account binding, token issuance and device correlation **only within an approved technical scope**. A staff account label never identifies a person or their mental state on its own.
6. **Use fair fact gathering:** Employee relations and counsel decide whether/when to ask Talia neutral questions, retain answers verbatim, explain the process where appropriate and permit clarification; do not suppress contrary evidence or treat memory gaps as admissions.
7. **Ask destination questions separately:** Resolve service ownership and authorization, source-side enqueue, object creation/delivery, recipient login/download and completeness. A gateway accepted manifest and recipient download are not synonyms.
8. **Apply reversible containment:** Approve pause with the data owner, record exact job/route/expiry, verify independent state, preserve essential aggregate reporting and define a monitored restart decision.
9. **Escalate based on evidence:** If actual unauthorized recipient use or account misuse emerges, seek appropriate privacy/legal and HR review before public attribution or disciplinary decisions; preserve factual uncertainty and any labor/contract rights applicable to the real situation.
10. **Close only what can be checked:** A verified future pause and a tested narrow reporting candidate can coexist with unresolved investigation of an earlier export. Report separate financial/operational, security, privacy and personnel states.

[NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) emphasizes preserving and interpreting sources for IT investigations and cautions that forensics are not self-executing legal rules. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) is an older final guide for organizational log-management practices; it is contextual, and newer revision drafts should not be represented as final. [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework) frames privacy risks voluntarily and does not establish jurisdiction-specific due-process requirements.

## 8. Recovery and approval gates for a permitted minimal extract

**Recovery means re-enabling a legitimate business outcome**, not silently restarting the suspicious raw export. Any allowed extract needs a new, exact, documented **purpose-and-destination authorization envelope**. Data owner, platform steward, IAM, privacy reviewer and independent change checker must have distinct receipts.

| Gate | Evidence required | Owner and rejection rule |
|---|---|---|
| **G1 Purpose** | Signed business use, audience, duration, comparison with existing approval and alternative aggregation | Sanaa: "quarterly project" without exact purpose/approval is insufficient |
| **G2 Data minimization** | Six approved nonidentifying fields, aggregate granularity, up to 1,200 grouped rows, data mapping and negative field test | Sanaa + Helena: raw CDS-9 customer rows are not automatically permitted |
| **G3 Destination identity** | DST-214 trusted registry entry, owner, receiving role, external-sharing prohibition as applicable | Osman: DST-771 cannot be substituted from an email or a past job |
| **G4 Permissions** | RPT-INTERNAL scoped role, denied outside-role access, least privilege, accountable requesting identity | Bruna: service account reach and actual individual access are separate |
| **G5 Hold integrity** | HOLD-OWNER-09, OP-HOLD-21 and STATE-0930, expiry/review, other paths assessed | Bruna/Sanaa: an approved hold without application readback is not enough |
| **G6 Evidence and privacy** | Scoped retained logs, minimum data copies, source/copy provenance, personnel fairness plan, counsel review | Farah/Helena/Daria: do not collect a blanket customer or employee dossier |
| **G7 Isolated acceptance** | ID-09 schema/count/role tests and negative role test, fixture and timestamps | Lucien/Helena: isolated positive results do not certify production |
| **G8 Production release** | Separate exact-scoped owner approval, authorized operator, rollback, monitoring and independent live readback | Sanaa/Osman/Bruna: **not supplied** in canonical ID-09 |
| **G9 Prior-job resolution** | Origin assessment, approval reconciliation, destination-side receipt/download scope, lawful next owner and review | Eliot/Helena: status remains open; not a blocker to every safe aggregate report if separately controlled |
| **G10 Communication and residual risk** | Approved audience/status, no personal attribution without proof, executive risk record and next update | Cora/Magnus: case closure is not public accusations or unsupported "no breach" |

**Canonical end state (90 minutes):** A future **specific recurring raw export is held and read back**; the prior JOB-880 **was generated and queued**, while complete external delivery/recipient download remain unknown. The approved-purpose record does **not** cover the 84,200-row raw export to DST-771. The account holder's responsibility and intent are **undetermined**. A narrow 1,200-row aggregate candidate has passed isolated checks; production release is **pending** distinct approvals and readback. Security and privacy investigation of prior events remain open. An honest exercise may end with unanswered attribution and recipient questions.

**Critical negative test:** A model answer saying “HOLD-OWNER-09 proves the data never left ESC” is false. The pause is **later**, specific to recurrence, and cannot affect earlier enqueued activity. A model answer saying “the recipient downloaded 84,200 rows” is also false because neither J03 nor G01 supplies that evidence.

## 9. Learner artifacts and independent assessment rubric

Every team submits a **frozen** record for each round and a consolidated A1–A6 packet. Observers rate only actually supplied evidence, not oral details retroactively added after the next card.

| Artifact | Required content | Independent falsifier |
|---|---|---|
| **A1 Chronology and hypothesis ledger** | UTC event vs ingestion vs release/freeze, account vs person and H1–H5 with evidence limits | Was ID-07 or ID-08 used before release? |
| **A2 Approval and data minimization matrix** | Scope of APR-AGG-12, source fields/row types, DST-214 vs DST-771, missing approval, due owner | Which signed approval permits raw DST-771? |
| **A3 Job, delivery and custody chain** | J00–J05, G01, source/collection/digest, enqueue/manifest/receive/download gaps, minimization | What log proves recipient download? |
| **A4 Containment authorization ledger** | Sanaa's exact pause, Bruna operation, separate independent scheduler readback, duration, fallback, alternate paths | Was the hold merely requested or effective? |
| **A5 Bounded recovery candidate** | Exact fields/count/role/destination, role-negative control, G1–G10, production approval and rollback status | Which receipt proves production safe restart? |
| **A6 Privacy, HR and debrief record** | Neutral witness account, legal/HR gates, restricted record scope, approved/unsent messages, due action/retest | Did the team equate holder to perpetrator or collect unnecessary records? |

**Scoring method:** 10 criteria × **0–2** = **0–20**. **0** = absent/contradicted; **1** = relevant but missing essential evidence/clock/role/limit; **2** = complete enough for a separate reviewer to reproduce the reasoning from frozen artifacts. Record exact A-ID and released source in two independent reviewer sheets before discussing a disputed score. A facilitator failure to release a card is **not observed**, not a participant zero. These scales are original educational choices, **not NIST grading or employment adjudication**.

| Criterion | Full two-point evidence |
|---|---|
| **C1 Identity and attribution** | Staff account, named holder, initiator and intent separated; no guilt claim |
| **C2 Authorization** | Approved raw-versus-aggregate purpose, exact destination, owner and missing receipt assessed |
| **C3 Three-clock chronology** | Source/ingestion/release/freeze times; no future evidence imported |
| **C4 Transfer semantics** | J02 source package, J03 enqueue, G01 manifest acceptance and recipient download distinguished |
| **C5 Minimum forensics** | Scoped J records, source/copy/derivative, ACQ-0932/HASH-0933 and coverage limits |
| **C6 Proportional containment** | Sanaa approval + Bruna application + STATE-0930 readback, continuity and expiry |
| **C7 HR and privacy** | Daria/Helena impartial process, minimized customer/employee evidence, restricted access |
| **C8 Destination and access** | DST-771 owner and risk, RPT-INTERNAL role and unobserved receiving-person access |
| **C9 Authorized recovery** | G1–G10 including isolated-versus-production distinction, negative role and retention |
| **C10 Communications and learning** | Accurate pending status, no personal blame, accountable fixes and measurable retests |

**Noncompensable failures:** initiating any real export; unnecessarily collecting full employee/customer content; identifying Talia as dishonest from staff-tm label; obtaining private employee records without approval; disabling the account or imposing sanctions without owner/HR/legal process; declaring recipient download from J03/G01; or claiming an isolated test proves production acceptance. Stop the exercise and record **critical process failure** regardless of numeric score. Suggested classroom interpretation: 17–20 strong, 12–16 material gaps, 0–11 substantial rework; list unobserved cards and reviewer disagreements separately.

## 10. Facilitator worked answers and decision questions

**Release answers only after each participant's relevant decision is frozen.** Alternate branches may pass if they preserve evidence, purpose, fairness, authority and verification. No favored conclusion should be rescued by a fabricated approval or log.

| Round | Worked answer / justification | Incorrect shortcut and challenge |
|---|---|---|
| ID-00 | Staff-tm can request reporting, but APR-AGG-12 approves only internal six-field aggregates to DST-214 | “Analyst role permits every extract.” Which owner-approved destination and fields? |
| ID-01 | Record 84,200-row package prepared + DST-771 enqueued; initiator/receipt unknown; triage without accusation | “Talia stole 84,200 records.” Where are initiator and recipient evidence? |
| ID-02 | Treat Talia's uncertainty as neutral witness context, preserve alternate automation/delegation hypotheses | “Could be authorized” proves approval—or guilt. Which exact record distinguishes? |
| ID-03 | Sanaa authorizes recurrence-only hold, Bruna's execution **pending**; internal aggregates continue | “Owner signature proves all export stopped.” Which operational readback? |
| ID-04 | J00 session refresh and J01 identity tag do not identify a human; J02/J03 differ from recipient download | “22:14 outside hours = insider intent.” Could scheduler/service be involved? |
| ID-05 | OP-HOLD-21 and STATE-0930 support only this schedule; ACQ/HASH support scoped copy bytes | “The past queued package was recalled.” What receipt says that? |
| ID-06 | Delegated scheduler path is plausible; expand only scoped technical evidence; HR process impartial | “Account owner is definitely initiator.” Who does the source show as initiator? |
| ID-07 | DST-771 unauthorized for raw CDS-9 in register; G01 accepted manifest only; recipient access unknown | “Gateway accepted, so external human downloaded.” Where is the recipient read event? |
| ID-08 | Raw JOB-880 lacks matching approval in complete scoped register; personal intent still undetermined | “Unauthorized-by-register means criminal misconduct.” What evidence relates to intent? |
| ID-09 | Permit a narrow isolated aggregate candidate; do **not** claim production release or full prior-event resolution | “Six columns tested means case closed.” Where are production gate and receiving audit? |
| ID-10 optional | A future production receipt applies only prospectively to the narrow extract | “Later approval retroactively authorizes last night's raw export.” Which original approval was valid then? |

### Worked contrasting case: correct hold versus premature clearance

**Acceptable:** “At ID-03, Sanaa authorizes a four-hour pause of future JOB-880 recurrence. Bruna's scheduler execution has not yet been released. We will request independent state readback, preserve the 22:14–22:24 sources with minimum data, and keep approved internal APR-AGG-12 reporting. The holder's involvement and recipient download are unknown.” **Incorrect:** “The owner approved a pause, so data cannot have left and Talia is cleared.” A later verified pause cannot adjudicate the earlier job, and acquittal/accusation based solely on this action is unsupported.

### Worked contrasting case: manifest accepted versus recipient download

**At ID-07:** “G01 identifies a manifest accepted by DST-771 service, which is unapproved for raw CDS-9 in the scoped register. An accepted manifest does not prove complete customer rows were present at the receiving system or downloaded by a person. Seek authorized destination object creation/access logs and exact delivery receipts; maintain privacy and personnel neutrality.” A branch asserting data exfiltration to a human based on G01 alone receives **C4=0** when the statement contradicts its own evidence limitations.

### Independent practice IP-05 (paper only)

At minute 70, before ID-07, create a **seven-column table** for J00–J05: source time, recorded identity, event status, initiator certainty, authorization record, transfer/receipt evidence and next independently obtainable discriminator. At minute 85 append G01, DST-771 and APR-AGG-12 and revise **without deleting** the earlier conclusion.

**Worked explanation:** J00 refresh belongs to staff-tm, not a person; J01 job with staff-tm and DST-771 has initiator **unknown**; J02 84,200-row source package prepared by reporting-worker, not received externally; J03 enqueued, not downloaded; J04 scheduler enabled, not necessarily initiator; J05 dashboard read with staff-tm, a separate route. At 85, G01 adds **manifest acceptance only** and the data owner confirms no scoped raw-DST-771 approval. The investigation can find an **approval control exception** without a person's culpability or verified recipient download. Distinguish **not observed** from **no**.

### Scoring calibration and accepted alternatives

Observer Pearl scores C1 **0** if a submission names Talia as perpetrator solely from staff-tm. Another observer suggesting **1** because the account association was correct must reconcile to 0 for the **contradictory personal attribution**. A later correction is a new artifact, not rewriting the first.

At ID-03, a learner may reasonably propose expanding the pause to another exact identified schedule **if** they describe its separate data-owner approval, business impact and verification; it is **not** a supplied executed action. At ID-09, a team can keep even the minimal report paused if it identifies unresolved G1–G8 evidence and a proportionate continuity alternative. The rubric rewards defensible reasoning, not automatic restoration.

## 11. Communications, debrief and measurable improvements

**Internal draft only, not approved or sent:** 

> “An export job associated with a reporting account was observed outside its usual reporting window. We have paused the specified future scheduled raw-export recurrence and are reviewing whether the earlier job matched authorized purpose, destination and access controls. Available audit records do not identify the human initiator or establish recipient download. Authorized limited reporting remains under independent review. Please preserve relevant work records through approved channels and avoid speculation about any individual.”

Cora routes the draft to Sanaa, Eliot, Helena, Daria (for employee fairness), Willa and Magnus as appropriate. Log **drafted / reviewed / approved / sent / acknowledged** separately; do not portray the draft as an actual message or send customer notices without counsel's fact/jurisdiction assessment. Communicate with the account holder confidentially and neutrally, not through a public security bulletin.

In the 25-minute debrief, ask: Which fact is **observed** and which is inferred? What does “export completed” mean in each component? What did the staff-account tag not establish? What did the account holder actually say? Was the data-owner hold applied and independently checked? Did the team preserve only what was needed? Did any role misuse the lack of receipt as proof of no exposure—or the manifest acceptance as proof of recipient download? What evidence justifies restoring internal aggregate reporting, and what remains open from the prior job? How would a neutral reviewer evaluate the HR/privacy process?

| Improvement ticket | Fictional owner / proposed interval after exercise | Measurable independent retest |
|---|---|---|
| **I-01 Specific export approval envelope** | Sanaa + Lucien; 21 days | In isolated fixtures, permit only approved field/row/destination tuple; reject an exact 84,200 raw-row mismatch |
| **I-02 Job-to-initiator attribution capability** | Bruna + Osman; 30 days | Synthetic manual vs scheduled/delegated requests recorded with distinct initiator *type*, source trust and no human overclaim |
| **I-03 Transfer/receipt audit coverage** | Osman + Farah; 30 days | Fixture demonstrates separate generated, enqueued, manifest accepted, object created and authorized recipient downloaded states |
| **I-04 Owner-controlled recurring hold** | Sanaa + Bruna + Willa; 21 days | Pause only one approved schedule, independent readback, verify internal aggregate route and expiry/release control |
| **I-05 Privacy/employee fairness rehearsal** | Helena + Daria; 14 days | Test neutral interview, restricted access, minimization and independent review with a deliberately misleading account-holder label |
| **I-06 Approved minimal report acceptance** | Lucien + Sanaa + Cora; 35 days | Scoped six-column dataset and RPT-INTERNAL role pass positive test; unrelated role/destination fail; approved message stays factual |

These intervals and classroom thresholds are **fictional**, not NIST mandates or completed remediation. The exercise can be scored when A1–A6 and frozen decisions are submitted, even though the underlying **fictional incident is unresolved**. Neither a good tabletop score nor a simulated technical pause proves actual organizational compliance, employee misconduct, receipt by an external person or the absence of data exposure.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 (final April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — CSF-aligned incident preparedness, detection, response and recovery; not this classroom's prescriptive HR/role workflow.
2. [NIST CSWP 29 — Cybersecurity Framework 2.0 (final February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — nonprescriptive functions Govern, Identify, Protect, Detect, Respond, Recover.
3. [NIST Privacy Framework Version 1.0 (January 2020)](https://www.nist.gov/privacy-framework/privacy-framework) — voluntary enterprise privacy risk management, no legal force by itself; later draft revisions must not be called final.
4. [NIST SP 800-53 Rev. 5, updated publication and subsequent releases](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — customizable security/privacy control catalog for access, audit, incident handling and processing transparency; not an employment-law adjudication standard.
5. [NIST SP 800-86, Guide to Integrating Forensic Techniques into Incident Response (2006)](https://csrc.nist.gov/pubs/sp/800/86/final) — historical guidance on interpreting varied evidence sources, forensics within management/legal authorization.
6. [NIST SP 800-92, Guide to Computer Security Log Management (2006)](https://csrc.nist.gov/pubs/sp/800/92/final) — historical final guidance on log source collection/retention and reliability; draft revision is not represented as final.
7. [NIST Privacy Framework FAQ](https://www.nist.gov/privacy-framework/frequently-asked-questions) — confirms the framework is voluntary, regulation-agnostic and adaptable to diverse jurisdictions.

All source events, symbolic destinations, persons, customer-data field examples, counts, decision logs, scores and facilitator outcomes were **originally authored as invented classroom material**; no personal/customer data are exposed. External primary references are attributed/linked but their text is not copied or relicensed. Original OpenCyber Academy writing follows [RIGHTS.md](../../../RIGHTS.md) and its CC0 scope and third-party exceptions. This is not legal or employment advice, an accusation, an accredited qualification, or evidence of a real incident.
