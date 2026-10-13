# OT, IoT and Cyber-Physical Security: Engineering Secure Control Systems

- Language: English (`en`); engineering course, five years; approximately 4,000 hours of planned study.
- Editorial state: **draft**. Chapters 1–50 of 50 have authored teaching text; exercises EX001–EX150 have matching worked results; offline labs use Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: future engineers who will design, implement and verify security for industrial control, OT and cyber-physical systems.
- Relation to neighbouring books: the critical-infrastructure engineering book emphasises sectors; the master's OT book emphasises empirical study design. **This book is about building control-system security**.
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
| **Lena Okafor** | Engineer on CNHP | Invented |

### Core sources

- NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); Modbus [Application Protocol V1.1b3](https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf); Giraldo et al. [CSUR 2018](https://doi.org/10.1145/3203245); Urbina et al. [CCS 2016](https://doi.org/10.1145/2976749.2978388).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) model a tank level as the integral of net flow; (2) use that model to compute how long operators have after a pump stops; (3) explain why that time is a security quantity, not only a process one.

### 1.1 Level is accumulated flow

Feed tank T-1 at Ashford Batch Plant (ABP) holds V(t) cubic metres. If the make-up pump stops at t = 0 and the reactor keeps drawing q(t) m³/h, then V(t) = V₀ − ∫₀ᵗ q(s) ds. The level falls exactly as fast as the outflow, and the time until it reaches the minimum safe hold-up V_min is the t* that solves ∫₀^t* q(s) ds = V₀ − V_min. When q is constant this is (V₀ − V_min)/q; when q varies, you integrate.

### 1.2 Why a security engineer cares

An attacker who can stop a pump or spoof a level reading changes this integral. The hold-up time is the window in which operators or a safety system must notice and act. If T-1 holds 12 m³, the minimum is 2 m³ and the reactor draws about 1.8 m³/h, operators have roughly 5.5 hours. That number goes straight into the detection requirement: an alarm that fires after six hours detects nothing useful. Calculus turns "detect quickly" into "detect within 5.5 hours, with margin".

Lena writes the number into the requirement together with how it was calculated.

### 1.3 Varying draw

ABP's draw oscillates with the batch recipe: q(t) = 1.8 + 0.4 sin(2πt/6). Its integral has a closed form, and the lab solves for t* by bisection. The answer, 5.53 h, is close to the average-rate estimate of 5.56 h because the oscillation averages out over a full six-hour cycle; with a shorter window or a skewed recipe the two would diverge, and the conservative choice is the smaller time.

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

> **Synthetic case — Ashford Batch Plant.** Lena Okafor, engineer on the Control Network Hardening Programme (CNHP), used the hold-up calculation to argue that a low-level alarm on T-1 must be independent of PLC-A, because a compromised PLC could suppress both pump status and the alarm inside the 5.5-hour window.

### 1.4 Errors and limits

Models assume the level sensor is honest; Chapter 29 treats sensor spoofing. Mixing m³/h with minutes is the most common slip. Always choose the conservative root when uncertainty is large.

A spoofed level reading is the case this model cannot handle: if the transmitter reports a full tank while T-1 drains, the integral is correct but nobody is looking at it. That is why Lena pairs the hold-up calculation with an independent level switch. Check units at every step, write the time in hours with the assumed draw beside it, and repeat the calculation whenever the recipe changes the reactor's demand.

### Exercises

- **EX001 — Constant draw.** T-2 holds 9 m³, minimum 1.5 m³, constant draw 1.25 m³/h. Time to minimum? Rubric: 3 = 6.0 h with working; 2 = right method, arithmetic slip; 1 = formula only; 0 = none.
- **EX002 — Requirement.** Turn your EX001 answer into a detection requirement with margin. Rubric: 3 = time bound with stated margin and independence from the controlling PLC; 2 = time bound only; 1 = vague "fast"; 0 = none.
- **EX003 — Lab reading.** Why are the bisection and average-rate answers so close here, and when would they not be? Rubric: 3 = full sine cycle averages to 1.8; skewed or short window diverges; 2 = one half; 1 = vague; 0 = wrong.

### Synthesis

Hold-up time is an integral and a security budget at once: it bounds how late detection may be.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) represent an OT network as a directed graph; (2) compute reachability between Purdue levels; (3) prove that removing an edge cannot add a path.

### 2.1 Graphs of conduits

In ISA/IEC 62443 vocabulary, zones are groups of assets with common security requirements and conduits are the permitted communication paths between them. A directed graph models this exactly: nodes are zones (L4 office, L3.5 DMZ, L3 historian, L2 SCADA, L1 PLC, L1 SIS, L0 I/O) and an edge a→b means a can initiate traffic to b. Asking "can the office network write to the safety system?" becomes "is L1-SIS reachable from L4?".

Lena builds ABP's graph from the firewall export, not from the network diagram, because the export is what is enforced.

### 2.2 Reachability

Depth-first search computes the set of nodes reachable from a start node in time proportional to nodes plus edges. Reachability is transitive: if L4→L3 and L3→L2 and L2→L1-SIS, then L4 reaches SIS even with no direct rule. Firewall reviews that check rules one at a time miss exactly this composition, which is why engineers compute closure rather than reading rule lists.

Lena runs the search from every zone, not only the office, and keeps the result as a table that the next review can compare against.

### 2.3 Monotonicity proof

Claim: deleting an edge never enlarges a reachable set. Proof: any path in the smaller graph uses only edges that also exist in the larger graph, so every node reachable after deletion was reachable before. The practical rule follows: rule removals can be approved quickly; rule additions need analysis, because they can create new transitive paths.

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

> **Synthetic case — Ashford Batch Plant.** ABP's original network had a convenience rule L4→L2 for remote HMI viewing. The reachability lab shows that in the flat design the office zone reaches L1-SIS; in the zoned design with a DMZ and no SCADA→SIS conduit, it does not.

### 2.4 Errors and limits

Graphs model permitted initiation, not actual traffic or vulnerabilities. Bidirectional protocols and remote-access tools can create hidden reverse edges; inventory them explicitly.

Lena adds a remote-access tool used by a vendor as an explicit edge from outside the plant into L2, since its sessions are initiated outward but carry commands inward. Without that edge, the graph would show the office cut off from SCADA while a support session could still reach it. Each such edge is listed with its owner and the record that justifies it, and the graph is rebuilt after any change to remote-access tooling or vendor contracts.

### Exercises

- **EX004 — Closure.** Edges: A→B, B→C, C→D, B→E. List all nodes reachable from A. Rubric: 3 = {A,B,C,D,E}; 2 = one missing; 1 = direct only; 0 = none.
- **EX005 — Proof use.** Explain in two sentences why adding L3→L1-SIS needs more review than removing L4→L2. Rubric: 3 = addition can create new transitive paths, removal cannot (monotonicity); 2 = intuition only; 1 = vague; 0 = wrong.
- **EX006 — Lab.** Which single edge in the flat design gives L4 its path to L1-SIS? Rubric: 3 = L2→L1-SIS (with L4→L2 or L4→L3→L2 upstream); 2 = names L4→L2 only; 1 = vague; 0 = wrong.

### Synthesis

Zones and conduits are a graph; reachability, not rule-by-rule reading, answers who can touch the safety system.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) compute serial-link timing for fieldbus polling; (2) relate physical process speed to required control cycle times; (3) recognise that physical signals can be manipulated outside the network.

### 3.1 Bits on a wire

Much plant communication still runs over RS-485 serial at rates such as 115,200 bit/s. With one start bit, eight data bits and one stop bit, each byte costs ten bit-times. A 40-byte Modbus RTU response therefore takes 40 × 10 / 115,200 ≈ 3.5 ms on the wire, before device processing. Summing every poll in a cycle tells you whether the schedule fits the controller's cycle budget.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Expected output:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

Lena does this sum for the trunk to PLC-A before approving any monitoring device on it, and the result is the 21 ms figure she later uses throughout the programme.

### 3.2 Process time constants

A level loop on a 12 m³ tank changes over minutes; a pressure loop on a compressor changes in tens of milliseconds. The required control and detection speed follows the physics. Security monitoring that adds 200 ms of latency is harmless on the tank and dangerous on the compressor. Always ask what the process time constant is before inserting inspection devices inline.

For ABP, the feed tanks and reactor level are slow loops, while a compressor skid nearby is fast. Lena lists the loops on each trunk with their time constants before choosing where a monitor may sit.

### 3.3 Physical-layer manipulation

Sensors measure physics: a 4–20 mA loop, a thermocouple voltage, a pulse from a flow meter. An adversary or a fault can alter those signals without touching any network packet — by injecting current, heating a probe or vibrating a meter. Network monitoring cannot see this; physical plausibility checks (Chapter 29) and tamper-evident enclosures can.

> **Synthetic case — Ashford Batch Plant.** Lena's polling budget for the RS-485 trunk to PLC-A came to 21 ms per cycle, comfortably inside the 100 ms cycle. That left room for an inline serial monitor, which she approved only after measuring its added latency on a bench copy.

### 3.4 Errors and limits

Timing calculations ignore device turnaround and retries; measure on a bench before committing. Do not test signal injection on live loops.

Lena's bench copy of the RS-485 trunk to PLC-A is where the polling budget and the serial monitor's added latency were measured, and it is the only place course work touches serial timing. Any signal-injection experiment, even a small bias on a 4–20 mA loop, belongs on a bench with a spare transmitter, never on T-1's live loop. Record bench results with the equipment used, because a different transmitter or cable can change the numbers.

### 3.5 Worked example — signal levels and the time budget (synthetic ABP)

T-1's level transmitter sends a 4–20 mA signal over 180 m of twisted pair to PLC-A. A 0.2 mA bias injected at a marshalling cabinet shifts the reading by 0.2/16 = 1.25 % of span, which for the transmitter's 9 m³ calibrated span is about 0.11 m³ — small enough to hide inside normal noise. The tank's time constant (span over typical inflow, 9/1.25 ≈ 7.2 h) tells Lena how long such a bias can act before the hold-up calculation from Chapter 1 is wrong by a whole safety margin. She therefore specifies a second, independent level switch on T-1 wired to SIS-B and a periodic comparison of transmitter and switch, because a physical-layer attack on one loop cannot then silently defeat both.

### Exercises

- **EX007 — Wire time.** How long does a 120-byte frame take at 19,200 bit/s with 10 bits per byte? Rubric: 3 = 62.5 ms with working; 2 = slip; 1 = method; 0 = none.
- **EX008 — Budget.** Using the lab's 244 bytes per cycle, what is the slowest baud rate that still fits a 50 ms budget? Rubric: 3 = 48,800 bit/s (so 57,600 standard) with working; 2 = number without standard rate; 1 = method; 0 = none.
- **EX009 — Physical.** Give two physical-layer manipulations a network IDS cannot detect and one compensating control each. Rubric: 3 = two manipulations plus controls; 2 = two without controls; 1 = one; 0 = none.

### Synthesis

Physics sets the timing budget for control and for any security device you put in the loop.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, pure functions that decide whether an OT message is permitted; (2) represent industrial addresses with exact types; (3) test against synthetic decoded traffic, never live plant traffic.

### 4.1 Decisions as functions

An allow-list for Modbus is a function `permit(source, function_code, register) -> (bool, reason)`. Making it pure — inputs in, decision out, no hidden configuration — lets you test it on a laptop with synthetic records. The reason string matters: "register-out-of-range" tells a reviewer that the HMI tried to write outside the setpoint block, which is a different story from an unknown station using a diagnostic function.

Lena keeps the reason strings short and fixed so that logs can be counted by reason.

### 4.2 Exact types

Store function codes as integers, register ranges as `range` objects, and station identities as fixed strings from an inventory. A frequent bug treats the 4xxxx "holding register" notation as a string and matches by prefix, so 400500 looks like 40050. Convert addresses once, at parse time, into integers with documented offsets.

Lena writes one conversion function for register addresses and tests it at both ends of the HMI's writable range, 40001 and 40010, and one step outside each. Station names come from the inventory, so a typo in the allow-list fails a lookup instead of silently creating a new station that matches nothing.

### 4.3 Tests on synthetic decoded frames

The lab below never opens a socket; it checks already-decoded tuples. That is deliberate. Course code must not send Modbus traffic to any device. Write one test per rule, plus boundary registers 40001 and 40010.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Expected output:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

Tests are grouped by rule so that a failure points straight at the clause that broke. The historian's write test, which caught function 16, is kept as a permanent case. Lena's test table lists each tuple, the expected decision and the reason string, and a reviewer can read it without running anything. New stations or registers added to the allow-list arrive with their own rows in the same pull request.

### 4.3b Logging what the function decided

Every decision should be logged with the source, function code, register, decision, reason and the version of the allow-list file. When an operator asks why an HMI write was blocked at 03:12, the log answers in one line. Without the version field, nobody can tell whether the block came from yesterday's list or today's.

> **Synthetic case — Ashford Batch Plant.** Lena's first allow-list let HIST-1 use function 16 (write multiple registers) because it "only reads". The test table caught it: the historian has no business writing, so function 16 was removed and the test now expects BLOCK.

### 4.4 Errors and limits

An allow-list on a monitor is only as good as the decoder. Malformed frames must be counted and alarmed, not silently dropped. Real enforcement devices need vendor validation before deployment.

Lena's monitor counts malformed frames per minute and raises an alarm if the count rises, because a sudden burst can mean a failing device or a decoder bug. Treating such frames as permitted would turn every decoder gap into an open door. The monitor in this course only observes; any device that actually blocks traffic at ABP is a vendor product validated on the bench first.

### Exercises

- **EX010 — Rule.** Write the permit rule (in words or code) for "HIST-1 may read input and holding registers, nothing else". Rubric: 3 = fc 3 and 4 only, all else BLOCK with reason; 2 = misses a reason; 1 = vague; 0 = includes writes.
- **EX011 — Boundary.** Which register values test the edges of the HMI write range in the lab, and what is expected for 40011? Rubric: 3 = 40001 and 40010 PASS, 40011 BLOCK; 2 = one edge; 1 = vague; 0 = wrong.
- **EX012 — Lab.** Why does ENG-WS fc=8 block, and why is that the right default? Rubric: 3 = no (ENG-WS, 8) entry; diagnostics/default-deny; 2 = first half; 1 = vague; 0 = wrong.

### Synthesis

Pure, typed, tested permit functions are the smallest trustworthy unit of OT security software.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write OT security findings that operators and safety engineers can act on; (2) separate observation, consequence and recommendation; (3) avoid alarmist or unbounded language.

### 5.1 Three audiences

A control-room operator needs to know what to watch for. A process-safety engineer needs to know whether a safety function is affected. A manager needs cost and downtime. One finding can serve all three if it states: asset and zone; what was observed and how; the plausible process consequence; the safety-layer status; the fix and the maintenance window needed.

Lena writes each finding once, in that order, so each reader finds their part quickly. A finding missing any of these parts goes back to its author before review.

### 5.2 Bounded consequences

"An attacker could blow up the plant" is neither true nor useful. A bounded statement reads: "A station on L2 can write setpoint registers on PLC-A without authentication. A setpoint change on T-1 level could overfill the tank in roughly 40 minutes; the independent high-high trip on SIS-B would stop the feed pump before overflow." This names the path, the time, and the protective layer that still holds.

Lena checks every bounded statement with the process-safety engineer before it is sent, since the minutes to overflow and the trip that holds come from the safety analysis, not from the security team.

### 5.3 Structure of a short report

Summary (three sentences); scope and method; findings ordered by consequence; residual risk with protective layers named; appendix with evidence references. Diagrams of zones are worth more than pages of rule tables.

Lena's reports for CNHP fit on two pages plus the appendix. The summary names the most serious finding and whether any safety function is affected. Each finding cites its evidence by hash and states the maintenance window needed for the fix, so planners can schedule it. A zone diagram with the affected conduit highlighted usually explains the finding faster than the text.

### 5.3b Words to avoid and words to use

Avoid "trivial", "catastrophic" and "fully compromised": none can be checked. Use measured quantities — minutes to overflow, number of reachable zones, protective layers intact — and name the evidence. A safety engineer will trust a finding that says "SIS-B remains independent" far more than one that says "everything is at risk".

> **Synthetic case — Ashford Batch Plant.** Lena's first draft of a finding said the SCADA network was "totally insecure". The review version: "Remote-viewing rule L4→L2 allows office hosts to reach SCADA servers (rule FW-12, observed in configuration export 3 March). Recommend removal; viewing via the DMZ historian replica instead. Downtime: none."

### 5.4 Errors and limits

Never include working attack procedures in reports; reference the evidence store. Do not claim a safety consequence without the safety engineer's review.

Evidence such as configuration exports stays in the sealed store, and the report cites it by hash, so anyone with access can verify it without the report carrying sensitive detail. Lena sends every finding that mentions SIS-B or a trip to the process-safety engineer for review before release, and records the reviewer's name in the report. A consequence the engineer has not confirmed is written as a question, not a claim.

### Exercises

- **EX013 — Rewrite.** Rewrite "the PLC can be hacked" as a bounded finding sentence for PLC-A. Rubric: 3 = path, zone, observation, consequence bound, protective layer; 2 = one missing; 1 = still vague; 0 = unchanged.
- **EX014 — Audience.** For the FW-12 finding, write one sentence each for operator, safety engineer and manager. Rubric: 3 = three tailored sentences; 2 = two; 1 = one; 0 = none.
- **EX015 — Residual risk.** After FW-12 removal, state one residual risk honestly. Rubric: 3 = specific remaining path (e.g. engineering workstation, vendor remote access) and its control; 2 = generic; 1 = "none"; 0 = none.

### Synthesis

Good OT findings are bounded, name protective layers and give each audience what it needs to decide.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use series to reason about repeated retries of plant communications; (2) apply a simple differential model to alarm backlog; (3) decide when a continuous model is good enough for a maintenance debate.

### 6.1 Geometric retries on a fieldbus

If each Modbus request succeeds with probability p = 0.9 independently (synthetic, for a noisy trunk), the chance of succeeding within k tries is 1 − (1 − p)^k. With k = 3, that is 0.999. Retries raise reliability but multiply traffic: expected attempts until success equal 1/p ≈ 1.11, so a 1,000-poll cycle expects about 1,110 frames. The communications budget (Chapter 3) must count the retries, not only the logical polls.

Lena includes retries when she checks the RS-485 trunk to PLC-A, since a noisy period can raise traffic by a tenth or more.

### 6.2 Alarm backlog as a rate equation

Let B(t) be open alarms. Alarms arrive at rate a and are acknowledged at rate c when staffed. Then B′ ≈ a − c. If a = 3.3/h (the pre-rationalisation rate from the alarm lab) and two operators together clear 2.0/h, the backlog grows. After rationalisation to 1.05/h, the same staff clears it. The model is crude — it ignores priority — but it makes staffing and rationalisation quantitative.

```python
"""Lab: alarm load per operator hour before and after rationalisation (synthetic counts)."""
before = {"T-1 high": 140, "T-2 high": 95, "R-101 temp": 30, "pump trip": 6, "comm loss PLC-A": 210, "door open": 75}
remove = {"comm loss PLC-A": 200, "door open": 70, "T-1 high": 110}   # chattering/duplicate alarms removed
hours = 24 * 7
tb = sum(before.values()); ta = tb - sum(remove.values())
print(f"week alarms before={tb} after={ta}")
print(f"per operator-hour before={tb/hours:.2f} after={ta/hours:.2f}")
top = max(before, key=before.get)
print(f"worst source before: {top} ({before[top]/tb:.0%} of load)")
```

Expected output:

```text
week alarms before=556 after=176
per operator-hour before=3.31 after=1.05
worst source before: comm loss PLC-A (38% of load)
```

Lena uses the model to argue for rationalisation before asking for staff. The numbers made the case clearly.

### 6.3 When continuous is enough

Maintenance debates often need an order of magnitude: "Will 200 chattering communication-loss alarms per week overwhelm one operator?" Yes: that alone is about 1.2/h. Reserve exact analysis for loops that affect safety timing.

> **Synthetic case — Ashford Batch Plant.** The alarm lab cut weekly load from 556 to 176 by removing known chattering sources. Lena used B′ to show that one night operator could keep up after the change, which unblocked the CNHP proposal that had been stuck on "we need more staff first".

### 6.4 Errors and limits

Independence of retries fails when the trunk is systematically down. Backlog models ignore safety-critical alarms that must interrupt; treat those separately.

When the trunk to PLC-A is down, every retry fails together, so the geometric formula greatly overstates reliability; Lena treats a trunk outage as a separate case with its own alarm. Likewise, high-high level on T-1 or a trip from SIS-B must reach the operator at once, whatever the backlog of routine alarms. The rate model is for planning staffing and rationalisation, not for deciding which alarms may wait.

### Practice note

Keep a weekly plot of a and c next to the alarm-rationalisation log. When a rises after a firmware change, you know to look for a new chatter source before blaming the operators.

### Exercises

- **EX016 — Retries.** With p = 0.85 and 500 polls, expected frames? Rubric: 3 ≈ 588 with working; 2 = slip; 1 = formula; 0 = none.
- **EX017 — Backlog.** B(0)=40, a=1.0/h, c=1.5/h. Hours to clear? Rubric: 3 = 80 h; 2 = method; 1 = qualitative; 0 = none.
- **EX018 — Lab.** What fraction of pre-change load was "comm loss PLC-A"? Rubric: 3 = 38%; 2 = count only; 1 = vague; 0 = wrong.

### Synthesis

Series and rates turn "try again" and "hire someone" into numbers that fit a communications or staffing decision.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) report detection rates with intervals; (2) compare detectors without overclaiming; (3) refuse rankings that the sample cannot support.

### 7.1 Rates and intervals

Sixty synthetic trials with 0 false alarms and 60/60 detections sounds perfect — until you remember that a Wilson 95% interval for 0/60 still allows a few percent false-alarm rate in the long run. Report the interval, not only the point. For 60/60 detections the interval for the miss rate is also narrow, but it is not zero forever.

Lena's reports for CNHP give the count, the interval and the seed list together, so a reader can see both the result and how much it could move with more trials.

### 7.2 Comparing detectors

The residual CUSUM lab shows a band detector missing class-A attacks while CUSUM catches them with mean delay ~25 samples, both with 0/60 false alarms on this seed set. That is evidence that CUSUM beats the band *on these synthetic attacks*, not that CUSUM is universally better. Prefer paired designs on the same traces and state the attack class.

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

Lena's pilot plan keeps the same traces for both detectors and names the attack class tested, so the comparison can be repeated on new seeds later.

### 7.3 Base rates in the control room

If genuine cyber-physical attacks are rare, a detector with even a 1% false-alarm rate will dominate the operator's attention. Bayes' rule applies exactly as in Chapter 7 of neighbouring security courses: precision collapses when the base rate is tiny. Design for the plant's base rate, not a lab's balanced set.

> **Synthetic case — Ashford Batch Plant.** A vendor claimed "99% detection, 0% false alarms" from a 20-run demo. Lena asked for the attack class, the seed list and the false-alarm interval; none were provided. The pilot used the CUSUM lab design instead.

### 7.4 Errors and limits

Synthetic attacks are not the adversary. Intervals assume independent trials; correlated seeds invalidate them. Never invent a p-value for a table you did not test.

Lena's pilot reports state that the attacks were synthetic, list the seeds and explain how they were generated. If two seeds produce nearly identical traces, she counts them as one trial, because treating them as independent would make the interval look narrower than the evidence supports. Any statistical test she reports is one she actually ran, with its inputs kept so a reviewer can rerun it.

### Practice note

Publish the seed list and detector parameters with every detection claim in CNHP documents. Reproducibility is cheaper than arguing about a slide six months later, and it is what Urbina et al. and Giraldo et al. demand of evaluations.

### Exercises

- **EX019 — Interval.** State what 0/60 false alarms lets you claim at ~95%. Rubric: 3 = upper bound ~5–6% (rule of three / Wilson), not "zero forever"; 2 = bound only; 1 = "zero"; 0 = none.
- **EX020 — Lab.** For CUSUM on class A, report detections and mean delay. Rubric: 3 = 60/60 and ~24.8; 2 = one number; 1 = vague; 0 = wrong.
- **EX021 — Ranking refusal.** Band and CUSUM both show FA=0/60 on class B (no detections). Write the sentence that refuses calling them equal in quality. Rubric: 3 = cites no power / need class-A or larger n; 2 = vague caution; 1 = declares equal; 0 = none.

### Synthesis

Detection claims need intervals, attack class and base-rate honesty — not a single percentage.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) place PLC, SIS and SCADA on a privilege and dependency map; (2) explain why safety systems need independent hardware; (3) design evidence collection that does not require writing to the PLC.

### 8.1 Privilege in the plant

A PLC executes the basic regulatory loop. An SIS implements the safety instrumented functions and must be able to act when the PLC is wrong or compromised. SCADA and HMIs are supervisory: they set setpoints and display state. Architecture that lets SCADA write into SIS logic collapses that independence — which is exactly what the reachability lab warned about.

At ABP, PLC-A runs the regulatory loops on T-1, T-2 and R-101, and SIS-B holds the trips. Lena marks these roles on her privilege map.

### 8.2 Independence is physical

Independence is not a VLAN tag. It means separate controllers, sensors where required by the safety requirement specification, and conduits that do not allow the regulatory network to alter safety logic. NIST SP 800-82 and ISA/IEC 62443 both treat safety systems as needing careful zoning; process-safety standards (IEC 61511) go further on independence. Security architecture must not undo what safety architecture paid for.

Lena checks independence by tracing wires and conduits, not by reading labels in the network drawing. SIS-B's own level sensors on T-1 are the clearest example of that independence.

### 8.3 Evidence without writing to the PLC

Authorized assessment of OT prefers read-only methods: configuration exports, mirrored historian data, span ports, serial monitors in listen mode. Writing a test setpoint to a live PLC is a process change and needs the same authorization as an engineering change. Course labs never write to real devices.

> **Synthetic case — Ashford Batch Plant.** SIS-B is a separate controller with its own sensors for high-high level on T-1. CNHP's rule set forbids any conduit from L2/L3 into SIS engineering ports except through a locked physical keyswitch during scheduled tests.

### 8.4 Errors and limits

"Air gap" claims often hide USB, vendor laptops and cellular modems. Inventory those out-of-band paths as carefully as IP routes.

Lena's inventory for ABP lists every USB port on HMIs and engineering workstations, every vendor laptop that connects for support and every cellular modem fitted for remote diagnostics. Each gets an owner and a control, such as port blocking or a logged sign-out. A plant described as isolated is checked against this list before anyone repeats the claim in a report, because one forgotten modem can create a path the zone graph never shows.

