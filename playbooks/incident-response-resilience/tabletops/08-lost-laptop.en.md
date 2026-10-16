# TableTop 08 — Lost field laptop: credential containment without invented breach certainty

**Edition:** English · **Exercise ID:** TTX-LFL-08 · **Catalog ID:** `lost-laptop` · **Editorial date:** 2026-10-15  
**Status:** Original fictional defensive tabletop, published as learning material; independent technical, privacy and human review pending.  
**Audience:** Field engineering, service/data ownership, endpoint/MDM, IAM, SOC/forensics, legal/privacy, employee support, recovery, communications, executive command and facilitators.  
**Run time:** 15-minute prebrief, 90-minute progressive exercise and 25-minute debrief. All simulated evidence is provided on paper; no actual device, account or customer data is used.  
**Navigation:** [Previous tabletop — 07 Water-system controller anomaly](07-water-ot-anomaly.en.md) · [Incident-response playbook index](../README.md) · [Next catalog item — 09 Web application compromise (summary only, not an authored tabletop)](../../../web/tabletop/scenarios.json). This expands the **eighth** entry of the original ten-scenario catalog without duplicating or editing it. See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Entirely fictional incident and safety contract

**Everything is invented for this exercise:** the organization, device, human names, dates, asset and identity records, job sites, logs, control settings, credentials-as-labels, decisions and verification receipts. No real worker, physical device, account, password, token, access path, encryption recovery material or customer record is included. **SVC-FIELD-12**, **NB-FLD-027** and other identifiers are symbolic references, **never usable secrets or live asset identifiers**. Participants do not perform technical actions; all later 'results' are clearly labeled synthetic facilitator cards. Do not track a real employee's location, probe an account with a lost credential, remotely wipe an actual endpoint, or collect personal messages for this tabletop.

Fictional **Cairnshore Engineering Services (CES)** sends engineers to customer sites to document instrument installation and service compliance. Its field toolkit allows authorized offline work during network outages and later synchronizes reviewed service notes. Company-issued laptop **NB-FLD-027** was assigned to engineer **Keira Mbeki**. Keira reports that she cannot locate the device after travel between two scheduled job sites. She **does not assert it was stolen** and has no evidence that another person physically accessed it.

The device inventory says **disk encryption enabled**, but the field derives from an **old check**. MDM reports its last successful check-in **two days earlier**. A field application may have cached service credential reference **SVC-FIELD-12**, but neither its effective authorization nor its offline lifetime is initially known. At case opening there is no confirmed theft, credential abuse, data extraction, read of local files or legally classified breach.

### Distinctions no participant may collapse

1. **Missing/reported lost:** the custodian does not know the device's whereabouts. It may be misplaced, inaccessible, stolen or recovered later; none is demonstrated merely by a report.
2. **Stolen:** requires evidence supporting unauthorized taking. A missing laptop is not proof of theft; a later recovery is not proof of past non-access.
3. **Physically accessed/unlocked:** needs separate evidence. A signed-in account, a stale MDM state and an unconfirmed physical sighting cannot demonstrate a file was read.
4. **Encryption configured / attested / effective at loss:** asset checkbox, dated device attestation, key protection and actual lost-time state are **different claims**. Neither inventory's 'enabled' nor an old check-in proves present cryptographic protection or that no keys were accessible.
5. **Service credential possibly cached / still usable / successfully abused:** expected credential presence, cloud-side identity state, active or offline derivatives and observed access calls require separate source coverage. Revocation may block new **online** service access while not remotely erasing an offline cached copy.
6. **Data risk / proven disclosure / reportable breach:** possible local records and unknown encryption affect risk assessment; none establishes access, acquisition, unauthorized disclosure or a specific legal notification duty without substantiated facts and jurisdiction-specific review.

### Observable learning objectives

- **O1 — Governance and humane reporting:** identify accurate business/device custody, qualified change owners, immediate loss-reporting path, proportionate employee assistance and personal-data boundaries.
- **O2 — Source quality:** compare device inventory, MDM timestamps, identity and field-system logs with coverage and freshness; freeze observations separately from hypotheses.
- **O3 — Containment:** obtain appropriate service-owner/IAM authorization to revoke SVC-FIELD-12, distinguish action receipt from effectiveness, and independently verify rejection **without replaying the missing secret**; preserve relevant MDM and access evidence.
- **O4 — Data and privacy:** investigate potential local/offline data and device protection with limited evidence, while neither overclaiming encryption nor labeling the situation a proven breach.
- **O5 — Recovery:** provision a managed and currently attested encrypted replacement, issue distinct least-privilege time-bounded field credentials and restore only approved offline and online tools.
- **O6 — Reviewable outcome:** define acceptance gates, support safe field continuity, collect exercised decisions and worked answers, and establish measurable post-exercise improvements.

### NIST SP 800-61 Rev. 3 and CSF 2.0, not a rigid older phase recipe

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025 final) is a CSF 2.0 Community Profile replacing Rev. 2. It integrates **Detect, Respond, Recover** with organizational preparation and ongoing improvement under **Govern, Identify and Protect** in [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final). This paper's card timings, authorizer names, score values and response gates are **original instruction**, not mandated NIST practice.

| Teaching phase | CSF 2.0 connection | Required decision boundary |
|---|---|---|
| Preparation: custody, field-data categories, device onboarding, attestation freshness, service-account design | Govern / Identify / Protect | Which risks and owners existed before loss? |
| Detection and analysis: loss report, stale MDM and identity coverage | Detect | Which facts do current and historical sources actually show? |
| Containment: proportional account action, logging preservation, remote-action uncertainty | Respond | Revoke and verify the named online credential without claiming offline effects |
| Recovery: replacement device, restricted identity, safe approved field workflow | Recover | Independent new-device compliance and functional checks before acceptance |
| Improvement: test reporting, recent encryption evidence, offline privilege and logging | Govern / Identify/Improvement | Which repeatable negative-control test will demonstrate a real fix? |

