# Network and Communications Security: Bachelor's Course

- Language: English (`en`); course 103, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Five offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students who need a complete grounding in network and communications security, from foundations through an evidenced capstone with a small partner organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student from mathematical, computing and ethical foundations through addressing, logging, cryptography and research methods, to designing, testing and deploying segmentation, secure wireless, VPNs and logging for a group of small clinics, then evaluating the result and presenting a thesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priya Nair** | Bachelor's student | Invented |
| **Dr Tomasz Kowal** | Supervisor | Invented |
| **Northbridge University** | Fictional university | Invented |
| **Harbourside Community Clinics** | Fictional partner (four clinics) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use logic and sets to state network rules precisely; (2) reason with powers of two; (3) check claims with counterexamples.

### 1.1 Why precision matters

Priya Nair begins her bachelor's degree at the fictional Northbridge University and, in her first week, hears about the fictional Harbourside Community Clinics, four small clinics sharing one wireless passphrase for staff, visitors and medical carts. A tutor asks the class to write down, exactly, who should be able to reach what. Most first attempts are vague, such as "visitors should not see patient systems". Mathematical reasoning gives tools to make such statements precise enough to check, and precision is the first habit of network security, because a rule that can be read two ways will eventually be configured the wrong way.

### 1.2 Sets and membership

A set is a collection of distinct items, and much of network security is about membership. The set of clinic devices can be split into subsets: staff laptops, clinical carts, visitor phones and network equipment. A rule such as "no visitor device may reach any clinical device" becomes a statement about pairs drawn from two sets. Union, intersection and complement let Priya ask useful questions: which devices are in both the staff and clinical sets, which devices belong to no planned set, and whether the sets together cover every device seen on the network.

### 1.3 Powers of two

Computers count in binary, so network sizes come in powers of two. An address block with eight host bits holds two to the power eight, 256 addresses; seven bits hold 128; four bits hold 16. Each extra bit doubles the size, and each bit removed halves it. Priya practises moving between bit counts and sizes until it is automatic, because later she must size subnets for each clinic group. A common mistake is to treat sizes as decimal round numbers, asking for a block of 100 or 200, when only powers of two are possible.

### 1.4 Counterexamples

A general claim, such as "every visitor device is on the guest network", is disproved by a single counterexample: one visitor phone found on the staff network. Priya learns that security claims are usually universal, about all devices or all paths, so testing them means searching for counterexamples rather than collecting confirming cases. A hundred visitor phones correctly placed do not prove the claim; one misplaced phone disproves it. This idea returns throughout the course, in testing firewall rules, reviewing configurations and evaluating whether a control works.

### Worked example

Priya writes the clinic rule as: for every device d in Visitors and every device c in Clinical, d cannot open a connection to c. She then lists what evidence would be a counterexample.

> **Synthetic case.** The clinics and devices are synthetic.

### Errors and limits

Informal language such as "usually" or "should" hides exceptions; precise statements make exceptions visible.

### Exercises

- **EX001 — Universal claim test.** What single observation would disprove "no visitor device reaches clinical devices"? *Rubric:* 3 = one visitor device successfully connecting to a clinical device, explained as a counterexample to a universal claim;; 2 = a visitor connecting;; 1 = mentions testing without a specific observation;; 0 = none.
- **EX002 — Bits to size.** How many addresses does a block with six host bits contain? *Rubric:* 3 = 64, from two to the power six, with the doubling rule explained;; 2 = 64;; 1 = a guess near 64 without method;; 0 = none.
- **EX003 — Unplanned devices.** Using set language, describe devices that belong to no planned group. *Rubric:* 3 = the complement of the union of planned sets, needing investigation;; 2 = devices outside all groups;; 1 = lists one device;; 0 = none.

### Synthesis

Sets, powers of two and counterexamples turn vague security wishes into precise, checkable statements.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe how hosts send data; (2) explain addresses at each layer; (3) identify where controls can act.

### 2.1 From application to wire

When a clinic receptionist opens the booking system, several layers cooperate. The application forms a request, the transport layer splits it into segments and adds port numbers, the network layer adds source and destination IP addresses, and the link layer frames it for the local network with hardware addresses. At the destination, each layer removes its header and passes the data up. Priya draws this as a stack because each layer is a place where a control can act: an application can check users, the network layer can filter addresses, and the link layer can separate local segments.

### 2.2 Addresses and names

Devices are identified in several ways at once. A hardware address identifies a network card on the local segment; an IP address identifies a host across networks; a port identifies a service on that host; a name such as booking.clinic.example is translated to an address by DNS. Each identifier has different strength. Hardware addresses can be changed by software, IP addresses can be reassigned, and names depend on DNS answers being correct. Knowing which identifier a control relies on tells Priya how easily it might be confused or misled.

### 2.3 Shared media and switching

Older networks used shared media where every device heard every frame. Modern switches send frames only to the port of the destination, but wireless networks are shared again: every device on a channel can receive the radio signal. Encryption on the wireless link protects frames from outsiders, but devices that share the same network and key can still talk to one another. This explains part of the clinics' problem. With one passphrase for everyone, visitor phones are on the same local network as clinical carts, separated by nothing except good luck.

### 2.4 Where controls sit

Priya maps possible controls onto the clinic network: separate wireless networks and virtual LANs at the link layer, a firewall between them at the network layer, encryption with TLS at the transport layer, and user authentication in applications. No single layer is enough. A firewall cannot tell which person is using a laptop, and an application login does nothing to stop an infected visitor phone scanning other devices nearby. Thinking in layers helps her see gaps where one control is assumed to cover something it cannot see.

### Worked example

Priya traces a booking request and marks the four identifiers involved: hardware address, IP address, port 443 and the booking system's name.

> **Synthetic case.** Systems and names are synthetic.

### Errors and limits

Assuming one layer's control protects another layer leaves gaps, such as relying on logins to stop local network attacks.

### Exercises

- **EX004 — Shared passphrase effect.** What does one shared wireless passphrase mean for visitor phones and clinical carts? *Rubric:* 3 = same local network, able to reach each other, encryption protects only from outsiders;; 2 = same network;; 1 = mentions passwords only;; 0 = none.
- **EX005 — Identifier strength.** Why is a hardware address a weak basis for trust? *Rubric:* 3 = software can change it, only meaningful locally;; 2 = can be changed;; 1 = says it is unique;; 0 = none.
- **EX006 — Layer gaps.** Give one threat an application login does not address. *Rubric:* 3 = infected device scanning neighbours at network level;; 2 = network attacks;; 1 = vague;; 0 = none.

### Synthesis

Layers explain how data moves and where each kind of control can act.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small stdlib Python scripts; (2) handle input carefully; (3) produce readable output.

### 3.1 Why security students program

Priya will analyse logs, check configurations and test rules, and doing these by hand is slow and error-prone. Short scripts make checks repeatable: the same script run next month gives comparable results. The course uses only the Python standard library so labs run anywhere without installing packages, and every lab uses synthetic data invented for teaching. Programming here is a tool for careful reasoning, not an end in itself, and the scripts are short enough to read in full, which matters because a script nobody understands cannot be trusted to support a conclusion.

### 3.2 Data structures for networks

Python's built-in structures map well to network data. A list holds rules in order, which matters because firewalls apply the first matching rule. A dictionary maps names to addresses or zones to subnets. A set holds unique items, such as the distinct devices seen in a log, and supports the union and intersection reasoning from chapter 1. A tuple holds a fixed record, such as source, destination and port. Choosing the right structure makes code simpler and errors less likely, for example using a set when duplicates must not be counted twice.

### 3.3 Handling bad input

Real data contains mistakes: truncated log lines, misspelled zone names, addresses with extra spaces. A script that crashes on the first bad line gives no result, and one that silently skips bad lines can give a misleading result. Priya learns to count and report malformed input separately, so a reader can see how much data was ignored. She also validates values, such as checking that a port is between 0 and 65535, before using them. Careful input handling is a security habit as well as a programming one, since attackers often rely on software mishandling unexpected input.

### 3.4 Readable output

Output should answer a question clearly. Priya's scripts print aligned columns with headers, end with a summary line, and state units such as percentages or counts. She avoids printing thousands of lines when a total and a short list of exceptions would do. Readable output helps the clinic's small IT team, who are not programmers, use the results. It also helps reviewers: a summary line such as "3 of 8 below minimum" can be checked against the listed rows, which makes errors in the script easier to notice.

### Worked example

Priya writes a script that reads synthetic device records, skips and counts two malformed lines, and prints a table of devices by group with a final count.

> **Synthetic case.** All data are synthetic.

### Errors and limits

Scripts that silently drop bad input can produce confident but wrong summaries.

### Exercises

- **EX007 — Ordered rules structure.** Which Python structure suits firewall rules, and why? *Rubric:* 3 = list, because order decides first match;; 2 = list;; 1 = dictionary without reason;; 0 = none.
- **EX008 — Malformed line handling.** How should a script treat malformed log lines? *Rubric:* 3 = count and report them separately, not crash or silently skip;; 2 = skip them;; 1 = ignore;; 0 = none.
- **EX009 — Port validation.** What range should a port value be checked against? *Rubric:* 3 = 0 to 65535, rejecting values outside;; 2 = 0-65535;; 1 = up to 1024;; 0 = none.

### Synthesis

Small, readable stdlib scripts make security checks repeatable and reviewable.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear technical prose; (2) cite sources accurately; (3) structure a short report.

### 4.1 Writing for a reader

Priya's first assignment is a two-page report on wireless risks at a small clinic. Her tutor explains that technical writing serves a reader with limited time: state the main point first, then the evidence, then the detail. Each paragraph should make one point, and each sentence should be easy to follow on first reading. Jargon is defined the first time it appears or avoided. A clinic manager reading the report should understand the risk and the recommendation from the first paragraph, even if they skip the rest.

### 4.2 Citing sources

Claims that come from others must be cited, and citations must be accurate. Priya cites NIST SP 800-153, the guidelines for securing wireless local area networks, when describing separation of wireless networks, and checks the title, number and year against the document itself. She learns to prefer primary sources, such as standards and peer-reviewed papers, over summaries. A citation lets readers check a claim, so a wrong number or title wastes their time and damages the writer's credibility. Every citation in this course comes from the verified reference list.

### 4.3 Report structure

A short technical report usually contains a summary, background, findings, recommendations and references. Findings state what was observed with evidence; recommendations state what should change, who should do it and why. Priya keeps findings and opinions separate: "visitor phones joined the same network as clinical carts" is a finding, while "this is unacceptable" is an opinion that needs justification. This separation lets readers accept the evidence even if they weigh the risk differently, and it makes the report easier to act on.

### 4.4 Revising

First drafts are rarely clear. Priya revises by reading the report aloud, cutting sentences that repeat earlier points, and checking that each recommendation follows from a finding. She asks a classmate to summarise the report after one reading; if the summary differs from her intended main point, the report needs work. Revision takes as long as drafting, but it is where most of the improvement happens. Good writing matters in security because recommendations that are not understood are not acted on, however correct they are.

### Worked example

Priya's revised summary reads: "All four clinics use one wireless network for visitors, staff and clinical devices. We recommend separate networks for each group, starting with visitors."

> **Synthetic case.** The report and clinics are synthetic.

### Errors and limits

Citations copied from other documents without checking often contain errors.

### Exercises

- **EX010 — Finding versus opinion.** Classify "the clinic's wireless design is dangerous" and rewrite it as a finding. *Rubric:* 3 = opinion; rewritten as an observed fact with evidence;; 2 = opinion;; 1 = rewrites without classifying;; 0 = none.
- **EX011 — Primary source preference.** Why prefer a NIST publication to a blog summary of it? *Rubric:* 3 = primary, accurate, checkable;; 2 = more reliable;; 1 = vague;; 0 = none.
- **EX012 — Summary test.** How can a classmate help test a report's clarity? *Rubric:* 3 = summarise after one read, compare with intended point;; 2 = read it;; 1 = proofread;; 0 = none.

### Synthesis

Clear structure, accurate citations and revision make technical writing useful to its readers.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain confidentiality, integrity and availability; (2) identify assets and threats; (3) relate controls to risks.

### 5.1 The three goals

Security is often described through three goals. Confidentiality means information is seen only by those allowed to see it, such as patient records seen only by clinical staff. Integrity means information and systems are not changed improperly, such as test results not altered in transit. Availability means systems work when needed, such as the booking system during opening hours. Priya notices that the goals can conflict: locking down the network might protect confidentiality but harm availability if a needed connection is blocked, so security decisions involve balancing them.

### 5.2 Assets and threats

An asset is something of value: patient data, the booking system, clinical carts, the clinic's reputation. A threat is something that could harm an asset: malware on a visitor phone, a staff member's stolen password, a failed network switch. A vulnerability is a weakness a threat could exploit, such as a shared wireless network or an outdated protocol. Listing assets first keeps attention on what matters to the clinics. Without that, security work tends to focus on interesting technical issues rather than the ones that would actually hurt patients or staff.

### 5.3 Risk

Risk combines how likely a harmful event is with how much harm it would cause. A visitor phone infected with malware is fairly likely in a busy waiting room; the harm if it reaches clinical carts could be serious. A switch failure is less likely and causes disruption rather than data loss. Priya rates risks roughly as high, medium or low, recognising that precise numbers are rarely available for small organisations. The value of the exercise is in comparing risks consistently so that limited money and staff time go to the most important ones first.

### 5.4 Controls

A control reduces risk by lowering likelihood or harm. Separating visitor wireless from clinical devices reduces the likelihood that malware spreads to them. Backups reduce the harm of data loss. Logging does not prevent harm but helps detect and investigate it. Controls are often grouped as preventive, detective and corrective. Priya learns that good designs combine all three, because no preventive control is perfect, and detection and recovery limit the damage when prevention fails. The CIS Controls offer a prioritised list of such safeguards for organisations of different sizes.

### Worked example

Priya builds a small risk table for the clinics with five rows; the shared wireless network is rated high likelihood and high impact and placed first.

> **Synthetic case.** The risk table is synthetic.

### Errors and limits

Rating risks without first listing assets tends to over-weight technical issues and miss business impact.

### Exercises

- **EX013 — Goal conflict.** Give an example where confidentiality and availability conflict at the clinics. *Rubric:* 3 = strict blocking protects data but blocks a needed service;; 2 = blocking;; 1 = defines terms only;; 0 = none.
- **EX014 — Control types.** Classify central logging as preventive, detective or corrective. *Rubric:* 3 = detective, explaining it finds rather than stops;; 2 = detective;; 1 = preventive;; 0 = none.
- **EX015 — Threat versus vulnerability.** Distinguish the threat from the vulnerability in "malware on a visitor phone spreads over the shared network". *Rubric:* 3 = threat malware phone; vulnerability shared network;; 2 = one correct;; 1 = confuses;; 0 = none.

### Synthesis

Assets, threats, vulnerabilities, risk and controls form the basic vocabulary of security decisions.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) model networks as graphs; (2) reason about paths and reachability; (3) use relations for policy.

### 6.1 Networks as graphs

A graph has nodes connected by edges, and it is a natural model for networks. Priya draws the clinic network with devices and network groups as nodes and permitted connections as edges. Questions about security then become questions about graphs: can a visitor phone reach a clinical cart by any path, how many steps does it take, and which single edge would disconnect them if removed? Graph thinking moves attention from individual rules to the overall shape of what can reach what, which is often where design problems become obvious.

### 6.2 Directed edges and reachability