### Practice note

Draw the privilege map on one page: who can change setpoints, who can change logic, who can change safety setpoints, and through which physical ports. Hang it in the engineering room. Arguments about "just a temporary rule" die faster when the map is visible.

### Exercises

- **EX022 — Map.** Name three actions that require SIS engineering privilege and three that a normal HMI may do. Rubric: 3 = six correctly split; 2 = four; 1 = vague; 0 = none.
- **EX023 — Independence.** Why is VLAN separation alone insufficient for SIS independence? Rubric: 3 = shared controller/sensors/management path can still couple; 2 = one reason; 1 = vague; 0 = claims VLAN enough.
- **EX024 — Evidence.** Propose a read-only evidence path for "HMI can write register 40050". Rubric: 3 = config export or monitored span showing the write capability / attempt, no live write; 2 = partial; 1 = live write; 0 = none.

### Synthesis

Keep safety logic independent in hardware and conduits; collect evidence without becoming an actuator.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) design a schema for OT findings that forbids exploit recipes; (2) implement idempotent updates keyed by asset and weakness; (3) property-test zone rules.

### 9.1 Schema without payloads

Store title, asset, zone, weakness class, evidence hash, consequence bound, protective layers intact, status. Reject fields named payload, shell or exploit. Evidence lives in a sealed store; the ticket holds the hash.

Lena's schema rejects a record outright if a forbidden field appears, rather than stripping it quietly, so the person who submitted it learns not to. Consequence bounds and intact protective layers are separate fields, which lets the safety engineer filter findings that touch SIS-B. The evidence hash links each ticket to its sealed proof without copying any of it into the ticket system.

### 9.2 Idempotent upserts

Two scanners reporting the same open Modbus write on PLC-A must become one finding. Fingerprint = (asset, weakness class, register-or-path). Retries and re-imports leave one row.

Lena tests this by importing the same scanner output twice and by importing two scanners' reports of the same issue; both cases must leave exactly one finding. The fingerprint uses the register or path, not the scanner's own wording, because two tools describe the same weakness differently. When fingerprints collide for genuinely different problems, a person splits them and records why.

### 9.3 Property tests for zones

State: "for every host in the office zone and every SIS register, permit is false". Generate synthetic hosts and assert. Property tests catch the bug where a new office subnet was added to inventory but not to the deny side of the allow-list.

> **Synthetic case — Ashford Batch Plant.** After the FW-12 finding, Lena added a property test: no L4 host may have a permit path to L1-SIS. CI runs it on every firewall-export change.

The test runs on synthetic hosts drawn from the inventory.

### 9.4 Errors and limits

Schemas drift; version them. Property generators that never emit the new subnet miss the bug they were written to catch — include inventory diffs as inputs.

Lena feeds the property test with the latest inventory diff, so every new subnet is tested in the next run. The schema has a version field, and older records are migrated with a recorded script rather than edited by hand. When a test is changed, she checks that it still fails on the original bug, since a property that can no longer fail protects nothing.

### Practice note

When someone asks for a "just this once" exception host, require a time-boxed exception object in the schema with an expiry and an owner. Exceptions without expiry become permanent conduits.

### 9.1b Schema evolution without downtime

When the finding schema gains a required field, deploy a two-phase change: first accept and persist the field as optional while backfilling; then flip the validator to required. Windows mid-flight must not break because a mobile client is one version behind. Publish the schema version in API responses so clients can refuse to write when incompatible. Bulk imports from scanners must pass the same validation path as interactive creates, including forbidden-field checks, or payloads will sneak in through the trusted import side door.

### Exercises

- **EX025 — Reject.** Write a validation rule that rejects payload-like fields. Rubric: 3 = rule + failing example; 2 = rule; 1 = idea; 0 = none.
- **EX026 — Fingerprint.** Why do two reports of PLC-A register 40050 collapse? Rubric: 3 = same fingerprint; 2 = "same finding"; 1 = vague; 0 = wrong.
- **EX027 — Property.** State one property after adding a DMZ zone. Rubric: 3 = e.g. L4 reaches L2 only via L3.5; 2 = informal; 1 = wrong; 0 = none.

### Synthesis

Schemas, idempotency and properties keep OT security tooling boring — in the good sense.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) refuse unauthorized plant access and dual-use requests; (2) apply stop conditions that protect process safety; (3) document consent so a review can reconstruct it.

### 10.1 Authorization is not enthusiasm

A plant manager saying "go ahead" in a corridor is not written authorization. OT work needs a signed scope naming units, methods, windows, stop conditions and a process-safety contact who can halt the plant. Without that document, the engineer stops. NIST SP 800-82 and ISA/IEC 62443 assume authorized, planned activity — not clever improvisation.

Lena keeps a copy of the signed scope with every work package and checks it before each session. If the scope does not cover a planned step, she stops and asks for an amendment rather than interpreting it generously. The process-safety contact's phone number is on the permit itself.

### 10.2 Dual use

This programme teaches zoning, monitoring, measurement and reporting. It does not teach exploit development against PLCs, weaponised protocol stacks or bypasses of safety systems. When a peer asks for "just the PoC against brand X", the answer is the finding description and the vendor's disclosure channel, not a working attack.

Lena's refusals are polite and specific, pointing to what she can offer instead: a finding with bounded consequences, a reference to the vendor's disclosure process and a design change that removes the exposure. The record of each request and refusal is kept with the project notes.

### 10.3 Stop conditions that protect the process

Stop if: an unexpected process alarm fires; latency or cycle time exceeds the budget; a safety system indicates a fault; the process-safety contact says stop. Software hard-denies help, but humans always win. Never disable a safety function to "make the test work".

> **Synthetic case — Ashford Batch Plant.** During a bench test of the serial monitor, cycle time rose above 50 ms. Lena stopped, removed the device, and re-tested on a spare trunk before any plant window was booked.

These conditions are printed on the permit.

### 10.4 Errors and limits

Ethics is a constraint on every later chapter. Legal text here is orientation, not advice. Live plants are never course lab targets.

Every later chapter assumes this boundary. Lena's work at ABP happens under a signed scope with named stop conditions and a process-safety contact; nothing in the course is ever aimed at a running plant. Where a question touches law, such as data protection or contracts with vendors, she asks the site's legal adviser rather than relying on course notes, and records the advice she received.

### Practice note

Print the stop conditions on the work permit hung at the panel. Under noise and time pressure, people remember what they can see. A stop condition buried in page 12 of a PDF is a stop condition that will be missed.


### 10.5 Worked example — a permit that says no (synthetic ABP)

A contractor asks to run an active Modbus scan of PLC-A during a batch "to finish the inventory faster". Lena's permit review applies three tests: is the owner's written authorization specific to this host and technique (it is not); does a stop condition exist that an operator can trigger (none was written); and is there a passive alternative (a mirror-port capture plus the engineering project export gives the same inventory). She declines the active scan, records the reason, and issues a permit for passive capture only, with the shift lead named as the person who can stop the work. NIST SP 800-82r3 warns that active scanning can disrupt OT devices, which is the engineering reason behind the ethical one.

### Exercises

- **EX028 — Refuse.** Two-sentence refusal to a request for a working PLC exploit for a graded assignment. Rubric: 3 = refuses, offers allowed alternative, cites safety; 2 = refuses only; 1 = vague; 0 = provides exploit.
- **EX029 — Stop.** List four stop conditions for an ABP window. Rubric: 3 = four process-relevant; 2 = three; 1 = one; 0 = none.
- **EX030 — Fields.** Six fields a signed OT work permit must contain. Rubric: 3 = units, methods, window, rate/impact limits, contacts, stop/resume; 2 = four; 1 = two; 0 = none.

### Synthesis

Written permission, process-first stop conditions and a refusal habit are safety engineering.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) describe what an authorized observer can learn from OT protocols without attacking them; (2) define function-code and register scope; (3) treat protocol denies as successful controls.

### 11.1 Observation points

Serial monitors see Modbus RTU on the wire; SPAN ports see Ethernet/IP or Modbus TCP; application logs see HMI actions. An assessment that only has HMI screenshots should not claim fieldbus visibility. State the vantage in the method section of every finding.

Lena writes the vantage point into each finding's method field, so readers know what could and could not be seen. At ABP, a serial monitor on the RS-485 trunk to PLC-A gives fieldbus visibility, while the HMI's own logs show operator actions. Findings based only on one of these say so, because each can miss what the other sees.

### 11.2 Ports are not semantics

TCP 502 often means Modbus TCP, but the meaningful scope is which function codes and which register ranges each station may use. Port 502 open is incomplete without the allow-list status and the stations observed. Chapter 4's permit function is the right abstraction.

Lena's findings about open ports always add which stations were seen using which function codes, so the reader knows whether the port matters. At ABP, the allow-list states that HMI-1 may write only registers 40001 to 40010 and that the historian may only read. A port scan alone would show none of that.

### 11.3 Denies are coverage

A firewall that blocks office-to-SCADA, or a monitor that drops function 16 from HIST-1, is evidence that a control worked for that probe. Coverage boards should count planned checks that were denied as completed checks, not as failures to get in.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Expected output:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

> **Synthetic case — Ashford Batch Plant.** The CNHP coverage board lists HIST-1 cannot write as a planned check. The lab's BLOCK on function 16 is a green result for that check, not a red test failed.

Lena's board shows each planned check with its expected result.

### 11.4 Errors and limits

Banner grabs lie; confirm with application-level or decoded-frame evidence. Course environments never scan live plants.

Lena treats a device banner as a hint and confirms the product from the engineering project export or from decoded frames before recording it in the inventory. Banners can be outdated after a firmware update or deliberately generic. The confirmation step also prevents a common error where a gateway's banner is mistaken for the controller behind it. In the course, all such checks run on captured or synthetic data, never on a live plant network.

### Practice note

Keep a one-page protocol inventory: trunk, baud rate, stations, function codes in use, allow-list owner. Update it when a vendor adds a station. Most mystery traffic is an undocumented engineering laptop.

### 11.1b Protocol families in the work permit

Work permits should name protocol families explicitly: Modbus TCP with function codes 3/4/6 on registers 40001-40010 is clearer than port 502. If write codes are forbidden from assessment stations, say so. If only listen-only taps are authorized, say so. Ambiguity here becomes an argument during the window when someone wants to try a diagnostic function just to see. When the permit names function codes, the monitor's allow-list for that window should name the same codes, so the permission and the evidence can be compared line by line.

At ABP, Lena's permit for serial verification says listen-only on the RS-485 trunk to PLC-A, names HMI-1's allowed writes, and forbids diagnostic function codes from the assessment laptop. During window W-17 a vendor's request to try a diagnostic was declined for exactly this reason, and evaluated later under its own permit.

### Exercises

- **EX031 — Vantage.** Match three evidence types to the minimum vantage. Rubric: 3 = correct mapping (e.g. RTU CRC errors to serial; Modbus TCP FC to IP decode; setpoint change attribution to HMI/app log); 2 = two; 1 = one; 0 = none.
- **EX032 — Scope.** Rewrite "test Modbus on PLC-A" as a scoped method card line. Rubric: 3 = codes, registers, stations, read-only, window; 2 = partial; 1 = port only; 0 = none.
- **EX033 — Lab.** Why does HMI-1 fc=6 reg=40050 block while 40003 passes? Rubric: 3 = register-out-of-range vs in WRITE_REGS; 2 = one side; 1 = vague; 0 = wrong.

### Synthesis

Scope OT protocols by semantics (codes, registers, stations); celebrate denies that match the plan.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) harden HMI and engineering workstations without breaking control; (2) collect OS evidence under least privilege; (3) plan patching inside maintenance windows.

### 12.1 Workstations are part of the control system

HMIs and engineering workstations often run general-purpose OSes with decades of legacy software. Treating them as just PCs is how malware walks into L2. Hardening baselines (application allow-listing, local admin removal, USB control) must be tested against the HMI vendor's support matrix — an unsupported hardening change that blanks a screen during a batch is an availability incident.

At ABP, Lena tests each hardening change on a bench HMI running the same vendor version before it reaches the control room, and records which items the vendor supports.

### 12.2 Least privilege for engineers

Named accounts, time-boxed admin rights, logged elevations. Shared engineer passwords are still common and still wrong: they destroy attribution and linger after contractors leave. Findings about shared passwords are configuration findings, not invitations to crack hashes.

At ABP, the shared engineer password on eng-WS-1 is replaced with named accounts, and each elevation is logged with the person and the reason. Contractors receive accounts that expire at the end of their work order. Lena reports shared passwords from the configuration and the account list, never by testing them.

### 12.3 Patch windows

OT patches land in maintenance windows, not on Patch Tuesday. Fit jobs by risk into the available hours; defer what does not fit rather than overrunning into production.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Expected output:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Synthetic case — Ashford Batch Plant.** The patch lab deferred the historian DB patch because W1 and W2 were full with higher-risk PLC and HMI work. Lena scheduled a dedicated window the next month instead of squeezing it into Sunday morning.

Each deferred job keeps its ticket and date. Deferrals are reviewed monthly.

### 12.4 Errors and limits

Do not disable antivirus or allow-listing to make the vendor happy without a written exception and compensating monitoring. Offline plants still need media control.

When the HMI vendor asks for an exception, Lena records which protection is relaxed, on which host, for how long, and what monitoring replaces it. The exception has an owner and an expiry date. Offline hosts still receive media through a scanning station and a logged transfer, since USB sticks are the usual route into an isolated network.

### Practice note

Every deferred patch gets a ticket with residual risk and a date. Deferred-without-date is how decade-old HMI OS images survive. Review the deferred list in the same meeting that plans the next window.

### 12.1b Image and offline analysis

Full-disk images of HMIs are high impact: they take systems offline, may contain proprietary recipes and tempt out-of-scope browsing. Prefer live, least-privilege reads and configuration exports. If an image is truly required, the work permit must name chain-of-custody, encryption at rest, who may mount it, and a destroy-by date — and the course labs still do not practice imaging real hosts. Offline plants still need media control; air gaps that hide USB and cellular modems are not air gaps.

Lena has never needed a full image at ABP.

### Exercises

- **EX034 — Account.** Specify a least-privilege pattern for PLC engineering access. Rubric: 3 = named, time-boxed, logged, dual control for logic download; 2 = three of four; 1 = shared admin; 0 = none.
- **EX035 — Lab.** Which job was deferred and why? Rubric: 3 = historian DB patch; windows full after higher-risk jobs; 2 = name only; 1 = vague; 0 = wrong.
- **EX036 — Exception.** Write a one-line USB exception for a vendor bring-up with compensating control. Rubric: 3 = time-boxed, scanned media, monitored host; 2 = partial; 1 = open USB; 0 = none.

### Synthesis

Harden and patch workstations as if they were controllers — because for malware, they are the door.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) protect historian and recipe data without blocking operations; (2) scope database assessment without extracting proprietary batches; (3) design synthetic datasets for labs.

### 13.1 Historians are crown jewels

Historians hold process values that reveal production rates, recipes and sometimes quality data. Unauthorized writes can corrupt batch records; unauthorized reads can leak commercial data. Zone them (L3), allow read paths through controlled replicas, and never expose SQL to L4.

At ABP, HIST-1 sits in L3 and office users read from the DMZ replica, never from the control-zone historian. Write access to HIST-1 is limited to the collection service, and every change to batch records is logged. Lena checks both paths during each conduit review.

### 13.2 Minimize extracts

Authorized database work uses synthetic or masked copies. Exporting real batch genealogy into a student laptop is a confidentiality incident. The work permit must state: no full dumps, column allow-lists, row limits, destroy-by date.

Lena's work permit for historian access lists the allowed columns and the row limit in plain words. Extracts go to an approved analysis host, not a personal laptop, and their deletion is recorded. A request for more data than the question needs is narrowed before any query runs.

### 13.3 Synthetic process data

Generate deterministic tank levels and setpoints with fixed seeds so labs reproduce. The CUSUM and PI labs do this; never copy a production historian into the course repository.

> **Synthetic case — Ashford Batch Plant.** Ops provided Lena with a week of synthetic T-1/T-2/R-101 values at 1 Hz for detector trials — no customer order numbers, no operator names.

ABP's week of synthetic T-1, T-2 and R-101 values at one-hertz resolution was generated this way, and its seed is recorded with the dataset. Lena reruns the generator to confirm the file matches before each trial.

### 13.4 Errors and limits

Masking that leaves unique rare recipes can still identify production runs. Prefer synthetic generation for teaching.

A recipe that ABP runs only twice a year can identify the batch even with names removed. Lena therefore uses synthetic data for teaching and keeps masked real data only for investigations that truly need it, with access limited to the investigators. Masking choices are recorded and reviewed with the quality team. Rare-batch cases are listed in the extract request. The quality team reviews those cases before release.

### Practice note

Draw the data-flow: sensor to PLC to historian to replica to L4 reports. Every arrow needs an owner and a protocol. Mystery arrows are where exfiltration and accidental exposure live.

### 13.1b Row-level and column-level controls

Modern historians and warehouses offer row and column policies. Assessment questions become: does role R see column C? Does row filter F apply? Test with the role itself. Document the policy engine version; we ran SELECT * against an admin role proves little about analyst exposure. Record each role-and-column result with the account used and the date, so the next review repeats exactly the same checks.

Lena tests ABP's replica with an analyst account before each review. Results go in the review notes.

### 13.5 Worked example — a minimised historian extract (synthetic ABP)

Quality engineers request "all R-101 data for last year". Lena's extract contains only the four tags the deviation investigation needs (reactor temperature, jacket temperature, agitator speed, feed valve position) at one-minute resolution, for the 11 batches under review, with batch IDs replaced by study codes and the operator-name column dropped. The extract is a read from the DMZ replica, never from the control-zone historian, and the query text and a SHA-256 hash of the output file go into the request ticket so the same rows can be reproduced or deleted later. The result is 11 × 4 tags × about 480 minutes ≈ 21,000 rows instead of tens of millions.

### Exercises

- **EX037 — Permit clause.** Write a data-handling clause for a historian assessment. Rubric: 3 = replica only, column allow-list, row limit, destroy-by, no dumps; 2 = three; 1 = one; 0 = none.
- **EX038 — Authz.** How do you test whether role analyst can write annotations in the historian without injection techniques? Rubric: 3 = connect as analyst, attempt write, record grant/deny; 2 = idea; 1 = injection; 0 = none.
- **EX039 — Synthetic.** Three fields safe for a synthetic tank table and two that must not appear. Rubric: 3 = e.g. tag, value, timestamp vs operator_name, customer_order; 2 = partial; 1 = weak; 0 = none.

### Synthesis

Minimize data, test roles, synthesize for teaching. The historian is not a trophy store.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) put OT security tools under version control with review; (2) gate conduit-widening changes; (3) keep CI on synthetic fixtures only.

### 14.1 Tools are products

Allow-list compilers, reachability checkers and detector configs are software. They need repositories, reviews, tags and changelogs. A work permit that cites the firewall export without a hash is incomplete.

Lena keeps CNHP's tools in a single repository with tagged releases and a changelog, and every work permit cites the tag and the hash of the exports it relies on. When a reviewer asks which version of the reachability checker produced a result, the answer is a tag, not a memory.

### 14.2 Gate widening

Merges that add a conduit, open a function code or remove a deny require a second reviewer and a linked authorization ticket. Tightening changes can be lighter. Encode this in CODEOWNERS on the policy paths.

Lena assigns code owners from control engineering to the allow-list and conduit files, so widening changes cannot merge without them. Tightening changes still need one reviewer. The rule is enforced by code-owner settings on the policy paths, so it cannot be skipped by a busy reviewer. A widening change also needs a linked authorization ticket naming who approved the new path and why.

### 14.3 CI fixtures

CI runs labs and unit tests on synthetic data. Never point CI at a plant VPN. Seed data lives in the repo; plant credentials live in a vault and never in CI logs.

> **Synthetic case — Ashford Batch Plant.** A PR added a temporary L4 to L2 rule for a vendor visit. CI's reachability check failed because L1-SIS became reachable; the PR was blocked until the rule was rewritten through the DMZ.

Lena's pipeline loads synthetic fixtures for ABP's zones and allow-list.

### 14.4 Errors and limits

Tags can drift from what operators run; record the running hash in the engagement log at window start.

Lena's engagement log records the hash of the monitor binary and allow-list actually running at the start of each window. If it differs from the tagged release, the window waits until the difference is explained. That check found one bench monitor still running a release candidate after a hotfix. Running hashes go in the window's record. A mismatch is treated as a stop, not a warning.

### Practice note

Policy repos use the same dual-approval culture as PLC logic downloads. If downloading ladder to PLC-A needs two people, publishing a conduit that reaches PLC-A should too.

### 14.1b Release trains vs hotfixes

Normal improvements ride a release train with Lab I/II. Safety hotfixes may skip features but not verification: a minimal fail-closed regression pack is mandatory. Tag hotfixes clearly so a window can pin either the train build or the hotfix SHA with eyes open. Version pins appear in the kickoff checklist beside the work-permit hash; if the pin and the running binary disagree, the window does not start.

ABP's hotfixes carry their own tag and the regression pack result in the release note, so a window lead can see exactly what was verified.

### 14.5 Worked example — reviewing a change to permit() (synthetic ABP)

A pull request widens the HMI's writable range on PLC-A from 40001–40010 to 40001–40012 for a new agitator setpoint. Lena's review checklist: the requirement ID that justifies 40011–40012; new conformance vectors for 40012 (pass) and 40013 (block); unchanged default-deny for unknown sources; a version bump and changelog line; and a second reviewer from control engineering who confirms the registers' meaning in the PLC project. The merge waits for the bench run of the vectors against the actual firewall build. Software engineering discipline here is not ceremony: a one-character range error would let the HMI write a register the process design never intended.

### Exercises

- **EX040 — Pin.** Write the method sentence that pins the allow-list for a window. Rubric: 3 = name, hash/tag, date loaded; 2 = name+tag; 1 = name; 0 = none.
- **EX041 — Gate.** One-sentence merge policy for conduit files. Rubric: 3 = second reviewer + AUTH for widen; 2 = reviewer only; 1 = vague; 0 = none.
- **EX042 — CI.** Why must CI never use plant VPN credentials? Rubric: 3 = unauthorized automation, secret leakage, non-determinism; 2 = one solid reason; 1 = vague; 0 = wrong.

### Synthesis

Treat OT security software like production software: versions, review gates, synthetic CI.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) map CIA and safety to OT assessment questions; (2) distinguish vulnerability, exposure and process risk; (3) refuse empty security scores.

### 15.1 CIA plus safety

Confidentiality: who can read recipes or trends? Integrity: who can change setpoints or logic? Availability: what stops the batch? Safety: which protective layers remain independent? Every finding should say which properties are affected and whether a safety function is in scope.

Lena adds a line to every CNHP finding naming the affected properties and whether SIS-B is in scope. At ABP, a finding about an unauthenticated write to PLC-A affects integrity and, through the tank level, possibly safety; a finding about the historian replica affects confidentiality. Naming the property tells readers which team must respond.

### 15.2 Vulnerability, exposure, risk

An unauthenticated Modbus write is a vulnerability. On a PLC reachable from L2 it is an exposure. Process risk adds likelihood and consequence for the plant — which needs the safety engineer's model, not a universal CVSS-only story. Tickets store consequence bounds and protective layers separately; risk acceptance stays with the plant owner.

Lena's ticket template has separate fields for each so that none is lost. Lena records the exposure, such as reachability from L2, separately from the vulnerability, so that fixing either one can be tracked. The plant manager signs any acceptance of residual risk.

### 15.3 Empty scores

A single OT risk = 42 hides whether SIS independence holds. Prefer concrete measures: open high-consequence findings, conduits into SIS, detector false-alarm rate at the plant's base rate, patch deferral age. If you show a score, show the model and inputs.

> **Synthetic case — Ashford Batch Plant.** Lena stopped putting a composite score on CNHP slides. The deck now shows: SIS reachable from L4? No. Critical opens: 1. Alarms per operator-hour: 1.05. Deferred high-risk patches: 0.

Each CNHP measure has a definition and a source, so it can be recomputed.

### 15.4 Errors and limits

Fundamentals are vocabulary; they are not a complete hazard analysis. Continue into threat and failure analysis for structured study.

The vocabulary helps people describe findings consistently, but it does not replace the plant's process hazard analysis. Lena links CNHP findings to the hazard analysis where they touch a hazard, and leaves consequence judgments to the process-safety engineer. Threat and failure analysis later in the programme gives the structured method. Each finding links to the relevant hazard. The safety engineer reviews those links.

### Practice note

When someone asks for a traffic-light dashboard, offer three lights that mean something: SIS independence intact (yes/no), critical findings open (count), patch deferrals past date (count). Refuse a fourth light called overall cyber.

### 15.1b From property to test

If a finding claims integrity impact, the validation plan must include an integrity check (who can still write). If it claims availability impact, validation includes a canary or synthetic probe — not a new attack. Align property, finding and re-test method in one paragraph of the ticket. The re-test result goes into the same ticket as the original finding, with the date and the check used, so closure can be audited later.

At ABP, the FW-12 finding claimed an integrity exposure, so its re-test checked that the office zone could no longer reach SCADA, using the same reachability method.

### Exercises

- **EX043 — Map.** Map unauthenticated setpoint write on PLC-A to C/I/A/safety with one sentence each. Rubric: 3 = all four scoped; 2 = three; 1 = one; 0 = none.
- **EX044 — Terms.** Distinguish vulnerability, exposure and process risk for that write. Rubric: 3 = clear split; 2 = two clear; 1 = muddled; 0 = none.
- **EX045 — Score refusal.** Stakeholder wants a 0-100 hackability score. Refuse with alternatives. Rubric: 3 = refuses + concrete measures; 2 = refuses only; 1 = vague; 0 = invents score.

### Synthesis

Name the property, separate exposure from process risk, prefer measures you can recompute.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) write testable OT security requirements; (2) trace a requirement to a conduit rule and a lab; (3) manage interfaces between PLC, SIS, historian and security monitors.

### 16.1 Testable requirements

"The plant should be secure" is not a requirement. "No host outside L1/L2 shall initiate writes to PLC-A holding registers; verified by reachability analysis and allow-list tests on synthetic fixtures" is. Each requirement needs an id, a shall-statement, a verification method and an owner.

Lena assigns each CNHP requirement an id such as R-12 and an owner before any design work starts. A requirement without a verification method is returned to its author. Lena also checks that each one can be tested on synthetic fixtures, because a requirement that can only be verified by writing to a live controller cannot be accepted.

