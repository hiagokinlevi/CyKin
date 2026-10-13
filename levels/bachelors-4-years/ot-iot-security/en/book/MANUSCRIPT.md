# OT, IoT and Cyber-Physical Security: Bachelor's Foundations and Capstone

- Language: English (`en`); bachelor's course, four years; approximately 3,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: broad security and computing students who need rigorous foundations in OT, IoT and cyber-physical security, ending in a scoped capstone and thesis.
- Relation to neighbouring books: the [engineering book](../../../../engineering-5-years/ot-iot-security/en/book/MANUSCRIPT.md) is design-heavy; the [master's book](../../../../masters-2-years/ot-iot-security/en/book/MANUSCRIPT.md) is research-led. **This book balances foundations, theory, cases, methods and research skills.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited degree. No authority to access real plants. All plants, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–18 are foundations, each applied to a plant from its first page. Chapters 19–32 are the OT, IoT and CPS core, with Laboratory I (25) and Laboratory II (30). Chapters 33–40 are research methods, a comparative project, the capstone and the thesis. Each chapter has learning outcomes, teaching sections, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block. Labs run offline with `python3 file.py`; never point them at a real system.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lakeside District Heating Plant (LDHP)** — boiler control PLC-H, safety trip SIS-H, HMI-1, historian HIST-1, engineering workstation EWS-1, IoT heat meters and meter gateways | System studied throughout | Invented |
| **Maya Chen** | Undergraduate on placement with LDHP's engineering office | Invented |

### Core sources

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA advisories [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a) and [AA22-103A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a); ICS-CERT [IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

After this chapter you can (1) turn a plant sentence into a quantity with units; (2) estimate an order of magnitude before computing; (3) state the assumption that makes a calculation valid; and (4) recognise when a precise-looking number hides a guess. The running case is the synthetic Lakeside District Heating Plant (LDHP).

### 1.1 Why an OT student needs proof habits

Security claims about a heating plant are quantitative whether we admit it or not. "The network change is low risk" really means "the probability of losing supply-temperature control, multiplied by the harm to households, is below a threshold we accept." Mathematical reasoning makes the hidden terms visible. The habit is simple: write every quantity with its unit, name the assumption that links it to the next quantity, and check the result against a rough estimate made before any calculator is touched.

### 1.2 Units and dimensional checks

District heating mixes kilowatts, cubic metres per hour, degrees Celsius and seconds. Delivered heat power is approximately P = ρ · c · Q · ΔT, with water density ρ ≈ 1000 kg/m³ and specific heat c ≈ 4.19 kJ/(kg·K). If you write Q in m³/h you must divide by 3600 to obtain kg/s. A dimensional check catches that slip before it becomes a wrong boiler sizing argument in a risk register.

### 1.3 Implication, contrapositive and counter-example

"If the SIS is independent, then a SCADA compromise cannot disable the trip." The contrapositive — "if a SCADA compromise can disable the trip, the SIS is not independent" — is logically equivalent and often easier to test. The converse is not equivalent: a trip that survives one test does not prove independence. One documented counter-example, such as a shared engineering workstation that can download to both controllers, refutes a universal claim.

### Worked example (synthetic LDHP)

LDHP pumps Q = 180 m³/h with ΔT = 30 K. Estimate first: 0.05 m³/s × 1000 kg/m³ × 4.19 kJ/(kg·K) × 30 K ≈ 6,300 kW. Exact: 180/3600 = 0.05 m³/s, so P = 50 kg/s × 4.19 × 30 = 6,285 kW ≈ 6.3 MW. If an attacker could only change the supply setpoint by 5 K, ΔT falls to 25 K and the delivered heat drops to 5,237.5 kW, a 1,047.5 kW shortfall. That shortfall, not the packet, is the consequence a risk owner can weigh.

> **Synthetic case — Lakeside District Heating Plant.** Student Maya Chen joins LDHP's engineering office. Her first memo must express the heat shortfall caused by a 5 K setpoint error in kilowatts, with every assumption listed.

### Errors and limits

The heat formula ignores pipe losses and the fact that density and heat capacity drift with temperature. A two-significant-figure answer is honest; six digits imply knowledge you do not have.

### Exercises

- **EX001 — Heat at reduced flow.** LDHP's flow falls to 150 m³/h while ΔT stays 30 K. Compute the delivered power and show the unit conversion. *Rubric:* 3 = 5,237.5 kW with m³/h→kg/s shown; 2 = correct value, no conversion; 1 = forgot /3600; 0 = no attempt.
- **EX002 — Contrapositive of a zoning claim.** Write the contrapositive of "if the meter gateway has no route to the control zone, it cannot write to PLC-H". *Rubric:* 3 = correct contrapositive and why it is testable; 2 = correct form only; 1 = gives converse; 0 = none.
- **EX003 — Estimating before computing.** Give a one-line order-of-magnitude estimate of daily heat delivered at 6.3 MW. *Rubric:* 3 = ≈150 MWh/day with method; 2 = right order; 1 = unit error; 0 = none.

### Synthesis

Quantities with units, assumptions said aloud and counter-examples sought: these three habits turn a security opinion about a plant into an argument someone can check.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the layers of a programmable logic controller from I/O card to scan cycle; (2) contrast a PLC with a general-purpose server; (3) explain why deterministic timing is a security property in OT; and (4) list what a firmware image contains.

### 2.1 The scan cycle

A PLC repeatedly reads inputs, executes logic, writes outputs and services communications. At LDHP the boiler PLC-H completes this loop every 20 ms. If communication handling grows — for example because a misconfigured historian polls 400 registers every 50 ms — the scan time stretches and the watchdog may trip the controller into a safe stop. A denial of service in OT can therefore arrive as ordinary traffic that is simply too much.

### 2.2 PLC versus server

A server is designed to run many programs, accept updates and recover by reboot. A PLC is designed to run one program for years, often with no user accounts, limited logging and firmware that the vendor signs (or, in older models, does not sign). Rebooting a server is routine; restarting a controller in a running boiler house requires a work permit, operator presence and a plan to hold the process safe.

### 2.3 What lives in firmware

Firmware bundles a real-time operating system, protocol stacks, the runtime that executes ladder or structured text, and a bootloader. Security consequences follow: a protocol stack bug can affect every program on the device, and an unsigned update path lets anyone who reaches the engineering port replace the runtime. NIST SP 800-82r3 treats firmware integrity and controlled program download as core OT practices.

### Worked example (synthetic LDHP)

PLC-H has a 20 ms target scan and a 100 ms watchdog. Logic takes 9 ms, I/O 4 ms, and each Modbus request costs 0.6 ms to service. With 10 requests per scan the cycle is 9 + 4 + 6 = 19 ms. If a new dashboard adds 30 requests per scan, the cycle becomes 37 ms: still under the watchdog, but the 20 ms timing that tuned loops expect is lost and control quality degrades before any alarm fires.

> **Synthetic case — Lakeside District Heating Plant.** Maya finds a dashboard project asking for "all tags, every scan". She converts the request into scan milliseconds and recommends polling the historian, not the controller.

### Errors and limits

Vendor scan models differ; some service communications in a separate task. Never measure scan impact by loading a production controller — use a bench unit or the vendor's figures.

### Exercises

- **EX004 — Communications load and scan time.** With 9 ms logic, 4 ms I/O and 0.6 ms per request, how many requests per scan keep PLC-H at or under 20 ms? *Rubric:* 3 = 11 requests, shown; 2 = right number, no working; 1 = ignores I/O; 0 = none.
- **EX005 — Server habits that hurt controllers.** Name two server administration habits that are unsafe on a running PLC and give the OT alternative for each. *Rubric:* 3 = two habits with alternatives; 2 = one pair; 1 = habits without alternatives; 0 = none.
- **EX006 — Firmware layers and blast radius.** Explain why a vulnerability in a controller's protocol stack is wider in impact than a bug in one ladder rung. *Rubric:* 3 = shared stack serves every program and is reachable before logic runs; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A controller is a timed machine first and a computer second; its security starts with respecting the scan cycle and controlling what may be loaded onto it.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) read structured data with Python's standard library; (2) validate values against engineering ranges; (3) write output that a reviewer can check line by line; and (4) explain why validation code is a safety-relevant artefact.

### 3.1 Tags as records

An OT tag list is a table: tag name, engineering unit, low and high limits, current value. Python's `csv` module reads such tables without third-party packages, which matters on locked-down engineering laptops where installing software needs approval. Treat each row as a dictionary and keep raw text separate from parsed numbers so a parsing failure is visible rather than silently becoming zero.

### 3.2 Range validation

A temperature of 141 °C on a probe calibrated for 20–130 °C is either a real excursion, a failed sensor or a manipulated value. Code cannot tell which; it can flag the row and stop it reaching a report labelled "normal". The same applies to a negative flow, which is physically impossible for a one-way meter and therefore always a data-quality or integrity question.

### 3.3 Readable output

Print one decision per line with the input that caused it. Reviewers in plant change boards are rarely programmers; they will trust output they can trace to a row.

```python
"""Lab 03: validate a synthetic LDHP tag list (no plant access)."""
import csv, io
RAW = """tag,unit,lo,hi,value
TT-101,degC,20,130,96.5
TT-102,degC,20,130,141.0
PT-201,bar,0,16,9.8
FT-301,m3/h,0,250,-3.0
LT-401,pct,0,100,57
"""
bad = []
for row in csv.DictReader(io.StringIO(RAW)):
    v, lo, hi = float(row["value"]), float(row["lo"]), float(row["hi"])
    ok = lo <= v <= hi
    print(f"{row['tag']:7} {v:7.1f} {row['unit']:5} {'ok' if ok else 'OUT-OF-RANGE'}")
    if not ok: bad.append(row["tag"])
print("flagged:", ", ".join(bad))
```

Run with `python3 lab_tags.py`. Verified output:

```text
TT-101     96.5 degC  ok
TT-102    141.0 degC  OUT-OF-RANGE
PT-201      9.8 bar   ok
FT-301     -3.0 m3/h  OUT-OF-RANGE
LT-401     57.0 pct   ok
flagged: TT-102, FT-301
```

### Worked example (synthetic LDHP)

The lab flags TT-102 (141.0 °C, above 130) and FT-301 (−3.0 m³/h, below 0). Maya's note separates them: TT-102 could be a genuine high reading and goes to the operator immediately; FT-301 is physically impossible and goes to instrumentation as a suspected wiring or scaling fault, with integrity review if the fault cannot be explained.

> **Synthetic case — Lakeside District Heating Plant.** The tag list in the lab is invented; real LDHP limits would come from the instrument index maintained by the control engineers.

### Errors and limits

Range checks catch gross errors, not subtle manipulation inside the band. Floating-point comparison at the boundary needs a stated rule (inclusive here). The script reads a string, not a live system.

### Exercises

- **EX007 — Extending the tag table.** Add row `TT-103,degC,20,130,130.0`. What does the lab print for it and why? *Rubric:* 3 = ok, because limits are inclusive; 2 = ok without reason; 1 = says out-of-range; 0 = none.
- **EX008 — Unparseable values.** Describe what the script does if a value cell contains `n/a`, and propose a fix. *Rubric:* 3 = ValueError stops the run; catch it and flag BAD-VALUE; 2 = one of the two; 1 = says it becomes zero; 0 = none.
- **EX009 — Triage of two flags.** Explain why TT-102 and FT-301 go to different people. *Rubric:* 3 = plausible excursion vs impossible value, operator vs instrumentation; 2 = partial; 1 = treats both alike; 0 = none.

### Synthesis

Small, readable stdlib programs that flag rather than fix are the first tool an OT security student should trust and be able to defend.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) structure a technical memo as claim, evidence and limitation; (2) cite a standard by its exact identifier and edition; (3) write for an operator, an engineer and a manager without changing the facts; and (4) avoid inflated language in security findings.

### 4.1 Claim, evidence, limitation

Every paragraph in an OT security memo should let the reader find three things: what you assert, what you observed that supports it, and where the assertion stops. "Port 502 on PLC-H is reachable from the office VLAN (observed in the approved firewall rule export of 3 March); we did not test whether writes succeed" is a better sentence than "PLC-H is wide open", because it is checkable and honest about scope.

### 4.2 Citing standards precisely

Write "NIST SP 800-82 Rev. 3 (September 2023)", not "NIST guidance". For the 62443 family name the part: IEC 62443-3-3 covers system security requirements and security levels; IEC 62443-2-1 covers the asset owner's security programme; IEC 62443-4-2 covers component requirements. A reader must be able to open the exact document. Do not cite a clause number you have not read.

### 4.3 One fact, three audiences

The operator needs to know what to watch for; the engineer needs the technical path; the manager needs cost, downtime and residual risk. Keep the facts identical across versions — only emphasis and vocabulary change. If the versions disagree on facts, one of them is wrong.

### Worked example (synthetic LDHP)

Weak: "Hackers could take over the boiler, which is extremely dangerous." Rewritten: "A host on the office VLAN can open Modbus/TCP connections to PLC-H (rule 14 in the 3 March export). We have not tested write access. The SIS-H high-temperature trip is hardwired and does not depend on this path. Recommended: remove rule 14 and route historian reads through the DMZ." The rewrite gives location, evidence, untested scope, the independent safeguard and an action.

> **Synthetic case — Lakeside District Heating Plant.** Maya's memo is reviewed by the plant's shift lead, who asks only one question: "What should my operators do differently tonight?" The memo must answer it.

### Errors and limits

Avoid "military-grade", "fully secure" and "zero risk". Passive voice that hides who observed what weakens evidence. A literature review is not a substitute for your own observation.

### Exercises

- **EX010 — Rewriting an inflated finding.** Rewrite "the historian is a massive backdoor" as a claim–evidence–limitation sentence for LDHP. *Rubric:* 3 = all three parts with a concrete observation; 2 = two parts; 1 = still inflated; 0 = none.
- **EX011 — Choosing the right 62443 part.** Which IEC 62443 part would you cite for a requirement on PLC-H's own authentication capability, and which for the plant's patch-management programme? *Rubric:* 3 = 4-2 and 2-1 (2-3 also acceptable for patching) with reasons; 2 = one correct; 1 = cites "62443" only; 0 = none.
- **EX012 — Operator version.** Write the two-sentence operator version of the rule-14 finding. *Rubric:* 3 = observable symptom plus action; 2 = one; 1 = technical jargon only; 0 = none.

### Synthesis

Good OT writing is checkable: exact sources, observed evidence and stated limits, in words each audience can act on.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) define confidentiality, integrity and availability for a heating plant; (2) add safety and reliability as first-class properties; (3) separate threat, vulnerability and consequence; and (4) map one public technique from MITRE ATT&CK for ICS to an LDHP asset.

### 5.1 The OT order of concern

In office IT, confidentiality often leads. In a district heating plant the order usually inverts: the safety of people and equipment first, then availability and integrity of control, and only then confidentiality of data. Recipe tables or customer meter readings still matter — the meter data are personal data — but a leaked spreadsheet does not scald anyone, while a manipulated setpoint can.

### 5.2 Threat, vulnerability, consequence

A threat is an actor or event with intent or potential to cause harm. A vulnerability is a weakness that makes harm possible. A consequence is what actually happens to the process. Students often confuse them: "Modbus has no authentication" is a vulnerability, "a disgruntled contractor" is a threat source, and "loss of heat to 4,000 homes in January" is a consequence. Risk statements need all three.

### 5.3 ATT&CK for ICS as a vocabulary

MITRE ATT&CK for ICS catalogues adversary behaviour observed against industrial systems. Technique T0836 *Modify Parameter* describes changing controller parameters such as setpoints or limits to cause an effect; T0883 *Internet Accessible Device* describes reaching controllers exposed directly to the internet. Use these identifiers to describe behaviour precisely — not as a checklist claiming completeness.

### Worked example (synthetic LDHP)

Statement: "An unauthorized party with access to the office VLAN (threat) could use the unauthenticated Modbus path through rule 14 (vulnerability) to change the supply setpoint, behaviour described by ATT&CK for ICS T0836 Modify Parameter, reducing delivered heat by about 1 MW (consequence, from Chapter 1); the hardwired SIS-H limits over-temperature harm." Each clause is separable and each can be challenged.

> **Synthetic case — Lakeside District Heating Plant.** The plant manager asks whether encrypting the historian database is the top priority. Maya ranks it below separating the office from PLC-H and explains why using the OT order of concern.

### Errors and limits

ATT&CK lists observed behaviour; absence of a technique is not proof it cannot happen. Safety is not the same as security, and security controls must never weaken a safety function.

### Exercises

- **EX013 — Sorting threat, weakness and harm.** Classify: (a) "default password on the meter gateway", (b) "ransomware crew", (c) "boiler trips and district loses heat for six hours". *Rubric:* 3 = vulnerability, threat, consequence; 2 = two right; 1 = one; 0 = none.
- **EX014 — Ranking LDHP priorities.** Justify placing setpoint integrity above meter-data confidentiality at LDHP, without saying confidentiality is unimportant. *Rubric:* 3 = physical consequence vs privacy harm, both retained; 2 = ranking only; 1 = dismisses privacy; 0 = none.
- **EX015 — Mapping an exposed gateway.** Which ATT&CK for ICS technique ID describes the meter gateway being reachable from the internet, and what does mapping it not prove? *Rubric:* 3 = T0883 and "does not prove exploitation or completeness"; 2 = ID only; 1 = wrong ID; 0 = none.

### Synthesis

Security literacy in OT means speaking precisely about threats, weaknesses and physical consequences, with safety at the top and shared vocabularies used honestly.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) model zones and conduits as a directed graph; (2) compute reachability with breadth-first search; (3) reason about which single edge removal disconnects a critical node; and (4) use sets to express allow-lists.

### 6.1 Zones and conduits as a graph

IEC 62443-3-2 asks asset owners to partition a system into zones (groups of assets sharing security requirements) connected by conduits (the communication channels between zones). A directed graph captures this: nodes are zones, edges are conduits in the direction a session can be opened. A path from the enterprise zone to the safety zone is a question about graph reachability, which is mechanical once the graph is drawn honestly.

### 6.2 Breadth-first search

BFS visits a start node, then all its neighbours, then theirs, marking each visited node once. It runs in time proportional to nodes plus edges, so even a large refinery's conduit list is checked instantly. The danger is not the algorithm but the input: a forgotten vendor modem or a dual-homed laptop is an edge the diagram omits.

```python
"""Lab 06: reachability over a synthetic LDHP zone/conduit graph (BFS)."""
from collections import deque
CONDUITS = {"Enterprise": ["DMZ"], "DMZ": ["SCADA"], "SCADA": ["Control"],
            "Control": ["SIS"], "MeterCloud": ["MeterGW"], "MeterGW": ["SCADA"], "SIS": []}
def reach(src):
    seen, q = {src}, deque([src])
    while q:
        for n in CONDUITS.get(q.popleft(), []):
            if n not in seen: seen.add(n); q.append(n)
    return seen
for z in ["Enterprise", "MeterCloud", "SCADA"]:
    r = sorted(reach(z) - {z}); print(f"{z:10} -> {r}  SIS reachable: {'SIS' in r}")
CONDUITS["Control"] = []  # design change: SIS gets its own hardwired trip, no Control->SIS data conduit
print("after removing Control->SIS:", "SIS" in reach("Enterprise"))
```

Run with `python3 lab_reach.py`. Verified output:

