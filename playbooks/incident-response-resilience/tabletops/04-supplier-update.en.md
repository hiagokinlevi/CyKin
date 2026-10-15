# TableTop 04 — Compromised supplier update: signed delivery, uncertain build and controlled rollback

**Edition:** English · **Exercise ID:** TTX-SUP-04 · **Catalog ID:** `supplier-update` · **Editorial date:** 2026-10-15  
**Editorial state:** Original fictional defensive teaching scenario; independent technical and human review pending.  
**Audience:** Supplier liaison, product owner, endpoint IT, SOC/forensics, release/change management, service continuity, legal/privacy, communications, executive incident command and independent observers.  
**Format:** 15-minute briefing, 90-minute paper-only inject exercise and 25-minute debrief; facilitate in a room or locally without interacting with a real system.  
**Catalog relationship:** This expands [the existing fourth scenario in the ten-item catalog](../../../web/tabletop/scenarios.json), not an eleventh incident. The [playbook index](../README.md) links this supplementary exercise; it is not a replacement course manuscript, executable runbook or deployed site experience. See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Context, objectives and non-operational safety boundary

**Entirely fictitious case.** The people, organization, supplier, applications, host IDs, hashes-as-labels, certificates, logs, clocks, artifacts, installation counts, advisory updates, performance measurements and actions are invented teaching fixtures. They do **not** identify an actual security incident, real product, validated cryptographic material, live network address, patient/customer data or exploitable sample. There is no malware, usable credential, signature byte sequence, exploit command or real deployment procedure in this document. A classroom participant writes decisions and reads printed cards only. Never install, execute, quarantine, scan, contact, modify, roll back or publish to a production system as part of this lesson; organizations must use their separately approved response and release processes.

**Fictional organization:** **Oriole County Permit Services (OCPS)** handles residents' permit applications. Its 36 managed endpoints use the fictional **Northstar Workflow Bridge** application from fictional supplier **LumenField Software**. The software assists intake, document indexing and queued case transfer. Intake continuity matters: interrupting the bridge may delay permit submissions, while allowing a suspect update to continue can increase evidence and business risk. Neither scenario pressure justifies treating every endpoint as infected.

At 09:20 UTC, a signed version **5.4.2** has reached several managed endpoints. Some experience changed behavior after installation. At 10:05 UTC, a *preliminary* supplier alert warns of a **possible compromise of a build process** but cannot yet specify every affected build/version. A valid package signature attests to verification against a signing identity and particular bytes under the verifier's trust policy; it is **not a guarantee that source, build environment, generated artifact or runtime behavior was safe**. An installation receipt indicates a specified client state at its check time; it cannot itself prove that code ran maliciously.

**Keep five evidence grades separate:**

1. **Signed package verified:** the tested package bytes, identity and signature chain match a trusted record under known policy; this does **not** establish benign source or build.
2. **Installation confirmed:** version/package identity appears in a host-side inventory and independent installer or management receipt for that device; scheduling or download is not installation.
3. **Suspicious behavior observed:** a bounded, time-stamped change in telemetry; it is a correlation and a hypothesis to investigate, not by itself malware or exfiltration.
4. **Build assessed as affected:** an authoritative supplier or independent source can tie a specific version/digest/build window to an incident under investigation, with the *strength and limitations of that assessment* recorded; "suspect" is not "confirmed malicious."
5. **Malicious action proven:** a preserved execution/operation trace plus interpretation and authorization boundary supports a particular harmful or unauthorized operation at a particular host/time, after plausible alternatives and coverage limits are assessed. No such proof is given in the canonical classroom cards; **do not fabricate it**.

### Learning objectives

- **O1 — Govern and constrain:** recognize product ownership, supplier-response authority, rollout/change rights, service dependency, safe stop conditions and risk accountability.
- **O2 — Inventory rigor:** reconcile intended, downloaded, installed, running, removed and unobserved states by host/ring/time/version, preserving immutable snapshots and coverage.
- **O3 — Package trust and supply-chain provenance:** distinguish signature verification, file hash, approved manifest, build provenance, vendor notification and independent acceptance.
- **O4 — Evidence-based response:** preserve logs and installation artifacts safely; correlate version, process, network behavior and source timing; choose proportional containment with service owner.
- **O5 — Controlled recovery:** test a verified previous candidate, approve and exercise rollback with dependency/continuity gates, then independently check production state and monitoring if such later evidence exists.
- **O6 — Honest communication and improvement:** explain unknown affected versions, avoid claims of generalized compromise, record escalation and a falsifiable supplier/rollout review.

### NIST and supply-chain alignment — not an invented mandate

