# OT, IoT and Cyber-Physical Security: Engineering Secure Control Systems

- Language: English (`en`); engineering course, five years; approximately 4,000 hours of planned study.
- Editorial state: **draft**. Chapters 1–50 of 50 have authored teaching text; exercises EX001–EX100 (two per chapter) have matching worked results; offline labs use Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: future engineers who will design, implement and verify security for industrial control, OT and cyber-physical systems. Entry knowledge: secondary-school mathematics and physics.
- Relation to neighbouring books: the [critical-infrastructure engineering book](../../../critical-sector-security/en/book/MANUSCRIPT.md) emphasises sectors and cross-sector cascades; the [master's OT book](../../../../masters-2-years/ot-iot-security/en/book/MANUSCRIPT.md) emphasises empirical study design. **This book is about building control-system security**: requirements, Purdue/62443 architecture, PLC/SCADA conduits, detection, safety–security co-engineering, verification and capstone evidence.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited degree or licence. No authority to access real plants. All plants, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–19 build foundations applied to OT from the first page. Chapter 20 sets OT context. Chapters 21–42 are the field core with design studios (25, 35) and verification laboratories (30, 40). Chapters 43–50 are practice and capstone. Keep labels: **requirement**, **design decision**, **evidence**, **residual risk**.

### Synthetic design case

| Element | Role | Boundary |
|---|---|---|
| **Ashford Batch Plant (ABP)** — reactor R-101, feed tanks T-1/T-2, PLC-A, SIS-B, SCADA, historian | System under design | Invented |
| **Control Network Hardening Programme (CNHP)** | The engineering programme | Invented |
| Cedar Industrial Park | Site context | Invented |

### Core sources

- NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); Modbus [Application Protocol V1.1b3](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf); Giraldo et al. [CSUR 2018](https://doi.org/10.1145/3203245); Urbina et al. [CCS 2016](https://doi.org/10.1145/2976749.2978388).

## Contents

1. [Calculus I](#ch-01)
2. [Discrete mathematics](#ch-02)
3. [Physics for computing](#ch-03)
4. [Programming I](#ch-04)
5. [Engineering communication](#ch-05)
6. [Calculus II](#ch-06)
7. [Probability and statistics](#ch-07)
8. [Computer architecture](#ch-08)
9. [Programming II](#ch-09)
10. [Engineering ethics and safety](#ch-10)
11. [Networks and protocols](#ch-11)
12. [Operating systems](#ch-12)
13. [Data systems](#ch-13)
14. [Software engineering](#ch-14)
15. [Security fundamentals](#ch-15)
16. [Systems engineering](#ch-16)
17. [Control and feedback basics](#ch-17)
18. [Security architecture](#ch-18)
19. [Identity and cryptography](#ch-19)
20. [OT, IoT and cyber-physical security: engineering context](#ch-20)
21. [OT, IoT and cyber-physical security: requirements](#ch-21)
22. [OT, IoT and cyber-physical security: system and data models](#ch-22)
23. [OT, IoT and cyber-physical security: threat and failure analysis](#ch-23)
24. [OT, IoT and cyber-physical security: methods I](#ch-24)
25. [Design studio I](#ch-25)
26. [OT, IoT and cyber-physical security: architecture alternatives](#ch-26)
27. [OT, IoT and cyber-physical security: control design](#ch-27)
28. [OT, IoT and cyber-physical security: implementation I](#ch-28)
29. [OT, IoT and cyber-physical security: measurement](#ch-29)
30. [Verification laboratory I](#ch-30)
31. [OT, IoT and cyber-physical security: implementation II](#ch-31)
32. [OT, IoT and cyber-physical security: reliability](#ch-32)
33. [OT, IoT and cyber-physical security: safety and resilience](#ch-33)
34. [OT, IoT and cyber-physical security: integration](#ch-34)
35. [Design studio II](#ch-35)
36. [OT, IoT and cyber-physical security: performance and scale](#ch-36)
37. [OT, IoT and cyber-physical security: operations](#ch-37)
38. [OT, IoT and cyber-physical security: validation](#ch-38)
39. [OT, IoT and cyber-physical security: maintainability](#ch-39)
40. [Verification laboratory II](#ch-40)
41. [OT, IoT and cyber-physical security: system optimization](#ch-41)
42. [OT, IoT and cyber-physical security: applied research](#ch-42)
43. [Industry or public-service practice](#ch-43)
44. [Engineering capstone I](#ch-44)
45. [Independent design review](#ch-45)
46. [Engineering capstone II](#ch-46)
47. [Failure and recovery trial](#ch-47)
48. [Evidence dossier](#ch-48)
49. [Engineering thesis](#ch-49)
50. [Final defense](#ch-50)
51. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes and connection

After this chapter you can (1) treat tank level as a stock whose rate of change is a flow; (2) compute derivatives and definite integrals for feed-tank hold-up; (3) solve "how long until empty" by bisection; and (4) explain why an average-rate shortcut can mislead a batch schedule. It opens the Ashford Batch Plant design case and prepares Calculus II.

### 1.1 Stocks and flows in a batch plant

A feed tank is a stock of feedstock; a dosing pump is a flow. A reactor heel is a stock; a discharge valve is a flow. OT security questions are often stock-and-flow questions under adversity: *if the makeup pump stops because its PLC loses a legitimate command path, how long until the batch must abort?* The answer is an integral of outflow compared with usable volume — not a single datasheet number.

The derivative $dV/dt$ is the instantaneous rate of change of volume $V$. The definite integral $\int_a^b q(t)\,dt$ is the amount transferred. The fundamental theorem links them: if $V'=-q$, then $V(b)-V(a)=-\int_a^b q(t)\,dt$.

### 1.2 Derivatives and integrals you will use

Polynomial, exponential and trigonometric derivatives; product and chain rules; antiderivatives of the same. Batch demand is rarely constant: a six-hour recipe may draw faster in the charge phase. If $q(t)=1.8+0.4\sin(2\pi t/6)$ m³/h, the peak draw is 2.2 m³/h and the antiderivative is $1.8t-(0.4\cdot 6/(2\pi))\cos(2\pi t/6)+C$.

### 1.3 Numerical root finding

Set drawn volume equal to usable volume and solve for $T$. Bisection halves a bracketing interval until the tolerance is met; it is slow and reliable for continuous monotonic drawdown.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

**Ashford Batch Plant (ABP)** is a synthetic specialty-chemical batching facility at Cedar Industrial Park. Feed tank T-1 holds 12 m³; the minimum usable level is 2 m³. Makeup stops at t=0 while the reactor still draws $q(t)$ above. Average-rate estimate: $(12-2)/1.8\approx 5.56$ h. Exact integral + bisection: about **5.53 h**. Here the sinusoid nearly averages out over the short horizon; in Chapter 6 a longer outage will show larger gaps.

### Practical activity

Lab 1 (Python 3 stdlib):

```python
# Lab 1 - tank hold-up after feed pump stop (Ashford Batch Plant, synthetic)
import math
V0, VMIN = 12.0, 2.0   # m3 in feed tank T-1
def outflow(t):         # m3/h to reactor; t hours after stop of makeup
    return 1.8 + 0.4*math.sin(2*math.pi*t/6)
def drawn(t):
    return 1.8*t - (0.4*6/(2*math.pi))*(math.cos(2*math.pi*t/6)-1)
lo,hi=0.0,24.0
for _ in range(50):
    mid=(lo+hi)/2
    lo,hi=(mid,hi) if drawn(mid)<V0-VMIN else (lo,mid)
print(f"time to min level: {lo:.2f} h")
print(f"average-rate estimate: {(V0-VMIN)/1.8:.2f} h")
```

Expected output:

```text
time to min level: 5.53 h
average-rate estimate: 5.56 h
```

### Common errors and limits

- Mixing L/s with m³/h (1 L/s = 3.6 m³/h).
- Treating nameplate volume as usable volume.
- Trusting Euler with a coarse step without a finer check.
- Presenting the sinusoid as measured plant data.

### Exercises — chapter 1

**EX001 — Peak draw.** *Objective:* find maximum of q(t) and compare with pump capacity 2.0 m³/h. *Inputs:* q(t) from §1.2. *Steps:* (1) differentiate; (2) find max; (3) conclude whether capacity binds. *Expected evidence:* derivative and sentence. *Rubric:* 3 = correct max 2.2 and capacity shortfall stated; 2 = one slip; 1 = derivative only; 0 = none.

**EX002 — Hold-up sensitivity.** *Objective:* rerun Lab 1 with VMIN=3.0 and report the new time. *Inputs:* Lab 1. *Steps:* change VMIN, rerun, compare. *Expected evidence:* two numbers and a scheduling note. *Rubric:* 3 = correct new time and links to abort risk; 2 = number only; 1 = not run; 0 = none.

### Chapter synthesis

Batch plants are stocks and flows. Hold-up time is an integral solved for its bound; check numerics; keep units; never let an average hide a peak that aborts a batch.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes and connection

After this chapter you can (1) use sets, relations and graphs to model OT assets and conduits; (2) apply Boolean logic to interlock conditions; (3) count paths in a small attack graph; and (4) explain why graph models omit timing and physics.

### 2.1 Sets and inventories

An asset inventory is a set. Zones are subsets. A conduit is a permitted relation between zones. Discrete mathematics gives the language for saying "the set of hosts that can write to PLC-A" without ambiguity.

### 2.2 Graphs for reachability

Nodes are devices; directed edges are allowed protocol flows. Reachability from an engineering workstation to a safety PLC is a path-existence question. Lab 23 (Chapter 23) will compute this on a Purdue graph; here you practise adjacency lists and breadth-first search by hand on five nodes.

### 2.3 Boolean interlocks

A permit-to-run might be `(level_OK AND temp_OK AND NOT estop)`. Truth tables and simplification catch missing terms — the classic error is omitting the safety PLC's healthy bit.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

ABP's permit-to-agitate requires: agitator VFD healthy, reactor level above heel, SIS not tripped, and local e-stop clear. Written as a Boolean expression and expanded, the engineer finds that "SCADA mode remote" was incorrectly ANDed into the safety path — a category error: mode is a control concern, not a safety precondition.

### Practical activity

Draw a five-node graph: EngWS → SCADA → PLC-A → IO; EngWS → SIS (should be absent). List all EngWS reachability sets with and without the forbidden edge.

### Common errors and limits

- Treating undirected "connectivity" as directed protocol permission.
- Putting safety permits in the same logic as production enables without SIL reasoning.
- Counting paths as probabilities.

### Exercises — chapter 2

**EX003 — Truth table.** *Objective:* build the truth table for permit-to-agitate with four inputs. *Inputs:* §2.3. *Steps:* enumerate 16 rows; mark unsafe true rows. *Expected evidence:* table. *Rubric:* 3 = complete and flags unsafe combinations; 2 = incomplete; 1 = expression only; 0 = none.

**EX004 — Path count.** *Objective:* count simple paths EngWS→IO in the five-node graph. *Inputs:* activity graph. *Steps:* enumerate. *Expected evidence:* number and list. *Rubric:* 3 = correct enumeration; 2 = missed path; 1 = guess; 0 = none.

### Chapter synthesis

Sets, graphs and Boolean logic are the discrete skeleton of OT architecture and interlocks; they do not replace physics or timing analysis.

### Continue studying — chapter 02 of 50

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes and connection

After this chapter you can apply **Physics for computing** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 3.1 Sensors measure physics

A level transmitter infers level from pressure or time-of-flight. Injecting a register value attacks a representation; the physical process continues under its own laws. OT engineers must keep both models: the bits and the physics.

### 3.2 Scaling, quantisation and noise

4–20 mA loops and ADC counts need scaling. Noise and quantisation set a floor for residual detectors — a CUSUM tighter than sensor noise false-alarms.

### 3.3 Actuator dynamics

Pumps and valves have inertia and stroke time. Scan cycle plus stroke delay bounds how fast an attack or a defence can move the process.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies physics for computing to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies physics for computing to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying physics for computing without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 3

**EX005 — Physics for computing drill.** *Objective:* perform a defined physics for computing task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX006 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Physics for computing is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 03 of 50

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes and connection

After this chapter you can apply **Programming I** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 4.1 Programming for reproducible labs

Use Python 3 standard library only in this course's labs. Prefer functions that return values; name variables after plant tags (`true_level`, `residual`).

### 4.2 Control flow and data structures

Lists of samples, dicts of device attributes, and clear loops over time steps are enough for tank models and reachability.

### 4.3 Checking yourself

Always run a nominal case (expect no alarm) and an attack case (expect alarm after onset) before trusting a detector function.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies programming i to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies programming i to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying programming i without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 4

**EX007 — Programming I drill.** *Objective:* perform a defined programming i task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX008 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Programming I is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 04 of 50

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes and connection

After this chapter you can apply **Engineering communication** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 5.1 Audience and purpose

An OT design note has operators, assessors and future maintainers as audiences. Purpose is a decision, not a narrative.

### 5.2 Requirement language

Write verifiable requirements: "PLC-A shall reject setpoint writes outside [lo, hi] and alarm within one scan" — not "the system shall be secure".

### 5.3 Traceability

Every safety-relevant claim needs a link to a test, analysis or review record with a version.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies engineering communication to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies engineering communication to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying engineering communication without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 5

**EX009 — Engineering communication drill.** *Objective:* perform a defined engineering communication task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX010 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Engineering communication is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 05 of 50

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes and connection

After this chapter you can apply **Calculus II** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 6.1 Differential equations for tanks

A single tank: $\dot V = q_{in}-q_{out}(V)$. Linearising around an operating point yields first-order lag models used in detector design.

### 6.2 Steady state and time constants

At equilibrium $q_{in}=q_{out}$. The time constant sets how fast residuals should be evaluated.

### 6.3 Numerical integration

Euler and RK4 appear in labs; always compare step sizes before trusting a simulated attack impact.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies calculus ii to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies calculus ii to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying calculus ii without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 6

**EX011 — Calculus II drill.** *Objective:* perform a defined calculus ii task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX012 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Calculus II is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 06 of 50

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes and connection

After this chapter you can apply **Probability and statistics** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 7.1 Randomness in sensors and processes

Measurement noise is not attack. Model it explicitly when setting CUSUM allowances.

### 7.2 False alarms and base rates

Even a 1% false-alarm probability per minute devastates operator trust over a shift. Report false alarms per shift, not only ROC AUC.

### 7.3 Estimation

Sample means and bootstrap intervals describe simulation noise; they do not validate a structural model.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies probability and statistics to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies probability and statistics to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying probability and statistics without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 7

**EX013 — Probability and statistics drill.** *Objective:* perform a defined probability and statistics task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX014 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Probability and statistics is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 07 of 50

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes and connection

After this chapter you can apply **Computer architecture** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 8.1 Controllers are computers

PLCs have CPUs, memory, scan cycles and watchdog timers. A slow network flood can miss scans — an availability attack with physical consequences.

### 8.2 Memory and I/O maps

Holding registers and coils are just memory; knowing the map is necessary for legitimate engineering and for understanding attack surfaces — never practise mapping on production.

### 8.3 Real-time constraints

Hard deadlines in the scan differ from best-effort IT scheduling. Security controls that add unbounded latency need budget analysis.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies computer architecture to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies computer architecture to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying computer architecture without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 8

**EX015 — Computer architecture drill.** *Objective:* perform a defined computer architecture task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX016 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Computer architecture is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 08 of 50

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes and connection

After this chapter you can apply **Programming II** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 9.1 Modules and packages

Split simulation, detection and reporting. Labs in later chapters import earlier generators.

### 9.2 File formats

CSV traces with headers; JSON manifests with SHA-256 hashes; never commit secrets.

### 9.3 Complexity control

Prefer clear O(n) loops over clever code in safety-adjacent tooling.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies programming ii to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies programming ii to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying programming ii without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 9

**EX017 — Programming II drill.** *Objective:* perform a defined programming ii task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX018 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Programming II is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 09 of 50

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes and connection

After this chapter you can apply **Engineering ethics and safety** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 10.1 Safety culture meets security

Stop work authority applies to cyber experiments too. Never test on production; bound lab hazards with independent layers.

### 10.2 Dual use

Publish capability classes and defences; withhold product-specific exploitation pending coordinated disclosure.

### 10.3 Professional duty

Engineers owe the public safe operation. A clever demo that risks a spill fails that duty regardless of intent.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies engineering ethics and safety to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies engineering ethics and safety to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying engineering ethics and safety without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 10

**EX019 — Engineering ethics and safety drill.** *Objective:* perform a defined engineering ethics and safety task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX020 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Engineering ethics and safety is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 10 of 50

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes and connection

After this chapter you can apply **Networks and protocols** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 11.1 Layers and industrial protocols

Ethernet/IP, Modbus/TCP, DNP3 and OPC UA carry different security properties. Modbus Application Protocol defines function codes without authentication ([spec V1.1b3](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf)).

### 11.2 Segmentation

Purdue levels and IEC 62443 zones/conduits limit who can write setpoints. Flat networks make every compromise a plant-wide event.

### 11.3 Timing and determinism

Jitter matters. Security appliances must be assessed for latency under load.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies networks and protocols to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies networks and protocols to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying networks and protocols without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 11

**EX021 — Networks and protocols drill.** *Objective:* perform a defined networks and protocols task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX022 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Networks and protocols is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 11 of 50

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes and connection

After this chapter you can apply **Operating systems** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 12.1 RTOS and PLC executives

Scan-based executives differ from general-purpose OS scheduling. Patching and antivirus practices from IT can break determinism if naively copied.

### 12.2 Access control on engineering stations

Engineering workstations are high-value; they hold projects that can rewrite plant logic. Harden and monitor them.

### 12.3 Logging

Controller logs are scarce; historians and mirror ports often supply detection evidence.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies operating systems to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies operating systems to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying operating systems without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 12

**EX023 — Operating systems drill.** *Objective:* perform a defined operating systems task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX024 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Operating systems is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 12 of 50

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes and connection

After this chapter you can apply **Data systems** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 13.1 Historians and recipes

Batch plants store recipes, setpoints and quality data. Integrity of recipe downloads is a product-safety issue as well as a cyber issue.

### 13.2 Time series

Aligned timestamps enable residual checks; clock skew creates false residuals.

### 13.3 Backups

Offline, verified backups of PLC projects are recovery requirements — test restores on engineering systems, not on the running CPU without a change window.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies data systems to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies data systems to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying data systems without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 13

**EX025 — Data systems drill.** *Objective:* perform a defined data systems task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX026 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Data systems is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 13 of 50

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes and connection

After this chapter you can apply **Software engineering** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 14.1 Lifecycle

Requirements → design → implementation → verification → operation → maintenance. OT adds safety validation gates.

### 14.2 Change control

A ladder-logic change is a plant change. Dual authorisation and offline test are normal.

### 14.3 Technical debt

Legacy protocols without authentication are debt with interest denominated in risk.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies software engineering to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies software engineering to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying software engineering without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 14

**EX027 — Software engineering drill.** *Objective:* perform a defined software engineering task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX028 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Software engineering is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 14 of 50

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes and connection

After this chapter you can apply **Security fundamentals** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 15.1 CIA and safety

In OT, availability and integrity often outrank confidentiality — but recipe theft and ransomware still matter.

### 15.2 Attack surfaces

Exposed engineering ports, default credentials, flat networks, and shared accounts.

### 15.3 Defence in depth

Zones, allow-lists, signed binaries where supported, monitoring, and incident procedures — no single control suffices.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies security fundamentals to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies security fundamentals to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying security fundamentals without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 15

**EX029 — Security fundamentals drill.** *Objective:* perform a defined security fundamentals task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX030 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Security fundamentals is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 15 of 50

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes and connection

After this chapter you can apply **Systems engineering** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 16.1 System boundary

CNHP's boundary includes PLC-A, SIS-B, SCADA, historian, and conduits — not the corporate ERP, except at the DMZ.

### 16.2 Requirements flow-down

System requirements become zone and component requirements (IEC 62443 security levels as hypotheses to engineer against).

### 16.3 Interfaces

Every conduit needs an owner, a protocol allow-list and a monitoring plan.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies systems engineering to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies systems engineering to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying systems engineering without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 16

**EX031 — Systems engineering drill.** *Objective:* perform a defined systems engineering task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX032 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Systems engineering is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 16 of 50

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes and connection

After this chapter you can explain feedback control, tune a simple PI mentally, and see why actuator commands are security-relevant.

### 17.1 The loop

Reported level compared with setpoint drives inflow. Attackers who forge the reported level drive the controller to the wrong action — manipulation of view with physical consequences.

### 17.2 PI control

Control effort $u = k_p e + k_i \int e$. Too much $k_p$ oscillates; zero $k_i$ leaves steady-state error.

### 17.3 Security relevance

Watch residual and control effort. A fight between controller and attacker often shows up as saturated commands.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.


In addition, record the scan-cycle budget and any actuator stroke delay that bounds how fast the process can move after a forged command; without those times, delay metrics are uninterpretable. State whether the SIS is independent of the BPCS path under test.
### Worked example (synthetic Ashford Batch Plant)

ABP level loop on T-1 uses PI; Lab 17 shows three tunings on a synthetic tank.

### Practical activity

```python
# Lab 17 - discrete PI level control vs. setpoint step (synthetic)
def sim(kp, ki, steps=200, sp=60.0):
    level, integ, err_hist = 50.0, 0.0, []
    for t in range(steps):
        err = sp - level
        integ += err * 0.1
        u = max(0.0, min(3.0, kp*err + ki*integ))   # inflow m3/h capped
        level += (u - 0.02*level)*0.1
        err_hist.append(abs(err))
    return level, sum(err_hist)/len(err_hist), max(err_hist[50:])
for kp,ki in ((0.05,0.0),(0.05,0.01),(0.2,0.01)):
    final, mae, peak = sim(kp,ki)
    print(f"kp={kp} ki={ki} final={final:.2f} mae={mae:.2f} peak_abs_err_after_5s={peak:.2f}")
```

Expected output:

```text
kp=0.05 ki=0.0 final=44.61 mae=13.29 peak_abs_err_after_5s=15.38
kp=0.05 ki=0.01 final=57.22 mae=8.34 peak_abs_err_after_5s=10.91
kp=0.2 ki=0.01 final=58.15 mae=4.62 peak_abs_err_after_5s=6.17
```

### Common errors and limits

- Ignoring actuator saturation.
- Tuning on a process with unmodelled delay.
- Treating simulation tunings as plant-ready.

### Exercises — chapter 17

**EX033 — Apply Control and feedback basics.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX034 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Control and feedback basics advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 17 of 50

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes and connection

After this chapter you can apply **Security architecture** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 18.1 Reference architectures

Purdue + DMZ; IEC 62443 zones; cloud-connected IIoT variants that erode air gaps.

### 18.2 Trust boundaries

Where identity is asserted; where commands become physical; where safety takes over.

### 18.3 Pattern catalogue

Brokered historian reads; jump hosts for engineering access; unidirectional gateways for high-consequence outbound data.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies security architecture to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies security architecture to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying security architecture without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 18

**EX035 — Security architecture drill.** *Objective:* perform a defined security architecture task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX036 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Security architecture is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 18 of 50

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes and connection

After this chapter you can apply **Identity and cryptography** to OT engineering problems on the Ashford Batch Plant case, with definitions, a worked calculation, and a bounded practical activity. It builds toward the field chapters (20–42).

### 19.1 Identity in OT

Human users, service accounts, device identities. Shared operator logins destroy attribution.

### 19.2 Cryptography in constrained devices

Integrity protection (MACs) on setpoints matters more often than confidentiality on temperature readings — but both can be required.

### 19.3 Key management

Provisioning, rotation and emergency access must work when the plant network is degraded.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

On ABP, the team applies identity and cryptography to a CNHP decision about reactor R-101 and feed tanks T-1/T-2. All numbers are synthetic. The worked path shows inputs, calculation, result and the design decision it supports — and what it does *not* support (no claim about a real plant).

### Practical activity

Complete a one-page calculation or short Python 3 stdlib snippet that applies identity and cryptography to a synthetic ABP quantity (level, flow, reachability, or alarm rate). Record inputs, outputs and assumptions.

### Common errors and limits

- Applying identity and cryptography without units.
- Treating synthetic ABP numbers as field measurements.
- Skipping assumptions about sensor honesty or network reachability.
- Claiming safety integrity from a teaching calculation.

### Exercises — chapter 19

**EX037 — Identity and cryptography drill.** *Objective:* perform a defined identity and cryptography task on synthetic ABP data. *Inputs:* chapter worked example. *Steps:* (1) recompute; (2) change one input; (3) state the design impact. *Expected evidence:* calculation and sentence. *Rubric:* 3 = correct and scoped; 2 = slip; 1 = incomplete; 0 = none.

**EX038 — Assumption log.** *Objective:* list five assumptions in the worked example and mark which are physical vs organisational. *Inputs:* worked example. *Steps:* table with type and failure mode if false. *Expected evidence:* table. *Rubric:* 3 = five distinct assumptions with failure modes; 2 = thin; 1 = list only; 0 = none.

### Chapter synthesis

Identity and cryptography is a tool for OT design decisions when units, assumptions and scope are explicit. ABP remains synthetic; evidence from this chapter does not authorise work on real controllers.

### Continue studying — chapter 19 of 50

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: engineering context

### Learning outcomes and connection

After this chapter you can place ABP in the OT landscape: Purdue levels, ISA/IEC 62443, ATT&CK for ICS, and public incident lessons at source fidelity.

### 20.1 What OT security is about

Operational technology runs physical processes. NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) emphasises safety and availability alongside confidentiality. The unit of concern is the control loop and its safety functions — distinct from the sector-cascade focus of the critical-infrastructure course.

### 20.2 Purdue and zones

Levels 0–5 with an industrial DMZ structure ABP: IO and flame detectors (0), PLC-A and SIS-B (1), SCADA/HMI (2), historian/MES (3), site business (4), enterprise (5). IEC 62443 zones and conduits refine who may write setpoints.

### 20.3 Threat evidence

MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) catalogues techniques such as *Modify Parameter* and *Spoof Reporting Message*. Public cases (Stuxnet's manipulation of view, Ukraine 2015 breaker operations, TRITON targeting SIS) show documented adversary goals. Cite public analyses only.

### 20.4 IIoT pressure

Cloud historians and remote vendor access erode classic air gaps. Each new conduit needs an owner and an allow-list.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

ABP's CNHP charter: harden conduits so that a compromised engineering laptop cannot write to SIS-B, and so that single-sensor replay on T-1 level is detectable via an independent flow meter residual.

### Practical activity

Sketch ABP's Purdue diagram with at least eight nodes and mark conduits that CNHP will allow-list.

### Common errors and limits

- Confusing OT security with sector regulation alone.
- Treating ATT&CK techniques as frequencies.
- Assuming air gaps still exist because a slide says so.

### Exercises — chapter 20

**EX039 — Apply engineering context.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX040 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: engineering context advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 20 of 50

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: requirements

### Learning outcomes and connection

After this chapter you can write verifiable OT requirements for protection, detection, degraded operation and recovery.

### 21.1 Requirement sources

Consequences (overflow, off-spec batch, SIS spuriously tripped), stakeholders (operators, quality, safety officer), standards (62443 target SLs), threats (ATT&CK techniques), constraints (legacy Modbus devices).

### 21.2 Degraded operation

Require local automatic control for 72 h without SCADA; require manual runbooks for R-101 within 30 minutes of a declare-compromised decision.

### 21.3 Detection requirements

Event recall and max delay for class A replay; false alarms ≤ 1 per shift; independent sensing path for residual checks.

### 21.4 Conflicts

Strong authentication vs emergency access; patching vs validated builds — record negotiations with owners.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

| ID | Requirement | Verification |
|---|---|---|
| R1 | Setpoint writes outside configured bounds rejected within one scan | Test |
| R2 | SIS-B not reachable from SCADA engineering path | Reachability analysis |
| R3 | Residual alarm on T-1 single-sensor replay within 60 s mean | Lab/test |
| R4 | Local auto continues 72 h without SCADA | Demonstration |

### Practical activity

Write five CNHP requirements with source and verification method.

### Common errors and limits

- "Secure the PLC" as a requirement.
- No degraded-operation requirements.
- Silent conflict resolution.

### Exercises — chapter 21

**EX041 — Apply requirements.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX042 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: requirements advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 21 of 50

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: system and data models

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: system and data models** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 22.1 Purpose

tag lists, P&IDs as graphs, data dictionaries, historian schemas, and trust annotations on each signal (source, scaling, authority).

### 22.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 22.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 22.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies models to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 22

**EX043 — Apply system and data models.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX044 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: system and data models advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 22 of 50

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: threat and failure analysis

### Learning outcomes and connection

After this chapter you can combine cyber threat enumeration with process failure analysis without writing exploit instructions.

### 23.1 Threat enumeration

Use ATT&CK for ICS technique names as hypotheses about *what* an adversary might try (spoof reporting, modify parameter), not as step-by-step guides.

### 23.2 Failure analysis

HAZOP guide words (more/less/no flow) gain cyber causes: forged setpoints, stuck valves via denied commands, false-normal HMI.

### 23.3 Reachability

Lab 23 compares flat vs zoned Purdue graphs for SIS exposure.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.


In addition, record the scan-cycle budget and any actuator stroke delay that bounds how fast the process can move after a forged command; without those times, delay metrics are uninterpretable. State whether the SIS is independent of the BPCS path under test.
### Worked example (synthetic Ashford Batch Plant)

Flat ABP networking lets L4 reach SIS; zoned design removes that edge.

### Practical activity

```python
# Lab 23 - reachability count on a synthetic Purdue-layered OT network
# Nodes: L5-ERP, L4-Office, L3.5-DMZ, L3-Hist, L2-SCADA, L1-PLC, L1-SIS, L0-IO
edges_flat=[("L5","L4"),("L4","L3"),("L3","L2"),("L2","L1-PLC"),("L2","L1-SIS"),("L1-PLC","L0"),("L1-SIS","L0"),("L4","L2")]
edges_zoned=[("L5","L4"),("L4","L3.5"),("L3.5","L3"),("L3","L2"),("L2","L1-PLC"),("L1-SIS","L0"),("L1-PLC","L0")]  # SIS not reachable from SCADA
def reach(edges, start):
    g={}; 
    for a,b in edges: g.setdefault(a,[]).append(b)
    seen=set(); stack=[start]
    while stack:
        n=stack.pop()
        if n in seen: continue
        seen.add(n); stack.extend(g.get(n,[]))
    return seen
for name,e in (("flat",edges_flat),("zoned",edges_zoned)):
    r=reach(e,"L4")
    print(f"{name}: L4 reaches {sorted(r)} count={len(r)} writes_to_SIS={'L1-SIS' in r}")
```

Expected output:

```text
flat: L4 reaches ['L0', 'L1-PLC', 'L1-SIS', 'L2', 'L3', 'L4'] count=6 writes_to_SIS=True
zoned: L4 reaches ['L0', 'L1-PLC', 'L2', 'L3', 'L3.5', 'L4'] count=6 writes_to_SIS=False
```

### Common errors and limits

- Producing exploit steps.
- Ignoring safety PLC independence.
- Counting graph edges as residual risk without consequence analysis.

### Exercises — chapter 23

**EX045 — Apply threat and failure analysis.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX046 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: threat and failure analysis advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 23 of 50

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — OT, IoT and cyber-physical security: methods I

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: methods I** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 24.1 Purpose

risk matrices with consequence units in physical terms, zone risk assessment per 62443-3-2 as a method, and when to use qualitative vs quantitative approaches.

### 24.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 24.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 24.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies methods I to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 24

**EX047 — Apply methods I.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX048 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: methods I advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 24 of 50

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes and connection

After this chapter you can apply **Design studio I** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 25.1 Purpose

a facilitated studio that selects a zone map for ABP, records ADRs, and produces a revision-controlled architecture sketch.

### 25.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 25.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 25.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies design studio I to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 25

**EX049 — Apply Design studio I.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX050 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Design studio I advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 25 of 50

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: architecture alternatives

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: architecture alternatives** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 26.1 Purpose

compare flat, Purdue+DMZ, and unidirectional-gateway options with reachability and operability scores.

### 26.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 26.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 26.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies architecture alternatives to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 26

**EX051 — Apply architecture alternatives.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX052 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: architecture alternatives advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 26 of 50

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — OT, IoT and cyber-physical security: control design

### Learning outcomes and connection

After this chapter you can specify detection and interlock controls, including a residual CUSUM for single-sensor replay.

### 27.1 Alarm philosophy

Alarms need priority, consequence and response. Cyber-informed alarms (residual high) join process alarms.

### 27.2 Residual detection

Mass-balance residual + CUSUM detects class A replay; class B (second sensor spoofed) fails — a design boundary.

### 27.3 BPCS vs SIS

Safety functions live in SIS-B with independent sensors where required; do not "fix" safety by blocking it from the SCADA path without safety assessment.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.


In addition, record the scan-cycle budget and any actuator stroke delay that bounds how fast the process can move after a forged command; without those times, delay metrics are uninterpretable. State whether the SIS is independent of the BPCS path under test.
### Worked example (synthetic Ashford Batch Plant)

Lab 27 on synthetic reactor level:

### Practical activity

```python
# Lab 27 - residual CUSUM vs band on batch reactor level (synthetic)
import random
def run(seed, atk, det, k=0.8, h=6.0):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(500):
        inflow=1.0+rng.gauss(0,0.05)+(0.08 if atk and t>=250 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=250: lvl=50+rng.gauss(0,0.3)
        if atk=="B" and t>=250: fm=1.0+rng.gauss(0,0.02)
        est+=fm-0.02*est
        hit=abs(lvl-50)>2.0 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-k); hit=s>h
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,None,det) is not None for i in range(60))
    for atk in ("A","B"):
        hits=[a-250 for a in (run(i,atk,det) for i in range(60)) if a is not None and a>=250]
        print(f"{det} class{atk} FA={fa}/60 det={len(hits)}/60 mean_delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Expected output:

```text
band classA FA=0/60 det=0/60 mean_delay=nan
band classB FA=0/60 det=0/60 mean_delay=nan
cusum classA FA=0/60 det=60/60 mean_delay=24.8
cusum classB FA=0/60 det=0/60 mean_delay=nan
```

### Common errors and limits

- Relying on band alarms alone against replay.
- Putting detection logic only in the same PLC that is attacked.
- Hiding class B failure.

### Exercises — chapter 27

**EX053 — Apply control design.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX054 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: control design advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 27 of 50

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — OT, IoT and cyber-physical security: implementation I

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: implementation I** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 28.1 Purpose

allow-lists, engineering jump hosts, secure project transfer, and configuration baselines.

### 28.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 28.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 28.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies implementation I to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 28

**EX055 — Apply implementation I.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX056 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: implementation I advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 28 of 50

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — OT, IoT and cyber-physical security: measurement

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: measurement** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 29.1 Purpose

event recall, delay, false alarms/shift, overfill at alarm; avoid point-adjusted F1 as sole metric.

### 29.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 29.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 29.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies measurement to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 29

**EX057 — Apply measurement.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX058 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: measurement advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 29 of 50

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes and connection

After this chapter you can apply **Verification laboratory I** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 30.1 Purpose

execute a planned test suite on the synthetic model and record verdicts against R1–R4.

### 30.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 30.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 30.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies verification laboratory I to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 30

**EX059 — Apply Verification laboratory I.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX060 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Verification laboratory I advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 30 of 50

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — OT, IoT and cyber-physical security: implementation II

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: implementation II** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 31.1 Purpose

monitoring use cases, historian integrity, backup/restore drills on engineering systems.

### 31.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 31.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 31.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies implementation II to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 31

**EX061 — Apply implementation II.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX062 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: implementation II advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 31 of 50

[← Chapter 30](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — OT, IoT and cyber-physical security: reliability

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: reliability** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 32.1 Purpose

MTBF/MTTR of security appliances, fail-open vs fail-closed conduits, and common-cause with controllers.

### 32.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 32.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 32.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies reliability to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 32

**EX063 — Apply reliability.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX064 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: reliability advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 32 of 50

[← Chapter 31](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — OT, IoT and cyber-physical security: safety and resilience

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: safety and resilience** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 33.1 Purpose

SIS independence, bypass management, cyber-informed HAZOP, recovery to a safe state.

### 33.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 33.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 33.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies safety and resilience to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 33

**EX065 — Apply safety and resilience.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX066 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: safety and resilience advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 33 of 50

[← Chapter 32](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — OT, IoT and cyber-physical security: integration

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: integration** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 34.1 Purpose

end-to-end batch start under CNHP controls; interface contracts between MES, SCADA and PLC.

### 34.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 34.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 34.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies integration to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 34

**EX067 — Apply integration.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX068 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: integration advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 34 of 50

[← Chapter 33](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes and connection

After this chapter you can apply **Design studio II** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 35.1 Purpose

revise architecture after a tabletop that injects class B sensor spoofing; update ADRs.

### 35.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 35.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 35.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies design studio II to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 35

**EX069 — Apply Design studio II.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX070 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Design studio II advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 35 of 50

[← Chapter 34](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — OT, IoT and cyber-physical security: performance and scale

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: performance and scale** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 36.1 Purpose

scan-time budgets, mirror-port capacity, detector CPU load, alarm rates under burst conditions.

### 36.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 36.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 36.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies performance and scale to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 36

**EX071 — Apply performance and scale.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX072 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: performance and scale advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 36 of 50

[← Chapter 35](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — OT, IoT and cyber-physical security: operations

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: operations** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 37.1 Purpose

shift handover of cyber alarms, patch windows, vendor access procedures, exercise cadence.

### 37.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 37.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 37.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies operations to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 37

**EX073 — Apply operations.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX074 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: operations advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 37 of 50

[← Chapter 36](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — OT, IoT and cyber-physical security: validation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: validation** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 38.1 Purpose

factory/site acceptance for security requirements; freeze thresholds before validation like research practice.

### 38.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 38.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 38.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies validation to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 38

**EX075 — Apply validation.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX076 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: validation advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 38 of 50

[← Chapter 37](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — OT, IoT and cyber-physical security: maintainability

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: maintainability** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 39.1 Purpose

documentation, spare PLC images, key rotation, obsolescence plans for unsupported protocol stacks.

### 39.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 39.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 39.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies maintainability to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 39

**EX077 — Apply maintainability.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX078 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: maintainability advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 39 of 50

[← Chapter 38](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes and connection

After this chapter you can apply **Verification laboratory II** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 40.1 Purpose

regression suite after a change; hash manifests; independent review of results.

### 40.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 40.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 40.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies verification laboratory II to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 40

**EX079 — Apply Verification laboratory II.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX080 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Verification laboratory II advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 40 of 50

[← Chapter 39](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — OT, IoT and cyber-physical security: system optimization

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: system optimization** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 41.1 Purpose

trade false alarms vs delay; cost of independent sensors vs residual risk accepted.

### 41.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 41.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 41.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies system optimization to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 41

**EX081 — Apply system optimization.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX082 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: system optimization advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 41 of 50

[← Chapter 40](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — OT, IoT and cyber-physical security: applied research

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: applied research** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 42.1 Purpose

a bounded experiment to choose detector parameters — research in service of design, not publication.

### 42.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 42.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 42.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies applied research to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 42

**EX083 — Apply applied research.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX084 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: applied research advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 42 of 50

[← Chapter 41](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes and connection

After this chapter you can apply **Industry or public-service practice** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 43.1 Purpose

placement expectations: observe, do not touch production, write a reflective risks-and-controls memo.

### 43.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 43.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 43.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies industry practice to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 43

**EX085 — Apply Industry or public-service practice.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX086 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Industry or public-service practice advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 43 of 50

[← Chapter 42](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes and connection

After this chapter you can apply **Engineering capstone I** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 44.1 Purpose

scope CNHP delivery: architecture, requirements trace, test plan, safety bounds.

### 44.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 44.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 44.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies capstone I to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 44

**EX087 — Apply Engineering capstone I.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX088 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Engineering capstone I advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 44 of 50

[← Chapter 43](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes and connection

After this chapter you can apply **Independent design review** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 45.1 Purpose

red-team the design with checklists; record findings and dispositions.

### 45.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 45.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 45.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies independent design review to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 45

**EX089 — Apply Independent design review.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX090 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Independent design review advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 45 of 50

[← Chapter 44](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes and connection

After this chapter you can apply **Engineering capstone II** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 46.1 Purpose

complete implementation evidence on synthetic/lab systems; freeze the evidence pack.

### 46.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 46.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 46.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies capstone II to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 46

**EX091 — Apply Engineering capstone II.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX092 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Engineering capstone II advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 46 of 50

[← Chapter 45](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes and connection

After this chapter you can apply **Failure and recovery trial** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 47.1 Purpose

tabletop plus synthetic-model trial of SCADA loss and class A replay; measure recovery times.

### 47.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 47.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 47.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies failure and recovery trial to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 47

**EX093 — Apply Failure and recovery trial.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX094 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Failure and recovery trial advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 47 of 50

[← Chapter 46](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes and connection

After this chapter you can apply **Evidence dossier** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 48.1 Purpose

assemble requirements, ADRs, test results, residual risks with owners.

### 48.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 48.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 48.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies evidence dossier to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 48

**EX095 — Apply Evidence dossier.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX096 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Evidence dossier advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 48 of 50

[← Chapter 47](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes and connection

After this chapter you can apply **Engineering thesis** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 49.1 Purpose

monograph structure arguing CNHP meets R1–R4 within stated assumptions.

### 49.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 49.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 49.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies engineering thesis to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 49

**EX097 — Apply Engineering thesis.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX098 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Engineering thesis advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 49 of 50

[← Chapter 48](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes and connection

After this chapter you can apply **Final defense** to the Ashford Batch Plant CNHP with verifiable outputs and explicit residual risk.

### 50.1 Purpose

claim audit, examiner questions, disclosure posture, operator brief with confidence levels.

### 50.2 Method

Define inputs (inventory, zone map, threat assumptions), steps, and outputs (artefacts with owners). Use only synthetic ABP data or isolated lab rigs with independent physical safety layers.

### 50.3 Interface to other chapters

Upstream artefacts feed this chapter; downstream chapters consume its outputs. Traceability IDs (R#, ADR-#, T#) stay stable across revisions.

### 50.4 Quality bar

A reviewer should be able to re-run any calculation, see the assumption list, and find the residual risk owner without asking you.

### Engineering notes for this chapter

On the synthetic Ashford Batch Plant, every calculation supports a Control Network Hardening Programme decision: a requirement identifier, an architecture decision record, a test case or a residual risk with an owner. State the units of every quantity (metres cubed, seconds, scans, alarms per shift). Separate **observations** (what a log or simulation printed) from **claims** (what you assert about detection or safety) and never promote a network event to a physical-consequence claim without a process model. If a laboratory activity is physical, bound it with an independent safety layer and a named stop authority; this course never authorises work on production PLCs, safety systems or plant networks. Re-verify cited standards (NIST SP 800-82 Rev. 3, ISA/IEC 62443, ATT&CK for ICS, Modbus specifications) before relying on a clause in a real project. Keep synthetic data labelled synthetic so that teaching numbers cannot be mistaken for field measurements.

### Worked example (synthetic Ashford Batch Plant)

CNHP applies final defense to reactor R-101 and tanks T-1/T-2. Results are teaching artefacts only.

### Practical activity

Produce the chapter's primary artefact (one to two pages) for ABP with IDs and assumptions listed.

### Common errors and limits

- Missing residual-risk owner.
- Using production systems.
- Artefacts without version IDs.
- Overclaiming field effectiveness.

### Exercises — chapter 50

**EX099 — Apply Final defense.** *Objective:* produce the required artefact for ABP. *Inputs:* chapter text. *Steps:* (1) draft; (2) list assumptions; (3) name residual-risk owner. *Expected evidence:* artefact. *Rubric:* 3 = complete, scoped, owned; 2 = thin ownership; 1 = vague; 0 = none.

**EX100 — Critique.** *Objective:* find one overclaim in a peer's draft and rewrite it. *Inputs:* peer artefact or your own prior draft. *Steps:* mark verb; rewrite with scope. *Expected evidence:* before/after. *Rubric:* 3 = precise rewrite; 2 = weak; 1 = nitpick only; 0 = none.

### Chapter synthesis

Final defense advances CNHP when artefacts are verifiable, assumptions listed and residual risks owned. ABP is synthetic; do not touch production systems.

### Continue studying — chapter 50 of 50

[← Chapter 49](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · End of route

<a id="worked-results"></a>

## Worked results

One defensible answer per exercise; alternatives that meet evidence and scope standards also earn full marks. All ABP numbers are synthetic.

### Chapter 1

- **EX001** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX002** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 2

- **EX003** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX004** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 3

- **EX005** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX006** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 4

- **EX007** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX008** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 5

- **EX009** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX010** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 6

- **EX011** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX012** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 7

- **EX013** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX014** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 8

- **EX015** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX016** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 9

- **EX017** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX018** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 10

- **EX019** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX020** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 11

- **EX021** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX022** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 12

- **EX023** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX024** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 13

- **EX025** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX026** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 14

- **EX027** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX028** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 15

- **EX029** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX030** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 16

- **EX031** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX032** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 17

- **EX033** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX034** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 18

- **EX035** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX036** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 19

- **EX037** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX038** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 20

- **EX039** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX040** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 21

- **EX041** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX042** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 22

- **EX043** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX044** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 23

- **EX045** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX046** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 24

- **EX047** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX048** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 25

- **EX049** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX050** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 26

- **EX051** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX052** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 27

- **EX053** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX054** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 28

- **EX055** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX056** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 29

- **EX057** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX058** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 30

- **EX059** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX060** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 31

- **EX061** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX062** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 32

- **EX063** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX064** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 33

- **EX065** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX066** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 34

- **EX067** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX068** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 35

- **EX069** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX070** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 36

- **EX071** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX072** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 37

- **EX073** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX074** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 38

- **EX075** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX076** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 39

- **EX077** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX078** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 40

- **EX079** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX080** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 41

- **EX081** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX082** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 42

- **EX083** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX084** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 43

- **EX085** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX086** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 44

- **EX087** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX088** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 45

- **EX089** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX090** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 46

- **EX091** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX092** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 47

- **EX093** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX094** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 48

- **EX095** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX096** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 49

- **EX097** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX098** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

### Chapter 50

- **EX099** — Complete the stated drill with correct calculation or artefact, explicit units/assumptions, and a scoped design conclusion for synthetic ABP only.
- **EX100** — Deliver the required critique or assumption/ownership table; overclaims rewritten with evidence and scope; residual risk named.

**End of worked results.** Return to the [course chapter index](../SUBJECTS.md).
