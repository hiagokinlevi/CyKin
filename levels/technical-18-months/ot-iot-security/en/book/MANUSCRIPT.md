# OT, IoT and Cyber-Physical Security: A Technical Operator's Workbook

- Language: English (`en`); technical course, eighteen months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical operators and maintenance technicians who work on or beside industrial lines and must recognise, report and help recover from security problems.
- Relation to neighbouring books: the [professional course book](../../../../professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md) is shorter; the [technologist book](../../../../technologist-3-years/ot-iot-security/en/book/MANUSCRIPT.md) adds implementation and design. **This book is procedural and floor-focused.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to access real sites. All sites, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–4 explain the line, safety, networks and protocols; 5–13 cover the daily controls (register, accounts, media, vendor access, logs, advisories, backups, segmentation, IoT); 14–17 cover noticing, reporting, recovering and change control; 18 is the capstone walk-through. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, four exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 5, 9 and 11 read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Harbor Point Food Packaging Line (HPFL)** — filler PLC-FILL, wrapper PLC-WRAP, panel HMI-1, vision camera VIS-CAM, engineering laptop ENG-LT, firewall FW-1 | Line studied throughout | Invented |
| **Tomás Reyes** | Maintenance technician at HPFL | Invented |

### Core sources

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — What operational technology is on a packaging line

### Learning outcomes

You will (1) name the main OT components on a food packaging line; (2) explain why OT priorities differ from office IT; and (3) describe what can physically go wrong when a control system misbehaves.

### 1.1 The line as a system

A packaging line turns film, trays and product into sealed, labelled packs. Programmable logic controllers (PLCs) read sensors and drive motors, heaters and valves many times a second. Operator panels, called human-machine interfaces (HMIs), show the state of the line and let operators start, stop and adjust it. A vision camera rejects badly sealed packs. An engineering laptop holds the programs and is used to change them. NIST SP 800-82r3 calls this whole family operational technology: systems that monitor or control physical processes.

### 1.2 Why priorities differ

In an office, losing confidentiality of a spreadsheet is the classic harm. On a line, the first questions are: can someone get hurt, will food be unsafe, will the line stop? A sealing heater that runs too hot can burn a worker or leave packs unsealed and contaminated. That is why availability and safe behaviour come before confidentiality here, and why you never "just reboot" a controller to see what happens.

At HPFL this order shapes small decisions. Tomás does not unplug HMI-1 because it looks odd; he first asks the supervisor whether the line is safe to stop. A fix that protects data but leaves the sealing heater uncontrolled would be the wrong fix, however sensible it looks in an office.

### 1.3 What an attacker or a mistake can change

The same changes come from malice or error: a setpoint altered, a program replaced, an HMI locked, a network flooded. MITRE ATT&CK for ICS lists, for example, T0836 Modify Parameter. Your job as a technician is to notice such changes, report them and help restore safely — not to investigate devices by yourself.

Because the same change can come from either source, Tomás records what changed, when and on which device, without deciding why. On HPFL a changed wrapper speed could be an operator clearing a backlog or someone misusing a password; Chapter 9 shows a case where it was the first. The report is equally useful in both cases.

### Worked example (synthetic HPFL)

On his first shift, Tomás Reyes walks the line with the supervisor and draws it: filler PLC-FILL, wrapper PLC-WRAP, panel HMI-1, vision camera VIS-CAM, engineering laptop ENG-LT. Beside each box he writes one sentence on what happens physically if it fails. The wrapper sentence reads: "film stops, packs pile up, jam risk at the infeed."

> **Synthetic case — Harbor Point Food Packaging Line (HPFL).** The plant, Tomás Reyes and every number in this book are invented for teaching.

### Errors and limits

A drawing from one walk is incomplete; spare panels and wireless devices are easy to miss. Consequences are judged with operations staff, not alone.

### Exercises

- **EX001 — Naming the parts.** List four OT components of the HPFL line and the job of each. *Rubric:* 3 = four components each with a correct job; 2 = three; 1 = names only; 0 = none.
- **EX002 — Office versus line.** Explain in two sentences why "reboot it and see" is acceptable for an office PC but not for PLC-WRAP. *Rubric:* 3 = physical consequence plus safe-state/production argument; 2 = one reason; 1 = vague; 0 = none.
- **EX003 — Heater consequence.** Describe two harms if the sealing heater setpoint is raised far above normal. *Rubric:* 3 = burn/fire risk and unsafe or rejected packs; 2 = one; 1 = "it breaks"; 0 = none.
- **EX004 — One ATT&CK technique.** Which ATT&CK for ICS technique describes a changed setpoint, and could the same change be accidental? *Rubric:* 3 = T0836 Modify Parameter and yes, by error; 2 = technique only; 1 = wrong ID; 0 = none.

### Synthesis

OT security on a line starts from physical consequence: people, food and production come first.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Safety first: permits, consequence and who decides

### Learning outcomes

You will (1) explain how permits to work and lockout protect people; (2) state who has authority to stop or change the line; and (3) apply the rule that security work never bypasses safety controls.

### 2.1 Safety systems are not security tools

Light curtains, emergency stops and guard interlocks keep hands away from moving parts. They are designed and verified by safety engineers and they must keep working whatever happens to the network. A security technician never disables, bridges or reconfigures them, even "temporarily for testing".

On HPFL that covers the light curtains at the wrapper infeed, the emergency stops along the line and the interlocks on guard doors. If a security task seems to need one of them changed, the task is wrong, not the safety device. Stop and ask the supervisor, and record the question.

### 2.2 Permits and lockout

Work on a running plant needs a permit: a written record of who does what, where, when, which hazards exist and how they are controlled. Lockout/tagout isolates energy before hands go into a machine. Plugging a laptop into the wrapper's switch is also work on the plant: it can change traffic the PLC sees, so it goes through the same permit process.

The permit names the person in charge, the time window and what will be touched. At HPFL Tomás's permit for photographing the wrapper cabinet said that no tools would go inside and no connections would be made. Writing that down protects him as well as the line, because everyone knows what the task did and did not include.

### 2.3 Who decides

The shift supervisor decides whether the line runs. The controls engineer owns PLC programs. The quality manager decides whether product is safe to ship. Security staff advise and report; they do not make those decisions alone. Knowing this chain saves time in an incident because you call the right person first.

At HPFL that means a quality concern goes to the quality manager, a question about PLC logic to the controls engineer, and anything about stopping the line to the shift supervisor. Keep their names and numbers on the site sheet. When unsure who decides, ask the supervisor first; they will know who else to involve.

### 2.4 Stop conditions

Every task has written stop conditions: for example, stop if any alarm appears that is not explained, if an operator asks you to stop, or if a device behaves differently from the plan. Stopping is never a failure.

Write the stop conditions on the permit before starting, and agree them with the supervisor. When one occurs, stop work, make the area safe, tell the supervisor and record what happened. A task can resume later under a new or amended permit. Pressing on because the job is nearly finished is how small surprises become incidents.

### Worked example (synthetic HPFL)

Tomás needs to photograph the wrapper cabinet labels for the inventory. He asks the supervisor, who issues a permit for 10:00–10:20 during a planned film change, notes "cabinet door open, no tools inside, no connections", and names the electrician who opens the panel. Tomás photographs, the electrician closes the door, the permit is signed off.

> **Synthetic case — HPFL.** The permit and times are invented.

### Errors and limits

Permit forms vary by site; follow the local one. A permit does not make an unsafe task safe; it only records that hazards were considered.

### Exercises

- **EX005 — Light curtain request.** A colleague suggests bridging the wrapper light curtain while testing network traffic. What do you do? *Rubric:* 3 = refuse, safety systems untouched, escalate to supervisor/safety engineer; 2 = refuse only; 1 = ask for permission to bridge; 0 = agree.
- **EX006 — Why a laptop needs a permit.** Give one technical reason connecting ENG-LT to the line switch needs a permit. *Rubric:* 3 = can alter traffic/broadcasts seen by PLCs or push changes, affecting process; 2 = generic risk; 1 = "rules say so"; 0 = none.
- **EX007 — Matching decisions to people.** Who decides (a) whether the line runs, (b) whether a PLC program changes, (c) whether product ships? *Rubric:* 3 = supervisor, controls engineer, quality manager; 2 = two right; 1 = one; 0 = none.
- **EX008 — Writing stop conditions.** Write three stop conditions for photographing cabinet labels. *Rubric:* 3 = three specific, observable conditions; 2 = two; 1 = vague; 0 = none.

### Synthesis

Safety controls are untouchable, permits record the work, and named people make operational decisions.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Network basics on the line

### Learning outcomes

You will (1) read an IP address and subnet mask; (2) explain what switches, VLANs and firewalls do on a plant network; and (3) sketch the HPFL network from a description.

### 3.1 Addresses and subnets

Every networked device has an IP address such as 10.20.1.11. A /24 mask means the first three numbers name the network and the last names the device, so 10.20.1.11 and 10.20.1.12 are neighbours on 10.20.1.0/24. Devices on the same subnet can talk directly; traffic to another subnet goes through a router or firewall.

At HPFL the line devices share 10.20.1.0/24, so PLC-FILL, PLC-WRAP, HMI-1 and VIS-CAM can reach each other directly. Offices sit on 10.10.0.0/16, and traffic between the two must pass FW-1. Knowing this tells Tomás that a firewall rule is what decides whether an office PC can reach a PLC.

### 3.2 Switches and VLANs

A switch connects devices with cables. A VLAN splits one physical switch into separate logical networks, so the line devices and office PCs can share hardware without sharing traffic. A mistake in a VLAN setting can quietly connect two networks that were meant to be apart, which is why switch changes need the same care as PLC changes.

At HPFL the line is on VLAN 20 and offices on VLAN 10. If a port on a shared switch were set to the wrong VLAN, an office PC plugged into it would land on the line network without passing FW-1. Report any doubt about a port's VLAN to the network owner rather than testing it.

### 3.3 Firewalls

A firewall forwards or blocks traffic between networks according to rules: source, destination, port and action. On a plant, the important firewall sits between the office network and the line. Good rules name specific hosts and ports; "any to any" rules defeat the purpose.

At HPFL, FW-1 should allow ENG-LT to reach the PLCs and little else. Each rule should have a comment saying why it exists and who owns it. Chapter 12 shows how to read FW-1's table and what to do with a rule that has no owner.

### 3.4 Unmanaged switches and wireless

Small unmanaged switches inside cabinets and wireless bridges are common and are often missing from drawings. They matter because they create connections nobody reviews.

Look for them during walk-downs: a small switch inside a cabinet with more cables than expected, or a wireless bridge on a mast. Photograph what you find and report it with its location. A device that joins the line network to another network without passing FW-1 makes the firewall rules irrelevant for that path.  Ask the network owner whether each one is known and approved.

### 3.5 Addresses you should not assume

Devices can have a second network card, a serial port or a cellular modem that does not show on the drawing. Ask the owner for every interface, not just the main address.

