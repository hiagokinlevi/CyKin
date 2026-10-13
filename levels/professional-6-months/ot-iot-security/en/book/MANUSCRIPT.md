# OT, IoT and Cyber-Physical Security: A Professional Practitioner's Guide

- Language: English (`en`); professional course, six months; approximately 360 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: entry-level security practitioners joining an organisation, here a hospital, whose building and facility systems are cyber-physical.
- Relation to neighbouring books: the [rapid course book](../../../../rapid-1-month/ot-iot-security/en/book/MANUSCRIPT.md) is a four-chapter introduction; the [technical book](../../../../technical-18-months/ot-iot-security/en/book/MANUSCRIPT.md) goes deeper into floor procedure. **This book is a compact practitioner's guide built on building systems.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to access real sites. All sites, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–3 explain hospital building systems, patient safety and building networks; 4–10 cover inventory, accounts, internet exposure, contractor access, segmentation, monitoring and advisories; 11 covers incident response and 12 the capstone risk report. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, five exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 4, 6 and 9 read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Millbrook Hospital Building Systems** — theatre air-handling units AHU-OT1/2, CHILLER-1, medical gas alarm MGAS-PANEL, LIFT-CTRL, access control DOOR-SRV, workstation BMS-WS | Hospital studied throughout | Invented |
| **Aisha Bello** | Junior security analyst at Millbrook | Invented |

### Core sources

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Building systems as cyber-physical systems

### Learning outcomes

You will (1) list the building systems a hospital depends on; (2) explain how each becomes a cyber-physical system once networked; and (3) describe the patient consequences of their failure.

### 1.1 What runs a hospital building

Behind the wards sit air-handling units that keep operating theatres at controlled temperature, humidity and pressure; chillers and boilers; medical gas alarm panels that warn when oxygen pressure drops; elevators that move patients between floors; and access control on doors to pharmacies and maternity units. A building management system (BMS) ties many of these together on a network with a central workstation.

Section one point one develops building systems as cyber-physical systems with a the organisation note Aisha Bello can demo offline.

### 1.2 Why they are cyber-physical

Each system reads sensors and drives equipment in the physical world through controllers. Once those controllers are networked, a change made on a screen anywhere on the network can move a damper, stop a pump or unlock a door. NIST SP 800-82r3 covers building automation explicitly within operational technology for exactly this reason.

Section one point two develops building systems as cyber-physical systems with a the organisation note Aisha Bello can demo offline.

Under section one point two, the mentor expects building claims to carry owners and dates.

### 1.3 Consequence for patients

Office IT failures delay work. Building-system failures can harm patients: a theatre that loses positive pressure risks surgical infection; a silenced gas alarm hides a real drop; a stuck elevator delays an emergency transfer. Security planning in a hospital begins by asking which failure would hurt someone, and how quickly.

Section one point three develops building systems as cyber-physical systems with a the organisation note Aisha Bello can demo offline.

Under section one point three, the mentor expects building claims to carry owners and dates.

### 1.4 Who owns them

Building systems are often owned by estates or facilities teams, maintained by contractors, and invisible to the hospital's IT security staff. Closing that gap — agreeing who is responsible for the security of each system — is often the first practical win.

Section one point four develops building systems as cyber-physical systems with a the organisation note Aisha Bello can demo offline.

Under section one point four, the mentor expects building claims to carry owners and dates.

Section one point four treats what runs hospital building as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha Bello, newly hired as a junior security analyst at Millbrook Hospital, meets the estates manager and lists the systems on a whiteboard with one consequence each. "AHU-OT1: theatre 1 loses pressure — surgery postponed or infection risk." "MGAS-PANEL: oxygen pressure alarm silent — ward staff unaware of supply fault."

> **Synthetic case — Millbrook Hospital Building Systems.** The hospital, Aisha Bello and every figure in this book are invented for teaching.

### Errors and limits

Consequences must be confirmed with clinical and estates staff; an analyst's guess is a starting point only.

### Exercises

- **EX001 — Five systems.** List five hospital building systems and what each controls. *Rubric:* 3 = five systems each with a correct function; 2 = four; 1 = two; 0 = none.
- **EX002 — Becoming cyber-physical.** Explain in two sentences how networking turns an air-handling unit into a cyber-physical security concern. *Rubric:* 3 = networked controller lets remote screen change physical equipment; consequence named; 2 = one point; 1 = vague; 0 = none.
- **EX003 — Theatre pressure.** Why does loss of positive pressure in an operating theatre matter? *Rubric:* 3 = unfiltered air enters, surgical infection risk, surgery postponed; 2 = one; 1 = comfort; 0 = none.
- **EX004 — Silent gas alarm.** Describe the harm if MGAS-PANEL alarms are disabled during a real pressure drop. *Rubric:* 3 = staff unaware, patients on oxygen at risk, delayed response; 2 = partial; 1 = "noise stops"; 0 = none.
- **EX005 — Ownership gap.** Why is agreeing who owns building-system security an early win? *Rubric:* 3 = estates/contractors/IT gap leaves nobody patching or monitoring; clear owner enables every next step; 2 = partial; 1 = paperwork; 0 = none.

### Synthesis

Hospital building systems move air, gas, people and doors; their failure can hurt patients, so their security needs an owner.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Patient safety, contingency and authority

### Learning outcomes

You will (1) explain why clinical safety outranks security convenience; (2) describe hospital contingency arrangements for building systems; and (3) identify who may authorise changes in clinical areas.

### 2.1 Clinical safety first

A security fix that switches off a theatre's ventilation during surgery is worse than the risk it fixes. Every security task in clinical areas is planned with the people responsible for patients, and timed around them.

Section two point one develops patient safety contingency and authority with a the organisation note Aisha Bello can demo offline.

Under section two point one, the mentor expects patient claims to carry owners and dates.

Section two point one treats clinical safety first contingency as testable only when evidence and ticket IDs are recorded.

### 2.2 Contingency already exists

Hospitals prepare for building failures independent of cyber attacks: cylinder oxygen when piped supply fails, portable cooling, manual door keys, elevator rescue procedures. These are also the fall-back when a networked system is untrusted. Knowing them lets security staff suggest isolating a system without leaving patients unsupported.

Section two point two develops patient safety contingency and authority with a the organisation note Aisha Bello can demo offline.

Under section two point two, the mentor expects patient claims to carry owners and dates.

### 2.3 Authority

Estates managers authorise work on building plant; theatre managers decide when a theatre is available; the medical gas authorised person controls gas systems; IT security advises. Contractors work under an estates permit. Analysts never instruct a contractor to change a clinical system directly.

Section two point three develops patient safety contingency and authority with a the organisation note Aisha Bello can demo offline.

Under section two point three, the mentor expects patient claims to carry owners and dates.

Section two point three treats clinical safety first contingency as testable only when evidence and ticket IDs are recorded.

### 2.4 Permits in hospitals

Work in clinical areas often needs infection-control approval as well as an estates permit: a technician opening a ceiling panel in a theatre can release dust. Even a non-invasive check may need a booking slot.

Section two point four develops patient safety contingency and authority with a the organisation note Aisha Bello can demo offline.

Under section two point four, the mentor expects patient claims to carry owners and dates.

Section two point four treats clinical safety first contingency as testable only when evidence and ticket IDs are recorded.

### 2.5 Talking to clinicians

Explain security work in the language of patient risk and theatre time. "We need one hour on Saturday so nobody can change theatre air from outside" gets agreement faster than a list of protocols.

Section two point five develops patient safety contingency and authority with a the organisation note Aisha Bello can demo offline.

Under section two point five, the mentor expects patient claims to carry owners and dates.

Section two point five treats clinical safety first contingency as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha wants to read firmware labels on the theatre air-handling controllers in the roof plant room. The estates manager issues a permit for Saturday 07:00–08:00 when no theatre lists run; the theatre manager confirms; a contractor accompanies her; no settings are touched. She photographs the labels and the permit is closed at 07:40.