Network connections usually have a direction: a staff laptop may open a connection to the booking server, but the server should not open connections to laptops. Directed graphs capture this. Reachability means there is some path following the arrows from one node to another, possibly through intermediate nodes. Priya learns that removing a direct edge is not enough if an indirect path remains; for example, a visitor phone blocked from the clinical network might still reach it through a shared printer that both groups can use. Reachability must be checked over all paths.

### 6.3 Relations and policy

A relation is a set of ordered pairs, and a firewall policy can be described as a relation between source groups and destination services. Properties of relations help reasoning. A policy that is not symmetric allows connections one way only. A transitive closure computes everything reachable through any number of hops, which matches the reachability question above. Writing the policy as a relation lets Priya compare the intended policy with the configured one as two sets of pairs and list exactly the pairs that differ.

### 6.4 Counting paths and pairs

With four groups, there are twelve ordered pairs of different groups. Priya counts how many are needed for clinic work and finds only four: staff to booking, clinical to lab results, staff and clinical to the internet. The shared wireless network effectively allows all twelve. Counting the difference between what is allowed and what is needed gives a simple measure of excess access, which she will use later to show how much a redesign reduces exposure, in the same way that larger projects count reachable zone pairs.

### Worked example

Priya's graph shows that removing the visitor-to-clinical edge still leaves a path through the shared printer, so the printer must be moved or restricted.

> **Synthetic case.** The graph is synthetic.

### Errors and limits

Checking only direct rules misses indirect paths through shared devices.

### Exercises

- **EX016 — Indirect path.** Why is removing a direct edge not always enough? *Rubric:* 3 = indirect path via shared node remains;; 2 = other paths;; 1 = says it is enough;; 0 = none.
- **EX017 — Ordered pairs count.** How many ordered pairs of distinct groups exist with four groups? *Rubric:* 3 = twelve, four times three;; 2 = 12;; 1 = 16;; 0 = none.
- **EX018 — Excess access measure.** How can excess access be measured simply? *Rubric:* 3 = allowed pairs minus needed pairs;; 2 = compare;; 1 = vague;; 0 = none.

### Synthesis

Graphs and relations let network policies be checked for reachability and excess access.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain IP addressing and subnets; (2) use CIDR notation; (3) check device placement with a script.

### 7.1 IP addresses and prefixes

An IPv4 address has 32 bits, usually written as four decimal numbers. CIDR notation, such as 10.20.1.0/25, gives a network address and the number of bits fixed as the network prefix; the remaining bits identify hosts. A /24 leaves eight host bits, 256 addresses; a /25 leaves seven, 128 addresses. Two addresses in each block are traditionally reserved, for the network itself and broadcast, so a /25 has 126 usable hosts. Private ranges such as 10.0.0.0/8 are used inside organisations and are not routed on the internet.

So the block 10.20.1.0/25 runs from 10.20.1.0 to 10.20.1.127: hosts take .1 to .126, and .127 is the broadcast address.

### 7.2 Planning subnets for groups

Priya proposes one subnet per group for a clinic: staff, clinical devices, guest wireless and network management. Each is sized for current devices plus growth, rounded up to a power of two. Management gets a small /28 because only switches and access points live there. Separate subnets do not by themselves stop traffic, since routers forward between them, but they give each group a distinct address range that firewall rules can refer to, which is the foundation for any segmentation design.

### Lab — Device placement

```python
"""Check which synthetic clinic devices fall inside which planned subnet (stdlib only)."""
import ipaddress
nets = {"staff": "10.20.0.0/24", "clinical": "10.20.1.0/25", "guest": "10.20.2.0/24", "mgmt": "10.20.3.0/28"}
nets = {k: ipaddress.ip_network(v) for k, v in nets.items()}
devices = {"reception-pc": "10.20.0.15", "ecg-cart": "10.20.1.40", "visitor-phone": "10.20.2.77",
           "switch-1": "10.20.3.2", "old-printer": "10.20.1.200", "nurse-tablet": "10.20.0.130"}
for name, a in devices.items():
    ip = ipaddress.ip_address(a); zone = next((z for z, n in nets.items() if ip in n), "UNPLANNED")
    print(f"{name:14}{a:13}{zone}")
for z, n in nets.items(): print(f"{z:9}{str(n):15}usable hosts {n.num_addresses - 2}")
```

Run with `python3 lab_cidr.py`. Verified output:

```text
reception-pc  10.20.0.15   staff
ecg-cart      10.20.1.40   clinical
visitor-phone 10.20.2.77   guest
switch-1      10.20.3.2    mgmt
old-printer   10.20.1.200  UNPLANNED
nurse-tablet  10.20.0.130  staff
staff    10.20.0.0/24   usable hosts 254
clinical 10.20.1.0/25   usable hosts 126
guest    10.20.2.0/24   usable hosts 254
mgmt     10.20.3.0/28   usable hosts 14
```

### 7.3 Reading the result

The script places five of six synthetic devices in their expected groups. The old printer at 10.20.1.200 falls outside every planned subnet, because the clinical /25 ends at 10.20.1.127. This is exactly the kind of counterexample from chapter 1: a single device breaks the claim that every device has a planned home. In a real clinic, such devices are common, often with fixed addresses set years ago. Priya lists it for readdressing rather than widening the clinical subnet to include it, which would quietly enlarge the group.

### 7.4 Protocols and ports

Above IP, TCP provides reliable connections and UDP sends independent datagrams. Services listen on ports: 443 for HTTPS, 53 for DNS, 22 for SSH. Rules refer to protocol and port as well as addresses, so knowing which services each group uses is essential. Priya starts a list of the services the clinics need between groups. This list of needed flows becomes the basis of later policy, and anything not on it is a candidate to block. She records the protocol, port and direction for each entry, with the group that starts the connection.

### Worked example

The lab reports the clinical /25 has 126 usable hosts and finds one unplanned device, the old printer.

> **Synthetic case.** Addresses and devices are synthetic.

### Errors and limits

Widening a subnet to fit a stray device enlarges a group without anyone deciding it should.

### Exercises

- **EX019 — Unplanned printer.** Why is the old printer at 10.20.1.200 unplanned? *Rubric:* 3 = clinical /25 ends at .127, outside all subnets;; 2 = outside range;; 1 = wrong subnet without reason;; 0 = none.
- **EX020 — Usable hosts.** How many usable hosts does a /28 provide? *Rubric:* 3 = 14, sixteen minus network and broadcast;; 2 = 14;; 1 = 16;; 0 = none.
- **EX021 — Stray device fix.** Should the clinical subnet be widened to include the printer? *Rubric:* 3 = no, readdress the device to avoid enlarging the group;; 2 = no;; 1 = yes;; 0 = none.

### Synthesis

CIDR subnets give each group an address range that later controls can rely on.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure larger scripts; (2) test functions; (3) process text records safely.

### 8.1 Functions and structure

As scripts grow, Priya splits them into functions that each do one job: reading input, parsing a line, classifying a record and printing a summary. Small functions are easier to test and reuse. A function that parses a log line, for example, can be tested on a handful of examples, including malformed ones, before it is trusted on a full file. She names functions after what they do, such as parse_line or in_subnet, so the main part of the script reads almost like a description of the analysis.

### 8.2 Testing

A test runs a function on known input and checks the output. Priya writes tests for the subnet check: an address inside the range, one just outside, the network address itself and an invalid address. Edge cases like these catch most mistakes. Python's built-in unittest module or simple assert statements are enough for course labs. Tests are kept with the script, so anyone changing it can rerun them and see whether behaviour changed, which is the same principle as regression testing of firewall rules later in the course.

### 8.3 Regular expressions

Logs and configuration files are text, and regular expressions describe patterns in text, such as a priority number in angle brackets at the start of a syslog line. They are powerful but easy to get wrong: a pattern that is too loose matches lines it should not, and one that is too strict rejects valid lines. Priya anchors patterns to the start of the line where possible, tests them against examples of both valid and invalid input, and keeps them simple enough to read. Complex patterns are split into named parts.

### 8.4 Safety in tools

Security scripts often handle untrusted data, such as logs containing text supplied by users or attackers. Priya never passes such text to a shell or evaluates it as code, and she treats unexpected values as data to be reported, not instructions. She avoids writing to files outside the working directory and does not need network access for any lab. These habits keep analysis tools from becoming a weakness themselves, which matters because tools run with the analyst's permissions and can do harm if misled by crafted input.

### Worked example

Priya's tested in_subnet function passes four cases: inside, just outside, network address and an invalid string that raises a clear error.

> **Synthetic case.** All test data are synthetic.

### Errors and limits

Regular expressions tested only on valid input often accept malformed lines silently.

### Exercises

- **EX022 — Edge case choice.** List three edge cases for testing a subnet membership function. *Rubric:* 3 = inside, just outside, network address or invalid;; 2 = two;; 1 = one;; 0 = none.
- **EX023 — Regex anchoring.** Why anchor a log-parsing pattern to the start of a line? *Rubric:* 3 = prevents matching text embedded elsewhere;; 2 = accuracy;; 1 = speed;; 0 = none.
- **EX024 — Untrusted text rule.** What must never be done with text read from logs? *Rubric:* 3 = pass to shell or evaluate as code;; 2 = run it;; 1 = print it;; 0 = none.

### Synthesis

Functions, tests and careful text handling make analysis scripts trustworthy.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) model network inventory data; (2) query it; (3) keep data accurate and minimal.

### 9.1 Why inventories matter

Priya cannot secure devices she does not know exist. An inventory lists each device with its type, owner, location, network group and address. The CIS Controls place inventory of enterprise assets first for this reason: every later control depends on knowing what is there. At the clinics, the inventory is a spreadsheet last updated two years ago. Comparing it with devices actually seen on the network reveals missing entries, retired devices still listed and devices nobody can identify, each of which needs follow-up.

### 9.2 Tables and keys

A relational database stores data in tables of rows and columns. Priya designs two tables: devices, with a unique identifier, type, owner and group, and addresses, linking device identifiers to IP addresses and dates. A key uniquely identifies each row, and linking tables by keys avoids repeating information. If a device changes address, only the addresses table changes. This structure also records history, which helps investigations ask which device held an address at a given time, a question flat spreadsheets struggle to answer reliably.

### 9.3 Queries

A query asks the database a question, such as "which devices in the guest group have fixed addresses" or "which clinical devices have no named owner". Python's standard library includes sqlite3, so Priya can create a small database file and run SQL queries without a server. She writes queries that answer operational questions rather than dumping all data. Each query result is a list of follow-up actions: devices to readdress, owners to find or records to correct. Queries are saved with the project so the same checks can be rerun each month.

### 9.4 Accuracy and minimisation

Inventory data decays as devices are added and removed, so it needs regular checks against what the network actually sees. It should also contain only what is needed. Recording which staff member uses which laptop is useful for security, but storing personal details beyond a name and role is not. Priya applies data minimisation: each column must have a purpose. Smaller, accurate data is easier to protect and more useful than large stores of stale information, which also carry privacy obligations.

### Worked example

A query finds three clinical devices with no owner and one visitor tablet recorded in the staff group.

> **Synthetic case.** Inventory data are synthetic.

### Errors and limits

An inventory that is never compared with the live network quickly becomes misleading.

### Exercises

- **EX025 — Inventory first.** Why do the CIS Controls put asset inventory first? *Rubric:* 3 = later controls depend on knowing assets;; 2 = foundation;; 1 = vague;; 0 = none.
- **EX026 — Address history.** Why keep address history in a separate table? *Rubric:* 3 = track which device held which address over time;; 2 = history;; 1 = duplication;; 0 = none.
- **EX027 — Minimisation example.** Give one column that would breach data minimisation in a device inventory. *Rubric:* 3 = unnecessary personal detail such as home address;; 2 = personal data;; 1 = owner name;; 0 = none.

### Synthesis

Accurate, minimal inventories are the base for every later network control.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) identify ethical duties; (2) work only with authorisation; (3) handle sensitive data responsibly.

### 10.1 Authorisation first

Security students learn about weaknesses, and that knowledge carries responsibility. Priya's course is clear: testing or examining any network requires written permission from its owner, defining scope, time and methods. Without permission, even well-meant checks can be illegal and can disrupt services. When the clinics later agree to work with Northbridge, the agreement states exactly what Priya may review, mostly configurations and logs provided by the clinic team, and states that she will not run tests against live clinical systems.

### 10.2 Professional codes

Professional bodies publish codes of ethics that emphasise avoiding harm, honesty, respecting privacy and working within one's competence. Priya reads her university's code and notes how it applies: she should report findings honestly even when they are embarrassing for the partner, avoid claiming expertise she lacks, and protect information she sees. Codes do not answer every question, but they give a starting point when a situation is unclear and a shared standard that others can hold her to. When unsure, she asks her supervisor before acting rather than after.

### 10.3 Sensitive data

Clinic networks carry health information, which is among the most sensitive personal data. Even logs can reveal it: a device name may include a patient room, and timing of connections can reveal appointments. Priya works only with sanitised data where names and identifiers are replaced, stores it on encrypted university storage and deletes it at the end of the project as agreed. She never copies data to personal devices. These steps are part of the agreement and are checked by her supervisor, Dr Tomasz Kowal.

### 10.4 Reporting problems

If Priya notices a serious weakness, she reports it promptly to the clinic's IT lead through the agreed channel, not to classmates or online. If she makes a mistake, such as accessing a file outside scope, she reports it immediately. Honest reporting builds trust and lets the partner act. Concealing problems, even small ones, damages trust and can leave patients and staff exposed. The course treats prompt, private, honest reporting as a core skill, not an optional courtesy. Reports state facts, evidence and suggested next steps, without speculation.

### Worked example

Priya's project agreement lists permitted activities, data handling rules, a reporting contact and an end date for data deletion.

> **Synthetic case.** The agreement is synthetic.

### Errors and limits

Assuming permission because a system is easy to reach is a common and serious error.

### Exercises

- **EX028 — Agreement contents.** List three things a project agreement should state. *Rubric:* 3 = scope, data handling, reporting contact or end date;; 2 = two;; 1 = one;; 0 = none.
- **EX029 — Out-of-scope mistake.** What should Priya do if she accidentally opens an out-of-scope file? *Rubric:* 3 = report immediately to the agreed contact;; 2 = tell someone;; 1 = ignore;; 0 = none.
- **EX030 — Hidden health data.** How can network logs reveal health information? *Rubric:* 3 = device names, connection timing linked to patients;; 2 = names;; 1 = they cannot;; 0 = none.

### Synthesis

Authorisation, honesty and careful data handling come before any technical work.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain how operating systems use the network; (2) manage host firewalls; (3) apply updates.

### 11.1 Network stacks in the host

Every device's operating system contains a network stack that sends and receives packets, manages connections and exposes services through listening ports. A clinic laptop might listen for file sharing, remote assistance and printer discovery without anyone choosing those services. Priya learns to list listening services on her own lab machine using built-in tools, and to ask of each one whether it is needed. Services that listen on the network are entry points, so turning off unneeded ones reduces exposure without any change to the network itself.

### 11.2 Host firewalls

Most operating systems include a host firewall that filters traffic to and from that device. It complements network firewalls: a network firewall separates groups, while a host firewall protects a device even from others in the same group. At the clinics, enabling host firewalls on clinical carts to accept connections only from the lab results server would limit damage if another clinical device were infected. Host firewalls must be managed centrally, though, since configuring dozens of devices by hand leads to inconsistent settings that nobody can verify.

### 11.3 Updates and patching

Operating systems and network software receive security updates that fix vulnerabilities. Delays in applying them leave known weaknesses open, and attackers often target flaws that have had fixes available for months. Priya studies the clinics' update practice and finds laptops update automatically but clinical carts are updated only when a supplier visits. She notes that devices which cannot be updated quickly are exactly those that most need network separation, because the network becomes their main protection while patches wait. She recommends a written schedule agreed with the supplier, with remote updates where possible.