Relevant context: [NIST SP 800-111](https://csrc.nist.gov/pubs/sp/800/111/final) describes storage encryption for laptops and other end-user devices but is **older guidance (2007)**, not proof that this missing device was encrypted; [NIST SP 800-124 Rev. 2](https://csrc.nist.gov/pubs/sp/800/124/r2/final) covers enterprise mobile-device management/lifecycle technologies, with applicability varying for laptops and the particular MDM product; [NIST SP 800-46 Rev. 2](https://csrc.nist.gov/pubs/sp/800/46/r2/final) covers telework, enterprise remote access and BYOD risk; [NIST SP 800-53 Rev. 5 Update 1](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) offers customizable access, media, audit and privacy control families. None is an individual device attestation or a universal reporting law.

## 2. Named teams, authority and conflicts of interest

These authorizations are **fictional teaching delegations**. A real organization needs its own approved IAM, endpoint response, employee/privacy and client communication rules. A tabletop participant may cover two roles only if independent decisions remain different signed records.

| Team / named participant | May decide or perform **in the simulation** | Cannot conclude or authorize |
|---|---|---|
| **Keira Mbeki — Field Engineer and Reporter** | Report last remembered custody, sanctioned work context and device uncertainty; provide relevant facts voluntarily; request approved replacement | Certify encryption remotely, determine disclosure, approve own credential exceptions or be treated as suspect without evidence |
| **Olan Mercer — Field Service Owner** | Define essential field workflows, access and downtime requirements; approve service impact of account revocation and replacement tool set | Waive security identity controls, inspect private employee material or assert the laptop was stolen |
| **Yasmin Gupta — Endpoint / MDM Owner** | Preserve permitted device inventory and dated attestation records; prepare approved missing-device mode and conditional remote action; enroll/attest replacement | Treat last check-in as current state, call queued wipe successful, or infer physical data access |
| **Benoit Fraser — IAM and Service Credential Owner** | Map SVC-FIELD-12 scope, online sessions and cached derivatives; approve/revoke/rotate its exact identity; obtain independent relying-service status | Declare all offline copies erased or prove effectiveness from an unconfirmed ticket |
| **Svetlana Cho — SOC Incident Commander** | Open incident, frame alternatives, coordinate narrowly scoped cyber response and escalation | Declare theft, negligent employee, exfiltration or a legal breach from suspicion |
| **Teagan Alvi — Forensic Evidence Custodian** | Preserve minimum access/MDM/system/audit records with clock, collector, custody, integrity and query limits | Collect personal location traces, files, photos or messages without separate proportional/legal review |
| **Violet Harel — Customer Data and Contract Owner** | Define possible field-data categories, approved local caching and contractual/service risks; review data-impact evidence | Assume all job records reside on the laptop or that an unproved data breach occurred |
| **Anoushka Wynn — Privacy and Employee Relations** | Govern employee-support contact, fair neutral fact gathering, data minimization, rights, retention and any jurisdictional notification assessment with counsel | Impose a workplace finding or universal report deadline based on the device's absence |
| **Cai Jensen — Field Continuity Coordinator** | Arrange temporary paper-approved service visits, handoff and safe queue reconciliation until tool access is restored | Bypass identity approval or import unverified customer records |
| **Felipe Lazar — Recovery / Endpoint Provisioning** | Prepare the managed replacement, restore only approved field tools and collect independent encryption/compliance attestations | Self-approve privileged credentials, treat enrollment alone as encryption evidence |
| **Bianca Ueda — Communications** | Draft limited employee/customer operations updates with named reviewers and delivery receipts | Claim 'customer data stolen' or 'encrypted and safe' absent evidence |
| **Zelda Nair — Executive Sponsor** | Allocate incident resources and accept qualified residual business risk under charter | Replace IAM/device/data-owner evidence or unilaterally clear legal/privacy issues |
| **Oberon Rios — Independent Facilitator / Evaluator** | Release fixed cards, time/freeze decisions, apply rubric and report unresolved findings | Invent logs to make a good ending, coach scoring or make real cloud/endpoint changes |

**Authority chain:** Olan owns field continuity; Benoit approves identity revocation and scoped reissue; Yasmin owns MDM state actions; Felipe provisions the replacement; Teagan preserves sources; Violet determines data category/custody questions; Anoushka limits employee and data investigations; Svetlana coordinates the security response. Zelda cannot override these technical facts. Record **proposed / approved / reported applied / independently verified / accepted** separately.

## 3. Facilitator packet, evidence rules and three clocks

Facilitator Oberon prepares sealed synthetic cards **LL-00 through LL-10**, releasing **LL-00 only** during briefing. Give participants blank **A1–A6** artifacts: custody timeline, MDM/encryption evidence sheet, credential/access-scope matrix, containment ledger, data-risk worksheet and recovery/communication sheet. Answers are withheld until the related round freezes.

**Clocks:** (i) *fictional source/event timestamp UTC*, including historical observations, (ii) *exercise minute of card release*, and (iii) *exercise minute when a team freezes its decision*. An October 13 MDM observation revealed in a later round was **not** known at an earlier exercise minute. Acquisition and log-ingestion times also differ. Historical records do not become current because the investigator reads them today.

**Decision record:** `decision ID | reported source/time | card release/freeze minutes | observed vs inferred | alternatives and disconfirming source | asset/credential/data scope | business and worker privacy cost | authorizers | proposed/approved/synthetic executed/independently verified | rollback/expiry | next check`. A missing field becomes **unknown**, not a negative finding.

**Safe evidence discipline:** Copy only authorized MDM/IdP/access/field-service log metadata required to answer explicit questions. Preserve original/source and collector/copy identifiers, acquisition time, query scope, retention and independent readback where possible. Do **not** collect Keira's personal messages, photos, private location history, nonwork account records or contacts by default. A conversation with an employee is an optional, supportive and neutral fact-finding step, not a forensic authorization.

**Stop card:** Proposals to track a personal phone without authority, log in using SVC-FIELD-12, actively test a missing credential, erase endpoint history, announce a breach from inventory checkbox, wipe a real device, disable all users indiscriminately or declare employee misconduct stop the classroom scenario. Any real security action follows distinct organizational consent, lawful authorization and risk review.

## 4. Progressive injects and immutable decision checkpoints

The exercise lasts **90 minutes**. Times below are fictional UTC on **15 October 2026** unless dated otherwise. Future facts must not be used in earlier frozen decisions.

| Exercise minute | Card | Fictional case time | Decision/output due before next card |
|---:|---|---|---|
| 0–8 | **LL-00** | Oct 13 / Oct 15 baseline | Custody and pre-existing controls, boundaries |
| 9–18 | **LL-01** | Oct 15, 08:40 | Lost versus stolen; respectful first response |
| 19–28 | **LL-02** | Oct 15, 08:55 | MDM and encryption freshness |
| 29–38 | **LL-03** | Oct 15, 09:10 | Service credential scope and access logs |
| 39–47 | **LL-04** | Oct 15, 09:25 | Data-at-rest and employee privacy assessment |
| 48–58 | **LL-05** | Oct 15, 09:40 | Narrow credential revocation plan and preservation |
| 59–67 | **LL-06** | Oct 15, 10:11 | Provider action and independent rejection |
| 68–75 | **LL-07** | Oct 15, 10:30 | Offline remote-action limitations, impact evidence |
| 76–83 | **LL-08** | Oct 15, 11:20 | Replacement device enrollment and fresh attestation |
| 84–90 | **LL-09** | Oct 15, 11:45 | Scoped field tools and conditional acceptance |
| After freeze only | **LL-10 optional** | Oct 15, 13:00 | Later recovery of old device, no retroactive clearance |

### Prebrief — LL-00: asset baseline is not current protection (minute 0)

**Fictional approved inventory** lists NB-FLD-027 assigned to Keira for authorized site visits, model category “managed field laptop,” and a corporate encryption policy requiring approved full-device protection, secured key material and documented compliance. The inventory's **encryption enabled** field was last explicitly evaluated **September 30**, **15 days** before this exercise. The MDM card's last successful check-in will be released later: do not assume it was at the time of loss. Offline work may include selected service-note templates, but no complete cache manifest is supplied at baseline. Field platform **FIELD-SYNC** relies on service identity SVC-FIELD-12, with least-privilege configuration **not yet verified**.

**Decisions:** Olan records which approved visits must continue and which safe paper-approved fallback exists. Yasmin lists the device and evidence sources needed for trustworthy enrollment/encryption claims. Benoit asks which account, target services, credential issuer and offline derivatives are authorized. Violet identifies permitted customer-data classes but does not state what is on this laptop. Svetlana prepares a provisional loss response; Anoushka emphasizes neutral reporting. No claim of theft, disclosure or encryption efficacy is supportable yet.

### Round 1 — LL-01: field engineer reports missing laptop (minutes 9–18; Detect)

**Fictional 08:40 report:** Keira cannot find NB-FLD-027 after travel between two scheduled site visits. She last remembers placing it in her approved work bag **the prior evening**, but is unsure whether it remained there. No independent witness, physical recovery or theft evidence is supplied. Her report is timely under a hypothetical internal policy that expects prompt notification upon discovery, but the case does **not** impose a universal legal deadline.

**Decisions and rationale:**

- Keira supplies **work-relevant** last-known custody, not personal movements, and reports any documented corporate access she reasonably remembers.
- Svetlana classifies **missing corporate field device with possible offline-access risk**, not a confirmed theft or data breach.
- Yasmin places the *asset incident record* into missing-device review under approved policy; **no successful remote device contact** is implied.
- Olan/Cai plan field service continuity and avoid encouraging reuse of unverified offline files.
- Anoushka limits follow-up to necessary facts and ensures there is no accusatory employee notification.

**Alternatives:** A) Wait indefinitely for recovery: avoids user friction but leaves possible service access unresolved. B) Immediately revoke all company accounts: broad service harm with no scoped evidence. C) preserve limited source records and prioritize the named cached credential while planning replacement: more proportionate. Conditional enterprise action still needs explicit authorization.