```text
Enterprise -> ['Control', 'DMZ', 'SCADA', 'SIS']  SIS reachable: True
MeterCloud -> ['Control', 'MeterGW', 'SCADA', 'SIS']  SIS reachable: True
SCADA      -> ['Control', 'SIS']  SIS reachable: True
after removing Control->SIS: False
```

### 6.3 Cut edges

An edge whose removal disconnects the attacker-facing zones from the critical zone is a cut edge for that pair. In the lab, Control→SIS is such an edge: removing it makes SIS unreachable from Enterprise and from MeterCloud. Engineering often prefers removing a data conduit to a safety system entirely and relying on hardwired trips, which is exactly what the lab's design change represents.

### Worked example (synthetic LDHP)

The lab shows the meter cloud reaching SIS through MeterGW → SCADA → Control → SIS. Maya expresses the conduit list as a set of ordered pairs and notes that the MeterGW→SCADA edge exists only so billing can read flow totals. Replacing it with a one-way export from the historian removes a second path; removing Control→SIS removes the last one.

> **Synthetic case — Lakeside District Heating Plant.** The zone names and conduits in the lab are invented to keep the graph small enough to check by hand.

### Errors and limits

Reachability says a session may be opened, not that it will succeed or what it can do. Undirected drawings hide the difference between "SCADA polls the gateway" and "the gateway can connect to SCADA".

### Exercises

- **EX016 — Tracing a BFS by hand.** List the order in which BFS from MeterCloud visits nodes in the original graph. *Rubric:* 3 = MeterCloud, MeterGW, SCADA, Control, SIS; 2 = right set, wrong order; 1 = missing a node; 0 = none.
- **EX017 — An omitted vendor modem.** A vendor modem gives the internet a direct conduit to Control. After the lab's design change, is SIS reachable from the internet? *Rubric:* 3 = no, Control has no outgoing edge to SIS after the change, but Control itself is now exposed; 2 = "no" only; 1 = "yes"; 0 = none.
- **EX018 — Allow-list as a set.** Express "HIST-1 may read from PLC-H; HMI-1 may read and write PLC-H" as a set of (source, destination, action) tuples. *Rubric:* 3 = three tuples, nothing extra; 2 = minor extra; 1 = uses ranges of hosts; 0 = none.

### Synthesis

Drawing zones and conduits as a directed graph turns segmentation arguments into checks that anyone can rerun — provided the graph includes every real edge.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) decode the Modbus/TCP MBAP header and function code from raw bytes; (2) distinguish read and write function codes; (3) explain why Modbus offers no authentication; and (4) state what a protocol decoder can and cannot tell an analyst.

### 7.1 Modbus/TCP in one frame

Modbus/TCP carries a seven-byte MBAP header — transaction identifier (2 bytes), protocol identifier (2, always zero), length (2) and unit identifier (1) — followed by the protocol data unit beginning with a one-byte function code. The Modbus Application Protocol Specification V1.1b3 defines the codes: 3 reads holding registers, 6 writes a single register, 16 writes multiple registers.

### 7.2 No identity in the protocol

Nothing in the frame says who sent it. Any host that can open TCP port 502 to a controller can issue a write if the device accepts it. Security must therefore come from the network (segmentation, allow-listing) or from a secured variant such as Modbus/TCP Security, which wraps the protocol in TLS with certificate-based roles.

```python
"""Lab 07: decode synthetic Modbus/TCP request headers (offline bytes only)."""
import struct
FC = {1: "read coils", 3: "read holding registers", 4: "read input registers",
      5: "write single coil", 6: "write single register", 16: "write multiple registers"}
frames = ["000100000006010300640002", "00020000000601060064012c", "000300000006011000c80001"]
for h in frames:
    b = bytes.fromhex(h)
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    addr, val = struct.unpack(">HH", b[8:12])
    kind = "WRITE" if fc in (5, 6, 15, 16) else "read"
    print(f"tid={tid} unit={unit} fc={fc} ({FC[fc]}) addr={addr} arg={val} -> {kind}")
```

Run with `python3 lab_modbus.py`. Verified output:

```text
tid=1 unit=1 fc=3 (read holding registers) addr=100 arg=2 -> read
tid=2 unit=1 fc=6 (write single register) addr=100 arg=300 -> WRITE
tid=3 unit=1 fc=16 (write multiple registers) addr=200 arg=1 -> WRITE
```

### 7.3 Reading the output

Frame 2 writes value 300 to register 100; frame 3 is a multiple-register write starting at 200. Notice the decoder prints the starting address and the first argument but does not know what register 100 *means* — that comes from the PLC's register map, which is plant documentation, not protocol.

### Worked example (synthetic LDHP)

In LDHP's register map, holding register 100 is the supply temperature setpoint in tenths of a degree. Frame 2 therefore sets 30.0 °C — far below the 90 °C operating point. The protocol decoder alone would have reported "write single register, addr 100, value 300"; only the register map converts that into "setpoint to 30 °C, potential loss of heat". Maya adds a register-map lookup column to her analysis notebook for exactly this reason.

> **Synthetic case — Lakeside District Heating Plant.** The frames in the lab were composed by hand; no device or network was contacted.

### Errors and limits

Some devices use zero-based addressing and some documents use 40001-style numbering; mixing them causes off-by-one errors. Decoding traffic from a plant you are not authorised to monitor is not acceptable practice.

### Exercises

- **EX019 — Decoding a fourth frame.** Decode `000400000006010400320004`. *Rubric:* 3 = tid 4, fc 4 read input registers, addr 50, count 4, read; 2 = function code right; 1 = byte order wrong; 0 = none.
- **EX020 — What the frame cannot say.** Give two facts about frame 2 that cannot be learned from its bytes. *Rubric:* 3 = sender identity/authorisation and engineering meaning of register 100; 2 = one; 1 = lists header fields; 0 = none.
- **EX021 — Scaling a setpoint write.** Using LDHP's tenths-of-a-degree scaling, what register value sets 92.5 °C? *Rubric:* 3 = 925; 2 = 92 or 93 with scaling noted; 1 = 92.5; 0 = none.

### Synthesis

A protocol decoder gives you structure; plant documentation gives you meaning; and segmentation, not the protocol, gives you identity.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure an analysis tool as pure functions with tests; (2) use `unittest` from the standard library; (3) make functions fail closed; and (4) version a script so a result can be reproduced months later.

### 8.1 Pure functions are reviewable

A function that takes inputs and returns a decision, without reading the network or the clock, can be tested exhaustively. For OT tooling this matters because the reviewer is often a control engineer who will accept a tool only if its behaviour on edge cases is demonstrated. Keep input and output (files, printing) at the edges and the decision logic in the middle.

### 8.2 Fail closed

When an allow-list function receives an unknown source, an unknown function code or a malformed address, it should return "block" rather than raise an exception that a caller might catch and ignore. Failing closed in a monitoring tool means "flag for review"; in an enforcement device it means "deny". Neither means "assume fine".

### 8.3 Tests as documentation

A small `unittest` case list reads like a specification:

```python
import unittest
def classify(fc):
    return "write" if fc in (5, 6, 15, 16) else ("read" if fc in (1, 2, 3, 4) else "unknown")
class T(unittest.TestCase):
    def test_codes(self):
        self.assertEqual(classify(3), "read"); self.assertEqual(classify(16), "write")
        self.assertEqual(classify(43), "unknown")
unittest.main(argv=["x"], exit=False)
```

Running it prints `Ran 1 test` and `OK`. Code 43 (encapsulated interface transport, used for device identification) is deliberately "unknown" rather than "read", because the tool's author has not reasoned about it.

### Worked example (synthetic LDHP)

Maya's first classifier returned "read" for anything not in the write set. A reviewer asked what code 8 (diagnostics) would return. The answer — "read" — was wrong: some diagnostic sub-functions restart communications. She changed the default to "unknown" and added the test above.

> **Synthetic case — Lakeside District Heating Plant.** The classifier is a teaching tool for offline captures, not an enforcement device.

### 8.4 Logging decisions for review

Each decision the tool makes should be written with the input that produced it, the rule that fired and the script version, for example `fc=8 -> unknown (rule: default) v=3f2a91c`. A control engineer reviewing a week of captures can then filter on "unknown" and decide, case by case, whether the classifier needs a new rule. This record is also what lets you show later that a surprising result came from a known version of the code and not from an edit made afterwards.

### Errors and limits

Tests prove the cases you wrote, not the ones you forgot. Record the script's version (a git commit hash) next to every result you publish.

### Exercises

- **EX022 — Classifying diagnostics.** What does `classify(8)` return in the final version, and why is that preferable? *Rubric:* 3 = "unknown"; diagnostics may change device state, so do not assume read; 2 = value only; 1 = "read"; 0 = none.
- **EX023 — A missing test case.** Write one additional assertion that would have caught Maya's original bug. *Rubric:* 3 = assertEqual(classify(8), "unknown") or similar non-read code; 2 = tests a write code; 1 = tests code 3; 0 = none.
- **EX024 — Reproducing an old result.** Name two things to record with a published analysis so it can be reproduced six months later. *Rubric:* 3 = script commit hash and exact input file hash/date; 2 = one; 1 = "save the output"; 0 = none.

### Synthesis

Reviewable OT tools are pure, tested, fail closed and versioned — properties that let a sceptical engineer trust their output.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) model historian data as time, tag and value; (2) aggregate and filter with SQL in SQLite; (3) detect sampling gaps; and (4) explain why the historian is both a security asset and a security risk.

### 9.1 The historian's role

A process historian stores time-series data from controllers for trending, reporting and investigation. Because it sits between control and business networks, it is often the bridge an intruder uses — and also the best record an investigator has. NIST SP 800-82r3 recommends placing data that business users need into a DMZ copy so that enterprise users never query the control-zone historian directly.

### 9.2 A minimal schema

Three columns — timestamp, tag, value — carry most historian content; production systems add quality codes and compression. SQLite, built into Python, is sufficient to learn the queries.

```python
"""Lab 09: query a synthetic historian in an in-memory SQLite database."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table h(ts integer, tag text, v real)")
rows = [(t, "TT-101", 90 + (t % 5)) for t in range(0, 60, 5)] + [(t, "PT-201", 9.5) for t in range(0, 60, 10)]
rows.append((35, "TT-101", 128.0))
db.executemany("insert into h values(?,?,?)", rows)
for tag, n, mx, mean in db.execute("select tag,count(*),max(v),round(avg(v),2) from h group by tag order by tag"):
    print(f"{tag}: n={n} max={mx} mean={mean}")
print("excursions >120:", db.execute("select ts,v from h where tag='TT-101' and v>120").fetchall())
print("gap check PT-201 samples:", [r[0] for r in db.execute("select ts from h where tag='PT-201' order by ts")])
```

Run with `python3 lab_hist.py`. Verified output:

```text
PT-201: n=6 max=9.5 mean=9.5
TT-101: n=13 max=128.0 mean=92.92
excursions >120: [(35, 128.0)]
gap check PT-201 samples: [0, 10, 20, 30, 40, 50]
```

### 9.3 Aggregates hide events

TT-101's mean of 92.92 °C looks normal; the maximum of 128.0 °C at t = 35 does not. Always pair an average with an extreme and a count. The gap check confirms PT-201 was sampled every 10 time units without loss; a missing timestamp in that list would be the first sign of a collection fault or deliberate suppression.

### Worked example (synthetic LDHP)

Maya is asked: "Was there any over-temperature last shift?" A dashboard showing hourly means says no. Her query `select ts, v from h where tag='TT-101' and v > 120` returns one excursion at t = 35, 128 °C. She reports it with the count of samples examined (13) and notes that the SIS-H trip point (assumed 135 °C in this synthetic plant) was not reached.

> **Synthetic case — Lakeside District Heating Plant.** Values, tags and the 135 °C trip point are invented for teaching.

### Errors and limits

Historian compression (deadband or swinging-door) can drop points that did not change "enough", so short spikes may be absent. Timestamps may come from the historian, not the controller. Never grant write access to historian tables for analysis work.

### Exercises

- **EX025 — Counting examined samples.** Why does the lab report n = 13 for TT-101 rather than 12? *Rubric:* 3 = 12 regular samples (0–55 step 5) plus the inserted excursion; 2 = notes extra row; 1 = guesses; 0 = none.
- **EX026 — Query for a sampling gap.** Write SQL that returns PT-201 timestamps where the next sample is more than 10 units later. *Rubric:* 3 = window function LEAD (or self-join) with ts difference > 10; 2 = correct idea, syntax slip; 1 = counts rows only; 0 = none.
- **EX027 — Deadband compression and spikes.** Explain how deadband compression could hide a brief excursion. *Rubric:* 3 = point stored only on change beyond deadband or exception/heartbeat, so a short spike between stored points can vanish; 2 = partial; 1 = "compression loses data" only; 0 = none.

### Synthesis

Ask the historian for extremes, counts and gaps, not just averages — and treat its placement and permissions as security design.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) distinguish authorization from permission to access; (2) list the elements of a written work permit for OT testing; (3) handle discovered vulnerabilities through coordinated disclosure; and (4) refuse requests that would endanger people or exceed scope.

### 10.1 Authorization comes from the owner

Only the asset owner — or someone the owner has delegated in writing — can authorise testing of an OT system. A plant employee who is curious, a vendor who "has access anyway" or a lecturer who wants a demo cannot grant it. In the industrial setting authorization must also come from operations: a test that is legal but unsafe is still unacceptable.

### 10.2 The work permit

A sound OT test authorization names the systems in scope, the time window, the techniques allowed (passive capture only, read-only queries, or bench testing), the people on the call, the stop conditions ("if any process alarm occurs, stop and notify the shift lead"), and the rollback plan. It is signed by the owner and by the operations manager for the affected area.

### 10.3 Coordinated disclosure

If you find a vendor product flaw, report it to the vendor and, where appropriate, to CISA, whose ICS advisories publish coordinated fixes. ETSI EN 303 645 provision 5.2 requires consumer IoT manufacturers to publish a vulnerability disclosure policy; many industrial vendors operate similar programmes. Publishing exploit detail before a fix exists can put every plant using that product at risk.

### Worked example (synthetic LDHP)

A classmate offers Maya the IP address of a "real" heating controller found on an internet search engine and suggests "just reading one register to prove it works". Maya declines: no owner authorization, no permit, unknown process consequence. She instead notes the exposure category (ATT&CK for ICS T0883) and suggests the classmate report the exposure to the national CERT, which can contact the owner.

> **Synthetic case — Lakeside District Heating Plant.** The classmate and the exposed controller are fictional; the reasoning is the point.

### Errors and limits

"Read-only" is not automatically harmless — some legacy devices crash on unexpected requests. Ethics codes do not replace law; learners must know their jurisdiction's computer misuse statute.

### Exercises

- **EX028 — Permit stop condition.** Write one stop condition for a passive network capture at LDHP's control switch. *Rubric:* 3 = observable trigger plus action and who is told; 2 = trigger only; 1 = vague "if problems"; 0 = none.
- **EX029 — Who may authorise?** A contractor's project manager emails "go ahead and scan PLC-H". Is that sufficient? *Rubric:* 3 = no; needs owner and operations sign-off with scope and window; 2 = no without reason; 1 = yes with caveats; 0 = yes.
- **EX030 — Disclosing a vendor flaw.** List the first two steps after finding a crash bug in a controller model on a bench unit. *Rubric:* 3 = preserve evidence privately and contact vendor/PSIRT (and CISA or national CERT); 2 = one; 1 = post on social media; 0 = none.

### Synthesis

In OT, ethical practice is operational: written owner authorization, explicit stop conditions and coordinated disclosure protect people as well as reputations.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) identify where general-purpose operating systems appear in an OT architecture; (2) explain why vendor support matrices constrain hardening; (3) apply application allow-listing and removable-media control; and (4) collect host evidence with least privilege.

### 11.1 Windows and Linux inside the plant

PLCs run real-time firmware, but HMIs, engineering workstations, historians and OPC servers run Windows or Linux. These hosts are where phishing payloads, infected USB sticks and remote-access tools land. NIST SP 800-82r3 treats them as OT assets with OT constraints: they may not be patched monthly, may run software certified only for an old OS build, and may be needed around the clock.

### 11.2 Support matrices

The HMI vendor certifies a specific OS version, service pack and antivirus product. Applying an unsupported hardening setting — disabling a service the HMI runtime uses, for example — can leave operators with a blank screen during a cold snap. Hardening therefore follows a test-on-bench, change-board, deploy-in-window sequence, and exceptions are documented with compensating controls.

### 11.3 Allow-listing and media control

Application allow-listing permits only known executables, which suits HMIs because their software set rarely changes. Removable-media control — scanning kiosks, blocked USB storage, signed transfer media — addresses the most common way malware crosses an air gap. Both are host controls listed among IEC 62443-3-3 system requirements for malicious-code protection (SR 3.2).

### 11.4 Evidence with least privilege

For an investigation, prefer exporting the event log, the installed-software list and the running-process list with a read-only account over imaging the disk of a running HMI. Imaging may require downtime and copies proprietary recipes.

### Worked example (synthetic LDHP)

LDHP's HMI-1 runs a Windows build certified by its vendor. Maya proposes three changes: enable allow-listing in audit mode for two weeks, then enforce; block USB mass storage except via the scanning kiosk; remove the local administrator account used by all shifts and issue named accounts. The vendor confirms the first two; the third requires a runtime service account, which she documents as an exception.

> **Synthetic case — Lakeside District Heating Plant.** The vendor response is invented; real vendors publish their own hardening guides.

### Errors and limits

Audit mode that is never switched to enforce is theatre. Antivirus scans during peak load can slow an HMI; schedule them.

### Exercises

- **EX031 — Why audit mode first?** Explain the purpose of running allow-listing in audit mode before enforcing it on HMI-1. *Rubric:* 3 = discover legitimate executables without blocking operations, then enforce on a reviewed list; 2 = partial; 1 = "for testing"; 0 = none.
- **EX032 — Choosing an evidence method.** For a suspected infection on HMI-1, choose between live export and disk imaging and justify it. *Rubric:* 3 = live read-only export first; image only if justified, permitted and scheduled; 2 = choice only; 1 = image immediately; 0 = none.
- **EX033 — Documenting a hardening exception.** Write the exception record for the runtime service account. *Rubric:* 3 = reason, compensating control, owner, review date; 2 = three; 1 = reason only; 0 = none.

### Synthesis

General-purpose hosts are the softest layer of a plant; harden them within vendor support, control what runs and what is plugged in, and investigate them gently.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) estimate a false-alarm rate with a confidence bound; (2) use the rule of three for zero observed events; (3) compare Wilson intervals with naive point estimates; and (4) avoid the base-rate fallacy when evaluating alerts.

### 12.1 Zero is not zero

A detector that raised no false alarms in 40 quiet days has a point estimate of 0, but the honest statement is a bound. The rule of three gives an approximate 95 % upper limit of 3/n when zero events are seen in n independent trials; with n = 40 that is 7.5 %.

### 12.2 Wilson intervals

The Wilson score interval behaves well for small counts and proportions near 0 or 1, unlike the textbook normal approximation, which can produce negative lower bounds.

```python
"""Lab 12: false-alarm estimates and rule-of-three bounds (synthetic counts)."""
import math
def wilson_upper(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    return (p + z*z/(2*n) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
for k, n in [(0, 40), (0, 300), (3, 300)]:
    r3 = 3 / n if k == 0 else float("nan")
    print(f"k={k:2} n={n:3} point={k/n:.4f} wilson95_upper={wilson_upper(k,n):.4f} rule_of_three={r3:.4f}")
```

