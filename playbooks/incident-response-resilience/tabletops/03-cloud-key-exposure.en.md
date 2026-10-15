# TableTop 03 — Exposed deployment credential: audit evidence, bounded revocation and trustworthy recovery

**Language:** English · **Exercise ID:** TTX-CKE-03 · **Catalog ID:** `cloud-key-exposure` · **Date:** 2026-10-15  
**State:** Original fictional teaching material; independent technical and human review pending.  
**Audience:** Cloud project ownership, IAM, SOC, forensic evidence, development, locally authorized release operations, legal/privacy, communications, executive command, facilitator/evaluator.  
**Time:** 15-minute briefing, 90-minute round-based tabletop, 25-minute after-action review.  
**Relationship to catalog:** This document develops [scenario 03 of the existing ten-entry index](../../../web/tabletop/scenarios.json); it neither adds a scenario nor changes the catalog, a course book or a website. Return to the [incident-response playbook index](../README.md). See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Fictional context, boundaries and learning goals

**All names, projects, tokens, resource labels, times, event IDs, permissions, artifact identifiers, outcomes and numbers are invented classroom fixtures.** This is a paper exercise, not a live cloud runbook. No working key, credential prefix, secret material, test exploit, API request, production account, repository checkout, network action or runnable deployment workflow is provided. **CRED-DPL-7** is a fictional inventory *reference only*, not a credential value or usable key identifier. Do not copy a secret into any record, execute a token test, fetch an alleged historical leaked string, scan someone else's account, operate production, use GitHub Actions, or disclose customer data as part of the exercise.

**Fictional organization:** Northbridge Transit Analytics (NTA) runs a regional passenger-status dashboard. The fictional project **prj-passenger-prod** contains **svc-public-api**, **cfg-dashboard**, **bucket-render-assets** and **dataset-journeys**. Separate projects **prj-analytics-stage** and **prj-audit-vault** hold staging builds and independent forensic copies. A protected, locally authorized deployment broker traditionally used a long-lived deploy credential recorded in inventory as **CRED-DPL-7**, associated with a service identity **deploy-broker**. Engineering intended the identity to publish only approved dashboard artifacts. Its **actual effective grants**, inherited permissions and delegation are not known at the start.

At **09:00 UTC**, the credential value appears in a publicly visible source commit. An audit summary later shows unfamiliar use of the associated identity, but affected resource coverage is incomplete. The critical reasoning challenge is to preserve minimum trustworthy evidence **before** authorized rotation when feasible, act promptly to stop further credential use, identify what it could reach, verify recorded actions and actual resource changes, and restore an approved release path with **short-lived, narrowly scoped identities**. Publication alone proves exposure, **not** attacker identity, successful misuse, data theft, all-project compromise or customer impact.

**Four distinct claims must never be collapsed:**

1. **Exposed credential:** a public revision contains the actual value (withheld from this teaching file). Exposure is confirmed and merits protective action regardless of subsequent use.
2. **Observed credential use:** a provider audit event associates a request with a credential reference, principal, time and operation. It need not identify a person or prove the request succeeded.
3. **Unauthorized operation/change:** an actual state or operation is compared against an authoritative, complete approved change window, including scope and version. One unapproved resource reference is not an account-wide breach.
4. **Data impact:** content access, export, downstream effect and other identities require their **own** evidence and coverage. Missing events in a management-only query cannot prove no exfiltration.

**Objectives:** **O1** identify delegated authority and possible project/resource blast radius; **O2** preserve source, collection and chronological audit evidence; **O3** enact proportionate, independently verified credential revocation without unsafe use of the credential; **O4** distinguish metadata access, API requests, actual resource mutations and confirmed data access; **O5** recover with approved source→artifact provenance, minimal privilege, short lifetime and gated production verification; **O6** record honest communications, a measurable improvement plan and a handoff a different shift can reproduce.

### NIST alignment without claiming a prescribed NIST exercise

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), finalized April 2025, incorporates incident response into risk management as a [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) Community Profile. It replaces Rev. 2 and is **not** the old rigid four-phase response checklist. This tabletop aligns **Govern/Identify/Protect** with ownership, inventory, release approval and identity protections; **Detect** with exposure and audit evidence; **Respond** with triage, containment and communications; **Recover** with controlled identity and artifact restoration; and **Identify/Improvement** with corrective-action tests. The card release times, characters, scoring and approval forms are original classroom design, **not** mandatory NIST procedures.

| Function focus | Exercise decisions | What does **not** follow automatically |
|---|---|---|
| Govern / Identify / Protect | Name project, identity, IAM grants, approved manifest, retention and who may act | The word “deploy” is not an effective permission evaluation |
| Detect | Preserve public-revision metadata; separate unfamiliar audit use from hypothesis | A successful login/request is not necessarily an attacker or exfiltration |
| Respond | Acquire bounded source logs; approve and verify timely disabling; assess scope and changed resource | A request or approval is not execution or effectiveness |
| Recover | Test signed artifact in isolation; adopt short-lived scoped identity; independently verify production after approval | An isolated pass does not establish production acceptance |
| Identify/Improvement | Rehearse leak blocking, log completeness, credential expiry and negative controls | A tabletop score does not certify a real cloud environment |

## 2. Named role cards and noninterchangeable authority

These authorizations are **fictional**; real response actions require actual tenant, service and legal delegations. No role authorizes production work in the exercise.

