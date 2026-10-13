# OT, IoT and Cyber-Physical Security: Doctoral Research Methods and Thesis Practice

- Language: English (`en`); doctoral research track, two years; approximately 1,600 hours of planned study.
- Editorial state: **draft**. Chapters 1–8 of 8 have authored teaching text, exercises EX001–EX050 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: advanced researchers with research experience and a defensible question about the security of industrial control systems (ICS), operational technology (OT), the industrial Internet of Things (IIoT) or other cyber-physical systems (CPS). Entry knowledge: the content planned for the [master's](../../../../masters-2-years/ot-iot-security/en/book/PLAN.md) track in this area or equivalent experience, plus working literacy in control theory (state-space models, feedback loops), probability and statistics, and at least one industrial protocol such as Modbus or DNP3.
- Relationship to neighbouring courses: the [doctoral critical-infrastructure course](../../../critical-sector-security/README.md) studies services, sectors and cross-sector cascades; the [doctoral incident-response course](../../../incident-response-resilience/README.md) studies organizational detection and response. **This book studies the control loop itself**: sensors, actuators, controllers, the physical process, industrial protocols and the safety functions that keep people alive when everything else fails.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights.
- Educational boundary: this track is an independent educational blueprint. It is not an accredited doctoral program, grants no degree, and grants no authority to access, scan, test or study any real plant, controller, device, vendor product or person. Every plant, organization, dataset, testbed, participant and numerical result in a worked example is **synthetic** unless a sentence explicitly cites a public source. Nothing here is an operational procedure for a real facility.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the eight chapters in order; they follow the arc of one doctoral project. Chapter 1 sets the integrity and safety standards for research where an experiment can open a valve. Chapter 2 maps the frontier of OT security research and isolates an open question. Chapter 3 turns it into a falsifiable contribution. Chapter 4 replicates the baselines and pilots the procedure on a model before any testbed is touched. Chapter 5 runs the main study and validates it on an independent second testbed. Chapter 6 submits the claims to adversarial critique. Chapter 7 assembles the thesis and a tiered reproducibility archive. Chapter 8 prepares the defense, coordinated disclosure and a publication plan.

Each chapter contains learning outcomes, teaching sections, a worked example, a practical activity with offline Python 3 standard-library code, common errors and limits, numbered exercises with a 0–3 rubric, a synthesis and a **Continue studying** block. Attempt every exercise before opening the [worked results](#worked-results).

Keep five labels in every research note: **observation** (what a named instrument or source recorded), **inference** (what you conclude and under which assumptions), **claim** (what you will defend, with scope), **decision** (what someone chose because of it) and **physical consequence** (what happens to the process, equipment, people or environment). OT research goes wrong most often when a network observation is silently promoted to a claim about the physical process.

### The synthetic research corpus

The book follows one invented project, the **Setpoint Study**, which asks: *does a detector that checks physical invariants across independent sensors (a mass-balance residual with a cumulative-sum test) detect sensor-replay manipulation of a level-control loop earlier and with fewer false alarms than a fixed-band process alarm, and under which attacker capabilities does that advantage disappear?*

| Synthetic element | Role | Boundary |
|---|---|---|
| **Kestrel Water Works, Plant A** — one storage tank, one inflow pump, a flow meter, a level transmitter, a PLC and a Modbus/TCP link to a SCADA historian | Primary model context (Chapters 1, 3–5). | Invented utility; no real plant, staff or record. |
| **Testbed T2, "Harrow Process Lab"** — a university-style two-tank rig with a separate safety relay | Independent validation context (Chapters 5–6). | Invented laboratory. |
| **TankBench-21** | A synthetic "published" benchmark whose reported detection score cannot be reproduced (Chapter 4). | Invented; do not search for it. |
| Synthetic studies **S1–S8** | Fictional papers used for appraisal practice (Chapter 2). | Invented. |
| Operators **O01–O10** | Fictional control-room participants in a blinded alarm review (Chapter 5). | Invented; no human-subjects data appear. |

Lab outputs come from the fixtures printed in the text and run with Python 3 standard library only. They demonstrate methods; they are not findings about any real system.

### Source policy

Factual statements about standards, public incidents or published research link to sources the author consulted; re-verify versions before relying on them. Core references used throughout:

- NIST, [SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*](https://csrc.nist.gov/pubs/sp/800/82/r3/final) (September 2023).
- ISA, [ISA/IEC 62443 series of standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) (overview page).
- MITRE, [ATT&CK for ICS matrix](https://attack.mitre.org/matrices/ics/).
- Modbus Organization, [*Modbus Application Protocol Specification V1.1b3*](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf).
- J. Giraldo et al., ["A Survey of Physics-Based Attack Detection in Cyber-Physical Systems"](https://doi.org/10.1145/3203245), *ACM Computing Surveys* 51(4), 2018.
- D. Urbina et al., ["Limiting the Impact of Stealthy Attacks on Industrial Control Systems"](https://doi.org/10.1145/2976749.2978388), ACM CCS 2016.
- R. Sommer and V. Paxson, ["Outside the Closed World: On Using Machine Learning for Network Intrusion Detection"](https://doi.org/10.1109/SP.2010.25), IEEE S&P 2010.
- D. Arp et al., ["Dos and Don'ts of Machine Learning in Computer Security"](https://www.usenix.org/conference/usenixsecurity22/presentation/arp), USENIX Security 2022.
- E. S. Page, ["Continuous Inspection Schemes"](https://doi.org/10.1093/biomet/41.1-2.100), *Biometrika* 41, 1954 (the CUSUM test).
- U.S. DHS, [*The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research*](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) (2012).
- CISA, [Coordinated Vulnerability Disclosure Program](https://www.cisa.gov/coordinated-vulnerability-disclosure-process).
- ACM, [Artifact Review and Badging, Version 1.1](https://www.acm.org/publications/policies/artifact-review-and-badging-current).
- iTrust/SUTD, [Secure Water Treatment (SWaT) and related datasets](https://itrust.sutd.edu.sg/itrust-labs_datasets/) — described only at the level of its public page.

Generic methodological vocabulary (verification versus validation, common random numbers) is identified as such rather than given an invented citation.

## Contents

1. [Advanced research integrity and methods](#ch-01)
2. [OT, IoT and cyber-physical security: research frontier](#ch-02)
3. [Original contribution proposal](#ch-03)
4. [Baseline replication and pilot](#ch-04)
5. [Main study and independent validation](#ch-05)
6. [Peer critique and revision](#ch-06)
7. [Thesis synthesis and reproducibility archive](#ch-07)
8. [Defense and publication plan](#ch-08)
9. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes and connection

After this chapter you can: (1) explain why the physical process, not the packet, is the object of OT security research; (2) place a research claim on a ladder from network observation to physical consequence; (3) design an experiment whose worst credible outcome is bounded by an independent safety layer; (4) apply the Menlo principles to industrial research; and (5) choose detection metrics that cannot be gamed by scoring conventions. The chapter builds on your entry knowledge of research design and prepares the frontier mapping of Chapter 2.

### 1.1 The object of study: a control loop with consequences

An information system fails by disclosing, corrupting or withholding data. An industrial control system can fail in all of those ways, but its defining failure is different: a **physical process** leaves its safe envelope. A pump runs dry, a tank overflows, a chlorine dose exceeds its limit, a turbine overspeeds. NIST SP 800-82 Rev. 3 frames OT as systems that "interact with the physical environment" and stresses that safety and availability usually dominate the priority order that confidentiality leads in IT. That difference reshapes research. A detection method that flags every malicious Modbus write but cannot say whether the process was endangered has answered an IT question in an OT setting.

The doctoral researcher therefore models the loop explicitly. A **sensor** measures a process variable (level, pressure, flow). A **controller**, typically a programmable logic controller (PLC), compares it with a **setpoint** and computes a command. An **actuator** (pump, valve, breaker) changes the process. A **supervisory layer** (SCADA, HMI, historian) observes and adjusts setpoints. Beneath them all sits a **safety instrumented system (SIS)** or hard-wired interlock designed to bring the process to a safe state independently of the control system. Each element is a possible point of manipulation, and each element's honesty is something your detector either assumes or tests.

### 1.2 A ladder of claims

Write every claim on a five-rung ladder and refuse to climb a rung without evidence for it:

1. **Protocol observation** — a frame with function code 6 (write single register) reached unit 1 (the Modbus specification defines the function codes).
2. **Control inference** — the setpoint register changed from 50 to 80.
3. **Process inference** — the tank level trajectory was consistent with the new setpoint.
4. **Safety inference** — the trajectory would (or would not) cross the high-high trip within the modelled horizon.
5. **Consequence claim** — equipment damage, release or harm would (or would not) have occurred, given the independent protection layers.

Most published OT detection papers stop at rung 1 or 2 and report accuracy; most practical value lies at rungs 3–5. A thesis need not reach rung 5, but it must say where it stops.

### 1.3 Safety before integrity of results

A badly run IT experiment loses data; a badly run OT experiment can injure someone. The integrity rules of ordinary research — honest reporting, pre-registration of analyses, retention of raw data — remain, but a new rule takes precedence: **never test on production**. Experiments run on simulations, on isolated laboratory rigs whose worst case is harmless, or, exceptionally, on an operator's system under the operator's written authorization, its own safety review and a named person with stop authority. Even in a laboratory the researcher should list the worst credible physical outcome of every experiment (for example "water spills onto the floor of the rig enclosure") and the independent layer that bounds it (a mechanical float switch, not the PLC under test). If the only protection is the system you are attacking, the experiment is not bounded.

### 1.4 Ethics and dual use

The Menlo Report adapts the Belmont principles to ICT research: respect for persons, beneficence, justice, and respect for law and public interest. In OT research **beneficence** dominates: an evasion technique that defeats every published detector is a real contribution and also a recipe. The ethical response is not silence but proportion. Publish the *class* of weakness, the defensive measurement and the mitigation; withhold vendor-specific exploitation detail until coordinated disclosure (Chapter 8) has run. **Respect for persons** applies to operators you interview or observe: they may reveal unsafe practices that could cost them their jobs, so consent forms must state who sees raw notes. **Respect for law** covers export control of some industrial technologies and contractual limits on testbed data.

### 1.5 Data that describes a plant is sensitive

Network captures, PLC programs, piping and instrumentation diagrams, and alarm logs together form a map of how to hurt a facility. Treat them as sensitive even when the facility is a university rig, because rigs reuse commercial controllers and their configurations reveal product behaviour. Define tiers early: T0 public, T1 shareable under licence, T2 shareable with vetted researchers, T3 never leaves the owner. Chapter 7 turns these tiers into a release manifest.

Assign each artefact a tier when it is created, not when the thesis is written, and record the owner who can change it. A capture taken on Testbed T2 starts at T2 even if it looks harmless. Lowering a tier needs a written reason, such as removing addresses and controller identifiers, and a second person who checks the result.

### 1.6 Metrics that resist gaming

Detection research in OT has a measurement problem. Attacks in time-series datasets are long contiguous segments; a widely used scoring convention, *point adjustment*, marks a whole attack segment as detected if any single point inside it is flagged. As Lab 1 shows, it can turn a detector that finds 10% of attack points into one reporting near-perfect F1. Arp et al. list this family of pitfalls — inappropriate performance measures, base-rate neglect, lab-only evaluation — for machine learning in security generally. For OT the defensible metric set is: **event-level recall** (fraction of attack episodes detected), **time to detection** measured from attack onset, **false alarms per operator shift** (because alarm floods are themselves a safety hazard), and **physical impact at detection** (how far the process had moved when the alarm fired). The last metric is OT-specific and is the one most often omitted.

### 1.7 Worked example: the first protocol review of the Setpoint Study

The candidate's first protocol proposed replaying recorded attacks on Kestrel Plant A's live historian network "read-only". The review board raised three issues. First, *read-only is a claim, not a property*: a capture tool on a span port is passive, but a tool that polls the PLC is active and adds load to a controller with a fixed scan cycle. Second, the worst credible outcome was not stated. Third, the metric was point-adjusted F1. The revised protocol (a) moves all attack experiments to a simulation of Plant A and later to the isolated Testbed T2; (b) states the worst outcome on T2 as "upper tank overflows into the drip tray", bounded by a mechanical float valve independent of the PLC; (c) reports event recall, delay, false alarms per 8-hour shift and maximum overfill; and (d) names the laboratory manager as stop authority.

### 1.8 Practical activity — Lab 1: point adjustment inflates scores

Run this offline. It creates a 100-sample synthetic label sequence with two attack segments and a detector that flags five samples.

```python
# Lab 1 (synthetic): how "point-adjusted" scoring inflates an OT anomaly detector.
labels = [0]*20 + [1]*30 + [0]*30 + [1]*10 + [0]*10      # two attack segments (100 samples)
alarms = [0]*100
for i in (5, 40, 85, 86, 87):    # detector flagged five samples
    alarms[i] = 1
def scores(lab, pred):
    tp = sum(l and p for l, p in zip(lab, pred)); fp = sum((not l) and p for l, p in zip(lab, pred))
    fn = sum(l and not p for l, p in zip(lab, pred))
    prec = tp/(tp+fp) if tp+fp else 0.0; rec = tp/(tp+fn) if tp+fn else 0.0
    return round(prec, 3), round(rec, 3), round(2*prec*rec/(prec+rec), 3) if prec+rec else 0.0
def point_adjust(lab, pred):
    out = pred[:]; i = 0
    while i < len(lab):
        if lab[i]:
            j = i
            while j < len(lab) and lab[j]: j += 1
            if any(pred[i:j]): out[i:j] = [1]*(j-i)
            i = j
        else: i += 1
    return out
def events(lab, pred):
    segs, i = [], 0
    while i < len(lab):
        if lab[i]:
            j = i
            while j < len(lab) and lab[j]: j += 1
            segs.append((i, j)); i = j
        else: i += 1
    return sum(any(pred[a:b]) for a, b in segs), len(segs)
print("pointwise P/R/F1 :", scores(labels, alarms))
print("point-adjust     :", scores(labels, point_adjust(labels, alarms)))
print("events detected  :", events(labels, alarms))
```

Expected output:

```text
pointwise P/R/F1 : (0.8, 0.1, 0.178)
point-adjust     : (0.976, 1.0, 0.988)
events detected  : (2, 2)
```

Interpretation: both episodes were detected (event recall 1.0), which is genuinely useful, but the point-adjusted F1 of 0.988 hides that the first alarm in segment one came 20 samples after onset. Report event recall *with* delay, never point-adjusted F1 alone.

The same five alarms produce three very different stories. Pointwise, the detector found three of forty attack samples and raised two false alarms. Point-adjusted, it looks almost perfect. By events, it found both episodes, one of them late. Only the third view, paired with delay, tells an operator what would have happened at the tank, so it is the one the Setpoint Study reports.

### 1.9 Common errors and limits

- Treating a protocol anomaly as a process anomaly (rung 1 presented as rung 3).
- Calling a passive capture "safe" while running active polling tools.
- Using the PLC under test as the only safety bound in a laboratory.
- Reporting one aggregate score without false alarms per shift.
- Assuming university rigs are not sensitive because they are small.

Each error has a guard. Write the rung next to every claim in your notes. Call any tool that sends requests to a controller active, whatever it reads. Name the independent layer that bounds every laboratory run, such as the float valve on T2. Report false alarms per eight-hour shift beside recall. Tier university rig data as you would plant data.

### Exercises — chapter 1

Rubric for all exercises in this book: **3** = correct, scoped, evidence-labelled and honest about limits; **2** = correct with a minor gap in scope or evidence; **1** = partially correct or unlabelled claims; **0** = missing, unsafe or overclaiming.

- **EX001** — *Objective:* classify claims. *Input:* the statement "Our detector stops tank overflows." *Steps:* rewrite it as one claim on each of rungs 1–4 of the ladder for a Modbus setpoint attack. *Evidence:* four scoped claims. *Constraint:* no rung-5 claim without protection-layer data.
- **EX002** — *Objective:* bound an experiment. For an attack on Testbed T2's pump, state the worst credible outcome, the independent protection layer and the stop authority. *Evidence:* a three-row table.
- **EX003** — *Objective:* passive versus active. Classify five data-collection methods (span-port capture, PLC polling, historian export, engineering-workstation project upload, firmware dump) as passive or active and give one risk each.
- **EX004** — *Objective:* Menlo analysis. Apply the four principles to publishing a new evasion technique against physics-based detectors. *Evidence:* one paragraph per principle and a publication decision.
- **EX005** — *Objective:* data tiers. Assign T0–T3 to: a PLC ladder program, an anonymized alarm-count table, a network capture with IP addresses, a P&ID, a synthetic simulator. Justify each.
- **EX006** — *Objective:* metrics. Using Lab 1, compute event-level detection delay for each segment and explain why point adjustment hides it.
- **EX007** — *Objective:* protocol. Draft the ten headings of a Setpoint Study protocol including stop and abandonment conditions.

### Chapter synthesis

OT research studies control loops whose failure is physical. Climb the claim ladder only with evidence, bound every experiment with an independent safety layer, treat plant data as sensitive, and choose metrics — event recall, delay, false alarms per shift, physical impact at detection — that a scoring convention cannot inflate.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — OT, IoT and cyber-physical security: research frontier

### Learning outcomes and connection

After this chapter you can (1) organize the OT security literature into research families, (2) read standards as testable hypotheses, (3) appraise detection papers against known evaluation pitfalls, (4) use public incidents only at the level their analysts published, and (5) state a falsifiable gap. It builds on the claim ladder of Chapter 1 and feeds the proposal of Chapter 3.

### 2.1 Why the frontier is hard to see

OT security research is scattered across control engineering (fault detection, resilient control), computer security (intrusion detection, protocol analysis), safety engineering (hazard analysis, functional safety), and industrial practice (vendor white papers, government advisories). The same idea appears under different names: a control engineer's *residual-based fault detection* is a security researcher's *physics-based anomaly detection*. A scoping search must therefore use synonyms from each community and search engineering databases as well as security venues.

Keep a synonym table with a column per community and a row per idea, and update it as screening reveals new terms. Search engineering databases with the control vocabulary and security venues with the security vocabulary, then merge and deduplicate. Record which community each included study came from, so a reader can see whether the map is balanced or leans to one tradition.

### 2.2 Research families

**Architecture and segmentation.** The Purdue reference model, described in NIST SP 800-82 Rev. 3, layers enterprise (levels 4–5), operations management (3), supervisory control (2), basic control (1) and the physical process (0), with an industrial DMZ between IT and OT. ISA/IEC 62443-3-2 reframes segmentation as *zones and conduits* with target security levels. Research questions include whether segmentation designs actually reduce reachable attack paths and how cloud-connected IIoT erodes the layered model.

**Protocol security.** Classic industrial protocols such as Modbus were designed without authentication: the Modbus Application Protocol specification defines function codes and data models but no security fields. DNP3 added Secure Authentication; OPC UA includes a security model. Research studies adoption, implementation flaws and the cost of retrofitting security into deterministic networks.

**Detection.** Network-based detection models traffic; process-based (physics-based) detection models the plant. Giraldo et al. surveyed physics-based detection and found that evaluations rarely consider an adversary who knows the detector; Urbina et al. proposed measuring how much a *stealthy* attacker can move the process while staying below the detector's threshold — the impact-at-detection idea from Chapter 1.

**Safety–security co-engineering.** Hazard analysis methods (HAZOP, STPA) are being extended to adversarial causes; IEC 62443 and functional-safety standards are being aligned. Research asks how a security failure can defeat a safety function and how to certify both.

**Threat evidence.** MITRE ATT&CK for ICS catalogues adversary techniques such as *Modify Parameter*, *Spoof Reporting Message* and *Manipulation of View*, each grounded in public reporting. Public incidents — Stuxnet's manipulation of centrifuge drives while showing normal values, the 2015 Ukrainian distribution outages, and malware targeting safety instrumented systems (TRITON/TRISIS) — show that *manipulation of view*, the replay of normal values to operators, is a documented adversary goal, not a speculative one.

### 2.3 Standards as hypotheses

A standard encodes expert belief: "zones with security level 2 resist casual attackers". Treat such statements as hypotheses. A thesis can measure whether a zone design reduces reachability, whether a recommended alarm practice reduces operator overload, or whether a security level is achievable within a controller's scan-time budget. Do not cite a standard as evidence that its recommendations work; cite it as the claim you test.

Write each tested statement in the thesis as the standard puts it, then as the measurable hypothesis you derived from it, so readers can judge the translation. A null result is useful: if a recommended zone design does not reduce reachability in your topology, that says something about the design or the topology, and both are worth reporting.

### 2.4 Appraisal: what makes an OT detection paper credible

Apply Sommer and Paxson's warning — anomaly detection works poorly when the "normal" space is open and attacks are rare — and the Arp et al. checklist. Ask of every paper: Was the dataset a testbed or a plant? Were attacks generated by the same people who built the detector? Is the adversary aware of the detector? Is the threshold chosen on the test set? Is impact at detection reported? Public datasets such as iTrust's SWaT come from a real (scaled-down) water treatment testbed, which makes them valuable, but each dataset has a fixed attack set and a fixed plant; generalization claims beyond them need a second context.

### 2.5 Worked example: appraising synthetic studies S1–S8

| Study (synthetic) | Data | Adversary aware? | Threshold source | Impact reported? | Verdict |
|---|---|---|---|---|---|
| S1 | one public testbed dataset | no | test set | no | optimistic |
| S2 | simulation | yes (bounded) | validation | yes | strong but single plant |
| S3 | plant logs, no attacks | — | — | — | false-alarm study only |
| S4 | testbed | no | test set | no | point-adjusted F1 |
| S5 | simulation + testbed | partial | validation | partial | promising |
| S6 | network only | no | validation | no | rung 1 only |
| S7 | testbed, multi-sensor spoof | yes | validation | yes | shows replay+flow evasion |
| S8 | survey | — | — | — | map |

The pattern is the gap: no study combines (a) a detector-aware adversary, (b) thresholds fixed before testing, (c) impact at detection, and (d) validation on a second, independent plant.

### 2.6 Practical activity — Lab 2: code the map

Copy the table into a CSV and count, with Python's `csv` module, how many studies satisfy each criterion. Expected counts from the table: adversary aware fully = 2 (S2, S7), validation thresholds = 4 (S2, S5, S6, S7), impact reported fully = 2 (S2, S7), two contexts = 1 (S5). Change one coding decision and note how the gap statement changes; record that sensitivity in your notes.

A small change can move a study across the line. If S5's adversary awareness is coded as full rather than partial, three studies satisfy that criterion instead of two, but none yet combines all four properties, so the gap survives. Record each coding rule with an example, and ask a second coder to code the table independently before you rely on it.

### 2.7 A falsifiable gap

Weak gap: "Physics-based detection is understudied." Strong gap: "No evaluation reports both detection delay and maximum process deviation at detection for sensor-replay attacks on a level loop, with thresholds fixed in advance, on two independent plants; we predict that a mass-balance residual reduces delay relative to a band alarm, and that the advantage disappears when the attacker also controls the independent flow sensor." The strong version names the condition under which the contribution fails.

The strong gap predicts its own failure, which the Setpoint Study later confirms as class B. That prediction is what lets a committee judge the thesis fairly: if the residual detector had also caught class B, the gap would need revisiting, because a detector should not be able to see through a consistent lie on both sensors without some other independent signal.

### 2.8 Common errors and limits

Citing vendor marketing as evidence; treating ATT&CK techniques as frequencies (they are documented possibilities, not base rates); claiming novelty because of a new dataset name; describing incidents beyond what public analyses state.

A vendor paper can point to a question but cannot answer it. ATT&CK tells you that manipulation of view has been seen, not how often. A new dataset is novel only if it lets you test something you could not test before. When describing Stuxnet, Ukraine or TRITON, say what the cited analysts reported and stop there.

### Exercises — chapter 2

- **EX008** — Build a synonym table with at least four terms from control engineering and four from security for the concept "detect manipulated sensor data".
- **EX009** — Map the Setpoint Study's Plant A components to Purdue levels 0–3 and name the conduit a historian query crosses.
- **EX010** — Rewrite one IEC 62443 zone-and-conduit recommendation as a measurable hypothesis.
- **EX011** — Appraise study S4 with five questions from §2.4 and state what result it can support.
- **EX012** — Choose two ATT&CK for ICS techniques relevant to the Setpoint Study and explain why their presence in the matrix is not evidence of frequency.
- **EX013** — Run Lab 2, change S5's adversary coding to "yes", and report how the gap statement changes.
- **EX014** — Write a weak and a strong gap statement for a different OT topic (for example DNP3 Secure Authentication adoption).

### Chapter synthesis

The frontier lies across communities; read it with synonyms, treat standards as hypotheses and appraise detection papers for adversary awareness, threshold leakage, impact reporting and second-context validation. A gap is useful only when it says how it could be closed and how the closing could fail.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes and connection

After this chapter you can (1) choose the type of contribution your thesis makes, (2) express a detection mechanism as a physical invariant, (3) define an explicit attacker model, (4) state hypotheses with thresholds and rivals, and (5) predeclare the conditions under which your contribution fails. It turns the gap of Chapter 2 into a study that Chapter 4 can pilot.

### 3.1 Types of contribution

An OT security thesis can contribute a **mechanism** (a new detector or protection), a **measurement** (a way to quantify impact or exposure), an **empirical finding** (how operators or plants actually behave), or a **validated principle** (a design rule that holds across contexts). The Setpoint Study contributes a measurement-backed comparison: it does not invent the CUSUM test (Page, 1954) or residual-based detection (surveyed by Giraldo et al.); it tests when a cross-sensor invariant helps against a specific, documented adversary goal — manipulation of view — and quantifies where it stops helping. Honest positioning of this kind is a strength in a defense, not a weakness.

### 3.2 The mechanism as a physical invariant

Plant A's tank obeys a discrete mass balance: next level = level + inflow − outflow, with outflow ≈ 0.02 × level through a fixed orifice in the synthetic model (equilibrium 50 units when inflow is 1.0). A level transmitter and a flow meter measure different quantities produced by the same physics. If an attacker replays old level readings while forcing the pump, the level estimate predicted from the flow meter diverges from the reported level. The **residual** r = reported level − predicted level should be near zero under normal operation and drift away under that attack. A **CUSUM** accumulates residual magnitude above an allowance k and alarms when the sum exceeds a threshold h; it is designed to catch small persistent shifts that a fixed band misses.

The invariant has an assumption written into it: the flow meter is honest. If the attacker controls both sensors (or the PLC that reports them), the invariant can be satisfied by a consistent lie. Stating this assumption is the beginning of the attacker model.

### 3.3 Attacker model

Write the model as capabilities, knowledge and goal:

| Element | Setpoint Study assumption |
|---|---|
| Capabilities | Write access to the pump command and the level reading on the SCADA link (consistent with ATT&CK for ICS *Modify Parameter* and *Spoof Reporting Message*); **class A**: level sensor only; **class B**: level and flow sensors. |
| Knowledge | Knows the band alarm limits; for class B also knows the detector. |
| Goal | Raise the true level while keeping displayed values normal (manipulation of view). |
| Out of scope | Compromise of the mechanical float valve; physical tampering. |

### 3.4 Hypotheses and thresholds

- **H1 (detection):** against class A replay, residual CUSUM detects ≥95% of episodes with mean delay ≤ 60 steps, while the band alarm detects ≤ 10%.
- **H2 (false alarms):** on 100 nominal runs, residual CUSUM produces no more false-alarm runs than the band alarm.
- **H3 (impact):** maximum true overfill at detection is lower with CUSUM than with the band alarm.
- **H4 (failure condition):** against class B, CUSUM detection falls to ≤ 10% — the predicted boundary of the contribution.

Thresholds are justified, not decorative: 60 steps corresponds, in the synthetic time base, to the time the overfill takes to reach half of the margin to the high-high trip. H4 is a hypothesis you *want* to be able to confirm: a method whose limits are measured is more useful than one whose limits are unknown.

### 3.5 Baselines and rivals

The baselines are (a) the **band alarm** that a plant already has, (b) a **network detector** that flags any write to the level register — trivially effective if writes are rare, useless if the attacker replays at the sensor — and (c) an **oracle** with access to true level, giving the best possible delay. Rival explanations for any CUSUM advantage include threshold tuning on test data, a simulator that is too clean, and attack magnitudes chosen to suit the method. Each rival gets a test in Chapter 4 or 5.

### 3.6 Worked example and Lab 3

Lab 3 implements the model and both detectors for 100 seeded runs per condition.

```python
# Lab 3 - Setpoint Study (synthetic): fixed-band alarm vs. physics-residual CUSUM on one tank.
# Python 3 standard library only. Attack: pump forced to over-fill while the level sensor replays
# nominal values ("replay"); variant "replay+flow" also spoofs the inflow meter.
import random

def run(seed, attack, detector, steps=600, onset=300):
    rng = random.Random(seed)
    true_level, s, first_alarm, max_dev = 50.0, 0.0, None, 0.0
    est = 50.0
    for t in range(steps):
        inflow = 1.0 + rng.gauss(0, 0.05)
        if attack and t >= onset:
            inflow += 0.05                      # forced pump: hidden extra inflow
        true_level += inflow - 0.02 * true_level
        level_meas = true_level + rng.gauss(0, 0.3)
        flow_meas = inflow + rng.gauss(0, 0.02)
        if attack and t >= onset:
            level_meas = 50.0 + rng.gauss(0, 0.3)   # replayed nominal level
            if attack == "replay+flow":
                flow_meas = 1.0 + rng.gauss(0, 0.02)
        est = est + flow_meas - 0.02 * est      # mass-balance prediction from flow meter
        if detector == "band":
            hit = abs(level_meas - 50.0) > 1.5
        else:
            s = max(0.0, s + abs(level_meas - est) - 0.6)
            hit = s > 6.0
        if hit and first_alarm is None:
            first_alarm = t
        if t >= onset:
            max_dev = max(max_dev, true_level - 50.0)
    return first_alarm, max_dev

for det in ("band", "cusum"):
    fa = sum(run(k, None, det)[0] is not None for k in range(100))
    for atk in ("replay", "replay+flow"):
        res = [run(k, atk, det) for k in range(100)]
        hits = [a - 300 for a, _ in res if a is not None and a >= 300]
        delay = f"{sum(hits)/len(hits):.1f}" if hits else "n/a"
        print(f"{det:5s} {atk:11s} false_alarm_runs={fa}/100 detected={len(hits)}/100 "
              f"mean_delay={delay} worst_true_overfill={max(d for _, d in res):.2f}")
```

Expected output:

```text
band  replay      false_alarm_runs=9/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.36
band  replay+flow false_alarm_runs=9/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.26
cusum replay      false_alarm_runs=0/100 detected=100/100 mean_delay=31.8 worst_true_overfill=3.36
cusum replay+flow false_alarm_runs=0/100 detected=0/100 mean_delay=n/a worst_true_overfill=3.26
```

Reading the output against the hypotheses: H1 is supported in the model (100/100, delay 31.8 versus 0/100); H2 is supported (0 versus 9 false-alarm runs — the narrow ±1.5 band fires on noise); H4 is confirmed (class B evades completely). "Worst true overfill" is the maximum over the *whole* attack window, so H3 requires a separate measurement of overfill at the alarm time — an exercise below. All numbers are properties of a synthetic model, not of any plant.

### 3.7 Common errors and limits

Claiming a mechanism is novel when only its application is; omitting the honest-sensor assumption; choosing attack magnitudes after seeing detector behaviour; having no condition under which the hypothesis fails.

Each of these errors has a visible symptom in a proposal: a contribution sentence that claims to invent CUSUM, an attacker model without a class B, an attack gain changed after Lab 3 was run, or a hypothesis list without H4. Read the proposal for those symptoms before sending it to the committee, and fix them while the study is still cheap to change.

### Exercises — chapter 3

- **EX015** — Classify the Setpoint Study's contribution type and write a two-sentence positioning statement citing prior work.
- **EX016** — Derive the equilibrium level of the Lab 3 tank when inflow is 1.05 and explain what this means for the attacker's goal.
- **EX017** — Extend the attacker-model table with a class C attacker who controls the PLC logic itself; predict the outcome for each detector.
- **EX018** — Modify Lab 3 to record true overfill *at the alarm time* and test H3.
- **EX019** — Justify a different delay threshold for H1 using a stated high-high trip level and the overfill rate.
- **EX020** — List three rival explanations for a CUSUM advantage and the test that would rule each out.

### Chapter synthesis

A strong proposal positions itself honestly, expresses the mechanism as a physical invariant, makes the honest-sensor assumption explicit through an attacker model, and predeclares hypotheses — including the one that marks where the contribution fails.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes and connection

After this chapter you can (1) distinguish reproduction, replication and re-implementation, (2) diagnose why a published OT detection result cannot be reproduced, (3) verify a process simulator before trusting it, (4) design a bounded pilot on an isolated rig, and (5) make a predeclared go/no-go decision. It takes the hypotheses of Chapter 3 and prepares the main study of Chapter 5.

### 4.1 Terms

The ACM artifact-badging policy distinguishes **repeatability** (same team, same setup), **reproducibility** (different team, same artifacts) and **replicability** (different team, own artifacts). In OT these differ sharply because plants, controllers and datasets are rarely shareable. Fix your vocabulary before claiming any of them.

For the Setpoint Study, rerunning Lab 3 on the same code and seeds is repeatability. A colleague running the archived code is reproducibility. The TankBench-21 work is a re-implementation from the paper's description, closer to replication. Saying so precisely keeps a reviewer from reading a re-scoring as independent confirmation of the original result.

### 4.2 Diagnosing a failed reproduction: TankBench-21

The synthetic benchmark TankBench-21 reports an F1 of 0.96 for a band-plus-rate alarm. The candidate's re-implementation gets 0.31. A disciplined diagnosis lists hypotheses and tests each: (a) **scoring convention** — the paper used point adjustment (Lab 1 shows this alone can explain a gap of this size); (b) **threshold leakage** — thresholds were chosen on the test split; (c) **label alignment** — attack labels start when the attack script launched, not when the process first deviated; (d) **sampling** — the paper downsampled to 10 s, smoothing noise. Re-scoring with point adjustment yields 0.94, inside a predeclared tolerance of ±0.05, so the reproduction "succeeds" — but it succeeds in reproducing an inflated metric. The thesis records both numbers and adopts event-level recall plus delay.

### 4.3 Verifying the simulator

Verification asks whether the model is built right; validation asks whether it is the right model (standard modelling vocabulary). Verification tests for the Lab 3 tank include: equilibrium at 50.0 with nominal inflow (analytical check); mass conservation over 1,000 steps without noise; residual mean near zero under no attack; and seeds producing identical traces on two machines. A detector evaluated on an unverified simulator is evaluated on an unknown system.

Write each verification test as code that fails loudly, and run the suite before every batch of experiments. If the equilibrium check fails after a change to the outflow term, no detector result from that version is usable until it passes. Keep the test output with the run records so an examiner can see that verification preceded the results it supports.

### 4.4 Tuning without leakage: Lab 6

The CUSUM has two parameters, allowance k and threshold h. Tune them on separate seeds from the evaluation seeds and examine robustness to model error. Lab 6 sweeps k and adds a constant 0.4-unit level-sensor calibration bias — a realistic mismatch between model and instrument.

```python
# Lab 6 (synthetic): CUSUM drift k vs. false alarms and detection delay - the tuning trade-off reviewers ask about.
import random
def first_alarm(seed, attack, k, h=6.0, steps=600, onset=300, bias=0.0):
    rng = random.Random(seed); true, est, s = 50.0, 50.0, 0.0
    for t in range(steps):
        inflow = 1.0 + rng.gauss(0, 0.05) + (0.05 if attack and t >= onset else 0.0)
        true += inflow - 0.02*true
        lvl = true + rng.gauss(0, 0.3) + bias
        if attack and t >= onset: lvl = 50.0 + rng.gauss(0, 0.3) + bias
        est += inflow + rng.gauss(0, 0.02) - 0.02*est
        s = max(0.0, s + abs(lvl - est) - k)
        if s > h: return t
    return None
for bias in (0.0, 0.4):
    for k in (0.4, 0.6, 0.8, 1.0):
        fa = sum(first_alarm(i, False, k, bias=bias) is not None for i in range(100))
        d = [a-300 for a in (first_alarm(i, True, k, bias=bias) for i in range(100)) if a is not None and a >= 300]
        print(f"bias={bias} k={k} false_alarm_runs={fa}/100 detected={len(d)}/100 mean_delay={sum(d)/len(d) if d else float('nan'):.1f}")
```

Expected output:

```text
bias=0.0 k=0.4 false_alarm_runs=0/100 detected=100/100 mean_delay=25.6
bias=0.0 k=0.6 false_alarm_runs=0/100 detected=100/100 mean_delay=30.9
bias=0.0 k=0.8 false_alarm_runs=0/100 detected=100/100 mean_delay=38.0
bias=0.0 k=1.0 false_alarm_runs=0/100 detected=100/100 mean_delay=46.1
bias=0.4 k=0.4 false_alarm_runs=97/100 detected=19/100 mean_delay=35.4
bias=0.4 k=0.6 false_alarm_runs=4/100 detected=99/100 mean_delay=46.1
bias=0.4 k=0.8 false_alarm_runs=0/100 detected=100/100 mean_delay=55.6
bias=0.4 k=1.0 false_alarm_runs=0/100 detected=100/100 mean_delay=66.5
```

With a perfect model the smallest k looks best. A small calibration bias makes k = 0.4 useless: 97 runs alarm before the attack starts, and only 19 alarms land after onset. The defensible choice is k = 0.8, which trades about 7 steps of delay (versus k = 0.6 without bias) for robustness. This is the kind of result reviewers expect to see *before* the main study.

### 4.5 A bounded pilot on Testbed T2

The pilot answers feasibility questions only: can the rig run the replay scenario safely, can the historian log at 1 Hz, and does the float valve stop overflow? Pilot data are not used for hypothesis tests. Go/no-go criteria are written in advance: go if three consecutive runs complete with the float valve never reached, log loss below 1%, and no unplanned controller restart; otherwise revise. The pilot plan also records who may stop a run and how (a physical emergency stop that cuts pump power, independent of the PLC).

### 4.6 Common errors and limits

Calling a re-scoring a replication; trusting a simulator because it "looks right"; tuning on evaluation seeds; using pilot data to test hypotheses; lacking an independent emergency stop.

Each error lets a result look better than it is. A re-scoring with point adjustment only confirms that the original convention was used. A plausible-looking trace is not a passed verification test. Seeds shared between tuning and evaluation leak information. Pilot runs answer feasibility, not hypotheses. And without a physical stop that cuts pump power independently of the PLC, the pilot is not bounded.

### Exercises — chapter 4

- **EX021** — Classify three activities (rerunning your own Lab 3, a colleague running your archive, a colleague building their own tank model) under ACM terms.
- **EX022** — Write a reproduction log entry for TankBench-21 with the four hypotheses, tests and outcomes.
- **EX023** — Write and run a verification test for mass conservation in the noise-free Lab 3 model.
- **EX024** — Using Lab 6, choose k for a plant where calibration bias up to 0.4 is expected and justify it with two numbers.
- **EX025** — Write go/no-go criteria for a T2 pilot including a safety criterion and a data-quality criterion.
- **EX026** — Explain why the reproduced 0.94 is not evidence that the TankBench-21 detector is good.

### Chapter synthesis

Reproduce baselines with a predeclared tolerance and diagnose gaps systematically; verify the simulator; tune on separate seeds and stress-test against model error; and pilot only for feasibility with independent physical stop authority.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes and connection

After this chapter you can (1) design a paired experiment with common random numbers, (2) report uncertainty that separates simulation noise from model uncertainty, (3) validate on an independent second context, (4) incorporate a blinded operator review, and (5) write an honest results paragraph including mixed results. It executes the plan piloted in Chapter 4 and produces the claims Chapter 6 will attack.

### 5.1 Paired design

When comparing two detector settings, run both on the **same** random seeds (common random numbers, a standard simulation technique). The difference per seed removes shared noise and narrows confidence intervals. Lab 5 compares k = 0.8 with k = 0.6 on two plant variants: Plant A with an attack inflow gain of 0.05 and Plant B, a larger tank where the same pump manipulation produces only 0.02 units per step.

```python
# Lab 5 (synthetic): paired comparison of detection delay on two plant models with common random numbers + bootstrap CI.
import random
def delay(seed, k, gain):
    rng = random.Random(seed); true, est, s = 50.0, 50.0, 0.0
    for t in range(700):
        inflow = 1.0 + rng.gauss(0, 0.05) + (gain if t >= 300 else 0.0)
        true += inflow - 0.02*true
        lvl = 50.0 + rng.gauss(0, 0.3) if t >= 300 else true + rng.gauss(0, 0.3)
        est += inflow + rng.gauss(0, 0.02) - 0.02*est
        s = max(0.0, s + abs(lvl - est) - k)
        if s > 6.0 and t >= 300: return t - 300
    return 400
for plant, gain in (("A", 0.05), ("B", 0.02)):
    diffs = [delay(i, 0.8, gain) - delay(i, 0.6, gain) for i in range(200)]
    rng = random.Random(7); boots = sorted(sum(rng.choice(diffs) for _ in diffs)/len(diffs) for _ in range(2000))
    print(f"plant {plant}: mean delay(k=0.8)-delay(k=0.6)={sum(diffs)/len(diffs):.1f} steps, 95% CI [{boots[50]:.1f}, {boots[1949]:.1f}]")
```

Expected output:

```text
plant A: mean delay(k=0.8)-delay(k=0.6)=6.9 steps, 95% CI [6.5, 7.4]
plant B: mean delay(k=0.8)-delay(k=0.6)=45.4 steps, 95% CI [38.4, 53.0]
```

The robustness chosen in Chapter 4 costs about 7 steps on Plant A but about 45 steps on Plant B, where the attack signal is weaker. Undetected runs are capped at 400 steps (right-censoring); the Plant B mean is therefore a lower bound on the true cost. The bootstrap interval describes simulation noise only — it says nothing about whether the tank model represents any real plant.

### 5.2 Three kinds of uncertainty

Separate **stochastic** uncertainty (seed-to-seed variation, captured by the interval), **parametric** uncertainty (orifice coefficient, noise levels, calibration bias — explored by sensitivity analysis as in Lab 6) and **structural** uncertainty (is a single-tank mass balance the right model at all?). Only the second testbed addresses the third.

In the Setpoint Study the interval in Lab 5 covers only the first kind. Lab 6 covers part of the second, through calibration bias and allowance. Testbed T2 is the first evidence on the third, and its lower recall shows that the model's honest, lag-free flow meter was too simple. Report each kind in its own place so readers do not mistake one for another.

### 5.3 Independent validation on Testbed T2

T2 differs from the Plant A model in ways that matter: two coupled tanks, a different flow meter with its own lag, and a PLC scan cycle of 100 ms. Thresholds are frozen from Plant A tuning before any T2 data are examined — the validation would otherwise be another tuning exercise. Synthetic T2 results: class A replay detected in 18 of 20 episodes (two missed because the flow-meter lag hid small manipulations), median delay longer than in simulation, zero false alarms over 40 nominal hours, and class B evasion confirmed in all 10 trials. The study thus supports H1 with a qualification (lower recall on a laggy instrument) and confirms H4.

### 5.4 The blinded operator review

Ten synthetic operators (O01–O10) reviewed alarm timelines without knowing which detector produced them. Eight preferred the CUSUM alarm because it arrived with a residual trend they could interpret; two found a "residual" abstract and wanted the predicted level shown on the HMI. The finding is about interpretability, not detection accuracy, and it changes the design: the thesis recommends displaying predicted versus reported level.

Ten participants cannot support a statistical claim about operator populations, and the study does not make one. The review shows that interpretability is a design concern worth measuring with real consenting control-room staff later. Record the protocol, the blinding method and each operator's stated reason, so the recommendation can be traced to what was said rather than to a count.

### 5.5 Writing mixed results honestly

"In the synthetic Plant A model and on the synthetic Testbed T2, a mass-balance residual CUSUM detected class A sensor-replay attacks that a ±1.5 band alarm missed, with no false-alarm runs in nominal operation. Recall fell from 100% in simulation to 90% on T2 owing to flow-meter lag. Robustness to a 0.4-unit calibration bias required a larger allowance, which lengthened detection delay by about 7 steps on Plant A and at least 45 on the weaker-signal Plant B. When the attacker also controlled the flow meter (class B), detection failed in every trial, as predicted."

### 5.6 Common errors and limits

Independent seeds for paired comparisons; tuning on the validation testbed; hiding censored runs; presenting intervals as real-world uncertainty; omitting the failure condition from the abstract.

Each item has a concrete check in this study: Lab 5 uses common random numbers, T2 thresholds are frozen from Plant A tuning, capped runs are reported as censored at 400 steps, the bootstrap interval is labelled simulation noise, and the abstract states that class B evaded detection in every trial. A reviewer should be able to confirm each check from the archive.

### Exercises — chapter 5

- **EX027** — Rerun Lab 5 with independent seeds for the two settings and compare interval widths with the paired version.
- **EX028** — Classify six sources of uncertainty in the Setpoint Study as stochastic, parametric or structural.
- **EX029** — Write the freeze rule for thresholds before T2 validation and explain what would invalidate the validation.
- **EX030** — Explain how right-censoring biases the Plant B mean and propose a better summary.
- **EX031** — Turn the operator-review finding into one design recommendation and one limitation.
- **EX032** — Write a 120-word results paragraph for a study where H1 failed on T2.

### Chapter synthesis

Paired designs sharpen comparisons; uncertainty has three kinds and intervals capture only one; validation means frozen thresholds on an independent context; and an honest results paragraph carries its qualifications and its failure condition.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes and connection

After this chapter you can (1) organize an internal red-team review of your own claims, (2) convert objections into testable hypotheses, (3) characterize boundary conditions instead of hiding them, (4) perform a dual-use review of a paper before submission, and (5) write a responsive reviewer letter. It attacks the results of Chapter 5 and feeds the thesis argument of Chapter 7.

### 6.1 Objections as hypotheses

Invite two colleagues — ideally a control engineer and an offensive security researcher — to attack the claims. Record each objection as a hypothesis with a test:

| Objection (red team) | Hypothesis | Test | Outcome (synthetic) |
|---|---|---|---|
| "Your attacker is naive: a smart attacker ramps slowly." | A slow ramp below the CUSUM allowance evades detection while still overfilling. | Sweep attack gain from 0.005 to 0.05. | Gain 0.005 is detected in only 14/100 runs and 0.01 in 55/100, but worst overfill in the 300-step window stays at 1.12 and 1.37 units, against 3.36 at gain 0.05 — the impact-bounding argument of Urbina et al. |
| "The flow meter is just another PLC input." | If the meter is wired to the same PLC as the level sensor, class B is as easy as class A. | Inspect T2 wiring and Plant A design. | On T2 both pass through one PLC; the honest-sensor assumption holds only for a separately wired meter. |
| "Operators would notice the pump running." | Pump-state display reveals attack. | Review HMI design. | Only if pump state comes from an independent contact, not from the commanded value. |
| "Results depend on noise level." | Higher sensor noise raises false alarms at fixed k. | Lab 6 with noise doubled. | Requires retuning; reported as parametric sensitivity. |

The second objection is the most important: it reveals that the defense's strength is an **architectural** property (independent sensing paths), not an algorithmic one. The thesis claim is revised accordingly.

### 6.2 Boundary conditions

A good thesis maps where the method works. For the Setpoint Study the boundaries are: (1) an independent second measurement of the same physics must exist and be outside the attacker's control; (2) the model error must be smaller than the attack signal; (3) attacks slower than the allowance can evade, but their impact within a stated horizon is bounded (in the model, ≤1.37 units of overfill in 300 steps for gains ≤0.01). These are stated in the abstract, not buried in a limitations section.

Each boundary should be stated with the evidence that measures it: the T2 wiring inspection for the first, the calibration-bias sweep in Lab 6 for the second, and the attack-gain sweep from the red-team review for the third.

### 6.3 The narrowed claim

Before: "Physics-based CUSUM detects sensor manipulation in water plants." After: "Where an independently wired sensor measures a quantity linked by a known mass balance, a residual CUSUM with allowance tuned for expected calibration error detects single-sensor replay attacks that band alarms miss, and bounds the overfill achievable by slower attacks; it provides no protection when the attacker controls both sensing paths." The narrowed claim is weaker in reach and much stronger in evidence.

Keep the before and after versions in the thesis, so readers see how critique changed the argument. Check every later sentence against the narrowed claim: an abstract or conclusion that drifts back toward water plants in general undoes the work. The narrowed claim also gives operators a direct test of their own site: is the second measurement independently wired?

### 6.4 Dual-use review

Before submission ask: Does the paper give a recipe for the class B evasion against a named product? (No: it describes the capability class, which is already documented as manipulation of view.) Does it reveal T2's configuration? (Only generic structure.) Would a defender gain more than an attacker? (Yes: the architectural recommendation — independent sensing paths — is actionable for defenders and well known to capable attackers.) Record the answers in the thesis appendix.

Ask one reviewer outside the project to answer the same questions without seeing your answers, and record any disagreement and how it was resolved. If later work finds a flaw specific to a product, such as a PLC accepting writes it should refuse, the review is repeated and disclosure is handled under the coordinated process before publication.

### 6.5 Responding to reviewers

Answer every point, quote it, state what changed and where, and disagree with evidence where you must. Example: "Reviewer 2 states that CUSUM is not novel. We agree and have revised §1 to position the contribution as a measurement of when cross-sensor invariants help against manipulation of view, citing Page (1954) and Giraldo et al. (2018). The new contribution statement is on p. 3."

Keep a table with one row per reviewer point: the quotation, your response, the change made and its location. Where you disagree, cite the measured result, such as class B evading in every trial, rather than restating your opinion. Send the table with the revised manuscript so the editor can check every change.

### 6.6 Common errors and limits

Defending instead of testing; hiding the class B failure; claiming generality across plants after two contexts; responding to reviewers without stating changes.

Each error turns critique into defence. Treat each objection as a hypothesis with a test. Put class B in the abstract. Limit generality to the two contexts measured, the Plant A model and Testbed T2. In reviewer letters, state what changed and where, so a reader can verify the revision instead of trusting the claim. Keep the objections table in the thesis.

### Exercises — chapter 6

- **EX033** — Turn the objection "your threshold is overfitted" into a hypothesis and a test.
- **EX034** — Modify Lab 3 to sweep attack gain (0.005, 0.01, 0.02, 0.05) for CUSUM and report detection and worst overfill.
- **EX035** — Write the boundary-condition paragraph for the abstract in ≤ 80 words.
- **EX036** — Rewrite the claim "the method secures water utilities" as a narrowed claim.
- **EX037** — Conduct a dual-use review for publishing the exact flow-meter spoofing sequence used on T2.
- **EX038** — Write a reviewer response to "Testbed results are not representative of real plants."

### Chapter synthesis

Critique is data: convert objections into tests, let them narrow the claim, publish boundary conditions prominently, and review dual-use before submission. The most valuable objection here turned an algorithmic claim into an architectural one.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes and connection

After this chapter you can (1) map the thesis argument from evidence to claim, (2) choose a thesis format, (3) build a tiered, hash-checked archive that fails closed, (4) document synthetic data and models, and (5) write limitations that say which direction each bias pushes. It assembles Chapters 1–6 and prepares the defense.

### 7.1 Argument map

Use a Toulmin structure: **claim** (narrowed claim of §6.3), **data** (Lab 3, Lab 5, T2 results), **warrant** (the mass balance links flow and level; an attacker controlling only one cannot keep both consistent), **backing** (verification tests, Page's CUSUM properties), **qualifier** ("in two synthetic contexts"), **rebuttal** (class B, slow ramps, laggy instruments). Each element points to a chapter and an artifact.

Draw the map as one page and check each arrow: does the cited data actually support the warrant, and does the rebuttal list every boundary from the critique chapter? An element with no artefact behind it is a gap to close before the defense. Keep the map current as wording changes, because examiners often ask how a single sentence connects to the evidence.

### 7.2 Format

A monograph suits a single integrated argument; a publication-based thesis suits independent papers with a linking chapter. Either way, the reproducibility archive belongs to the thesis, not to one paper.

For the Setpoint Study a publication-based thesis maps naturally onto the three planned papers, with the linking chapter carrying the narrowed claim and the boundary conditions. A monograph would place the same material in one continuous argument. Choose with your committee early, because the choice changes how much repetition is acceptable and how co-authored work is credited.

### 7.3 Tiered archive

OT artifacts carry different risks. Code and the synthetic simulator are T0 (public). Synthetic traces are T1. Testbed configurations are T2 (vetted researchers). Plant-derived maps are T3 and never released. A release must **fail closed**: if any file's hash differs from the manifest, nothing is released; files above the release tier are excluded automatically. Lab 7 demonstrates this logic.

```python
# Lab 7: fail-closed reproducibility manifest check (stdlib). Creates synthetic files in ./archive_demo.
import hashlib, json, os
os.makedirs("archive_demo", exist_ok=True)
files = {"lab3.py": "print('model')\n", "traces_T1.csv": "t,level\n0,50.0\n", "plant_map_T3.txt": "RESTRICTED\n"}
for n, c in files.items():
    open(os.path.join("archive_demo", n), "w").write(c)
manifest = [{"path": n, "tier": "T3" if n.startswith("plant_map") else "T1",
             "sha256": hashlib.sha256(c.encode()).hexdigest()} for n, c in files.items()]
manifest[1]["sha256"] = "0"*64          # simulate a stale hash after an edit
def check(release_tier_max="T1"):
    ok = True
    for e in manifest:
        h = hashlib.sha256(open(os.path.join("archive_demo", e["path"]), "rb").read()).hexdigest()
        if e["tier"] > release_tier_max:
            print("EXCLUDE (tier)", e["path"], e["tier"]); continue
        if h != e["sha256"]:
            print("FAIL (hash)   ", e["path"]); ok = False
        else:
            print("OK            ", e["path"])
    return ok
print("release allowed:", check())
```

Expected output:

```text
OK             lab3.py
FAIL (hash)    traces_T1.csv
EXCLUDE (tier) plant_map_T3.txt T3
release allowed: False
```

The stale hash blocks the release, and the T3 file is never considered. The comparison `e["tier"] > release_tier_max` works because tier names sort lexically T0 < T1 < T2 < T3 — a convenience that would break with a tier named "T10", which is noted in the archive's README.

### 7.4 Documenting synthetic data and models

State for each synthetic dataset whether it is **invented** (parameters chosen for teaching) or **calibrated** (fitted to a real system's statistics). The Setpoint Study's tank is invented. Record parameters, seeds, generator code version and the intended use; warn against using it to make claims about real plants.

Write this documentation as a short data sheet stored with the generator code, and include the equilibrium, the orifice coefficient of 0.02, the noise levels and the attack gains. Name the labs that used each configuration. Anyone reusing the traces should see at once that they describe a teaching model, not measurements from Kestrel or any other plant.

### 7.5 Directional limitations

A useful limitations table states the direction of each bias: noise-free flow meter in simulation (*overstates* recall — confirmed by T2), single-loop model (*unknown* direction for multi-loop plants), synthetic operators (*unknown*), testbed scale (*likely overstates* signal-to-noise), censoring at 400 steps (*understates* Plant B delay cost).

The direction matters because it tells a reader how to adjust confidence. If a bias overstates recall, the real-world figure is likely lower; if it is unknown, the reader should not assume either way. Keep the table beside the results rather than at the end, and update it when new evidence, such as T2's lower recall, settles a direction.

### 7.6 Common errors and limits

Archives that release everything or nothing; manifests not checked; calling invented data "realistic"; limitations without direction.

An archive that releases everything leaks plant-level detail; one that releases nothing cannot be checked. A manifest that is never verified gives false comfort, which is why Lab 7 fails closed. Synthetic data should be called invented or calibrated, never realistic. And every limitation should say whether it pushes results up, down or in an unknown direction. Run the manifest check on the release copy, never only on the working directory.

### Exercises — chapter 7

- **EX039** — Draw (as a table) the Toulmin map of the narrowed claim with chapter references.
- **EX040** — Fix Lab 7 so tiers compare numerically and add a T10 test case.
- **EX041** — Assign tiers to eight Setpoint Study artifacts and justify two borderline choices.
- **EX042** — Write a dataset card for the Lab 3 simulator (purpose, parameters, invented/calibrated, prohibited uses).
- **EX043** — Add two rows to the directional limitations table.
- **EX044** — Argue for monograph or publication-based format for the Setpoint Study.

### Chapter synthesis

The thesis is an argument whose every element points to evidence; the archive releases only what is safe and verified, failing closed; synthetic data are labelled as invented or calibrated; and limitations say which way they bias the result.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes and connection

After this chapter you can (1) audit a claim register before the defense, (2) prepare for examiner question families, (3) sequence publications, (4) route product vulnerabilities through coordinated disclosure, and (5) translate findings for operators and standards bodies. It completes the project begun in Chapter 1.

### 8.1 Claim-register audit

Every claim in the thesis needs evidence, scope and a falsifier, and must avoid overreach wording. Lab 8 automates the first pass.

```python
# Lab 8: audit a thesis claim register (synthetic). Every claim needs evidence, scope and a falsifier.
claims = [
 {"id": "C1", "text": "Residual CUSUM detects replay on Plant A tank model", "evidence": "Lab3 100/100", "scope": "simulated tank, single-sensor replay", "falsifier": "replay+flow"},
 {"id": "C2", "text": "Method secures water utilities", "evidence": "", "scope": "", "falsifier": ""},
 {"id": "C3", "text": "Band alarms miss replay", "evidence": "Lab3 0/100", "scope": "band +/-1.5", "falsifier": ""},
 {"id": "C4", "text": "Detection holds on testbed T2", "evidence": "Ch5 table 5.2", "scope": "T2, class A replay", "falsifier": "class B: flow meter also spoofed"},
]
overreach = ("secures", "prevents all", "guarantees", "real-world")
for c in claims:
    issues = [f for f in ("evidence", "scope", "falsifier") if not c[f]]
    if any(w in c["text"].lower() for w in overreach): issues.append("overreach wording")
    print(c["id"], "PASS" if not issues else "REVISE: " + ", ".join(issues))
```

Expected output:

```text
C1 PASS
C2 REVISE: evidence, scope, falsifier, overreach wording
C3 REVISE: falsifier
C4 PASS
```

C2 must be deleted or narrowed; C3 needs a falsifier (for example "a band narrow enough to catch replay would exceed the shift false-alarm budget"). A keyword list is a crude check; the human audit still reads every claim.

The keyword list in Lab 8 is deliberately short, so passing it proves little. A human audit should still read C4 against the T2 results: its scope is class A replay because class B evaded detection on T2, and the 18 of 20 recall belongs beside the claim, not only in the results chapter. Repeat the audit after every revision of the abstract or conclusion, and keep each run's output in the claim register's history so examiners can see how the claims narrowed.

### 8.2 Examiner question families

Prepare answers for: **positioning** ("what is new beyond Page and Giraldo?"), **validity** ("why should a testbed generalize?"), **adversary** ("what does a stronger attacker do?"), **safety** ("how did you bound T2 experiments?"), **ethics** ("what did you withhold and why?"), and **impact** ("what should an operator change on Monday?"). The answer to the last is architectural: provide an independently wired second measurement of key process quantities and display predicted versus reported values.

Rehearse each family aloud with a colleague who interrupts, and keep a sheet with a short answer and a pointer to the figure or table that supports it. When you do not know, say what evidence would answer the question and what you actually have. Answer the question asked, then stop.

### 8.3 Publication sequencing

Paper 1: the evaluation-methodology contribution (impact-at-detection and event metrics, with the TankBench-21-style reproduction lesson told generically). Paper 2: the Setpoint Study comparison with boundary conditions. Paper 3: the operator interpretability finding with human-factors collaborators. Release the T0/T1 archive with Paper 2.

Plan each paper so that it does not contradict the thesis or the other papers, and record which claims and figures each one reuses. If the operator paper is delayed by human-factors review, the other two can still appear; the archive is released with Paper 2 because that is the paper whose numbers it reproduces. Agree authorship with collaborators before writing begins.

### 8.4 Coordinated disclosure

If the research reveals a vulnerability in a commercial product — for example a PLC accepting unauthenticated writes to a register that should be read-only — report it to the vendor and, where appropriate, to a coordinator such as CISA's coordinated vulnerability disclosure program, agree a timeline, and publish technical detail only after mitigations are available. A design property documented in a public specification (Modbus lacking authentication) is not a vulnerability disclosure; an implementation flaw is.

Record the disclosure timeline in the thesis appendix with dates for first contact, vendor acknowledgment and publication. If the vendor does not respond, follow the coordinator's process rather than publishing early. The thesis can still describe the class of weakness while withholding product names and steps until mitigations exist.

### 8.5 Translation for practice

Write a two-page brief for operators with confidence levels: "High confidence (model + testbed): band alarms alone do not detect replayed level readings. Medium confidence (two contexts): an independent flow measurement plus a residual check detects single-sensor replay. No protection: if one device or PLC controls both measurements." Suggest to standards working groups that independent measurement paths be considered when assessing zone security levels — as a proposal, not as a finding of compliance.

Test the brief with one or two operators before release: can they say what to check on Monday? If they cannot, the confidence levels or the recommendation need rewording. Keep the brief consistent with the narrowed claim, and do not let a shorter format drop the case where one device controls both measurements.

### 8.6 Post-doctoral program

Extend to multi-loop plants, test calibrated rather than invented models, measure operator response time with real (consenting) control-room staff, and study class C attackers who modify PLC logic.

Each extension tests one boundary the thesis measured but could not cross. Multi-loop plants test whether residuals stay interpretable when loops interact. Calibrated models test whether invented parameters overstated separation. Real operators test interpretability at scale. Class C attackers, who can rewrite controller logic, test whether any invariant survives when the controller itself lies; the same safety bounds and ethics review apply to all four.

### Exercises — chapter 8

- **EX045** — Audit three claims from your own Chapter 5 results paragraph using Lab 8's criteria.
- **EX046** — Write model answers to the positioning and safety examiner questions.
- **EX047** — Sequence three papers with venues of the right type (security, control, human factors) and justify order.
- **EX048** — Decide whether each of three findings is a disclosure case: Modbus lacks authentication; a PLC firmware accepts writes to a protected register; T2's PLC shares wiring for both sensors.
- **EX049** — Write the operator brief's three confidence statements for a study where class B was not tested.
- **EX050** — Outline a two-year post-doctoral program with two falsifiable hypotheses.

### Chapter synthesis

Audit every claim, prepare for the six question families, publish in an order that builds credibility, disclose implementation flaws through coordination, and translate findings with explicit confidence. The doctoral contribution is a measured method *and* its measured limits.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course: Critical infrastructure and sector security, doctoral (course 207) →](../../../critical-sector-security/en/SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Each answer shows one defensible response; the rubric (§1.9) rewards alternatives that meet the same standard of evidence, scope and honesty. All numbers are from the synthetic labs.

### Chapter 1

- **EX001** — Rung 1: "A Modbus write (function code 6) to holding register 40001 on unit 1 was observed." Rung 2: "The level setpoint changed from 50 to 80." Rung 3: "The level trajectory rose toward 80, consistent with the new setpoint." Rung 4: "In the model the trajectory would cross the high-high trip at t+420 s absent intervention." Rung 5 is withheld: no data on the mechanical relief layer. "Stops overflows" is replaced by "raised an alarm N s before the modelled trip".
- **EX002** — Worst outcome: upper tank overflows into the drip tray (≈2 L water). Independent layer: mechanical float valve closing the inlet, plus drip tray sized for 10 L. Stop authority: named lab manager with a physical e-stop cutting pump power. Rubric: a PLC interlock as the only layer scores ≤1.
- **EX003** — Span capture: passive; risk = sensitive data at rest. PLC polling: active; adds load to scan cycle. Historian export: passive to the PLC but active on the historian; risk = server load and data volume. Project upload from engineering workstation: active; can trigger controller mode changes on some products. Firmware dump: active and potentially disruptive; may require stopping the controller.
- **EX004** — Respect for persons: no humans directly; vendors' customers are indirectly affected. Beneficence: defenders learn to require independent sensing; attackers gain little beyond documented manipulation-of-view tactics if product-specific steps are withheld. Justice: small utilities, least able to patch, bear risk — publish low-cost mitigations. Law/public interest: check disclosure obligations and export rules. Decision: publish the capability class and defence; withhold product-specific sequences until coordinated disclosure completes.
- **EX005** — Ladder program: T2/T3 (reveals logic and safety interlocks). Anonymized alarm counts: T1. Capture with IPs: T2 (topology). P&ID: T3 for real plants, T2 for a rig. Synthetic simulator: T0.
- **EX006** — Segment 1 starts at index 20; first alarm at 40 → delay 20 samples. Segment 2 starts at 80; first alarm at 85 → delay 5. Point adjustment credits all 30 and 10 points as detected, hiding the 20-sample delay during which the process moved.
- **EX007** — Title and question; background and gap; hypotheses H1–H4; attacker model; systems (simulator, T2) and safety bounds; data tiers and handling; metrics; analysis plan with frozen thresholds; stop conditions (float valve reached, unplanned restart, log loss >1%) and abandonment conditions (T2 cannot be made safe; simulator fails verification); ethics and disclosure plan.

### Chapter 2

- **EX008** — Control: fault detection and isolation, residual generation, analytical redundancy, observer-based monitoring, sensor validation. Security: false data injection, sensor spoofing, manipulation of view, replay attack, physics-based anomaly detection.
- **EX009** — Level 0: tank, pump, level transmitter, flow meter. Level 1: PLC. Level 2: SCADA/HMI. Level 3: historian (operations). A historian query from the enterprise crosses the IT/OT DMZ conduit (level 3.5) and the level 3–2 conduit.
- **EX010** — "Zones between level 2 and level 1 with a conduit limited to read function codes reduce the number of hosts able to issue Modbus writes to PLCs by ≥90% compared with a flat network, measured by reachability analysis of the synthetic topology."
- **EX011** — S4: testbed data; adversary unaware; threshold on test set; no impact; point-adjusted F1. It supports at most "the detector flags some samples within these attack segments on this testbed"; not generalization, delay or impact claims.
- **EX012** — *Spoof Reporting Message* and *Modify Parameter*. The matrix documents that adversaries have used or could use a technique, grounded in public reports; it does not count occurrences across all plants, so it gives no base rate.
- **EX013** — Adversary-aware count becomes 3 (S2, S5, S7). The gap statement must drop "no study has a detector-aware adversary" and keep the combination gap (aware + frozen thresholds + impact + two contexts), which still no single study satisfies — S5 reports impact only partially.
- **EX014** — Weak: "DNP3-SA is rarely used." Strong: "No measurement reports the proportion of DNP3 outstations in a defined public sample that negotiate Secure Authentication, nor the latency it adds on serial links; we predict adoption below 10% and latency above the polling budget on 9.6 kbit/s links, and would be refuted by adoption above 30%."

### Chapter 3

- **EX015** — Contribution type: measurement-backed comparison with characterized limits. "We do not propose a new detector; building on CUSUM (Page, 1954) and residual-based detection (Giraldo et al., 2018), we measure when a cross-sensor mass-balance invariant detects manipulation of view, and the attacker capability at which it fails."
- **EX016** — Equilibrium L* = inflow/0.02 = 1.05/0.02 = 52.5 units. A persistent 0.05 extra inflow raises the level by only 2.5 units at steady state; the attacker needs larger forcing (or a blocked outlet) to reach a trip, which affects which gains are realistic in Chapter 6.
- **EX017** — Class C modifies PLC logic, so it can forge both reported values consistently and suppress alarms computed in the PLC. Band alarm: evaded. CUSUM in the PLC: evaded. CUSUM computed outside the PLC on independently wired sensors: still detects. Conclusion: detector placement matters as much as algorithm.
- **EX018** — Recording `true_level − 50` at the first alarm gives, for CUSUM and gain 0.05, a mean overfill of 1.22 units and a maximum of 1.60 at alarm time; the band alarm never fires after onset, so its overfill grows to the window maximum of 3.36. H3 is supported in the model.
- **EX019** — Suppose the high-high trip is at 56 (margin 6) and the attack drives level up at up to ≈0.05 units/step initially. Half the margin (3 units) would be reached in roughly 60–80 steps once the exponential approach is accounted for; a 60-step threshold is conservative. A different trip level justifies a different threshold by the same arithmetic.
- **EX020** — (1) Threshold tuning on test data → tune on separate seeds (Lab 6) and freeze. (2) Simulator too clean → add calibration bias and validate on T2. (3) Attack magnitude chosen to suit method → sweep gains (EX034) and report the full curve.

### Chapter 4

- **EX021** — Rerunning own Lab 3: repeatability. Colleague running your archive: reproducibility. Colleague building their own tank model: replicability.
- **EX022** — Hypotheses: scoring convention, threshold leakage, label alignment, sampling. Tests: re-score with point adjustment (→0.94, within ±0.05: explains gap); retune on train split (no further change); shift labels to first process deviation (small change); downsample (small change). Outcome: reproduction of the reported number succeeds only under point adjustment; event-level metrics adopted.
- **EX023** — Run the noise-free model `true += 1.0 - 0.02*true` for 1,000 steps from 50.0; the result is 50.000000, confirming equilibrium; a stricter test computes accumulated inflow minus outflow and checks it equals final minus initial level within floating-point tolerance.
- **EX024** — k = 0.8: with 0.4 bias it has 0/100 false-alarm runs and 100/100 detections (delay 55.6), whereas k = 0.6 has 4/100 false-alarm runs. The 7–10 step delay cost is accepted for zero false alarms.
- **EX025** — Go if: three consecutive runs complete without the float valve being reached (safety); historian log loss <1% at 1 Hz (data); no unplanned PLC restart (stability); e-stop tested before each session. Otherwise no-go and revise.
- **EX026** — Because 0.94 reproduces a point-adjusted score that credits whole segments for a single alarm; it says nothing about delay or false alarms per shift, and thresholds may have been tuned on test data.

### Chapter 5

- **EX027** — Replacing the paired seed for k = 0.6 with seed i+1000 gives Plant A 6.9 steps, CI [5.3, 8.5] (width 3.2) versus paired [6.5, 7.4] (width 0.9); Plant B 47.3, CI [36.5, 58.6] versus [38.4, 53.0]. Pairing narrows intervals because shared noise cancels.
- **EX028** — Stochastic: sensor noise draws, inflow noise. Parametric: orifice coefficient, calibration bias. Structural: single-tank model, ignoring flow-meter lag.
- **EX029** — "Allowance k = 0.8 and threshold h = 6.0 are fixed, hashed and recorded before any T2 attack data are loaded." Inspecting T2 attack data before freezing, or changing k after seeing T2 results, invalidates the validation.
- **EX030** — Undetected runs set to 400 make the mean a lower bound. Report detection proportion separately and median delay among detected, or a Kaplan–Meier style curve of time to detection.
- **EX031** — Recommendation: show predicted versus reported level on the HMI. Limitation: synthetic operators; preferences may not predict real response times.
- **EX032** — Example: "H1 was not supported on T2: the residual CUSUM detected 9 of 20 class A episodes, compared with 100 of 100 in simulation. Flow-meter lag of several seconds produced residual transients that required a larger allowance, which then masked small manipulations. False alarms remained zero. We conclude the simulator overstated the signal-to-noise ratio and that instrument dynamics must be modelled before deployment claims are made."

### Chapter 6

- **EX033** — Hypothesis: performance drops when thresholds are evaluated on seeds or testbeds unseen during tuning. Test: tune on seeds 0–99, evaluate on 1000–1099 and on T2 with frozen values; compare detection and false alarms.
- **EX034** — Sweep result: gain 0.005 → 14/100 detected, mean delay 186.0, worst overfill 1.12; 0.01 → 55/100, 168.3, 1.37; 0.02 → 100/100, 90.4, 1.87; 0.05 → 100/100, 31.8, 3.36. Slow attacks evade but achieve limited overfill in the window.
- **EX035** — "The method requires an independently wired second measurement linked to the attacked one by a known mass balance; model error must be smaller than the attack signal. Attacks slower than the allowance may evade but achieved ≤1.37 units of modelled overfill in 300 steps. It gives no protection when one attacker controls both measurements."
- **EX036** — "In two synthetic contexts, a residual CUSUM using an independently wired flow meter detected single-sensor level replay that a band alarm missed; it does not protect against an attacker who controls both measurements."
- **EX037** — Publishing the exact T2 sequence gives attackers a ready recipe for a specific product configuration while defenders need only the capability class and architectural fix. Decision: publish the class and the defence; share exact sequences only with the vendor under coordinated disclosure, if a product flaw is involved.
- **EX038** — "We agree that testbeds differ from plants and have narrowed our claims to the two contexts studied (§6.3). We tested structural uncertainty by validating thresholds frozen on simulation on an independent testbed with different instruments (§5.3), report the resulting recall loss, and list plant-scale validation as future work (§8.6)."

### Chapter 7

- **EX039** — Claim: narrowed claim (Ch 6.3). Data: Lab 3, Lab 5, T2 (Ch 3, 5). Warrant: mass balance links flow and level (Ch 3.2). Backing: verification tests, CUSUM theory (Ch 4.3). Qualifier: two synthetic contexts (Ch 5). Rebuttal: class B, slow ramps, lag (Ch 5–6).
- **EX040** — Store tiers as integers (`int(e["tier"][1:])`) and compare numbers; a T10 entry with release maximum T1 is then excluded rather than wrongly passing as "T10" < "T2".
- **EX041** — Simulator code T0; synthetic traces T1; Lab notebooks T1; T2 rig wiring diagram T2; T2 PLC program T2; operator review notes T2; Plant A-style real configs T3; pilot videos T2. Borderline: wiring diagram (T2 because it reveals the shared-PLC weakness); operator notes (T2 because identifiable quotes).
- **EX042** — Purpose: teaching and method demonstration. Parameters: inflow 1.0±0.05, outflow 0.02×level, level noise σ = 0.3, flow noise σ = 0.02, attack gain 0.05 at step 300. Status: invented, not calibrated. Prohibited uses: claims about real plants, benchmarking products.
- **EX043** — Fixed attack onset at step 300 (*unknown*; may favour detectors with warm-up). Single attacker goal (*overstates* generality).
- **EX044** — Publication-based suits it: three separable contributions (metrics, comparison, operator study) with a linking chapter; a monograph is defensible if the institution prefers one integrated argument.

### Chapter 8

- **EX045** — Using the EX032 or §5.5 paragraph: "detected class A replay in simulation" → PASS with scope; "robust to calibration bias" → REVISE: add scope (≤0.4 units); "works on real plants" → REVISE: overreach.
- **EX046** — Positioning: "The CUSUM and residuals are established; our contribution is measuring delay and impact at detection for manipulation of view across two contexts and identifying the attacker capability at which the method fails." Safety: "All attacks ran in simulation or on T2 with a mechanical float valve independent of the PLC, a drip tray, a physical e-stop and a named stop authority; no production system was touched."
- **EX047** — 1: methodology paper at a security venue (establishes metrics); 2: comparison at a control/CPS security venue (uses those metrics); 3: operator study at a human-factors venue. Order builds the vocabulary later papers depend on.
- **EX048** — Modbus lacks authentication: documented design property, not a disclosure. PLC accepts writes to a protected register: implementation flaw → coordinated disclosure. Shared wiring on T2: lab configuration issue → tell the lab owner; not a product vulnerability.
- **EX049** — High: band alarms alone miss replayed level readings. Medium: independent flow measurement plus residual detects single-sensor replay. Unknown: protection against an attacker controlling both measurements was not tested — do not assume it.
- **EX050** — Year 1: multi-loop calibrated model; H: residual detection recall ≥80% with false alarms ≤1 per shift when loops couple. Year 2: consenting operator study; H: displaying predicted-versus-reported values reduces time to correct diagnosis by ≥20%. Both with frozen thresholds and refutation criteria.

**End of the worked results.** Return to the [course chapter index](../SUBJECTS.md).