Run with `python3 lab_rule3.py`. Verified output:

```text
k= 0 n= 40 point=0.0000 wilson95_upper=0.0876 rule_of_three=0.0750
k= 0 n=300 point=0.0000 wilson95_upper=0.0126 rule_of_three=0.0100
k= 3 n=300 point=0.0100 wilson95_upper=0.0290 rule_of_three=nan
```

### 12.3 Reading the numbers

For 0/40 the Wilson upper bound (8.76 %) is a little above the rule of three (7.5 %); for 0/300 both shrink to about 1 %. Three false alarms in 300 gives a point estimate of 1 % but an upper bound near 2.9 %. Collecting more quiet days is the only way to narrow the interval.

### 12.4 Base rates

Suppose real attacks occur on 1 day in 1,000 and a detector catches 90 % of them while raising a false alarm on 2 % of quiet days. Of 1,000 days, it flags about 0.9 true and 19.98 false — so roughly 4 % of alerts are real. Operators who learn that most alerts are noise begin to ignore them, which is why alarm-management practice treats nuisance rates as a safety issue.

### Worked example (synthetic LDHP)

The control engineer says a new supply-temperature detector "never false-alarms". Maya asks for the denominator: 40 days. She writes: "0 false alarms in 40 days; 95 % upper bound ≈ 8.8 % per day (Wilson); about 300 quiet days would be needed to claim below roughly 1 %."

> **Synthetic case — Lakeside District Heating Plant.** Counts are invented; the methods are standard.

### 12.5 Per-shift framing for operators

Operators think in shifts, not proportions. A 2 % per-day false-alarm rate on one detector sounds small, but forty such detectors produce almost one nuisance alarm per day. Convert rates into "expected alarms per shift" before asking a control room to accept a new detector.

### Errors and limits

Bounds assume independent trials; consecutive days in the same weather regime are correlated, so the true uncertainty is wider.

### Exercises

- **EX034 — Upper bound for zero in 150.** Apply the rule of three to 0 false alarms in 150 days. *Rubric:* 3 = 2 % with "approximate 95 % upper bound"; 2 = number only; 1 = says 0 %; 0 = none.
- **EX035 — Alert precision under a low base rate.** With a 1-in-500 attack-day rate, 95 % detection and 1 % false alarms, what fraction of alerts are real? *Rubric:* 3 ≈ 16 % with working; 2 = method right, arithmetic slip; 1 = answers 95 %; 0 = none.
- **EX036 — Correlated trials.** Why do 40 consecutive winter days overstate the information in "0/40"? *Rubric:* 3 = days share conditions so are not independent; effective n smaller; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Always publish detection claims with a count, a denominator and a bound; and judge alerts by how often they are right, not just how often attacks are caught.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) design named, role-based accounts for operators, engineers and vendors; (2) explain the IEC 62443 foundational requirement for identification and authentication control; (3) separate "view", "operate" and "engineer" privileges; and (4) design time-bounded vendor access.

### 13.1 Shared accounts break attribution

Control rooms historically used one shift login. When a setpoint changes, the log shows "operator" — not which operator. IEC 62443-3-3 groups requirements into seven foundational requirements; FR 1, identification and authentication control, asks that human users be uniquely identified. Named accounts let an investigation separate an honest mistake from misuse.

### 13.2 Roles that match work

At LDHP three roles suffice for HMI-1: *view* (trends and alarms), *operate* (acknowledge alarms, change setpoints within limits) and *engineer* (change limits, download logic from the engineering workstation). FR 2, use control, covers enforcing those privileges. Least privilege means a contractor reviewing trends gets *view* only.

### 13.3 Emergency access

A plant cannot lock operators out during an emergency because a directory server is down. Design break-glass accounts: sealed credentials, local authentication, immediate alerting on use, and post-event review. This is availability and safety shaping identity design.

### 13.4 Vendor remote access

Vendors need remote access for diagnostics. CISA advisory AA21-042A, on the 2021 compromise of a US water treatment facility's control system through remote-access software, recommended multiple-factor authentication, strong passwords for remote desktop credentials, auditing remote connections and closing unused RDP ports. A safer design: a jump host in the DMZ, multi-factor authentication, sessions enabled by the shift lead for a fixed window, and recording.

### Worked example (synthetic LDHP)

Maya maps current practice: one shared HMI login, vendor access via an always-on remote desktop tool. Her design: named accounts in three roles; break-glass envelope in the shift-lead safe; vendor sessions through the DMZ jump host, enabled for four hours per ticket, recorded and reviewed weekly.

> **Synthetic case — Lakeside District Heating Plant.** LDHP's accounts and vendor are invented; the cited advisory describes a real incident.

### Errors and limits

MFA on a control-room console can slow emergency response; use it for remote and engineering access, and rely on physical control-room security for local operation where justified.

### Exercises

- **EX037 — Assigning a role.** A boiler service contractor needs to check combustion trends for a week. Which role and what time limit? *Rubric:* 3 = view only, expiring after the week, named account; 2 = role right; 1 = operate; 0 = engineer.
- **EX038 — Break-glass review.** List three things to check after the break-glass account was used. *Rubric:* 3 = who used it and why, actions taken, credential rotated; 2 = two; 1 = one; 0 = none.
- **EX039 — Lessons from AA21-042A.** Name two remote-access measures recommended in the water-facility advisory that apply to LDHP. *Rubric:* 3 = two correct measures; 2 = one; 1 = generic "use antivirus"; 0 = none.

### Synthesis

Identity in OT must make every action attributable, every privilege match a job and every emergency survivable.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) recognise personal data in smart-meter and building-automation streams; (2) apply data minimisation and purpose limitation; (3) choose aggregation intervals that serve operations without revealing household behaviour; and (4) relate privacy to ETSI EN 303 645 provision 5.8.

### 14.1 Heat meters reveal lives

LDHP's IoT meters report each household's heat consumption. Hourly readings show when residents wake, cook, travel or are away — the same inference problem that made electricity smart meters controversial. In many jurisdictions such readings are personal data because they relate to an identifiable household.

### 14.2 Minimisation and purpose

Billing needs a monthly total. Network balancing needs neighbourhood flow, not house-level detail. Fault detection may need individual readings, but perhaps daily and retained for weeks, not years. Writing the purpose next to each data flow forces the question "do we need this granularity?"

### 14.3 Aggregation as a control

Aggregating 40 households in a street segment before data leave the gateway removes individual patterns while keeping the operational signal. Aggregation is not perfect: if one dwelling dominates the segment, its pattern remains visible, so engineers check the minimum group size.

### 14.4 The consumer IoT baseline

ETSI EN 303 645 provision 5.8 asks that personal data in transit between a device and associated services be protected (for example encrypted), and provision 6 addresses data protection more generally — informing consumers what data is processed and why. A district-heating meter is not always "consumer IoT", but the provisions are a useful checklist.

### Worked example (synthetic LDHP)

The analytics team requests five-minute household readings "for future machine learning". Maya's response: monthly totals for billing; daily per-household readings retained 60 days for leak detection; street-level hourly aggregates (minimum 20 dwellings) for balancing; five-minute household data not collected without a defined purpose and a privacy impact assessment.

> **Synthetic case — Lakeside District Heating Plant.** The analytics request and retention periods are invented examples.

### Errors and limits

Pseudonymising meter IDs does not anonymise them if addresses are kept elsewhere. Privacy law varies; this chapter is orientation, not legal advice.

### Exercises

- **EX040 — Inferring occupancy.** Give two things an observer could infer from hourly heat readings of one flat. *Rubric:* 3 = two plausible inferences (absence, daily routine, number of occupants); 2 = one; 1 = vague; 0 = none.
- **EX041 — Granularity per purpose.** For leak detection, propose a reading interval and retention period and justify both. *Rubric:* 3 = daily (or hourly) with weeks-scale retention and reasoning; 2 = values only; 1 = keep everything; 0 = none.
- **EX042 — When aggregation fails.** Why might a segment containing one large school and five flats fail as a privacy aggregate? *Rubric:* 3 = school dominates; flats' patterns lost but school's revealed / group too small; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Operational IoT data is often personal data; collect it for a purpose, at the coarsest useful granularity, and protect it in transit and at rest.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) correct for clock offset when combining logs; (2) preserve the chain of custody for exported evidence; (3) distinguish observation, inference and assumption in a timeline; and (4) state measurement uncertainty.

### 15.1 Clocks disagree

Controllers, HMIs and historians often keep independent clocks, and a PLC without network time can drift by minutes per month. Before sequencing events, measure the offset — for instance, by comparing a known event (an operator's setpoint change) in both logs — and record how it was measured.

```python
"""Lab 15: align two synthetic logs with a measured clock offset."""
from datetime import datetime, timedelta
hmi = [("2026-03-02T10:00:07", "operator changed SP TT-101 to 95"), ("2026-03-02T10:02:40", "alarm TT-101 HI")]
plc = [("2026-03-02T09:58:52", "SP write accepted"), ("2026-03-02T10:01:30", "valve CV-11 to 80%")]
offset = timedelta(seconds=75)  # measured: PLC clock is 75 s behind the reference
ev = [(datetime.fromisoformat(t), "HMI", m) for t, m in hmi] + [(datetime.fromisoformat(t) + offset, "PLC", m) for t, m in plc]
for t, src, m in sorted(ev):
    print(t.time(), src, m)
```

Run with `python3 lab_clock.py`. Verified output:

```text
10:00:07 HMI operator changed SP TT-101 to 95
10:00:07 PLC SP write accepted
10:02:40 HMI alarm TT-101 HI
10:02:45 PLC valve CV-11 to 80%
```

### 15.2 What the corrected timeline shows

After adding the measured 75-second offset, the PLC's "SP write accepted" lines up with the HMI entry at 10:00:07, which supports the hypothesis that the write came from HMI-1. Without correction the PLC event appears 75 seconds before the operator acted — a sequence that might be misread as an external write followed by an operator reaction.

### 15.3 Chain of custody

For each exported file record who exported it, from which system, when, by what method, and its SHA-256 hash. Store the original read-only and work on copies. This is how a timeline becomes evidence a manager, insurer or court can rely on.

### 15.4 Observation, inference, assumption

Label each timeline entry. "PLC log line at 09:58:52 local PLC time" is an observation. "The write originated from HMI-1" is an inference. "The PLC clock offset was constant all morning" is an assumption. Mixing them is the most common flaw in incident reports.

### Worked example (synthetic LDHP)

Maya's table has three columns — corrected time, source, statement — plus a fourth for the label (O/I/A). The offset row reads: "Offset 75 s ± 2 s, measured by matching the 10:00:07 HMI setpoint change to the PLC acceptance message (A: offset constant during 09:30–10:30)."

> **Synthetic case — Lakeside District Heating Plant.** Log lines and the offset are invented.

### Errors and limits

One matched event gives one offset measurement; drift during the period may make it wrong later. Time zones and daylight-saving shifts are a separate error source.

### Exercises

- **EX043 — Applying the offset.** A PLC log line reads 10:04:10. What is the corrected time? *Rubric:* 3 = 10:05:25; 2 = correct direction, arithmetic slip; 1 = subtracts; 0 = none.
- **EX044 — Labelling timeline entries.** Label O, I or A: (a) "CV-11 moved to 80 % at 10:02:45", (b) "the valve move was automatic control action", (c) "no other host wrote to PLC-H". *Rubric:* 3 = O, I, A; 2 = two right; 1 = one; 0 = none.
- **EX045 — Custody fields.** List five fields of a custody record for the exported PLC log. *Rubric:* 3 = five relevant fields including hash; 2 = four; 1 = no hash; 0 = none.

### Synthesis

Evidence in OT is only as good as its clocks, its custody record and its honesty about what was seen versus concluded.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) place LDHP assets in the Purdue reference levels; (2) design a DMZ between enterprise and control zones; (3) assign target security levels to zones using IEC 62443-3-2 concepts; and (4) explain defence in depth without claiming that any single layer is sufficient.

### 16.1 Purdue levels as a starting map

The Purdue model numbers levels from the physical process (0) through sensors and actuators (1), supervisory control (2), site operations (3) up to enterprise (4–5). It is old and imperfect — cloud services and IIoT gateways blur the levels — but it gives a shared vocabulary. At LDHP, transmitters and the boiler are level 0–1, PLC-H and SIS-H level 1, SCADA and HMI level 2, HIST-1 level 3, and billing and e-mail level 4.

### 16.2 The industrial DMZ

Between levels 3 and 4 sits a demilitarised zone holding systems both sides need: a historian replica, a patch server, a jump host for remote access. The rule is that no session crosses the DMZ end to end; enterprise users connect to DMZ services, and control-zone systems push or are pulled by DMZ services. NIST SP 800-82r3 describes this pattern in its discussion of defence-in-depth architecture.

### 16.3 Security levels

IEC 62443 defines security levels SL 1–4 by the attacker a zone must resist, from casual or coincidental violation (SL 1) up to sophisticated means with extended resources (SL 4). Risk assessment sets a target level (SL-T) per zone; components then need capabilities (SL-C) that, with compensating measures, achieve it (SL-A).

### Worked example (synthetic LDHP)

Maya proposes SL-T 3 for the boiler control zone (PLC-H, HMI-1), SL-T 2 for the IoT meter zone, and keeps SIS-H as its own zone with no routable conduits at all. Rationale: control-zone compromise can cause loss of heat to thousands of homes; meter compromise mainly affects billing and privacy; the SIS must remain independent of both.

> **Synthetic case — Lakeside District Heating Plant.** Security-level choices here illustrate reasoning; a real assessment follows IEC 62443-3-2's documented process.

### Errors and limits

A DMZ with a firewall rule "any → any" between its halves is a diagram, not a control. Purdue levels do not dictate trust; an IIoT sensor may talk directly to a cloud service and must be zoned on its own merits.

### Exercises

- **EX046 — Placing the meter gateway.** Where would you place LDHP's IoT meter gateway in or around the Purdue model, and why does it not fit neatly? *Rubric:* 3 = own zone (often beside level 3/DMZ) because it bridges field devices and a cloud service; 2 = level without reason; 1 = level 1 inside control zone; 0 = none.
- **EX047 — A DMZ rule set.** Write two firewall rules that let enterprise users see historian data without reaching HIST-1. *Rubric:* 3 = HIST-1 → DMZ replica (push) and Enterprise → replica (read), no Enterprise → HIST-1; 2 = one; 1 = direct rule; 0 = none.
- **EX048 — Justifying SL-T 3.** In two sentences, justify SL-T 3 for the boiler control zone. *Rubric:* 3 = consequence severity and plausible skilled attacker; 2 = one; 1 = "it is important"; 0 = none.

### Synthesis

Architecture is the art of deciding which sessions may exist; zones, conduits, a real DMZ and security levels make those decisions explicit and testable.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain message authentication codes and why integrity often matters more than secrecy in OT; (2) use `hmac` and `hashlib` from the standard library; (3) prevent replay with counters; and (4) list the operational costs of cryptography on constrained devices.

### 17.1 Integrity first

A heat meter's reading is not secret to its owner, but a forged reading changes a bill and a forged control command changes a process. A message authentication code (MAC) lets a receiver who shares a secret key verify that a message came from a key holder and was not altered. HMAC with SHA-256 is a widely used construction, standardised in FIPS 198-1.

### 17.2 Replay

A valid message captured yesterday is still valid cryptographically today. Including a strictly increasing counter (or a timestamp checked against a window) inside the authenticated data lets the receiver reject repeats.

```python
"""Lab 17: HMAC-protected meter readings with a replay counter (synthetic key)."""
import hmac, hashlib
KEY = b"synthetic-lab-key-not-for-use"
def tag(ctr, kwh): return hmac.new(KEY, f"{ctr}|{kwh}".encode(), hashlib.sha256).hexdigest()[:16]
last = 0
msgs = [(1, 120.5, tag(1, 120.5)), (2, 121.0, tag(2, 121.0)), (2, 121.0, tag(2, 121.0)), (3, 99.0, tag(3, 121.4))]
for ctr, kwh, t in msgs:
    if not hmac.compare_digest(t, tag(ctr, kwh)): print(ctr, kwh, "REJECT bad tag")
    elif ctr <= last: print(ctr, kwh, "REJECT replay")
    else: last = ctr; print(ctr, kwh, "accept")
```

Run with `python3 lab_hmac.py`. Verified output:

```text
1 120.5 accept
2 121.0 accept
2 121.0 REJECT replay
3 99.0 REJECT bad tag
```

### 17.3 Reading the run

Message 2 is accepted once and rejected the second time as a replay, even though its tag is correct. Message 3 carries a tag computed for 121.4 kWh but claims 99.0 kWh, so verification fails. Note `hmac.compare_digest`, which compares in constant time and avoids leaking how many leading characters matched.

### 17.4 Operational costs

Keys must be provisioned per device, rotated and revoked; a meter replaced after a fault needs a new key, and a shared fleet-wide key means one extracted key forges every meter. Constrained devices may lack hardware for secure key storage. ETSI EN 303 645 provision 5.4 asks that sensitive security parameters be stored securely and that hard-coded critical security parameters in device software are not used.

### Worked example (synthetic LDHP)

Maya computes the size overhead: a truncated 16-hex-character (64-bit) tag plus an 8-byte counter adds 16 bytes per reading. At one reading per hour per meter across 4,000 meters, that is 1.5 MB per day — trivial for the network, but the key-management process is the real cost.

> **Synthetic case — Lakeside District Heating Plant.** The key in the lab is a placeholder string; never embed keys in code.

### Errors and limits

Truncating MACs reduces forgery resistance; 64 bits is a common minimum for such designs. Hashing alone (without a key) provides no authentication. Encryption without integrity protection can be malleable.

### Exercises

- **EX049 — Detecting a counter reset.** After a meter firmware update the counter restarts at 1. What does the lab's receiver do, and how should the design handle it? *Rubric:* 3 = rejects as replay; re-key or persist counter with a key-epoch field; 2 = behaviour only; 1 = accepts; 0 = none.
- **EX050 — Why not plain SHA-256?** Explain why appending SHA-256(reading) does not stop forgery. *Rubric:* 3 = no secret: anyone can recompute the hash for a forged value; 2 = partial; 1 = "SHA-256 is weak"; 0 = none.
- **EX051 — Fleet-wide key risk.** Describe the consequence of all 4,000 meters sharing one HMAC key. *Rubric:* 3 = extracting it from one meter forges readings for any meter; per-device keys limit blast radius; 2 = partial; 1 = vague; 0 = none.

### Synthesis

For OT data, authenticated integrity with replay protection is the main cryptographic goal, and key management — not the algorithm — decides whether it works.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) turn a vague worry into a researchable question; (2) choose between descriptive, comparative and experimental designs; (3) define variables, measures and threats to validity; and (4) search for and evaluate peer-reviewed OT security literature.

### 18.1 From worry to question

"Are our detectors good?" is not a question you can answer. "On LDHP's synthetic supply-temperature data, does a CUSUM detector reach a lower false-alarm rate than a fixed band at equal detection rate for slow ramps?" is. It names the population (synthetic data), the comparison, the outcome measures and the attack class.

### 18.2 Design choices