| Team / named participant | May decide, approve or record | Cannot infer or override |
|---|---|---|
| **Elena Varga — Passenger Dashboard Project Owner** | Service-impact acceptability, bounded release freeze, recovery acceptance criteria and business go/no-go | IAM revocation, invisible log coverage or data-access clearance |
| **Hana Okoye — Cloud IAM Owner** | Evaluate credential/principal binding, policy version, inherited/delegated rights and authorized token disablement; approve replacement trust | That deactivating the parent token automatically kills every derived session |
| **Mateo Costa — Cloud Operations** | Execute a **separately authorized** IAM/project operation; capture independent provider receipt and readback; plan rollback | Self-approve broad tenant isolation or promote an unverified artifact |
| **Priya Raman — SOC Incident Commander** | Set case priority, coordinate investigation and containment approvals, define investigation questions and review clocks | Identify a human solely from a service principal or accept production for Elena |
| **Jonah Lee — Forensic Evidence Custodian** | Capture authorized read-only logs, source/derivative IDs, timestamps, integrity/chain receipts and unresolved coverage | Use the exposed credential, paste its bytes or declare an export complete from a request |
| **Amina Haddad — Development Lead** | Confirm public commit metadata and prior approved source; safeguard source history; attest approved build manifest and provenance | Claim deletion from HEAD revokes a key or run unknown artifacts |
| **Ravi Shah — Local Release Coordinator** | Prepare an authorized protected local release path, approved artifact request and short-lived federation proposal | Use GitHub Actions in this repository, operate live deployment or bypass independent review |
| **Isabel Cole — Legal and Privacy** | Analyze preservation/privacy obligations, scope of possible data access, disclosure and notification as facts permit | Assert stolen data or a universal legal reporting deadline from a service call |
| **Dana Moore — Communications** | Draft scope-bounded operational information with approval/sending/readback fields | Tell customers “all clear,” “breach confirmed,” or “attacker identified” without proof |
| **Evelyn Hart — Executive Sponsor** | Resource allocation, escalation and residual enterprise risk within explicit charter | Replace the IAM/project owner, reviewer, or production verifier |
| **Jordan Reed — Independent Facilitator/Observer** | Release synthetic injects, timestamp frozen artifacts, apply written scoring and document disputes | Invent missing logs, coach scored decisions, operate a cloud or pre-release later cards |

**Separate receipts:** A project owner's approval to pause deploys, IAM authorization to revoke a credential, operator's provider receipt, independent credential-state readback, deployment-owner acceptance and evidence of monitoring are different objects. Neither approval nor successful ticket creation proves any operation occurred.

## 3. Exercise packet, three clocks and required recording discipline

Only **CK-00** is initially available. The facilitator keeps **CK-01 through CK-09** sealed until their assigned exercise minute. Participants receive a blank **evidence ledger**, **IAM scope matrix**, **release manifest comparison**, **containment decision log**, **recovery acceptance sheet** and **observer score sheet**. One person may simulate multiple functions only if the written two-party authorization and independent check requirements remain separate.

Three clocks are recorded independently: **(a)** *fictional event UTC*, according to the specific source and clock confidence; **(b)** *exercise elapsed minute of release*; **(c)** *exercise minute when the participant freezes the decision*. A later card that describes an earlier event cannot justify a previously frozen action. Record whether a timestamp is event, collection, ingestion, approval or source-publication time.

**Decision row:** `ID | case checkpoint | exercise freeze minute | released CK IDs | observed evidence/source/limits | competing hypotheses | affected identity/resource | chosen option and service cost | owner and IAM/command approval | proposed/approved/executed/independently-verified | rollback/stop | next trigger`. If a field is unsupported write **pending / unknown / not observed**, not “no.”

**Safety stop:** No secret values, account calls, key “testing,” unapproved token rotation, live deployments, destructive alteration of historical evidence, invented collection receipt, customer disclosure, production commands or GitHub Actions. A paper-only request for evidence is allowed; do not mistake it for acquisition. This is also a no-credential publication safeguard.

## 4. Inject release ledger and complete facilitator case

| Exercise minute | Card | Source event UTC (fictional) | Decisions and frozen artifact |
|---:|---|---|---|
| 0–7 | **CK-00** | 08:40 | Owner, release authorization, effective-scope unknowns |
| 8–18 | **CK-01** | 09:00, detection 09:06 | Confirm exposure, preserve minimal public evidence, prepare containment |
| 19–29 | **CK-02** | 09:18 | Unfamiliar usage hypothesis and log requests |
| 30–40 | **CK-03** | 09:25 | Effective IAM/resource matrix and risk priorities |
| 41–51 | **CK-04** | 08:50–09:31, acquired 09:40 | Join events by time, resource, principal, result |
| 52–61 | **CK-05** | 09:44–09:49 | Preservation versus rapid disable tradeoff |
| 62–70 | **CK-06** | 10:03–10:07 | Revocation operation and independent verification |
| 71–80 | **CK-07** | 10:20 | Version comparison, authorized change assessment |
| 81–90 | **CK-08** | 11:02–11:12 | Short-lived identity, artifact and return gates |
| After final freeze only | **CK-09 (optional)** | 11:35 | New bounded receipt cannot change past decisions |

### CK-00 — Prepared baseline (minute 0; Govern, Identify, Protect)

**Fictional signed baseline, 08:40:** NTA's production project **prj-passenger-prod** contains a public-facing dashboard service **svc-public-api**, release settings **cfg-dashboard**, asset bucket **bucket-render-assets**, and dataset **dataset-journeys**. Stage and audit-vault projects are separate. The last fully approved release is **REL-88** referencing **ART-88** (approved artifact) and config **CFG-22**. The approved release chain is *reviewed source revision → trusted artifact identity → project-owner change approval → deployment operator receipt → independent service/config check*. Source and digest details are held in an approved internal manifest, not displayed as magic plaintext hashes.