Record each interface in the register, not only the main IP address. A cellular modem added by a machine builder for remote support is a common example, and it can bypass FW-1 entirely. If the owner does not know whether a device has other interfaces, check the manual or ask the supplier before assuming it does not.

### Worked example (synthetic HPFL)

The controls engineer tells Tomás: line devices use 10.20.1.0/24 on VLAN 20, offices use 10.10.0.0/16 on VLAN 10, a firewall FW-1 joins them, and only ENG-LT may reach the PLCs. Tomás draws two boxes, puts PLC-FILL (10.20.1.11), PLC-WRAP (10.20.1.12), HMI-1 (10.20.1.21) and VIS-CAM (10.20.1.31) in the line box, and writes the one allowed rule on FW-1.

> **Synthetic case — HPFL.** Addresses and VLAN numbers are invented.

### Errors and limits

A drawing describes intent; actual cabling may differ. Confirm against switch configuration with the network owner, never by probing devices.

### Exercises

- **EX009 — Same subnet?** Are 10.20.1.31 and 10.20.2.31 on the same /24 network? Explain. *Rubric:* 3 = no, third octet differs so different /24; 2 = no without reason; 1 = yes; 0 = none.
- **EX010 — VLAN mistake.** What could happen if the port for an office printer is set to VLAN 20 by mistake? *Rubric:* 3 = printer joins line network, bypassing FW-1, creating unreviewed path; 2 = "wrong network" only; 1 = printer stops; 0 = none.
- **EX011 — Rule quality.** Rewrite "any → 10.20.1.0/24 any allow" into a rule matching the HPFL intent. *Rubric:* 3 = source ENG-LT address only, destination PLCs, required port, allow, plus default deny; 2 = host-specific without deny; 1 = still broad; 0 = none.
- **EX012 — The hidden switch.** Why does an unmanaged switch found in the wrapper cabinet matter for security? *Rubric:* 3 = unreviewed connection point, no logging/VLAN control, may extend network; 2 = one point; 1 = "it's old"; 0 = none.

### Synthesis

Addresses, VLANs and firewall rules decide who can talk to a controller; mistakes in them silently open paths.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Industrial protocols at the operator's level

### Learning outcomes

You will (1) describe what Modbus/TCP and similar industrial protocols carry; (2) explain why many lack authentication; and (3) recognise normal versus unusual protocol use from a description.

### 4.1 What the protocols carry

HMIs and PLCs exchange values: temperatures, speeds, counts, start and stop bits. Modbus, published by the Modbus Organization, is one widely used example; over Ethernet it is called Modbus/TCP and normally uses port 502. A request says "read registers 100–110" or "write value 180 to register 205". Other common families include EtherNet/IP and PROFINET; the idea is similar.

At HPFL HMI-1 reads values from PLC-FILL and PLC-WRAP such as speeds and temperatures, and sends writes when operators press buttons. ENG-LT uses a separate programming connection to change PLC logic. Knowing which connections are expected is what lets anyone notice an unexpected one.

### 4.2 Why authentication is missing

Classic Modbus has no built-in way to check who sends a request. If a device can reach the PLC on port 502, it can usually read and often write. This was acceptable when the network was a closed cable inside a cabinet. It is not acceptable once that network connects to offices or the internet, which is why segmentation (Chapter 12) carries so much weight.

At HPFL this means that the firewall and VLANs are the main protection for PLC-FILL and PLC-WRAP. If an office PC could reach port 502 on either PLC, it could send writes that look exactly like those from HMI-1. Report any sign of such a path immediately, without trying it.

### 4.3 Normal patterns

On a healthy line the pattern is boring: HMI-1 reads the same registers every second, and writes happen when operators press buttons. A new device sending writes, or reads of unusual register ranges, is worth reporting. You do not need to decode packets yourself; you need to know what normal looks like and who to call.

Writing the normal pattern down also helps after changes. If a new device is added to the line, the expected pattern is updated in the same change ticket. A monitoring tool run by the network owner can then compare actual traffic with the written pattern, as in Tomás's notebook entry.

### 4.4 Do not experiment

Sending test requests to a live PLC can change outputs. Protocol learning happens on a simulator or a lab PLC, never on the line.

The controls engineer can arrange time on a lab PLC or simulator if you want to practise. Even read requests to a live controller add load and can disturb older devices. If you are curious about what a register holds, ask the engineer rather than querying the PLC on the line.  Learning on a lab PLC lets you make mistakes safely and see their effects without risk.

### Worked example (synthetic HPFL)

The controls engineer shows Tomás a summary from the line's monitoring tool: HMI-1 reads PLC-WRAP every second; ENG-LT connected twice last month during approved changes. Tomás notes "writes only from HMI-1 and ENG-LT" as the expected pattern in his notebook.

> **Synthetic case — HPFL.** The monitoring summary is invented.

### Errors and limits

Some newer protocol versions add security features, but plants run old devices for decades; assume the weakest common case unless the owner confirms otherwise.

### Exercises

- **EX013 — A write request.** In plain words, what does "write 180 to register 205" do on PLC-WRAP if register 205 is wrapper speed? *Rubric:* 3 = sets speed to 180, physical change immediately; 2 = changes a value; 1 = reads; 0 = none.
- **EX014 — Port 502 reachable.** A vendor tablet on the line VLAN can reach port 502 on PLC-FILL. Why is that a concern? *Rubric:* 3 = no authentication so tablet can read/write process values; 2 = "unauthorised access"; 1 = slow network; 0 = none.
- **EX015 — Spot the unusual one.** Which is unusual: (a) HMI-1 reading every second, (b) VIS-CAM writing to PLC-WRAP, (c) ENG-LT during an approved change? *Rubric:* 3 = (b) with reason; 2 = (b) only; 1 = other; 0 = none.
- **EX016 — Learning safely.** Where should Tomás practise sending Modbus requests, and why not on the line? *Rubric:* 3 = simulator/lab PLC; requests change live outputs; 2 = place only; 1 = "after hours on line"; 0 = none.

### Synthesis

Industrial protocols move process values with little or no authentication, so reachability equals control.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Keeping an asset register

### Learning outcomes

You will (1) list the fields a useful OT asset register needs; (2) find gaps in a register with a short script; and (3) explain why an incomplete register delays incident response.

### 5.1 What to record

For every device: identifier, location, zone or VLAN, owner, make and model, firmware version, network address and what it controls. NIST SP 800-82r3 treats inventory as a foundation because every later activity — patching, monitoring, incident response — depends on knowing what exists.

At HPFL the register covers PLC-FILL, PLC-WRAP, HMI-1, VIS-CAM and ENG-LT, and later the IoT sensors. Each field answers a question someone will ask in a hurry: whom to call, which firmware, which address. A missing field is a finding to fix, not a blank to tolerate.

### 5.2 Where the data comes from

Purchase records, contractor drawings, cabinet labels, the engineering software project and, carried out by the network owner, passive network monitoring. Each source misses something, so they are compared.

```python
"""Lab 5: check a synthetic HPFL asset register for missing owner or firmware fields (no scanning)."""
reg = [
    {"id": "PLC-FILL", "zone": "line", "owner": "maintenance", "fw": "3.2"},
    {"id": "PLC-WRAP", "zone": "line", "owner": "maintenance", "fw": ""},
    {"id": "HMI-1", "zone": "line", "owner": "", "fw": "n/a"},
    {"id": "VIS-CAM", "zone": "line", "owner": "quality", "fw": "1.0.7"},
    {"id": "ENG-LT", "zone": "office", "owner": "controls", "fw": "n/a"},
]
for r in reg:
    gaps = [k for k in ("owner", "fw") if not r[k]]
    print(f"{r['id']:9} zone={r['zone']:7} {'OK' if not gaps else 'MISSING ' + ','.join(gaps)}")
print("complete:", sum(1 for r in reg if r["owner"] and r["fw"]), "of", len(reg))
```

Run with `python3 lab_assets.py`. Verified output:

```text
PLC-FILL  zone=line    OK
PLC-WRAP  zone=line    MISSING fw
HMI-1     zone=line    MISSING owner
VIS-CAM   zone=line    OK
ENG-LT    zone=office  OK
complete: 3 of 5
```

At HPFL Tomás used photographs of cabinet labels to fill the missing firmware version for PLC-WRAP. Where two sources disagree, record both and ask the owner which is right. Never fill gaps by probing devices on the line; monitoring is done only by the network owner, passively.

### 5.3 Reading the result

The script prints which records are incomplete. PLC-WRAP has no firmware recorded, so nobody can tell whether a new advisory applies. HMI-1 has no owner, so nobody would be called if it misbehaved. Three of five records are complete; that ratio is a simple measure to track each month.

The fix for each gap is a question to the right person. Firmware can come from a cabinet label or from the controls engineer's software; ownership comes from the supervisor. Rerunning the script after each answer shows progress, as Tomás's rerun did when all five records became complete.

### 5.4 Keeping it alive

A register is only useful if it is updated when things change. Tie updates to change tickets: no device is installed, moved or replaced without the record changing in the same ticket.

Add a register check to the change ticket template so it cannot be skipped. Once a month, compare the register with what the network owner's monitoring sees and with a walk-down of cabinets. Any device seen but not registered is reported and added, or removed if nobody can explain it.

### 5.5 Spares and retired devices

Spare PLCs on a shelf and devices removed from service belong in the register too, marked as spare or retired. A spare loaded with an old program may be installed in a hurry during a breakdown, and a retired HMI thrown in a skip may still hold passwords and network settings.

Before a spare is installed, check that its program matches the verified backup of the device it replaces. Before a retired device leaves the site, wipe it according to the vendor's instructions and record that it was done. Both steps belong in the register entry for that device.

### Worked example (synthetic HPFL)

Tomás uses the cabinet photographs from Chapter 2 to read PLC-WRAP's firmware label: 2.0. He asks the supervisor who owns HMI-1; the answer is "operations", so he records it. A rerun of the script now shows five of five complete.

> **Synthetic case — HPFL.** The register and labels are invented.

### Errors and limits

Labels can be out of date after a firmware update; confirm through the engineering software with the controls engineer. A register is sensitive: it is a map for attackers too, so store it with access control.

### Exercises

- **EX017 — Missing fields.** Name two fields PLC-WRAP was missing or could be missing that matter during an advisory. *Rubric:* 3 = firmware version and model/make; 2 = one; 1 = colour or unrelated; 0 = none.
- **EX018 — Ratio after fixes.** If HMI-1's owner is filled but PLC-WRAP's firmware is still blank, what does the last line print? *Rubric:* 3 = "complete: 4 of 5"; 2 = 4 without format; 1 = 5; 0 = none.
- **EX019 — Linking to change.** Propose a rule that keeps the register current. *Rubric:* 3 = every install/move/replace ticket must update register before closure; 2 = periodic review only; 1 = "be careful"; 0 = none.
- **EX020 — Protecting the register.** Give one reason the register should not be on a public share. *Rubric:* 3 = reveals addresses, versions and targets to attackers; 2 = "confidential"; 1 = it's big; 0 = none.