[NIST SP 800-61 Rev. 3 (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident response across the [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final): **Govern, Identify and Protect** support preparation and risk management; **Detect, Respond and Recover** address incident actions; improvement follows across the functions. The current framework does **not** prescribe this paper exercise's card schedule, names, scoring or automatic isolation. [NIST SP 800-161 Rev. 1, Update 1 (November 2024)](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) is the updated current C-SCRM publication; it supersedes the original May 2022 Rev. 1 publication and treats visibility into supplied products, their development/integration/deployment and acquisition risk as risk-management concerns. [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) provides secure software development practices, including protection of software and vulnerability response. Neither standard says that a signature alone proves a safe build or makes these classroom approvals legally binding.

| Teaching decision | CSF 2.0 emphasis | Evidence boundary |
|---|---|---|
| Know supplier owner, approved artifact, version inventory, staged rings and rollback candidate | Govern / Identify / Protect | Approved source and product map, not generic supplier reputation |
| Detect changed behavior and receive a preliminary supply-chain notice | Detect | Observation, source authenticity and confidence separately |
| Preserve records, stop further rollout, evaluate isolation versus service impact | Respond | Approval, execution and independent readback separately |
| Select verified older candidate and test dependencies in isolation before a phased return | Recover | Candidate test is not a production deployment receipt |
| Rehearse supplier verification, provenance, staged updates and negative controls | Identify / Govern | Follow-up owner, measurable retest and explicit unknowns |

## 2. Participants, teams and non-interchangeable authority

These are **fictional classroom delegations**. A participant may act out more than one team only if the written approvals remain from different authorized roles. No role has permission to alter a real endpoint or publish a build.

| Named role and team | May decide in the fictional exercise | Cannot approve or infer |
|---|---|---|
| **Dr. Mira Solano — LumenField Supplier Security Liaison** | Provide statements through a pre-registered supplier security contact, explain advisory scope and artifact provenance **with disclosed confidence** | Decide OCPS rollback, certify every customer endpoint safe, or convert a preliminary finding into confirmed malware |
| **Tobias Wren — OCPS Product and Service Owner** | Approve service-impact tolerance, critical intake acceptance criteria and staged production return after evidence | Declare endpoint maliciousness, independently change signing trust, or override security preservation |
| **Avery Kim — Endpoint IT Owner** | Establish device inventory, stop client targeting via approved change, propose proportionate endpoint actions, independently verify host-side state | Isolate caseworker fleets solely from package version without security/service review |
| **Safiya Diallo — SOC Incident Commander** | Open case, prioritize correlation and proportionate containment, set evidence/review questions and approve SOC scope | Identify attacker, assert all installs malicious or authorize an untested production rollback |
| **Maxime Laurent — Digital Forensics / Evidence Custodian** | Preserve original package manifests, source/derivative identities, installer, signing-verification and endpoint log records using permitted read-only channels | Run a suspect binary, fabricate a digest or treat a snapshot request as a completed acquisition |
| **Livia Sato — Product Quality and Artifact Verifier** | Verify independent package ID/manifest trust and dependency requirements; define isolated positive/negative tests | Treat valid signature as code-quality certification or accept supplier assertion without scope |
| **Hugo Martins — Change Control and Locally Authorized Release** | Approve a bounded rollout pause/rollback change envelope after required owners; record simulated operator/readback statuses and rollback plan | Bypass service authority, issue real deploy, use GitHub Actions or quietly promote an untested candidate |
| **Noelle Chen — Service Continuity Lead** | Set contingency intake routes, backlog limits, reconciliation and manual service recovery targets with Tobias | Declare endpoint clean or alter security constraints without SOC approval |
| **Iris Haddad — Legal and Privacy** | Set preservation and personal-data minimization, assess supplier obligations and notification questions when facts warrant | Assert a breach, data exfiltration or universal reporting deadline from timing coincidence |
| **Petra Novak — Communications** | Draft precise internal/supplier/customer status, track review, approval, dispatch and acknowledgment separately | Say all endpoints are compromised, supplier is malicious or service fully restored without evidence |
| **Rajesh Bose — Executive Incident Sponsor** | Resource allocation, crisis escalation and enterprise residual-risk decisions | Overrule a signed owner no-go, waive forensic scope or invent a vendor assurance |
| **Quentin Hale — Neutral Facilitator and Observer** | Release fixed cards, time/freeze artifacts, administer negative controls, independently score submitted decisions | Manufacture endpoint findings, announce later evidence early or substitute words for missing receipts |

**Separate authority gates:** The supplier speaks to the supplier's evidence; product owner accepts service outcomes; endpoint IT owns endpoint changes; SOC sets investigative/containment justification; independent custodian records evidence; change manager authorizes controlled execution only after relevant owner approval; quality lead tests dependencies; continuity lead validates fallback; legal reviews disclosure. Executive urgency cannot replace endpoint/service-specific approvals. A signed change request, an operator acknowledgement, independent effect verification and production acceptance are **different** records.

## 3. Exercise mechanics, clocks, inventories and safety stop

This is a **90-minute paper exercise** with a 15-minute briefing and 25-minute debrief. Initially the facilitator releases **SU-00 only**, and keeps later **SU-01 through SU-10** sealed. All card observations are synthetic and can be reproduced by another learner from their written tables. Observer Quentin logs three distinct clocks: **source event UTC**, **facilitator exercise-release minute**, and **decision freeze minute**. A later card containing an earlier event time cannot justify an earlier decision. Capture original evidence and working interpretation separately; do not silently edit a frozen record.

**Paper packet:** a signed-but-aging device inventory baseline, blank distribution/host receipt matrix, source-acquisition ledger, signature/provenance comparison, change-decision form, continuity/dependency card, rollback acceptance form, communications draft and 10-point scoring sheet. The supplier has a **pre-existing** security contact in contract record **VND-11**. Do not call numbers from unsolicited advisory content; verify the bulletin through the already established supplier channel.

**Decision record schema:** `decision ID | case-time UTC | exercise-release/freeze minute | available SU cards | observation | hypothesis & counterexample | exact hosts/ring/version | service dependency/cost | named approvals | proposed / approved / simulated executed / independently verified | preservation/rollback | next trigger`.

**Stop card:** A participant asks to install, execute, detonate, reverse-engineer or distribute suspect packages; run commands on live endpoints; mass isolate critical devices without impact assessment; access real supplier/customer data; publish a real IOC as fact; enable GitHub Actions; or assert maliciousness from a signature alone. Stop the tabletop, document the proposal and return to paper-only decision gates. Actual emergency response uses the relevant organization's procedures, not these classroom cards.

## 4. Progressive inject schedule and frozen decisions

| Exercise minutes | Card(s) and fictional source UTC | Primary test | Required frozen artifact |
|---:|---|---|---|
| 0–7 | **SU-00** (08:30) | Inventory and authority baseline | Exposure map and unknowns |
| 8–18 | **SU-01** (09:20) | Signed package and rollout states | Installation/targeting ledger |
| 19–29 | **SU-02** (09:35) | Behavioral change and alternative causes | Observations vs hypotheses |
| 30–41 | **SU-03** (10:05) | Preliminary, unverified notice and pause | Proportionate freeze decision |
| 42–52 | **SU-04** (10:18) | Authenticate supplier and scope | Contact receipt with limits |
| 53–63 | **SU-05** (10:32) and **SU-06** (10:48) | Provenance and forensic collection | Hash/signature/custody ledger |
| 64–73 | **SU-07** (11:06) | Investigate endpoint behaviors and coverage | Host impact/containment branches |
| 74–82 | **SU-08** (11:28) | Supplier build-window update and prior version | Rollback candidate decision |
| 83–90 | **SU-09** (12:00) and **SU-10** (12:40, released last) | Failed gate then corrected isolated candidate | NO-GO / conditional plan, frozen separately |

### Prebrief — SU-00: baseline and partial mapping (minute 0)

**Fictional baseline 08:30 UTC:** OCPS uses Northstar Workflow Bridge on **36 managed casework endpoints**, divided into four rollout partitions. The last fully approved general deployment is **5.4.1**, build reference **PKG-541-BASE**, from a prior approved release. This **does not** establish that it is a safe rollback candidate today; its hash, signing trust, dependency compatibility and supplier status still require validation. Update **5.4.2** is approved *for staged distribution* only: no exception authorizes overriding an emergency freeze or disabling logging. The intended rollout spans 18 first-target devices, then 12 queued devices; six devices are expressly excluded for operational reasons.

| Device cohort | Devices in asset inventory | Planned treatment | Evidence at SU-00 |
|---|---:|---|---|
| Canary **C01–C08** | 8 | First-target signed update | Planned only; no installation receipt yet |
| Wave **W01–W10** | 10 | First-target signed update | Planned only |
| Pending **P01–P12** | 12 | Later queue | Not yet targeted in approved plan |
| Excluded **X01–X06** | 6 | Stay on 5.4.1 pending compatibility | Planned exclusion, not proof of current host state |
| **Total** | **36** | **18 first-target + 12 pending + 6 excluded** | Host evidence still to come |

Tobias identifies **case intake**, **attachment indexing**, **case-to-queue reconciliation** and **manual intake fallback** as affected services. Noelle says the fallback is written but last supervised drill was months ago; this is a readiness gap, not proof of a live outage. The 12:00 team meeting is not an approved RTO. Safiya opens provisional response when evidence arrives. **Prebrief action:** name host owner, supplier pre-registered contact, rollout approval, source of truth for installed state and safe continuity options.

### Round 1 — SU-01: signed update and incomplete installation count (minutes 8–18)

**Fictional 09:20 UTC update-controller snapshot:** Version **5.4.2**, package reference **PKG-542-S**, appears with a **valid signature verification result** from the previously trusted vendor signing identity **V-SIGN-A**, and the package identifier matches the local approved rollout catalog. The signed artifact was distributed through the regular channel. **This is a bounded verification of the tested package identity and bytes, not a proof of harmless behavior or clean upstream build inputs.**

Independent host inventory and installer reports show **C01–C08 (8)** and **W01–W07 (7)** on 5.4.2: **15 confirmed installations**. The controller lists **W08–W10 (3)** as *targeted with no successful host receipt*, not confirmed installed and not known uninstalled. **P01–P12 (12)** remain queued with no dispatch receipt; **X01–X06 (6)** have current 5.4.1 host snapshots, but are only a sample of the total fleet at this checkpoint. Counts reconcile: **8 + 7 + 3 + 12 + 6 = 36**; **15 confirmed / 3 targeted-unknown / 12 queued / 6 excluded-current**.

**Decision:** Avery freezes a versioned SU-01 inventory and avoids saying “18 infected” or “only 15 affected.” Hugo can *propose* stopping future delivery as a precaution, but must distinguish a queued job from a host install and verify that the change is approved and applied. Livia requests signed package manifest, certificate chain/validity context, hash verification method and upstream build provenance. Maxime preserves host-side installer and controller logs using separate source/collection IDs. **Negative control:** 5.4.2 present on a device is **installation**, not confirmed malicious action.

### Round 2 — SU-02: behavioral anomaly with a counterexample (minutes 19–29)

**Fictional 09:35 UTC SOC telemetry, scoped to sampled managed endpoints:** On **C03** after install, an application background service runs an additional indexing job at 09:27, not seen in the previous local sample. On **W04**, outbound connection *count* rises from **8 to 24** events during a same-length sample window; no payload or recipient classification is supplied. A **5.4.1 endpoint X02** also shows a network-count rise during its office-hour window. The sensors have no memory inspection or complete fleet coverage. The software change log mentions a planned indexing-performance enhancement, but its exact runtime mapping is not yet verified.

**Observation:** new job on one 5.4.2 sample, elevated connections on another, and a **similar non-exclusive signal on X02**. **Hypotheses:** H1 expected authorized release behavior; H2 unrelated business workload/measurement effect; H3 potentially harmful behavior in a supplier build; H4 local endpoint cause unrelated to the update. **Discriminator requests:** compare sampled hosts under the same clock and baseline, package/build provenance, allowed destinations, owner-approved process inventory and evidence of actual unauthorized operations. An increase in count alone is not data exfiltration.

**Decision:** Safiya scopes a fact-finding case and proposes increased monitoring; Avery prepares a bounded hold on the update channel rather than automatically isolating all 36 endpoints. Tobias/Noelle assess the business cost of removing indexing functions from active casework. Maxime captures time-window and telemetry-source limitations before any intrusive response. **Incorrect shortcut:** “Valid signature, so safe” **or** “network spike, so all hosts compromised.”

### Round 3 — SU-03: preliminary notice, not an affected-version list (minutes 30–41)

**Fictional 10:05 UTC:** A message bearing supplier branding says its build integrity team is investigating a **possible compromise in a build environment**. The bulletin is explicitly **preliminary**, states that the vendor is investigating release provenance, and **does not identify the full affected-version range, malicious component, confirmed intrusion time or all deployment populations**. Its included URL/telephone number have not yet been verified against contract contact **VND-11**. A generic customer forum repeats the claim; neither forum nor display branding authenticates the advisory.

**Decision:** Hugo, with Tobias's service-impact approval and Safiya's case rationale, records a **new delivery pause proposal** for the 5.4.2 pipeline; Avery verifies the controller-side pause and the status of client retries instead of claiming a freeze from the ticket alone. The default **is no further rollout** pending authenticated supplier clarification. Maxime preserves the original notice/transport metadata without using unknown attachment/link content; Iris evaluates supplier contract preservation. Noelle prepares manual casework continuity. The response should be precautionary yet bounded, not an unsupported finding that every installed package is malicious.

**Conditional branch:** An active fleetwide containment command may stop business-critical intake or obscure forensic state. Absent observed harmful activity and owner/safety approvals, do **not** mass-disconnect endpoints merely because a preliminary advisory arrived. If later credible signs of active harm emerge, evaluate targeted isolation with SOC justification, endpoint owner execution, service risk and verification.

### Round 4 — SU-04: authenticate supplier via an existing channel (minutes 42–52)

**Fictional 10:18 UTC:** Supplier contract **VND-11**, signed well before SU-03, supplies a dedicated security-response contact for **Dr. Mira Solano**. OCPS procurement (represented by Tobias's authorized liaison) places a *classroom callback* using that **pre-existing contact**, verifies the counterpart under the contract protocol and records receipt **CALL-11**. Mira confirms LumenField issued the preliminary warning and is investigating possible build-system compromise. Mira **cannot yet say whether 5.4.2 is affected**, identify a malicious payload, certify that 5.4.1 is clean or enumerate every affected release. She requests package references and deployment counts through the trusted supplier-support channel, without secret or customer data.

**Decision:** Safiya raises confidence in the **authenticity of the preliminary notice**, not in maliciousness of installed software. Avery reports 15 confirmed installs, 3 targeted-unknown and 12 queued using their exact status labels; Livia supplies symbolic package identity and verification methods, not raw executables. Iris maintains contract/evidence handling. Petra drafts an internal notice that status remains uncertain. **Wrong inference:** “Supplier callback verified the advisory, therefore 5.4.2 is confirmed compromised.” **Missing:** build/digest-specific evidence and an independent effect analysis.

### Round 5 — SU-05 and SU-06: signature, provenance and evidence source are separate (minutes 53–63)

**SU-05, fictional 10:32 UTC release evidence:** Livia obtains an internally archived, approved vendor manifest **MAN-542** for version 5.4.2 and an earlier manifest **MAN-541** for 5.4.1 via the existing supplier channel. The **tested bytes** of local archived package PKG-542-S agree with the symbolic digest reference **D-542-A**; its signature validates under V-SIGN-A with the documented trust and timestamp policy. The earlier **PKG-541-BASE** has independent archived digest label **D-541-V**, a distinct trusted prior signature and pre-warning release provenance. **No actual hash bytes or sample are printed or computed in this tabletop.** The supplier's **build-input and build-run integrity** for PKG-542-S remains unverified. Successful signature verification means the package was signed according to the configured signer/trust policy; it does **not** establish the signer only signed benign output, nor whether the build environment was clean.

**SU-06, fictional 10:48 UTC evidence preservation:** Maxime's custodian ledger records original source references for the downloaded package, signing-verification report, controller deployment history and sampled endpoint telemetry. There is a **read-only collection request COL-46** for C03/W04/W08; by 10:48, **C03/W04 acquisition receipt ACQ-48** identifies source, collector, timestamps, stored copy and a completed **independent copy readback against a separately recorded digest reference**. W08 is **request only**, without source export or host receipt; W08's installed state remains unknown. Endpoint archive coverage beyond these sources is unproven. The investigator did **not** execute or detonate the suspect package.

**Decision:** Preserve **original / acquired copy / derivative** identities. Note that hash equality speaks to **the specific acquired bytes** and chain-of-custody handling, not to benign code. Livia records build provenance **unknown**, despite signature validity; Maxime requests artifact-by-build evidence from vendor and safely scoped behavior/installer logs, and records what was not collected. Hugo verifies the new rollout pause with **controller and selected endpoint retry readbacks**, without claiming that targets not yet observed are safe. **Negative control:** A matching digest does not demonstrate a trusted source tree or malware absence.

### Round 6 — SU-07: bounded host effects and proportionate isolation (minutes 64–73)

**Fictional 11:06 UTC comparison:** The permitted investigation receives updated host-side reports. **C03** shows an index task introduced by the updated application, but the corresponding approved feature list is incomplete. **W04** shows additional network connections to **service-label CACHE-ALPHA**, whose owner has not been confirmed; no data transfer contents are supplied. **X02 (5.4.1)** has similarly elevated counts on a separate office-hour path, supporting an ordinary-load alternative. **W08** returns only a controller "targeted" status with **no client acknowledgement**. No provided event establishes credential theft, persistence outside approved application behavior, code execution from an unauthorized file, or data exfiltration. Sensor scope is limited to these selected hosts.

**Decisions by role:**

- Safiya: record **suspicious-but-unattributed behavior** on C03/W04 with falsifiable hypotheses, not confirmed malicious execution.
- Avery: consider a **limited containment** of an endpoint only when a defined harmful behavior, high-confidence containment rationale or direct risk to data/service appears; prepare host owner, preservation, staff workflow alternative, execution and verification.
- Tobias and Noelle: compare service impact of endpoint isolation against the risk of an unverified supplier update; protect active intake through an approved substitute.
- Maxime: preserve current affected-host state and permitted logs before disruptive change when safe; a source capture is not a host isolation receipt.
- Hugo: keep future rollout stopped while investigating targeted client acknowledgements and version inventory.

**Conditional alternatives:** A1 (broad fleet isolation) has severe continuity and evidence risk without demonstrated fleetwide harmful effects; reject absent new high-confidence findings and named approvals. A2 (no action because signature passes) ignores build and provenance uncertainty; reject. A3 (pause distribution, investigate named hosts, prepare narrowly approved isolation triggered by evidence) is defensible. None of these branches reports a real action in the paper case.

### Round 7 — SU-08: supplier version scope improves, maliciousness still unproved (minutes 74–82)

**Fictional 11:28 UTC supplier follow-up via VND-11:** Mira provides a signed, versioned advisory **ADV-2**. Supplier investigation identifies an **unresolved build-integrity anomaly** in a particular build window that includes the provenance record for **5.4.2 / D-542-A**; it lists this exact digest as **suspect / under investigation**. It does **not** declare the artifact malicious or establish an attacker-controlled action. The same notice states that prior build **5.4.1 / D-541-V** was produced before the suspect window and is **not included in the currently identified investigation set**. This is useful bounded information, **not** a proof that every copy of 5.4.1 is risk-free; check signed provenance, dependencies and tested behavior.

**Decision:** Product owner and release lead consider a **versioned 5.4.1 rollback candidate**, but only after confirming exact trusted digest, signer identity, application settings and data/queue schema compatibility. A new owner-approved rollback plan must preserve casework data and evidence, have individual ring/host targeting, rollback of rollback, independent acceptance and a service continuity fallback. Livia demands a negative dependency test; Noelle identifies the minimum safe case intake path. Iris evaluates whether a reportable data impact exists (none proved), and Petra drafts a fact-limited operational message. **No production rollback is authorized just because vendor says 5.4.1 predates a window.**

### Round 8 — SU-09 and SU-10: isolated rollback fails, then passes narrower tests (minutes 83–90)

**SU-09, fictional 12:00 UTC isolated test card, release at exercise minute 83:** A **separately marked classroom fixture**, not a run on OCPS production, tests archived **PKG-541-BASE / D-541-V** in an isolated imitation of the permit workflow. The version is linked to the approved prior manifest, but **queued intake record type Q-4 uses a field introduced with 5.4.2**. The isolated 5.4.1 candidate can open case cards and display their status, but the Q-4 ingest/reconciliation test fails: it **would lose the documented association in this fixture** unless a compatible, independently approved adapter or migration strategy is tested. **Decision freeze at minute 85:** **NO-GO** for production rollback; a good signature and two green tests cannot override a failed business data-integrity gate. Preserve failure state and isolate candidate.

**SU-10, fictional 12:40 UTC result released at exercise minute 87 only after SU-09 is frozen:** A different, explicitly **versioned isolated candidate**, **RB-541-B**, adds a separately reviewed compatibility adapter **ADP-4B** without using the suspect build as its source. A bounded independent test reports (a) manifest/hash and trust readback for the 5.4.1 package, (b) case open and update, (c) Q-4 queue/record identity reconciliation passes in the specific synthetic fixture, (d) rejected unapproved plugin state in a negative test, and (e) a scoped monitoring interval without recurrence of the C03 index anomaly **in that isolated fixture**. These results do **not** show production rollback occurred, that all endpoint dependencies were tested, that 5.4.2 is malicious, that every host is clean, or that privacy impact is zero.

**Decision:** Livia and Noelle approve the **isolated candidate only**; Tobias evaluates the production service and acceptance plan; Hugo drafts a new **staged, separately approved** change with sign-offs, limited canary ring, data safety checks, independent version readback and rollback stop conditions. Avery is the hypothetical endpoint operator. Safiya requires investigation of anomalous hosts and bounded monitoring regardless of release choice. **Canonical close: rollout paused; suspicious update population assessed with uncertainty; 5.4.1/adapter isolated candidate passes named tests; production cutover and complete security closure remain pending.**

### Optional continuation — not a supplied production outcome

If a subsequent exercise needs a success or failure branch, create a **new** numbered card with time, producer and source for a small approved canary result and a separate production monitoring/readback record. Do not retrospectively rewrite SU-09 or SU-10. This optional continuation is **not** part of the canonical outcome and is not counted as observed here.

## 5. Worked host/version calculation and independent negative controls

A student can reproduce the core case without running a single command:

1. Start with **36 inventory endpoints** at SU-00: C group 8 + W group 10 + P group 12 + X group 6 = 36.
2. At SU-01, count **15 installed** (C01–C08 + W01–W07), **3 targeted/no host receipt** (W08–W10), **12 queued/not dispatched by the recorded source** (P01–P12), **6 current older version** (X01–X06). **18 targeted is not 18 installed.**
3. Assign **version and package identity** from source and independent host confirmation. A controller's successful dispatch or cached download is not a device-side install receipt. “Pending” may mean not queried or no receipt; do not silently convert it into confirmed absence.
4. For C03/W04, compare behavior **before and after**, with clock alignment and coverage. X02 demonstrates network-count elevation can occur on an older version, so correlation is not exclusive proof.
5. SU-05 verifies signature/hash for specific archived bytes. It cannot certify supplier build inputs. SU-08 attaches *suspected build window* to a specific digest **after** the earlier decisions; do not cite SU-08 to justify a minute-29 malware verdict.
6. SU-09 has a **failed required Q-4 dependency check**. SU-10 is **a later candidate** with a narrower isolated test pass. Never treat that as retroactive validity for SU-09 or production state.

| Claim | Supplied proof | Defensible conclusion |
|---|---|---|
| Package signed by trusted supplier identity | SU-01/SU-05 limited signature verification | Signature-valid tested bytes under known trust policy; **not** safe build guarantee |
| 5.4.2 installed on the whole first wave | Only 15 current host receipts | 15 installed; three first-wave targets lack host evidence |
| Endpoint behavior changed | SU-02 and SU-07 sampled telemetry | Suspicious observations with competing explanations and incomplete sensors |
| All installed hosts ran malicious code | **None** | No proof of malicious code or action on any supplied host |
| 5.4.2 is in supplier's suspected build set | SU-08 authenticated version/digest-specific advisory | Suspect/under investigation for D-542-A, **not** a confirmed malicious payload |
| Data were exfiltrated | **None** | No content, destination ownership, capture or full data log; unknown |
| Previous version is suitable for production now | SU-09 fails, SU-10 isolated later passes | Later test candidate only; production change, compatibility scope and monitoring still gated |
| Rollout was successfully stopped on all 36 hosts | Only proposed/partially scoped controller/readback | Source/target-specific pause status; all-host denial not supplied |

**Mandatory negative controls:** NC-1 signature-valid package could still originate in a compromised build pipeline. NC-2 downloaded/targeted is not installed. NC-3 higher network count also observed on 5.4.1, reducing specificity. NC-4 an older version can be operationally **unsafe** if schema changes make rollback inconsistent. NC-5 a verified digest proves tested-byte identity, not supplier process trust. NC-6 no unusual event in an uninstrumented endpoint is **unknown**, not clean. NC-7 authenticated advisory is not a confirmed affected-version list until the source says so. NC-8 a late isolated test does not validate a prior unsafe production release.

**Independent practice IP-04 (paper only):** Create a six-row evidence matrix for (signed, installed, suspicious behavior, vendor-suspect digest, proved unauthorized action, production recovery) using SU-01, SU-02, SU-05, SU-08 and SU-10. Freeze the matrix at minute 63 and again at minute 90 with `yes / no / unknown`, supporting card and missing proof. The [facilitator worked answer](#10-facilitator-worked-answers-and-scoring-calibration) supplies the two checkpoints. An educator may use these fixtures for discussion, not as a live forensic or anti-malware test.

## 6. Conditional response branches and proportionality

No effect is claimed merely because a participant chooses a branch. A future simulated effect needs its own **action receipt** and independent readback, after the relevant approvals and card release.

| Proposed option | Who could authorize and with what evidence | Conditional outcome and reason to refuse |
|---|---|---|
| **Pause 5.4.2 rollout** | Hugo change approval + Tobias impact acceptance + Avery controller execution/readback | Prevents new targeted updates **only to covered rings/clients**; retries and offline devices remain open |
| **Preserve original packages/telemetry** | Maxime evidence authority, service owner constraints for intrusive acquisition, valid collection/readback receipts | Source and acquired copy separate; safe evidence collection does not prove package benign |
| **Continue full rollout because signature is valid** | No approved rationale from supplied facts | Reject: valid signature does not resolve build compromise hypothesis |
| **Isolate all 36 endpoints** | Would require specific incident evidence, endpoint ownership, service/continuity impact approval and proportionate scope | Not justified solely by preliminary notice or limited anomalies; harms intake/evidence |
| **Isolate C03/W04 only if escalation threshold met** | Safiya evidence-based recommendation, Avery implementation, Tobias/Noelle impact and fallback review | Report as **proposed** until independent action/effect receipts; preserve state if safe |
| **Wait indefinitely for complete vendor attribution** | No acceptable reason to resume suspect distribution while evidence matures | Maintain bounded update freeze and review cadence; do not stall safe protective action |
| **Roll back to 5.4.1 immediately** | Requires verified digest/provenance, service-owner approved compatibility and business tests | SU-09 shows Q-4 identity failure → **NO-GO** |
| **Stage validated RB-541-B return** | Livia test, Noelle continuity, Tobias service approval, Hugo versioned change, Avery operator and Safiya monitor | SU-10 isolated candidate permits consideration, **not** production acceptance or fleet restoration |
| **Claim no data exposure after quiet sampled telemetry** | Would require complete relevant logging/collection and legal review, not supplied | Unsupported; preserve uncertainty and document next review |

**Competing risk reasoning:** A strong responder can pause distribution without disconnecting active workflows, while investigating C03/W04 more closely. If a new independently verified harmful action threatens residents' records, Safiya could propose narrow host isolation with owner-approved continuity, but that **new fact** is not in SU-00–SU-10. Conversely a third-party signature issue alone does not justify manufacturing a malware classification.

## 7. Forensic preservation and supplier authenticity contract

This is a conceptual **evidence and governance checklist**, not instructions to execute software or probe systems. An authorized real responder must check applicable tool behavior, device owner policy, legal permission and business safety.

1. **Create a versioned case record:** record how the notice was received, published time versus internal ingestion, exact supplier advisory revision, contact provenance and unverified portions. Do not send data to untrusted URLs or forum contacts.
2. **Authenticate supplier communications:** use **VND-11** existing vendor contact. Record call attempt, answered/identity confirmed, actual statement, supplier case ID, scope and next promised update as **separate** events.
3. **Preserve package identity without running it:** request original artifact reference, authoritative manifest, signer/chain/trust policy, signing time context, package hash and build attestation if available. Capture **reference labels**, not executable contents in this exercise.
4. **Distinguish source, acquisition and analysis derivative:** preserve immutable source metadata and permitted read-only host/controller copy with collector, times, hash/readback outcomes and the limits of the acquisition. A requested collection is not a verified copy.
5. **Protect endpoint evidence:** preserve installer receipts, package state, process and network event metadata, relevant source clock offsets and log retention windows before disruptive containment when safe and time allows. Never delay urgent safety action indefinitely for a perfect copy.
6. **Inventory actual installation:** record host/ring/product version, artifact digest reference, target time, download/installer/management receipt, running process state, sensor coverage, owner and next poll. Offline or missing host evidence remains unknown.
7. **Triage behavior, not reputation alone:** compare observed actions against documented expected change, independent baseline/control host, resource access and authorization; separate code/execution proof, suspicious signal and data-impact interpretation.
8. **Pause and scope containment:** require business service impact and security rationale for narrow host or fleet action. Record approved, simulated-executed, independently checked and rollback-ready statuses separately.
9. **Preserve incompatible rollback evidence:** prior signed artifact, supported data schema, queued work, forward/backward conversion limits, fallback method, configuration, independent acceptance and legal retention.
10. **Close only supported claims:** a signed package, a host update event, an authenticated supplier warning and a suspicious process are **different** provenance/effect levels. Record open cases and accountable follow-up.

**Rights and data restraint:** Use fabricated filenames, fictional host IDs and symbolic hash references; no client permit records, access tokens, malicious payloads, copied vendor code or private supplier incident notices are needed. Real vendor statements may carry contractual confidentiality; a classroom adaptation must not assert permission to reproduce them.

## 8. Recovery design: prior verified version, dependencies and acceptance

A recovery candidate is not accepted merely because its signature matches an earlier manifest. Define **version-specific** rollback semantics: whether forward data schema Q-4 can be processed by 5.4.1; whether database migration was reversible; queue replay/duplication controls; client/server compatibility; allowed config/feature flags; emergency failure mode; backup/rollback restoration points; monitoring coverage; and whether the supplier's prior build falls outside its *currently known* investigation scope. Livia and Noelle must substantiate isolated checks; Tobias accepts business service functionality, and Hugo cannot execute until change authorization is complete.

| Gate | Evidence the second reviewer must see | Responsible owner and NO-GO condition |
|---|---|---|
| **G1 baseline/coverage** | Total 36 reconciled across confirmed installs, targets-unknown, pending and excluded with timestamped host evidence | Avery: do not pretend 18 dispatched means 18 installed |
| **G2 supplier provenance** | VND-11 verified contact, ADV-2 revision, build window/digest identity and explicit uncertainty | Mira + Livia: an emailed logo is not authentication or proof of malware |
| **G3 package validation** | Source identity, signer/trust policy, artifact reference and hash readback tied to exact candidate and source | Livia + Maxime: signed bytes alone do not pass the build-integrity question |
| **G4 preservation and security** | Source/copied/derivative evidence, telemetry scopes, open behaviors, proportionate containment receipts | Safiya + Maxime: missing logs/host receipts not presumed clean |
| **G5 schema/queue safety** | Q-4 backward compatibility, permitted adapter identity, deduplication/record association and negative test | Noelle + Livia: **SU-09 fails → hard NO-GO** |
| **G6 isolated candidate** | SU-10 PKG-541-BASE/ADP-4B provenance and named positive/negative tests, isolation boundary | Livia + Tobias: isolated result does not prove full fleet |
| **G7 production change permission** | Exact cohort, package/adapter/config, release freeze exception, owner and endpoint approval, named operator and rollback | Tobias + Hugo + Avery: **not supplied** |
| **G8 production independent checks** | Host-side installed version/hash, critical intake workflow, case/queue count and identity readback, defined monitor window | Noelle + SOC: **not supplied** |
| **G9 residual/legal communications** | Open supplier investigation and exposure questions, truthful signed status and next update | Iris + Petra + Rajesh: no generalized “all clear” |

**Canonical gate verdict at minute 90:** G1 can be reported for the supplied cohorts with three first-wave unknowns; G2 supplier bulletin is authenticated **and still preliminary**; G3 archived bytes match intended signatures; G4 remains partly open; G5 failed for the first 5.4.1 attempt, G6 passed for a **later isolated variant**, while G7/G8 lack production receipts. Therefore **production return remains pending**. No rollout-wide malicious impact, data theft, or clean fleet can be claimed.

**Independent verification is a separate event:** An operator saying “rollback requested” or a change ticket approved cannot replace host-side version/hash readback or a functional business test. A non-recurring suspicious event in a short isolated observation interval does not prove eradication in production.

## 9. Required artifacts and evaluation rubric

Collect exactly **A1–A6** as frozen original classroom records; the learner should be able to complete every required inference from the printed SU cards without internet access, credentials or executing a build.

| Artifact | Expected substantive evidence | Evidence question |
|---|---|---|
| **A1 chronology/release ledger** | SU event UTC, release minute, decision freeze, source/quality, current hypotheses | Could an observer detect hindsight? |
| **A2 version/installation matrix** | 36 endpoints by ring, dispatched/targeted, host installed/version, digest, unknown status | Which 3 devices lack actual install receipts? |
| **A3 package and forensic provenance** | Signer trust, manifest, symbolic digest, source/acquired/derivative IDs, acquisition/hash-readback receipts, gaps | Does a valid signature certify upstream build safety? |
| **A4 containment/change record** | Precautionary rollout pause scope/readback, isolation alternatives/cost, owner approvals, independent verification | Was action actually done or only proposed? |
| **A5 rollback/acceptance sheet** | SU-09 Q-4 fail, later SU-10 ADP-4B pass, exact candidate, G1–G9, owner/production/monitor statuses | What would prove safe production restoration? |
| **A6 messages/after-action** | Draft/review/approved/sent labels, open supplier questions, owner, due date, measured negative-control drill | Does any statement exceed its evidence? |

**Original 10-criterion classroom rubric:** Score **0** if absent/contradicted, **1** if present but missing relevant evidence, time, authority or scope, **2** if demonstrably reproducible and properly bounded, for **0–20 total**. This is an educational scoring scheme, **not** a NIST test certification. Two independent observers cite exact SU cards and frozen artifacts before reconciling a disagreement. If a required card was never released due to facilitator error, mark that criterion **not observed**, not a participant zero.

| Criterion | Full 2-point standard |
|---|---|
| **C1 baseline and authority** | Named supplier/product/endpoint/SOC/change/continuity owner, applicable gates, accurate timing |
| **C2 installation state** | 8+7+3+12+6=36 accounted, targeted vs installed vs queued vs excluded distinguished |
| **C3 signature and provenance** | Trust/digest/signed package bounded; upstream build quality remains unknown |
| **C4 preliminary supplier contact** | Authentic VND-11 callback, advice confidence/version uncertainty, no maliciousness leap |
| **C5 evidence discipline** | Separate original/export/derivative, ACQ-48 readback, W08 missing receipt, clocks |
| **C6 behavioral reasoning** | C03/W04 and X02 counterexample, sensor limits, no blanket code/exfil conclusions |
| **C7 controlled pause/isolation** | Change pause readback, service impact and proportionate host decision separated |
| **C8 rollback dependency** | SU-09 hard failure Q-4 prohibits production rollback; no green-lights averaging |
| **C9 later candidate vs production** | SU-10 isolated pass not retrospective; G7/G8 production signatures and monitor checks pending |
| **C10 communication/debrief** | Scope-limited messages, owner/timeline/falsifiable supplier and technical improvements |

**Noncompensable safety/process stop:** a live execution or detonation of a suspect package; destructive endpoint isolation without authority or continuity review; shipment of an untested downgrade after SU-09 failure; invented malware/exfil attribution; real secrets or private customer records; GitHub Actions/deployment in this exercise. Stop and record the issue even when paper score is high. Suggested classroom interpretation: **17–20** well-evidenced reasoning, **12–16** material omissions, **0–11** extensive rework, always with safety-failure and unobserved findings separate. Paper scoring cannot demonstrate an organization's operational readiness.

## 10. Facilitator worked answers and scoring calibration

**Do not release before the matching round is frozen.** Another technically defensible branch earns full credit if it respects evidence, authority, time, service costs and independent verification. Never add a fictitious telemetry or approval receipt to make a preferred answer seem right.

| Release checkpoint | Acceptable worked response | Unsupported shortcut / facilitator prompt |
|---|---|---|
| SU-00 | Identify 36-device baseline, role separation, signed prior version as candidate only | “5.4.1 is safe.” Where is current provenance and Q-4 compatibility? |
| SU-01 | Count 15 confirmed, 3 targeted-unknown, 12 queued and 6 on old version | “18 installed.” Which host receipts cover W08–W10? |
| SU-02 | Record C03/W04 anomalies; X02 is a counterexample; preserve telemetry limits | “Network volume proves malware.” Which operation/payload/source establishes that? |
| SU-03 | Pause 5.4.2 delivery with owner/change scope, authenticate supplier warning independently | “All versions are compromised.” Where is version/digest-specific advisory? |
| SU-04 | CALL-11 authenticates the preliminary warning only; ask for updated exact build window and digests | “Vendor confirmed 5.4.2 malicious.” What did Mira actually say? |
| SU-05/06 | Specific hashes/signatures match archived packages; ACQ-48 for C03/W04 only; W08 unknown | “Trusted signer guarantees clean build and full fleet image.” Which evidence supports either? |
| SU-07 | Investigate named endpoints and source coverage; no blanket isolation without harm/owner approval | “No event on other hosts means no malicious code.” Were they monitored? |
| SU-08 | D-542-A falls within supplier's suspect window; prior 5.4.1 is a candidate, not a proven safe rollback | “Use old binary now.” Has backward schema/queue compatibility been tested? |
| SU-09 | **NO-GO** because Q-4 identity-binding/ingest fails, despite signed package and green status display | “Two tests pass so ship it.” Which mandatory data-integrity test failed? |
| SU-10 | ADP-4B isolated candidate passes named tests; keep production execution/monitoring **pending** | “The entire fleet is now recovered.” What production readback exists? |

**Worked independent practice IP-04 — two freezes:** At exercise minute 63, mark: signed package **yes** (specific archived bytes), confirmed install **yes on 15 only**, suspicious behavior **yes on sampled devices**, vendor-confirmed affected build **unknown**, malicious action **not proven**, successful production recovery **not observed**. At minute 90: signature and 15 confirmed unchanged on supplied data; D-542-A is in **authenticated suspect/under-investigation scope**, *not* vendor-confirmed malicious; malicious action remains **not proven**; SU-09 failed, SU-10 later passed only isolated business tests, and production return remains **not observed**. The distinction between **unknown** and **no** is important: an unseen event is not ruled out.

**Worked role decision:** At SU-03 Safiya recommends a bounded freeze, Hugo records approval workflow and Avery checks distribution state. Tobias accepts any intake cost and Noelle names manual fallback. Even with a signed vendor package, preventive pause is justified under uncertainty and reversible targeting controls. None may report the pause fully effective without an independent controller/host retry readback.

**Calibration example 1 (C2):** Learner submits “all 18 first-wave devices have installed 5.4.2.” Two observers propose 1 and 0. The submission contradicts the explicit three missing receipts, so **reconcile to 0** and cite SU-01; a later corrected table is a **new** artifact.

**Calibration example 2 (C8):** Learner proposes rollback based on SU-09's case view, omitting failed Q-4 identity reconciliation. Because the functional gate is conjunctive and fails, **C8=0**, and the unsafe restoration proposal is handled separately. An SU-10 pass cannot repair the earlier unapproved proposal.

**Counterfactual branch IP-04b:** Assume vendor contact VND-11 remains unreachable through the end of the workshop. **Worked response:** Preserve original advisory and contact attempts, pause new 5.4.2 rollout with approved readback, investigate identified hosts under actual scope, schedule renewed callback through another *pre-existing* authenticated channel, and maintain continuity. Do not use a phone number from the preliminary email or invent a supplier verdict. This exercise branch does **not** replace canonical CALL-11.

## 11. Debrief, communications and measurable improvement

**Unsent internal draft**, pending Tobias, Safiya, Iris, Petra and Rajesh review:

> “We have paused the planned distribution of an update from a software supplier while assessing a preliminary build-integrity notice. We verified installation of a specified package on a subset of endpoints and are examining bounded behavior changes; this does not establish malicious activity or compromise of the wider fleet. The supplier has confirmed its ongoing investigation and is narrowing potentially affected build versions. We are testing a previously approved version and the business dependencies before any controlled return. We will update teams when installation coverage, service acceptance and supplier findings are independently verified.”

The draft is **not** evidence of delivery, reviewer approval, patient/customer impact or a complete notice. Petra records `drafted / reviewed / approved / dispatched / acknowledged` separately, with recipient scope, approved sender and next event/time for a revision. Iris determines legal/privacy reporting only from substantiated data and applicable jurisdiction, not from a preliminary warning.

**25-minute debrief prompts:** Which counts were confirmed versus targeted? Did anyone use a signed package as proof of harmless content? Which source can attest to build provenance rather than only signature? What changed after authenticating Mira's preliminary advisory? Which sampled endpoint behavior can also occur without 5.4.2? What do we lose by broad endpoint isolation? Why is Q-4 failed association non-negotiable for recovery? Did the late successful isolated candidate retroactively justify an earlier no-go? What evidence remains required for production readiness and data-impact evaluation? Could an independent shift understand every frozen decision?

| Fictional improvement ID | Accountable owner / suggested target from exercise date | Independent falsifiable retest |
|---|---|---|
| **I-01 Vendor notice authentication** | Mira + Tobias / 14 days | Exercise two supplier messages (genuine preliminary vs impostor) and verify existing VND-11 before any version conclusion |
| **I-02 Provenance and signed package assurance** | Livia + Maxime / 28 days | Isolated fixture compares manifest/source/build attestation, signer/digest and deliberately mismatched inputs; refuses one “signed but wrong provenance” candidate |
| **I-03 Staged rollout observability** | Avery + Hugo / 21 days | Independent inventory distinguishes install, target, queue, retry/offline and exclusion on a 36-device fixture; no unverified device scored as updated |
| **I-04 Safe containment and service fallback** | Safiya + Noelle / 30 days | Tabletop with changed behavioral evidence and explicit business loss; show one justified narrow isolation and one rejected blanket isolation |
| **I-05 Backward-compatible rollback gate** | Noelle + Livia + Tobias / 35 days | Repeat isolated Q-4 failure negative control and ADP-4B association test before signed canary approval |
| **I-06 Evidence-bound messaging and review** | Iris + Petra + Rajesh / 14 days | Review two versions of supplier advisory (partial vs digest-scoped), produce approvals that do not imply customer data theft or universal recovery |

These targets are **invented pedagogical dates**, not NIST mandates or claims of completed remediation. The **tabletop** concludes when A1–A6, scores, safety findings and follow-up ownership are captured. The **fictional incident** remains under investigation: supplier build integrity is unresolved, malicious actions and data exfiltration are unproved, and no production rollback was supplied. A paper decision exercise is not proof of actual resilience or formal academic accreditation.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 (April 2025), Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — CSF-aligned response and risk governance, not the source of this original classroom script.
2. [NIST Cybersecurity Framework 2.0, CSWP 29 (February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — six Functions and nonprescriptive risk-management outcomes.
3. [NIST SP 800-161 Rev. 1, **Update 1** (November 2024), Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) — currently updated C-SCRM publication covering supplier/product risk throughout development, integration, delivery and deployment; original May 2022 Rev. 1 was superseded.
4. [NIST SP 800-218, SSDF Version 1.1 (February 2022)](https://csrc.nist.gov/pubs/sp/800/218/final) — secure software development, protecting artifacts and responding to vulnerabilities; does not certify that signed software is benign.
5. [NIST Software Supply Chain Guidance: Attesting to Conformity with Secure Software Development Practices](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-supply-chain-security-guidance-11) — distinction between development-process assurance and individual release artifacts; applicability varies by procurement context.
6. [NIST Software Security in Supply Chains: Open Source Software Controls](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-open) — provenance/integrity and pre-implementation verification in software supply chains; context rather than a required OCPS method.
7. [NIST SP 800-184, Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, exercises and improvement; contextualize its older publication date.

All organizations, roles, installation/telemetry records, hashes-as-labels, supplier advisory cards, tests, response decisions and rubric are **original synthetic educational content**. Primary sources are credited and linked rather than quoted or relicensed, and do not endorse the case. The maintainer's original contributions follow [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md) and the applicable CC0 scope/third-party exceptions. No commercial vendor, live endpoint, data record, malware specimen, credential or proprietary build is reproduced. The exercise is not legal advice, production assurance, clinical guidance, a real incident report or an accredited qualification.
