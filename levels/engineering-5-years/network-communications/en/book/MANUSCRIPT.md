# Network and Communications Security: Engineering Course

- Language: English (`en`); course 126, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Eight offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students who must specify, design, build, verify and defend a segmented, monitored network for a real organisation under governance and budget constraints.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student redesigning a district council's flat network across eight offices, from foundations in probability, addressing and protocols through requirements, threat analysis, architecture options, zone policy, migration, monitoring, redundancy, verification, operations and an evidence-based capstone, thesis and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Kofi Mensah** | Engineering student | Invented |
| **Dr Elena Vasquez** | Supervisor | Invented |
| **Ravenmoor Institute of Technology** | Fictional institute | Invented |
| **Ashcombe District Council** | Fictional partner (eight offices) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |
| [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to describe network quantities; (2) interpret derivatives of traffic and queue length; (3) connect limits to capacity planning.

### 1.1 The case

Kofi Mensah is a five-year engineering student at the fictional Ravenmoor Institute of Technology, supervised by Dr Elena Vasquez. His long project is with the fictional Ashcombe District Council, whose eight offices share one flat network: staff laptops, servers, desk phones, CCTV cameras and guest Wi-Fi all sit in the same address space and can reach each other freely. Last year a guest laptop infected with malware was found trying to connect to council file servers. Nothing was lost, but the council asked for a segmented design and secure links between offices. This book follows Kofi from foundations to a defended engineering thesis.

### 1.2 Rates of change

Network engineering is full of quantities that change over time: bytes transferred, queue lengths in a router, the number of active connections. The derivative of transferred bytes with respect to time is throughput. If a backup job's transferred total grows as a smooth curve, the slope at any moment tells Kofi the instantaneous rate, which matters when checking whether a link of fixed capacity will be saturated. A steep slope at 02:00 in the council's traffic graph is the nightly backup, and its peak rate decides whether that link needs more capacity.

### 1.3 Queues and limits

A router queue grows when packets arrive faster than they can be sent. If arrival rate exceeds service rate by a constant amount, queue length grows linearly; its derivative is that difference. As utilisation approaches one, average waiting time in simple queue models grows without bound, which is a limit in the calculus sense. Kofi uses this to explain to council staff why a link at 95 percent utilisation feels far slower than one at 70 percent, even though the difference in load looks small.

### 1.4 Why this matters for security

Security controls add work to the network path. A firewall inspecting traffic has a service rate; if inspection slows it, queues build at busy times. Kofi will later measure added latency, and calculus gives him the language to reason about how small increases in per-packet cost become large delays near capacity. It also helps him read rate-based alerts, such as a sudden rise in connection attempts, as changes in slope rather than raw counts.

Security decisions in networks are quantitative more often than they look. Whether a link can absorb a backup and an incident response capture at once, or how quickly a log store fills, are questions of rates and totals. An engineer who can estimate them catches impossible plans early, before a control is designed that the network cannot carry.

### Worked example

Given cumulative backup bytes B(t) = 2t² gigabytes for t in hours from 0 to 3, the throughput is B'(t) = 4t GB per hour, peaking at 12 GB per hour at the third hour, which Kofi compares with the inter-office link capacity.

> **Synthetic case.** Kofi Mensah, Ravenmoor Institute of Technology, Ashcombe District Council and all figures are synthetic.

### Errors and limits

Real traffic is bursty, not smooth; derivatives of fitted curves describe trends, not individual packets.

### Exercises

- **EX001 — Throughput derivative.** If B(t) = 5t + t² GB, what is throughput at t = 4 hours? *Rubric:* 3 = 13 GB/h with method;; 2 = correct value only;; 1 = method without value;; 0 = none.
- **EX002 — Utilisation intuition.** Explain why delay rises sharply as utilisation approaches 1. *Rubric:* 3 = waiting time grows without bound in queue models;; 2 = queues grow;; 1 = none;; 0 = none.
- **EX003 — Security link.** How does a firewall's service rate relate to queue growth? *Rubric:* 3 = slower inspection lowers service rate, queues at peaks;; 2 = slows traffic;; 1 = none;; 0 = none.

### Synthesis

Calculus turns traffic graphs into rates and helps reason about queues and the cost of inspection near capacity.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) model networks as graphs; (2) use sets and relations for policy; (3) reason about paths and reachability.

### 2.1 Graphs for networks

A network is naturally a graph: devices or zones are vertices and links or permitted flows are edges. In Ashcombe's flat network, every zone can reach every other, so the zone graph is complete. Segmentation removes edges. Graph theory lets Kofi count paths, find which vertices are reachable from a compromised one and check that no unintended path exists, for example from guest Wi-Fi to the file servers through some intermediate zone.

Treating zones as nodes and permitted flows as directed edges lets Kofi ask exact questions: which zones can reach the file servers, and through how many hops. Direction matters, because a rule allowing staff to reach printers does not allow printers to reach staff, and confusing the two is a common design error.

### 2.2 Sets and relations

A firewall policy can be described as a relation: a set of ordered pairs of source and destination zones, each with permitted services. Set operations answer design questions. The intersection of what is allowed and what is needed shows justified rules; the difference between allowed and needed shows excess access. Kofi writes the needed flows as a set first, then designs rules to match it exactly, which is the least privilege principle of Saltzer and Schroeder expressed mathematically.

Writing the allowed relation and the needed relation as sets makes review mechanical: excess access is the difference between them.

### 2.3 Reachability and closure

Direct rules are not the whole story. If guest can reach a print server and the print server can reach file servers, guest has an indirect path. The transitive closure of the reachability relation captures all such paths. Kofi computes closures for candidate designs to confirm that removing one edge actually isolates a zone rather than leaving a detour.

The transitive closure of the allowed relation shows every pair that can communicate through intermediate zones, including paths no single rule mentions. If a guest zone can reach a print server, and the print server can reach file servers, then guests indirectly reach files. Reviewing the closure, not just the rule list, is what exposes such chains.

### 2.4 Counting

With six zones there are thirty directed pairs. Each pair can be allowed or denied for each service, so the number of possible policies is enormous. Counting shows why designs need principles, such as default deny, rather than case-by-case choices.

With n zones there are n times n minus one directed pairs, so eight zones give fifty-six. Multiply by dozens of services and the space of possible rule sets is vast. Default deny reduces the decision to listing the few flows that are needed, which is both shorter to write and far easier to review than listing everything forbidden.

### Worked example

For zones {guest, print, files} with edges guest→print and print→files, the closure adds guest→files, revealing an indirect path that the direct rules hid.

> **Synthetic case.** Zones are synthetic.

### Errors and limits

Reachability on zones ignores which services are permitted; a full model needs the service dimension too.

### Exercises

- **EX004 — Excess access.** Given allowed A and needed N, which set shows excess access? *Rubric:* 3 = A minus N with explanation;; 2 = A−N;; 1 = other;; 0 = none.
- **EX005 — Indirect path.** Find the closure for a→b, b→c, c→d and list new pairs. *Rubric:* 3 = a→c, a→d, b→d;; 2 = two;; 1 = none;; 0 = none.
- **EX006 — Pair count.** How many directed pairs exist among 8 zones? *Rubric:* 3 = 56 with reasoning;; 2 = 56;; 1 = wrong;; 0 = none.

### Synthesis

Graphs and relations make segmentation designs precise and expose indirect paths.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate signal propagation to latency; (2) understand wireless coverage; (3) consider physical layer security.

### 3.1 Propagation delay

Signals in fibre travel at roughly two thirds of the speed of light, about 200 kilometres per millisecond. Between two Ashcombe offices 40 kilometres apart, one-way propagation is about 0.2 milliseconds; most observed delay comes instead from queues and processing. This tells Kofi where latency budgets go and why adding a firewall hop matters more than distance within the district.

Signals travel through fibre at roughly two thirds of the speed of light, about five microseconds per kilometre. That floor cannot be engineered away, so a link between distant offices always adds delay, and protocols or controls that need many round trips feel slower across it. Measured latency well above the propagation floor points to queuing or processing instead.

### 3.2 Wireless coverage

Wi-Fi signals weaken with distance and walls. Access points placed for good indoor coverage often also cover car parks, so guest and staff networks can be heard outside buildings. NIST SP 800-153 recommends considering coverage when securing wireless networks. Kofi notes that physical leakage is a reason to require strong authentication and encryption rather than relying on the building as a boundary.

Radio signal strength falls quickly with distance and walls, so coverage maps never stop neatly at building edges. A guest network that is usable in a car park is reachable by anyone parked there. Engineers therefore plan access point placement and transmit power with coverage boundaries in mind, and treat wireless as reachable from outside regardless.

### 3.3 Electrical and physical layer

Network cabinets in offices hold switches whose ports anyone with physical access could use. Physical security of cabinets and disabling unused ports are basic controls. Kofi records cabinet locations and port counts during site visits.

The physical layer is where many security assumptions quietly rest. An unused wall port that is still patched to a switch gives anyone in the room network access, and a cable run through a shared ceiling can be tapped or disconnected. Disabling unused ports, labelling patch panels and locking wiring closets are physical controls that support every logical control above them. Engineers should record these in the same inventory as switches and rules.

### 3.4 Power and heat

Firewalls and switches need stable power and cooling. A security appliance that overheats in a cupboard becomes a reliability problem. Kofi checks that each site's cabinet has ventilation and an uninterruptible power supply.

Network equipment fails when power is lost or when cooling fails, so availability depends on facilities as much as configuration. Uninterruptible power supplies give minutes, not hours, and a closet without ventilation can overheat a switch on a summer weekend. Engineers estimate load in watts, check supply runtime, and decide which devices must stay up during an outage, such as core switches and the firewall, before choosing what may shut down.

### Measuring delay in practice

Kofi checks his estimates against measurements supplied by the council's network team. Round-trip times between offices average about three milliseconds, so propagation accounts for well under a fifth of the delay. Most of the rest comes from switches, routers and the existing edge devices. This matters for the design: adding a firewall hop at each site will add processing delay of the same order as current equipment, so the latency budget must be set from measurement rather than from distance. He records the measured baseline so later chapters can compare against it.

### Worked example

For a 40 km fibre path, propagation is 40 / 200 = 0.2 ms one way, small compared with a measured 3 ms round-trip time dominated by equipment.

> **Synthetic case.** Distances are synthetic.

### Errors and limits

Copper and wireless have different propagation and loss characteristics; do not apply fibre figures universally.

### Exercises

- **EX007 — Propagation estimate.** Estimate one-way propagation over 120 km of fibre. *Rubric:* 3 = 0.6 ms with method;; 2 = value;; 1 = none;; 0 = none.
- **EX008 — Car park coverage.** Why does Wi-Fi reaching a car park matter for security? *Rubric:* 3 = outsiders can connect or listen; need auth and encryption;; 2 = exposure;; 1 = none;; 0 = none.
- **EX009 — Unused ports.** Give one physical layer control for office cabinets. *Rubric:* 3 = locked cabinets or disabled unused ports;; 2 = lock;; 1 = none;; 0 = none.

### Synthesis

Physics sets latency floors and explains why wireless and physical access shape security design.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small Python programs to parse network data; (2) use the ipaddress module; (3) test with synthetic inputs.

### 4.1 Why program

Network engineers handle lists of addresses, rules and flows that are too long to check by hand. Kofi writes small Python programs using only the standard library, which runs on any council machine without installing packages. Each program reads synthetic data, computes a result and prints a clear summary.

Manual checks do not scale: comparing a few hundred rules or addresses by eye is slow and error-prone, and the same check must be repeated after every change. A short program performs the comparison identically each time, produces output that can be saved as evidence, and lets another engineer rerun it to confirm the result. That repeatability is the real reason engineers program.

### 4.2 The ipaddress module

Python's ipaddress module understands networks and addresses. It can check whether an address belongs to a subnet, split a block into smaller subnets and test whether two networks overlap. These operations are exactly what subnet planning and rule analysis need, and using a tested library avoids errors in hand-written bit manipulation.

Python's standard ipaddress module parses addresses and networks, tests membership, and detects overlapping subnets correctly, including edge cases such as host bits set in a network definition. Using it avoids fragile string handling. For example, checking whether a proposed subnet overlaps any existing one becomes a loop over network objects calling overlaps, which is clear to read and easy to test.

### 4.3 Structuring a script

Kofi's scripts follow one pattern: a docstring explaining purpose, input data near the top, small functions for each step and a final summary line. This makes them easy for council engineers to read and adapt.

A useful script separates three parts: reading input, computing results, and printing a report. Keeping the computation in small functions with clear names lets each be tested on its own and reused later. Constants such as file names belong at the top, and the main block simply calls the functions in order. This structure makes a script readable months later, when the original author has forgotten the details.

### 4.4 Testing

Each script is tested with inputs where the answer is known, including edge cases such as a /32 single address or an empty rule list. Tests are kept with the scripts.

A test feeds a function a small, known input and checks the output against an answer worked out by hand. For network scripts, good test cases include an exact overlap, adjacent subnets that do not overlap, and invalid input. Writing tests before trusting a script on real data catches mistakes cheaply, and rerunning them after every change shows nothing that worked before has broken.

### Reading data files

Most of Kofi's inputs arrive as CSV exports from the council's tools. Python's csv module reads them into dictionaries keyed by column name, which makes scripts robust to column order changes. He checks that the expected columns exist before processing and prints a clear error if one is missing, rather than failing later with a confusing message. Dates are parsed with the datetime module and stored in UTC, because logs from different devices may use different local time settings and comparisons only make sense on a common clock.

### Worked example

A ten-line script checks whether 10.40.12.5 is in 10.40.12.0/25 using ip_address(...) in ip_network(...), printing True.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Strings like "10.40.12.0/25" with host bits set raise errors unless strict=False is used; understand why before suppressing it.

### Exercises

- **EX010 — Membership check.** Write the expression testing whether 192.168.5.9 is in 192.168.5.0/24. *Rubric:* 3 = correct code;; 2 = near;; 1 = none;; 0 = none.
- **EX011 — Edge cases.** Name two edge cases for a subnet-splitting script. *Rubric:* 3 = /32 and overlapping input;; 2 = one;; 1 = none;; 0 = none.
- **EX012 — Library choice.** Why prefer ipaddress over manual bit operations? *Rubric:* 3 = tested, fewer errors;; 2 = easier;; 1 = none;; 0 = none.

### Synthesis

Small, tested standard-library scripts are the engineer's tools for checking designs.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write design documents for mixed audiences; (2) draw clear network diagrams; (3) present trade-offs.

### 5.1 Audiences

Kofi's work will be read by council IT staff, managers and examiners. Each needs different detail. Managers need the problem, the decision and the cost; engineers need addressing, rules and procedures; examiners need method and evidence. He plans each document by asking who will read it and what they must decide.

Different readers need different things from the same design. Council managers want cost, risk and disruption in plain terms; operations staff need exact steps and rollback plans; auditors need evidence that controls exist and are checked. Writing one document that tries to serve all three usually serves none, so engineers prepare a short summary, a technical design and a separate evidence record.

### 5.2 Diagrams

A good network diagram shows zones, the controls between them and the direction of permitted flows, using a legend. Kofi draws a logical diagram of zones and policy separately from a physical diagram of sites and links, because mixing them makes both unreadable.

A good network diagram shows zones, the boundaries between them, and the permitted flows, with a legend explaining symbols. It should omit detail that does not help the reader's decision, such as every cable, while keeping what does, such as where the firewall sits. Dating each diagram and keeping it with the design prevents people from trusting an outdated picture.

### 5.3 Trade-off tables

Design choices are presented as tables of options against criteria: security, cost, complexity and operational effort. Each cell has a short justification, so readers can disagree with a judgement rather than the whole table.

A trade-off table lists options as rows and criteria as columns, such as cost, security benefit, operational effort and disruption. Filling every cell forces the engineer to consider each option fairly, and stating the evidence behind each score makes the comparison checkable. Readers can then disagree with a specific cell rather than with the whole recommendation, which makes review discussions far more productive.

### 5.4 Plain language

Terms like segmentation are explained once in plain words: dividing the network so a problem in one part cannot easily spread to others.

Plain language means short sentences, familiar words, and defining any technical term on first use. Instead of writing that inter-VLAN routing will be restricted via ACLs, write that the network will stop guest devices from reaching staff computers. Readers who are not engineers make funding and approval decisions, so if they misunderstand the design, even an excellent technical plan may not be adopted. Testing a draft on a non-specialist colleague quickly reveals unclear passages.

### Writing a design decision record

For each significant choice, Kofi writes a short decision record: the context, the options considered, the decision and its consequences. Records are numbered and never deleted; if a decision changes, a new record supersedes the old one and links to it. This gives the council a history of why the network looks the way it does, which is valuable when staff change. It also helps examiners follow the reasoning in his thesis, because each design element can be traced to a recorded decision rather than reconstructed afterwards.

### Worked example

Kofi's one-page summary for managers states the problem (guest malware reaching servers), the proposal (six zones with default-deny policy) and the decision needed (budget for two firewalls).

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Diagrams without legends or direction arrows are often misread.

### Exercises

- **EX013 — Manager summary.** What three things should a manager summary contain? *Rubric:* 3 = problem, proposal, decision/cost;; 2 = two;; 1 = one;; 0 = none.
- **EX014 — Logical vs physical.** Why separate logical and physical diagrams? *Rubric:* 3 = readability, different purposes;; 2 = clarity;; 1 = none;; 0 = none.
- **EX015 — Trade-off cells.** Why justify each trade-off cell? *Rubric:* 3 = allow targeted disagreement;; 2 = clarity;; 1 = none;; 0 = none.

### Synthesis

Clear documents and diagrams let each audience make its decisions.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use integrals to compute totals from rates; (2) apply exponential models; (3) estimate data volumes.

### 6.1 Totals from rates

If throughput r(t) is known over a day, the integral gives total data transferred. Kofi integrates a fitted rate curve for the nightly backup to estimate daily volume over the inter-office link, which feeds capacity planning for the new encrypted tunnels.

If a link carries data at a known rate, the total transferred is the rate multiplied by time, or the area under the rate curve when the rate varies. Engineers use this to estimate log volumes and backup sizes. For example, a sensor producing two megabytes of logs per minute generates about 2.9 gigabytes per day, which tells Kofi how much storage a retention period needs before any purchase.

### 6.2 Exponential decay and growth

Some quantities change in proportion to their size. The probability that a link has not yet failed often follows an exponential model, and log volumes may grow roughly exponentially as more devices are added. Kofi uses these models carefully as approximations.

Many network quantities change in proportion to their current size. Traffic that grows by a fixed percentage each month grows exponentially, so capacity that seems ample today can run out sooner than a straight-line estimate suggests. Decay works the other way: the share of devices still running an old firmware version often halves over a regular period. Fitting the right model prevents both overspending and surprise shortfalls.

### 6.3 Retention estimates

Logging every allowed and denied flow creates large volumes. If flow records arrive at a rate that grows over the day, integrating gives daily volume, and multiplying by retention days gives storage needs. This helps size log storage for the ninety days the council requires.

Retention planning combines daily volume, compression, and the number of days records must be kept. Thirty days of three gigabytes per day is ninety gigabytes before compression, and engineers add headroom for growth and incident surges, when logging often increases sharply. The required period comes from policy and investigation needs, not from what happens to fit on an existing disk.

### 6.4 Checking with data

Models are checked against measured totals. If an integral predicts 50 GB but measurements show 70 GB, the model is wrong and Kofi revises it.

Models are only useful if they match reality, so engineers compare estimates with measured values from a pilot. If measured log volume is double the estimate, the assumptions need revisiting before the full rollout.

Engineers record each assumption, such as events per device per minute and average record size, so a mismatch can be traced to the specific assumption that was wrong. The corrected model then becomes the basis for the full plan.

### Growth and headroom

Capacity plans must look ahead. If the number of council devices grows by about eight percent a year, log volume grows roughly in proportion, and compound growth over five years raises volume by nearly half. Kofi models this as exponential growth and plans storage with headroom for five years, then checks the plan yearly against actual volume. He also notes that growth is not smooth: a new office or a camera upgrade can add a step change, so the yearly review asks the council about planned projects as well as measuring trends.

### Worked example

With r(t) = 2 + sin(πt/12) GB per hour over 24 hours, the integral is 48 GB because the sine term integrates to zero over a full period.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

Integrating a poor model gives precise-looking wrong answers; validate against measurement.

### Exercises

- **EX016 — Integral total.** Integrate r(t) = 3 GB/h over 8 hours. *Rubric:* 3 = 24 GB;; 2 = value;; 1 = none;; 0 = none.
- **EX017 — Storage estimate.** If flow logs total 2 GB per day, estimate 90-day storage. *Rubric:* 3 = 180 GB with headroom note;; 2 = 180 GB;; 1 = none;; 0 = none.
- **EX018 — Model check.** What should Kofi do when a model underpredicts measured volume? *Rubric:* 3 = revise model;; 2 = note;; 1 = none;; 0 = none.

### Synthesis

Integration turns rates into volumes for capacity and storage planning.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) model failures probabilistically; (2) summarise measurements; (3) reason about uncertainty.

### 7.1 Random failures

Link failures are often modelled as a Poisson process: independent events at an average rate. With six inter-office links each failing about 1.2 times a year, the total rate is 7.2 a year. The model gives the probability of any number of failures, which helps decide how much redundancy and on-call cover are needed.

Hardware such as power supplies and disks fails at random times, but at fairly stable average rates. Modelling failures as random events with a known rate lets engineers estimate how often a device will be unavailable over a year. This turns vague worries into numbers that support choices such as buying a spare switch, adding redundant links, or accepting the risk for a minor office.

### Lab — Link failure probabilities

```python
"""Probability of k WAN link failures in a year if failures are Poisson with mean 1.2 per link-year over 6 links (stdlib only)."""
import math
lam = 1.2 * 6
for k in range(0, 13, 2):
    print(f"P(failures = {k:2d}) = {math.exp(-lam) * lam**k / math.factorial(k):.4f}")
print(f"P(failures >= 10) = {1 - sum(math.exp(-lam) * lam**k / math.factorial(k) for k in range(10)):.4f}")
```

Run with `python3 lab_poisson.py`. Verified output:

```text
P(failures =  0) = 0.0007
P(failures =  2) = 0.0194
P(failures =  4) = 0.0836
P(failures =  6) = 0.1445
P(failures =  8) = 0.1337
P(failures = 10) = 0.0770
P(failures = 12) = 0.0303
P(failures >= 10) = 0.1904
```

### 7.2 Reading the result

The most likely yearly counts are around six to eight. The chance of ten or more failures is about 19 percent, not negligible. Kofi concludes that relying on single links for critical services will regularly cause outages, which supports redundant tunnels later.

A model result such as a 0.3 percent chance of two simultaneous failures in a year is an estimate under stated assumptions, not a guarantee. Kofi reports it with those assumptions, notes that failures sharing a cause such as a power cut are not independent, and explains what the number means in practical terms for council staff.

### 7.3 Summarising measurements

Latency samples are summarised with median and high percentiles rather than mean alone, because a few slow packets matter to users. Kofi reports p95 as well as median.

Measurements such as latency vary, so a single average hides important behaviour. The median shows the typical experience, while a high percentile such as the 95th shows how bad the slow cases get, which is often what users notice. Reporting both, along with the number of samples and the measurement period, lets readers judge whether the summary reflects normal conditions.

### Percentiles and outliers

Latency and throughput measurements rarely follow neat distributions. A few very slow samples, from a busy moment or a retransmission, can pull the mean far from typical experience. Kofi reports the median as the typical value and the 95th percentile to describe the slow tail that users notice. He also keeps the maximum, because a single extreme value may reveal a real fault, such as a misconfigured interface. Reporting these three numbers together gives a fair picture without hiding either the typical case or the bad moments.

### Uncertainty in small samples

Some of Kofi's measurements come from short tests with a few dozen samples. Estimates from small samples are uncertain, and two tests can differ simply by chance. He therefore reports how many samples each figure is based on and avoids treating small differences as meaningful. Where a decision depends on a measurement, such as whether a firewall meets a latency budget, he repeats the test at a different time of day. Consistent results across repeats give more confidence than one precise-looking number from a single short run.

### Worked example

Using the lab, Kofi reports P(failures ≥ 10) ≈ 0.19 to the council.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