Descriptive studies characterise what exists (inventory of protocols on a network). Comparative studies contrast groups or methods without controlling assignment. Experiments manipulate one variable — detector type — while holding others fixed, typically through simulation in OT because experimenting on live plants is unsafe.

### 18.3 Validity

Internal validity asks whether the measured difference is caused by the manipulated variable; external validity asks whether results generalise beyond the synthetic plant. Construct validity asks whether "false-alarm rate per run" really measures operator burden. Name each threat and what you did about it.

### 18.4 Reading the literature

Giraldo et al. (2018, *ACM Computing Surveys*, doi:10.1145/3203245) survey physics-based attack detection in CPS and highlight that many papers evaluate detectors without a consistent adversary model. Urbina et al. (CCS 2016, doi:10.1145/2976749.2978388) propose evaluating detectors by the impact a stealthy attacker can still cause while remaining undetected, rather than by detection rate alone. These two papers frame the detector lab in Chapter 25.

### Worked example (synthetic LDHP)

Maya drafts: Question — the CUSUM vs band comparison above. Design — simulation experiment, 40 seeds per condition. Measures — false alarms per run, detection within 100 samples, mean delay. Threats — synthetic noise is Gaussian (external validity); thresholds tuned by hand (internal validity).

> **Synthetic case — Lakeside District Heating Plant.** The research plan is a teaching exercise using simulated data only.

### Errors and limits

Searching only vendor white papers yields marketing, not evidence. Do not cite a paper you have not opened; verify DOIs resolve.

### Exercises

- **EX052 — Sharpening a vague question.** Rewrite "Is the IoT meter network secure?" as a researchable question. *Rubric:* 3 = population, measure and comparison stated; 2 = two; 1 = still vague; 0 = none.
- **EX053 — Naming a validity threat.** Identify one external-validity threat in Maya's design and one mitigation. *Rubric:* 3 = Gaussian noise/single plant; add real-noise profiles or second model; 2 = threat only; 1 = internal threat; 0 = none.
- **EX054 — Urbina's metric in one sentence.** State the evaluation idea of Urbina et al. (2016). *Rubric:* 3 = measure the maximum impact an undetected (stealthy) attacker can achieve, not just detection rate; 2 = partial; 1 = wrong; 0 = none.

### Synthesis

Research begins with a sharp question, a design that fits it, honest validity threats and sources you have actually read.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — OT, IoT and cyber-physical security: scope and theory

### Learning outcomes

You will (1) define OT, IIoT, consumer IoT and cyber-physical systems and where they overlap; (2) explain the feedback loop as the object being protected; (3) identify the core standards for each domain; and (4) describe why safety and security engineering must be co-ordinated.

### 19.1 Definitions

Operational technology is hardware and software that monitors or controls physical devices and processes. NIST SP 800-82r3 broadened its scope from "industrial control systems" to OT generally, including building automation and transport. IoT devices are network-connected things with sensing or actuation; NIST IR 8259 frames the baseline activities manufacturers should perform for them. A cyber-physical system is the combination of computation, networking and physical process in a closed loop.

### 19.2 The loop as the asset

The thing an OT defender protects is not a computer but a feedback loop: sensor → controller → actuator → process → sensor. An attacker can falsify the sensor reading, change the controller's logic or parameters, override the actuator, or disrupt the communication that ties them together. Each corresponds to ATT&CK for ICS tactics such as *Impair Process Control* and *Inhibit Response Function*.

### 19.3 Standards map

IEC 62443 covers industrial automation and control systems for asset owners, integrators and product suppliers. NIST SP 800-82r3 is a guide for OT security programmes. NIST IR 8259 (and 8259A) sets IoT device cybersecurity capability baselines for manufacturers. ETSI EN 303 645 is the European baseline for consumer IoT. They overlap but answer different questions: who must do what, for which kind of system.

### 19.4 Safety and security

Functional safety (IEC 61508, IEC 61511 for process industries) assumes random and systematic failures; security assumes an adversary. A safety instrumented system must stay independent so that a cyber-induced process upset still ends in a safe state. IEC 62443 and IEC 61511 both point practitioners to co-ordinate the two analyses.

### Worked example (synthetic LDHP)

Maya maps LDHP's supply-temperature loop: TT-101 → PLC-H → fuel valve FV-12 → boiler → TT-101. She lists one attack point per element and the independent safeguard: SIS-H with its own temperature transmitter TT-101S, hardwired to the fuel shut-off.

> **Synthetic case — Lakeside District Heating Plant.** Loop tags are invented.

### Errors and limits

Labels like "OT" and "IoT" are conveniences; a building-management sensor on Wi-Fi is both. Do not choose a standard by brand familiarity; choose by role and system type.

### Exercises

- **EX055 — Four attack points on one loop.** Name one attack point per element of the TT-101 loop. *Rubric:* 3 = four, one per element; 2 = three; 1 = two; 0 = none.
- **EX056 — Matching standards to roles.** Which document fits (a) the meter manufacturer's product baseline, (b) LDHP's own OT security programme? *Rubric:* 3 = NIST IR 8259 or ETSI EN 303 645 / IEC 62443-4-2; and SP 800-82r3 or IEC 62443-2-1; 2 = one; 1 = same answer for both; 0 = none.
- **EX057 — Why TT-101S matters.** Explain why SIS-H uses its own transmitter rather than reading TT-101 through PLC-H. *Rubric:* 3 = falsified or failed TT-101/PLC path would blind the SIS; independence; 2 = partial; 1 = cost; 0 = none.

### Synthesis

OT, IoT and CPS security protect feedback loops; the right standard depends on your role, and safety independence is non-negotiable.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: foundational cases

### Learning outcomes

You will (1) summarise three documented incidents from primary sources; (2) extract the attack path and the defensive lesson from each; (3) distinguish what is publicly confirmed from speculation; and (4) relate each case to LDHP.

### 20.1 Ukraine power grid, December 2015

The US ICS-CERT alert IR-ALERT-H-16-056-01 reports that three Ukrainian regional electric power distribution companies suffered coordinated cyber attacks causing outages that affected about 225,000 customers. The alert reports that the actors probably used legitimate credentials acquired beforehand for remote access, wiped systems with KillDisk malware, overwrote some HMIs and corrupted the firmware of serial-to-Ethernet devices at substations. Power was restored, but the companies continued under constrained operations. Lesson: stolen credentials and remote access were the path, and recovery depended on being able to run without the damaged automation.

### 20.2 Mirai, 2016

Antonakakis et al. ("Understanding the Mirai Botnet", USENIX Security 2017) measured a botnet that infected hundreds of thousands of IoT devices, largely by logging in with factory-default credentials over Telnet, and then launched large denial-of-service attacks. Lesson: universal default passwords at scale are an infrastructure risk — which is exactly what ETSI EN 303 645 provision 5.1 prohibits.

### 20.3 Water treatment facility, February 2021

CISA advisory AA21-042A describes unauthorised access to a US drinking-water treatment plant's SCADA system through remote-access software, with an attempt to raise sodium hydroxide levels. An operator noticed and reversed the change. Plant personnel noticed and corrected the change before the SCADA software alarmed. The advisory names desktop-sharing software and an end-of-life operating system as likely weaknesses. Lesson: operator vigilance matters, and remote-access tools are part of the attack surface.

### 20.4 Reading cases carefully

Each source documents some facts and not others. Write what the source says, cite it, and mark everything else as inference. Popular retellings often add certainty the primary report does not have.

### Worked example (synthetic LDHP)

Maya builds a table: case, initial access, effect, what stopped it, LDHP analogue. For the 2021 water case the analogue is LDHP's always-on vendor remote-desktop tool (Chapter 13); for Mirai, the meter gateways' default passwords; for Ukraine, the need to operate after automation is damaged — LDHP keeps documented manual boiler-start procedures.

> **Synthetic case — Lakeside District Heating Plant.** Only the LDHP analogues are synthetic; the three cases come from the cited public sources.

### Errors and limits

Attribution claims in news reports are not part of this chapter's evidence. Case lessons generalise only where the conditions match.

### Exercises

- **EX058 — Primary source details.** From the 2016 ICS-CERT alert, state the approximate number of customers affected and one action the actors took against field devices. *Rubric:* 3 = ~225,000 and corrupted serial-to-Ethernet firmware (or KillDisk on HMIs); 2 = one; 1 = wrong figure; 0 = none.
- **EX059 — Mirai's entry method.** What did Mirai mainly exploit to infect devices and which ETSI provision addresses it? *Rubric:* 3 = default credentials over Telnet; provision 5.1; 2 = one; 1 = "a zero-day"; 0 = none.
- **EX060 — Fact versus inference.** Mark as fact-from-source or inference: (a) "an operator reversed the sodium hydroxide change" (b) "the intruder intended mass poisoning". *Rubric:* 3 = (a) fact from AA21-042A, (b) inference; 2 = one; 1 = both facts; 0 = none.

### Synthesis

Read incidents from primary sources, separate fact from story, and turn each into a concrete question about your own plant.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: system models

### Learning outcomes

You will (1) build a discrete-time model of a tank or loop; (2) explain proportional control and its steady-state offset; (3) use a model to predict how fast a manipulated setpoint changes the process; and (4) state what a simplified model leaves out.

### 21.1 Why model

A model turns "the attacker changes the setpoint" into "the level reaches the overflow alarm in 12 minutes". Defenders use that time to size detection and response: if the process gives 12 minutes, a detector that takes 20 is useless for that scenario.

### 21.2 A buffer tank with proportional control

LDHP's expansion vessel buffers water volume as temperature changes. The lab models its level with a proportional controller that sets inflow to kp·(setpoint − level), clipped to the pump's 0–5 range, against a constant outflow.

```python
"""Lab 21: discrete-time model of a synthetic buffer tank with a proportional level loop."""
level, sp, kp = 40.0, 60.0, 0.08
for step in range(0, 61):
    inflow = max(0.0, min(5.0, kp * (sp - level) * 10))
    outflow = 2.0
    if step % 10 == 0: print(f"t={step:2} level={level:5.1f}% inflow={inflow:4.2f}")
    level += (inflow - outflow) * 0.5
print("steady-state error ~", round(sp - level, 1), "pct (P-only offset)")
```

Run with `python3 lab_tank.py`. Verified output:

```text
t= 0 level= 40.0% inflow=5.00
t=10 level= 55.0% inflow=4.00
t=20 level= 57.5% inflow=2.01
t=30 level= 57.5% inflow=2.00
t=40 level= 57.5% inflow=2.00
t=50 level= 57.5% inflow=2.00
t=60 level= 57.5% inflow=2.00
steady-state error ~ 2.5 pct (P-only offset)
```

### 21.3 Reading the model

The level rises quickly while inflow is saturated at 5, then settles at 57.5 % rather than 60 %. That 2.5-point gap is the classic proportional-only offset: at equilibrium inflow must equal outflow (2.0), which requires a non-zero error (2.0 / 0.8 = 2.5). Integral action removes the offset; engineers usually use PI or PID control.

### 21.4 Using the model for security

If an attacker moves the setpoint from 60 % to 95 %, the model predicts how long the level takes to cross a high alarm at 85 %. The same model tells you how a sensor bias of +10 points would make the controller under-fill the vessel. Models connect cyber actions to process time.

### Worked example (synthetic LDHP)

Using the lab's dynamics, with inflow saturated at 5 and outflow 2, level rises at (5 − 2) × 0.5 = 1.5 points per step. From the 57.5 % steady state to an 85 % alarm is 27.5 points, so about 18–19 steps. If one step represents 20 seconds, operators have roughly six minutes.

> **Synthetic case — Lakeside District Heating Plant.** The tank gains and step length are invented.

### Errors and limits

Real vessels have nonlinear geometry, valve dynamics and measurement noise. A model validated on normal operation may be wrong in the extreme states an attacker seeks. Never derive real plant limits from a classroom model.

### Exercises

- **EX061 — Offset at a higher gain.** If kp = 0.16 (gain ×10 = 1.6), what steady-state offset does the model predict? *Rubric:* 3 = 2.0 / 1.6 = 1.25 points; 2 = right method; 1 = says zero; 0 = none.
- **EX062 — Time to alarm.** Starting at 57.5 % with saturated inflow, how many steps until the level exceeds 70 %? *Rubric:* 3 = 9 steps (57.5 + 1.5 × 9 = 71.0); 2 = 8–9 with reasoning; 1 = ignores outflow; 0 = none.
- **EX063 — Effect of sensor bias.** If the level sensor reads 10 points high, where does the true level settle? *Rubric:* 3 = about 47.5 % (controller holds measured 57.5); 2 = direction right; 1 = 67.5; 0 = none.

### Synthesis

Simple process models give defenders a clock: how long a manipulated loop takes to reach harm, and therefore how fast detection and response must be.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: data and dependencies

### Learning outcomes

You will (1) build an asset and dependency inventory; (2) trace data flows from field device to business use; (3) find single points of failure, including people and suppliers; and (4) use a software bill of materials to reason about inherited vulnerabilities.

### 22.1 Inventory first

You cannot protect what you have not listed. NIST SP 800-82r3 places asset inventory at the start of an OT security programme. A useful inventory records not only make, model and firmware but also function, zone, owner, criticality and what depends on the asset.

### 22.2 Dependency chains

PLC-H depends on 24 V power, its I/O modules, the control network switch, the engineering workstation for logic changes and the vendor for firmware. HMI-1 depends on Windows, the HMI runtime licence server and the domain controller for named accounts. A licence server outage that blanks HMIs is an availability incident with a cyber root cause, even with no attacker.

### 22.3 Supplier dependencies

The meter gateway firmware embeds an open-source TCP/IP stack and a TLS library. If a vulnerability is published in the stack, every gateway inherits it. A software bill of materials (SBOM) lists such components so that, when an advisory appears, the plant can answer "are we affected?" in hours rather than weeks. CISA ICS advisories identify affected products and versions, which only helps if your inventory records versions.

### 22.4 People as dependencies

If only one engineer can restore PLC-H's logic from backup, that person is a single point of failure. Document procedures and cross-train.

### Worked example (synthetic LDHP)

Maya writes the dependency list for the supply-temperature function: TT-101, PLC-H (firmware v3.2), FV-12, control switch SW-2, HMI-1, licence server LIC-1, engineering workstation EWS-1, vendor support contract. She marks LIC-1 as a hidden single point of failure and recommends a licence grace-period check with the HMI vendor.

> **Synthetic case — Lakeside District Heating Plant.** Versions and names are invented.

### Errors and limits

An inventory built only from network scanning misses serial devices and switched-off spares, and active scanning can disturb fragile devices; combine passive capture, configuration exports and walk-downs.

### Exercises

- **EX064 — Fields of an inventory record.** List six fields for an OT asset inventory entry. *Rubric:* 3 = six including firmware version, zone and criticality; 2 = four or five; 1 = make/model only; 0 = none.
- **EX065 — Answering an advisory.** A CISA advisory lists the gateway's TLS library versions 2.0–2.4 as affected. What two inventory facts decide whether LDHP is affected? *Rubric:* 3 = gateway firmware version and its SBOM component version; 2 = one; 1 = vendor name only; 0 = none.
- **EX066 — A hidden single point.** Identify one non-network single point of failure at LDHP and a mitigation. *Rubric:* 3 = e.g. one engineer, licence server, sole spare; with mitigation; 2 = point only; 1 = network device only; 0 = none.

### Synthesis

Inventories, dependency chains and SBOMs let a plant reason about failures and advisories before they arrive.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: methods I

### Learning outcomes

You will (1) perform a consequence-driven risk assessment for one zone; (2) use a likelihood–consequence matrix responsibly; (3) relate the assessment to the IEC 62443-3-2 workflow; and (4) record residual risk with an owner.

### 23.1 Start from consequence

In OT, assessment begins by asking what the process can do that would be unacceptable — loss of heat in winter, over-pressure, scalding — and only then which cyber paths could cause it. Starting from vulnerabilities produces long lists of low-impact findings; starting from consequence focuses effort on the loops that matter.

### 23.2 The 62443-3-2 workflow in outline

IEC 62443-3-2 describes identifying the system under consideration, performing an initial high-level risk assessment, partitioning into zones and conduits, performing a detailed risk assessment per zone, and documenting security requirements and target security levels. You do not need the full standard to practise the reasoning, but cite it correctly.

### 23.3 Matrices and their traps

A 5 × 5 matrix multiplies a likelihood score by a consequence score. It is a communication tool, not arithmetic: "3 × 4 = 12" does not mean twice as bad as 6. Rank-reversal errors happen when categories are wide. Always keep the narrative scenario next to the score.

### 23.4 Residual risk

After controls, some risk remains. It must have an owner who accepts it in writing, a review date and the assumptions it rests on.

### Worked example (synthetic LDHP)

Scenario S-3: office malware reaches PLC-H via rule 14 and lowers the supply setpoint (ATT&CK for ICS T0836). Consequence 4 (district-wide heat loss for hours, no injury because SIS-H handles over-temperature but not under-temperature). Likelihood 3 before controls. After removing rule 14 and adding an allow-list, likelihood 1. Residual: insider with engineering access remains; owner: plant manager; review in six months.

> **Synthetic case — Lakeside District Heating Plant.** Scores are illustrative.

### Errors and limits

Likelihood for targeted attacks is a judgement, not a frequency; state who judged it and on what basis. Do not let a low score hide a catastrophic consequence.

### Exercises

- **EX067 — Consequence first.** Write one unacceptable consequence for the IoT meter zone and the cyber path that could cause it. *Rubric:* 3 = concrete consequence plus path; 2 = one; 1 = vulnerability list; 0 = none.
- **EX068 — Interpreting matrix scores.** Scenario A scores 2 × 5 = 10 and B scores 5 × 2 = 10. Are they equally urgent? *Rubric:* 3 = no; A has catastrophic consequence and needs different treatment; judge by narrative; 2 = "no" only; 1 = yes; 0 = none.
- **EX069 — Residual risk record.** Write the residual-risk statement for S-3 after controls. *Rubric:* 3 = remaining path, owner, review date, assumption; 2 = three; 1 = "risk accepted"; 0 = none.

### Synthesis

Consequence-driven assessment, honest use of matrices and owned residual risk make an OT risk register a decision tool rather than a spreadsheet.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — OT, IoT and cyber-physical security: controls

### Learning outcomes

You will (1) choose preventive, detective and corrective controls for a scenario; (2) map them to IEC 62443-3-3 foundational requirements; (3) recognise controls that could harm availability or safety; and (4) design compensating controls for legacy devices.

### 24.1 Control families

IEC 62443-3-3 groups system requirements under seven foundational requirements: identification and authentication control (FR 1), use control (FR 2), system integrity (FR 3), data confidentiality (FR 4), restricted data flow (FR 5), timely response to events (FR 6) and resource availability (FR 7). Using them as headings keeps a control plan balanced.

### 24.2 Matching controls to S-3

For the setpoint-manipulation scenario: restrict data flow with a firewall allow-list (FR 5); require named accounts on HMI-1 (FR 1); add operator-confirmed setpoint limits in PLC-H logic (FR 3 in effect, and a process control); alert on setpoint writes from any host other than HMI-1 (FR 6); keep tested backups of PLC logic (FR 7).

### 24.3 Controls that hurt

Active intrusion prevention that drops "suspicious" Modbus writes can block a legitimate emergency command. Account lockout after failed logins can lock an operator out during an incident. Each control needs a failure-mode question: if it misfires, what happens to the process?