### Round 2 — LL-02: MDM last check-in and stale encryption state (minutes 19–28)

**Fictional 08:55 read-only MDM inventory export:** NB-FLD-027 last checked in successfully at **October 13, 08:55 UTC**, exactly **48 hours** before this collection. Its encryption dashboard label reads “enabled,” but that result refers back to a **September 30 policy/attestation check**; no fresh September 30–October 15 hardware, lock state, key protection or lost-time attestation is supplied. Device remote-wipe eligibility is shown as *configured*, not a command completion. MDM cannot currently reach the device.

**Decision:** Yasmin records **last observed management contact = 48 hours ago**, and **encryption status at loss = not independently attested**. This is not “device has been offline for exactly 48 hours”; a silent management channel may result from connectivity, power, policy, agent failure or other causes. Teagan preserves the original MDM export and acquisition receipt through authorized read-only interfaces. Violet/Anoushka include encryption uncertainty as a data-risk input without concluding readable data existed or were accessed.

**Negative control:** The old "enabled" indicator and a management check-in **do not** prove the device was protected at loss; the absence of a recent check-in **does not** prove a person accessed, powered on or stole it.

### Round 3 — LL-03: cached service identity and scoped log differences (minutes 29–38)

**Fictional 09:10 IAM and field-platform summary:** Device configuration says SVC-FIELD-12 was *eligible for offline credential caching*, but no post-loss source has inspected the lost machine. A central identity record associates the service identity with **field report-upload** access and **limited regional job-metadata read**; effective privileges of earlier issued tokens, local copies and delegated paths remain **not fully reconciled**. Two source records are supplied:

| Record | Source event UTC | Account/principal | Operation and status | Meaning and limit |
|---|---|---|---|---|
| **IAM-03A** | Oct 14, 18:12 | Keira corporate user | Successful ordinary login through an approved office context | Account use before reported loss; not proof NB-FLD-027 was present, or that Keira used it then |
| **SVC-03B** | Oct 14, 19:10 | SVC-FIELD-12 | Successful metadata-read request from a labeled backend sync worker | Service identity use before missing report; does not identify a person, show a device-side cache or prove customer-file access |

The source query covers a named corporate gateway and one field-service API over **October 14, 12:00–October 15, 09:00 UTC**, **not** every API, offline cache, earlier session, local file or external route. No source shows a successful post-report login by this credential in the covered routes at this checkpoint.

**Decision:** Benoit draws a **potential permission** matrix by resource, identity, issued credential lifetime and revoked derivative; unknown paths stay open. Svetlana separates the user account from the service account, historic request from present use, and scope from actually observed actions. Olan identifies which upload workflows may fail if SVC-FIELD-12 is revoked. Teagan preserves source/query bounds without downloading service-note contents.

**Incorrect conclusion:** “There are no suspicious accesses in this query, therefore the laptop was not opened and no files were read.” The log sources do not cover local data access or every identity route.

### Round 4 — LL-04: potential stored data, but no observed disclosure (minutes 39–47)

**Fictional 09:25 data classification review:** Field-data policy permits a restricted offline *service-note worksheet*, with customer identifiers minimized, for approved visits. The inventory has no reliable current file listing for NB-FLD-027. A week-old approved work order references **two assigned site tasks**, but is **not** evidence that any particular file was downloaded, locally persisted or read. The last successful field sync record is outside the reported loss window. No data extraction event, third-party possession or data-exposure receipt is supplied. Keira's personal device, personal accounts, private travel details and unrelated messages are out of investigative scope at this stage.

**Decisions:** Violet documents data classes as **possible**, not **confirmed present**. Anoushka assesses proportional minimization, access restrictions, support for Keira and law/contract questions that depend on actual facts and jurisdiction. Svetlana and Teagan request only permitted corporate-device, identity and field-app metadata; a content collection requires separate necessity, approval and safeguards. Bianca prepares a **draft-only**, strictly operational message if field visits are disrupted—no "breach" headline.

**Alternative:** A blanket search of employee personal content is rejected. Even if customer data may be present, the investigation must define a necessary and lawful question before collecting sensitive material.

### Round 5 — LL-05: source preservation and specific credential containment (minutes 48–58; Respond)

**Fictional 09:40 authorization packet:** Teagan's authorized read-only **REQ-LOG-05** requests relevant MDM state, service-token issuance/revocation metadata and gateway access events; by 09:36, source-specific archive **EV-ARCH-36** has a collection receipt with source/window, collector, restricted case storage and capture time. Independent readback of copy bytes **EV-HASH-38** is recorded at 09:38 for **that exported subset**, not every missing endpoint record. A separate request for offline token-generation history remains pending.