> **Synthetic case — Millbrook.** The permit and times are invented.

### Errors and limits

Local roles have different titles; learn your hospital's list. Contingency plans may be untested; ask when they were last exercised.

### Exercises

- **EX006 — Fix that harms.** Give an example of a security fix that could harm patients if timed badly. *Rubric:* 3 = concrete action (e.g. reboot AHU controller) with clinical consequence; 2 = generic; 1 = none clinical; 0 = none.
- **EX007 — Contingency matches.** Match each contingency to its system: cylinder oxygen, manual keys, portable cooling. *Rubric:* 3 = gas supply, access control, HVAC/chillers; 2 = two; 1 = one; 0 = none.
- **EX008 — Who authorises gas work.** Who controls work on medical gas systems at Millbrook? *Rubric:* 3 = medical gas authorised person, under estates; 2 = estates only; 1 = IT; 0 = none.
- **EX009 — Infection control.** Why might a firmware-label check in a theatre need infection-control approval? *Rubric:* 3 = opening panels/access can release dust or breach clean area; 2 = vague; 1 = no reason; 0 = none.
- **EX010 — Isolation suggestion.** How does knowing contingency plans help when proposing to isolate the BMS during an incident? *Rubric:* 3 = can show patients stay supported via manual/fallback, so isolation acceptable; 2 = partial; 1 = irrelevant; 0 = none.

### Synthesis

Clinical safety sets the timing; contingency plans make security actions possible; named roles authorise them.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Networks and protocols in building systems

### Learning outcomes

You will (1) describe how BMS controllers communicate; (2) explain why building protocols are often unauthenticated; and (3) identify where building networks touch the hospital network.

### 3.1 Field and supervisory layers

Sensors and actuators connect to field controllers by wire. Controllers talk to each other and to the BMS server over a building network. Common protocols include BACnet, usually carried over UDP on port 47808 as BACnet/IP, and Modbus/TCP for some plant such as chillers. Many devices also offer a web interface for configuration.

Section three point one develops networks and protocols in building with a the organisation note Aisha Bello can demo offline.

Under section three point one, the mentor expects networks claims to carry owners and dates.

### 3.2 Trust by default

Like many industrial protocols, classic BACnet and Modbus deployments accept commands from anything that can reach them. A laptop on the same network can usually read every point and often write setpoints. Secure variants exist but are not yet common in installed buildings.

Section three point two develops networks and protocols in building with a the organisation note Aisha Bello can demo offline.

Under section three point two, the mentor expects networks claims to carry owners and dates.

Section three point two treats field and supervisory layers as testable only when evidence and ticket IDs are recorded.

### 3.3 Where the networks meet

The BMS workstation may sit on the hospital's corporate network so estates staff can reach it from offices. Contractors add remote access for support. Lifts may have their own cellular link to the manufacturer. Each meeting point is a place an attacker on the hospital network could step into building control.

Section three point three develops networks and protocols in building with a the organisation note Aisha Bello can demo offline.

Under section three point three, the mentor expects networks claims to carry owners and dates.

### 3.4 What an analyst does

Ask the estates team and contractor for a network drawing; compare it with switch and firewall configuration held by the network team; never scan building controllers to find out. Some old controllers crash under scans.

Section three point four develops networks and protocols in building with a the organisation note Aisha Bello can demo offline.

Under section three point four, the mentor expects networks claims to carry owners and dates.

Section three point four treats field and supervisory layers as testable only when evidence and ticket IDs are recorded.

### 3.5 Wireless

Some sensors report over wireless links to gateways. Ask where each gateway connects and who manages its keys.

Section three point five develops networks and protocols in building with a the organisation note Aisha Bello can demo offline.

Under section three point five, the mentor expects networks claims to carry owners and dates.

Section three point five treats field and supervisory layers as testable only when evidence and ticket IDs are recorded.

For section three point five, the organisation will not accept networks work without a written trail.

### Worked example (synthetic Millbrook)

The contractor's drawing shows the BMS on VLAN 300, with the workstation BMS-WS dual-homed: one network card on VLAN 300, one on the corporate VLAN. Aisha notes that BMS-WS bridges corporate and building networks — anyone who compromises it reaches every controller — and adds it to her risk list.

> **Synthetic case — Millbrook.** VLANs and hosts are invented.

### Errors and limits

Protocol names and ports vary by installation; confirm with the integrator. A drawing does not prove what is cabled.

### Exercises

- **EX011 — Two layers.** Describe the field and supervisory layers of a BMS. *Rubric:* 3 = sensors/actuators wired to controllers; controllers and server on building network; 2 = partial; 1 = one; 0 = none.
- **EX012 — BACnet trust.** What can a laptop on VLAN 300 typically do with BACnet/IP controllers? *Rubric:* 3 = read points and often write setpoints without authentication; 2 = read only; 1 = nothing; 0 = none.
- **EX013 — Dual-homed workstation.** Why is BMS-WS's second network card a risk? *Rubric:* 3 = bridges corporate to building network bypassing firewall; compromise reaches controllers; 2 = partial; 1 = speed; 0 = none.
- **EX014 — Meeting points.** Name three places where Millbrook building networks may meet other networks. *Rubric:* 3 = dual-homed workstation, contractor remote access, lift cellular link (or similar); 2 = two; 1 = one; 0 = none.
- **EX015 — No scanning.** Give two reasons Aisha does not scan building controllers to map them. *Rubric:* 3 = old controllers can crash; not authorised/risk to clinical areas; better sources exist; 2 = one; 1 = "slow"; 0 = none.

### Synthesis

Building controllers trust whoever reaches them, so every point where building and hospital networks meet matters.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — An inventory of building devices

### Learning outcomes

You will (1) build a building-device inventory grouped by system; (2) flag devices without vendor support; and (3) explain how support status changes risk decisions.

### 4.1 What to record

System, device name, location, owner, controller model, firmware, installation year, network address, vendor support status and clinical consequence. Building plant lasts twenty years or more, so support status matters more here than in office IT.

Section four point one develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point one, the mentor expects an claims to carry owners and dates.

Section four point one treats what to record grouping as testable only when evidence and ticket IDs are recorded.

### 4.2 Grouping

Grouping by system shows who to talk to: HVAC devices go to the estates mechanical lead, the gas panel to the medical gas authorised person, the lift to its maintenance contractor.

Section four point two develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point two, the mentor expects an claims to carry owners and dates.

Section four point two treats what to record grouping as testable only when evidence and ticket IDs are recorded.

```python
"""Lab 4: group a synthetic Millbrook building-device list by system and flag unsupported firmware."""
devices = [("AHU-OT1", "HVAC", "2019", True), ("AHU-OT2", "HVAC", "2019", True),
           ("CHILLER-1", "HVAC", "2015", False), ("MGAS-PANEL", "medical gas alarm", "2021", True),
           ("LIFT-CTRL", "elevator", "2012", False), ("DOOR-SRV", "access control", "2020", True)]
by = {}
for name, system, year, supported in devices:
    by.setdefault(system, []).append(name)
    if not supported:
        print(f"UNSUPPORTED {name:10} system={system} installed={year}")
for system, names in sorted(by.items()):
    print(f"{system:18} {len(names)} device(s): {', '.join(names)}")
```

Run with `python3 lab_bms.py`. Verified output:

```text
UNSUPPORTED CHILLER-1  system=HVAC installed=2015
UNSUPPORTED LIFT-CTRL  system=elevator installed=2012
HVAC               3 device(s): AHU-OT1, AHU-OT2, CHILLER-1
access control     1 device(s): DOOR-SRV
elevator           1 device(s): LIFT-CTRL
medical gas alarm  1 device(s): MGAS-PANEL
```

### 4.3 Reading the output