### Synthesis

A complete, current, protected register is the base on which every other OT security task stands.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Accounts and passwords on HMIs and engineering tools

### Learning outcomes

You will (1) explain the risks of shared and default accounts; (2) apply simple account practices that work on a shift floor; and (3) handle a forgotten or leaked password correctly.

### 6.1 Shared accounts

Many HMIs ship with one "operator" account used by every shift. Then logs say "operator did it" and nobody knows who. Where the system supports it, give each person their own account; where it does not, record who was on shift and keep the shared password known only to the crew.

At HPFL the admin account on HMI-1 was used by operators to change wrapper speed, as Chapter 9 shows, which made the change hard to trace. Named accounts, or at least a shift log of who held the shared password, would have shown the person at once.

### 6.2 Default passwords

Default credentials are published in manuals, so anyone can look them up. ETSI EN 303 645 makes "no universal default passwords" its first provision for consumer IoT, and the same idea applies to plant devices: change defaults before a device goes into service.

At HPFL, check defaults on every new device before it joins the line network, including the vision camera and IoT sensors. Record in the register that the default was changed and when. If a device cannot change its default, report it so the owner can decide on other controls.

### 6.3 Privileged accounts

Admin accounts on HMI-1 and the engineering software can change screens, users and logic. They are used only for planned work, by named people, and their use is reviewed. They are not the everyday login.

At HPFL the admin password on HMI-1 was found on a sticky note on the panel, which shows how quickly privileged access spreads when it is used for everyday tasks. Review admin logins regularly against planned work, and remove admin rights from people whose roles no longer need them.

### 6.4 Practical rules

Use passphrases that are long but typeable with gloves; do not write passwords on the panel; lock the screen or log out when leaving; never share a password over the radio or by text.

These rules suit a shift floor where people wear gloves, share panels and work under time pressure. If a rule cannot be followed in practice, report that rather than quietly ignoring it; the owner may find a better way, such as a badge-based login.  Review the rules with each new shift team.

### 6.5 When a password leaks

Report it, then the owner changes it at a time that will not disturb the line. Look at recent logins for that account (Chapter 9).

At HPFL, when Tomás found the admin password on a sticky note, the controls engineer changed it at the next planned stop and checked the login log for unexpected admin sessions. Record the leak, the change and the review in one report.  Look for logins at odd hours or from unexpected places, and for setpoint changes that nobody can explain. Tell the shift team when the new password is in use.

### Worked example (synthetic HPFL)

Tomás notices a sticky note on HMI-1 reading "admin / Harbor2024". He photographs it as evidence, removes it, tells the supervisor and the controls engineer, and writes a short report. The engineer changes the admin password at the next planned stop and checks the login log for unexpected admin sessions.

> **Synthetic case — HPFL.** The note and password are invented.

### Errors and limits

Some old HMIs cannot hold individual accounts; compensate with shift logs and physical control. Changing a password on a running system can lock out operators if done carelessly.

### Exercises

- **EX021 — Logs and shared logins.** Why does a single shared "operator" login weaken an investigation? *Rubric:* 3 = cannot attribute actions to person; need shift records; 2 = "less secure"; 1 = vague; 0 = none.
- **EX022 — Default credential risk.** Explain why default passwords are dangerous even on an isolated line. *Rubric:* 3 = published, anyone with physical/network reach (contractor, laptop) can log in; isolation imperfect; 2 = one point; 1 = "hackers"; 0 = none.
- **EX023 — The sticky note.** List Tomás's steps in order after finding the note. *Rubric:* 3 = photograph, remove, report to supervisor/engineer, password changed at planned stop, logs checked; 2 = most; 1 = just remove; 0 = none.
- **EX024 — Daily login choice.** Should the controls engineer use the admin account for routine monitoring? Why? *Rubric:* 3 = no; least privilege, reduces accidental change and misuse; 2 = no only; 1 = yes; 0 = none.

### Synthesis

Named accounts, changed defaults and limited admin use make actions traceable and harder to abuse.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Removable media and laptops

### Learning outcomes

You will (1) explain how USB drives and laptops carry malware into plants; (2) apply a scanning and logging routine for media; and (3) decide which laptops may connect to the line.

### 7.1 How malware crosses the gap

Lines without internet links still receive files: firmware updates, recipe files, vendor tools and photos. Each comes on a USB drive or laptop that has been elsewhere. NIST SP 800-82r3 lists removable media as a common path into OT, and well-known incidents spread exactly this way.

At HPFL a vendor arriving with a recipe file on a personal drive is a routine event. The file may be harmless, but the drive has been in other plants and offices. Treat every file entering the line as needing the same routine, however trusted its source.

### 7.2 A media routine

Use only drives issued by the site. Before any drive reaches a line device, scan it on a dedicated, up-to-date scanning station outside the line, record the drive number, file names, scan result and person in a log, and keep the drive under control until it is used. Unknown drives found on the floor are handed to security, never plugged in "to see whose it is".

At HPFL the scanning station sits outside the line, and site drives are numbered, such as HP-07. The log lets anyone trace a file back to its source if a problem appears later. Check the log during walk-throughs; a drive missing from it is a finding.

### 7.3 Laptops

Only ENG-LT and approved vendor laptops connect to line equipment. An approved laptop is patched, runs anti-malware, has no personal software and is checked before each visit. A vendor laptop that cannot meet that standard uses a site-owned laptop with the vendor's tools installed instead.

Keep a list of approved laptops in the register with their owner and the date each was last checked. At HPFL ENG-LT is the only site laptop allowed to program the PLCs. A vendor laptop that cannot be checked does not connect; the vendor uses a site laptop with their tools instead.

### 7.4 Transferring files without USB

Some sites move files through a controlled transfer server in the DMZ instead of drives. That keeps a record of every file and removes the need to plug media into line devices at all.

At HPFL the DMZ already holds a file transfer server. Files arriving there can be scanned automatically and logged with sender and time, and line devices fetch them through a documented conduit. Removing drives from the routine also removes the risk of a drive being lost on the floor.

### Worked example (synthetic HPFL)

A vendor arrives with a recipe file on a personal drive. Tomás takes the drive to the scanning station, copies the file onto site drive HP-07 after a clean scan, logs "HP-07, recipe_v12.csv, clean, Tomás, 09:30", and hands HP-07 to the controls engineer. The personal drive goes back to the vendor unplugged from anything on the line.

> **Synthetic case — HPFL.** The vendor, drive numbers and file are invented.

### Errors and limits

A clean scan only means no known malware was found; new malware can pass. Keep the routine anyway: it cuts most risk and gives a record if something goes wrong.

### Exercises

- **EX025 — Found on the floor.** A USB stick labelled "Wages 2026" lies by HMI-1. What do you do? *Rubric:* 3 = do not plug in; hand to security/supervisor; record where found; 2 = hand in only; 1 = check on office PC; 0 = plug into HMI.
- **EX026 — Media log fields.** List four fields in the media log. *Rubric:* 3 = drive id, files, scan result, person and time; 2 = three; 1 = one; 0 = none.
- **EX027 — Clean scan meaning.** A colleague says "the scan was clean, so the file is safe". Correct the statement. *Rubric:* 3 = only no known malware found; new threats possible; routine still reduces risk; 2 = partial; 1 = agree; 0 = none.
- **EX028 — Vendor laptop refusal.** The vendor's laptop has no anti-malware. What alternative lets the work proceed? *Rubric:* 3 = site-owned laptop with vendor tools, or transfer files via scanning station; 2 = reschedule only; 1 = allow anyway; 0 = none.

### Synthesis

Every file entering the line passes a scanned, logged, controlled path; unknown media never touch line devices.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Remote access for vendors

### Learning outcomes

You will (1) describe how vendors reach plant systems remotely; (2) explain lessons from the 2021 Oldsmar water advisory; and (3) run a remote session following a simple checklist.

### 8.1 Why vendors connect

Machine builders support their equipment remotely to diagnose faults without travelling. That is useful, but a permanent, always-on link into the line is also a permanent way in for anyone who steals the credentials.

At HPFL the wrapper builder occasionally needs to read fault logs. That need is real, and refusing all remote access would mean waiting days for a visit. The answer is to allow access only through a controlled route, for a specific job, under the site's watch.

### 8.2 What the advisory found

CISA advisory AA21-042A describes the compromise of a U.S. water treatment facility in 2021 in which remote access software was used to reach a control system. Its recommendations include using multi-factor authentication, strong passwords for remote desktop, closing unused remote desktop ports and auditing remote connections. Those points apply directly to a packaging line.

At HPFL that means checking that no remote desktop software runs directly on HMI-1 or ENG-LT, that vendor accounts use multi-factor authentication, and that remote sessions are logged and reviewed. The lessons meeting in Chapter 16 later found a remote desktop port on HMI-1 opened by a contractor, exactly the kind of route the advisory warns about.

### 8.3 A safer pattern

Remote access goes through one site-controlled gateway in the DMZ, never software installed directly on HMIs. Each vendor has a named account with multi-factor authentication. The connection is disabled by default and enabled for a ticketed session window. Someone at the site watches the session and can end it. Sessions are logged and reviewed.

Write the pattern into a short procedure that vendors receive before their first session. The supervisor opens a ticket with a time window; the technician enables the account and watches. If a vendor asks for permanent access, the request goes to the supervisor and is normally refused.

### 8.4 Ending the session

When work finishes, the account is disabled again, the change is recorded, and the operator confirms the line behaves normally. A session left enabled "for next time" is the commonest failure.

At HPFL Tomás disabled the vendor's account at 14:38, before the window closed, and recorded the start and end times in the ticket. Check vendor accounts weekly to confirm none are left enabled. An account found enabled outside a ticket is reported as a finding.  Confirm also that the vendor's change appears in the register.

### Worked example (synthetic HPFL)

The wrapper builder needs to read a fault log. The supervisor opens ticket 4471 for 14:00–14:45. Tomás enables the vendor's gateway account, watches the screen share, sees the engineer only open the fault viewer, and disables the account at 14:38. He records the session in the ticket with start and end times.

> **Synthetic case — HPFL.** The ticket, vendor and times are invented.

### Errors and limits

Some machines arrive with built-in cellular modems for vendor support; they bypass the gateway entirely and must be found and controlled. Watching a session cannot catch everything; logging and review add a second check.

### Exercises

- **EX029 — Advisory recommendations.** Name three recommendations from AA21-042A. *Rubric:* 3 = three of MFA, strong RDP passwords, close unused RDP ports, audit remote connections; 2 = two; 1 = one; 0 = none.
- **EX030 — Always-on link.** Explain why "the vendor link is always on so support is faster" is a risk. *Rubric:* 3 = permanent entry for stolen credentials, unattended use; 2 = vague risk; 1 = agree; 0 = none.
- **EX031 — Session record.** What should Tomás write in ticket 4471 after the session? *Rubric:* 3 = vendor name/account, start/end, what was done, account disabled, line normal; 2 = some; 1 = "done"; 0 = none.
- **EX032 — The hidden modem.** During a walk-down Tomás finds a cellular modem in the filler cabinet. Why is it important? *Rubric:* 3 = bypasses gateway/MFA/logging, unmanaged path; report to owner; 2 = one; 1 = remove it himself; 0 = none.