### 24.4 Legacy and compensating controls

PLC-H's firmware cannot authenticate Modbus clients. The compensating approach is to surround it: allow-list conduits so only HMI-1 and HIST-1 can reach it, monitor traffic passively, and protect the engineering workstation that can change its logic.

### Worked example (synthetic LDHP)

Maya's table has columns: control, FR, prevents/detects/corrects, failure mode, owner. The setpoint-limit row reads: "PLC-H rejects supply setpoints outside 70–110 °C unless engineer mode is active — FR 3 — prevents — failure mode: blocks a legitimate out-of-band change during commissioning; mitigated by engineer mode with logging — owner: control engineering."

> **Synthetic case — Lakeside District Heating Plant.** Limits and owners are invented.

### Errors and limits

Controls listed but not tested provide no assurance. Mapping to FRs shows coverage of categories, not that a requirement is satisfied at the target security level.

### Exercises

- **EX070 — Mapping a meter-zone control.** Give one control for each of FR 1, FR 5 and FR 6 in the meter zone. *Rubric:* 3 = three relevant controls correctly mapped; 2 = two; 1 = one; 0 = none.
- **EX071 — Asking the failure-mode question.** What is the failure mode of locking HMI accounts after three bad passwords, and a safer alternative? *Rubric:* 3 = operator locked out in emergency; alert-and-delay or exempt control-room consoles with physical security; 2 = one; 1 = vague; 0 = none.
- **EX072 — Compensating for a device that cannot authenticate.** List three compensating controls for a meter gateway that cannot change its default password. *Rubric:* 3 = isolate, restrict management interface, monitor, plan replacement (any three); 2 = two; 1 = one; 0 = none.

### Synthesis

A good OT control plan covers all seven foundational requirements, asks how each control fails, and surrounds what cannot be fixed.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) run a reproducible detector experiment with fixed seeds; (2) compare a fixed band against a CUSUM detector on false alarms, detection and delay; (3) report results with denominators; and (4) connect results to the evaluation critique in Urbina et al. (2016).

### 25.1 The experiment

The lab simulates LDHP's supply temperature at 90 °C with Gaussian noise (σ = 1 °C). In attack runs, starting at sample 100 a slow ramp adds 0.08 °C per sample — a stealthy setpoint drift in the spirit of ATT&CK for ICS T0836. The band detector alarms when the reading leaves 90 ± 3.5 °C. CUSUM accumulates positive deviations minus a slack of 0.5 °C and alarms above 12.

```python
"""Lab 25: compare a fixed band and a CUSUM detector on synthetic supply temperature."""
import random
def run(seed, attack):
    rnd = random.Random(seed); s = 0.0; band = cus = None
    for t in range(200):
        x = 90 + rnd.gauss(0, 1.0) + (0.08 * (t - 100) if attack and t >= 100 else 0)
        if band is None and abs(x - 90) > 3.5: band = t
        s = max(0.0, s + (x - 90) - 0.5)
        if cus is None and s > 12: cus = t
    return band, cus
fa_b = sum(run(s, False)[0] is not None for s in range(40)); fa_c = sum(run(s, False)[1] is not None for s in range(40))
det = [run(1000 + s, True) for s in range(40)]
db = [b for b, _ in det if b is not None and b >= 100]; dc = [c for _, c in det if c is not None and c >= 100]
print(f"band : false alarms {fa_b}/40, detections {len(db)}/40, mean delay {sum(b-100 for b in db)/max(1,len(db)):.1f}")
print(f"cusum: false alarms {fa_c}/40, detections {len(dc)}/40, mean delay {sum(c-100 for c in dc)/max(1,len(dc)):.1f}")
```

Run with `python3 lab_detect.py`. Verified output:

```text
band : false alarms 9/40, detections 37/40, mean delay 28.8
cusum: false alarms 0/40, detections 40/40, mean delay 23.1
```

### 25.2 Interpreting the output

On 40 quiet runs the band raised false alarms in 9 runs — with σ = 1 °C, a single sample beyond 3.5 σ is rare but over 200 samples per run it happens — while CUSUM raised none. Against the ramp, CUSUM detected all 40 runs with a mean delay of 23.1 samples; the band detected 37 of 40 (counting only alarms at or after sample 100) with a mean delay of 28.8. Because the band also fires on noise, some of its "detections" are lucky noise excursions.

### 25.3 Honest reporting

Write: "CUSUM 0/40 false-alarm runs (Wilson 95 % upper ≈ 8.8 %), 40/40 detections, mean delay 23.1 samples, seeds 0–39 quiet and 1000–1039 attack." Do not write "CUSUM is perfect". Urbina et al. would also ask how large a ramp an attacker could sustain below CUSUM's threshold — a smaller slope might evade it for far longer.

### Worked example (synthetic LDHP)

Maya halves the attack slope to 0.04 °C/sample in a copy of the script and records the change in delay, keeping the seeds. This turns one result into a curve and shows the attacker's trade-off between speed and stealth.

> **Synthetic case — Lakeside District Heating Plant.** All data are simulated; seeds make the output reproducible.

### Errors and limits

Gaussian, independent noise is optimistic. Thresholds were set by hand on the same data family they are evaluated on.

### Exercises

- **EX073 — Reading false-alarm runs.** State the band detector's false-alarm count and give a 95 % upper bound for CUSUM's. *Rubric:* 3 = 9/40 band; CUSUM 0/40 with ≈7.5–8.8 % upper; 2 = one; 1 = "CUSUM 0 %"; 0 = none.
- **EX074 — Why a slack term?** Explain the role of the 0.5 °C slack in CUSUM. *Rubric:* 3 = subtracts expected noise so the sum drifts to zero under normal operation and grows only under sustained shift; 2 = partial; 1 = "reduces alarms"; 0 = none.
- **EX075 — Applying the stealth critique.** Describe one additional experiment inspired by Urbina et al. *Rubric:* 3 = sweep attack slope/size to find the largest undetected impact within a time window; 2 = vary threshold; 1 = more seeds only; 0 = none.

### Synthesis

A laboratory result is a count over seeds with bounds and an attacker model; changing the attacker is the next experiment, not an afterthought.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: methods II

### Learning outcomes

You will (1) apply STRIDE-style threat modelling to a data-flow diagram of the meter system; (2) translate threats into ATT&CK for ICS techniques where applicable; (3) write abuse cases with preconditions; and (4) prioritise mitigations against the consequence ranking from Chapter 23.

### 26.1 Data-flow diagrams

Draw processes (circles), data stores (parallel lines), external entities (boxes) and data flows (arrows), then mark trust boundaries where data crosses from one zone to another. LDHP's meter system: meters → gateway (radio) → gateway → billing cloud (TLS) → cloud → billing database → historian replica (one-way export for network balancing).

### 26.2 STRIDE per element

Spoofing, Tampering, Repudiation, Information disclosure, Denial of service and Elevation of privilege give a prompt list. At the meter–gateway radio link: spoofing (a fake meter), tampering (altered readings), information disclosure (household consumption). At the gateway: elevation of privilege via its web interface. STRIDE was designed for software, so add an OT prompt: *physical consequence* — can this threat change heat delivery?

### 26.3 Abuse cases

An abuse case states actor, precondition, action and outcome. "A tenant with radio equipment and knowledge of the meter protocol (precondition: no message authentication on the radio link) replays last month's lower readings (action) so that the bill is reduced (outcome)." Writing preconditions makes the mitigation obvious: authenticate readings and use counters, as in Chapter 17.

### 26.4 Mapping to ATT&CK

Not every IoT threat has an ATT&CK for ICS technique, and that is fine. Where it does — gateway reached from the internet (T0883), remote services abused (T0886) — record the ID to link with threat intelligence.

### Worked example (synthetic LDHP)

Maya's table yields 14 threats. Ranked by consequence, the top three are: gateway takeover pushing malicious configuration to all meters in its street; tampering with readings in transit; cloud account compromise exposing every household's history. Replay by one tenant ranks lower: real, but limited to one bill.

> **Synthetic case — Lakeside District Heating Plant.** The threat list is an exercise output, not an assessment of a real product.

### Errors and limits

A threat model is only as complete as its diagram. STRIDE lists threats, not likelihood. Re-run the model when the architecture changes.

### Exercises

- **EX076 — STRIDE at the trust boundary.** Name one threat for each of S, T and D at the gateway-to-cloud flow. *Rubric:* 3 = three plausible threats; 2 = two; 1 = one; 0 = none.
- **EX077 — Writing an abuse case.** Write an abuse case for the gateway's web interface. *Rubric:* 3 = actor, precondition, action, outcome; 2 = three; 1 = vague; 0 = none.
- **EX078 — Ranking replay below gateway takeover.** Justify the ranking. *Rubric:* 3 = scope of impact (one bill vs a whole street/configuration) and consequence; 2 = partial; 1 = "less likely" only; 0 = none.

### Synthesis

Threat modelling turns a diagram into a ranked list of abuse cases whose preconditions point directly to mitigations.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — OT, IoT and cyber-physical security: verification

### Learning outcomes

You will (1) write test vectors for an allow-list policy; (2) include boundary, negative and unknown-source cases; (3) run conformance tests offline before any deployment; and (4) explain why verification evidence is part of the IEC 62443 lifecycle.

### 27.1 Policies need tests

A firewall or protocol-aware allow-list is code, even when written as rules. Verification means showing, with recorded evidence, that the policy permits what operations need and blocks what it should. IEC 62443-4-1 (secure product development lifecycle) and the system integrator's commissioning activities both expect documented testing.

### 27.2 Designing vectors

Good vectors include: each permitted (source, function) pair; each boundary of a register range (first, last, one past last); a permitted source using a forbidden function; an unknown source; and a write function the plant never uses (16, write multiple). Expected results are written before running the test.

```python
"""Lab 27: conformance test of a Modbus allow-list against a test vector table."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}
WRITE_RANGE = range(100, 120)
def permit(src, fc, reg):
    if (src, fc) not in ALLOW: return "BLOCK"
    if fc == 6 and reg not in WRITE_RANGE: return "BLOCK"
    return "PASS"
vectors = [("HMI-1", 3, 100, "PASS"), ("HMI-1", 6, 119, "PASS"), ("HMI-1", 6, 120, "BLOCK"),
           ("HIST-1", 6, 105, "BLOCK"), ("ENG-WS", 16, 100, "BLOCK"), ("HIST-1", 4, 10, "PASS")]
fails = 0
for src, fc, reg, want in vectors:
    got = permit(src, fc, reg); fails += got != want
    print(f"{src:6} fc={fc:2} reg={reg:3} want={want:5} got={got:5} {'ok' if got == want else 'FAIL'}")
print("failures:", fails, "of", len(vectors))
```

Run with `python3 lab_allow.py`. Verified output:

```text
HMI-1  fc= 3 reg=100 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=119 want=PASS  got=PASS  ok
HMI-1  fc= 6 reg=120 want=BLOCK got=BLOCK ok
HIST-1 fc= 6 reg=105 want=BLOCK got=BLOCK ok
ENG-WS fc=16 reg=100 want=BLOCK got=BLOCK ok
HIST-1 fc= 4 reg= 10 want=PASS  got=PASS  ok
failures: 0 of 6
```

### 27.3 Reading the result

All six vectors match. Notice vector 3: register 120 is one past the end of `range(100, 120)`, so it must block — the classic off-by-one boundary. Vector 4 confirms the historian cannot write even within the writable range. A clean run is evidence for these six cases only; it says nothing about function code 23 (read/write multiple) unless you add it.

### 27.4 From lab to plant

Before deploying a policy to LDHP's control-zone firewall, the same vectors are replayed in a bench environment with the actual device, in monitor mode first, and the result attached to the change ticket.

### Worked example (synthetic LDHP)

A colleague proposes extending HMI-1's writable range to include register 120 (a new pump speed setpoint). Maya first changes the expected result of vector 3 to PASS, adds vector (HMI-1, 6, 121, BLOCK), then edits `WRITE_RANGE` to `range(100, 121)`, and reruns. The test change is reviewed alongside the policy change.

> **Synthetic case — Lakeside District Heating Plant.** Register numbers are invented.

### Errors and limits

Tests written after the code tend to confirm what the code does, not what the plant needs. Offline conformance does not prove device performance under load.

### Exercises

- **EX079 — A missing function code.** Add a vector for (HMI-1, 23, 105). What should it expect and what does the lab return? *Rubric:* 3 = expect BLOCK; lab returns BLOCK because (HMI-1, 23) not in ALLOW; 2 = one; 1 = PASS; 0 = none.
- **EX080 — Boundary after the range change.** After `WRITE_RANGE = range(100, 121)`, list the two boundary vectors you would keep. *Rubric:* 3 = reg 120 PASS and reg 121 BLOCK; 2 = one; 1 = 119 only; 0 = none.
- **EX081 — Writing expectations first.** Why write expected results before running? *Rubric:* 3 = avoids confirming code behaviour; ties tests to operational requirement; 2 = partial; 1 = "good practice"; 0 = none.

### Synthesis

Verification is a written list of expected decisions, including boundaries and unknowns, run before deployment and kept as evidence.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — OT, IoT and cyber-physical security: failure analysis

### Learning outcomes

You will (1) build a fault tree for loss of district heat; (2) combine AND and OR gates with simple probabilities; (3) add cyber-induced events to a safety-style analysis; and (4) use failure modes and effects analysis (FMEA) for an IoT gateway.

### 28.1 Fault trees

A fault tree starts with an undesired top event and decomposes it into causes joined by gates. An OR gate means any child causes the parent; an AND gate needs all children. For independent events, P(OR) ≈ sum of probabilities when they are small, and P(AND) = product.

### 28.2 Adding cyber events

Top event: loss of heat to the district for more than four hours. OR children: (a) both boilers trip and cannot restart; (b) circulation pumps stop; (c) supply setpoint manipulated and not detected for four hours. Event (c) is itself an AND: unauthorised setpoint write *and* operators fail to notice *and* the detector fails. Cyber events break the independence assumption: one intruder can cause several "independent" failures at once, so treat common-cause carefully.

### 28.3 FMEA for the gateway

FMEA lists each component, its failure modes, effects, detection and severity. Gateway failure modes include power loss (readings missing — detected by heartbeat), corrupted firmware (malformed data — detected by validation), configuration tampering (plausible false readings — hard to detect), and certificate expiry (uplink refused — detected by monitoring).

### Worked example (synthetic LDHP)

Annual probabilities (illustrative): unauthorised write 0.05; operators miss it for four hours 0.2; detector misses 0.1. P(c) = 0.05 × 0.2 × 0.1 = 0.001. Boilers both fail to restart 0.002; pumps 0.003. P(top) ≈ 0.002 + 0.003 + 0.001 = 0.006 per year. But if the intruder can also suppress HMI alarms, "operators miss" is no longer 0.2 and the AND gate's independence collapses — P(c) may approach 0.05 × 1 × 0.1 = 0.005.

> **Synthetic case — Lakeside District Heating Plant.** All probabilities are invented for illustration and should not be reused.

### 28.4 Bow-tie view

A bow-tie diagram places the top event in the centre, threats and preventive barriers on the left, and consequences with mitigating barriers on the right. It helps operators see that SIS-H is a mitigating barrier for over-temperature but offers nothing for under-temperature caused by a lowered setpoint.

### Errors and limits

Probabilities for adversarial events are judgements; present them as ranges. Fault trees miss interactions not drawn.

### Exercises

- **EX082 — Computing a cyber AND gate.** With write 0.1, operators miss 0.3, detector misses 0.2, compute P(c). *Rubric:* 3 = 0.006; 2 = method right; 1 = sums instead; 0 = none.
- **EX083 — Common cause.** Explain how one intrusion can break the AND gate's independence. *Rubric:* 3 = same actor suppresses alarms/blinds detector, so events correlated; 2 = partial; 1 = vague; 0 = none.
- **EX084 — An FMEA line.** Write the FMEA row for gateway certificate expiry. *Rubric:* 3 = mode, effect, detection, severity, action; 2 = four; 1 = mode only; 0 = none.

### Synthesis

Fault trees and FMEA bring cyber events into reliability engineering — provided you challenge the independence that adversaries are paid to break.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — OT, IoT and cyber-physical security: operations

### Learning outcomes

You will (1) design an OT security monitoring workflow with operators in the loop; (2) write an incident-response playbook step that respects process safety; (3) plan patching within maintenance windows; and (4) run a tabletop exercise.

### 29.1 Monitoring that operators trust

Passive network monitoring at LDHP's control switch builds a baseline of who talks to whom. Alerts — a new host talking Modbus, a write from an unexpected source, a firmware download — go to a security analyst who calls the shift lead before anyone touches the plant. NIST SP 800-82r3 stresses that OT incident response must be coordinated with operations because containment actions can themselves cause a process upset.

### 29.2 Playbook steps

Good OT playbook steps name the decision-maker and the safe state. "Isolate PLC-H from the network" is dangerous if operators lose the HMI. Better: "Shift lead decides whether to move the boiler to local manual control; only then does the analyst block the suspicious source at the firewall."

### 29.3 Patching in windows

LDHP has a monthly four-hour maintenance window. Patches are tested on a bench HMI, ranked by risk (exposure × consequence), and applied in order until the window is full; the rest are deferred with a dated ticket and compensating controls. IEC TR 62443-2-3 discusses patch management in IACS environments.

### 29.4 Tabletop exercises

A tabletop rehearses a scenario on paper: who is called, what is decided, what information is missing. It reveals gaps without risking the process.

### Worked example (synthetic LDHP)

Tabletop scenario: at 02:10 on a January night the monitor alerts "Modbus write to PLC-H register 100 from 10.20.4.17 (office VLAN)". Walkthrough: analyst calls shift lead (02:12); operator confirms supply setpoint changed to 30 °C and restores 90 °C (02:15); shift lead approves blocking 10.20.4.17 at the firewall (02:18); evidence collection begins. Gap found: nobody had the firewall administrator's night phone number.

> **Synthetic case — Lakeside District Heating Plant.** Times, addresses and the gap are invented.

### Errors and limits

Playbooks rot as staff and networks change; review them after every exercise. Automatic blocking in OT should be exceptional and pre-agreed.

### Exercises

- **EX085 — Rewriting a dangerous playbook step.** Rewrite "Shut down the SCADA server immediately" safely. *Rubric:* 3 = decision-maker, safe process state first, then containment; 2 = partial; 1 = unchanged; 0 = none.
- **EX086 — Filling a window.** Patches need 1.5 h (risk 9), 2 h (risk 6), 1 h (risk 8), 1 h (risk 3) in a 4 h window. Which go in? *Rubric:* 3 = risk 9, 8 and 3 (3.5 h) with the risk-6 patch deferred on a dated ticket; 2 = right set, no deferral record; 1 = overruns the window; 0 = none.
- **EX087 — Tabletop gap fix.** Propose a fix for the missing phone number and how to test it. *Rubric:* 3 = on-call roster in playbook plus test call in next exercise; 2 = one; 1 = vague; 0 = none.

### Synthesis

OT operations security keeps operators in charge of the process, patches by risk within windows, and rehearses until gaps are found on paper rather than at 2 a.m.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) assess a synthetic IoT fleet against selected ETSI EN 303 645 provisions; (2) report per-device and fleet-wide gaps; (3) relate the provisions to the NIST IR 8259 manufacturer activities; and (4) prioritise remediation.

### 30.1 The baseline