### 16.2 Traceability

Matrix: requirement to design element to test case to plant evidence. When a finding shows a conduit into SIS, you know which requirement and test failed. Without the matrix, post-mortems become blame.

Lena keeps the matrix as a file in the CNHP repository, updated in the same pull request as the policy it describes. Each row links a requirement such as R-12 to the zoned edge list, the reachability test and the latest firewall-export hash. When a test fails, the matrix shows which requirement is at risk and who owns it.

### 16.3 Interfaces

PLC-A publishes process values; SIS-B consumes dedicated sensors; the historian consumes PLC tags; the serial monitor consumes a listen-only tap. Agree tag lists and update rates. An interface change is a change request, not a quiet edit during a batch.

> **Synthetic case — Ashford Batch Plant.** Requirement R-12 "SIS not reachable from L4" traces to the zoned edge list, lab_reach.py, and the quarterly firewall-export hash in the dossier.

Lena keeps the tag list for each interface in the repository, with its owner and update rate.

### 16.4 Errors and limits

Traceability matrices rot if not updated in the same PR as the policy. Keep them next to the code.

Lena's continuous integration fails a pull request that changes a policy file without touching the matrix, which keeps the two in step. Each row also carries the date it was last verified. Rows that have not been checked for a quarter are flagged in the review meeting, because an old link is often a broken one. Owners confirm each row yearly.

### Practice note

Put requirement ids in firewall-object names and in detector config comments (req=R-12). Searchability during an incident beats a slide that once mapped requirements to modules.

### 16.1b Glossary and retirement

Maintain a one-page glossary: work permit, ConduitSet, allow-list, planned technique, sealed evidence. Stakeholders misuse coverage and risk constantly; the glossary is a requirements artefact. Traceability also covers retirement: when a requirement is withdrawn, mark it superseded with a pointer rather than deleting the row. Historical findings still cite old ids.



Internal SLAs between services matter: the monitor may need the finding store to accept an event within N seconds during a stop condition. Write that as a requirement with a synthetic load test. Without it, stop-condition pages arrive after the human already called process safety.

### Exercises

- **EX046 — Shall.** Rewrite "stop office from touching SCADA" as two shall-requirements. Rubric: 3 = two testable shalls with verify method; 2 = one good; 1 = still vague; 0 = none.
- **EX047 — Trace.** For R-12, name the artefact and the failing test signal. Rubric: 3 = zoned edges + L1-SIS in reach(L4); 2 = one; 1 = vague; 0 = none.
- **EX048 — Interface.** List three fields in a tag-list interface contract. Rubric: 3 = tag name, type/engineering units, update rate (or equiv.); 2 = two; 1 = one; 0 = none.

### Synthesis

Requirements you can test, links you can follow, interfaces you version.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) tune a simple PI loop and see integral action remove offset; (2) place security sensors in the control loop without destabilising it; (3) avoid alert storms that hide process alarms.

### 17.1 PI in one page

A proportional controller leaves steady-state offset; integral action accumulates error and removes it. The lab steps the level setpoint from 50 to 60 and shows kp-only versus kp+ki. Security engineers need this fluency so they do not propose detectors that fight the controller.

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

Lena uses the lab to explain to colleagues why a detector should watch the error, not the raw level. The lab output shows the offset disappearing once integral action is added, which helps colleagues see how a controller responds to a disturbance. A detector that alarms on the level itself would fire whenever a setpoint changes.

### 17.2 Sensors in the loop

Inline inspection adds latency. If the process time constant is minutes (tank level), tens of milliseconds are fine. If it is tens of milliseconds (fast pressure), prefer passive taps. Measure before deploying (Chapter 3).

On the bench, Lena compares each candidate device's added latency with the time constant of the loop it would sit in: on T-1's trunk the margin is minutes, on the compressor skid only tens of milliseconds, so one device can be acceptable on the first and unacceptable on the second. Measured latency on the bench decided both choices, not the vendor's stated figures. Lena records the measured values with the time constants of each loop, so the decision can be revisited if a process changes.

### 17.3 Alert storms

If every medium cyber alert pages the whole site, people silence the pager — and then miss the process alarm that matters. Severity routing and rate limits on notifications are damping, exactly as in the alarm-rationalisation lab.

> **Synthetic case — Ashford Batch Plant.** After PI lab review, Lena rejected an inline DPI box on the compressor skid (fast loop) and approved a listen-only serial tap on the slow tank trunk.

Lena's routing at ABP pages the shift lead only for high-severity events.

### 17.4 Errors and limits

Textbook PI ignores valve stiction and sensor delay. Use plant historians for real tuning; the lab is for intuition.

Lena tells reviewers that the lab's tidy curves are not what the plant historian shows. Real loops at ABP have valve stiction and transmitter delay, which make the response slower and noisier. Any detector threshold proposed from lab results is checked against a week of historian data before it is used, and tuning of real controllers stays with control engineers. Lena logs any differences found.

### Practice note

Draw the loop: setpoint, error, controller, actuator, process, sensor, and mark where your security device sits. If you cannot mark it, you do not know whether you are measuring or actuating.

### 17.1b Set-points and human placement

Write the set-point next to the sensor (cycle time ≤ 50 ms). Review set-points when the plant changes recipes or when false pages exceed an agreed rate. Put humans where judgment about authorization is required; put automation where delay is dangerous. Approving a conduit widen is human. Denying an out-of-range write is automation.

At ABP, the cycle-time set-point for the serial monitor is 50 ms, and it is reviewed when recipes change. The rule of thumb is simple: automation for fast, well-defined decisions, people for judgments about authorization and risk.

### Exercises

- **EX049 — Lab.** Which (kp, ki) pair reaches nearest 60 with lowest mae? Rubric: 3 = (0.2, 0.01) with figures; 2 = pair only; 1 = wrong pair; 0 = none.
- **EX050 — Placement.** Inline vs tap for a 20 ms pressure loop — choose and justify. Rubric: 3 = tap/passive, latency risk; 2 = choice without why; 1 = inline casually; 0 = none.
- **EX051 — Damping.** One damping rule for cyber alerts in the control room. Rubric: 3 = specific (batch, severity, rate); 2 = vague; 1 = none useful; 0 = none.

### Synthesis

Understand the loop before inserting security; damp alerts so process alarms stay audible.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) apply Purdue/62443 zoning at ABP; (2) define trust boundaries for engineering access; (3) choose when a synthetic range is the right place to test.

### 18.1 Zones that match safety

L0/L1 hold process and basic control; L2 supervision; L3 site operations; L3.5 DMZ; L4/L5 enterprise. SIS sits with carefully controlled conduits. Architecture diagrams must match the reachability graph, not a marketing Purdue poster.

Lena checks the ABP diagram against the reachability results from the firewall export at each review. At ABP, SIS-B's engineering ports are reachable only through the keyswitch path during scheduled tests, and the office reaches SCADA data only through the DMZ historian replica. Where the diagram and the reachability results disagree, the results win and the diagram is corrected. Lena marks the diagram with the export hash it was checked against.

### 18.2 Engineering access

Engineering workstations and vendor laptops cross trust boundaries. Prefer: DMZ jump host, time-limited accounts, monitored sessions, no standing VPN from the internet to L2. USB and cellular modems are architecture too — inventory them.

At ABP, vendor sessions pass through a DMZ jump host with time-limited accounts and recorded sessions. Lena's inventory lists every engineering laptop allowed to connect, and any standing VPN found in a review is reported as a finding. USB use on engineering workstations is logged and reviewed monthly.

### 18.3 Synthetic ranges

When methods are noisy or the plant is fragile, use a synthetic or digital-twin range that mirrors configuration. Results then support claims about the mirrored config, not about live process behaviour. Say so in the report.

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

> **Synthetic case — Ashford Batch Plant.** CNHP's target architecture is the zoned graph: L4 views through L3.5; SIS engineering only via keyswitch; no L2 to L1-SIS conduit.

Lena's bench copy of ABP's firewall and monitor is such a range; its reports state that results apply to the mirrored configuration only.

### 18.4 Errors and limits

Diagrams age. Re-validate zones against the live firewall export at each window.

Lena compares the diagram with the live firewall export at the start of each window and records any difference as a finding. A diagram that has not been checked against the export is marked as unverified, so nobody relies on it by mistake during an incident. The six-month re-test later found exactly this kind of drift. The check takes minutes with the reachability script. Its result is filed with the window record.

### Practice note

Hang the zone diagram next to the privilege map from Chapter 8. When a vendor asks for a temporary rule, point at the wall and ask which edge they want to add — and which requirement it breaks.

### 18.1b Jump hosts and egress

Engineering jump hosts are high-value: harden them, log session start/stop, forbid personal file sync agents, and rebuild from golden images between windows when feasible. Assessment and engineering zones need egress allow-lists: only in-scope plant CIDRs and the evidence store. Open egress turns a compromised laptop into a pivot the work permit never authorized.



Network diagrams for the assessment zone go into the dossier with the same hash discipline as evidence files. When an auditor asks how traffic reached L2, you show the diagram version that was live, not a newer cleaned-up sketch.

### Exercises

- **EX052 — Zone sketch.** Place HMI, PLC-A, SIS-B, historian, office PC in zones and name two controls on the arrows. Rubric: 3 = clear zones + two controls; 2 = zones only; 1 = muddle; 0 = none.
- **EX053 — Boundary.** Why is "email a recipe CSV to my Gmail" a boundary violation? Rubric: 3 = data leaves controlled zones/authz; 2 = privacy handwave; 1 = vague; 0 = okays it.
- **EX054 — Twin claim.** Limitation sentence for synthetic-range-only tests. Rubric: 3 = claims config not live process; 2 = vague; 1 = overclaim; 0 = none.

### Synthesis

Zones, engineering-access boundaries and honest limits on what a twin can prove.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) assess OT identity without attacking crypto; (2) use hashing for evidence integrity; (3) handle engineering credentials safely.

### 19.1 Identity in the plant

Ask: which accounts exist on HMIs, historians and engineering hosts? Which use shared passwords? Which integrate with the site directory? MFA on L4 jump hosts is common; MFA on a legacy HMI may be impossible — document compensating controls (physical access, session recording).

Lena's identity review at ABP listed every account on HMI-1, the historian and eng-WS-1, with its owner and whether it was shared. The shared engineer password was the clearest finding and was replaced with named accounts. Where MFA could not be added to a legacy HMI, she recorded the compensating controls, such as locked control-room access and session recording on the jump host, and named who checks them.

### 19.2 Evidence hashing

Hash configuration exports and evidence files (SHA-256); store digests in the ticket. Re-hash later to detect tampering. Pair hashes with actor id and work-permit version.

Lena hashes every firewall export when it is collected and stores the digest in the ticket with the time, her account and the work-permit version. Later reviews re-hash the stored file and compare. A mismatch is investigated before the evidence is used, because a changed export could mean tampering, a careless edit or simply the wrong file. The manifest names the algorithm used.

### 19.3 Secrets

Engineering credentials live in a vault; short-lived checkouts; rotate at window end. No secrets in git, screenshots or chat. Service accounts for historians get unique passwords and monitored use.

> **Synthetic case — Ashford Batch Plant.** A shared "engineer" password on eng-WS-1 was replaced with named accounts after CNHP's identity review. Checkout of the PLC project files now logs the person, not a mythic shared user.

At ABP, engineering credentials for PLC-A's project are checked out from the vault for one window and rotated afterwards.

### 19.4 Errors and limits

Hashes detect change, not malice versus accident. Pair them with access logs. Do not attempt to crack plant password hashes in this course.

A matching hash proves only that a file has not changed since it was hashed, not that it was collected lawfully or interpreted correctly. Lena pairs hash checks with the access log for the evidence store, which shows who touched each file and when. Password findings are reported from configuration and account lists; cracking hashes is outside the programme and outside any permit she holds.

### Practice note

Break-glass accounts for plant emergencies need dual control to retrieve and automatic rotation after use. An unbroken break-glass password taped under a keyboard is not a control.

### 19.1b Certificates and break-glass

For TLS-facing historians and jump hosts, record presented certificates under authorization. Expired or mismatched certs are operations findings. Lena's certificate record lists, for each host, the subject, issuer, expiry date and date observed, so an expiring certificate on the historian replica becomes a dated ticket rather than a surprise outage. Prefer SHA-256 for evidence manifests; document the algorithm in the manifest.



Algorithm choices for manifests are a version field, not a silent swap mid-window. When the algorithm changes, existing manifests keep their original algorithm field and are re-hashed into a new manifest rather than edited.

### Exercises

- **EX055 — Questions.** Five identity questions for ABP's engineering hosts. Rubric: 3 = five concrete; 2 = three; 1 = one; 0 = none.
- **EX056 — Hash.** What do you do when a sealed firewall export's hash mismatches? Rubric: 3 = restore/re-export, investigate writes, process finding; 2 = file only; 1 = vague; 0 = ignore.
- **EX057 — Secret rule.** One-line policy for PLC project passwords in tickets. Rubric: 3 = never in ticket; vault reference; 2 = don't share; 1 = weak; 0 = allows paste.

### Synthesis

Read identity config; hash evidence; keep secrets in a vault.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: engineering context

### Learning outcomes

You will (1) place OT security engineering among SP 800-82, ISA/IEC 62443 and ATT&CK for ICS; (2) define what this degree programme builds; (3) state the safety boundary for all later chapters.

### 20.1 Discipline map

NIST SP 800-82 guides ICS security. ISA/IEC 62443 structures zones, conduits and security levels. ATT&CK for ICS names adversary techniques for planning and coverage — not as a residual-risk score. Modbus specs define the protocol you allow-list. Academic surveys (Giraldo et al.; Urbina et al.) warn against detectors evaluated only on easy attacks. Engineers build the platforms and processes that make those sources operable under process-safety constraints.

Lena uses each source for what it is good at and cites the exact revision.

### 20.2 What we build

CNHP at Ashford Batch Plant is the running example: zoning, allow-lists, detectors with honest metrics, patch windows, evidence dossiers. Graduates design, verify and operate such programmes — they do not invent exploits against PLCs.

The programme's outputs are concrete: a zoned network with tested reachability, allow-lists enforced on Modbus traffic, detectors with published false-alarm intervals, a patch schedule with dated deferrals and a dossier an auditor can verify. Each later chapter adds one part of that system and shows how Lena built and checked it at ABP without endangering a batch.

### 20.3 Safety boundary

No exploit payloads, no unauthorized plant access, no live personal or proprietary batch data in labs, labs on synthetic local data only. Dual-use requests are refused (Chapter 10). Process safety stop conditions always win. This boundary is a requirement on every design review in Chapters 21-50.

> **Synthetic case — Ashford Batch Plant.** Leadership asked for a red team that hacks the plant. Lena reframed the charter: an authorized hardening programme that enforces zones and measures detection without endangering batches.

Lena checks every design against this boundary.

### 20.4 Errors and limits

Frameworks evolve; re-check URLs and versions before citing in a thesis. This chapter orients; it does not replace reading the primary sources.

Lena's list of sources records the revision and access date for each standard and paper used in CNHP documents. Before citing a framework in her thesis, she checks whether a newer revision exists and notes any change that affects her argument. The chapter gives only enough orientation to start; reading the primary sources is part of the work.

### Practice note

Keep a one-page "sources we actually use" list in the CNHP binder with access dates. Examiners and auditors ask which revision of 62443 you meant; "the ISA one" is not an answer.

### 20.1b Neighbouring courses and deliverables

This engineering book assumes comfort with calculus, probability and software engineering from earlier chapters. The bachelor's OT book is broader; the technologist book emphasizes implementation drills. Operators need runbooks and tickets; engineers need schemas, tests and ADRs. Capstone grading looks for both. Each deliverable names its intended reader on its first page.

Lena's own deliverables at ABP include both kinds. Her runbooks and tickets serve the operators who run the plant each day, while the schemas, tests and decision records serve the engineers who will maintain the tools after her. Assessors look for both.

### Exercises

- **EX058 — Framework fit.** Pair each need with SP 800-82 / 62443 / ATT&CK ICS / Modbus spec. Rubric: 3 = four sensible pairs; 2 = three; 1 = two; 0 = none.
- **EX059 — Charter.** Rewrite "hack the plant" as an engineering charter sentence. Rubric: 3 = authorization + hardening/measurement + safety; 2 = partial; 1 = still attack-centric; 0 = none.
- **EX060 — Boundary.** Three concrete out-of-scope items for this programme. Rubric: 3 = three clear; 2 = two; 1 = one; 0 = none.

### Synthesis

Engineers enable authorized OT hardening; they do not replace process safety with cleverness.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: requirements

### Learning outcomes

You will (1) elicit requirements from process safety, operations and security; (2) separate functional, safety and measurement requirements; (3) write acceptance criteria a tester can run on synthetic fixtures.

### 21.1 Sources

Process safety wants independent protection layers. Operations wants viewing without downtime. Security wants deny-by-default conduits. Elicitation interviews produce shall-statements tagged by source. Conflicts (convenience viewing vs SIS isolation) are recorded, not papered over.

At ABP, Lena interviewed the process-safety engineer, the shift leads, the control engineers and the IT network team separately, then brought conflicts to a joint meeting. The clearest conflict was the remote-viewing rule FW-12, which operations valued and safety could not accept. It was recorded with both positions, and the resolution, viewing through the DMZ replica, became a requirement with an owner.

### 21.2 Three families

Functional: "The serial monitor shall decode Modbus RTU on trunk A and emit allow/deny decisions." Safety: "If the allow-list file does not load, the monitor shall fail closed (drop all non-essential traffic or alarm and require human action per the design)." Measurement: "CNHP shall report planned-vs-observed ATT&CK for ICS technique coverage with denominators." Safety requirements win ties.

Lena tags each CNHP requirement with its family, so reviews can check that safety ones are tested first. Ties are settled in writing.

### 21.3 Acceptance criteria

Each requirement has a Given/When/Then on synthetic data. Example: Given deny of L2 to L1-SIS, When reachability runs from L4, Then L1-SIS not in the reachable set. Criteria that need a live plant write are rejected at review.

> **Synthetic case — Ashford Batch Plant.** Safety requirement S-1 "fail closed on missing allow-list" failed its acceptance test when a typo path returned PASS. The fix shipped before any plant window.

Criteria are reviewed with the requirement's owner. Each criterion is a test.

### 21.4 Errors and limits

Stakeholders invent requirements mid-window; park them in a backlog with an AUTH ticket, do not hot-patch production monitors during a batch.

When someone asks for a new monitor rule during a batch, Lena records it in the backlog with an authorization ticket and evaluates it after the window. Changing a production monitor mid-batch risks an outage or a fail-open bug that nobody has tested. The backlog item names who asked, why and when it will be reviewed, so the request is not lost and the person who raised it sees it handled.

### Practice note

Acceptance tests are named after requirement ids and fail CI when skipped. Orphan Must requirements are either tested or formally deferred with an executive owner.

### 21.1b MoSCoW under safety

Must/Should/Could prioritization still places all safety requirements in Must. A Could that weakens Must (optional deny of write codes) is reclassified or rejected. Product managers do not outvote fail-closed. Log fields carry the requirement id as well (req=S-1), so a deny event can be traced to the requirement it enforces.

At ABP, S-1 and R-12 are both Must items, and no product decision can move them down. A request to make write-code denies optional for convenience was rejected on this basis, and the rejection is recorded with the requirement it would have weakened.

### Exercises

- **EX061 — Elicit.** Write one functional and one safety shall from "office must not reach SIS". Rubric: 3 = both testable; 2 = one; 1 = vague; 0 = none.
- **EX062 — Acceptance.** Given/When/Then for fail-closed on missing allow-list. Rubric: 3 = complete with expected deny/alarm; 2 = partial; 1 = idea; 0 = none.
- **EX063 — Conflict.** Convenience L4 to L2 viewing vs zoning — record conflict and chosen rule. Rubric: 3 = conflict named + safety-first rule via DMZ; 2 = rule only; 1 = picks convenience; 0 = none.

### Synthesis

Requirements come from people, split into families, and ship with acceptance tests on synthetic fixtures.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: system and data models

### Learning outcomes

You will (1) draw an entity model for assets, zones, conduits and findings; (2) choose keys and cardinality; (3) keep exploit content out of the model.

### 22.1 Entities

Plant 1—* Unit; Unit 1—* Asset; Zone 1—* Asset; Conduit *—* Zone (from/to); Finding *—* EvidenceObject (by hash); TechniqueTag *—* Finding. Cardinality mistakes (many active conduit sets without a version pointer) cause auditors to ask which rules were live.

Lena's model gives each ConduitSet a version and records which version was live at any time, so an auditor can see the rules that applied on a given day. Each Finding links to its evidence by hash, and technique tags link to findings only after review.

### 22.2 Keys

Finding ids are UUID. Evidence is content-addressed by SHA-256. ConduitSet has (plant_id, version_int). Never key findings by title — titles change.

Lena's schema uses these keys throughout CNHP. A finding about FW-12 kept its identifier when its title was reworded after review, and its history stayed intact. Evidence keyed by its hash cannot be silently replaced, since a different file would have a different key. The ConduitSet version number increases with every published change and never reuses an old value.

### 22.3 Forbidden attributes

No attribute for payload, shellcode or step-by-step attack. EvidenceObject stores bytes in a sealed bucket; the model stores only hash, media type and retention class.

> **Synthetic case — Ashford Batch Plant.** An early schema had notes as free text; people pasted engineering passwords. Lena replaced it with structured fields plus an evidence hash, and a linter rejects password-like strings in titles.

Lena's linter enforces the list. It runs on every record created or imported, including bulk imports from scanners, and rejects password-like strings in titles. Rejected records return an error explaining which field was refused.

### 22.4 Errors and limits

Models that force every ATT&CK for ICS technique as mandatory fields generate junk tags. Keep technique tags optional and reviewed.

At ABP, technique tags are added by an analyst after the finding is written, and a second person reviews them. A finding with no fitting technique is left untagged rather than forced into the nearest one. This keeps coverage figures honest, because a junk tag would count as observed coverage for a technique nobody really tested. Tags are reviewed when the ATT&CK for ICS version changes.

### Practice note

Soft-delete findings with actor and reason; hard purge only via retention jobs that emit audit events. Silent DELETE FROM findings is a repudiation gift.

### 22.1b Attachment limits and time

Evidence objects need size caps and media-type allow-lists. Unbounded uploads become availability attacks and tempt dumping of bulk proprietary data. Every mutable entity needs created_at, created_by, and for state changes updated_at/updated_by or an append-only event. Prefer UTC with explicit offsets in exports.



Exports state their time zone once in the file header as well as in each timestamp. API clients that issue DELETE in a loop during a buggy retry get credentials revoked after a threshold.


### 22.5 Worked example — modelling a finding without leaking the plant (synthetic ABP)

Lena's data model for CNHP findings has entities Asset, Zone, Conduit, Finding and Evidence. A Finding references an Asset by key, never embeds its IP address or credentials, and stores evidence as a hash plus a pointer to the controlled evidence store. The forbidden-attribute list (passwords, full packet payloads, recipe values) is enforced by a schema check that rejects any record containing those fields. When a finding about PLC-A's open Modbus port is exported for management, it reads "Asset PLC-A, Conduit L2→L1, ATT&CK for ICS T0869 Standard Application Layer Protocol, severity high" — enough to act on, not enough to attack with.

### Exercises

- **EX064 — Cardinality.** Why is ConduitSet versioned instead of edited in place? Rubric: 3 = audit of what was authorized when; 2 = vague versioning; 1 = best practice; 0 = none.
- **EX065 — Key.** Why content-address evidence? Rubric: 3 = integrity + dedup + tamper evidence; 2 = one reason; 1 = vague; 0 = none.
- **EX066 — Forbidden.** Validation that stops passwords in title. Rubric: 3 = heuristic/linter + process; 2 = one; 1 = vague; 0 = none.

### Synthesis

Model assets, zones, versions, findings and hashes — not attacks.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: threat and failure analysis

### Learning outcomes

You will (1) enumerate failures of the OT security programme itself; (2) use a lightweight STRIDE-on-tools pass; (3) feed results into requirements without building exploit modules.

### 23.1 The programme can fail dangerously

Allow-lists failing open, reachability CI skipped, detectors with silent false-alarm storms, patch deferrals without dates — these threaten process safety and honesty, not only confidentiality of a tool.

Lena lists these failures first in CNHP's threat analysis because they could harm the plant through the tools meant to protect it. A monitor that fails open would let unauthorized writes reach PLC-A while everyone believed they were blocked. A reachability check skipped in continuous integration would let a new conduit to SIS-B merge unseen. Each failure gets a requirement and a test.

### 23.2 STRIDE on CNHP tools

Spoofing: fake engineering account. Tampering: edit firewall export after seal. Repudiation: no actor on deny events. Information disclosure: historian replica world-readable. Denial of service: scanner floods a trunk. Elevation: one person can publish a conduit to SIS. Each row gets a mitigation requirement.

Lena runs the analysis on each CNHP tool and records rows in the backlog with owners. For ABP, the most serious rows were the monitor failing open and one person publishing a conduit to SIS-B; they became requirement S-1 and the dual-approval gate on conduit changes. Each row is reviewed again when its mitigation ships.

### 23.3 Plant threats stay in hazard analysis

Threats to the process belong in the plant's process hazard analysis and cyber-informed HAZOP, not as features of a student tool. Do not build automated exploitation to satisfy a STRIDE row.

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

> **Synthetic case — Ashford Batch Plant.** STRIDE row fail open became safety requirement S-1. Row solo conduit publish became the dual-approval gate.

Lena passes plant threats to the process-safety engineer for the hazard analysis. She supplies facts about the tools and network, such as which zones can reach PLC-A, and the engineer judges the process consequences. Nothing in CNHP's tools simulates an attack on the process.

### 23.4 Errors and limits

STRIDE is a prompt, not a proof. Revisit when adding a new trust boundary (for example a vendor SaaS historian).

Lena repeats the analysis whenever CNHP adds a trust boundary, such as a new remote-access path for a vendor or a change to where alerts are sent. The rows from earlier reviews are kept, so the team can see which threats were added, which mitigations were built and which remain open. A STRIDE table never proves a tool safe; tests and reviews do that.

### Practice note

Include jumphost compromised in the model: short-lived credentials, egress allow-lists, rapid revocation. If the response is only trust the jumphost, the analysis is incomplete.

### 23.1b Abuse vs misuse and backlog