### 11.4 Least functionality

The principle of least functionality says a system should provide only the capabilities it needs. For a clinical cart, that might mean one application, one outbound connection to the lab results server and no file sharing or remote desktop. Removing unneeded functions reduces both the chances of a vulnerability and the work of keeping things patched. Priya connects this to Saltzer and Schroeder's classic design principles, especially economy of mechanism and least privilege, which argue that simpler systems with fewer privileges are easier to make secure.

### Worked example

Priya's check of a synthetic clinical cart lists five listening services; only one is needed, and the others are recommended for removal.

> **Synthetic case.** Device data are synthetic.

### Errors and limits

Disabling a service without checking dependencies can break clinical workflows; confirm with the device owner first.

### Exercises

- **EX031 — Host versus network firewall.** What does a host firewall add beyond a network firewall? *Rubric:* 3 = protection within the same group or segment;; 2 = device-level;; 1 = duplicates;; 0 = none.
- **EX032 — Unpatched devices.** Why do slow-to-patch devices most need separation? *Rubric:* 3 = network is main protection while patches wait;; 2 = exposure;; 1 = vague;; 0 = none.
- **EX033 — Least functionality link.** Which classic design principles support least functionality? *Rubric:* 3 = economy of mechanism and least privilege (Saltzer and Schroeder);; 2 = least privilege;; 1 = none named;; 0 = none.

### Synthesis

Host services, firewalls and updates complement network controls and shrink each device's exposure.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) describe data with summary statistics; (2) reason about rates and base rates; (3) avoid common errors.

### 12.1 Describing data

Network data are often skewed: most connections are small and short, a few are very large. In such data, the mean can mislead, because a single large transfer drags it upwards. Priya learns to report the median, which is the middle value, together with percentiles such as the 95th, which show the tail. For example, describing daily denied connections at a clinic, she reports a median of 40 and a 95th percentile of 180, which tells the reader both the usual level and how high bad days go.

### 12.2 Rates and comparisons

Counts are hard to compare when groups differ in size. A clinic with 60 staff will produce more alerts than one with 15, without being less secure. Rates, such as alerts per 100 devices per week, allow fair comparison. Priya also learns to compare against a baseline from the same place over time, since changes from normal are often more informative than absolute levels. A sudden rise in denied guest connections at one clinic matters more than a steady high level that has always been there.

### 12.3 Base rates

When a detector looks for rare events, even a small false alarm rate produces many false alarms. If one connection in ten thousand is malicious and a detector flags one percent of normal connections, almost all flagged connections are harmless. This is the base-rate problem described by Axelsson in his 2000 paper on intrusion detection. Priya works through the numbers by hand and sees why alert volume alone says little about whether a detector is useful, and why tuning thresholds is a constant part of network monitoring.

### 12.4 Common errors

Priya lists errors to avoid: treating correlation as cause, generalising from one clinic to all, ignoring missing data, and reporting precise-looking percentages from tiny samples. Saying "75 percent of devices were misplaced" sounds serious until the reader learns there were four devices. She reports sample sizes alongside every percentage. These habits are basic, but many security reports break them, and readers who make decisions based on such reports can be misled into spending money on the wrong problems. She also asks a classmate to check her figures before submission.

### Worked example

With 10,000 connections, 1 malicious, a detector catching it and flagging 1% of the rest raises about 101 alerts, of which 1 is real.

> **Synthetic case.** Numbers are synthetic.

### Errors and limits

Percentages without sample sizes can make small findings look large.

### Exercises

- **EX034 — Median choice.** Why report the median rather than the mean for connection sizes? *Rubric:* 3 = skew; mean pulled by large values;; 2 = skew;; 1 = preference;; 0 = none.
- **EX035 — Base-rate arithmetic.** With 1 malicious in 10,000 and 1% false alarms, roughly how many alerts are real? *Rubric:* 3 = about 1 of 101, explained;; 2 = about 1;; 1 = most;; 0 = none.
- **EX036 — Fair comparison.** How should alert counts be compared between clinics of different size? *Rubric:* 3 = rates per devices or staff per period;; 2 = rates;; 1 = raw counts;; 0 = none.

### Synthesis

Robust summaries, rates and base-rate awareness prevent misleading conclusions from network data.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) distinguish authentication and authorisation; (2) design network access by identity; (3) manage accounts.

### 13.1 Authentication and authorisation

Authentication establishes who someone is, usually by password plus another factor; authorisation decides what they may do. At the clinics, the shared wireless passphrase authenticates nobody: anyone who knows it, including former staff and visitors who saw it on a whiteboard, is treated the same. Priya explains that network access should depend on identity, so that staff, clinical devices and visitors receive different access, and that leaving staff can be removed without changing a secret shared by everyone else. Authorisation can then be granted per group rather than to everyone at once.

### 13.2 Individual credentials for staff

Enterprise wireless modes let each staff member authenticate with their own account, checked against a central directory. When someone leaves, disabling their account removes their wireless access as well, and logs record which account connected, which helps investigations. NIST SP 800-153 recommends strong authentication for wireless clients for these reasons. For visitors, a separate guest network with a regularly changed passphrase or a simple registration page is enough, since guests receive only internet access. The guest network is also kept entirely separate from internal zones, so a leaked guest passphrase exposes nothing internal.

### 13.3 Devices without users

Clinical carts and printers cannot type passwords. They are authenticated using device certificates or, where unsupported, placed on a restricted network that allows only their specific connections. Priya notes that device identity based only on hardware addresses is weak, as chapter 2 explained, so restricted networks for such devices must assume they could be impersonated and limit what they can reach accordingly. This is defence in depth: the network does not fully trust a device it cannot strongly identify. Their allowed destinations are listed explicitly in the needed-flows list.

### 13.4 Account lifecycle

Accounts must be created when people join, changed when roles change and removed when they leave. Priya finds three accounts at the clinics belonging to staff who left more than a year ago. She recommends a monthly review comparing accounts with the staff list from human resources, with any differences investigated. Administrator accounts receive special attention: they should be separate from everyday accounts, used only when needed and protected with a second factor, since misuse of them could change the network itself.

### Worked example

Priya's design gives staff individual wireless accounts, clinical carts a restricted network, visitors a guest network and administrators separate protected accounts.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

A shared secret known by many people cannot be revoked for one person without changing it for all.

### Exercises

- **EX037 — Shared passphrase weakness.** Why can't a shared passphrase remove one leaver's access? *Rubric:* 3 = everyone shares it; changing affects all;; 2 = shared;; 1 = vague;; 0 = none.
- **EX038 — Device identity.** How should devices that cannot use passwords be handled? *Rubric:* 3 = certificates or restricted network limiting reach;; 2 = restricted;; 1 = ignore;; 0 = none.
- **EX039 — Stale accounts.** What process catches accounts of former staff? *Rubric:* 3 = monthly comparison with HR staff list;; 2 = review;; 1 = vague;; 0 = none.

### Synthesis

Identity-based access lets the network treat people and devices differently and revoke access individually.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) apply privacy principles to network data; (2) minimise collection; (3) set retention.

### 14.1 Privacy and security

Privacy concerns how personal information is collected, used and shared; security protects information from unauthorised access. They overlap but differ. A perfectly secure log store can still violate privacy if it collects more than needed or is used to watch staff for purposes they were not told about. At the clinics, network logs show when staff devices connect, which could reveal working patterns. Priya learns that security monitoring must itself respect privacy, or it loses staff trust and may break the law.

### 14.2 Purpose and minimisation

Collection should have a stated purpose, and only data needed for that purpose should be collected. For security monitoring, Priya specifies the purpose as detecting and investigating threats to clinic systems. That justifies recording connection source, destination, time and decision, but not the content of web pages visited by staff. Data minimisation reduces the harm if logs are leaked and simplifies compliance. It also improves analysis, since smaller, focused data are easier to search than large volumes of irrelevant detail.

### 14.3 Retention

Data should be kept only as long as needed. Security logs are useful for investigating incidents, which may be discovered weeks after they start, so a retention period of around ninety days is common for small organisations. Keeping logs for years increases risk and storage cost with little extra security benefit. Priya recommends ninety days for connection logs, with longer retention only for records of administrative changes, and an automatic deletion job so retention happens without anyone needing to remember.

### 14.4 Transparency

People should know what is collected about them. Priya drafts a short notice for clinic staff explaining that network connections are logged for security, what is recorded, how long it is kept and who can see it. Visitors using guest wireless see a brief notice on the registration page. Transparency costs little and builds trust. It also constrains use: once the notice says logs are for security, using them to track staff timekeeping would break that promise and should be refused.

### Worked example

Priya's logging specification records five fields for connections, sets ninety days' retention and includes a staff notice.

> **Synthetic case.** Specification is synthetic.

### Errors and limits

Monitoring introduced without notice often damages trust even when its purpose is legitimate.

### Exercises

- **EX040 — Content logging.** Why should connection logs not record web page content? *Rubric:* 3 = beyond security purpose, privacy harm;; 2 = unnecessary;; 1 = storage;; 0 = none.
- **EX041 — Retention choice.** Justify a ninety-day retention period. *Rubric:* 3 = incidents found weeks later, longer adds risk;; 2 = investigation;; 1 = arbitrary;; 0 = none.
- **EX042 — Purpose limit.** What should happen if a manager wants logs to check staff punctuality? *Rubric:* 3 = refuse; outside stated security purpose;; 2 = refuse;; 1 = allow;; 0 = none.

### Synthesis

Purpose, minimisation, retention and transparency keep security monitoring respectful of privacy.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) define measurable security indicators; (2) collect evidence reliably; (3) interpret change.

### 15.1 What to measure

Security is hard to measure directly, so practitioners use indicators that relate to it. Priya chooses indicators for the clinics: the number of group pairs that can reach each other, the share of devices with a known owner, the share of servers using current TLS versions and the number of denied guest-to-internal connections per week. Each indicator links to a risk from her table. Indicators should be cheap to collect, understandable to managers and hard to improve without actually improving security.

### 15.2 Reliable evidence

Evidence is reliable if someone else could collect it again and get the same result. Priya documents each measurement: the data source, the date range, the script used and its version. She keeps raw data for the project's duration, so figures can be rechecked. Screenshots and verbal reports are weak evidence because they cannot be repeated. This discipline matters most when results are surprising, since a surprising result that cannot be reproduced is likely to be challenged, and rightly so.

### 15.3 Before and after

To show that a change helped, Priya measures before and after, under similar conditions. If denied guest connections fall after separating networks, she checks that guest usage did not simply fall at the same time, perhaps because of a holiday. Comparing rates rather than counts helps, as does measuring for several weeks either side of the change. Without this care, normal variation can be mistaken for an effect, and money can be spent repeating a change that did nothing. She also notes any other changes made during the same period.

### 15.4 Gaming indicators

Any indicator can be improved in ways that do not help security. If the indicator is "number of open alerts", closing alerts without investigating them improves it. Priya pairs indicators so that gaming one shows in another: open alerts alongside a sample review of closed alerts. She also explains each indicator's purpose to the people measured by it. Indicators work best as information for improvement, not as targets with rewards attached, which tends to encourage gaming. She reviews the indicator set each term and retires indicators that have stopped being useful.

### Worked example

Priya's indicator sheet lists four indicators, each with source, script, frequency and linked risk.

> **Synthetic case.** Indicators are synthetic.

### Errors and limits

Comparing a single week before and after a change confuses normal variation with effect.

### Exercises

- **EX043 — Indicator qualities.** Name three qualities of a good security indicator. *Rubric:* 3 = cheap, understandable, hard to game or linked to risk;; 2 = two;; 1 = one;; 0 = none.
- **EX044 — Holiday effect.** Why check guest usage when denied guest connections fall? *Rubric:* 3 = fall may reflect fewer guests, not the control;; 2 = other causes;; 1 = vague;; 0 = none.
- **EX045 — Reproducibility record.** What should be recorded for each measurement? *Rubric:* 3 = source, date range, script and version;; 2 = source;; 1 = result only;; 0 = none.

### Synthesis

Well-chosen, reproducible indicators provide evidence that security actually improved.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) apply defence in depth; (2) design zones and boundaries; (3) document architecture.

### 16.1 Defence in depth

No single control is perfect, so security architecture layers controls so that one failing does not expose everything. At the clinics, Priya plans separate wireless networks, a firewall between groups, host firewalls on devices, encrypted connections to servers and central logging. If a visitor device is infected, the guest network separation stops it reaching clinical devices; if separation is misconfigured, host firewalls still limit what it can reach; and logging records the attempts for investigation either way. Each layer is chosen to cover a different failure, not to repeat another layer.

### 16.2 Zones and boundaries

A zone groups devices with similar trust and needs; a boundary between zones is where controls apply. Priya proposes four zones for each clinic: staff, clinical, guest and management. Traffic between zones passes through a firewall that permits only needed flows, following NIST SP 800-41r1 guidance on firewall policy, which recommends denying by default and allowing specific traffic. Within a zone, traffic flows more freely, which is why zones should be kept small and similar in purpose. Each zone's purpose is written in one sentence so new devices can be placed consistently.

### 16.3 Management separation

The devices that run the network, such as switches, access points and the firewall, need their own protected zone. If an attacker reaches a management interface, they can change the network itself, undoing every other control. Priya places management interfaces in a management zone reachable only from a dedicated administrator workstation, with administrator accounts protected by a second factor. This separation is often missing in small organisations, where management pages are reachable from the same network as everyone else. All administrative logins are logged centrally.

### 16.4 Documenting architecture

An architecture document records zones, boundaries, permitted flows and the reasons behind them. Priya includes a diagram, a table of zones with their subnets and a list of needed flows. She writes the reasoning for key choices, such as why clinical devices are separated from staff laptops. Documentation lets others review the design before it is built, and later lets the clinic team understand why a rule exists before changing it, which prevents well-intended changes from weakening the design. The document is reviewed whenever zones or flows change.

### Worked example

Priya's architecture document has a one-page diagram, a four-zone table and eight needed flows between zones.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Zones defined by building location rather than trust and purpose tend to mix devices with very different needs.

### Exercises

- **EX046 — Layer failure.** What still protects clinical devices if guest separation is misconfigured? *Rubric:* 3 = host firewalls and logging;; 2 = host firewall;; 1 = vague;; 0 = none.
- **EX047 — Default deny basis.** Which publication guides default-deny firewall policy here? *Rubric:* 3 = NIST SP 800-41r1;; 2 = NIST;; 1 = vague;; 0 = none.
- **EX048 — Management zone purpose.** Why must management interfaces be in their own zone? *Rubric:* 3 = reaching them allows changing the network, undoing controls;; 2 = protect;; 1 = convenience;; 0 = none.

### Synthesis

Layered controls, purposeful zones and a protected management zone form a resilient architecture.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain encryption, integrity and authentication; (2) describe TLS; (3) audit TLS versions.

### 17.1 What cryptography provides

Cryptography supports three services on networks. Encryption keeps data confidential from those without the key. Integrity checks, such as message authentication codes, detect if data were changed. Authentication, often through certificates and digital signatures, proves who is at the other end. Priya stresses to classmates that cryptography protects data in transit between two endpoints; it does nothing to stop an infected endpoint from misusing data, or a correctly authenticated user from doing something they should not. Knowing these limits prevents encryption from being treated as a complete security solution.

### 17.2 How TLS protects connections