Benoit proposes **revoking SVC-FIELD-12** and any supported centrally managed active sessions issued under it, after evaluating exact permission and service dependency. Olan authorizes a bounded disruption to report-upload, with Cai's approved fallback. Svetlana coordinates; Yasmin records that device contact/wipe remains unavailable. No exposed token value, replay procedure or service-account password is printed.

**Decisions:** Benoit signs **IAM-AUTH-40** for the exact credential reference, change operator, relying services and independent verifier; Olan signs service impact; Teagan records that log collection is **partial**. Move promptly to revocation even if perfect logs are unavailable: preservation before a credential change is valuable, but an indefinitely active suspected cached secret carries risk. Record planned vs approved vs performed statuses separately.

**Conditional branch:** If a current authorized service owner had already migrated a field integration to a new restricted identity, verify that separately; do not assume one credential remains necessary forever. Do not revoke every service identity without owner/risk analysis.

### Round 6 — LL-06: revocation applied and observed online rejection (minutes 59–67)

**Fictional 10:11 independent IAM receipts:** Provider operation **IAM-OP-1002** reports SVC-FIELD-12 centrally revoked at 10:02. Independent administrator readback **IAM-STATE-1005** shows that identity/credential disabled in the named IAM service at 10:05. At 10:09, an existing passive gateway record **ACCESS-DENY-1009** associates an incoming request with the **revoked reference** and records **authentication rejected** on the named field API; the class did not generate the request and it does not attribute a human or device. A permitted application-owner check reports that an approved alternative field worker still functions with a separate identity. No record proves what is stored offline on the lost laptop or whether independent cached derivatives still work outside the checked services.

**Decision:** Benoit and Teagan distinguish **approved → provider-action receipt → independent disabled state → passive rejected request**. It is reasonable to say **the old credential fails for the observed online request and is disabled in the named IAM service**, not that every offline copy was erased, every account was safe or no data were accessed earlier. Olan/Keira must not "test" by signing in with the lost credential. If the relying-service semantics require separately invalidating sessions/refresh tokens, record a scoped follow-up rather than assuming revocation propagates immediately.

**Negative control:** A gateway deny can demonstrate specific online enforcement without proving which person tried access, how a local cache behaves offline or whether local disk encryption protected other files.

### Round 7 — LL-07: remote-wipe queued is not remote-wipe completed (minutes 68–75)

**Fictional 10:30 MDM status:** Under Yasmin's authorized device policy a **remote lock/wipe instruction is queued** for NB-FLD-027, but **no post-loss check-in, command acknowledgment, cryptographic erasure attestation or device receipt exists**. The asset location and physical possession remain unknown. A bounded follow-up identity query reports **no successful SVC-FIELD-12 use on the covered corporate API between 10:02 and 10:25**, but does not cover every route or local file access. Keira confirms she can continue essential on-site tasks temporarily through a supervisor-approved paper process; there is no evidence that the missing device was recovered.

**Decisions:** Yasmin marks remote action **pending/unverified**, not complete. Svetlana maintains the missing-device incident and follow-up monitoring. Violet/Anoushka update the data-risk statement: encryption at loss unknown, actual stored data unknown, unauthorized physical access unknown, online credential containment supported in named service, alternate routes under review. Cai preserves business continuity and reconciliation. Revocation evidence is positive for the **exact checked service** but cannot discharge the separate data disclosure assessment.

**Conditional branch:** If a later independent physical recovery occurs, isolate the found device **under authorized organizational evidence handling**, verify chain of custody and investigate damage/unauthorized access before reuse. Finding it would not automatically demonstrate that it was never accessed. This branch is not observed in LL-07.

### Round 8 — LL-08: replacement encryption is freshly attested (minutes 76–83; Recover)

**Fictional 11:20 replacement enrollment receipt:** Felipe provisions **NB-FLD-028** using approved managed-build image **FIELD-BASE-4** and policy profile **EP-ENC-4**. Independent endpoint owner Yasmin retrieves fresh signed **MDM-ATT-1118** at 11:18 from the **new** device, documenting management enrollment, disk-protection control state and key-protection compliance for the named profile. Independent policy readback **MDM-READ-1120** at 11:20 confirms the device remains enrolled/compliant, approved screen-lock policy and required endpoint security controls in this specific observation window. No recovery key or cryptographic value is disclosed. These are **fictional device-state receipts**, not proof the missing NB-FLD-027 ever met the same controls.

**Decisions:** Felipe submits the replacement for separate Yasmin review rather than self-certifying. Benoit prepares distinct **field identity SVC-FIELD-28** with **upload-only** project-scoped permission for specifically approved service reports and a defined offline lifetime; service owner Olan signs its necessity. Violet ensures no unnecessary customer dataset is copied to the replacement; Cai tests approved continuity and eventual reconciliation with paper-held tasks. **Do not restore a saved service credential or unreviewed backup from the missing laptop.**

**Limit:** A current policy check demonstrates configured/enforced attributes at 11:18–11:20 under the supplied trusted interface. It cannot prove future permanent compliance, immunity to physical attacks or retroactively cure missing-device encryption uncertainty.

### Round 9 — LL-09: approved field tools, identity and honest risk acceptance (minutes 84–90)

**Fictional 11:45 separate functional review:** Recovery test package **FIELD-TOOLS-APPROVED** contains only the approved inspection notes template, approved site schedule and field reporting client versions. In a **synthetic isolated, managed-device acceptance record** the named service owner checks one **test-only** service note completion and upload; the resulting artifact has the right fictional work-order association, no duplicate queued note, and audit evidence that **SVC-FIELD-28** may upload a permitted report while a negative access check to an unrelated project is **denied**. Yasmin independently rechecks enrollment/encryption policy status on the replacement. Benoit confirms SVC-FIELD-12 **disabled** in IAM-STATE-1005 and the separate passive online **ACCESS-DENY-1009** receipt; no actual test with the old token was run. Olan signs approved field service continuity. Anoushka and Violet sign a **data-risk statement with unresolved questions**, not "no breach."

**Acceptance discussion:** It is defensible to accept **the replacement-device/workflow track**, because (a) the lost service credential is rejected on a specified online path and centrally disabled, (b) the new device has fresh independent encryption/management attestation, (c) its replacement identity is least-privilege, and (d) approved field tools function in the bounded fixture. **Keep the missing-device data investigation OPEN**: NB-FLD-027 had no fresh lost-time encryption evidence, unknown local data and physical possession, and unverified remote wipe/offline derivatives.

**No-go alternatives:** If MDM-ATT-1118 is missing, do not certify the replacement as encrypted. If ACCESS-DENY-1009 is missing, retain an online revocation verification gate even if the operation ticket says complete. If SVC-FIELD-28 can access unrelated projects, reduce rights and retest. If the work-order identity is wrong, reject service recovery despite a successful login.

### LL-10 — Optional future device recovery; never rewrite old conclusions