Poisson assumes independence; storms or shared ducts cause correlated failures.

### Exercises

- **EX019 — Total rate.** What is the combined yearly failure rate for 6 links at 1.2 each? *Rubric:* 3 = 7.2;; 2 = value;; 1 = none;; 0 = none.
- **EX020 — Tail probability.** What is P(≥10 failures) in the lab? *Rubric:* 3 = 0.1904;; 2 = about 0.19;; 1 = wrong;; 0 = none.
- **EX021 — Independence limit.** Give one reason link failures may not be independent. *Rubric:* 3 = shared duct or weather;; 2 = correlation;; 1 = none;; 0 = none.

### Synthesis

Probability models turn failure rates into planning decisions.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe how network devices process packets; (2) understand fast and slow paths; (3) relate hardware limits to security features.

### 8.1 Packet processing

Switches and routers forward packets using specialised hardware that looks up destinations quickly. Firewalls do more: they track connection state and evaluate rules. Some work happens in fast hardware paths, some in a general-purpose processor.

Each packet arriving at a router or firewall goes through steps: it is received, its headers are parsed, a forwarding or policy decision is made, and it is queued for output. Every step costs time and processing capacity. Understanding this pipeline explains why enabling extra inspection features reduces throughput, and why the stated capacity of a device depends on which features are switched on.

### 8.2 Fast and slow paths

New connections often go through a slower path for rule evaluation; later packets of the same connection follow a fast path using cached state. A sudden surge of new connections can therefore load a firewall more than high throughput on existing ones.

Many devices handle ordinary packets on a fast path, often in dedicated hardware, while unusual packets go to a slower general processor. Packets needing logging, fragmentation handling or certain options may take the slow path. If a design causes much traffic to be logged individually, the slow path can become a bottleneck, so engineers check which features force slow-path handling before enabling them widely.

### 8.3 Memory and state tables

Stateful firewalls hold a table of active connections. Each entry uses memory; the table has a maximum size. Kofi notes table capacity when sizing firewalls for council sites.

Stateful firewalls remember each active connection in a table. The table has a fixed size, so a sudden increase in connections, whether from a legitimate surge or a fault, can fill it, after which new connections are refused. Engineers size tables from measured peak connection counts with headroom, and monitor table usage so they are warned before it becomes full.

### 8.4 Feature cost

Enabling deep inspection or decryption uses more processor time, lowering throughput. Vendors publish separate throughput figures for these features, which Kofi compares with expected load.

Vendor data sheets often quote throughput with few features enabled. With deep inspection, logging and encryption switched on, real capacity can be much lower. Engineers ask for figures under the planned configuration, or test in a lab with representative synthetic traffic, before relying on a device in production.

Monitoring processor and memory load after enabling a feature confirms whether the estimate held.

### Encryption offload

Encrypting inter-office tunnels with IPsec uses processor time for every packet. Many firewalls include hardware that accelerates the cryptographic operations, so tunnel throughput depends heavily on whether this offload is available for the chosen algorithms. NIST SP 800-77 Rev. 1 recommends modern algorithms such as AES in GCM mode, which are commonly accelerated. Kofi checks that candidate devices accelerate the algorithms he intends to use, because a device that falls back to software encryption could become the bottleneck for backups between offices.

### Hardware lifecycle

Network security devices receive firmware updates that fix flaws and add features, but only for as long as the vendor supports the model. A firewall bought near the end of its product life may stop receiving updates within a few years. Kofi records the vendor's published end-of-support dates for each candidate and prefers models with at least five years of remaining support. He also notes that firmware updates usually require a reboot, which shapes the redundancy design: with a pair of firewalls, one can be updated while the other carries traffic.

### Worked example

A candidate firewall rated 5 Gb/s plain but 1 Gb/s with inspection is adequate for a 400 Mb/s site with margin.

> **Synthetic case.** Specifications are synthetic.

### Errors and limits

Datasheet figures are measured under ideal conditions; plan with margin.

### Exercises

- **EX022 — Connection surge.** Why can many new connections stress a firewall more than high throughput? *Rubric:* 3 = slow path per new connection;; 2 = slow path;; 1 = none;; 0 = none.
- **EX023 — State table.** What happens when the state table is full? *Rubric:* 3 = new connections dropped or evicted;; 2 = failures;; 1 = none;; 0 = none.
- **EX024 — Margin.** Why size firewalls with margin over datasheet figures? *Rubric:* 3 = ideal conditions, growth;; 2 = safety;; 1 = none;; 0 = none.

### Synthesis

Understanding packet paths explains why security features affect performance.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger analysis programs; (2) read configuration files safely; (3) handle errors.

### 9.1 Larger programs

As analysis grows, Kofi splits scripts into modules: parsing, policy evaluation and reporting. Each module has tests.

As scripts grow beyond a page, structure becomes essential. Splitting code into modules by purpose, such as parsing, analysis and reporting, keeps each part small enough to understand. Clear function names, short docstrings, and avoiding global variables make it possible for a colleague to review the code and for Kofi to change one part without breaking another.

A short README explaining how to run the program completes the structure.

### 9.2 Parsing configurations

Exported firewall configurations are text. Kofi parses them into structured records, rejecting lines he cannot interpret rather than silently skipping them.

Device configurations are text with structure: sections, indentation and keywords. A parser reads that text into data structures such as lists of rules, each with source, destination, service and action fields. Once parsed, rules can be checked automatically for problems such as overly broad sources, duplicates or unused objects. Parsers should be written for synthetic samples first and should report lines they cannot understand rather than silently skipping them.

### 9.3 Error handling

Programs report clear errors on malformed input, naming the line. Silent failures could hide missing rules.

Real input is messy: files are missing, lines are malformed, values are out of range. A robust script detects these cases, reports them clearly with the line number, and either continues safely or stops. Silent failure is the worst outcome, because a script that ignores a malformed rule may report a clean policy that is actually wrong. Explicit error messages make problems visible to the person running the check.

### 9.4 Reproducibility

Scripts and synthetic inputs are versioned together, so any result can be regenerated.

A result is reproducible when someone else can run the same script on the same input and get the same output. That requires recording the script version, the input file, and any settings, and avoiding hidden dependencies such as the current date or random values without a fixed seed. Reproducibility turns analysis into evidence that reviewers can trust.

Saving the output alongside these details completes the record.

### Working with structured exports

Some council tools export configurations as JSON rather than text. Python's json module loads these into nested dictionaries and lists, which are easier to process reliably than free text. Kofi writes small functions that convert each vendor's export into a common internal format: a list of rules with source, destination, service and action. Converting early means the rest of his analysis code works the same way regardless of where the data came from, and adding support for a new device only requires a new converter.

### Command-line interfaces

To make scripts usable by council engineers, Kofi gives them simple command-line options using the argparse module: the input file, an optional output file and a verbose flag. Help text explains each option. This avoids engineers editing code to change file names, which is where mistakes creep in. Each script exits with a non-zero status when it finds a problem, such as a rule that violates policy, so it can be used later in automated checks before a configuration is deployed.

### Code review

Before council engineers rely on a script, a second person reads it. Review catches mistakes that tests miss, such as a comparison that treats port 0 as false, and spreads understanding so the council is not dependent on one author. Kofi keeps scripts short enough to review in one sitting and writes comments explaining why, not what. Review comments and their resolutions are kept with the code history, which also shows examiners how quality was checked. Reviewers use a short checklist covering input handling, edge cases and output format.

### Worked example

A parser reads "allow staff servers 443" lines into tuples and raises an error on "allow staff" missing fields.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Skipping unparseable lines can silently omit rules from analysis.

### Exercises

- **EX025 — Module split.** Name three modules for a policy analysis tool. *Rubric:* 3 = parse, evaluate, report;; 2 = two;; 1 = one;; 0 = none.
- **EX026 — Silent skip risk.** Why reject unparseable lines? *Rubric:* 3 = avoid missing rules;; 2 = safety;; 1 = none;; 0 = none.
- **EX027 — Error message.** What should an error message include? *Rubric:* 3 = line number and content;; 2 = line;; 1 = none;; 0 = none.

### Synthesis

Structured, tested, versioned code makes analysis trustworthy.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional ethics; (2) work within authorisation; (3) consider safety of public services.

### 10.1 Professional duties

Engineers hold public safety and trust. Council networks support services such as social care and emergency planning; outages can harm residents.

Engineers working on public infrastructure owe duties to the people who rely on it, not only to whoever pays. That means telling the client honestly about risks, staying within competence, declaring conflicts of interest, and refusing to sign off work that is unsafe. Professional bodies publish codes of conduct that set out these duties, and students should read the one that applies to them.

### 10.2 Authorisation

Kofi's project agreement lists what he may do: review configurations and logs, design, and test in a lab. He does not scan or probe council networks; tests on production happen only with council staff, in approved windows.

Security work on any network needs written permission from someone entitled to give it, stating scope, timing and methods. Without it, even well-meant checks can be illegal and can disrupt services. Kofi keeps signed authorisation from the council for each activity, works only on in-scope systems, and stops and asks if he finds he needs to go beyond the agreed boundary.

### 10.3 Data care

Logs contain staff and resident information. Kofi works with pseudonymised exports and synthetic data.

Network data such as logs and captures can contain personal information: addresses linked to people, browsing records, or message contents. Engineers collect only what the purpose needs, store it securely, limit who can access it, and delete it when the retention period ends. For teaching and testing, synthetic data avoids these risks entirely and should be the default.

Access to real data should itself be logged and periodically reviewed.

### 10.4 Change safety

Network changes can cut services. Every change has a rollback plan and is scheduled with service owners.

Every change to a live network carries a risk of disruption. Safe practice is to plan the change, have it reviewed, schedule it for a low-impact time, prepare a tested rollback, and verify afterwards that services still work. Recording each step creates a trail that helps later investigation if something does go wrong, and builds trust with the organisation.

Changes that fail are reviewed without blame to improve the process.

### Professional codes

Professional bodies publish codes of conduct that set expectations for engineers: act in the public interest, work within competence, be honest about results and respect confidentiality. Kofi reads his institution's code and the ACM Code of Ethics and notes how each applies to his project. Working within competence, for example, means he asks the council's specialists before advising on telephony quality, an area he has not studied. Being honest about results means reporting limitations in his measurements even when they weaken his recommendations.

### Safety of critical services

Some council systems support urgent work: the out-of-hours social care line, emergency planning and CCTV used by public safety teams. A network change that breaks these is a safety issue, not just an inconvenience. Kofi identifies these services with the council and marks them in his design. Changes affecting them are scheduled in agreed windows, tested in the lab first, and have a named owner available during the change. Failure modes are considered too: if a firewall fails, these services must fail over rather than stop.

### Worked example

Kofi declines a request from a staff member to test whether guest Wi-Fi can reach servers by trying it himself, and instead asks the network team to check firewall configuration.

> **Synthetic case.** The scenario is synthetic.

### Errors and limits

Good intentions do not replace authorisation.

### Exercises

- **EX028 — Probing request.** How should Kofi handle a request to probe the network himself? *Rubric:* 3 = decline, route to authorised team;; 2 = decline;; 1 = accept;; 0 = none.
- **EX029 — Rollback.** Why must every change have rollback? *Rubric:* 3 = restore service quickly;; 2 = safety;; 1 = none;; 0 = none.
- **EX030 — Public harm.** Give one way a council network outage could harm residents. *Rubric:* 3 = service example;; 2 = vague;; 1 = none;; 0 = none.

### Synthesis

Ethical engineering protects residents, staff and trust.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain addressing, routing and transport; (2) plan subnets; (3) identify protocols in use.

### 11.1 Layers

Networks are built in layers: physical links, Ethernet switching, IP routing, transport protocols such as TCP and UDP, and applications. Security controls work at different layers: switch port security at Ethernet, firewalls at IP and transport, TLS at application.

Layered models separate network functions: physical transmission, local delivery, routing between networks, end-to-end transport and applications. Each layer relies on the one below. Security controls also sit at particular layers, such as port security at the link layer, filtering at the network layer, and authentication at the application layer. Knowing which layer a control works at shows which threats it can and cannot address.

### 11.2 Addressing plan

Segmentation needs a clean addressing plan. Each zone gets its own subnet sized for its devices with growth room. Kofi uses a private block from RFC 1918 space.

An addressing plan assigns each zone its own subnet with room to grow, using a consistent pattern so that an address reveals its zone. When subnets map neatly to zones, firewall rules can refer to whole subnets rather than individual hosts, which keeps rules short and makes errors easier to spot. Documenting the plan in one place prevents accidental overlaps.

### Lab — Subnet plan

```python
"""Split a synthetic 10.40.0.0/16 site block into zone subnets (stdlib only)."""
import ipaddress as ip
need = {"staff": 600, "servers": 120, "voice": 300, "cctv": 80, "guest": 400, "mgmt": 30}
pool = list(ip.ip_network("10.40.0.0/16").subnets(new_prefix=22))
plan = {}; nxt = 0
for z, n in sorted(need.items(), key=lambda x: -x[1]):
    bits = (n + 2 - 1).bit_length(); pref = 32 - bits
    net = list(pool[nxt].subnets(new_prefix=pref))[0]; nxt += 1
    plan[z] = net; print(f"{z:8} hosts {n:4d} -> {net} ({net.num_addresses - 2} usable)")
print("overlaps:", any(a.overlaps(b) for i, a in enumerate(plan.values()) for b in list(plan.values())[i+1:]))
```

Run with `python3 lab_subnet.py`. Verified output:

```text
staff    hosts  600 -> 10.40.0.0/22 (1022 usable)
guest    hosts  400 -> 10.40.4.0/23 (510 usable)
voice    hosts  300 -> 10.40.8.0/23 (510 usable)
servers  hosts  120 -> 10.40.12.0/25 (126 usable)
cctv     hosts   80 -> 10.40.16.0/25 (126 usable)
mgmt     hosts   30 -> 10.40.20.0/27 (30 usable)
overlaps: False
```

### 11.3 Reading the plan

The script assigns staff a /22 with 1022 usable addresses, guest and voice /23s, servers and CCTV /25s and management a /27. No subnets overlap. Each zone starts on its own /22 boundary, leaving room to grow and making firewall rules simple to write.

Reading an addressing plan, an engineer checks that subnets do not overlap, that each is large enough for expected devices, and that related zones are grouped so they can be summarised. Gaps left between blocks allow future expansion without renumbering. A plan that fails these checks will cause problems once routing and rules are built on it.

### 11.4 Protocols in use

Kofi lists protocols each zone needs: HTTPS and SMB for staff to servers, SIP over TLS for voice, RTSP for CCTV and SSH for management. This list becomes the basis of the policy.

Before designing rules, engineers list the protocols the organisation actually relies on, such as DNS, DHCP, web traffic, file sharing, printing and voice. Each has known ports and behaviours. Writing this list from evidence, such as synthetic flow summaries in a lab, rather than from assumptions, prevents rules that block a forgotten but essential service.

### Name resolution and time

Two supporting services underpin everything else: DNS, which turns names into addresses, and time synchronisation, which keeps logs consistent. Every zone needs access to the council's DNS resolvers and time servers, so these flows appear in the protocol list even though nobody thinks of them as applications. NIST SP 800-81-2 gives guidance on secure DNS deployment, including restricting which hosts can query internal resolvers. Kofi places the resolvers in the server zone and allows DNS from each zone only to them, not to arbitrary external servers.

### Transport choices

TCP provides reliable, ordered delivery with connection set-up; UDP sends independent datagrams without set-up. Voice traffic often uses UDP for media because late packets are useless, while file access uses TCP. These differences affect firewall design: stateful firewalls track TCP connections clearly, while UDP flows are tracked with timeouts. Kofi notes which protocols each zone uses on which transport, because rules must specify both, and because short UDP timeouts can break long phone calls if set too aggressively. He records the timeout chosen for each UDP service and the reason, so later engineers can tune it safely.

### Worked example

The management /27 has exactly 30 usable addresses; Kofi notes it should grow to /26 if devices increase.

> **Synthetic case.** Addresses are synthetic.

### Errors and limits

Tight subnets leave no growth room; renumbering later is disruptive.

### Exercises

- **EX031 — Usable hosts.** How many usable addresses in a /25? *Rubric:* 3 = 126;; 2 = value;; 1 = none;; 0 = none.
- **EX032 — Boundary choice.** Why start each zone on a /22 boundary? *Rubric:* 3 = growth and simple rules;; 2 = growth;; 1 = none;; 0 = none.
- **EX033 — Layer mapping.** Match TLS and firewall rules to layers. *Rubric:* 3 = application vs network/transport;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

A clean addressing plan and protocol list are the foundation of segmentation.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) understand host networking; (2) configure host firewalls; (3) secure network services on servers.

### 12.1 Host networking

Operating systems hold routing tables, interface settings and local firewall rules. Even within a segmented network, hosts should restrict inbound connections.

Every host has its own network configuration: addresses, routes, DNS servers and active interfaces. A laptop with both wired and wireless connections may bridge networks unexpectedly. Reviewing host configuration alongside network design ensures that hosts behave as the design assumes, and that a device placed in one zone does not quietly reach another through a second interface.

Engineers sample a few hosts per type to confirm this.

### 12.2 Host firewalls

Windows Defender Firewall and Linux nftables let hosts allow only needed services. Defence in depth means a misconfigured network rule is not the only barrier.

Host firewalls filter traffic on the device itself, adding protection even inside a zone. They are valuable because network firewalls usually do not see traffic between hosts in the same subnet. Engineers set a default that denies inbound connections except those the host's role needs, and manage the rules centrally so they stay consistent across many machines.

### 12.3 Listening services

Kofi reviews which services servers listen on, using exported reports from the council team, and compares with the protocol list.

A listening service is a program waiting for incoming connections. Every one is a potential entry point, so engineers inventory listening services on each host type, remove those not needed, and restrict the rest to the zones that must reach them. Comparing the inventory against the role of the host often reveals forgotten test services left running.

Repeating the inventory regularly catches new services.

### 12.4 Management interfaces

Management services such as SSH or remote desktop should listen only on management interfaces or accept connections only from the management zone.

Management interfaces of switches, firewalls and servers give full control of the device, so they deserve the strongest protection. Good practice puts them on a separate management network, reachable only from designated administration hosts, with strong authentication and logging of every session. Exposing them to ordinary staff or guest networks gives any compromised device a route to taking over infrastructure.

### Patching network-facing services

Services that accept network connections are the most exposed part of a host. Kofi asks the council team for the update status of servers in the future server zone and finds two running an outdated file-sharing component. Segmentation reduces who can reach them, but does not remove the need to patch. He records them for the council's patching process and notes in his design that segmentation is a second line, not a substitute for keeping exposed services up to date, as NIST SP 800-40 Rev. 4 stresses.

### Logging on hosts

Hosts record their own connection attempts and authentication events. These logs complement network logs: a firewall shows a connection was allowed, while the host shows whether a sign-in then succeeded. Kofi recommends forwarding key host logs from servers to the same central store as firewall logs, using syslog (RFC 5424) for Linux servers and the Windows event forwarding feature for Windows servers. Consistent time on hosts and network devices is essential so the two views line up during an investigation.

### Worked example

A file server listening on remote desktop to all addresses is changed by the council team to accept it only from the management zone.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Host firewalls disabled for troubleshooting are often never re-enabled; track such changes.

### Exercises

- **EX034 — Defence in depth.** Why keep host firewalls in a segmented network? *Rubric:* 3 = backup if network rule fails;; 2 = layers;; 1 = none;; 0 = none.
- **EX035 — Management restriction.** Where should SSH be reachable from? *Rubric:* 3 = management zone only;; 2 = restricted;; 1 = anywhere;; 0 = none.
- **EX036 — Troubleshooting risk.** What risk does troubleshooting create for host firewalls? *Rubric:* 3 = left disabled;; 2 = changes;; 1 = none;; 0 = none.

### Synthesis

Host controls complement network segmentation.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) store flow and log data; (2) query efficiently; (3) manage retention.

### 13.1 Data sources

The design generates firewall logs, flow records (IPFIX, RFC 7011) and VPN logs. Each needs storage and query.

Useful network data comes from several sources: firewall logs record allowed and denied connections, flow records summarise who talked to whom and how much, DNS logs show which names were looked up, and DHCP logs link addresses to devices over time. Each source answers different questions and has gaps. Engineers list what each source contains, how long it is kept, and whose clocks it uses, because combining sources only works when timestamps can be aligned reliably.

### 13.2 Schema

Kofi designs a simple table: time, source zone, destination zone, port, action, bytes. Zones rather than raw addresses make queries simpler and reduce personal data.

A schema defines the fields each record holds, their types and their meaning, such as timestamp in UTC, source address, destination address, port, action and bytes. Agreeing a common schema before collecting data lets records from different devices be stored together and queried consistently. Without it, one device's source field may mean something different from another's, and analysis quietly gives wrong answers that nobody notices until an investigation depends on them.

### 13.3 Queries

Typical queries: denies by zone pair this week; top talkers; new destination ports. Indexes on time and zone pair keep them fast.

Queries turn stored records into answers: how many denied connections came from the guest zone yesterday, or which hosts contacted a server outside working hours. Good queries state their time window and filters explicitly, and their results are checked against a small sample read by hand. Saving useful queries with a short description lets colleagues reuse them during incidents, when there is no time to write and debug new ones from scratch.

### 13.4 Retention

Logs are kept ninety days, then aggregated summaries are kept longer.

Retention decides how long each type of record is kept. Investigations often begin weeks after the event, so records must last long enough to answer late questions, yet personal data should not be kept longer than needed. Engineers set retention per source from policy, legal requirements and investigation experience, calculate the storage this needs, and automate deletion at the end of the period so that the rule is actually applied rather than forgotten.

### Pseudonymisation

Flow records link devices to activity, and staff laptops link to people. Kofi stores device identifiers in pseudonymised form, using a keyed hash so the same device always maps to the same pseudonym without revealing its real name. The key is held by the council, not by Kofi, so only authorised staff can re-identify a device during an investigation. This supports analysis of patterns, such as repeated denied attempts from one device, while limiting personal data visible to analysts and to him as a student.

### Data quality checks

Before analysing data, Kofi checks quality: are there gaps in time where a device stopped logging, duplicate records, or impossible values such as negative byte counts? A gap might look like a quiet period and mislead an analysis of traffic patterns. He writes a small script that reports gaps longer than ten minutes per source and counts malformed records. Problems are reported to the council team and noted in his analysis, so conclusions are not drawn from incomplete data. Recording these checks also lets a later analyst repeat the same cleaning steps and compare results fairly.

### Worked example

A query grouping denies by zone pair gives the weekly table used in later chapters.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Storing raw payloads creates privacy risk without benefit for policy analysis.

### Exercises

- **EX037 — Schema fields.** List six schema fields. *Rubric:* 3 = six;; 2 = five;; 1 = fewer;; 0 = none.
- **EX038 — Zone aggregation.** Why record zones rather than addresses? *Rubric:* 3 = simpler queries, less personal data;; 2 = simpler;; 1 = none;; 0 = none.
- **EX039 — Retention rule.** What happens after 90 days? *Rubric:* 3 = aggregated summaries kept;; 2 = deleted;; 1 = none;; 0 = none.

### Synthesis

A lean schema supports analysis while limiting data held.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) manage configuration as code; (2) review changes; (3) test configurations.

### 14.1 Configuration as code

Firewall policies can be kept as text in version control, with changes reviewed before deployment. This gives history, review and rollback.

Configuration as code means keeping device and firewall settings as text files in version control, rather than editing devices by hand. Every change is then recorded with who made it, when and why, and earlier versions can be restored. Templates generate consistent configuration for similar devices, which reduces drift between offices. The approach also makes review possible, because a proposed change appears as a readable difference that colleagues can inspect before it reaches production.

### 14.2 Review

Each change is reviewed by a second engineer against the needed-flows list.

Peer review means a second engineer reads every proposed change before it is applied. The reviewer checks that the change does what its description says, does not open unintended access, follows naming conventions, and has a rollback plan. Review catches mistakes the author cannot see in their own work. Keeping review comments with the change record also documents the reasoning, which helps later engineers understand why a rule exists and whether it can be removed.

### 14.3 Testing

Automated tests evaluate synthetic flows against the policy and check expected allow or deny results.