Transport Layer Security protects most web and many other connections. At the start, client and server agree on a protocol version and algorithms, the server proves its identity with a certificate, and they establish shared keys. After that, data are encrypted and integrity-protected. TLS 1.3, described in RFC 8446, simplified this exchange and removed older, weaker options. NIST SP 800-52r2 advises that servers support TLS 1.2 and 1.3 and not older versions, which have known weaknesses. Clients that only support old versions are identified and replaced or isolated rather than allowed to hold back every server.

### Lab — TLS version audit

```python
"""Flag synthetic server TLS settings below a TLS 1.2 minimum, as SP 800-52r2 recommends (stdlib only)."""
servers = [("portal", "TLSv1.3"), ("booking", "TLSv1.2"), ("lab-results", "TLSv1.0"), ("email", "TLSv1.2"),
           ("old-intranet", "TLSv1.1"), ("vpn", "TLSv1.3"), ("pharmacy", "TLSv1.2"), ("printer-ui", "SSLv3")]
rank = {"SSLv3": 0, "TLSv1.0": 1, "TLSv1.1": 2, "TLSv1.2": 3, "TLSv1.3": 4}
weak = [s for s, v in servers if rank[v] < rank["TLSv1.2"]]
for s, v in servers: print(f"{s:13}{v:8}{'FIX' if s in weak else 'ok'}")
print(f"{len(weak)} of {len(servers)} below TLS 1.2 ({100*len(weak)/len(servers):.1f}%)")
```

Run with `python3 lab_tls.py`. Verified output:

```text
portal       TLSv1.3 ok
booking      TLSv1.2 ok
lab-results  TLSv1.0 FIX
email        TLSv1.2 ok
old-intranet TLSv1.1 FIX
vpn          TLSv1.3 ok
pharmacy     TLSv1.2 ok
printer-ui   SSLv3   FIX
3 of 8 below TLS 1.2 (37.5%)
```

### 17.3 Reading the audit

The synthetic inventory shows three of eight services, 37.5 percent, below the TLS 1.2 minimum: the lab results service on TLS 1.0, an old intranet on TLS 1.1 and a printer's web interface on the obsolete SSL 3. The lab results service carries health data and is the priority. The printer interface is likely a device limitation, so the practical fix may be to restrict it to the management zone rather than upgrade it. Priya records each with an owner and a proposed action rather than a generic "upgrade everything".

### 17.4 Keys and certificates

Cryptography is only as strong as its key management. Certificates expire, private keys must be protected and trusted authorities must be chosen carefully. Priya finds the clinic's booking portal certificate expires in three weeks, with nobody assigned to renew it. An expired certificate causes browser warnings that train users to click through warnings, which is worse than the outage itself. She recommends an expiry register with reminders sixty days ahead and a named owner for each certificate. Private keys are stored only on the servers that need them, never emailed.

### Worked example

The audit flags lab-results, old-intranet and printer-ui; the printer is moved to the management zone and the other two are scheduled for upgrade.

> **Synthetic case.** Inventory is synthetic.

### Errors and limits

Encryption on the wire does not protect data on an infected endpoint.

### Exercises

- **EX049 — Audit result.** What share of services fall below TLS 1.2 in the lab? *Rubric:* 3 = 3 of 8, 37.5%, naming them;; 2 = 37.5%;; 1 = some;; 0 = none.
- **EX050 — Printer fix.** Why restrict rather than upgrade the printer interface? *Rubric:* 3 = device limitation; reduce exposure via management zone;; 2 = cannot upgrade;; 1 = ignore;; 0 = none.
- **EX051 — Expiry harm.** Why do expired certificates harm security beyond outages? *Rubric:* 3 = users learn to ignore warnings;; 2 = warnings;; 1 = vague;; 0 = none.

### Synthesis

TLS protects data in transit when versions are current and keys are well managed.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) form answerable questions; (2) choose methods; (3) plan data collection ethically.

### 18.1 Questions that can be answered

Research starts with a question precise enough to answer. "Is the clinic network secure?" cannot be answered; "what share of clinic devices sit outside a planned network group?" can. Priya practises narrowing questions by naming the population, the measure and the time frame. A good question also matters to someone: the clinic team would act on the answer. Her tutor warns that the most common weakness in student projects is a question too broad to answer with the time and data available.

### 18.2 Choosing methods

Different questions need different methods. Counting misplaced devices needs a survey of inventory and network data. Understanding why staff share the wireless passphrase needs interviews. Testing whether a firewall rule blocks traffic needs an experiment in a lab. Priya maps each sub-question to a method and lists what data each needs. Mixing methods is common in applied security research, because technical measurements explain what is happening while interviews explain why people behave as they do. She notes the cost and time of each method so the plan stays realistic for one term.

### 18.3 Sampling

Studying everything is often impossible, so researchers sample. If Priya can review only one week of logs, she should choose a typical week, not one with a holiday or an outage, and state why. If interviewing staff, she should include different roles rather than only those who volunteer first. Biased samples lead to conclusions that do not hold. Stating the sample and how it was chosen lets readers judge how far findings apply to the whole clinic network. She records the sampling rule before collecting data.

### 18.4 Ethics in research

Research involving people or their data needs ethical review. Priya's university requires her to describe what data she will use, how she will protect it, how participants consent to interviews and how findings will be reported without identifying individuals. Using sanitised logs and anonymous interview notes reduces risk. Ethical review sometimes feels like paperwork, but it protects participants and the researcher, and it often improves the study by forcing clearer thinking about purpose and data. Approval must be granted before any data are collected.

### Worked example

Priya narrows her question to "what share of devices seen on clinic networks in one typical week sit outside planned groups?"

> **Synthetic case.** The question is synthetic.

### Errors and limits

Choosing a convenient but unusual sample period can make results unrepresentative.

### Exercises

- **EX052 — Narrowing a question.** Rewrite "is the network secure?" as an answerable question. *Rubric:* 3 = names population, measure and time frame;; 2 = narrower;; 1 = still vague;; 0 = none.
- **EX053 — Interview need.** Why use interviews alongside log analysis? *Rubric:* 3 = explain why people act, not just what;; 2 = reasons;; 1 = unnecessary;; 0 = none.
- **EX054 — Sample bias example.** Give one way a log sample could be biased. *Rubric:* 3 = unusual week such as holiday or outage;; 2 = bad week;; 1 = vague;; 0 = none.

### Synthesis

Clear questions, matched methods, fair samples and ethical review make research credible.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Network and communications security: scope and theory

### Learning outcomes

You will (1) define the field's scope; (2) explain key models; (3) relate theory to clinic problems.

### 19.1 Scope of the field

Network and communications security protects data as it moves between systems and protects the networks that carry it. It covers segmentation and firewalls, secure protocols such as TLS and IPsec, wireless security, monitoring and detection, and the processes that keep these working. It overlaps with host security and identity, but its focus is on paths: who can reach what, how data are protected in transit, and how unusual traffic is noticed. Priya maps each clinic problem to this scope to see which belong to her project.

### 19.2 Trust and boundaries

Classic network designs trusted everything inside the perimeter and filtered only at the internet edge. The clinic network follows this model: once on the wireless network, any device can reach any other. Experience showed that attackers who get inside one device can then move freely. Modern thinking, summarised in NIST SP 800-207 on zero trust architecture, reduces implicit trust: access decisions consider identity and device state, and internal traffic is controlled as carefully as external traffic. For the clinics, this means treating the guest network as untrusted even though it sits inside the building.

### 19.3 Prevention, detection and response

Theory also distinguishes stages. Prevention tries to stop harmful traffic, through firewalls and authentication. Detection notices what prevention missed, through logs and intrusion detection systems, as described in NIST SP 800-94. Response contains and recovers, through procedures and backups. Priya realises the clinics have only weak prevention, almost no detection and an informal response process. Her project cannot fix everything, so she aims for meaningful improvement in prevention and basic detection. She writes a one-page response checklist as a first step, naming who to call and which devices to disconnect in an emergency.

### 19.4 Theory meets constraints

Theory describes ideal designs, but small organisations have limited staff, budgets and skills. The clinics have one part-time IT lead. Full zero trust is unrealistic, but applying its principles partially, such as separating zones and authenticating staff individually, is achievable. Priya learns that good practitioners adapt theory to constraints honestly, choosing the improvements that most reduce risk for the effort available and documenting what remains undone, rather than proposing designs nobody can run. Each deferred improvement is listed with its risk so managers can revisit it when resources allow.

### Worked example

Priya's scope statement covers wireless separation, firewall policy, TLS on clinic services and basic logging, excluding endpoint protection.

> **Synthetic case.** Scope is synthetic.

### Errors and limits

Proposing an ideal design without regard to staff capacity produces plans that are never implemented.

### Exercises

- **EX055 — Perimeter weakness.** What weakness of perimeter-only trust does the clinic network show? *Rubric:* 3 = inside devices reach everything;; 2 = internal movement;; 1 = vague;; 0 = none.
- **EX056 — Zero trust realism.** Why apply zero trust principles only partially at the clinics? *Rubric:* 3 = limited staff and budget;; 2 = resources;; 1 = not useful;; 0 = none.
- **EX057 — Detection guidance.** Which NIST publication covers intrusion detection and prevention systems? *Rubric:* 3 = SP 800-94;; 2 = 800-94;; 1 = other;; 0 = none.

### Synthesis

The field focuses on paths and protection in transit; theory guides, but constraints shape what is achievable.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Network and communications security: foundational cases

### Learning outcomes

You will (1) analyse common network incidents; (2) extract lessons; (3) relate cases to the clinics.

### 20.1 Learning from cases

Cases teach how failures happen in practice. Priya studies anonymised, synthetic case summaries prepared by her tutor, each based on common patterns rather than specific events. For each, she asks what happened, which controls were missing or failed, how it was detected and what changed afterwards. The aim is not to memorise incidents but to recognise patterns that recur, so that she can spot them in new settings such as the clinics before they turn into incidents. She records each pattern in a short table she can reuse.

### 20.2 Case: flat network spread

In the first case, a visitor's infected laptop at a small practice joins the shared wireless network. Malware scans the local network, finds a file share on a reception computer and encrypts its files. With no separation and no logging, the practice notices only when staff cannot open documents. The lessons are separation of visitor devices, host firewalls on shared computers and basic logging. Priya notes how closely this matches the clinics' current design, which strengthens her case for change.

### 20.3 Case: forgotten remote access

In the second case, a supplier installed remote access software on a server years ago for maintenance. The account used a weak password and was forgotten when the contract ended. Someone outside the organisation used it to log in. The lesson is that remote access paths must be inventoried, controlled through a known route, protected with strong authentication and removed when no longer needed. Priya adds a question to her clinic review: which suppliers have any form of remote access today?

### 20.4 Case: expired certificate

In the third case, a booking site's certificate expired over a weekend. Users saw warnings and many clicked through; some phoned to complain, and staff told them to ignore warnings. When a genuine fake site appeared later, users were already used to ignoring warnings. The lessons are certificate expiry monitoring and clear messages that warnings must not be ignored. This connects directly to the booking portal certificate Priya found close to expiry. Monitoring expiry dates is cheap compared with the cost of retraining users to trust warnings again.

### Worked example

Priya's case table lists three cases, their missing controls and the matching clinic risk for each.

> **Synthetic case.** All cases are synthetic composites.

### Errors and limits

Treating cases as stories rather than extracting controls leaves no practical lesson.

### Exercises

- **EX058 — Flat spread lessons.** List three controls that would have limited the flat network case. *Rubric:* 3 = separation, host firewall, logging;; 2 = two;; 1 = one;; 0 = none.
- **EX059 — Supplier access question.** What question did the remote access case add to the clinic review? *Rubric:* 3 = which suppliers have remote access now;; 2 = suppliers;; 1 = vague;; 0 = none.
- **EX060 — Warning fatigue.** How did the expired certificate later help a fake site? *Rubric:* 3 = users trained to ignore warnings;; 2 = warnings;; 1 = vague;; 0 = none.

### Synthesis

Common incident patterns reveal which basic controls matter most for small organisations.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Network and communications security: system models

### Learning outcomes

You will (1) model the clinic network as a system; (2) identify flows and dependencies; (3) use the model to reason about change.

### 21.1 A model of the clinics

Priya builds a model of the clinic network that is simpler than reality but captures what matters for security: four clinics, each with staff, clinical, guest and management groups; a shared booking service hosted by a provider on the internet; a lab results server at the main clinic; and links between clinics over the internet. The model leaves out cable routes and device brands, which do not affect who can reach what. A good model is small enough to reason about in full and detailed enough to answer the questions it was built for.

### 21.2 Flows as the core of the model

The heart of the model is the list of flows: which group starts a connection to which destination, on which service and why. Priya identifies eight needed flows, such as staff to the booking service over HTTPS and clinical carts to the lab results server. Everything else in the model follows from these flows: the firewall rules, the subnets that rules refer to and the logging that records them. If the flows are wrong or incomplete, every later step inherits the error, so she reviews the list with the clinic IT lead and two clinic managers before going further.

### 21.3 Dependencies

Flows depend on supporting services. Staff reaching the booking service by name need DNS; devices obtaining addresses need DHCP; accurate log times need time synchronisation. These supporting flows are easy to forget because nobody thinks of them as applications, yet blocking them breaks everything. Priya adds them to the model explicitly, with notes on which zone provides each service. Forgetting dependencies is one of the most common reasons segmentation projects cause outages on the day they go live. Each supporting service is given an owner and a test.

### 21.4 Reasoning about change

With the model, Priya can ask what happens if something changes before changing it. If the lab results server moves to a cloud provider, which flows change and which rules must follow? If a new clinic opens, which values are new and which stay the same? Answering these on paper is quick and cheap. The model also exposes surprises, such as discovering that the guest network depends on the same DNS server as clinical devices, which would let a busy guest network slow clinical name lookups.

### Worked example

Priya's model lists eight needed flows plus three supporting services, and reveals a shared DNS dependency between guest and clinical groups.

> **Synthetic case.** The model is synthetic.

### Errors and limits

Models that omit supporting services such as DNS and time lead to outages when rules are enforced.

### Exercises

- **EX061 — Model detail choice.** Why does the model omit cable routes and device brands? *Rubric:* 3 = they do not affect reachability questions;; 2 = irrelevant;; 1 = simplify;; 0 = none.
- **EX062 — Forgotten dependency.** Name a supporting service commonly forgotten in segmentation. *Rubric:* 3 = DNS, DHCP or time;; 2 = DNS;; 1 = vague;; 0 = none.
- **EX063 — Shared DNS risk.** Why is a DNS server shared by guest and clinical groups a concern? *Rubric:* 3 = guest load or misuse could affect clinical lookups;; 2 = shared;; 1 = vague;; 0 = none.

### Synthesis

A flow-centred model lets designers reason about security and change before touching the network.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Network and communications security: data and dependencies

### Learning outcomes

You will (1) collect logs in a standard format; (2) parse syslog; (3) summarise events by severity.

### 22.1 Why central logs

Logs record what network devices did: connections allowed and denied, logins, configuration changes and errors. At the clinics, each device keeps its own small log that overwrites itself within days, so evidence disappears before anyone looks. Central logging sends copies to one store where they are kept for the agreed period, searched together and protected from tampering on the devices that produced them. Priya treats central logging as the first detection control, since every later analysis depends on logs existing and being complete.

### 22.2 The syslog format

Many network devices send logs using syslog. RFC 5424 defines a structured format: a priority value in angle brackets, a version number, a timestamp, the host name, the application name and further fields, then the message. The priority combines facility, which indicates the type of source, and severity, from emergency to debug, as facility times eight plus severity. Standard formats let one parser handle many devices. Priya notes that real devices often deviate slightly from the standard, so parsers must cope with variations.