ETSI EN 303 645 V2.1.1 sets 13 cyber security provisions for consumer IoT, plus data-protection provisions. This lab checks four: 5.1 (no universal default passwords), 5.2 (implement a means to manage reports of vulnerabilities), 5.3 (keep software updated) and 5.5 (communicate securely). NIST IR 8259 covers similar ground from the manufacturer's process side — for example planning for updates and communicating with customers.

```python
"""Lab 30: score a synthetic IoT meter fleet against selected ETSI EN 303 645 provisions."""
fleet = {"MTR-A": {"unique_pw": True, "vuln_policy": True, "update": True, "tls": True},
         "MTR-B": {"unique_pw": False, "vuln_policy": True, "update": True, "tls": True},
         "MTR-C": {"unique_pw": True, "vuln_policy": False, "update": False, "tls": False}}
PROV = {"unique_pw": "5.1 no universal default passwords", "vuln_policy": "5.2 vulnerability disclosure",
        "update": "5.3 software updatable", "tls": "5.5 secure communication"}
for dev, f in fleet.items():
    miss = [PROV[k] for k, v in f.items() if not v]
    print(f"{dev}: {4-len(miss)}/4 met; missing: {miss or 'none'}")
print("fleet-wide gaps:", sorted({k for f in fleet.values() for k, v in f.items() if not v}))
```

Run with `python3 lab_fleet.py`. Verified output:

```text
MTR-A: 4/4 met; missing: none
MTR-B: 3/4 met; missing: ['5.1 no universal default passwords']
MTR-C: 1/4 met; missing: ['5.2 vulnerability disclosure', '5.3 software updatable', '5.5 secure communication']
fleet-wide gaps: ['tls', 'unique_pw', 'update', 'vuln_policy']
```

### 30.2 Reading the fleet result

MTR-A meets all four. MTR-B fails 5.1 only — fixable by forcing unique credentials at installation. MTR-C fails three provisions: no disclosure policy, no update mechanism and no secure communication. The fleet-wide gap list contains all four provisions, which looks alarming but is driven by just two models; report both views.

### 30.3 Prioritising

Severity depends on consequence and fixability. MTR-C's lack of update capability is structural — it cannot be patched — so replacement planning starts now. MTR-B's default password is the classic Mirai vector (Chapter 20) and is urgent but cheap.

### 30.4 Limits of checklist assessment

"Meets 5.3" in this lab is a boolean from a questionnaire. A real assessment checks evidence: does the update mechanism verify signatures, and are updates actually published?

### Worked example (synthetic LDHP)

Maya's remediation table: MTR-B — reset unique passwords during next meter read visit, 2 weeks. MTR-C — isolate behind gateway with TLS termination as a compensating control for 5.5, request vendor disclosure contact, schedule replacement within 12 months because 5.3 cannot be met. MTR-A — no action, re-check on firmware change.

> **Synthetic case — Lakeside District Heating Plant.** Device models and answers are invented.

### 30.5 Reproducing and extending the lab

Change one device's dictionary at a time and rerun, recording the output beside the edit. If two students get different results from the same dictionaries, compare Python versions and the exact file; the script is deterministic and should never differ.

### Errors and limits

ETSI EN 303 645 targets consumer devices; district meters may fall under other regimes. The four provisions checked are a subset.

### Exercises

- **EX088 — Adding a provision.** Add `"secure_storage"` mapped to 5.4 with MTR-A True, MTR-B True, MTR-C False. What does MTR-C now print? *Rubric:* 3 = spots the hard-coded 4 (prints 0/4), fixes it and gets 1/5 with four provisions missing; 2 = one of the two; 1 = says 1/4; 0 = none.
- **EX089 — Why fleet-wide gaps mislead.** Explain why "fleet-wide gaps: all four" could mislead a manager. *Rubric:* 3 = two models cause it; per-device view shows most issues in MTR-C; 2 = partial; 1 = vague; 0 = none.
- **EX090 — Evidence for 5.3.** What evidence would you request from a vendor to accept "software updatable"? *Rubric:* 3 = signed update mechanism, published update history/support period, test of update on bench; 2 = two; 1 = vendor says yes; 0 = none.

### Synthesis

Baseline assessments are useful when reported per device and fleet, backed by evidence, and turned into a dated remediation plan.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — OT, IoT and cyber-physical security: advanced cases

### Learning outcomes

You will (1) analyse a modular ICS attack framework from a CISA advisory; (2) distinguish capability from observed use; (3) derive detection opportunities from documented behaviour; and (4) compare a capability-focused advisory with an incident report.

### 31.1 Tools targeting ICS/SCADA devices

CISA, with partner agencies, published advisory AA22-103A in April 2022, warning that advanced persistent threat actors had developed custom tools able to scan for, compromise and control certain Schneider Electric PLCs, OMRON Sysmac NEX PLCs and OPC UA servers once they had access to the OT network. The same advisory describes a tool that exploited a vulnerable ASRock motherboard driver to compromise Windows-based engineering workstations.

### 31.2 Capability is not incident

Unlike the 2015 Ukraine alert, AA22-103A does not describe a disruption at a named victim. It describes capability. The right response is preparation: inventory affected product families, restrict engineering protocols to engineering workstations, monitor for unexpected connections, and protect workstation drivers. The advisory's mitigations include isolating ICS networks, enforcing multifactor authentication for remote access and monitoring for unusual drivers.

### 31.3 From behaviour to detection

Documented behaviour suggests specific detections: a new host speaking a PLC vendor's engineering protocol; program upload or download outside a change window (ATT&CK for ICS T0843 *Program Download*); OPC UA sessions from hosts other than known clients; loading of a known-vulnerable signed driver on a workstation.

### 31.4 Comparing case types

Incident reports teach what happened under real constraints; capability advisories teach what could happen next. Both are needed, and neither replaces your own inventory.

### Worked example (synthetic LDHP)

LDHP uses no product families named in AA22-103A. Maya does not stop there: she notes that the OPC UA server on HIST-1 is a generic exposure, adds "OPC UA sessions from non-approved clients" to monitoring, and adds "driver load events on EWS-1" to the workstation log forwarding list.

> **Synthetic case — Lakeside District Heating Plant.** LDHP's product mix is invented; AA22-103A is a real advisory.

### Errors and limits

Advisories are snapshots; check for updates. Do not download or run tools named in advisories outside an authorised, isolated research environment.

### Exercises

- **EX091 — Advisory scope.** Name the two PLC vendor families and the server type listed in AA22-103A. *Rubric:* 3 = Schneider Electric, OMRON (Sysmac NEX), OPC UA servers; 2 = two; 1 = one; 0 = none.
- **EX092 — A detection from T0843.** Write one detection rule idea based on program download behaviour. *Rubric:* 3 = alert on program download to PLC outside an approved change window or from a non-engineering host; 2 = partial; 1 = "monitor PLCs"; 0 = none.
- **EX093 — Not affected, still acting.** Why act on an advisory naming products you do not own? *Rubric:* 3 = techniques transfer (OPC UA, workstation drivers, engineering protocols); inventory may be incomplete; 2 = one; 1 = "to be safe"; 0 = none.

### Synthesis

Advanced-case analysis means reading advisories for behaviour, translating behaviour into detections, and refusing to conclude "not us" from a product list alone.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — OT, IoT and cyber-physical security: interdisciplinary interfaces

### Learning outcomes

You will (1) explain how security work interfaces with process safety, operations, procurement and law; (2) write security requirements for a procurement specification; (3) participate in a combined safety–security review; and (4) communicate with non-security professionals using their terms.

### 32.1 Safety engineers

Process safety teams run hazard and operability studies (HAZOP) and determine safety integrity levels for safety instrumented functions under IEC 61511. A security engineer joins to ask, for each hazard, whether a cyber cause could initiate it or disable the protection layer. The output is shared: a hazard log that lists cyber causes next to equipment failures.

### 32.2 Procurement

The cheapest time to fix security is before purchase. A specification can require IEC 62443-4-2 capabilities at a stated security level, ETSI EN 303 645 conformance for consumer-type devices, an SBOM, a vulnerability disclosure process, a defined support period and signed firmware. Without these clauses the plant inherits whatever the vendor ships.

### 32.3 Operations and maintenance

Operators judge any change by its effect on their shift. Present security changes in their terms: "this firewall change means the historian trend screen updates every 10 s instead of 2 s." Maintenance technicians need procedures that fit their tools; requiring a laptop they do not carry fails silently.

### 32.4 Law and regulation

Depending on jurisdiction, district heating may be regulated as critical infrastructure with incident-reporting duties. Security staff must know reporting deadlines and who reports. This book gives orientation, not legal advice.

### Worked example (synthetic LDHP)

In LDHP's HAZOP review of "high supply temperature", the existing causes were controller failure and valve stuck open. Maya adds "setpoint manipulated via unauthorised network write" as a cause, with existing safeguard SIS-H high-temperature trip (independent transmitter, hardwired) and a recommended additional safeguard: PLC-H setpoint limits (Chapter 24).

> **Synthetic case — Lakeside District Heating Plant.** The HAZOP node and recommendations are invented.

### Errors and limits

A security engineer is not qualified to change SIL determinations; recommend and let the safety team decide. Procurement clauses need verification at delivery.

### Exercises

- **EX094 — Three procurement clauses.** Write three security clauses for LDHP's next meter gateway purchase. *Rubric:* 3 = three specific, verifiable clauses; 2 = two; 1 = "must be secure"; 0 = none.
- **EX095 — A cyber cause in HAZOP.** For the node "low circulation flow", add one cyber cause and its safeguard. *Rubric:* 3 = plausible cyber cause plus independent safeguard; 2 = cause only; 1 = equipment failure; 0 = none.
- **EX096 — Explaining a change to operators.** Explain enforcing allow-listing on HMI-1 in operator terms. *Rubric:* 3 = what they see, what to do if blocked, who to call; 2 = two; 1 = jargon; 0 = none.

### Synthesis

OT security succeeds through other disciplines: safety reviews, procurement clauses, operator-centred changes and awareness of legal duties.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) design a replicable simulation study with pre-registered hypotheses; (2) choose sample sizes for proportion estimates; (3) report effect sizes and intervals rather than only significance; and (4) write a threats-to-validity section that a reviewer will accept.

### 33.1 Pre-registration

Writing hypotheses, measures, analysis and stopping rules before running the experiment prevents tuning the analysis to the result. For a detector study: "H1: CUSUM's false-alarm proportion over 300 quiet runs will be lower than the band's; primary measure: runs with any false alarm; analysis: difference in proportions with 95 % interval."

### 33.2 Sample size for a proportion

To estimate a proportion near p with 95 % margin of error E, n ≈ 1.96² p(1−p)/E². For p = 0.2 and E = 0.05, n ≈ 246. To claim a rate below 1 % when none are observed, the rule of three needs n ≈ 300.

### 33.3 Effect sizes

"p < 0.05" says little about size. Report the difference: band 22.5 % vs CUSUM 0 % false-alarm runs, difference 22.5 points (interval computed). Readers can then decide whether it matters operationally.

### 33.4 Replication package

Publish code, seeds, parameters, Python version and the exact command. In this book, labs embed their verified output so a reader can check a rerun matches.

### Worked example (synthetic LDHP)

Maya's capstone pre-registration fixes: 300 quiet and 300 attack seeds, three attack slopes, threshold chosen on a separate tuning set of 50 seeds and then frozen. Primary outcome: detection within 60 samples. She also states what result would falsify H1.

> **Synthetic case — Lakeside District Heating Plant.** The plan is for a simulated study.

### 33.5 Negative results

If CUSUM does not beat the band at the frozen threshold, that is a publishable finding in a bachelor's thesis provided the method was sound. Report it with the same intervals you would have used for a positive result, and discuss which assumption — noise model, attack slope or threshold choice — most likely explains it. Hiding a negative result and re-running with new settings until something "works" is the practice pre-registration exists to prevent.

### 33.6 Version control as a lab notebook

Commit the pre-registration file before the first experimental run, and commit results with the exact command that produced them. The commit history then shows the order of decisions, which is what an examiner checks when a result looks surprisingly clean.

### Errors and limits

Simulation studies replicate easily but may not transfer to plants. Multiple comparisons inflate false discoveries; adjust or pre-declare a primary outcome.

### Exercises

- **EX097 — Sample size for 10 % ± 3 %.** Compute n to estimate a proportion near 0.10 with ±0.03 at 95 %. *Rubric:* 3 ≈ 385; 2 = method; 1 = uses E = 3; 0 = none.
- **EX098 — Why freeze thresholds?** Explain why the threshold is tuned on separate seeds. *Rubric:* 3 = avoids overfitting to evaluation data; unbiased estimate; 2 = partial; 1 = vague; 0 = none.
- **EX099 — A falsifying outcome.** State the result that would falsify H1. *Rubric:* 3 = CUSUM false-alarm proportion ≥ band's (interval includes or exceeds zero difference); 2 = partial; 1 = "if CUSUM fails"; 0 = none.

### Synthesis

Rigour in applied OT research comes from pre-registration, adequate samples, effect sizes with intervals and complete replication packages.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two architectures for remote vendor access against explicit criteria; (2) build a weighted decision matrix and test its sensitivity; (3) document assumptions per option; and (4) recommend with residual risk.

### 34.1 The two options

Option A — persistent VPN from the vendor to a jump host in LDHP's DMZ, with MFA. Option B — on-demand brokered sessions: the shift lead enables a session for a ticket, the vendor connects through a cloud broker to the jump host, the session is recorded and ends after four hours. Both avoid direct connections to PLC-H.

### 34.2 Criteria

Exposure (how long a path exists), attribution (named users, recording), operational fit (can a vendor help at 3 a.m.?), cost and dependency on third parties. Weights reflect LDHP priorities: exposure 0.3, attribution 0.25, operational fit 0.25, cost 0.1, third-party dependency 0.1.

### 34.3 Scoring

Scores 1–5. A: exposure 2, attribution 3, fit 5, cost 4, dependency 4 → 0.6 + 0.75 + 1.25 + 0.4 + 0.4 = 3.40. B: exposure 5, attribution 5, fit 3, cost 3, dependency 2 → 1.5 + 1.25 + 0.75 + 0.3 + 0.2 = 4.00. B leads.

### 34.4 Sensitivity

Raise operational fit to 0.45 and lower exposure to 0.1: A = 0.2 + 0.75 + 2.25 + 0.4 + 0.4 = 4.00; B = 0.5 + 1.25 + 1.35 + 0.3 + 0.2 = 3.60. The ranking flips, so the recommendation depends on how much the plant values night-time vendor availability. Say so explicitly.

### Worked example (synthetic LDHP)

Maya recommends B with one change to address its weakest criterion: a documented night procedure in which the shift lead can enable a session by phone call to the on-call engineer. She records the residual risk that the cloud broker is a third-party dependency and requests its security attestation.

> **Synthetic case — Lakeside District Heating Plant.** Scores are the student's judgements on invented options.

### 34.5 Evidence for each score

Attach a reason to every number. B's attribution score of 5 rests on session recording and named vendor accounts in the broker; A's exposure score of 2 rests on the VPN being permanently reachable even when no work is scheduled. If a reviewer disputes a score, the evidence column shows exactly what to check, and the sensitivity test shows whether the dispute could change the recommendation at all.

### 34.6 Presenting the comparison

Show the plant manager the matrix, the sensitivity result and one paragraph per option describing a night-time support call under each design. Concrete scenarios are easier to judge than weighted totals.

### Errors and limits

Weighted matrices mix judgement with arithmetic; disclose weights and run sensitivity checks. Scores without evidence are opinions.

### Exercises

- **EX100 — Recomputing with equal weights.** Using weight 0.2 for all five criteria, score A and B. *Rubric:* 3 = A 3.6, B 3.6, tie noted; 2 = one right; 1 = arithmetic errors; 0 = none.
- **EX101 — An assumption behind B's exposure score.** Name one assumption behind giving B exposure 5. *Rubric:* 3 = sessions really end, broker cannot open sessions itself, shift lead enabling is enforced; 2 = vague but relevant; 1 = none relevant; 0 = none.
- **EX102 — When to flip the recommendation.** State the condition under which A should be chosen. *Rubric:* 3 = if 24/7 vendor availability outweighs exposure (fit weight high) and A's risk is compensated; 2 = partial; 1 = "if cheaper"; 0 = none.

### Synthesis

Comparative work is honest when criteria, weights, evidence and sensitivity are all visible, and the recommendation states when it would change.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) write a capstone proposal with problem, question, scope, method, ethics and timeline; (2) define deliverables that can be assessed; (3) state safety and authorization boundaries; and (4) obtain supervisor sign-off on scope.

### 35.1 Proposal structure

A capstone proposal for this course has seven parts: problem statement (one paragraph with a cited source), research or design question, scope and exclusions, method, ethics and safety boundaries, deliverables with acceptance criteria, and a timeline with milestones. Keep it under four pages; a supervisor must be able to approve or reject it in one meeting.

### 35.2 Scope that fits

Bachelor's capstones fail more often from scope than from difficulty. "Secure LDHP" is not a capstone. "Design, implement and evaluate a passive Modbus write monitor for LDHP's synthetic control-zone capture, measuring precision and recall on six attack classes" is.

### 35.3 Ethics and safety boundary

The proposal must state: all data are synthetic or provided by an owner under written agreement; no real controller or network will be probed; any tool is passive and offline; results that reveal a real product weakness go through coordinated disclosure. A supervisor signs this section.

### 35.4 Acceptance criteria

Each deliverable needs a check: "the monitor processes the 8-case evaluation set and reports TP/FP/FN/TN with precision and recall" is checkable; "a good tool" is not.

### Worked example (synthetic LDHP)

Maya's proposal. Problem: unauthorised setpoint writes such as those described in ATT&CK for ICS T0836 often go unnoticed by operators (motivated by CISA AA21-042A, where personnel noticed only by watching the screen). Question: how accurately can a rule-based monitor classify Modbus writes in a synthetic capture? Scope: offline, synthetic, Modbus/TCP only. Method: allow-list rules from Chapter 27 plus a rate rule; evaluation set from Chapter 38. Timeline: 12 weeks with milestones at weeks 3, 7 and 10.

> **Synthetic case — Lakeside District Heating Plant.** The capstone uses only synthetic captures.

### Errors and limits

Over-promising metrics in a proposal ("100 % detection") sets up failure. Proposals should anticipate a negative result being acceptable if well evidenced.

### Exercises

- **EX103 — Narrowing a capstone idea.** Rewrite "an AI that protects district heating" into a scoped capstone question. *Rubric:* 3 = data, method, measure, boundary; 2 = three; 1 = still broad; 0 = none.
- **EX104 — The ethics paragraph.** Write the ethics and safety boundary for Maya's project in three sentences. *Rubric:* 3 = synthetic only, no probing, disclosure route; 2 = two; 1 = generic; 0 = none.
- **EX105 — An acceptance criterion.** Write an acceptance criterion for the deliverable "evaluation report". *Rubric:* 3 = specific content and check (confusion matrix, intervals, seeds); 2 = partial; 1 = "complete report"; 0 = none.

### Synthesis

A strong proposal is small, checkable and bounded by explicit ethics — and it allows an honest negative result.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) plan a supervised placement or community project with a utility, school or municipality; (2) agree a written scope that excludes live testing; (3) deliver awareness or inventory work that helps a small operator; and (4) reflect on practice using a structured journal.