Abuse cases are intentional adversary actions against CNHP tools. Misuse cases are honest operators making dangerous mistakes (paste a CIDR that includes a partner). Design controls for both. STRIDE rows become issues with links to requirements. Misuse rows usually become validation rules; abuse rows usually become access controls.



Feeding the backlog means each STRIDE row has an owner and a due date. At ABP, the misuse case of an engineer pasting a partner's CIDR into the conduit file became a validation rule that rejects ranges outside the plant's address plan.

Both kinds feed the backlog.

### Exercises

- **EX067 — Fail open.** One test that proves fail-closed. Rubric: 3 = remove policy, expect deny+alert; 2 = idea; 1 = vague; 0 = none.
- **EX068 — STRIDE.** Mitigation for repudiation on deny events. Rubric: 3 = authenticated actor + immutable log; 2 = logging only; 1 = vague; 0 = none.
- **EX069 — Boundary.** Why doesn't programme STRIDE justify an exploit module? Rubric: 3 = different goal/safety boundary; 2 = partial; 1 = justifies it; 0 = none.

### Synthesis

Analyse how your programme can hurt the plant or lie; mitigate those first.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — OT, IoT and cyber-physical security: methods I

### Learning outcomes

You will (1) sequence work-permit to discovery to validation to reporting; (2) pick methods that match authorization and process risk; (3) define done for a method without writing to a PLC.

### 24.1 Sequence

Work permit first. Discovery enumerates assets and conduits by agreed methods. Validation confirms configuration issues with least privilege. Reporting delivers findings and evidence hashes. Skipping the permit is how unauthorized testing happens.

At ABP, every CNHP activity starts with a signed work permit naming units, methods, windows and stop conditions. Discovery uses passive capture and engineering project exports; validation uses configuration review and bench tests. Findings are reported with evidence hashes, and nothing moves to the next step until the previous one has produced its artefacts.

### 24.2 Method cards

Each card: name, purpose, privilege, noisy?, process impact, stop conditions, artefacts. Authenticated configuration review is a card; weaponised PLC exploit is not in this programme's deck.

Lena keeps ABP's method cards in the repository beside the work-permit template. A permit can only list methods that have a card, and each card states whether the method is noisy and what process impact it could have. Reviewers check the card's stop conditions against the permit, so a method cannot be used under weaker conditions than its card requires.

### 24.3 Done means artefacts

A method is done when inventory CSV, config hashes, finding drafts and coverage updates exist — not when someone feels finished.

> **Synthetic case — Ashford Batch Plant.** Method card for serial allow-list verification requires listen-only mode, cycle-time stop at 50 ms, and a lab-style decision table as artefact.

Lena's checklist for each method lists its required artefacts. For serial allow-list verification at ABP, that means the decision table, the capture hash, any draft findings and the updated coverage board. A method with missing artefacts is reopened, not closed with a note promising them later. Lena checks the list at the end of each window.

### 24.4 Errors and limits

Copying someone else's method list without matching authorization is cargo-cult 62443.

A method list copied from another plant or a published guide may assume authorizations, equipment or process tolerances that ABP does not have. Lena adapts each method to ABP's own permit, writes a card for it and has the card reviewed by control engineering before it is used. A borrowed method without that review is treated as unauthorized, however reputable its source, and stays out of the permit until reviewed.

### Practice note

Freeze methods during a window the same way you freeze conduits: new methods need the AUTH path, not while we were here we also tried.

### 24.1b Quiet vs noisy and dependencies

Quiet methods (listen-only decode, config export) fit more windows. Noisy methods need tighter rate limits and often off-peak hours. Encode method dependencies in the plan so reviews are not scheduled against an empty asset list. Lena's plan lists, for each method, the earlier methods whose artefacts it needs.



Method cards without a noisy field are how morning batch windows get congested. Noisy methods are booked against the batch schedule a week ahead, so the shift lead knows when to expect extra traffic.

Lena schedules quiet methods first.

### Field note — method freeze in practice

During ABP window W-17 a vendor asked to try an extra diagnostic function mid-shift. Lena parked the request in the next engagement's planning backlog and kept the method card frozen. The batch finished without unexplained traffic, and the diagnostic was evaluated the following month under a fresh work permit with its own stop conditions.

### Exercises

- **EX070 — Card.** Write a method card for listen-only Modbus decode. Rubric: 3 = all fields filled safely; 2 = missing one; 1 = includes writes/exploits; 0 = none.
- **EX071 — Sequence.** What is wrong with discovery before a signed work permit? Rubric: 3 = unauthorized testing; 2 = process vague; 1 = bad order; 0 = none.
- **EX072 — Done.** List four artefacts that close a zoning review method. Rubric: 3 = four concrete; 2 = two; 1 = one; 0 = none.

### Synthesis

Methods are authorized, carded and done when artefacts exist.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) sketch the allow/deny pipeline for ABP's serial monitor; (2) justify trade-offs in a short design review; (3) produce a one-page decision record.

### 25.1 Studio problem

Design: input frame to decode to load ConduitSet/allow-list to evaluate permit to emit event to forward or drop. Options: embed policy in code vs signed data file; sync vs async alerts on denies.

Lena's studio team at ABP sketches the whole path on one page and labels where a frame is denied if the policy is missing. The two choices debated were whether the allow-list lives in code or in a signed data file, and whether alerts about denies are sent synchronously or queued. Each option is written down with its consequences before anyone argues for one.

### 25.2 Trade-offs

Policy-as-signed-data lets updates ship without redeploying firmware but needs signature verification and fail-closed on bad signatures. Async alerts scale but can reorder; for SIS-path denies, prefer sync alert.

Lena's team agrees that a bad signature must stop all non-essential traffic, exactly as requirement S-1 demands for a missing policy. Sync alerts are kept for denies on write codes and SIS-related paths, where delay matters; routine read denies are queued. The team also records what happens if the signing key is lost: the monitor keeps the last valid list and alarms, and no unsigned update is accepted.

### 25.3 Decision record

One page: context, options, decision, consequences, date, owners. Store next to the code.

> **Synthetic case — Ashford Batch Plant.** Studio chose signed JSON allow-lists, sync path for denies that touch write codes, async bulk for routine reads. ADR-004 captures it.

ADR-004 records the studio's decision on signed JSON allow-lists in this format, with Lena and the control-engineering lead as owners. It sits in the repository next to the policy code, so anyone changing the loader can read why it works the way it does.

### 25.4 Errors and limits

Studios that skip safety requirements produce pretty diagrams that fail open.

Lena's studio refuses to review a design until it shows where the monitor denies traffic when the allow-list is missing or its signature fails. Designs that cannot answer are sent back before any discussion of layout or tools. The constraint cards make the safety requirements visible on the table from the first minute, so they cannot be forgotten in enthusiasm for a clever architecture. Rejected designs are recorded too.

### Practice note

Facilitators pause the room with: Where do we DENY if policy is missing? If nobody can answer, architecture is not ready.

### 25.1b Constraint cards and gallery

Hand each studio team constraint cards: residency, two-engineer ops, fail-closed, no empty scores, SIS independence. Designs that violate a card are rejected before aesthetic debate. Studios end with a gallery: teams post ADR drafts and others try to find a fail-open path in five minutes.



A studio sketch must name trust boundaries, data stores and the fail-closed path in writing. Ten minutes of labelling beats an hour of aesthetic layout. Fail-open paths found in the gallery are written into the ADR before it is accepted.

### Field note — labelling before layout

Studio teams that spent the first twenty minutes naming DENY points and trust boundaries produced ADRs that survived review. Teams that started with colour palettes rediscovered fail-open paths during gallery. CNHP now requires a labelled fail-closed path on the whiteboard photograph attached to every ADR.

### Exercises

- **EX073 — Options.** Two options for policy delivery and one risk each. Rubric: 3 = two + risks; 2 = options; 1 = one; 0 = none.
- **EX074 — ADR.** Decision line for sync deny alerts on write codes. Rubric: 3 = clear decision + why; 2 = decision only; 1 = vague; 0 = none.
- **EX075 — Review.** Three questions a reviewer must ask. Rubric: 3 = fail-closed, authn of policy, latency budget; 2 = two; 1 = one; 0 = none.

### Synthesis

Studio work ends in a recorded decision, not a vibe.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: architecture alternatives

### Learning outcomes

You will (1) compare on-prem monitors vs cloud analytics for OT data; (2) evaluate against residency and process-safety constraints; (3) pick an alternative with explicit rejection of the others.

### 26.1 Alternatives

A: on-prem serial/IP monitors with local detectors. B: on-prem collection with site historian analytics. C: cloud analytics SaaS receiving process values. Each serves different constraints.

Lena describes each option for ABP in the same structure: where process data goes, who operates it, how it fails and what it costs. Option C would send process values off site, which immediately raises data-residency and recipe-confidentiality questions. Options A and B keep data on site but differ in how quickly they can enforce decisions on the write path.

### 26.2 Criteria

Process safety independence, data residency, fail-closed behaviour, operability by the site team, cost. Weight safety and residency above novelty.

Lena agrees the weights with the process-safety engineer and the plant manager before scoring. Safety independence and data residency carry the most weight because a failure there cannot be undone by later fixes. Each option is scored with evidence, and options that fail a safety criterion are rejected regardless of their other scores. The weights are published in the analysis so reviewers can challenge them.

### 26.3 Decision

ABP rejected C because recipe-adjacent trends must not leave the site without a board-level exception. Chose A for write-path enforcement with B for longer-term detection research on replicas.

> **Synthetic case — Ashford Batch Plant.** A vendor demo of C looked slick; counsel and process safety blocked unrestricted upload. ADR-011 records the rejection.

ADR-011 records this decision. The reasons are short: option A enforces decisions locally on the write path and can be run by site engineers; option B adds detection research but needs skills the night shift lacks, so it is kept for daytime work on replicas. Option C remains rejected until residency rules change, which is its recorded revisit trigger.

### 26.4 Errors and limits

Alternatives analysis that ignores the work permit's data clauses is theatre.

At ABP, the permit's data clauses forbid process values leaving the site without a board-level exception, so option C failed before any technical comparison. Lena records that constraint at the top of the analysis, so readers see why C was rejected without reading the scoring. An analysis that had scored C highly while ignoring the permit would have wasted the board's time and might have pressured someone into granting an exception.

### Practice note

Document the skills each alternative demands. A cloud pipeline nobody on site can operate fails open socially even if it fails closed technically.

### 26.1b Cost, skills and revisit triggers

Include rough annual cost and the skills each alternative demands. An option that needs six FTEs to operate fail-closed is not free. End alternatives analysis with a decision, rejected options with reasons, and a revisit trigger (reopen if residency law changes).



Switching costs matter: a monolith that already exports signed allow-lists can grow into services; a SaaS contract with residency exceptions is harder to unwind mid-incident. Prefer options that keep an offline escape hatch for deny/allow.

ADR-011 states its revisit trigger.

### Field note — skill assumptions

Option B's analytics path assumed a site engineer who understood event ordering. ABP did not have that person on nights. Until hiring caught up, Lena kept write-path enforcement on option A and limited B to daytime research on replicas. Architecture that assumes unavailable skills fails open socially.

### Exercises

- **EX076 — Criterion.** Add one criterion for SIS data and score A/B/C. Rubric: 3 = sensible criterion + scores; 2 = criterion; 1 = vague; 0 = none.
- **EX077 — Reject C.** Rejection sentence with residency/safety reason. Rubric: 3 = clear; 2 = partial; 1 = cost only; 0 = accepts C.
- **EX078 — Fallback.** When is pure local A the right runtime? Rubric: 3 = WAN outage / isolation drill; 2 = vague; 1 = always; 0 = never.

### Synthesis

Choose architecture against weighted constraints; record rejected options.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — OT, IoT and cyber-physical security: control design

### Learning outcomes

You will (1) design preventive, detective and corrective controls for CNHP; (2) bind controls to requirements; (3) avoid controls that require exploit skills to operate.

### 27.1 Three kinds

Preventive: allow-list before forward. Detective: alert on denied write codes. Corrective: auto-disable a compromised engineering account at window end. Each maps to a requirement id.

At ABP, the allow-list on the serial monitor is preventive, the alert when HMI-1 tries to write outside 40001 to 40010 is detective, and disabling temporary engineering accounts at the end of each window is corrective. Lena records the requirement id beside each control, so a reviewer can see which requirement fails if the control is removed or weakened.

### 27.2 Operator skill

Controls must be operable by engineers who follow runbooks — not only by exploit specialists. A control that needs custom shellcode to verify is the wrong control for this programme.

Lena writes a runbook entry for each CNHP control describing how to check it with ordinary tools, such as replaying a synthetic frame on the bench and reading the decision log. If a control can only be verified by someone writing exploit code, she replaces it with one that can be checked safely by the site's own engineers during routine work.

### 27.3 Compensation

If a legacy PLC cannot enforce allow-lists, add detective monitoring and tighter human approval for engineering access. Document the compensation in the work permit.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Expected output:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

> **Synthetic case — Ashford Batch Plant.** Writes outside 40001-40010 are denied — preventive gate with a detective event when someone tries.

At ABP, compensation is written into the work permit with an owner and a review date, so it is checked rather than assumed. For a legacy PLC that cannot enforce an allow-list, Lena pairs detective monitoring on its trunk with two-person approval for engineering access.

### 27.4 Errors and limits

Stacks of compensating controls without an owner become ignored alerts.

Lena's control register lists every compensating control at ABP with its owner, its alerts and the date it was last tested. A control found without an owner gets one before the next window, or it is removed from the register and its requirement is marked unmet. Controls that nobody watches are counted as missing, because their alerts will be ignored when they finally fire. Ownership is reviewed at each health day.

### Practice note

Schedule a quarterly control-health day: break each preventive control in a synthetic lab and confirm detective controls fire. Untested controls are wishes.

### 27.1b Ownership and break-glass detection

Every control has an owner who receives its alerts and a review date. Log when an operator uses break-glass to skip dual approval. Break-glass without detection is just a hidden single control. Weekly review of break-glass events is part of the control design, and each review names who used break-glass and the reason given.



Each control's register entry also states how it fails: whether a broken allow-list blocks traffic or passes it decides which detective alert must fire first and who is paged when it does.

### Field note — control health day

On the March health day the team deleted the allow-list on a bench monitor and confirmed the detective alert fired in 12 seconds. The preventive path denied writes immediately. One compensating control for a legacy PLC had no owner; it received one before the next window.

### Exercises

- **EX079 — Map.** One preventive and one detective control for evidence tampering. Rubric: 3 = both; 2 = one; 1 = vague; 0 = none.
- **EX080 — Operable.** Why is verify by exploiting again a bad control? Rubric: 3 = dual-use + unstable + wrong skill; 2 = one reason; 1 = vague; 0 = defends it.
- **EX081 — Lab.** Which rule blocks HIST-1 fc=16? Rubric: 3 = fc-not-allowed; 2 = vague deny; 1 = wrong; 0 = none.

### Synthesis

Controls are preventive/detective/corrective, owned, and operable without exploits.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — OT, IoT and cyber-physical security: implementation I

### Learning outcomes

You will (1) implement permit() with explicit reason codes; (2) add tests for each clause; (3) log without storing secrets.

### 28.1 Implementation shape

Pure function: inputs source, function code, register, AllowListVersion to (allow: bool, reason: str). No network I/O inside the predicate. That keeps tests fast and free of plant contact.

Lena's permit function at ABP follows this shape exactly: it takes the decoded frame fields and the allow-list version and returns a decision with a reason. Loading the allow-list and writing logs happen outside the function, so its tests run in milliseconds on synthetic data and never risk contact with the plant.

### 28.2 Clause tests

One test file per clause: station allow, function code, register range, policy-unavailable. Synthetic fixtures only. Mutation: break a clause and watch the test fail.

```python
"""Lab: Modbus function-code allow-list on synthetic, already-decoded requests (no network)."""
ALLOW = {("HMI-1", 3), ("HMI-1", 6), ("HIST-1", 3), ("HIST-1", 4)}  # (source, function code)
WRITE_REGS = {("HMI-1", 6): range(40001, 40011)}                     # HMI may write setpoints only
reqs = [("HMI-1", 3, 40001), ("HMI-1", 6, 40003), ("HMI-1", 6, 40050),
        ("HIST-1", 3, 30001), ("HIST-1", 16, 40001), ("ENG-WS", 8, 0), ("HIST-1", 4, 30010)]
for src, fc, reg in reqs:
    if (src, fc) not in ALLOW:
        d = "BLOCK fc-not-allowed"
    elif (src, fc) in WRITE_REGS and reg not in WRITE_REGS[(src, fc)]:
        d = "BLOCK register-out-of-range"
    else:
        d = "PASS"
    print(f"{src:7} fc={fc:2} reg={reg:5} -> {d}")
```

Expected output:

```text
HMI-1   fc= 3 reg=40001 -> PASS
HMI-1   fc= 6 reg=40003 -> PASS
HMI-1   fc= 6 reg=40050 -> BLOCK register-out-of-range
HIST-1  fc= 3 reg=30001 -> PASS
HIST-1  fc=16 reg=40001 -> BLOCK fc-not-allowed
ENG-WS  fc= 8 reg=    0 -> BLOCK fc-not-allowed
HIST-1  fc= 4 reg=30010 -> PASS
```

Lena keeps one test file per clause for ABP's permit function, with fixtures named after the requirement they check. Mutation testing confirmed each file fails when its clause is broken: deleting the register-range check, for example, made the out-of-range tests fail at once. A clause whose tests survive a mutation is treated as untested.

### 28.3 Logging

Log decision, reason, policy version, actor. Do not log passwords or full frame payloads that might contain proprietary recipe data. Redact as needed.

> **Synthetic case — Ashford Batch Plant.** Implementation I shipped reason codes that the timeline UI shows — operators finally saw why a write was blocked at 03:12.

Lena's logs show which policy version made each decision. Frame payloads are left out because they can contain recipe values. Lena checks a sample of logs after each release to confirm nothing sensitive slipped in.

### 28.4 Errors and limits

Stringly-typed reasons drift; use an enum shared with the coverage board.

Lena's implementation uses a shared list of reason codes, such as register-out-of-range and policy-unavailable, published as a versioned document. The coverage board and the timeline view read the same list, so a new code cannot appear in logs without being understood elsewhere. Consumers that see an unknown code treat it as a deny and raise an alert for the tool owner. The document is reviewed with each predicate change.

### Practice note

Fuzz the predicate with random stations, codes and broken UTF-8. It must DENY or error closed, never ALLOW on parse failure.

### 28.1b Reason catalogue and fuzzing

The catalogue lists, for each reason code, the clause that emits it and the test that pins it: fc-not-allowed, register-out-of-range, policy-unavailable, station-unknown. Fuzz inputs that once found a bug join a regression list that is replayed on every release, with the seed that produced them.



Code review checklists for predicate changes include: new clause, new tests, reason-code docs, fuzz case, fail-closed on parse error. Reviewers who skip the list are doing social review, not safety review.

Lena's checklist is attached to every predicate review.

### Field note — fuzz findings

A five-minute fuzz harness threw a UTF-8 station name that previously crashed the decoder into an uncaught exception — which the caller treated as ALLOW. The fix returned DENY parse-error and the harness now runs in CI on every predicate change.


### 28.5 Worked example — a clause test that caught a real bug (synthetic ABP)

Each clause of the permit function gets its own test: source allowed, function code allowed, register in range, default deny. Lena's fuzzing harness then feeds 10,000 random (source, function, register) triples drawn from a seeded generator and asserts that every PASS satisfies all clauses. On the first run it found that function code 23 (read/write multiple registers) passed for HMI-1 because the implementation checked only the read half of the request. The fix rejects 23 unless explicitly listed, a clause test now pins it, and the incident note records which seed reproduced the failure, so anyone can rerun it.

### Exercises

- **EX082 — Signature.** Type signature of permit and why AllowListVersion is an argument. Rubric: 3 = signature + version pin reason; 2 = signature; 1 = vague; 0 = none.
- **EX083 — Mutation.** Which test fails if register range is ignored? Rubric: 3 = 40050 expects BLOCK; 2 = vague; 1 = wrong; 0 = none.
- **EX084 — Redact.** Two log fields to redact. Rubric: 3 = e.g. passwords, full recipe-bearing payloads; 2 = one; 1 = vague; 0 = none.

### Synthesis

Pure predicate, clause tests, safe logs.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — OT, IoT and cyber-physical security: measurement

### Learning outcomes

You will (1) define coverage with a denominator; (2) separate activity metrics from outcome metrics; (3) evaluate detectors with attack class and intervals (Urbina/Giraldo lessons).

### 29.1 Coverage needs a plan

ATT&CK for ICS coverage is observed intersect planned over planned, not observed over all techniques. Without a plan, coverage is vanity.

At ABP, Lena writes the plan of techniques to be tested before each assessment, and the coverage board counts only those. Observed techniques outside the plan are reported separately. The figure of 31 of 44 planned techniques observed means something because the 44 were chosen in advance and the planning guide is published with the board. The plan is fixed before testing.

### 29.2 Activity vs outcome

Activity: frames decoded, tools launched. Outcome: verified remediations, SIS reachability still false, false-alarm rate at plant base rate. Steer on outcomes.

Lena's monthly CNHP report leads with outcomes: remediations verified by re-test, whether SIS-B is still unreachable from L4, and the detector's false-alarm rate at ABP's base rate. Activity counts, such as frames decoded, appear only in a capacity appendix. Steering on activity would reward running more tools rather than fixing more problems. Outcomes are what the plant manager funds.

### 29.3 Detector honesty

Report false-alarm intervals, detection delay, and attack class. A band detector that misses stealthy residual attacks is not equivalent to a CUSUM that catches them — the lab makes that visible.

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

> **Synthetic case — Ashford Batch Plant.** CNHP reports planned-technique coverage and detector FA/delay by class — not a single secure percent.

Lena's pilot report for ABP lists results by attack class. Each class has its own false-alarm interval and mean delay, so a reader can see that CUSUM caught the stealthy residual attacks the band detector missed.

### 29.4 Errors and limits

Denominators stolen from another plant invalidate the metric. Synthetic attacks are not the adversary.

Lena never borrows a denominator from another site's plan, because ABP's techniques, assets and processes differ. If a comparison with another plant is needed, both sites must use the same planning rules, and the report says so. She also states in each report that synthetic attacks represent chosen classes, not the behaviour of a real adversary, so readers do not overrate the detection figures. Both caveats appear in every report.

### Practice note

Caption every dashboard widget with the formula and the plant id. A widget without a formula is decoration and should be removed in review.

### 29.1b Sampling and cohort comparisons

If you sample 50 of 500 assets, say so and do not scale findings as if you visited all 500. Comparing coverage across windows requires the same planning rules. Publish the planning guide beside the coverage board so 71% in March means the same kind of denominator as 71% in September.



Sample selection is recorded with its seed or rule, so the same assets can be revisited at re-test. Prefer metrics that under-claim success, such as counting a fix only after re-test.

ABP's planning guide is published beside the board.

### Field note — methodology lines on charts

When CNHP changed planning rules in June, Pulse-style charts gained a vertical line labelled methodology_id=2026-06. Leadership stopped comparing May's 80% to July's 70% as if they meant the same denominator. Honesty in the chart legend prevented a false narrative of decline.

### Exercises

- **EX085 — Formula.** Write coverage formula and explain a bad denominator. Rubric: 3 = planned denominator + example of all-ICS misuse; 2 = formula; 1 = vanity; 0 = none.
- **EX086 — Lab.** Compare band vs CUSUM on class A in one sentence. Rubric: 3 = CUSUM detects, band does not, FA both 0 in sample; 2 = partial; 1 = wrong; 0 = none.
- **EX087 — Under-claim.** One design that under-claims success. Rubric: 3 = require re-test before closed; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Plan the denominator; measure outcomes; evaluate detectors by class with intervals.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) run a verification plan against ABP's monitor and zoning; (2) record pass/fail with evidence hashes; (3) stop the lab if a safety test fails.

### 30.1 Plan

Tests: allow in-scope reads; deny bad function codes; deny out-of-range writes; fail-closed missing policy; reachability SIS from L4 is false; cycle time under budget with tap. Each row: id, setup, action, expected, evidence path.

At ABP, each row of the plan names the requirement it checks, such as S-1 for the missing-policy row and R-12 for the reachability row. The cycle-time row uses the bench copy of the trunk to PLC-A with the tap installed, checking the time stays well under the 50 ms stop. Rows are written before the lab runs.

### 30.2 Execution

Use synthetic hosts and benches only. Capture stdout and config hashes. Any safety failure (fail-open or SIS reachable) stops the lab and opens a blocker — no continue to gather data.

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

Lena's lab at ABP runs on the bench range with synthetic hosts and fixtures. When the missing-policy row failed once, the lab stopped and a blocker was opened against S-1; no further rows were run until it was fixed, because continuing would have produced results about a monitor already known to be unsafe.

### 30.3 Report

One-page lab report: environment versions, results table, open blockers, sign-off. Attach hashes.

> **Synthetic case — Ashford Batch Plant.** Lab I failed the missing-policy row once; release halted until S-1 was fixed.

Lena's report for each Lab I run lists the tool versions, the fixture-set hash, each row's result and any open blockers, and it is signed by the independent runner. Hashes of logs and exports are attached, so a reviewer can confirm the evidence matches what was run. A report without hashes is not evidence.

### 30.4 Errors and limits

Labs on shared benches collide; book the synthetic range.

Lena books ABP's bench range for each lab run on the shared calendar, with the release under test in the booking. Two teams once ran different builds on the same bench at overlapping times, and their logs became impossible to separate. Since then, a lab run without a booking does not count as release evidence, and the bench is reset to a known state before each booked run. Booking takes minutes.

### Practice note

Lab I is run by someone who did not implement the change under test. The recorded pass needs an independent green checklist.

### 30.1b Golden fixtures and inventory

Keep a sealed directory of synthetic fixtures with known expected decisions. Lab runs must hash-match the fixture set before they count as release evidence. Photograph or export the lab environment inventory into the lab report. It passed on my machine without inventory is not transferable evidence.



Fixture changes are reviewed like code: a new expected decision must name the requirement it comes from. Lab result logs are evidence; retain them with the release tag.

Lena's fixture set is sealed and hashed.

### Field note — independent green

The implementer of a hotfix offered to run Lab I to save time. The reviewer refused, ran the safety rows personally, and found a path that still ALLOWed when the policy file was a directory instead of a file. Independent runners catch assumptions authors stop seeing.


### 30.5 Worked example — reading a laboratory result honestly (synthetic ABP)