A planning note says deploy-broker “should only publish dashboard code” but does **not** include evaluated IAM scope, group inheritance, role conditions, session derivatives or logging coverage. A desired noon release is not an RTO or a waiver of approval. **Decision:** Elena names authorized service impacts; Hana requests actual effective grants; Amina and Ravi freeze verified manifest references; Jonah confirms which audit sources and copies may legally be preserved. **Failing response:** assert deploy-broker can modify every project or that the dashboard is known safe from a job label.

### CK-01 — Public commit exposure (minute 8; Detect)

**Fictional 09:00:** Public commit **PUB-204** contains actual CRED-DPL-7 bytes, intentionally **withheld** here; at 09:06 scanner alert **SRC-06** identifies public exposure, but **does not copy** the value into the incident ticket. A later screenshot says a successor commit removed the value from current HEAD at 09:11; the original public history remains available at this time. No actor, token-expiry, exploit or source-clone count is established.

**Decision:** Priya declares **exposure confirmed**, opens case **NTA-IR-003**, seeks bounded evidence and immediate IAM consultation. Jonah requests source commit ID, first exposure time, source-control retention and read-only provider audit; no secret strings enter chat, tickets or exercise. Amina preserves relevant revision identities, stops further re-publication and plans protected source hygiene (without silently destroying investigative history). Elena approves a scoped release freeze; Ravi records availability cost. Hana prepares disablement through trusted administrator identity. **Contrast:** Removing a string from today's tip does not revoke it, delete all prior copies or prove it was never used.

### CK-02 — Unfamiliar identity use (minute 19; Detect and Respond)

**Fictional event 09:18:** A provider summary associates one API request after PUB-204 with **deploy-broker / CRED-DPL-7** from unfamiliar network label **NET-UNFAMILIAR**, but aggregates regions and provides no exact resource or API result. This shows a **source's assertion about credential use**; it does not yet identify the human, endpoint, resource effect, or any data payload. “Unfamiliar” is relative to current runbook knowledge, not an automatic malicious attribution.

**Decision:** Jonah requests the original event, identity issuance/delegation records, project/region and source coverage. Amina checks permitted local release history; Hana independently determines effective scope and revocation semantics; Priya records competing hypotheses: **H1** authorized automation not yet reconciled, **H2** unauthorized external token use, **H3** other delegated or copied identity activity. Do not assume equal probabilities or assert that one hypothesis is proven. Exposure warrants timely containment even if H1 later explains this particular event.

### CK-03 — Credential scope is not account-wide power (minute 30; Identify/Respond)

**Fictional IAM owner policy export `IAM-VER-6` at 09:25** associates CRED-DPL-7 with principal deploy-broker. This is **one evaluated policy snapshot**, and delegation and temporary derivatives have not yet been fully reconciled.

| Project and resource | Effective permission at snapshot | Explicit limit or unexamined boundary |
|---|---|---|
| prj-passenger-prod / svc-public-api | Read release state; update artifact reference | No direct data-export grant shown in this policy |
| prj-passenger-prod / cfg-dashboard | Read config metadata; update versioned release pointer | IAM administration not authorized here |
| prj-passenger-prod / bucket-render-assets | Read **bucket metadata** | Object-content reads and data-event logging are a separate question |
| prj-passenger-prod / dataset-journeys | No direct grant in this evaluated policy | Other identities, service behavior and paths unexamined |
| prj-analytics-stage | No grant in supplied snapshot | Inherited/delegated trust unresolved beyond this snapshot |
| prj-audit-vault | No grant; separate evidence collector | Do not assume all logging is complete |

**Decision:** Hana records **potential authority**, not realized action, by principal/project/resource/verb/policy version; flags incomplete delegation and lifetime. Elena and Mateo prioritize the two potentially mutable production resources, not a blanket shutdown. Priya requests observed use and state diffs for these exact targets. **Negative control:** A role name and a single policy snapshot never prove that no other cloud identity could access data.

### CK-04 — Raw activity records: distinguish request, result and effect (minute 41)

**Fictional export `MGMT-40` acquired 09:40** covers one account/region, **management-plane** events during **08:45–09:40 UTC**. **All operations below are invented labels, not real API names or executable calls.** This is the entire supplied tabletop dataset; no student executed queries to create it. *Principal* indicates a service identity, not a named human operator.

| Row | Event / ingestion UTC | Principal / credential reference | Project / resource | Fictional operation | Recorded response |
|---|---|---|---|---|---|
| **L01** | 08:50 / 08:51 | deploy-broker / CRED-DPL-7 | prj-passenger-prod / svc-public-api | ReadReleaseState | success; REL-88 pre-release check |
| **L02** | 09:18 / 09:22 | deploy-broker / CRED-DPL-7 | prj-passenger-prod / cfg-dashboard | ReadConfigMetadata | success; NET-UNFAMILIAR |
| **L03** | 09:21 / 09:28 | deploy-broker / CRED-DPL-7 | prj-passenger-prod / svc-public-api | SetArtifactReference | success API response; **resulting state not independently checked** |
| **L04** | 09:24 / 09:32 | deploy-broker / CRED-DPL-7 | prj-passenger-prod / bucket-render-assets | ReadBucketMetadata | success; object data not shown |
| **L05** | 09:27 / 09:31 | deploy-broker / CRED-DPL-7 | prj-passenger-prod / dataset-journeys | ReadDataset | **denied for that request** |
| **L06** | 09:31 / 09:39 | independent collector / not CRED-DPL-7 | prj-audit-vault / export-ledger | WriteAuditCopy | success response; acquisition receipt still needed |