Configuration can be tested before deployment. Syntax checks confirm the device will accept it; policy tests confirm that required flows are allowed and forbidden flows are denied, using a list of expected results; and lab trials with synthetic traffic confirm behaviour on real equipment. Automated tests run on every change, so a mistake that would block a critical service is found in minutes in the lab rather than by users on a Monday morning.

### 14.4 Deployment

Approved changes are deployed in windows, with automatic backups of the previous configuration.

Deployment applies an approved, tested change to production. Safe deployment proceeds in stages, starting with one low-risk device or office, checking that services work, then continuing. Each step has a defined rollback, and the deployment record notes the exact version applied. Automating deployment from version control removes manual retyping, which is a frequent source of errors, and guarantees that what runs on the device is exactly what was reviewed.

### Change review checklist

Reviewers use a short checklist for each policy change: does the change match an entry in the needed-flows list; is the source and destination as narrow as possible; is there an owner and a reason; does it include a test; and is there a rollback. The checklist turns review from a general impression into specific questions that can be answered yes or no. Kofi tests it on ten historical council changes and finds that four would have failed on narrowness, which suggests the checklist would have prevented overly broad rules.

### Environments

Changes are first applied to a lab firewall with the same software version and a copy of the policy. Synthetic test flows confirm behaviour before production. Kofi builds the lab from spare equipment provided by the council. A lab never perfectly matches production, so he documents known differences, such as fewer interfaces, and treats lab success as necessary but not sufficient. Production changes are still scheduled carefully and verified afterwards with the same tests. Each known difference is reviewed whenever the lab or production equipment changes, so the list stays accurate.

### Documentation as part of the change

A change is not finished until its documentation is updated: the needed-flows list, the diagram if zones or links changed, and the decision record if the change reflects a new design choice. Kofi includes documentation updates in the review checklist so they cannot be skipped. Out-of-date documentation is a common cause of later errors, because engineers trust diagrams that no longer match reality and make changes based on them. Reviewers reject a change whose documentation is missing, just as they would reject one whose tests fail.

### Worked example

A test asserts that guest→servers:443 is denied; a change that broke this fails review.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

Tests only cover cases written; maintain them as requirements change.

### Exercises

- **EX040 — Version control benefits.** List three benefits of version-controlled policy. *Rubric:* 3 = history, review, rollback;; 2 = two;; 1 = one;; 0 = none.
- **EX041 — Policy test.** Write one policy test case. *Rubric:* 3 = flow and expected result;; 2 = partial;; 1 = none;; 0 = none.
- **EX042 — Test limits.** What is the limit of automated policy tests? *Rubric:* 3 = only cover written cases;; 2 = incomplete;; 1 = none;; 0 = none.

### Synthesis

Treating configuration as code brings software discipline to networks.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to networks; (2) use least privilege and defence in depth; (3) classify threats.

### 15.1 CIA in networks

Confidentiality: encrypt links and restrict access. Integrity: prevent tampering in transit, using protocols like TLS (RFC 8446) and IPsec (RFC 4301). Availability: redundancy and capacity.

Confidentiality, integrity and availability apply directly to networks. Confidentiality means traffic is not readable by those who should not see it, which is why links between offices are encrypted. Integrity means data and configuration are not altered without authority, so changes are controlled and logged. Availability means services can be reached when needed, which requires capacity and redundancy. A good design states which of the three each control supports.

### 15.2 Least privilege

Each zone gets only the flows it needs. Saltzer and Schroeder's principles apply directly to network policy.

Least privilege means each user, device and zone gets only the access it needs to do its job, and no more. In networks this becomes rules that allow specific flows between specific zones on specific services, rather than broad permissions. It limits the damage when something is compromised, because the attacker inherits only the narrow access of that device. Applying it requires knowing what access is actually needed, which is why flow inventories matter.

### 15.3 Defence in depth

Segmentation, host firewalls, encryption and monitoring combine so one failure is not fatal.

Defence in depth layers independent controls so that the failure of one does not expose everything. Network segmentation, host firewalls, strong authentication, monitoring and backups each address threats in different ways. If a guest device evades the wireless isolation, zone rules still block it from servers, and monitoring may still detect the attempt. The layers should fail independently; two controls relying on the same configuration file are less independent than they appear.

### 15.4 Threat categories

Kofi lists threats: malware spreading laterally, eavesdropping on inter-office links, misconfiguration and outages.

Grouping threats into broad categories helps engineers check designs systematically. Common categories include unauthorised access, interception of traffic, tampering with data or configuration, denial of service, and misuse by authorised people. For each category, the design should name the controls that reduce it and the evidence that they work. Categories are prompts for thinking, not a complete list, so engineers also consider threats specific to the organisation.

### Attack surface

The attack surface of a network is the set of points where an unauthorised party could try to interact with systems. In a flat network, every device exposes its services to every other device, so the surface is large. Segmentation shrinks it by limiting which zones can reach which services. Kofi measures attack surface simply, as the number of permitted zone-service pairs, so that design options can be compared numerically, and he tracks how this number changes as the design develops.

### Trust boundaries

A trust boundary is where data or connections pass between areas with different levels of trust, such as guest Wi-Fi and internal servers, or a council office and the internet. Controls concentrate at these boundaries. Kofi marks every boundary on his diagrams and lists the controls at each one: filtering, encryption, authentication and logging. Boundaries without controls become obvious, which is how he discovers that the CCTV supplier's remote maintenance connection currently enters the network without any filtering. The boundary list later becomes the starting point for the threat analysis and for choosing where firewalls are placed.

### Worked example

For the guest incident, segmentation addresses lateral spread, and monitoring would have detected the attempts sooner.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Encryption alone does not stop lateral movement inside a network.

### Exercises

- **EX043 — Integrity protocol.** Name a protocol that protects integrity in transit. *Rubric:* 3 = TLS or IPsec with RFC;; 2 = name;; 1 = none;; 0 = none.
- **EX044 — Encryption limit.** Why doesn't encryption stop lateral movement? *Rubric:* 3 = controls content, not reachability;; 2 = different;; 1 = none;; 0 = none.
- **EX045 — Threat list.** List three network threats for the council. *Rubric:* 3 = three;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Core principles map directly onto network design choices.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) manage requirements through a lifecycle; (2) trace requirements to tests; (3) manage interfaces.

### 16.1 Lifecycle

Kofi follows a lifecycle: needs, requirements, design, implementation, verification, operation.

The systems engineering lifecycle runs from understanding needs, through requirements, design, implementation and verification, to operation and eventual retirement. Each stage produces documents that the next one relies on. Security must be considered at every stage, not added at the end, because a weakness designed into an architecture is far costlier to fix after deployment. Reviews between stages confirm that each output is complete and consistent before work continues.

Retirement also needs planning.

### 16.2 Requirements

Requirements are testable statements, such as "guest devices cannot initiate connections to any internal zone".

A requirement states what the system must do or how well, in terms that can be checked. Good requirements are specific, measurable, and free of design choices: guest devices must not reach staff servers is a requirement, while use a particular firewall model is a design decision. Each requirement has an identifier, a source such as a council policy, and a planned verification method, so nothing is lost or left untested.

### 16.3 Traceability

Each requirement links to design elements and tests, so coverage gaps are visible.

Traceability links each requirement to the design elements that satisfy it and the tests that verify it. A traceability matrix makes gaps visible: a requirement with no test is unverified, and a design element linked to no requirement may be unnecessary. When requirements change, the links show what design and tests must be revisited. Reviewers and auditors use the matrix to confirm that every promise in the requirements was actually kept.

### 16.4 Interfaces

Interfaces with other systems, such as the phone provider and CCTV supplier, are documented.

Interfaces are the points where systems meet: between zones, between the council network and suppliers, or between the firewall and the logging platform. Many failures occur at interfaces, because each side assumes something about the other. Interface specifications record what crosses the boundary, in which direction, in what format, and who is responsible for each side. Agreeing them in writing prevents gaps that neither team realises they own.

### Stakeholders

Systems engineering starts with stakeholders: the people affected by the system and its changes. For Ashcombe they include IT staff, office managers, the telephony provider, the CCTV supplier, the information governance officer and residents who depend on services. Kofi interviews representatives of each group to collect needs, recording who said what. Some needs conflict, such as the CCTV supplier wanting broad remote access and governance wanting tight control; recording them explicitly allows the conflict to be resolved openly rather than discovered late.

### Verification and validation

Verification asks whether the system meets its requirements; validation asks whether the requirements meet the real need. A network can pass every test and still fail users if a requirement was wrong, for example if a needed flow was missed. Kofi plans both: tests against requirements in the lab and in production, and a validation period in which office staff report anything that stopped working. Their reports feed back into the requirements, closing the loop that systems engineering depends on.

### Configuration items

Systems engineering treats each managed element as a configuration item with an identity, version and owner: firewall policies, switch configurations, VPN settings and diagrams. NIST SP 800-128 describes security-focused configuration management in these terms. Kofi lists the configuration items for the new design and where each is stored, so that changes can be controlled and audits can confirm what is deployed matches what was approved. Each item is stored in version control, so every approved change has a recorded author, date and reason.

### Worked example

Kofi drafts eight requirements, each with an owner and verification method.

> **Synthetic case.** Requirements are synthetic.

### Errors and limits

Vague requirements like "secure network" cannot be verified.

### Exercises

- **EX046 — Testable rewrite.** Rewrite "guest is safe" as testable. *Rubric:* 3 = specific measurable statement;; 2 = partial;; 1 = vague;; 0 = none.
- **EX047 — Traceability value.** What does traceability reveal? *Rubric:* 3 = untested requirements;; 2 = gaps;; 1 = none;; 0 = none.
- **EX048 — Interface example.** Name one external interface. *Rubric:* 3 = phone provider or CCTV supplier;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Systems engineering keeps design tied to verifiable needs.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe feedback loops in network operations; (2) tune thresholds; (3) avoid oscillation.

### 17.1 Feedback in operations

Monitoring, alerts and changes form a feedback loop: observe, decide, act, observe again.

Operations form a feedback loop: monitoring measures the network, people or automation compare measurements with targets, and actions adjust the system. A good loop corrects problems quickly and steadily. A poor one reacts too slowly, so problems grow, or too aggressively, so corrections cause new problems. Seeing operations as feedback helps engineers design alert rules and automated responses that keep the network stable rather than chasing noise.

### 17.2 Thresholds

Alert thresholds set when action happens. Too low creates noise; too high misses problems.

A threshold turns a continuous measurement into a decision, such as alerting when link utilisation exceeds 85 percent for five minutes. Set too low, thresholds produce constant alerts that staff learn to ignore; set too high, they miss real problems. Engineers choose thresholds from measured normal behaviour, add a duration condition to avoid reacting to brief spikes, and review them periodically as traffic patterns change.

Each threshold has a documented owner.

### 17.3 Oscillation

Automatic responses, such as blocking sources, can oscillate if they react too quickly. Damping, such as minimum durations, helps.

Oscillation happens when a control loop overcorrects repeatedly, such as traffic shifting back and forth between two links as each in turn becomes busy. It wastes capacity and makes behaviour unpredictable. Remedies include hysteresis, using different thresholds for switching on and off, and adding delay before acting again. Engineers watch for oscillation whenever an automated response feeds back into the measurement that triggers it.

### 17.4 Human loop

Most council responses involve humans; clear runbooks reduce delay in the loop.

Many network responses keep a person in the loop: an alert is raised, an operator investigates, and decides on action. People add judgement but also delay and fatigue. Engineers design alerts that give the operator enough context to decide quickly, document runbooks for common cases, and limit alert volume so attention stays on what matters. Measuring time from alert to action shows whether the human part of the loop is working.

### Measuring the loop

A feedback loop can be measured. Kofi defines the time from an event, such as a burst of denied connections, to an alert, from alert to acknowledgement by an analyst, and from acknowledgement to action. Each interval points to a different improvement: faster detection, better on-call arrangements or clearer runbooks. Measuring these intervals during exercises shows where the council's response is slowest, which is usually acknowledgement outside office hours rather than detection itself. Repeating the measurement after each improvement shows whether the change actually shortened the slowest interval.

### Stability of automated controls

Some network controls adjust automatically, such as rate limits that tighten when traffic surges. Poorly designed automation can amplify problems: a rate limit that blocks a busy service causes retries, which increase traffic, which tightens the limit further. Kofi avoids automatic blocking in the council design except for clearly defined cases, and where automation is used, he requires limits on how often it can act and an alert to humans whenever it does, so people stay in control of significant changes.

### Learning from incidents

Each incident is a chance to adjust the loop. After an event, the team reviews whether alerts fired, whether thresholds were right and whether runbooks helped. Adjustments are recorded as changes like any other. Over time this tunes the monitoring to the council's actual network rather than generic defaults, which is the same principle as control engineering: a system is tuned by observing its response and correcting. Reviews are blameless, focusing on how the system and process can improve rather than on who made a mistake.

### Worked example

A rate alert at 100 denies per minute fires constantly from guest; raising it to 300 and grouping by source reduces noise.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Automated blocking without damping can cut off legitimate services.

### Exercises

- **EX049 — Threshold trade-off.** Describe the threshold trade-off. *Rubric:* 3 = noise vs misses;; 2 = one;; 1 = none;; 0 = none.
- **EX050 — Damping.** Give an example of damping. *Rubric:* 3 = minimum block duration or hold-off;; 2 = example;; 1 = none;; 0 = none.
- **EX051 — Runbook role.** How do runbooks affect the feedback loop? *Rubric:* 3 = reduce human delay;; 2 = faster;; 1 = none;; 0 = none.

### Synthesis

Feedback thinking helps design stable monitoring and response.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) describe zone-based architecture; (2) compare perimeter and zero trust models; (3) place controls in an architecture.

### 18.1 Zones and conduits

A zone groups systems with similar trust and function; a conduit is the controlled path between zones. This vocabulary, common in industrial security, suits the council well. Kofi proposes six zones: staff, servers, voice, CCTV, guest and management. Each conduit has a defined set of permitted services and a control point, usually a firewall. The architecture is easy to explain to managers because it mirrors how they already think about departments and access, and easy to verify because each conduit can be tested separately.

### 18.2 Perimeter and zero trust

Traditional designs trust everything inside the perimeter. NIST SP 800-207 describes zero trust, where every access request is evaluated using identity, device state and context, regardless of network location. The council cannot move to full zero trust in one project, but Kofi's design takes steps in that direction: internal zones do not trust each other by default, management access requires authentication through a jump host, and remote access is tied to user identity rather than to a shared tunnel. He describes the design as segmentation with zero trust principles, not as zero trust itself.

### 18.3 Placing controls

Controls are placed where they are most effective. Inter-zone filtering sits on a pair of firewalls at the main office and smaller firewalls at branch offices. Encryption protects links between offices. Host firewalls add depth. Logging collects decisions at each control point. Kofi draws a control placement diagram showing each control and the threat it addresses, so that gaps, such as an uncontrolled supplier connection, are visible at a glance.

Each placement is recorded on the diagram with its purpose.

### 18.4 Simplicity

Saltzer and Schroeder's economy of mechanism argues for designs simple enough to check. Kofi resists adding more zones than the council can manage. Six zones with clear purposes are easier to operate correctly than fifteen finely divided ones, and errors in complex policies are a known risk documented by Wool (2004).

Simple designs have fewer parts to misconfigure and are easier to review and operate. Every extra zone, exception or special path adds a place for errors. Engineers prefer the simplest design that meets the requirements, and justify any added complexity by a specific need.

### Worked example

Kofi's architecture diagram shows six zones, eleven conduits and five control types, with a legend mapping each control to the threats from chapter 15.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Calling a design zero trust when it only adds segmentation overstates its protection and confuses stakeholders.

### Exercises

- **EX052 — Zone vocabulary.** Define zone and conduit in one sentence each. *Rubric:* 3 = both correct with example;; 2 = both;; 1 = one;; 0 = none.
- **EX053 — Zero trust claim.** Why does Kofi avoid calling his design zero trust? *Rubric:* 3 = only partial adoption, honesty;; 2 = partial;; 1 = none;; 0 = none.
- **EX054 — Zone count.** Argue for six zones rather than fifteen. *Rubric:* 3 = manageability and error risk with citation;; 2 = simpler;; 1 = none;; 0 = none.

### Synthesis

A zone and conduit architecture with zero trust principles gives the council a clear, verifiable structure.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain certificates and keys for network devices; (2) choose VPN authentication; (3) apply TLS guidance.

### 19.1 Keys and certificates

Network devices prove their identity with cryptographic keys. A certificate binds a public key to a name and is signed by a certificate authority. For the council's VPN between offices, each firewall gets a certificate from the council's internal authority. This is stronger than shared passwords, which are often reused, rarely changed and hard to revoke for a single device. If one firewall is stolen, its certificate is revoked without affecting the others.

Each certificate's owner and expiry date should be recorded in an inventory.

### 19.2 IPsec and IKEv2

Site-to-site tunnels use IPsec (RFC 4301) with keys negotiated by IKEv2 (RFC 7296). NIST SP 800-77 Rev. 1 recommends IKEv2, certificate authentication, and modern algorithms such as AES-GCM with strong Diffie-Hellman groups. Kofi follows these recommendations and records the chosen parameters in the design, so that future reviewers can compare them with updated guidance rather than guessing what was configured.

IKEv2 negotiates keys and algorithms between the two ends and re-keys periodically, so a key exposed later reveals limited traffic. Engineers choose current algorithm suites and authenticate peers with certificates rather than shared secrets where possible.

### 19.3 TLS for applications

Within zones, applications such as the case management system use TLS. NIST SP 800-52 Rev. 2 recommends TLS 1.2 or 1.3 with specific cipher suites, and RFC 8446 defines TLS 1.3. Kofi checks the council's main web applications' TLS settings using reports from the council's web team and lists two older systems still allowing outdated protocol versions for remediation.

TLS protects individual application connections such as web and mail. Engineers require current protocol versions, disable outdated ones, and ensure clients validate server certificates, since encryption without validation does not confirm who is on the other end.

### 19.4 Key lifecycle

Keys and certificates expire and must be renewed. Expired certificates cause outages that look like network failures. Kofi adds certificate expiry dates to the monitoring and sets alerts sixty days before expiry, and documents how a certificate is revoked if a device is lost.

Keys pass through generation, distribution, use, rotation and destruction. Each stage needs a defined owner and procedure. Rotation limits the exposure if a key leaks, and an inventory with expiry dates prevents outages caused by certificates silently expiring. Revocation must also be planned, so a compromised key can be withdrawn quickly.

### Worked example

The VPN profile specifies IKEv2, certificate authentication, AES-256-GCM and a 3072-bit or elliptic-curve Diffie-Hellman group, with lifetimes recorded in the design.

> **Synthetic case.** Parameters are illustrative and synthetic.

### Errors and limits

Strong algorithms do not help if private keys are stored unprotected on shared drives.

### Exercises

- **EX055 — Certificates vs passwords.** Give two advantages of certificate authentication for site VPNs. *Rubric:* 3 = per-device revocation and no shared secrets;; 2 = one;; 1 = none;; 0 = none.
- **EX056 — Guidance mapping.** Which documents guide IPsec and TLS choices? *Rubric:* 3 = SP 800-77r1/RFC 7296 and SP 800-52r2/RFC 8446;; 2 = some;; 1 = none;; 0 = none.
- **EX057 — Expiry alerts.** Why alert sixty days before certificate expiry? *Rubric:* 3 = time to renew without outage;; 2 = warning;; 1 = none;; 0 = none.

### Synthesis

Certificates, IKEv2 and current TLS guidance give the design strong, manageable cryptography.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Network and communications security: engineering context

### Learning outcomes

You will (1) describe the council's current network; (2) identify constraints; (3) frame the engineering problem.

### 20.1 Current state

Ashcombe's eight offices connect over leased lines to the main office, which hosts most servers and the internet connection. Inside each office, one flat subnet holds all devices. Guest Wi-Fi shares this subnet, separated only by a captive portal. The CCTV supplier reaches cameras through a remote access appliance that bypasses the edge firewall. Kofi documents this from configuration exports and site visits, never by scanning.

Kofi records this state with dated evidence so later improvements can be measured.

This baseline is shared with the council.

### 20.2 Constraints

The council has a limited budget, two network engineers and services that cannot be interrupted during working hours. Some devices, like older phones and cameras, cannot be reconfigured easily. Any design must be implemented in phases over a year and operated by the existing team afterwards. These constraints rule out designs that need specialist skills or continuous tuning.

Constraints include budget, staff skills, existing equipment, and the need to keep services running during change. Writing them down early prevents designs that cannot be delivered.

### 20.3 The engineering problem

Kofi states the problem: design and implement segmentation and secure inter-office connectivity so that guest and compromised devices cannot reach internal services, supplier access is controlled, and services remain available, within budget and team capacity. Each part of this statement becomes a group of requirements in the next chapter.

Stated clearly, the problem is to separate devices into zones with only needed flows allowed, and secure links between offices, within the constraints and without disrupting services. A clear statement keeps later work focused on what matters.

### 20.4 Success measures

He proposes measures: reachable zone pairs, unexpected denied flows, VPN availability, added latency and change failure rate. These will be measured before and after implementation.

Success measures turn goals into checks. Examples include the number of reachable zone pairs before and after, the share of required flows working on day one, time to detect a denied connection from the guest zone, and the number of incidents caused by changes. Each measure has a baseline, a target, and a method of collection, agreed with the council before work starts so that results cannot later be reinterpreted to look better.

### Learning from the incident

The guest laptop incident is the clearest evidence of the problem. Council logs show the infected laptop attempted connections to file servers on the file-sharing port for several hours before a staff member noticed the slow network. Nothing in the flat design stopped the attempts, and nothing alerted anyone. Kofi treats the incident as a case study rather than a crisis: it shows that a single untrusted device could reach internal services, and that monitoring would not have caught it. Both gaps become requirements, and the incident timeline becomes a test scenario for the finished design.

### Worked example

The current-state document includes a site table, a logical diagram of the flat network and a list of eleven known issues.

> **Synthetic case.** The council and network are synthetic.

### Errors and limits

Documenting current state from old diagrams alone misses undocumented changes; use configuration exports.

### Exercises

- **EX058 — Supplier bypass.** Why is the CCTV supplier's appliance a concern? *Rubric:* 3 = bypasses edge firewall, uncontrolled entry;; 2 = risk;; 1 = none;; 0 = none.
- **EX059 — Constraint impact.** How do team constraints shape the design? *Rubric:* 3 = simple, operable by two engineers;; 2 = simpler;; 1 = none;; 0 = none.
- **EX060 — Measure list.** List five success measures. *Rubric:* 3 = five;; 2 = four;; 1 = fewer;; 0 = none.

### Synthesis

A precise problem statement with constraints and measures guides the whole design.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Network and communications security: requirements

### Learning outcomes

You will (1) write security and operational requirements; (2) prioritise them; (3) assign verification methods.

### 21.1 Security requirements

Kofi writes requirements such as: R1 guest devices cannot initiate connections to internal zones; R2 traffic between zones is denied unless explicitly permitted; R3 device management is only possible from the management zone via an authenticated jump host; R4 inter-office VPNs use IKEv2 with certificate authentication; R7 CCTV cameras can reach only the video recorder.

Each security requirement is linked to the threat it addresses and the test that will verify it.

Vague wording is replaced with testable statements before review.

### 21.2 Operational requirements

Others address operations: R5 firewall and VPN logs are retained for ninety days; R6 VPN failover completes within sixty seconds; R8 device configurations are backed up daily. Operational requirements are often forgotten in security designs but determine whether the design survives contact with daily work.

Operational requirements cover what staff need to run the network: monitoring, change procedures, backup of configurations, and acceptable maintenance windows. They matter because a secure design that operators cannot manage will drift back to an insecure state.

### 21.3 Prioritisation

Requirements are ranked as must, should or could, with stakeholders. Must requirements are those tied to the guest incident and supplier access; could requirements include finer segmentation of staff by department, deferred to a later phase.

Not all requirements can be met at once, so engineers rank them. Common methods label each as must, should or could, based on risk reduction, legal need and cost. Ranking is agreed with the council, so if time or budget runs short, the least important work is dropped first, rather than whatever happens to be last.

### 21.4 Verification methods

Each requirement has a verification method: test, inspection, analysis or demonstration. R1 is verified by test, R4 by inspection of configuration, R6 by a failover test.

