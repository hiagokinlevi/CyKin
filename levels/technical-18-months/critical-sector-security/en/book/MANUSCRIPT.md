# Critical Infrastructure and Sector Security: Hands-on Technical Practice

- Language: English (`en`); technical course, eighteen months; approximately 1,200 hours of planned study (course 069 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–18 of 18 have authored teaching text, fifteen offline labs, exercises EX001–EX072 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: technical operators — network and systems technicians, SCADA and telemetry technicians, junior security analysts in operations centres — who already know networks, operating systems and basic scripting and now work on systems that move water, power or patients' air. Entry knowledge: networks, operating systems, scripting and safe lab practice.
- How this course differs from its neighbours. The [technologist book](../../../../technologist-3-years/critical-sector-security/en/book/MANUSCRIPT.md) teaches implementers to build, operate and hand over a whole monitored service. The [professional](../../../../professional-6-months/critical-sector-security/en/book/MANUSCRIPT.md) and [rapid](../../../../rapid-1-month/critical-sector-security/en/book/MANUSCRIPT.md) courses address managerial decisions and a first introduction. **This technical book is about hands-on technical depth**: opening the packets of industrial protocols, auditing and hardening hosts, configuring and verifying conduit firewalls, detecting failure modes and unauthorized commands, troubleshooting by eliminating hypotheses, and producing evidence that another technician can check. Every chapter asks: *what exactly would you type, read, change or test, and how would you prove it?*
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights and are not relicensed here.
- Educational boundary: this course is an independent educational blueprint. It is not an accredited programme, grants no qualification and grants no authority to access, scan, test or change any real infrastructure, operator, device, dataset or person. Every organization, place, person, address, record, frame, value and numerical result in a worked example or lab is **synthetic** unless a sentence explicitly cites a public source. IP addresses come from private ranges ([RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) or documentation ranges ([RFC 5737](https://www.rfc-editor.org/rfc/rfc5737)). Nothing in this book is an operational procedure for a real utility, hospital or grid, and nothing in it is legal, clinical or regulatory advice.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

The eighteen chapters follow one technical officer through eighteen months at a regional operations centre. The course outcome is practical: **diagnose failures, configure controls and verify outcomes** in critical infrastructure, in a reproducible lab and under supervision.

- **Stage 1 (Chapters 1–6)** covers service architecture and poll budgets, Modbus/TCP decoding, host and account auditing, strict data parsing, technical scope and evidence, and the zone-and-conduit system model.
- **Stage 2 (Chapters 7–12)** covers telemetry and time, failure modes, tools and DNP3 link-layer checking, firewall configuration, verification by traceable tests, and the first contained laboratory (a Modbus responder with a write policy).
- **Stage 3 (Chapters 13–18)** covers hypothesis-driven troubleshooting, drift-detection automation, dependency analysis, technical documentation and safety, the second contained laboratory (a detection pipeline) and a supervised project with a sealed evidence package.

Every chapter has learning outcomes, teaching sections with definitions, a worked example, a practical activity, common errors and limits, four numbered exercises and a synthesis. Fifteen chapters contain a Python lab. Labs use the Python 3 standard library only (outputs in this draft were produced with Python 3.13.5); they need no network, packages, privileges or real data, and every output is printed in the text so you can check your run. Lab 12 uses `socket.socketpair()`, which connects two sockets inside one process and cannot reach any network. Labs that write files do so only inside a temporary directory they create and remove. Write your answer to each exercise before opening the [worked results](#worked-results); the 0–3 rubric shows what an assessor rewards, and a different defensible answer can earn full credit.

Keep four labels in every working note: **observed** (what a named tool or person recorded, with UTC time and source), **inferred** (what you conclude and why), **done** (what you changed, under which change record) and **open** (what is still unknown, and who owns it).

### The synthetic setting used in this book

| Synthetic element | Role in the book | Boundary |
|---|---|---|
| **Kestrel Vale** — a fictional region | Setting for all examples. | Invented place. |
| **Kestrel Vale Regional Operations Centre (KVROC)** | Runs supervisory systems for three operators. The reader is a **technical officer**; L. Ferreira is the security lead; J. Tan and R. Kaur are colleagues. | Invented; no real organization or person. |
| **Kestrel Water** — stations KW-01 to KW-12 (RTUs at 10.10.*n*.2), A. Mensah operations manager | Main source of Modbus/TCP examples. | Invented. |
| **Kestrel Grid** substation **SS-3** (DNP3 outstation address 10; master address 1; front end fep-01) | DNP3 examples. | Invented. |
| **Kestrel General Hospital** building-management system | Healthcare dependency examples. | Invented. |
| Hosts scada-01, eng-ws-15, hmi-02, hist-02, jump-01, fw-01, ntp-ops, ad-ops, esx-02/03 and every frame, log line, value and time | Context for labs and exercises. | Invented. |

Because the data are synthetic, the book can tell you what a real technician rarely knows for certain. Use that to learn how checks fail, never as evidence about real organizations.

### Source policy

Every factual statement about a protocol, standard, public incident or published guidance links to a source consulted in October 2026. Standards and guidance change: re-verify each before relying on it. Ordinary professional vocabulary is not given an invented reference. A citation supports the general claim beside it, never the synthetic details. Public incidents are described only at the level their publishers released, and never as technique.

### Safety rules for practical work

1. Practise only on the book's labs, equipment you own, or systems whose owner has given you **written, specific** permission naming systems, actions and window (Chapter 5).
2. Never connect a scanner, test laptop or script to a live control network without that permission and the agreement of the people responsible for the physical process. In operational technology a read can be an action.
3. Never touch protection or safety systems as part of security work (Chapter 16).
4. If you notice a weakness in a real system, stop, record what you saw, and report it privately to its owner or through coordinated disclosure. Do not "confirm" it.
5. Keep secrets out of notes, tickets and screenshots.

## Contents

1. [Computing and service architecture](#ch-01) — layers, three paths and the poll-cycle budget.
2. [Networks and protocols](#ch-02) — unauthenticated industrial protocols and Modbus/TCP decoding.
3. [Operating systems and identities](#ch-03) — effective SSH configuration, UIDs, service accounts and groups.
4. [Scripting and data formats](#ch-04) — strict CSV/JSON parsing, validation order and record coordinates.
5. [Security scope and evidence](#ch-05) — technical scope, passive first, verifiable evidence.
6. [Critical infrastructure and sector security: system model](#ch-06) — zones, conduits and sector differences.
7. [Critical infrastructure and sector security: data and telemetry](#ch-07) — syslog, clocks and UTC timelines.
8. [Critical infrastructure and sector security: failure modes](#ch-08) — gaps, stuck values, spikes and explainable rules.
9. [Critical infrastructure and sector security: tools and methods](#ch-09) — method choice, tool validation and the DNP3 CRC.
10. [Critical infrastructure and sector security: control configuration](#ch-10) — first-match policies, shadowing and supplier access.
11. [Critical infrastructure and sector security: verification](#ch-11) — traceable positive and negative tests.
12. [Contained laboratory I](#ch-12) — a Modbus responder with a write policy and exception responses.
13. [Critical infrastructure and sector security: troubleshooting](#ch-13) — hypotheses, predictions, elimination and escalation.
14. [Critical infrastructure and sector security: automation](#ch-14) — hash-based drift detection and safe automation.
15. [Critical infrastructure and sector security: integration and dependencies](#ch-15) — dependency graphs and boundary integration points.
16. [Technical documentation and safety](#ch-16) — executable documents, safety authority and transient devices.
17. [Contained laboratory II](#ch-17) — an integrated, self-monitoring detection pipeline.
18. [Supervised technical project](#ch-18) — project phases and a sealed evidence package.

Appendices: [Worked results and assessment notes](#worked-results) · [Glossary](#glossary) · [References](#references).

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes and connection

After this chapter you should be able to:

- draw the technical architecture of a supervisory control service — field devices, communication links, front-end and SCADA servers, historian, HMI, engineering workstation, management plane — and say which component does what;
- distinguish the **control path**, the **monitoring path** and the **management path**, and explain why a technician protects each differently;
- calculate a **poll-cycle budget** and use it to predict what a slow or dead link does to the freshness of operator data;
- identify the shared platform components (virtualization hosts, directory, time, storage) whose failure crosses service boundaries.

This is the first chapter of a hands-on course. Everything later — protocol decoding, hardening, detection, troubleshooting — assumes you can point at a box on the diagram and say what traffic it sends, what it stores and what breaks if it stops. The entry knowledge (networks, operating systems, scripting) is assumed; the new element is the physical process at the other end of the wire.

### 1.1 The layers of a supervisory control service

Most critical-sector services that move water, power, air or people share a recognizable layered shape. NIST's guide to operational technology describes the same components in general terms ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); the names below are the ones used in this book.

- **Field devices**: sensors (level, flow, chlorine, pressure, temperature, current), actuators (pumps, valves, breakers) and the controllers that connect them — **PLCs** (programmable logic controllers) running local logic and **RTUs** (remote terminal units) built for remote sites with limited communications.
- **Communication links**: fibre, licensed radio, cellular routers, leased lines or an operator's MPLS network. Their latency, loss and cost shape everything above them.
- **Front-end processor (FEP) or SCADA server**: polls field devices, applies scaling and alarms, and keeps the current state of the process.
- **Historian**: stores time series for reporting, investigation and regulatory records.
- **HMI** (human–machine interface): the operator's screens, from which commands such as "start pump 2" are issued.
- **Engineering workstation**: holds controller projects and the vendor tools that change controller logic; the single most powerful computer in the system.
- **Management plane**: jump hosts, directory services, time servers, backup, virtualization management and the monitoring collector.

### 1.2 Three paths, three protection problems

A technician should be able to trace three different paths on the diagram.

The **control path** carries commands to the process: HMI → SCADA server → link → controller → actuator. Integrity and availability of this path are what keep people safe; an unauthorized or corrupted write here is the worst case in this book.

The **monitoring path** carries measurements back: sensor → controller → link → SCADA server → historian and HMI. If it is wrong, operators act on false information — a failure that can be as dangerous as a bad command, and harder to notice.

The **management path** changes the system itself: an engineer downloading new logic, an administrator patching the historian, a vendor connecting to diagnose a fault. It is used rarely but holds the most privilege, and it is where most real intrusions into control environments have been reported to begin; CISA's alert on the December 2015 attacks on Ukrainian distribution companies describes remote access and credential use preceding the operational impact ([CISA IR-ALERT-H-16-056-01](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01)).

The three paths often share cables, switches and servers. Drawing them separately is how you discover that a "monitoring" laptop on the control-centre switch can also reach controller programming ports.

### 1.3 Polling and freshness

Most station protocols in this book are **request–response**: the SCADA server asks, the device answers. The time to refresh every station once is the **poll cycle**. For each station it is roughly *polls per cycle × (link round-trip time + device turnaround time)*. If the server polls stations one after another on a single channel, the cycle is the **sum** over stations; if it has an independent channel per station, the cycle is set by the **slowest** station.

Two consequences matter for security work. First, a slow link (a congested cellular router, a degraded radio path) stretches the cycle for everyone polled after it. Second, a device that does not answer costs the full **timeout** on every poll, so one dead station can stretch the cycle more than a slow one. Freshness requirements — "every station refreshed at least every 5 s" — therefore depend on timeouts and retry counts as well as link speed, and a security control that adds latency (a VPN, an inspection proxy) must be checked against this budget before it goes in.

### 1.4 Shared platforms

Modern control centres run their SCADA servers, historians and directory on virtualization hosts, often shared between services. A shared hypervisor, directory, time source or storage array is a point where a fault in one sector becomes a fault in several. Lab 15 in Chapter 15 traces these dependencies with code; here, simply learn to mark every shared component on the diagram with the services that depend on it.

At KVROC the host esx-02 runs the SCADA server, the historian and the hospital BMS server, so its outage or a bad patch can affect water and healthcare monitoring together. Mark each shared component with every service that depends on it, and ask who owns the host when those services disagree about a change window.

### 1.5 Worked example: the Kestrel Vale operations centre (synthetic)

You are a technical officer at the **Kestrel Vale Regional Operations Centre (KVROC)**, which runs supervisory systems for **Kestrel Water** (12 stations, KW-01 to KW-12), monitoring of building-management systems for **Kestrel General Hospital**, and the telecontrol front end for one substation (**SS-3**) of **Kestrel Grid**. Station RTUs sit in 10.10.0.0/16 (KW-*n* is 10.10.*n*.2); the control centre is 10.20.0.0/24 (SCADA server `scada-01` 10.20.0.10, engineering workstation `eng-ws-15` 10.20.0.15, historian `hist-02` 10.20.0.21); corporate desks are 10.30.0.0/16; the management network is 10.90.0.0/24 (jump host `jump-01` 10.90.0.20). All names and addresses are fictional.

Operations require every station refreshed within 5 seconds. `scada-01` polls all twelve stations on one channel. Lab 1 computes the budget.

**Lab 1** (save as `lab01.py`, run with `python3 lab01.py`):

```python
# Lab 1 - poll-cycle budget for a SCADA server polling stations (offline, standard library only)
# Synthetic Kestrel Water figures. Each poll = request + response over the link plus device turnaround.
stations = {  # name: (link, round-trip ms on the link, device turnaround ms, polls per cycle)
 "KW-01": ("fibre", 4, 20, 3), "KW-02": ("fibre", 4, 20, 3), "KW-03": ("fibre", 5, 25, 3),
 "KW-04": ("cellular", 180, 40, 4), "KW-05": ("cellular", 210, 40, 4), "KW-06": ("cellular", 650, 40, 4),
 "KW-07": ("radio", 420, 60, 3), "KW-08": ("radio", 460, 60, 3), "KW-09": ("cellular", 190, 40, 4),
 "KW-10": ("fibre", 4, 20, 3), "KW-11": ("radio", 440, 60, 3), "KW-12": ("cellular", 200, 40, 4),
}
REQUIRED_S = 5.0          # operations require every station refreshed at least every 5 s
TIMEOUT_MS = 1500         # a poll that gets no reply costs the full timeout
def cycle(stations, sequential=True, dead=()):
    per = {}
    for n, (link, rtt, turn, polls) in stations.items():
        per[n] = polls * (TIMEOUT_MS if n in dead else rtt + turn)
    return (sum(per.values()) if sequential else max(per.values())) / 1000, per
c, per = cycle(stations)
print(f"sequential cycle {c:.2f} s (requirement {REQUIRED_S} s) -> {'OK' if c <= REQUIRED_S else 'FAILS'}")
worst = max(per, key=per.get); print(f"slowest station {worst}: {per[worst] / 1000:.2f} s per cycle")
c2, _ = cycle(stations, dead={"KW-06"})
print(f"sequential with KW-06 not answering: {c2:.2f} s")
c3, _ = cycle(stations, sequential=False, dead={"KW-06"})
print(f"one polling channel per station, KW-06 dead: {c3:.2f} s")
```

Expected output (Python 3.13.5):

```text
sequential cycle 11.33 s (requirement 5.0 s) -> FAILS
slowest station KW-06: 2.76 s per cycle
sequential with KW-06 not answering: 14.57 s
one polling channel per station, KW-06 dead: 6.00 s
```

The result says the requirement is already failed (11.33 s), mostly because of cellular and radio stations, with KW-06 the slowest. A dead KW-06 adds a further 3.24 s because every unanswered poll costs 1.5 s. Even with a channel per station the cycle is 6.00 s while KW-06 is dead: per-station channels remove the *sum* problem but not the *timeout* problem. A technician who is asked to "add an encrypted tunnel to the cellular stations" now knows the question to ask first: how many milliseconds does it add per poll, and what does that do to an already failing cycle?

### 1.6 Practical activity: draw your own three-path diagram

Using the KVROC description, draw the control, monitoring and management paths in three colours. Mark every component that appears on more than one path, and every shared platform component. Keep the drawing: Chapters 6, 10 and 15 refine it.

Use three colours or three page layers so that a shared switch or jump host stands out. Then check whether eng-ws-15 appears on both the management path and the control path: if it does, a compromise of that workstation reaches every station. Keep the drawing with Lab 1's budget, because a later tunnel or encryption proposal has to be judged against both the paths and the poll cycle.

### 1.7 Common errors and limits

- Drawing only the network and forgetting the management path, which is where privilege lives.
- Treating the historian as "just IT"; it is often the bridge between control and corporate networks.
- Measuring link speed but not timeouts and retries; dead devices dominate poll cycles.
- Assuming a parallel architecture fixes freshness; it changes the arithmetic, not the timeout.
- Lab 1's model ignores retries, serial-line contention and protocol overhead; treat its numbers as a first estimate, then measure.

- Forgetting that a dead station costs the full timeout on every poll, so one non-answering RTU can stretch the cycle more than a slow one.
- Drawing the control and monitoring paths and leaving out the jump host, directory and time server.
- Treating Lab 1's numbers as measured values rather than a first estimate that still needs retries and protocol overhead checked on site.

### Exercises — chapter 1

**EX001 — Path classification.** *Objective:* separate the three paths. *Inputs:* these flows: HMI → scada-01 "start pump 2"; KW-04 RTU → scada-01 level reading; eng-ws-15 → KW-04 project download; jump-01 → hist-02 SSH; hist-02 → corporate report server CSV export. *Steps:* classify each as control, monitoring or management (or a combination) and state the worst consequence if an unauthorized party could alter it. *Expected evidence:* a five-row table. *Rubric:* 3 = correct classes with the project download recognized as the most dangerous management action and the CSV export recognized as a cross-zone monitoring flow; 2 = one misclassification; 1 = classes without consequences; 0 = none.

**EX002 — Fix the cycle on paper.** *Objective:* use the poll-cycle model. *Inputs:* Lab 1. *Steps:* propose two changes that bring the sequential cycle under 5 s with all stations healthy, and say which also limits the effect of one dead station. Change the lab to test them. *Expected evidence:* modified parameters and the new printed cycle times. *Rubric:* 3 = changes are realistic (separate channels for slow link types, fewer polls per cycle for slow stations, a shorter timeout with a justified retry policy) and verified by running the lab; 2 = correct but unverified; 1 = "buy faster links" only; 0 = none.

**EX003 — Tunnel impact.** *Objective:* check a security control against an operational budget. *Inputs:* a proposed encrypted tunnel adds 35 ms to each round trip on the five cellular stations. *Steps:* compute the effect on the sequential cycle and on the per-station-channel design. *Expected evidence:* arithmetic and a recommendation. *Rubric:* 3 = correct increases (5 stations × 4 polls × 35 ms = 0.70 s sequential; 0.14 s on the slowest cellular station's own cycle) and a recommendation that ties the tunnel to the channel redesign; 2 = arithmetic right, weak recommendation; 1 = qualitative only; 0 = none.

**EX004 — Shared platform list.** *Objective:* find cross-service dependencies. *Inputs:* the KVROC description and your diagram. *Steps:* list four components likely to be shared by water, hospital and grid services and, for each, the first question you would ask its owner. *Expected evidence:* four rows. *Rubric:* 3 = for example virtualization hosts, directory, time source and monitoring collector, each with a specific question (capacity headroom, administrative group, time source redundancy, behaviour when full); 2 = generic questions; 1 = components only; 0 = none.

### Chapter synthesis

A critical-sector service is a set of layers joined by three paths. Commands, measurements and changes travel different routes and fail in different ways; the management path holds the most privilege. Request–response polling makes freshness a matter of arithmetic, and timeouts, not bandwidth, usually decide it. Every later chapter adds a technique to one of these paths, so keep the diagram and the budget at hand.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes and connection

After this chapter you should be able to:

- explain why most industrial protocols carry no authentication, and what that means for whoever can reach a controller's port;
- decode a Modbus/TCP frame by hand and in code: MBAP header, unit identifier, function code, address and quantity;
- tell read functions from write functions and recognize diagnostic and identification functions that deserve review;
- turn a decoder into a first detection: writes from any host other than the authorized engineering source.

Chapter 1 drew the paths. This chapter opens the packets on the control and monitoring paths so that later chapters can filter, verify and detect them.

### 2.1 Industrial protocols and trust

Protocols such as Modbus and DNP3 were designed for closed serial networks where anything on the wire was assumed to belong there. Their TCP/IP versions kept that assumption: a classic Modbus/TCP device accepts a valid write from **any** host that can open a TCP connection to port 502. Secure variants exist — the Modbus Organization publishes a Modbus/TCP Security specification using TLS ([Modbus specifications](https://www.modbus.org/modbus-specifications)), and DNP3 has Secure Authentication ([DNP Users Group overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol)) — but installed devices often do not support them. Until they do, **reachability is authorization**, and the network controls of Chapters 10 and 11 are the main defence.

### 2.2 The Modbus data model

A Modbus device exposes four tables: **coils** (single-bit read/write), **discrete inputs** (single-bit read-only), **input registers** (16-bit read-only) and **holding registers** (16-bit read/write). What a register *means* — level in centimetres, a pump setpoint, a mode flag — is defined by the device's configuration and documented in a **register map**. The protocol itself carries numbers, not meanings, so a decoder can tell you "write to holding register 7" but only the register map tells you that register 7 is the pump-2 setpoint.

Common public function codes are 1 (read coils), 2 (read discrete inputs), 3 (read holding registers), 4 (read input registers), 5 (write single coil), 6 (write single register), 15 (write multiple coils), 16 (write multiple registers), 8 (diagnostics) and 43/14 (read device identification). Function codes are defined in the Modbus Application Protocol specification published by the Modbus Organization ([Modbus specifications](https://www.modbus.org/modbus-specifications)).

### 2.3 The MBAP header

On TCP each Modbus request starts with a 7-byte **MBAP header** followed by the protocol data unit:

| Bytes | Field | Notes |
|---|---|---|
| 0–1 | Transaction identifier | Pairs a response with its request. |
| 2–3 | Protocol identifier | Always 0 for Modbus. |
| 4–5 | Length | Number of bytes that **follow** this field (unit id + PDU). |
| 6 | Unit identifier | Addresses a device behind a gateway; often 1 or 255. |
| 7 | Function code | What to do. |
| 8– | Data | For codes 1–6: a 2-byte address and a 2-byte quantity or value. |

All multi-byte fields are big-endian. Python's `struct` module decodes them with the format `>HHHBB` ([Python struct](https://docs.python.org/3/library/struct.html)). The frame `00 03 00 00 00 06 01 06 00 07 01 2c` therefore reads: transaction 3, protocol 0, six bytes follow, unit 1, function 6 (write single register), register 7, value 0x012C = 300.

Two consistency checks catch most malformed or non-Modbus traffic on port 502: the protocol identifier must be 0, and the length field must equal the number of bytes after it. A detection tool that skips these checks will misread garbage as commands.

### 2.4 Worked example: a capture from KW-04 (synthetic)

A technician exported eight requests sent to the KW-04 RTU (10.10.4.2) during a maintenance morning. KVROC policy says only the engineering workstation `eng-ws-15` (10.20.0.15) may write to station controllers; `scada-01` (10.20.0.10) only reads.

**Lab 2** (save as `lab02.py`, run with `python3 lab02.py`):

```python
# Lab 2 - decode Modbus/TCP frames and flag writes (offline, standard library only)
# Synthetic capture from Kestrel Water station KW-04; addresses are private (RFC 1918).
import struct
ENGINEERING = {"10.20.0.15"}          # only the engineering workstation may write
WRITE_FC = {5: "write single coil", 6: "write single register",
            15: "write multiple coils", 16: "write multiple registers"}
READ_FC = {1: "read coils", 2: "read discrete inputs", 3: "read holding registers", 4: "read input registers"}
capture = [  # (source, destination, frame as hex)
    ("10.20.0.10", "10.10.4.2", "000100000006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000200000006010400100002"),
    ("10.20.0.15", "10.10.4.2", "00030000000601060007012c"),
    ("10.30.3.7",  "10.10.4.2", "000400000006010500a0ff00"),
    ("10.30.3.7",  "10.10.4.2", "00050000000b011000070002040064000a"),
    ("10.20.0.10", "10.10.4.2", "0006000000060103"),
    ("10.20.0.10", "10.10.4.2", "000700010006010300000004"),
    ("10.20.0.10", "10.10.4.2", "000800000006012b0e010000"),
]
def decode(hexframe):
    b = bytes.fromhex(hexframe)
    if len(b) < 8: return None, "short frame (< 8 bytes)"
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", b[:8])
    if pid != 0: return None, f"protocol id {pid} is not 0 (not Modbus)"
    if length != len(b) - 6: return None, f"length field {length} but {len(b) - 6} bytes follow"
    addr, qty = struct.unpack(">HH", b[8:12]) if len(b) >= 12 else (None, None)
    return (tid, unit, fc, addr, qty), None
for src, dst, h in capture:
    d, err = decode(h)
    if err: print(f"{src:<11} -> {dst}  MALFORMED  {err}"); continue
    tid, unit, fc, addr, qty = d
    if fc in WRITE_FC:
        verdict = "ok (engineering)" if src in ENGINEERING else "ALERT unauthorized write"
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {WRITE_FC[fc]:<24} addr={addr} value/qty={qty}  {verdict}")
    elif fc in READ_FC:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {READ_FC[fc]:<24} addr={addr} qty={qty}  ok")
    else:
        print(f"{src:<11} -> {dst}  tid={tid} unit={unit} fc={fc:<2} {'other function':<24}  REVIEW (not on read/write list)")
```

Expected output (Python 3.13.5):

```text
10.20.0.10  -> 10.10.4.2  tid=1 unit=1 fc=3  read holding registers   addr=0 qty=4  ok
10.20.0.10  -> 10.10.4.2  tid=2 unit=1 fc=4  read input registers     addr=16 qty=2  ok
10.20.0.15  -> 10.10.4.2  tid=3 unit=1 fc=6  write single register    addr=7 value/qty=300  ok (engineering)
10.30.3.7   -> 10.10.4.2  tid=4 unit=1 fc=5  write single coil        addr=160 value/qty=65280  ALERT unauthorized write
10.30.3.7   -> 10.10.4.2  tid=5 unit=1 fc=16 write multiple registers addr=7 value/qty=2  ALERT unauthorized write
10.20.0.10  -> 10.10.4.2  MALFORMED  length field 6 but 2 bytes follow
10.20.0.10  -> 10.10.4.2  MALFORMED  protocol id 1 is not 0 (not Modbus)
10.20.0.10  -> 10.10.4.2  tid=8 unit=1 fc=43 other function            REVIEW (not on read/write list)
```

Reading the output line by line: the SCADA reads are normal; the engineering workstation wrote the value 300 to register 7 — expected if there is a change ticket; a corporate desk (10.30.3.7) wrote coil 160 to ON (0xFF00 = 65280) and then wrote two registers starting at 7. Those two lines are the finding of the morning: a host in the corporate zone can reach a station controller and change it. Two frames are malformed — one truncated, one with a non-zero protocol identifier — and function 43 (device identification) is neither a read of process data nor a write, so it is marked for review: an identification query from a known SCADA server may be a vendor feature; the same query from an unknown host is classic reconnaissance (MITRE lists remote system information discovery among ICS techniques: [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)).

### 2.5 Practical activity

Decode the three frames below by hand, then add them to Lab 2 and confirm: `000900000006010100000010`, `000a0000000601050003 0000` (remove the space), `000b00000006020300640001`. Write down the function, address and quantity or value of each, and whether the unit identifier is what you expect for KW-04.

Write the function, address and quantity or value for each frame, and whether the unit identifier matches what KW-04 uses. Then add the frames to Lab 2 and confirm that your hand decode matches the script. If a frame has a space in the hex, remove it before pasting; spaces are not part of the capture.

### 2.6 Common errors and limits

- Treating port 502 traffic as Modbus without checking the protocol identifier and length.
- Reading register numbers as meanings without the device's register map.
- Alerting on every function-43 query, or on none; context (source, frequency) decides.
- Forgetting that responses matter too: an exception response (function code + 0x80) tells you a request was refused (Chapter 12).
- A decoder that sees only what the capture point sees: traffic between two devices on the same station switch never reaches a control-centre sensor.

- Alerting on every write without checking whether the source is the engineering workstation named in policy.
- Treating a malformed frame as an attack when it may be a truncated export or a non-Modbus probe; report it as malformed first.
- Assuming a decoder at the control centre sees traffic between two devices on the same station switch.

### Exercises — chapter 2

**EX005 — Hand decode.** *Objective:* read MBAP and PDU fields without code. *Inputs:* `0010000000060110000a0002` is truncated; `001100000006010f00000008`. *Steps:* decode each field you can and state whether each frame is valid. *Expected evidence:* field tables with reasoning. *Rubric:* 3 = recognizes the first as function 16 missing its byte count and values (length 6 is consistent with what is present but a valid fc 16 needs more), the second as function 15 at address 0 for 8 coils, also incomplete without byte count and data; 2 = fields right, validity missed; 1 = partial; 0 = none.

**EX006 — Extend the decoder.** *Objective:* improve a detection tool. *Inputs:* Lab 2. *Steps:* (1) for function 16, also decode the byte count and the register values; (2) print the values for the 10.30.3.7 frame. *Expected evidence:* code change and new output line. *Rubric:* 3 = byte count 4 and values 100 and 10 printed, with a length check that the byte count equals 2 × quantity; 2 = values without check; 1 = attempted; 0 = none.

**EX007 — Write policy as data.** *Objective:* express an allowlist precisely. *Inputs:* KVROC policy. *Steps:* write an allowlist of (source, destination range, function codes) entries for normal operation and for an approved maintenance window, and say who switches between them. *Expected evidence:* two short tables and an owner. *Rubric:* 3 = SCADA read-only codes to all stations; engineering writes only to the station named in the ticket and only during the window; switch owned by KVROC on-call with Kestrel Water approval; 2 = no window; 1 = vague; 0 = none.

**EX008 — Reconnaissance or feature?** *Objective:* reason about ambiguous traffic. *Inputs:* function 43 queries from `scada-01` every 24 h to all stations, and the same query from 10.20.0.31 to four stations within three seconds. *Steps:* decide which needs action and what you would check first. *Expected evidence:* a short note. *Rubric:* 3 = the daily SCADA query treated as a probable inventory feature to confirm with the vendor; the burst from an unknown host treated as a priority finding — identify 10.20.0.31 (Chapter 17 revisits it) without probing it; 2 = right priority, weak checks; 1 = both ignored or both alarmed; 0 = none.

### Chapter synthesis

Classic industrial protocols trust whoever can reach them, so network position is authority. Modbus/TCP frames have a fixed, checkable structure; decoding them correctly — including the length and protocol checks — is the basis for every later filter and detection. Writes from the wrong place are the first rule; identification and diagnostic functions need context; and a decoder only sees what its capture point sees.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 18

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes and connection

After this chapter you should be able to:

- audit a Linux host that supports a control service: listening services, SSH daemon settings, local accounts and privileged groups;
- explain why `sshd` takes the **first** value it reads for most keywords, and how that defeats careless edits;
- identify root-equivalent accounts, service accounts with interactive shells and accounts that no current person owns;
- turn findings into a prioritized hardening change that will not lock operators out.

Chapters 1–2 described the service and its traffic. The servers in the control centre — historian, SCADA server, jump host — run ordinary operating systems; this chapter makes their configuration something you can check, not assume.

### 3.1 What hardening means at technician level

Hardening is removing what is not needed and constraining what is. For a server in a control environment that means: services listening only on the interfaces they need; administrative access only through the management path; no shared or orphaned accounts; service accounts that cannot log in interactively; and configuration that is recorded so that drift can be detected (Chapter 14). NIST's general server guide gives the broader checklist ([SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final)); the CISA Cross-Sector Cybersecurity Performance Goals summarize the account and credential practices most often missing ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

### 3.2 Reading sshd configuration correctly

OpenSSH's daemon reads `sshd_config` from top to bottom and, for most keywords, **the first value obtained is used**; later lines for the same keyword are ignored ([sshd_config(5)](https://man.openbsd.org/sshd_config)). Comments begin with `#`. So a file that has `PasswordAuthentication yes` near the top and someone's later fix `PasswordAuthentication no` at the bottom still allows passwords. The reliable check is the effective configuration: on a real host, `sshd -T` prints it; in Lab 3 the parser keeps the first value, as the daemon does.

Settings that matter on a control-centre host: `ListenAddress` restricted to the management interface; `PermitRootLogin no`; `PasswordAuthentication no` once keys or certificates work; `X11Forwarding no`; a low `MaxAuthTries`; and `AllowGroups` naming a group whose membership you also review.

### 3.3 Accounts and identities

On Linux, privilege is a number: **UID 0** is root, whatever the account's name. An extra UID-0 account ("backup2", "support") is a second root password that nobody rotates. **Service accounts** (UIDs below 1000 by convention on many distributions) run daemons; they should have a non-interactive shell such as `/usr/sbin/nologin`, so that a stolen service credential cannot be used to log in. **Person accounts** should map to someone on the current authorization roster; a vendor account that sits in `sudo` permanently is standing privilege that should be time-bound (Chapter 10). Group membership is part of the identity: being in `sudo` or `ops-admins` is often more important than the account itself.

### 3.4 Worked example: auditing HIST-02 (synthetic)

`hist-02` stores Kestrel Water's time series. KVROC policy: SSH only on the management address 10.90.0.21; no root login; keys only; at most three attempts; only J. Tan and R. Kaur authorized.

**Lab 3** (save as `lab03.py`, run with `python3 lab03.py`):

```python
# Lab 3 - audit a host configuration and its local accounts (offline, standard library only)
# Synthetic files from historian host HIST-02 at the Kestrel Vale operations centre.
sshd_config = """
Port 22
ListenAddress 0.0.0.0
PermitRootLogin yes
PasswordAuthentication yes
# PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding yes
MaxAuthTries 6
AllowGroups ops-admins
"""
passwd = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
histsvc:x:998:998:historian service:/opt/hist:/bin/bash
jtan:x:1001:1001:J. Tan:/home/jtan:/bin/bash
rkaur:x:1002:1002:R. Kaur:/home/rkaur:/bin/bash
backup2:x:0:0:temp backup:/root:/bin/bash
vendor:x:1003:1003:vendor support:/home/vendor:/bin/bash"""
group = """ops-admins:x:1100:jtan,vendor
sudo:x:27:jtan,rkaur,vendor"""
policy = {"PermitRootLogin": "no", "PasswordAuthentication": "no", "X11Forwarding": "no",
          "ListenAddress": "10.90.0.21", "MaxAuthTries": "3"}
roster = {"jtan", "rkaur"}                     # people currently authorized on HIST-02
eff = {}
for line in sshd_config.splitlines():
    line = line.split("#", 1)[0].strip()
    if not line: continue
    key, val = line.split(None, 1)
    eff.setdefault(key, val)                   # sshd uses the FIRST value it reads for a keyword
findings = []
for k, want in policy.items():
    if eff.get(k) != want: findings.append(f"sshd {k} is {eff.get(k)!r}, policy {want!r}")
for line in passwd.splitlines():
    name, _, uid, gid, gecos, home, shell = line.split(":")
    if uid == "0" and name != "root": findings.append(f"account {name} has UID 0 (root equivalent)")
    if 0 < int(uid) < 1000 and shell.endswith("sh") and not shell.endswith("nologin"):
        findings.append(f"service account {name} has interactive shell {shell}")
    if int(uid) >= 1000 and name not in roster: findings.append(f"person account {name} not on roster")
for line in group.splitlines():
    g, _, _, members = line.split(":")
    for m in members.split(","):
        if m and m not in roster: findings.append(f"group {g} contains {m} (not on roster)")
for f in findings: print(f)
print("findings:", len(findings))
```

Expected output (Python 3.13.5):

```text
sshd PermitRootLogin is 'yes', policy 'no'
sshd PasswordAuthentication is 'yes', policy 'no'
sshd X11Forwarding is 'yes', policy 'no'
sshd ListenAddress is '0.0.0.0', policy '10.90.0.21'
sshd MaxAuthTries is '6', policy '3'
service account histsvc has interactive shell /bin/bash
account backup2 has UID 0 (root equivalent)
person account vendor not on roster
group ops-admins contains vendor (not on roster)
group sudo contains vendor (not on roster)
findings: 10
```

Ten findings. Note the `PasswordAuthentication` line: the file contains a commented `no`, which some reviewers read as "already fixed". It is a comment, and the effective value is `yes`. The most dangerous findings are `backup2` with UID 0 (an unmanaged second root) and `vendor` in `sudo` (standing privileged supplier access). The historian service account with `/bin/bash` matters because the service's credentials are stored on disk for the historian to use.

A safe hardening order: (1) confirm a working key-based login for J. Tan and R. Kaur from `jump-01`; (2) restrict `ListenAddress`, `PermitRootLogin`, `PasswordAuthentication` in one change, keeping an existing session open while you test a new one; (3) remove `backup2` after preserving its login history; (4) remove `vendor` from `sudo` and move vendor access to a time-bound procedure; (5) set the service account's shell to `nologin` after checking that no maintenance script logs in as it.

### 3.5 Practical activity

On a virtual machine you own, run `sshd -T | sort` and compare the output with the file. Add a duplicate keyword lower in the file, reload, and confirm that the first value wins. Record the exact OpenSSH version, because behaviour of `Include` and `Match` blocks varies by version.

Record the OpenSSH version and the path of every file that `sshd -T` shows as included. After you reload, open a second session before you close the first, so a bad ListenAddress or AllowGroups change cannot lock you out. Compare the effective values with Lab 3's policy table and note any keyword that appears twice in the file.

### 3.6 Common errors and limits

- Reading the file instead of the effective configuration.
- Fixing SSH settings from the only open session and locking everyone out; always test a second session first.
- Checking account names instead of UIDs.
- Removing a service account's shell without checking scripts that depend on it.
- Lab 3 handles neither `Include` files nor `Match` blocks; real audits must.

- Editing PasswordAuthentication at the bottom of the file while an earlier yes still wins.
- Removing vendor from sudo without a time-bound procedure for the next support visit.
- Checking account names instead of UIDs, so a second root named backup2 is missed.

### Exercises — chapter 3

**EX009 — First value wins.** *Objective:* reason about effective configuration. *Inputs:* Lab 3's `sshd_config`. *Steps:* (1) predict the effective `PasswordAuthentication` if the commented line is uncommented and left where it is; (2) say where the fix must go. *Expected evidence:* prediction and placement. *Rubric:* 3 = still `yes` because the earlier line wins; the fix replaces the first occurrence (or the earlier line is deleted), verified with `sshd -T`; 2 = right answer, no verification; 1 = predicts `no`; 0 = none.

**EX010 — Prioritize the HIST-02 findings.** *Objective:* order changes by risk and safety. *Inputs:* Lab 3 output. *Steps:* group the ten findings into today / this week / next maintenance window, with one-line reasons and a preservation step where needed. *Expected evidence:* a three-group list. *Rubric:* 3 = UID-0 `backup2` and `vendor` sudo today with login history preserved first; SSH binding and root/password settings as one tested change; service shell after script check; 2 = sensible but no preservation; 1 = unordered; 0 = none.

**EX011 — Extend the audit.** *Objective:* add a check. *Inputs:* Lab 3. *Steps:* add a check that flags any account other than `root` whose shell is interactive and whose home directory is `/root` or `/`. Report the new output. *Expected evidence:* code and output. *Rubric:* 3 = flags `backup2` (home `/root`) and only it; explains why shared home directories hide accountability; 2 = works without explanation; 1 = attempted; 0 = none.

**EX012 — Service account design.** *Objective:* design a non-interactive identity. *Inputs:* the historian service needs to read files in `/opt/hist` and write to its database. *Steps:* specify UID range, shell, home, group, file permissions and how its credential is stored and rotated. *Expected evidence:* a short specification. *Rubric:* 3 = system UID, `nologin` shell, dedicated group, least-privilege file modes, credential readable only by the service, rotation owner and interval; 2 = one gap; 1 = generic; 0 = none.

### Chapter synthesis

Operating-system hardening is checkable: effective settings, UIDs, shells and group memberships can be read and compared with a written policy. Know how the daemon actually reads its file, look at numbers rather than names, and order changes so that you never lock out the people who run the service.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 18

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes and connection

After this chapter you should be able to:

- parse CSV and JSON operational data with the standard library, without hand-written string splitting;
- validate every record against an explicit schema: field count, units, numeric form, finiteness, timestamp format and physical range;
- report each problem with its **record coordinates** (file and line) so another person can find it;
- choose between **reject** and **quarantine**, and summarize results in machine-readable form.

The technician's scripts in later chapters — decoders, auditors, detectors — all read data someone else produced. This chapter makes them strict about what they accept, because a script that silently "fixes" bad input produces confident wrong answers.

### 4.1 Formats you will meet

- **CSV** — exports from historians, HMIs and spreadsheets. RFC 4180 describes the common format, including quoting: a field containing a comma must be enclosed in double quotes ([RFC 4180](https://www.rfc-editor.org/rfc/rfc4180)). Splitting lines on commas breaks on the first quoted value; use `csv.reader`, which also tracks `line_num`.
- **JSON** — APIs, configuration exports and tool output ([RFC 8259](https://www.rfc-editor.org/rfc/rfc8259)). Use `json.loads`; note that Python's parser accepts the non-standard tokens `NaN` and `Infinity` unless you pass `parse_constant` to reject them.
- **Timestamps** — use RFC 3339 / ISO 8601 with an explicit offset, ideally UTC with `Z` ([RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)). A timestamp without an offset is ambiguous by up to a day and across daylight-saving changes.
- **Binary frames** — Chapter 2's `struct` decoding; always check lengths before unpacking.

### 4.2 A validation order that fails closed

Check in an order where each step can assume the previous ones passed:

1. **Structure**: the right number of fields. If not, nothing else in the record can be trusted — reject.
2. **Identity and type**: known station and tag; unit as the schema says (a level in feet is not a level in metres); value parses as a number.
3. **Finiteness**: `float("nan")` and `float("inf")` parse successfully but are not measurements — reject.
4. **Time**: the timestamp parses in the agreed format; it is not in the future beyond a small tolerance.
5. **Plausibility**: value within the physical range of the instrument and process.

**Reject** what cannot be interpreted (wrong structure, wrong unit, not a number). **Quarantine** what is interpretable but implausible (out of range, future time): a real sensor fault or a real attack both look like this, and an operator must see it rather than have it silently dropped. Never coerce: turning `"12,5"` into 12.5 or 125 by guessing the decimal separator creates data that was never measured.

### 4.3 Record coordinates

Every finding should say where it came from — file, line, and field — so that someone else can verify it. `csv.reader.line_num` counts physical lines read so far, including the header, so the first data row is line 2. Quoted fields containing newlines make physical lines differ from records; `line_num` reports the line where the record ended, which is still a usable coordinate.

When you paste a finding into a ticket, keep the line number next to the station name, so the next person can open the export and go straight to the row. If a quoted field spans lines, say so, because the coordinate then marks the end of the record rather than its start.

### 4.4 Worked example: validating a station export (synthetic)

An export from Kestrel Water's historian lists one reading per station. The analysis time is 06:00Z on 12 October 2026.

**Lab 4** (save as `lab04.py`, run with `python3 lab04.py`):

```python
# Lab 4 - validate a telemetry export with record coordinates (offline, standard library only)
# Synthetic CSV export from Kestrel Water stations; "now" is 2026-10-12T06:00:00Z.
import csv, io, json, math
from datetime import datetime, timezone
export = """station,tag,value,unit,ts
KW-01,LEVEL_M,3.42,m,2026-10-12T05:58:00Z
KW-02,CL2_MGL,0.61,mg/L,2026-10-12T05:58:00Z
KW-03,LEVEL_M,,m,2026-10-12T05:58:00Z
KW-04,CL2_MGL,7.9,mg/L,2026-10-12T05:58:00Z
KW-05,FLOW_LS,"12,5",L/s,2026-10-12T05:58:00Z
KW-06,LEVEL_M,2.10,ft,2026-10-12T05:58:00Z
KW-07,LEVEL_M,2.95,m,2026-10-12 05:58
KW-08,LEVEL_M,nan,m,2026-10-12T05:58:00Z
KW-09,FLOW_LS,41.0,L/s,2026-10-12T07:15:00Z
KW-10,LEVEL_M,1.88,m,2026-10-12T05:58:00Z,extra
"""
SCHEMA = {"LEVEL_M": ("m", 0.0, 12.0), "CL2_MGL": ("mg/L", 0.0, 5.0), "FLOW_LS": ("L/s", 0.0, 400.0)}
now = datetime(2026, 10, 12, 6, 0, tzinfo=timezone.utc)
result = {"accept": [], "reject": [], "quarantine": []}
reader = csv.reader(io.StringIO(export))
header = next(reader)
for row in reader:
    where = f"line {reader.line_num}"
    if len(row) != len(header): result["reject"].append((where, f"{len(row)} fields, expected {len(header)}")); continue
    r = dict(zip(header, row))
    unit, lo, hi = SCHEMA[r["tag"]]
    if r["unit"] != unit: result["reject"].append((where, f"{r['station']} unit {r['unit']!r}, expected {unit!r}")); continue
    try: v = float(r["value"])
    except ValueError: result["reject"].append((where, f"{r['station']} value {r['value']!r} not a number")); continue
    if not math.isfinite(v): result["reject"].append((where, f"{r['station']} value not finite")); continue
    try:
        ts = datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError: result["reject"].append((where, f"{r['station']} timestamp {r['ts']!r} not RFC 3339 UTC")); continue
    if ts > now: result["quarantine"].append((where, f"{r['station']} timestamp {(ts - now).seconds // 60} min in the future")); continue
    if not lo <= v <= hi: result["quarantine"].append((where, f"{r['station']} {r['tag']}={v} outside {lo}-{hi}")); continue
    result["accept"].append((where, r["station"]))
for k in ("reject", "quarantine"):
    for where, why in result[k]: print(f"{k:<10} {where:<8} {why}")
print(json.dumps({k: len(v) for k, v in result.items()}))
```

Expected output (Python 3.13.5):

```text
reject     line 4   KW-03 value '' not a number
reject     line 6   KW-05 value '12,5' not a number
reject     line 7   KW-06 unit 'ft', expected 'm'
reject     line 8   KW-07 timestamp '2026-10-12 05:58' not RFC 3339 UTC
reject     line 9   KW-08 value not finite
reject     line 11  6 fields, expected 5
quarantine line 5   KW-04 CL2_MGL=7.9 outside 0.0-5.0
quarantine line 10  KW-09 timestamp 75 min in the future
{"accept": 2, "reject": 6, "quarantine": 2}
```

Only two of ten rows are accepted. Each rejection names its line: an empty value (line 4), a decimal comma inside a quoted field (line 6), a level in feet (line 7), a timestamp without seconds or offset (line 8), `nan` (line 9) and an extra field (line 11). The quarantined rows are the interesting ones: chlorine at 7.9 mg/L is outside the instrument range — a sensor fault, a scaling error or a manipulated value — and KW-09's timestamp is 75 minutes in the future, which in Chapter 7 you will learn to suspect as a clock problem. Both are passed to a person with their coordinates.

The JSON summary on the last line is deliberately machine-readable, so that a monitoring job can alert when the rejection count rises.

### 4.5 Practical activity

Add a station-identity check to Lab 4: only KW-01 to KW-12 are valid. Then add a row `KW-13,LEVEL_M,2.0,m,2026-10-12T05:58:00Z` and confirm it is rejected with its line number. Finally, make the timestamp parser accept an explicit `+00:00` offset as well as `Z` without accepting naive timestamps.

Reject KW-13 with its line number and a reason that names the allowed set. For timestamps, accept both Z and an explicit plus-zero offset, and still reject a bare local time. Re-run the lab and confirm that the JSON summary's reject count rises by one for the new station.

### 4.6 Common errors and limits

- Splitting CSV on commas.
- Coercing ambiguous values instead of rejecting them.
- Letting `nan` through because `nan > hi` is false.
- Accepting naive timestamps and assuming local time.
- Reporting "6 rejected" with no coordinates, which nobody can check.
- Lab 4 checks single readings; rate-of-change and stuck values need a series (Chapter 8).

- Letting nan through because comparisons with it are false, so an out-of-range check never fires.
- Reporting only totals with no coordinates, so nobody can find the bad rows.
- Coercing a decimal comma into a float and writing the invented value into the historian.

### Exercises — chapter 4

**EX013 — Predict before running.** *Objective:* reason about the validator. *Inputs:* Lab 4 with three new rows: `KW-11,LEVEL_M,12.0,m,2026-10-12T05:59:00Z`; `KW-12,LEVEL_M,inf,m,2026-10-12T05:59:00Z`; `KW-02,CL2_MGL,-0.0,mg/L,2026-10-12T05:59:00Z`. *Steps:* predict each verdict and the new summary, then run. *Expected evidence:* predictions, actual output, explanation of any surprise. *Rubric:* 3 = accept, reject (not finite), accept; summary `{"accept": 4, "reject": 7, "quarantine": 2}`; notes −0.0 should be normalized; 2 = one wrong but explained; 1 = guesses; 0 = none.

**EX014 — Reject or quarantine?** *Objective:* apply the distinction. *Inputs:* (a) flow −3.0 L/s; (b) unit "M" instead of "m"; (c) level 11.9 m on a 12 m tank; (d) timestamp 4 s in the future. *Steps:* decide and justify. *Expected evidence:* four verdicts. *Rubric:* 3 = (a) quarantine (interpretable, implausible; might be reverse flow or offset); (b) reject or normalize only if the schema explicitly allows case-insensitive units — not guess; (c) accept, perhaps with a high-level alarm; (d) accept within an agreed clock tolerance; 2 = one weak; 1 = all reject; 0 = none.

**EX015 — JSON with traps.** *Objective:* harden JSON parsing. *Inputs:* `{"station": "KW-03", "value": NaN}`. *Steps:* show what `json.loads` returns by default and write the one-line change that rejects it. *Expected evidence:* code and behaviour. *Rubric:* 3 = default returns `nan` float; `json.loads(s, parse_constant=lambda c: (_ for _ in ()).throw(ValueError(c)))` or an equivalent function that raises; explains RFC 8259 does not allow NaN; 2 = works without explanation; 1 = attempted; 0 = none.

**EX016 — Summary for monitoring.** *Objective:* design a machine-readable result. *Inputs:* Lab 4. *Steps:* extend the JSON summary with counts by reason and by station, and propose one alert condition on it. *Expected evidence:* example JSON and the condition. *Rubric:* 3 = stable keys, counts by reason, alert such as "any quarantine of CL2_MGL, or rejects > 10 % of rows for two consecutive exports"; 2 = no reason breakdown; 1 = prose only; 0 = none.

### Chapter synthesis

Operational data arrive malformed, ambiguous and occasionally hostile. Parse with real parsers, validate in an order that fails closed, never coerce, and report every finding with coordinates. Reject what you cannot interpret; quarantine what you can interpret but should not believe; and keep summaries machine-readable so that the validator itself can be monitored.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 18

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes and connection

After this chapter you should be able to:

- write a **technical scope** for a task in a critical environment: systems, actions allowed, time window, contacts and stop conditions;
- explain why, in operational technology, a passive observation is preferred and an active one needs explicit approval;
- collect technical evidence so that someone else can verify it: what, from where, when (UTC), by whom, how, and its hash;
- separate **observed**, **inferred**, **done** and **open** in every working note.

Chapters 1–4 gave you tools. Before you point any of them at a real system, this chapter defines what you are allowed to touch and how you will prove what you saw.

### 5.1 Scope is a safety control

In an office network, an over-eager scan wastes time. In a control network it can stop a process: some controllers and older network stacks behave badly when probed, and a "read" can trigger vendor diagnostics or fill a session table. NIST's OT guide recommends caution with active scanning in operational environments and prefers passive methods where possible ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); NIST's testing guide describes rules of engagement for any assessment ([SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)).

A technical scope answers, in writing, before work starts:

- **Purpose** — what question the work answers.
- **Systems in scope** — named hosts and addresses; everything else is out.
- **Allowed actions** — for example "read running configuration", "passive capture on SPAN port", "one TCP connect test to port 502 with no Modbus request".
- **Window** — date and times, with the operator's agreement.
- **People** — who authorized it (the system owner), who is on site, who in the control room is informed.
- **Stop conditions** — any unexpected device behaviour, alarm or request from operations.
- **Evidence handling** — where results are stored and who may read them.

### 5.2 Passive first

Many questions can be answered without sending a packet: configuration exports, firewall logs, switch MAC tables, a passive capture from a mirror (SPAN) port, the historian's own records. Prefer these. When an active test is genuinely needed — for example to verify a deny rule in Chapter 11 — make it the smallest test that answers the question, from a named source, at an agreed time.

Prefer a SPAN capture or a configuration export before any connect test. When an active test is needed, use a marked source address, the smallest action that answers the question, and an agreed window with operations informed at start and end.

### 5.3 What makes technical evidence usable

A screenshot of a terminal proves little. Usable evidence records:

1. **What** — the raw output or file, not a summary.
2. **Source** — host and tool, with version.
3. **Time** — in UTC with the host's clock offset if known (Chapter 7).
4. **Collector** — who ran it.
5. **Method** — the exact command or query.
6. **Integrity** — a SHA-256 hash recorded at collection time, so later copies can be checked ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)); Chapter 18 seals a whole package.

NIST's guide to integrating forensic techniques into incident response discusses collection and preservation order ([SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final)). At technician level the rule is simple: **preserve before you change**. If you are about to fix something that may be evidence of misuse, collect it first.

### 5.4 Four labels

Every note you write in this course uses four labels. **Observed**: what a tool or person recorded, with source and time. **Inferred**: what you conclude, and why. **Done**: what you changed, under which change record. **Open**: what remains unknown, and who owns it. Mixing them — "the RTU was compromised" when you observed only a configuration session — is how wrong conclusions spread.

A note that says only "RTU compromised" fails the test: it mixes inference with observation. Write the four labels on every working note in this course, including the KW-04 reachability check, so a reader can see what was measured and what remains open.

### 5.5 Worked example: scoping the KW-04 check (synthetic)

After Lab 2 showed writes from a corporate desk, L. Ferreira (KVROC security lead) asks you to confirm whether the corporate zone can reach station port 502. A sound scope:

| Element | Content |
|---|---|
| Purpose | Confirm or refute reachability from corporate zone to KW-04 tcp/502. |
| In scope | fw-01 configuration and logs (read); one TCP connect from test desk 10.30.99.9 to 10.10.4.2:502, no Modbus payload. |
| Out of scope | All other stations; any Modbus request; desk 10.30.3.7 (preserve, do not touch). |
| Window | 13 Oct 2026 10:00–10:30 local, agreed with A. Mensah (Kestrel Water operations). |
| People | Authorizer A. Mensah; operator in Kestrel Water control room informed at start and end. |
| Stop | Any KW-04 alarm, communication loss or operator request. |
| Evidence | Firewall config export, connect test output, fw-01 log lines; hashes in the case folder. |

The working note after the test reads: *Observed* — connect from 10.30.99.9 to 10.10.4.2:502 completed at 08:04:11Z; fw-01 logged rule R4 allow. *Inferred* — corporate hosts can reach station Modbus because of R4 (Chapter 10). *Done* — nothing changed. *Open* — who created R4 and why (owner: L. Ferreira).

### 5.6 Practical activity

Write a scope for a passive capture on the control-centre switch's SPAN port for 24 hours. Include storage limits and who may read the capture, since it will contain process values and possibly credentials sent in clear text.

State a maximum file size and a retention period, because a day of process values and clear-text credentials is both large and sensitive. Name who may read the capture and where it is stored, and say that the capture stops if the switch's mirror port affects forwarding. Mark the activity as passive and list stop conditions that include any operator request.

### 5.7 Common errors and limits

- Starting work on a verbal "go ahead".
- Scanning a subnet to "see what's there" in a control network.
- Collecting evidence without UTC times or hashes.
- Fixing first and collecting later.
- Treating scope as paperwork: it is what stops a test becoming an incident.

- Starting from a verbal go-ahead and writing the scope afterwards.
- Scanning a subnet in a control network to discover devices.
- Fixing a finding before collecting the evidence that showed it. A scope written after the work cannot protect the process during it.

### Exercises — chapter 5

**EX017 — Repair a scope.** *Objective:* find missing elements. *Inputs:* "Run a scan of 10.10.0.0/16 on Tuesday to find open ports. Approved by IT." *Steps:* list each defect and rewrite. *Expected evidence:* defect list and rewritten scope. *Rubric:* 3 = identifies wrong authorizer (system owner needed), unbounded range, active scanning in OT, no window, no stop conditions, no evidence handling; rewrite prefers passive inventory sources; 2 = most defects; 1 = cosmetic; 0 = none.

**EX018 — Label the note.** *Objective:* separate observation and inference. *Inputs:* "The vendor hacked KW-09 last night — the RTU config changed and data stopped, so I reset it." *Steps:* rewrite with the four labels. *Expected evidence:* labelled note. *Rubric:* 3 = observed (config session time, data gap), inferred (possible unapproved change; attribution unknown), done (reset — and the loss of evidence it caused), open (who, why; owner); 2 = labels without noticing the evidence loss; 1 = partial; 0 = none.

**EX019 — Evidence record.** *Objective:* produce verifiable evidence. *Inputs:* you export fw-01's rule set to `fw-01-rules-20261013.txt`. *Steps:* write the evidence record fields and the command that produces its hash on Linux. *Expected evidence:* record and `sha256sum fw-01-rules-20261013.txt`. *Rubric:* 3 = all six elements, UTC time with clock source, hash stored separately from the file; 2 = one missing; 1 = hash only; 0 = none.

**EX020 — Passive alternatives.** *Objective:* avoid unnecessary active tests. *Inputs:* three questions: which hosts talk to KW-07; what firmware KW-07 runs; whether KW-07 accepts telnet. *Steps:* propose a passive or read-only method for each and say when an active test would still be justified. *Expected evidence:* three rows. *Rubric:* 3 = flow logs or SPAN capture; asset records or the vendor tool during an approved engineering session; configuration export or the vendor's documentation, with an active check only in a scoped window with operations present; 2 = one weak; 1 = all active; 0 = none.

### Chapter synthesis

In critical environments, scope protects the process as much as the tester. Write it before you start, prefer passive methods, and make every piece of evidence verifiable by someone else: raw, sourced, timed in UTC, attributed and hashed. Preserve before you change, and keep observed, inferred, done and open apart.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 18

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Critical infrastructure and sector security: system model

### Learning outcomes and connection

After this chapter you should be able to:

- build a technical system model of a critical service: assets, zones, conduits, protocols, trust boundaries and the physical consequence each zone can cause;
- use the zone-and-conduit vocabulary of ISA/IEC 62443 at a technician's level;
- describe how water, healthcare and electricity services differ technically — protocols, timing, safety systems and who may change what;
- mark on the model where each later chapter's controls and detections will sit.

Chapters 1–5 were the general foundations. From here on the course applies them to critical sectors. The system model is the technician's map: without it, a firewall rule, a detection or a troubleshooting step has nothing to refer to.

### 6.1 Zones and conduits

The ISA/IEC 62443 series groups assets with similar security requirements into **zones** and the communication paths between them into **conduits** ([ISA/IEC 62443 overview](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)). The practical rules a technician applies:

- every asset belongs to exactly one zone;
- every permitted communication between zones is a declared conduit with a purpose, protocol, direction and owner;
- anything not declared is not permitted, and if observed is a finding (Lab 17 and Chapter 11 verify this);
- a zone's protection should match the worst physical consequence of the assets inside it.

The common shape of a supervisory system — field, control, supervisory, operations-DMZ, enterprise — appears in NIST SP 800-82 Rev. 3 as an example architecture ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Use it as a vocabulary, not a template: a real site has historical exceptions, and the model's job is to show them.

### 6.2 What to record for each element

For each **asset**: name, address, function, zone, owner, software and firmware versions, protocols spoken, management method and the physical consequence of loss or misuse. For each **conduit**: source zone, destination zone, protocol and port, direction of initiation, purpose, owner, enforcement point (which firewall rule) and monitoring point (which sensor sees it). For each **trust boundary**: what crosses it and what checks happen there.

For eng-ws-15 record that it can program RTUs and that its loss or misuse has zone-wide consequence. For each conduit, name the firewall rule that should enforce it and the sensor that should see it, so a later verification knows where to look. Leave no asset without a zone and no permitted path without a conduit owner.

### 6.3 Sector differences that matter at the keyboard

- **Water**: widely dispersed stations on cellular or radio links; Modbus or DNP3 telemetry; long equipment lives; small operators with limited staff. Consequences include loss of pressure, overflow and incorrect chemical dosing. CISA's advisory on attacks against internet-exposed Unitronics PLCs in water systems is a reminder that exposure plus default credentials is enough ([CISA AA23-335A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)).
- **Electricity**: substations with protection relays whose timing is measured in milliseconds; DNP3 or IEC 60870-5-104 telecontrol to a control centre; IEC 61850 inside modern substations; strict separation of protection from supervisory functions. A technician never changes protection settings; those belong to protection engineers.
- **Healthcare**: building-management systems (ventilation, pressure in isolation rooms, medical gases monitoring), clinical device networks and IT systems in one building, often sharing infrastructure; downtime affects patients directly and changes are bound by clinical engineering and device manufacturers' instructions.

In all three, **safety instrumented systems** and protection functions are designed to act independently of the supervisory system. The technician's model shows them as separate zones and never routes management traffic through them.

### 6.4 Worked example: the KVROC model (synthetic)

| Zone | Assets | Worst consequence | Notes |
|---|---|---|---|
| Z1 Station field (10.10.0.0/16) | KW-01..12 RTUs, pumps, analysers | Wrong dosing, overflow, loss of supply | Modbus/TCP, no authentication |
| Z2 Control centre (10.20.0.0/24) | scada-01, hmi-02, eng-ws-15, hist-02 | Loss of view and control of all stations | eng-ws-15 can program RTUs |
| Z3 Substation SS-3 | outstation (DNP3 address 10), protection relays | Loss of telecontrol; protection is separate | DNP3 over operator MPLS via fep-01 |
| Z4 Hospital BMS | bms-server, controllers | Ventilation and pressure alarms lost | Monitored only; KVROC has read access |
| Z5 Management (10.90.0.0/24) | jump-01, ntp-ops, ad-ops, collector | Compromise reaches every zone | Highest privilege |
| Z6 Corporate (10.30.0.0/16) | desks, email, report server | Business disruption | Internet-connected |

Declared conduits include: C1 Z2 scada-01 → Z1 tcp/502 read polls; C2 Z2 eng-ws-15 → Z1 tcp/502 writes during approved windows; C3 Z5 jump-01 → Z2 tcp/22; C4 Z2 hist-02 → Z6 report server, HTTPS push of daily CSV. Lab 2 already showed an **undeclared** path: Z6 desk → Z1 tcp/502. In the model it appears as a red line with a question: which rule allows it, and since when? Chapter 10 answers.

### 6.5 Practical activity

Extend the model with two conduits for Z3 (fep-01 to the outstation and the vendor's remote support path) and one for Z4. For each, record purpose, protocol, initiator, owner, enforcement point and monitoring point. Mark which conduits a single compromised Z5 host could abuse.

For the vendor remote-support path into Z3, record whether it terminates on the jump host or reaches the outstation directly. For Z4, mark that KVROC has read access only. Then list which of those conduits a compromised jump host in Z5 could open, and which controls would still apply.

### 6.6 Common errors and limits

- Zones drawn by IP subnet rather than by consequence and trust.
- Conduits without owners or purposes, which nobody can later remove.
- Omitting the management zone because it is "IT".
- Modelling the safety system as a normal controller.
- A model that is never compared with observed traffic; Chapter 11 does that.

- Drawing zones by subnet alone when two hosts in the same subnet have different consequences.
- Leaving conduits without owners, so nobody can remove them later.
- Putting a safety or protection function in the same zone as ordinary supervisory controllers.

### Exercises — chapter 6

**EX021 — Place the assets.** *Objective:* assign zones by consequence. *Inputs:* a cellular router at KW-06; the vendor's remote-support gateway for SS-3; the report server; a laptop used by Kestrel Water engineers at stations. *Steps:* assign each to a zone (existing or new) and justify. *Expected evidence:* four placements. *Rubric:* 3 = router in Z1 boundary with its management treated as Z5-level privilege; vendor gateway in its own remote-access zone, not Z3; report server Z6; engineering laptop as a transient asset with its own controls (Chapter 16); 2 = one weak; 1 = by subnet only; 0 = none.

**EX022 — Write a conduit.** *Objective:* declare a path completely. *Inputs:* hist-02 must send a daily CSV to the corporate report server. *Steps:* write the conduit entry with all fields. *Expected evidence:* one completed entry. *Rubric:* 3 = initiated from Z2 outward (push, not pull from corporate), HTTPS to one named host and port, purpose, owner, enforcement rule and monitoring point named, review date; 2 = one missing; 1 = "allow hist to corporate"; 0 = none.

**EX023 — Sector contrast.** *Objective:* recognize technical differences. *Inputs:* a proposal to apply the same weekly patch-and-reboot schedule to scada-01, the SS-3 front end and the hospital BMS server. *Steps:* explain for each sector what must be checked first. *Expected evidence:* three short paragraphs. *Rubric:* 3 = water: redundancy and poll interruption; grid: telecontrol windows agreed with the grid control room, no effect on protection; hospital: clinical engineering and manufacturer constraints, ventilation alarms continuity; 2 = generic; 1 = accepts one schedule; 0 = none.

**EX024 — Model versus capture.** *Objective:* compare declared and observed. *Inputs:* Lab 2 output and the conduit list in 6.4. *Steps:* list every observed flow not explained by a declared conduit. *Expected evidence:* list with reasons. *Rubric:* 3 = the corporate-desk writes (no conduit), possibly the device-ID query if no conduit covers it, malformed frames from scada-01 as an anomaly to explain; 2 = writes only; 1 = none found; 0 = none.

### Chapter synthesis

The system model joins assets, zones, conduits and consequences into one map. It says what should happen, so that anything else is visible as a finding. Sectors differ in protocols, timing and who may change what, and safety and protection functions stay separate from everything a technician touches.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 18

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Critical infrastructure and sector security: data and telemetry

### Learning outcomes and connection

After this chapter you should be able to:

- name the telemetry sources a technician uses in a control environment — process data, device logs, firewall and host logs, flow records, passive captures — and what each can and cannot show;
- parse RFC 5424 syslog, compute facility and severity from the priority value, and handle lines that are not RFC 5424;
- measure and correct clock offsets against an NTP reference and build a single UTC timeline;
- explain how an uncorrected clock reverses cause and effect.

Chapter 6 said where things are. This chapter is about what they tell you, and whether you can put their stories in the right order.

### 7.1 Sources and blind spots

| Source | Shows | Does not show |
|---|---|---|
| Process data (historian) | Values and alarms over time | Who caused a change |
| HMI and SCADA event logs | Operator actions, alarm acknowledgements | Actions taken directly on the controller |
| Controller/RTU logs | Configuration sessions, mode changes (if supported and enabled) | Often nothing; many devices log little |
| Firewall logs | Allowed and denied connections at the boundary | Traffic inside a zone |
| Host logs (jump host, servers) | Logins, commands, service events | Activity on devices without logging |
| Passive capture / flow records | Who talked to whom, with what function | Encrypted content; traffic not passing the sensor |

NIST's log management guide describes collection, retention and protection of these records ([SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final)). The technician's first job is to know which source answers which question, and which questions no source answers.

### 7.2 Syslog structure

RFC 5424 defines the modern syslog format: `<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG` ([RFC 5424](https://www.rfc-editor.org/rfc/rfc5424)). The priority value is *facility × 8 + severity*: `<38>` is facility 4 (security/authorization), severity 6 (informational). The timestamp is RFC 3339 with an offset, and a dash (`-`) means "nil" — for a timestamp, *the sender did not know the time*. Many devices still send the older BSD format (`<13>Oct 11 23:15:02 host app: ...`) with no year and no zone; count such lines and parse them separately rather than dropping them.

### 7.3 Time

Every timeline is only as good as its clocks. NTP (RFC 5905) lets hosts measure their **offset** from a reference ([RFC 5905](https://www.rfc-editor.org/rfc/rfc5905)). In control environments some devices have no NTP client, drift by minutes, or are deliberately isolated from time sources. Record, for every host that contributes to a timeline, its measured offset at a known moment, and correct its timestamps by subtracting it: *corrected = reported − (host clock − reference)*. Convert everything to UTC before sorting; local offsets such as `+01:00` are correct but easy to misorder by eye.

### 7.4 Worked example: the 23:14 sequence (synthetic)

On the night of 11 October, an operator reported that pump 2 at KW-04 started unexpectedly. You collected six lines and measured clock offsets the next morning (the RTU was 212 s behind the reference).

**Lab 7** (save as `lab07.py`, run with `python3 lab07.py`):

```python
# Lab 7 - parse RFC 5424 syslog, correct clock offsets and build a UTC timeline (offline, stdlib)
# Synthetic lines from the Kestrel Vale operations centre; offsets measured against the NTP reference.
import re
from datetime import datetime, timedelta, timezone
lines = [
 "<38>1 2026-10-11T23:14:05.120Z fw-01 filterlog - - - block tcp 10.30.3.7:51544 -> 10.10.4.2:502",
 "<86>1 2026-10-12T00:13:58+01:00 jump-01 sshd 812 - - Accepted publickey for jtan from 10.90.0.40",
 "<134>1 2026-10-11T23:16:40Z hmi-02 hmi - - - operator setpoint change KW-04 PUMP2 start",
 "<38>1 2026-10-11T23:15:31Z rtu-kw04 auth - - - config session opened user=eng",
 "<13>Oct 11 23:15:02 eng-ws-15 app: project download started",
 "<38>1 - hist-02 histd - - - archive rollover",
]
offset_s = {"fw-01": 0.0, "jump-01": 0.4, "hmi-02": 0.0, "rtu-kw04": -212.0}   # host clock minus reference
pat = re.compile(r"^<(\d{1,3})>1 (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) ?(.*)$")
events, unparsed = [], []
for ln in lines:
    m = pat.match(ln)
    if not m: unparsed.append(("not RFC 5424", ln)); continue
    pri, ts, host, app, _pid, _msgid, _sd, msg = m.groups()
    if ts == "-": unparsed.append(("no timestamp", ln)); continue
    t = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)
    t_corr = t - timedelta(seconds=offset_s.get(host, 0.0))
    fac, sev = divmod(int(pri), 8)
    events.append((t_corr, host, f"fac={fac} sev={sev}", msg, offset_s.get(host, 0.0)))
for t, host, fs, msg, off in sorted(events):
    note = f" (clock corrected {-off:+.1f} s)" if off else ""
    print(f"{t.strftime('%H:%M:%S.%f')[:-3]}Z {host:<9} {fs:<11} {msg}{note}")
for why, ln in unparsed: print("UNPARSED", why, "|", ln)
```

Expected output (Python 3.13.5):

```text
23:13:57.600Z jump-01   fac=10 sev=6 Accepted publickey for jtan from 10.90.0.40 (clock corrected -0.4 s)
23:14:05.120Z fw-01     fac=4 sev=6 block tcp 10.30.3.7:51544 -> 10.10.4.2:502
23:16:40.000Z hmi-02    fac=16 sev=6 operator setpoint change KW-04 PUMP2 start
23:19:03.000Z rtu-kw04  fac=4 sev=6 config session opened user=eng (clock corrected +212.0 s)
UNPARSED not RFC 5424 | <13>Oct 11 23:15:02 eng-ws-15 app: project download started
UNPARSED no timestamp | <38>1 - hist-02 histd - - - archive rollover
```

Before correction, the RTU line (23:15:31Z) appeared *before* the HMI setpoint change (23:16:40Z), suggesting someone configured the RTU and then the operator acted. After correction the RTU session happened at 23:19:03Z — **after** the operator's start command. The story changes from "someone tampered first" to "an engineering session followed the operator's action", which leads to a different question (who opened a configuration session at 23:19 and why). Two lines could not be placed: the BSD-format line from the engineering workstation has no year or zone, and the historian line has a nil timestamp. They are reported, not discarded; the engineering workstation's "project download started" is potentially the most important line of all, and placing it requires its own clock check and the workstation's local logs.

### 7.5 Practical activity

Measure the offset of a machine you own against a public or local NTP server (for example `chronyc tracking` or `ntpq -p` on Linux, `w32tm /stripchart` on Windows), record it with the time of measurement, and repeat after 24 hours to see drift.

Record the host, the reference, the offset and the time of measurement. After twenty-four hours, compare the new offset with the old one to see drift. Keep both readings with the timeline work in Lab 7, so a later investigation knows how uncertain a correction made from a single measurement would be.

### 7.6 Common errors and limits

- Sorting by the text of mixed-offset timestamps.
- Correcting clocks in the wrong direction; write the formula down every time.
- Dropping lines that do not parse; count and report them.
- Assuming an offset measured today applied last night; drift and resynchronization change it, so state the uncertainty.
- Assuming the absence of a log line means the absence of an event — many devices simply do not log.

- Sorting mixed-offset timestamps as text and reversing the order of events.
- Correcting clocks in the wrong direction; write corrected equals reported minus offset every time.
- Dropping lines that do not parse instead of counting them as unparsed.
- Treating a missing log line as proof that nothing happened.

### Exercises — chapter 7

**EX025 — Decode priorities.** *Objective:* compute facility and severity. *Inputs:* `<86>`, `<134>`, `<11>`, `<165>`. *Steps:* compute each. *Expected evidence:* four pairs with names. *Rubric:* 3 = 86 → 10/6 (authpriv, informational); 134 → 16/6 (local0, informational); 11 → 1/3 (user, error); 165 → 20/5 (local4, notice); 2 = arithmetic right, names missing; 1 = partial; 0 = none.

**EX026 — Correct a clock.** *Objective:* apply the offset formula. *Inputs:* fep-01 logs an event at 02:10:00Z; its offset measured an hour later was +47 s (host ahead). *Steps:* give the corrected time and the uncertainty you would state. *Expected evidence:* corrected time and a sentence on uncertainty. *Rubric:* 3 = 02:09:13Z; uncertainty because the offset was measured later and drift is unknown, e.g. "±a few seconds; offset measured 03:10Z"; 2 = right time without uncertainty; 1 = wrong direction; 0 = none.

**EX027 — Place the BSD line.** *Objective:* handle legacy formats safely. *Inputs:* the `eng-ws-15` line in Lab 7. *Steps:* list what you need to place it on the timeline and write the parsing rule you would add. *Expected evidence:* list and rule. *Rubric:* 3 = year from collection context, the host's time zone setting and its measured offset; parse with explicit zone assignment and mark the result "assumed zone"; 2 = rule without the assumptions recorded; 1 = drop it; 0 = none.

**EX028 — Blind-spot question.** *Objective:* match questions to sources. *Inputs:* "Did anyone write to KW-04 directly from the station's local laptop port?" *Steps:* say which sources could answer it, which cannot, and what you would need to add. *Expected evidence:* short analysis. *Rubric:* 3 = control-centre firewall and capture cannot see local station traffic; RTU logs might, if it logs configuration and writes; add a station-level sensor or RTU logging and physical access records; 2 = partly; 1 = "check the firewall"; 0 = none.

### Chapter synthesis

Telemetry is a set of partial witnesses. Know what each source can see, parse formats strictly while counting what you cannot parse, and correct every clock against a reference before you order events. A timeline built on uncorrected clocks can reverse cause and effect; one built on corrected clocks, with its uncertainties stated, is evidence.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 18

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Critical infrastructure and sector security: failure modes

### Learning outcomes and connection

After this chapter you should be able to:

- name the common technical failure modes of telemetry and control — gap, stuck value, spike, drift, out-of-range, stale timestamp, loss of control authority — and their usual causes;
- detect them in a time series with simple, explainable rules;
- explain why an in-range value can still be false, and why a perfectly constant value is suspicious;
- keep fault and attack hypotheses open together until evidence separates them.

Chapter 7 put events in order. This chapter asks of each measurement: is it true? Many security events first appear as "bad data", and many bad-data events are ordinary faults. A technician must recognize both.

### 8.1 A catalogue of failure modes

| Mode | Looks like | Ordinary causes | Security-relevant causes |
|---|---|---|---|
| **Gap** | Missing samples | Link outage, polling overload (Chapter 1), device reboot | Blocked or dropped traffic, denial of service |
| **Stuck / flatline** | Identical values for longer than the process allows | Frozen sensor, failed analog input, SCADA serving last known value | Replayed or frozen values hiding a real change |
| **Spike** | A jump faster than physics permits | Electrical noise, scaling error, bad sample | Injected value |
| **Drift** | Slow divergence from reality | Sensor fouling, calibration age | Slow manipulation (rare, hard to detect) |
| **Out of range** | Impossible value | Wiring fault, wrong scaling | Crafted value |
| **Stale timestamp** | Value with an old or future time | Clock error (Chapter 7), buffered data | Replay |
| **Loss of control authority** | Commands not executed or executed by someone else | Local/remote switch left in local, interlock | Unauthorized write |

The point of the table is not that every gap is an attack. It is that the same symptom has both kinds of cause, so detections should report the **symptom** precisely, and investigation (Chapter 13) separates the causes.

### 8.2 Rules that explain themselves

Each detection in this chapter is a rule a person can read and verify:

- **Gap**: more than *N* consecutive missing samples, where *N* is set from the poll cycle and the process's tolerance.
- **Stuck**: more than *M* identical consecutive readings, where *M* reflects how much a healthy sensor naturally varies. A chlorine analyser reporting exactly 0.62 for twenty minutes is suspicious because real analysers fluctuate in their last digit.
- **Spike**: a change between consecutive samples larger than the **maximum physically plausible step** — a 12 m tank cannot rise 6.8 m in a minute. This catches values that range checks miss.
- **Range**: outside the instrument or process limits (Chapter 4).

These rules are crude but transparent: when one fires, everyone can see why. Statistical or learned anomaly detectors can add sensitivity later; they should not replace rules that operators understand.

### 8.3 In-range is not true

A value of 9.80 m on a 12 m tank passes every range check. If the previous minute read 2.96 m and the next 2.97 m, the 9.80 is impossible as a measurement. Conversely, a constant value is always "in range". Range checks protect against the absurd; **rate** and **variation** checks protect against the plausible-looking false.

Use a maximum step from the process, such as half a metre per minute for a tank level, so that a single wild sample is caught even when it lies inside the instrument's range. Write the step limit next to the range limit in the tag's schema, and review both after every false alarm.

### 8.4 Worked example: four tags, twenty minutes (synthetic)

**Lab 8** (save as `lab08.py`, run with `python3 lab08.py`):

```python
# Lab 8 - classify telemetry failure modes (offline, standard library only)
# Synthetic one-minute readings from four Kestrel Water tags, 06:00-06:19Z on 2026-10-12.
series = {
 "KW-01 LEVEL_M": [3.40,3.41,3.41,3.42,3.43,3.43,3.44,3.45,3.45,3.46,3.47,3.47,3.48,3.49,3.49,3.50,3.51,3.51,3.52,3.53],
 "KW-02 CL2_MGL": [0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62,0.62],
 "KW-05 FLOW_LS": [41.0,40.8,41.2,40.9,None,None,None,None,None,None,None,41.1,40.7,41.0,41.3,40.9,41.2,41.0,40.8,41.1],
 "KW-07 LEVEL_M": [2.95,2.96,2.95,2.97,2.96,2.96,9.80,2.97,2.96,2.98,2.97,2.97,2.98,2.97,2.99,2.98,2.98,2.99,2.98,2.99],
}
LIMITS = {"LEVEL_M": (0.0, 12.0), "CL2_MGL": (0.0, 5.0), "FLOW_LS": (0.0, 400.0)}
MAX_STEP = {"LEVEL_M": 0.5, "CL2_MGL": 0.3, "FLOW_LS": 25.0}   # physically plausible change per minute
STUCK_MIN, GAP_MIN = 15, 5
for name, xs in series.items():
    tag = name.split()[1]; lo, hi = LIMITS[tag]; out = []
    run, longest = 0, 0
    for i in range(len(xs)):                     # gaps
        run = run + 1 if xs[i] is None else 0; longest = max(longest, run)
    if longest >= GAP_MIN: out.append(f"gap: {longest} consecutive missing minutes")
    vals = [(i, v) for i, v in enumerate(xs) if v is not None]
    same, best = 1, 1
    for (i0, a), (i1, b) in zip(vals, vals[1:]):  # stuck / flatline (exact repeats)
        same = same + 1 if a == b else 1; best = max(best, same)
        if abs(b - a) > MAX_STEP[tag] and i1 - i0 == 1:
            out.append(f"spike: 06:{i1:02d}Z jump {a} -> {b} exceeds {MAX_STEP[tag]}/min")
    if best >= STUCK_MIN: out.append(f"stuck: {best} identical readings in a row")
    out += [f"range: {v} outside {lo}-{hi}" for _, v in vals if not lo <= v <= hi]
    print(f"{name:<14} {'; '.join(out) if out else 'no failure mode detected'}")
```

Expected output (Python 3.13.5):

```text
KW-01 LEVEL_M  no failure mode detected
KW-02 CL2_MGL  stuck: 20 identical readings in a row
KW-05 FLOW_LS  gap: 7 consecutive missing minutes
KW-07 LEVEL_M  spike: 06:06Z jump 2.96 -> 9.8 exceeds 0.5/min; spike: 06:07Z jump 9.8 -> 2.97 exceeds 0.5/min
```

KW-01 behaves like a slowly filling tank — no finding. KW-02's chlorine is identical for all twenty readings: either the analyser has frozen, the RTU is returning a stored value, or the value is being supplied by something other than the analyser. KW-05 has a seven-minute gap — check the link and polling first (Chapter 13). KW-07 shows a single-sample excursion to 9.80 m and back: a classic noise or scaling glitch, but also exactly what a one-off injected write to a reporting register would look like. Each line is a symptom with a precise description; none is yet a cause.

### 8.5 Choosing thresholds

Set thresholds from evidence, not guesses: look at a week of healthy data per tag, find the largest natural step and the longest natural run of identical values, and set the rule above them with a margin. Record the reason beside the number, and review after every false alarm and every missed event. A stuck-value rule on a tag that legitimately sits at 0.00 (a pump that is off) needs a condition — for example, apply it only while the pump runs.

### 8.6 Practical activity

Add a **drift** check to Lab 8: compare each tag's mean over the first five minutes with its mean over the last five minutes and flag a change larger than a tag-specific limit. Discuss why KW-01's steady rise should *not* be flagged, and what extra information (pump state, inflow) would make drift detection meaningful.

KW-01's steady rise is process behaviour while a pump fills the tank, so a naive mean comparison would flag it wrongly. Drift becomes meaningful when you know the pump state or inflow, or when you compare two sensors that should agree. Set the tag-specific limit from a week of healthy data, and record the reason beside the number.

### 8.7 Common errors and limits

- Treating every bad value as an attack — or none.
- Range checks only.
- Stuck-value rules on tags that legitimately sit still.
- Thresholds with no recorded rationale.
- Lab 8 sees one series at a time; real investigation compares related tags (a pump running while flow is zero is a cross-tag inconsistency).

- Applying a stuck-value rule to a tag that legitimately sits at zero while a pump is off.
- Setting thresholds from a guess instead of from healthy data with a recorded rationale.
- Investigating one series in isolation when a pump-running bit and a zero flow would show a cross-tag fault.

### Exercises — chapter 8

**EX029 — Name the mode.** *Objective:* classify symptoms. *Inputs:* (a) level rises 0.01 m/min while the inlet valve reports closed; (b) flow reads 0.00 for 40 minutes while pump 1 reports running; (c) the historian shows values timestamped 03:00–03:10 that arrived at 03:25; (d) pump 2 does not start after an HMI command and the RTU reports "local". *Steps:* name the mode and two candidate causes each. *Expected evidence:* four rows. *Rubric:* 3 = (a) cross-tag inconsistency/drift — valve feedback fault or a leak/bypass; (b) stuck or cross-tag inconsistency — failed flow meter or frozen value; (c) buffered/stale data — link outage with store-and-forward, or replay; (d) loss of control authority — local switch at site, or interlock; 2 = modes right, causes thin; 1 = partial; 0 = none.

**EX030 — Predict a rule change.** *Objective:* reason about thresholds. *Inputs:* Lab 8 with `STUCK_MIN = 25` and `MAX_STEP["LEVEL_M"] = 7.0`. *Steps:* predict the new output, then run. *Expected evidence:* prediction and actual output. *Rubric:* 3 = KW-02 no longer flagged (20 < 25), KW-07 spike no longer flagged (6.84 < 7.0, 6.83 < 7.0), KW-05 gap still flagged; explains what is lost; 2 = mostly right; 1 = guesses; 0 = none.

**EX031 — Conditional stuck rule.** *Objective:* reduce false alarms. *Inputs:* a flow tag legitimately reads 0.0 when its pump is off. *Steps:* write the rule in pseudocode using pump state. *Expected evidence:* rule and a test case. *Rubric:* 3 = apply stuck detection only while pump state = running for at least the poll interval; includes a test with pump off (no alert) and running with constant non-zero flow (alert); 2 = no test; 1 = disables the rule; 0 = none.

**EX032 — Fault or attack plan.** *Objective:* keep both hypotheses open. *Inputs:* KW-02 stuck at 0.62. *Steps:* list three checks that would point to a fault and three that would point to manipulation, all read-only. *Expected evidence:* six checks. *Rubric:* 3 = fault: analyser local display, RTU analog input diagnostics, maintenance records; manipulation: unexpected writes to the reporting register in captures, configuration session logs, comparison with a manual sample by operations; 2 = one side thin; 1 = one hypothesis only; 0 = none.

### Chapter synthesis

Telemetry fails in a small number of recognizable ways, and each symptom has both ordinary and malicious causes. Detect symptoms with transparent rules — gap, stuck, spike, range — whose thresholds come from healthy data and whose reasons are written down. In-range is not the same as true. Report the symptom precisely and leave the cause to investigation.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 18

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Critical infrastructure and sector security: tools and methods

### Learning outcomes and connection

After this chapter you should be able to:

- choose the right technical tool for a question in a control environment: configuration export, passive capture, protocol decoder, log query, vendor engineering tool or active test;
- implement and verify an integrity check from its published parameters, using DNP3's link-layer CRC as the example;
- explain the difference between an **error-detection code** and **authentication**, and why a valid CRC proves nothing about who sent a frame;
- validate a tool before trusting it: known-answer tests, negative tests and documented versions.

Chapters 7 and 8 used telemetry. This chapter is about the instruments themselves — how to pick them, build small ones correctly and know when they lie.

### 9.1 Choosing a method

| Question | Prefer | Avoid unless scoped |
|---|---|---|
| What is configured? | Configuration export, vendor tool read-only view | Probing ports to infer configuration |
| Who talks to whom? | Flow logs, passive capture on a SPAN port or tap | Active scanning |
| What does a device run? | Asset records, engineering-tool inventory during an approved session | Fingerprinting by probing |
| Does a deny rule work? | Firewall logs plus one scoped connect test | Broad scans |
| Is a frame well-formed? | Decoder with protocol checks (Chapter 2, this chapter) | Eyeballing hex |

The guide to OT security in NIST SP 800-82 Rev. 3 discusses passive monitoring and the risks of active techniques ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)). Packet analysers such as Wireshark include dissectors for Modbus and DNP3; your own scripts are for the checks those tools do not do for you, and for repeatable, reviewable automation.

### 9.2 DNP3 at the link layer

DNP3 is widely used in electricity and water telecontrol. Each link-layer frame starts with a 10-byte header: start bytes `05 64`, a **length** byte, a **control** byte, a 2-byte **destination** and a 2-byte **source** address (little-endian), and a 2-byte **CRC**. User data follow in blocks of up to 16 bytes, each with its own CRC. In the control byte, bit 7 (DIR) is set for frames from the master, bit 6 (PRM) for primary (initiating) frames, and the low four bits are the link function code — for example primary 0 "reset link states", primary 4 "unconfirmed user data", secondary 11 "link status". The DNP Users Group publishes an overview; the full standard is IEEE 1815 ([DNP3 overview](https://www.dnp.org/About/Overview-of-DNP3-Protocol)).

The CRC is **CRC-16/DNP**: polynomial 0x3D65, initial value 0, input and output reflected, final XOR 0xFFFF, with the catalogue check value 0xEA82 for the ASCII string `123456789` ([CRC catalogue](https://reveng.sourceforge.io/crc-catalogue/16.htm)). Reflected, the polynomial is 0xA6BC, which is the constant used in a bit-by-bit implementation.

### 9.3 Validate the tool first

A CRC routine that is subtly wrong still produces numbers. Before using it, run a **known-answer test**: compute the CRC of `123456789` and compare with 0xEA82. Then a **negative test**: change one bit of a valid frame and confirm the check fails. Lab 9 does both — the `assert` line is the known-answer test — and record the Python version, because the result of any tool is evidence only if the tool is identified.

Keep the assert that checks the catalogue value in the script, and fail the job if it does not hold after a change to the CRC function. Record the Python version next to every result that will be used as evidence. Run the negative test on a frame you corrupted yourself, so you know the checker rejects bad CRCs before you trust it on a capture.

### 9.4 Error detection is not authentication

A CRC is computed from public parameters; anyone who can send a frame can compute a valid CRC. It detects accidental corruption, not forgery. Lab 9 shows this directly: a frame from an unknown source address (77) has a **valid** CRC. Telling genuine from forged needs either cryptographic authentication (DNP3 Secure Authentication, or a protected tunnel) or context — known source addresses, known paths, expected timing. Compare Chapter 15 of the technologist book, which uses HMAC (RFC 2104) for authenticity ([RFC 2104](https://www.rfc-editor.org/rfc/rfc2104)).

### 9.5 Worked example: checking SS-3 headers (synthetic)

The Kestrel Grid master (DNP3 address 1) polls substation SS-3's outstation (address 10) through fep-01. A technician captured six link headers.

**Lab 9** (save as `lab09.py`, run with `python3 lab09.py`):

```python
# Lab 9 - check DNP3 link-layer headers and their CRC (offline, standard library only)
# CRC-16/DNP: poly 0x3D65 (reflected 0xA6BC), init 0x0000, reflected in/out, xorout 0xFFFF.
# Synthetic frames between the Kestrel Grid master (address 1) and substation SS-3 outstation (address 10).
import struct
def crc_dnp(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA6BC if crc & 1 else crc >> 1
    return crc ^ 0xFFFF
assert crc_dnp(b"123456789") == 0xEA82          # catalogue check value
def header(length, ctrl, dest, src):
    h = bytes([0x05, 0x64, length, ctrl]) + struct.pack("<HH", dest, src)
    return h + struct.pack("<H", crc_dnp(h))
capture = [
    ("master->SS-3", header(0x05, 0xC0, 10, 1).hex()),     # primary function 0: reset link states
    ("SS-3->master", header(0x05, 0x0B, 1, 10).hex()),     # secondary function 11: link status
    ("master->SS-3", header(0x11, 0xC4, 10, 1).hex()),     # primary function 4: unconfirmed user data
    ("master->SS-3", "056411c40a000100" + "ffff"),          # wrong CRC
    ("unknown->SS-3", header(0x11, 0xC4, 10, 77).hex()),   # source not in station table
    ("master->SS-3", "0565" + header(0x05, 0xC0, 10, 1).hex()[4:]),  # bad start bytes
]
KNOWN_SOURCES = {1}
for label, hx in capture:
    b = bytes.fromhex(hx)
    if b[:2] != b"\x05\x64": print(f"{label:<14} {hx}  REJECT start bytes {b[:2].hex()}"); continue
    got = struct.unpack("<H", b[8:10])[0]; want = crc_dnp(b[:8])
    length, ctrl, dest, src = b[2], b[3], *struct.unpack("<HH", b[4:8])
    if got != want: print(f"{label:<14} {hx}  REJECT crc {got:04x} != {want:04x}"); continue
    direction = "from master" if ctrl & 0x80 else "from outstation"
    note = "" if src in KNOWN_SOURCES or src == 10 else "  ALERT unknown source address"
    print(f"{label:<14} {hx}  ok len={length} ctrl=0x{ctrl:02x} ({direction}, fc={ctrl & 0x0F}) dest={dest} src={src}{note}")
```

Expected output (Python 3.13.5):

```text
master->SS-3   056405c00a000100b1ac  ok len=5 ctrl=0xc0 (from master, fc=0) dest=10 src=1
SS-3->master   0564050b01000a006ded  ok len=5 ctrl=0x0b (from outstation, fc=11) dest=1 src=10
master->SS-3   056411c40a0001000615  ok len=17 ctrl=0xc4 (from master, fc=4) dest=10 src=1
master->SS-3   056411c40a000100ffff  REJECT crc ffff != 1506
unknown->SS-3  056411c40a004d0073e6  ok len=17 ctrl=0xc4 (from master, fc=4) dest=10 src=77  ALERT unknown source address
master->SS-3   056505c00a000100b1ac  REJECT start bytes 0565
```

Three frames are valid and expected. One has CRC `ffff` where `1506` was expected — corruption or a crafted frame; on a noisy link, a run of CRC failures is a link-quality finding for the telecom provider. One has wrong start bytes and is rejected before anything else is read. The most important line is the one that *passes* the CRC: source address 77 is not in the station table. The CRC says the bytes arrived intact; only the address check says they came from somewhere unexpected.

### 9.6 Practical activity

Extend Lab 9 to verify the CRC of each 16-byte user-data block that follows the header. Construct a frame with 17 bytes of user data (one full block and one 1-byte block), compute both block CRCs, and corrupt one byte in the second block to show the check catches it.

Construct the frame with one full sixteen-byte block and a one-byte block, each with its own CRC. Corrupt one byte in the second block and confirm that only that block's check fails. Keep the construction steps in the lab notes so a reviewer can rebuild the same frame.

### 9.7 Common errors and limits

- Trusting a home-made checker without a known-answer test.
- Getting byte order wrong: DNP3 addresses and CRC are little-endian; Modbus fields are big-endian.
- Treating "CRC valid" as "authentic".
- Active probing when a passive source answers the question.
- Lab 9 checks headers only; transport and application layers carry the commands and need their own decoding.

- Mixing Modbus big-endian fields with DNP3 little-endian addresses in the same decoder without stating the byte order.
- Treating a valid CRC as proof of authenticity when the source address is unknown.
- Active probing when a passive capture or a configuration export answers the question.

### Exercises — chapter 9

**EX033 — Known-answer test.** *Objective:* validate a tool. *Inputs:* Lab 9's `crc_dnp`. *Steps:* (1) replace `0xA6BC` with `0x3D65` and run; (2) explain the result. *Expected evidence:* output and explanation. *Rubric:* 3 = the assertion fails because a right-shifting (reflected) algorithm needs the reflected polynomial; the known-answer test caught a plausible bug before any frame was judged; 2 = observes failure without explanation; 1 = attempted; 0 = none.

**EX034 — Decode the control byte.** *Objective:* read DNP3 link fields. *Inputs:* control bytes 0xC9, 0x44 and 0x0B. *Steps:* give DIR, PRM and function code for each and name the function. *Expected evidence:* three rows. *Rubric:* 3 = 0xC9: DIR 1, PRM 1, fc 9 request link status; 0x44: DIR 0, PRM 1, fc 4 unconfirmed user data from an outstation (for example an unsolicited response); 0x0B: DIR 0, PRM 0, fc 11 link status; 2 = one wrong; 1 = bits only; 0 = none.

**EX035 — Forgery thought experiment.** *Objective:* separate integrity and authenticity. *Inputs:* a frame with valid CRC, source address 1 and destination 10, arriving at the outstation from an address on the MPLS network that is not fep-01. *Steps:* explain what the CRC shows, what the address shows and what would actually establish authenticity. *Expected evidence:* short explanation. *Rubric:* 3 = CRC shows no accidental corruption; DNP3 address 1 is self-asserted; authenticity requires Secure Authentication or a cryptographic tunnel terminating at known endpoints, plus network enforcement of the path; 2 = partial; 1 = "valid CRC so genuine"; 0 = none.

**EX036 — Method selection.** *Objective:* pick the least intrusive method. *Inputs:* questions: (a) which DNP3 master addresses SS-3 has seen this month; (b) whether fep-01's firewall permits only the outstation; (c) the outstation's firmware version. *Steps:* choose a method for each and justify. *Expected evidence:* three choices. *Rubric:* 3 = (a) passive capture or fep-01 logs analysed with a decoder; (b) configuration export plus logs, then a scoped test if needed; (c) asset record or vendor tool during an approved session with the protection engineer's agreement; 2 = one intrusive choice; 1 = scanning; 0 = none.

### Chapter synthesis

Pick the least intrusive method that answers the question, and validate every tool before trusting it: known-answer tests, negative tests, recorded versions. DNP3's link-layer CRC shows the discipline in miniature — implement it from published parameters, check it against the catalogue value — and also its limit: error detection proves the bytes arrived intact, never who sent them.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 18

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Critical infrastructure and sector security: control configuration

### Learning outcomes and connection

After this chapter you should be able to:

- translate declared conduits (Chapter 6) into a first-match firewall policy with a default deny;
- evaluate a rule set against test flows in code, and detect **shadowed** and **redundant** rules;
- recognize the configuration patterns that silently widen access — "temporary" broad rules, overlapping "duplicates", any-port allows;
- configure supplier and remote access as time-bound, logged and routed through the management zone;
- plan a configuration change so that it can be verified (Chapter 11) and rolled back.

Chapters 6–9 described and observed the system. This chapter changes it, starting with the control that most directly limits who can reach an unauthenticated protocol: the conduit firewall.

### 10.1 Rule sets as programs

Most network firewalls evaluate rules **top to bottom and apply the first match**. NIST's firewall guide describes policy design, default deny and rule-set management ([SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final)). Thinking of a rule set as a small program clarifies three defects:

- **Shadowed rule**: a later rule whose traffic is entirely matched by an earlier rule with the opposite action. It never takes effect, though its comment says it does.
- **Redundant rule**: a later rule entirely matched by an earlier rule with the same action. Harmless today; confusing tomorrow, when someone deletes the earlier one.
- **Broadening "duplicate"**: a rule that looks like a copy of another but has a wider source, destination or port. It is not redundant; it is a new permission.

Order matters, so every change must be reviewed in context, not as a single line.

### 10.2 Patterns that erode a policy

- **Temporary rules** that outlive their purpose ("allow corporate to control centre for the migration").
- **Any-port** allows (`tcp any`) where a single port was needed.
- **Subnet sources** where one host was needed.
- **Rules without owner, ticket or expiry**.
- **Management access from user zones** instead of through the jump host.

CISA's primary mitigations for operational technology emphasize removing internet exposure, changing default passwords, securing remote access and segmenting IT from OT ([CISA primary mitigations for OT](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology)).

### 10.3 Remote and supplier access

Configure supplier access so that it exists only when needed: the account or path is disabled by default; enabled for a ticketed job and a fixed window; authenticated with multi-factor authentication at the jump host; the session is logged; and an alert fires on any use outside an enabled window. CISA's advisory on PRC state-sponsored actors describes actors maintaining long-term access to critical infrastructure environments, including through valid accounts and remote access ([CISA AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)) — the reason standing access is a finding even when nobody is misusing it today.

### 10.4 Worked example: fw-01 (synthetic)

The policy on `fw-01` between the KVROC zones has seven rules. Lab 10 checks it for shadowing and against five test flows, each with the outcome the conduit list expects.

**Lab 10** (save as `lab10.py`, run with `python3 lab10.py`):

```python
# Lab 10 - evaluate a first-match firewall policy and find shadowed rules (offline, stdlib)
# Synthetic conduit policy for fw-01 between Kestrel Vale zones; addresses are RFC 1918.
from ipaddress import ip_address, ip_network
rules = [  # id, action, source, destination, protocol, port (None = any)
    ("R1", "allow", "10.20.0.10/32", "10.10.0.0/16", "tcp", 502),    # SCADA server polls stations
    ("R2", "allow", "10.20.0.15/32", "10.10.0.0/16", "tcp", 502),    # engineering workstation
    ("R3", "allow", "10.90.0.20/32", "10.20.0.0/24", "tcp", 22),     # jump host to control centre
    ("R4", "allow", "10.30.0.0/16",  "10.20.0.0/24", "tcp", None),   # "temporary" corporate access
    ("R5", "deny",  "10.30.3.0/24",  "10.20.0.0/24", "tcp", 3389),   # intended: block RDP from desks
    ("R6", "allow", "10.20.0.0/24",  "10.10.4.0/24", "tcp", 502),    # duplicate of R1 for KW-04
    ("R7", "deny",  "0.0.0.0/0",     "0.0.0.0/0",    "any", None),   # default deny
]
def matches(rule, src, dst, proto, port):
    _, _, s, d, p, pt = rule
    return (ip_address(src) in ip_network(s) and ip_address(dst) in ip_network(d)
            and p in ("any", proto) and pt in (None, port))
def covers(a, b):   # does earlier rule a match everything rule b matches?
    return (ip_network(b[2]).subnet_of(ip_network(a[2])) and ip_network(b[3]).subnet_of(ip_network(a[3]))
            and a[4] in ("any", b[4]) and a[5] in (None, b[5]))
for i, r in enumerate(rules):
    for earlier in rules[:i]:
        if covers(earlier, r):
            kind = "redundant" if earlier[1] == r[1] else "SHADOWED (never takes effect)"
            print(f"{r[0]} {kind}: fully covered by {earlier[0]}"); break
tests = [("10.20.0.10", "10.10.4.2", "tcp", 502, "allow"), ("10.30.3.7", "10.20.0.5", "tcp", 3389, "deny"),
         ("10.30.3.7", "10.10.4.2", "tcp", 502, "deny"), ("10.30.8.2", "10.20.0.5", "tcp", 445, "deny"),
         ("10.20.0.12", "10.10.4.2", "tcp", 502, "deny")]
for src, dst, proto, port, expect in tests:
    hit = next(r for r in rules if matches(r, src, dst, proto, port))
    status = "PASS" if hit[1] == expect else "FAIL"
    print(f"{status} {src}->{dst} {proto}/{port}: {hit[1]} by {hit[0]} (expected {expect})")
```

Expected output (Python 3.13.5):

```text
R5 SHADOWED (never takes effect): fully covered by R4
PASS 10.20.0.10->10.10.4.2 tcp/502: allow by R1 (expected allow)
FAIL 10.30.3.7->10.20.0.5 tcp/3389: allow by R4 (expected deny)
PASS 10.30.3.7->10.10.4.2 tcp/502: deny by R7 (expected deny)
FAIL 10.30.8.2->10.20.0.5 tcp/445: allow by R4 (expected deny)
FAIL 10.20.0.12->10.10.4.2 tcp/502: allow by R6 (expected deny)
```

Three findings:

1. **R5 is shadowed by R4.** The comment says RDP from corporate desks is blocked, but R4 already allowed all TCP from 10.30.0.0/16, so R5 never applies — the "block" has never worked.
2. **R4 is the real problem.** A "temporary" rule allows every TCP port from the whole corporate zone into the control centre. Its tests fail (RDP and SMB are allowed). Note what the tests do *not* show: corporate desk to station port 502 is denied by R7, so fw-01 does not explain the corporate-desk writes captured at KW-04 in Chapter 2. That path must exist somewhere else; record it as open (Chapter 13 finds it).
3. **R6 is not a duplicate of R1.** It allows the whole control-centre subnet to write to KW-04, including 10.20.0.12, which has no business there.

A sound change: delete R4 (after confirming with the owner what still uses it — the firewall logs will show); move the RDP block above any allow if it is still needed, or rely on the default deny; replace R6 with nothing (R1 and R2 already cover the required paths). Re-run the evaluator with the new rule set before the change and the live tests afterwards (Chapter 11).

### 10.5 Change planning

Every configuration change in a control environment needs: the exact before and after; the reason (finding or requirement); the expected effect, written as tests; a rollback plan; the window agreed with operations; and who verifies. NIST's guide to security-focused configuration management describes baselines and change control ([SP 800-128](https://csrc.nist.gov/pubs/sp/800/128/upd1/final)). The firewall export before and after is evidence; hash it (Chapter 5).

Export and hash the rule set before and after the change, and keep both digests in the change record. Write the expected effect as the same tests Lab 10 runs, so verification is a re-run rather than a new invention. Agree the window with operations, and name who will confirm that SCADA polling still meets the freshness requirement after the change.

### 10.6 Practical activity

Rewrite the fw-01 policy from the conduit list in Chapter 6: one rule per declared conduit, each with ticket and owner in its comment, then the default deny. Run Lab 10 on your version until all five tests pass and no rule is shadowed or redundant. Add two tests of your own for conduit C3.

Put each allow above the default deny, with ticket and owner in the comment. Remove R4 and R6 rather than trying to patch them. Add two tests for conduit C3: jump host to control centre on tcp/22 allowed, and a corporate desk to the same port denied. Re-run until every test passes and no rule is shadowed or redundant.

### 10.7 Common errors and limits

- Reviewing a new rule without reading the rules above it.
- Deleting a broad rule without checking its current users in the logs.
- Treating "looks like a duplicate" as "safe to keep".
- Configuring supplier access as permanently enabled "for emergencies".
- Lab 10 models a stateless first-match policy with exact containment; real firewalls add state, objects, NAT and zones, and their own analysis tools.

- Reviewing a new rule without reading the rules above it that may already allow or deny the same traffic.
- Deleting a broad rule without checking the firewall logs for current users.
- Leaving supplier access permanently enabled for emergencies.

### Exercises — chapter 10

**EX037 — Explain the shadow.** *Objective:* reason about order. *Inputs:* Lab 10. *Steps:* (1) move R5 above R4 and predict the test results; (2) run and compare. *Expected evidence:* prediction and output. *Rubric:* 3 = no shadowing reported; test 2 (RDP) passes (deny by R5); test 4 (SMB) still fails (allow by R4); test 5 still fails (R6); 2 = mostly; 1 = guesses; 0 = none.

**EX038 — Fix the policy.** *Objective:* produce a correct rule set. *Inputs:* Lab 10. *Steps:* remove R4 and R6 (keep R5 or remove it with justification); run. *Expected evidence:* new rule list and output with five PASS lines. *Rubric:* 3 = five PASS lines; justification for R5 (redundant with the default deny once R4 goes, so remove or keep for explicit logging); notes the need to check R4's users in logs first; 2 = passes without justification; 1 = partial; 0 = none.

**EX039 — Supplier access configuration.** *Objective:* configure time-bound access. *Inputs:* the SS-3 relay vendor needs remote access about twice a year. *Steps:* specify the account state, enablement steps, path, authentication, logging, alerting and expiry. *Expected evidence:* a configuration specification. *Rubric:* 3 = disabled by default; enabled by KVROC on-call against a ticket approved by Kestrel Grid; path via jump-01 with MFA and session recording; never directly to the relay network; alert on use outside a window; automatic expiry; next-day review; 2 = one element missing; 1 = "VPN for vendor"; 0 = none.

**EX040 — Detect broadening.** *Objective:* extend the evaluator. *Inputs:* Lab 10's `covers`. *Steps:* add a check that reports when a later rule with the same action *partially* overlaps an earlier one and is broader in source or destination. *Expected evidence:* code and output. *Rubric:* 3 = reports R6 as broadening R1 (source /24 contains R1's /32; destination /24 inside /16; same port), explains why this deserves review; 2 = detects without explanation; 1 = attempted; 0 = none.

### Chapter synthesis

A firewall rule set is a first-match program, and its defects are program defects: shadowed rules that never act, redundant rules that confuse, and look-alike rules that widen access. Configure conduits one rule per declared purpose with a default deny, keep supplier access disabled until needed, and plan every change with its tests and rollback. Then verify, which is the next chapter.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 18

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Critical infrastructure and sector security: verification

### Learning outcomes and connection

After this chapter you should be able to:

- write requirements as testable statements and link each to at least one test (**traceability**);
- design **positive** tests (the needed function still works) and **negative** tests (the forbidden action fails) for every control change;
- refuse to count a test without evidence, and report requirements as verified, failed or untested;
- verify without harming the process: small, scoped tests in agreed windows.

Chapter 10 changed configuration. A change is not finished when it is applied; it is finished when its requirements are shown to hold. This chapter makes that showing systematic.

### 11.1 Requirements that can be tested

"The historian is hardened" cannot be tested. "SSH on hist-02 listens only on 10.90.0.21" can. Write each requirement so that a named test, run by someone else, could fail it. Split compound requirements: "only the SCADA server and engineering workstation reach station tcp/502" needs a positive test (SCADA still polls) **and** a negative test (another control-centre host is refused).

Write each requirement so that a named test could fail it. Split compounds: only the SCADA server and engineering workstation may reach station tcp/502 needs a positive poll from the SCADA server and a negative refusal from another control-centre host. Put the requirement identifiers in the change record before the work starts.

### 11.2 Positive and negative tests

**Negative tests** show a control blocks what it should; **positive tests** show it does not block what operations need. A firewall change that passes all its negative tests but stops historian collection has failed. In control environments the positive tests matter as much as the negative ones: availability is usually the first priority. NIST's testing guide discusses planning and executing technical tests ([SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)); continuous monitoring guidance stresses that control effectiveness must be re-shown over time, not assumed ([SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

### 11.3 Evidence rules

A test counts only if it has: an identifier, the requirement it verifies, the method, the time, the person, the result and an evidence file (Chapter 5). A "config review only" with no recorded output is a useful activity but not a test result. A requirement with no counted test is **untested** — not verified, and not failed. Reporting untested as verified is the single most common way verification misleads.

A config review with no recorded output is useful activity but not a counted test. REQ-6 in Lab 11 stays untested until someone produces a deny line from the collector; reporting it as verified because the rule exists would hide the gap. Keep evidence files next to the test identifiers in the verification record.

### 11.4 Worked example: verifying CHG-2207 (synthetic)

CHG-2207 hardened SSH on hist-02 and was meant to close corporate access to the control centre on fw-01. The verification record:

**Lab 11** (save as `lab11.py`, run with `python3 lab11.py`):

```python
# Lab 11 - requirement-to-test traceability after a hardening change (offline, stdlib)
# Synthetic verification record for change CHG-2207 on HIST-02 and fw-01, 2026-10-12.
requirements = {
 "REQ-1": "SSH listens only on management address 10.90.0.21",
 "REQ-2": "Root cannot log in over SSH",
 "REQ-3": "Corporate desks cannot reach control-centre RDP",
 "REQ-4": "Only SCADA server and engineering workstation reach station tcp/502",
 "REQ-5": "Historian still receives KW-01..KW-12 readings after change",
 "REQ-6": "Firewall denies are logged to the collector",
}
tests = [  # test id, requirement, method, positive/negative, result, evidence
 ("T1", "REQ-1", "listening-socket listing on host", "neg", "pass", "ss-output-0612.txt"),
 ("T2", "REQ-1", "connect to 10.20.0.21:22 from jump host", "neg", "pass", "conn-0614.txt"),
 ("T3", "REQ-2", "root login attempt from jump host", "neg", "pass", "auth-0615.log"),
 ("T4", "REQ-3", "RDP connect from 10.30.3.7", "neg", "fail", "conn-0618.txt"),
 ("T5", "REQ-4", "Modbus read from 10.20.0.12", "neg", "fail", "conn-0620.txt"),
 ("T6", "REQ-4", "Modbus read from SCADA 10.20.0.10", "pos", "pass", "poll-0621.txt"),
 ("T7", "REQ-5", "count stations reporting 06:30-06:40Z", "pos", "pass", "hist-count.csv"),
 ("T8", "REQ-2", "config review only", "neg", "pass", ""),
]
status = {}
for tid, req, method, kind, res, ev in tests:
    if not ev: print(f"{tid} {req} ignored: no evidence file recorded ({method})"); continue
    status.setdefault(req, []).append((tid, kind, res))
for req, text in requirements.items():
    rs = status.get(req, [])
    if not rs: verdict = "UNTESTED"
    elif any(r == "fail" for _, _, r in rs): verdict = "FAILED"
    else: verdict = "verified"
    kinds = "+".join(sorted({k for _, k, _ in rs})) or "-"
    print(f"{req} {verdict:<9} tests={','.join(t for t, _, _ in rs) or '-':<6} kinds={kinds:<7} {text}")
v = sum(1 for r in requirements if status.get(r) and all(x[2] == "pass" for x in status[r]))
print(f"verified {v}/{len(requirements)}; the change is not complete until every requirement is verified")
```

Expected output (Python 3.13.5):

```text
T8 REQ-2 ignored: no evidence file recorded (config review only)
REQ-1 verified  tests=T1,T2  kinds=neg     SSH listens only on management address 10.90.0.21
REQ-2 verified  tests=T3     kinds=neg     Root cannot log in over SSH
REQ-3 FAILED    tests=T4     kinds=neg     Corporate desks cannot reach control-centre RDP
REQ-4 FAILED    tests=T5,T6  kinds=neg+pos Only SCADA server and engineering workstation reach station tcp/502
REQ-5 verified  tests=T7     kinds=pos     Historian still receives KW-01..KW-12 readings after change
REQ-6 UNTESTED  tests=-      kinds=-       Firewall denies are logged to the collector
verified 3/6; the change is not complete until every requirement is verified
```

Three requirements verified, two failed, one untested. REQ-3 failed because R4 was left in place: the ticket said "fix the RDP rule", and the engineer corrected R5 rather than the rule that shadowed it — a common pattern when a change is written as a line edit instead of as a requirement. REQ-4 failed its negative test (10.20.0.12 can still read stations, via R6) while its positive test passed — exactly why both kinds are needed. REQ-6 has no test at all; nobody checked that denies reach the collector, so the detections of Chapter 17 would be blind to denied attempts. T8 was ignored because it has no evidence file. The change goes back to "in progress" with three open items, each with an owner.

### 11.5 Safe verification in control networks

- Prefer reading results the system already records (firewall logs, historian counts) over generating traffic.
- When generating traffic, use a marked test source (for example 10.30.99.9), the smallest possible action (a TCP connect with no payload), and an agreed window with operations informed.
- Never verify a write-block by attempting a write to a live controller; verify it with a connect test and the firewall log, or against a spare device in a lab (Chapter 12).
- Stop at the first unexpected behaviour.

Prefer historian counts and firewall logs over generating traffic. When you must generate traffic, use a marked test source such as 10.30.99.9, a TCP connect with no Modbus payload, and an agreed window with operations informed. Never verify a write-block by writing to a live controller.

### 11.6 Practical activity

Write a test for REQ-6 that does not touch a station: a connect attempt from the marked test desk to a control-centre port that should be denied, then a query on the collector for the matching deny line within 60 s. Add it to Lab 11 as T9 with an evidence file name and re-run.

Use the marked test desk, then query the collector for the matching deny within sixty seconds. Add the test as T9 with an evidence file name and re-run Lab 11 so that REQ-6 moves from untested to verified or failed. Keep the collector query text in the evidence file so the test can be repeated.

### 11.7 Common errors and limits

- Only negative tests; the change breaks operations unnoticed.
- Counting a test without evidence.
- Reporting "5 of 6 tests passed" instead of the status of each requirement.
- Verifying once and assuming forever; re-verify after related changes.
- Lab 11 treats any failing test as a failed requirement; a requirement can also be *partly* verified if a test covers only some of its scope — say so in words.

- Running only negative tests and missing that historian collection stopped.
- Counting a test without an evidence file.
- Reporting five of six tests passed instead of each requirement's status.
- Verifying once and never again after a related change.

### Exercises — chapter 11

**EX041 — Make it testable.** *Objective:* rewrite requirements. *Inputs:* "Remote access is secure", "Time is synchronized", "Logs are kept". *Steps:* rewrite each as one or more testable requirements for KVROC. *Expected evidence:* rewritten requirements with a test idea each. *Rubric:* 3 = specific statements such as "vendor access to SS-3 is possible only via jump-01 with MFA during an enabled window", "all Z2 hosts within 1 s of ntp-ops", "fw-01 allow and deny events reach the collector within 60 s and are retained 12 months"; each with a test; 2 = one vague; 1 = restated; 0 = none.

**EX042 — Add the missing test.** *Objective:* close an untested requirement. *Inputs:* Lab 11 and the activity in 11.6. *Steps:* add T9 for REQ-6 with result pass and evidence file `collector-0630.txt`; run. *Expected evidence:* output. *Rubric:* 3 = REQ-6 verified via T9, total "verified 4/6"; explains that REQ-3 and REQ-4 still block completion; 2 = output only; 1 = attempted; 0 = none.

**EX043 — Positive tests for a firewall change.** *Objective:* protect availability. *Inputs:* the fw-01 fix from EX038. *Steps:* list the positive tests needed before closing the change. *Expected evidence:* list with method and evidence. *Rubric:* 3 = SCADA polls all twelve stations (historian count), engineering workstation can connect to a station in an approved window, jump-01 SSH to Z2 works, hist-02 daily export still arrives; each with evidence source; 2 = some; 1 = none positive; 0 = nothing.

**EX044 — Untested is not verified.** *Objective:* report honestly. *Inputs:* a manager's summary "CHG-2207: 7 of 8 tests passed, done". *Steps:* write the corrected one-paragraph status. *Expected evidence:* paragraph. *Rubric:* 3 = states per-requirement status (3 verified, 2 failed, 1 untested), names the open items and owners, says the change is not complete; 2 = correct but no owners; 1 = minor edit; 0 = none.

### Chapter synthesis

Verification turns a configuration change into a demonstrated result. Write requirements that can fail, test each with positive and negative tests, count only tests with evidence, and report each requirement as verified, failed or untested. In control networks, verify with the smallest scoped actions, and never by experimenting on the live process.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 18

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes and connection

After this chapter you should be able to:

- build a **contained** laboratory in which protocol behaviour can be studied without any network or real device;
- implement a minimal Modbus/TCP responder with a **write policy**: which registers may be written, within which value range;
- generate and read Modbus **exception responses** (illegal function, illegal data address, illegal data value);
- assess a lab against a rubric: containment, reproducibility, evidence and honesty about what the lab does not model.

Chapters 1–11 analysed traffic and configuration. This chapter builds something you can safely break. It is the first of two assessed laboratories; Chapter 17 is the second.

### 12.1 What "contained" means

A contained lab cannot affect anything outside itself. In this book that is guaranteed technically, not by good intentions: Lab 12 uses `socket.socketpair()`, which creates two connected sockets **inside one process** ([Python socket](https://docs.python.org/3/library/socket.html)). Nothing listens on a port, nothing is routed, and the program cannot reach a real controller even by mistake. Larger labs use isolated virtual networks with no route out, or spare hardware on a bench with its network cable going nowhere else. Write down the containment property of every lab you build, and how you checked it.

### 12.2 The responder's job

A real controller decides whether to execute a write based on its own logic, which in classic Modbus devices often means "always". Some devices and protocol gateways allow write protection by register range; many do not. The lab responder makes the policy explicit:

- **reads** of holding registers (function 3) are allowed within the table, quantity 1–125 (the protocol's limit for one read);
- **writes** of single registers (function 6) are allowed only to register 7, the pump setpoint, and only for values 100–400;
- anything else returns an **exception**: the function code with its high bit set (code + 0x80) and an exception code — 01 illegal function, 02 illegal data address, 03 illegal data value — as defined in the Modbus Application Protocol specification ([Modbus specifications](https://www.modbus.org/modbus-specifications)).

A normal response to function 6 echoes the request. A normal response to function 3 carries a byte count and the register values.

### 12.3 Logging inside the device

The responder logs every read, every accepted write with its old and new value, and every exception. On real equipment these are exactly the records you wished you had in Chapter 7. A burst of exception 02 responses from one source is a strong sign of someone mapping the register space; a run of exception 03 is someone testing limits.

On real equipment those logs are often missing, which is why the lab makes them visible. A burst of illegal-address exceptions from one source is a mapping sign; a run of illegal-value exceptions is someone testing limits. Keep the lab log with the hex responses so a reviewer can match each exception to a request.

### 12.4 Worked example: the bench responder (synthetic)

**Lab 12** (save as `lab12.py`, run with `python3 lab12.py`):

```python
# Lab 12 - contained Modbus/TCP responder with a write policy (offline, standard library only)
# Uses socket.socketpair(): both ends live inside this process; nothing touches a real network.
import socket, struct
regs = [0] * 10; regs[0], regs[1], regs[7] = 342, 61, 250      # level cm, chlorine x100, pump setpoint
WRITABLE = {7: (100, 400)}                                      # register: allowed value range
log = []
def respond(req: bytes) -> bytes:
    tid, pid, length, unit, fc = struct.unpack(">HHHBB", req[:8])
    def exc(code):
        log.append(f"tid={tid} fc={fc} exception {code}")
        return struct.pack(">HHHBBB", tid, 0, 3, unit, fc | 0x80, code)
    if pid != 0 or length != len(req) - 6: return exc(3)
    if fc == 3:
        addr, qty = struct.unpack(">HH", req[8:12])
        if not 1 <= qty <= 125 or addr + qty > len(regs): return exc(2)
        data = struct.pack(f">{qty}H", *regs[addr:addr + qty])
        log.append(f"tid={tid} read {addr}..{addr + qty - 1}")
        return struct.pack(">HHHBBB", tid, 0, 3 + len(data), unit, 3, len(data)) + data
    if fc == 6:
        addr, val = struct.unpack(">HH", req[8:12])
        if addr not in WRITABLE: return exc(2)
        lo, hi = WRITABLE[addr]
        if not lo <= val <= hi: return exc(3)
        old, regs[addr] = regs[addr], val
        log.append(f"tid={tid} WRITE reg {addr} {old}->{val}")
        return req[:12]                                         # echo is the normal fc 6 reply
    return exc(1)
client, server = socket.socketpair()
def call(tid, fc, a, b):
    client.sendall(struct.pack(">HHHBBHH", tid, 0, 6, 1, fc, a, b))
    server.sendall(respond(server.recv(260)))
    r = client.recv(260)
    return r.hex()
print("read 0..2     ", call(1, 3, 0, 3))
print("write 7=300   ", call(2, 6, 7, 300))
print("write 7=900   ", call(3, 6, 7, 900))
print("write 0=0     ", call(4, 6, 0, 0))
print("fc 8 diag     ", call(5, 8, 0, 0))
print("read 8..12    ", call(6, 3, 8, 5))
client.close(); server.close()
print("registers", regs[:3], "setpoint", regs[7])
for entry in log: print("log:", entry)
```

Expected output (Python 3.13.5):

```text
read 0..2      0001000000090103060156003d0000
write 7=300    00020000000601060007012c
write 7=900    000300000003018603
write 0=0      000400000003018602
fc 8 diag      000500000003018801
read 8..12     000600000003018302
registers [342, 61, 0] setpoint 300
log: tid=1 read 0..2
log: tid=2 WRITE reg 7 250->300
log: tid=3 fc=6 exception 3
log: tid=4 fc=6 exception 2
log: tid=5 fc=8 exception 1
log: tid=6 fc=3 exception 2
```

Read the hex responses. The first is a normal read: `03 06` (function 3, six bytes) followed by 0x0156 = 342, 0x003D = 61 and 0. The write of 300 to register 7 is echoed and the log records 250 → 300. Writing 900 returns `86 03` — function 6 + 0x80, exception 3, illegal value. Writing register 0 returns `86 02`, illegal address — register 0 is a measurement, not writable. Function 8 (diagnostics) returns `88 01`, illegal function. A read of five registers starting at 8 runs past the 10-register table and returns `83 02`. The registers at the end show that only the approved write took effect.

### 12.5 Assessment rubric for a contained lab

| Criterion | 3 (excellent) | 1 (weak) |
|---|---|---|
| Containment | Technically impossible to reach a real device; property stated and checked | Relies on "I won't point it at anything" |
| Reproducibility | Fixed inputs; exact output recorded with Python version | Output varies or is not recorded |
| Fidelity statement | Lists what the lab models and what it does not | Claims to represent real devices |
| Evidence | Logs and outputs kept, hashed, linked to exercises | Screenshots only |
| Safety of extension | Changes reviewed so they cannot remove containment | Adds real network code without review |

### 12.6 What the lab does not model

Real devices differ: some ignore unit identifiers, some accept writes to any register, some crash on malformed requests, and few log anything. The responder handles one request at a time, has no concurrency, timeouts or partial reads. Its value is in making policy and exceptions visible, not in predicting a particular vendor's behaviour. Never use results from a lab to decide how a live device will respond to a test.

Never use lab results to decide how a live device will respond to a test. Real devices differ in unit-identifier handling, write protection and logging, and many crash on malformed requests. State those gaps in the assessment, and keep live verification to scoped, authorized methods from Chapter 11.

### 12.7 Practical activity

Add function 16 (write multiple registers) to the responder with the same policy: every register in the range must be writable and every value in limits, or the whole write is refused. Test four cases: all allowed; one address not writable; one value out of range; byte count inconsistent with quantity.

Refuse the whole write if any register is not writable or any value is out of limits. Test all allowed, one address not writable, one value out of range, and a byte count that does not match the quantity. Record the four hex responses and the log lines next to them.

### 12.8 Common errors and limits

- Using a real network socket "just for testing" and leaving it bound to all interfaces.
- Accepting partial multi-register writes.
- Forgetting the response for function 6 is an echo, then mis-parsing it.
- Treating lab behaviour as vendor behaviour.

- Binding a real listening socket for testing and leaving it on all interfaces.
- Accepting a partial multi-register write that changes some registers before refusing others.
- Treating the lab's exception behaviour as a vendor's behaviour. State containment as a technical property in every lab report.

### Exercises — chapter 12

**EX045 — Read the responses.** *Objective:* decode exception and normal replies. *Inputs:* Lab 12 output. *Steps:* for each of the six responses, give the transaction id, function (with or without exception bit), and meaning. *Expected evidence:* six rows. *Rubric:* 3 = all six correct, including 0x86 = exception to 6, 0x88 = exception to 8, 0x83 = exception to 3; 2 = one wrong; 1 = normal replies only; 0 = none.

**EX046 — Implement function 16.** *Objective:* extend the responder safely. *Inputs:* activity 12.7. *Steps:* implement and run the four cases. *Expected evidence:* code and outputs. *Rubric:* 3 = all-or-nothing behaviour; exception 02 for a non-writable address, 03 for an out-of-range value, 03 (or a malformed-request handling with justification) for an inconsistent byte count; normal reply echoes address and quantity only; log lines for each; 2 = works with one wrong code; 1 = partial writes accepted; 0 = none.

**EX047 — Detect mapping attempts.** *Objective:* use device-side logs. *Inputs:* the responder's log. *Steps:* write a rule that alerts on mapping or limit-testing behaviour and test it by adding five reads of out-of-range addresses from one transaction sequence. *Expected evidence:* rule and output. *Rubric:* 3 = for example "≥3 exception-02 responses within 60 s from one source"; demonstrates it fires on the test and not on the original six requests (which contain only two exception-02 replies; counting 02 and 03 together would already reach three and fire); 2 = fires on both; 1 = rule only; 0 = none.

**EX048 — Assess a lab.** *Objective:* apply the rubric. *Inputs:* a colleague's lab that runs a Modbus server on `0.0.0.0:502` on a laptop "only used in the office". *Steps:* score it on containment and fidelity and propose a fix. *Expected evidence:* scores and fix. *Rubric:* 3 = containment 1 (reachable from any network the laptop joins, and the laptop may be taken to stations); fix with socketpair or loopback-only binding plus host firewall, or an isolated VM network; fidelity statement required; 2 = fix without reasoning; 1 = accepts it; 0 = none.

### Chapter synthesis

A contained lab is one where safety is a technical property. Lab 12 builds a Modbus responder that enforces a write policy and returns proper exceptions, making visible what most real devices hide: which requests were refused and why. Assess every lab for containment, reproducibility, evidence and a candid statement of what it does not model.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 18

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Critical infrastructure and sector security: troubleshooting

### Learning outcomes and connection

After this chapter you should be able to:

- apply a structured troubleshooting method — define the symptom, collect read-only observations, list hypotheses, test predictions, preserve, then change;
- eliminate hypotheses by comparing what each predicts with what you observed, in a way others can check;
- recognize when a fault investigation becomes a security incident, and what to preserve at that moment;
- keep a **troubleshooting log** that is also evidence.

Chapter 8 described symptoms; Chapters 7, 9 and 11 gave you observations. This chapter puts them together under time pressure, when a station has gone quiet and operators want it back.

### 13.1 The method

1. **Define the symptom** precisely: which tag, since when (UTC), how detected, what still works.
2. **Collect read-only observations** in order of cost: other stations' status; link and router counters; firewall logs; a TCP connect test from the normal polling source; a protocol read; device configuration records.
3. **List hypotheses** — at least one ordinary and one security-relevant — before testing any.
4. **Write each hypothesis's predictions**: what would you observe if it were true?
5. **Compare** predictions with observations. A hypothesis contradicted by a reliable observation is refuted; one consistent with all of them stays.
6. **Preserve** anything that might be evidence before changing it (Chapter 5).
7. **Change** one thing, under a change record, and verify (Chapter 11).
8. **Record** the cause, the evidence, and what would have detected it sooner.

The discipline of writing predictions *before* comparing is what stops the first plausible story from becoming the conclusion.

### 13.2 From fault to incident

A troubleshooting exercise becomes a possible incident when an observation is unexplained by any approved activity: an unapproved configuration session, an unknown source, a changed file with no change record. At that point stop changing things, preserve (configuration, logs, session records), and hand over through the incident process. NIST's incident response recommendations place this decision within the organization's broader risk management ([SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). The technician's job is not to decide that an attack happened; it is to notice that the explanation is missing and to keep the evidence intact.

### 13.3 Worked example: KW-09 goes quiet (synthetic)

At 07:05Z on 12 October, KW-09's readings stop arriving; all other stations are fine. You collect read-only observations for fifteen minutes and list five hypotheses.

**Lab 13** (save as `lab13.py`, run with `python3 lab13.py`):

```python
# Lab 13 - eliminate hypotheses for "KW-09 readings missing" (offline, standard library only)
# Synthetic observations collected read-only between 07:05 and 07:20Z on 2026-10-12.
observed = {
 "rtu_ping": True,              # RTU answers ICMP from the SCADA server
 "tcp502_handshake": True,      # TCP connect to 10.10.9.2:502 succeeds from SCADA server
 "modbus_reply": "exception 2", # read of registers 0..3 returns illegal data address
 "fw_denies": False,            # no fw-01 denies for 10.10.9.2 in the window
 "radio_errors": False,         # cellular router CRC/error counters flat
 "rtu_config_changed": True,    # rtu-kw09 config session at 06:41Z (clock-corrected) by user eng
 "change_ticket": False,        # no approved change ticket for KW-09 today
 "other_stations_ok": True,
}
hypotheses = {  # what each hypothesis predicts we would observe
 "H1 radio/link failure":           {"rtu_ping": False, "tcp502_handshake": False, "radio_errors": True},
 "H2 firewall change blocks polls": {"tcp502_handshake": False, "fw_denies": True},
 "H3 SCADA server fault":           {"other_stations_ok": False},
 "H4 RTU register map changed":     {"rtu_ping": True, "tcp502_handshake": True, "modbus_reply": "exception 2",
                                     "rtu_config_changed": True},
 "H5 RTU powered off":              {"rtu_ping": False},
}
for h, pred in hypotheses.items():
    clash = [k for k, v in pred.items() if observed[k] != v]
    print(f"{h:<32} {'REFUTED by ' + ', '.join(clash) if clash else 'CONSISTENT with all observations'}")
print("unapproved RTU configuration session -> preserve RTU config and session logs, then treat as possible incident"
      if observed["rtu_config_changed"] and not observed["change_ticket"] else "change was approved")
```

Expected output (Python 3.13.5):

```text
H1 radio/link failure            REFUTED by rtu_ping, tcp502_handshake, radio_errors
H2 firewall change blocks polls  REFUTED by tcp502_handshake, fw_denies
H3 SCADA server fault            REFUTED by other_stations_ok
H4 RTU register map changed      CONSISTENT with all observations
H5 RTU powered off               REFUTED by rtu_ping
unapproved RTU configuration session -> preserve RTU config and session logs, then treat as possible incident
```

Four hypotheses are refuted by specific observations: the link is up (ping, handshake, flat error counters); the firewall is not denying; the SCADA server is polling other stations successfully; the RTU is powered. One remains consistent: the RTU's register map changed, so the SCADA server's reads now hit addresses the device no longer has — exception 02, exactly as in the Chapter 12 lab. And the RTU logged a configuration session at 06:41Z (clock-corrected) with no change ticket.

That last observation turns a fault into a possible incident. The correct next steps are: preserve the RTU's current configuration export and its session log, and the jump-host and engineering-workstation logs for 06:30–06:50Z; inform the Kestrel Water duty manager that KW-09 values are unavailable (they may need a site visit for manual readings); open an incident record. Restoring the previous configuration is the fix — but only after preservation and with the incident lead's agreement.

### 13.4 Second case: the corporate desk at KW-04

Chapter 10 left an open item: fw-01 denies corporate-desk traffic to stations, yet a capture at KW-04 showed writes from 10.30.3.7. Hypotheses: (a) the capture's source address was translated by some device; (b) another path to KW-04 exists that bypasses fw-01. Read-only checks: the KW-04 cellular router's configuration export shows a port-forward of tcp/502 from its carrier-side private address, and the carrier's private network is also reachable from the corporate remote-access VPN. Hypothesis (b) is consistent; the path was installed during a 2024 commissioning and never removed. The lesson is architectural (Chapter 15): every station router is a potential boundary, and the model in Chapter 6 must include it.

### 13.5 The troubleshooting log

Write as you go, in UTC, with the four labels: *observed*, *inferred*, *done*, *open*. A good log lets a colleague taking over at shift change continue without asking you anything, and lets an investigator later reconstruct what was changed and when. Chapter 16 gives a template; Chapter 18 seals it as project evidence.

Write as you go in UTC with the four labels, so a colleague at shift change can continue without asking you anything. Include evidence references for each observation, such as the RTU config export hash and the jump-host log interval. Chapter 16 gives a template; Chapter 18 seals the log as project evidence.

### 13.6 Practical activity

Add hypothesis H6 "RTU firmware crashed into a degraded mode" to Lab 13 with predictions you think it makes, and observe whether the existing observations refute it. If they do not, name the single additional read-only observation that would.

If the existing observations do not refute H6, name one additional read-only check, such as a vendor diagnostic that reports firmware state, that would. Write the predictions before you invent the check, so the new observation has something to contradict. Keep H6 in the list until it is refuted or the incident process takes over.

### 13.7 Common errors and limits

- Rebooting first, which destroys volatile evidence and often hides the cause.
- Testing hypotheses one at a time and stopping at the first that "fits".
- Treating a consistent hypothesis as proven; it is only *not yet refuted*.
- Changing several things at once.
- Lab 13 compares exact predicted values; real observations have uncertainty, and a single unreliable observation should not refute a hypothesis on its own.

- Rebooting first and destroying volatile evidence.
- Stopping at the first hypothesis that fits instead of testing predictions against all observations.
- Treating a consistent hypothesis as proven; it is only not yet refuted.
- Changing several things at once so that the fix cannot be attributed.

### Exercises — chapter 13

**EX049 — Predictions first.** *Objective:* practise the method. *Inputs:* KW-05's seven-minute gap from Chapter 8. *Steps:* list three hypotheses with their predictions for ping, TCP handshake, Modbus reply, radio counters and other stations. *Expected evidence:* a table. *Rubric:* 3 = at least one link hypothesis, one polling/SCADA hypothesis and one security-relevant hypothesis, with distinct predictions so that observations could separate them; 2 = overlapping predictions; 1 = hypotheses only; 0 = none.

**EX050 — Add H6.** *Objective:* extend the lab. *Inputs:* activity 13.6. *Steps:* implement and run. *Expected evidence:* code, output and the extra observation. *Rubric:* 3 = plausible predictions (for example ping true, handshake true, reply timeout or exception 04); recognizes that if H6 predicts exception 02 it is not refuted, and proposes a read-only check such as the RTU's diagnostic page or uptime counter; 2 = runs without reasoning; 1 = attempted; 0 = none.

**EX051 — The moment of escalation.** *Objective:* recognize when to stop and preserve. *Inputs:* the KW-09 case. *Steps:* write the escalation message to the incident lead and the list of items preserved, with times. *Expected evidence:* message and list. *Rubric:* 3 = message states observed facts and the unexplained session, separates inference, asks for a decision on restoration; preserved items include RTU config export and session log, jump-01 and eng-ws-15 logs for the window, the troubleshooting log itself, each with hash; 2 = good but no hashes; 1 = "we've been hacked"; 0 = none.

**EX052 — Close the KW-04 path.** *Objective:* fix the bypass found in 13.4. *Inputs:* the router port-forward and the VPN reachability. *Steps:* propose the change, its preservation step, its tests and its owner. *Expected evidence:* change plan. *Rubric:* 3 = preserve router config first; remove the port-forward; restrict carrier private network from the corporate VPN; negative test from a marked VPN client and positive test of SCADA polling; check all other station routers for the same pattern; owner named; 2 = fix without broad check; 1 = remove only; 0 = none.

### Chapter synthesis

Troubleshooting in a critical service is a method, not a hunch: define the symptom, observe read-only, write hypotheses with predictions, eliminate by evidence, preserve, then change one thing and verify. When an observation is unexplained by approved activity, the fault has become a possible incident; stop, preserve and escalate. The log you keep is both the shift handover and the evidence.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue studying — chapter 13 of 18

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Critical infrastructure and sector security: automation

### Learning outcomes and connection

After this chapter you should be able to:

- automate configuration **drift detection** with cryptographic hashes and an approved manifest;
- classify differences as missing, new, approved change or unapproved change, and act differently on each;
- design automation that is safe in control environments: read-only by default, small blast radius, preserve-before-revert, and human approval for anything that touches the process;
- protect the automation itself, since a tool that can change every host is a target.

Chapters 10–13 changed, verified and troubleshot by hand. This chapter makes the repeatable checks automatic, so that a technician's attention goes to the differences that matter.

### 14.1 Why hashes

A SHA-256 digest ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)) of a file changes if any byte changes, and it is infeasible to construct a different file with the same digest. Comparing digests against a manifest recorded at a known-good moment tells you **which** files changed, cheaply and without storing copies. It does not tell you **how** they changed — for that you need the approved copy, kept in version control — and it does not tell you **whether** the change was legitimate — for that you need the change records. Python's `hashlib` provides SHA-256 in the standard library ([Python hashlib](https://docs.python.org/3/library/hashlib.html)).

### 14.2 Four outcomes, four actions

| Outcome | Meaning | Action |
|---|---|---|
| Unchanged | Matches the manifest | Nothing |
| Changed, approved | A change record covers it | Verify (Chapter 11), then update the manifest |
| Changed, unapproved | No record | **Preserve**, investigate, then revert under a change |
| New or missing | File appeared or vanished | Investigate before deleting or restoring |

The most dangerous automation mistake is "revert all drift automatically". It destroys the evidence of an unapproved change and may undo an emergency fix made at 03:00 that has not yet been written up. Automated *detection* is cheap and safe; automated *correction* needs a short, explicit list of what may be auto-fixed, and nothing that touches process control.

### 14.3 Worked example: drift on hist-02 (synthetic)

A nightly job compares hist-02's key files with the manifest approved after CHG-2207. Lab 14 simulates one night, using a temporary directory.

**Lab 14** (save as `lab14.py`, run with `python3 lab14.py`):

```python
# Lab 14 - detect configuration drift against an approved manifest (offline, standard library only)
# Files are created in a temporary directory that is removed at the end.
import hashlib, json, pathlib, tempfile
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory() as tmp:
    root = pathlib.Path(tmp)
    files = {"sshd_config": "ListenAddress 10.90.0.21\nPermitRootLogin no\nPasswordAuthentication no\n",
             "ntp.conf": "server 10.90.0.5 iburst\n",
             "fw-01.rules": "R1 allow 10.20.0.10 10.10.0.0/16 tcp 502\nR7 deny any any\n"}
    for n, t in files.items(): (root / n).write_text(t)
    manifest = {n: sha(root / n) for n in files}                       # approved baseline
    approved_changes = {"ntp.conf": "CHG-2210"}
    (root / "ntp.conf").write_text("server 10.90.0.5 iburst\nserver 10.90.0.6 iburst\n")   # approved
    (root / "sshd_config").write_text(files["sshd_config"].replace("PermitRootLogin no", "PermitRootLogin yes"))
    (root / "debug.sh").write_text("nc -l -p 9000\n")                  # new, unexpected file
    current = {p.name: sha(p) for p in sorted(root.iterdir())}
    for name in sorted(set(manifest) | set(current)):
        if name not in current: print(f"MISSING   {name}")
        elif name not in manifest: print(f"NEW       {name}  -> investigate before removing")
        elif current[name] != manifest[name]:
            tag = f"approved ({approved_changes[name]}) -> update baseline" if name in approved_changes else "UNAPPROVED -> preserve, then revert"
            print(f"CHANGED   {name}  {tag}")
        else: print(f"unchanged {name}")
    print("manifest digest", hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()[:16])
```

Expected output (Python 3.13.5):

```text
NEW       debug.sh  -> investigate before removing
unchanged fw-01.rules
CHANGED   ntp.conf  approved (CHG-2210) -> update baseline
CHANGED   sshd_config  UNAPPROVED -> preserve, then revert
manifest digest fdea74f1d09e359c
```

`fw-01.rules` is unchanged. `ntp.conf` changed and CHG-2210 covers it (a second NTP server was added): verify that time is synchronized, then update the manifest. `sshd_config` changed with no record — someone re-enabled root login. `debug.sh` is new and contains a listener command. Both are preserved (copy, hash, timestamps, the account that last wrote them if the host records it) before anything is reverted, and the second is very likely to become an incident. The manifest's own digest is printed so that the manifest itself can be checked; store that digest somewhere the host's administrators cannot change (Chapter 18).

### 14.4 Safe automation in control environments

- **Read-only first.** Most valuable automation only collects and compares: configurations, firmware versions, account lists, firewall rules, certificate expiry.
- **Small blast radius.** Act on one host or a few; halt if many hosts differ in the same way, which usually means the desired state or the collector is wrong.
- **Rate and timing.** Collection traffic to field devices must respect the poll budget (Chapter 1) and never run during process-critical periods without agreement.
- **Human approval** for every change that could affect the process, however small.
- **Log every run** to the collector, with what was read and what was changed.

### 14.5 Protecting the automation

The automation account can read or change every host it manages, so: keep its credentials in a vault and rotate them; restrict where it may connect from; require review of changes to its desired state; alert on runs outside the schedule. The CISA advisory on long-term access to critical infrastructure describes actors using legitimate administration tools and valid accounts ([CISA AA24-038A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a)); an over-privileged automation account is exactly such a tool.

Keep automation credentials in a vault, restrict where the account may connect from, and alert on runs outside the schedule. A tool that can change every host is as attractive to an adversary as an engineering workstation. Review changes to its desired state the same way you review firewall changes.

### 14.6 Practical activity

Extend Lab 14 so that, for an unapproved change, it writes a preservation record — file name, old digest, new digest, size and modification time — into the temporary directory before printing the finding, and prints the preservation record's own SHA-256.

Write the preservation record before printing the finding, and include the record's own digest in the output. That way a later investigator can show that the copy taken at detection time matches what the job claimed to save. Keep the temporary directory's cleanup after the hashes are recorded.

### 14.7 Common errors and limits

- Automatic revert of all drift.
- Manifests stored on the host they protect.
- Hashing only; no approved copy to compare content with.
- Automation polling field devices aggressively and degrading the process.
- Lab 14 ignores permissions, ownership and timestamps, which matter as much as content (a world-writable service file is drift).

- Automatically reverting all drift and destroying evidence of an unapproved change.
- Storing the manifest on the host it protects.
- Hashing content only and ignoring permissions that make a service file world-writable.
- Polling field devices so aggressively that the poll cycle fails.

### Exercises — chapter 14

**EX053 — Classify and act.** *Objective:* apply the four outcomes. *Inputs:* Lab 14 output. *Steps:* write the action and owner for each line, in order of execution. *Expected evidence:* ordered list. *Rubric:* 3 = preserve sshd_config and debug.sh first (copy, hash, metadata), notify security lead; investigate debug.sh before removal; revert sshd_config under a change after preservation; verify NTP and update manifest for ntp.conf; nothing for fw-01.rules; 2 = order wrong; 1 = revert all; 0 = none.

**EX054 — Auto-fix list.** *Objective:* limit automation. *Inputs:* candidate auto-fixes: re-enable log forwarding, reset sshd_config, restart historian service, correct NTP server list, push firewall rules, re-set PLC setpoint. *Steps:* mark each as auto-fix, ticket, or never-automate, with reasons. *Expected evidence:* six rows. *Rubric:* 3 = log forwarding and NTP list auto-fix (restore visibility and time, low process risk); sshd_config and firewall push ticketed (preservation and lock-out risk); historian restart ticketed with operations; PLC setpoint never automated by security tooling; 2 = one wrong; 1 = all auto; 0 = none.

**EX055 — Halt guard.** *Objective:* reduce blast radius. *Inputs:* a fleet of 14 hosts; on one night 9 show `ntp.conf` changed identically. *Steps:* propose a guard condition and explain what the pattern likely means. *Expected evidence:* guard and explanation. *Rubric:* 3 = halt when more than a set share (for example 25 %) of hosts show the same change; most likely an unrecorded but deliberate fleet change or a wrong manifest — confirm with the change calendar before any action; still treat as a finding until explained; 2 = guard without interpretation; 1 = revert all nine; 0 = none.

**EX056 — Preservation record.** *Objective:* extend the lab. *Inputs:* activity 14.6. *Steps:* implement and show output. *Expected evidence:* code and output. *Rubric:* 3 = record written before the finding line, contains the required fields, its digest printed; explains why the record's digest must be stored off-host; 2 = record without digest; 1 = attempted; 0 = none.

### Chapter synthesis

Automate the checks that never change: collect, hash, compare with an approved manifest and classify differences. Act differently on approved, unapproved, new and missing items — preserve before you revert, and keep automatic correction to a short list that never touches the process. Protect the automation as the powerful tool it is.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue studying — chapter 14 of 18

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Critical infrastructure and sector security: integration and dependencies

### Learning outcomes and connection

After this chapter you should be able to:

- model technical dependencies — virtualization, directory, time, storage, telecom, power — as a graph and compute what a single failure affects;
- find components shared across services and sectors, including indirect sharing through a dependency of a dependency;
- treat every integration point (station routers, carrier networks, vendor gateways, data exports) as a boundary to be modelled, controlled and monitored;
- turn a dependency analysis into concrete checks and controls.

Chapter 13 found a path to KW-04 that bypassed the firewall through a carrier network. That was a dependency nobody had drawn. This chapter draws them systematically.

### 15.1 Interdependency

Critical infrastructures depend on each other physically (power for pumps), through information (telemetry over a carrier network), geographically (shared ducts and sites) and logically (shared staff, software and administration). This classification comes from Rinaldi, Peerenboom and Kelly's widely cited paper ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131)). For a technician the most frequent surprises are *logical*: a directory, a hypervisor cluster, a time source or a monitoring collector shared by systems whose owners each think it is theirs.

For a technician the most frequent surprises are logical: a directory, a hypervisor or a time source that several services share without any one owner claiming them. Draw those first, then the physical and carrier links. Lab 15 makes the shared nodes visible as counts across services.

### 15.2 Dependencies as a graph

Write each dependency as "A needs B". To find what fails when B fails, follow the edges **backwards** — everything that needs B, everything that needs those, and so on. That is a breadth-first search on the reversed graph. Two results matter: the **set of services** affected, and the **path** by which each is affected, because the path tells you where a control or a redundancy would break the chain.

Indirect sharing is the important case. In the KVROC model the hospital BMS server and the SCADA server both authenticate against `ad-ops`, which runs on `esx-03`, while the grid front end also runs on `esx-03`. No service owner lists `esx-03` as "theirs"; all three depend on it.

### 15.3 Worked example: KVROC dependencies (synthetic)

**Lab 15** (save as `lab15.py`, run with `python3 lab15.py`):

```python
# Lab 15 - trace failure impact through technical dependencies (offline, standard library only)
# Synthetic dependency map for the Kestrel Vale operations centre: "A needs B" edges.
from collections import deque
needs = {
 "water-telemetry": ["scada-01", "cell-router-kw", "fw-01"],
 "scada-01": ["ad-ops", "ntp-ops", "hist-02", "esx-02"],
 "hist-02": ["esx-02", "san-01"],
 "hospital-bms": ["bms-server", "fw-02"],
 "bms-server": ["esx-02", "ad-ops"],
 "grid-ss3-telecontrol": ["fep-01", "telco-mpls"],
 "fep-01": ["ntp-ops", "esx-03"],
 "ad-ops": ["esx-03"],
 "ntp-ops": ["gps-clock"],
}
def impacted(failed):
    rev = {}
    for a, bs in needs.items():
        for b in bs: rev.setdefault(b, []).append(a)
    seen, q = set(), deque([failed])
    while q:
        for a in rev.get(q.popleft(), []):
            if a not in seen: seen.add(a); q.append(a)
    return sorted(seen)
services = {"water-telemetry", "hospital-bms", "grid-ss3-telecontrol"}
for comp in ["esx-02", "esx-03", "gps-clock", "san-01", "telco-mpls"]:
    hit = impacted(comp)
    print(f"{comp:<10} -> services {sorted(services & set(hit))} via {len(hit)} dependants")
counts = {c: len(services & set(impacted(c))) for c in {b for bs in needs.values() for b in bs}}
print("shared by all three services:", sorted(c for c, n in counts.items() if n == 3))
```

Expected output (Python 3.13.5):

```text
esx-02     -> services ['hospital-bms', 'water-telemetry'] via 5 dependants
esx-03     -> services ['grid-ss3-telecontrol', 'hospital-bms', 'water-telemetry'] via 7 dependants
gps-clock  -> services ['grid-ss3-telecontrol', 'water-telemetry'] via 5 dependants
san-01     -> services ['water-telemetry'] via 3 dependants
telco-mpls -> services ['grid-ss3-telecontrol'] via 1 dependants
shared by all three services: ['esx-03']
```

`esx-02` hosts the SCADA server, the historian and the BMS server, so its failure affects water and hospital monitoring. `esx-03` is the only component that affects all three services — directly for the grid front end, indirectly through the directory for the other two. `gps-clock`, the reference for `ntp-ops`, affects water and grid: losing it does not stop anything immediately, but Chapter 7 showed what drifting clocks do to every later investigation. `telco-mpls` affects only the grid, and `san-01` only water.

Technical actions follow: the directory needs a second domain controller on a different host (and the SCADA server's behaviour when the directory is unreachable must be tested — can operators still log in to the HMI?); `ntp-ops` needs a second, independent reference and monitoring of offset; `esx-03` capacity and administrator group become a cross-sector concern reviewed with all three owners.

### 15.4 Integration points are boundaries

Every place the service connects to something it does not control is a boundary:

- **Station communication equipment** — cellular routers, radios, the carrier's private network. Chapter 13's port-forward was here. Each router's configuration belongs in the asset inventory, under change control and drift detection (Chapter 14).
- **Vendor remote-support gateways** — Chapter 10.
- **Data exports** — the historian's daily push to the corporate report server (Chapter 6 conduit C4). Exports should be pushed outward from the control side, never pulled by a corporate host with credentials into the control zone.
- **Shared services** — directory, time, monitoring. Their administrators effectively administer every dependant.

CISA's National Critical Functions work frames these dependencies at national scale ([National Critical Functions](https://www.cisa.gov/national-critical-functions-set)); the technician applies the same reasoning to one operations centre.

### 15.5 Practical activity

Add a `power-ups-a` node that `esx-02` and `esx-03` both need, and a `cell-carrier` node that `cell-router-kw` and `telco-mpls` both need. Re-run Lab 15 and record which components are now shared by all three services. Then propose one technical change for each.

After the change, record which components are shared by all three services and propose one technical response for each, such as a second domain controller or a second power feed. Keep the new edges in the same format as the lab so that the graph stays runnable. Review the proposals with the three service owners before any change.

### 15.6 Common errors and limits

- Listing direct dependencies only.
- Treating the directory and time service as "infrastructure" with no service owner.
- Assuming carriers isolate customers' private networks from each other and from corporate VPNs without checking.
- Counting dependants instead of looking at which *services* and through which *paths*.
- Lab 15's graph is binary (needs / does not need); real dependencies have degraded modes and timers (a cached credential works for hours; a clock drifts slowly).

- Listing only direct dependencies and missing the hypervisor under the directory.
- Treating the directory and time service as infrastructure with no service owner.
- Assuming a carrier isolates customer private networks without checking.
- Counting dependants without looking at which services and through which paths.

### Exercises — chapter 15

**EX057 — Paths matter.** *Objective:* trace an impact path. *Inputs:* Lab 15. *Steps:* modify the program to print, for `esx-03`, one dependency path from it to each affected service. *Expected evidence:* code and three paths. *Rubric:* 3 = for example esx-03 → fep-01 → grid-ss3-telecontrol; esx-03 → ad-ops → scada-01 → water-telemetry; esx-03 → ad-ops → bms-server → hospital-bms; explains that a second directory on another host breaks two of the three; 2 = paths without interpretation; 1 = attempted; 0 = none.

**EX058 — New shared components.** *Objective:* run the activity. *Inputs:* activity 15.5. *Steps:* run and interpret. *Expected evidence:* output and two technical changes. *Rubric:* 3 = `power-ups-a` and `esx-03` shared by all three (and `cell-carrier` affecting water and grid); changes such as separate UPS feeds for the two hosts and a second carrier or radio path for the most critical stations; 2 = output only; 1 = partial; 0 = none.

**EX059 — Degraded-mode test.** *Objective:* test behaviour when a dependency fails. *Inputs:* ad-ops unavailable. *Steps:* write a scoped test plan, in a maintenance window, to establish whether operators can still log in to the HMI and whether SCADA polling continues. *Expected evidence:* test plan with stop conditions. *Rubric:* 3 = test on a standby or lab replica first; in production, blocks only the HMI's path to the directory for a short window with operations present; checks cached logins, local emergency accounts, polling continuity; stop conditions; evidence; 2 = no replica step; 1 = "turn off the domain controller"; 0 = none.

**EX060 — Export direction.** *Objective:* configure a boundary correctly. *Inputs:* the corporate report server currently logs in to hist-02 every night with a stored password to pull the CSV. *Steps:* redesign and list the configuration changes on both hosts and on fw-01. *Expected evidence:* design and changes. *Rubric:* 3 = hist-02 pushes over HTTPS to one endpoint; corporate credential into Z2 removed; fw-01 rule direction reversed (Z2 → Z6 only, specific host and port); push integrity checked (digest in the payload or a signed file); monitoring for failed pushes; 2 = push without removing old credential; 1 = vague; 0 = none.

### Chapter synthesis

Services fail through what they depend on, and the most dangerous dependencies are shared ones that no owner claims. Model dependencies as a graph, search it backwards from each component, and look at the paths, not just the counts. Treat every integration point — station routers, carriers, vendor gateways, exports, directory and time — as a boundary under the same control, change and monitoring discipline as the firewall.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue studying — chapter 15 of 18

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes and connection

After this chapter you should be able to:

- write technical documents that another technician can execute safely: work instructions, troubleshooting logs, change records and as-built configuration records;
- integrate **physical and process safety** into technical work: permits, isolation, the authority of operations, and stop conditions;
- control **transient devices** — laptops and removable media taken to sites — so they do not carry malware or data between zones;
- keep secrets out of documents.

Chapters 1–15 produced findings, changes and evidence. This chapter is about the documents that make that work repeatable and safe, and about the safety rules that override any technical plan.

### 16.1 The documents a technician owns

| Document | Purpose | Must contain |
|---|---|---|
| **Work instruction** | Lets a competent colleague perform a task correctly | Preconditions, numbered steps with expected results, stop conditions, rollback, who to call |
| **Troubleshooting log** | Records an investigation as it happens | UTC times, four labels (observed, inferred, done, open), evidence references |
| **Change record** | Authorizes and records a change | Before/after, reason, tests (Chapter 11), rollback, window, approver, verifier |
| **As-built record** | States what is actually configured | Versions, configuration digests (Chapter 14), deviations from design and their approval |

Write steps as imperative actions with an observable result: "Run `sshd -T | grep -i passwordauthentication`; expect `passwordauthentication no`." A step without an expected result cannot be checked, and a document that cannot be checked will drift from reality.

### 16.2 Safety comes first and belongs to operations

In a water works, a substation or a hospital plant room, the people responsible for the physical process have authority over it. A technician's work there starts with their permission and stops at their request. Practical rules:

- **Permits and isolation**: work on or near process equipment follows the site's permit-to-work and isolation procedures; a security task does not exempt you.
- **Protection and safety systems** are never touched by security work: protection relays in a substation, safety instrumented systems, medical gas alarms.
- **Inform before acting**: the control room knows when you start, what you are doing and when you finish.
- **Stop conditions** are written into every work instruction (Chapter 5) and honoured immediately.

NIST SP 800-82 Rev. 3 discusses the relationship between OT security and safety ([SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)); the UK NCSC Cyber Assessment Framework treats the operator's understanding of its essential functions as a foundation for security ([NCSC CAF](https://www.ncsc.gov.uk/collection/caf)).

### 16.3 Transient devices and media

A laptop that visits stations, the control centre and the corporate office is a bridge across every zone. Controls a technician can apply:

- dedicated engineering laptops that never join the corporate network or the internet;
- a known-good image, updated and scanned at a controlled point before each site visit;
- removable media only from a controlled pool, scanned before use, with a log of where each item has been;
- no personal devices on control networks;
- a record of every connection made at a site (which port, which device, when).

The CISA performance goals list controls on removable media and on device configuration ([CISA CPGs](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)).

### 16.4 Secrets and sensitive information

Documents must not contain passwords, private keys, API tokens or one-time codes. Write "credential from vault entry `kw-rtu-eng`" instead of the credential. Network diagrams, register maps and firewall exports of critical infrastructure are sensitive: store them with access control, share them on a need-to-know basis, and remove them from tickets that go to suppliers. This book prints a few fake values only because they are fake.

Write credential from vault entry rather than the credential itself. Store network diagrams, register maps and firewall exports with access control, and strip them from tickets that go to suppliers. This book prints fake values only because they are fake; treat real ones as sensitive design information.

### 16.5 Worked example: a work instruction (synthetic)

**WI-KW-07 — Export KW-04 RTU configuration for drift baseline.** *Preconditions*: change record CHG-2219 approved; Kestrel Water control room informed; engineering laptop ENG-L3 scanned today (record in the media log). *Steps*: (1) at 10:00 local, call the control room; record the operator's name. (2) On ENG-L3, open the vendor tool in read-only mode; expected: status bar shows "Online — read only". (3) Export the configuration to `KW04-20261013.cfg`; expected: file size between 40 and 60 kB. (4) Run `sha256sum KW04-20261013.cfg`; record the digest in CHG-2219. (5) Disconnect; inform the control room. *Stop conditions*: any alarm at KW-04; tool requests to switch to "online edit"; operator request. *Rollback*: none needed (read-only), but if any write is suspected, inform operations immediately and open an incident. *Evidence*: file, digest, call times.

### 16.6 Practical activity

Write a work instruction for the KW-04 router change from EX052, including preservation, the change, positive and negative tests, rollback and stop conditions. Ask someone else to read it and list every step where they would have to guess.

Include preservation of the router's configuration before the change, positive and negative tests afterwards, rollback steps and stop conditions that include any KW-04 alarm. Ask a colleague to mark every step where they would have to guess; those steps need an expected result or a screenshot of the vendor tool. Keep the reviewed copy with the change record.

### 16.7 Common errors and limits

- Steps without expected results.
- Documents that contain credentials or are shared too widely.
- Treating a site visit as an IT task and skipping the permit or the control-room call.
- One laptop for everything.
- Documentation written after the work, from memory.

- Writing steps without expected results.
- Putting credentials or full firewall exports into a widely shared ticket.
- Skipping the permit or the control-room call because the task looks like ordinary IT.
- Using one laptop for corporate, control-centre and site work.
- Writing the document from memory after the work.

### Exercises — chapter 16

**EX061 — Repair a work instruction.** *Objective:* make steps executable. *Inputs:* "Log into the RTU (password Kestrel2024!) and check settings. Fix anything wrong. Tell ops when done." *Steps:* list the defects and rewrite. *Expected evidence:* defect list and rewritten instruction. *Rubric:* 3 = removes the credential (and recommends rotating it, since it has been written down), adds preconditions, read-only mode, expected results, stop conditions, informs operations before, replaces "fix anything" with a change record; 2 = most; 1 = cosmetic; 0 = none.

**EX062 — Transient device policy.** *Objective:* control a bridge across zones. *Inputs:* one engineer uses the same laptop for email and for station work. *Steps:* write a short technical policy and the transition plan. *Expected evidence:* policy and plan. *Rubric:* 3 = dedicated engineering laptops with a controlled image, no corporate or internet use, pre-visit check, media pool and log, connection record; transition that preserves the current laptop's project files after scanning; 2 = policy without transition; 1 = "be careful"; 0 = none.

**EX063 — Safety boundaries.** *Objective:* recognize what is out of bounds. *Inputs:* during a substation visit you find a protection relay with a default web password. *Steps:* state what you do and do not do, and how you record it. *Expected evidence:* short procedure. *Rubric:* 3 = do not log in or change it; record observation (device, time, how noticed); report to the Kestrel Grid protection engineer and the KVROC security lead; protection engineers decide and act; sensitive finding handled on need-to-know basis; 2 = right actions, weak record; 1 = changes the password; 0 = none.

**EX064 — As-built record.** *Objective:* document reality. *Inputs:* fw-01 after the EX038 fix and hist-02 after CHG-2207. *Steps:* draft an as-built record with versions, digests (placeholders allowed), deviations and approvals. *Expected evidence:* one-page record. *Rubric:* 3 = states actual configuration, includes digests and where they are stored, lists open deviations (REQ-3/4 before fix) with approvals or tickets, dated and signed; 2 = no deviations; 1 = copies the design; 0 = none.

### Chapter synthesis

Good technical documents are executable and checkable: numbered steps with expected results, stop conditions, rollback and evidence. Safety and the authority of operations override every technical plan; protection and safety systems are out of bounds. Laptops and media that move between zones need their own controls, and secrets never belong in documents.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue studying — chapter 16 of 18

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes and connection

After this chapter you should be able to:

- integrate the course's techniques — decoding (Chapter 2), validation (Chapter 4), detection rules (Chapters 8 and 10), episodes and self-checks — into one detection pipeline;
- write detection rules from the system model, not from a product catalogue: new talker, unauthorized write, identification query;
- group alerts into **episodes** and explain the trade-off of the grouping window;
- make the pipeline monitor itself: every input record is either parsed or counted as dropped;
- assess the pipeline against a rubric and identify its blind spots.

Chapter 12 built a device. This second assessed laboratory builds the watcher, in the same contained way: fixed synthetic inputs, standard library only, no network.

### 17.1 Rules from the model

Each rule is derived from a statement in the system model:

- **NEW-TALKER**: the model lists the hosts that may speak Modbus to stations (scada-01, eng-ws-15). Any other source is a finding.
- **UNAUTH-WRITE**: only the engineering workstation may write (Chapter 2).
- **DEVICE-ID-QUERY**: function 43 is reconnaissance-shaped; alert, with context.

These are deliberately simple and explainable (Chapter 8). MITRE ATT&CK for ICS catalogues adversary techniques that such rules relate to, including discovery and unauthorized command messages ([ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)); use it to check coverage, not as the source of rules.

### 17.2 Episodes

One unauthorized host may generate dozens of alerts in a minute. Grouping alerts with the same rule and source into an **episode** — extended while new alerts arrive within a window of the previous one — gives an analyst one item with a count and a time span. The window is a trade-off: too short and one activity becomes many episodes; too long and two separate activities merge. Record the chosen window and why.

Record the chosen window and why. In Lab 17 a five-minute window splits the 07:12 write into its own episode, which is what you want if an analyst might otherwise think the activity had stopped. Too long a window would merge that later write with the earlier burst and hide the gap.

### 17.3 The pipeline monitors itself

A detector that silently drops records it cannot parse is blind exactly where an attacker sends malformed traffic. The pipeline must account for every input: *records = parsed + dropped*, checked by an assertion, with dropped records listed and counted. The NIST continuous monitoring guidance makes the same point at programme level: monitoring must itself be monitored ([SP 800-137](https://csrc.nist.gov/pubs/sp/800/137/final)).

Assert that records equal parsed plus dropped, and list every dropped record with time and source. Unparseable traffic from an unknown host should still raise a new-talker finding on the source address, which Lab 17's practical activity adds. A detector that fails closed on its own accounting is fit for duty use.

### 17.4 Worked example: the 07:03 activity (synthetic)

Ten records from the control-centre sensor on 12 October.

**Lab 17** (save as `lab17.py`, run with `python3 lab17.py`):

```python
# Lab 17 - contained detection pipeline for station traffic (offline, standard library only)
# Synthetic records: (UTC time, source, destination, Modbus/TCP frame hex). Rules come from Chapters 2, 9 and 10.
import struct
from datetime import datetime, timedelta
KNOWN = {"10.20.0.10": "scada-01", "10.20.0.15": "eng-ws-15"}
WRITERS = {"10.20.0.15"}
WRITE_FC = {5, 6, 15, 16}
recs = [
 ("07:00:00", "10.20.0.10", "10.10.4.2", "000100000006010300000004"),
 ("07:00:05", "10.20.0.10", "10.10.5.2", "000200000006010300000004"),
 ("07:02:10", "10.20.0.15", "10.10.4.2", "00030000000601060007012c"),
 ("07:03:00", "10.20.0.31", "10.10.4.2", "000400000006012b0e010000"),
 ("07:03:01", "10.20.0.31", "10.10.5.2", "000500000006012b0e010000"),
 ("07:03:02", "10.20.0.31", "10.10.6.2", "000600000006012b0e010000"),
 ("07:03:03", "10.20.0.31", "10.10.7.2", "0007000000060103"),
 ("07:04:40", "10.20.0.31", "10.10.4.2", "00080000000601060007ffff"),
 ("07:05:30", "10.20.0.31", "10.10.4.2", "00090000000601060007ffff"),
 ("07:12:00", "10.20.0.31", "10.10.4.2", "000a0000000601060007ffff"),
]
alerts, dropped, parsed = [], [], 0
for t, src, dst, hx in recs:
    b = bytes.fromhex(hx)
    if len(b) < 8 or struct.unpack(">H", b[4:6])[0] != len(b) - 6:
        dropped.append((t, src, "malformed")); continue
    parsed += 1; fc = b[7]
    if src not in KNOWN: alerts.append((t, "NEW-TALKER", src))
    if fc in WRITE_FC and src not in WRITERS: alerts.append((t, "UNAUTH-WRITE", src))
    if fc == 43: alerts.append((t, "DEVICE-ID-QUERY", src))
assert parsed + len(dropped) == len(recs), "pipeline lost records"
episodes = []   # merge same rule+source within 5 minutes of the previous alert in the episode
for t, rule, src in alerts:
    ts = datetime.strptime(t, "%H:%M:%S")
    e = next((e for e in episodes if e["key"] == (rule, src) and ts - e["last"] <= timedelta(minutes=5)), None)
    if e: e["count"] += 1; e["last"] = ts
    else: episodes.append({"key": (rule, src), "first": ts, "last": ts, "count": 1})
for e in episodes:
    print(f"{e['first']:%H:%M:%S}-{e['last']:%H:%M:%S}Z {e['key'][0]:<15} {e['key'][1]:<11} x{e['count']}")
print(f"records {len(recs)} parsed {parsed} dropped {len(dropped)} {dropped} alerts {len(alerts)} episodes {len(episodes)}")
```

Expected output (Python 3.13.5):

```text
07:03:00-07:05:30Z NEW-TALKER      10.20.0.31  x5
07:03:00-07:03:02Z DEVICE-ID-QUERY 10.20.0.31  x3
07:04:40-07:05:30Z UNAUTH-WRITE    10.20.0.31  x2
07:12:00-07:12:00Z NEW-TALKER      10.20.0.31  x1
07:12:00-07:12:00Z UNAUTH-WRITE    10.20.0.31  x1
records 10 parsed 9 dropped 1 [('07:03:03', '10.20.0.31', 'malformed')] alerts 12 episodes 5
```

Interpretation: a host never seen before, 10.20.0.31, queried device identification on three stations in three seconds, sent one malformed frame to a fourth, then wrote 0xFFFF to register 7 (the pump setpoint) at KW-04 twice, and again six and a half minutes later. Five episodes summarize twelve alerts. Two observations matter beyond the alerts themselves:

1. The **07:12 write** is a separate episode because it came more than five minutes after the previous alert. An analyst reading only the first three episodes might think the activity had stopped.
2. The **malformed frame** from the new talker was dropped and produced no alert — the self-check shows it, and it is the first thing to fix: unparseable traffic from an unknown host should itself raise NEW-TALKER, since the source address is known even when the payload is not.

The value 0xFFFF (65,535) to a setpoint register whose policy range is 100–400 is the kind of write Lab 12's responder would refuse with exception 03 — if the device had such a policy. Most do not, so the network-side detection and the firewall (Chapter 10) are what stand between this host and the process. In the KVROC story this is the moment to preserve, inform Kestrel Water and open an incident (Chapter 13).

### 17.5 Assessment rubric

| Criterion | 3 | 1 |
|---|---|---|
| Containment | Fixed inputs; no network; stated | Reads live traffic without scope |
| Rule provenance | Each rule cites the model statement it enforces | Rules from a list without rationale |
| Self-monitoring | Records accounted for; dropped listed | Silent drops |
| Episode design | Window stated with trade-off | Arbitrary or none |
| Blind spots | Lists what the sensor cannot see (station-local traffic, encrypted links) | Claims full coverage |
| Reproducibility | Output recorded with Python version | Not recorded |

Score Lab 17 against each row and write one improvement for any score below three. Blind spots must include station-local traffic and any path that does not pass the control-centre sensor, as Chapter 13 found for KW-04. Keep the scored rubric with the lab output and the Python version.

### 17.6 Practical activity

Change the pipeline so that a dropped (malformed) record from an unknown source raises NEW-TALKER, and add a rule that alerts on any write whose value is outside the register's policy range, using the Lab 12 policy table. Record the new output and how the episodes change.

Raise NEW-TALKER for a malformed record from an unknown source, and alert on writes outside the Lab 12 policy range. Re-run and record how the episode list changes, especially whether the malformed line now appears inside the 07:03 new-talker episode. Keep both outputs so the improvement is visible.

### 17.7 Common errors and limits

- Rules copied from a catalogue without a model statement behind them.
- Episodes so long that separate activity disappears.
- Dropping malformed records silently.
- Believing the sensor sees everything: Chapter 13 found a path to KW-04 that did not pass this sensor.
- The pipeline's timestamps are the sensor's; correct its clock like any other (Chapter 7).

- Copying rules from a catalogue without a model statement behind them.
- Choosing an episode window so long that separate activity disappears.
- Dropping malformed records silently.
- Believing the sensor sees every path to a station.

### Exercises — chapter 17

**EX065 — Read the episodes.** *Objective:* interpret pipeline output. *Inputs:* Lab 17 output. *Steps:* write a five-line summary for the KVROC duty lead using the four labels. *Expected evidence:* summary. *Rubric:* 3 = observed: unknown host 10.20.0.31, identification queries to three stations, writes of 65,535 to KW-04 register 7 at 07:04:40, 07:05:30 and 07:12:00, one malformed frame; inferred: reconnaissance followed by attempted setpoint changes; done: nothing changed; open: identity of host, effect on KW-04, path; asks for operations check of KW-04 pump 2; 2 = no labels; 1 = vague; 0 = none.

**EX066 — Fix the blind drop.** *Objective:* improve self-monitoring. *Inputs:* activity 17.6 (first half). *Steps:* implement and run. *Expected evidence:* code and output. *Rubric:* 3 = NEW-TALKER episode for 10.20.0.31 now extends to six records within the same episode (07:03:00–07:05:30 x6), total alerts 13; records still accounted for; 2 = works, counts not explained; 1 = attempted; 0 = none.

**EX067 — Window trade-off.** *Objective:* reason about grouping. *Inputs:* Lab 17. *Steps:* predict episode counts with windows of 1 minute and 10 minutes, then run. *Expected evidence:* predictions and outputs. *Rubric:* 3 = 1 minute: NEW-TALKER splits (07:03:00–07:03:02, 07:04:40–07:05:30, 07:12:00), UNAUTH-WRITE splits into 07:04:40–07:05:30 and 07:12:00, DEVICE-ID one → 6 episodes; 10 minutes: NEW-TALKER and UNAUTH-WRITE each one episode → 3 episodes; recommends a value with reason; 2 = mostly right; 1 = guesses; 0 = none.

**EX068 — Value-range rule.** *Objective:* combine device policy and network detection. *Inputs:* activity 17.6 (second half). *Steps:* implement for functions 6 and 16 and run. *Expected evidence:* code and output. *Rubric:* 3 = alerts on all three 0xFFFF writes and not on eng-ws-15's write of 300; explains that the rule detects but does not prevent, so the firewall remains necessary; 2 = function 6 only; 1 = attempted; 0 = none.

### Chapter synthesis

A detection pipeline is a small system with its own requirements: rules that trace to the system model, episodes that summarize without hiding, and a self-check that accounts for every record. Built contained and assessed honestly — including its blind spots — it turns the course's separate techniques into something a duty lead can act on.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue studying — chapter 17 of 18

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes and connection

After this chapter you should be able to:

- plan and execute a bounded technical project in a critical environment under supervision: scope, baseline, change, verification, troubleshooting log and handover;
- assemble a project **evidence package** and seal it with a manifest of SHA-256 digests and a separately recorded seal;
- detect any later change to sealed evidence, and explain what a seal does and does not prove;
- present the project for assessment against a rubric and state its open items honestly.

This chapter closes the course. It uses everything before it on one realistic task, and its output is what an employer or assessor would ask to see: not a claim of competence, but evidence of it.

### 18.1 Choosing a project

A good supervised project is narrow, valuable and checkable. Examples drawn from this book: harden the corporate-to-control-centre conduit and verify it (Chapters 10–11); close the station-router bypass across all stations (Chapter 13); deploy drift detection on the control-centre servers (Chapter 14); build and test the detection pipeline against a replayed, sanitized capture (Chapter 17). Every project needs a **supervisor** (here L. Ferreira) and an **authorizer** who owns the affected systems (here A. Mensah for Kestrel Water).

Agree the supervisor, the owner who signs the scope and the success criteria before day one. Pick one conduit or one class of host, not the whole programme. Write the open items you expect to leave, so honesty about limits is planned rather than improvised at assessment.

### 18.2 Phases

1. **Scope** (Chapter 5): purpose, systems, actions, window, people, stops, evidence handling — signed.
2. **Baseline**: configuration exports and digests before anything changes (Chapter 14); current test results (Chapter 11).
3. **Change**: under a change record with rollback (Chapter 10).
4. **Verification**: positive and negative tests, every requirement verified, failed or untested.
5. **Troubleshooting log** throughout, with the four labels (Chapter 13).
6. **Handover**: as-built record, work instructions, open items with owners (Chapter 16).
7. **Evidence package**: everything above, sealed.

Do not skip baseline digests even when the change seems small; without them you cannot prove what changed. Keep the troubleshooting log open for the whole window, including interruptions and false starts. The evidence package is last, after handover documents exist to put in it.

### 18.3 Sealing evidence

A **manifest** lists each artefact with its SHA-256 digest ([FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)). The **seal** is the digest of the manifest itself. Record the seal **outside** the package — in the change record, an email to the supervisor, the assessment form — because anyone who can edit the package can also edit a manifest stored inside it. Later, re-computing the artefacts' digests shows whether anything has changed; re-computing the manifest's digest and comparing with the externally recorded seal shows whether the manifest has been altered.

What a seal proves: the artefacts are byte-for-byte what they were when sealed. What it does not prove: that they were true, complete or created when they claim. Those depend on how they were collected (Chapter 5) and on independent records (firewall logs on the collector, change tickets in their own system). For stronger guarantees, organizations use signatures with keys held by a separate party or trusted time-stamping; the principle is the same.

### 18.4 Worked example: the KW-04 conduit project (synthetic)

R. Kaur's project removed the broad corporate rule R4 on fw-01 (CHG-2215), verified the result, and investigated the KW-09 event on the way. The evidence package is sealed and then, a week later, re-verified.

**Lab 18** (save as `lab18.py`, run with `python3 lab18.py`):

```python
# Lab 18 - seal and re-verify a project evidence package (offline, standard library only)
# Synthetic artefacts from the supervised project; written only inside a temporary directory.
import hashlib, pathlib, tempfile
artefacts = {
 "01-scope.md": "Scope: KW-04 conduit hardening; authorized by A. Mensah (Kestrel Water) 2026-10-05.\n",
 "02-before-fw.txt": "R4 allow 10.30.0.0/16 10.20.0.0/24 tcp any\n",
 "03-after-fw.txt": "R4 removed CHG-2215\n",
 "04-tests.csv": "test,result\nT4,pass\nT5,pass\nT9,pass\n",
 "05-troubleshooting-log.md": "07:05Z KW-09 missing; H4 consistent; RTU config preserved as E-17.\n",
}
with tempfile.TemporaryDirectory() as tmp:
    d = pathlib.Path(tmp)
    for n, t in artefacts.items(): (d / n).write_text(t)
    lines = [f"{hashlib.sha256((d / n).read_bytes()).hexdigest()}  {n}" for n in sorted(artefacts)]
    (d / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")
    seal = hashlib.sha256((d / "MANIFEST.sha256").read_bytes()).hexdigest()
    print("manifest:")
    for l in lines: print(" ", l[:16] + "...", l.split("  ")[1])
    print("seal (record this outside the package):", seal[:24])
    (d / "04-tests.csv").write_text("test,result\nT4,pass\nT5,pass\nT9,pass\nT10,pass\n")   # later edit
    for l in (d / "MANIFEST.sha256").read_text().splitlines():
        h, n = l.split("  ")
        ok = hashlib.sha256((d / n).read_bytes()).hexdigest() == h
        print(f"verify {n:<26} {'OK' if ok else 'MISMATCH'}")
```

Expected output (Python 3.13.5):

```text
manifest:
  72d8be01e70067c7... 01-scope.md
  8d52d15a3e02b7f8... 02-before-fw.txt
  2cd59665641b4779... 03-after-fw.txt
  d6eccc2e2ac61ecb... 04-tests.csv
  6d2525605f11521c... 05-troubleshooting-log.md
seal (record this outside the package): 062b9a1fd700dd0eac04b3a8
verify 01-scope.md                OK
verify 02-before-fw.txt           OK
verify 03-after-fw.txt            OK
verify 04-tests.csv               MISMATCH
verify 05-troubleshooting-log.md  OK
```

Four artefacts verify; `04-tests.csv` does not. Someone added a T10 line after sealing. It may be an honest later test — but it must be added as a new, separately dated artefact with its own entry, not by editing a sealed file. The assessor asks R. Kaur to restore the sealed version from the archive (its digest must match the manifest), and to submit T10 as `06-tests-addendum.csv` in a new, re-sealed package version, with both seals recorded.

### 18.5 Assessment rubric for the project

| Criterion | 3 (meets the technical outcome) | 1 |
|---|---|---|
| Scope and authorization | Signed scope with owner, window and stops | Verbal approval |
| Technical correctness | Change achieves requirements; no collateral damage | Partial or harmful |
| Verification | All requirements verified or explicitly open, positive and negative tests with evidence | Pass counts only |
| Troubleshooting | Hypotheses, predictions, eliminations, preservation | Narrative |
| Documentation | Executable work instructions, as-built record, no secrets | Notes from memory |
| Evidence | Manifest, external seal, verification run | Folder of screenshots |
| Honesty about limits | Open items with owners; blind spots stated | "All done" |

### 18.6 Continuing practice

After the course, keep three habits: verify before you report, preserve before you change, and correct clocks before you order events. Keep labs contained, and never test real infrastructure without written authorization from its owner. Revisit standards and guidance when they change; every source in this book is dated October 2026.

After the course, keep three habits: verify before you report, preserve before you change, and correct clocks before you order events. Keep labs contained, and never test real infrastructure without written authorization from its owner. Revisit standards and guidance when they change; every source in this book is dated October 2026.

### 18.7 Common errors and limits

- Projects too broad to verify.
- Seals stored inside the package.
- Editing sealed artefacts instead of adding new ones.
- Reporting only successes.
- Lab 18 uses in-memory text and a temporary directory; real packages include binary exports and large captures, which hash the same way but need storage with access control.

- Choosing a project so broad that verification never finishes.
- Storing the seal inside the package where an editor can change both.
- Editing a sealed artefact instead of adding a dated addendum.
- Reporting only successes and hiding untested requirements.

### Exercises — chapter 18

**EX069 — Project scope.** *Objective:* define a supervised project. *Inputs:* choose one project from 18.1. *Steps:* write the scope, requirements (testable) and the list of artefacts the evidence package will contain. *Expected evidence:* one-page plan. *Rubric:* 3 = all scope elements, at least four testable requirements with positive and negative tests, artefacts mapped to phases, supervisor and authorizer named; 2 = one gap; 1 = generic; 0 = none.

**EX070 — Verify a seal.** *Objective:* use the seal correctly. *Inputs:* Lab 18. *Steps:* modify the program to also re-compute the manifest's digest at the end and compare it with the recorded seal; then also edit `MANIFEST.sha256` to match the tampered tests file and show what the seal comparison reports. *Expected evidence:* code and outputs for both cases. *Rubric:* 3 = first case: seal matches (manifest untouched) while one artefact mismatches; second case: all artefacts "OK" against the edited manifest, but the seal comparison fails — explains why the seal must be stored outside; 2 = one case; 1 = attempted; 0 = none.

**EX071 — Handle the late addition.** *Objective:* manage evidence changes. *Inputs:* the T10 edit. *Steps:* write the procedure the assessor described, step by step, including what is recorded where. *Expected evidence:* procedure. *Rubric:* 3 = restore sealed original from archive and check its digest; add addendum as new artefact with date and collector; produce a new manifest version and seal; record both seals externally with reason; never overwrite version 1; 2 = missing external record; 1 = "edit and reseal"; 0 = none.

**EX072 — Self-assessment.** *Objective:* apply the rubric honestly. *Inputs:* R. Kaur's project as described in this chapter and Chapters 10–13. *Steps:* score each rubric criterion with one sentence of evidence and list the open items. *Expected evidence:* scored table and open items. *Rubric:* 3 = scores justified from the text (for example verification limited by REQ-4 until R6 is removed; evidence criterion reduced by the post-seal edit until corrected), open items include R6, KW-04 router bypass across other stations, REQ-6 coverage, and the KW-09 incident outcome, each with owner; 2 = scores without evidence; 1 = all 3s; 0 = none.

### Chapter synthesis

A supervised project shows technical competence as evidence: a signed scope, a baseline, a controlled change, verification of every requirement, a troubleshooting log, executable documentation and a sealed package. A seal proves that evidence has not changed since sealing, if it is recorded outside the package; it does not prove the evidence was true. State what is open, who owns it, and what you could not see.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue studying — chapter 18 of 18

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer and what the rubric rewards. A different answer earns full credit when it meets the same standard of evidence, scope and honesty about limits. Numerical results come from the offline labs in this book, run with Python 3.13.5 and the standard library only; where a result depends on a modified lab, the modification is described so you can reproduce it. All figures describe synthetic data; never present them as findings about real operators.

### Chapter 1: EX001–EX004

**EX001 — Path classification.** HMI → scada-01 "start pump 2": control; worst case an unauthorized start or stop of a pump (overflow, pressure transient). KW-04 → scada-01 reading: monitoring; worst case operators act on a false level. eng-ws-15 → KW-04 project download: management (and indirectly control); worst case replaced controller logic — the most dangerous action on the list, because it changes what the controller does even when no further command is sent. jump-01 → hist-02 SSH: management; worst case altered or deleted historical records, or a foothold in Z2. hist-02 → corporate CSV: monitoring data leaving the control zone; worst case disclosure of operational data or, if implemented as a pull, a corporate credential into Z2 (Chapter 15).

**EX002 — Fix the cycle on paper.** Example: (1) poll the four fibre stations and the five cellular stations on separate channels from the three radio stations (three channels: fibre 0.31 s, cellular 6.52 s, radio 4.50 s — cellular still too slow); (2) reduce cellular polls per cycle from 4 to 2 by combining register reads into one request (cellular channel 3.26 s) and give KW-06 its own channel (2 polls × 690 ms = 1.38 s; remaining cellular 1.88 s). With channels of ≤ 4.5 s all healthy stations meet 5 s. Limiting a dead station: a timeout of 800 ms with no immediate retry keeps a dead KW-06 at 1.6 s on its own channel. Full credit verifies by editing `stations`, `TIMEOUT_MS` and the `cycle` function and reports the printed values; any configuration that runs and meets the requirement earns credit if the timeout is justified against real link latency.

**EX003 — Tunnel impact.** Sequential: 5 cellular stations × 4 polls × 35 ms = 700 ms, so 11.33 → 12.03 s. Per-station channels: each cellular station's own cycle rises by 4 × 35 = 140 ms; KW-06 becomes 2.90 s, still under 5 s. Recommendation: the tunnel is acceptable only together with the channel redesign (EX002), and its latency should be measured in a pilot, not assumed.

**EX004 — Shared platform list.** Virtualization hosts — "What is the headroom if one host fails, and which guests restart where?" Directory — "Who is in the administrator groups, and can operators log in to the HMI if the directory is unreachable?" Time source — "What is the reference, is there a second one, and is offset monitored?" Monitoring collector — "What happens when its disk fills or it stops — do sources buffer, and does anyone get alerted?"

### Chapter 2: EX005–EX008

**EX005 — Hand decode.** Frame 1: tid 0x0010 = 16, protocol 0, length 6, unit 1, function 16 (write multiple registers), start address 10, quantity 2 — but function 16 must also carry a byte count (4) and four bytes of values, so the PDU is incomplete; a correct parser rejects it even though the MBAP length matches the bytes present. Frame 2: tid 17, length 6, unit 1, function 15 (write multiple coils), address 0, quantity 8 — also missing its byte count (1) and the coil byte. Full credit notes that MBAP checks alone do not validate a PDU; each function has its own structure.

**EX006 — Extend the decoder.** In the write branch: `if fc in (15, 16): bc = b[12]; data = b[13:13 + bc]` and for 16, `vals = struct.unpack(f">{qty}H", data)` after checking `bc == 2 * qty and len(data) == bc`. For the 10.30.3.7 frame `...011000070002040064000a`, the byte count is 4 and the values are 100 and 10 — two registers starting at 7 (setpoint and the next register).

**EX007 — Write policy as data.** Normal: (10.20.0.10, 10.10.0.0/16, {1, 2, 3, 4}). Maintenance window: add (10.20.0.15, the station named in the ticket, {3, 5, 6, 15, 16}) for the window only. The KVROC on-call switches the policy on and off against a ticket approved by Kestrel Water operations; the switch is logged and the window expires automatically.

**EX008 — Reconnaissance or feature?** The daily query from scada-01 is consistent with an inventory feature; confirm in the SCADA vendor documentation and add it to the model as an expected flow. The three-second burst from 10.20.0.31 is a priority: an unknown host in Z2 querying identification across stations is reconnaissance-shaped. First checks are read-only: DHCP and switch records for the address, the asset inventory, the jump-host and directory logs for that host. Do not probe it. Chapter 17 shows what it did next.

### Chapter 3: EX009–EX012

**EX009 — First value wins.** If the commented line is uncommented where it stands (after `PasswordAuthentication yes`), the effective value is still `yes` because sshd uses the first value read. The fix must replace the first occurrence (or delete it), then be confirmed with `sshd -T | grep -i passwordauthentication`.

**EX010 — Prioritize the HIST-02 findings.** Today: preserve `last`/`lastlog`/auth logs for `backup2` and `vendor`; remove `backup2` (UID 0) and remove `vendor` from `sudo` and `ops-admins`. This week, as one tested change from an open session: `ListenAddress 10.90.0.21`, `PermitRootLogin no`, `PasswordAuthentication no` (after confirming key logins for both authorized people), `X11Forwarding no`, `MaxAuthTries 3`. Next window: set `histsvc` shell to `/usr/sbin/nologin` after checking scheduled jobs and scripts. Vendor access moves to the time-bound process of Chapter 10.

**EX011 — Extend the audit.** Add inside the passwd loop: `if name != "root" and home in ("/root", "/") and not shell.endswith("nologin"): findings.append(f"account {name} has interactive shell and home {home}")`. Output adds `account backup2 has interactive shell and home /root`, findings 11. A shared home directory mixes shell history and keys between identities, so actions cannot be attributed.

**EX012 — Service account design.** System UID (for example 998), shell `/usr/sbin/nologin`, home `/opt/hist` owned by root and readable by group `histsvc`; data directory writable only by `histsvc`; database credential in a file mode 0400 owned by `histsvc`, or in the platform's secret store; rotated yearly and after any staff change with access, owner KVROC platform team; the account is never used by people.

### Chapter 4: EX013–EX016

**EX013 — Predict before running.** KW-11 12.0 → accept (inclusive range); KW-12 `inf` → reject "value not finite" (line 13); KW-02 −0.0 → accept. Summary `{"accept": 4, "reject": 7, "quarantine": 2}` (verified by running). Normalize −0.0 to 0.0 before storage.

**EX014 — Reject or quarantine?** (a) Quarantine: interpretable but outside range — reverse flow, sensor offset or manipulation. (b) Reject unless the schema explicitly defines units case-insensitively; never guess. (c) Accept; a high-level process alarm is the operator's tool, not the validator's. (d) Accept if within an agreed clock tolerance (for example 5 s); otherwise quarantine as a clock issue.

**EX015 — JSON with traps.** `json.loads('{"station": "KW-03", "value": NaN}')` returns `{'station': 'KW-03', 'value': nan}`. Define `def no_const(c): raise ValueError(f"non-standard JSON constant {c}")` and call `json.loads(s, parse_constant=no_const)`; it now raises. RFC 8259 does not permit NaN or Infinity.

**EX016 — Summary for monitoring.** Example: `{"accept": 2, "reject": 6, "quarantine": 2, "by_reason": {"not a number": 2, "unit": 1, "timestamp": 1, "not finite": 1, "field count": 1, "range": 1, "future": 1}, "by_station": {"KW-03": 1, ...}}`. Alert: any quarantine of a CL2_MGL tag, or rejects above 10 % of rows in two consecutive exports, or the export missing entirely.

### Chapter 5: EX017–EX020

**EX017 — Repair a scope.** Defects: "IT" is not the system owner (Kestrel Water must authorize); 10.10.0.0/16 is every station; active scanning in a control network; no window or time; no allowed actions; no stop conditions; no contacts; no evidence handling. Rewrite: purpose "establish the services exposed by station RTUs"; method first from asset records, configuration exports and a 24 h passive capture; if a gap remains, one connect test per named port on one named station in an agreed window with the control room informed, authorized by A. Mensah, stop on any alarm, evidence hashed in the case folder.

**EX018 — Label the note.** *Observed:* RTU KW-09 configuration session at 06:41Z (clock-corrected); readings stopped 07:05Z. *Inferred:* possible unapproved change; who made it is unknown — "vendor" is not established. *Done:* RTU reset at 07:30Z by me, without preservation — the running configuration and session log before reset may be lost. *Open:* who opened the session and why; whether a configuration export or backup exists from before the reset; owner L. Ferreira.

**EX019 — Evidence record.** What: `fw-01-rules-20261013.txt` (raw export). Source: fw-01, management CLI, firmware version recorded. Time: 2026-10-13T08:12:40Z, collector host synchronized to ntp-ops (offset +0.1 s). Collector: R. Kaur. Method: exact export command. Integrity: `sha256sum fw-01-rules-20261013.txt` output recorded in the case record, stored separately from the file.

**EX020 — Passive alternatives.** Who talks to KW-07: fw-01 and router flow logs or a SPAN capture. Firmware: asset records, the vendor tool's inventory during an approved engineering session. Telnet: the RTU's configuration export and the vendor's documentation of default services. Active test justified only if records conflict, in a scoped window with operations present, as a single connect test.

### Chapter 6: EX021–EX024

**EX021 — Place the assets.** KW-06 cellular router: at the Z1 boundary; its management interface is as privileged as Z5 and belongs in the inventory and drift checks. SS-3 vendor gateway: its own remote-access zone, connecting only via jump-01, never placed in Z3. Report server: Z6. Engineering laptop: a transient asset with its own controls (Chapter 16), never permanently in any zone.

**EX022 — Write a conduit.** C4: source hist-02 (Z2) → destination report-01 (Z6) tcp/443; initiated from Z2 (push); purpose daily operations report CSV; owner Kestrel Water operations data lead; enforcement fw-01 rule with ticket; monitoring: collector alert if no push by 06:30 or on any connection from Z6 to hist-02; review annually.

**EX023 — Sector contrast.** Water: confirm redundant SCADA server or schedule outside critical periods; polling interruption duration agreed with operations. Grid: front-end reboots agreed with the grid control room, telecontrol loss procedures ready; protection unaffected but confirm. Hospital: clinical engineering and the BMS manufacturer's supported patch level; ventilation and isolation-room alarm continuity during reboot. One weekly schedule fits none of them.

**EX024 — Model versus capture.** Not explained by declared conduits: 10.30.3.7 → KW-04 writes (no corporate conduit to Z1); the function-43 query from scada-01 if C1 is declared as "read polls" only (add it explicitly if confirmed as a feature); two malformed frames from scada-01 — an anomaly to explain (driver fault or a different program on that host).

### Chapter 7: EX025–EX028

**EX025 — Decode priorities.** `<86>`: 86 = 10 × 8 + 6 → facility 10 (authpriv), severity 6 (informational). `<134>`: 16 × 8 + 6 → local0, informational. `<11>`: 1 × 8 + 3 → user, error. `<165>`: 20 × 8 + 5 → local4, notice.

**EX026 — Correct a clock.** Offset +47 s means the host is ahead; corrected = 02:10:00 − 47 s = **02:09:13Z**. State the uncertainty: "offset measured at about 03:10Z; drift over the hour unknown; treat as ±5 s unless drift data are available".

**EX027 — Place the BSD line.** Needed: the year (from collection context — the export date), the workstation's configured time zone, and its measured offset. Rule: lines matching `^<\d+>[A-Z][a-z]{2} [ \d]\d \d\d:\d\d:\d\d ` are parsed with an explicit year and zone from a per-host table, and the event is flagged `assumed_zone=true` on the timeline. If the host's zone or offset is unknown, place it in a separate "unplaced" list rather than guessing.

**EX028 — Blind-spot question.** Control-centre firewall logs and the Z2 sensor cannot see traffic between a laptop and the RTU on the station's local switch or serial port. The RTU's own logs might, if it records configuration sessions and writes and if logging is enabled. Add: RTU event logging forwarded when the link is up, a station-level passive sensor where justified, and physical access records (door alarms, site visit log).

### Chapter 8: EX029–EX032

**EX029 — Name the mode.** (a) Cross-tag inconsistency or drift: valve position feedback fault, or flow entering by another route (bypass, leak, manual valve). (b) Stuck value / cross-tag inconsistency: failed flow meter, or a frozen or substituted value. (c) Stale/buffered data: store-and-forward after a link outage, or a replay. (d) Loss of control authority: local/remote switch left in "local" after maintenance, or an interlock preventing start.

**EX030 — Predict a rule change.** With `STUCK_MIN = 25` and level `MAX_STEP = 7.0`: KW-02 is no longer flagged (20 < 25); KW-07's steps of 6.84 and 6.83 are below 7.0, so no spike; KW-05's gap is still reported; KW-01 unchanged. Verified output: only `KW-05 FLOW_LS gap: 7 consecutive missing minutes`. What is lost: the frozen analyser and the single-sample excursion — both potentially safety-relevant.

**EX031 — Conditional stuck rule.** `if pump_state == "running" for the whole run and run_length_identical(flow) >= M: alert("flow stuck while pump running")`. Tests: pump off for 40 min with flow 0.0 → no alert; pump running with flow exactly 41.0 for M samples → alert; pump running with natural variation → no alert.

**EX032 — Fault or attack plan.** Fault indicators: analyser local display differs from the reported value or shows a fault code; RTU analog-input diagnostics (open loop, frozen input); maintenance records showing calibration or work on the analyser. Manipulation indicators: captured writes to the reporting register or a related scaling register; an RTU configuration session in the window; manual grab sample by operations that disagrees with 0.62 while the analyser display agrees with the sample. All are read-only or performed by operations.

### Chapter 9: EX033–EX036

**EX033 — Known-answer test.** With `0x3D65` in the right-shifting loop, the assertion fails (`AssertionError`) and the program stops before judging any frame. A bit-reflected (LSB-first) implementation must use the reflected polynomial 0xA6BC; the normal form 0x3D65 belongs to MSB-first implementations. The known-answer test turned a silent, plausible bug into an immediate failure.

**EX034 — Decode the control byte.** 0xC9 = 1100 1001: DIR 1 (from master), PRM 1, function 9 — request link status. 0x44 = 0100 0100: DIR 0 (from outstation), PRM 1 (primary), function 4 — unconfirmed user data, as used for example by an outstation's unsolicited response. 0x0B = 0000 1011: DIR 0, PRM 0, function 11 — link status (secondary).

**EX035 — Forgery thought experiment.** The CRC shows only that the bytes were not accidentally corrupted. The DNP3 source address 1 is a field the sender writes; any host can claim it. Authenticity needs cryptographic protection — DNP3 Secure Authentication, or a tunnel whose endpoints are authenticated (for example TLS terminating at fep-01 and the outstation or its gateway) — plus network enforcement that only fep-01's path reaches the outstation. The unexpected network source is itself the finding.

**EX036 — Method selection.** (a) Passive: decode a capture at fep-01 or its logs over the month and list source addresses. (b) Configuration export of fep-01's firewall and its logs; a single scoped connect test only if the export is ambiguous. (c) Asset record; otherwise the vendor tool in read-only mode during an approved session arranged with Kestrel Grid's protection or telecontrol engineer — never by probing the outstation.

### Chapter 10: EX037–EX040

**EX037 — Explain the shadow.** With R5 above R4: no shadowed rule is reported; tests: 1 PASS, 2 PASS (deny by R5), 3 PASS, 4 FAIL (SMB allowed by R4), 5 FAIL (R6). Reordering fixed the RDP comment's promise but not the broad rule.

**EX038 — Fix the policy.** Remove R4 and R6. All five tests PASS (RDP and SMB now deny by R7; 10.20.0.12 denied by R7). R5 is now redundant with the default deny; keep it only if a separate log category for RDP attempts is wanted (then it should be placed above any allow), otherwise remove it. Before removing R4, check fw-01 logs for 30 days to list what used R4 and give each legitimate use its own conduit.

**EX039 — Supplier access configuration.** `vendor-ss3` disabled by default. Kestrel Grid raises a ticket; KVROC on-call enables the account for a fixed window (for example 4 h) in the access tool; vendor connects to jump-01 with MFA; session recorded; jump-01 permits only the vendor gateway's management address and the specific engineering port at SS-3, never the whole substation network; an alert fires on any login outside an enabled window; the account disables automatically; next working day the session log is reviewed against the ticket.

**EX040 — Detect broadening.** Add: `def overlaps(a, b): return ip_network(a[2]).overlaps(ip_network(b[2])) and ip_network(a[3]).overlaps(ip_network(b[3])) and (a[4] in ("any", b[4]) or b[4] == "any") and (a[5] is None or b[5] is None or a[5] == b[5])`, and for a later rule with the same action that overlaps but is not covered, report it when its source or destination is not a subnet of the earlier one. Verified output adds `R6 broadens R1: same action, wider source 10.20.0.0/24`, the same for R2, and `R7 broadens R5` — the last is the intended default deny and should be excluded (for example skip rules whose source and destination are both `0.0.0.0/0`). Review is needed because the rule looks like a duplicate in a quick reading but grants the whole control-centre subnet write access to KW-04.

### Chapter 11: EX041–EX044

**EX041 — Make it testable.** "Remote access is secure" → "Vendor access to SS-3 is possible only via jump-01 with MFA during an enabled window" (test: attempt outside window is refused and alerts). "Time is synchronized" → "All Z2 and Z5 hosts are within 1 s of ntp-ops" (test: offset report). "Logs are kept" → "fw-01 allow and deny events reach the collector within 60 s and are retained 12 months" (test: marked connect attempt then collector query; retention check of oldest record).

**EX042 — Add the missing test.** With T9 for REQ-6 the output shows REQ-6 verified via T9 and "verified 4/6". REQ-3 and REQ-4 still fail, so CHG-2207 is not complete.

**EX043 — Positive tests for a firewall change.** SCADA polls all twelve stations (historian count for a 10-minute window equals 12 stations); eng-ws-15 connect to the ticketed station in a window; jump-01 SSH to hist-02 and scada-01; hist-02 daily export arrives at the report server; HMI to scada-01 sessions unaffected. Evidence: historian query output, connect logs, collector entries.

**EX044 — Untested is not verified.** "CHG-2207 is not complete. Of six requirements, three are verified with evidence (REQ-1, REQ-2, REQ-5), two failed (REQ-3: corporate RDP still allowed because R4 remains; REQ-4: 10.20.0.12 can reach station Modbus because of R6) and one is untested (REQ-6, deny logging). T8 was a configuration review without recorded output and is not counted. Owners: R4 and R6 removal — R. Kaur under a new change; REQ-6 test — J. Tan. Re-verification after the fix."

### Chapter 12: EX045–EX048

**EX045 — Read the responses.** tid 1: function 3, normal, 6 bytes: 342, 61, 0. tid 2: function 6, normal echo — register 7 = 300 written. tid 3: 0x86 = exception to function 6, code 03 illegal data value (900 outside 100–400). tid 4: 0x86, code 02 illegal data address (register 0 not writable). tid 5: 0x88 = exception to function 8, code 01 illegal function. tid 6: 0x83 = exception to function 3, code 02 (range 8–12 exceeds the table).

**EX046 — Implement function 16.** Parse `addr, qty, bc = struct.unpack(">HHB", req[8:13])`; if `bc != 2 * qty or len(req) != 13 + bc` return exception 03; decode values; if any address in `addr..addr+qty-1` is not in WRITABLE return 02; if any value is outside its range return 03; otherwise write all and return `struct.pack(">HHHBBHH", tid, 0, 6, unit, 16, addr, qty)`. Log each outcome. No partial writes.

**EX047 — Detect mapping attempts.** Rule: three or more exception-02 responses to one source within 60 s. The original six requests produce two exception-02 replies (tid 4 and tid 6), so it does not fire; adding five out-of-range reads produces seven and it fires. Counting 02 and 03 together would already reach three in the original run (tids 3, 4, 6) and fire on ordinary mistakes; keeping the limit-testing rule (exception 03) separate gives clearer alerts.

**EX048 — Assess a lab.** Containment 1: a server on `0.0.0.0:502` is reachable from any network the laptop joins, including a station network if the laptop is used on site. Fidelity: no statement, score 1. Fix: `socketpair()` or bind to 127.0.0.1 with a host firewall rule, or an isolated VM network with no route out; add a fidelity statement; record outputs with the Python version.

### Chapter 13: EX049–EX052

**EX049 — Predictions first.**

| Hypothesis | Ping | TCP 502 | Modbus reply | Radio/cell counters | Other stations |
|---|---|---|---|---|---|
| Link outage | fail | fail | none | errors rising | ok |
| SCADA polling overload (Chapter 1) | ok | ok | ok when polled, but polls late | flat | also delayed |
| Traffic blocked or flooded by an unauthorized host | ok or fail | fail or slow | timeouts | flat | ok |

The observations that separate them are the counters (link), the other stations' freshness (SCADA) and firewall/flow logs (security-relevant).

**EX050 — Add H6.** Example: `"H6 RTU firmware degraded": {"rtu_ping": True, "tcp502_handshake": True, "modbus_reply": "timeout"}` is refuted by `modbus_reply` (observed exception 2). If you instead predict exception 02 (some devices return it in a degraded mode), H6 remains consistent, and the extra read-only observation is the RTU's diagnostic or status page (uptime, mode) via the vendor tool in read-only mode, or its event log showing a restart.

**EX051 — The moment of escalation.** Message: "07:22Z — KW-09 readings stopped at 07:05Z. Observed: link, firewall and SCADA healthy; RTU replies exception 02 to normal reads; RTU logged a configuration session at 06:41Z (clock-corrected) by user 'eng' with no change ticket. Inferred: register map changed by that session; who and why unknown. Done: nothing changed. Request: decision on restoring the previous configuration after preservation. Kestrel Water duty manager informed at 07:20Z." Preserved: RTU configuration export (07:25Z) and session log; jump-01 and eng-ws-15 logs 06:30–06:50Z; fw-01 logs for 10.10.9.2; the troubleshooting log — each with SHA-256 and collection time.

**EX052 — Close the KW-04 path.** Preserve the router configuration and its connection logs; remove the tcp/502 port-forward under a change approved by Kestrel Water; ask the carrier (via the contract owner) to remove reachability from the corporate remote-access VPN to the station private network; negative test from a marked VPN client to KW-04's carrier address; positive test of SCADA polling; then export and check all eleven other station routers for port-forwards and management exposure; add router configurations to drift detection. Owner: KVROC network lead, with Kestrel Water approval.

### Chapter 14: EX053–EX056

**EX053 — Classify and act.** (1) Preserve `sshd_config` and `debug.sh`: copies, digests, size, mtime, owner, and relevant auth logs; inform L. Ferreira. (2) Investigate `debug.sh` (who created it, whether it ran, whether a listener is active) before removal — likely incident. (3) Revert `sshd_config` to the approved version under a change, after preservation; verify with `sshd -T`. (4) For `ntp.conf`: verify offset against both servers, then update the manifest with reference CHG-2210. (5) `fw-01.rules`: nothing.

**EX054 — Auto-fix list.** Re-enable log forwarding: auto-fix (restores visibility, no process effect). Correct NTP server list: auto-fix (time integrity, low risk). Reset `sshd_config`: ticket (preserve first; lock-out risk). Restart historian: ticket with operations (data gap). Push firewall rules: ticket with tests (can cut polling). Re-set PLC setpoint: never automated by security tooling — process control belongs to operations.

**EX055 — Halt guard.** Halt if the same key changes identically on more than 25 % of hosts (here 9 of 14 = 64 %). Most likely an unrecorded fleet change by the platform team or a stale manifest; check the change calendar and the desired-state repository. Until explained it remains a finding — an attacker with the automation account could produce the same pattern.

**EX056 — Preservation record.** Before printing the unapproved-change line: `rec = {"file": name, "old": manifest[name], "new": current[name], "size": p.stat().st_size, "mtime": p.stat().st_mtime}`; write it as JSON to `root / f"preserve-{name}.json"` and print its SHA-256. The record's digest must be stored off-host (case record or collector), because an administrator of the host could otherwise rewrite both the file and the record.

### Chapter 15: EX057–EX060

**EX057 — Paths matter.** Keep a `parent` map in the breadth-first search and walk back from each service. Paths: esx-03 → fep-01 → grid-ss3-telecontrol; esx-03 → ad-ops → scada-01 → water-telemetry; esx-03 → ad-ops → bms-server → hospital-bms. A second directory server on a different host breaks the water and hospital paths; the grid path needs fep-01 redundancy on another host.

**EX058 — New shared components.** After adding the nodes, shared by all three services: `esx-03` and `power-ups-a` (verified). `cell-carrier` affects water and grid. Changes: feed esx-02 and esx-03 from separate UPS units and circuits; give the most critical stations and the SS-3 telecontrol a second, independent communication path (different carrier or licensed radio).

**EX059 — Degraded-mode test.** First on a replica or standby HMI: block its directory traffic and test login with cached credentials and with the documented local emergency account. In production, in an agreed window with Kestrel Water operations present: block the HMI's path to ad-ops for 10 minutes at fw-01; confirm operators can log in and act, and that scada-01 polling continues (historian count). Stop conditions: any loss of operator view or control, any alarm; immediate rule removal as rollback. Evidence: rule change log, login records, historian counts.

**EX060 — Export direction.** hist-02 pushes the CSV over HTTPS to report-01 with a service credential that can only upload; the corporate account and stored password used to log in to hist-02 are removed and the password rotated; fw-01 permits only hist-02 → report-01 tcp/443, and nothing from Z6 to hist-02; include a SHA-256 digest of the file in the upload metadata and check it on receipt; alert if no push arrives by 06:30.

### Chapter 16: EX061–EX064

**EX061 — Repair a work instruction.** Defects: password in the document (and therefore compromised — rotate it); no preconditions or change record; no read-only mode; no expected results; "fix anything" authorizes unplanned change; operations told only afterwards; no stop conditions or rollback. Rewrite in the WI-KW-07 pattern: change record, control-room call before, vault reference for the credential, read-only export with expected results, findings recorded for a separate change, stop conditions, call after.

**EX062 — Transient device policy.** Policy: engineering work on control systems only from dedicated laptops built from a controlled image, never used for email or internet; pre-visit update and malware scan at a controlled station, recorded; removable media from a numbered pool, scanned, logged; every site connection recorded. Transition: scan the current laptop's project files on an isolated system, copy verified files to the new engineering laptop, record digests, then return the old laptop to corporate use only.

**EX063 — Safety boundaries.** Do not log in, test or change anything. Record device identity, location, time and how the condition was noticed (for example the login page displayed a default-credential notice in vendor documentation — not a login attempt). Report the same day to the Kestrel Grid protection engineer and L. Ferreira; the protection engineers decide on and make any change under their procedures. Store the finding with restricted access.

**EX064 — As-built record.** Example: fw-01 firmware version x.y; rule set digest (placeholder) stored in CHG-2215 and in the collector; rules R1, R2, R3, R7 as-built; deviation: R5 retained for logging (approved by L. Ferreira). hist-02: OpenSSH version; effective configuration digest from `sshd -T`; open deviation until EX010 is completed: `histsvc` shell; dated and signed by the implementer and verifier.

### Chapter 17: EX065–EX068

**EX065 — Read the episodes.** "*Observed:* 07:03–07:12Z, unknown host 10.20.0.31 sent device-ID queries to KW-04, KW-05, KW-06, one malformed frame to KW-07, and wrote 65,535 to KW-04 register 7 (pump-2 setpoint) at 07:04:40, 07:05:30 and 07:12:00. *Inferred:* reconnaissance followed by attempted setpoint changes. *Done:* nothing. *Open:* identity and owner of 10.20.0.31; whether KW-04 accepted the writes; how the host reached Z2. Request: Kestrel Water to check KW-04 pump 2 and setpoint now; preserve sensor data."

**EX066 — Fix the blind drop.** In the malformed branch, append NEW-TALKER when the source is unknown before `continue`. Verified output: NEW-TALKER 07:03:00–07:05:30Z ×6, alerts 13, episodes 5, records still accounted for (10 = 9 parsed + 1 dropped).

**EX067 — Window trade-off.** 1 minute: 6 episodes — NEW-TALKER splits into 07:03:00–07:03:02 (×3), 07:04:40–07:05:30 (×2), 07:12:00 (×1); UNAUTH-WRITE into 07:04:40–07:05:30 (×2) and 07:12:00; DEVICE-ID one. 10 minutes: 3 episodes — NEW-TALKER 07:03:00–07:12:00 ×6, DEVICE-ID ×3, UNAUTH-WRITE 07:04:40–07:12:00 ×3. All verified by running. Five minutes is a reasonable default for a human-paced activity; the 10-minute setting keeps the 07:12 write visible as part of the same activity, which is arguably better here — record the choice and revisit it with real data.

**EX068 — Value-range rule.** Add `POLICY = {7: (100, 400)}`; for function 6 decode `addr, val` from bytes 8–12; for 16 decode each value; alert `VALUE-RANGE` when an address in POLICY gets a value outside its range. It fires on the three 0xFFFF writes and not on eng-ws-15's write of 300. It detects but does not prevent: the device may still accept the write, so the firewall and access controls remain the preventive layer.

### Chapter 18: EX069–EX072

**EX069 — Project scope.** Example (station-router bypass): purpose — remove unauthorized paths to station Modbus via cellular routers; systems — twelve station routers (read), changes only on routers with findings; window — agreed per station with Kestrel Water; authorizer A. Mensah; supervisor L. Ferreira; stops — any communication loss or alarm. Requirements: no port-forward to tcp/502 on any router (negative: config check and VPN-client connect test); SCADA polls all stations (positive: historian count); router configs under drift detection (test: injected benign change detected); router management only from jump-01 (negative test). Artefacts: scope, baseline exports and digests, change records, test results, troubleshooting log, as-built record, manifest and seal.

**EX070 — Verify a seal.** After verification, compute `hashlib.sha256((d / "MANIFEST.sha256").read_bytes()).hexdigest()` and compare with `seal`: case 1 prints "seal OK" while `04-tests.csv` mismatches. Case 2: rewrite the manifest line for `04-tests.csv` with the new digest; every artefact now verifies "OK", but the manifest digest differs from the recorded seal, so the seal check fails. Only an externally stored seal reveals that the manifest itself was edited.

**EX071 — Handle the late addition.** (1) Retrieve version 1 of the package from the archive; check every artefact and the manifest against the externally recorded seal. (2) Restore `04-tests.csv` to the sealed content. (3) Save T10 results as `06-tests-addendum.csv` with collector and UTC time. (4) Create version 2 of the manifest including all six artefacts; compute seal 2. (5) Record seal 2 in the change record and the assessment form with the reason, keeping seal 1. (6) Never overwrite version 1.

**EX072 — Self-assessment.** Scope 3 (signed, owner and stops). Technical correctness 2 (R4 removed; R6 still present). Verification 2 (REQ-4 failing until R6 is removed; REQ-6 tested only after EX042). Troubleshooting 3 (KW-09 hypotheses, predictions, preservation). Documentation 2 (as-built pending for router findings). Evidence 2 until the post-seal edit is corrected, then 3. Honesty 3 if open items are listed. Open items: remove R6 (R. Kaur); router bypass check across all stations (network lead); REQ-6 regression test monthly (J. Tan); KW-09 incident outcome (L. Ferreira).

<a id="glossary"></a>

## Glossary

- **Conduit** — a declared communication path between zones with purpose, protocol, direction and owner (Chapter 6).
- **Contained laboratory** — a lab that technically cannot affect anything outside itself (Chapter 12).
- **CRC** — cyclic redundancy check; detects accidental corruption, not forgery (Chapter 9).
- **Drift** — difference between a host's actual configuration and its approved manifest (Chapter 14).
- **Effective configuration** — the settings a program actually uses after parsing its files, for example `sshd -T` (Chapter 3).
- **Episode** — a group of related alerts reported as one item with a count and time span (Chapter 17).
- **Exception response (Modbus)** — a reply whose function code has the high bit set, with an exception code such as 01, 02 or 03 (Chapter 12).
- **Known-answer test** — checking a tool against a published input and output before trusting it (Chapter 9).
- **MBAP header** — the 7-byte Modbus Application Protocol header on TCP (Chapter 2).
- **Negative / positive test** — a test that a forbidden action fails / that a needed function still works (Chapter 11).
- **Poll cycle** — time to refresh every polled device once (Chapter 1).
- **Quarantine** — keeping interpretable but implausible input for review (Chapter 4).
- **Record coordinates** — file, line and field identifying where a finding came from (Chapter 4).
- **Seal** — the digest of an evidence manifest, recorded outside the package (Chapter 18).
- **Shadowed rule** — a firewall rule that never takes effect because an earlier rule matches all its traffic with the opposite action (Chapter 10).
- **Stuck value** — a reading repeated longer than the process allows (Chapter 8).
- **Traceability** — the link from each requirement to the tests and evidence that verify it (Chapter 11).
- **Transient device** — a laptop or medium that moves between zones or sites (Chapter 16).
- **UID 0** — the root identity on Linux, whatever the account name (Chapter 3).
- **Zone** — a group of assets with similar security requirements (Chapter 6).

<a id="references"></a>

## References

Standards, guidance and public pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them. A citation supports the general claim beside it in the text, never the synthetic case details.

### Standards and guidance

- Cybersecurity and Infrastructure Security Agency. [Cyber-Attack Against Ukrainian Critical Infrastructure (IR-ALERT-H-16-056-01)](https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01). February 2016.
- Cybersecurity and Infrastructure Security Agency. [IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities (AA23-335A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a). December 2023.
- Cybersecurity and Infrastructure Security Agency. [PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure (AA24-038A)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a). February 2024.
- Cybersecurity and Infrastructure Security Agency. [Primary Mitigations to Reduce Cyber Threats to Operational Technology](https://www.cisa.gov/resources-tools/resources/primary-mitigations-reduce-cyber-threats-operational-technology).
- Cybersecurity and Infrastructure Security Agency. [Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals).
- Cybersecurity and Infrastructure Security Agency. [National Critical Functions Set](https://www.cisa.gov/national-critical-functions-set).
- DNP Users Group. [Overview of DNP3 Protocol](https://www.dnp.org/About/Overview-of-DNP3-Protocol). (The full protocol is standardized as IEEE Std 1815.)
- International Society of Automation. [ISA/IEC 62443 Series of Standards (overview)](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).
- MITRE. [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/).
- Modbus Organization. [Modbus specifications](https://www.modbus.org/modbus-specifications) — Modbus Application Protocol, Messaging on TCP/IP Implementation Guide, and Modbus/TCP Security.
- National Cyber Security Centre (UK). [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf).
- National Institute of Standards and Technology. [FIPS 180-4, Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final).
- National Institute of Standards and Technology. [SP 800-41 Rev. 1, Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final).
- National Institute of Standards and Technology. [SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
- National Institute of Standards and Technology. [SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).
- National Institute of Standards and Technology. [SP 800-86, Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final).
- National Institute of Standards and Technology. [SP 800-92, Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final).
- National Institute of Standards and Technology. [SP 800-115, Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final).
- National Institute of Standards and Technology. [SP 800-123, Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final).
- National Institute of Standards and Technology. [SP 800-128, Guide for Security-Focused Configuration Management of Information Systems](https://csrc.nist.gov/pubs/sp/800/128/upd1/final).
- National Institute of Standards and Technology. [SP 800-137, Information Security Continuous Monitoring (ISCM)](https://csrc.nist.gov/pubs/sp/800/137/final).

### Protocols, algorithms and software documentation

- Arkko, J., Cotton, M., and Vegoda, L. [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737). IETF, 2010.
- Bray, T. (ed.). [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259). IETF, 2017.
- Cook, G. [Catalogue of parametrised CRC algorithms with 16-bit width (CRC-16/DNP)](https://reveng.sourceforge.io/crc-catalogue/16.htm).
- Gerhards, R. [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424). IETF, 2009.
- Klyne, G., and Newman, C. [RFC 3339: Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339). IETF, 2002.
- Krawczyk, H., Bellare, M., and Canetti, R. [RFC 2104: HMAC: Keyed-Hashing for Message Authentication](https://www.rfc-editor.org/rfc/rfc2104). IETF, 1997.
- Mills, D., Martin, J., Burbank, J., and Kasch, W. [RFC 5905: Network Time Protocol Version 4](https://www.rfc-editor.org/rfc/rfc5905). IETF, 2010.
- OpenBSD project. [sshd_config(5) manual page](https://man.openbsd.org/sshd_config).
- Python Software Foundation. [struct](https://docs.python.org/3/library/struct.html), [socket](https://docs.python.org/3/library/socket.html), [hashlib](https://docs.python.org/3/library/hashlib.html) and [ipaddress](https://docs.python.org/3/library/ipaddress.html). Python 3 documentation.
- Rekhter, Y., et al. [RFC 1918: Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918). IETF, 1996.
- Shafranovich, Y. [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180). IETF, 2005.

### Research

- Rinaldi, S. M., Peerenboom, J. P., and Kelly, T. K. [Identifying, Understanding, and Analyzing Critical Infrastructure Interdependencies](https://doi.org/10.1109/37.969131). *IEEE Control Systems Magazine*, 21(6), 11–25, 2001.