Laboratory I replays a recorded day of ABP traffic plus 40 injected write attempts through the permit function and the alarm logic. Results: 40 of 40 injected writes blocked; 2 legitimate engineering writes blocked because the engineering workstation was missing from the allow-list during commissioning; 0 alarms suppressed. Lena reports the two false blocks as a design defect, not noise — in a live plant they would have stopped a scheduled recipe change — and adds a commissioning-mode vector set. The lab report states what was not tested: performance under load, serial links and SIS-B, which is out of scope by design.

### Exercises

- **EX088 — Row.** Write the fail-closed lab row. Rubric: 3 = complete row; 2 = partial; 1 = vague; 0 = none.
- **EX089 — Stop.** What happens on SIS reachable from L4? Rubric: 3 = stop, blocker, no plant use; 2 = note only; 1 = continue; 0 = none.
- **EX090 — Evidence.** Three hashes to attach. Rubric: 3 = policy, binary/version, result log; 2 = two; 1 = one; 0 = none.

### Synthesis

Verify safety first; stop on fail-open or SIS exposure; hash everything.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — OT, IoT and cyber-physical security: implementation II

### Learning outcomes

You will (1) add idempotent finding upserts; (2) enforce schema validation on write; (3) version API responses for CNHP tools.

### 31.1 Upsert

PUT /findings/{id} with full body; same id twice yields one row. Dedup fingerprints propose ids; humans confirm merges across different root causes.

At ABP, finding ids come from the client on create and are reused on every retry, so a network failure mid-request cannot create a duplicate. Fingerprints suggest when two findings may be the same problem, but a person confirms any merge, because two findings on PLC-A can share a register and still have different causes. Merges are logged with reasons.

### 31.2 Validate on write

Reject unknown fields and forbidden names; coerce severity through an enum. Validation errors return machine-readable codes.

Lena's finding store at ABP rejects any record with an unknown field or a forbidden name, such as payload or password, and returns a code saying which field failed. Severity accepts only the agreed values. The same validator runs for interactive creates and bulk imports, a lesson learned after a trusted import path once let a password through in a notes field. Errors are documented with examples.

### 31.3 API versioning

Prefix /v1/; additive changes only within v1. Breaking changes require /v2/ and a migration note.

> **Synthetic case — Ashford Batch Plant.** A mobile client sent risk_score; validator rejected it — empty scores stay out (Chapter 15).

Lena's API for ABP has stayed on v1 so far. Lena publishes the additive-change rule in the API documentation, and continuous integration compares each new schema with the last release to catch removed or renamed fields. If a breaking change ever becomes necessary, v1 will keep running alongside v2 for an announced period, so mobile clients and scanner imports can migrate without failing in the middle of a window.

### 31.4 Errors and limits

Idempotency keys must not be derived from wall-clock alone.

An idempotency key built from the current time changes between retries, so each retry looks like a new request and creates a duplicate. Lena's clients generate the key once per logical operation, store it with the pending request and reuse it until the server confirms success. The rule is documented with the API, and the client libraries enforce it, so individual developers cannot reintroduce the time-based shortcut. Reviews check this rule explicitly.

### Practice note

Bulk import from scanners must pass the same schema validation as interactive create, including forbidden-field checks.

### 31.1b Partial updates and concurrency

PATCH that allows severity changes without evidence references invites silent downgrades. Prefer full PUT of the validated body, or a restricted PATCH that cannot clear evidence hashes or change status to closed without a re-test pointer. Use ETags so two remediators do not clobber each other.



Optimistic concurrency with ETags prevents lost updates that clear re-test pointers. Bulk deletes are forbidden without dual control. Document upsert semantics in OpenAPI so mobile clients do not invent retry ids.

ETags are required on every finding update.

### Field note — bulk import incident

A scanner import path skipped forbidden-field checks because it was trusted. Someone's notes field contained a password. After scrubbing and rotating, bulk import was rewired through the same validator as interactive create. Trusted import is how payloads enter sealed stores.



Clients that omit the finding id on create receive 400 with a link to the upsert documentation, so retries cannot invent duplicates by accident.


### 31.5 Worked example — idempotent upsert of asset records (synthetic ABP)

Two inventory sources report PLC-A: the engineering project export and passive network discovery. Lena's upsert keys on (site, asset tag), not on IP address, because the IP changes when a controller is replaced. Each write carries the source and an observed-at time; a later observation updates firmware version only if its source is authoritative for that field (the project export wins for firmware; discovery wins for "last seen"). Replaying the same import twice produces no change — the test that proves idempotency. Without these rules, a bulk import once overwrote PLC-A's firmware field with "unknown" and hid it from an advisory check.

### Exercises

- **EX091 — Upsert.** Why is POST-without-id risky for retries? Rubric: 3 = duplicates on retry; 2 = vague; 1 = wrong; 0 = none.
- **EX092 — Reject.** JSON body that must 400. Rubric: 3 = contains payload/password/risk_score; 2 = weak; 1 = valid body; 0 = none.
- **EX093 — Version.** Is renaming reason_code to reason a v1-safe change? Rubric: 3 = no, breaking to v2; 2 = hesitant; 1 = yes; 0 = none.

### Synthesis

Idempotent writes, strict schema, explicit versions.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — OT, IoT and cyber-physical security: reliability

### Learning outcomes

You will (1) set availability targets for OT security tools; (2) use retries with budgets that respect cycle time; (3) degrade safely when a dependency fails.

### 32.1 Targets

Allow/deny path during windows: high availability. Coverage dashboards: best-effort. State the target; do not imply five-nines without a budget.

At ABP, the deny path on the serial monitor must work throughout every window, while the coverage dashboard may be unavailable for an hour without harm. Lena writes both targets down with the budget behind each, so nobody assumes the dashboard needs the same care as enforcement, or that enforcement can tolerate the dashboard's outages. Targets are reviewed each year.

### 32.2 Retries

Retries help flaky uploads of evidence but need a deadline so the trunk budget still holds. Cap total attempts.

Lena's evidence uploader at ABP retries with increasing delays and gives up after a fixed number of attempts or a deadline, whichever comes first. Failed uploads stay queued on disk and are reported, so nothing is lost. Retries never run on the trunk to PLC-A, where they could crowd out control traffic and break the cycle budget. The limits are written in the permit.

### 32.3 Safe degradation

If the finding store is down, continue deny/allow locally and queue drafts on disk — never fail open on policy checks.

> **Synthetic case — Ashford Batch Plant.** During a findings-store outage, Lena's laptop queue held drafts; the serial monitor kept denying out-of-range writes.

Lena tests this degraded mode in Lab II on the bench. During a real outage of the finding store, drafts queued on Lena's laptop and the serial monitor kept denying out-of-range writes. When the queue reached its threshold, discovery stopped automatically and Lena was paged, so no scans ran while findings could not be recorded.

### 32.4 Errors and limits

Retries against a rate-limited trunk can look like floods; coordinate budgets with the work permit.

Lena's work permit at ABP states the maximum request rate for any assessment traffic on each trunk, including retries. If retries would exceed it, the tool waits instead. She coordinates with the site's monitoring team before a window, so a burst of retries is not mistaken for an attack and does not trigger an unnecessary incident response. Rates are set with the control engineers. They are reviewed yearly.

### Practice note

When the draft queue grows past a threshold, stop starting new discovery methods and page the lead. Untracked scans while findings cannot be recorded create risk.

### 32.1b Error budgets and health checks

Define error budgets for the deny path separately from best-effort UI budgets. Health-check policy storage and event sink at start of window. Starting a window blind and discovering a broken sink mid-scan is an operations failure this chapter is meant to prevent. Retries need deadlines so trunk budgets still hold.



Chaos experiments run only on synthetic ranges, never during a client's signed window. Record experiment ids separately from window ids so metrics do not mix. Publish both deny-path and UI error budgets.

### Field note — queue back-pressure

When the draft queue hit 50 during a store outage, Track-style discovery stopped automatically and paged Lena. Deny/allow continued. Untracked scans while findings cannot be recorded are how windows create invisible risk; back-pressure is a safety feature.


### 32.5 Worked example — degrading safely when the collector fails (synthetic ABP)

CNHP's monitoring collector sits on a mirror port. If it fails, nothing in the process should change: the design keeps the collector out of every control path. Lena's reliability targets are about evidence, not production: 99.5 % capture availability per month and alerts on loss above 0.1 %. Retries to the central store use exponential back-off with a cap so that a store outage does not flood the DMZ link shared with the historian replica. When the queue fills, the collector drops the oldest raw packets but keeps the summary records, and it raises a "visibility degraded" alert so analysts know their absence of alerts means less.

### Exercises

- **EX094 — Target.** Availability sentence for the deny path. Rubric: 3 = windowed target + measure; 2 = vague high; 1 = five-nines joke; 0 = none.
- **EX095 — Degrade.** What must never degrade to ALLOW? Rubric: 3 = policy/allow-list decisions; 2 = partial; 1 = UI; 0 = wrong.
- **EX096 — Queue.** Back-pressure rule when the draft queue is long. Rubric: 3 = stop new discovery + page; 2 = partial; 1 = ignore; 0 = none.

### Synthesis

Reliable denies, budgeted retries, degrade closed.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — OT, IoT and cyber-physical security: safety and resilience

### Learning outcomes

You will (1) write stop conditions as executable checks; (2) plan rollback of tool changes mid-window; (3) run a tabletop on a deny-list or cycle-time miss.

### 33.1 Executable stops

Stop conditions are code: cycle-time canary, process-alarm feed, client kill-switch file, SIS fault input. Humans also call stop; software must not disagree with a human stop.

At ABP, the serial monitor's stop logic reads the cycle-time canary, the process-alarm feed, a kill-switch file and SIS-B's fault input. Any one of them stops assessment activity at once. A human call to stop always wins, and the software has no setting that can override it or delay it until a running job finishes.

### 33.2 Rollback

Pin releases; keep previous monitor binary signed. If a new build mis-evaluates allow-lists, roll back within minutes.

Lena keeps the previous signed monitor build on the bench and in the window kit, so rollback is a tested command, not a rebuild. The rollback was rehearsed before the first plant window and is repeated after each major release. A rollback restores both the binary and the allow-list version that ran with it. Rollback restores the previous state within minutes. Both are pinned.

### 33.3 Tabletop

Walk a scenario: cycle time exceeds 50 ms at 02:40; who is called; what is said; when resume is allowed. Update the runbook where the tabletop stuck.

> **Synthetic case — Ashford Batch Plant.** Tabletop found the kill-switch file path undocumented; runbook v1.4 fixed it before the next window.

ABP's tabletops run each term with the shift lead present. The first tabletop found that the kill-switch file path was undocumented, and runbook v1.4 fixed it before the next window. Each scenario names who is called, what they are told and who may allow work to resume.

### 33.4 Errors and limits

Resilience theatre is a binder nobody opens. Drill once per term.

Lena's resilience drills at ABP happen once per term, use the real runbook and include at least one stop and one rollback. Each drill produces at least one runbook edit or a recorded reason why none was needed. A binder that has not been opened since the last audit is treated as untested, however complete it looks on the shelf. Drill results are filed with the runbook version. Gaps get owners.

### Practice note

Pre-write SMS/email templates for stop, resume and rollback. Under stress people omit the work-permit version or the next checkpoint time.

### 33.1b Secondary contacts and resume authority

Stop conditions that page only one person fail when that person is offline. Maintain primary and secondary contacts with acknowledged handoff. Who may resume after a stop? Name the role in the work permit. The monitor should require a resume token tied to that role and AllowListVersion.



After every real stop, run a five-minute hotwash and file at least one runbook edit. Resume authority is named in the work permit; Boolean flips anyone on the jumphost can toggle are forbidden.

### Field note — resume token

After a stop, resume required a token issued to the process-safety contact's role and bound to AllowListVersion v1.4.2. A Boolean flip on the jumphost was removed from the UI. Resume without authority is how stop conditions become optional.


### 33.5 Worked example — an executable stop during commissioning (synthetic ABP)

During firewall cut-over on the L3–L2 conduit, the stop condition reads: "If the HMI loses PLC-A values for more than 10 seconds, or any SIS-B trip occurs, revert to the previous rule set." The revert is a single pre-staged command tested twice the day before, and the shift lead holds the authority to call it; the engineer does not argue. Resume requires a written token from the shift lead after the cause is understood. Separately, Lena confirms SIS-B's high-level trip on R-101 is hardwired and unaffected by the change, consistent with IEC 61511's expectation that the safety function stays independent.

### Exercises

- **EX097 — Kill switch.** Design a human kill switch honored in ≤30s. Rubric: 3 = mechanism + poll + fail closed; 2 = idea; 1 = vague; 0 = none.
- **EX098 — Rollback.** Three preconditions to roll back mid-window. Rubric: 3 = prior binary, policy pin, notify process-safety; 2 = two; 1 = one; 0 = none.
- **EX099 — Inject.** One tabletop inject. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = unsafe.

### Synthesis

Stops you can run, rollbacks you can do, tabletops that update runbooks.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — OT, IoT and cyber-physical security: integration

### Learning outcomes

You will (1) integrate monitor events into the finding store; (2) define idempotent consumers; (3) test contracts with fixtures.

### 34.1 Event contract

Deny/allow events: schema version, ids, UTC timestamps, source, fc, register, reason, policy version. Consumers ignore unknown fields; producers stay additive.

Lena's event contract at ABP is versioned and published with fixtures for every reason code. Each event carries both the time it happened and the time it was received, plus the clock source. Producers may add fields but never remove or rename them within a version, so older consumers keep working. Fixtures are checked into the repository. Changes are reviewed.

### 34.2 Idempotent consumers

Finding store keys processed events by event_id. Replaying the log must not create duplicate findings.

Lena tests replay on the bench by feeding a full day's event log through the consumer twice and checking that the finding count does not change. The test caught a bug where events were keyed by timestamp instead of event_id, which duplicated three tickets during a replay storm before the fix landed. Replay tests run in continuous integration. Failures block the merge. The test runs nightly.

### 34.3 Contract tests

Fixture JSON for each reason code; consumer tests assert resulting ticket fields. Run in CI on synthetic fixtures.

> **Synthetic case — Ashford Batch Plant.** A replay storm duplicated three tickets until event_id idempotency landed.

Lena's contract tests run on every pull request and on a schedule. They use one fixture for each reason code and assert the ticket fields the consumer should create, such as asset, technique and severity. A scheduled run against staging catches producer changes even when no pull request is open, so drift is found before a window rather than during one.

### 34.4 Errors and limits

Clock skew muddies timelines; prefer event time plus receive time.

Lena's timeline view at ABP shows event time and receive time side by side, so a reader can see when a device clock is wrong. Lab II later injected a 90-second skew on PLC-A and found that two events were mis-ordered in the dossier until an offset correction was applied. Clock sources are recorded in each event for exactly this reason. Lena keeps clocks synchronised where possible. Drift is alarmed.

### Practice note

Poison events (future timestamps, unknown policy versions) go to a dead-letter queue with an alert — not into findings and not into /dev/null.

### 34.1b Dead letters and schema drills

Events that fail validation go to a dead-letter queue with an alert. Operators replay after fixing the producer. Practice adding an optional field end-to-end in a dry run: producer, consumer, fixture, docs. Teams that only evolve schemas in emergencies invent incompatible shortcuts.



Contract tests run on a schedule against staging fixtures even when no PR is open, catching silent producer drift. Dead-letter age is an SLO chart beside deny-path latency.

ABP runs a schema drill each term. Drill results are recorded.

### Field note — poison quarantine

A producer bug emitted events with timestamps in 2099. Dead-letter quarantine caught them; no findings were created against random hosts. Invisible drops would have been worse — at least quarantine pages someone.



Include a consumer canary that fails the deploy if poison events are not quarantined within one minute in staging.



Schema evolution drills once per term keep producer and consumer teams from inventing incompatible shortcuts under incident pressure.


### 34.5 Worked example — integrating alerts with the maintenance system (synthetic ABP)

CNHP alerts flow into ABP's maintenance-management system so that a "program download to PLC-A" alert can be matched to an open work order. The event contract carries an event ID, asset tag, ATT&CK for ICS technique (T0843 Program Download), time with clock source, and evidence hash. The consumer is idempotent on event ID, so a replayed alert does not create two work orders. Contract tests run in CI with fixtures from both sides; an event lacking a technique field is sent to a dead-letter queue and reviewed daily, rather than dropped. A download with no matching work order escalates to the shift lead within five minutes.

### Exercises

- **EX100 — Field.** Why include policy_version on every event? Rubric: 3 = audit which rules applied; 2 = vague; 1 = wrong; 0 = none.
- **EX101 — Replay.** How does event_id prevent duplicate findings? Rubric: 3 = upsert/ignore duplicates; 2 = vague; 1 = wrong; 0 = none.
- **EX102 — Fixture.** Two fixtures required before a new reason code. Rubric: 3 = producer example + consumer expected ticket; 2 = one; 1 = vague; 0 = none.

### Synthesis

Contracts, idempotent consumers, fixture tests.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) redesign CNHP's coverage UI against under-claim principles; (2) defend the design in a review; (3) produce UI copy that refuses empty scores.

### 35.1 Problem

Stakeholders want a big green percentage. Design a UI that shows planned/observed/not-seen and refuses a single security score.

At ABP the plant manager first asked for one percentage that would show whether CNHP was working. Lena's team explained that any single figure would mix observed techniques, conduit drift and SIS-B reachability, which need different owners and different budgets. The resulting screen gives each measure its own line with its denominator visible, and the planned-but-not-seen techniques are listed by id so the manager can ask which ones matter before approving the next phase.

### 35.2 Copy

71% of planned ICS techniques observed — not a residual-risk score. Button: export denominator. Show SIS reachable? as a separate yes/no.

Lena's team tested this wording with the plant manager and two shift leads before release. One shift lead read an early draft that said only seventy-one percent and assumed the plant was seventy-one percent safe, which is exactly the misreading the caveat prevents. The export button produces the list of the 44 planned techniques with each marked observed or not seen, and the SIS-B line never shows a percentage, because reachability is either true or false on the day of the check.

### 35.3 Review

Reviewers try to force a red/yellow/green risk badge; studio must hold the line with measurement chapter rules.

> **Synthetic case — Ashford Batch Plant.** Studio II killed the badge; the dashboard lists planned-not-seen techniques by id and SIS reachability separately.

Critics in the studio argued that executives would not read a list. Lena's team answered with the manager's actual decision: which conduits to fund and close next, which a colour cannot express. The removed badge also had no defined rule for turning yellow, so two reviewers had already disagreed about its colour on the same data. Replacing it with named items ended that argument and gave each item an owner.

### 35.4 Errors and limits

Dark patterns (just for executives) reintroduce empty scores — reject in CODEOWNERS for UI.

At ABP a later request asked for an executive-only summary view with a single coloured dial. Lena's team declined it during code review, citing the studio decision and the measurement rules, and offered instead a one-page export with the same three numbers and their denominators. Requiring a code owner to approve every change to the dashboard interface means this argument is settled by a named reviewer who knows the history, rather than reopened quietly by whoever edits the screen next.

### Practice note

User research task: explain this number to a plant manager without saying we are safe. If users cannot, the copy has failed.

### 35.1b Accessibility and export truth

Under-claiming metrics must still be readable: large type for the fraction, plain language for the caveat, keyboard access to the denominator export. If the UI and the CSV export disagree, the export wins for the report. Build exports first; treat UI as a view.



Narrative exports generated from the same query as the UI paste into reports without screenshot ambiguity. Hiding the caveat in a tooltip reintroduces the empty-score problem for anyone who does not hover.

Lena checks every release against the export.

### Field note — CFO explain task

In user research, three managers explained the coverage fraction as how safe we are. After copy changes that forbade that reading and surfaced SIS reachability separately, the same task produced explanations about planned checks and open findings instead.



Export as the source of truth removes arguments about what a screenshot meant in a status meeting.


### 35.5 Worked example — the studio critique (synthetic ABP)

Studio II's brief: a plant manager must decide whether to approve the next CNHP phase from one screen. Lena's team shows three numbers with denominators — 31 of 44 planned ATT&CK for ICS techniques observed in testing, 6 of 9 conduits matching the zone design, SIS-B reachable from any routed zone: no — plus a short list of open high findings. Critics argued for a single risk badge; the team replied that the manager's decision depends on which conduits remain open, not on an average. The accepted design puts the open-conduit list first, because it is the item the manager can actually fund.

### Exercises

- **EX103 — Copy.** Subtitle under the coverage number. Rubric: 3 = denies residual-risk reading; 2 = weak caveat; 1 = none; 0 = implies safety.
- **EX104 — Badge.** One sentence refusing a RAG badge. Rubric: 3 = clear + alternative; 2 = refuse only; 1 = accepts; 0 = none.
- **EX105 — Export.** Columns in denominator export. Rubric: 3 = technique id, planned, observed, notes; 2 = partial; 1 = just %; 0 = none.

### Synthesis

UI that teaches the metric, not a traffic light of vibes.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — OT, IoT and cyber-physical security: performance and scale

### Learning outcomes

You will (1) size monitors under cycle-time budgets; (2) apply token-bucket thinking to assessment traffic; (3) measure plant impact with a canary.

### 36.1 Cycle time is first-class

Throughput goals that ignore the PLC cycle budget are bugs. Size decode pipelines so the wire-plus-decode time stays inside the budget measured in Chapter 3.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Expected output:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

At ABP the RS-485 trunk to PLC-A runs a 21 ms polling cycle inside a 100 ms control cycle, and the stop condition fires if cycle time reaches 50 ms. Lena sizes the monitor so that tapping, decoding and logging add nothing to the wire time, because the tap is passive and the decoder runs on its own host. Load tests on the bench replay a full day of captured traffic at double speed to confirm the decoder never falls behind the trunk.

### 36.2 Assessment traffic

When active methods are authorized, rate-limit them so they cannot starve control traffic. Prefer listen-only methods; when you must poll, share a global budget across scanners.

During CNHP assessment windows at ABP, only one active tool may poll the trunk at a time, and its request rate is written in the permit before it starts. Passive discovery from the tap covers most of the inventory, so active polling is limited to the few devices that do not speak on their own. Each tool reports its rate to the shared budget, and the window lead can pause all active methods with one switch if cycle time rises.

### 36.3 Canaries

A synthetic canary request or cycle-time probe every minute tracks health; stop conditions fire on threshold (Chapter 33).

> **Synthetic case — Ashford Batch Plant.** With 21 ms cycles on the RS-485 trunk, Lena left headroom under 50 ms so a decode spike would not trip the stop.

The canary at ABP reads one harmless status register on PLC-A every minute and records the response time beside the trunk cycle time. If either moves toward its threshold, the window lead is paged before the stop condition is reached, which gives time to pause active work calmly instead of reacting to an automatic stop.

### 36.4 Errors and limits

Distributed scanners need a coordinated global budget or they N× the limit.

At ABP two scanners once ran from different hosts, each within its own rate, and together exceeded the trunk budget. Lena moved the budget to a single coordinator that grants tokens to every scanner, so the total stays within the permit no matter how many tools are running. A scanner that cannot reach the coordinator is not allowed to send anything, which keeps the failure safe rather than letting each tool fall back to its own limit.

### Practice note

Publish a rate-limit economics note: cost of waiting versus cost of a batch interruption. Most arguments for raising limits dissolve when interruption cost is written down.

### 36.1b Fairness and warm-up

When several methods share one budget, a noisy enumerator can starve a quiet config review. Weight or separate budgets by method class. Ramp traffic at window start and drain before hard stop. Instant full-rate starts look like floods to defenders and trip unrelated alarms.



Document who may raise a rate limit and which AUTH ticket type is required. Separate budgets for quiet versus noisy methods so a hungry enumerator cannot starve config review work.

Lena enforces both budgets in the coordinator.

### Field note — warm-up schedule

The scheduler now ramps assessment polls over five minutes at window start. Instant full-rate starts had tripped unrelated vibration alarms on a neighbouring skid. Warm-up is courtesy to the process and to the people who own it.


### 36.5 Worked example — measuring monitoring load on PLC-A (synthetic ABP)

A proposed asset-health poller would read 120 holding registers from PLC-A every second. On the bench controller, Lena measures scan time with and without the poller: 18 ms baseline, 23 ms with polling, against a 50 ms watchdog. The increase is acceptable on the bench, but she still caps the poller at 120 registers every 5 seconds in production, adds a canary on one line before plant-wide rollout, and alarms if scan time exceeds 30 ms. Assessment traffic gets the same treatment: any test tool must declare its request rate, and the permit sets a maximum.

### Exercises

- **EX106 — Lab.** Bytes and time per cycle at 115200 — report both. Rubric: 3 = 244 bytes, 21.2 ms; 2 = one; 1 = wrong; 0 = none.
- **EX107 — Headroom.** If budget is 50 ms and cycle is 21 ms, what headroom remains and why keep it? Rubric: 3 = ~29 ms for spikes/retries; 2 = number only; 1 = use it all; 0 = none.
- **EX108 — Global.** Why do three uncoordinated pollers break a 2 req/s permit? Rubric: 3 = 3× rate; 2 = vague; 1 = deny; 0 = none.

### Synthesis

Budget first, scale second, canary always.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — OT, IoT and cyber-physical security: operations

### Learning outcomes

You will (1) write a window runbook; (2) hand over between shifts; (3) manage close-out including account disable and evidence seal.

### 37.1 Runbook contents

Contacts, work-permit pointer, tool versions, stop conditions, escalation tree, evidence paths. Keep it short enough to use under stress.

Lena's ABP runbook fits on four printed pages. It names the window lead and the control engineer, links the work permit and lists the versions of each tool allowed. Stop conditions, including cycle time at 50 ms, are on the first page, followed by the escalation tree and the location of the evidence folder. Runbook v1.4 added the kill-switch file path after the tabletop found it missing, and every change since is recorded in the version history.

### 37.2 Handover

Shift log: open findings, last event ids, pending approvals, kill-switch state, process alarms during the window. Verbal handover plus the log.

At ABP the outgoing lead reads the shift log aloud to the incoming lead and both initial it. The log lists open findings with owners, the last event ids recorded by the monitor, any approvals still pending, whether the kill switch is armed, and any process alarms raised during the window. Speaking the items aloud catches entries one person thought obvious and the other had never seen, such as a temporary rule awaiting removal.

### 37.3 Close-out

Disable temporary accounts, rotate secrets, seal evidence, export metrics, schedule retrospective. A checklist beats memory.