Each requirement is verified by one of four methods: inspection of configuration or documents, analysis such as a reachability model, demonstration in normal use, or a test with defined inputs and expected results. Choosing the method when writing the requirement makes sure it is checkable, and recording the result as evidence closes the loop between promise and proof.

### Requirement quality checks

Kofi checks each requirement against simple quality rules: it states one thing, is testable, avoids describing a solution where a need will do, and has a named owner. R2, for example, originally said that a particular firewall model would block traffic between zones; he rewrote it to describe the behaviour, so that the requirement survives a change of equipment. A peer reviews the set using the same rules, and two requirements are split because each combined two separate needs that would be verified differently.

### Worked example

The requirements table has eight rows with ID, text, priority, owner and verification method.

> **Synthetic case.** Requirements are synthetic.

### Errors and limits

Requirements without verification methods often turn out to be untestable late in the project.

### Exercises

- **EX061 — Requirement style.** Rewrite "VPNs should be secure" as a verifiable requirement. *Rubric:* 3 = specific protocol and auth;; 2 = partial;; 1 = vague;; 0 = none.
- **EX062 — Operational importance.** Why include operational requirements like log retention? *Rubric:* 3 = design must survive daily operation;; 2 = important;; 1 = none;; 0 = none.
- **EX063 — Verification method.** Choose a verification method for R6 and explain. *Rubric:* 3 = test, timed failover;; 2 = test;; 1 = none;; 0 = none.

### Synthesis

Clear, prioritised requirements with verification methods anchor design and testing.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Network and communications security: system and data models

### Learning outcomes

You will (1) model zones and permitted flows; (2) compare reachability; (3) define data flows for logging.

### 22.1 Flow model

Kofi models the design as a directed graph of zones with permitted services on each edge. The model is derived from the needed-flows list collected from stakeholders: staff need file and web services, phones need the call server, cameras need the recorder and management needs administrative access to devices.

A flow model lists every needed communication as source zone, destination zone, service and purpose. It is built from interviews and synthetic flow summaries, and becomes the basis for rules.

Each flow names its owner.

### Lab — Reachability comparison

```python
"""Zone-to-zone reachability: flat network vs proposed segmented policy (synthetic, stdlib only)."""
zones = ["staff", "servers", "voice", "cctv", "guest", "mgmt"]
allowed = {("staff", "servers"), ("voice", "servers"), ("cctv", "servers"), ("mgmt", "servers"), ("mgmt", "staff"),
           ("mgmt", "voice"), ("mgmt", "cctv")}
pairs = [(a, b) for a in zones for b in zones if a != b]
print(f"directed zone pairs {len(pairs)}; flat reachable {len(pairs)}; segmented reachable {len(allowed)}")
print(f"reduction {1 - len(allowed)/len(pairs):.1%}; guest reaches internal zones: {any(a=='guest' for a,_ in allowed)}")
```

Run with `python3 lab_reach.py`. Verified output:

```text
directed zone pairs 30; flat reachable 30; segmented reachable 7
reduction 76.7%; guest reaches internal zones: False
```

### 22.2 Reading the model

The flat network allows all thirty directed zone pairs. The segmented design allows seven, a 76.7 percent reduction. Guest reaches no internal zone, satisfying R1. Management reaches four zones for administration, which is necessary but makes management the most sensitive zone, reinforcing R3's jump host requirement.

Reading the model, Kofi looks for zones that talk to many others, which are critical, and flows without a stated purpose, which may be unnecessary. Both shape the rule design and review.

Unclear flows are queried.

### 22.3 Data model for logs

Each control point emits records with time, zones, service and action. Kofi defines this common format so that logs from different firewalls can be analysed together, matching the schema from chapter 13.

The log data model defines which fields every firewall and VPN record must carry, such as time, zone, address, service, action and rule identifier. Including the rule identifier is especially useful, because it lets analysts see exactly which rule allowed or denied each connection, linking monitoring back to the design.

### Host-level exceptions

Some flows are narrower than zones. The staff zone may reach the recorder only for viewing footage, not every CCTV device. Kofi records such host-level rules in a separate table alongside the zone model, with each exception tied to a needed flow. This keeps the zone model readable while making exceptions explicit. When counting reachability, he reports both the zone-level figure and the number of host-level exceptions, so the simplicity of the zone picture does not hide additional paths that exist in practice.

### Model as a test oracle

The model is more than a diagram. Kofi uses it as the expected answer for tests: for any proposed flow, the model says whether it should be permitted. Later, the actual firewall configuration is tested against the model with synthetic flows, and any disagreement is either a configuration error or a model that needs updating. Keeping one authoritative model, rather than separate understandings in documents and devices, is what makes the later verification chapters possible. The model is versioned alongside the configurations, so each test result can be tied to the model version it used.

### Worked example

Kofi computes transitive closure on the seven allowed edges and confirms no indirect path reaches servers from guest.

> **Synthetic case.** Model data are synthetic.

### Errors and limits

A zone-level model can hide host-level exceptions; record any host-specific rules separately.

### Exercises

- **EX064 — Reduction value.** State the reduction in reachable zone pairs. *Rubric:* 3 = 30 to 7, 76.7%;; 2 = percent;; 1 = none;; 0 = none.
- **EX065 — Management sensitivity.** Why is the management zone most sensitive? *Rubric:* 3 = reaches many zones;; 2 = access;; 1 = none;; 0 = none.
- **EX066 — Closure check.** Why compute transitive closure? *Rubric:* 3 = detect indirect paths;; 2 = completeness;; 1 = none;; 0 = none.

### Synthesis

Modelling reachability shows the design's effect quantitatively and confirms key requirements.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Network and communications security: threat and failure analysis

### Learning outcomes

You will (1) analyse threats against the design; (2) analyse failure modes; (3) prioritise mitigations.

### 23.1 Threat analysis

Kofi walks through each conduit and asks what could go wrong: a compromised staff laptop reaching servers over permitted services, a stolen branch firewall, a misconfigured rule opening guest access, interception of inter-office traffic, and abuse of supplier access. For each, he records likelihood, impact and existing controls. This structured approach avoids focusing only on dramatic threats.

Each threat is recorded with its likely source and the zones it affects.

Insiders and suppliers are included alongside outside attackers.

Evidence for each is cited.

### 23.2 Failure analysis

Security devices can fail. A firewall failure at the main office would isolate all branches; a certificate expiry would drop tunnels; a logging server failure would blind monitoring. Kofi uses a simple failure modes and effects table, listing each failure, its effect, detection method and mitigation.

Failure analysis asks what happens when parts break: a firewall, a link, a power supply. For each, engineers record the effect, how it would be detected and the planned response.

Shared causes are noted.

### 23.3 Prioritisation

Highest priority mitigations: redundant firewalls at the main office, certificate expiry monitoring, policy change review and supplier access through the jump host with time-limited accounts. Lower priority: redundant logging, since temporary loss of logs is less harmful than loss of connectivity.

Threats and failures are ranked by likelihood and impact, using evidence where possible. High-ranked items get controls first; low-ranked ones may be accepted, with reasons recorded and reviewed later.

The ranking is revisited after each incident.

Changes in rank are dated.

### 23.4 Residual risk

Some risk remains: compromised staff laptops can still reach servers over permitted services. This is addressed by host controls and monitoring, not segmentation, and is stated as residual risk.

Residual risk is what remains after controls are applied. No design removes all risk, so engineers state what remains, why it is acceptable, and who accepted it. The council's risk owner signs the acceptance, and the list is reviewed when circumstances change, such as a new service or a new type of incident.

### Supplier access threats

Supplier connections deserve particular attention because they are trusted by design yet managed by another organisation. If the CCTV supplier's own systems were compromised, their access could become an entry point to the council. Kofi's analysis lists the controls that limit this: named accounts rather than a shared login, multi-factor authentication, access only through the jump host, access limited to the CCTV zone, and accounts enabled only for agreed maintenance windows. Each control reduces either the likelihood of misuse or the reach of any misuse.

### Worked example

The failure table lists nine failure modes; four are ranked high and get mitigations in the design.

> **Synthetic case.** Analysis is synthetic.

### Errors and limits

Threat analysis that ignores operational failures produces designs that are secure but fragile.

### Exercises

- **EX067 — Threat example.** Describe one threat that segmentation does not address. *Rubric:* 3 = compromised staff laptop over permitted services;; 2 = example;; 1 = none;; 0 = none.
- **EX068 — Failure effect.** What is the effect of main-office firewall failure without redundancy? *Rubric:* 3 = branches isolated;; 2 = outage;; 1 = none;; 0 = none.
- **EX069 — Residual risk.** How is residual risk from permitted flows handled? *Rubric:* 3 = host controls and monitoring, stated explicitly;; 2 = monitoring;; 1 = none;; 0 = none.

### Synthesis

Combining threat and failure analysis yields a design that is both secure and resilient.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Network and communications security: methods I

### Learning outcomes

You will (1) apply policy design methods; (2) derive rules from needed flows; (3) review rules systematically.

### 24.1 From flows to rules

Kofi derives rules directly from the needed-flows list: each flow becomes one rule specifying source zone, destination zone or host, service and a reason. The final rule is default deny. This method follows NIST SP 800-41 Rev. 1, which recommends deny-by-default policies built from documented requirements.

Each needed flow in the model becomes one or more allow rules, with a final deny for everything else. Grouping addresses into named objects keeps rules readable and consistent.

Every rule carries a reference back to the flow it implements, so reviewers can check that nothing was added without a documented need and that removed flows lose their rules.

### 24.2 Rule ordering

In first-match firewalls, order matters. Specific rules come before general ones, and no allow rule may be shadowed by an earlier deny. Kofi checks ordering with a script that compares each rule with earlier ones.

Firewalls usually apply the first matching rule, so order matters. Specific rules go before broad ones, and a broad allow placed early can silently override later denies. Engineers review order deliberately and test that each rule is actually reached.

Analysis tools or simple scripts can detect shadowed rules, which are never reached because an earlier rule matches every packet they would match, and such rules should be removed or reordered.

### 24.3 Naming and documentation

Each rule has an identifier, owner and reason, matching the needed-flows list. Rules without owners are a common source of later confusion.

Every rule and object gets a meaningful name following a convention, such as zone, destination and service. Each rule records its purpose, the requirement or flow it serves, its owner, and a review date. Documentation lives with the configuration in version control, so it changes together with the rules. A rule whose purpose nobody can explain is a candidate for removal at the next review.

### 24.4 Review method

Before deployment, a second engineer reviews each rule against the flows list using the checklist from chapter 14.

Rule review follows a fixed method so nothing is skipped. The reviewer compares rules against the flow model, looking for missing needed flows, rules allowing more than needed, duplicates, rules shadowed by earlier ones, and rules with no recent hits. Each finding is recorded with a proposed action. Repeating the review on a schedule, and after major changes, keeps the rule set from slowly accumulating exceptions.

### Grouping services

Rules often refer to groups of services or hosts, such as all file-sharing ports or all branch recorders. Groups make policies shorter and easier to review, but a group that is too broad can quietly permit more than intended. Kofi defines groups from the needed-flows list, names them clearly and reviews their membership as carefully as the rules. A change to a group's membership affects every rule using it, so group changes go through the same review as rule changes.

### Testing rules before deployment

For each rule, Kofi writes at least one test flow that should be allowed and one similar flow that should be denied, such as the same source and destination on a different port. Passing both shows the rule is neither too narrow nor too broad. These tests run against the policy in the lab and are kept for regression testing, so later changes that accidentally widen a rule are caught. The approach mirrors unit testing in software, applied to network policy.

### Worked example

Twelve needed flows produce twelve allow rules plus default deny; review finds one rule broader than its flow and narrows it.

> **Synthetic case.** Rules are synthetic.

### Errors and limits

Copying old rules into a new design imports old mistakes; derive rules from needs instead.

### Exercises

- **EX070 — Derivation.** Why derive rules from needed flows rather than old rules? *Rubric:* 3 = avoid importing mistakes;; 2 = cleaner;; 1 = none;; 0 = none.
- **EX071 — Ordering rule.** State one ordering principle for first-match policies. *Rubric:* 3 = specific before general;; 2 = order;; 1 = none;; 0 = none.
- **EX072 — Rule metadata.** List three metadata fields for each rule. *Rubric:* 3 = ID, owner, reason;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Rules derived from documented needs, ordered carefully and reviewed, form a clean policy.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) develop a detailed segmentation design; (2) present to peers; (3) incorporate critique.

### 25.1 Studio work

In the first design studio, Kofi turns the architecture into a detailed design: VLANs and subnets per office, firewall interfaces, routing and the policy. He presents it to peers and staff for critique.

A design studio is a structured session where the engineer presents work in progress and invited peers question it. Kofi prepares diagrams, the flow model and open questions, and records every comment. Studios catch design problems while they are cheap to fix.

Inviting reviewers from operations as well as design brings practical concerns, such as maintenance effort, into view early.

### 25.2 Critique

Peers ask how phones that need to reach the provider's cloud are handled, and whether the CCTV recorder should sit in the server zone. Kofi adds an outbound rule for the phone provider and moves the recorder into the CCTV zone, adjusting rules accordingly.

Good critique addresses the design, not the person, and explains its reasoning. Kofi treats each comment as a hypothesis to check, responding with evidence or a change rather than defending his first choice.

Giving critique well also matters: specific, kind and evidence-based comments help peers more than vague praise or blunt rejection.

### 25.3 Trade-offs

Placing the recorder in the CCTV zone means cameras never cross a zone boundary, but staff viewing footage must reach it from the staff zone. He adds one narrow rule for viewing.

Studios often surface trade-offs, such as more zones improving isolation but increasing operational load. Kofi records each with the options, criteria and chosen direction, so the decision can be reviewed later.

Making trade-offs explicit prevents later surprise, because stakeholders have seen and accepted the costs of the chosen direction. It also helps when conditions change, because the record shows which assumption drove the decision and therefore which decisions deserve to be reopened.

### 25.4 Documentation

The revised design is documented with diagrams, subnet tables and the rule list.

After the studio, Kofi writes a short record listing attendees, the material presented, each comment, the response, and actions with owners and dates. He shares it with participants to confirm accuracy. The record shows how the design evolved and why, which helps reviewers of the final thesis and anyone who later maintains the network and wonders why a particular choice was made.

Short, prompt records are more useful than long ones written weeks later.

### Addressing and VLAN details

The studio also settles details that are easy to overlook. Each office receives VLAN numbers that are the same across sites for the same zone, so engineers recognise them anywhere. Subnets follow the plan from chapter 11, with each office taking a consistent slice of the address space. Default gateways sit on the branch firewall, so traffic between zones passes through it. These conventions make troubleshooting faster and reduce mistakes, because an engineer can predict a device's VLAN and gateway from its zone and office.

### Peer review record

Kofi records every critique point, his response and whether the design changed. Of fourteen points raised, nine lead to changes, three are answered with existing design features and two are deferred to later phases with reasons. The record is attached to the design document. It shows examiners that critique was taken seriously and gives the council a view of options considered and set aside, which is often as useful as the final design itself. Deferred points carry a target phase and an owner, so they are revisited rather than quietly forgotten.

### Worked example

After critique, the design has seven allow rules between zones and two outbound internet rules.

> **Synthetic case.** The design is synthetic.

### Errors and limits

Ignoring critique to protect a design leads to problems in implementation.

### Exercises

- **EX073 — Recorder placement.** Why move the recorder into the CCTV zone? *Rubric:* 3 = cameras stay within zone;; 2 = simpler;; 1 = none;; 0 = none.
- **EX074 — Viewing rule.** What rule supports staff viewing footage? *Rubric:* 3 = staff to recorder viewing service only;; 2 = staff access;; 1 = none;; 0 = none.
- **EX075 — Studio value.** What does studio critique provide? *Rubric:* 3 = early detection of design issues;; 2 = feedback;; 1 = none;; 0 = none.

### Synthesis

Studio critique improves the design before any equipment is touched.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Network and communications security: architecture alternatives

### Learning outcomes

You will (1) compare alternative architectures; (2) evaluate against criteria; (3) justify a choice.

### 26.1 Alternatives

Kofi compares three options: A) central firewalls at the main office with branches routing all inter-zone traffic there; B) firewalls at every office; C) a cloud-delivered security service with branch connectors.

For each major decision, engineers consider several realistic alternatives, such as different zone counts or VPN approaches, so the final choice is a comparison rather than a default.

Including a do-minimum option, such as only isolating guest Wi-Fi, gives a useful baseline: every more ambitious alternative must show enough extra benefit to justify its extra cost and disruption. Considering at least three options also guards against the common habit of comparing a preferred design with an obviously poor one.

### 26.2 Criteria

Criteria: security, availability, cost, latency and operational effort.

Criteria are the qualities used to compare alternatives: security benefit, cost, operational effort, disruption during rollout, and fit with existing skills and equipment. Agreeing criteria and their weights with the council before scoring prevents the analysis being shaped to favour a preferred option. Each criterion needs a clear scale, such as low, medium or high, with a short description of what each level means, so scores are consistent.

Weights should reflect the council's priorities rather than the engineer's.

### 26.3 Evaluation

Option A is cheapest but makes the main office a single dependency and adds latency for branch-local traffic. Option C reduces hardware but depends on internet links and a new skill set. Option B costs more but keeps local traffic local and survives WAN outages. Kofi chooses B with small firewalls at branches.

Scores are recorded with brief evidence for each.

Each alternative is scored against every criterion, with the evidence noted, such as lab measurements, vendor documentation or operator interviews. Weighted totals give a ranking, but Kofi also checks how sensitive the ranking is to the weights: if a small change in one weight reverses the order, the decision is close and deserves discussion rather than being presented as clear-cut.

### 26.4 Justification

The choice is recorded in a decision record with the evaluation table, so future engineers understand why.

The justification explains why the chosen alternative is best against the agreed criteria, acknowledges its weaknesses, and notes what evidence would change the decision. Writing it plainly lets council managers understand and approve the choice. It also helps future engineers: if conditions change, such as a large budget increase, they can see whether the original reasoning still holds and revisit the decision with confidence.

### Sensitivity of the choice

Kofi tests whether the choice of option B depends on the weights. If cost is weighted twice as heavily, option A edges ahead; if availability is weighted more, B's lead grows. He presents this sensitivity to the council's managers, explaining that the choice depends on how much they value branch independence during WAN outages. They confirm that keeping branch services running matters more than the extra cost, which makes the decision theirs, informed by the analysis, rather than his. The sensitivity table is kept in the decision record so the choice can be revisited if priorities change.

### Future migration paths

The chosen architecture should not block future change. Kofi notes that branch firewalls can later forward traffic to a cloud-delivered service if the council adopts one, and that the zone model and policy would carry across. Recording this migration path reassures managers that option B is not a dead end and shows how today's design relates to longer-term zero trust ambitions described in NIST SP 800-207. He also notes which parts would need replacing, such as on-site inspection features, so future costs are visible early.

### Worked example

The table scores B highest on availability and latency, second on cost.

> **Synthetic case.** Scores are synthetic.

### Errors and limits

Scoring without weights hides priorities; agree weights with stakeholders.

### Exercises

- **EX076 — Option A weakness.** What is the main weakness of central firewalls only? *Rubric:* 3 = single dependency and latency;; 2 = dependency;; 1 = none;; 0 = none.
- **EX077 — Option C risk.** What new dependency does option C introduce? *Rubric:* 3 = internet links and new skills;; 2 = cloud;; 1 = none;; 0 = none.
- **EX078 — Weights.** Why agree criterion weights with stakeholders? *Rubric:* 3 = reflect priorities;; 2 = fairness;; 1 = none;; 0 = none.

### Synthesis

Comparing alternatives systematically makes the chosen architecture defensible.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Network and communications security: control design

### Learning outcomes

You will (1) specify firewall policies; (2) design management access; (3) design logging.

### 27.1 Policy specification

The policy is specified as a table and as code. Each rule names zones, services and action, ending in default deny.

The policy specification states, for every pair of zones, which services are allowed and why, with everything else denied. It is written in a structured table that both people and scripts can read. Because it is the source of truth, the firewall configuration is checked against it, not the other way round, and changes to access start by changing the specification and getting it approved.

### Lab — Evaluating flows

```python
"""Evaluate synthetic flows against a first-match zone policy with default deny (stdlib only)."""
policy = [("staff", "servers", 443, "allow"), ("staff", "servers", 445, "allow"), ("voice", "servers", 5061, "allow"),
          ("cctv", "servers", 554, "allow"), ("mgmt", "*", 22, "allow"), ("*", "*", None, "deny")]
flows = [("staff", "servers", 443), ("staff", "servers", 3389), ("guest", "servers", 443), ("cctv", "servers", 554),
         ("cctv", "staff", 445), ("mgmt", "cctv", 22), ("voice", "servers", 5061), ("staff", "cctv", 554)]
def decide(f):
    for i, (s, d, p, a) in enumerate(policy, 1):
        if s in ("*", f[0]) and d in ("*", f[1]) and p in (None, f[2]): return a, i
for f in flows:
    a, i = decide(f); print(f"{f[0]:6}->{f[1]:8}:{f[2]:<5} {a:5} (rule {i})")
print("allowed", sum(decide(f)[0] == "allow" for f in flows), "of", len(flows))
```

Run with `python3 lab_policy.py`. Verified output:

```text
staff ->servers :443   allow (rule 1)
staff ->servers :3389  deny  (rule 6)
guest ->servers :443   deny  (rule 6)
cctv  ->servers :554   allow (rule 4)
cctv  ->staff   :445   deny  (rule 6)
mgmt  ->cctv    :22    allow (rule 5)
voice ->servers :5061  allow (rule 3)
staff ->cctv    :554   deny  (rule 6)
allowed 4 of 8
```

### 27.2 Reading the evaluation

Of eight synthetic flows, four are allowed by specific rules and four denied by the default rule, including guest to servers and staff to servers over remote desktop. The latter is a deliberate decision: remote desktop to servers is only allowed from management.

Evaluating the policy against the flow model shows which needed flows are covered and which allowed flows are unneeded. Any mismatch is investigated before deployment.

Typical findings include allowed flows left over from earlier testing, needed flows that the specification forgot, and rules broader than the flow requires, such as a whole subnet where one server would do. Each finding is resolved by updating either the specification or the rules.

### 27.3 Management access

Management uses a jump host with multi-factor authentication; device management interfaces accept connections only from it.

Management access to network devices is limited to a dedicated management zone reached only from approved administration workstations. Administrators authenticate individually, with multi-factor authentication, so actions are attributable to a person. Every session is logged. Separating management traffic this way means a compromised staff laptop cannot reach device consoles, and audit records show exactly who changed what and when.

Emergency access procedures are also documented and tested.

### 27.4 Logging design

All denies and a sample of allows are logged with the common schema.

Logging design decides what each device records and where it goes. Firewalls log denied connections and selected allowed ones, VPN gateways log connections and authentications, and devices log configuration changes. Logs are sent promptly to a central store with synchronised clocks, so they survive if a device is wiped. The design also sets retention and access controls, since logs themselves contain sensitive information.

Log volumes are estimated in advance to size storage.

### Policy for internet access

Each zone's access to the internet is also controlled. Staff browse through the council's web filter; phones reach only the provider's services; cameras reach only the supplier's update server during maintenance; guest Wi-Fi reaches the internet but nothing internal. Kofi writes these outbound rules with the same care as internal ones, because unrestricted outbound access lets compromised devices contact attackers' systems freely, and limiting it is one of the most effective controls a small organisation can apply. Outbound denies are reviewed weekly alongside internal ones, since they can reveal infected or misconfigured devices.

### Configuration consistency

With nine firewalls across eight offices, consistency matters. Kofi generates each branch policy from a common template and a small per-site file listing local subnets. Differences between branches are limited to these local values. A script compares deployed policies with generated ones and reports any drift, which addresses a common failure where one site's firewall is changed during an emergency and never brought back into line. Any drift found is either corrected or, if intended, added to the per-site file through a normal reviewed change.

### Worked example

Adding a test for each flow ensures future changes do not alter these outcomes unnoticed.

> **Synthetic case.** Flows are synthetic.

### Errors and limits

Logging every allow on busy links can overwhelm storage; sample or summarise.

### Exercises