### Synthesis

Vendor access is through one gateway, named and multi-factor, enabled only for watched, logged windows.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Reading logs and alarms

### Learning outcomes

You will (1) tell process alarms from security-relevant events; (2) filter a log with a short script; and (3) decide when a pattern needs escalation.

### 9.1 Two kinds of messages

HMIs and PLCs report process alarms such as low film or a jam. They also record logins, setting changes and program downloads. Process alarms are handled by operators; the second kind tells you who did what to the system, and that is where security clues usually appear.

At HPFL low film and jam alarms belong to operators. Logins, setpoint changes and program downloads are the records to export and keep. Separating the two keeps the security review short enough to happen every day.

### 9.2 Patterns that matter

Several failed logins followed by a success can mean someone guessed a password. A setpoint changed outside a planned job, a program download nobody expected, or an admin login at an odd hour all deserve a look. One event alone is often innocent; the sequence is what matters.

```python
"""Lab 9: filter a synthetic HMI event log for security-relevant entries."""
log = """06:02 HMI-1 login operator1 ok
06:15 PLC-FILL alarm low-film
07:40 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:41 HMI-1 login admin fail
07:43 HMI-1 login admin ok
07:45 PLC-WRAP setpoint speed 120->180 by admin
08:10 PLC-FILL alarm jam-cleared"""
fails = 0
for line in log.splitlines():
    t, dev, kind, *rest = line.split()
    if kind == "login" and rest[-1] == "fail":
        fails += 1
    if kind == "setpoint" or (kind == "login" and rest[0] == "admin" and rest[-1] == "ok"):
        print("REVIEW", line)
print("failed logins:", fails)
```

Run with `python3 lab_logs.py`. Verified output:

```text
REVIEW 07:43 HMI-1 login admin ok
REVIEW 07:45 PLC-WRAP setpoint speed 120->180 by admin
failed logins: 3
```

At HPFL the lab shows exactly this kind of sequence: three failed admin logins, a success, then a speed change two minutes later. Each event alone could be ignored. Together they raise a question that needs an answer from the supervisor.

### 9.3 Reading the output

The script counts three failed admin logins, then shows a successful admin login at 07:43 and a wrapper speed change from 120 to 180 two minutes later. Together that is a story worth checking: was a planned change happening at 07:45, and who was logged in?

The script does not explain what happened; it only picks out lines worth asking about. The next step is to check whether a change was planned and who was on shift. At HPFL the answer turned out to be innocent, but the sequence was still worth checking.

### 9.4 Escalate, do not investigate alone

Tomás's job is to notice and report with evidence: the log lines, the time, what the line did. The controls engineer and security lead decide what happens next.

Report with the log lines attached, the time you noticed them and what the line was doing then. Do not log into devices to look further or change passwords yourself. If the controls engineer asks for more evidence, they will tell you what to collect and how.  Keep a copy of what you reported and when you sent it.

### 9.5 Time matters

Logs are only comparable if device clocks agree. Note any clock difference you know of in your report.

If HMI-1 and PLC-WRAP disagree by several minutes, a setpoint change might appear to happen before the login that caused it. Ask the controls engineer how clocks are set on the line and record any known offset in the register.  When you export logs, note the time on your watch and the time shown on each device, so the difference can be corrected later. A clock that drifts by minutes can make an innocent sequence look suspicious, or hide a suspicious one.

### Worked example (synthetic HPFL)

Tomás asks the supervisor; no change was planned. The night operator says he forgot the admin password, tried three times, then remembered it and raised speed to clear a backlog. The change is reverted, recorded, and admin use for speed changes is withdrawn from operators.

> **Synthetic case — HPFL.** The log and explanation are invented.

### Errors and limits

Logs on small devices are short and may overwrite themselves within days, so export them regularly. An innocent explanation should still be recorded.

### Exercises

- **EX033 — Classifying entries.** Which lines in the lab log are process alarms and which are security-relevant? *Rubric:* 3 = low-film and jam-cleared process; logins and setpoint security; 2 = mostly; 1 = one; 0 = none.
- **EX034 — Five failures.** If two more failed admin lines are added before 07:43, what does the last line print? *Rubric:* 3 = "failed logins: 5"; 2 = 5; 1 = 3; 0 = none.
- **EX035 — Why sequence matters.** Explain why the 07:43 login matters more after the failures than alone. *Rubric:* 3 = success after failures suggests guessing; tied to setpoint change; 2 = one point; 1 = "it's admin"; 0 = none.
- **EX036 — Report content.** Write the four facts Tomás includes when reporting the 07:45 change. *Rubric:* 3 = time, device, change values, account/login sequence (plus line effect); 2 = three; 1 = one; 0 = none.

### Synthesis

Security clues sit in login and change records; sequences, not single lines, justify escalation.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Patches and security advisories

### Learning outcomes

You will (1) read an ICS advisory and find the facts that matter; (2) match an advisory to the asset register; and (3) explain why plants often mitigate before they patch.

### 10.1 Where advisories come from

Vendors and CISA publish advisories for industrial products; CISA's index lists them with product names, affected versions, impact and mitigations. An advisory is the starting point, not the decision.

At HPFL the controls engineer and Tomás check advisories for the makers of PLC-FILL, PLC-WRAP, HMI-1 and VIS-CAM. Matching each one against the register tells them quickly whether any action is needed, and the register's firmware fields make that possible.  Note in the record where each advisory came from and when it was read, and whether it has since been revised.

### 10.2 Reading one

Find five facts: product and model, affected versions, what an attacker could do, whether it needs network or physical access, and the vendor's fix or workaround. Then look up the register: do we have that model, at that version, reachable in that way?

At HPFL the advisory affecting PLC-WRAP needed network access to its programming port, and FW-1 already allowed that only from ENG-LT. Answering the five questions made that clear within minutes. Record the answers in the advisory record, even when the result is that no action is needed.

### 10.3 Why not patch immediately

A firmware update on a PLC stops it, may change behaviour and needs testing with the program. Food plants also need quality checks after changes. So the usual order is: confirm exposure, apply a mitigation quickly (for example, block the vulnerable service at the firewall), then schedule the patch for a planned stop with a rollback plan.

At HPFL the mitigation for PLC-WRAP was already in place on FW-1, and the patch was scheduled for a planned stop three weeks later. The rollback plan should name the saved program and firmware version to return to if the update causes problems.

### 10.4 Recording the decision

Each advisory gets a record: applies or not, why, mitigation, planned patch date, owner. A decision not to patch, with reasons and a review date, is still a decision.

Keep the records in one place, linked to the register, so that a later reader can see which advisories were considered and why. Review open items monthly. A record without a review date tends to be forgotten.  At HPFL the record for the PLC-WRAP advisory named FW-1's existing rule as the mitigation and gave the date of the planned stop for the patch. When the patch is applied, the record is closed with the new firmware version.

### 10.5 HMI and laptop updates

Windows-based HMIs and ENG-LT also need operating system updates, but only those the HMI vendor has approved, installed during planned stops.

Ask the HMI vendor which updates are approved, and record each update in the register and change ticket. Test after updating that screens show correct values and that HMI-1 still communicates with both PLCs. Updates for ENG-LT follow the same planned approach.  Keep the previous image or restore point so the update can be undone if screens or communication fail. Never let an HMI update itself automatically from the internet; that would need a connection the line should not have.

### Worked example (synthetic HPFL)

A synthetic advisory states that firmware 2.0 of the wrapper's PLC model allows unauthenticated program changes over the network. The register (after Chapter 5) says PLC-WRAP runs 2.0. The controls engineer confirms FW-1 already blocks the programming port from everything except ENG-LT, records that as the mitigation, and schedules firmware 2.3 for the next planned stop in three weeks.

> **Synthetic case — HPFL.** The advisory and versions are invented; real advisories are at cisa.gov.

### Errors and limits

Advisories can be revised; recheck before acting. Version strings may be reported differently on labels and in software.

### Exercises

- **EX037 — Five facts.** List the five facts to extract from an advisory. *Rubric:* 3 = product/model, versions, impact, access needed, fix/workaround; 2 = four; 1 = two; 0 = none.
- **EX038 — Does it apply?** An advisory affects versions before 2.2 of PLC-FILL's model; PLC-FILL runs 3.2. Applies? *Rubric:* 3 = no, 3.2 is later, record as not applicable with reason; 2 = no; 1 = yes; 0 = none.
- **EX039 — Mitigate first.** Why does the engineer mitigate at FW-1 before patching PLC-WRAP? *Rubric:* 3 = patch needs stop/testing/quality; firewall reduces exposure now; 2 = one; 1 = "lazy"; 0 = none.
- **EX040 — Record of a deferred patch.** Write the advisory record for PLC-WRAP. *Rubric:* 3 = applies, reason, mitigation, planned date, owner, review; 2 = most; 1 = "patch later"; 0 = none.

### Synthesis

Advisories are matched against the register, mitigated quickly and patched at a planned, tested stop.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Backups and restore

### Learning outcomes

You will (1) list what must be backed up on a line; (2) verify backup integrity with hashes; and (3) explain why a restore must be tested.

### 11.1 What to back up

PLC programs, HMI projects and screens, recipe files, device configurations (switches, firewall, camera settings) and the engineering software licence details. Without them, recovering from failure or attack means rebuilding from memory.

At HPFL that means programs for PLC-FILL and PLC-WRAP, HMI-1's project, recipe files, VIS-CAM's settings and the configurations of FW-1 and the line switches. List each item in the register with the date of its latest backup. An item missing from the list is likely to be missing from the backups too.

### 11.2 Where to keep backups

At least one copy off the line network, ideally offline, so malware that encrypts the line cannot reach it. Label each with device, date and version.

At HPFL the controls engineer keeps an offline store, which is where an older matching copy of the wrapper program was found. Keep at least two copies of each important backup, and record where each is. Check that the offline copy can be reached during a night shift.  Note who may take a copy off site.

### 11.3 Checking integrity

A hash such as SHA-256 is a fingerprint of a file: any change gives a different value. Record the hash when the backup is made; check it before restoring.

```python
"""Lab 11: verify synthetic PLC backup files against recorded SHA-256 values."""
import hashlib
files = {"PLC-FILL_2026-09.bak": b"fill program v3.2 rungs 1-140",
         "PLC-WRAP_2026-09.bak": b"wrap program v2.0 rungs 1-88 edited"}
recorded = {"PLC-FILL_2026-09.bak": hashlib.sha256(b"fill program v3.2 rungs 1-140").hexdigest(),
            "PLC-WRAP_2026-09.bak": hashlib.sha256(b"wrap program v2.0 rungs 1-88").hexdigest()}
for name, data in files.items():
    h = hashlib.sha256(data).hexdigest()
    print(f"{name:22} {h[:12]} {'MATCH' if h == recorded[name] else 'MISMATCH - do not restore'}")
```