**Coverage:** The supplied management-only source contains **no object-data event set**, no cross-region/all-account aggregation, no external runner/credential issuer history, no user identity behind a bearer principal, and no completeness guarantee for service-specific logs. Event time and ingestion time differ; do not backdate when a learner first saw this evidence. [AWS CloudTrail Event history documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) explains that that **real AWS interface** shows recent per-region **management** events, not data events. This scenario is deliberately *cloud-neutral*, not an AWS CloudTrail export.

**Practice checkpoint:** L01 is **before** 09:00 publication; L02–L05 are **after** publication and associate with the same principal/credential; L06 is another identity. L02/L04 are **metadata reads**, not object-data extraction; L03 is a successful response to an update *request* pending state verification; L05 is one **denied** dataset request, not account-wide prevention. A successful signed call does not prove exfiltration, malicious actor identity or broad resource changes. The team's **next** discriminator for L03 is an independent resource-version comparison **and** approved release manifest. Freeze this answer **before CK-07**.

### CK-05 — Preserve minimum audit, but do not delay revocation indefinitely (minute 52)

**Fictional 09:44–09:49:** Jonah's management-log export **request** is recorded as **REQ-44**, but a request is not a copy. The independent audit collector returns archive **AUD-CK-1** and scoped **capture receipt EXP-47** at 09:47, with account, region, source kind, collector identity and time. **Independent digest readback still pending**, and the data-plane coverage inquiry remains open. Hana's 09:49 IAM status says the compromised token is still active. The dashboard is still serving read-only users, and the deploy route can be frozen without stopping that read path.

**Tradeoff and decision:** Priya recommends preserving the bounded management snapshot **already available**, documenting missing hash/cross-scope/data logs, then promptly revoking the *specific exposed credential*. Hana authorizes exact principal/token target, operator, scope, check and rollback strategy. Elena approves service impact of the release freeze **separately**. Mateo prepares scoped authorized execution. Jonah continues preservation through an independent collector after disabling. **Negative control:** A log request is not a received immutable export; an archive receipt without independently verified readback is not full forensic completion.

**Conditional alternate:** If preservation cannot be accomplished quickly while suspicious activity may continue, an approved emergency response may revoke immediately and document the evidence-loss risk; “logs before rotation” is a sequencing preference **subject to incident safety and urgency**, not an excuse to keep a public credential valid indefinitely.

### CK-06 — Revoke and validate without ever replaying the exposed token (minute 62)

**Fictional 10:03–10:07 receipts:** Hana's scoped authorization **IAM-A09** names CRED-DPL-7 and Mateo as operator. Provider response **OP-1003** records an accepted disable/revoke operation at 10:03. Using a **separate authorized administrator identity**, Hana obtains **IAM-STATE-1006** at 10:06 showing CRED-DPL-7 disabled. A **pre-existing provider log** at 10:07, **L07**, records a rejected authentication attempt associated with that reference; **the team did not produce that attempt**. Elena's bounded read-only dashboard check still passes. No card proves whether derived sessions, alternate identities or cached access remained valid.

**Decision and worked receipt chain:** **proposed → IAM-approved → provider-reported applied → independently read back disabled** for the *one credential*. The old token is never re-used for an active test. Account for possible session derivatives based on real provider semantics and separately gathered logs. Do not count a single rejected request or a working dashboard as proof of full eradication, end-to-end safety or no prior data access. The business owner and IAM owner preserve separate acceptance roles.

**Conditional:** If independent IAM state is missing or contradictory, treat effectiveness as **pending**, escalate to authorized IAM personnel and investigate live dependencies without mass deletion of unrelated identities. Replacement must not be another hard-coded shared long-lived secret.

### CK-07 — Approved release versus independent resource state (minute 71)

**Fictional 10:20:** Signed comparison **CMP-20** includes (a) the **complete, frozen approved production release register** through 10:20; its last valid release remains **REL-88 → ART-88** and **no approval exists for 09:21**, and (b) two independent owner-authorized state snapshots agree **svc-public-api currently references ART-OTHER-89**, not ART-88. Artifact content, provenance and execution behavior for ART-OTHER-89 were not supplied. No other resource's complete state is supplied. This card is **released after CK-06** and cannot repair a CK-04 decision.

**What can now be said:** The **specific svc-public-api deployment reference** is out of alignment with approved release authority. This is a **documented unapproved reference state**, and L03 is a plausible related operation because it names the same principal, resource and write request. It still does not identify the real operator, establish whether ART-OTHER-89 was malicious, show a data export, prove that all projects changed or demonstrate any other service's final state. Treat correlation and source-time limits honestly.

**Choices:** Elena maintains deployment restrictions and service owner checks; Amina preserves an ART-OTHER-89 **metadata/reference snapshot without executing unknown code**; Jonah records the two readbacks and scope, requests service logs and data-event coverage; Priya updates the incident's *specific change* finding without human attribution; Isabel assesses any applicable privacy/legal obligations without alleging data theft. Mateo plans version-safe rollback from the trusted approved release only under separate authorization. A blind “repair” that overwrites unpreserved state can destroy forensic evidence.

### CK-08 — Trusted isolated candidate and short-lived deployment identity (minute 81)