- **EX079 — Allowed count.** How many flows were allowed? *Rubric:* 3 = 4 of 8;; 2 = four;; 1 = none;; 0 = none.
- **EX080 — RDP decision.** Why is staff→servers RDP denied? *Rubric:* 3 = only management may administer;; 2 = policy;; 1 = none;; 0 = none.
- **EX081 — Allow sampling.** Why sample allowed flows rather than log all? *Rubric:* 3 = volume;; 2 = storage;; 1 = none;; 0 = none.

### Synthesis

A specified, tested policy with controlled management access is the core control.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Network and communications security: implementation I

### Learning outcomes

You will (1) plan phased implementation; (2) migrate a pilot office; (3) verify behaviour.

### 28.1 Phasing

Implementation proceeds office by office, starting with a small branch. Each phase: prepare configuration, test in lab, migrate during an agreed window, verify and observe for two weeks.

Rolling out segmentation in phases limits risk. Each phase covers a defined set of offices or zones, with entry criteria, such as tests passed, and exit criteria, such as no unresolved service problems. Lessons from one phase change the plan for the next.

A clear phase plan also helps staff know when their office will change.

### 28.2 Pilot office

The pilot branch has forty devices. Kofi and the council engineers create VLANs, readdress devices and enable the new firewall in monitor mode first, logging what would be denied without blocking.

The pilot uses one small office whose staff agree to report problems. It tests the design under real conditions while limiting the impact of mistakes, and provides evidence for the wider rollout.

Before the pilot, Kofi confirms the office's flows with local staff, prepares the rules in monitor mode, and agrees a short daily check-in. Success criteria are set in advance, so the decision to proceed is based on evidence rather than impressions.

### 28.3 Monitor mode findings

Monitor mode reveals two flows missing from the needed list: a printer sending scans to a file share and phones fetching configuration from the provider. Both are added to the flows list and rules.

In monitor mode, rules log what they would block without blocking it. Reviewing these logs reveals needed flows missing from the model, which are added before enforcement.

Common findings include printers reaching a print server in another office, a forgotten scheduled backup, and devices using unexpected DNS servers. Each is checked with the service owner before being approved as a needed flow, because some findings reveal behaviour that should stop rather than be allowed.

### 28.4 Enforcement

After a week with no unexpected denies, enforcement is enabled.

Enforcement switches rules from monitoring to actually blocking. It is scheduled for a quiet period, with staff on hand, a tested rollback, and a contact route for users who find a service broken. After switching, engineers watch denied-connection logs closely for a few days. Any unexpected block of a legitimate flow is investigated, the flow model updated with approval, and the rule corrected, rather than adding a broad emergency exception.

### Readdressing devices

Moving devices into new subnets is the most disruptive part of migration. Devices using automatic addressing simply receive new addresses after reconnecting, but printers, phones and cameras with fixed addresses need manual changes. Kofi and the engineers prepare a list of fixed-address devices from the inventory, schedule their changes in the migration window and test each one afterwards. Devices that cannot be reached are noted for a follow-up visit rather than delaying the whole migration. The updated inventory, with new addresses, is saved after each window so documentation matches the deployed network.

### Rollback plan

Each migration window has a rollback plan: the previous switch and firewall configurations are saved, and reverting takes about fifteen minutes. A decision point is set halfway through the window: if critical tests fail by then, the team rolls back rather than troubleshooting under pressure. For the pilot, the decision point passes without issues, but having it agreed in advance keeps the team calm and protects services if something goes wrong. The saved configurations are checked to load correctly in the lab before each window, so rollback is known to work.

### Worked example

The pilot completes with no service interruptions reported.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Skipping monitor mode risks blocking needed but undocumented flows.

### Exercises

- **EX082 — Monitor mode.** What does monitor mode do? *Rubric:* 3 = logs would-be denies without blocking;; 2 = logs;; 1 = none;; 0 = none.
- **EX083 — Missing flows.** Name the two missing flows found. *Rubric:* 3 = printer scans and phone config;; 2 = one;; 1 = none;; 0 = none.
- **EX084 — Enforcement criterion.** When is enforcement enabled? *Rubric:* 3 = after a week with no unexpected denies;; 2 = later;; 1 = none;; 0 = none.

### Synthesis

Phased migration with monitor mode reduces risk.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Network and communications security: measurement

### Learning outcomes

You will (1) measure policy effects; (2) analyse denied flows; (3) identify issues.

### 29.1 What to measure

After enforcement, Kofi measures denied flows by zone pair. Expected denies, such as guest to servers, show the policy working; unexpected denies point to missing rules or misbehaving devices.

Measures follow the success criteria agreed earlier: reachable zone pairs, required flows working, denied connections from guest devices, and change-related incidents. Each is collected the same way as the baseline.

Using the same collection method matters, because a change in method can produce a difference that looks like improvement but is really just a different way of counting. Kofi documents each method alongside the numbers so the comparison stays honest.

### Lab — Denied flows

```python
"""Summarise a week of synthetic denied flows by zone pair to find expected vs unexpected denies (stdlib only)."""
from collections import Counter
denies = [("staff","servers",3389)]*41 + [("cctv","staff",445)]*3 + [("guest","servers",443)]*118 + [("staff","cctv",554)]*9 + [("voice","staff",5060)]*2
c = Counter((a, b) for a, b, _ in denies)
expected = {("guest", "servers")}
for (a, b), n in c.most_common():
    print(f"{a:6}->{b:8} {n:4d} {'expected' if (a,b) in expected else 'investigate'}")
print("total denies", len(denies), "| to investigate", sum(n for k, n in c.items() if k not in expected))
```

Run with `python3 lab_flows.py`. Verified output:

```text
guest ->servers   118 expected
staff ->servers    41 investigate
staff ->cctv        9 investigate
cctv  ->staff       3 investigate
voice ->staff       2 investigate
total denies 173 | to investigate 55
```

### 29.2 Reading the result

Of 173 denies in a week, 118 are guest to servers, expected. The remaining 55 need investigation: 41 staff remote desktop attempts to servers, nine staff connections to cameras, three camera connections to staff devices and two phone connections to staff.

Results are compared with baseline and target, noting uncertainty and anything unusual in the measurement period.

For example, a fall in reachable zone pairs from fifty-six to nine shows segmentation is in place, but the meaning depends on whether all nine remaining pairs are needed. Results are presented with their limits, so readers do not assume more certainty than the evidence supports.

### 29.3 Investigation

Remote desktop attempts come from staff who used to administer servers informally; they are directed to the jump host. Camera connections to staff are cameras trying to send email alerts; the supplier reconfigures them. Staff connections to cameras are a training issue: footage is viewed via the recorder.

Where results differ from expectations, Kofi investigates causes rather than adjusting the numbers, and records findings.

An investigation starts from the measurement, gathers relevant logs and configuration history, forms possible explanations, and tests each against the evidence. Findings may show a measurement error, a design gap, or an operational issue, and each leads to a different follow-up action.

### Allowed flow analysis

Denied flows tell only half the story. Kofi also reviews a sample of allowed flows to check that permitted rules are used as expected. One rule permitting staff access to a legacy application shows no traffic for a month; its owner confirms the application was retired, and the rule is removed. Regularly reviewing rule usage keeps the policy from accumulating unused rules, the problem that research on firewall policies has repeatedly found in long-lived rule bases. Rule owners are asked to confirm their rules each quarter, which spreads responsibility beyond the network team.

### Trends over time

A single week can mislead. Kofi tracks denied flows weekly for two months after each office migration. Unexpected denies spike in the first week as hidden dependencies surface, then fall as rules and habits adjust. A rise later would suggest a change elsewhere, such as a new device type, and triggers investigation. Plotting these trends gives managers a simple picture of the migration settling down. Each trend chart is annotated with migration dates and policy changes, so managers can link changes in counts to causes.

### Worked example

After fixes, unexpected denies fall to four per week.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Treating all denies as attacks wastes effort; most reveal configuration or habit issues.

### Exercises

- **EX085 — Expected share.** What share of denies were expected? *Rubric:* 3 = 118 of 173;; 2 = most;; 1 = none;; 0 = none.
- **EX086 — Camera denies.** What caused cameras to contact staff devices? *Rubric:* 3 = email alerts misconfigured;; 2 = config;; 1 = none;; 0 = none.
- **EX087 — Interpretation.** Why not treat all denies as attacks? *Rubric:* 3 = most are configuration or habits;; 2 = noise;; 1 = none;; 0 = none.

### Synthesis

Measuring denies reveals hidden dependencies and habits.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify requirements in the lab; (2) record evidence; (3) trace results.

### 30.1 Lab setup

The lab replicates one office with spare equipment and virtual machines representing zones.

The verification lab reproduces the design on a small scale, using spare or virtual equipment, synthetic addresses and synthetic traffic. It is isolated from the production network so tests cannot disrupt services. Its configuration is drawn from the same version-controlled files as production, so tests exercise exactly what will be deployed. Documenting the lab setup allows others to rebuild it and repeat the tests.

The lab is reset before each test run.

### 30.2 Test cases

Tests check R1, R2, R3 and R7 by attempting permitted and forbidden connections from test machines within the lab only.

Each test case states its purpose, the requirement it verifies, the input such as a synthetic connection attempt, and the expected result such as allowed or denied. Cases cover both needed flows that must work and forbidden flows that must fail, plus edge cases such as boundary addresses. Writing expected results before running tests prevents the engineer from reinterpreting outcomes afterwards.

### 30.3 Evidence

Each test records date, configuration version, expected and actual result.

Evidence records what each test actually did and showed: the date, configuration version, test input, observed output, and pass or fail. Logs or screenshots are stored with the record. Good evidence lets a reviewer confirm the result without rerunning the test, and supports the thesis and the council's acceptance. Evidence that cannot be traced to a specific configuration version is much weaker, because it may describe a setup that no longer exists.

### 30.4 Results

All tests pass; one test reveals a rule allowing management to cameras on an unnecessary port, which is narrowed.

Results are summarised as pass rates per requirement, with every failure listed, its cause, and the fix applied and retested. A clean summary hides nothing, because reviewers trust a report that shows failures honestly more than one where everything passed first time. Remaining failures that are accepted are recorded as residual risk with an owner.

Results are shared with the council in plain terms.

### Test design

Kofi designs tests from the requirements, not from the configuration. For R1, tests attempt connections from a guest test machine to each internal zone on common services and expect every one to fail; they also confirm guest can still reach the internet, so the test detects over-blocking as well as under-blocking. Designing from requirements means the tests would catch a configuration that looks tidy but does not meet the need. Each test names the requirement it supports, which later feeds directly into the traceability table used for validation.

### Negative and positive tests

Every requirement gets both positive tests, showing permitted flows work, and negative tests, showing forbidden flows fail. A policy that blocks everything would pass all negative tests, so positive tests are essential. Kofi balances the two, with roughly equal numbers. He also includes boundary tests, such as the port just beside a permitted one, to show rules are exactly as narrow as intended. Tests use synthetic devices in the lab, so no real user traffic or council data is involved in testing.

### Regression testing

The lab tests are kept as a regression suite. After any policy change, the full suite runs in the lab before the change reaches production. This catches unintended side effects, such as a new rule placed above an existing deny that widens access. The suite takes about ten minutes to run and becomes part of the council's change process after the project. The suite is updated whenever a requirement or needed flow changes, so it always reflects the current agreed design. New tests are reviewed like any other change.

### Worked example

The test log has 24 entries, all passing after the fix.

> **Synthetic case.** Lab results are synthetic.

### Errors and limits

Lab differences from production must be noted.

### Exercises

- **EX088 — Lab scope.** Why test only within the lab? *Rubric:* 3 = authorisation and safety;; 2 = safe;; 1 = none;; 0 = none.
- **EX089 — Evidence fields.** List four evidence fields. *Rubric:* 3 = four;; 2 = three;; 1 = fewer;; 0 = none.
- **EX090 — Lab finding.** What did the lab reveal? *Rubric:* 3 = unnecessary management port;; 2 = issue;; 1 = none;; 0 = none.

### Synthesis

Lab verification provides evidence before production rollout.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Network and communications security: implementation II

### Learning outcomes

You will (1) implement inter-office VPNs; (2) migrate remaining offices; (3) control supplier access.

### 31.1 VPN rollout

Site-to-site IPsec tunnels with IKEv2 and certificates are configured between each branch and the main office, following SP 800-77 Rev. 1.

Site-to-site VPN links replace unprotected links between offices one by one. Each is configured from the template, tested in the lab, then deployed in a maintenance window with rollback ready, and traffic is checked afterwards.

Before each link goes live, Kofi confirms both ends use matching settings, certificates are valid, and monitoring shows the tunnel status. Afterwards, he checks that traffic between offices flows through the tunnel rather than the old path, and records the result as evidence.

### 31.2 Remaining offices

Remaining offices migrate using the pilot method.

Once the pilot succeeds, the remaining offices follow in planned order, usually starting with smaller sites where problems affect fewer people. Each office gets the same checklist: confirm local flows, deploy rules in monitor mode, review findings, enforce, and verify. Keeping the process identical across sites makes problems easier to spot, because any difference in outcome points to something particular to that office rather than to the method.

Progress is tracked on a simple shared schedule.

### 31.3 Supplier access

The CCTV supplier's appliance is removed; the supplier connects via the jump host with named, time-limited accounts.

Suppliers who maintain council systems need remote access, but only to their own systems. Engineers give each supplier an individual account, restrict access to specific hosts and services, require multi-factor authentication, log sessions, and enable access only when needed. Access is reviewed regularly and removed when a contract ends.

Supplier sessions are recorded where contracts permit, so actions can be reviewed after an incident. Contracts should also state security expectations, such as reporting breaches promptly and protecting credentials.

### 31.4 Communication

Office managers receive notices before each migration.

Staff need to know what is changing, when, and what to do if something stops working. Kofi helps the council send short notices before each office's change, naming the date, the expected effect, and a contact for problems. After the change, a brief follow-up confirms completion. Clear communication reduces the number of support calls, helps staff report genuine problems quickly, and builds trust in the security programme rather than resentment of it.

Feedback channels stay open afterwards.

### Certificate management in practice

Each firewall's certificate is issued by the council's internal certificate authority with a two-year lifetime and stored on the device. Kofi documents the issuance and renewal steps and adds every certificate to the expiry monitoring. He also tests revocation in the lab: when a branch firewall's certificate is revoked, the main office refuses its tunnel, as intended. This confirms that a stolen branch device could be cut off quickly, which was one of the threats identified in chapter 23. Renewal steps are rehearsed in the lab once a year so engineers remember them.

### Migration timeline

The remaining seven offices are migrated at a pace of roughly one every three weeks, allowing two weeks of observation after each. Larger offices take two migration windows, splitting staff and voice from cameras and guest. The timeline is published to office managers with dates, so they can plan around the short disruptions. Two migrations are moved for local events, which the schedule absorbs without affecting the overall finish. After each migration, a short note records issues found and lessons for the next office.

### Supplier transition

Before removing the supplier's appliance, Kofi and the council agree a transition plan with the CCTV supplier: their engineers receive named accounts, test access through the jump host during a maintenance window and confirm they can perform routine tasks. Only then is the appliance removed. The supplier's contract is updated to reflect the new access method and the requirement to request access windows, which turns a security change into an agreed working practice. Supplier access through the jump host is logged and reviewed monthly by the council engineers.

### Worked example

All eight offices migrate within five months.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Removing supplier access abruptly can break maintenance contracts; agree changes first.

### Exercises

- **EX091 — VPN standard.** Which guidance governs the VPN configuration? *Rubric:* 3 = SP 800-77r1;; 2 = NIST;; 1 = none;; 0 = none.
- **EX092 — Supplier change.** How does the supplier now connect? *Rubric:* 3 = jump host with named, time-limited accounts;; 2 = jump host;; 1 = none;; 0 = none.
- **EX093 — Agreement first.** Why agree supplier changes in advance? *Rubric:* 3 = contract obligations;; 2 = cooperation;; 1 = none;; 0 = none.

### Synthesis

Implementation completes segmentation and secures links and supplier access.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Network and communications security: reliability

### Learning outcomes

You will (1) model availability; (2) design redundancy; (3) test failover.

### 32.1 Availability model

A single tunnel with 99.5 percent availability gives about 44 hours of downtime a year.

An availability model estimates the share of time a service can be reached, combining the availability of each component it depends on. Components in series multiply, so a chain of many parts is less available than any one of them; redundant parallel components improve availability. The model shows where a single failure would cut off an office.

Inputs such as failure and repair times come from records or vendor data, stated as assumptions.

### Lab — Redundant tunnels

```python
"""Availability of a site's VPN with one vs two independent tunnels (synthetic, stdlib only)."""
a = 0.995
for n in (1, 2):
    av = 1 - (1 - a) ** n
    print(f"tunnels {n}: availability {av:.6f}; expected downtime {(1-av)*8760:.2f} h/year")
```

Run with `python3 lab_avail.py`. Verified output:

```text
tunnels 1: availability 0.995000; expected downtime 43.80 h/year
tunnels 2: availability 0.999975; expected downtime 0.22 h/year
```

### 32.2 Reading the model

Two independent tunnels raise availability to 99.9975 percent, about 13 minutes a year, assuming independent failures.

Reading the model, Kofi identifies the components that contribute most to downtime and the single points of failure. These become candidates for redundancy, while components with little effect do not justify extra spending. He reports results with assumptions stated, such as estimated failure and repair times.

Results are best presented as expected hours of downtime per year, which managers grasp more easily than percentages such as 99.9. The model is then used to compare options, such as a second internet link, by showing how much downtime each would remove relative to its cost.

### 32.3 Independence

Independence requires different providers or paths. Kofi recommends a second link from a different provider at the three largest offices.

Redundancy only helps if failures are independent. Two links through the same duct, or two firewalls on the same power circuit, can fail together. Engineers check for shared causes and record them, because the simple model overstates availability when components share dependencies.

Where dependence cannot be removed, the risk is stated honestly. For example, if both main office links leave the building through one duct, a single excavation can cut both, and the report should say so even if the numerical model suggests high availability.

### Failover design

Redundant links help only if traffic moves to the surviving link quickly. Kofi configures tunnel monitoring so the branch firewall detects a dead tunnel within twenty seconds and routes traffic through the second tunnel. The requirement R6 sets a sixty-second limit for failover. He tests failover in the lab by disabling one link and timing recovery, and later repeats the test at one branch in an approved window, recording the times as evidence. Failover is retested after any change to tunnel or routing configuration, because small changes can slow detection.

### Main office redundancy

The main office firewall carries all inter-office traffic, so it is deployed as an active-standby pair. If the active unit fails, the standby takes over with existing connections preserved. Firmware updates are applied to the standby first, then roles are swapped, avoiding downtime. Kofi documents the pair's health checks and the alert raised when one unit is unavailable, so the team knows when redundancy is temporarily lost. The pair is tested twice a year by deliberately failing the active unit during an approved maintenance window and timing the switch.

### Limits of the model

The availability model assumes failures are independent and that failover is instant. In reality, both providers might share a road where cables run, and failover takes up to sixty seconds. Kofi states these limits next to the figures and asks providers for route information where possible. The model is a guide to decisions, not a guarantee, and presenting its assumptions keeps managers' expectations realistic. Where providers cannot supply route information, the risk of a shared path is recorded as an open assumption. The figures are recalculated once real outage data for a full year becomes available.

### Worked example

The council funds second links at three offices.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Two links in the same duct are not independent.

### Exercises

- **EX094 — Downtime calculation.** Compute downtime for 99.5% availability. *Rubric:* 3 = 43.8 h;; 2 = value;; 1 = none;; 0 = none.
- **EX095 — Redundant result.** What does the lab give for two tunnels? *Rubric:* 3 = 0.999975, 0.22 h;; 2 = value;; 1 = none;; 0 = none.
- **EX096 — Independence condition.** What makes tunnels independent? *Rubric:* 3 = different providers and paths;; 2 = different;; 1 = none;; 0 = none.

### Synthesis

Redundancy dramatically improves availability when failures are independent.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Network and communications security: safety and resilience

### Learning outcomes

You will (1) protect critical services; (2) plan degraded modes; (3) exercise recovery.

### 33.1 Critical services

Out-of-hours social care and CCTV are critical. They get priority on redundant links.

Critical services are those the council cannot do without for long, such as emergency contact systems, payments and core file access. Listing them with their dependencies, including network zones, links and authentication, shows what must be protected and restored first after a disruption. Each service has an owner who agrees the acceptable outage time.

This list guides both design and recovery planning, so it is reviewed annually.

### 33.2 Degraded modes

If the main office is isolated, branches keep local services and phones fall back to mobile.

A degraded mode is a planned way of continuing with reduced function, such as an office using a backup internet link with limited services, or staff working from paper forms. Planning degraded modes in advance means a failure leads to a known, safe fallback instead of improvisation, and that security controls still apply during the fallback.

Staff practise switching to degraded modes so they know how.

### 33.3 Recovery

Configuration backups allow rebuild of a failed firewall within four hours.

Recovery restores normal service after a disruption. Plans list steps in order, starting with critical services, and include restoring configuration from version control, verifying rules, and checking that monitoring works again. Each step has an owner and expected time. Recovery is not complete until services are verified and the cause is understood, so the same failure is less likely to recur.

Lessons are recorded and the plan updated.

Timings are compared with targets.

### 33.4 Exercises

A tabletop exercise walks through main office loss.

Recovery plans are tested through exercises. A tabletop exercise walks through a scenario on paper, such as a firewall failure at the main office, with each participant describing their actions. A practical exercise restores a configuration in the lab and times it. Exercises reveal missing steps, outdated contacts and unrealistic timings. Findings are recorded, plans updated, and exercises repeated, so the organisation is ready when a real disruption happens.

Exercises should be blameless and realistic.

### Recovery documentation

Recovery depends on documentation that is available when the network is not. Kofi keeps printed copies of the recovery runbook, firewall backups on encrypted storage at two sites and contact lists for providers and suppliers. The runbook gives step-by-step instructions for replacing a failed branch firewall from a spare, including which configuration file to load and which tests to run afterwards. He tests the runbook by asking an engineer unfamiliar with the project to follow it in the lab. Gaps found in that test are corrected before the runbook is approved.

### Spare equipment

Hardware failures take time to resolve under support contracts. The council keeps one spare branch firewall, preloaded with the common template, at the main office. With the runbook and backups, a failed branch firewall can be replaced within four hours, well inside the time a branch can operate in degraded mode. The spare is updated with firmware quarterly so it is ready when needed. The spare's firmware and template version are logged so engineers know its state before using it. Its location and access arrangements are listed in the runbook so it can be collected quickly out of hours.

### Resilience against misconfiguration

Many outages are caused by configuration changes rather than hardware. The design's resilience therefore includes the change process: review, lab testing, rollback plans and change windows. Kofi counts change-related incidents before and after the project as a resilience measure, alongside link availability, reflecting the reality that people and process failures are as important as equipment failures. He also reviews each change-related incident to see which safeguard failed, and strengthens that step. Over the project, this shows change failures falling as the process matures, giving the council evidence that discipline in change management improves availability as much as extra hardware does.

### Worked example

The exercise reveals that the out-of-hours line depends on the main office; a backup route is added.

> **Synthetic case.** The exercise is synthetic.

### Errors and limits

Resilience untested in exercises often fails in reality.

### Exercises

- **EX097 — Degraded mode.** Describe one degraded mode. *Rubric:* 3 = branches local, phones to mobile;; 2 = one;; 1 = none;; 0 = none.
- **EX098 — Exercise finding.** What did the exercise reveal? *Rubric:* 3 = out-of-hours line dependency;; 2 = dependency;; 1 = none;; 0 = none.
- **EX099 — Rebuild target.** What is the firewall rebuild target? *Rubric:* 3 = four hours from backups;; 2 = hours;; 1 = none;; 0 = none.

### Synthesis

Planning degraded modes protects critical services.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Network and communications security: integration

### Learning outcomes

You will (1) integrate logging and monitoring; (2) integrate with identity; (3) coordinate with other teams.

### 34.1 Logging integration

Firewall and VPN logs flow to the central store using syslog (RFC 5424).

The new firewalls and VPN gateways must send logs into the council's existing central store. Integration means agreeing formats, timestamps in UTC, transport, and field mapping to the common schema, then testing that records arrive complete and promptly. Kofi checks a sample of synthetic events end to end, from device to query result, before relying on the logs for monitoring.