### Lab — Syslog parsing

```python
"""Parse synthetic RFC 5424 syslog lines and count by severity (stdlib only)."""
import re, collections
lines = ["<134>1 2026-03-02T08:00:01Z fw1 filter - - - allow staff->portal",
         "<132>1 2026-03-02T08:00:05Z fw1 filter - - - deny guest->clinical",
         "<132>1 2026-03-02T08:00:06Z fw1 filter - - - deny guest->clinical",
         "<131>1 2026-03-02T08:01:00Z ap3 radius - - - auth failure user n.ortiz",
         "<134>1 2026-03-02T08:02:10Z fw1 filter - - - allow clinical->lab",
         "<130>1 2026-03-02T08:03:00Z fw1 system - - - config changed by admin2",
         "bad line without header",
         "<132>1 2026-03-02T08:04:40Z fw1 filter - - - deny guest->mgmt"]
names = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]
pat = re.compile(r"^<(\d{1,3})>1 (\S+) (\S+) (\S+)")
count, bad = collections.Counter(), 0
for l in lines:
    m = pat.match(l)
    if not m: bad += 1; continue
    pri = int(m.group(1)); count[names[pri % 8]] += 1
for k in names:
    if count[k]: print(f"{k:8}{count[k]}")
print("parsed", sum(count.values()), "malformed", bad)
```

Run with `python3 lab_syslog.py`. Verified output:

```text
crit    1
err     1
warning 3
info    2
parsed 7 malformed 1
```

### 22.3 Reading the summary

The parser reads eight synthetic lines and parses seven, reporting one malformed line rather than crashing or silently skipping it. By severity there are three warnings, all denied guest connections towards clinical and management groups; two informational allowed connections; one error for a failed wireless authentication; and one critical event for a configuration change by an administrator. Priya points out that the critical configuration change and the repeated guest denies are the items worth a human look, while the allowed connections are routine.

### 22.4 Time and completeness

Logs from different devices can only be combined if clocks agree. Priya adds time synchronisation to every device and records times in UTC, converting for display. She also monitors completeness: if a device that normally sends hundreds of lines an hour sends none, either it is quiet or logging has failed. Silent failures are dangerous because they look like calm periods. A simple check comparing each device's hourly count against its usual range catches most of them before an investigation discovers missing evidence.

### Worked example

The lab reports three warnings, one error, one critical and two informational events, with one malformed line.

> **Synthetic case.** Log lines and names are synthetic.

### Errors and limits

Parsing logs without counting malformed lines hides data loss.

### Exercises

- **EX064 — Priority arithmetic.** Which severity does priority 132 represent, and why? *Rubric:* 3 = warning: 132 mod 8 = 4;; 2 = warning;; 1 = guesses;; 0 = none.
- **EX065 — Items to review.** Which parsed events deserve human review first? *Rubric:* 3 = critical config change and guest denies;; 2 = config change;; 1 = all;; 0 = none.
- **EX066 — Silent logging failure.** How can a silent logging failure be detected? *Rubric:* 3 = compare device line counts with usual range;; 2 = monitor volume;; 1 = vague;; 0 = none.

### Synthesis

Standard-format central logs with synchronised time and completeness checks make detection possible.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Network and communications security: methods I

### Learning outcomes

You will (1) gather requirements; (2) analyse threats systematically; (3) prioritise controls.

### 23.1 Requirements from needs

Priya turns clinic needs into security requirements that can be tested. Each requirement states what must be true, not how to achieve it. Her list includes: R1, guest devices cannot reach staff, clinical or management groups; R2, inter-group traffic is denied unless listed as a needed flow; R3, network devices are managed only from the management zone; R4, staff wireless uses individual accounts; R5, clinic services use TLS 1.2 or later; and R6, logs are kept centrally for ninety days. Numbering requirements lets later tests and evidence refer to them exactly.

### 23.2 Threat analysis

A systematic threat analysis asks, for each group and boundary, what could go wrong. Priya walks through the model: an infected visitor phone attempting to reach clinical carts; a former staff member using the shared passphrase from the car park; a supplier's forgotten remote access; an attacker intercepting lab results over an old protocol; a misconfigured rule opening guest to management. For each threat she notes which requirement addresses it. Threats with no matching requirement reveal gaps in the requirement list.

### 23.3 Prioritising

Not everything can be done at once. Priya rates each threat by likelihood and impact using the simple scale from chapter 5, then orders controls by how much risk they remove for their cost. Separating the guest network removes the most risk cheaply and comes first. Individual staff accounts come second. TLS upgrades for lab results come third because they protect sensitive data but depend on the supplier. Central logging is started early because it supports evidence for everything else. She explains the order to managers in one page.

### 23.4 Assumptions

Every analysis rests on assumptions, and stating them lets others check them. Priya assumes the clinics' internet provider links are reliable, that the booking service provider secures its own systems, and that clinical carts cannot be modified by staff. If any assumption is wrong, the priorities might change. She lists them in the design document and asks the IT lead to confirm or correct each one. One assumption proves false: some carts do allow staff to install apps, which raises the risk of infected carts.

### Worked example

The threat table maps five threats to six requirements; the false assumption about carts raises one threat from medium to high.

> **Synthetic case.** The analysis is synthetic.

### Errors and limits

Requirements written as solutions, such as "buy a firewall", cannot be tested and limit design options.

### Exercises

- **EX067 — Requirement form.** Rewrite "install a firewall" as a testable requirement. *Rubric:* 3 = states outcome such as inter-group traffic denied unless listed;; 2 = outcome;; 1 = keeps solution;; 0 = none.
- **EX068 — Gap detection.** How does threat analysis reveal missing requirements? *Rubric:* 3 = threats without matching requirement;; 2 = unmatched threats;; 1 = vague;; 0 = none.
- **EX069 — False assumption effect.** What changed when the cart assumption proved false? *Rubric:* 3 = infected cart risk raised; priorities revisited;; 2 = risk up;; 1 = vague;; 0 = none.

### Synthesis

Testable requirements, systematic threat analysis and stated assumptions guide prioritised controls.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Network and communications security: controls

### Learning outcomes

You will (1) write firewall rules from needed flows; (2) find shadowed and redundant rules; (3) apply default deny.

### 24.1 From flows to rules

A firewall rule names a source, destination, service and action. Priya writes one allow rule for each needed flow, then a final rule denying everything else, following the default-deny approach of NIST SP 800-41r1. Rules are evaluated top to bottom and the first match decides, so order matters. Specific rules belong above general ones. She writes a comment on each rule naming the flow and requirement it serves, which later lets reviewers check that every rule has a reason and every reason has a rule.

### 24.2 Rule order problems

Two common problems arise from order. A shadowed rule can never match because an earlier rule matches all the same traffic with a different action; it looks active but does nothing. A redundant rule matches only traffic that an earlier rule already handles with the same action; it is harmless but adds clutter. Wool's 2004 study of real firewall configurations found such errors common and more frequent in larger rule sets. Finding them by eye is hard, so Priya writes a small checker.

### Lab — Rule audit

```python
"""Find shadowed rules in a synthetic first-match rule list (stdlib only)."""
rules = [(1, "guest", "*", "*", "deny"), (2, "staff", "portal", 443, "allow"), (3, "guest", "portal", 443, "allow"),
         (4, "*", "*", 53, "allow"), (5, "staff", "*", "*", "allow"), (6, "staff", "lab", 443, "allow"),
         (7, "clinical", "lab", 443, "allow"), (8, "*", "*", "*", "deny")]
def covers(a, b):  # rule a matches every packet rule b matches
    return all(x == "*" or x == y for x, y in zip(a[1:4], b[1:4]))
for i, b in enumerate(rules):
    for a in rules[:i]:
        if covers(a, b):
            kind = "redundant" if a[4] == b[4] else "shadowed (never reached)"
            print(f"rule {b[0]} {kind} by rule {a[0]}"); break
```

Run with `python3 lab_rules.py`. Verified output:

```text
rule 3 shadowed (never reached) by rule 1
rule 6 redundant by rule 5
```

### 24.3 Reading the audit

The checker finds rule 3, allowing guest devices to the portal on port 443, shadowed by rule 1, which denies all guest traffic. Someone intended guests to reach the portal, but the rule never takes effect. Rule 6, allowing staff to the lab server, is redundant because rule 5 already allows staff everything. The deeper problem is rule 5 itself: a broad staff-to-anything allow defeats the purpose of separating groups. Priya recommends replacing it with specific staff flows, moving rule 3 above rule 1 if guest portal access is truly needed, and removing rule 6.

### 24.4 Rules need owners

A rule without an owner is never reviewed and rarely removed. Priya records, for each rule, the person or role who requested it and confirms it remains needed. She also notes rule 4, allowing DNS from anywhere to anywhere: it supports a needed dependency but is broader than necessary, since devices should use only the clinic's DNS servers. Narrowing it reduces the chance that malware uses DNS to communicate outside. Regular review with owners keeps a policy aligned with real needs as the clinics change.

### Worked example

After fixes, the policy has seven specific allow rules and a final deny, with no shadowed or redundant rules.

> **Synthetic case.** Rules are synthetic.

### Errors and limits

Broad allow rules added for convenience quietly undo segmentation.

### Exercises

- **EX070 — Shadowed rule meaning.** Why does rule 3 never take effect? *Rubric:* 3 = rule 1 denies all guest traffic first;; 2 = earlier deny;; 1 = order;; 0 = none.
- **EX071 — Broad staff rule.** What is wrong with rule 5? *Rubric:* 3 = staff-to-anything defeats separation;; 2 = too broad;; 1 = vague;; 0 = none.
- **EX072 — DNS rule narrowing.** How should the any-to-any DNS rule be narrowed? *Rubric:* 3 = only to clinic DNS servers;; 2 = specific servers;; 1 = remove;; 0 = none.

### Synthesis

Default deny, careful ordering and owned, specific rules make a policy enforce what was intended.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) build a lab network; (2) test rules safely; (3) record results.

### 25.1 Why a lab

Changing a live clinic network to test ideas would risk disrupting patient care. A lab reproduces the important parts on spare equipment or virtual machines: four groups, a firewall with the proposed rules and test devices in each group. Priya's lab runs entirely on university equipment, uses invented addresses and has no connection to the clinics. Mistakes in a lab cost only time, so it is the right place to learn how rules behave and to make the errors that would be serious elsewhere.

### 25.2 Designing tests

Tests come from requirements. For R1, Priya tries connections from a test device in the guest group to each other group and expects all to fail; she also checks guest can still reach the internet, so the test catches over-blocking. For each needed flow, she tests that it works. For a few flows, she tests neighbouring ports to confirm rules are not broader than intended. Every test has an expected result written in advance, so outcomes are judged against predictions rather than explained afterwards.

### 25.3 Running and recording

Priya runs the tests and records each result with the date, the rule set version and the outcome. Two tests fail: clinical carts cannot reach the lab results server because she forgot the server listens on a second port, and guest devices can reach the management group's web page because of a typo in a subnet. Both are fixed and the full set is rerun. Recording failures, not just final passes, shows how the design improved and helps her tutor see her reasoning.

### 25.4 Limits of the lab

A lab is not the real network. It has fewer devices, simpler traffic and no forgotten equipment hidden in a cupboard. Passing lab tests is necessary but not sufficient. Priya lists differences between lab and clinics, such as the real clinics having a printer shared between groups, and plans checks in the real environment for each difference. Being honest about lab limits prevents overconfidence when the design is finally deployed. She also records which lab results she expects to differ in the clinics and how she will check them on site.

### Worked example

Of twenty lab tests, eighteen pass at first; after two fixes, all twenty pass.

> **Synthetic case.** Lab results are synthetic.

### Errors and limits

Testing only that permitted flows work misses rules that allow too much.

### Exercises

- **EX073 — Over-blocking check.** Why test that guests can still reach the internet? *Rubric:* 3 = detect over-blocking as well as under-blocking;; 2 = both;; 1 = unnecessary;; 0 = none.
- **EX074 — Typo failure.** What did the guest-to-management failure reveal? *Rubric:* 3 = subnet typo allowing access;; 2 = typo;; 1 = vague;; 0 = none.
- **EX075 — Lab limits.** Name one difference between the lab and real clinics. *Rubric:* 3 = shared printer, more devices, hidden equipment;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

A safe lab with requirement-based tests catches errors before they reach a live network.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Network and communications security: methods II

### Learning outcomes

You will (1) plan secure wireless; (2) design remote access; (3) choose protocols for inter-site links.

### 26.1 Planning wireless networks

Wireless needs special care because its signal crosses walls into car parks and neighbouring buildings. Following NIST SP 800-153, Priya plans separate wireless networks for staff, clinical devices and guests, each linked to its own group and subnet. Staff wireless uses individual accounts; clinical wireless uses device certificates where supported; guest wireless uses a simple passphrase changed monthly and gives internet access only. Access point management interfaces sit in the management zone and are never reachable from the wireless networks they serve.

### 26.2 Guest isolation

On the guest network, devices should not be able to reach each other, because one infected phone could otherwise attack others in the waiting room. Most access points offer client isolation, which forwards guest traffic only to the internet gateway. Priya adds this to the design and to the test list. She also limits guest bandwidth so heavy use cannot slow clinical traffic sharing the same internet link, which protects availability as well as confidentiality. The isolation test sends traffic between two guest test devices and expects it to fail, while confirming both still reach the internet.

### 26.3 Remote staff access

Some staff work from home and need the booking system and clinic files. Priya compares options: exposing services directly to the internet, which increases attack surface; or a VPN that authenticates staff and encrypts traffic before it reaches clinic systems. She chooses a VPN with individual accounts and a second factor. NIST SP 800-77r1 describes IPsec VPN design, and SP 800-52r2 covers TLS where a TLS-based VPN is used. VPN users land in a restricted group that reaches only the services they need.

### 26.4 Linking the clinics

The four clinics connect over the internet. Traffic between them, such as clinical carts at a branch reaching the lab results server at the main clinic, must be protected in transit. Priya proposes site-to-site IPsec tunnels between clinic firewalls, using IKEv2 as specified in RFC 7296, with certificates rather than shared keys so a stolen device's credentials can be revoked individually. Only needed flows are allowed through the tunnels, so a problem at one clinic does not automatically spread to the others.

### Worked example

Priya's design adds three wireless networks per clinic, client isolation for guests, a VPN for remote staff and IKEv2 tunnels between clinics.

> **Synthetic case.** The design is synthetic.

### Errors and limits

VPN users given full network access recreate a flat network from outside.

### Exercises

- **EX076 — Client isolation purpose.** What does client isolation protect against on guest wireless? *Rubric:* 3 = infected guest attacking other guests;; 2 = guest-to-guest;; 1 = outsiders;; 0 = none.
- **EX077 — VPN landing zone.** Why place VPN users in a restricted group? *Rubric:* 3 = avoid full access, limit reach to needed services;; 2 = limit;; 1 = convenience;; 0 = none.
- **EX078 — Tunnel authentication.** Why use certificates instead of shared keys for clinic tunnels? *Rubric:* 3 = revoke individually if a device is stolen;; 2 = revocation;; 1 = stronger;; 0 = none.

### Synthesis

Separate wireless networks, guest isolation, restricted VPN access and protected inter-site links extend segmentation beyond one building.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Network and communications security: verification

### Learning outcomes

You will (1) verify configuration against design; (2) review DNS and name resolution; (3) detect drift.

### 27.1 Verification versus testing