Run with `python3 lab_hash.py`. Verified output:

```text
PLC-FILL_2026-09.bak   0278a5f83d56 MATCH
PLC-WRAP_2026-09.bak   9974ecb17bab MISMATCH - do not restore
```

Store the hashes separately from the backups, for example in the change ticket or a register, so that someone who alters a backup cannot also alter its hash. Lab 11 checks two backup files against recorded hashes and shows what a mismatch looks like.

### 11.4 Reading the result

The filler backup matches its recorded hash. The wrapper backup does not: its content was edited after the hash was recorded. Restoring it could load a program nobody approved, so it is set aside and reported.

A mismatch does not prove an attack; it proves the file changed after its hash was recorded. At HPFL the edit was traced to an approved but unrecorded adjustment. The procedure was updated so that every change produces a new backup and hash in the same ticket.

### 11.5 Test restores

A backup never restored is a hope, not a plan. Once or twice a year, restore a program to a spare or lab PLC and compare it with the running one.

Record the test restore in the register with the date, the device, the backup used and the result. If a restore fails, find out why before a real failure forces the question. At HPFL a spare PLC from the shelf could be used for this, after checking it is marked as spare in the register.

### 11.6 How often

Back up after every approved change and on a fixed monthly date, whichever comes first, so the newest good copy is never far behind the running program.

At HPFL the September backups were the newest before the wrapper edit, which is why a later approved change without a new backup caused confusion. Tie backups to change tickets so that each approved change produces a fresh copy and hash.  Check monthly that the newest backup of each device is newer than its last approved change. If not, take a fresh backup and hash it before the next shift.

### Worked example (synthetic HPFL)

Tomás reports the mismatch. The controls engineer finds an older, matching copy in the offline store and compares the edited file: someone added a line to the wrapper program after the September backup without a change ticket. The edit is traced to an approved but unrecorded adjustment; the register and procedure are updated.

> **Synthetic case — HPFL.** Files and hashes are produced by the lab with invented contents.

### Errors and limits

A matching hash proves the file is unchanged since recording, not that the recorded version was good. Hashes must be stored separately from the backups.

### Exercises

- **EX041 — Backup list.** Name five things to back up on the HPFL line. *Rubric:* 3 = five correct items; 2 = four; 1 = two; 0 = none.
- **EX042 — Mismatch decision.** What does Tomás do with the wrapper backup marked MISMATCH? *Rubric:* 3 = do not restore; set aside; report; find verified copy; 2 = report only; 1 = restore anyway; 0 = none.
- **EX043 — A changed byte.** If the filler data had one character changed, what would the lab print for that file? *Rubric:* 3 = different hash and "MISMATCH - do not restore"; 2 = mismatch; 1 = match; 0 = none.
- **EX044 — Hash storage.** Why are hashes stored apart from the backup files? *Rubric:* 3 = attacker altering backups could also alter hashes in same place; 2 = vague; 1 = space; 0 = none.

### Synthesis

Backups are offline, labelled, hashed and test-restored; a mismatch stops a restore.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Segmentation and firewall rules

### Learning outcomes

You will (1) explain zones and conduits from IEC 62443 in plain words; (2) read a firewall rule table; and (3) spot rules that weaken segmentation.

### 12.1 Zones and conduits

IEC 62443 groups assets with similar security needs into zones and calls the controlled connections between them conduits. At HPFL: the line zone (PLCs, HMI, camera), a DMZ (historian copy, remote access gateway, file transfer server) and the office zone. Traffic only crosses through conduits that are firewalled and documented.

Write each conduit with its purpose, the traffic it allows and its owner. At HPFL the conduits are the line pushing to the DMZ historian, ENG-LT reaching the PLCs, and vendor access through the gateway in the DMZ. Anything else crossing a zone boundary is a finding.

### 12.2 The DMZ

Office users want production data; the line must not accept office connections. So the line pushes data to a server in the DMZ and the office reads it there. No connection then needs to go straight from office to line.

At HPFL the line pushes data to the historian copy in the DMZ, and office users read it there. Vendor access and file transfer also land in the DMZ. That way FW-1 needs no rule allowing office machines straight into the line, which is exactly the kind of rule Chapter 12's worked example removes.

### 12.3 Reading rules

Each rule has source, destination, port and action, read top to bottom; the first match wins. A last "deny everything" rule makes anything not listed blocked.

Reading top to bottom matters because a broad allow rule placed above a narrow deny makes the deny useless. When reviewing a table, ask for each rule: who owns it, why it exists, and whether a rule above it already decides the same traffic. FW-1's table at HPFL has four rules, which makes this easy to practise.

### 12.4 Weak rules

Look for "any" sources, broad port ranges, rules with no comment or owner, and temporary rules that were never removed. Each one should be questioned and either justified or removed through change control.

At HPFL rule 3, office any to line any marked temp 2025, showed all of these warning signs at once. It was removed through change control and tested at the next stop. Record each question raised and its answer, so that a removed rule is not later re-added without review.

### 12.5 Do not edit on your own

Firewall changes are made by the network owner with a change ticket and a rollback plan; a wrong rule can stop the line.

If you find a weak rule, report it with the rule number and your reason. The network owner decides how to change it, prepares a rollback and tests at a planned stop. Your role is to notice and explain the risk.  At HPFL the network owner removed rule 3 only after raising a change and agreeing a test at the next stop. A rule changed by someone else, however well meant, leaves no record and no rollback, and could stop the line.

### Worked example (synthetic HPFL)

Tomás reviews FW-1's table with the network owner. Rule 1 allows ENG-LT to the PLCs' programming port; rule 2 lets the line push to the DMZ historian; rule 3, "office any → line any allow — temp 2025", has no owner. Rule 4 denies all. They raise a change to delete rule 3, test at the next stop, and the line runs normally afterwards.

> **Synthetic case — HPFL.** The rule table is invented.

### Errors and limits

A good rule table can be undone by an unmanaged switch or modem bypassing the firewall; walk-downs and diagrams complement rule review.

### Exercises

- **EX045 — Zones at HPFL.** Name the three HPFL zones and one asset in each. *Rubric:* 3 = line/DMZ/office with correct assets; 2 = two; 1 = one; 0 = none.
- **EX046 — First match.** With rule 3 above rule 4, what happens to office traffic to HMI-1? *Rubric:* 3 = allowed by rule 3 before deny applies; 2 = allowed; 1 = denied; 0 = none.
- **EX047 — Why a DMZ.** Explain how the DMZ lets office staff see production data without connecting to the line. *Rubric:* 3 = line pushes to DMZ server, office reads there, no office→line rule; 2 = partial; 1 = "it's safer"; 0 = none.
- **EX048 — Removing a rule.** Outline the safe steps to remove rule 3. *Rubric:* 3 = change ticket, owner confirms, planned window, rollback, test, record; 2 = some; 1 = delete now; 0 = none.

### Synthesis

Zones are separated by documented, owned conduits; broad or ownerless rules are removed through change control.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — IoT devices on the factory floor

### Learning outcomes

You will (1) identify IoT devices on a line; (2) check them against a baseline of ETSI EN 303 645 provisions; and (3) decide how to connect them safely.

### 13.1 What counts as IoT here

Smart energy meters, wireless vibration sensors, the vision camera, a cloud-connected label printer and tablets used by quality staff. They often arrive through purchasing rather than engineering, so nobody checks them first.

At HPFL the quality team asked for wireless vibration sensors on the wrapper motors, and the vision camera is already in place. Each of these devices should appear in the register, with an owner and the network it uses. Purchasing should involve the network owner before ordering.  Ask purchasing to tell you about every networked device ordered.

### 13.2 A baseline to check against

ETSI EN 303 645 sets baseline security provisions for consumer IoT, and NIST IR 8259 describes what manufacturers should do. Both are useful checklists for plant devices too. Questions to ask a supplier: are there universal default passwords? Is there a way to report vulnerabilities? Will software updates be provided and for how long? Is communication encrypted? Can the device be reset and its data deleted?

Send the questions to the supplier before purchase and keep the answers with the purchase record. Where possible, check claims on delivery: does the device force a password change at setup, and does it really use TLS? An answer that cannot be checked is still useful, but it should be marked as a claim.

### 13.3 Connecting safely

IoT devices that talk to a vendor cloud belong in their own segment, not the line VLAN. Allow only the cloud addresses they need, block them from reaching PLCs, and record them in the register with an owner and an update plan.

At HPFL the vibration sensor gateway was placed on a new IoT VLAN allowed only to the vendor's cloud addresses. Check after installation that the gateway cannot reach the PLCs, with the network owner, through a rule review rather than probing.

### 13.4 End of support

When a supplier stops publishing updates, plan replacement. A cheap sensor left unpatched for years on the line network is an easy foothold.

Record the supplier's stated support period in the register, so that the end of support can be planned well before it arrives. At HPFL the vibration sensor supplier promised updates for five years; the replacement date belongs in the register next to the device entry.  If a device must stay after support ends, tighten its isolation and record the decision with a review date. Tell the owner well in advance so that budget can be planned.

### Worked example (synthetic HPFL)

Quality wants wireless vibration sensors VIB-1 to VIB-4 on the wrapper motors, reporting to a vendor cloud. Tomás sends the supplier the five questions. Answers: unique passwords per device, a published disclosure address, updates for five years, TLS to the cloud, factory reset documented. The network owner puts the sensor gateway on a new IoT VLAN allowed only to the vendor's cloud addresses.

> **Synthetic case — HPFL.** The sensors and supplier answers are invented.

### Errors and limits

Supplier answers are claims; check what you can (for example, that the device forced a password change at setup). ETSI EN 303 645 targets consumer products, so industrial devices may need further requirements from IEC 62443-4-2.

### Exercises

- **EX049 — Spotting IoT.** List three IoT devices that might appear at HPFL outside the engineering drawings. *Rubric:* 3 = three plausible devices; 2 = two; 1 = one; 0 = none.
- **EX050 — Supplier questions.** Write the five baseline questions to a supplier. *Rubric:* 3 = default passwords, disclosure, update period, encryption, reset/deletion; 2 = four; 1 = two; 0 = none.
- **EX051 — Placement.** Where should the VIB sensor gateway connect, and what should it be allowed to reach? *Rubric:* 3 = separate IoT VLAN; only vendor cloud; blocked from PLCs; 2 = separate only; 1 = line VLAN; 0 = none.
- **EX052 — Updates ended.** The label printer supplier announces end of support. What does Tomás record and plan? *Rubric:* 3 = register status, risk note, compensating isolation, replacement plan/date; 2 = some; 1 = ignore; 0 = none.