Two devices are unsupported: CHILLER-1, installed in 2015, and LIFT-CTRL from 2012. "Unsupported" means the vendor will publish no fixes for new weaknesses. They cannot simply be replaced — a chiller costs a large sum and replacement takes planning — so they need compensating controls: tighter network isolation, no remote access, closer monitoring.

Section four point three develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point three, the mentor expects an claims to carry owners and dates.

### 4.4 Using the inventory

The inventory feeds advisory matching (Chapter 10), segmentation (Chapter 8) and the capstone risk report (Chapter 12). Keep it under access control.

Section four point four develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point four, the mentor expects an claims to carry owners and dates.

Section four point four treats what to record grouping as testable only when evidence and ticket IDs are recorded.

For section four point four, the organisation will not accept an work without a written trail.

### 4.5 Where the data comes from

The BMS contractor's handover file, estates maintenance records, purchase orders, the network team's switch tables and walk-downs in plant rooms all contribute. Each source misses something: handover files predate later additions, purchase records miss items bought by contractors, and plant rooms hold devices nobody listed. Comparing them, and recording which source supplied each field, makes the inventory trustworthy.

Section four point five develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point five, the mentor expects an claims to carry owners and dates.

### 4.6 Consequence column

Write the clinical consequence in plain words for each device, agreed with estates and clinical leads, so priorities are clear to non-specialists.

Section four point six develops an inventory of building devices with a the organisation note Aisha Bello can demo offline.

Under section four point six, the mentor expects an claims to carry owners and dates.

Section four point six treats what to record grouping as testable only when evidence and ticket IDs are recorded.

For section four point six, the organisation will not accept an work without a written trail.

### Worked example (synthetic Millbrook)

Aisha takes the two unsupported devices to the estates manager. They agree: CHILLER-1 is moved behind a dedicated firewall rule allowing only BMS-WS, and LIFT-CTRL's cellular link is reviewed with the lift contractor. Both are added to the capital replacement plan with target years.

> **Synthetic case — Millbrook.** Devices and years are invented.

### Errors and limits

Support status must be confirmed with the vendor; installation year alone is a hint. Inventories age; review quarterly.

### Exercises

- **EX016 — Inventory fields.** List six fields for a building-device inventory. *Rubric:* 3 = six correct fields including support status and consequence; 2 = four; 1 = two; 0 = none.
- **EX017 — Extending the lab.** Add `("BOILER-2", "HVAC", "2010", False)`. What new lines does the lab print? *Rubric:* 3 = "UNSUPPORTED BOILER-2 system=HVAC installed=2010" and HVAC 4 devices; 2 = one line; 1 = wrong; 0 = none.
- **EX018 — Meaning of unsupported.** Explain to the estates manager what "unsupported" means for CHILLER-1. *Rubric:* 3 = no vendor fixes for new flaws; risk grows; compensate and plan replacement; 2 = partial; 1 = "broken"; 0 = none.
- **EX019 — Compensating controls.** Propose three compensating controls for LIFT-CTRL. *Rubric:* 3 = isolation, remove/restrict cellular link, monitoring, replacement plan; 2 = two; 1 = one; 0 = none.
- **EX020 — Who to call.** Using the grouping, who receives the MGAS-PANEL entry? *Rubric:* 3 = medical gas authorised person; 2 = estates; 1 = IT; 0 = none.

### Synthesis

A system-grouped inventory with support status shows owners and where compensating controls must carry the risk.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Accounts, defaults and device baselines

### Learning outcomes

You will (1) find default and shared accounts on building systems; (2) apply ETSI EN 303 645 and NIST IR 8259 ideas to procurement; and (3) set practical password rules for estates staff.

### 5.1 Defaults in buildings

Controllers and web interfaces often leave the factory with documented usernames and passwords. Integrators sometimes keep one password across every site they maintain. Both mean that anyone who has read a manual or worked for that integrator can log in.

Section five point one develops accounts defaults and device baselines with a the organisation note Aisha Bello can demo offline.

Under section five point one, the mentor expects accounts claims to carry owners and dates.

Section five point one treats defaults in buildings shared as testable only when evidence and ticket IDs are recorded.

### 5.2 Shared estates accounts

The BMS workstation may have one login used by every shift engineer. That makes changes untraceable. Individual accounts, even if only on the BMS server, let the trend log name the person who changed a setpoint.

Section five point two develops accounts defaults and device baselines with a the organisation note Aisha Bello can demo offline.

Under section five point two, the mentor expects accounts claims to carry owners and dates.

Section five point two treats defaults in buildings shared as testable only when evidence and ticket IDs are recorded.

### 5.3 A procurement baseline

ETSI EN 303 645 requires no universal default passwords, a vulnerability disclosure policy, software updates and secure communication, among other provisions; NIST IR 8259 lists foundational activities manufacturers should perform. Hospital purchasing can turn these into contract questions for new building devices, so the problem shrinks over time.

Section five point three develops accounts defaults and device baselines with a the organisation note Aisha Bello can demo offline.

Under section five point three, the mentor expects accounts claims to carry owners and dates.

Section five point three treats defaults in buildings shared as testable only when evidence and ticket IDs are recorded.

### 5.4 Rules that estates staff can follow

Unique passwords per device stored in a managed password vault; named accounts on the BMS; admin rights only for planned work; passwords changed when a contractor's staff leave.

Section five point four develops accounts defaults and device baselines with a the organisation note Aisha Bello can demo offline.

Under section five point four, the mentor expects accounts claims to carry owners and dates.

Section five point four treats defaults in buildings shared as testable only when evidence and ticket IDs are recorded.

### 5.5 Checking the change worked

After a password is changed, try the old one from the BMS workstation in the same booked slot to confirm it fails, and confirm operators can still log in with the new arrangement.

Section five point five develops accounts defaults and device baselines with a the organisation note Aisha Bello can demo offline.

Under section five point five, the mentor expects accounts claims to carry owners and dates.

Section five point five treats defaults in buildings shared as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha and the BMS contractor review DOOR-SRV, the access control server. Its web interface still accepts the factory password listed in the public manual. The contractor changes it during a booked slot, records it in the hospital's vault, and creates named accounts for the three security officers who manage door schedules.

> **Synthetic case — Millbrook.** Device and accounts are invented.

### Errors and limits

ETSI EN 303 645 targets consumer IoT; for industrial-grade building controllers, IEC 62443-4-2 component requirements are a better match. Some old controllers allow only one account.

### Exercises

- **EX021 — Why integrator passwords matter.** Explain the risk of one integrator password reused across many hospitals. *Rubric:* 3 = one leak or ex-employee opens every site; 2 = partial; 1 = vague; 0 = none.
- **EX022 — Traceable changes.** How do named BMS accounts help after an unexpected setpoint change? *Rubric:* 3 = trend/audit log shows who changed it; supports investigation; 2 = partial; 1 = none; 0 = none.
- **EX023 — Contract questions.** Turn three ETSI EN 303 645 provisions into purchase-contract questions. *Rubric:* 3 = three accurate questions (defaults, disclosure, updates/encryption); 2 = two; 1 = one; 0 = none.
- **EX024 — Contractor leaver.** A contractor engineer who knew Millbrook passwords leaves the firm. What happens? *Rubric:* 3 = change affected passwords in vault, review access, record; 2 = some; 1 = nothing; 0 = none.
- **EX025 — Right standard.** Which standard fits an industrial BMS controller better than ETSI EN 303 645, and why? *Rubric:* 3 = IEC 62443-4-2; component requirements for industrial automation; 2 = name only; 1 = wrong; 0 = none.

### Synthesis

Changed defaults, named accounts, vaulted passwords and baseline contract questions close the easiest doors.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Internet exposure of building systems

### Learning outcomes

You will (1) explain why building interfaces end up on the internet; (2) compare an exposure export with an approved list; and (3) respond to an unapproved exposure.

### 6.1 How it happens