```python
"""Lab: fit patch jobs into plant maintenance windows (synthetic, greedy by risk)."""
windows = [("W1 Sat 02-06", 4.0), ("W2 Sun 02-04", 2.0)]
jobs = [("HMI OS update", 1.5, 8), ("historian DB patch", 2.5, 5), ("PLC-A firmware", 3.0, 9),
        ("eng-WS AV update", 0.5, 3), ("switch firmware", 1.0, 6)]   # name, hours, risk score
left = {w: h for w, h in windows}; plan = {w: [] for w, _ in windows}; deferred = []
for name, h, r in sorted(jobs, key=lambda j: -j[2]):
    for w, _ in windows:
        if left[w] >= h:
            left[w] -= h; plan[w].append(name); break
    else:
        deferred.append(name)
for w, _ in windows:
    print(w, plan[w], f"spare={left[w]:.1f}h")
print("deferred:", deferred)
```

Expected output:

```text
W1 Sat 02-06 ['PLC-A firmware', 'switch firmware'] spare=0.0h
W2 Sun 02-04 ['HMI OS update', 'eng-WS AV update'] spare=0.0h
deferred: ['historian DB patch']
```

> **Synthetic case — Ashford Batch Plant.** Close-out caught the deferred historian patch still without a date — escalated before the retro.

Lena's close-out checklist is run by two people and its result is stored with a hash. A historian patch had been deferred during the window with no date, so the checklist flagged it and the patch received an owner and a date before the retrospective met.

### 37.4 Errors and limits

Runbooks in wikis nobody can access from the control room fail; keep an offline copy.

At ABP the control room lost network access to the wiki during one window, and the lead needed the escalation tree immediately. Since then, the latest runbook is printed and kept in a folder beside HMI-1, and a copy sits on the engineering workstation for offline use. Each printed copy carries its version number, and the close-out checklist confirms the paper copy matches the current version, so an old procedure is not followed by mistake during an incident.

### Practice note

On-call for CNHP tools is not a license to widen conduits. Pages are about tool safety and permit enforcement; process incidents route to the plant IR/process-safety path.

### 37.1b Calendar and spare kits

Windows belong on a shared calendar with work-permit version in the description. Accidental overlap of two noisy methods on the same trunk is an operations failure. Ops kits include spare jump-host images, printed contact cards and offline permit copies for when SSO is down.



Store the close-out checklist result hash so incomplete close-outs cannot be marked done quietly. Handover includes reading the last ten monitor denies aloud to the incoming lead.

Lena checks the calendar at every handover. Overlaps are logged as findings.

### Field note — offline kit

SSO failed during a Sunday window. The offline runbook copy and printed contact cards let the team stop cleanly and notify process safety. Wikis nobody can reach from the control room are not runbooks.



Operations metrics include pages per window and mean time to acknowledge stops; vanity metrics like hosts touched stay off the ops dashboard.


### 37.5 Worked example — a shift handover with security content (synthetic ABP)

ABP's handover sheet gains three lines: open CNHP alerts and who owns them; any vendor remote session enabled or scheduled; and any temporary rule or bypass in force with its expiry time. On 14 March the night shift recorded a temporary firewall rule for a vendor diagnostic expiring at 06:00; the day shift checked at 06:15, found it still present, and removed it with the engineer's agreement. Without the handover line, the rule would have become a permanent conduit. Close-out of each security work order requires the evidence pointer and confirmation that temporary changes were reverted.

### Exercises

- **EX109 — Checklist.** Six close-out steps. Rubric: 3 = six sensible; 2 = four; 1 = two; 0 = none.
- **EX110 — Handover.** Three fields the shift log must include. Rubric: 3 = findings/events/approvals (or equiv.); 2 = two; 1 = one; 0 = none.
- **EX111 — Lab.** Which job was deferred and what must close-out record? Rubric: 3 = historian patch + residual risk + next window date; 2 = name only; 1 = vague; 0 = wrong.

### Synthesis

Operate with runbooks, handovers and ruthless close-out.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — OT, IoT and cyber-physical security: validation

### Learning outcomes

You will (1) validate fixes with re-tests; (2) avoid validation that reintroduces process risk; (3) record negative results.

### 38.1 Re-test design

Same vantage, least privilege, same evidence standard. For an allow-list fix: confirm the write is denied on the bench; do not spray writes at the live PLC.

When the HIST-1 allow-list was tightened at ABP, Lena re-tested from the same jump host and account used for the original finding. She replayed a function 16 write to the bench copy of PLC-A and confirmed the monitor denied it with the expected reason code. The live check was read-only: she compared the deployed allow-list version with the bench version rather than sending writes toward production equipment.

### 38.2 Negative results

Still open is a valid validation outcome. Finding stores must accept it without forcing close.

At ABP the re-test of shared engineering passwords found they were still in use on two workstations, so the finding stayed open with new evidence attached. Lena's finding store allows a re-test to record still open with a date and a reason, and the owner receives a new deadline. Forcing every re-test to close a finding would encourage reviewers to mark fixes done when they are only partly applied.

### 38.3 No new methods

Validation uses the method that found the issue, or a weaker read-only check — not a chance to try new attacks.

> **Synthetic case — Ashford Batch Plant.** Re-test of the L4 to L2 rule: reachability now excludes L1-SIS; ticket closed with export hash. A separate finding on shared eng passwords stayed open.

Lena's validation plan names the original method in the ticket before the re-test starts. When a reviewer suggested trying a new fuzzing tool during validation, she logged it as a proposal for the next assessment instead.

### 38.4 Errors and limits

Different environment (bench vs plant) means you validated the bench.

At ABP, Lena's allow-list fix was first validated on the bench copy of PLC-A, and the ticket said so. A separate read-only check confirmed that the production monitor was running the same allow-list version, and only then was the finding marked fixed in production. Reports keep the two results apart, because a bench pass cannot show that the plant's configuration matches the bench, and some differences, such as firmware revisions, would change the result.

### Practice note

Automated re-tests are allow-listed checks with hard timeouts. They never include credential stuffing or exploit retries.

### 38.1b Evidence of validation and adjudication

Validation tickets link to the original finding, the method used, the timestamp and the hash of the new evidence. Looks good to me without those fields does not close a critical. Disputes escalate to a named adjudicator who compares evidence hashes — they do not re-attack.



When many similar findings share a root cause, re-test a sample plus the originally reported assets, and say so. Adjudicator decisions are final for the window and may only be appealed in the retrospective.

Lena's tickets carry all four fields.

### Field note — sample re-test

Twenty HMIs shared a missing allow-list entry. Validation re-tested five plus the originally reported two, documented the sample, and left the finding open until the fleet job finished. Claiming all twenty closed after two checks would have been a measurement lie.


### 38.5 Worked example — validation re-test of the zoning design (synthetic ABP)

Six months after deployment, Lena re-runs the reachability check from Chapter 2 against the live firewall export and the passive-discovery conduit list. The export matches the design for 8 of 9 conduits; the ninth shows an undocumented L4→L3 rule added during an ERP upgrade. The validation report records the negative finding with evidence, assigns it to the network owner, and does not introduce any new test method mid-validation, so results remain comparable with the commissioning baseline. The SIS-B zone remains unreachable in both datasets, which is reported as confirmed rather than assumed.

### Exercises

- **EX112 — Re-test.** Steps to validate a removed L4 to L2 rule safely. Rubric: 3 = export+reachability, expect no path, evidence, no live writes; 2 = partial; 1 = live attack; 0 = none.
- **EX113 — Negative.** Why must still open be storable? Rubric: 3 = honesty/metrics; 2 = vague; 1 = always close; 0 = none.
- **EX114 — Env.** Limitation when re-test was bench-only. Rubric: 3 = clear; 2 = vague; 1 = claims plant; 0 = none.

### Synthesis

Validate narrowly; keep negatives; don't widen methods.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — OT, IoT and cyber-physical security: maintainability

### Learning outcomes

You will (1) budget for policy and dependency updates; (2) keep adapters thin; (3) document ownership including vacation coverage.

### 39.1 Churn

ATT&CK for ICS techniques, PLC firmwares and vendor HMI support matrices change. Budget calendar time for updates; pin versions and watch advisories.

At ABP, Lena keeps a dependency page listing the ATT&CK for ICS release used by the mapper, the firmware revisions of PLC-A and SIS-B, and the HMI vendor's supported versions. A subscription to vendor advisories feeds a weekly review, and each pinned version has a review date. When the technique list changes, the coverage plan is rebuilt from the new release before the next assessment, so the 44 planned techniques never silently refer to an outdated catalogue.

### 39.2 Thin adapters

Isolate third-party SDKs behind interfaces so upgrades do not rewrite the finding store core.

Lena's team learned this from the screen-scraping alarm adapter, which broke with each HMI update and touched code far beyond its purpose. CNHP now places every vendor library behind a small interface owned by the team, with contract tests that use recorded vendor output. When a vendor changes its library, only the adapter and its tests change; the permit function, finding store and dossier code stay untouched, and the release notes can say exactly which part moved.

### 39.3 Ownership

Every service has a named owning squad and a backup. CODEOWNERS enforces review. Missing vacation coverage is a release blocker.

> **Synthetic case — Ashford Batch Plant.** The ATT&CK for ICS mapper is an adapter; upgrading the technique list is a data PR, not a rewrite.

At ABP each CNHP service page names an owner and a backup by person, not by team alias. Before a release, the pages are checked against the leave calendar, and a release with no cover during the next window is held until someone is trained.

### 39.4 Errors and limits

Orphan tools rot into fail-open museums.

The screen-scraping alarm adapter at ABP is the example Lena uses: one engineer understood it, it needed eleven fixes in a year, and it failed silently whenever the HMI changed. A tool with no owner stops being patched, and when it breaks nobody notices whether it is failing closed or open. Lena's rule is that a tool without an owner and backup is either adopted by a named person within a month or retired with a published deletion date.

### Practice note

Write a bus-factor note: who can release, who understands permit(), who can restore the sealed store. If the answer is one person, schedule cross-training before the next season.

### 39.1b Deprecation and deletion plans

Announce API deprecations with dates; keep dual-run periods. Maintainability includes knowing how to retire a tool: export dossiers, revoke credentials, archive code. Calendar a dependency upgrade month each year so CVE pins do not wait for an emergency.



Ownership pages list vacation coverage by name. Treat missing coverage as a release blocker equal to a failing test. Cross-training sessions use the same synthetic fixtures as Lab I.

Lena applies this plan to every CNHP tool, including the replaced adapter. Its retirement was announced in advance.

### Field note — vacation blocker

A release was blocked because the only person who understood permit() was on leave without a trained backup. Cross-training on Lab I fixtures the next week cleared the blocker. Maintainability is mostly about people allowed to be on holiday.



API deprecation windows keep dual-run periods so Pulse-style consumers do not break mid-window when reason codes change.



Deletion plans for retiring a monitor include dossier export, credential revocation and archive of the code tag.


### 39.5 Worked example — removing a fragile adapter (synthetic ABP)

CNHP had a custom adapter that parsed the HMI vendor's alarm export by screen-scraping. Each HMI update broke it, and only one engineer understood it. Lena's maintainability review measures churn (11 fixes in a year), ownership (one person) and blast radius (alarm statistics for the whole plant). She replaces it with the vendor's supported OPC UA alarm interface, keeps the adapter read-only for one release as a fallback, publishes a deletion date, and writes the runbook so a second engineer can operate the new path. Fewer bespoke parts mean fewer silent failures in security evidence.

### Exercises

- **EX115 — Pin.** How do you pin the monitor for a window and still allow safety patches? Rubric: 3 = version pin + mini Lab I for hotfix; 2 = partial; 1 = latest always; 0 = none.
- **EX116 — Adapter.** One method on a StoragePort interface. Rubric: 3 = e.g. put_evidence(hash,bytes); 2 = vague; 1 = concrete SDK call; 0 = none.
- **EX117 — Owner.** Ownership line for the serial monitor. Rubric: 3 = squad + backup + contact; 2 = squad; 1 = team; 0 = none.

### Synthesis

Pins, adapters and named owners keep tools alive safely.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify end-to-end flow from frame to ticket to coverage; (2) inject faults; (3) sign a release candidate.

### 40.1 End-to-end

Synthetic frame to monitor decision to event to finding ticket to coverage update. Record hashes at each hop.

In ABP's Lab II, Lena replays a synthetic frame on the bench and follows it through each step: the permit function's decision with its reason code, the alert, the maintenance-system work order, the finding ticket and the coverage update. A hash is recorded at each hop, so the dossier can prove that the ticket describes the same event the monitor saw. A chain that cannot be traced hop by hop is not counted as passing, even when the final result looks right.

### 40.2 Faults

Kill finding store mid-flow; confirm monitor still denies and drafts queue. Corrupt an evidence file; confirm hash mismatch alert. Feed a flat (unsafe) edge list; confirm reachability fails the SIS check.

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

Lena's Lab II faults also include collector power loss, which raised the visibility-degraded alert in 40 seconds, and 90 seconds of clock skew on the bench copy of PLC-A. Each fault is injected separately and then in pairs, because a failure that is harmless alone can corrupt evidence when combined with another.

### 40.3 Sign-off

Release candidate checklist signed by implementer and reviewer; safety rows must be green.

> **Synthetic case — Ashford Batch Plant.** Lab II found coverage updated before ticket create on retry — fixed ordering with an outbox.

At ABP the Lab II sign-off lists every row with its result and any open defect with an owner, such as the event mis-ordering caused by clock skew. Lena's ordering fix ensures the ticket is written before the coverage board updates, so a retry cannot count a finding that was never recorded.

### 40.4 Errors and limits

E2E without fault injection only proves the happy path.

Lena's first end-to-end run at ABP passed every row, yet Lab II with faults injected found that clock skew mis-ordered two events in the dossier and that a retry updated coverage before the ticket existed. Neither defect would appear on a clean run, because both depend on timing failures that only occur when something breaks. Lab II sign-off therefore requires each fault script to have run and its result recorded, and a run with no faults is reported as a smoke test.

### Practice note

Malicious fixture pack: wrong hashes, reordered events, future timestamps, flat graph claiming to be zoned. Passing only happy fixtures is an incomplete laboratory.

### 40.1b Observability and parity

Lab II enables debug logs temporarily but seals a redacted copy. Leaving debug on in window builds can leak secrets. Lab environment mirrors production tool versions and policy signing keys (test keys). A flaky Lab II is a blocker, not a retry-until-green ritual.



Happy-path green with malicious-pack red still fails Lab II sign-off. Fault-injection scripts are checked into the lab folder and pinned by SHA in the report. Environment parity gaps explain green-in-lab red-in-window surprises.

Lena's sign-off checks for parity gaps.

### Field note — malicious pack

Lab II's malicious pack included a flat graph labelled as zoned. The reachability check failed closed and blocked the release. Happy-path-only laboratories ship lies.



Seal Lab II logs with the same manifest tool the dossier uses so students practise one hashing workflow.



Flaky tests are quarantined and fixed; shipping with sometimes fail-closed is shipping fail-open.


### 40.5 Worked example — end-to-end fault injection (synthetic ABP)

Laboratory II exercises the full chain on the bench: replayed traffic → permit function → alert → maintenance-system work order → dossier. Injected faults: collector power loss, clock skew of 90 seconds on PLC-A, a malformed event, and a dead-letter backlog. Results: power loss raised "visibility degraded" in 40 s; clock skew was detected by the time-source check but mis-ordered two events in the dossier until the offset correction was applied; the malformed event reached the dead-letter queue; the backlog cleared in 7 minutes. Sign-off lists the mis-ordering as an open defect with an owner.

### Exercises

- **EX118 — Ordering.** Why create ticket before coverage count increases? Rubric: 3 = coverage must reflect recorded findings; 2 = vague; 1 = either order; 0 = none.
- **EX119 — Fault.** Expected monitor behaviour when finding store is down. Rubric: 3 = still evaluate/deny; queue drafts; 2 = partial; 1 = fail open; 0 = none.
- **EX120 — Sign-off.** Two signatures required — who? Rubric: 3 = implementer + independent reviewer; 2 = one; 1 = manager only; 0 = none.

### Synthesis

E2E with faults; green safety; two signatures.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — OT, IoT and cyber-physical security: system optimization

### Learning outcomes

You will (1) profile OT security pipelines ethically; (2) optimize under cycle-time and ROE constraints; (3) reject optimizations that weaken safety.

### 41.1 Profile first

Measure where time goes: decode, permit eval, event write. Optimize the dominant term. Synthetic load only.

At ABP, Lena profiled the monitor on the bench before any optimisation was approved. Replaying a recorded day of trunk traffic, she measured how long decoding, permit evaluation and event writing each took, and found event writing dominated. Batching writes cut overall latency without changing a single permit rule. She uses synthetic or replayed load only, because profiling against live equipment would add exactly the risk the monitor exists to reduce, and the bench copy of PLC-A behaves closely enough for timing work.

### 41.2 Constraint-preserving

Caching AllowListVersion is fine if invalidation on publish is correct. Caching allow decisions across stations is not — stations differ.

In CNHP the allow-list is cached in memory with its version number, and every publish clears the cache before the new version is used, so stale rules cannot linger. Caching individual decisions was rejected, because HMI-1 and the engineering workstation are allowed different registers, and a decision cached for one would be wrong for the other. Lena's tests include a publish during heavy load to confirm that the first decision after publishing always uses the new version.

### 41.3 Safety veto

Any optimization that skips deny-list checks, shortens audit fields or fails open is rejected regardless of speedup.

```python
"""Lab: does a polling schedule fit the PLC scan/communication budget? (synthetic)"""
link_bps = 115200; bits_per_byte = 10           # RS-485 serial, 8N1 + start bit
polls = [("T-1 level", 8), ("T-2 level", 8), ("R-101 block", 40), ("pump status", 8), ("historian sweep", 120)]
overhead = 12                                    # bytes of request+framing per poll (assumed)
total = sum(n + overhead for _, n in polls)
t = total * bits_per_byte / link_bps
print(f"bytes per cycle={total} time per cycle={t*1000:.1f} ms")
for target in (100, 50):
    print(f"cycle budget {target} ms -> {'fits' if t*1000 <= target else 'OVERRUN'}")
```

Expected output:

```text
bytes per cycle=244 time per cycle=21.2 ms
cycle budget 100 ms -> fits
cycle budget 50 ms -> fits
```

> **Synthetic case — Ashford Batch Plant.** Caching signed allow-lists in memory cut latency; invalidation on publish kept safety. A proposal to skip register checks for known good HMIs was vetoed.

Lena records each vetoed proposal at ABP with its expected speedup and the reason it was rejected. The decision log means the same idea is not reopened every quarter without new safety arguments.

### 41.4 Errors and limits

Benchmarks on laptops do not predict plant trunks.

At ABP, a decoder that ran easily on a developer laptop fell behind when Lena tested it on the bench copy of the RS-485 trunk with real timing and frame sizes. Laptops have faster processors and none of the serial timing limits that matter on the plant. Lena now accepts performance figures only from the bench, and each benchmark report states the trunk's 21 ms polling cycle and the 50 ms stop next to the measured result, so readers can judge the margin.

### Practice note

Optimization proposals require a safety paragraph. Proposals without it are returned unread.

### 41.1b Load shedding and N+1

Under overload, shed discovery work before shedding deny evaluation. Chatty ticket updates during bulk import crush the finding store — batch writes and measure. Keep headroom under the cycle-time budget so a retry storm does not breach it.



Reject optimization PRs that remove reason codes from logs even if latency improves. Benchmarks cite the cycle-time budget next to the achieved rate so unconstrained benches are obvious.

Lena's reviews apply each rule. At ABP, Lena tested overload by replaying traffic at triple speed: discovery paused first while deny decisions continued at full rate and stayed well under the cycle budget.

### Field note — safety paragraph

An optimization PR that removed reason codes from hot-path logs to save microseconds was returned unread for lack of a safety paragraph. The revised PR kept the codes and found its speedup elsewhere. Safety paragraphs are not bureaucracy; they are the veto mechanism.



Capacity headroom under the cycle budget is documented next to the token-bucket or poll schedule so the next debate starts from numbers.


### 41.5 Worked example — optimisation with a safety veto (synthetic ABP)

Production asks to shorten the R-101 batch by raising the feed rate, and asks CNHP to relax the permit function's rate limit on setpoint writes from one per 10 s to one per second to suit the faster recipe. Lena profiles first: only the charge phase needs faster writes. She proposes a phase-specific limit, applied only while the batch state is "charge", and submits it to the process safety engineer, who confirms SIS-B's high-temperature and high-level trips are unaffected. The safety engineer holds a veto over any optimisation touching a safety-relevant loop; this one passed, with a load test on the bench.

### Exercises

- **EX121 — Veto.** An optimization that must be rejected. Rubric: 3 = safety-weakening example; 2 = vague; 1 = okays it; 0 = none.
- **EX122 — Cache.** When is decision caching safe? Rubric: 3 = same version+station+fc+reg, short TTL, invalidate on publish; 2 = partial; 1 = always; 0 = none.
- **EX123 — Shed.** What do you shed first under overload? Rubric: 3 = discovery/assessment before deny evaluation; 2 = partial; 1 = drop denies; 0 = none.

### Synthesis

Speed under constraints; safety has veto power.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — OT, IoT and cyber-physical security: applied research

### Learning outcomes

You will (1) frame a research question about OT security programmes; (2) choose measures and baselines with detector-evaluation hygiene; (3) keep dual-use out of student research.

### 42.1 Questions that fit

Does dual-approval reduce conduit-widen incidents? Does showing denominators change stakeholder interpretation of coverage? Not new bypass against PLC brand X.

Lena's applied research at ABP followed this pattern: she asked how many days of baseline traffic a new-conduit detector needs before false alerts drop below one per week. The question could be answered with recorded traffic and would directly change how the plant configures its monitor. She declined a suggestion to study bypasses against a particular PLC brand, because that would produce attack knowledge without improving how ABP runs its defences.

### 42.2 Design

Pre-register measures; use synthetic or consented operational data; report intervals and attack classes (Urbina et al.; Giraldo et al.). Replication beats novelty theatre.

Lena registered her measures, baseline lengths and threshold before analysing ABP's 60 days of recorded traffic. Her amendment log records one change: the ERP upgrade on day 33 added new traffic, so that day was analysed separately rather than dropped. Results are reported with intervals for each baseline length, so readers can see where the evidence is weak. She would rather confirm an earlier finding carefully than claim a new one that nobody can reproduce.

### 42.3 Disclosure

If research accidentally finds a live issue, follow responsible disclosure — not a class blog.

> **Synthetic case — Ashford Batch Plant.** Lena's applied study compared ticket reopen rates before/after requiring re-test evidence; pre-registered, synthetic+anonymized.

Lena's research plan named the vendor's product security team as the first contact for any flaw found in a product, and it set publication only after the vendor responded. The thesis would describe a fault only in general terms. Her supervisor reviewed the plan before any traffic was analysed.

### 42.4 Errors and limits

Course projects are not human-subjects work; avoid collecting personal operator data.

Lena's research at ABP used traffic between devices, not records of what individual operators did, so no person could be identified from her data. Where operator actions appeared in logs, such as acknowledgements on HMI-1, she removed user names before analysis. Studying people properly needs ethics review that a course project does not have, so any question about operator behaviour is left for future work with the appropriate approvals rather than answered with data collected informally.

### Practice note

Preregistered analysis code lives in the repo with a freeze commit before data collection. Amending after peeking requires a logged amendment.

### 42.1b Data sharing and negative results

Even synthetic-plus-anonymized operational metrics need a written agreement with the host for student theses. Publishable applied research includes negative results. Hiding negatives biases the next cohort toward empty confidence.



State the dual-use boundary in the thesis ethics section with a concrete refusal example. Negative results get the same figure quality as positive ones in the thesis template.

Lena's thesis reports which baselines failed the threshold. Lena's host agreement for ABP's data was signed before analysis, and her thesis reports the baseline lengths that never reached the threshold with full figures.

### Field note — amendment log

After peeking at pilot data, a student wanted to change the primary measure. The amendment log recorded the reason and kept the original measure as a secondary analysis. Pre-registration without amendment discipline is theatre.



Data sharing agreements, even for anonymized metrics, are written before student theses begin — mentor said it was fine is not enough.



Negative results are publishable and required in the thesis template's results section.


### 42.5 Worked example — a research question that fits the plant (synthetic ABP)

Lena's applied research asks: on ABP's recorded traffic, how many days of baseline are needed before a new-conduit detector's false alerts fall below one per week? The design uses 60 days of synthetic-but-realistic traffic, sliding baselines of 3, 7, 14 and 28 days, and a pre-registered threshold. The amendment log records one change: an ERP upgrade added traffic on day 33, so that day is analysed separately rather than silently removed. Disclosure planning is part of the design: if the work reveals a product flaw, it goes to the vendor's PSIRT before publication.

### Exercises

- **EX124 — Question.** One acceptable research question. Rubric: 3 = programme/process focused; 2 = borderline; 1 = exploit focused; 0 = none.
- **EX125 — Measure.** Primary measure for dual-approval study. Rubric: 3 = e.g. unapproved widen attempts/quarter; 2 = vague; 1 = security; 0 = none.
- **EX126 — Dual-use.** Refuse a project that asks for a new PLC exploit. Rubric: 3 = refusal + alternative; 2 = refusal; 1 = accepts; 0 = none.

### Synthesis

Research the programme and process; leave weaponization alone.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) adapt CNHP engineering to a host organization's constraints; (2) write a practice report without proprietary detail; (3) translate between process safety, ops and engineering.

### 43.1 Placement

In industry or public service, work-permit templates, residency and procurement differ. Your job is still fail-closed tooling and honest measurement — not clever unauthorized tests.

On her placement at a contract manufacturer, Lena found different permit forms, a different procurement process and stricter rules on where data could be stored than at ABP. She adapted her methods to the host's process instead of importing ABP's forms. What did not change was the core of her practice: tools that stop safely when unsure, measurements with their denominators, and tests run only within the scope the host had approved in writing.

### 43.2 Sanitized reporting

Course deliverables use synthetic names and aggregates. Real plant identifiers stay inside the host's systems.

Lena's placement report described the vendor laptop risk without naming the host, its plants or its devices. Addresses and host names stayed inside the host's systems, and figures were given only as counts or ranges. The host's clearance review checked the report before it reached the university, and her supervisor graded the sanitized version, so nothing identifying left the organisation. Lena kept the originals on the host's systems.

### 43.3 Translation

Process safety hears independence and SIL. Ops hears windows and alarms. Engineering hears schemas and tests. Same facts, three dialects.