**Fictional 11:02–11:12:** Amina/Ravi supply authorized, independent **source → approved manifest → ART-88** provenance references in packet **PKG-88-TRUSTED**. The classroom card describes a previously witnessed **isolated fixture** in which the artifact byte-reference/readback matches that manifest; **no literal digest or executable output is invented or reproduced here**. The isolated dashboard candidate passes two bounded tests: approved status-view read and route health check. A negative-control test in the **same isolated fixture** records that the limited test identity cannot mutate an unrelated staging resource. No production promotion, real-world application security assessment, full customer-data access inventory or all-service monitoring result is supplied.

**Identity recovery proposal:** Hana/Ravi replace the persistent deploy token with **short-lived, narrowly scoped workload identity** issued when a protected, authorized local release process needs it. Appropriate federation/role trust is restricted by *subject, audience, source context, project, action and expiry* where the provider supports those controls. Limit the deploy principal to approved service resources and require a separate reviewer for policy changes. Do **not** embed new secrets in source, deploy scripts, build artifacts, log samples or public incident records. No GitHub Actions are to be created or enabled in this repository: this is a fictional local release design respecting the project's deployment policy. Official provider background: [Google Cloud Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) and [AWS IAM temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

**Go/no-go:** Elena and Hana must approve target and identity scope independently; Amina/Ravi document trusted artifact and local release handoff; Mateo would execute only a permitted future production change, with independent resource readback, new telemetry window and rollback owner. **Canonical result is NO production acceptance yet.** Passing an isolated test does not retrospectively validate the unauthorized resource state or prove full recovery.

### CK-09 — Optional, clearly later extension only after freeze

**Fictional 11:35:** A facilitator may issue a **new** card saying a narrowly authorized production readback now reports ART-88 for **svc-public-api**, with owner-approved release references and a bounded smoke test. If released, that supports only the named service, reference and observed window; it does not prove every resource clean, all possible access routes closed, or customer data never accessed. **CK-09 is not part of the canonical evidence set for rounds 0–8**, and cannot be cited before its release.

## 5. Reproducible correlation and negative tests (paper only)

A second learner can reproduce the assessment using exactly CK-01, CK-03, CK-04, CK-06 and CK-07:

1. **Time:** publication 09:00; L01 08:50 **before**; L02–L05 after; L06 is a different identity; L07 is later after IAM disablement. Ingestion time is not first-use time.
2. **Principal:** L01–L05 associate deploy-broker/CRED-DPL-7. A service principal or request signature does **not** identify which human or workload originated the call.
3. **Scope:** Only two resources in CK-03 have the stated write capability; L02/L04 refer to metadata reads; L05 is a denied attempted dataset read; distinguish potential permission from observed invocation.
4. **Effect:** L03 success refers to a request. **Only CK-07** supplies an independent config readback plus complete approved release register supporting a specific **unapproved artifact-reference state**.
5. **Coverage:** CK-04 is **one account, one region, management-only**, and supplies no data-object events or cross-cloud history; therefore “no data read” is not a defensible negative conclusion.
6. **Revocation:** OP-1003 reports action, IAM-STATE-1006 independently shows disabled, L07 reports one rejected attempt. None proves all derived sessions invalidated or all other identities safe.
7. **Recovery:** CK-08 demonstrates an isolated candidate. It supplies no production acceptance receipt or incident impact closure.

| Claim under review | Supported evidence | Defensible limit |
|---|---|---|
| Token exposed in public revision | CK-01 | Exposure yes; unauthorised use not deducible from exposure alone |
| Token identity used post-publication | CK-02, CK-04 L02–L05 | Covered provider records, not human attribution |
| Dataset exfiltration established | **None**; L05 denies one request | Unknown without data-plane/access coverage |
| All project resources changed | **None** | One observed service reference differs from approved target |
| svc-public-api in unapproved state | CK-07 comparison and approved register | Specific version/reference at a bounded time; cause/intent still open |
| Old credential disabled | CK-06 IAM-state independent readback | Exact credential only; derived sessions untested |
| Production safe and recovered | **None** in canonical CK-08 | Isolated functional candidate only |

**Negative controls:** NC-1 a successful *metadata* read is not an object download; NC-2 a denied call is a result for **one** request, not all routes; NC-3 role label is not effective IAM scope; NC-4 a hash/digest match proves the **tested bytes** agree, not that software is benign or deployment approved; NC-5 disabling a parent credential may not erase previously issued credentials; NC-6 a “quiet” log view with missing data-plane events is **unknown**, not negative evidence; NC-7 a late card cannot fix an earlier unsupported decision.

**Reproduction contract:** This is a **manual join and decision-audit fixture**, not a claim that any cloud command, hash tool, secret scanner, API call or lab actually executed. No actual hash value, credential, tool output or production behavior is asserted. A facilitator must not invent missing entries to reward a preferred response.

## 6. Conditional branches, evidence versus consequences

Every possible branch is a hypothetical decision until an **additional labeled facilitator receipt** is issued. Do not confuse a proposal, classroom approval and actual deployed effect.