A contractor opens a port so they can reach the BMS web page from home; a lift company adds a router; a firewall rule from a project is never removed. MITRE ATT&CK for ICS lists T0883 Internet Accessible Device for exactly this situation, and CISA advisories repeatedly urge removing control system interfaces from direct internet access.

Section six point one develops internet exposure of building systems with a the organisation note Aisha Bello can demo offline.

Under section six point one, the mentor expects internet claims to carry owners and dates.

### 6.2 Checking exposure

The hospital's network team, or an authorised service, produces a list of the hospital's public addresses and open services. The analyst compares it with the approved list — normally only the remote access gateway.

Section six point two develops internet exposure of building systems with a the organisation note Aisha Bello can demo offline.

Under section six point two, the mentor expects internet claims to carry owners and dates.

Section six point two treats how it happens checking as testable only when evidence and ticket IDs are recorded.

```python
"""Lab 6: compare a synthetic external-exposure export with approved internet-facing services."""
approved = {("203.0.113.10", 443)}
found = [("203.0.113.10", 443, "VPN gateway"), ("203.0.113.24", 47808, "BACnet/IP"),
         ("203.0.113.24", 80, "BMS web login")]
for ip, port, svc in found:
    print(f"{ip}:{port:<6} {svc:14} {'approved' if (ip, port) in approved else 'NOT APPROVED - report'}")
print("unapproved:", sum((ip, port) not in approved for ip, port, _ in found))
```

Run with `python3 lab_exposure.py`. Verified output:

```text
203.0.113.10:443    VPN gateway    approved
203.0.113.24:47808  BACnet/IP      NOT APPROVED - report
203.0.113.24:80     BMS web login  NOT APPROVED - report
unapproved: 2
```

### 6.3 Reading the result

The VPN gateway on 203.0.113.10 port 443 is approved. Address 203.0.113.24 exposes BACnet/IP on 47808 and a BMS web login on 80. Both are unapproved: anyone on the internet could attempt to read or command controllers, or guess the web password.

Section six point three develops internet exposure of building systems with a the organisation note Aisha Bello can demo offline.

Under section six point three, the mentor expects internet claims to carry owners and dates.

Section six point three treats how it happens checking as testable only when evidence and ticket IDs are recorded.

### 6.4 Responding

Report at once to the network team and estates; ask the network owner to close the exposure through emergency change; check logs for connections from outside; find who opened it and why, and give them a supported route instead.

Section six point four develops internet exposure of building systems with a the organisation note Aisha Bello can demo offline.

Under section six point four, the mentor expects internet claims to carry owners and dates.

Section six point four treats how it happens checking as testable only when evidence and ticket IDs are recorded.

### 6.5 Preventing recurrence

Add a monthly exposure check to the network team's calendar, require an end date on every firewall rule opened for a project, and make contractors request remote access through the gateway process rather than asking for ports.

Section six point five develops internet exposure of building systems with a the organisation note Aisha Bello can demo offline.

Under section six point five, the mentor expects internet claims to carry owners and dates.

Section six point five treats how it happens checking as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

The network team traces 203.0.113.24 to a firewall rule added in 2023 for a chiller commissioning project. They remove it within the hour; firewall logs show many external connection attempts to port 47808 over recent months. The contractor is given gateway accounts instead.

> **Synthetic case — Millbrook.** The addresses are from the documentation range 203.0.113.0/24 and the events are invented.

### Errors and limits

Exposure lists are snapshots; repeat monthly. Only test addresses your organisation owns, through authorised means.

### Exercises

- **EX026 — How exposure happens.** Describe two ways a BMS interface becomes internet-reachable. *Rubric:* 3 = two concrete routes (contractor port, leftover rule, vendor router); 2 = one; 1 = vague; 0 = none.
- **EX027 — Third finding.** If the export also found 203.0.113.10 port 22, what would the lab print for it and the total? *Rubric:* 3 = NOT APPROVED line and "unapproved: 3"; 2 = one; 1 = approved; 0 = none.
- **EX028 — Technique name.** Which ATT&CK for ICS technique describes the 203.0.113.24 situation? *Rubric:* 3 = T0883 Internet Accessible Device; 2 = name only; 1 = wrong; 0 = none.
- **EX029 — Response steps.** List the response steps after finding an unapproved exposure. *Rubric:* 3 = report, emergency close via owner, check logs, find cause, provide safe alternative; 2 = three; 1 = one; 0 = none.
- **EX030 — Testing boundary.** Why does Aisha not test other hospitals' addresses "for comparison"? *Rubric:* 3 = not authorised, potentially illegal, could disrupt; 2 = one; 1 = fine; 0 = none.

### Synthesis

Only the gateway faces the internet; anything else found is reported, closed and replaced with a supported route.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Contractor and vendor remote access

### Learning outcomes

You will (1) inventory every remote route into building systems; (2) apply CISA AA21-042A lessons; and (3) design a controlled remote access process for contractors.

### 7.1 Many hands

A hospital may have separate contractors for BMS, chillers, lifts, fire alarms and access control, each wanting remote support. Without a policy, each installs its own route: a remote desktop tool on the workstation, a router, a cellular modem.

Section seven point one develops contractor and vendor remote access with a the organisation note Aisha Bello can demo offline.

Under section seven point one, the mentor expects contractor claims to carry owners and dates.

Section seven point one treats many hands lessons from as testable only when evidence and ticket IDs are recorded.

### 7.2 Lessons from AA21-042A

The CISA advisory on the 2021 compromise of a U.S. water treatment facility describes remote access software being used to reach a control system. Its recommendations include multi-factor authentication, strong remote desktop passwords, closing unused remote desktop ports and auditing remote connections. MITRE ATT&CK for ICS describes misuse of such routes as T0886 Remote Services.

Section seven point two develops contractor and vendor remote access with a the organisation note Aisha Bello can demo offline.

Under section seven point two, the mentor expects contractor claims to carry owners and dates.

### 7.3 A controlled process

One hospital-owned remote access gateway; a named, multi-factor account for each contractor engineer; accounts disabled by default and enabled per ticket; access limited to the specific system the contractor maintains; sessions recorded where possible; the account disabled when the session ends.

Section seven point three develops contractor and vendor remote access with a the organisation note Aisha Bello can demo offline.

Under section seven point three, the mentor expects contractor claims to carry owners and dates.

Section seven point three treats many hands lessons from as testable only when evidence and ticket IDs are recorded.

### 7.4 Removing the old routes

Once the gateway is in place, remove remote desktop tools installed directly on building workstations and disconnect unmanaged modems — in agreement with the contractor and estates, at a planned time, so support is not lost during an emergency.

Section seven point four develops contractor and vendor remote access with a the organisation note Aisha Bello can demo offline.

Under section seven point four, the mentor expects contractor claims to carry owners and dates.

Section seven point four treats many hands lessons from as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha's route inventory finds four ways in: the gateway, a remote desktop tool on BMS-WS installed by the BMS contractor, the lift's cellular link, and a chiller vendor's router. Estates agrees a plan: the remote desktop tool is removed in week 1 after the contractor's gateway account works; the chiller router in week 2; the lift link is restricted to the lift contractor's service centre with a ticket requirement.

> **Synthetic case — Millbrook.** Routes and timing are invented.

### Errors and limits

Some lift and fire alarm links are required for safety monitoring; restrict and record them rather than removing them blindly.

### Exercises