Gaps found in testing are fixed before go-live.

### 34.2 Identity integration

Jump host authentication uses the council directory with multi-factor authentication.

Network access decisions and administrator logins should use the council's central identity system, not separate local accounts on each device. This means one place to add and remove people, consistent multi-factor authentication, and logs that link actions to named individuals. When someone leaves, removing their central account removes all their access at once, which is far more reliable than updating many devices.

Local emergency accounts remain, tightly controlled and audited.

### 34.3 Teams

The service desk is trained to recognise segmentation-related issues.

Several council teams share responsibility for the network: infrastructure, service desk, security and application owners. Integration includes agreeing who handles which requests, who approves changes, and who responds to alerts. A simple responsibility table, reviewed with each team, prevents tasks falling between teams and avoids conflicting changes. Kofi also runs short handover sessions so staff understand the new design they will operate.

Contact lists are kept current and tested regularly.

Escalation paths are written down.

### 34.4 Monitoring

Alerts cover tunnel down, certificate expiry and unusual deny spikes.

Monitoring confirms that the new design keeps working. Dashboards show link health, firewall load, denied connections by zone, and VPN status, with alerts on agreed thresholds. Regular reports compare measures against success targets. Monitoring is assigned to named staff with documented runbooks, so it continues after Kofi's project ends, which is the real test of whether the engineering has been successfully handed over.

Monitoring itself is checked for silent failures.

### Time and correlation

Logs from nine firewalls, the jump host and servers must line up in time to be useful. All devices synchronise to the council's time servers, and the central store records both the device timestamp and arrival time. Kofi checks a sample of records and finds one branch firewall eight minutes out because its time source was misconfigured; the fix is made and a monitoring check added. Accurate time is what lets an analyst follow a single event across several devices.

### Handover to operations

Integration includes people. Kofi runs sessions with the two network engineers and the service desk, covering the zone model, how to read deny logs, how to request a policy change and what alerts mean. He provides a one-page quick reference for the service desk listing common symptoms, such as a printer that cannot scan, and the likely cause. Calls about blocked services are routed to the network team with the device and time, which speeds diagnosis. Sessions are recorded so new staff can watch them later.

### Integration testing

Before declaring integration complete, Kofi runs end-to-end checks: a test deny on a branch firewall must appear in the central store, trigger the correct dashboard count and, for a spike, raise an alert to the on-call engineer. Each step is timed. Testing the whole chain, rather than each component separately, finds gaps such as an alert rule pointing at the wrong log field, which only appears when real records flow through the system. The end-to-end check is repeated monthly so silent breaks are found quickly.

### Worked example

Integration testing confirms logs arrive within one minute.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Integration gaps appear between teams, not devices.

### Exercises

- **EX100 — Log protocol.** Which protocol carries logs? *Rubric:* 3 = syslog RFC 5424;; 2 = syslog;; 1 = none;; 0 = none.
- **EX101 — Alert list.** List three alerts. *Rubric:* 3 = three;; 2 = two;; 1 = one;; 0 = none.
- **EX102 — Service desk.** Why train the service desk? *Rubric:* 3 = recognise segmentation issues;; 2 = support;; 1 = none;; 0 = none.

### Synthesis

Integration makes the design operable.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) refine the design after implementation; (2) address remaining gaps; (3) present to council stakeholders.

### 35.1 Reviewing what was built

Halfway through implementation, Kofi runs a second design studio with the council engineers, Dr Vasquez and two peers. The first studio reviewed plans; this one reviews what was actually built. He presents the deployed zone model, the measured fall in reachable zone pairs, the unexpected denies found and fixed, and the host-level exceptions that accumulated during migration. Comparing the built system with the design shows where reality diverged from intention, and those divergences are where the most useful lessons lie, because each one is either a design flaw, an implementation shortcut or a need nobody captured.

### 35.2 Gaps raised

Participants raise three gaps. First, staff at one office share a printer with guests in reception; the printer sits in the staff zone and is reachable from guest through a temporary rule added during migration. Second, guest wireless at two offices still uses an older captive portal on the same hardware as staff wireless, so a fault or misconfiguration could join them. Third, the management zone now contains a monitoring server that also needs internet access for updates, which blurs the boundary that made management the most tightly controlled zone. Each gap is small but undermines a requirement.

### 35.3 Responses

Kofi answers each gap with a specific change. A dedicated printer, reachable from guest only on the printing service, replaces the shared one, and the temporary rule is removed. The older guest wireless hardware is replaced so guest and staff networks are separated in the way NIST SP 800-153 recommends for wireless networks. The monitoring server fetches updates through the staff web filter instead of receiving direct internet access, so the management zone keeps its rule of no outbound connections. Every response is costed, given an owner and scheduled, and the temporary rule is removed within a week.

### 35.4 Presenting to stakeholders

The studio ends with a twenty-minute presentation to council managers, who care about service and cost rather than rule syntax. Kofi shows three things: the fall in reachable zone pairs, the original guest malware scenario now blocked, and the remaining work with dates and owners. Managers ask mainly about disruption, and he reports two short interruptions across six migrations, both resolved within the agreed change window. Translating technical results into service terms keeps managers' support, which matters because the remaining work, such as replacing wireless hardware, needs their budget approval.

### Worked example

The studio produces a list of nine actions, each with an owner and a date; seven are completed before the end of implementation.

> **Synthetic case.** The studio and actions are synthetic.

### Errors and limits

Temporary rules added during migration tend to become permanent unless each has an expiry and an owner.

### Exercises

- **EX103 — Temporary rule risk.** Why must migration-time temporary rules have expiries? *Rubric:* 3 = otherwise become permanent excess access;; 2 = cleanup;; 1 = none;; 0 = none.
- **EX104 — Printer solution.** How is the shared printer problem solved? *Rubric:* 3 = dedicated guest-reachable printer, rule removed;; 2 = separate printer;; 1 = none;; 0 = none.
- **EX105 — Management boundary.** Why route the monitoring server's updates via the web filter? *Rubric:* 3 = keep management zone without direct internet;; 2 = boundary;; 1 = none;; 0 = none.

### Synthesis

Reviewing the built system against the design catches drift while it is still cheap to fix.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Network and communications security: performance and scale

### Learning outcomes

You will (1) measure latency added by controls; (2) check capacity under load; (3) plan for growth.

### 36.1 Latency budget

The council's phone system and file access are sensitive to delay, so the new firewall hop must not noticeably slow them. Kofi sets a budget: the firewall must add less than one millisecond at the main office under normal load. He derives this from the phone provider's guidance on acceptable end-to-end delay and the baseline measured early in the project, reserving most of the allowance for existing switches, links and distance between offices. A written budget turns a vague worry about slowness into a number that can be measured, tested and either met or missed.

### Lab — Added latency

```python
"""Added latency through the new firewall: percentiles from synthetic samples in ms (stdlib only)."""
import statistics as st
s = [0.21,0.24,0.22,0.25,0.30,0.23,0.26,0.28,0.22,0.24,0.31,0.27,0.25,0.23,0.95,0.26,0.24,0.29,0.22,0.25]
q = st.quantiles(s, n=100)
print(f"n {len(s)} median {st.median(s):.3f} p95 {q[94]:.3f} max {max(s):.3f} ms; budget 1.0 ms met: {max(s) < 1.0}")
```

Run with `python3 lab_latency.py`. Verified output:

```text
n 20 median 0.250 p95 0.918 max 0.950 ms; budget 1.0 ms met: True
```

### 36.2 Reading the measurement

The lab reports twenty synthetic samples with a median of 0.25 milliseconds, a 95th percentile of about 0.92 and a maximum of 0.95. The budget is met, but the tail sits close to it, so Kofi looks at the slowest sample rather than stopping at the median. He links it to a burst of new connections when the nightly backup starts, which matches the slow-path behaviour for connection set-up described earlier in the course. He recommends staggering backup start times across servers, a cheap change that reduces bursts without altering any security rule.

### 36.3 Capacity under load

Latency at normal load says little about busy periods. Kofi runs throughput tests in the lab with all inspection features enabled, since vendor figures often assume features are switched off. The main firewall pair carries about twice the council's measured peak traffic, and branch firewalls about three times their local peak. The connection-state table stays below a third of capacity at peak. With the growth rates estimated in the planning chapters, these margins cover roughly five years, which matches the expected replacement cycle and avoids buying larger equipment than the council needs.

### 36.4 Scaling the policy

Traffic is not the only thing that grows; the policy grows too, and larger rule bases tend to contain more errors, as Wool's study of firewall configurations found. Kofi keeps the policy template-based, so adding an office means adding its local subnet values rather than writing new rules. He also sets a review trigger: when the total rule count rises by twenty percent from the approved baseline, the team reviews the whole policy for unused, overlapping or overly broad rules. This keeps growth deliberate rather than letting the rule base drift into the complexity that caused trouble before.

### Worked example

After staggering backups, a repeat measurement shows the 95th percentile falls to 0.41 milliseconds.

> **Synthetic case.** Measurements are synthetic.

### Errors and limits

Twenty samples describe one period; repeat at different times before concluding the budget is always met.

### Exercises

- **EX106 — Budget check.** Is the 1.0 ms budget met in the lab, and how close is the tail? *Rubric:* 3 = met, max 0.95, p95 0.918;; 2 = met;; 1 = none;; 0 = none.
- **EX107 — Slow sample cause.** What caused the slow sample and what fixes it? *Rubric:* 3 = connection burst at backup start, stagger;; 2 = backups;; 1 = none;; 0 = none.
- **EX108 — Growth trigger.** Why trigger a review when rule count rises 20 percent? *Rubric:* 3 = more rules, more errors;; 2 = size;; 1 = none;; 0 = none.

### Synthesis

Measured latency and capacity show the design performs within budget with room to grow.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Network and communications security: operations

### Learning outcomes

You will (1) define operational routines; (2) manage changes; (3) monitor health.

### 37.1 Daily and weekly routines

Operations depend on small routines done reliably. Each morning, an engineer checks tunnel status, firewall pair health and overnight alerts, which takes about ten minutes. Weekly, the team reviews unexpected denies by zone pair, certificates expiring within sixty days and configuration drift reports from the comparison script. Monthly, they review rule usage and remove unused rules after confirming with each rule's owner. Every routine has a written checklist, an expected duration and a place to record results, so anyone can see whether checks were done and what they found.

### 37.2 Change management

Policy changes follow the process designed earlier: a request stating the reason and owner, review against the needed-flows list, a lab test against the regression suite, a scheduled deployment and verification afterwards. Emergency changes are permitted when a service is down, but they must be recorded within one working day and reviewed at the next weekly meeting, so urgency never becomes a permanent bypass. Kofi tracks the change failure rate, meaning the share of changes that cause an incident or rollback, because it shows whether the process is actually preventing mistakes.

### 37.3 Monitoring health

Dashboards show tunnel availability, deny trends by zone pair, firewall processor and memory use, and the rate at which logs arrive in the central store. That last measure is easy to overlook but important. If a firewall stops sending logs, the dashboards simply go quiet, which looks exactly like a calm network. Kofi therefore alerts when log arrival from any device drops well below its normal rate. A silent logging failure would blind every other control that depends on logs, so monitoring the monitoring is treated as a core task rather than an extra.

### 37.4 On-call and escalation

Out of hours, only two kinds of alert page the on-call engineer: loss of tunnels at offices that run critical services, and failure of the main firewall pair. Everything else waits for the next working day, when it is handled through the normal routines. Kofi keeps the paging list short deliberately, because engineers who are woken often by alerts that turn out to be harmless learn to ignore pages, and an ignored page during a real outage is worse than no page at all. The list is reviewed quarterly against actual pages received.

### Learning from incidents in operation

When something does go wrong in operation, the council engineers hold a short blameless review within a week. The review records what happened, how it was detected, how long detection and recovery took, and which routine or control would have caught it sooner. The rollback caused by a misordered rule led to a new check in the change template: every proposed rule is tested in the lab against the full regression suite, not only against the flow it was meant to allow. Reviews focus on improving the system rather than blaming a person, which encourages engineers to report near misses honestly.

### Worked example

In the first three months of operation, the change failure rate is 4 percent, with one rollback caused by a rule placed in the wrong order.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Routines that rely on one engineer fail during leave; train both engineers and document routines.

### Exercises

- **EX109 — Weekly items.** List three weekly operational checks. *Rubric:* 3 = three;; 2 = two;; 1 = one;; 0 = none.
- **EX110 — Silent logging.** Why alert on a drop in log arrival? *Rubric:* 3 = logging failure blinds monitoring;; 2 = visibility;; 1 = none;; 0 = none.
- **EX111 — Paging policy.** Why page only for critical alerts out of hours? *Rubric:* 3 = keep pages meaningful;; 2 = fatigue;; 1 = none;; 0 = none.

### Synthesis

Simple, recorded routines and change management keep the segmented network healthy.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Network and communications security: validation

### Learning outcomes

You will (1) trace requirements to evidence; (2) identify gaps; (3) validate with users.

### 38.1 Traceability

Validation begins with traceability: linking every requirement to the tests that check it and to their latest results. Kofi builds on the table started during requirements work. For each of R1 to R8, the table lists the test identifiers, whether each test passed, failed or is pending, and the date and configuration version of the result. Reading across a row shows how well one requirement is supported; scanning the whole table shows which requirements have no evidence at all. The lab that follows builds this table from synthetic records so the gaps can be counted.

### Lab — Requirement traceability

```python
"""Requirement-to-test traceability for the segmentation design (synthetic, stdlib only)."""
reqs = {"R1 guest isolated": ["T1", "T2"], "R2 default deny between zones": ["T3"], "R3 mgmt via jump host only": ["T4"],
        "R4 VPN uses IKEv2 with certificates": ["T5"], "R5 logs retained 90 days": [], "R6 failover < 60 s": ["T6"],
        "R7 CCTV reaches recorder only": ["T7"], "R8 config backed up daily": []}
passed = {"T1", "T2", "T3", "T4", "T5", "T7"}
for r, ts in reqs.items():
    st = "untested" if not ts else ("pass" if all(t in passed for t in ts) else "fail/pending")
    print(f"{r:38} {','.join(ts) or '-':6} {st}")
print("covered", sum(1 for t in reqs.values() if t), "of", len(reqs))
```

Run with `python3 lab_trace.py`. Verified output:

```text
R1 guest isolated                      T1,T2  pass
R2 default deny between zones          T3     pass
R3 mgmt via jump host only             T4     pass
R4 VPN uses IKEv2 with certificates    T5     pass
R5 logs retained 90 days               -      untested
R6 failover < 60 s                     T6     fail/pending
R7 CCTV reaches recorder only          T7     pass
R8 config backed up daily              -      untested
covered 6 of 8
```

### 38.2 Reading the trace

The lab reports that six of eight requirements have tests and five of those pass. R6, failover within sixty seconds, is pending because the production failover test has not yet been scheduled. R5, keeping logs for ninety days, and R8, daily configuration backup, have no tests at all. These gaps are easy to miss because they describe operational behaviour rather than traffic filtering, and test design naturally focuses on filtering. That is exactly why a trace is valuable: it checks coverage against the list of requirements rather than against what engineers happened to think of testing.

### 38.3 Closing gaps

Kofi adds two tests. For R5, an inspection test checks that the oldest record in the central log store is at least ninety days old and that the deletion job removes nothing younger. For R8, a test restores the previous day's configuration backup onto the lab firewall and confirms that it loads and passes the regression suite. Both pass. The production failover test for R6 is then scheduled with the council in an approved window and completes in forty-two seconds, inside the limit. Every requirement now has passing evidence with a date.

### 38.4 User validation

Passing tests shows the requirements are met, but not that the requirements captured what people actually need. To check that, Kofi asks each office manager to complete a short form after migration: was any work blocked, slowed or made harder, and how was it resolved? Two issues are reported, a scanner that could not send to a shared folder and a supplier portal that failed, and both had already been found and fixed through deny analysis. This agreement between user reports and technical monitoring gives confidence that nothing important was missed.

### Verification and validation compared

Verification asks whether the system was built right: does each control behave as the requirements state? Validation asks whether the right system was built: does it meet the real needs of the people who depend on it? Kofi needs both. A network could pass every requirement test yet still block a service nobody remembered to list, or the requirements could miss a need entirely. The traceability table supports verification, while the managers' form and service desk trends support validation. Presenting both in the dossier shows examiners that the design is correct and also useful to the council in practice.

### Worked example

After closing gaps, all eight requirements have passing evidence, and the trace is attached to the evidence dossier.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Untested operational requirements often fail silently until needed in an incident.

### Exercises

- **EX112 — Coverage figure.** What coverage does the lab report before fixes? *Rubric:* 3 = 6 of 8 covered, R5 and R8 untested, R6 pending;; 2 = 6 of 8;; 1 = none;; 0 = none.
- **EX113 — R8 test.** Describe a test for daily configuration backups. *Rubric:* 3 = restore yesterday's backup to lab;; 2 = restore;; 1 = none;; 0 = none.
- **EX114 — Validation vs verification.** How does the managers' form differ from tests? *Rubric:* 3 = validates needs, not requirements;; 2 = users;; 1 = none;; 0 = none.

### Synthesis

Traceability exposes gaps; closing them gives complete evidence that the design meets its requirements.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Network and communications security: maintainability

### Learning outcomes

You will (1) design for long-term maintenance; (2) document thoroughly; (3) reduce dependency on individuals.

### 39.1 Documentation set

Kofi leaves the council a documentation set designed for the engineers who will run the network after he leaves. It contains an architecture overview, the zone model, the needed-flows list, the policy templates and per-site files, operational runbooks, the regression test suite and the decision records. Each document names an owner and a review date, so responsibility is clear and stale documents are noticed. Everything is stored in version control alongside the configurations, which means documentation and configuration change together and their history can be compared when something goes wrong.

### 39.2 Simplicity over cleverness

Throughout the design, Kofi faced choices between clever configurations and plain ones, and he chose plain. Every branch policy comes from one template; object names follow one convention that states zone, role and site; exceptions live in a single listed file rather than scattered across rules. A clever arrangement might save a few rules, but it costs understanding, and an engineer who misunderstands a configuration is likely to break it. The test Kofi applies is whether someone joining the team in three years could explain each rule after reading the documentation for an afternoon.

### 39.3 Knowledge transfer

Documents alone rarely transfer knowledge. For the last three office migrations, the two council engineers lead the work themselves while Kofi observes and answers questions only when asked. This builds their confidence and, just as importantly, exposes places where the documentation assumed knowledge they did not have. Each gap found, such as a missing step for loading certificates, is corrected immediately in the runbook. By the end, the engineers have carried out complete migrations without help, which is stronger evidence of maintainability than any amount of written material.

### 39.4 Vendor and lifecycle

Equipment has a life cycle that outlasts any project. Kofi records the firmware update schedule for each device model, the vendor's announced end-of-support dates, the support contract terms and the spare equipment plan. He adds the end-of-support dates to the council's budget calendar, so replacement can be funded a year ahead rather than discovered when security updates stop. Firmware updates follow the change process and are tested in the lab first. Without this record, maintenance would depend on someone remembering vendor announcements, which is not a reliable control.

### Decision records

A decision record captures one significant design choice: the context, the options considered, the option chosen, the reasons and the expected consequences. Kofi writes one for each major choice, such as firewalls at every office rather than only at the centre, IKEv2 with certificates rather than shared keys, and a jump host for supplier access. Each record is short, usually under a page. Years later, an engineer wondering why something was built a certain way can read the reasoning instead of guessing, and can tell whether the original conditions still hold before changing it. This prevents well-meant changes that quietly undo earlier protections.

### Worked example

An engineer from another council team uses only the documentation to add a new subnet at a branch, completing it correctly in under an hour.

> **Synthetic case.** The test is synthetic.

### Errors and limits

Documentation written at the end of a project is usually incomplete; write it alongside the work.

### Exercises

- **EX115 — Document list.** List five documents in the set. *Rubric:* 3 = five;; 2 = four;; 1 = fewer;; 0 = none.
- **EX116 — Knowledge transfer method.** How did Kofi transfer knowledge? *Rubric:* 3 = engineers led migrations with observation;; 2 = training;; 1 = none;; 0 = none.
- **EX117 — Maintainability test.** How was documentation tested? *Rubric:* 3 = outside engineer completed a task using it;; 2 = tried;; 1 = none;; 0 = none.

### Synthesis

Maintainable designs are simple, documented and owned by the people who will run them.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) run a full regression and failure suite; (2) verify against the incident scenario; (3) record evidence.

### 40.1 Full regression

At the end of implementation, Kofi runs the complete regression suite in the lab against final configurations generated from the templates for every office. The suite contains positive tests showing permitted flows work, negative tests showing forbidden flows fail, and boundary tests on ports and addresses next to permitted ones. Running it against every office, not just a sample, confirms that per-site values have not introduced site-specific errors. All tests pass, and the results are recorded with the configuration versions used, so the evidence can be reproduced later.

### 40.2 Incident scenario

He then reconstructs the incident that started the project, entirely in the lab with synthetic devices: a test machine on the guest network attempts the same kinds of file-sharing connections towards internal zones that the infected laptop made. Every attempt is denied and logged, and because the number of attempts exceeds the deny-spike threshold, an alert reaches the test on-call address within two minutes. In the old flat network, the same behaviour went unnoticed for hours. The comparison is the clearest single piece of evidence that the project addressed its original problem.

### 40.3 Failure tests

Security that fails during an outage is not enough, so the lab also tests failures. Kofi disables one tunnel at a branch and confirms traffic moves to the second within the requirement. He powers off the active main firewall and confirms the standby takes over with existing connections preserved. He issues a test certificate with a short life and confirms that monitoring flags it sixty days before expiry. Each test has a defined expected result written before it runs, so the outcome is judged against a prediction rather than interpreted afterwards.

### 40.4 Evidence

Each test result is recorded with the date, the tester, the configuration and template versions, the expected result and the actual result. Failed results are kept alongside the later passing ones, with a note of the fix. All records go into the evidence dossier, indexed by requirement. Recording evidence this carefully may seem excessive for a lab, but it allows an examiner or auditor to see exactly what was tested against which configuration, and it allows the council to rerun the same tests after future changes and compare results directly.

### Regression after every change

The regression suite is not run only once at the end. Kofi wires it into the change process so that every policy change is tested in the lab against all positive, negative and boundary tests before deployment. This matters because a rule added to fix one flow can unintentionally open another, especially when rule order decides the outcome. Running the whole suite takes about twelve minutes, which is short enough that engineers do not skip it. Over the project, the suite catches three changes that would have broken an existing requirement, each fixed before reaching any office. The suite itself is versioned with the configurations.

### Limits of laboratory evidence

Lab results are strong evidence but not complete proof. The lab uses the same firewall models and generated configurations, yet real offices have traffic patterns, cabling faults and user behaviour the lab cannot reproduce. Kofi therefore pairs each lab result with a production observation where possible: the failover test is repeated in a maintenance window, deny patterns are compared with lab predictions, and latency is measured on live links. Where production confirmation is impossible or unsafe, as with the incident reconstruction, he states clearly that the evidence is lab-only. Being explicit about this difference is part of honest engineering reporting and helps examiners judge the strength of each claim.

### Worked example

The suite runs 96 tests with all passing; the incident scenario produces an alert in 1 minute 40 seconds.

> **Synthetic case.** Lab results are synthetic.

### Errors and limits

Reconstructing incidents must be done only in the lab with synthetic devices.

### Exercises

- **EX118 — Incident result.** What happened in the reconstructed incident? *Rubric:* 3 = denied, logged, alerted under two minutes;; 2 = blocked;; 1 = none;; 0 = none.
- **EX119 — Failure tests.** Name three failure tests. *Rubric:* 3 = tunnel, firewall, certificate;; 2 = two;; 1 = one;; 0 = none.
- **EX120 — Lab-only reconstruction.** Why reconstruct the incident only in the lab? *Rubric:* 3 = authorisation and safety;; 2 = safe;; 1 = none;; 0 = none.

### Synthesis

The final lab suite shows the design blocks the original incident and survives failures.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Network and communications security: system optimization

### Learning outcomes

You will (1) identify inefficiencies; (2) optimise policy and logging; (3) balance cost and coverage.