| Response branch | Authority and evidence prerequisites | Conditional consequence / uncertainty |
|---|---|---|
| Remove token from visible latest source only | Amina preserves revision metadata; source owner approves history changes where applicable | Exposure from historical public commit remains; token not revoked |
| Freeze new deployment of affected service | Elena accepts dashboard release impact; Ravi records change control | Bounded release stopped **only if operator/queue receipt exists** |
| Disable leaked credential promptly | Hana IAM approval, Mateo action receipt, independent IAM-state check; minimal log collection when feasible | CK-06 establishes disabled credential, **not** all active derived sessions |
| Wait indefinitely for perfect logs | No acceptable authority to ignore suspected ongoing use | Reject; urgency and evidence-loss tradeoff must be documented |
| Delete/overwrite changed production service immediately | Owner change gate, evidence preservation and rollback required | Blind edit risks losing state and disrupting service; reject absent gates |
| Replace with another permanent shared token | Would require strict storage, rotation and exception approval | Restores old risk pattern; prefer short-lived federated identity |
| Restore ART-88 in isolation | Reviewed source-manifest provenance, separate test environment and explicit negative test | CK-08 supports **isolated** fixture only |
| Promote approved artifact to production | Owner/IAM/release approvals, verified source, operator receipt, independent production probes and rollback | Not observed in canonical case; **pending** |
| Claim all data was safe | Requires data-event coverage and privacy/legal/owner assessment beyond supplied logs | Unsupported; preserve unknown status |

**Worked tradeoff:** CK-05 gives EXP-47 for a scoped archive but no independent hash readback yet. Hana need not wait indefinitely: approve a narrow disablement now, label forensic-copy verification pending, and continue independent evidence work afterwards. If a participant delays for a complete data-plane history, ask what continuing credential exposure costs.

**Worked chronology:** At CK-04, L03 indicates a successful update request but no independent state readback. A statement of “confirmed unauthorized deployment” then is premature. At CK-07 the separate, later owner-approved comparison supports a specific unapproved **reference state**; record that as a new finding and preserve the original CK-04 snapshot.

## 7. Evidence-first but time-bounded containment procedure

This is a **discussion checklist**, not an executable procedure for another person's cloud. In a real response, operators must validate account, scope, permissions, approvals, vendor semantics and recovery procedures.

1. Open the case with source ID and **no secret bytes**. Preserve commit/time/location metadata through an authorized source custodian. A public value should be treated as exposed even if latest HEAD no longer shows it.
2. Determine the exact credential principal, issuance and expiry, inherited/delegated IAM grants, identity project, and any temporary derivatives. A role name or single resource listing is not enough.
3. Use a separate, trusted security collector for **read-only** management, data-access, IAM, configuration and local release logs as available; label account/region, source, event/ingestion and retention windows. Preserve source/copy/derivative identities and acquisition receipts; do not assert completeness if coverage is unknown.
4. Document competing hypotheses with tests: legitimate operator or third-party use, user/service principal reuse, a change already approved elsewhere, an unknown deployment, data access through other identities. Do not anchor on “attacker” without disambiguation.
5. Preserve a minimal defensible snapshot **when it can be acquired promptly and safely**. If active exposure imposes urgent risk, approve immediate revocation and record which original evidence was not yet copied. Waiting for a flawless forensic package is not a safety condition.
6. IAM owner signs exact **credential reference** to disable, scope, operator, expected service loss, stop condition and independent verification. Operator executes through authorized channel only; no one attempts to authenticate using the compromised token.
7. Verify independently with a privileged but **different** IAM identity; review provider response, final credential state, any passive rejection observations and possible derivatives. Mark unobserved session lifetimes unknown.
8. Compare only covered audit requests with resource versions, signed release manifests and independent state readback. Prioritize explicit write-capable resources, while investigating data paths to the extent justified and logged.
9. Prepare new short-lived, least-privilege workload identity under trust/subject/audience/project conditions; keep bootstrap and authorization separate from source control and release artifacts. Validate expiry, denied unrelated operation and rollback in a permitted isolated fixture.
10. Require distinct service-owner, IAM, release operator, security and post-change reviewer receipts for production acceptance. Do not close legal/privacy impact on the basis of a quiet management-only log window.