- **EX031 — Counting routes.** List the four remote routes Aisha found. *Rubric:* 3 = gateway, remote desktop on BMS-WS, lift cellular, chiller router; 2 = three; 1 = one; 0 = none.
- **EX032 — Applying the advisory.** Apply two AA21-042A recommendations to the BMS contractor's access. *Rubric:* 3 = MFA on gateway account and audit of sessions (or close RDP port/strong password); 2 = one; 1 = vague; 0 = none.
- **EX033 — Per-system limits.** Why should the chiller contractor's account not reach the access control server? *Rubric:* 3 = least privilege; compromise of one contractor limited to its system; 2 = partial; 1 = no reason; 0 = none.
- **EX034 — Removal timing.** Why is the remote desktop tool removed only after the gateway account works? *Rubric:* 3 = avoid losing support during an emergency; test replacement first; 2 = partial; 1 = no reason; 0 = none.
- **EX035 — Safety link.** The fire alarm monitoring link uses a cellular modem. Should it be unplugged? *Rubric:* 3 = no; safety monitoring; restrict, document and review with owner; 2 = no only; 1 = yes; 0 = none.

### Synthesis

All remote help goes through one gateway with named, multi-factor, ticketed accounts; legacy routes are retired carefully.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Segmentation for building networks

### Learning outcomes

You will (1) define zones and conduits for Millbrook's building systems using IEC 62443 terms; (2) write a minimal rule set; and (3) plan the migration without disrupting clinical areas.

### 8.1 Zones

IEC 62443-3-2 describes grouping assets into zones with similar security requirements and connecting them through conduits. At Millbrook a sensible start is: a BMS zone (controllers and BMS server), a safety-relevant zone (medical gas alarm and lift, each separately), an access control zone, a DMZ for the gateway and data exports, and the corporate zone.

Section eight point one develops segmentation for building networks with a the organisation note Aisha Bello can demo offline.

Under section eight point one, the mentor expects segmentation claims to carry owners and dates.

### 8.2 Conduits and rules

Write each conduit as a small set of rules: BMS-WS (moved into the BMS zone) to controllers on BACnet/IP; gateway to BMS-WS for contractor sessions; BMS server to a DMZ data server for energy reports. Everything else is denied. Corporate PCs never connect straight to controllers.

Section eight point two develops segmentation for building networks with a the organisation note Aisha Bello can demo offline.

Under section eight point two, the mentor expects segmentation claims to carry owners and dates.

Section eight point two treats zones conduits and rules as testable only when evidence and ticket IDs are recorded.

### 8.3 Fixing the dual-homed workstation

Removing BMS-WS's corporate network card closes the bridge from Chapter 3. Estates staff who need to view the BMS from offices use a read-only dashboard on the DMZ server, or a jump host reached through the gateway.

Section eight point three develops segmentation for building networks with a the organisation note Aisha Bello can demo offline.

Under section eight point three, the mentor expects segmentation claims to carry owners and dates.

Section eight point three treats zones conduits and rules as testable only when evidence and ticket IDs are recorded.

### 8.4 Migrating safely

Change one conduit at a time, at times agreed with estates and theatre managers; watch for lost points on the BMS after each step; keep the previous configuration ready to restore.

Section eight point four develops segmentation for building networks with a the organisation note Aisha Bello can demo offline.

Under section eight point four, the mentor expects segmentation claims to carry owners and dates.

Section eight point four treats zones conduits and rules as testable only when evidence and ticket IDs are recorded.

### 8.5 Documentation

Publish the zone diagram and rule table with revision numbers and owners so contractors can request changes against them.

Section eight point five develops segmentation for building networks with a the organisation note Aisha Bello can demo offline.

Under section eight point five, the mentor expects segmentation claims to carry owners and dates.

Section eight point five treats zones conduits and rules as testable only when evidence and ticket IDs are recorded.

For section eight point five, the organisation will not accept segmentation work without a written trail.

### Worked example (synthetic Millbrook)

Over three planned Saturday mornings the network team creates the zones, moves BMS-WS fully into the BMS zone and deploys the rules. After step 2 two controllers stop reporting; the cause is a forgotten conduit to a time server, which is added under the same change. Energy reports now come from the DMZ server.

> **Synthetic case — Millbrook.** Steps and findings are invented.

### Errors and limits

Segmentation does not stop an attacker who already has gateway credentials; it limits where they can go. Zone designs must be reviewed when systems are added.

### Exercises

- **EX036 — Zone list.** Propose five zones for Millbrook. *Rubric:* 3 = BMS, safety-relevant (gas/lift), access control, DMZ, corporate; 2 = four; 1 = two; 0 = none.
- **EX037 — Writing a conduit.** Write the rule letting the BMS server send energy data to the DMZ server. *Rubric:* 3 = source BMS server, destination DMZ data server, specific port, allow; plus default deny; 2 = no deny; 1 = any; 0 = none.
- **EX038 — Office viewing.** How do estates staff view the BMS from their offices after BMS-WS loses its corporate card? *Rubric:* 3 = read-only DMZ dashboard or jump host via gateway; 2 = partial; 1 = re-add card; 0 = none.
- **EX039 — Lost points.** Two controllers stop reporting after a rule change. What is the safe response? *Rubric:* 3 = check clinical impact, restore previous config if needed, find missing conduit, fix under change; 2 = partial; 1 = ignore; 0 = none.
- **EX040 — Limit of segmentation.** What does segmentation not protect against? *Rubric:* 3 = misuse of legitimate gateway credentials/insider within allowed conduits; 2 = vague; 1 = everything protected; 0 = none.

### Synthesis

Zones with narrow conduits stop office compromises from reaching controllers; migrate one conduit at a time.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Monitoring trends and logs

### Learning outcomes

You will (1) use BMS trend logs as security evidence; (2) flag changes outside approved windows with a short script; and (3) combine trend, login and network evidence.

### 9.1 Trends as evidence

A BMS records values over time — temperatures, setpoints, valve positions — mainly for engineers. The same records show when a setpoint changed and, with named accounts, who changed it. They are often the best evidence of tampering in a building system.

Section nine point one develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point one, the mentor expects monitoring claims to carry owners and dates.

Section nine point one treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

### 9.2 Change windows

Estates agrees windows for planned setpoint changes, for example weekday mornings. A change outside a window is not necessarily malicious, but it needs an explanation.

Section nine point two develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point two, the mentor expects monitoring claims to carry owners and dates.

Section nine point two treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

```python
"""Lab 9: flag operating-theatre temperature setpoint changes outside a synthetic change window."""
trend = [("01:00", 20.0), ("02:00", 20.0), ("03:00", 26.0), ("04:00", 26.0), ("09:00", 21.0)]
window = ("08:00", "10:00")
prev = None
for t, sp in trend:
    if prev is not None and sp != prev:
        inside = window[0] <= t <= window[1]
        print(f"{t} setpoint {prev}->{sp} {'in window' if inside else 'OUTSIDE WINDOW - review'}")
    prev = sp
```

Run with `python3 lab_trend.py`. Verified output:

```text
03:00 setpoint 20.0->26.0 OUTSIDE WINDOW - review
09:00 setpoint 26.0->21.0 in window
```

### 9.3 Reading the output

At 03:00 the theatre setpoint rose from 20 °C to 26 °C, outside the 08:00–10:00 window; it was set back to 21 °C at 09:00 inside the window. The 03:00 change is the one to review.

Section nine point three develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point three, the mentor expects monitoring claims to carry owners and dates.

Section nine point three treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

### 9.4 Combining sources

Check the BMS audit log for who was logged in at 03:00; the gateway log for remote sessions; the firewall log for connections to the BMS zone. Agreement between sources strengthens the conclusion either way.

Section nine point four develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point four, the mentor expects monitoring claims to carry owners and dates.

Section nine point four treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

### 9.5 Alerting

Where the BMS supports it, raise an alarm for setpoint changes outside windows on critical units, sent to the estates on-call engineer.

Section nine point five develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point five, the mentor expects monitoring claims to carry owners and dates.

Section nine point five treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

For section nine point five, the organisation will not accept monitoring work without a written trail.

### 9.6 Keeping evidence

When a change needs review, export the relevant trend and audit records the same day, note the export time, and store them with the review notes; BMS retention is often short.

Section nine point six develops monitoring trends and logs with a the organisation note Aisha Bello can demo offline.