Testing checks behaviour by sending traffic; verification also checks that the configuration matches the approved design. Priya compares the firewall rules exported from the lab with the needed-flows list, rule by rule, and lists differences. Some differences are errors, others are flows missing from the list. Both kinds are resolved before deployment. Verification catches problems tests miss, such as a rule allowing traffic nobody tested because nobody knew it was there. She records each difference, its cause and its resolution in a verification log, which becomes evidence that the deployed configuration was checked against the design.

### 27.2 DNS checks

Name resolution is a quiet but important dependency. Priya verifies that each group uses the intended DNS server, that the clinic's internal names resolve only internally, and that external queries go through the provider's resolver rather than directly to arbitrary servers. NIST SP 800-81-2 offers guidance on secure DNS deployment. Controlling DNS supports security in two ways: it prevents some malware from using its own resolvers, and DNS logs show which names devices look up, which can reveal infections early.

A clinic device that suddenly queries an unfamiliar external resolver is therefore worth investigating, because the bypass itself is a signal.

### 27.3 Configuration drift

After deployment, configurations change through emergency fixes, upgrades and forgotten tweaks. Drift is the gap between the approved configuration and the running one. Priya plans a monthly comparison: export the running configuration, compare it with the stored approved version and list differences. Each difference is either approved through the normal change process or reverted. A simple script comparing the two files is enough for a small organisation and much better than discovering drift during an incident. Approved configurations are stored with version history so changes can be traced.

### 27.4 Independent checking

The person who wrote a configuration often reads what they meant rather than what they wrote. Priya asks a classmate to verify her lab configuration against the design without help. The classmate finds an object named for the clinical subnet that actually contains the guest range, an error Priya had read past several times. Independent checks are cheap and effective, and small organisations can arrange them with a partner organisation or a supplier under agreement. She thanks the classmate in her report and records the error as evidence of the check's value.

### Worked example

Verification finds three differences: one error, one missing flow and one unused rule.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Verifying only by reading one's own configuration misses errors the author expects not to see.

### Exercises

- **EX079 — Untested rule.** What kind of problem does configuration verification catch that testing misses? *Rubric:* 3 = rules nobody knew existed so never tested;; 2 = hidden rules;; 1 = vague;; 0 = none.
- **EX080 — DNS control value.** Give two security benefits of controlling DNS. *Rubric:* 3 = block malware resolvers; logs reveal infections;; 2 = two;; 1 = one;; 0 = none.
- **EX081 — Drift handling.** What happens to each difference found in a drift check? *Rubric:* 3 = approved via change process or reverted;; 2 = fix;; 1 = ignore;; 0 = none.

### Synthesis

Comparing configuration to design, checking DNS and monitoring drift keep the deployed network faithful to its design.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Network and communications security: failure analysis

### Learning outcomes

You will (1) analyse how controls fail; (2) plan for failure safely; (3) learn from near misses.

### 28.1 How controls fail

Controls fail in several ways: misconfiguration, hardware failure, expired credentials, overload and human workarounds. Priya lists each control in her design and asks how it could fail. The firewall could be misconfigured or fail; the guest passphrase could leak; certificates could expire; logs could stop arriving; staff could plug a visitor's device into a staff network port. For each, she notes how the failure would be noticed and what would limit damage. Controls without any way of noticing failure need attention first.

### 28.2 Fail open or fail closed

When a control fails, it can fail open, letting traffic through, or fail closed, blocking it. A failed firewall usually fails closed, cutting services; a failed logging system fails open in effect, since traffic continues unrecorded. Neither is always right. For clinical services, failing closed could delay patient care, so Priya plans a spare firewall configuration and a quick recovery procedure rather than any bypass. Deliberately documented choices are better than discovering behaviour during an outage. She records the expected failure mode of each control in the design document.

### 28.3 Human workarounds

When controls get in the way, people find ways around them. If clinical staff cannot print from a cart because a rule is missing, someone might connect the cart to the staff wireless. Workarounds often defeat security more completely than attackers do. Priya plans a quick route for staff to report blocked work, a target to fix genuine needs within a day, and monitoring for devices appearing in the wrong group. Reducing friction is part of making controls survive in practice.

### 28.4 Near misses

A near miss is an event that could have caused harm but did not, such as a certificate found with two days left. Priya recommends recording near misses alongside incidents, with a short note on what nearly happened and what will prevent it. Near misses are far more common than incidents, so they offer many more chances to learn. Organisations that only study actual incidents learn slowly and often only after harm has occurred. A short monthly review of near misses keeps the lessons visible and turns each one into a specific improvement with an owner.

### Worked example

Priya's failure table covers seven controls; logging has no failure detection and becomes the first fix.

> **Synthetic case.** Failure analysis is synthetic.

### Errors and limits

Assuming a control works because it was configured once ignores later failures.

### Exercises

- **EX082 — Fail-open example.** Give an example of a control that effectively fails open. *Rubric:* 3 = logging failure; traffic continues unrecorded;; 2 = logging;; 1 = firewall;; 0 = none.
- **EX083 — Workaround prevention.** How can staff workarounds be reduced? *Rubric:* 3 = quick reporting route and fast fixes for genuine needs;; 2 = fix fast;; 1 = punish;; 0 = none.
- **EX084 — Near miss value.** Why record near misses? *Rubric:* 3 = more frequent, learning before harm;; 2 = learning;; 1 = unnecessary;; 0 = none.

### Synthesis

Planning for how controls fail, including human workarounds, makes designs resilient in practice.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Network and communications security: operations

### Learning outcomes

You will (1) plan routine operations; (2) manage changes; (3) respond to alerts.

### 29.1 Routine checks

Security depends on small tasks done regularly. Priya drafts a weekly routine for the clinic IT lead: review denied connections from the guest group, check that every device sent logs, look at certificates expiring within sixty days and confirm backups of firewall configurations exist. Each item has a checklist and an expected time, totalling about forty minutes. Keeping the routine short makes it realistic for a part-time role. A routine that takes half a day would soon be skipped during busy weeks.

### 29.2 Change management

Changes to rules or wireless settings follow a simple process: a written request stating what and why, a check against the needed-flows list, a test in the lab where possible, a scheduled time outside clinic hours and a check afterwards. Emergency changes are allowed when patient care is affected but are recorded the same day and reviewed later. Priya keeps the process light enough that the IT lead will use it, since a process that is too heavy gets bypassed.

### 29.3 Responding to alerts

Priya defines what triggers an alert: repeated denies from one guest device towards internal groups, a configuration change outside a scheduled window, or a device that stops logging. Each alert type has a short response note: what to check first, when to disconnect a device and whom to contact. Alerts outside working hours go to email for review the next morning, since the clinics have no overnight staff, and clinical systems have separate supplier support for urgent faults. Each response note fits on one page.

### 29.4 Supporting the IT lead

A single part-time person cannot do everything. Priya suggests the clinics agree a support arrangement with a local provider for out-of-hours emergencies, and write down passwords and procedures in a sealed, controlled record so that someone else can act if the IT lead is unavailable. Documentation and backup arrangements reduce dependence on one person, a common weakness in small organisations that only becomes visible during illness, holidays or departures. Priya also recommends that a second staff member learns the weekly routine, so basic checks continue during absences and someone besides the IT lead can recognise when something looks wrong.

### Worked example

The weekly routine has four checks and takes about forty minutes; two alert types are defined with response notes.

> **Synthetic case.** Routines are synthetic.

### Errors and limits

Routines too long for the staff available are skipped first when work is busy.

### Exercises

- **EX085 — Routine length.** Why keep the weekly routine around forty minutes? *Rubric:* 3 = realistic for part-time role, won't be skipped;; 2 = short;; 1 = arbitrary;; 0 = none.
- **EX086 — Emergency changes.** How are emergency changes controlled? *Rubric:* 3 = recorded same day, reviewed later;; 2 = recorded;; 1 = not allowed;; 0 = none.
- **EX087 — Single-person risk.** What reduces dependence on the single IT lead? *Rubric:* 3 = documentation, controlled credential record, external support;; 2 = documentation;; 1 = vague;; 0 = none.

### Synthesis

Short routines, light change control and clear alert responses keep controls working over time.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) rehearse a complete deployment in the lab; (2) test failure and recovery; (3) produce a lab report.

### 30.1 Full rehearsal

Before proposing deployment at a clinic, Priya rehearses the whole change in the lab: creating the new wireless networks, moving test devices into their groups, applying the firewall rules, enabling logging and running every test. She times each step. The rehearsal takes three hours, which tells the clinics how long a real change window must be. It also exposes ordering problems, such as needing the management network working before access points can receive their new settings. She updates the deployment checklist to put steps in the right order.

### 30.2 Failure and recovery tests

Priya simulates failures. She restores the firewall from its backup configuration and checks all tests pass afterwards; she expires a test certificate and confirms the monitoring script reports it; she stops logging from one device and confirms the completeness check notices within an hour. Each test has an expected outcome written beforehand. Testing recovery matters as much as testing protection, because a design that cannot be restored quickly after a failure will tempt staff to bypass it. Results are added to the lab report with timings.

### 30.3 Rollback plan

Every deployment needs a way back. Priya's rollback plan saves the existing configurations of the access points and firewall before changes, sets a decision point two hours into the window, and reverts if critical tests have not passed by then. She practises the rollback in the lab and it takes twenty minutes. Having a rehearsed rollback lets the team stop calmly rather than troubleshooting under pressure while clinic staff wait for systems to return. The saved configurations are tested to load correctly before each window, so rollback is known to work.

### 30.4 The lab report

Priya writes a lab report covering the setup, tests, results, failures found, fixes and limits. It includes a table linking each requirement to its tests and results. The report is short, around six pages, and written for the clinic IT lead as well as her tutor. It becomes the basis for the deployment proposal she will present later, and it gives the clinics evidence that the design was tested carefully before anyone touched their network. An appendix lists the exact rule set version tested, so the report can be matched to configurations later.

### Worked example

The rehearsal takes three hours; rollback takes twenty minutes; all twenty-six tests pass after two fixes.

> **Synthetic case.** Lab results are synthetic.

### Errors and limits

A rollback plan that was never practised often fails when needed.

### Exercises

- **EX088 — Rehearsal timing value.** What did timing the rehearsal tell the clinics? *Rubric:* 3 = required change window length;; 2 = window;; 1 = vague;; 0 = none.
- **EX089 — Rollback decision point.** What is the purpose of a decision point in the window? *Rubric:* 3 = revert calmly if tests not passed;; 2 = stop;; 1 = vague;; 0 = none.
- **EX090 — Report audience.** Who is the lab report written for? *Rubric:* 3 = IT lead and tutor;; 2 = IT lead;; 1 = tutor only;; 0 = none.

### Synthesis

A full rehearsal with failure, recovery and rollback tests prepares a safe real deployment.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Network and communications security: advanced cases

### Learning outcomes

You will (1) analyse complex, multi-factor cases; (2) trace chains of small failures; (3) propose layered fixes.

### 31.1 Chains of small failures

Serious incidents rarely have one cause. Priya studies a synthetic composite case in which a small charity suffered a data loss. A supplier's remote access account had a weak password; the server it reached sat on a flat network; logs were kept for only three days; and nobody reviewed them. Each weakness alone might have been survivable. Together they allowed an intruder to enter, move to a file server and copy data for two weeks before anyone noticed. She practises drawing the chain step by step and marking where any one control would have broken it.

### 31.2 Where layered controls help

For each link in the chain, Priya identifies a control: strong, individual supplier accounts would have stopped the first step; segmentation would have kept the remote access server away from the file server; central logs kept for ninety days would have preserved evidence; and a weekly review of unusual access would have shortened the time before detection. The lesson is that small organisations do not need perfect controls, but they do need several reasonable ones, because each breaks the chain at a different point.

### 31.3 Case: wireless bridge

A second composite case concerns a clinic-like practice where a staff member connected a small wireless router to a network port to improve signal in a back room. The router used a default passphrase and bridged its users directly onto the internal network, bypassing the firewall and guest separation entirely. Priya draws lessons for the clinics: monitor for unknown devices, disable unused network ports, provide good official coverage so staff have no reason to improvise, and explain to staff why such devices are dangerous.

### 31.4 Applying cases to the design

Priya checks her clinic design against both cases. The supplier lesson leads her to specify that any supplier access goes through the VPN with individual accounts and only to the supplier's own systems. The wireless bridge lesson adds a requirement for detecting unknown devices and a recommendation to survey wireless coverage before deployment. Comparing a design against concrete cases is a practical way to find gaps that abstract threat lists miss, because cases show how real people and systems behave.

### Worked example

Priya's chain diagram for the charity case has four links; her design adds controls at each.

> **Synthetic case.** Cases are synthetic composites.

### Errors and limits

Focusing on the final step of an incident ignores earlier links where cheaper controls would have worked.

### Exercises

- **EX091 — Chain link control.** Which control breaks the chain at the movement-to-file-server step? *Rubric:* 3 = segmentation separating remote access server from file server;; 2 = segmentation;; 1 = logging;; 0 = none.
- **EX092 — Rogue router lesson.** List two controls against staff-installed wireless routers. *Rubric:* 3 = detect unknown devices, disable unused ports, good coverage;; 2 = two;; 1 = one;; 0 = none.
- **EX093 — Supplier access design.** How does the clinic design handle supplier access after this case? *Rubric:* 3 = via VPN, individual accounts, only to their systems;; 2 = VPN;; 1 = unchanged;; 0 = none.

### Synthesis

Incidents are chains; layered reasonable controls break them at several points.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Network and communications security: interdisciplinary interfaces

### Learning outcomes

You will (1) work with clinical, legal and management perspectives; (2) communicate risk; (3) align security with care.

### 32.1 Clinical priorities

In a clinic, patient care comes first, and security that delays care will be bypassed or rejected. Priya meets a nurse manager who explains that clinical carts must work immediately at the start of each session and that a login screen appearing mid-procedure is unacceptable. This shapes the design: carts use device certificates rather than staff logins, and changes are scheduled outside clinic hours. Listening to clinical staff early prevents designs that look secure on paper but fail in the reality of patient care.

### 32.2 Legal and regulatory views

Health data are subject to data protection law, and the clinics must be able to show that they protect it appropriately. The clinics' data protection officer is interested in evidence: what controls exist, who checks them and how incidents would be handled. Priya's requirement list, test results and logging specification become useful evidence. She learns that framing technical work in terms of obligations and evidence helps legal colleagues, who do not need to understand firewall rules to see that risks are being managed.

### 32.3 Management and budget

Managers decide what is funded, and they compare security against other needs such as staff and equipment. Priya presents costs, benefits and risks in plain language: new access points and a firewall per clinic cost a stated amount, reduce the risk of an infection spreading to clinical devices, and support legal obligations. She avoids frightening language and exaggerated claims, which damage trust. Managers respond well to clear options with costs, including a cheaper first phase that delivers guest separation alone.

### 32.4 Translating between groups

Each group uses different language: clinicians talk about patients and sessions, lawyers about obligations and evidence, managers about cost and risk, and technical staff about rules and protocols. Priya acts as a translator, writing a one-page summary for each audience from the same design. The facts are identical; the emphasis changes. This skill is often more valuable than deep technical knowledge in small organisations, where the security practitioner must win support from people who will never read a configuration. She checks each summary with someone from that group.

### Worked example

Priya produces three one-page summaries of the same design for clinical, legal and management readers.

> **Synthetic case.** Meetings are synthetic.

### Errors and limits

Presenting technical detail to non-technical decision makers usually delays decisions.

### Exercises