**Fictional 13:00, released only after all LL-09 decisions freeze:** A separately labeled extension may report that NB-FLD-027 was found by a trusted corporate custodian with a signed transfer receipt, but **no live examination** of its prior use is provided. This could lower some physical-loss uncertainty prospectively and permit authorized evidence collection; it does not establish the device was never stolen, unlocked or read while missing. Do not use LL-10 to change the 08:55 encryption conclusion or erase an earlier residual-risk assessment.

## 5. Worked evidence timeline, scope and negative controls

The exercise uses **source-provided facts**, not a forensic lab. A different team can reproduce all supported conclusions from the released paper records.

| Proposition | Source(s) actually supporting it | What it does **not** prove |
|---|---|---|
| Engineer reported lost laptop | LL-01, Keira 08:40 | Theft, third-party possession or physical access |
| Inventory says encryption enabled | LL-00, September 30 record | Effective protection on October 15 |
| MDM last checked in | LL-02, October 13 08:55 | Offline continuously for precisely 48 hours or current device state |
| Service credential may be cached | LL-00/03 configured eligibility | It was present at loss, usable offline, or used maliciously |
| Historic service login occurred | SVC-03B October 14 19:10 | Same device, human, post-loss compromise or customer-file read |
| Data may be present | LL-04 approved offline capability/work orders | Files were actually cached, unlocked, read or copied |
| A limited audit copy was preserved | EV-ARCH-36 and EV-HASH-38 | Full log completeness or integrity of lost disk |
| Revocation succeeded in named IAM | IAM-OP-1002 and IAM-STATE-1005 | All derived/offline credentials invalidated everywhere |
| Revoked credential rejected online | ACCESS-DENY-1009 in covered field API | Person attempting use, or data absence on other paths |
| Remote-wipe action is pending | LL-07 queued status | Device received/acted on wipe or disk was erased |
| Replacement is managed/encrypted in stated window | MDM-ATT-1118 + MDM-READ-1120 on NB-FLD-028 | NB-FLD-027 encryption at loss or future infallibility |
| Approved field operation recovered | LL-09 bounded synthetic report, scoped identity | All field workflows/clients or old-device data exposure cleared |

**Reproducible clock check:** Last MDM contact was October 13 at 08:55 UTC, and the MDM export was October 15 at 08:55 UTC: elapsed **48 hours**. The encryption source is **September 30** and is older still. **Do not** call either "current at loss." Identity events from October 14 occurred before the October 15 08:40 loss report; whether the device was physically present during those calls is not independently established. In particular **reported time ≠ verified time last possessed**.

**Mandatory negative controls:**

- **NC-1:** Missing is not automatically stolen; recovered is not proof of no earlier access.
- **NC-2:** Inventory encryption checkbox is not a recent trusted attestation; the last check-in is not the lost-time state.
- **NC-3:** Revocation approval/operation is not independent online rejection; a passive deny is scoped to one relying service.
- **NC-4:** Online credential rejection does not remotely remove offline cached files or credentials.
- **NC-5:** A managed replacement's fresh attestation tells nothing about the missing device's actual security posture.
- **NC-6:** An incomplete cloud/field API query without suspicious results cannot rule out local data read or other service activity.
- **NC-7:** Assigned work orders do not prove specific customer data were copied to disk.
- **NC-8:** Remote wipe **queued** does not mean delivered, applied or verified.
- **NC-9:** An employee's uncertain memory is not proof of negligence or criminal intent.
- **NC-10:** A successful test upload on NB-FLD-028 is not a complete incident recovery or a legal breach clearance.

## 6. Containment alternatives and conditional consequences

All actions are **hypothetical choices** until a named later synthetic receipt proves a bounded action/effect. No branch asks a participant to use a live token or device.

| Option | Owner, justification, safety and verification | Conditional result / failure mode |
|---|---|---|
| **A. Wait for physical recovery before doing anything** | Would require accountable risk acceptance and short review interval; no such clearance is supplied | Leaves cached credential exposure risk uncontained |
| **B. Revoke SVC-FIELD-12 narrowly and verify** | Benoit identity approval, Olan continuity impact, Teagan logs, IAM state plus independent passive reject | Strongest supported containment for known online identity; offline derivatives remain unknown |
| **C. Disable every employee and field identity** | Unproven scope, substantial service cost, separate authorization needed | Disproportionate; may block urgent field work and obscure source attribution |
| **D. Queue remote lock/wipe** | Yasmin authorized policy and business-data considerations, device target verified, no destructive step in class | On unavailable device, queue state is **not execution or erasure** |
| **E. Announce encrypted and safe** | Would need current trusted NB-FLD-027 lost-time attestation and additional data-risk review | Unsupported; September 30 checkbox insufficient |
| **F. Declare breach based on absent device** | Would require fact- and jurisdiction-specific assessment by Violet/Anoushka | Unsupported; no theft/access/acquisition confirmed |
| **G. Search all Keira personal records** | Separate lawful need/approval, necessity, proportionality and retention safeguards required | Rejected on supplied facts; unnecessary privacy invasion |
| **H. Restore field service using old cached token** | Would violate scoped identity recovery and reintroduce exposure | NO-GO; use independently authorized new least-privilege identity |
| **I. Use managed replacement and approved scoped tools** | Yasmin's current attestation, Felipe onboarding, Benoit new grants, Olan business sign-off, negative access test | LL-09 supports a **bounded** recovered field workflow, not full impact closure |
| **J. Declare remote wipe successful from MDM queue** | Would require receipt/readback that the device actually processed command | Unverified; must keep pending |

**Worked containment contrast:** At LL-03 one participant says, "The identity logged in yesterday, so the lost laptop has been stolen and abused; wipe it and fire the engineer." That merges a service principal, historical network use, physical possession and employee intent. A defensible option is to preserve the permitted evidence, obtain Benoit's approval to revoke SVC-FIELD-12, independently verify online enforcement, keep offline/cache risks explicit and support the employee with a managed replacement. Severity can be high **without** invented wrongdoing.

**Conditional escalation:** If a *new* source later verifies unauthorized service use after loss, scope response to the actual service, identity, time and records; preserve proof and consult the data owner/privacy lead. If a physical device is recovered, handle it under custody rather than powering it on ad hoc. Neither possible future event is in the canonical LL cards.

## 7. Minimal evidence, employee privacy and encryption assurance

This is an **assessment checklist**, not authorization to search a device or process personal data. It is designed around source scope, fair reporting and case handling:

