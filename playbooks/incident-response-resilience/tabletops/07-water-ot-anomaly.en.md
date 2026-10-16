# TableTop 07 — Water-system controller anomaly: physical safety before cyber containment

**Edition:** English · **Exercise ID:** TTX-WOT-07 · **Catalog scenario ID:** `water-ot-anomaly` · **Editorial date:** 2026-10-15  
**Status:** Original fictional defensive educational exercise; independent technical, process-safety and human review pending.  
**Format:** 15-minute prebrief, 90-minute facilitated paper exercise and 30-minute debrief. No live plant equipment, chemical process, PLC, SCADA system, packet capture, scan, network change or actual water-quality test is operated.  
**Audience:** Water-plant operators, process safety, water quality, instrumentation, OT engineering/network, SOC and evidence staff, continuity, legal/privacy, communications, utility command and independent observers.  
**Navigation:** This expands the existing [scenario 07 in the ten-entry catalog](../../../web/tabletop/scenarios.json), not a new catalog entry. [Previous written tabletop: 06, public portal disruption](06-ddos-portal.en.md) · [Playbook index](../README.md) · [Next catalog scenario: 08, lost laptop — summary only, tabletop not yet authored](../../../web/tabletop/scenarios.json). See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Fictional plant, safety contract and technical learning objectives

**Every name, organization, host label, field instrument, time, work order, configuration version, record, source receipt, simulated outcome and conclusion below is invented.** There is no actual waterworks, material-specific target, treatment recipe, chemical identity, concentration, valve setting, calibration value, control-system command, engineering drawing or exploitable device detail in this text. Symbolic tokens such as **SP-APPROVED** and **SP-UNRECONCILED** are *labels*, not dosing settings. **ENV-APPROVED** names an owner's abstract, pre-existing safe operating envelope; its physical limits are deliberately omitted. Participants must not calculate or set a chemical dose or manually manipulate an actual plant from the case.

**Fictional organization:** **Brookfen Municipal Water Utility (BMWU)** operates a treatment facility with a supervised chemical-dosing process. Its process controller **CTRL-P**, control-room human-machine interface **HMI-P**, independent locally observed process indicator **FIELD-P**, sensor chain **SENS-P**, and actuator interface **ACT-P** are invented. The treatment system's network segment **NET-SHARED** also transports other monitored safety-related functions, including alarm status and independent permissive information. Neither the ability of those functions to operate independently nor the effect of cutting the segment is established at the opening.

**Trigger:** A control-room display shows the **chemical dosing setpoint** labeled **SP-UNRECONCILED**, while signed work order **WO-218** calls for **SP-APPROVED**. The HMI process-value display and the local field indication also **disagree**. A mismatch is a reason to invoke process-safety assessment; it is **not** proof that the process has changed physically, that a human issued an unauthorized command, that the local gauge is correctly calibrated, or that a cyberattack happened. Operators and the process-safety lead—not SOC—decide whether the operation remains safe and whether an approved manual fallback, isolation of output, interruption of service, or public-safety escalation is necessary.

**Non-negotiable safety rule:** **No active network scan, controller reboot, remote command, broad device/network isolation, ad hoc setpoint write, actuator test or other intrusive response is performed or recommended for live equipment before an explicitly authorized decision by the responsible process-safety owner**, supported by control engineers, operators and current dependency review. This tabletop contains **only paper decisions and supplied fictional evidence**. Where public or worker safety cannot be established, stop the exercise's hypothetical normal-operation assumption and defer to the plant's **own approved emergency response plan and licensed operating staff**. Never invent a treatment method or safe numeric limit.

### Six observable learning objectives

- **O1 — Process and decision authority:** separate plant/process owner, licensed operator, water-quality, instrumentation, OT engineer, network custodian, security investigator and executive responsibilities; name safety stops.
- **O2 — Trust boundaries and physics:** distinguish a signed work-order target, configured setpoint, HMI displayed process variable, independent local measurement and actual water-quality assurance; compare only quantities, units, instruments and time windows that are genuinely comparable.
- **O3 — Source-provenance investigation:** keep setpoint-change requests, controller state readback, HMI cache, sensor metadata, operator field observation and safety-alarm path records separate. A successful command response or shared account label is **not** proof of physical effect or human attribution.
- **O4 — Safe containment:** preserve control logs **read-only**, authorize safe physical checks and an approved manual operating procedure, and protect shared alarm/interlock dependencies from unassessed network changes.
- **O5 — Conditional recovery:** perform engineering- and operator-authorized bounded testing of sensors, actuators, process alarms, network dependencies and approved setpoint correspondence before returning to automatic control.
- **O6 — Evidence-limited learning:** document why a physical reading is reliable or uncertain, calibrate alternative hypotheses, score frozen decisions, communicate accurately and prescribe falsifiable corrective tests.