### 41.1 Policy optimisation

Once the network is stable, Kofi looks for waste. Rule usage data show three rules unused for ninety days and two address groups containing devices that no longer exist. He asks each rule owner to confirm the rules are no longer needed, then removes them through the normal change process, cutting the policy by about eight percent. Because removing a rule can break a rarely used flow, the regression suite is run before and after, and it confirms behaviour is unchanged. A smaller policy is easier to review and less likely to hide mistakes.

### 41.2 Logging optimisation

Full logging of every allowed connection on busy links produces far more data than the team ever analyses, and storage costs money. Kofi switches allowed traffic to periodic flow summaries, which record source, destination, service and volume, while keeping full records for every deny and every management connection. Storage falls by about forty percent. Before making the change, he lists the questions past investigations needed to answer and checks that all of them can still be answered from summaries. Optimisation is accepted only if no needed evidence is lost.

### 41.3 Alert optimisation

The deny-spike alert was set conservatively at launch and fired eleven times in its first month, mostly because of guest devices repeatedly trying to reach printers or file shares they had remembered from other networks. These alerts were real but rarely important. Kofi groups denies by source device before counting and sets a higher threshold for the guest zone than for staff or servers. Alerts drop to three a month, all of which warranted a look. Fewer, more meaningful alerts mean engineers take each one seriously rather than dismissing them.

### 41.4 Cost

Optimisation has a direct financial effect. The council had planned to buy additional log storage during the year because of growth projected from the launch configuration. After the logging change, current storage covers the required ninety days with room to spare, and the purchase is cancelled. Kofi records the saving and its cause in the project report, so managers can see that operational care pays off. He also notes the time engineers save on alert handling, since staff time is usually the council's largest and most constrained cost.

### Optimising for people as well as machines

Optimisation is not only about storage and rules. Kofi also measures how long routine tasks take the engineers. The weekly deny review originally took about ninety minutes because the report listed every deny individually. Grouping denies by zone pair and showing only changes from the previous week cuts the review to about twenty-five minutes while still surfacing the cases that need investigation. Time saved on routine work is time available for improvement and for responding properly to real alerts. He records the before and after times so the council can see the benefit, and so later changes to the report can be judged against them.

### Guarding against over-optimisation

Every optimisation removes something, whether rules, log detail or alerts, and each removal could hide a future problem. Kofi applies three safeguards. First, he checks each change against known investigation and audit needs before making it. Second, he keeps changes reversible: log summarisation can be switched back to full detail for a zone during an incident. Third, he records the reason for each optimisation, so a reviewer can revisit it if conditions change, for example if the council later faces a new regulatory retention requirement. These safeguards keep efficiency gains from turning into blind spots that only appear when an incident needs the missing data.

### Worked example

After optimisation, regression tests pass and investigation queries still return complete results for the test period.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Optimising logs can remove evidence needed later; check investigation needs first.

### Exercises

- **EX121 — Rule removal check.** How is behaviour confirmed unchanged after removing rules? *Rubric:* 3 = regression suite;; 2 = tests;; 1 = none;; 0 = none.
- **EX122 — Logging change.** What logging change saved storage? *Rubric:* 3 = summaries for allows, full for denies;; 2 = summaries;; 1 = none;; 0 = none.
- **EX123 — Alert tuning.** How was the deny-spike alert improved? *Rubric:* 3 = grouping by source and zone-specific threshold;; 2 = threshold;; 1 = none;; 0 = none.

### Synthesis

Optimisation keeps the design lean without reducing protection or visibility.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Network and communications security: applied research

### Learning outcomes

You will (1) frame a research question from the project; (2) analyse data; (3) relate to literature.

### 42.1 Question

Kofi frames a research question that comes directly from operating the network: do unexpected denies in the first weeks after an office migrates predict later service complaints from that office? If they do, engineers could use deny counts as an early warning and prioritise which offices to visit or call. A good applied question is narrow enough to answer with available data, useful to the partner if answered either way, and stated before the data are examined, so that the analysis tests the question rather than searching for any pattern that happens to appear.

### 42.2 Data

The data are weekly counts of unexpected denies per office and service desk tickets mentioning network access, both covering eight migrations. Before analysis, office names and any staff identifiers are replaced with codes, and only counts leave the council's systems, which the information governance officer approves. Kofi also records each office's staff numbers, migration date and season, because these may explain differences. Using data the council already collects for operations avoids new monitoring of staff, which keeps the study proportionate and simplifies its ethical review.

### 42.3 Analysis

Kofi plots first-week unexpected denies against tickets in the first two weeks for each office. Offices with more denies tend to have more tickets, a positive association. Because larger offices could simply have more of both, he repeats the comparison per hundred staff, and the pattern weakens but remains. With only eight offices, a single unusual office could create or hide the pattern, so he reports the direction and size of the association without a strong statistical claim, describing it as suggestive and worth testing on more data rather than established.

### 42.4 Literature

He places the finding in context. Wool's 2004 study of firewall rule sets showed that configuration errors are common and grow with complexity, which supports the idea that newly introduced policies will contain gaps that surface as unexpected denies. Sommer and Paxson's 2010 paper on machine learning for intrusion detection warns how hard it is to generalise from limited operational data, which supports his caution. Linking a small local result to established work shows readers where it fits and stops it from being presented as more novel or more general than it is.

### Method and threats to validity

Kofi writes a short method section. He defines an unexpected deny as a denied flow in an allowed business category that was not on the expected list, and a service complaint as a ticket mentioning network access. Both definitions are fixed before he looks at the results. He then lists threats to validity. Offices differ in size, so larger offices may simply have more of both; he therefore also compares counts per hundred staff. Ticket wording varies, so some complaints may be missed. Migrations happened in different seasons, which could affect workload. Naming these threats helps readers judge the finding fairly rather than overstating it.

### From finding to practice

Even a suggestive result can inform practice when acting on it is cheap. Kofi recommends that, for future migrations, engineers review unexpected denies daily in the first week and contact the office manager when the count exceeds a simple threshold. The cost is a few minutes a day, and the possible benefit is fewer frustrated staff and faster discovery of missing flows. He also suggests that if the council or neighbouring councils carry out more migrations, they record the same two measures so a larger dataset can test the association properly. This turns a small study into the start of a continuing evidence base.

### Worked example

The analysis is written as a two-page note for the council and a section of the thesis.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Eight data points cannot support strong claims.

### Exercises

- **EX124 — Research question.** State Kofi's research question. *Rubric:* 3 = denies predict complaints;; 2 = partial;; 1 = none;; 0 = none.
- **EX125 — Claim strength.** How strongly can he claim the association? *Rubric:* 3 = suggestive only, eight offices;; 2 = weak;; 1 = strong;; 0 = none.
- **EX126 — Practical use.** How could engineers use the finding? *Rubric:* 3 = prioritise investigation of offices with many denies;; 2 = prioritise;; 1 = none;; 0 = none.

### Synthesis

Applied research turns project data into modest, useful evidence.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within public-sector governance; (2) engage stakeholders; (3) follow procurement.

### 43.1 Governance

Councils change their systems through formal governance. Significant network changes go to a change advisory board, which checks risk, timing and rollback plans, and anything touching personal data goes to information governance review. Kofi learns to write short papers for each: a page stating what will change, why, the risk of changing and of not changing, the rollback plan and who is responsible. Boards meet monthly, so a missed submission costs weeks. Treating governance as part of the engineering plan, rather than an obstacle, keeps the project on schedule.

### 43.2 Procurement

Public bodies must buy equipment and services through procurement rules designed to ensure fair competition and value for money. The council's firewalls and second network links are bought through existing public-sector framework agreements, which are faster than a full tender but still take several weeks for quotes, approval and ordering. Kofi builds these lead times into the schedule and orders long-lead items such as links early. He also writes clear technical requirements for the purchase, so the equipment bought matches the design rather than whatever is cheapest.

### 43.3 Stakeholders

More people are affected by the network than the IT team. Office managers care about disruption; staff representatives and unions care about whether logging will be used to monitor individuals; the information governance officer cares about lawful handling of personal data. Kofi meets each group early, explains what logs contain and that they are used for security and troubleshooting, not performance management, and records that commitment in the logging notice. Early consultation prevents objections late in the project, when they would be far more disruptive.

### 43.4 Public accountability

A council spends public money and holds residents' data, so its decisions may be examined by auditors, elected members or the public through information requests. Kofi therefore records decisions, the options considered, costs and approvals in a form that a non-specialist could follow. This differs from many private-sector projects, where informal agreements may be enough. Good records also protect staff: if a decision is later questioned, the record shows it was reasoned, approved by the right body and based on the information available at the time.

### Data protection in network logs

Network logs contain addresses, device names and sometimes usernames, which can identify staff and residents. Under data protection law, the council must have a lawful basis for collecting them, keep them only as long as needed and protect them from misuse. Kofi works with the information governance officer to write a short logging notice that explains what is collected, why, for how long and who can access it. Access to raw logs is limited to the security engineers, and every search is itself recorded. The ninety-day retention in requirement R5 is justified by investigation needs and documented, so it can be defended if questioned.

### Working with suppliers

Public bodies depend on suppliers for equipment, links and services such as the CCTV system. Kofi learns that security expectations must be written into contracts, not just discussed. The council's revised supplier terms require remote access only through the jump host, named individual accounts, notice before changes and prompt reporting of security incidents. Existing contracts are amended at renewal. Supplier performance against these terms is reviewed annually. This approach turns the CCTV bypass problem found at the start of the project into a general rule, so future suppliers cannot create the same hidden path through the firewall without breaching their contract.

### Worked example

Kofi's change paper for the board fits on two pages and is approved first time.

> **Synthetic case.** Processes are synthetic.

### Errors and limits

Ignoring governance delays projects more than technical problems.

### Exercises

- **EX127 — Monitoring consultation.** Why consult unions on monitoring? *Rubric:* 3 = staff privacy and trust;; 2 = privacy;; 1 = none;; 0 = none.
- **EX128 — Procurement planning.** Why plan for procurement time? *Rubric:* 3 = weeks-long frameworks;; 2 = delays;; 1 = none;; 0 = none.
- **EX129 — Accountability.** Why record decisions in public bodies? *Rubric:* 3 = accountability for spending and data;; 2 = audit;; 1 = none;; 0 = none.

### Synthesis

Public-service practice requires governance, consultation and accountability.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define the capstone scope; (2) plan evaluation; (3) set success criteria.

### 44.1 Scope

The capstone covers the whole segmentation and VPN project across all eight offices: the zone model, office firewalls, IKEv2 tunnels with certificates, central logging, monitoring and the operational processes that keep them working. It excludes endpoint protection and application security, which belong to other council teams, though Kofi notes where they interact, such as host firewalls on servers. Stating scope clearly protects the evaluation from being judged on things the project never aimed to change, and stops the project from quietly expanding beyond what can be finished and measured.

### 44.2 Evaluation plan

Kofi chooses six measures: reachable zone pairs, unexpected denies per week, VPN availability, latency added by the firewalls, change failure rate and requirement coverage. For each, the plan states how it is measured, from which data, over what period and by whom. Reachable pairs come from the policy model; denies and availability from central logs; latency from lab and live measurements; change failures from the change log; coverage from the traceability table. Defining measurement in advance stops later arguments about which numbers count.

### 44.3 Criteria

Measures need targets that define success. Kofi sets four criteria: guest isolation verified by both lab and production tests; every requirement supported by passing evidence; VPN availability above 99.9 percent over the measurement period; and added latency within the one-millisecond budget. Each criterion is clear enough that two people would agree whether it was met. The criteria are agreed with Dr Vasquez and the council before results are collected, which prevents the temptation to adjust targets after seeing the numbers.

If VPN availability came in at 99.8 percent, for example, that criterion would be reported as not met rather than reframed.

### 44.4 Risks

Kofi lists the risks to completing the capstone. Procurement delays could postpone second links and shorten the availability measurement. Staff availability matters because migrations need council engineers present. A serious incident elsewhere in the council could pull the team away for weeks. Each risk has a likelihood, an impact and a response: links are ordered early, migrations are scheduled around known leave, and the plan identifies which measures could still be reported if time runs short. Managing project risk is part of engineering, not separate from it.

### Linking criteria to requirements

Each success criterion traces back to one or more requirements and to the original problem. Guest isolation verified addresses R1 and the guest malware incident that started the project. All requirements evidenced covers R1 to R8 through the traceability table. Availability above 99.9 percent relates to R6 and to the council's need for reliable access to central services. Latency within budget protects the phone system. Writing these links explicitly prevents the capstone from drifting into measuring things that are easy to count but unrelated to what the council actually needed, and makes it clear to examiners why each measure matters.

### Baseline for comparison

A result only has meaning against a baseline. Kofi uses the measurements gathered before any change, documented in the early chapters: thirty reachable zone pairs on the flat network, no logging of internal traffic, a single VPN path per office and no record of changes. Where a baseline value was not measured, such as availability under the old design, he estimates it from service desk records and states it as an estimate. He resists the temptation to compare against an imagined worst case, which would make improvements look larger than they are. A fair baseline makes the capstone results credible.

### Schedule and checkpoints

The capstone runs over two academic terms. Kofi sets checkpoints every four weeks: migrations complete, monitoring baselines stable, failover trials done, measurements collected and analysis written. At each checkpoint, he and Dr Vasquez review progress against the plan and decide whether to adjust scope. One planned extra, an evaluation of a newer wireless authentication method, is deferred at the second checkpoint because procurement for the second links has slipped. Recording these decisions shows that scope was managed deliberately rather than abandoned, and keeps the core evaluation on schedule with sufficient time left for writing.

### Worked example

The capstone plan is approved by Dr Vasquez and the council.

> **Synthetic case.** The plan is synthetic.

### Errors and limits

Changing criteria after results undermines credibility.

### Exercises

- **EX130 — Criteria list.** List four success criteria. *Rubric:* 3 = four;; 2 = three;; 1 = fewer;; 0 = none.
- **EX131 — Criteria timing.** Why fix criteria early? *Rubric:* 3 = avoid moving goalposts;; 2 = credibility;; 1 = none;; 0 = none.
- **EX132 — Capstone risk.** Name one capstone risk. *Rubric:* 3 = procurement delay;; 2 = risk;; 1 = none;; 0 = none.

### Synthesis

Clear criteria frame the capstone evaluation.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) obtain external review; (2) respond to findings; (3) record changes.

### 45.1 Reviewer

Kofi asks an experienced network engineer from a neighbouring council to review the design and evidence. The reviewer has no involvement in the project and no stake in its success, which is what makes the review independent. They also understand the constraints of a small public body, such as limited staff and procurement rules, so their advice is practical. Dr Vasquez agrees the choice and the scope of the review in advance. The reviewer receives read-only lab access and the documentation, but no access to production systems.

### 45.2 Findings

The reviewer reports two significant findings. First, all administrative access passes through a single jump host, so if it fails, engineers cannot manage firewalls without breaking the management design; that makes the jump host a single point of failure. Second, guest wireless is isolated from internal zones but guests can still reach one another, so an infected guest device could attack other guests' devices. Neither finding breaks a stated requirement, which shows the value of review: it finds weaknesses the requirements themselves did not anticipate.

### 45.3 Responses

Kofi accepts both findings. A second jump host is built at a different office, with the same controls and logging, and engineers test that either can be used to manage every firewall. Client isolation is enabled on the guest wireless network so guest devices can reach the internet but not each other. Both changes go through the normal change process, are lab tested against the regression suite, and add new tests to it so that the fixes cannot later be undone silently. The responses are small, but they close real gaps.

### 45.4 Record

Every finding, the response, the date it was closed and the evidence of closure are entered in a review log that goes into the dossier. Rejected suggestions are recorded too, with reasons. The log shows examiners that the design was tested by someone outside the project and that criticism changed it. It also gives future reviewers a starting point, so they can see what was already examined and concentrate on new areas rather than repeating the same review. Unrecorded reviews lose most of their value once the reviewer has left.

### Preparing material for a reviewer

A useful review needs good material. Kofi prepares a review pack containing the architecture overview, the zone model, the needed-flows list, the policy template, the traceability table and a summary of test results, together with a short list of questions he wants answered, such as whether the management design is robust. He gives the reviewer read-only lab access rather than production access. The pack is limited to around forty pages so the reviewer can read it properly in the time available. Asking specific questions focuses the review on areas where Kofi is least certain of his own judgement.

### Handling disagreement

Not every review comment must be accepted. The reviewer also suggests moving voice into the staff zone to simplify the policy. Kofi disagrees, because the phone provider requires separate quality-of-service treatment and voice handsets have limited security features, so separation reduces risk. He records the suggestion, his reasoning and the evidence, and Dr Vasquez agrees. A clear record of rejected suggestions shows that each comment was considered seriously, and lets a future reviewer reopen the question if circumstances change, such as replacing the handsets with devices that support stronger controls and simpler management.

### Second review after changes

After implementing the accepted findings, Kofi asks the same reviewer for a short follow-up check. The reviewer confirms that the second jump host fails over correctly in the lab and that guest client isolation works on both wireless controller models used by the council. This closes the review loop with evidence rather than a statement that changes were made. The follow-up takes the reviewer about two hours, a small cost compared with the value of independent confirmation. Both reviews are included in the dossier with dates, the reviewer's role and a summary of findings and responses.

### Worked example

Both changes are completed and regression tested.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Reviews by people involved in the design miss blind spots.

### Exercises

- **EX133 — Jump host finding.** What was the jump host finding? *Rubric:* 3 = single point of failure;; 2 = availability;; 1 = none;; 0 = none.
- **EX134 — Client isolation.** What does client isolation add? *Rubric:* 3 = guests cannot reach each other;; 2 = isolation;; 1 = none;; 0 = none.
- **EX135 — Independence.** Why use a reviewer from another council? *Rubric:* 3 = fresh perspective;; 2 = independent;; 1 = none;; 0 = none.

### Synthesis

Independent review strengthens the design.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete implementation; (2) measure outcomes; (3) compare with criteria.

### 46.1 Completion

By the end of the capstone, all eight offices are migrated to the six-zone model behind their own firewalls, the CCTV supplier reaches cameras only through the jump hosts, and the three offices with funded second links have redundant tunnels. Kofi checks completion against the original scope rather than declaring it done when work slows: each office has a signed-off migration record, a passing regression run and an entry in the operational routines. Two minor items, a label update and a diagram correction, are listed as open with owners.

### 46.2 Measures

The measured outcomes are: reachable zone pairs down from thirty to seven; unexpected denies settled at around four per week across all offices; VPN availability of 99.97 percent over three months; added latency within the one-millisecond budget in both lab and live measurements; and a change failure rate of four percent. Each figure is linked to its source data in the dossier, so a reader can check how it was produced. Reporting the measures with their sources matters more than the numbers themselves, which would be unconvincing without them.

### 46.3 Criteria comparison

Kofi compares each result against the criteria agreed before measurement. Guest isolation is verified in both the lab and production. All eight requirements have passing evidence in the traceability table. Availability of 99.97 percent exceeds the 99.9 percent target. Latency is within budget. All four criteria are met. He presents this as a simple table with the criterion, the target, the result and a link to evidence, avoiding persuasive language, so the comparison speaks for itself and examiners can verify each line independently.

### 46.4 Limitations

Meeting the criteria does not make the results universal. The availability figure covers only three months, which may not include rare events such as a long provider outage. The project involved one council, so results may differ in organisations with different sizes, suppliers or skills. Some measurements, like the incident reconstruction, were possible only in the lab. Kofi states each limitation next to the result it affects rather than in a separate section that readers might skip, which helps readers judge how far the findings can be trusted and applied elsewhere.

### Interpreting the availability figure

VPN availability of 99.97 percent over three months means total outage across all offices of roughly forty minutes per office over the period. Most of that came from a single provider fault at one branch before its second link was installed. Since the three offices with second links had no measurable outage, Kofi reports availability separately for single-link and dual-link sites. Averaging across all offices would hide the difference that the project's investment made. He also notes that one provider fault in a short period is not enough to estimate long-term availability accurately for any single site.

### Unintended effects

Evaluation should look for effects nobody planned. Kofi checks service desk categories before and after migration. Tickets about network access rose briefly in the first week at each office, then fell below the old level, partly because clearer zone documentation helped staff and engineers understand where devices belonged. One unintended negative effect appears: a few staff began using personal mobile hotspots to reach blocked services. Kofi recommends a clear request process for new flows and a short communication explaining why certain connections are blocked, since workarounds of this kind undermine the controls the project built.

### Cost against outcome

The council spent money on firewalls, second links, staff time and Kofi's placement. He presents costs alongside outcomes: the reduction in reachable paths, the blocked incident scenario, improved availability at dual-link sites and the new ability to detect and investigate internal traffic. He avoids putting a speculative monetary value on avoided incidents, instead noting the cost and disruption of the original guest malware incident as a reference point. Decision makers can then judge whether the outcomes justify the expense, and which elements, such as second links at further offices, are worth extending in future budgets.

### Worked example

The outcome table is added to the dossier.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Short measurement periods can overstate availability.

### Exercises

- **EX136 — Reachability outcome.** State the reachability outcome. *Rubric:* 3 = 30 to 7;; 2 = reduced;; 1 = none;; 0 = none.
- **EX137 — Availability limit.** Why is three months a limitation? *Rubric:* 3 = short period may overstate;; 2 = short;; 1 = none;; 0 = none.
- **EX138 — Criteria met.** Were all criteria met? *Rubric:* 3 = yes with evidence;; 2 = yes;; 1 = none;; 0 = none.

### Synthesis

The capstone meets its criteria within stated limits.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a live recovery trial; (2) measure recovery; (3) learn.

### 47.1 Trial

To prove the recovery plan works outside the lab, Kofi and the council engineers carry out a live trial: with change board approval, they replace a working branch firewall with the spare during a weekend window when the office is closed. The trial follows the recovery runbook exactly, as if the original firewall had failed, and a second engineer watches for any step that is unclear or missing. Running a recovery for real, rather than discussing it, is the only reliable way to know how long it takes.

### 47.2 Measurement

The target, set in the resilience design, is to restore service at a branch within four hours of deciding to replace its firewall. Timing starts when the old unit is disconnected and stops when the regression tests for that office pass on the new one. The trial takes two hours and fifty minutes, comfortably inside the target. Kofi also records how long the office would have been without central services, and confirms that the office's local fallback arrangements would have covered that period.

### 47.3 Issues

The trial finds one significant issue: the spare firewall was running firmware two versions older than production, and updating it added thirty minutes. The quarterly update of the spare had been missed during a busy period. In a real outage, those thirty minutes might matter. The team adds the spare's firmware check to the monthly routine checklist, not just the quarterly one, and adds a step to the runbook to check the firmware version first. Finding this during a planned trial is far better than finding it during a real failure.

### 47.4 Lessons

After the trial, the team holds a short review. The runbook is updated with the firmware check, a clearer step for loading the per-site configuration and a realistic time estimate for each stage. The trial report records the timeline, the issue and the changes made, and goes into the dossier as evidence for the recovery requirement. The council agrees to repeat a recovery trial each year, rotating among engineers, so that recovery skills and spare equipment both stay ready rather than decaying between rare real failures.

### Planning the trial safely

A live trial changes a working office, so it needs careful planning. Kofi writes a plan with the scope, the window, the success measure, the rollback step and the people involved. The office manager is informed, and the trial is scheduled for a weekend when the office is closed. The original firewall is kept powered off but connected and ready, so rollback takes minutes. The council's change advisory board approves the plan. A stop condition is defined in advance: if the replacement is not passing traffic within three hours, the original is restored and the trial is recorded as incomplete.

### Recording the timeline

During the trial, one engineer acts as recorder and notes the time of each step: start, old unit removed, spare connected, configuration loaded, firmware updated, tunnels established, tests passed and finish. The timeline shows exactly where time went. Loading the configuration from backup took eight minutes; the firmware update took thirty; tunnel establishment took four. Without the timeline, the team would only know the total and might guess wrongly about which step to improve. The recorded timeline becomes part of the updated runbook as a realistic estimate for future replacements at any branch office.

### Extending the trial programme