Under section nine point six, the mentor expects monitoring claims to carry owners and dates.

Section nine point six treats trends as evidence change as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha checks the logs: no gateway sessions at 03:00, but the BMS audit log shows the night engineer raised the setpoint during a chiller fault to reduce load, and forgot to record it. The explanation is documented, and the on-call procedure gains a step: record any out-of-window change in the shift log.

> **Synthetic case — Millbrook.** The trend and explanation are invented.

### Errors and limits

Trend logs may sample infrequently and miss short changes; clocks must be synchronised. Retention may be weeks only — export what you need.

### Exercises

- **EX041 — Window logic.** Why is the 09:00 change not flagged? *Rubric:* 3 = 09:00 falls inside 08:00–10:00 window; 2 = "allowed"; 1 = wrong; 0 = none.
- **EX042 — Modified trend.** If the window were 02:00–04:00, what would the lab print? *Rubric:* 3 = 03:00 "in window", 09:00 "OUTSIDE WINDOW - review"; 2 = one; 1 = same; 0 = none.
- **EX043 — Three sources.** Which three logs does Aisha combine with the trend? *Rubric:* 3 = BMS audit, gateway, firewall; 2 = two; 1 = one; 0 = none.
- **EX044 — Clinical impact.** What clinical impact could a theatre setpoint of 26 °C have overnight? *Rubric:* 3 = theatre unusable/out of specification at start of list, delay or infection-control concern; 2 = partial; 1 = none; 0 = none.
- **EX045 — Process improvement.** What change prevents the next unexplained out-of-window change? *Rubric:* 3 = shift log entry required, alarm on out-of-window change; 2 = one; 1 = blame; 0 = none.

### Synthesis

Trend logs show what changed and when; combined with access logs they explain it.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Advisories and patching for building systems

### Learning outcomes

You will (1) match advisories to the building inventory; (2) decide between patching and mitigation; and (3) track decisions over time.

### 10.1 Sources

CISA's advisories index includes many building automation, access control and lift products, alongside vendor notices. Subscribe to those relevant to Millbrook's vendors.

Section ten point one develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

Under section ten point one, the mentor expects advisories claims to carry owners and dates.

Section ten point one treats sources matching choosing tracking as testable only when evidence and ticket IDs are recorded.

For section ten point one, the organisation will not accept advisories work without a written trail.

### 10.2 Matching

For each advisory: is the product in our inventory, at an affected version, reachable in the way the advisory describes? Unsupported devices (Chapter 4) often match old advisories that will never be fixed.

Section ten point two develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

Under section ten point two, the mentor expects advisories claims to carry owners and dates.

Section ten point two treats sources matching choosing tracking as testable only when evidence and ticket IDs are recorded.

### 10.3 Choosing

Patching a BMS controller usually needs a contractor visit, a booked slot and checks of every point afterwards. Mitigations — firewall rules, disabling a web interface, restricting the gateway account — can often be applied sooner. Record which you chose and why.

Section ten point three develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

Under section ten point three, the mentor expects advisories claims to carry owners and dates.

Section ten point three treats sources matching choosing tracking as testable only when evidence and ticket IDs are recorded.

### 10.4 Tracking

A simple register: advisory, products affected here, decision, mitigation, patch date, owner, review date. Report open high-consequence items to the estates manager monthly.

Section ten point four develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

Under section ten point four, the mentor expects advisories claims to carry owners and dates.

Section ten point four treats sources matching choosing tracking as testable only when evidence and ticket IDs are recorded.

For section ten point four, the organisation will not accept advisories work without a written trail.

### 10.5 Testing after patching

Afterwards, the contractor confirms every point reports, alarms work and schedules are correct; estates signs off.

Section ten point five develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

Under section ten point five, the mentor expects advisories claims to carry owners and dates.

Section ten point five treats sources matching choosing tracking as testable only when evidence and ticket IDs are recorded.

For section ten point five, the organisation will not accept advisories work without a written trail.

### 10.6 Vendor contact

When an advisory is unclear about building configurations, ask the vendor or integrator directly: which models and options are affected, whether the vulnerable feature is enabled by default, and whether a mitigation has been tested on systems like Millbrook's. Record the answer and who gave it. Vendors' product security teams usually respond faster when the question names the exact model and version from the inventory.

Section ten point six develops advisories and patching for building with a the organisation note Aisha Bello can demo offline.

### Worked example (synthetic Millbrook)

A synthetic advisory warns that DOOR-SRV's web interface allows authentication bypass in version 4.1; Millbrook runs 4.1. The interface is reachable only from the access control zone after Chapter 8, and the vendor fix 4.2 needs a 30-minute outage of door scheduling. The decision: restrict the interface to the security office's workstation today, patch on Sunday 06:00 with manual keys issued to ward managers during the outage.

> **Synthetic case — Millbrook.** The advisory and versions are invented; real advisories are listed by CISA.

### Errors and limits

Advisories may omit details; ask vendors. A mitigation must be checked to actually block the described path.

### Exercises

- **EX046 — Three matching questions.** State the three questions that decide whether an advisory matters here. *Rubric:* 3 = product present, version affected, reachable as described; 2 = two; 1 = one; 0 = none.
- **EX047 — Unsupported match.** An advisory affects LIFT-CTRL with no fix planned. What is the decision? *Rubric:* 3 = compensating isolation/monitoring, record, accelerate replacement; 2 = partial; 1 = ignore; 0 = none.
- **EX048 — Door outage plan.** Why issue manual keys during the DOOR-SRV patch? *Rubric:* 3 = door schedules unavailable, restricted areas must stay controlled and accessible; 2 = partial; 1 = no reason; 0 = none.
- **EX049 — Register entry.** Write the tracking entry for the DOOR-SRV advisory. *Rubric:* 3 = advisory, product/version, decision, mitigation, patch date, owner, review; 2 = most; 1 = little; 0 = none.
- **EX050 — Checking a mitigation.** How would you confirm the interface restriction works? *Rubric:* 3 = network owner confirms rule; authorised test from another zone fails and from security office succeeds; 2 = partial; 1 = assume; 0 = none.

### Synthesis

Advisories are matched, mitigated quickly, patched at booked times with fall-backs, and tracked to closure.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Incident response for hospital building systems

### Learning outcomes

You will (1) adapt the incident response steps to building systems; (2) decide when to isolate the BMS; and (3) coordinate with clinical, estates and IT teams.

### 11.1 Planning ahead

NIST SP 800-82r3 stresses preparing OT incident response with operations staff. In a hospital that means estates, clinical site managers, the IT security team and contractors agree beforehand: who leads, what each system's manual fall-back is, and how to reach contractors at night.

Section eleven point one develops incident response for hospital building with a the organisation note Aisha Bello can demo offline.

Under section eleven point one, the mentor expects incident claims to carry owners and dates.

Section eleven point one treats planning ahead detect and as testable only when evidence and ticket IDs are recorded.

### 11.2 Detect and assess

An alarm, an out-of-window setpoint or a ransom note on BMS-WS starts the process. The first question is clinical: is any area unsafe now? The site manager and estates decide immediate protective steps — moving a theatre list, switching to cylinder oxygen alarms monitored by staff.

Section eleven point two develops incident response for hospital building with a the organisation note Aisha Bello can demo offline.

Under section eleven point two, the mentor expects incident claims to carry owners and dates.

Section eleven point two treats planning ahead detect and as testable only when evidence and ticket IDs are recorded.

### 11.3 Contain

If the BMS cannot be trusted, controllers can usually run their last programmed schedules without the server. Isolating the BMS zone at its firewall stops further remote commands while plant keeps running locally. Estates staff patrol plant rooms and check critical values by hand.

Section eleven point three develops incident response for hospital building with a the organisation note Aisha Bello can demo offline.

Under section eleven point three, the mentor expects incident claims to carry owners and dates.