### Synthesis

Floor IoT is checked against a baseline, isolated to what it needs and replaced when support ends.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Recognising abnormal behaviour

### Learning outcomes

You will (1) describe what normal looks like for the HPFL line; (2) recognise signs that may indicate an attack or a fault; and (3) use ATT&CK for ICS names to describe what you saw.

### 14.1 Knowing normal

Operators know the line's sound, rhythm and screens. Technicians add network and system normal: which devices talk, which accounts log in, how often programs change. Write it down; "normal" kept only in people's heads disappears with shift changes.

At HPFL Tomás already wrote down that writes come only from HMI-1 and ENG-LT. Similar notes can cover typical login times, how often PLC programs change and which devices appear on the network. Keep them in the register or a shared document, dated and updated after changes.

### 14.2 Signs to report

A setpoint changes without anyone pressing a button. HMI screens freeze or show values that disagree with gauges. A program download appears in the log with no job. A new device appears on the network. Remote sessions occur outside a ticket. The line stops with no mechanical cause.

Report any of these with the time, the device and what you saw, and attach photographs or log lines where you can. At HPFL a mismatch between HMI-1 and a handheld thermometer turned out to be a failed sensor, but the report still led to a quick diagnosis.

### 14.3 Naming what you saw

MITRE ATT&CK for ICS gives shared names: T0836 Modify Parameter for altered setpoints, T0886 Remote Services for misuse of remote access, T0843 Program Download for unexpected logic changes. Using these names in a report helps the security team, but report what you observed, not a guess at the attacker.

The names help when reports are compared across shifts or sites. Write the observation first, then the technique name if it fits: for example, wrapper speed changed from 120 to 180 by admin at 07:45, which fits Modify Parameter. Leave intent and attribution to the security team.

### 14.4 Fault or attack?

Most abnormal events are faults or mistakes. That does not matter at first: the response is the same — keep people safe, preserve evidence, report. Deciding the cause comes later.

At HPFL the temperature mismatch was a failed sensor, and the speed change was an operator's well-meant adjustment. Both were handled with the same steps: make safe, record, report. The cause was found afterwards, with the evidence that had been kept.  Treating every event the same way also avoids embarrassment: nobody is accused, and nothing is dismissed too early.

### 14.5 What not to do

Do not reboot devices, delete logs, unplug cables or "fix" values before the supervisor and engineer agree; you could destroy the evidence of what happened or create a new hazard.

The supervisor decides whether the line keeps running; the engineer decides how to examine devices. Your part is to photograph, note the time and call. If a hazard requires immediate action, follow normal safety procedures and record what you did.  At HPFL Tomás photographed both temperature readings and called the supervisor; he did not reset the sensor. That restraint kept the evidence that later showed the cause.

### Worked example (synthetic HPFL)

HMI-1 shows the filler at normal temperature, but the operator's handheld thermometer reads 12 °C higher. Tomás photographs both readings, notes the time, and calls the supervisor, who stops the filler safely. Later the engineer finds a failed sensor — a fault, not an attack — but the evidence made the diagnosis quick.

> **Synthetic case — HPFL.** The readings are invented.

### Errors and limits

A list of signs is not complete; trust experienced operators who say "this is not right". ATT&CK describes techniques, not certainty about intent.

### Exercises

- **EX053 — HMI disagrees with gauge.** What does a difference between HMI and a local gauge suggest, and what is the first action? *Rubric:* 3 = sensor fault or manipulated display; keep safe/stop via supervisor, record evidence; 2 = one part; 1 = trust HMI; 0 = none.
- **EX054 — Matching techniques.** Match to ATT&CK for ICS: (a) unplanned program download; (b) vendor session outside ticket; (c) changed speed value. *Rubric:* 3 = T0843, T0886, T0836; 2 = two; 1 = one; 0 = none.
- **EX055 — Same response.** Why is the initial response the same for a fault and an attack? *Rubric:* 3 = safety and evidence first, cause unknown at start; 2 = partial; 1 = "it isn't"; 0 = none.
- **EX056 — Writing down normal.** Give three items for an HPFL "normal" sheet. *Rubric:* 3 = three specific items (talkers, login pattern, change frequency etc.); 2 = two; 1 = vague; 0 = none.

### Synthesis

Knowing normal lets you notice the abnormal; respond for safety and evidence before deciding cause.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Reporting an incident and first actions

### Learning outcomes

You will (1) follow the HPFL first-response steps; (2) write a clear first report; and (3) explain why evidence is preserved before recovery starts.

### 15.1 First steps

Make people safe: the supervisor decides whether to stop or isolate the affected part of the line using normal procedures. Then call the incident contact on the site sheet. Record what you see as you go. Do not try to remove malware or restore systems yourself.

At HPFL the night supervisor switched the line to local panel control and stopped the wrapper before anything else happened. Tomás then photographed the screen and called the incident contact. Following the steps in order keeps people safe and leaves evidence intact.

### 15.2 A good first report

It answers: what did you notice, where, when, which devices, what the line is doing now, what has been done so far and who you have told. Short facts beat long theories. NIST SP 800-82r3 stresses that OT incident response must be planned with operations, because actions taken in panic can hurt the process.

At HPFL Tomás's report fitted in one sentence per point and was sent within minutes. Later corrections were added in writing, not by changing the first report. Keep a copy of every report you send, with the time.

### 15.3 Preserving evidence

Photograph screens, keep a written timeline, and leave devices as they are unless safety requires otherwise. If a device must be isolated, the engineer does it by a planned method — for example, disabling a switch port — and records exactly when.

Keep the written timeline in the order events happened, with times from a single reference such as your watch, and note any known clock differences between devices. Photographs should show the device name and the screen together.  Store photographs with the timeline in one place.

### 15.4 Communication

Use the site's contact list. Do not post about the incident on social media or chat groups. Do not contact vendors or authorities yourself unless the incident lead asks.

At HPFL the incident lead decides who speaks to vendors, customers and authorities. Avoid speculating to colleagues about the cause, because rumours spread quickly on a shift floor. If someone outside asks you about the incident, refer them to the incident lead.  Use the phone numbers on the site sheet, not numbers saved privately, because they are kept current.

### 15.5 Notification duties

Some sectors and countries require reports to regulators or to CISA within set times; the incident lead handles this, but your timeline is what makes it possible.

At HPFL Tomás's timeline, with its times and photographs, gave the incident lead what was needed for any required notification. Keep it accurate and complete, and pass corrections to the lead in writing as soon as you find them.  Times matter most: when the event was noticed, when it was reported and when the line was stopped. Note them as they happen rather than reconstructing them afterwards.

### Worked example (synthetic HPFL)

At 03:10 HMI-1 shows a ransom message. Tomás tells the night supervisor, who switches the line to local panel control and stops the wrapper. Tomás photographs the screen and calls the incident contact at 03:14. His report reads: "03:10 HMI-1 ransom screen; line on local control, wrapper stopped 03:12; no other screens affected seen; nothing unplugged; supervisor informed."

> **Synthetic case — HPFL.** The incident is invented.

### Errors and limits

Contact lists go out of date; check them quarterly. A first report can be wrong; correct it in writing rather than deleting it.

### Exercises

- **EX057 — Ordering the steps.** Put in order: call incident contact; supervisor makes line safe; photograph screen; restore HMI. *Rubric:* 3 = safe, photograph, call; restore later by owners; 2 = mostly right; 1 = restore first; 0 = none.
- **EX058 — Improving a report.** Rewrite "HMI is hacked, probably Russians" into a factual first report. *Rubric:* 3 = time, device, observation, line state, actions, who told; no speculation; 2 = partial; 1 = still speculation; 0 = none.
- **EX059 — Unplugging.** A colleague wants to unplug HMI-1's network cable immediately. What do you say? *Rubric:* 3 = isolate only via supervisor/engineer, planned, recorded; safety and evidence; 2 = wait; 1 = do it; 0 = none.
- **EX060 — Who notifies.** Who decides whether to notify regulators or CISA? *Rubric:* 3 = incident lead/management; technician supplies timeline; 2 = lead only; 1 = technician alone; 0 = none.

### Synthesis

Safety first, facts recorded, evidence preserved, the right people called; recovery comes after.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Recovery and returning to production

### Learning outcomes

You will (1) describe the steps to restore a line after an incident; (2) verify restored systems before restarting; and (3) explain why lessons learned must change something.

### 16.1 Order of recovery

Recovery is planned by the incident lead, controls engineer and operations. Usually: confirm the cause is contained, rebuild affected computers from known-good images, restore PLC programs from verified backups (Chapter 11), change passwords that may be exposed, then test.

At HPFL HMI-1 was rebuilt from the vendor's image, both PLC programs were compared with matching backups, and the admin password was changed. Following the order prevents restarting with a problem still present. Each step is recorded with its time and the person who did it.

### 16.2 Verification before restart

Compare restored PLC programs with verified copies, check HMI screens show correct values against local gauges, confirm firewall rules match the approved table, and run the line empty through a test cycle. Quality signs off before product runs.

At HPFL the test cycle ran empty for 30 minutes and quality signed off at 11:20 before production restarted. Record each check and its result in the incident file. If any check fails, the line does not restart until the cause is understood.  Keep the comparison results with the incident file.

### 16.3 Watching afterwards

Attackers sometimes return. For days after restart, watch logins, remote sessions and new devices more closely, and report anything unusual immediately.

Agree with the supervisor how long the watch period lasts and who reviews logs each day. At HPFL the lessons meeting found an internet-reachable remote desktop port opened by a contractor, which makes close watching of remote sessions especially important. Report anything unusual to the incident lead, not only to your shift.  Note the end date of the watch period in the incident file so it does not quietly lapse.

### 16.4 Lessons learned

A short meeting within two weeks answers: what happened, what worked, what did not, what changes. Each change has an owner and date. A lessons session that changes nothing has failed.

At HPFL the lessons meeting assigned closing the remote desktop port on HMI-1 and a monthly check to the network owner. Each action is tracked until it is done and shown to be effective, and the meeting notes are kept with the incident file.  Invite the operators who were on shift; they often know what worked.

### 16.5 Record keeping

Keep the timeline, photographs, decisions and test results together. They support insurance, regulators and the next improvement.

Store the records together in one folder or ticket, with access limited to people who need them. Include the first report, its corrections, photographs and the test cycle results. The next walk-through can then check whether lessons were applied.  Keep the records for as long as the site's policy requires, and note who may read them. When an insurer or regulator asks a question months later, the answer should come from these records rather than from memory, which fades quickly.

### 16.6 Communicating the restart

Tell every shift what changed: new passwords, any screens that look different, and which unusual signs to report during the watch period.

At HPFL that meant telling every shift that the admin password had changed and that unexpected remote sessions or new devices should be reported. A short written note left at HMI-1, without passwords, helps people who missed the briefing.  Brief the next two shifts in person if possible, and ask them to confirm they understood. Questions raised at these briefings often show where the procedure needs to be clearer, so record them as well.