> **Synthetic case — Ashford Batch Plant.** Lena's placement memo used only ABP synthetic figures; real partner plant names were omitted.

In her placement memo, Lena wrote the same laptop finding three ways: for process safety, as a threat to the independence of the line controllers; for operations, as a scheduling need for updates; and for engineering, as a configuration change. Each reader got the version they needed.

### 43.4 Errors and limits

I can't tell you what I did is not a practice report — use synthetic reconstruction agreed with the host.

Lena's placement report could not include the host's real network details, so she agreed a synthetic reconstruction with her host mentor that kept the structure of the finding but replaced every identifying detail. Her constraints appendix stated what she had not been allowed to examine. This gave the university something to assess without exposing the host, and it is the standard for any placement where the work itself cannot be described directly.

### Practice note

If your placement host sells OT scanners, disclose that and still refuse empty scores. Marketing decks are not measurement.

### 43.1b Clearance and conflicts

Public-service placements may involve clearances. Course artefacts stay at the lowest sensitivity: synthetic reconstructions. Never paste restricted text into GitHub. Practice reports include a constraints appendix graded as heavily as the technical work.



Agree the sanitized reconstruction with the host mentor in writing before writing the practice report. If the host forbids even sanitized metrics, use a fully synthetic twin scenario labelled as such.

Lena's own appendix followed this rule. Lena's agreement with her host mentor was written before drafting began, and it named the figures she could use and the ones she could not.

### Field note — constraints appendix

A public-service host forbade foreign SaaS and required FOIA-ready logs. The practice report's constraints appendix explained why architecture C was impossible and why A was chosen. Graders marked the appendix as heavily as the code.



Clearance and need-to-know rules mean course artefacts stay synthetic; never paste restricted host text into public repositories.


### 43.5 Worked example — translating a placement finding (synthetic ABP)

On placement at a contract manufacturer, Lena observes that the vendor laptop used for PLC updates also browses the internet. Her sanitized report omits host names and addresses, describes the risk in plant terms — "a single laptop carries both internet exposure and the ability to download logic to the line controllers (ATT&CK for ICS T0843)" — and recommends a dedicated, offline-updated engineering laptop. The host organisation's clearance review approves the report before it reaches her university, and the constraints appendix states what she was not permitted to examine.

### Exercises

- **EX127 — Dialect.** Translate fail closed on missing policy for process safety. Rubric: 3 = safety/risk wording; 2 = partial; 1 = jargon dump; 0 = none.
- **EX128 — Sanitize.** Rewrite a sentence that leaks a real hostname. Rubric: 3 = synthetic substitute; 2 = partial; 1 = still leaks; 0 = none.
- **EX129 — Constraint.** Two public-service constraints that change architecture. Rubric: 3 = e.g. residency, procurement, FOIA; 2 = one; 1 = vague; 0 = none.

### Synthesis

Practice is real constraints plus sanitized learning artefacts.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) propose a capstone that ships a measurable CNHP improvement; (2) define scope and non-goals; (3) set a verification plan mapped to Lab I rows.

### 44.1 Proposal

Problem, users, requirements (safety first), architecture sketch, milestones, verification lab plan, ethics paragraph. Capstones that need exploit work are rejected.

Lena's Capstone I proposal was a zone-and-conduit policy compiler that reads ABP's zone model and emits firewall rules plus test vectors. Its requirements put safety first: SIS-B must stay unreachable from every routed zone. Her milestones, lab plan and ethics paragraph were reviewed before coding began. The project needed no exploit work, because its job was to prove that rules match the design, not to break into anything on the plant.

### 44.2 Non-goals

Explicitly list what you will not build (exploit modules, live plant scanning, ML risk oracles, empty scores).

Lena's non-goals were written into her proposal and signed by her supervisor: no live deployment, no configuration of SIS-B and no active scanning. When a classmate suggested adding automatic scanning to check deployed rules, she pointed to the frozen list and kept the compiler's checks working on exports instead. Writing the non-goals down early gave her a clear answer for every tempting extension during the term.

### 44.3 Milestone 1

Something demoable on synthetic data in week 3: e.g. kill-switch honored in ≤30s with a test.

> **Synthetic case — Ashford Batch Plant.** Capstone I proposals that mentioned auto-pwn were returned; signed allow-list distribution with fail-closed advanced.

Other proposals in Lena's cohort built signed allow-list distribution. Lena's own milestone 1 for the compiler met reachability for all nine of ABP's conduits but produced test vectors for only seven rules. The demo ran entirely on synthetic exports, and the gap became the opening item for milestone 2.

### 44.4 Errors and limits

Scope creep is the main killer — freeze non-goals.

During Lena's capstone, reviewers suggested adding a dashboard, live firewall pushes and support for a second plant. Each would have taken weeks and none was needed to prove the compiler matched the design. She answered each suggestion with the frozen non-goals and placed them in a future-work list instead. The two missing vectors from milestone 1 became her first milestone 2 task, so the remaining time went to finishing what she had promised. Her final scope matched the proposal.

### Practice note

Proposals that cannot name a Lab I row for each Must requirement return to draft.

### 44.1b Success metrics and checkpoints

Define two metrics you will show at defense (e.g. deny-all time, percent of merges with AUTH tickets). Capstone I has mandatory checkpoints: proposal accepted, milestone 1 demo, mid ethics check. Missing a checkpoint freezes coding until recovered.



Risk register for the capstone: scope creep, dependency delay, reviewer unavailability, ethics boundary confusion — each with early warning and mitigation. Milestone demos that skip fail-closed are graded zero for that checkpoint.

Lena's two metrics were conduit reachability and vector coverage. Both appear in her defense.

### Field note — ethics early

A proposal that included a live plant scan was rejected at the ethics checkpoint before any code was written. Mapping Must requirements to Lab I rows in the same review prevented a beautiful design that could not show fail-closed.



Advisor checkpoints are mandatory; silent drift produces unreviewable piles at the end of term.



Success metrics named in Capstone I are the same metrics shown at defense — no bait and switch.


### 44.5 Worked example — capstone milestone 1 (synthetic ABP)

Lena's capstone builds a verified zone-and-conduit policy compiler: it reads a zone model and emits firewall rules plus conformance vectors. Non-goals: no live deployment, no SIS-B configuration, no active scanning. Milestone 1 success metric: for ABP's nine-conduit model, the compiler produces rules whose reachability (checked with the Chapter 2 graph code) exactly equals the design, and every rule has at least one pass and one block vector. At the checkpoint it met reachability for 9/9 conduits but produced vectors for only 7/9 rules; the gap is the milestone 2 opening item.

### Exercises

- **EX130 — Non-goal.** Three non-goals for a coverage-board capstone. Rubric: 3 = three clear; 2 = two; 1 = one; 0 = none.
- **EX131 — Milestone.** Week-3 milestone with acceptance test. Rubric: 3 = demo + test; 2 = demo only; 1 = vague; 0 = none.
- **EX132 — Ethics.** Four-sentence ethics paragraph. Rubric: 3 = auth, synthetic, dual-use, disclosure; 2 = partial; 1 = weak; 0 = none.

### Synthesis

Ship safety-relevant programme value; freeze non-goals early.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) run a review that can reject; (2) use a checklist tied to safety requirements; (3) record dissenting opinions.

### 45.1 Review rights

Reviewers may block merge for fail-open paths, missing tests, SIS reachability regressions, or empty scores in UI. LGTM without the checklist is invalid.

At ABP, CNHP reviewers have written authority to block a merge on any of these grounds, and the plant manager has agreed not to override a block to meet a deadline. A reviewer who approves without completing the checklist has not reviewed the change, and the merge is reverted until a proper review is done. Lena keeps a record of blocks and their reasons, which showed that most blocks concerned missing tests rather than unsafe designs.

### 45.2 Checklist

Fail-closed; policy authn; schema forbids payloads; coverage has denominator; secrets redaction; rollback path documented; SIS reachability test green.

Lena's checklist at ABP has one line for each item, and each line links to the requirement it enforces, such as S-1 for fail-closed behaviour and R-12 for SIS-B reachability. The reviewer ticks a line only after seeing the evidence, such as the test that fails when policy is missing. Rollback is checked by naming the previous version and the command to restore it, and the reachability test must have run on the exact commit being merged.

### 45.3 Dissent

If one reviewer disagrees, record the dissent in the ADR even if overruled — future incidents need that trail.

> **Synthetic case — Ashford Batch Plant.** A coverage badge PR was blocked twice under this checklist; the third revision shipped the honest UI (Chapter 35).

At ABP the external reviewer's dissent about the collector sending alerts to the HMI was recorded verbatim, and in that case it changed the design. Lena keeps overruled dissents in the same place, because a later incident may prove them right.

### 45.4 Errors and limits

Reviews after merge are archaeology, not control.

At ABP a small change to the alert format was once merged before review because the deadline was close, and the review that followed found it had removed the reason code that operators relied on. The fix required a second release during a window. Since then CNHP's merge queue refuses any change without a completed checklist, and a review requested after merging is recorded as a process failure in the retrospective rather than counted as a review.

### Practice note

Reviewers run the critical tests locally on synthetic fixtures before the meeting — not only read the diff.

### 45.1b External reviewers and SLOs

Once per term, invite an engineer from outside the squad to review a safety-critical PR. Reviews complete within an agreed number of business days or the change expires from the merge queue (not auto-merges). Forbid Friday-evening merges before windows unless a safety hotfix with Lab I evidence.



Blocking comments must cite a requirement id or checklist item number. Repeated checklist skips by the same reviewer trigger a coaching conversation. The calendar is part of the control design.

ABP's external reviewer came from a water utility.

### Field note — Friday merge ban

A non-hotfix UI merge on Friday evening before a Saturday window was reverted. The calendar rule exists because tired reviewers miss fail-open paths. Heroic late merges are a smell.



External reviewers once per term catch normalized deviance such as we always skip that test.



Review SLOs prevent rubber-stamping under calendar pressure; expired merges return to draft rather than auto-merge.


### 45.5 Worked example — a dissent that changed the design (synthetic ABP)

In the independent design review, an external reviewer from a water utility challenged the plan to let the monitoring collector send alerts directly to the HMI. Her argument: an alert flood could distract operators during an upset, and a compromised collector would gain a path into L2. The review checklist item "does any security component add a conduit into a control zone?" had been ticked incorrectly. The dissent is recorded verbatim, the design changes so alerts go to the SOC and the shift lead's phone instead, and the review SLO (comments answered within five working days) is met.

### Exercises

- **EX133 — Block.** Blocking comment for a fail-open retry. Rubric: 3 = cites safety req + fix ask; 2 = vague block; 1 = nit; 0 = approve.
- **EX134 — Checklist.** Add one item for serial taps. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = none.
- **EX135 — Dissent.** One sentence of recorded dissent. Rubric: 3 = clear; 2 = hedged; 1 = none; 0 = none.

### Synthesis

Reviews that can say no, with a checklist and a memory.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) finish implementation against the frozen proposal; (2) run Verification Lab II; (3) deliver operator docs and ops ownership.

### 46.1 Freeze

Feature freeze date is real: after it, only safety fixes. New ideas go to a sequel proposal.

Lena's capstone froze at v1.0 of her compiler. After the freeze, she fixed only the silent stall in the vector loader, because it could hide a failure, and logged every new idea, such as support for a second plant, in a sequel proposal. The freeze date was agreed with her supervisor at the proposal stage, so nobody could treat it as a soft target when the last weeks became busy.

### 46.2 Verify

Capstone must pass Lab II (Chapter 40) on synthetic fixtures with signed checklist.

Lena reran Lab II for the compiler on a clean machine built from the v1.0 tag, using only synthetic fixtures. The run included all 214 unit tests, the conformance vector sets, the reachability equivalence check and the bench firewall replay. The checklist was signed by Lena and her reviewer, and the report named the tests that need bench hardware, so a later rerun without that hardware cannot quietly treat skipped tests as passes.

### 46.3 Docs

Runbook section, ADR, operator tutorial with screenshots of synthetic UI — no plant data. Ops signature required before tag.

```python
"""Lab: alarm load per operator hour before and after rationalisation (synthetic counts)."""
before = {"T-1 high": 140, "T-2 high": 95, "R-101 temp": 30, "pump trip": 6, "comm loss PLC-A": 210, "door open": 75}
remove = {"comm loss PLC-A": 200, "door open": 70, "T-1 high": 110}   # chattering/duplicate alarms removed
hours = 24 * 7
tb = sum(before.values()); ta = tb - sum(remove.values())
print(f"week alarms before={tb} after={ta}")
print(f"per operator-hour before={tb/hours:.2f} after={ta/hours:.2f}")
top = max(before, key=before.get)
print(f"worst source before: {top} ({before[top]/tb:.0%} of load)")
```

Expected output:

```text
week alarms before=556 after=176
per operator-hour before=3.31 after=1.05
worst source before: comm loss PLC-A (38% of load)
```

> **Synthetic case — Ashford Batch Plant.** One Capstone II team in Lena's cohort delivered signed allow-list distribution; Lab II green; runbook updated the same day.

That team's project was separate from Lena's capstone, the compiler. Her documentation for the compiler included the demo script, the list of non-goals and a handover note naming which tests need bench hardware, all signed by operations before tagging.

### 46.4 Errors and limits

Demo magic on a laptop with hand-waved fail-closed does not pass.

At Lena's capstone review, a classmate's demo showed a policy tool working on a laptop but could not show what happened when the policy file was missing. The examiners marked the fail-closed requirement as not met. Lena's demo deleted the policy on the bench and showed the denial with its reason code, then restored it, because claims about safe failure must be shown under failure rather than described while everything is working.

### Practice note

Silent runbook test: a second engineer follows the runbook cold on synthetic data while the author is silent. Places they stall become doc fixes.

### 46.1b Demo script and handover

Capstone II demo follows a script on synthetic data: show fail-closed, show coverage denominator, show SIS reachability. Without ops signature the release tag is not cut. Link the silent-run recording hash in the Lab II report for advisor audit.



Advisor review watches the silent-run recording and files doc issues before sign-off. Capstone code without an ops owner at merge is unfinished. Demo scripts are recorded next to the lab report.

Lena's demo followed this script exactly. Her ops owner signed at merge.

### Field note — silent run stall

The peer silent-run stalled on missing test policy key documentation. The doc fix shipped the same day. Capstone II is not done until someone who did not write the code can operate the stop path from the runbook alone.



Handover to ops names the owning squad in README and CODEOWNERS before Lab II sign-off.



Demo scripts on synthetic data are mandatory; improvised demos skip safety.


### 46.5 Worked example — freeze and verify (synthetic ABP)

At capstone II freeze, Lena tags the compiler at v1.0 and reruns all verification on a clean machine from the tag: 214 unit tests, 18 conformance vector sets, the reachability equivalence check and the bench firewall replay. One run stalled silently because the bench firewall's API rate-limited the vector loader; the fix is a timeout with an explicit failure message rather than a retry loop. Documentation includes the demo script, the list of non-goals, and a handover note naming which tests require bench hardware so a successor does not mistake skipped tests for passes.

### Exercises

- **EX136 — Freeze.** What is allowed after feature freeze? Rubric: 3 = safety fixes only; 2 = bugs; 1 = features; 0 = none.
- **EX137 — Artefacts.** Five delivery artefacts. Rubric: 3 = five; 2 = three; 1 = code only; 0 = none.
- **EX138 — Ops.** Why is ops signature required beside Lab II? Rubric: 3 = ownership/runbook readiness; 2 = vague; 1 = bureaucracy; 0 = none.

### Synthesis

Freeze, verify, document, name ops — then operate.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a scripted failure trial; (2) measure recovery time; (3) file corrective actions.

### 47.1 Script

Inject: allow-list file deleted; finding store killed; clock skew; duplicate event replay; flat graph substituted for zoned. Observe denies, queues, alerts, reachability fail.

In ABP's bench failure trial, Lena's team deleted the allow-list file while replayed traffic was running, then stopped the finding store, skewed the clock on the bench copy of PLC-A and replayed duplicate events. Finally they substituted a flat graph for the zoned one. Observers recorded whether writes were denied, whether findings queued, whether alerts fired and whether the reachability check failed on the flat graph. Each inject was run separately before any combination was attempted.

### 47.2 Measures

Time to deny-all writes after policy loss; time to alert; time to restore; findings lost (should be 0 with queue); SIS reachability check still fails closed on bad graph.

At ABP the trial measured 45 seconds to deny all writes after the allow-list was deleted, against a 30-second target. Alerts fired within the target, and no findings were lost, because drafts queued while the finding store was down. The reachability check correctly failed when the flat graph was substituted, showing SIS-B as reachable. Each measure was recorded by an observer with a stopwatch and checked against the logs, so the numbers did not rely on anyone's memory.

### 47.3 Corrective actions

Each miss becomes a ticket with owner and due date — not only a lesson-learned slide.

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

> **Synthetic case — Ashford Batch Plant.** Trial showed 45s to deny-all writes; target 30s — poll interval tightened.

At ABP the 45-second deny time became a ticket for the monitor's owner with a due date. The fix shortened the policy check interval, and the inject was rerun until it met the target twice. The ticket closed only after the second passing run, and the next trial date was booked before the observers left the room.

### 47.4 Errors and limits

Trials on production windows are forbidden; use synthetic ranges.

Lena's trials at ABP run on the bench range with synthetic traffic, never during a production window. Deleting the allow-list on the live monitor would test the same code path but could interrupt engineering writes while a batch was running on R-101. The bench copy of PLC-A and the replayed trunk traffic give the timing evidence needed. Production checks after a fix are read-only, such as confirming that the deployed version matches the one tested on the bench.

### Practice note

Celebrate tickets filed — they are the output. A trial with zero tickets usually skipped hard injects.

### 47.1b Blameless correction and recurrence

Write corrective tickets against components and runbooks, not against individuals who followed a bad procedure. After a fix, re-run the inject that found the gap. Close the ticket only when the measure meets the SLO twice. Observers rotate so nobody is permanently exempt.



Observers note timings and deviations — they do not fix things live. Schedule the next trial date before leaving the room so recurrence tests actually happen. Scoreboard photos go into the dossier.

ABP's tickets follow this rule. Nobody was blamed.

### Field note — zero-ticket smell

A trial that produced zero tickets had skipped the flat-graph inject. Re-running with the hard inject filed three tickets and tightened the SIS reachability gate. Celebrate tickets; suspect clean scoreboards.



Blameless correction writes tickets against components and runbooks, not against people who followed a bad procedure.



Recurrence tests close tickets only after the inject meets the SLO twice.


### 47.5 Worked example — recovery trial on the bench (synthetic ABP)

The trial scenario: PLC-A's logic is corrupted (simulated by loading a wrong program on the bench controller) during a batch. Measures: time to detect (program-change alert 35 s), time to decide (shift lead chooses safe hold, 4 min), time to restore verified logic from the offline backup (22 min) and time to resume (41 min total). The trial reveals that the backup's hash had never been recorded, so verification relied on a manual comparison. Corrective actions get owners and dates: record backup hashes, add a restore drill to the quarterly calendar, and track recurrence.

### Exercises

- **EX139 — Inject.** One inject and expected safe behaviour. Rubric: 3 = both; 2 = inject only; 1 = vague; 0 = unsafe.
- **EX140 — Measure.** Primary measure for policy-loss inject. Rubric: 3 = time to deny writes; 2 = vague uptime; 1 = none; 0 = none.
- **EX141 — Action.** Turn a 45s result into a corrective ticket title. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = none.

### Synthesis

Break it on purpose; measure; ticket the gaps.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble a dossier a third party can re-hash; (2) structure retention classes; (3) exclude dual-use and proprietary material.

### 48.1 Contents

Work permit PDF, ConduitSet/allow-list JSON, finding exports, evidence objects, hash manifest, tool versions, lab reports. Reader can verify without trusting your laptop.

Lena's CNHP dossier at ABP contains the signed work permit, the zone model and allow-list v1.4.2 as files, finding exports, the evidence objects, a hash manifest, tool versions and the laboratory reports. An auditor can take the dossier to a clean machine and check every hash against the manifest, without needing access to Lena's laptop or her account. The first page explains how to do this in a few steps.

### 48.2 Retention

Classes: window working (90 days), sealed evidence (agreed years), aggregate metrics (longer). Deletion jobs are tested.

At ABP, working data from each window is kept for 90 days, and sealed evidence for safety-relevant change records is kept for seven years, following the site's record schedule. Aggregate metrics, such as the alarm rate falling from 556 to 176 per week, are kept longer. Lena tests the deletion job each quarter on a copy of the store, so that expired working data is actually removed rather than assumed gone.

### 48.3 Exclusions

No payloads, no live credentials, no proprietary batch genealogy. If it cannot be shared with counsel safely, it does not belong.

> **Synthetic case — Ashford Batch Plant.** Dossier v3 re-hashed clean after a findings.json edit incident; process note included.

Lena's dossier at ABP replaces raw captures, passwords and recipe values with hashes and pointers to the controlled store. After a findings file was edited by mistake, version three was re-hashed and the process note explains how the error was found.

### 48.4 Errors and limits

Dossiers in personal cloud accounts fail residency and retention.

At ABP a contractor once copied window evidence to a personal cloud folder to work from home. The folder was outside the site's retention schedule and outside the approved data location, so the copy was deleted and the evidence restored from the sealed store. Lena's dossier now lives only in the controlled store, and the manifest records its location, so any copy elsewhere is clearly unofficial and can be identified during an audit.

### Practice note

Automate dossier builds from tags. Manual dragging of files is how findings get edited after seal.

### 48.1b Reader checklist and redaction log

Include a one-page how to verify this dossier at the top. When redacting, keep a redaction log (what, why, actor) inside the sealed store. Hand the dossier to someone outside the project for a re-hash drill. Manifest generation fails the build if any path matches a forbidden-name regex.



Third-party readability: if outsiders cannot find the manifest or the work-permit version, the dossier fails. Test restore from dossier on a clean machine once per term as a graded exercise.

Lena's dossier passes this test each term.

### Field note — automated dossier

make dossier ENG=2026-03-abp produces the zip and manifest. After automation, the findings.json post-seal edit class of incident stopped. The happy path became the safe path.



Redaction logs record what, why and actor so future readers know a blank was intentional.



Reader checklists at the front of the dossier turn verification into a graded skill, not a guided tour.



Automation makes the happy path the safe path for dossiers.


### 48.5 Worked example — what goes in, what stays out (synthetic ABP)

Lena's CNHP evidence dossier includes the zone model and its version, conformance results, laboratory reports, the validation re-test, open findings with owners and the residual-risk acceptance signed by the plant manager. It excludes raw packet captures, passwords and recipe parameters, replacing them with hashes and pointers to the controlled store; the redaction log lists each exclusion and why. Retention follows the site's record schedule: seven years for safety-relevant change records. The reader checklist on page one tells an auditor how to verify any hash against the stored originals.

### Exercises

- **EX142 — Manifest.** Sketch a hash manifest format (3 rows). Rubric: 3 = path+algo+digest; 2 = digests only; 1 = vague; 0 = none.
- **EX143 — Class.** Retention class for work permit PDF vs scratch notes. Rubric: 3 = sealed vs working/delete; 2 = partial; 1 = same forever; 0 = none.
- **EX144 — Exclude.** Student pastes a password into a finding — what do you do? Rubric: 3 = scrub, rotate, process finding; 2 = scrub only; 1 = ignore; 0 = publish.

### Synthesis

Dossiers are verifiable, classified and boringly safe.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) structure a thesis around a programme claim; (2) defend measures and limits; (3) cite SP 800-82, 62443, ATT&CK for ICS and evaluation papers correctly.

### 49.1 Claim

One sentence: what you built/measured and for whom. Example: Signed allow-list distribution with fail-closed semantics reduces unauthorized writes forwarded in synthetic trials.

Lena's own claim was about her compiler: for ABP's nine-conduit model, generated rules matched the design's reachability and caught three errors manual review missed. Her sentence names what she built, which plant model it was tested on and what it showed, so an examiner can check each part against the evidence. She rewrote it several times until every clause pointed to a specific result in the body.

### 49.2 Body

Related work, design, verification, results with intervals and attack classes, limitations, ethics.

Lena's thesis follows this order. Related work cites IEC 62443-3-2 and SP 800-82r3 for the methods she used. Design explains how the compiler turns ABP's zone model into rules. Verification shows the equivalence check and conformance vectors, results report the three errors found, limitations state that a flawed zone model would be compiled faithfully, and the ethics chapter explains why no live plant was touched. Each part points to evidence.

### 49.3 Citations

Use verified URLs/DOIs from the source policy; do not invent papers. Note access dates. Giraldo et al. CSUR 2018 doi 10.1145/3203245; Urbina et al. CCS 2016 doi 10.1145/2976749.2978388.

> **Synthetic case — Ashford Batch Plant.** Thesis draft used only synthetic trial data and cited SP 800-82 Rev. 3 correctly.

Lena checked every reference in her thesis against its DOI or official URL and recorded the access date. Each citation has a note saying how the work was used, so none is listed without being read. Her advisor checked the notes.

### 49.4 Errors and limits

A thesis that evaluates exploitation skill is out of programme scope.

Lena's thesis measures whether her compiler produces correct rules, not whether she can break into a plant. Her ethics chapter states that the work used only synthetic exports of ABP's zone model and the bench firewall, and it gives an example of a request she refused: testing generated rules against a live plant firewall. Examiners judge the engineering and evidence, so attack skill is neither demonstrated nor assessed in the defense.

### Practice note

Threats-to-validity page is graded. Examiners read that page first. Length is not rigor; structured limits are.

### 49.1b Related work honesty and reproducibility

Cite frameworks you actually used. Padding related work with unread papers is discovered in defense. Ship enough to replay synthetic trials: fixture hashes, tool SHAs, scripts. Available on request is not a reproducibility appendix. Put the claim sentence in bold on page one.



How-used notes stop citation padding cold in advisor review. The threats-to-validity page is graded; leaving it blank fails the thesis gate regardless of implementation quality. Examiners read that page first.

Lena's threats page lists the compiler's reliance on a correct zone model.

### Field note — claim on page one

Examiners and advisors share the same target when the claim sentence is bold on page one. Thin, accurate related work with how-used notes beats a padded bibliography that collapses under the first question.



Reproducibility appendices ship fixture hashes, tool SHAs and scripts — available on request is insufficient.



Related-work honesty prefers thin accurate citations with how-used notes over unread padding.


### 49.5 Worked example — a thesis claim with its evidence (synthetic ABP)