1. **Identify the accountable people** for device, data, IAM, field tools, security response, worker support and legal/privacy assessment before requesting intrusive action.
2. **Collect exact MDM state:** device ID, policy profile, source record, collection and last check-in timestamp, dated encryption attestation, management reachability, last known lock/key-protection controls and remote-command receipts. Do **not** interpret an offline MDM dashboard as the device's present state.
3. **Distinguish encryption evidence:** historical inventory tag, last trusted hardware/disk-control attestation, source provenance and relevance to actual lost interval. An attestation can support a dated state, not an immutable lifetime property. **For NB-FLD-027 the current/lost-time status remains unknown.**
4. **Map permitted offline data categories, not invented files:** field assignment permissions and maximum eligible data classes, approved cache behavior and retention, server-side sync/read summaries. Avoid copying all customer records or reconstructing private travel history.
5. **Preserve source and acquisition separately:** MDM export, IAM issuance/revocation, relying-service events and field platform logs with collector, UTC/time zone, retention, query scope, read-only copy and independent digest status. Logs outside coverage remain unexamined.
6. **Verify scope and revoke centrally:** determine which exact identity, tokens, sessions, delegation and resources were eligible; assign authorized IAM action. If a credential may remain cached offline, central revocation is not the same as erasing the physical cache.
7. **Validate without risky credential reuse:** an independent administrator state readback and existing **passive** rejected authentication event can substantiate online enforcement for named services; do not obtain/use the missing token to run a new test.
8. **Apply employee-data minimization:** speak to Keira respectfully, document only work-relevant custody and reported loss, shield private information from broad incident distribution and apply restricted case access/retention. Scope personal investigations separately under counsel and HR policy.
9. **Assess data-risk claims separately:** possible customer data categories, encryption strength at loss, access paths, actual observed read/receipt and coverage. Only qualified data/legal owners decide whether external notification thresholds and contractual obligations apply in the relevant jurisdiction.
10. **Track all pending controls:** remote wipe/lock queue, device return, credential derivatives, logs/attestation gaps, field report backlog and next review. “Pending” is a substantive answer, not a failure to complete the exercise.