### Worked example (synthetic HPFL)

After the ransom incident, HMI-1 is rebuilt from the vendor's image; both PLC programs are compared with matching backups and found unchanged. The admin password is changed. A test cycle runs empty for 30 minutes, quality signs off at 11:20, and production restarts. The lessons meeting finds HMI-1 had an internet-reachable remote desktop port opened by a contractor; the action — close it and add a monthly check — is assigned to the network owner.

> **Synthetic case — HPFL.** The recovery is invented.

### Errors and limits

Restoring from a backup taken after the compromise reloads the problem; verified dates and hashes matter. Pressure to restart quickly is real; the test cycle is non-negotiable.

### Exercises

- **EX061 — Recovery order.** Put in order: test cycle; rebuild HMI; quality sign-off; change passwords; confirm containment. *Rubric:* 3 = containment, rebuild, passwords, test, sign-off; 2 = mostly; 1 = random; 0 = none.
- **EX062 — Verification checks.** Name three checks before restarting the line. *Rubric:* 3 = programs vs verified copy, HMI vs gauges, firewall rules, empty test cycle; 2 = two; 1 = one; 0 = none.
- **EX063 — Bad backup.** Why could restoring a backup from the day of the incident be a mistake? *Rubric:* 3 = may contain attacker's change; use verified pre-incident copy; 2 = partial; 1 = no problem; 0 = none.
- **EX064 — Turning a lesson into action.** Write the action from the HPFL lessons meeting in owner/date form. *Rubric:* 3 = close RDP port + monthly check, network owner, date; 2 = no owner/date; 1 = "be careful"; 0 = none.

### Synthesis

Recover in order, verify before restart, watch afterwards and turn lessons into owned actions.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Change management and documentation

### Learning outcomes

You will (1) explain why every change on the line needs a ticket; (2) write a change request with a rollback plan; and (3) keep drawings and records in step with reality.

### 17.1 Why change control is security

Most problems on plants come from changes nobody recorded: a firewall rule added in a hurry, a program edited during a breakdown, a camera bolted on by a contractor. Change control means every change is requested, reviewed, approved, carried out and recorded. It also makes it easy to notice an unrecorded change, which may be the first sign of an attack.

At HPFL several problems in this book started as unrecorded changes: the edited wrapper program in Chapter 11, the temporary firewall rule in Chapter 12 and the remote desktop port in Chapter 16. Each would have been visible sooner with a ticket.

### 17.2 A change request

It states what will change, why, which devices, who does it, when, the risk to the process, how success is checked, and how to undo it. Emergency changes during a breakdown are allowed but get recorded afterwards within one shift.

At HPFL Tomás's request for the VIS-CAM update covered all of these in a few lines. Keep the form short so that people actually use it. The approver checks that the success test and the rollback are realistic before agreeing.

### 17.3 Rollback

Before the change, save the current program or configuration and its hash. If the check fails, restore it. A change with no rollback is a gamble.

At HPFL the rollback for VIS-CAM was to reinstall firmware 1.0.7 from a saved file with its hash recorded. Test that the saved file is complete before starting the change. If rollback itself fails, stop and call the controls engineer.  At HPFL the hashes of saved files were recorded in the change ticket, so a restored file could be checked before loading. Without that, a rollback could load a corrupted or edited copy without anyone noticing.

### 17.4 Keeping documents current

Update the asset register, network drawing and rule table in the same ticket. Mark drawings with a revision number and date.

At HPFL the network drawing was still at revision 3 while the IoT VLAN appeared only in revision 4 drafts, which the capstone walk-through found. Updating documents in the same ticket prevents that gap from opening.  When a drawing changes, mark the old revision as superseded and keep it, so past decisions can still be understood. Check revision numbers during each walk-through; a drawing whose revision is behind reality is itself a finding, as HPFL learned.

### 17.5 Reviewers

The person who makes a change should not be the only person who approves it. At HPFL the controls engineer reviews program changes, the network owner reviews firewall and switch changes, and the supervisor confirms the production window. A second pair of eyes catches typing errors in addresses and values before they reach the line.

Record the reviewer's name in the ticket. If the only person who can review is unavailable, wait for the next window unless the change is an emergency.

### Worked example (synthetic HPFL)

The vision camera supplier needs firmware 1.1.0 on VIS-CAM. Tomás writes: "Change 512 — update VIS-CAM 1.0.7 to 1.1.0 for reject-accuracy fix; by quality technician; Tuesday 06:00 planned stop; risk: rejects stop working; check: 20 test packs including 5 bad seals rejected; rollback: reinstall 1.0.7 from saved file, hash recorded." The update passes the check and the register shows 1.1.0.

> **Synthetic case — HPFL.** The change and supplier fix are invented.

### Errors and limits

Change control can become a paper exercise; keep forms short and enforce the key fields. Emergency changes must not become the normal route.

### Exercises

- **EX065 — Fields of a request.** List six fields of a change request. *Rubric:* 3 = what, why, devices, who, when, risk, check, rollback (any six); 2 = four; 1 = two; 0 = none.
- **EX066 — Breakdown edit.** The engineer edits PLC-FILL during a 2 a.m. breakdown. What must happen afterwards? *Rubric:* 3 = recorded as emergency change within shift, new backup and hash, register updated; 2 = record only; 1 = nothing; 0 = none.
- **EX067 — Failed check.** VIS-CAM's test lets 2 of 5 bad seals through. What happens next? *Rubric:* 3 = rollback to 1.0.7, verify, record failure, contact supplier; 2 = rollback; 1 = run anyway; 0 = none.
- **EX068 — Unrecorded change.** Why is an unrecorded change worth reporting even if it looks harmless? *Rubric:* 3 = may be unauthorised/attack sign; breaks baseline and backups; 2 = one; 1 = ignore; 0 = none.

### Synthesis

Requested, reviewed, reversible and recorded changes keep the line known; unrecorded ones are warnings.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Capstone: a security walk-through of the line

### Learning outcomes

You will (1) combine the book's skills into one planned walk-through; (2) produce a short findings list with priorities; and (3) present it to the supervisor and engineer.

### 18.1 Planning

Agree scope, date and permit with the supervisor: which cabinets, which records, no connections to devices, stop conditions. Bring the asset register, network drawing, rule table and media and remote-access logs.

Write the plan on the permit: the time window, the cabinets to be opened by an electrician, the records to be checked and the stop conditions. At HPFL the walk-through had a two-hour permit. Agree beforehand who will receive the findings and when.  Book the date well before so that operations can plan around it.

### 18.2 What to check

Physical: cabinets locked, no unexplained modems or switches, no passwords on panels, no loose USB drives. Records: register complete, backups recent and hashes matching, advisories recorded, changes closed. Access: vendor accounts disabled outside sessions, admin use limited.

Use a checklist so that nothing is missed and so the next walk-through can be compared with this one. At HPFL the checklist led Tomás to the modem in the filler cabinet, ENG-LT's old anti-malware signatures, the outdated drawing and a recipe drive missing from the media log.

### 18.3 Writing findings

Each finding: what you saw, where, why it matters (consequence), suggested fix, owner. Keep evidence (photographs, log extracts) with it.

Write findings during or right after the walk-through, while details are fresh. At HPFL the cellular modem finding included its location in the filler cabinet, a photograph and the consequence that someone could reach the filler from outside. Each finding needs one owner who agrees to act.  Keep each finding to a few lines so it can be read quickly in the meeting. Separate what you saw from what you think it means.

### 18.4 Prioritising

Order by consequence and ease: anything that gives an unreviewed path to PLCs comes first; tidy-ups last. Present the top three clearly; long lists hide the important items.

At HPFL the modem came first because it was an unreviewed path to a PLC. ENG-LT's old anti-malware signatures came second, because that laptop programs the PLCs. The missing drive and the outdated drawing followed. Write a one-line reason for each ranking.  Agree the order with the supervisor, who may know production reasons for changing it.

### 18.5 Following up

Agree owners and dates in the meeting, then check progress monthly.

Record the owners and dates in a short list shared with the supervisor. At each monthly check, note what was completed and what slipped, with a reason. At HPFL the next walk-through should start by confirming that the filler cabinet modem has been disconnected or controlled. Findings that keep slipping are raised with the supervisor rather than quietly carried forward.  Close each item only with evidence that it was done.

### 18.6 Presenting to the supervisor

Use plain language and consequences the supervisor cares about: "this modem could let someone change the filler from outside" works better than protocol names. Bring photographs, keep to ten minutes, and end with the decisions you need: owner, date and any production window. Thank the operators who helped; their cooperation decides whether the next walk-through is welcome.

Send a short written summary afterwards with the findings, owners and dates.  Keep a copy of the summary with the walk-through evidence, so the next walk-through can start by checking what changed since. If the supervisor does not agree with a ranking, record the disagreement and the reason.

### Worked example (synthetic HPFL)

Tomás's walk-through, under a two-hour permit, finds: (1) the cellular modem in the filler cabinet still connected; (2) ENG-LT anti-malware signatures 40 days old; (3) the network drawing at revision 3 while the IoT VLAN exists only in revision 4 drafts; (4) one recipe drive missing from the media log. He ranks the modem first, the laptop second, the drive third and the drawing fourth, and the supervisor assigns owners.

> **Synthetic case — HPFL.** The findings are invented.

### Errors and limits

A walk-through is a snapshot; issues return without regular repetition. It does not replace a professional assessment against IEC 62443.

### Exercises

- **EX069 — Permit scope.** Write the scope and three stop conditions for the walk-through. *Rubric:* 3 = areas, records, no device connections, three specific stops; 2 = partial; 1 = vague; 0 = none.
- **EX070 — Finding format.** Rewrite "modem bad" as a full finding. *Rubric:* 3 = what/where/why/fix/owner/evidence; 2 = four parts; 1 = two; 0 = none.
- **EX071 — Ranking.** Justify ranking the modem above the old anti-malware signatures. *Rubric:* 3 = modem is a live unreviewed path to PLCs; laptop only risky when connected and is controlled; 2 = partial; 1 = reversed; 0 = none.
- **EX072 — Follow-up plan.** How should Tomás make sure the four findings are actually fixed? *Rubric:* 3 = owners and dates agreed, tracked, monthly check, evidence of closure; 2 = some; 1 = "remind people"; 0 = none.

### Synthesis

A planned walk-through ties inventory, access, backups, changes and evidence into ranked, owned fixes.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Harbor Point Food Packaging Line, Tomás Reyes and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** PLC-FILL controls the filler; PLC-WRAP drives the wrapper motors and heaters; HMI-1 shows status and takes operator commands; VIS-CAM inspects seals and rejects bad packs; ENG-LT stores and changes PLC programs.

**EX002.** An office PC restart loses at most unsaved work, while restarting PLC-WRAP stops motors and heaters mid-cycle, can jam film or leave product unsafe, and must follow the line's stop procedure with operations agreeing.