- **EX094 — Clinical constraint.** How did clinical needs shape authentication for carts? *Rubric:* 3 = device certificates, no staff login mid-procedure;; 2 = certificates;; 1 = vague;; 0 = none.
- **EX095 — Legal value of evidence.** Why are test results useful to the data protection officer? *Rubric:* 3 = evidence that risks are managed;; 2 = evidence;; 1 = vague;; 0 = none.
- **EX096 — Phased option.** What cheaper first phase was offered to managers? *Rubric:* 3 = guest separation alone;; 2 = guest network;; 1 = vague;; 0 = none.

### Synthesis

Security succeeds in organisations when it fits clinical work, legal duties and management priorities.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) design a measurement study; (2) analyse results honestly; (3) check agreement between reviewers.

### 33.1 From question to study design

For her capstone, Priya asks: after guest separation, does the number of guest-originated connection attempts reaching internal groups fall to zero, and how many guest alerts need human attention each week? The study compares four weeks before and four weeks after deployment at two clinics. She defines each measure precisely, chooses data sources and writes the analysis plan before collecting data, so the analysis cannot be bent to fit the results she hopes to see. Two clinics are chosen because they have similar visitor numbers, which makes their results easier to compare.

### 33.2 Measurement validity

A measure is valid if it captures what it claims to. "Guest connections reaching internal groups" before deployment comes from flow records, since no firewall existed; after deployment it comes from firewall allow logs. Different sources might count differently, so Priya checks both on a test day when both are available and confirms they agree closely. Without this check, an apparent change could simply reflect a change in how data were counted rather than a change in the network. The agreement check is recorded in her method chapter.

### 33.3 Reliability of human judgement

Some measures depend on judgement, such as whether an alert needed attention. Two people may judge the same alert differently. Priya and the IT lead each label the same sample of alerts independently, then measure how often they agree beyond what chance would produce. Cohen's kappa is a common statistic for this, and Landis and Koch suggested widely used descriptive bands for interpreting it. Measuring agreement shows whether a judgement-based measure is consistent enough to report. Low agreement would mean the labelling rules need clarifying before results are reported.

### 33.4 Honest analysis

Priya commits to reporting all results, including those that do not support her design. If guest connections to internal groups do not fall to zero, she will report it and investigate why. She reports sample sizes, the time periods and any data problems. Honest reporting matters especially in student projects with partners, where there can be pressure to present only good news. Partners benefit more from accurate findings than from flattering ones, because accurate findings show what still needs fixing.

### Worked example

The analysis plan defines two measures, their sources, a validity check and an agreement check, all written before data collection.

> **Synthetic case.** The study is synthetic.

### Errors and limits

Changing measurement sources at the same time as the intervention can create false effects.

### Exercises

- **EX097 — Plan timing.** Why write the analysis plan before collecting data? *Rubric:* 3 = prevents bending analysis to fit results;; 2 = avoid bias;; 1 = tidiness;; 0 = none.
- **EX098 — Source change risk.** Why check flow records against firewall logs on one day? *Rubric:* 3 = confirm sources count alike, avoid false change;; 2 = validity;; 1 = vague;; 0 = none.
- **EX099 — Agreement statistic.** Which statistic measures agreement between two reviewers beyond chance? *Rubric:* 3 = Cohen's kappa, Landis and Koch bands;; 2 = kappa;; 1 = percentage only;; 0 = none.

### Synthesis

Pre-planned measures, validity checks, agreement statistics and honest reporting make findings trustworthy.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare design options systematically; (2) use criteria and weights; (3) justify a choice.

### 34.1 Options for the clinics

Priya compares three ways to separate clinic groups. Option A uses separate wireless networks and virtual LANs with access control lists on existing switches, at low cost but with limited logging. Option B adds a small firewall at each clinic, giving stateful filtering, logging and VPN support. Option C sends all traffic to a cloud-delivered security service, which reduces on-site equipment but depends on internet links and a subscription. Each option could work; the question is which fits the clinics best.

### 34.2 Criteria and weights

She chooses criteria that matter to the clinics: risk reduction, cost over five years, ease of operation for one part-time IT lead, resilience when the internet link fails, and quality of logging. Managers weight risk reduction and ease of operation highest. Each option is scored from one to five on each criterion. The weighted totals put option B first, option C second and option A third, mainly because option A's limited logging fails the detection needs identified earlier. The weights are agreed with managers before any scoring is done.

### 34.3 Sensitivity

Priya tests whether the result depends on the weights. If cost is weighted much higher, option A moves level with B; if internet resilience is weighted lower, option C nearly matches B. She presents these sensitivities to managers so they understand the choice depends on their priorities. Making the decision's dependence on values visible prevents analysis from appearing more objective than it is, and lets managers own the choice rather than simply accepting a number. She shows the sensitivity results as a small table with each changed weight and the resulting order of options.

### 34.4 Justifying the choice

The clinics choose option B. Priya writes a decision record explaining the options, scores, sensitivities and reasons, noting that option C may become attractive later if internet links become more reliable and the clinics grow. The record helps future staff understand why the design looks as it does and when to revisit it. Comparative analysis does not guarantee the best choice, but it makes the reasoning visible and open to challenge. It also records which assumptions would change the decision, such as a large rise in subscription prices or a fall in firewall support quality.

### Worked example

Weighted scores are B 4.2, C 3.6, A 3.1; sensitivity shows A approaching B only when cost dominates.

> **Synthetic case.** Scores are synthetic.

### Errors and limits

Choosing weights after seeing scores lets analysts steer results.

### Exercises

- **EX100 — Option A weakness.** Why did option A rank last? *Rubric:* 3 = limited logging failed detection needs;; 2 = logging;; 1 = cost;; 0 = none.
- **EX101 — Sensitivity purpose.** What does the sensitivity analysis show managers? *Rubric:* 3 = choice depends on their priorities;; 2 = dependence on weights;; 1 = vague;; 0 = none.
- **EX102 — Revisit trigger.** When might option C be reconsidered? *Rubric:* 3 = more reliable links or growth;; 2 = later;; 1 = never;; 0 = none.

### Synthesis

Systematic comparison with visible weights and sensitivity supports a justified, revisitable decision.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) define capstone scope and requirements; (2) plan deployment and measurement; (3) manage risks.

### 35.1 Capstone scope

Priya's capstone deploys option B at two of the four clinics: separate wireless networks for staff, clinical and guest groups; a firewall with the default-deny policy; individual staff wireless accounts; central logging; and the TLS upgrade for the lab results service, which the supplier has agreed to schedule. The other two clinics will follow after the capstone using her documentation. Limiting the capstone to two clinics makes it achievable in one term while still giving real evidence. The two chosen clinics have the most visitors and the most clinical carts.

### 35.2 Requirements and tests

The proposal lists requirements R1 to R6 from chapter 23 and, for each, the tests and evidence that will show it is met. R1 is tested by attempting connections from a guest test device to each internal group on site, with the clinic's permission and during a scheduled window. R5 is tested by the TLS audit script. R6 is tested by checking the oldest log record after ninety days, which falls after the capstone ends, so she will report it as pending with a configuration check instead.

### 35.3 Plan and measurement

Deployment happens on two Saturdays, using the rehearsed steps and rollback plan. Measurement follows the study design in chapter 33: four weeks before and four after, with denied and allowed guest-to-internal connection counts and a weekly alert review. Priya schedules a midpoint review with Dr Kowal and the clinic IT lead. Writing the plan as a timeline with named responsibilities makes it easy to see when something slips and what depends on it. Each task on the timeline names who does it and what must be finished first, so delays are spotted early.

### 35.4 Risks

Priya lists project risks: the supplier delaying the TLS upgrade, a clinical device failing to connect to its new network, the IT lead being unavailable, and bad weather or illness affecting the Saturdays. For each she plans a response, such as reporting the TLS upgrade as out of her control if delayed, testing every clinical device type in the lab first, and booking a reserve Saturday. Managing these risks openly reassures the clinics that their services are protected during the project.

### Worked example

The proposal is approved with one change: the clinics ask for guest separation first, a week before the full deployment.

> **Synthetic case.** The proposal is synthetic.

### Errors and limits

Capstones that try to cover every site and every control rarely finish with solid evidence.

### Exercises

- **EX103 — Two-clinic scope.** Why deploy at two clinics rather than four? *Rubric:* 3 = achievable in a term with real evidence;; 2 = time;; 1 = cost;; 0 = none.
- **EX104 — Pending requirement.** Why is R6 reported as pending? *Rubric:* 3 = ninety days falls after capstone; configuration checked instead;; 2 = timing;; 1 = failed;; 0 = none.
- **EX105 — Clinic change.** What change did the clinics request? *Rubric:* 3 = guest separation first, a week earlier;; 2 = guest first;; 1 = vague;; 0 = none.

### Synthesis

A focused scope, testable requirements, a timeline and planned risk responses make the capstone achievable.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) work professionally on site; (2) communicate with staff; (3) respond to unexpected findings.

### 36.1 Working on site

Priya's first site visit is with the clinic IT lead before deployment. She follows the clinic's rules: signing in, wearing a visitor badge, staying out of patient areas unless escorted and never photographing screens or rooms. She checks access point positions, network cupboards and device labels against the inventory. Professional conduct on site matters because clinics are workplaces for staff and sensitive spaces for patients, and a careless visitor can undermine trust in the whole project. She records what she inspected, when and with whom.

### 36.2 Unexpected findings

In a cupboard, Priya finds an unlabelled small router connected to the network, the very situation from the wireless bridge case. She does not unplug it, since it might support something important. Instead she reports it to the IT lead, who discovers it was installed by a former supplier to monitor a heating system. It is documented, and a plan is agreed to move the heating monitor to its own restricted connection. Reporting rather than acting alone respects authority and avoids accidental outages.

### 36.3 Talking with staff

Staff ask what is changing and whether they will notice. Priya explains briefly: staff will log on to wireless with their own accounts, visitors will use a separate network, and nothing else should change. She provides a one-page guide and the IT lead's contact for problems. Explaining changes in advance reduces anxiety and makes staff more likely to report problems early, rather than finding their own workarounds when something unexpected happens on deployment day. The guide uses plain language and screenshots of the new sign-in screen, avoiding technical terms.

### 36.4 Guest separation first

As the clinics requested, guest separation goes live a week early. Visitors join the new guest network from a sign in the waiting room. On the first day, the receptionist reports that the waiting room television, which streams health information videos, stopped working. It had used the old shared network. Priya and the IT lead connect it to the guest network, where it needs only internet access. The fix takes ten minutes, and the case is recorded as a missed device for the inventory.

### Worked example

The site visit finds one unknown router and two inventory errors; guest separation goes live with one quickly fixed issue.

> **Synthetic case.** Site details are synthetic.

### Errors and limits

Unplugging unknown equipment without checking can cause outages to unexpected services.

### Exercises

- **EX106 — Unknown router response.** Why didn't Priya unplug the unknown router? *Rubric:* 3 = might support something important; report instead;; 2 = risk;; 1 = forgot;; 0 = none.
- **EX107 — Missed device.** What was the waiting room television issue and fix? *Rubric:* 3 = used old network; moved to guest;; 2 = moved;; 1 = vague;; 0 = none.
- **EX108 — Site photography.** Why avoid photographing screens and rooms on site? *Rubric:* 3 = patient privacy and clinic rules;; 2 = privacy;; 1 = vague;; 0 = none.

### Synthesis

Professional conduct, careful reporting and clear communication make field work safe and trusted.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) review evidence critically; (2) measure agreement on alert labels; (3) interpret kappa.

### 37.1 Reviewing evidence

In a seminar, Priya presents her early evidence to classmates and Dr Kowal, who question it. Why are there two weeks of before data instead of four at one clinic? Because logging started late, she explains, and she reports it as a limitation. Are guest-to-internal attempts after separation zero? Allowed attempts are zero; denied attempts continue at a low rate, mainly from devices looking for printers. Critical review exposes weaknesses early, while they can still be fixed or explained. She records every question and her answer.

### 37.2 Labelling alerts

To measure how many guest alerts need attention, Priya and the IT lead each label twenty alerts independently as needing attention or not. Labels depend on judgement: a burst of denied connections from one phone might be harmless printer discovery or a sign of infection. Independent labelling, without discussing each case, is essential; otherwise the two reviewers influence each other and agreement looks higher than it really is. Both use the same short written definition of an alert needing attention, so differences reflect judgement rather than different rules, and the twenty alerts are drawn at random from the four-week period.

### Lab — Agreement on labels

```python
"""Cohen's kappa for two reviewers labelling synthetic alerts (stdlib only)."""
a = "TTFTFFTTFTFFTTTFFTFT"
b = "TTFTFTTTFFFFTTTFFTFF"
n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
pe = sum((a.count(c) / n) * (b.count(c) / n) for c in "TF")
k = (po - pe) / (1 - pe)
print(f"n {n} observed agreement {po:.2f} chance {pe:.3f} kappa {k:.2f}")
```

Run with `python3 lab_kappa.py`. Verified output:

```text
n 20 observed agreement 0.85 chance 0.500 kappa 0.70
```

### 37.3 Interpreting kappa

The reviewers agree on seventeen of twenty alerts, 85 percent. Because both label about half the alerts as needing attention, chance agreement alone would be 50 percent. Cohen's kappa adjusts for this and gives 0.70. On the bands proposed by Landis and Koch, this is substantial agreement, enough to report the measure with confidence. Priya also reviews the three disagreements with the IT lead and writes a clearer labelling guide, which should raise agreement in later weeks. She reports kappa together with the raw agreement and the sample size.

### 37.4 Strengthening the evidence

After the seminar, Priya adds a short note to each limitation, describing its effect. The shorter before period at one clinic makes that clinic's comparison less certain, so she reports it separately. The continuing denied attempts are explained with examples. She adds the kappa result to support the alert measure. Evidence that has survived questioning is stronger than evidence nobody has examined, and the seminar improved her capstone more than another week of data would have. The revised evidence appendix is reviewed by Dr Kowal.

### Worked example

Agreement is 0.85 with chance 0.50, giving kappa 0.70, substantial on the Landis and Koch bands.

> **Synthetic case.** Labels are synthetic.

### Errors and limits

Reporting raw agreement without adjusting for chance overstates reliability.

### Exercises

- **EX109 — Kappa value.** What kappa does the lab report and how is it described? *Rubric:* 3 = 0.70, substantial per Landis and Koch;; 2 = 0.70;; 1 = 0.85;; 0 = none.
- **EX110 — Chance adjustment.** Why is 85 percent agreement not enough on its own? *Rubric:* 3 = chance gives 50 percent here; kappa adjusts;; 2 = chance;; 1 = it is enough;; 0 = none.
- **EX111 — Independence of labels.** Why must reviewers label alerts independently? *Rubric:* 3 = discussion inflates agreement;; 2 = bias;; 1 = speed;; 0 = none.

### Synthesis

Critical review and agreement statistics make judgement-based evidence credible.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) deploy the design at two clinics; (2) verify on site; (3) handle issues.

### 38.1 Deployment days

On two Saturdays, Priya and the IT lead deploy the full design at the two clinics. They follow the rehearsed checklist: save existing configurations, configure the management network, update access points with the staff and clinical networks, install the firewall with the approved rules, enable logging and run the on-site tests. The first clinic takes three and a half hours, slightly longer than the lab rehearsal because two access points need firmware updates. The second takes under three hours. Each step is ticked off and timed on the checklist.

### 38.2 On-site verification