### 36.1 What a bachelor's student can safely offer

Small water utilities, schools with building-management systems and community heating co-operatives often lack security staff. A student under supervision can help with documentation-heavy, low-risk work: an asset list from existing records, a review of remote-access arrangements, a password-hygiene checklist, an awareness session for operators. None of these needs touching a live controller.

### 36.2 The agreement

The placement agreement names the host organisation's responsible person, the supervisor, the deliverables, data-handling rules (what leaves the site, how it is stored and when it is deleted) and an explicit prohibition on scanning, probing or configuration changes. If the host asks for "a quick scan", the student refers the request to the supervisor.

### 36.3 Working with small operators

Advice must fit their budget and staff. "Deploy a SOC" is useless to a three-person co-operative; "remove the always-on remote-desktop tool and use the vendor's on-demand session feature, enabled by the manager's phone" is actionable. CISA's free resources for small water and wastewater systems are an example of guidance written for this audience.

### 36.4 Reflective journal

After each visit record: what I did, what I observed, what surprised me, what I would do differently, and any ethical question that arose. Reflection turns activity into learning.

### Worked example (synthetic)

Maya's placement with a fictional village heating co-operative produces a two-page asset list built from invoices and the panel builder's drawings, discovering an undocumented cellular router in the boiler house. Her recommendation: confirm with the panel builder what it is for, disable it if unneeded, and otherwise require the vendor to enable it only on request.

> **Synthetic case — fictional village co-operative.** The co-operative and router are invented.

### Errors and limits

A student is not a consultant; recommendations are reviewed by the supervisor before delivery. Community work must not create dependence the student cannot sustain after the placement.

### Exercises

- **EX106 — Responding to a scan request.** The co-operative manager asks Maya to "run a scan to see if we're hacked". Write her reply. *Rubric:* 3 = declines politely, explains scope, offers safe alternative, refers to supervisor; 2 = three; 1 = agrees with caveats; 0 = runs it.
- **EX107 — Data-handling rule.** Write one data-handling rule for the asset list. *Rubric:* 3 = where stored, who may access, deletion date; 2 = two; 1 = "keep it safe"; 0 = none.
- **EX108 — A journal entry.** Write the "what surprised me" line about the cellular router. *Rubric:* 3 = specific observation and lesson about undocumented paths; 2 = observation only; 1 = generic; 0 = none.

### Synthesis

Field practice lets students help small operators with documentation and judgement, bounded by written agreements that keep live systems untouched.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critically review a published OT security claim; (2) grade evidence quality from anecdote to replicated measurement; (3) check whether conclusions follow from the data presented; and (4) give and receive structured peer review.

### 37.1 A ladder of evidence

From weakest to strongest: vendor marketing claim; single anecdote; case report from a primary source; systematic measurement on one system; measurement replicated across systems or by independent teams. A seminar asks of every claim: which rung is this, and does the conclusion overreach it?

### 37.2 Reading a measurement paper

The Mirai study by Antonakakis et al. (USENIX Security 2017) is a good seminar text: it combines several data sources — network telescope scans, honeypots, DNS data and attack victim data — to estimate infection size and behaviour. Ask: what does each source see and miss? How were infected devices counted when IP addresses change? Which conclusions depend on one source only?

### 37.3 Reading a survey

Giraldo et al. (ACM Computing Surveys, 2018) classify physics-based detection work. A survey's strength is breadth; its risk is that it reports what papers claim rather than re-testing them. Use it to find primary papers and recurring weaknesses, such as inconsistent attacker models.

### 37.4 Structured peer review

Review format: summary in your own words; main strengths; major concerns (validity, missing comparisons, overreach); minor issues; a recommendation. Comment on the work, not the person.

### Worked example (synthetic LDHP)

A classmate's report claims "CUSUM eliminates false alarms in district heating". Maya's review: summary; strength — reproducible script with seeds; major concern — 0/40 synthetic runs support "no false alarms observed, upper bound ≈ 8.8 %", not elimination, and nothing was tested on real plant data; minor — the delay unit (samples) is not converted to minutes; recommendation — revise the claim and add the bound.

> **Synthetic case — Lakeside District Heating Plant.** The classmate's report is invented.

### Errors and limits

Peer review checks reasoning, not truth; reviewers miss errors too. Prestige of a venue is not evidence of correctness.

### Exercises

- **EX109 — Placing claims on the ladder.** Place on the evidence ladder: (a) a vendor brochure saying "blocks 99.9 % of ICS attacks", (b) AA21-042A. *Rubric:* 3 = (a) marketing claim, (b) primary case report; 2 = one; 1 = reversed; 0 = none.
- **EX110 — Questioning a single-source conclusion.** Identify one Mirai-study conclusion that would be weaker if based on honeypot data alone, and why. *Rubric:* 3 = infection size/population estimate; honeypots see only devices that contact them; 2 = partial; 1 = vague; 0 = none.
- **EX111 — Writing a major concern.** Write the major concern for a paper evaluating a detector on one simulated plant with hand-tuned thresholds. *Rubric:* 3 = generalisation and tuning-on-test bias, with requested fix; 2 = one; 1 = style comment; 0 = none.

### Synthesis

Evidence review asks how strong the evidence is, whether the conclusion fits it, and how to say so constructively.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement a capstone artefact in small, tested increments; (2) maintain a change log and decision record; (3) evaluate the artefact on a labelled set with a confusion matrix; and (4) report precision and recall with their denominators.

### 38.1 Increments

Build the smallest end-to-end version first: read a capture file, classify each write, print decisions. Then add rules one at a time, each with tests (Chapter 8) and conformance vectors (Chapter 27). A working small tool in week 4 beats an ambitious one that never runs.

### 38.2 Decision records

When you choose, record why: "Decision 7: treat writes during a scheduled maintenance window as benign-maint only if the ticket ID appears in the window list; alternatives considered: time-only rule (rejected: insiders could time attacks)." Decision records let examiners follow the reasoning.

### 38.3 Evaluation

The lab evaluates a monitor's output on eight labelled cases from Maya's synthetic set.

```python
"""Lab 38: capstone evaluation - precision/recall with denominators (synthetic results)."""
cases = [("replay", True, True), ("replay", True, True), ("setpoint", True, False), ("setpoint", True, True),
         ("benign-maint", False, True), ("benign", False, False), ("benign", False, False), ("drift", True, False)]
tp = sum(a and d for _, a, d in cases); fp = sum((not a) and d for _, a, d in cases)
fn = sum(a and not d for _, a, d in cases); tn = sum((not a) and not d for _, a, d in cases)
print(f"TP={tp} FP={fp} FN={fn} TN={tn}")
print(f"precision={tp}/{tp+fp}={tp/(tp+fp):.2f} recall={tp}/{tp+fn}={tp/(tp+fn):.2f}")
print("missed classes:", sorted({c for c, a, d in cases if a and not d}))
```

Run with `python3 lab_eval.py`. Verified output:

```text
TP=3 FP=1 FN=2 TN=2
precision=3/4=0.75 recall=3/5=0.60
missed classes: ['drift', 'setpoint']
```

### 38.4 Reading the confusion matrix

Three true positives, one false positive (a maintenance write flagged), two false negatives (one setpoint attack and the drift attack missed), two true negatives. Precision 3/4 = 0.75; recall 3/5 = 0.60. Eight cases are far too few for precise rates — a Wilson interval for 3/5 spans roughly 0.23 to 0.88 — so the honest use of this table is to find failure classes, not to rank tools.

### Worked example (synthetic LDHP)

Maya examines the two misses. The drift attack used many small writes, each within the allow-listed range — a rule-based monitor without a rate or trend rule cannot see it. The missed setpoint attack came from HMI-1 itself, which is allow-listed. Both lead to new decision records: add a cumulative-change rule, and correlate HMI writes with operator login events.

> **Synthetic case — Lakeside District Heating Plant.** The eight cases are a toy set for illustration.

### Errors and limits

Labels are only as good as the scenario author; an attack labelled "benign" corrupts every metric. Do not tune rules on the evaluation cases and then report the same numbers.

### Exercises

- **EX112 — Fixing the false positive.** Propose a change that would avoid flagging the maintenance write without hiding real attacks. *Rubric:* 3 = require matching ticket/window and engineer account, still log; 2 = partial; 1 = ignore maintenance hours; 0 = none.
- **EX113 — Recall after one fix.** If the cumulative-change rule catches the drift case and nothing else changes, what is the new recall? *Rubric:* 3 = 4/5 = 0.80; 2 = right number no fraction; 1 = 0.75; 0 = none.
- **EX114 — Why the interval matters.** Explain why the 0.60 recall cannot be compared with another tool's 0.70 on a different 10-case set. *Rubric:* 3 = tiny samples, wide overlapping intervals, different case mix; 2 = one; 1 = "different tools"; 0 = none.

### Synthesis

Implement in tested increments, record decisions, and use small evaluation sets to find failure classes rather than to claim rates.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate a capstone against its own proposal; (2) separate results, interpretation and limitations; (3) run a structured self-assessment against the course rubric; and (4) plan the work a successor would need to do.

### 39.1 Against the proposal

Return to the acceptance criteria written in Chapter 35. For each, record met, partly met or not met, with evidence. A capstone that misses a criterion but explains why — for example, the drift class could not be detected by rules alone — can still earn a strong grade.

### 39.2 Results versus interpretation

Results are what the evaluation produced: "recall 4/5 on the extended set". Interpretation is what you think it means: "the cumulative rule addresses slow manipulation". Limitations bound the interpretation: "tested only on synthetic data with one drift profile". Keeping three headings prevents results from silently absorbing opinion.

### 39.3 Self-assessment rubric

Score yourself 0–3 on: problem framing, method fit, evidence quality, safety and ethics, communication. Write one sentence of evidence per score. Supervisors use the same rubric; differences start a useful conversation.

### 39.4 Successor plan

List what you would do with three more months: a second process model, real (owner-provided) anonymised captures, an operator usability study. Rank by value to the question.

### Worked example (synthetic LDHP)

Maya's evaluation table: criterion 1 (processes 8-case set, reports confusion matrix) — met; criterion 2 (precision and recall with denominators) — met; criterion 3 (detects all six attack classes) — partly met, five of six after the cumulative rule, HMI-originated insider write still missed. Self-assessment: evidence quality 2 ("eight cases is a toy set"), safety 3 ("offline only, documented").

> **Synthetic case — Lakeside District Heating Plant.** Scores are a worked illustration.

### 39.5 The supervisor's view

Supervisors look for alignment between the question, the evidence and the claims. A frequent comment at this stage is that the conclusion section repeats the results instead of answering the research question. Rewrite the conclusion so its first sentence answers the question from Chapter 35 directly, its second states the strongest limitation, and its third names the next study.

### Errors and limits

Self-assessment tends to over-score communication and under-score method fit. Do not re-define acceptance criteria after the fact to fit results.

### Exercises

- **EX115 — Classifying three sentences.** Label as result, interpretation or limitation: (a) "precision 4/5"; (b) "the tool is ready for pilot"; (c) "one drift profile tested". *Rubric:* 3 = R, I, L; 2 = two; 1 = one; 0 = none.
- **EX116 — Scoring evidence quality.** Justify a score of 2 (not 3) for evidence quality in Maya's capstone. *Rubric:* 3 = reproducible and correct but small synthetic set limits generality; 2 = partial; 1 = "could be better"; 0 = none.
- **EX117 — The top successor task.** Which successor task most strengthens the research question and why? *Rubric:* 3 = additional process model or owner-provided captures to test generalisation; 2 = task only; 1 = UI polish; 0 = none.

### Synthesis

Evaluate a capstone against its own promises, keep results apart from opinions, and leave a ranked path for whoever continues the work.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) structure a bachelor's thesis in OT security; (2) design slides that show evidence rather than decoration; (3) prepare for an oral defence with anticipated questions; and (4) publish a replication package responsibly.

### 40.1 Thesis structure

Introduction (problem, question, contribution); background (standards and prior work, cited precisely — NIST SP 800-82r3, the relevant IEC 62443 parts, ATT&CK for ICS techniques, peer-reviewed papers you have read); method; results; discussion including limitations; conclusion and future work; appendices with code and data descriptions. Keep the synthetic label visible in every figure caption that uses LDHP data.

### 40.2 Slides

One message per slide, stated in its title: "Rule-based monitoring missed slow drift; a cumulative rule recovered it". Show the confusion matrix, the denominators and the interval. Avoid hacker imagery and padlock icons; examiners read them as a sign of weak content.

### 40.3 Anticipating questions

Prepare answers for: Why synthetic data? How would this fail on a real plant? What is the false-alarm burden on operators per shift? Why these attack classes? What would an attacker who knows your rules do? Answering "I don't know, but here is how I would find out" is acceptable; inventing numbers is not.

### 40.4 Responsible publication

Publish code, seeds and synthetic data under an open licence. Do not publish anything that is a working attack against real products. If the work found a real vulnerability, publication waits for coordinated disclosure (Chapter 10).

### Worked example (synthetic LDHP)

Maya's defence opens with the one-sentence contribution: "A rule-based Modbus write monitor with a cumulative-change rule detected five of six synthetic attack classes on LDHP captures; the remaining class — writes from a legitimate HMI — requires correlation with operator identity." Her closing slide lists three limitations and the successor plan from Chapter 39.

> **Synthetic case — Lakeside District Heating Plant.** The thesis is a worked illustration on simulated data.

### Errors and limits

A thesis is judged on reasoning and honesty more than on the size of the result. Long literature chapters that summarise without evaluating add pages, not marks.

### Exercises

- **EX118 — A slide title that carries the claim.** Write the title for the slide showing the 4/5 recall result. *Rubric:* 3 = full-sentence claim with qualifier; 2 = claim without qualifier; 1 = "Results"; 0 = none.
- **EX119 — Defending against an informed attacker.** Draft an answer to "what would an attacker who knows your rules do?" *Rubric:* 3 = admits evasion (e.g. via HMI or below cumulative threshold), cites Urbina-style impact budget, proposes defence; 2 = two; 1 = denies; 0 = none.
- **EX120 — What not to publish.** Name one item that should be excluded from the public replication package and why. *Rubric:* 3 = anything usable against real products or any owner-provided data; reason; 2 = item only; 1 = "the code"; 0 = none.

### Synthesis

A thesis ends the course by showing that you can frame an OT security question, answer it with honest evidence, and communicate the answer's limits to people who must act on it.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Lakeside District Heating Plant, Maya Chen and all plant numbers are synthetic. Any answer meeting the rubric scores equally.

**EX001.** 150/3600 = 0.04167 m³/s → 41.67 kg/s; P = 41.67 × 4.19 × 30 ≈ 5,237.5 kW (about 5.2 MW), roughly 1 MW below the 180 m³/h case.

**EX002.** "If the meter gateway can write to PLC-H, then it has a route to the control zone." It is testable because finding any successful write path forces a search for the route, and finding none supports (but does not prove) the original claim.

**EX003.** 6.3 MW × 24 h ≈ 151 MWh per day, so "about 150 MWh/day"; the estimate assumes constant load, which a winter-night profile would violate.

**EX004.** 9 + 4 = 13 ms leaves 7 ms; 7 / 0.6 = 11.67, so at most 11 requests per scan (11 × 0.6 = 6.6 ms → 19.6 ms).

**EX005.** (1) Rebooting to clear a fault → schedule a controlled stop with operators holding the process safe. (2) Installing updates immediately → stage firmware on a bench unit and deploy in a maintenance window with rollback. Disabling services ad hoc or running scanners are also acceptable examples.

**EX006.** The protocol stack is shared by the whole device and parses network input before any user logic executes, so a flaw there can crash or control the controller regardless of which program is loaded; a ladder bug only affects the function that rung implements.

**EX007.** `TT-103 130.0 degC ok` — the comparison `lo <= v <= hi` is inclusive, so a reading exactly at the high limit passes.

**EX008.** `float("n/a")` raises ValueError and the script stops with a traceback before printing the remaining rows. Wrap the conversion in try/except, print `BAD-VALUE` for that tag and add it to the flagged list so a missing value is never silently skipped.

**EX009.** 141 °C is physically possible and may be a real overheat, so the operator must check the process now; −3 m³/h cannot occur on a one-way meter, so it points to wiring, scaling or tampering and belongs to instrumentation with an integrity follow-up.

**EX010.** "HIST-1 accepts inbound connections from the office VLAN on its SQL port (firewall export, 3 March) and holds an outbound session to PLC-H; we did not test whether the office path can reach PLC-H through it."

**EX011.** IEC 62443-4-2 (component security requirements, e.g. authentication of human users on an embedded device) for PLC-H's capability; IEC 62443-2-1 for the asset owner's security programme that includes patch management, with IEC TR 62443-2-3 as the specific patch-management technical report.

**EX012.** "If you see a setpoint change on PLC-H that nobody on shift made, call the control engineer and note the time. Until rule 14 is removed, do not log in to office e-mail from the HMI room PC."

**EX013.** (a) vulnerability; (b) threat source; (c) consequence.

**EX014.** A manipulated setpoint produces immediate physical harm — cold homes or equipment stress — and can be irreversible within minutes, while a meter-data leak harms privacy and must still be prevented under data-protection duties; integrity of control is ranked first because its consequence is physical and time-critical, not because privacy can be neglected.

**EX015.** T0883 Internet Accessible Device. Mapping it shows exposure only; it does not prove anyone has exploited the gateway, nor that the list of mapped techniques covers every way LDHP could be attacked.

**EX016.** MeterCloud → MeterGW → SCADA → Control → SIS (each node has one outgoing edge, so the queue order is unique).

**EX017.** No: after the change Control has no outgoing conduit, so the new Internet→Control edge does not reach SIS. It does, however, expose PLC-level control directly to the internet, which is a severe finding in its own right.

**EX018.** {(HIST-1, PLC-H, read), (HMI-1, PLC-H, read), (HMI-1, PLC-H, write)}.

**EX019.** tid=4, protocol 0, length 6, unit 1, fc=4 (read input registers), starting address 0x0032 = 50, quantity 0x0004 = 4 → a read.

**EX020.** The bytes do not show who sent it or whether that host was authorised, and they do not show that register 100 is the supply setpoint in tenths of a degree — both come from network context and the plant's register map.

**EX021.** 925 (0x039D), because the register holds tenths of a degree Celsius.

**EX022.** "unknown". Function 8 sub-functions include restarting communications or clearing counters, so labelling it "read" would understate its effect; "unknown" forces a human to look.

**EX023.** `self.assertEqual(classify(8), "unknown")` — under the original code this returned "read" and the test would fail.

**EX024.** The git commit hash of the script that produced the result, and a SHA-256 hash (plus capture date) of the exact input file; the Python version is a useful third item.

**EX025.** Twelve regular TT-101 rows are inserted for t = 0, 5, …, 55, and the script appends one extra row (35, 128.0), giving 13.

**EX026.** `select ts from (select ts, lead(ts) over (order by ts) as nxt from h where tag='PT-201') where nxt - ts > 10;` (SQLite ≥ 3.25 supports LEAD; a self-join on the next greater timestamp also works). On the lab data it returns no rows.

**EX027.** With deadband (exception) compression a new value is archived only when it differs from the last archived value by more than the deadband; if a spike rises and falls between two archived points — or the archived point after it falls back within the band — the peak is never stored, so the historian shows a smooth trend.