Lena's thesis claim, on page one: "For ABP's nine-conduit model, a compiler that generates firewall rules and conformance vectors from a zone model produced rules equivalent in reachability to the design and caught three rule errors that manual review missed." The body supports each clause: the equivalence check, the three errors with their vectors, and the manual review's results on the same rule set. Related work cites IEC 62443-3-2 for the zone-and-conduit method and NIST SP 800-82r3 for segmentation guidance, and states plainly that formal verification tools exist that the thesis did not compare against.

### Exercises

- **EX145 — Claim.** One-sentence thesis claim for dual-approval of conduits. Rubric: 3 = measurable+scoped; 2 = vague; 1 = exploit claim; 0 = none.
- **EX146 — Limit.** One limitation paragraph (3 sentences). Rubric: 3 = external validity clear; 2 = partial; 1 = none; 0 = overclaim.
- **EX147 — Cite.** Give the DOI for Urbina et al. CCS 2016. Rubric: 3 = 10.1145/2976749.2978388; 2 = title only; 1 = wrong; 0 = none.

### Synthesis

One claim, honest limits, real citations.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present the claim and evidence in 20 minutes; (2) answer safety and measurement questions; (3) state what you would not do again.

### 50.1 Talk structure

Claim; demo on synthetic data; verification results; one failure-trial lesson; limits; questions. No live plant hacking demo.

Lena's defense followed this order. She stated her claim about the compiler, showed it on ABP's synthetic nine-conduit model, presented the equivalence and vector results, and described the silent stall in the vector loader and how a timeout fixed it. She then named the limitation that a wrong zone model would be compiled faithfully. Nothing in the talk touched a live system, and every number on her slides pointed to an artefact in the dossier.

### 50.2 Likely questions

Fail-closed proof? Denominator choice? Dual-use boundary? SIS independence? What broke in Lab II? Practice answering with pointers to artefacts.

Lena practised each question with her supervisor, answering with a pointer to an artefact rather than an opinion. For fail-closed behaviour, she pointed to the trial results; for SIS independence, to the reachability check showing SIS-B unreachable from every routed zone. For Lab II, she described the clock-skew defect and its fix. The hardest question, what happens if the design is wrong, received the most practice of all.

### 50.3 Reflection

End with one design mistake and the fix — examiners trust engineers who saw their own failures.

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

> **Synthetic case — Ashford Batch Plant.** Lena's defense led with the fail-closed lab and SIS reachability, not a slide of logos. When asked for a risk score, she refused and showed SIS reachability, critical opens and coverage denominators.

Lena's reflection was the silent stall during the freeze rerun: her vector loader had retried forever when the bench firewall rate-limited it, so a failed run looked like a slow one.

### 50.4 Errors and limits

Defense is not a sales pitch for a scanner vendor.

Lena's defense mentioned no product names and recommended no tools. When an examiner asked which commercial scanner she would buy, she explained that her work produced rules and evidence for any firewall and that the choice of product belonged to ABP's procurement process. Her slides showed results and limitations, not logos, so examiners judged her work on its evidence rather than on any vendor's marketing. She kept that line throughout.

### Practice note

Twenty minutes means rehearsal with a timer. Cutting the limits slide to save time is the wrong cut — examiners need your honesty more than a fourth demo click.

### 50.1b Examiner packet and aftercare

Provide examiners the claim sentence, Lab II summary, failure-trial measure and ethics paragraph one day ahead. After defense, schedule a maintenance review in ninety days: owning squad, pins, corrective tickets. Archive the talk deck next to the dossier with matching hashes.



Keep a parking lot for examiner ideas and process it within a week. Thank operators who ran synthetic trials; defense without their logs is storytelling. The final chapter of the degree is the first chapter of stewardship.

Lena sent her packet a day early.

### Field note — ninety-day review

Ninety days after defense, the owning squad, pins and corrective tickets were reviewed. One corrective had reopened; it was re-filed with a tighter SLO. Stewardship begins when the applause ends.


### 50.5 Worked example — answering the hardest defence question (synthetic ABP)

An examiner asks: "Your compiler proves reachability equals the design. What if the design is wrong?" Lena's prepared answer: the compiler verifies implementation against intent, not intent against threats; the design itself came from the consequence-driven assessment and was independently reviewed (Chapter 45); and the validation re-test (Chapter 38) found a real drift the compiler would have prevented. She closes by naming the limitation — a flawed zone model would be faithfully compiled — and the ninety-day plan to compare compiler output with a second team's independent design.

### Exercises

- **EX148 — Outline.** Six-bullet talk outline. Rubric: 3 = claim to demo to verify to failure to limits to Q; 2 = partial; 1 = vendor pitch; 0 = none.
- **EX149 — Answer.** 3-4 sentences answering what's your risk score? Rubric: 3 = refuse empty score + alternatives; 2 = partial; 1 = invents score; 0 = none.
- **EX150 — Mistake.** One real (synthetic-story) mistake and fix. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = none.

### Synthesis

Defend the engineering, the measures and the refusals.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)


<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Ashford Batch Plant, Lena Okafor, CNHP and all numbers are synthetic. Any answer meeting the rubric scores equally.

**EX001.** (9 − 1.5) / 1.25 = 7.5 / 1.25 = 6.0 hours.

**EX002.** "A low-level condition on T-2 shall be alarmed to the operator within 4 hours of make-up loss (6.0 h hold-up minus 2 h response margin), by an alarm path independent of the PLC controlling the make-up pump."

**EX003.** The sine term integrates to nearly zero over a full 6-hour period, so the mean draw is 1.8 m³/h and 10/1.8 ≈ 5.56 h. If the window covered only the high part of the cycle, or the recipe were skewed toward high draw, the true time would be shorter than the average-rate estimate.

**EX004.** From A: B (direct), C and E (via B), D (via C). Reachable set {A, B, C, D, E}.

**EX005.** Removing an edge can only shrink the reachable sets, so it cannot expose anything new. Adding L3→L1-SIS can create a path from every zone that already reaches L3 — including L4 and L5 — into the safety system, so it requires a full reachability check.

**EX006.** The edge L2→L1-SIS. L4 already reaches L2 (directly via L4→L2 and via L3), so that one SCADA-to-SIS conduit completes the path; the zoned design omits it.

**EX007.** 120 × 10 = 1,200 bits; 1,200 / 19,200 = 0.0625 s = 62.5 ms.

**EX008.** Required rate = 244 × 10 bits / 0.050 s = 48,800 bit/s. The next standard rate at or above that is 57,600 bit/s; 38,400 would overrun.

**EX009.** (1) Current injection into a 4–20 mA loop → redundant sensor with cross-check. (2) Heating or cooling a temperature probe → physical-model plausibility check against heater duty. Tamper-evident enclosures and seals are also acceptable controls.

**EX010.** permit(src, fc, reg): if src == "HIST-1" and fc in {3, 4} → PASS; if src == "HIST-1" otherwise → BLOCK "fc-not-allowed". No write codes (5, 6, 15, 16) are listed.

**EX011.** Test 40001 and 40010 with HMI-1 fc=6; both PASS. 40011 is outside range(40001, 40011) and must BLOCK "register-out-of-range".

**EX012.** There is no (ENG-WS, 8) tuple in ALLOW, so it blocks with fc-not-allowed. Function 8 is diagnostics; a default-deny list forces the engineering workstation's needs to be stated and approved rather than assumed.

**EX013.** "Any host on L2 can send Modbus write requests to PLC-A holding registers 40001–40010 without authentication (observed in a bench replay, 3 March). A change to the T-1 level setpoint could raise level toward overflow in about 40 minutes; the SIS-B high-high trip remains independent and would stop the feed."

**EX014.** Operator: "Report any setpoint change you did not make on T-1." Safety engineer: "SIS-B is not reachable from office zones; confirm its trip test is current." Manager: "Removing FW-12 costs no downtime and closes the office-to-SCADA path."

**EX015.** "Vendor remote access to the engineering workstation in L3 remains a path to PLC-A; it is controlled by time-limited sessions through the DMZ jump host with operator approval, which should be audited monthly."

**EX016.** Expected frames = 500 / 0.85 ≈ 588. The ROE/comms budget must cover ~588, not 500.

**EX017.** B′ = 1.0 − 1.5 = −0.5/h, so B(t) = 40 − 0.5t = 0 at t = 80 hours, assuming constant rates.

**EX018.** 210 / 556 ≈ 0.378, about 38% of the weekly load — the worst single source.

**EX019.** With 0 events in 60 trials, a rough 95% upper bound on the rate is about 3/60 = 5% (rule of three) or a Wilson upper bound near 6%. You may say false alarms were not observed in this sample; you may not claim the rate is zero in operation.

**EX020.** CUSUM class A: det=60/60, mean_delay≈24.8 samples (after the attack starts at t=250).

**EX021.** "Neither detector fired on class B in 60 trials, so this sample cannot rank them; we need a detectable attack class or a larger design before claiming equivalence or superiority."

**EX022.** SIS engineering: change trip setpoints, modify safety logic, force safety outputs during test. HMI: change regulatory setpoints within allowed ranges, acknowledge alarms, view trends. Exact lists may vary if the split is clear.

**EX023.** The PLC and SIS may still share sensors, power, engineering workstations or a management network. A compromised engineering host can re-flash both even if production VLANs are separate. Independence needs separate controllers and controlled engineering access, not only VLAN tags.

**EX024.** Export HMI/PLC allow-lists and scan tables showing 40050 writable; or capture on a span/serial monitor during a bench replay. Do not write 40050 on the live plant to "prove" it.

**EX025.** On ingest, if any key matches (?i)payload|shell|exploit|password, reject with 400. Example: `{"title":"x","payload":"..."}`.

**EX026.** Both share fingerprint (PLC-A, unauthorized-write, 40050); upsert keeps one row and attaches both evidence hashes.

**EX027.** "Every path from L4 to L2 includes L3.5" (or: L4 has no edge to L2/L1). Exact wording may vary if testable.

**EX028.** "I can't provide a working exploit or attack procedure against a real PLC — that is dual-use and outside this course. I can help you write a finding from synthetic evidence or point you to the vendor's coordinated disclosure process."

**EX029.** Unexpected process alarm; cycle time or latency over budget; SIS fault or trip; process-safety contact calls stop; deny-listed host probed; unexplained setpoint change — any four with clear triggers.

**EX030.** Units/assets in scope; permitted methods; date/time window; impact and rate limits; named engineering and process-safety contacts; stop and resume rules. Signed by someone with authority over the units.

**EX031.** Example: serial CRC/framing needs a serial monitor on the trunk; Modbus TCP function code needs IP capture/decode on the conduit; which operator changed a setpoint needs an HMI or app audit log. Other correct triples accepted.

**EX032.** Read-only decode of Modbus TCP to PLC-A from HMI-1/HIST-1; function codes 3/4/6 only; registers 40001-40010; no writes from the assessment station; window Sat 02:00-04:00 with process-safety contact on call.

**EX033.** WRITE_REGS allows HMI-1 fc=6 only for registers in range(40001, 40011). 40003 is inside (PASS); 40050 is outside (BLOCK register-out-of-range).

**EX034.** Named engineer accounts; admin rights via checked-out time-boxed group membership; all logic downloads logged; second person approves downloads to SIS and to production PLC outside a window.

**EX035.** historian DB patch (2.5 h, risk 5) deferred — W1 took PLC-A firmware and switch firmware; W2 took HMI OS and eng-WS AV; no spare hours.

**EX036.** Vendor USB allowed on eng-WS-2 only, 14 Mar 09:00-12:00, media scanned on a stand-alone kiosk, session video-logged; port disabled afterward.

**EX037.** Use the L3 replica only. SELECT limited to tag, value, timestamp. LIMIT 10000. No dumps. Files destroyed within 24 h and confirmed in the ticket.

**EX038.** Obtain analyst credentials issued for the test; connect; attempt an UPDATE/INSERT on a setpoint annotation table; record success or permission-denied. No crafted payloads.

**EX039.** Safe: tag_id, value, quality_code, timestamp. Forbidden: operator_name, customer_order_id, recipe_secret_key.

**EX040.** Modbus allow-list abp-modbus-v1.4.2 (git SHA c0ffee1), loaded 14 March 02:05 from the signed release bucket.

**EX041.** Any PR that widens conduits (added edge/code or removed deny) needs a linked AUTH ticket and a second code owner; tightening needs one owner.

**EX042.** CI with plant VPN credentials would touch systems outside a human-authorized window, could leak secrets into logs, and would make builds depend on plant networks. Synthetic fixtures keep CI safe and repeatable.

**EX043.** Confidentiality: little direct (setpoint writes are not reads). Integrity: unauthorized change to T-1 level setpoint. Availability: batch may abort or interlock. Safety: SIS-B high-high remains independent if conduits hold — state that explicitly.

**EX044.** Vulnerability: unauthenticated Modbus write. Exposure: writable from L2 HMI network. Process risk: plant owner's judgment of overflow likelihood and consequence given SIS-B — accepted or remediated by them.

**EX045.** We don't publish a single hackability score. Here are SIS-reachability (no), critical opens (1), alarms/operator-hour (1.05), deferred high-risk patches (0).

**EX046.** "No L4 host shall have a permitted conduit to L2 SCADA servers; verify by reachability on each firewall export." "All L4 viewing of process data shall use the L3.5 historian replica; verify by absence of direct L4 to L2 rules and by replica ACL tests."

**EX047.** Artefact: zoned edge list without L2 to L1-SIS and without L4 to L2. Signal: lab_reach reports writes_to_SIS=True or L1-SIS in reach from L4.

**EX048.** Tag name/id, data type and engineering units, update or exception rate, quality-code meaning, owner — any three with clear meaning.

**EX049.** kp=0.2 ki=0.01: final≈58.15, mae≈4.62, best of the three. Pure P (ki=0) leaves larger offset (final≈44.61).

**EX050.** Prefer a passive tap or mirroring; inline DPI risk adding latency comparable to the loop's time scale. Measure on a bench copy first.

**EX051.** Page immediately for safety-relevant cyber events; batch medium events into a shift digest; suppress duplicates of the same fingerprint for 24 h.

**EX052.** Office PC in L4; historian in L3; HMI in L2; PLC-A in L1; SIS-B in L1-safety. Controls: DMZ jump for L4 viewing; no L2 to SIS edge; allow-list on Modbus — any coherent sketch with two controls.

**EX053.** Recipe data leaves the controlled OT/IT path into an uncleared personal account, breaking confidentiality and retention.

**EX054.** Testing used a synthetic range mirroring ABP configuration; results support claims about that configuration under the work permit, not about live process behaviour or production data.

**EX055.** Named or shared accounts? Local or directory? Admin group membership? Last password change? Break-glass procedure? Session recording on jump hosts?

**EX056.** Re-export from the device or restore the sealed copy; re-verify hashes; check who wrote after the seal time; open a process finding about uncontrolled edits.

**EX057.** Plant and engineering secrets are never pasted into tickets, chat or git; tickets store only a vault reference id and last-rotated timestamp.

**EX058.** Example: ICS security guidance to SP 800-82; zones/conduits/SL to 62443; technique vocabulary to ATT&CK ICS; function-code details to Modbus Application Protocol.

**EX059.** Design and operate an authorized control-network hardening programme that enforces zones and allow-lists, measures detection honestly, and never endangers process safety or exceeds the signed work permit.

**EX060.** Working PLC exploits; scanning live plants without a work permit; exporting proprietary batch genealogy into labs; disabling SIS to facilitate a test.

**EX061.** Functional: "No firewall export shall contain a path from L4 to L1-SIS; verify by reachability CI." Safety: "If policy cannot be loaded, the enforcement point shall deny new sessions and alarm within 30 s."

**EX062.** Given allow-list path configured but file missing; When any permit() call; Then result is DENY with reason policy-unavailable and an alert fires; no write frames forwarded.

**EX063.** Conflict: operators want direct L4 to L2 viewing; safety/security want no L4 to L2 edge. Chosen rule: viewing via L3.5 historian replica only; direct rule forbidden; break-glass documented separately.

**EX064.** In-place edits erase which conduits were live at time t; versioning lets a finding point at the rule set that was authorized when the observation ran.

**EX065.** Re-hash detects change; identical files collapse; tickets reference immutable bytes.

**EX066.** Reject titles matching password-assignment patterns or high-entropy secrets; reviewers still check; vault references only in evidence metadata.

**EX067.** Deploy with allow-list path pointing at an empty mount; call permit(); expect DENY policy-unavailable and an alert; no frame forwarded.

**EX068.** Every deny event stores authenticated actor id and policy version; storage is append-only; deletes require break-glass dual control.

**EX069.** Programme STRIDE protects assessment integrity and process safety; exploit modules increase dual-use harm and violate the course boundary — they are not mitigations.

**EX070.** Name: Listen-only Modbus decode. Purpose: verify allow-list decisions. Privilege: tap access, no inject. Noisy: low. Impact: latency only. Stop: cycle time >50 ms or process alarm. Artefacts: decision table, config hash, cycle-time log.

**EX071.** Actions without a signed work permit are unauthorized; legal/ethical/process-safety failure regardless of intent.

**EX072.** Updated zone diagram hash; reachability report; firewall-export hash; finding drafts or explicit none found with coverage note.

**EX073.** Signed JSON file: risk = operators forget to sign or verify. Hard-coded policy: risk = redeploys for every allow-list change, drift across devices.

**EX074.** Deny decisions on write function codes alert synchronously before forwarding so stop conditions meet the sensor goal; read allows may queue asynchronously.

**EX075.** Does it fail closed? Who can publish policy? What is the added latency on the slowest trunk?

**EX076.** Criterion: SIS state never leaves L1 without keyswitch. A high if monitors stay local; B medium if replica excludes SIS; C low if uploads include safety tags.

**EX077.** Option C rejected: process and recipe-adjacent data would leave the site residency boundary required by ABP policy and the work permit data clause.

**EX078.** When site WAN is down or cloud path is out of permit — run local allow-lists and detectors only, with manual finding entry.

**EX079.** Preventive: append-only sealed bucket with write-once IAM. Detective: scheduled re-hash job alerts on mismatch.

**EX080.** It demands dual-use skill, is non-deterministic, and can harm the process; prefer config re-read or allow-list tests.

**EX081.** (HIST-1, 16) is not in ALLOW, so BLOCK fc-not-allowed — historians must not write multiple registers.

**EX082.** permit(source, fc, register, allow_list: AllowListVersion) -> (bool, Reason). AllowListVersion pins which rules were evaluated for audit.

**EX083.** The test that asserts BLOCK register-out-of-range for HMI-1 fc=6 reg=40050.

**EX084.** Authentication secrets; raw frames that embed proprietary recipe parameters; personal operator identifiers if not needed for the decision.

**EX085.** coverage = |observed ∩ planned| / |planned|. Using all ATT&CK for ICS techniques as denominator makes coverage look tiny or motivates junk planning — plan the techniques relevant to the engagement.

**EX086.** On class A, CUSUM detects 60/60 with ~25 sample delay; band detects 0/60; both show 0/60 FA in this seed set.

**EX087.** Status stays open until a re-test ticket passes; auto-close on vendor promise is forbidden.

**EX088.** ID V-04; setup: empty allow-list mount; action: permit(any write); expected: DENY policy-unavailable + alert; evidence: log hash.

**EX089.** Halt lab, open blocker, revoke plant-window approval until fix and re-lab pass.

**EX090.** Allow-list/policy file hash, monitor build/version hash, lab result log hash.

**EX091.** Network retry can create two findings with different server ids; clients should PUT known ids.

**EX092.** {"title":"x","payload":"..."} or {"password":"..."} or {"risk_score":42} — any forbidden/unknown per policy.

**EX093.** No — renaming breaks clients; keep reason_code in v1 or ship /v2/.

**EX094.** During signed windows, deny-path success ≥ 99.5% measured by synthetic probes every minute; outages page the lead.

**EX095.** Scope and allow-list evaluation — must fail closed, never ALLOW when uncertain.

**EX096.** Stop starting new discovery methods; page the lead; keep deny/allow running; drain the queue before resuming discovery.

**EX097.** Drop file /var/lib/otmon/STOP via SSH/SSO; monitor polls every 10s; if present or unreadable, deny writes and alert.

**EX098.** Previous signed binary available; AllowListVersion unchanged or re-verified; process-safety contact notified of the rollback.

**EX099.** At 02:40 cycle time on trunk A reads 62 ms for three minutes; lead is in a noisy area with spotty radio.

**EX100.** So reviewers know which AllowListVersion authorized the decision when the event fired.

**EX101.** Consumer stores processed event_ids; duplicates are ignored or upserted without new tickets.

**EX102.** A sample event JSON for the new reason, and the expected finding-store ticket fields after consume.

**EX103.** Share of planned ATT&CK for ICS techniques observed in this window — not a residual risk or compliance score.

**EX104.** We don't ship red/amber/green risk badges; use SIS reachability, critical opens and SLA/patch deferral counts instead.

**EX105.** technique_id, name, planned (Y/N), observed (Y/N), first_seen_utc, notes.

**EX106.** bytes per cycle=244; time per cycle≈21.2 ms at 115200 with 10 bits/byte.

**EX107.** About 29 ms headroom absorbs decode spikes and retries; spending it all leaves no margin for the stop condition to be meaningful.

**EX108.** Each may send 2/s → ~6/s aggregate, triple the permit — need a shared limiter.

**EX109.** Disable temp accounts; rotate vault secrets; seal evidence hashes; export coverage/SIS-reachability metrics; confirm kill-switch clear; book retro; notify process-safety of end timestamp.

**EX110.** Open finding ids + status; last processed event_id; pending approval requests; kill-switch state — any three+.

**EX111.** historian DB patch deferred; close-out must record residual risk and the scheduled next window date (not deferred forever).

**EX112.** Export current firewall rules; run reachability from L4; expect L2/L1-SIS not improperly reachable; store hashes; do not send traffic into the plant to prove it.

**EX113.** Otherwise metrics lie and boards look green while risk remains.

**EX114.** Re-test confirmed the bench/twin configuration only; plant runtime was out of scope for validation.

**EX115.** Pin exact version for the window; emergency patches need a mini verification lab (Chapter 30) before swap.

**EX116.** put_evidence(key: Hash, body: bytes) -> None / get_evidence(key) -> bytes.

**EX117.** Owner: CNHP Platform squad (primary Lena Okafor); backup: on-call OT eng; contact: #cnhp-monitors.

**EX118.** Otherwise coverage claims observed techniques without a durable finding record — metric lies under partial failure.

**EX119.** Continues allow/deny from local policy; queues drafts; alerts on queue growth; never ALLOW on policy errors.

**EX120.** Implementer of the change and a second engineer who did not write the code.

**EX121.** Skipping register-range checks for previously allowed HMIs, or failing open when the policy service is slow.

**EX122.** Cache key includes policy version, source, fc, and register; short TTL; hard invalidate on policy publish.

**EX123.** Shed discovery and best-effort analytics before shedding deny evaluation — operators can wait for a scan; they cannot wait for a deny that never comes.

**EX124.** Does requiring a denominator in coverage reports reduce executive over-claims of percent secure in post-window surveys?

**EX125.** Count of conduit-widening merges without AUTH ticket per quarter (or blocked attempts).

**EX126.** That project crosses the course dual-use line; consider studying fail-closed rates or re-test policies instead.

**EX127.** If the authorization rules file cannot be loaded, the system refuses to forward write traffic and alarms staff — it does not continue under uncertainty that could affect a protection layer.

**EX128.** Host plc-a-prod-03 becomes synthetic host PLC-A in the Ashford lab range.

**EX129.** Data residency; procurement bans on foreign SaaS; retention/FOIA logging; change advisory boards — any two concrete.

**EX130.** No residual-risk badge; no live ATT&CK auto-discovery on plant nets; no storage of payloads.

**EX131.** Kill-switch file stops write forwards within 30s — acceptance: unit+lab V-KS green on synthetic.

**EX132.** Work uses synthetic data under course work permits. No unauthorized plant access. No exploit development. Accidental live issues go to responsible disclosure, not the report appendix.

**EX133.** Blocking: on policy-service timeout this retries then ALLOW — violates S-1 fail-closed. Change to DENY+alert before merge.

**EX134.** Serial: confirms listen-only mode and cycle-time stop condition are tested in Lab I.

**EX135.** Dissent: I still prefer sync alerts for all denies during the first week of a new allow-list; overruled in ADR-019.

**EX136.** Safety/blocker fixes and doc corrections; no feature work.

**EX137.** Code+tests, Lab II report with hashes, ADR, runbook update, operator tutorial, ethics statement — any five.

**EX138.** Without an ops owner and a runnable runbook, Lab II green still leaves the plant without someone who can stop and resume safely.

**EX139.** Inject: delete allow-list file. Expect: DENY writes within 30s, alert, no ALLOW.

**EX140.** Seconds from inject to first deny-all-writes decision (and alert fired).

**EX141.** Tighten otmon policy poll from 15s to 5s — trial deny-all was 45s > 30s SLO.

**EX142.** work-permit.pdf sha256 18d7…; allow-list.json sha256 01cc…; findings.json sha256 7f5f….

**EX143.** Work permit PDF to sealed evidence; scratch notes to working, delete at 90 days or sooner.

**EX144.** Remove from store, rotate the exposed secret, open a process finding, re-seal manifest, notify owner.

**EX145.** Requiring dual approval and an AUTH ticket for conduit-widening merges reduced unapproved widen attempts to zero in 12 weeks of ABP synthetic CI data.

**EX146.** Trials used synthetic fixtures, not live plant traffic. Results may not transfer to organizations without CODEOWNERS. We did not measure reviewer fatigue.

**EX147.** https://doi.org/10.1145/2976749.2978388

**EX148.** Claim; synthetic demo; Lab II results; failure-trial lesson; limits/ethics; questions.

**EX149.** I don't produce a single residual-risk score — it isn't reproducible. Here are SIS reachable from L4 (no), critical opens, and planned-technique coverage with denominators; those are what we track.

**EX150.** Example: We cached allow decisions without policy version in the key; a publish left stale ALLOWs. Fix: include AllowListVersion in the cache key and hard-invalidate on publish.

<a id="references"></a>

## References

Links checked 12 October 2026; frameworks change, so re-verify.

- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series overview. <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS. <https://attack.mitre.org/matrices/ics/>
- Modbus Application Protocol V1.1b3. <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
- NIST SP 800-82 Rev. 3. Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
- Urbina, D. I., et al. (2016). Limiting the Impact of Stealthy Attacks on Industrial Control Systems. ACM CCS. <https://doi.org/10.1145/2976749.2978388>