Section eleven point three treats planning ahead detect and as testable only when evidence and ticket IDs are recorded.

### 11.4 Evidence and recovery

Preserve logs and images before rebuilding; restore BMS-WS and the server from verified backups; check every critical point against local readings; reconnect conduits one at a time.

Section eleven point four develops incident response for hospital building with a the organisation note Aisha Bello can demo offline.

Under section eleven point four, the mentor expects incident claims to carry owners and dates.

Section eleven point four treats planning ahead detect and as testable only when evidence and ticket IDs are recorded.

For section eleven point four, the organisation will not accept incident work without a written trail.

### 11.5 Communication

The incident lead informs hospital management, who decide about external notification. Analysts do not contact the press or regulators themselves.

Section eleven point five develops incident response for hospital building with a the organisation note Aisha Bello can demo offline.

Under section eleven point five, the mentor expects incident claims to carry owners and dates.

Section eleven point five treats planning ahead detect and as testable only when evidence and ticket IDs are recorded.

For section eleven point five, the organisation will not accept incident work without a written trail.

### Worked example (synthetic Millbrook)

At 22:40 BMS-WS shows a ransom message. Estates confirms theatres are empty and wards normal. The network team blocks the BMS zone conduits at 22:55; controllers continue on their schedules. Estates engineers patrol hourly. Next morning BMS-WS is rebuilt from a verified image, the server checked, and conduits restored by 14:00 after point checks.

> **Synthetic case — Millbrook.** The incident is invented.

### Errors and limits

Some controllers fail to safe defaults that differ from normal operation; know them before isolating. Patrol-based monitoring cannot last indefinitely; plan staffing.

### Exercises

- **EX051 — First question.** What is the first question after BMS-WS shows a ransom message, and who answers it? *Rubric:* 3 = is any clinical area unsafe; site manager/estates; 2 = question only; 1 = IT question; 0 = none.
- **EX052 — Why isolation is acceptable.** Explain why blocking the BMS zone conduits did not stop ventilation. *Rubric:* 3 = controllers run local schedules without server; 2 = partial; 1 = it did stop; 0 = none.
- **EX053 — Manual monitoring.** What replaces BMS monitoring while it is isolated? *Rubric:* 3 = estates patrols reading local values, staff checks of alarms; 2 = partial; 1 = nothing; 0 = none.
- **EX054 — Reconnecting.** Describe how conduits are restored after recovery. *Rubric:* 3 = one at a time with point checks against local readings; 2 = partial; 1 = all at once; 0 = none.
- **EX055 — Safe defaults.** Why must Aisha know controllers' fail-safe behaviour before recommending isolation? *Rubric:* 3 = some defaults change operation (e.g. fans off/full), could affect patients; 2 = partial; 1 = no need; 0 = none.

### Synthesis

Clinical safety leads, local control carries the plant, isolation stops remote harm and evidence precedes recovery.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Capstone: a building-systems risk report

### Learning outcomes

You will (1) assemble inventory, exposure, access, segmentation and monitoring findings into a risk report; (2) prioritise by clinical consequence and likelihood; and (3) present it to hospital managers.

### 12.1 Structure

Scope and method; systems in scope with owners; findings, each with evidence; risk rating; recommended actions with owners and dates; residual risk the hospital accepts. Keep it to a few pages with an appendix for evidence.

Section twelve point one develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point one, the mentor expects capstone claims to carry owners and dates.

Section twelve point one treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

### 12.2 Rating

Rate consequence (patient harm, service loss) and likelihood (exposure, ease, known activity) on simple three-level scales, agreed with estates and clinical leads. A medium likelihood with severe patient consequence usually outranks a high likelihood with minor consequence.

Section twelve point two develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point two, the mentor expects capstone claims to carry owners and dates.

Section twelve point two treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

### 12.3 Recommendations

Each one names a specific change, an owner, a date and how completion will be shown. Include quick wins (closing exposure, removing old remote tools) and longer projects (replacing unsupported plant).

Section twelve point three develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point three, the mentor expects capstone claims to carry owners and dates.

Section twelve point three treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

### 12.4 Presenting

Lead with the top three risks in patient terms; show what has already improved; ask for decisions, not admiration.

Section twelve point four develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point four, the mentor expects capstone claims to carry owners and dates.

Section twelve point four treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

For section twelve point four, the organisation will not accept capstone work without a written trail.

### 12.5 Evidence appendix

For each finding, keep the photograph, log extract or configuration excerpt that supports it, with the date and who collected it. Managers rarely read the appendix, but auditors and the next analyst will, and it lets anyone check that the finding was real.

Section twelve point five develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point five, the mentor expects capstone claims to carry owners and dates.

Section twelve point five treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

### 12.6 After the meeting

Record the decisions taken, owners and dates in the tracking register, send a one-page summary to attendees, and book the six-month review. Progress against the actions becomes the opening slide next time, which keeps attention on change rather than on new findings.

Section twelve point six develops capstone building-systems risk report with a the organisation note Aisha Bello can demo offline.

Under section twelve point six, the mentor expects capstone claims to carry owners and dates.

Section twelve point six treats structure rating recommendations presenting as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic Millbrook)

Aisha's report lists: (1) LIFT-CTRL unsupported with a cellular link — consequence high (patient transfers), likelihood medium; (2) residual contractor accounts not disabled after sessions — consequence high, likelihood medium; (3) trend logs kept only 14 days — consequence medium, likelihood high. Already fixed: internet exposure of BACnet, dual-homed BMS-WS, DOOR-SRV default password. Managers approve funding to replace LIFT-CTRL next year and a weekly check of gateway accounts.

> **Synthetic case — Millbrook.** The report and ratings are invented.

### Errors and limits

A report reflects the evidence available on its date; schedule a review. It is not a formal IEC 62443 assessment.

### Exercises

- **EX056 — Report sections.** List the six sections of the risk report. *Rubric:* 3 = scope/method, systems/owners, findings/evidence, rating, actions, residual risk; 2 = four; 1 = two; 0 = none.
- **EX057 — Ranking two risks.** Rank "BMS trend retention 14 days" against "lift unsupported with cellular link" and justify. *Rubric:* 3 = lift first; patient-transfer consequence outweighs evidence-loss consequence; 2 = right order; 1 = reversed; 0 = none.
- **EX058 — Writing a recommendation.** Write a complete recommendation for residual contractor accounts. *Rubric:* 3 = specific change, owner, date, evidence of completion; 2 = three; 1 = vague; 0 = none.
- **EX059 — Opening the presentation.** Write the opening sentence of Aisha's presentation to managers. *Rubric:* 3 = top risk in patient terms with ask; 2 = clear but technical; 1 = jargon; 0 = none.
- **EX060 — Residual risk.** Give one residual risk Millbrook must accept until next year, and why it is acceptable. *Rubric:* 3 = LIFT-CTRL until replacement with compensating controls named; 2 = risk only; 1 = none accepted; 0 = none.

### Synthesis

A short, evidenced, consequence-ranked report with owned actions turns findings into funded change.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Millbrook Hospital Building Systems, Aisha Bello and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Air-handling units control theatre temperature, humidity and pressure; chillers provide cooling water; medical gas alarm panels warn of gas pressure faults; elevator controllers move cars between floors; access control locks and unlocks restricted doors.

**EX002.** When the air-handling unit's controller joins the network, anyone reaching it can change fan speeds or setpoints from a screen far from the plant room. A theatre could lose pressure or temperature control without anyone touching the unit.

**EX003.** Positive pressure keeps unfiltered corridor air out of the sterile field; losing it raises the risk of surgical site infection and can force surgery to be postponed.

**EX004.** Ward staff would not learn that oxygen pressure had fallen, so patients relying on piped oxygen could be harmed before anyone noticed and switched to cylinders.

**EX005.** Building systems often fall between estates, contractors and IT, so nobody patches, monitors or reviews access; naming an owner makes every later control possible.