**EX028.** "If any alarm appears on the LDHP boiler HMI or the switch port shows errors during the capture, stop the capture, remove the tap only with the shift lead's consent, and inform the shift lead and the control engineer immediately."

**EX029.** No. A contractor's manager is not the asset owner; scanning requires written authorization from LDHP (or its delegate) and the operations manager, naming PLC-H, the window, the permitted technique and stop conditions — and active scanning of a live controller would likely be refused in favour of passive methods.

**EX030.** Record the firmware version, input and crash evidence on the bench system without sharing it publicly, then report through the vendor's PSIRT or disclosure policy (and to CISA or the national CERT if the vendor is unresponsive), agreeing a disclosure timeline.

**EX031.** Audit mode logs every executable that would have been blocked without stopping it, so the team can build a complete list of legitimate HMI binaries during real operations; enforcing an untested list could block the HMI runtime and cost operators their view of the process.

**EX032.** Start with a live, read-only export of event logs, process list, network connections and installed software using a named investigation account; take a disk image only if the evidence justifies it, the owner approves the downtime, and a spare or redundant HMI keeps operators in view of the plant.

**EX033.** "Exception HMI-1/SA-01: local service account `hmirt` retained because the vendor runtime requires it (vendor letter ref. V-221). Compensating controls: interactive logon denied, password vaulted and rotated quarterly, logon events forwarded to the SIEM. Owner: control engineering lead. Review: 1 March next year."

**EX034.** 3/150 = 0.02, so roughly a 2 % per-day upper bound at about 95 % confidence; the point estimate of 0 is not a claim of impossibility.

**EX035.** Per 500 days: 0.95 true alerts and 499 × 0.01 = 4.99 false alerts; precision = 0.95 / 5.94 ≈ 0.16, so only about 16 % of alerts are real.

**EX036.** Consecutive days share weather, load and staffing, so a detector's behaviour on day 12 predicts its behaviour on day 13; the observations are positively correlated and the effective sample size is smaller than 40, making the true upper bound larger than 7.5–8.8 %.

**EX037.** A named *view* account on HMI-1 (or the DMZ historian replica), set to expire at the end of the week; no operate or engineer privileges.

**EX038.** (1) Identify the person and the emergency that justified use; (2) review every action taken during the session against logs; (3) rotate and reseal the credential and confirm the alert fired as designed.

**EX039.** Any two of: use multiple-factor authentication; use strong passwords for RDP credentials; audit the network for RDP and close unused RDP ports; log and audit all remote connection attempts; move to a supported operating system.

**EX040.** Any two: when the flat is empty for days (holiday), the residents' wake and sleep times, whether someone works from home, roughly how many people live there.

**EX041.** Daily per-household totals retained for about 60 days: a leak shows as a sustained rise in consumption over days, so daily data detects it, and two months is enough to compare with the previous period before deletion.

**EX042.** The school's consumption is so much larger that the aggregate effectively is the school's profile, revealing its occupancy, while the five flats are too few to form a meaningful crowd; a minimum group size and a dominance check (no single site above, say, 30 % of the total) are needed.

**EX043.** 10:04:10 + 75 s = 10:05:25 reference time.

**EX044.** (a) O — it is a logged observation (after correction); (b) I — inferred from the controller's logic and timing; (c) A — an assumption unless the network capture covering the period was reviewed.

**EX045.** Exporter's name, source system and export method, date and time of export, SHA-256 hash of the file, storage location of the read-only original (plus any later transfers with signatures).

**EX046.** In its own IoT zone attached to the DMZ (roughly level 3.5), because it collects field data like a level 1–2 device yet talks to an external cloud service like a level 4 system; forcing it into the control zone would give the cloud a path to PLC-H.

**EX047.** Rule A: allow HIST-1 (control zone) → HIST-R (DMZ) on the replication port only, initiated from HIST-1. Rule B: allow Enterprise users → HIST-R on HTTPS. Implicit deny blocks any Enterprise → HIST-1 session.

**EX048.** Manipulating PLC-H could interrupt heat to thousands of households in winter, a severe public consequence. Attackers with ICS-specific skills and moderate resources — the kind described in CISA advisory AA22-103A on tools targeting ICS/SCADA devices — are plausible, which is the SL 3 attacker profile.

**EX049.** The receiver's `last` counter is still high, so every new message with counter ≤ last is rejected as a replay and the meter goes silent. Design fix: persist the counter across updates, or include a key-epoch number so a re-keyed meter starts a new counter space that the receiver accepts.

**EX050.** SHA-256 has no secret input: an attacker who changes the reading simply recomputes SHA-256 of the new value, so the receiver sees a matching hash; only a keyed MAC ties the tag to a secret the attacker lacks.

**EX051.** Extracting the key from one physically accessible meter lets an attacker produce valid tags for any meter's readings, so a single compromise undermines billing integrity for the whole district; per-device keys derived from a protected master limit the damage to one meter.

**EX052.** "Of LDHP's 4,000 synthetic meter configurations, what proportion meet ETSI EN 303 645 provisions 5.1, 5.3 and 5.5, and does the proportion differ between the two meter vendors?"

**EX053.** Threat: noise is idealised Gaussian, so results may not hold on real plant data with drift and quantisation. Mitigation: add noise profiles drawn from published process data (or a second simulated model with autocorrelated noise) and report whether the ranking changes.

**EX054.** Urbina et al. evaluate a detector by how much damage an attacker can still do while staying below its alarm threshold, so a detector with fewer false alarms but a large undetectable-impact budget is judged weaker.

**EX055.** Sensor: spoof or bias TT-101's signal. Controller: change PLC-H's setpoint or logic. Actuator: force FV-12 open via a manual override or I/O manipulation. Communication: interrupt or delay the PLC-H ↔ HMI link so operators lose visibility.

**EX056.** (a) NIST IR 8259 (with IR 8259A) or ETSI EN 303 645 for the meter maker; IEC 62443-4-2 if the meter is sold as an industrial component. (b) NIST SP 800-82r3 or IEC 62443-2-1 for LDHP's programme as asset owner.

**EX057.** If SIS-H read the temperature through PLC-H, an attacker who compromised PLC-H or falsified TT-101 would also blind the trip. A separate transmitter wired directly to SIS-H keeps the safety function independent of the control system it protects.

**EX058.** About 225,000 customers were affected; the actors corrupted the firmware of serial-to-Ethernet devices at substations (KillDisk wiping of HMIs is also an acceptable answer).

**EX059.** Factory-default or weak usernames and passwords reachable over Telnet; ETSI EN 303 645 provision 5.1 (no universal default passwords) addresses it.

**EX060.** (a) Fact reported in CISA AA21-042A. (b) Inference — the advisory reports the attempted change, not the intruder's intent.

**EX061.** At equilibrium inflow = outflow = 2.0 = 1.6 × error, so error = 1.25 points; the level settles at about 58.75 %.

**EX062.** Each saturated step adds 1.5 points: after 8 steps 69.5 %, after 9 steps 71.0 %, so 9 steps.

**EX063.** The controller drives the *measured* level to 57.5 %; with a +10 bias the true level is 47.5 % — the vessel is under-filled while the HMI looks normal.

**EX064.** Asset tag and function, make and model, firmware/software version, zone and network address (or serial link), owner, criticality rating (plus location and dependencies).

**EX065.** The firmware version installed on each LDHP gateway and the TLS library version that firmware contains according to its SBOM (or vendor statement); if the library is 2.0–2.4, the gateways are affected.

**EX066.** Only one engineer knows how to restore PLC-H logic from backup; mitigate with a written, tested restore procedure and a second trained engineer. (The HMI licence server or a single spare I/O card are also valid.)

**EX067.** Consequence: forged consumption readings for a whole street produce wrong bills and hide a real leak for weeks. Path: default password on the meter gateway lets an attacker alter readings before they are signed and sent to the cloud.

**EX068.** No. A (rare but catastrophic) may need design changes such as independent safeguards even if unlikely; B (frequent but minor) may be handled operationally. Equal products hide very different situations, so decide using the scenarios, not the number.

**EX069.** "Residual S-3: an insider with engineering credentials on EWS-1 could still change PLC-H setpoints. Assumes named accounts and logging are in place. Accepted by the plant manager; review on 1 April next year or after any change to engineering access."

**EX070.** FR 1: unique per-device credentials and named admin accounts on gateways. FR 5: gateways may open only outbound TLS to the billing cloud; no inbound sessions from it to the control zone. FR 6: alert when a gateway's configuration changes or it contacts an unknown destination.

**EX071.** An operator who mistypes during a stressful upset is locked out exactly when control is needed. Safer: progressive delay and an alert to the shift lead, with lockout disabled on physically secured control-room consoles.

**EX072.** Place it in its own VLAN with a firewall allowing only required flows; block its management interface from everywhere except a jump host; monitor its traffic for new destinations; schedule replacement with a compliant model.

**EX073.** Band: false alarms in 9 of 40 quiet runs. CUSUM: 0 of 40, with a 95 % upper bound of about 7.5 % (rule of three) or 8.8 % (Wilson), so "no false alarms observed", not "never".

**EX074.** The slack (reference value) is subtracted from each deviation so that under normal noise the cumulative sum keeps returning to zero; only a sustained shift larger than the slack makes it grow to the threshold, which suppresses single-sample noise alarms.

**EX075.** Sweep the ramp slope (e.g. 0.005–0.08 °C/sample) and, for each, record the temperature deviation reached before CUSUM alarms; the largest deviation achieved while undetected over a fixed horizon is the stealthy-attack impact metric Urbina et al. recommend.

**EX076.** S: an attacker presents a fake cloud endpoint to the gateway (spoofed server) if certificate validation is weak. T: readings altered on the path by a compromised proxy. D: the gateway's uplink is flooded or its cellular modem jammed so readings are not delivered.

**EX077.** Actor: an outsider on the internet. Precondition: the gateway's web interface is reachable from the internet and still uses the vendor default password. Action: logs in and uploads modified firmware or configuration. Outcome: all 40 meters behind that gateway report false readings and the gateway can be used to pivot towards the DMZ.

**EX078.** A tenant's replay affects one household's bill and is bounded in value, while gateway takeover affects every meter in its street and may provide a foothold toward other zones; the larger blast radius and possible operational effect put it higher.

**EX079.** Expected BLOCK, and `permit("HMI-1", 23, 105)` returns BLOCK because the pair (HMI-1, 23) is not in ALLOW — the policy is default-deny for unlisted functions.

**EX080.** (HMI-1, 6, 120) → PASS, the new last writable register; (HMI-1, 6, 121) → BLOCK, the first register past the range.

**EX081.** If expectations come from running the code, a bug becomes the expected result. Writing them first from the operational requirement (which registers HMI-1 truly needs) lets the test catch the mismatch.

**EX082.** 0.1 × 0.3 × 0.2 = 0.006 per year.

**EX083.** A single intruder who writes the setpoint can also suppress HMI alarms or disable the detector, so "operators miss" and "detector misses" become likely given the write; multiplying the marginal probabilities then underestimates P(c).

**EX084.** Component: meter gateway. Mode: TLS client certificate expires. Effect: cloud refuses uplink, readings queue then drop after buffer fills. Detection: certificate-expiry monitoring 30 days ahead and missing-heartbeat alert. Severity: medium (billing delay, no process effect). Action: automated renewal with alert on failure.

**EX085.** "Analyst informs the shift lead. The shift lead confirms operators can hold the boiler safe with local panels or the backup HMI, then authorises disconnecting the SCADA server's network link (not powering it off, to preserve evidence)."

**EX086.** Greedy by risk: risk-9 (1.5 h) and risk-8 (1 h) use 2.5 h; risk-6 needs 2 h and would overrun to 4.5 h, so it is deferred; risk-3 (1 h) fits, total 3.5 h. Apply 9, 8 and 3; defer the risk-6 patch with a dated ticket and compensating controls (or split the window plan if the risk-6 item can be shortened).

**EX087.** Add an on-call roster with night numbers for the firewall administrator and control engineer to the playbook's first page, and include a real test call to each number at the start of the next tabletop.

**EX088.** The loop uses `4-len(miss)`, so it would print `MTR-C: 0/4 met` unless the 4 is changed; after changing it to `len(f)-len(miss)`, MTR-C prints 1/5 met with 5.2, 5.3, 5.4 and 5.5 missing. Spotting the hard-coded 4 is part of the answer.

**EX089.** Every provision appears as a fleet gap, but MTR-A passes all of them and MTR-B fails only one; the manager might fund a full-fleet replacement when the real problem is concentrated in MTR-C plus a cheap password reset for MTR-B.

**EX090.** A description of how updates are cryptographically signed and verified on the device, the vendor's published update history and declared support period, and a bench demonstration of applying an update and rejecting a tampered one.

**EX091.** Schneider Electric PLCs, OMRON Sysmac NEX PLCs, and Open Platform Communications Unified Architecture (OPC UA) servers.

**EX092.** Alert whenever passive monitoring sees a program-download (or logic-change) operation to PLC-H that does not originate from EWS-1 or that occurs outside a change window recorded in the maintenance system.

**EX093.** The techniques — abusing OPC UA, engineering protocols and vulnerable workstation drivers — apply to other products, and an inventory that says "we have none" may be incomplete; acting on generic detections reduces exposure to the next variant.

**EX094.** (1) The vendor shall provide an SBOM for each firmware release in SPDX or CycloneDX format. (2) The gateway shall have no universal default password and shall force a unique credential at commissioning (ETSI EN 303 645 provision 5.1). (3) The vendor shall publish a vulnerability disclosure policy and provide security updates for at least seven years after delivery.

**EX095.** Cause: an unauthorised write stops circulation pump P-2 via its variable-speed drive's network interface. Safeguard: hardwired low-flow switch tripping the boiler burners through SIS-H, independent of the drive network.

**EX096.** "From Monday HMI-1 will only run the HMI program and approved tools. If something you normally use will not start, a message will appear — nothing in the plant changes. Note what you tried and call the control engineer on extension 214; do not try to work around it."

**EX097.** n = 1.96² × 0.10 × 0.90 / 0.03² = 3.8416 × 0.09 / 0.0009 ≈ 384.2, so about 385 runs.

**EX098.** Choosing the threshold on the same runs used for evaluation fits it to those runs' noise and makes the false-alarm and detection estimates optimistic; tuning on separate seeds and freezing gives an honest estimate of performance on unseen data.

**EX099.** H1 is falsified if, on the 300 quiet runs, CUSUM's proportion of runs with a false alarm is not lower than the band's — i.e. the 95 % interval for (band − CUSUM) includes zero or lies below it.

**EX100.** A = 0.2 × (2 + 3 + 5 + 4 + 4) = 3.6; B = 0.2 × (5 + 5 + 3 + 3 + 2) = 3.6 — an exact tie, which shows the weights are what separate the options.

**EX101.** That the broker cannot initiate sessions without the shift lead's approval and that sessions are terminated automatically at four hours; if either fails, B has a persistent path like A.

**EX102.** Choose A when the plant judges round-the-clock vendor availability more important than path exposure — for example if fit carries weight ≥ 0.45 as in the sensitivity run — and only with compensating controls such as session recording and monthly access reviews.

**EX103.** "Can a logistic-regression classifier trained on 20 synthetic LDHP supply-temperature features distinguish slow setpoint drift from normal load changes, measured by recall at a fixed 5 % false-alarm rate on held-out simulated runs, without any access to a real plant?"

**EX104.** "All data in this project are synthetic and generated by the scripts in the repository; no real controller, network or service will be contacted. The monitor only reads offline capture files. If the work reveals a weakness in any real product, it will be reported through the vendor's disclosure process and not published until coordinated."

**EX105.** "The evaluation report contains the confusion matrix for the 8-case set, precision and recall with numerators and denominators, the list of missed attack classes, the script commit hash and the seeds, and its numbers match a rerun of `lab_eval.py`."

**EX106.** "Thank you for trusting me with this. My placement agreement does not allow me to scan or probe your systems, because even simple scans can disturb older controllers. What I can do this week is go through your remote-access arrangements and logs with you, and I will ask my supervisor whether a qualified firm should do a technical assessment."

**EX107.** "The asset list is stored only in the university's encrypted project folder, shared with the supervisor and the co-operative manager, and deleted from all student devices on the last day of the placement."

**EX108.** "I was surprised that a cellular router could sit in the boiler house without appearing on any drawing or invoice — it means the co-operative's network diagram is not a reliable map of how outsiders can reach the boiler."

**EX109.** (a) Bottom rung — an unverified marketing claim with no method or denominator. (b) A primary case report from a government source: stronger, but a single incident.

**EX110.** The estimate of how many devices were infected: honeypots only observe bots that happen to scan or attack them, so they undercount and are biased by where the honeypots sit; the telescope data provide the broader population view.

**EX111.** "The detector is tuned and evaluated on the same simulated plant, so the reported false-alarm and detection rates are likely optimistic and may not generalise. Please tune thresholds on separate seeds, freeze them, and evaluate on at least one additional process model or published dataset."

**EX112.** Classify a write as benign-maint only when it comes from EWS-1 under a named engineer account and its time falls inside a maintenance window linked to an open ticket; still log the write and include it in the daily review so an insider cannot hide behind the window.

**EX113.** TP rises to 4 and FN falls to 1, so recall = 4/5 = 0.80; precision stays 4/5 = 0.80 if the false positive remains.

**EX114.** With 5 attack cases, 0.60 has a 95 % interval of roughly 0.23–0.88, and a 10-case set has a similarly wide interval and different attack classes, so the two figures overlap almost entirely and measure different things.

**EX115.** (a) Result. (b) Interpretation — and an overreaching one on this evidence. (c) Limitation.

**EX116.** The analysis is reproducible, uses correct metrics and reports denominators, but eight synthetic cases with one drift profile cannot support general claims, so evidence is sound but narrow — a 2 rather than a 3.

**EX117.** Testing on a second, independently built process model (or on anonymised captures provided by an owner under agreement), because the main open question is whether the rule set generalises beyond the plant it was designed on.

**EX118.** "Adding a cumulative-change rule raised recall from 3/5 to 4/5 on the eight-case synthetic set — a failure-class finding, not a rate estimate."

**EX119.** "They would make writes from HMI-1 itself or keep each change below the cumulative threshold, as Urbina et al. describe for stealthy attacks. My monitor cannot stop that; it bounds how far the setpoint can move unnoticed, and correlating writes with operator logins is the next defence I would test."

**EX120.** Any configuration export, capture or register map supplied by a real owner, even anonymised, because it can reveal their architecture; it stays under the data agreement while the public package contains only the synthetic generators and seeds.

<a id="references"></a>

## References

Links checked 12 October 2026; standards and advisories are revised, so re-verify editions before citing. DOIs were checked against Crossref.

- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA, DOE, NSA, FBI (2022). AA22-103A: APT Cyber Tools Targeting ICS/SCADA Devices. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-103a>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ICS-CERT (2016). IR-ALERT-H-16-056-01: Cyber-Attack Against Ukrainian Critical Infrastructure. <https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01>
- ISA/IEC 62443 series of standards (overview; parts 2-1, 2-3, 3-2, 3-3, 4-1 and 4-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0836 Modify Parameter, T0843 Program Download, T0883 Internet Accessible Device and T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus Application Protocol Specification V1.1b3. Listed at <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- NIST FIPS 198-1 (2008). The Keyed-Hash Message Authentication Code (HMAC). <https://csrc.nist.gov/pubs/fips/198-1/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