**EX003.** A much higher sealing temperature can scorch film, start a fire or burn a worker clearing a jam, and it can produce damaged or poorly sealed packs that must be rejected as food-safety risks.

**EX004.** T0836 Modify Parameter; yes — an operator mistyping a value causes the same physical effect, which is why changes are logged and checked whatever their cause.

**EX005.** Refuse and stop the plan: the light curtain is a safety function that must never be bypassed for security work; report the suggestion to the supervisor and find a test approach that leaves safety untouched, such as observing from a mirror port during a planned stop.

**EX006.** A connected laptop can broadcast, request addresses or run software that sends traffic to PLC-WRAP, which can slow its communication or change logic, so the process could be affected and the work must be planned and authorised.

**EX007.** (a) The shift supervisor; (b) the controls engineer who owns the PLC programs; (c) the quality manager.

**EX008.** Stop if the supervisor or an operator asks; stop if any live conductor or moving part is exposed beyond the agreed view; stop if an unexplained alarm appears on HMI-1 while the door is open.

**EX009.** No. With a /24 mask the first three octets are the network; 10.20.1 and 10.20.2 differ, so traffic between them must pass a router or firewall.

**EX010.** The printer would sit on the line VLAN with direct reach to PLCs and HMI-1, bypassing FW-1 rules; any compromise of the printer, or office users printing to it, would create a path nobody reviewed.

**EX011.** "ENG-LT (its office address) → PLC-FILL and PLC-WRAP on the programming port only, allow", followed by "any → 10.20.1.0/24 deny", so nothing else from the office reaches the line.

**EX012.** Anyone with a cable can join the line network through it, it has no VLANs or logs, and it may link the cabinet to devices not on any drawing, so it creates connections no one reviews.

**EX013.** It sets the wrapper's speed value to 180 immediately; the motor accelerates without any further confirmation, which can cause jams or unsafe film tension.

**EX014.** Classic Modbus does not check identity, so anything that reaches port 502 can read and possibly write PLC-FILL values; an unmanaged vendor tablet could change the filler by mistake or if compromised.

**EX015.** (b) VIS-CAM writing to PLC-WRAP: the camera should only send reject signals through its defined path, and a write from it is outside the expected pattern of HMI-1 and ENG-LT.

**EX016.** On a protocol simulator or a lab PLC on an isolated bench, because any request to the line can change real outputs and stop or endanger production.

**EX017.** The firmware version (to match advisories) and the exact make and model (advisories name specific products); without them you cannot decide whether PLC-WRAP is affected.

**EX018.** `complete: 4 of 5` — HMI-1 becomes OK, but PLC-WRAP still prints `MISSING fw`.

**EX019.** A change ticket that installs, moves or replaces a device cannot be closed until the asset register entry is updated and the updater's name is recorded in the ticket.

**EX020.** It lists every device's address, model and firmware, which tells an attacker exactly which targets exist and which known weaknesses to try.

**EX021.** All actions appear under one name, so the log cannot show which person changed a setpoint; investigators must reconstruct it from shift rosters and memory, which is slow and unreliable.

**EX022.** Default passwords are in public manuals, and "isolated" lines still receive contractor laptops, USB devices and remote links; anyone with any reach can log in with no effort.

**EX023.** Photograph the note as evidence, remove it, tell the supervisor and controls engineer, write a short report; the engineer changes the password at a planned stop and reviews recent admin logins.

**EX024.** No. Routine monitoring needs only viewing rights; using admin daily makes accidental changes and stolen-session damage more likely, so admin is reserved for planned work.

**EX025.** Leave it unplugged, note where and when it was found, and hand it to security or the supervisor; dropped drives with tempting labels are a known trick to get someone to plug them in.

**EX026.** Drive identifier, file names, scan result, the person handling it, and the date and time.

**EX027.** "Clean" means the scanner found no known malware; new or unrecognised malware can still pass, so the file is lower risk, not safe, and the log keeps a trail in case of problems.

**EX028.** Use a site-owned, managed laptop with the vendor's software installed, or have the vendor's files scanned and carried on a site drive, so the unmanaged laptop never connects to the line.

**EX029.** Use multi-factor authentication; use strong passwords for remote desktop; close unused remote desktop ports; audit remote connection activity.

**EX030.** A permanently enabled link can be used by anyone holding the vendor's credentials at any hour, with nobody watching, so a stolen password becomes an immediate path to the line.

**EX031.** Vendor and account used, start 14:00 and end 14:38, "viewed wrapper fault log only, no changes", account disabled, operator confirmed normal running.

**EX032.** A modem gives a route into the line that skips the gateway, MFA and logging; Tomás should photograph and report it to the supervisor and controls engineer rather than unplug it himself.

**EX033.** `06:15 low-film` and `08:10 jam-cleared` are process alarms; the logins at 06:02 and 07:40–07:43 and the 07:45 setpoint change are security-relevant.

**EX034.** `failed logins: 5` — the counter increments for every login line ending in "fail".

**EX035.** A success right after repeated failures suggests the password was guessed or found, and two minutes later the same account changed wrapper speed; alone, an admin login could simply be planned work.

**EX036.** At 07:45 on PLC-WRAP the speed setpoint changed from 120 to 180 by the admin account; that account logged in at 07:43 after three failures from 07:40; no planned change was known.

**EX037.** Product and model; affected versions; what an attacker could do; whether network or physical access is needed; the vendor's fix or workaround.

**EX038.** No. Only versions before 2.2 are affected and PLC-FILL runs 3.2; record "not applicable — running 3.2" with the date and who checked.

**EX039.** Updating the PLC needs a production stop, testing with the program and quality checks, which take weeks to arrange; restricting the programming port at FW-1 reduces exposure today.

**EX040.** "Applies: PLC-WRAP fw 2.0. Mitigation: FW-1 allows programming port only from ENG-LT. Patch to 2.3 at planned stop in three weeks. Owner: controls engineer. Review if mitigation changes."

**EX041.** PLC-FILL and PLC-WRAP programs, the HMI-1 project, recipe files, FW-1 and switch configurations, and VIS-CAM settings.

**EX042.** He does not restore it; he labels it as suspect, reports the mismatch to the controls engineer and helps locate an older copy whose hash matches.

**EX043.** It prints a different 12-character hash prefix for `PLC-FILL_2026-09.bak` and `MISMATCH - do not restore`, because any change alters the SHA-256 value.

**EX044.** Anyone able to modify backups in the same place could also rewrite the stored hashes to match, so the check would prove nothing.

**EX045.** Line zone — PLC-WRAP; DMZ — the historian copy or remote access gateway; office zone — staff PCs.

**EX046.** It is allowed: rule 3 matches office traffic to anything on the line before the final deny is reached, so HMI-1 is reachable from every office PC.

**EX047.** Line systems send data out to a server in the DMZ; office users connect only to that server, so there is no rule letting office computers start connections into the line zone.

**EX048.** Open a change ticket, confirm with the network owner that nothing depends on rule 3, schedule a planned stop, keep the old configuration as rollback, remove the rule, check the line and DMZ feeds work, and record the result.

**EX049.** A cloud-connected smart energy meter, a quality team tablet, and a Wi-Fi label printer.

**EX050.** Does each device have a unique password rather than a universal default? How do we report a vulnerability to you? For how long will security updates be provided? Is communication encrypted? Can the device be reset and our data deleted?

**EX051.** On a dedicated IoT VLAN whose firewall rules allow only the vendor's cloud addresses and block every route to the line zone, PLCs and HMI-1.

**EX052.** Mark the printer "end of support" in the register with the date, note the risk, keep it isolated to the minimum needed traffic, and raise a replacement purchase with a target date.

**EX053.** Either the sensor or the display is wrong, which could be a failed sensor or a manipulated value; Tomás records both readings with the time and the supervisor brings the filler to a safe stop before anyone diagnoses it.

**EX054.** (a) T0843 Program Download; (b) T0886 Remote Services; (c) T0836 Modify Parameter.

**EX055.** At the start nobody knows the cause, and in both cases people and product must be kept safe and the evidence preserved for whoever diagnoses it; treating a fault as an attack costs little, the reverse can cost a lot.

**EX056.** Only HMI-1 and ENG-LT write to the PLCs; admin logins happen only during ticketed work; PLC programs change about once a month at planned stops.

**EX057.** The supervisor makes the line safe; Tomás photographs the screen; he calls the incident contact; restoring HMI-1 happens later, decided by the incident lead and engineer.

**EX058.** "03:10, HMI-1 shows a ransom message. Line on local control, wrapper stopped at 03:12. No other affected screens seen. Nothing has been unplugged. Night supervisor informed; incident contact called 03:14."

**EX059.** Ask him to wait for the supervisor and engineer: pulling the cable can drop the panel the operators rely on and loses information; isolation is done by a planned method, such as disabling the switch port, with the time recorded.

**EX060.** The incident lead with site management decides; Tomás's timeline and photographs give them the facts they need to meet any deadline.

**EX061.** Confirm containment; rebuild HMI-1; change passwords; run the test cycle; quality signs off.

**EX062.** Compare PLC programs with verified backups; check HMI values against local gauges; confirm FW-1 rules match the approved table (and run an empty test cycle).

**EX063.** A backup taken on the incident day might already contain the attacker's changes or malware, so restoring it reinstalls the problem; use the newest copy verified as made before the compromise.

**EX064.** "Close the remote desktop port on HMI-1 and add a monthly external exposure check — owner: network owner — due within two weeks."

**EX065.** What changes, why, which devices, who does it, when, risk to the process, success check, rollback method.

**EX066.** The change is written up as an emergency change before the end of the shift, a new backup with its hash is stored, and the register or drawings are updated if anything changed.

**EX067.** Stop the test, reinstall 1.0.7 from the saved file, confirm rejects work again with test packs, record the failed attempt in change 512, and send the result to the supplier.

**EX068.** Nobody can tell whether it was authorised; it may be an attacker's change, and it means backups and the baseline of normal no longer match the line.

**EX069.** Scope: filler and wrapper cabinets, HMI-1 area, the register, backups, media and remote-access logs; no connections to any device. Stop if an unexplained alarm appears, if the supervisor or operators ask, or if a cabinet shows a live hazard beyond what the permit covers.

**EX070.** "Cellular modem connected inside the PLC-FILL cabinet (photo 3); gives an unmanaged route to the line bypassing FW-1 and the remote gateway; fix: controls engineer confirms purpose, disconnects or moves it behind the gateway; owner: controls engineer."

**EX071.** The modem is an active, unreviewed connection that could reach the PLCs at any moment, whereas ENG-LT only touches the line under permit and its signatures can be updated before next use.

**EX072.** Agree an owner and date for each item in the meeting, log them in the tracking sheet, check monthly and close each only with evidence such as a photograph or updated record.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0836 Modify Parameter, T0843 Program Download, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- Modbus Organization. Modbus specifications. <https://www.modbus.org/modbus-specifications>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