On-site tests repeat the lab tests in the real environment, with the clinics' permission and outside opening hours. Guest test devices cannot reach staff, clinical or management groups; staff devices reach the booking service and files; clinical carts reach the lab results server; and the management zone is reachable only from the administrator workstation. All tests pass at both clinics, and results are recorded with times and configuration versions for the evidence file. Any failure would trigger the rehearsed rollback at the decision point, so services return quickly while the cause is investigated.

### 38.3 Issues found

The first week brings three issues. A clinical cart model fails to connect because it does not support the certificate method; it is placed on the clinical network using its restricted fallback, which allows only its specific flow. A staff member forgets her new wireless password and is reset by the IT lead. And denied logs show a staff laptop trying to reach a clinical cart every morning, which turns out to be an old shortcut to a retired application, removed after checking with the user.

### 38.4 Supplier coordination

The lab results supplier upgrades its service to TLS 1.3 during the capstone, as agreed. Priya reruns the TLS audit and confirms the change. The supplier also agrees to connect for maintenance only through the VPN with a named account. Coordinating with suppliers takes time and depends on their schedules, so Priya had planned for delay; in this case it arrived on time, but the plan would have allowed her to report it as pending without undermining the rest of the capstone.

### Worked example

Both clinics are deployed; all on-site tests pass; three issues in the first week are resolved within a day each.

> **Synthetic case.** Deployment is synthetic.

### Errors and limits

Assuming every device supports the chosen authentication method causes deployment-day failures.

### Exercises

- **EX112 — Unsupported cart.** How was the cart that could not use certificates handled? *Rubric:* 3 = restricted fallback allowing only its flow;; 2 = fallback;; 1 = removed;; 0 = none.
- **EX113 — Morning denies.** What caused the daily denied laptop-to-cart connections? *Rubric:* 3 = old shortcut to retired application;; 2 = shortcut;; 1 = attack;; 0 = none.
- **EX114 — TLS confirmation.** How was the supplier's TLS upgrade confirmed? *Rubric:* 3 = rerunning the TLS audit script;; 2 = audit;; 1 = told;; 0 = none.

### Synthesis

Careful, rehearsed deployment with on-site verification and quick issue handling delivers the design safely.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) measure outcomes against requirements; (2) analyse before and after data; (3) state limitations.

### 39.1 Results against requirements

Priya evaluates each requirement. R1 is met: on-site tests and four weeks of logs show no allowed guest connections to internal groups. R2 is met: the policy denies all but the eight needed flows, verified by configuration review. R3 is met: management is reachable only from the administrator workstation. R4 is met for staff. R5 is met: the TLS audit now shows the lab results service on TLS 1.3, though the old intranet remains on TLS 1.1 and is scheduled for retirement. R6 is configured and partly evidenced.

### 39.2 Before and after

Before separation, flow records at the two clinics showed guest devices opening an average of 140 connections a week to internal groups, mostly printer and file-sharing discovery. After separation, allowed guest-to-internal connections are zero, while denied attempts average 95 a week and fall slowly as devices stop retrying. Guest alerts needing attention average two a week, with kappa of 0.70 supporting the labelling. The reachable group pairs fall from twelve to four needed pairs. Results are reported separately for each clinic as well as combined.

### 39.3 Limitations

The evaluation covers two clinics over four weeks after deployment, a short period that may not include unusual events. One clinic had only two weeks of before data. The guest measure before deployment came from a different source, checked for agreement on one day. Some evidence, such as recovery from firewall failure, comes from the lab only. Priya lists each limitation with its likely effect and states that results suggest, rather than prove, lasting improvement. These limits are repeated beside the results they affect.

### 39.4 Recommendations

Based on the evaluation, Priya recommends deploying the same design at the remaining two clinics using her documentation, retiring the old intranet, completing the ninety-day log retention check, adding certificate support for the remaining cart model when the supplier provides it, and reviewing the weekly routine after three months. Each recommendation has an owner and a target date agreed with the IT lead, so the project's value continues after her capstone ends. The recommendations are ordered by risk reduction, so the clinics can act on the most valuable ones first if time or money is short.

### Worked example

Reachable group pairs fall from twelve to four; allowed guest-to-internal connections fall from about 140 a week to zero.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Claiming permanent improvement from four weeks of data overstates the evidence.

### Exercises

- **EX115 — Reachability outcome.** How did reachable group pairs change? *Rubric:* 3 = twelve to four needed pairs;; 2 = reduced;; 1 = vague;; 0 = none.
- **EX116 — Continuing denies.** Why do denied guest attempts continue after separation? *Rubric:* 3 = devices keep retrying discovery; fall slowly;; 2 = retries;; 1 = attack;; 0 = none.
- **EX117 — Remaining TLS gap.** Which TLS gap remains and how is it handled? *Rubric:* 3 = old intranet on TLS 1.1, scheduled for retirement;; 2 = old intranet;; 1 = vague;; 0 = none.

### Synthesis

Evaluation against requirements, with honest limits, shows what the capstone achieved and what remains.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write the bachelor's thesis; (2) present to examiners and partners; (3) reflect on learning.

### 40.1 Structuring the thesis

Priya's thesis follows the project: problem and context, background and sources, requirements and threat analysis, design and option comparison, lab testing, deployment, evaluation and conclusions. Each chapter begins with its purpose and ends with what the next chapter uses. Claims are linked to evidence in appendices: test tables, measurement data and decision records. She keeps the main text to about forty pages, moving detailed configuration listings to appendices in sanitised form. Dr Kowal reviews two drafts, asking each time for clearer links between claims and evidence, and for limitations to be stated beside results.

### 40.2 Sanitising and approval

Before submission, Priya replaces real device names, addresses and staff names with synthetic ones, and removes any detail that could help an attacker, such as exact firewall models or passphrase policies. The clinic IT lead and data protection officer review the thesis and approve it in writing. This protects the clinics and also protects Priya, who can show the thesis to future employers without worrying about disclosing a partner's sensitive information. The approval letter is included in the appendices with its date, so examiners can see that the release was authorised.

### 40.3 Presenting

Priya presents twice: to examiners, focusing on method, evidence and limitations; and to clinic managers, focusing on outcomes, costs and next steps. Examiners ask why she did not use a cloud-delivered option, and she explains the comparison and sensitivity results. Managers ask whether the remaining clinics can be done without her, and she shows the documentation and the IT lead's role in both deployments. Adapting the same work to different audiences is the skill practised in chapter 32. Both talks are rehearsed in advance.

### 40.4 Reflection

In her reflection, Priya notes that the technical work was the easier part. Understanding clinical priorities, agreeing access with suppliers, sanitising data and earning the trust of a busy IT lead took more time and taught her more. She would start the inventory comparison earlier and involve clinical staff sooner. Her degree ends with a deployed design, evidence of improvement and a clinic team able to continue the work, which is the outcome a bachelor's capstone should aim for. She records these lessons for future students.

### Worked example

The thesis is submitted with approved sanitised appendices and passes with recommendations for publication as a case study.

> **Synthetic case.** The thesis is synthetic.

### Errors and limits

Theses that hide limitations invite harder questioning than those that state them clearly.

### Exercises

- **EX118 — Two audiences.** How did the two presentations differ? *Rubric:* 3 = examiners method and evidence; managers outcomes and costs;; 2 = audiences;; 1 = same;; 0 = none.
- **EX119 — Sanitising detail.** Give two details removed before submission. *Rubric:* 3 = real names, addresses, firewall models or passphrase policy;; 2 = two;; 1 = one;; 0 = none.
- **EX120 — Reflection lesson.** What did Priya find harder than the technical work? *Rubric:* 3 = people, suppliers, trust and data handling;; 2 = people;; 1 = vague;; 0 = none.

### Synthesis

The bachelor's route ends with a deployed, evidenced design and the professional skills to deliver it.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Priya Nair, Dr Tomasz Kowal, Northbridge University, Harbourside Community Clinics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** One visitor device successfully opening a connection to any clinical device.

**EX002.** Sixty-four, because two to the power six equals 64.

**EX003.** They are in the complement of the union of all planned sets and need investigating.

**EX004.** They share one local network and can reach each other; encryption only keeps outsiders out.

**EX005.** It can be changed in software and only has meaning on the local segment.

**EX006.** An infected visitor phone scanning other devices on the same network.

**EX007.** A list, because rule order determines which rule matches first.

**EX008.** Count and report them, so readers know how much data was excluded.

**EX009.** Between 0 and 65535 inclusive.

**EX010.** It is an opinion; a finding would be "visitor and clinical devices share one network".

**EX011.** The original is authoritative and checkable; summaries may distort it.

**EX012.** They summarise it after one reading; a mismatch shows unclear writing.

**EX013.** Blocking traffic to protect records could stop a needed service such as booking.

**EX014.** Detective: it helps find and investigate events but does not stop them.

**EX015.** The threat is the infected phone; the vulnerability is the shared network.

**EX016.** An indirect path, such as through a shared printer, may still connect the nodes.

**EX017.** Twelve, since each of four groups pairs with three others.

**EX018.** Count allowed group pairs and subtract those actually needed.

**EX019.** The clinical /25 covers .0 to .127, so .200 is outside every planned subnet.

**EX020.** Fourteen: sixteen addresses minus the network and broadcast addresses.

**EX021.** No; readdress the printer rather than silently enlarging the clinical group.

**EX022.** An address inside, one just outside, and the network address itself.

**EX023.** So it does not match similar text appearing elsewhere in the line.

**EX024.** It must never be executed or passed to a shell.

**EX025.** Every other control depends on knowing which devices exist.

**EX026.** It records which device held an address at any time, supporting investigations.

**EX027.** A staff member's home address, which serves no security purpose.

**EX028.** Scope of activities, data handling rules and a reporting contact.

**EX029.** Report it immediately through the agreed channel.

**EX030.** Device names and connection times can reveal rooms, patients or appointments.

**EX031.** It protects a device from others in its own group, which network firewalls do not filter.

**EX032.** Separation protects them while known vulnerabilities remain unpatched.

**EX033.** Saltzer and Schroeder's economy of mechanism and least privilege.

**EX034.** The data are skewed, and large transfers distort the mean.

**EX035.** About one of roughly 101 alerts is real.

**EX036.** Use rates, such as alerts per 100 devices per week.

**EX037.** The secret is shared, so revoking it means changing it for everyone.

**EX038.** Use device certificates, or place them on a restricted network with minimal access.

**EX039.** A monthly comparison of accounts against the HR staff list.

**EX040.** Content is not needed for the security purpose and would intrude on privacy.

**EX041.** Incidents are often found weeks later; much longer adds risk with little benefit.

**EX042.** Refuse, because it breaks the stated security purpose in the staff notice.

**EX043.** Cheap to collect, understandable, and hard to improve without real improvement.

**EX044.** Fewer visitors could explain the fall instead of the change.

**EX045.** The data source, date range and script version used.

**EX046.** Host firewalls limit access, and logging records attempts for investigation.

**EX047.** NIST SP 800-41r1, guidelines on firewalls and firewall policy.

**EX048.** Access to them would let an attacker change the network and undo every control.

**EX049.** Three of eight, 37.5 percent: lab-results, old-intranet and printer-ui.

**EX050.** It likely cannot be upgraded, so limiting who can reach it reduces exposure.

**EX051.** Users learn to click through browser warnings, weakening future protection.

**EX052.** "What share of clinic devices sit outside planned groups during one typical week?"

**EX053.** Logs show what happens; interviews explain why people behave that way.

**EX054.** Choosing a holiday week when usage is unusually low.

**EX055.** Once on the network, any device can reach any other, so one infection spreads.

**EX056.** With one part-time IT lead, full zero trust is unrealistic; partial steps reduce risk.

**EX057.** NIST SP 800-94.

**EX058.** Separating visitors, host firewalls on shared computers and logging.

**EX059.** Which suppliers currently have any form of remote access?

**EX060.** Users had learned to click through warnings, so the fake site's warning was ignored.

**EX061.** They do not affect who can reach what, which the model exists to answer.

**EX062.** DNS, which nearly every application flow depends on.

**EX063.** Heavy or misbehaving guest traffic could disrupt clinical name lookups.

**EX064.** Warning, because 132 modulo 8 is 4, the warning severity.

**EX065.** The critical configuration change and the repeated guest denies.

**EX066.** Alert when a device's hourly log count falls well below its usual range.

**EX067.** "Inter-group traffic is denied unless it is a listed needed flow."

**EX068.** A threat with no requirement addressing it shows a gap.

**EX069.** The risk of infected carts rose, so priorities were revisited.

**EX070.** Rule 1 denies all guest traffic before rule 3 can match.

**EX071.** It allows staff to reach everything, defeating group separation.

**EX072.** Allow DNS only to the clinic's own DNS servers.

**EX073.** To catch rules that block too much as well as too little.

**EX074.** A subnet typo let guests reach the management web page.

**EX075.** The real clinics have a printer shared between groups.

**EX076.** An infected guest device attacking other guests' devices.

**EX077.** So remote users reach only needed services, not the whole network.

**EX078.** A stolen device's certificate can be revoked without changing every site.

**EX079.** A rule allowing traffic that no test covered because nobody knew about it.

**EX080.** It stops malware using its own resolvers, and DNS logs can reveal infections.

**EX081.** It is either approved through change control or reverted.

**EX082.** A logging failure: traffic continues but is no longer recorded.

**EX083.** Provide a quick way to report blocked work and fix genuine needs within a day.

**EX084.** They are frequent and allow learning before any harm occurs.

**EX085.** A short routine fits a part-time role and will not be skipped.

**EX086.** They are allowed but recorded the same day and reviewed afterwards.

**EX087.** Documented procedures, a controlled credential record and an external support arrangement.

**EX088.** How long the real change window must be.

**EX089.** To revert calmly if critical tests have not passed by then.

**EX090.** Both the clinic IT lead and her tutor.

**EX091.** Segmentation keeping the remote access server away from the file server.

**EX092.** Detecting unknown devices and disabling unused network ports.

**EX093.** Through the VPN with individual accounts, limited to the supplier's systems.

**EX094.** Carts use device certificates so no login interrupts clinical work.

**EX095.** They show the clinics can demonstrate appropriate protection.

**EX096.** A first phase delivering guest separation only.

**EX097.** So the analysis cannot be changed to fit hoped-for results.

**EX098.** To confirm the two sources agree, so differences are real changes.

**EX099.** Cohen's kappa, interpreted with Landis and Koch's bands.

**EX100.** Its limited logging did not meet the detection needs identified earlier.

**EX101.** That the best option depends on how they weight criteria.

**EX102.** If internet links become more reliable and the clinics grow.

**EX103.** It is achievable in one term while still producing real evidence.

**EX104.** Ninety days of logs will not exist before the capstone ends.

**EX105.** Deploy guest separation a week before the full deployment.

**EX106.** It might have supported an important service, so she reported it instead.

**EX107.** It used the old shared network and was moved to the guest network.

**EX108.** Photos could capture patient information and break clinic rules.

**EX109.** 0.70, which Landis and Koch would call substantial agreement.

**EX110.** Half of agreement would occur by chance, so kappa adjusts for that.

**EX111.** Discussing cases influences labels and makes agreement look higher.

**EX112.** It used the restricted fallback network allowing only its specific flow.

**EX113.** An old shortcut to a retired application, removed after checking.

**EX114.** By rerunning the TLS audit script.

**EX115.** From twelve to four, the needed pairs only.

**EX116.** Guest devices keep retrying printer and file discovery, slowly decreasing.

**EX117.** The old intranet on TLS 1.1, scheduled for retirement.

**EX118.** Examiners heard method and evidence; managers heard outcomes, costs and next steps.

**EX119.** Real device names and exact firewall models.

**EX120.** Understanding clinical needs, working with suppliers and earning trust.

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