**Primary provider cautions:** [AWS CloudTrail's event types](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html) distinguish management/data events and caution against treating event files as ordered stack traces. [Google Cloud federation audit guidance](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation) emphasizes provider logs, unique subject mapping and identity correlation. Both are **examples of provider-specific conditions**, not a claim that the invented records literally came from AWS or Google Cloud.

## 8. Least-privilege recovery and acceptance gates

Identity recovery, service restoration and possible data impact are **separate decisions**. A protected local broker can employ short-lived credentials issued for a specific workload/run from a reviewed trust policy, with least privilege, narrow project/resource scope, issuer/audience/subject constraints, expiry and authenticated operator context. Official references include [Google Cloud Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), [Google Cloud workload identity audit examples](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity) and [AWS temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Tokens of limited lifetime reduce persistence of a leak but **do not** substitute for robust trust conditions or authorization review.

| Gate | Required evidence | Independent owner / no-go criterion |
|---|---|---|
| **G1 credential containment** | IAM-A09, OP-1003 and IAM-STATE-1006, plus derivative-session assessment | Hana/Priya: disabled **old credential** only; unreviewed derivatives are open risk |
| **G2 IAM least privilege** | Verified effective grants per action/project, constrained trust subject/audience and short expiry | Hana: do not accept shared long-lived credential or account-wide scope |
| **G3 forensic preservation** | Source/trail identity, independent archive receipt, digest readback status, coverage/retention limitations | Jonah: missing evidence not silently passed |
| **G4 artifact provenance** | Approved source revision, trusted signed manifest, byte-equivalence check in permitted fixture, version control | Amina/Jonah: unsigned or unknown ART-OTHER-89 is not a safe promotion |
| **G5 isolated tests** | CK-08 approved status view, route health, negative unrelated-resource mutation check | Ravi/Elena: these are isolated tests with limited routes |
| **G6 production change authority** | Exact service/version, Elena's service approval, Hana's identity review, distinct operator/rollback | Mateo: CK-08 contains **no production execution** |
| **G7 production readback** | New post-change provider/resource and application receipts, telemetry coverage, independent acceptance | Elena/SOC: do not infer production readiness from isolated smoke tests |
| **G8 privacy and residual risk** | Bounded data-access investigation, explicit unknowns, Isabel's legal assessment and Evelyn's risk decision | Isabel/Evelyn: no claim that all customer data was untouched |

**End-of-canonical-case go/no-go:** The exposed credential is **disabled** under CK-06, one production reference **deviates** from the authoritative approved register under CK-07, and a trusted artifact **passes isolated checks** under CK-08. **Production promotion/acceptance remains unobserved**, possible derivative credentials require review and data impact is unresolved. A sound exercise can end with the service's deployment path restricted rather than manufacturing a restored state.

**Clean-byte caveat:** Hash equivalence shows equality for a chosen byte sequence; it cannot by itself prove that the author, source tree, authorization or target is trustworthy. A 30-minute window without logged anomalous actions is never a timeless proof of safety unless relevant sources, detection coverage and scope are documented.

## 9. Required artifacts, scoring and noncompensable stops

Participants submit six frozen artifacts. The observer scores the **artifact as originally submitted**, not an answer revised after future cards.

| Artifact | Minimum independent-review content |
|---|---|
| **A1 event/release ledger** | CK availability, event vs ingestion vs exercise clocks, observations/hypotheses, next discriminator |
| **A2 credential/permissions matrix** | Identity reference, IAM snapshot/version, real grants, conditional access, project/resource scope and unknown delegation |
| **A3 forensic correlation sheet** | L01–L07 classification, source/copy/derivative, management/data-plane coverage, hashes/readbacks pending, affected-resource links |
| **A4 containment envelope** | Project owner freeze, Hana approval, Mateo provider receipt, independent IAM state, active sessions/rollback/impact |
| **A5 change and recovery decision** | REL-88/ART-88, unapproved reference, isolated controls, short-lived identity, production gates and residual risk |
| **A6 communication and after-action sheet** | Approved versus unsent language, privacy uncertainty, named fixes, deadlines and negative-control retests |

**Original classroom rubric:** 10 criteria × 0–2 points = **0–20**. **0** means absent or contradicted; **1** means relevant but missing source, clock, owner, action status or limitation; **2** means reproducible and justified from evidence **available then**. Score only released injects. If the facilitator omits a necessary card, mark dependent criterion **not observed / facilitation defect**, not participant zero. Two observers independently cite A1–A6 excerpts and reconcile against frozen records. This is **not** an NIST certification or a test of any live system.

| Criterion | Two-point standard |
|---|---|
| **C1 exposure** | Public commit proves exposure, not all further effects |
| **C2 principal/scope** | Deploy identity and policy grants separated from role name, resource reach and delegation gaps |
| **C3 clocks** | Publication, event, ingestion, release and freeze times not conflated |
| **C4 log integrity** | REQ-44 vs EXP-47 vs independent digest readback; data-plane scope explicit |
| **C5 timely revocation** | Prompt, approved exact-token disablement; action/provider/independent readback separate |
| **C6 API/effect distinction** | Metadata reads, write request, denied call and missing data events correctly classified |
| **C7 change triage** | Only CK-07 supports bounded unapproved svc-public-api reference; actor/content unknown |
| **C8 restricted identity** | Protected short-lived scoped issuance, expiry and negative permission tests |
| **C9 recovery** | REL-88 provenance, isolated versus production checks, G1–G8/rollback explicit |
| **C10 communication/improvement** | Unsent bounded update; owner, deadline, falsifiable retest and review |

**Noncompensable safety failures:** printing/sharing actual secrets, using a leaked token to validate it, performing real cloud calls, destroying evidence without authority, enabling or running GitHub Actions, treating a classroom result as production proof or claiming legal data exposure without evidence. Stop the exercise, label the fault and record it separately from score. Classroom-only interpretation: **17–20** strong reasoning, **12–16** material gaps, **0–11** substantial rework. Scores do not equal independent human review.

## 10. Facilitator worked answers and contrastive exercises

Release the worked solution **after** the matching round is frozen. Alternate decisions can pass if evidence, scope, authority and independent verification are equally strong.

| Round | Worked reasoning | Incorrect alternative / facilitator challenge |
|---|---|---|
| CK-00 | Map authorized manifest, IAM-policy unknowns and owner/release gates | “Deploy principal owns account.” Which policy snapshot proves it? |
| CK-01 | Confirm exposure and preserve commit metadata without secret; plan urgent disable | “Removing HEAD string fixes it.” What about history and copies? |
| CK-02 | Mark unfamiliar **associated use**, request raw records and legitimate-run comparison | “Named adversary logged in.” How does a service identity identify a person? |
| CK-03 | Scope potential writes to named resources and record delegation unknown | “Every project compromised.” Where is effective scope or an observed change? |
| CK-04 | L01 before public commit; L02/L04 metadata; L03 write request with no state; L05 denied; L06 another identity | “API success proves exfiltration.” Which data access event/payload supports that? |
| CK-05 | Preserve bounded archive receipt, note pending hash/data coverage, approve prompt disable | “No revocation until all forensics complete.” Why tolerate ongoing exposure? |
| CK-06 | Record exact credential disabled by independent identity; examine possible derivatives | “All sessions invalid.” Where is expiry/session evidence? |
| CK-07 | One unapproved artifact reference with independent state; causality/actor/data unknown | “All resources mutated.” Which other state readbacks exist? |
| CK-08 | Isolated trusted candidate and short-lived role design; production gate remains pending | “Green isolated tests = restored prod.” Where are approval and live readback? |
| CK-09 optional | Treat any later receipt as **new bounded evidence**, never rewrite CK-07 or CK-08 | “Hindsight proves earlier decision correct.” When was the card released? |

**Worked independent exercise P-03 (paper only):** At CK-04, classify L01–L06 by pre/post exposure, principal, operation, recorded outcome, resource, one unsupported inference and the **next evidence to request**. Keep answer frozen before CK-05.

**Worked answer:** **L01** is pre-exposure recorded deployment-state read, not malicious by association; **L02** post-exposure same-principal config-metadata read, not data exfil; **L03** post-exposure same-principal successful update *request*, final state and approval still unverified; **L04** post-exposure bucket metadata read, not content object read; **L05** post-exposure denied dataset request, not a statement about all data paths; **L06** audit-vault operation by separate collector identity, not use of the leaked reference. The essential follow-up is independent source/release records, IAM grant/trust analysis, resource version, event coverage and authorized data-plane logs. A CK-04 answer citing CK-07 is a **timing defect** even if the later facts support the claim.

**Worked independent exercise P-03b:** Suppose no EXP-47 archive receipt arrives by CK-05 but the leaked credential remains active with plausible abuse. **Answer:** obtain valid emergency authority and disable promptly, document why preferred pre-revocation preservation was incomplete, preserve remaining source through a separate trusted collector and mark omitted periods unknown. An absent collection receipt proves neither absence of use nor absence of sources. Never reenact the exposed token.

**Scoring calibration:** A learner writes in A3, “The management audit shows no data downloads, therefore no customer data were taken.” Even if events were correctly enumerated, that conclusion **contradicts explicit logging limitations**. Reconcile C6 to **0** for that claim and record the missing data-plane query. The learner may submit a separate corrected statement at the next checkpoint, but the previous frozen claim stays visible.

## 11. Communications, debrief and measurable follow-ups

**Unsent sample message**, requiring review by Elena, Priya, Isabel, Evelyn and Dana before any distribution:

> “A deployment credential appeared in publicly available source history. The identified credential has been disabled; we are investigating recorded use and assessing affected deployment resources. One production service’s artifact reference differs from our approved release register. We have an isolated recovery candidate, but a production acceptance decision has not been recorded. The identity of the operator and whether any customer data was accessed remain unconfirmed. We will communicate further based on independently verified findings.”

This draft must **not** be represented as an approved, dispatched or acknowledged notice; all such statuses are separate. Isabel owns applicable legal/privacy assessment rather than treating any authenticated call as a breach declaration. Dana may report only reviewable scope and next update trigger, never "all safe" or "exfiltration confirmed."

In a 25-minute debrief, each team answers: **(a)** which claim arrived first and at what exercise minute; **(b)** which source was trusted incorrectly; **(c)** how the true IAM grants differed from a job name; **(d)** which audit windows and data events are still missing; **(e)** whether credential disablement had independent state readback; **(f)** what specific state was outside an approved release; **(g)** why a trusted digest and isolated success did not authorize production; and **(h)** which retest would falsify a claimed remediation.

| Improvement item | Fictional accountable owner and target after exercise | Measurable independent retest |
|---|---|---|
| **I-01 stop plaintext secrets before publication** | Amina + Hana; 21 days | Approved synthetic secret fixture rejected by pre-publication detector, with **no value stored**; reviewer verifies negative/positive coverage |
| **I-02 scoped temporary deployment identity** | Hana + Ravi; 35 days | Isolated issuance with strict subject, audience, project/action and TTL; denied mutation outside allowed service; protected local operator path |
| **I-03 provider audit readiness** | Jonah + Priya; 21 days | Archive and independently read back management and authorized data-event fixtures across defined regions/projects; log missing categories |
| **I-04 resource version/rollback gate** | Elena + Mateo + Amina; 30 days | In isolated fixture, unknown ART-OTHER-89 is refused; trusted ART-88 passes versioned manifest check and independent negative-control rollback |
| **I-05 impact communication drill** | Isabel + Dana + Evelyn; 14 days | Two distinct approved mock messages, one for limited unknown audit use and one for confirmed unapproved resource state, neither inventing data theft |

Deadlines are **fictional educational targets**, not NIST mandates or evidence of completed fixes. The **tabletop** finishes when A1–A6, observer scores, stop conditions and improvement owner records are submitted. The **fictional incident** can remain unresolved: data impact and operator attribution are intentionally unknown, and canonical production restoration has **not** occurred.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — incident response within CSF 2.0 and risk management.
2. [NIST CSWP 29 — Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — nonprescriptive Govern, Identify, Protect, Detect, Respond and Recover.
3. [AWS CloudTrail — Understanding CloudTrail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html) — event types, field semantics and logging limitations.
4. [AWS CloudTrail — Working with Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) — 90-day per-region management-event history; not a data-event view.
5. [Google Cloud IAM — Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) — alternatives to long-lived service-account keys and temporary access.
6. [Google Cloud IAM — Best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation) — scoped subject, trust and auditing across identity provider and cloud logs.
7. [Google Cloud IAM — Example logs for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/audit-logging/examples-workload-identity) — identity/audit field examples, delegation visibility and data-access configuration.
8. [AWS IAM — Temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) — short-lived role/federation credentials and expiry.

All event cards, identities, resource names, decision gates, scores, tables, tests and worked answers are original **fictional** educational material. References are linked and paraphrased, never copied wholesale or relicensed; the original repository content follows [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md) and its CC0 scope/third-party exceptions. No academic credential, cloud compliance certification, production safety finding or real incident is claimed.