One successful trial does not prove every recovery path. Kofi proposes an annual programme: replacing a branch firewall from spare, restoring the main firewall pair configuration from backup in the lab, recovering the jump hosts and rebuilding a VPN tunnel with a new certificate. Each trial rotates among engineers so that recovery knowledge is not held by one person. Results are reviewed against targets, and runbooks are updated after each trial. Regular trials also keep spares, backups and certificates in a known good state, since problems such as outdated firmware are found before a real failure rather than during one.

### Worked example

The trial report is filed.

> **Synthetic case.** The trial is synthetic.

### Errors and limits

Recovery plans untested in reality often miss small but time-consuming steps.

### Exercises

- **EX139 — Trial time.** How long did recovery take? *Rubric:* 3 = 2h50 within 4h;; 2 = under 4h;; 1 = none;; 0 = none.
- **EX140 — Firmware issue.** What issue slowed recovery? *Rubric:* 3 = old firmware on spare;; 2 = firmware;; 1 = none;; 0 = none.
- **EX141 — Approval.** Why was approval needed? *Rubric:* 3 = live service change;; 2 = policy;; 1 = none;; 0 = none.

### Synthesis

A live trial proves recovery works and improves the runbook.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence; (2) organise for examiners; (3) protect sensitive details.

### 48.1 Contents

The evidence dossier gathers everything that supports the thesis claims: the requirements and their rationale, the traceability table, lab and production test results, measurements of reachability, denies, availability and latency, the independent review log, the recovery trial report and the decision records. Kofi includes failures and their fixes, not only final passing results. A dossier is different from an appendix of everything produced; each item is included because a specific claim in the thesis depends on it, and anything not supporting a claim is left out.

### 48.2 Organisation

Examiners have limited time, so the dossier is organised for finding things quickly. The index is arranged by requirement and by thesis chapter, so a reader checking a claim can go straight to its evidence. Every item has a short identifier used in the thesis text, such as T-R1-03 for the third test of requirement R1. Items are grouped into folders by type, and a one-page guide explains the structure. Good organisation also helps the council, which will reuse the dossier for audits long after the thesis is examined.

### 48.3 Sensitivity

Real network details could help an attacker, and real names and device identifiers are personal or confidential data. Before the dossier leaves the council, Kofi replaces internal addresses with synthetic ranges, replaces device and staff names with codes, and removes supplier account details. He keeps a mapping only on council systems, so the council can relate the sanitised dossier to real devices if needed. He checks every file, including images and log extracts, because sensitive details often hide in screenshots and examples rather than main text.

### 48.4 Approval

The council's information governance officer and network lead review the sanitised dossier and formally approve it for release to the examiners. This approval protects the council and Kofi: nobody can later claim that sensitive information was shared without permission. The approval, with date and names, is recorded in the dossier itself. Seeking approval also catches mistakes; in this case the reviewers spot one diagram still showing a real building name, which is replaced before release. Release controls are a normal part of professional work with partner data.

### Writing evidence summaries

Each dossier entry has a short summary on top: what the evidence is, which requirement or claim it supports, when it was produced, which configuration version it relates to and what it shows. An examiner can read the summaries to understand the evidence base without opening every file. Kofi writes summaries in plain language and states results directly, including failures that were later fixed. For example, the entry for the misordered rule rollback records the failure, the fix and the new template check. Including corrected failures shows the process worked, which is more convincing than a dossier containing only passing results.

### Integrity of the dossier

Evidence must be trustworthy. Kofi stores test outputs, measurements and configuration versions in version control, where each change is recorded with a date and author. Exported reports include a checksum so any later alteration can be detected. Raw data supporting summaries is kept, so examiners can check that a figure such as the 76.7 percent reduction can be recalculated from the underlying zone data. He avoids editing results after the fact; if an error is found, a correction is added as a new dated entry rather than replacing the original, preserving the history of what was known when.

### Reuse beyond the thesis

The dossier is designed to outlive the thesis. The council can use it as the baseline for future audits, as onboarding material for new engineers and as evidence for its cyber assurance submissions. Kofi organises it so these uses are easy: a council version omits academic discussion, while the thesis version includes it. Neighbouring councils interested in similar work can be given the synthetic, sanitised version. Building the dossier with these audiences in mind from the start avoids rework and increases the long-term value of the effort the council invested in the project.

### Worked example

The dossier index has 64 entries.

> **Synthetic case.** The dossier is synthetic.

### Errors and limits

Unindexed evidence is hard for examiners to use.

### Exercises

- **EX142 — Dossier contents.** List four dossier items. *Rubric:* 3 = four;; 2 = three;; 1 = fewer;; 0 = none.
- **EX143 — Sensitivity.** How are sensitive details protected? *Rubric:* 3 = synthetic replacements;; 2 = removed;; 1 = none;; 0 = none.
- **EX144 — Council approval.** Why does the council approve it? *Rubric:* 3 = confirm no sensitive data;; 2 = permission;; 1 = none;; 0 = none.

### Synthesis

An organised dossier supports the thesis claims.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write the thesis; (2) structure arguments; (3) state limits.

### 49.1 Structure

The thesis follows the engineering lifecycle so readers can see how each stage led to the next: the problem and context; requirements; analysis of threats and options; the chosen design; implementation and migration; verification and validation; evaluation against criteria; and discussion with conclusions. Each chapter opens by stating what it contributes and closes with what the next chapter takes from it. This structure lets a reader start with the problem and follow a continuous argument, rather than meeting a collection of separate reports.

### 49.2 Argument

A thesis is an argument, not a diary. Kofi's central claim is that a small public body can substantially reduce internal exposure with modest, verified segmentation without harming service. Every supporting claim in the thesis refers to evidence in the dossier by identifier, so readers can check it. Where evidence is weaker, such as the small research sample, he uses careful language and explains why. He removes sections that describe work but support no claim, which shortens the thesis and makes the argument easier to follow.

### 49.3 Limits

Dr Vasquez asks Kofi to make limits clearer, and he gathers them into a dedicated section as well as noting them beside affected results. The main limits are: a single council as the setting; a three-month availability period; a research sample of eight offices; and some evidence available only from lab tests. For each, he explains how it might affect the conclusions and what would reduce it. Clear limits make the thesis more credible, because readers trust authors who show they understand the weaknesses of their own evidence.

### 49.4 Contribution

Kofi states his contribution plainly: a documented, verified approach to segmenting a small, multi-site public-sector network, including the zone model, templated policy, migration method, test suite and evidence structure, together with measured outcomes from one real deployment. He does not claim new theory. Engineering theses often contribute by showing that known principles can be applied successfully under real constraints, and by documenting the method well enough that others can reuse it. Being precise about the contribution prevents examiners from judging the thesis against claims it never made.

### Writing the discussion chapter

The discussion chapter interprets results rather than repeating them. Kofi asks what the results mean for the council, for similar small public bodies and for practice more broadly. He compares his outcomes with expectations from the literature, such as the value of segmentation in limiting lateral movement described in NIST guidance and the link between policy complexity and errors. Where results differ from expectations, he offers explanations and notes which ones the evidence supports. He also discusses alternatives he did not choose, explaining when those alternatives might be better, so readers in different situations can adapt the approach.

### Citing sources accurately

Every factual claim from outside the project cites a source, and every source is checked. Kofi cites NIST special publications, RFCs and peer-reviewed papers, confirming each title, number and year against the original document. He avoids citing summaries or blog posts when the original standard is available. When a source makes a weaker claim than he wants to make, he either softens his own claim or finds stronger evidence. Accurate citation lets examiners verify claims and shows respect for the work of others, and it protects the thesis from errors copied through secondary sources.

### Future work

A good thesis ends with clear future work. Kofi lists four directions: a longer availability study across all offices once second links are complete; a larger study of whether early unexpected denies predict complaints, pooling data from neighbouring councils; evaluation of stronger device authentication on the staff network to reduce reliance on network location; and assessment of whether finer segmentation within the server zone is worthwhile. Each item states why it matters and what data would be needed. Future work shows that the author understands the limits of what was done and where the next valuable questions lie.

### Worked example

Dr Vasquez reviews drafts and asks for clearer limits.

> **Synthetic case.** The thesis is synthetic.

### Errors and limits

Claims without evidence weaken the thesis.

### Exercises

- **EX145 — Thesis structure.** List the seven parts. *Rubric:* 3 = seven;; 2 = five;; 1 = fewer;; 0 = none.
- **EX146 — Contribution.** State the contribution. *Rubric:* 3 = documented verified approach;; 2 = design;; 1 = none;; 0 = none.
- **EX147 — Limits.** Name two limits. *Rubric:* 3 = two;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

The thesis presents a verified engineering contribution with honest limits.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present the thesis; (2) answer questions; (3) reflect.

### 50.1 Presentation

The defense opens with a thirty-minute presentation. Kofi covers the problem, the design, the evidence, the limits and the contribution, using a few clear figures: the zone diagram, the reachable-pairs reduction, the traceability table and the criteria comparison. He avoids reading slides and does not try to show everything, since the examiners have read the thesis. The aim is to remind them of the argument and show that he understands it well enough to explain it simply. He keeps detailed figures on backup slides for questions.

### 50.2 Questions

The examiners then ask questions for about an hour. They probe three areas: whether the design really applies zero trust ideas or only uses the term; whether the approach would scale to a much larger organisation; and how much risk remains in the flows the policy still permits. Good examiners ask questions to test understanding, not to trap the candidate. Kofi listens to each question fully, asks for clarification when a question is ambiguous, and takes a moment to think before answering rather than rushing.

### 50.3 Answers

On zero trust, Kofi explains that the design applies some principles from NIST SP 800-207, such as reducing implicit trust between zones and controlling management access tightly, but does not authenticate every request per user and device, so it is a step towards zero trust rather than a full implementation. On scale, he points to the template approach and notes where larger organisations would need automation. On residual risk, he explains that permitted flows remain exposed and are managed by host controls, patching and monitoring of allowed traffic.

### 50.4 Reflection

At the end, the examiners ask what Kofi would do differently. He answers that he would involve the council's staff representatives and governance officer even earlier, and would build the traceability table from the first week rather than partway through. He reflects that the hardest parts of the project were not technical: securing time from busy engineers, winning budget, and agreeing how logs could be used. The examiners accept the thesis. His reflection, recorded in the final chapter, is that secure networks depend on people and process as much as on equipment.

### Preparing for the defense

Kofi prepares by listing likely questions and practising answers with his peers and Dr Vasquez in a mock defense. He reviews the weakest parts of the thesis, such as the small research sample and short availability period, and prepares honest answers that state the limit, explain its effect and describe how it could be addressed. He prepares backup slides with detailed figures, used only if asked. The mock defense reveals that his explanation of the traceability table is too fast, so he simplifies it. Preparation reduces anxiety and helps him answer clearly rather than defensively.

### Handling difficult questions

One examiner asks whether the project simply moved risk into the permitted flows. Kofi agrees that permitted flows still carry risk and explains how it is managed: flows are limited to named services, host controls and patching protect servers, and monitoring watches permitted traffic for unusual volume. He acknowledges that segmentation reduces but does not remove risk. When asked a question he cannot fully answer, about long-term costs of certificate management, he says so, gives his best estimate and explains how the council could measure it. Honest answers of this kind build examiners' confidence.

### Looking back on the route

The defense closes a five-year path that began with networking basics and ended with a verified design for a real organisation. Kofi notes how each stage contributed: foundations in addressing and protocols made the subnet plan possible, earlier work on monitoring shaped the logging design, and practice with requirements and testing gave the evidence that convinced examiners. He also recognises the role of the council engineers, who now own and run the network. The final lesson he records is that secure networks depend on clear requirements, simple designs, evidence and the people who maintain them.

### Worked example

The thesis is accepted.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

Defensive answers undermine strong work.

### Exercises

- **EX148 — Zero trust answer.** How does Kofi describe zero trust? *Rubric:* 3 = principles applied, not full;; 2 = partial;; 1 = none;; 0 = none.
- **EX149 — Scaling answer.** How does the design scale? *Rubric:* 3 = templates;; 2 = easily;; 1 = none;; 0 = none.
- **EX150 — Reflection.** State Kofi's reflection. *Rubric:* 3 = governance and people mattered;; 2 = stated;; 1 = none;; 0 = none.

### Synthesis

The defense closes a five-year route from foundations to verified engineering.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Kofi Mensah, Dr Elena Vasquez, Ravenmoor Institute of Technology, Ashcombe District Council and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** B'(t) = 5 + 2t, so 13 GB per hour at t = 4.

**EX002.** In simple queue models waiting time is proportional to 1/(1−ρ), which grows without bound as ρ approaches 1.

**EX003.** If inspection lowers the service rate below peak arrival rate, queues and delay grow at busy times.

**EX004.** A \ N: flows allowed but not needed.

**EX005.** Adds a→c, a→d and b→d.

**EX006.** 8 × 7 = 56.

**EX007.** 120 / 200 = 0.6 ms.

**EX008.** People outside can attempt to join or capture traffic, so strong authentication and encryption are needed.

**EX009.** Lock cabinets and disable unused switch ports.

**EX010.** ipaddress.ip_address("192.168.5.9") in ipaddress.ip_network("192.168.5.0/24")

**EX011.** A /32 network and an input list with overlapping networks.

**EX012.** It is tested and handles corner cases that manual code often gets wrong.

**EX013.** The problem, the proposal and the decision or cost needed.

**EX014.** They answer different questions; combining them makes both hard to read.

**EX015.** Readers can challenge one judgement without rejecting the whole analysis.

**EX016.** 3 × 8 = 24 GB.

**EX017.** 180 GB before compression, plus headroom.

**EX018.** Revise the model using the measured data.

**EX019.** 7.2 failures per year.

**EX020.** About 0.19.

**EX021.** Links sharing a duct can fail together after one excavation.

**EX022.** Each new connection needs rule evaluation on the slower path.

**EX023.** New connections may be refused or old entries evicted.

**EX024.** Datasheets assume ideal traffic, and load grows.

**EX025.** Parsing, policy evaluation and reporting.

**EX026.** Skipping them could omit rules and give wrong conclusions.

**EX027.** The line number and the problematic content.

**EX028.** Decline and route it to the authorised network team.

**EX029.** So service can be restored quickly if the change fails.

**EX030.** Social care staff unable to access case records during visits.

**EX031.** 126.

**EX032.** It leaves room to grow and keeps rules aligned.

**EX033.** TLS protects at the application/transport boundary; firewall rules act at network and transport layers.

**EX034.** They still protect hosts if a network rule is wrong.

**EX035.** Only from the management zone.

**EX036.** Firewalls disabled temporarily may be left off.

**EX037.** Time, source zone, destination zone, port, action, bytes.

**EX038.** Queries are simpler and fewer personal details are stored.

**EX039.** Raw records are deleted; aggregated summaries are kept.

**EX040.** History, review and rollback.

**EX041.** guest→servers:443 must be denied.

**EX042.** They only check the cases that were written.

**EX043.** TLS 1.3 (RFC 8446) or IPsec (RFC 4301).

**EX044.** It protects data in transit but does not restrict which hosts can connect.

**EX045.** Lateral malware spread, eavesdropping on links, misconfiguration.

**EX046.** Guest devices cannot initiate connections to any internal zone.

**EX047.** Requirements without tests or design elements.

**EX048.** The CCTV supplier's remote maintenance connection.

**EX049.** Low thresholds cause noise; high ones miss real issues.

**EX050.** Requiring a condition to persist five minutes before acting.

**EX051.** They shorten the decide and act steps.

**EX052.** A zone groups systems of similar trust; a conduit is the controlled path between zones, such as staff to servers over HTTPS.

**EX053.** It applies some zero trust principles but still relies on network zones, so the label would overstate it.

**EX054.** Fewer zones are easier to operate and verify, and complex policies are more error-prone (Wool, 2004).

**EX055.** Each device can be revoked individually, and there is no shared password to leak or reuse.

**EX056.** NIST SP 800-77 Rev. 1 with RFC 7296 for IPsec; SP 800-52 Rev. 2 with RFC 8446 for TLS.

**EX057.** It leaves time to renew and deploy before the expiry causes an outage.

**EX058.** It provides an entry point into the network that bypasses the edge firewall's controls.

**EX059.** The design must be operable by two engineers without specialist tuning.

**EX060.** Reachable zone pairs, unexpected denied flows, VPN availability, added latency, change failure rate.

**EX061.** Inter-office VPNs use IKEv2 with certificate authentication.

**EX062.** Without them, the design may work at launch but fail in operation or investigations.

**EX063.** Test: trigger a failover and time recovery.

**EX064.** From 30 to 7, a 76.7 percent reduction.

**EX065.** It can reach four other zones for administration.

**EX066.** To confirm no indirect path connects guest to internal zones.

**EX067.** A compromised staff laptop using permitted file-sharing access to servers.

**EX068.** All branch offices lose access to central services.

**EX069.** Through host controls and monitoring, and documented as residual risk.

**EX070.** Old rules may contain errors and excess access that would be carried over.

**EX071.** Place specific rules before general ones.

**EX072.** Identifier, owner and reason.

**EX073.** Cameras then reach the recorder without crossing a zone boundary.

**EX074.** A narrow rule from staff to the recorder's viewing service.

**EX075.** It surfaces issues before implementation, when changes are cheap.

**EX076.** The main office becomes a single dependency and branch traffic must travel there.

**EX077.** Dependence on internet links and a new operational skill set.

**EX078.** So the scoring reflects what the council values most.

**EX079.** Four of eight.

**EX080.** Remote desktop administration is restricted to the management zone.

**EX081.** Logging every allow on busy links would overwhelm storage.

**EX082.** It records what would be denied without blocking traffic.

**EX083.** Printer scans to file share and phones fetching provider configuration.

**EX084.** After a week with no unexpected denies in monitor mode.

**EX085.** 118 of 173.

**EX086.** Cameras attempting to send email alerts.

**EX087.** Most reflect configuration or habits, not malicious activity.

**EX088.** Testing connections in production without approval could disrupt services and exceed authorisation.

**EX089.** Date, configuration version, expected, actual.

**EX090.** A rule allowing management to cameras on an unnecessary port.

**EX091.** NIST SP 800-77 Rev. 1.

**EX092.** Via the jump host using named, time-limited accounts.

**EX093.** Abrupt changes can break maintenance obligations.

**EX094.** 0.005 × 8760 = 43.8 hours.

**EX095.** 0.999975 availability, about 0.22 hours a year.

**EX096.** Different providers and physical paths.

**EX097.** Branches continue local services while phones fall back to mobile.

**EX098.** The out-of-hours line depended on the main office.

**EX099.** Four hours from configuration backups.

**EX100.** Syslog (RFC 5424).

**EX101.** Tunnel down, certificate expiry, deny spikes.

**EX102.** To recognise and route segmentation-related problems.

**EX103.** Without an expiry and owner, they remain long after the need passes, widening access.

**EX104.** A dedicated printer reachable from guest only for printing, with the temporary rule removed.

**EX105.** It keeps the management zone free of direct internet access while allowing updates.

**EX106.** Yes; the maximum is 0.95 ms and p95 about 0.92 ms, close to the budget.

**EX107.** A burst of new connections when backups started; staggering start times.

**EX108.** Larger rule bases tend to have more errors, so growth should prompt review.

**EX109.** Unexpected denies by zone pair, certificates expiring within 60 days, configuration drift.

**EX110.** A silent logging failure would leave monitoring blind without anyone noticing.

**EX111.** Rare pages are taken seriously; frequent ones lead to ignored alerts.

**EX112.** Six of eight covered; R5 and R8 untested; R6 pending.

**EX113.** Restore yesterday's configuration backup to the lab firewall and confirm it loads correctly.

**EX114.** It checks whether real needs are met, not whether requirements are satisfied.

**EX115.** Architecture overview, zone model, needed-flows list, runbooks, decision records.

**EX116.** The council engineers led the final migrations while he observed.

**EX117.** An engineer from another team added a subnet using only the documentation.

**EX118.** All attempts were denied and logged, and an alert arrived within two minutes.

**EX119.** Disable a tunnel, power off the active firewall, expire a test certificate.

**EX120.** Testing such behaviour on production could disrupt services and exceed authorisation.

**EX121.** By running the regression test suite.

**EX122.** Summarising allowed flows while keeping full records for denies and management access.

**EX123.** Grouping by source and raising the guest zone's threshold.

**EX124.** Whether unexpected denies after migration predict later service complaints.

**EX125.** Only as suggestive, given eight offices.

**EX126.** Investigate offices with many unexpected denies first.

**EX127.** Logs relate to staff activity, so consultation protects trust and privacy.

**EX128.** Public procurement takes weeks and can delay installation.

**EX129.** Councils must account publicly for spending and data handling.

**EX130.** Guest isolation verified, all requirements evidenced, availability above 99.9%, latency within budget.

**EX131.** Criteria set after results could be chosen to fit them.

**EX132.** Procurement delays for second links.

**EX133.** The jump host was a single point of failure for management access.

**EX134.** Guest devices cannot connect to one another.

**EX135.** They bring an independent view without design bias.

**EX136.** From 30 to 7 reachable zone pairs.

**EX137.** A short period may not include rare failures.

**EX138.** Yes, all criteria were met.

**EX139.** Two hours fifty minutes.

**EX140.** The spare's firmware was out of date.

**EX141.** It changed a live office's network.

**EX142.** Requirements, trace, test results, decision records.

**EX143.** Real addresses and names are replaced with synthetic values.

**EX144.** To confirm nothing sensitive is disclosed.

**EX145.** Problem, requirements, design, implementation, verification, evaluation, discussion.

**EX146.** A documented, verified segmentation approach for small public bodies.

**EX147.** One council and a short measurement period.

**EX148.** The design applies zero trust principles but is not full zero trust.

**EX149.** Through policy templates with per-site values.

**EX150.** Governance and people mattered as much as technology.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Barker, E., Dang, Q., Frankel, S., Scarfone, K., & Wouters, P. (2020). *Guide to IPsec VPNs* (NIST SP 800-77 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-77r1>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Chandramouli, R., & Rose, S. (2013). *Secure Domain Name System (DNS) deployment guide* (NIST SP 800-81-2). NIST. <https://doi.org/10.6028/NIST.SP.800-81-2>
- Claise, B., Trammell, B., & Aitken, P. (2013). *Specification of the IP Flow Information Export (IPFIX) protocol* (RFC 7011). IETF. <https://www.rfc-editor.org/rfc/rfc7011>
- Ferguson, P., & Senie, D. (2000). *Network ingress filtering* (RFC 2827, BCP 38). IETF. <https://www.rfc-editor.org/rfc/rfc2827>
- Gerhards, R. (2009). *The Syslog protocol* (RFC 5424). IETF. <https://www.rfc-editor.org/rfc/rfc5424>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kaufman, C., Hoffman, P., Nir, Y., Eronen, P., & Kivinen, T. (2014). *Internet Key Exchange Protocol Version 2 (IKEv2)* (RFC 7296). IETF. <https://www.rfc-editor.org/rfc/rfc7296>
- Kent, S., & Seo, K. (2005). *Security architecture for the Internet Protocol* (RFC 4301). IETF. <https://www.rfc-editor.org/rfc/rfc4301>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lepinski, M., & Kent, S. (2012). *An infrastructure to support secure Internet routing* (RFC 6480). IETF. <https://www.rfc-editor.org/rfc/rfc6480>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Paxson, V. (1999). Bro: A system for detecting network intruders in real-time. *Computer Networks*, 31(23–24), 2435–2463. <https://doi.org/10.1016/S1389-1286(99)00112-7>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., & Hoffman, P. (2009). *Guidelines on firewalls and firewall policy* (NIST SP 800-41 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-41r1>
- Scarfone, K., & Mell, P. (2007). *Guide to intrusion detection and prevention systems (IDPS)* (NIST SP 800-94). NIST. <https://doi.org/10.6028/NIST.SP.800-94>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *2010 IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Souppaya, M., & Scarfone, K. (2012). *Guidelines for securing wireless local area networks (WLANs)* (NIST SP 800-153). NIST. <https://doi.org/10.6028/NIST.SP.800-153>
- Sriram, K., & Montgomery, D. (2019). *Resilient interdomain traffic exchange: BGP security and DDoS mitigation* (NIST SP 800-189). NIST. <https://doi.org/10.6028/NIST.SP.800-189>
- Wool, A. (2004). A quantitative study of firewall configuration errors. *Computer*, 37(6), 62–67. <https://doi.org/10.1109/MC.2004.2>