**EX006.** Restarting the AHU-OT1 controller to load a patch during a theatre list would stop air supply and pressure control while a patient is open on the table.

**EX007.** Cylinder oxygen backs up the piped medical gas supply; manual keys back up electronic access control; portable cooling backs up the HVAC plant and chillers.

**EX008.** The medical gas authorised person, working within the estates permit system, controls any work on medical gas systems, including the alarm panel.

**EX009.** Reaching some controllers means opening ceiling or wall panels in or near a clean area, which can release dust and contaminate the theatre unless infection control agrees timing and precautions.

**EX010.** If cylinders, manual keys and portable cooling can keep wards safe, Aisha can show that disconnecting the BMS network leaves patients supported, which makes the decision acceptable to clinical managers.

**EX011.** In the field layer, sensors and actuators are wired to local controllers; in the supervisory layer, those controllers communicate with each other and the BMS server and workstation over the building network.

**EX012.** It can usually read every point and often write setpoints or commands, because classic BACnet/IP installations do not authenticate the sender.

**EX013.** BMS-WS connects the corporate VLAN directly to VLAN 300 without passing a firewall, so malware or an attacker on the workstation gains reach to every building controller.

**EX014.** The dual-homed BMS-WS, the contractor's remote access link, and the lift manufacturer's cellular connection.

**EX015.** Some old controllers fail when scanned, which could stop ventilation in clinical areas; and drawings plus switch configuration give the same picture without touching live plant.

**EX016.** System, device name, location, owner, firmware version, vendor support status, network address, and clinical consequence of failure.

**EX017.** It prints `UNSUPPORTED BOILER-2   system=HVAC installed=2010` and the HVAC line becomes `HVAC               4 device(s): AHU-OT1, AHU-OT2, CHILLER-1, BOILER-2`.

**EX018.** The chiller's vendor will not publish fixes for weaknesses found from now on, so its risk grows over time; we must protect it in other ways and plan its replacement.

**EX019.** Place LIFT-CTRL in its own network segment reachable only by its maintenance gateway; restrict or remove the cellular link unless used under a ticket; monitor its connections; schedule replacement in the capital plan.

**EX020.** The medical gas authorised person, because the medical gas alarm system is theirs.

**EX021.** If that one password leaks, or an engineer who knew it leaves on bad terms, every hospital maintained by the integrator is open at once.

**EX022.** The BMS audit or trend log records which named account made the change, so the hospital can ask that person why and quickly separate a mistake from misuse.

**EX023.** "Does each device ship with a unique password or force one at setup?" "Do you publish a vulnerability disclosure policy and contact?" "For how many years will you provide security updates, and is communication encrypted?"

**EX024.** Change every password that engineer knew, with new values stored in the vault; review which accounts and remote access he held and disable them; record the change.

**EX025.** IEC 62443-4-2, because it sets security requirements for components of industrial automation and control systems, which is what BMS controllers are.

**EX026.** A contractor forwards a port so the BMS web page works from home; a project firewall rule stays after commissioning ends.

**EX027.** `203.0.113.10:22     ...  NOT APPROVED - report` for the new entry, and the total becomes `unapproved: 3`, since only port 443 on that address is approved.

**EX028.** T0883 Internet Accessible Device.

**EX029.** Report to the network team and estates; have the owner close it through an emergency change; review logs for external connections; find who opened it and why; give that party gateway access instead.

**EX030.** She has no authorisation for systems Millbrook does not own; probing them could break the law and disrupt another hospital's plant.

**EX031.** The hospital's remote access gateway; a remote desktop tool on BMS-WS; the lift's cellular link; the chiller vendor's router.

**EX032.** Give the BMS contractor's engineers individual gateway accounts with multi-factor authentication, and review the gateway's session logs after each support visit.

**EX033.** Each contractor needs only its own system; limiting the account means a stolen chiller-contractor password cannot open pharmacy or maternity doors.

**EX034.** If the old tool is removed first and the gateway account fails, the contractor could not help during a plant failure; testing the replacement first keeps support continuous.

**EX035.** No — fire alarm monitoring is a life-safety function; document the link, confirm with the fire safety owner that it only reaches the monitoring centre, and review it, rather than disconnecting it.

**EX036.** A BMS zone; a medical gas alarm zone and a lift zone (safety-relevant); an access control zone; a DMZ; the corporate zone.

**EX037.** "BMS server → DMZ data server on the agreed export port, allow", with the final "any → any deny" catching everything not listed.

**EX038.** They open a read-only dashboard on the DMZ data server, or, for changes, connect through the gateway to a jump host inside the BMS zone.

**EX039.** Confirm with estates whether the missing points affect clinical areas, restore the previous configuration if they do, identify the missing conduit (here a time server) and add it under the same change record.

**EX040.** It does not stop someone using valid gateway credentials, or an insider, from doing harm within the conduits that are allowed.

**EX041.** The script only flags a change whose time falls outside 08:00–10:00, and 09:00 lies inside that window.

**EX042.** `03:00 setpoint 20.0->26.0 in window` and `09:00 setpoint 26.0->21.0 OUTSIDE WINDOW - review`.

**EX043.** The BMS audit log, the remote access gateway log and the firewall log for the BMS zone.

**EX044.** The theatre would be out of its temperature range when the morning list starts, so surgery may be delayed until conditions recover, and staff comfort and sterility conditions would be compromised.

**EX045.** Require every out-of-window change to be written in the shift log with the reason, and configure a BMS alarm to the on-call engineer when a critical setpoint changes outside the window.

**EX046.** Do we have the product? Are we running an affected version? Can the weakness be reached in the way the advisory describes?

**EX047.** Record that it applies and cannot be patched, keep LIFT-CTRL isolated with only its maintenance route, monitor its connections, and raise its replacement priority in the capital plan.

**EX048.** During the 30-minute outage electronic door schedules may not work, so ward managers need keys to keep pharmacy and maternity doors both secure and usable.

**EX049.** "Advisory: DOOR-SRV web auth bypass, v4.1 (ours). Decision: mitigate then patch. Mitigation: interface limited to security office workstation. Patch 4.2 Sunday 06:00 with manual keys. Owner: estates security systems lead. Review after patch."

**EX050.** Ask the network owner to show the rule, then, under an agreed test, confirm the web page loads from the security office workstation and fails from another access-control-zone host.

**EX051.** "Is any clinical area unsafe right now?" — answered by the clinical site manager together with estates, before any technical action.

**EX052.** The field controllers hold their own programs and schedules and keep running the air-handling units without the BMS server or workstation; the firewall only stopped commands from outside the zone.

**EX053.** Hourly estates patrols reading local displays in plant rooms, and ward and theatre staff watching local alarms, including the medical gas panels.

**EX054.** After rebuilding, the network team re-enables one conduit at a time, and estates compares each critical BMS point with local readings before the next conduit is restored.

**EX055.** Some controllers revert to defaults such as fans at fixed speed or dampers closed when they lose the server, which could disturb theatre pressure, so the recommendation must account for that behaviour.

**EX056.** Scope and method; systems in scope and owners; findings with evidence; risk rating; recommended actions with owners and dates; accepted residual risk.

**EX057.** The lift comes first: if it is misused or fails, patient transfers between floors are delayed, a direct clinical harm, whereas short trend retention mainly weakens investigations.

**EX058.** "Gateway accounts are disabled automatically at the end of each ticketed session; owner: network team lead; by end of next month; evidence: weekly report showing no enabled contractor accounts outside open tickets."

**EX059.** "Our lifts carry patients between theatres and wards, and their controller can no longer be patched; we are asking you to fund its replacement next year."

**EX060.** LIFT-CTRL stays in service until replacement; this is acceptable because it is isolated in its own zone, its cellular link is restricted to the contractor's service centre under tickets, and its connections are monitored.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0883 Internet Accessible Device, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