A laptop is not necessarily the same platform as a phone/tablet MDM device; apply [NIST SP 800-124 Rev. 2](https://csrc.nist.gov/pubs/sp/800/124/r2/final) **to applicable management concepts**, not as proof an arbitrary laptop tool implements a specific capability. The storage-encryption categories in [NIST SP 800-111](https://csrc.nist.gov/pubs/sp/800/111/final) are relevant to risk modeling, but a disk-encryption product label is not an attestation. [NIST SP 800-46 Rev. 2](https://csrc.nist.gov/pubs/sp/800/46/r2/final) supports risk-based remote/field access design, without guaranteeing this field tool's implementation.

## 8. Replacement recovery and separate acceptance gates

**Recovery is not a single checkbox.** Online identity containment, replacement device security, field-work continuity, employee support and missing-device data risk are **separately owned tracks**. A signature cannot replace another role's evidence.

| Gate | Exact evidence necessary | Owner and NO-GO / open condition |
|---|---|---|
| **G1 loss classification** | Keira's report, asset ownership, physical custody timeline, neutral alternatives | Svetlana/Anoushka: no stolen/culpable verdict without evidence |
| **G2 source preservation** | MDM/IAM/gateway query provenance, collection receipts, readback and gaps | Teagan: request is not copy; subset hash not full completeness |
| **G3 revoked old online identity** | IAM-AUTH-40, IAM-OP-1002, IAM-STATE-1005 and ACCESS-DENY-1009 for specified path | Benoit + independent verifier: reject “failed” claim if no actual supported denial/readback |
| **G4 old-device cryptographic risk** | Fresh relevant lost-time encryption attestation if obtainable, key/lock context, physically verified state | Yasmin/Violet: **not established**; unresolved is documented data-risk input, not automatic breach |
| **G5 possible data exposure** | Actually stored data classes, service paths, post-loss access evidence, separate recipient/physical access and logging limits | Violet/Anoushka: no unsupported safety or disclosure verdict |
| **G6 managed replacement** | NB-FLD-028 inventory/ownership/enrollment, MDM-ATT-1118 and independent MDM-READ-1120 | Yasmin/Felipe: enrollment alone or old-device screenshot cannot satisfy |
| **G7 least-privilege offline access** | SVC-FIELD-28 narrow allowed resources, documented offline lifetime, no old credential restore; negative unrelated-scope check | Benoit/Olan: reject any unnecessary privilege or unbounded offline cache |
| **G8 approved tools/workflows** | FIELD-TOOLS-APPROVED version, authorized offline method, test-only note/work-order identity, no duplicate sync, service owner review | Felipe/Olan/Cai: working login is not completion or data-integrity acceptance |
| **G9 unresolved remote action** | Device-specific command ID, delivered/processed evidence if present, separate custody and return protocol | Yasmin: remote wipe remains **queued/unverified** in this case |
| **G10 risk/communications closure** | Honest case status, review authority, residual unknowns, next update, approved audience/delivery | Anoushka/Bianca/Zelda: do not send “encrypted and safe” or “breach confirmed” from unsupported facts |

**Canonical end at LL-09:** G3 is supported for the named **online** credential; G6, G7 and G8 are supported for the **replacement device and bounded synthetic workflow**; G4, G5 and G9 remain **unknown/open**, with unresolved physical loss and offline derivatives. Accept **the replacement's authorized field-service use** after its distinct owners sign. **Do not** close the original loss/data-risk assessment or assert that encryption was effective on NB-FLD-027 at the time it went missing.

**What a negative test actually shows:** The synthetic rejected unrelated-project access by SVC-FIELD-28 is a valid least-privilege check *for the specific service, time and permission tested*. It is not a guarantee about every route or future policy change. Fresh encryption attestation is **for NB-FLD-028**, not for NB-FLD-027.

## 9. Independent participant exercises and observer rubric

The facilitator withholds worked answers until each matching checkpoint freezes. Every exercise is **paper-only**, independently solvable from the supplied LL cards, and includes an objective, inputs, task, artifact and rubric.

### Independent practice EX-TTX08-01 — Classification without invented guilt

**Objective:** separate lost, stolen, accessed, exposed and breach. **Inputs:** LL-00 to LL-02. **Task:** classify each: (a) engineer cannot find laptop, (b) laptop was stolen, (c) its files were read, (d) it was effectively encrypted at loss, (e) a legally reportable data breach occurred. For each, provide source, confidence and one missing discriminator. **Artifact:** five-row observation/inference table. **Rubric:** 2 points each for correct classification and missing fact, maximum **10**.

### Independent practice EX-TTX08-02 — Dated encryption/MDM evidence

**Objective:** distinguish historical control status from present assurance. **Inputs:** LL-00, LL-02, LL-04. **Task:** calculate check-in age at 08:55 October 15 and explain why September 30 encryption flag, October 13 check-in and possible local-data classes cannot be combined into “the lost laptop was encrypted and no data were at risk.” **Artifact:** three-source confidence table with a risk update. **Rubric:** 2 points for exact 48-hour calculation, 2 for attestation freshness, 2 for local-data uncertainty, 2 for a valid next owner check, maximum **8**.

### Independent practice EX-TTX08-03 — Credential containment with independent receipts

**Objective:** justify proportionate service-credential revocation and effect verification. **Inputs:** LL-03, LL-05 and LL-06. **Task:** write five distinct statuses: proposed, authorized, provider-applied, independent IAM-state readback and observed relying-service rejection. Record scope/side effects and one important unknown. **Artifact:** signed hypothetical containment and evidence ledger. **Rubric:** 2 for independent authorities, 2 for source/clock distinction, 2 for bounded rejection, 2 for offline/derivative limit, maximum **8**.

### Independent practice EX-TTX08-04 — Remote wipe and privacy-limited risk

**Objective:** avoid overclaiming data exposure or employee fault. **Inputs:** LL-01, LL-04, LL-07. **Task:** contrast remote-wipe queued versus delivered versus cryptographically verified erased, identify privacy-minimal evidence sources and draft a non-accusatory two-sentence risk position. **Artifact:** conditional data-risk assessment with explicit unknowns and custodian/next trigger. **Rubric:** 2 for queue/receipt distinction, 2 for risk claims, 2 for privacy restraint, 2 for follow-up owner, maximum **8**.

### Independent practice EX-TTX08-05 — Acceptance of a replacement, not closure of old loss

**Objective:** evaluate conjunctive recovery evidence. **Inputs:** LL-06 through LL-09. **Task:** complete G1–G10 as passed/open/fail/not supplied; decide whether NB-FLD-028 may resume approved field work; list two reasons the original device incident must remain open. **Artifact:** owner-signed go/no-go sheet and a plain-language update. **Rubric:** 2 for identity validation, 2 for current encryption attestation, 2 for least-privilege/function, 2 for unresolved risks, maximum **8**.

## 10. Facilitator worked answers, competing choices and scoring

**Reveal only after the corresponding practice/round freezes.** The following are **acceptable bounded explanations**, not the only defensible paths. Any alternate requires source, owner, expected business/worker impact, independent verification and explicit limits. Do not backfill a missing result from later cards.

| Checkpoint | Worked decision with source and reason | Incorrect shortcut / discriminator |
|---|---|---|
| LL-00 | Inventory and prior device policy define expected controls; neither current encryption nor local data is proved | “Inventory says encrypted so safe.” When was that attested? |
| LL-01 | Record **reported missing**, not stolen; limit personal investigation and prepare targeted containment | “She lost it, therefore it was stolen.” Who witnessed taking? |
| LL-02 | 48-hour gap since MDM check-in; old Sept 30 encryption evidence not present-time protection | “MDM offline 48h means drive secure.” What evidence ties encryption to loss? |
| LL-03 | Separate user IAM-03A from service SVC-03B; no human/device or misuse attribution | “Service login means someone used missing laptop.” Which device/source? |
| LL-04 | Local data categories **possible**, actual files/reads unproved; minimize employee/customer evidence | “Two site jobs equal two client databases on disk.” Where is file evidence? |
| LL-05 | Obtain Benoit/Olan approvals; distinguish partial evidence copy, clock coverage and reissue dependencies | “Ticket requested = logs safe and key disabled.” Which receipts? |
| LL-06 | IAM action + independent state + passive gateway denial support **online** revocation for named service | “Old offline cache erased everywhere.” What device-side receipt exists? |
| LL-07 | Remote wipe queued, not delivered; preserve unknown encryption/access, verify exact covered API | “No check-in means wipe completed.” Which acknowledgment? |
| LL-08 | New NB-FLD-028 has **fresh** MDM-ATT-1118 and MDM-READ-1120; old device still unknown | “New device compliant proves old one was encrypted.” Which source spans old loss? |
| LL-09 | Accept bounded field note flow with new scoped identity and negative test; retain original data-risk case | “All work restored means no breach.” What about missing laptop contents/possession? |
| LL-10 optional | If recovered later, arrange safe custody and distinct permitted examination | “Found = never opened.” What evidence speaks to intervening custody? |

### Worked answer — EX-TTX08-01

(a) **Observed:** Keira reports missing NB-FLD-027 (LL-01). (b) **Not established:** stolen requires evidence of unauthorized taking. (c) **Not established:** files accessed requires a reliable physical/device/log source, not supplied. (d) **Unknown:** current-at-loss disk encryption not attested; Sept 30 policy result is historic and October 13 MDM contact is only presence/management history. (e) **Not established:** reportable breach depends on separately assessed actual data, controls, access facts and applicable rules; do not invent a deadline. A strong learner uses **unknown/not established** rather than automatically writing “no.”

### Worked answer — EX-TTX08-02

October 13 08:55 to October 15 08:55 = **2 days = 48 hours**. The Sept 30 disk-protection status is **15 calendar days** old; it does not prove last-boot state or the October 15 physical key situation. LL-04 adds possible approved offline categories, but no file manifest or read event. An evidence-bound risk update is “lost-time encryption unknown, potentially sensitive local data not inventoried, access not demonstrated; retain data-owner/privacy review and seek historical device attestation/custody evidence without personal surveillance.” Any recovered evidence would receive a separately dated update.

### Worked answer — EX-TTX08-03

`SVC-FIELD-12` is **proposed for revocation** (LL-05), **IAM-approved** by Benoit as IAM-AUTH-40 with Olan service impact, **provider-applied** by IAM-OP-1002, **independently state-checked** by IAM-STATE-1005, and **passively observed rejected** on the named field gateway by ACCESS-DENY-1009 (LL-06). The team itself performed no authentication. This supports online failure of the old reference in the covered service, not erasure of cached copies, universal session revocation or lack of earlier disclosure.

### Worked answer — EX-TTX08-04

The MDM command is **queued** at LL-07, with **no post-loss device check-in, delivery confirmation or erasure attestation**. The risk assessment remains “physical disposition unknown, loss-time encryption unknown, actual locally stored fields unknown, online service credential disabled in named IAM and one gateway denial observed; no proven theft, file read or disclosure.” Collect only company-owned device/identity/business metadata authorized by Yasmin, Teagan and Anoushka. Keep worker private accounts and location history outside scope absent separate authority. Set next review for additional MDM contact, device return, new permitted access evidence or data-owner decision.

### Worked answer — EX-TTX08-05

A defensible G1–G10 outcome at LL-09: **G1** report documented without theft claim; **G2** scoped source copy verified but completeness partial; **G3** online revocation **pass for named IAM/gateway**; **G4** old-device encryption unknown; **G5** possible data exposure unknown; **G6** new managed/encrypted device pass at stated observation time; **G7** new identity least privilege pass in tested fixture; **G8** named field workflow passes bounded test; **G9** queued remote action **pending**; **G10** replacement operational approval may pass while broader data/privacy closure remains **open**. Olan signs field return, Yasmin signs device controls, Benoit signs IAM restriction, Violet/Anoushka document open data-risk questions. No team declares a full incident clearance.

### Whole-exercise evaluation rubric (0–20)

For each item, score **0** = absent or contradicted, **1** = relevant but missing source, time, owner, test or limitation, **2** = a reproducible, bounded decision justified by the **then-released** evidence. Two observers independently cite A1–A6 before reconciling differences. A facilitator-missed card yields **not observed / exercise-conduct fault**, not participant zero. This is a classroom rubric, not a NIST certification or breach assessment.

| Criterion | Full two-point requirement |
|---|---|
| **C1** custody and classification | Missing, stolen, physical access, disclosure and intent clearly distinct |
| **C2** source time / freshness | Correct check-in calculation and encryption-attestation limitation |
| **C3** account/credential scope | User vs cached service identity, actual grants and unknown derivatives separated |
| **C4** evidence and privacy | MDM/IAM/source/copy/custody and worker data minimization maintained |
| **C5** authorized containment | Service owner/IAM sign-offs, no universal disablement |
| **C6** revocation verification | Provider action, independent state and passive rejected request with scope |
| **C7** remote-control reality | Queued remote wipe not reported as completed or guaranteed |
| **C8** replacement controls | Fresh NB-FLD-028 encryption/management attestation, no old-token reuse |
| **C9** field recovery | New least-privilege identity, safe approved tools, negative access/data-integrity test |
| **C10** truthful closure | Transparent unknown data risk, no false theft/breach verdict, action owners and retests |

**Noncompensable process stop:** publishing or testing a real credential, searching personal employee material without authority, executing actual remote wipe or device tracking for the class, making unsupported legal/breach claims, issuing unreviewed access, or labeling a person dishonest from loss alone. Stop, mark **critical process failure** independently of numeric score. Suggested classroom-only interpretation: **17–20 strong**, **12–16 material gaps**, **0–11 major rework**; state reviewer dissent and skipped cards. A high score cannot prove any real endpoint remains protected.

**Calibration contrast:** If a learner writes “IAM provider accepted revocation, therefore all offline caches are unusable,” score C6 **0** for a contradictory effect claim despite naming a real step. Another who writes “The provider state and passive field-gateway refusal establish a specific online block, but offline derivatives are unverified” may earn 2. A correction released after LL-07 is a new artifact, never a rewrite of the frozen LL-05 answer.

## 11. Debrief, communication and improvement backlog

**Unsent internal draft**, subject to Olan, Svetlana, Yasmin, Violet, Anoushka, Zelda and Bianca approval before any dispatch:

> “A managed field laptop was reported missing. We are reviewing device protection and relevant access records and have disabled the identified field service credential in the central system. A replacement device is being provisioned under current management and encryption controls so approved visits can continue. We have not established whether the device was stolen or accessed, what data may have remained locally, or whether a reportable disclosure occurred. We will update responsible teams when verified evidence changes those assessments.”

This draft is **not** approved/sent by virtue of being printed. Record `drafted / reviewed / approved / sent / acknowledged` separately. Protect Keira's privacy in all broadly circulated communications. External statements and legal notification depend on fact/jurisdiction determinations outside this scenario; no universal deadline is asserted.

**25-minute debrief:** Ask each role to show sources and clocks rather than an idealized story. What did “lost” prove? Why did the inventory checkbox fail current assurance? What can a 48-hour MDM gap establish? What did SVC-03B actually show? Which data categories could be present versus were demonstrated? Which parties could authorize revocation and field continuity? What exactly do IAM-STATE-1005 and ACCESS-DENY-1009 show? Why does queued wipe provide no erasure assurance? Which device has the fresh encryption attestation? What part of recovery is accepted, and which data-risk questions remain open?

| Improvement ID | Fictional owner and proposed time after exercise | Independent falsifiable retest |
|---|---|---|
| **I-01 recent encryption assurance** | Yasmin + Felipe, 21 days | Isolated managed-device fixture with intentionally stale encryption dashboard is **rejected**, current signed attestation/readback is accepted; audit detects age and policy gaps |
| **I-02 least privilege offline** | Benoit + Olan, 30 days | Synthetic short-lived field identity can upload permitted report, cannot read unrelated project, and fails after expiry at named online service |
| **I-03 rapid loss notification** | Keira's training lead + Anoushka, 14 days | Anonymous/synthetic loss report drill captures minimum work-relevant facts through approved channel without personal-location harvesting |
| **I-04 remote action and status truth** | Yasmin + Teagan, 28 days | Simulated queued/delivered/executed device commands yield distinct receipts; queued-only case is not scored 'erased' |
| **I-05 case source/copy sufficiency** | Teagan + Svetlana, 21 days | Read-only MDM/IdP/gateway evidence fixture includes complete provenance, independent copy hash and flagged query gaps |
| **I-06 verified replacement recovery** | Felipe + Cai + Violet, 30 days | New enrolled encrypted device completes scoped test-only field note with correct work-order association and no duplicate data; unauthorized role denied |
| **I-07 risk and communication discipline** | Anoushka + Bianca + Zelda, 14 days | Two deliberately misleading drafts (‘stolen’ and ‘no breach because encrypted’) are rejected and replaced with evidence-limited approved versions |

Time targets are **invented teaching proposals**, not regulatory or NIST deadlines and not completed remediation. The tabletop can be scored when A1–A6, EX-TTX08-01 through EX-TTX08-05, the rubric and the action owners are recorded. The missing laptop's **data-risk and physical-custody investigation remain open** while the new field device/workflow may be safely accepted within the supplied fictitious bounds. No real enterprise readiness, encryption status, criminal behavior or compliance is claimed.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management (April 2025, final)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — CSF 2.0-integrated incident response, not this tabletop's mandatory step list.
2. [NIST CSWP 29, Cybersecurity Framework 2.0 (February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — six voluntary, outcomes-based Functions.
3. [NIST SP 800-111, Guide to Storage Encryption Technologies for End User Devices (November 2007)](https://csrc.nist.gov/pubs/sp/800/111/final) — storage-encryption concepts and protection decisions; historical document, **not lost-device attestation**.
4. [NIST SP 800-124 Rev. 2, Guidelines for Managing the Security of Mobile Devices in the Enterprise (May 2023)](https://csrc.nist.gov/pubs/sp/800/124/r2/final) — lifecycle management, centralized enrollment and protections; platform applicability for laptops must be checked.
5. [NIST SP 800-46 Rev. 2, Guide to Enterprise Telework, Remote Access, and BYOD Security (July 2016)](https://csrc.nist.gov/pubs/sp/800/46/r2/final) — remote access and endpoint risk-management controls in field work.
6. [NIST SP 800-53 Rev. 5 Update 1, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — tailorable access, audit, media, encryption-related and privacy control families; not a certification or specific legal reporting duty.
7. [NIST SP 800-92, Guide to Computer Security Log Management (September 2006)](https://csrc.nist.gov/pubs/sp/800/92/final) — contextual historical log collection, time, analysis and retention considerations; newer drafts should not be claimed final.

All people, asset/device IDs, policies, service-account labels, evidence receipts, results, criteria and instructor solutions are **original synthetic educational material**. No third-party source text is copied wholesale or relicensed. Original material belongs within [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md) and its CC0 dedication scope and third-party exceptions. No customer personal data, employee private messages, working secrets or actual device command appears. The exercise is not a legal breach determination, forensic finding, employment accusation, accredited qualification, or real incident.