### NIST alignment without pretending this is a prescribed plant procedure

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (April 2025 final) integrates response into [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) risk management. Preparation touches **Govern, Identify and Protect**; incident-specific **Detect, Respond and Recover** are supported by continual improvement. It does not prescribe these particular chemical-operation steps, authorities or tabletop scores. [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) (September 2023 **final**) discusses OT security in the context of **physical safety, performance and reliability**. A Revision 4 **initial public draft** was posted September 2026; it is **not** the final standard and does not replace Rev. 3 for this exercise. [EPA water-sector cybersecurity planning](https://www.epa.gov/cyberwater/cybersecurity-planning) provides response and emergency-planning resources; this case neither claims specific legal duties for a particular utility nor copies the EPA templates.

| Teaching phase | CSF 2.0 Functions | Necessary safety/evidence decision |
|---|---|---|
| **Preparation / authorization** | Govern, Identify, Protect | Work-order authority, current process envelope, manual SOP, instrumentation/calibration and shared safety-function dependencies |
| **Detection and analysis** | Detect | Does a displayed/configured target deviate from WO-218? Are physical measurements independent, comparable, fresh and trustworthy? |
| **Containment and continuity** | Respond | Operator-approved manual procedure; safe physical checks; read-only control-log preservation; **no reflexive network isolation** |
| **Engineering recovery** | Recover | Independent verification of sensor/actuator behavior, approved setpoint, alarm dependencies, and controlled test evidence |
| **After-action improvement** | Govern, Identify/Improvement | Update work-order authorization, two-source measurement checks, log coverage and a witnessed safe-reversion drill |

The table is a **classroom mapping**. It is not a substitute for process-hazard analyses, the plant's legal/regulatory obligations, water-quality sampling program or a licensed operator's actual decisions.

## 2. Named teams and non-interchangeable authority

The following role charter is **fictional**, and the participants' names are distinct from the earlier TableTops. In real facilities, the designated responsible process operator and legal authorities must be identified under the utility's actual organization and applicable law. One classroom participant may act multiple characters, but the **independent safety review and signatures must remain separately attributable**.

| Person / team | May approve, decide or witness in the exercise | May not authorize or infer |
|---|---|---|
| **Tess Carrow — Process-Safety Authority and Plant Superintendent** | Decide safe process state, stop/distribution escalation, physical-verification requirements, entry to manual mode and conditions for controlled automatic return | Attribute cyber actor or accept a scan/reboot/network cut from SOC without process-safety review |
| **Emilia Shore — Lead Shift Operator** | Compare approved work order to local operating records, supervise safe independent physical checks, invoke the **plant's existing approved manual SOP** under Tess's authority, maintain field status and **sign operator acceptance** | Guess a dosing value, change the recipe from a tabletop, or accept HMI alone as safe evidence |
| **Soren Iqbal — Water Quality and Laboratory Steward** | Evaluate whether authorized sampling and laboratory checks are necessary, record chain/certainty and report whether **supplied** water-quality evidence supports operation | Prescribe a chemical dose, declare drinking water safe from one indicator, or infer contamination from screen disagreement |
| **Dante Kiraly — Instrumentation and Metrology Engineer** | Evaluate instrument tag equivalence, ranges, calibration currency, readback and bounded sensor/actuator test design with process approval | Treat an out-of-calibration gauge as physical truth or run intrusive tests during an unresolved hazard |
| **Yuna Presley — OT Control Engineering Owner** | Reconcile signed configuration against controller and HMI source identities, inspect read-only change history, prepare versioned rollback/automatic-return proposal | Write PLC/controller parameters, reboot or force output without Tess/Emilia's authorization and safe test plan |
| **Maalik Hsu — OT Network and Safety Dependencies** | Map shared NET-SHARED route, alarm/permissive dependencies, collection access and impact; propose only **authorized passive/log-source evidence** | Isolate network segment, scan devices or disable an alarm path on a cybersecurity hunch |
| **Kelsey Adewale — Cybersecurity Incident Commander** | Open security investigation, separate hypotheses from observations, prioritize preservation requests and coordinate authorities | Override plant operators, declare malicious actor or assign control changes to IT alone |
| **Tarek Fenn — Forensic Evidence Custodian** | Acquire permitted control logs and snapshots in **read-only** mode from existing safe interfaces, track scope/hashes/custody | Probe controllers, duplicate hazardous configuration values into public records or claim a request is a completed collection |
| **Adeline Greaves — Continuity and Public Service Liaison** | Support operator-approved contingency service arrangements, staffing, materials, affected-user communications planning and business-impact monitoring | Decide physical safety or promise water output is unaffected without operator/lab support |
| **Vida Escobar — Communications and Public Information** | Prepare bounded status updates after Tess/Soren/legal review; record drafted/approved/issued/acknowledged separately | Publish “water unsafe,” “water safe,” “attack confirmed,” or “fully restored” without appropriate evidence/authority |
| **Calum Desai — Legal, Privacy and Regulatory Coordination** | Evaluate fact- and jurisdiction-specific notice, worker protection, contracts, evidence retention and minimum data handling | Invent a universal regulatory threshold or personally certify process conditions |
| **Zora Bellwether — Utility Executive Incident Sponsor** | Allocate crews and continuity resources and record residual organizational risk/escalation decisions | Replace operator safety authority, technical test witness, or legal/regulatory determination |
| **Ivo Calder — Independent Facilitator and Evaluator** | Release fixed injects, freeze submissions, score by pre-announced rubric and record missing facts | Invent a water test, coach a scored decision or order real plant operations |

**Authority ledger:** `Tess = process-safety decision`; `Emilia = operator execution/field verification and independent sign-off`; `Dante/Yuna = engineering test design and interpretation`; `Maalik = network dependency evidence`; `Kelsey/Tarek = cyber/forensic framing`. No one signature substitutes for all others. A technical **proposal**, safety **approval**, operator **reported execution**, **independent verification**, and **controlled return accepted** are five separate states.

## 3. Safe facilitation, three clocks, source taxonomy and stopping criteria

**Room packet:** supply the fictional, sealed cards **WT-00 through WT-10**; release **WT-00 only** initially. Provide six blank outputs A1–A6, a role/approval sheet, a source/clock ledger, two hypothesis columns, manual-mode and safety dependency questions, a recovery acceptance form, and the rubric. No hardware, software, water, chemical material or network connection is needed. Case labels like `HMI-P`, `CTRL-P`, `WO-218` and `ENV-APPROVED` are **symbolic abstractions**, not actionable process data.

**Clock discipline:** (1) a record's **fictional plant/source UTC**, (2) the **facilitator exercise minute** when it is released, and (3) the **frozen decision minute** are separate. Field observations, display refreshes, controller event times, log ingestion and human interview times can be distinct. **A later-released card describing an earlier event cannot justify an earlier decision.** Keep old decisions immutable and add time-stamped revisions.

**Source hierarchy is not an automatic truth ranking.** WO-218 proves an *approved intended target* within its authority/validity, not the plant's current physical state. A controller readback proves its observed configuration at a stated time/source, not the actuation or source of an unauthorized instruction. HMI-P may display a cached value. FIELD-P represents a field instrument only after verified tag, units, range, calibration and sampling method. A laboratory or independent physical check supports only the named property, measurement interval and sample chain. An alarm stream is not self-authenticating if its network path is impaired. These different objects **must not** be equated merely because each has a timestamp.

**Stop card:** A proposed live scan, PLC reboot, network isolation, forced command, unsafe actuator exercise, guessed chemical change, physical water-safety claim without permitted measurement, unapproved public notice or use of a classroom fictional threshold as an actual plant control immediately **stops the exercise**. Participants record why the proposal was unsafe and defer to Tess/Emilia and the utility's own process safety and emergency response plan. If operation cannot be established safe, authorized staff decide protective actions; the facilitator does not supply chemistry or dosage instructions.

**Decision row contract:** `decision ID | source/event UTC | released WT IDs + minute | freeze minute | observed fact and source | competing hypotheses | physical/process safety state (known/unknown) | option and effect on shared alarms | exact decision authority | proposed/approved/simulated-executed/independently checked | stop/rollback | next review trigger`.

## 4. Progressive release ledger and fixed synthetic injects

The exercise clock is **90 minutes**, and the case's UTC event clock is entirely fictional. Each checkpoint requires a frozen paper artifact before later cards become usable.

| Exercise minutes | Card(s) | Fictional case/source UTC | Evidence question and output |
|---:|---|---|---|
| 0–7 | **WT-00** | 07:50 | Work order, plant authority and approved manual SOP prerequisites |
| 8–18 | **WT-01** | 08:11–08:13 | Screen/field discrepancy, observations vs hypotheses |
| 19–27 | **WT-02** | 08:17 | Distinguish setpoint from process variable and establish independent-check plan |
| 28–36 | **WT-03** | 08:22–08:25 | Controller event/actor uncertainty and log preservation |
| 37–45 | **WT-04** | 08:28 | Shared network alarm dependencies and prohibited containment |
| 46–55 | **WT-05** | 08:35–08:41 | Operator-authorized manual fallback, continuity and verification |
| 56–64 | **WT-06** | 08:46–08:50 | Read-only source acquisition and custody |
| 65–73 | **WT-07** | 09:02 | Independent controller configuration vs approved WO |
| 74–81 | **WT-08** | 09:18 | Limited engineering test finds failure; no-go |
| 82–87 | **WT-09** | 09:44 | Revised limited test, still not a plant return |
| 88–90 | **WT-10** | 10:10–10:22 | Bounded physical/operational acceptance or pending decision |

### WT-00 — Baseline and preapproved safety contract (minute 0)

**Synthetic 07:50 plant packet:** Supervisor Tess and lead operator Emilia signed work order **WO-218** for the dosing subsystem, approving target label **SP-APPROVED** under predefined and undisclosed **ENV-APPROVED** (process envelope). It specifies its work window and the responsible shift, but the packet does **not** state that its change has been executed. The plant has **SOP-MAN-2**, an approved manual operating and contingency procedure known to trained operators; its steps are deliberately **not reproduced** here. There is a documented plant emergency escalation tree. The last test of shared network alarm dependencies is old enough that it cannot prove the current NET-SHARED topology.

**Team decisions:** Tess checks WO validity, accountable shift and safe operating assumptions. Emilia identifies which **independent local readings** would be necessary and who is qualified to perform them. Soren identifies laboratory/quality status needed for any public-safety assessment. Yuna and Dante name source types for the setpoint and measurement channels; Maalik plans a **read-only** dependency inventory review. Kelsey prepares an incident record without declaring a cyberattack. No one orders a new physical setpoint.

**Why this matters:** The approved recipe *as a signed document* does not mean a controller currently holds or physically enacts it. A manual fallback is an approved **process**, not a license for the facilitator to invent manual chemical dosing steps.

### Round 1 — WT-01: two disagreements, neither yet a causal verdict (minutes 8–18; Detect)

**Synthetic 08:11–08:13:** The control-room display **HMI-P** reports configured setpoint label **SP-UNRECONCILED**, while the signed WO-218 names **SP-APPROVED**. At 08:11 HMI-P shows **PV-H** (a process-value indicator on screen), while an operator walking an approved observation route records field indication **PV-F** at 08:13. The **two observations are reported as disagreeing**, but the packet does not yet establish that both reference the same measurement point, use comparable scales, have aligned sampling times, or carry valid calibration. No physical process test, independent measurement acceptance, change-command actor attribution or water-quality result is supplied. The screen's possible cache behavior is unknown.

**Decisions:** Emilia informs Tess immediately and identifies a safe local cross-check through trained operators, **without changing setpoints**. Tess invokes the existing process-safety decision tree and, if safety cannot be established, the facility's emergency protocol. Dante asks about instrument tag, range, units and calibration; Yuna preserves configuration-source identity. Kelsey opens **BMWU-IR-007** as **OT process discrepancy under assessment**, not as proven malicious control. Soren withholds any claim about potable-water quality until authorized, relevant laboratory/process evidence exists.

**Four competing hypotheses:** H1 authorized but wrongly displayed/configured change or HMI staleness; H2 instrument/time/tag mismatch; H3 fault/configuration defect; H4 unauthorized command or malicious interference. Each is a question, not equal-probability truth. **Fault or operator error** can have safety implications without being a cyberattack; **cyber suspicion** does not authorize an unsafe control action.

### Round 2 — WT-02: an independent physical check must actually be comparable (minutes 19–27)

**Synthetic 08:17 field assessment receipt:** A second qualified operator supervised by Emilia checks **FIELD-P** via the plant's preapproved safe observation method, and records **two field-source identities** for the measurement chain. The record says one local indication appears **within ENV-APPROVED** for the *property measured* in that limited interval, but a second indicator's calibration status is **pending verification**. The HMI and field source labels have **not yet been independently matched to the same measurement point and physical units**. No chemical quality sample or actuator-position proof is present.

**Decision:** Tess sets the safety posture based on the available process evidence and the existing approved operating plan; unknown comparability remains a reason for caution. Dante requires tag/range/calibration checks before declaring either instrument authoritative. Soren plans qualified water-quality verification according to real plant procedures, without asserting results. Emilia records the immediate operator observation, who made it and the time rather than guessing a dosing amount.

**Worked comparison:** “FIELD-P looked normal” is **not** a universal clearance. The source supports “one named indication was within its owner's approved envelope at 08:17; another calibration and sensor comparability remain open.” A display setpoint and measured physical value are *different quantities* and should not be numerically subtracted even if both were available.

### Round 3 — WT-03: source event and shared login are not physical effect or actor (minutes 28–36)

**Synthetic 08:22–08:25 control event summary:** A preexisting controller event-log excerpt says **CFG-E07** recorded a **setpoint-write request** with response status **accepted** at 08:09 from shared operator role **OPS-ROLE**, while its human initiator, endpoint, and change ticket field are blank in the retained view. A separate HMI event at 08:10 records a cache refresh. The complete controller state, actuator output, physical process impact and permission chain are **not yet supplied**. It is possible the value changed, a request was queued or the display retained stale information; the event response alone does not determine those questions.

**Decisions:** Kelsey asks a bounded “who/what/when/authorized?” question and does not attribute wrongdoing to an operator. Tarek requests a lawful, nonintrusive read-only copy of existing controller/HMI logs with original record ID, time basis and access restrictions. Yuna asks for an independent **safe** current configuration readback through an approved method; the classroom performs none. Tess/Emilia continue safety-first disposition. **Negative control:** A shared role or successful request does **not** identify the human or prove that the physical dose changed.

### Round 4 — WT-04: proposed blanket isolation would damage shared safety observability (minutes 37–45; Respond)

**Synthetic 08:28 dependency review:** Maalik provides a **recently collected but still incomplete, read-only** network topology reference **NET-MAP-28**: the shared NET-SHARED path transports dosing HMI telemetry **and** at least two other monitored process-safety/alarm status feeds. The map does not prove whether the latter can function independently if the path is cut. No test shows controller fail-safe behavior when isolated, and no plant approval exists for switching that network state.

**Decision:** Tess explicitly **does not authorize broad NET-SHARED isolation, active scanning or controller reboot** while safety dependencies remain unknown. Maalik documents which independent process/safety channels must be checked first and proposes passive read-only review of existing network event records if access permits. Yuna explains potential loss of alarm visibility, while Emilia/Soren assess how operations would safely monitor until a planned change. Cyber team maintains evidence-preserving options and narrow security hypotheses.

**Conditionals:** If a later verified active harmful control action occurs, Tess may assess a *targeted* response with OT engineering, operators and emergency procedure, balancing immediate life/public risk, known failure modes and proof of action. That hypothetical future escalation is **not supplied**. “Disconnect everything to contain malware” is an unsafe shortcut in this fixture.

### Round 5 — WT-05: manual procedure is a governance gate, not a chemical recipe (minutes 46–55)

**Synthetic 08:35–08:41 process authority and operator receipts:** Tess signs a limited **SAFETY-35** paper authorization referencing existing **SOP-MAN-2**, specific trained operators, an observation/communications interval, stop and return triggers, and the need to maintain independent alarms/field oversight. Emilia's **OPER-39** report says trained staff **entered the approved manual operating state** under the actual fictional plant procedure at 08:39. A separate operator witness **READBACK-41** records that the named manual-state indicator and monitoring responsibilities were checked at 08:41. The classroom cards provide **no steps for chemical control**, actual actuator settings, specific dosing or public-water safety declaration. Manual state is a bounded *operating mode observation*, not proof the product is safe or that cyber root cause is resolved.

**Decisions:** Tess retains the process-safety go/no-go. Emilia supervises physical observation and reports issues via plant emergency routing. Adeline arranges trained staffing and approved continuity contingency if safe production cannot be assured. Soren coordinates required qualified water-quality sampling decisions; no lab results are invented. Vida prepares a factual unsent update. Yuna/Dante plan **non-disruptive** tests for later engineering review. SOC cannot declare case closed simply because manual mode is reported active.

**Contrast:** A team that announces “the plant is safe because it switched to manual” has skipped the difference between *mode selection*, *physical verification*, *quality assurance* and *safe continued service*.

### Round 6 — WT-06: read-only evidence, source and copy receipts (minutes 56–64)

**Synthetic 08:46–08:50 evidence packet:** Tarek's collection request **LOG-REQ-46** asks for existing HMI/controller change history, access events, timestamp references and network alarm-path history, each scoped to this incident. At 08:48 **OT-ARCH-48** reports a **read-only** export from an already approved historian interface, by an independent qualified evidence operator, covering controller and HMI management events **08:00–08:45**. At 08:50 **HASH-50** records a second independent byte-integrity check of that **particular acquired export copy**, not an integrity certification of the complete physical control state or all historian logs. The requested network alarm log slice is **still pending**; no active interrogation of CTRL-P or PLC register change occurred. There is an acknowledged time-sync uncertainty between HMI refresh and controller event time.

**Decision:** Tarek distinguishes `requested / acquired / independent copy-readback / analyzed` and labels source completeness **partial**. Kelsey reviews access to sensitive operational detail and uncertainty. Yuna/Dante refrain from drawing physical conclusions from a hash equality. Maalik continues read-only dependency checks without disabling the safety path. Legal/communications roles avoid publishing source details that would expose a real plant, though these cards are synthetic.

**Negative control:** “The logs are preserved” is too broad. The actual supported statement is “one bounded historian copy is acquired and its bytes independently checked; network alarm records and some time correlation remain pending.”

### Round 7 — WT-07: now a setpoint mismatch is independently confirmed, cause still unknown (minutes 65–73)

**Synthetic 09:02 independently authorized controller state readback:** After Tess approves the *specific safe, nonintrusive method* and Dante/Yuna review its process effect, an operator-verified state record **CFG-READ-02** reports current controller target label **SP-UNRECONCILED**. A separately preserved authenticated copy of **WO-218** names **SP-APPROVED**, with no signed change amendment in the **scoped complete work-order register** for the incident period. The HMI display may also be stale about a **process measurement**, but that question does not undo the independently read back **configured target**. No supplied source proves **who** changed the target, when actuation changed physically, whether an alarm was suppressed, or actual water-quality impact.

**Decision:** Tess/Emilia can now state **a configuration target deviates from the approved work-order target in the supplied scope**. Kelsey can open a technical **unreconciled/unauthorized-by-register configuration-change** investigation, without calling it an attack. Yuna preserves exact config source/version **under restricted evidence rules** and builds a proposed return plan; Dante requires independent verification of measurement chains; Soren keeps quality conclusions bounded. Nothing authorizes SOC to set the controller target. A comparison between **two symbolic target labels** can establish administrative mismatch **without publishing physical dosing values**.

**Chronology correction:** The existence of CFG-READ-02 at exercise minute 65 must **not** be imported to make the team's earlier WT-03 “request may or may not have changed state” answer look defective.

### Round 8 — WT-08: first limited engineering test fails a required gate (minutes 74–81; Recover)

**Synthetic 09:18 simulated *isolated/non-live* engineering test:** With a versioned test plan and Tess/Emilia's classroom approvals, Dante and Yuna review a **paper-described, bounded engineering test fixture**, not the actual operating plant. Test report **ENG-A** states (a) a first sensor channel and reference agree for one defined property/test interval, (b) **a second sensor path fails a comparability/calibration acceptance check**, (c) the proposed controller-setpoint label can be aligned with WO-218 in the isolated model, (d) there is **no** verified end-to-end actuator response or shared safety-alarm dependency acceptance. No chemical adjustment, actuator movement or live OT testing is carried out by learners.

**Decision:** Tess and Emilia record **NO-GO automatic return**. Dante requests repair/revalidation of the failed sensor path with its own controlled evidence. Yuna preserves the candidate and rollback; Maalik requires separate alarm/permissive continuity validation. Soren/Adeline maintain qualified quality-monitoring and manual operating/contingency review. **A passed configuration comparison cannot compensate for failed sensor or untested actuator/safety dependencies.**

**Negative control:** “One sensor passed, therefore automation is safe” improperly averages conjunctive safety gates. Failures must remain visible in the original frozen artifact.

### Round 9 — WT-09: later tests pass in a narrower fixture, not production acceptance (minutes 82–87)

**Synthetic 09:44 second engineering packet:** A **new** named test revision **ENG-B** includes a bounded, authorized **non-live** fixture that reports: two referenced sensor channels agree with an independent calibrated reference under the **defined model test conditions**; its simulated actuator-response/permissive check follows the approved engineered behavior **in that fixture**; an independently observed shared alarm-path check returns the expected **test signals**; the proposed target label matches WO-218. All observations are **test records** and their scopes do not show the live physical chemical process safe. The process historian link and actual operational performance remain separately controlled.

**Decision:** ENG-B permits **consideration** of a controlled live-return plan, not immediate automatic control. Tess requires a specific future limited plant safety test under real operational authorization and stop conditions, while Emilia demands independent real physical observations and monitoring. Dante/Yuna record what ENG-B can and cannot transfer to the live plant; Maalik confirms shared network/alarm test limitations. New approvals cannot retrospectively correct WT-08's NO-GO; keep both artifacts.

### Round 10 — WT-10: explicit independent physical gate and operator sign-off (minutes 88–90)

**Synthetic 10:10–10:22 operator/process acceptance card, released only after WT-09 freezes:** This card reports a **separately authorized, operator-controlled limited plant return assessment** under Tess's approved process and qualified staff—not a test executed for the educational exercise. It supplies **no physical steps, values, chemistry or equipment commands**. At two specified observation checkpoints, **FIELD-OBS-1** and **FIELD-OBS-2**, **independently checked field measures** of the named, comparable physical quantity are recorded **within preapproved ENV-APPROVED**; tags, units, time, instrument calibration acceptance and responsible operators are signed in the **restricted fictional plant record**, not disclosed as dosing instructions. Dante/Yuna's bounded operational receipts say the live sensor chains, actuator response constraints, approved target association and critical shared alarm/permissive paths passed the *specified controlled acceptance checks*. Soren's status does **not** declare all drinking-water quality dimensions assessed; required public-quality monitoring and applicable plant compliance decisions remain in their own programs.

**Authority and observed outcome:** Tess's **SAFETY-RETURN-22** approves a **staged return to automatic supervisory control** for the specified subsystem after those scoped observations; Emilia's **OPER-ACCEPT-22** confirms operating state, field monitoring, stop/rollback awareness and **operator sign-off**. The two independent physical observations and operator acceptance are the minimum **supported classroom acceptance** for the named controlled return. The card does not show every controller healthy, a recovered citywide service, exact cause, adversary identity or unlimited future safety.

**Decision:** The team may close **this narrow operational gate**, with named independent monitoring and review cadence, but leave technical root-cause attribution, missing alarm-log slices and any unsupplied water-quality assurance **open**. An alternative team may retain a **conditional hold** if it explains a genuine missing required check in its charter; a score should reward reasoning rather than reflexive restart.

**No hindsight:** This 10:22 event, revealed at exercise minute 88, does not justify what was written at WT-08 or WT-09. The fictitious operating result is *supplied later*, not produced by students.

## 5. Worked evidence matrix and independent exercises

Another facilitator can reproduce all inferences using the fixed WT cards, **without a controller, chemical sample, network tool, numeric dose or actual plant test**.

| Source/claim | Card and exact observation | What it does **not** establish |
|---|---|---|
| Intended setpoint | WT-00, signed WO-218 → SP-APPROVED | That controller or process presently implements it |
| Displayed configuration | WT-01, HMI-P → SP-UNRECONCILED | Whether HMI cache is fresh or physical effect occurred |
| Display versus field measurement | WT-01/02, PV-H differs from PV-F; calibration/tag equivalence pending | Either indication being inherently correct or comparable |
| Controller command response | WT-03, CFG-E07 `accepted` for shared OPS-ROLE | Human initiator, actual target/readback or physical change |
| Shared network dependence | WT-04, NET-MAP-28 includes other safety-related feeds | That disconnecting NET-SHARED is safe or will preserve alarms |
| Manual operating state | WT-05, SAFETY-35 + OPER-39 + READBACK-41 | Chemical quality clearance or end of cyber investigation |
| Acquired evidence copy | WT-06, OT-ARCH-48 + HASH-50 for scoped slice | Complete logs, network source coverage, physical state |
| Actual configured target | WT-07, CFG-READ-02 → SP-UNRECONCILED | Malicious actor, root cause, water-quality impact |
| First engineering candidate | WT-08, ENG-A has failed sensor gate | Permitted live auto return |
| Revised engineering candidate | WT-09, ENG-B passes limited model checks | Live physical response or plant operator acceptance |
| Narrow automatic return | WT-10 independent FIELD-OBS-1/2 + controls and operator signature | All systems safe forever or attacker identified |

### Independent practice EX-TTX07-01 — Evidence versus inference

**Objective:** classify statements without false attribution. **Inputs:** WT-00 through WT-03 only. **Task:** for each statement “HMI and WO differ,” “the physical chemical dose definitely changed,” “OPS-ROLE identifies the engineer,” “the field gauge alone proves water quality safe,” record `observed / hypothesis / unsupported`, source and missing discriminator. **Expected artifact:** a four-row evidence table with a next qualified test. **Rubric:** 2 points for each correctly bounded claim (maximum 8), then compare to the worked answer below.

### Independent practice EX-TTX07-02 — Safe containment decision

**Objective:** protect public/process safety under uncertainty. **Inputs:** WT-00–WT-05. **Task:** compare (A) cyber team's broad NET-SHARED isolation, (B) operator-approved SOP-MAN-2 with field checks and read-only preservation, and (C) ignoring discrepancy because HMI is probably stale. Name decision authority, safety function risk, evidence to retain, stop/rollback and next trigger. **Expected artifact:** a signed paper decision envelope, not physical instructions. **Rubric:** full credit only if the chosen option respects process authority and shared alarm dependencies.

### Independent practice EX-TTX07-03 — Source and chain of custody

**Objective:** distinguish logs requested, collected, verified and evaluated. **Inputs:** WT-03 and WT-06. **Task:** make a ledger for LOG-REQ-46, OT-ARCH-48 and HASH-50 and describe the missing alarm slice and time-correlation limitation. **Expected artifact:** source/copy/derivative and status entries with access/retention scope. **Rubric:** maximum 6 points for separate states and missing-source identification.

### Independent practice EX-TTX07-04 — Conjunctive recovery gate

**Objective:** evaluate a safe return to automation. **Inputs:** WT-07–WT-10, released at their actual exercise minutes. **Task:** freeze NO-GO at WT-08, then a separate WT-09 decision; at WT-10 determine which exact *additional* independent physical/operator evidence changes the acceptance status. **Expected artifact:** three immutable decision versions, including outstanding cyber/quality uncertainties. **Rubric:** 2 points per accurate gate and no retrospective repair, maximum 8.

### Independent practice EX-TTX07-05 — Communication and root-cause humility

**Objective:** draft a bounded notice. **Inputs:** WT-01–WT-10 as available. **Task:** write one internal 90-word status without numeric treatment instructions, with `drafted / reviewed / approved / sent` fields and the role that would authorize each; list two claims that must remain open. **Expected artifact:** an unsent communication, source IDs and next update condition. **Rubric:** maximum 6 points for source limits, safety approval and open questions.

## 6. Response options and conditional consequences

These are **classroom branches, not instructions to operate a utility**. A participant's proposal never manufactures approval, execution or effect receipts. If the facilitator adds hypothetical evidence, it must be a **new, time-stamped card**, preserving prior releases.

| Option | Required authority, reason and proposed proof | Conditional consequences and limits |
|---|---|---|
| **A. Let the screen override the signed work order** | No supported approval for this choice | Reject: HMI freshness, controller state and physical relation are not established |
| **B. Unilaterally force the WO setpoint into CTRL-P** | Qualified process/engineering owner authority and safe change procedure would be required, **not supplied** | Reject now: a blind write may change the physical process before safety checks |
| **C. Scan/reboot/isolate CTRL-P or NET-SHARED at SOC request** | Tess's process safety authorization, verified dependency safety, qualified OT plan, stop/rollback and monitoring would be required | Reject on current facts: alarm/permissive information shares the route |
| **D. Verify independent safe physical indications** | Emilia under Tess's approved procedure, calibrated/comparable sources, time and signed observations | Supports **measured property at specified checkpoints only**, not all water quality |
| **E. Enter approved manual process state** | SAFETY-35, SOP-MAN-2 and operator reporting with monitoring/stop conditions | WT-05 supports bounded state receipt, not universal process clearance |
| **F. Collect control logs read-only** | Tarek permission, qualified independent collector and bounded approved historian interface | One archived slice verified; missing alarm/time sources remain open |
| **G. Return to automatic after first green model test** | WT-08 lacks sensor, actuator and alarm acceptance | **NO-GO**: physical safety gates are conjunctive |
| **H. Consider return after ENG-B** | WT-09 permits a further process-authorized limited live acceptance review | Candidate only: no live operator/physical acceptance yet |
| **I. Accept narrow automatic return after WT-10** | Tess safety decision, engineering scoped checks, two independent physical readings, Emilia sign-off and monitored rollback | Supports named subsystem within time/window, not cause attribution or lifetime safety |
| **J. Announce cyberattack or contaminated water now** | Credible cause- and quality-specific findings plus lawful authorization would be necessary | Unsupported; alert and regulatory duties are separately assessed by qualified owners |

**Contrasting worked decision:** A cyber analyst sees an unexpected setpoint and proposes to “cut the OT subnet.” Maalik's WT-04 reveals that the same path carries other safety signals. The safer defensible decision is **stop active IT intervention**, retain safe existing read-only logs, invoke Tess/Emilia's process safety protocol and consider only a narrowly engineered later change after dependencies are independently understood. This is not an assertion that cyber containment is never appropriate; rather, that its consequences must be assessed by the authorized process owner.

**False reassurance test:** At WT-09, an analyst writes “the model test passed, therefore treated water is safe.” The model test covers limited sensor/actuator/alarm behaviors and does **not** assess all water-quality properties or real plant outputs. A correct alternative says “engineering candidate has passed named non-live checks; physical and operator acceptance remains pending.” A strong physical check can also coexist with unresolved cyber attribution.

## 7. Safe physical verification and read-only evidence contract

**No steps in this section are sufficient or intended for an actual treatment operation.** They are **questions to ask responsible plant personnel and evidence reviewers**. Only the facility's validated procedures and qualified personnel can govern live operation.

1. **Identify the real safety authority:** which person owns the process state, the current work-order revision and the plant emergency escalation? Document signed delegation, not inferred job title.
2. **Classify the objects being compared:** intended setpoint, actual controller-configured target, HMI displayed target, HMI process reading, local comparable process reading, laboratory result and quality acceptance are *different evidence types*. Record tag, units, method, sampling time, source and calibration status without publishing hazardous numeric values.
3. **Check field data independence:** a second observer or physically independent, verified measurement chain can corroborate a named property within an approved envelope. Two readings from one shared failed sensor do **not** establish independent corroboration; time-averaged/cached values may mislead.
4. **Prioritize safe control state:** use only existing, qualified operator-approved manual or emergency procedures when Tess authorizes. Note stop conditions and independent alarm/quality monitoring. “Manual active” is **not** a water-quality certificate.
5. **Protect OT dependencies:** determine which other safety-related functions rely on a proposed cut, reboot, scan or policy change. Until qualified process review and signed change exist, **do none of these actions**. Even passive evidence acquisition requires confirming that the approved source/interface itself is non-disruptive.
6. **Preserve original logs as sources:** use already approved read-only historians or backup copies as qualified owner permits, with source identity, capture scope, UTC offset/retention, acquisition receipt and independently verified bytes. Avoid active interrogation and never delete the original logs to “reset” alarms.
7. **Interpret control events narrowly:** accepted setpoint write does not prove human initiator, eventual controller state, physical output change or harmful public effect. Correlate authorized WO, independent config snapshot, sensor/actuator and quality evidence **only once each card is released**.
8. **Assess and test bounded recovery:** engineering checks sensor comparability/calibration, intended/permitted target, actuator response and shared alarms/permissives in approved limited tests; a laboratory or operator independently confirms the particular needed process/quality properties according to actual plant procedures.
9. **Require operator signature and rollback owner:** only after required independent measurements align with **the approved operating envelope** and the responsible operator signs the return may automatic control be accepted. Maintain active monitoring with explicit stop and recurrence triggers.
10. **Separate impact statements:** “configured target deviated from WO” can be true while actor, root cause, actual exposure and safe long-term performance remain unknown. Keep any legal/regulatory notices with the qualified utility and legal/public-safety owners.

**No diagram is used:** A generic arrows-and-roles chart would not explain more than the explicit source/authority tables; a literal plant topology or treatment diagram could be misleading or operationally unsafe. The **comparison matrix** and **release chronology** are the substantive explanatory visual structures.

## 8. Recovery and conjunctive acceptance gates

A controlled return has **independent evidence and multi-owner signatures**. A pass on one sensor, a successful code response, a mode-switch receipt or one "green" engineering test cannot compensate for a failed or unassessed safety requirement. Every gate has a source ID, responsible reviewer, decision time, scope, missing evidence and explicit `pass / fail / not evaluated` state.

| Gate | Required evidence | Accountable approver / NO-GO |
|---|---|---|
| **G1 approved process envelope** | Valid signed WO-218 version and **ENV-APPROVED** scope; no guessed numeric setting | Tess and Emilia: no uncontrolled target change |
| **G2 independent physical verification** | Comparable and fresh field-source measurements; independent instrument/calibration and operator witness | Emilia/Dante: unmatched tag/calibration is **not evaluated** |
| **G3 operator safety state** | SOP-MAN-2 authority, separate OPER-39 and READBACK-41, emergency stop and staffing | Tess/Emilia: manual mode alone not full clearance |
| **G4 source and incident custody** | CFG-E07, OT-ARCH-48, HASH-50 with evidence type, clock and missing alarm logs explicit | Tarek/Kelsey: missing logs not silently passed |
| **G5 sensor chains** | Both relevant channels independently tested for comparability/calibration in a bounded engineering fixture and live return as required | Dante: WT-08 failure → **NO-GO** |
| **G6 actuators and interlocks** | Restricted qualified engineering checks of permitted actuator behavior and safety/permissive route, with independent readback | Yuna/Maalik: untested function → **NO-GO** |
| **G7 automatic target/config** | Controller configuration and HMI source association correspond to approved WO, versioned records and change authority | Yuna/Tess: no blind setpoint writes |
| **G8 quality and public safety** | Process owner and Soren's required monitoring/sample program review; no extrapolation from one physical meter | Tess/Soren: unsupplied quality evidence remains separately open |
| **G9 controlled operational return** | WT-10 two independently checked field observations within envelope, qualified engineering receipts, Tess approval and **Emilia operator sign-off** | Tess/Emilia: no signed operator acceptance → **NO-GO** |
| **G10 monitoring/continuity** | Named watch interval, alarm availability, fallback/stop triggers, communications, review and next shift handoff | Adeline/Vida/Zora: no permanent “all safe” from one test |

**At WT-02:** One limited physical source within range with another calibration pending is **not enough** for automatic control or a public-water quality statement.  
**At WT-05:** The authorized manual state supports safe-process management as a **bounded operator response**, still with monitoring.  
**At WT-08:** ENG-A **fails** a required sensor gate; automatic return is **NO-GO** even if a setpoint label aligns.  
**At WT-09:** ENG-B reports **isolated fixture** passes for the specified model tests only; plant return is **not observed**.  
**At WT-10:** In the *fictional scenario only*, the separate physical process checks, engineering acceptance, authorized Tess decision and Emilia's explicit operator signature support **a narrow, monitored automatic return** for the named subsystem. Root cause, actor, other plant subsystems and any unsupplied water-quality program evidence remain open.

**Acceptance semantics:** A recorded sensor value being inside an approved range proves only a *particular measured property in a particular interval*, given instrument trust. A qualified sampling/quality conclusion follows separately from whatever the actual plant must measure. Do not use the symbolic case as a procedure for water dosing or distribute an unreviewed "safe to drink" claim.

## 9. Participant artifacts, rubric and hard stops

Each team delivers **six frozen artifacts**. The observer evaluates only the source set actually released by that point, not fluent explanations made after the fact.

| Artifact | Minimum testable fields | Independent reviewer challenge |
|---|---|---|
| **A1 source/clock/release ledger** | WO/WT source, source-event UTC, release/freeze minute, observation vs inference, unknowns | Was a later readback cited too early? |
| **A2 process and sensor comparison** | Intended/configured target, display/physical quantities, tags, time, calibration, approved envelope and qualified owner | Is the number actually the same physical variable? |
| **A3 authority and containment decision** | Tess approval, Emilia operator reporting, risks of shared safety feeds, banned live scan/reboot/isolation, stop trigger | Which process-safety owner authorized it? |
| **A4 forensic/source custody** | CFG-E07, LOG-REQ-46, OT-ARCH-48, HASH-50; source vs copy/derivative, missing alarm records | Does “requested” equal preserved? |
| **A5 engineering recovery record** | WT-08 fail, later WT-09 fixture status, WT-10 physical/operator gate, G1–G10 and rollback | Which exact receipt permits automatic return? |
| **A6 communication and after-action** | Clinical-style? **No**: utility public-safety status, uncertainty, operator/legal reviews, unsent/issued state and measurable corrective tasks | Does a screen mismatch become “attack” or “unsafe water” without proof? |

**Original classroom scoring:** ten criteria **0/1/2** = total **0–20**. `0` means contradicted or missing, `1` has a relevant finding with missing owner/time/evidence/limit, `2` is independently reproducible and correctly bounded from the **then-released** cards. Scores are educational, **not** NIST certification, water-quality attestation, or a test of a real process. Two reviewers independently cite the exact artifact and WT card; if the facilitator omitted a card, mark its criterion **not observed / exercise-conduct defect**, not participant zero. Reconcile disagreements by the written evidence, preserving original submissions.

| Criterion | Full two-point evidence |
|---|---|
| **C1 process/public safety** | Tess/Emilia ownership, qualified checks, emergency stop and priority before cyber containment |
| **C2 measurement distinction** | Intended versus configured target, HMI versus field property, calibration/source/time unknowns |
| **C3 incident calibration** | Observed discrepancy, fault/cache/human/cyber hypotheses without premature attacker claim |
| **C4 safe OT containment** | No intrusive scan/reboot/isolation without process approval and shared safety-path assessment |
| **C5 evidence chain** | LOG-REQ/OT-ARCH/HASH separate; coverage, source/clock/time uncertainty retained |
| **C6 authorization/history** | CFG-E07 shared role does not establish human actor; WT-07 independent state only after release |
| **C7 manual continuity** | Authorized SOP, separate operator observation, monitoring/stop trigger without recipe |
| **C8 conjunctive recovery** | ENG-A failed sensor, ENG-B bounded test and no retrospective repair |
| **C9 acceptance** | WT-10 independent physical in-envelope measures, tested sensor/actuator/alarms and operator signature |
| **C10 truthful debrief** | No invented dose, public quality claim or attribution; accountable improvements and retests |

**Noncompensable safety failures:** an actual scan, PLC reboot, subnet isolation or control write without approved process safety plan; an operational chemical instruction invented from this fiction; ignoring failed sensor/alarm gates; releasing a public "water safe" claim without its required qualified evidence; real incident data or credentials; invoking GitHub Actions or a real deploy. Stop, record **safety gate failed**, and route real emergencies to appropriate operators **regardless of paper score**. Suggested classroom-only score interpretation: **17–20** strong evidence-bound decisions, **12–16** material gaps, **0–11** substantial rework. A high score is not proof of operational readiness.

## 10. Facilitator worked answers and contrastive reasoning

**Withhold this section from participant packets until the relevant round is frozen.** The examples are defensible paths, not predetermined prescriptions. Alternatives can score well if they respect evidence, safety, role authority and independent checks without manufacturing missing observations.

| Checkpoint | Acceptable worked response, mechanism and limit | Unsupported shortcut and facilitator question |
|---|---|---|
| WT-00 | Work-order target is intent, not process fact; identify qualified owner/manual plan/dependency gaps | “Signed WO proves controller is right.” What was independently read back? |
| WT-01 | Separate displayed target mismatch and HMI-versus-field measurement disagreement; safe field assessment | “Mismatch means hacker changed chemical feed.” What direct cyber/physical evidence supports it? |
| WT-02 | One field property in range, other calibration and tag comparability open; no global safety clearance | “Local gauge is always correct.” Is its calibration/source comparable? |
| WT-03 | Accepted request tied to shared OPS-ROLE; human attribution and physical actuator effect unknown | “OPS-ROLE proves which operator did it.” Where is binding to a human? |
| WT-04 | Block broad cut/scan/reboot until Tess and OT staff assess shared alarm/permissive safety | “Cyber containment always comes first.” Which critical signals share the route? |
| WT-05 | SAFETY-35 authorization, OPER-39 manual status and READBACK-41 independent state are distinct | “Manual means public water is safe.” Where are qualified quality/physical results? |
| WT-06 | LOG-REQ-46 requested, OT-ARCH-48 acquired, HASH-50 verified specific bytes; alarm logs pending | “Hash proves controller was never tampered with.” What does it actually hash? |
| WT-07 | CFG-READ-02 independently confirms setpoint/config target differs from WO; identity/quality unknown | “Unapproved config equals confirmed attacker.” What alternatives remain? |
| WT-08 | ENG-A fails a sensor criterion; hold automatic return even if one check passes | “3 of 4 checks means safe enough.” Are gates conjunctive? |
| WT-09 | ENG-B passes bounded non-live fixture; require authorized limited real physical test and operator acceptance | “Lab green light means production safe.” Where are live measurements? |
| WT-10 | Two independent physical reads in approved envelope + scoped engineering checks + Tess approval + Emilia sign-off support narrow monitored automatic return | “Everything fixed forever.” Which subsystems and time windows were actually tested? |

### Worked answer — EX-TTX07-01

1. “HMI displayed setpoint differs from WO-218”: **observed administrative/display mismatch** (WT-00/01); request safe independent controller readback to establish actual target.
2. “Physical chemical dose definitely changed”: **unsupported**, as no actuator/flow/water-quality effect was observed (WT-01/03); require operator-authorized physical measurement and source verification.
3. “OPS-ROLE identifies the engineer”: **unsupported attribution**; shared role is not a human identity (WT-03); ask for authorized identity/change logs and corroboration.
4. “Field gauge alone proves water quality safe”: **unsupported**; unknown calibration/quantity and missing quality program (WT-02); process/quality decisions belong to trained staff.
The table should preserve each source and its negative control; no guessed chemical value is acceptable.

### Worked answer — EX-TTX07-02

**Prefer option B within Tess/Emilia's actual plant procedure**: independent safe physical observations, shared-alarm awareness, operator-authorized SOP-MAN-2 and read-only log preservation. Reject **A** now because NET-SHARED carries safety-related feeds with unverified independence; reject **C** because stale HMI is an unproved hypothesis. A defensible record explicitly leaves process safety under Tess and may require immediate emergency escalation if safe operation cannot be supported. It must name observation cadence, qualified staff and stop criteria **without offering plant operating steps**.

### Worked answer — EX-TTX07-03

`LOG-REQ-46` = requested, no acquisition; `OT-ARCH-48` = acquired read-only historian copy covering specified 08:00–08:45 source; `HASH-50` = independent byte equality for **that copy**. The alarm-path log is **pending** and HMI/controller clock alignment is **uncertain**. A perfect copy hash does not prove original source completeness, event semantics or lack of malicious action. Use restricted access and a next request rather than a claim of complete forensics.

### Worked answer — EX-TTX07-04

- **WT-08 frozen NO-GO:** one sensor gate fails; actuator/safety-alarm end-to-end tests unverified. Preserve the original failed result.
- **WT-09 new bounded candidate:** ENG-B passes a revised isolated fixture, so a qualified limited live plant acceptance **may be proposed**, but no automatic return is supported yet.
- **WT-10 new controlled acceptance:** FIELD-OBS-1/2 independently show the named comparable property within the owner's approved range, engineering checks pass for named sensor/actuator/alarms, Tess authorizes a staged return and Emilia signs as operator. The decision is **scope- and time-limited** and does not establish malicious actor, citywide safety or all quality results.
Any answer importing WT-10 to justify WT-08 is hindsight contamination.

### Worked answer — EX-TTX07-05

**Example unsent draft, for qualified review (not an issued public notice):**

> “The utility is evaluating a discrepancy between an approved process work order and information displayed by the plant control system. Trained operators are applying the utility's approved safety and contingency procedures while independent field and engineering checks are assessed. We have not established the cause of the discrepancy or its broader impact. Decisions about plant operation and public communication remain with the authorized process, water-quality and legal teams. We will issue an update when the required independent checks and approvals are recorded.”

Vida records `drafted`; Tess/Soren/Calum review scope and any applicable external-notice obligations; an authorized utility official approves; delivery and public receipt are **not supplied**. Do not state a dosing level, “attack confirmed” or a safe-water determination absent qualified evidence.

**Rubric calibration:** A participant at WT-08 says “most tests passed, resume automatic control.” One observer awards C8=1 for noting tests; another awards C8=0 because the statement **contradicts a required failed sensor gate**. Reconcile C8 to **0** for that unsafe decision, plus a **separate safety gate failed** record. WT-09 or WT-10 cannot silently revise the original submission.

## 11. Debrief, communications and improvement plan

Use 30 minutes. Ask each team to point to an artifact rather than retell an ideal story: Who actually approved WO-218, and what did it authorize? Are target setpoint, HMI process value and local measurement the same kind of number? What was known about calibrations and source clocks? Which safety feeds might be lost by blanket isolation? Was SOP-MAN-2 invoked through qualified staff rather than invented steps? What original log source was requested versus actually acquired? Did CFG-E07 attribute a human or prove physical effects? Why did ENG-A fail even though a target matched? What did ENG-B still not prove about the live process? Which WT-10 receipts permit **narrow** automatic return, and what water-quality and cyber findings remain open? Did any participant use a future card to justify a past action?

| Original exercise improvement item | Fictional owner and target interval after exercise | Falsifiable safe retest, not an actual plant operation |
|---|---|---|
| **I-01 Signed work-order/controller correspondence** | Tess + Yuna; 21 days | Paper/source review compares authorized WO revisions against qualified current configuration readbacks, with a deliberate mismatch correctly escalated |
| **I-02 Two-source physical verification readiness** | Emilia + Dante + Soren; 30 days | Independent, approved **non-live** measurement fixture includes mismatched tags/calibration; reviewer rejects comparison until resolved |
| **I-03 Shared safety network dependency mapping** | Maalik + Yuna; 30 days | Approved topology/functional review finds alarm/permissive dependencies before any proposed cut, with one unsafe isolation rejected |
| **I-04 Manual contingency and shift handoff** | Emilia + Adeline; 28 days | Operator-led, separately approved **paper rehearsal** documents manual-state authority, monitoring, stop triggers and shift handoff without dosing instructions |
| **I-05 Bounded OT source preservation** | Tarek + Kelsey; 21 days | Mock historian source/export/byte readback chain; demonstrate a missing alarm-log slice is reported unknown, not negative |
| **I-06 Conjunctive engineering return gate** | Dante + Yuna + Tess; 35 days | Two synthetic model candidates: failed sensor results in NO-GO; revised checks plus independent field/operator authorization are required for a new acceptance |
| **I-07 Evidence-limited public status** | Vida + Calum + Zora; 14 days | Compare drafts falsely declaring safe water/attack with accurate source-limited wording and qualified review receipts |

All dates and outcomes are **fictional educational proposals**, not NIST deadlines or evidence that BMWU performed remediation. The tabletop concludes when A1–A6, EX-TTX07-01 through EX-TTX07-05, observer scores, safety holds, approvals and improvement ownership are captured. The **fictional root cause and any broader public-water quality conclusions remain open** even if the limited automatic-control gate passed. No real-world readiness or legal compliance is asserted.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (April 2025, final)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — response across CSF 2.0 risk functions; not a chemical process procedure.
2. [NIST CSWP 29 — The NIST Cybersecurity Framework 2.0 (February 2024, final)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — outcome-based governance, identification, protection, detection, response and recovery.
3. [NIST SP 800-82 Rev. 3 — Guide to Operational Technology (OT) Security (September 2023, final)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — OT safety, reliability and performance constraints; an initial draft of Rev. 4 was published September 2026 but is not final.
4. [US EPA — Water Sector Cybersecurity Planning](https://www.epa.gov/cyberwater/cybersecurity-planning) — emergency/incident response planning resources and templates for water and wastewater facilities; applicability varies by actual system and jurisdiction.
5. [US EPA — Water Sector Cybersecurity Response](https://www.epa.gov/cyberwater/cybersecurity-response) — official water-sector incident response resources and reporting directions, not the source of any invented BMWU action.
6. [CISA — Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cybersecurity-performance-goals) — voluntary practices for IT/OT critical infrastructure; no universal legally binding dosing or operations rule.
7. [NIST OT Security Project and publications](https://csrc.nist.gov/Projects/operational-technology-security/publications) — identifies SP 800-82 Rev. 3 as final and Rev. 4 as draft (as of October 2026).

The setting, names, source cards, work-order references, physical test labels, scores, response choices and answer examples are **original invented educational content**. External sources are credited and paraphrased rather than copied or relicensed. Material owned by the maintainer is subject to [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md), including the CC0 dedication's third-party exceptions. No real operational setpoints, chemical instructions, malicious payloads, personal/customer data or production credentials are supplied. The case is **not** a public-water quality assessment, regulatory finding, safe-to-operate instruction, formal accreditation, or actual cyber incident.
