# OT, IoT and Cyber-Physical Security: A Rapid Introduction

- Language: English (`en`); rapid course, one month; approximately 80 hours of planned study.
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: new learners with no prior OT background.
- Relation to neighbouring books: the [professional course book](../../../../professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md) develops each topic into practice. **This book is a four-chapter introduction.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to access real sites. All sites, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapter 1 defines OT, IoT and CPS; Chapter 2 covers assets, networks and exposure; Chapter 3 covers recognising and reporting problems; Chapter 4 covers habits, response basics, limits and next steps. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, twelve or thirteen exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 2 and 3 read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Elmstead Solar and Battery Site** — inverters INV-01 to INV-04, battery energy storage system with battery management system, site controller SC-1, cameras, vendor monitoring portal | Site studied throughout | Invented |
| **Jonah Park** | Trainee at Elmstead | Invented |

### Core sources

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — What OT, IoT and cyber-physical security are

### Learning outcomes

You will (1) define operational technology, IoT and cyber-physical systems; (2) identify them at a solar and battery site; (3) explain why their security priorities differ from office IT; and (4) name the main public guidance.

### 1.1 Three overlapping terms

Operational technology (OT) is hardware and software that monitors or controls physical equipment and processes; NIST SP 800-82r3 is the main U.S. guide to securing it. The Internet of Things (IoT) is networked devices that sense or act on the world, often small and cloud-connected. A cyber-physical system (CPS) is any system where computing and physical processes are tightly linked. A modern energy site is all three at once.

### 1.2 A solar and battery site

Rows of solar panels feed inverters that turn direct current into grid alternating current. A battery energy storage system (BESS) stores energy, managed by a battery management system that watches cell temperatures and voltages. A site controller decides when to charge and discharge, following a schedule and instructions from the grid operator. Weather stations, cameras and the fire detection panel complete the picture. Many devices also report to vendor clouds.

### 1.3 Priorities

In office IT, protecting confidential data often comes first. On an energy site the first priorities are safety — batteries can overheat and catch fire — and keeping the process stable and available. Integrity of commands matters enormously: a false "discharge now" can damage equipment or disturb the grid. Confidentiality still matters, but rarely first.

### 1.4 Why it is a real concern

Industrial and IoT devices were often designed for closed networks and trusted users. Today they are reachable through remote access, clouds and shared networks. CISA publishes advisories for industrial products every week, and IoT botnets such as Mirai, studied by Antonakakis and colleagues, showed how many devices can be taken over through default passwords.

### 1.5 The guidance map

IEC 62443 is the international series for industrial automation security; NIST IR 8259 and ETSI EN 303 645 set baselines for IoT products; MITRE ATT&CK for ICS catalogues adversary techniques; CISA advisories report real weaknesses and incidents.

### Worked example (synthetic Elmstead)

Jonah Park joins Elmstead Solar and Battery Site as a trainee. On a tour he lists: inverters INV-01 to INV-04, the BESS with its battery management system, site controller SC-1, a connection to the grid operator, two cameras and a vendor monitoring portal. Next to each he writes one physical consequence of failure.

> **Synthetic case — Elmstead Solar and Battery Site.** The site, Jonah Park and every figure in this book are invented for teaching.

### Errors and limits

These definitions overlap; organisations use them differently. This book is introductory and grants no authority to access any real site.

### Exercises

- **EX001 — Defining OT.** Give a one-sentence definition of operational technology. *Rubric:* 3 = systems monitoring/controlling physical processes, hardware+software; 2 = partial; 1 = "factory computers"; 0 = none.
- **EX002 — IoT in your own words.** What distinguishes an IoT device from an office laptop? *Rubric:* 3 = senses/acts on physical world, often small, networked/cloud; 2 = partial; 1 = vague; 0 = none.
- **EX003 — CPS example.** Give an example of a cyber-physical system outside energy. *Rubric:* 3 = valid example with computing-physical link explained; 2 = example only; 1 = non-CPS; 0 = none.
- **EX004 — Inverter role.** What does an inverter do at Elmstead? *Rubric:* 3 = converts panel DC to grid AC; 2 = "converts power"; 1 = stores; 0 = none.
- **EX005 — Battery management.** Name two things the battery management system watches. *Rubric:* 3 = cell temperature and voltage (or state of charge); 2 = one; 1 = wrong; 0 = none.
- **EX006 — Deciding charge times.** Which device decides when the battery charges and discharges? *Rubric:* 3 = site controller SC-1 following schedule/grid operator; 2 = SC-1 only; 1 = inverter; 0 = none.
- **EX007 — First priority.** State the first security priority at a battery site and why. *Rubric:* 3 = safety, battery fire/overheating risk to people; 2 = safety only; 1 = confidentiality; 0 = none.
- **EX008 — False discharge.** Describe the harm of a false "discharge now" command. *Rubric:* 3 = equipment stress/damage, grid disturbance, breach of schedule; 2 = one; 1 = vague; 0 = none.
- **EX009 — Botnet lesson.** What did the Mirai botnet show about IoT devices? *Rubric:* 3 = many devices taken over via default passwords at large scale; 2 = partial; 1 = "viruses"; 0 = none.
- **EX010 — Matching guidance.** Which source fits each need: (a) industrial automation security series; (b) consumer IoT baseline; (c) adversary techniques? *Rubric:* 3 = IEC 62443, ETSI EN 303 645, ATT&CK for ICS; 2 = two; 1 = one; 0 = none.
- **EX011 — Advisories.** Who publishes advisories about weaknesses in industrial products in the U.S.? *Rubric:* 3 = CISA (with vendors); 2 = "government"; 1 = wrong; 0 = none.
- **EX012 — Listing the site.** List five Elmstead components from the tour. *Rubric:* 3 = five correct; 2 = four; 1 = two; 0 = none.
- **EX013 — Your authority.** Does finishing this book allow Jonah to log into Elmstead's inverters? Explain. *Rubric:* 3 = no; needs owner authorisation/role; book grants none; 2 = no only; 1 = yes; 0 = none.

### Synthesis

OT, IoT and CPS join computing to physical equipment; at an energy site safety and command integrity come first.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Assets, networks and exposure

### Learning outcomes

You will (1) explain why an inventory comes first; (2) review a device list for common weaknesses; (3) describe how a site network should be separated; and (4) recognise internet exposure and remote access risks.

### 2.1 Inventory first

You cannot protect what you do not know exists. NIST SP 800-82r3 places asset inventory at the foundation. For each device record name, function, location, owner, firmware version, network address and whether it connects to a cloud.

```python
"""Lab 2: review a synthetic Elmstead inverter list for default passwords, old firmware and cloud links."""
inv = [("INV-01", "5.1", False, True), ("INV-02", "5.1", True, True),
       ("INV-03", "4.7", False, True), ("INV-04", "5.1", False, False)]
LATEST = "5.1"
for name, fw, default_pw, cloud in inv:
    issues = []
    if default_pw: issues.append("default-password")
    if fw != LATEST: issues.append(f"old-fw {fw}")
    print(f"{name} cloud={'yes' if cloud else 'no '} {', '.join(issues) or 'ok'}")
print("needs action:", sum(1 for _, fw, d, _ in inv if d or fw != LATEST))
```

Run with `python3 lab_inverters.py`. Verified output:

```text
INV-01 cloud=yes ok
INV-02 cloud=yes default-password
INV-03 cloud=yes old-fw 4.7
INV-04 cloud=no  ok
needs action: 2
```

### 2.2 Reading the lab

INV-02 still uses its default password: anyone who has read the manual could log in. INV-03 runs firmware 4.7 while 5.1 is current, so it may miss security fixes. INV-04 has no cloud link and no issues. Two of four inverters need action. Fixing them is done by the owner and vendor at planned times, not by trainees experimenting.

### 2.3 Separating the network

IEC 62443 describes zones — groups of devices with similar needs — joined by conduits, controlled connections. At Elmstead the control zone holds SC-1, inverters and the battery management system; cameras sit in their own zone; the office network is separate again; a DMZ holds the server that shares data outward. Firewalls between zones allow only the connections that are needed.

### 2.4 Exposure and remote access

Devices reachable directly from the internet are a common weakness; MITRE ATT&CK for ICS calls this T0883 Internet Accessible Device. Remote access for vendors should go through one gateway with multi-factor authentication, enabled only when needed — recommendations echoed in CISA advisory AA21-042A after a 2021 water treatment facility compromise.

### 2.5 Cloud portals

Vendor clouds are convenient for monitoring, but a portal that can also send commands is effectively remote access. Ask whether it can control equipment, who has accounts, and whether multi-factor authentication is on.

### Worked example (synthetic Elmstead)

Jonah shows the lab output to the site engineer. She books the inverter vendor for next week to change INV-02's password and update INV-03, and notes that the monitoring portal can send charge commands — a finding for Chapter 3.

> **Synthetic case — Elmstead.** Devices, versions and settings are invented.

### Errors and limits

A list made from records may miss devices; walk-downs and network records complete it. Never scan a live site to build an inventory unless the owner has authorised and planned it.

### Exercises

- **EX014 — Why inventory.** Explain in one sentence why inventory comes before other controls. *Rubric:* 3 = every control depends on knowing devices; unknown devices unprotected; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Inventory fields.** Name five fields for an Elmstead device record. *Rubric:* 3 = five relevant fields; 2 = four; 1 = two; 0 = none.
- **EX016 — Default password risk.** Why is INV-02's default password dangerous? *Rubric:* 3 = published in manuals; anyone with reach logs in; 2 = partial; 1 = "weak"; 0 = none.
- **EX017 — Old firmware.** What does "old-fw 4.7" suggest about INV-03? *Rubric:* 3 = may lack security fixes in 5.1; check advisories; plan update; 2 = partial; 1 = slower; 0 = none.
- **EX018 — Changing the lab.** If INV-04's firmware were "4.9", what would the lab print for it and the total? *Rubric:* 3 = "INV-04 cloud=no  old-fw 4.9" and "needs action: 3"; 2 = one; 1 = ok; 0 = none.
- **EX019 — Who fixes it.** Who changes INV-02's password, and when? *Rubric:* 3 = owner/vendor at a planned time; 2 = owner only; 1 = Jonah now; 0 = none.
- **EX020 — Zones.** Name the four zones proposed for Elmstead. *Rubric:* 3 = control, cameras, office, DMZ; 2 = three; 1 = one; 0 = none.
- **EX021 — Conduit meaning.** What is a conduit in IEC 62443 terms? *Rubric:* 3 = controlled communication path between zones; 2 = "connection"; 1 = cable duct; 0 = none.
- **EX022 — Camera placement.** Why should cameras not share the control zone? *Rubric:* 3 = cameras often weak/internet-linked; compromise would reach controllers; 2 = partial; 1 = bandwidth; 0 = none.
- **EX023 — Internet-facing device.** Which ATT&CK for ICS technique describes a controller reachable from the internet? *Rubric:* 3 = T0883 Internet Accessible Device; 2 = name only; 1 = wrong; 0 = none.
- **EX024 — Vendor access pattern.** Describe a safe vendor remote access pattern in two sentences. *Rubric:* 3 = one gateway, MFA, named accounts, enabled per need, logged; 2 = three elements; 1 = one; 0 = none.
- **EX025 — Portal question.** What three questions should Jonah ask about the vendor monitoring portal? *Rubric:* 3 = can it control, who has accounts, is MFA on; 2 = two; 1 = one; 0 = none.
- **EX026 — No scanning.** Why does Jonah not scan Elmstead's network himself to complete the list? *Rubric:* 3 = not authorised; scans can disrupt devices; use records/walk-downs; 2 = one; 1 = fine to scan; 0 = none.

### Synthesis

Know every device, fix defaults and old firmware through planned work, separate zones, and keep remote access narrow.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Recognising and reporting problems

### Learning outcomes

You will (1) describe normal behaviour at Elmstead; (2) spot a command that does not fit the schedule; (3) describe what you saw using ATT&CK for ICS names; and (4) write a short, factual report.

### 3.1 Normal first

The site controller follows a daily schedule: discharge in the morning peak, charge at midday when solar output is high, discharge again in the evening. Commands come from SC-1. Logins happen during planned work. Writing this down is what lets anyone recognise abnormal.

```python
"""Lab 3: compare synthetic battery charge commands with the agreed daily schedule."""
schedule = {"06": "discharge", "12": "charge", "18": "discharge"}
commands = [("06", "discharge", "site-controller"), ("12", "charge", "site-controller"),
            ("14", "discharge", "remote-portal"), ("18", "discharge", "site-controller")]
for hour, cmd, src in commands:
    ok = schedule.get(hour) == cmd and src == "site-controller"
    print(f"{hour}:00 {cmd:9} from {src:15} {'expected' if ok else 'UNEXPECTED - report'}")
```

Run with `python3 lab_soc.py`. Verified output:

```text
06:00 discharge from site-controller expected
12:00 charge    from site-controller expected
14:00 discharge from remote-portal   UNEXPECTED - report
18:00 discharge from site-controller expected
```

### 3.2 Reading the lab

Three commands match the schedule and come from SC-1. At 14:00 a discharge command arrived from the vendor's remote portal: wrong time and wrong source. It may be a vendor test, a mistake or misuse of stolen credentials; you cannot tell from this line alone, and you do not need to. You report it.

### 3.3 Naming what you saw

MITRE ATT&CK for ICS gives shared names: T0836 Modify Parameter for changed settings, T0886 Remote Services for misuse of remote access routes, T0831 Manipulation of Control for unauthorised commands to the process. Use them to describe observations, not to accuse.

### 3.4 Other warning signs

Battery temperatures rising without load; inverter settings changed with no ticket; new devices on the network; screens disagreeing with local meters; accounts logging in at odd hours; alarms silenced.

### 3.5 Reporting

Tell the site engineer or the person on call immediately. State what, where, when, the current state and what you have done. Keep evidence: screenshots, log lines, times. Do not change settings, reboot devices or contact the vendor yourself unless asked.

### 3.6 Safety comes first

If a battery is overheating, follow the site's fire and safety procedure first; security questions wait.

### Worked example (synthetic Elmstead)

Jonah reports: "14:00 today, BESS received a discharge command from the vendor remote portal, outside schedule (schedule says charge 12:00–18:00). Battery currently discharging. I have not changed anything. Log export saved." The engineer calls the vendor, who has no record of a session; the portal account is disabled and its password reset with MFA enforced.

> **Synthetic case — Elmstead.** The command and response are invented.

### Errors and limits

Most unexpected events are mistakes or faults; still report them. Logs from clouds may arrive late or with different time zones.

### Exercises

- **EX027 — Describing normal.** Describe Elmstead's normal daily battery pattern. *Rubric:* 3 = discharge morning, charge midday, discharge evening, from SC-1; 2 = partial; 1 = vague; 0 = none.
- **EX028 — Two wrongs.** What two things make the 14:00 command unexpected? *Rubric:* 3 = wrong time vs schedule and wrong source (portal); 2 = one; 1 = vague; 0 = none.
- **EX029 — Possible explanations.** Give three possible explanations for the 14:00 command. *Rubric:* 3 = vendor test, mistake, stolen credentials; 2 = two; 1 = one; 0 = none.
- **EX030 — Lab variation.** If the 14:00 line came from "site-controller" with "charge", what would the lab print? *Rubric:* 3 = UNEXPECTED line with reason that hour 14 has no schedule entry; 2 = UNEXPECTED only; 1 = expected; 0 = none.
- **EX031 — Technique for commands.** Which ATT&CK for ICS technique fits an unauthorised discharge command? *Rubric:* 3 = T0831 Manipulation of Control; 2 = name only; 1 = wrong; 0 = none.
- **EX032 — Technique for the route.** Which technique fits misuse of the vendor portal as a way in? *Rubric:* 3 = T0886 Remote Services; 2 = name only; 1 = wrong; 0 = none.
- **EX033 — Five warning signs.** List five warning signs at a battery site. *Rubric:* 3 = five plausible signs; 2 = four; 1 = two; 0 = none.
- **EX034 — Report facts.** Which facts must Jonah's report contain? *Rubric:* 3 = what, where, when, current state, actions taken (evidence); 2 = four; 1 = two; 0 = none.
- **EX035 — Hands off.** Why does Jonah not reboot SC-1 after spotting the command? *Rubric:* 3 = could disturb process/safety and destroy evidence; decision belongs to engineer; 2 = one; 1 = should reboot; 0 = none.
- **EX036 — Overheating first.** A battery rack temperature alarm appears while Jonah is writing his report. What comes first? *Rubric:* 3 = site fire/safety procedure, alert on-call; report later; 2 = alert only; 1 = finish report; 0 = none.
- **EX037 — Vendor follow-up.** What did disabling the portal account and enforcing MFA achieve? *Rubric:* 3 = stopped further use of possibly stolen credentials; future logins need second factor; 2 = partial; 1 = nothing; 0 = none.
- **EX038 — Time zones.** Why should Jonah note the time zone of cloud log entries? *Rubric:* 3 = cloud may log UTC; mismatched times confuse sequence; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Write down normal, notice what does not fit, describe it plainly with shared names, and report it without touching anything.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Safe habits, response basics and next steps

### Learning outcomes

You will (1) practise the everyday habits that protect an OT site; (2) outline the first steps of an incident response; (3) explain the safety and legal limits on security work; and (4) plan your next course.

### 4.1 Everyday habits

Use only site-issued USB drives, scanned before use. Never plug unknown devices into site equipment. Lock screens. Keep passwords out of sight and out of chat. Report lost badges and laptops quickly. Do not install software on site computers. These habits block the commonest ways malware and intruders get in.

### 4.2 Responding to an incident

NIST SP 800-82r3 stresses planning response with operations. At Elmstead the steps are: make people and equipment safe using site procedures; call the on-call engineer; record what you see; preserve evidence; let the engineer and incident lead decide containment, such as disconnecting the vendor portal or putting the battery into a safe idle state; restore from verified backups; learn and improve.

### 4.3 Updates and devices

Vendors release firmware fixes; the owner applies them at planned times after checking compatibility. For new devices, ask suppliers questions drawn from ETSI EN 303 645 and NIST IR 8259: unique passwords, a vulnerability disclosure policy, an update period, encrypted communication.

### 4.4 Limits

Never test, scan or log into systems you are not authorised to use. Never bypass safety systems such as fire detection or battery protection. Never share exploit code or attack instructions. Learning happens on simulators and lab equipment.

### 4.5 Where next

The next course in this curriculum covers critical infrastructure and sector security. Longer courses in this area go deeper into networks, protocols, monitoring and design. Keep a record of exercises completed.

### Worked example (synthetic Elmstead)

During a drill, Jonah finds a camera showing an unfamiliar login screen. He follows the card on the control room wall: tells the on-call engineer, photographs the screen, notes the time, touches nothing. The engineer isolates the camera zone at its firewall; the control zone keeps running. In the debrief Jonah suggests adding the camera vendor's support number to the card.

> **Synthetic case — Elmstead.** The drill is invented.

### Errors and limits

These habits reduce risk but cannot remove it. Procedures differ by site; follow local rules.

### Exercises

- **EX039 — Habit list.** List four everyday habits that protect Elmstead. *Rubric:* 3 = four correct habits; 2 = three; 1 = one; 0 = none.
- **EX040 — Found drive.** A USB drive is left on SC-1's desk. What do you do? *Rubric:* 3 = do not plug in; hand to engineer/security; note where found; 2 = hand in; 1 = check it; 0 = plug in.
- **EX041 — Response order.** Put in order: preserve evidence; make safe; restore; call on-call; learn. *Rubric:* 3 = make safe, call, preserve, restore, learn; 2 = mostly; 1 = random; 0 = none.
- **EX042 — Containment choice.** Name one containment action the engineer might take at Elmstead. *Rubric:* 3 = disconnect portal/isolate zone/battery safe idle with reason; 2 = action only; 1 = delete logs; 0 = none.
- **EX043 — Supplier questions.** Write two questions for a new battery monitor supplier. *Rubric:* 3 = two baseline-based questions (unique passwords, disclosure, updates, encryption); 2 = one; 1 = price; 0 = none.
- **EX044 — Firmware timing.** Why is firmware applied at planned times rather than immediately? *Rubric:* 3 = needs compatibility check and safe stop; disruption risk; 2 = partial; 1 = no reason; 0 = none.
- **EX045 — Practice environment.** Where should Jonah practise using industrial protocols? *Rubric:* 3 = simulator/lab equipment, not live site; 2 = partial; 1 = live site at night; 0 = none.
- **EX046 — Safety bypass.** A colleague suggests disabling battery protection to "test" an alarm. Your answer? *Rubric:* 3 = refuse; safety systems untouched; escalate; 2 = refuse; 1 = agree with care; 0 = agree.
- **EX047 — Drill lesson.** What improvement did Jonah suggest after the drill, and why does it help? *Rubric:* 3 = add vendor support number to card; faster correct call; 2 = item only; 1 = none; 0 = none.
- **EX048 — Isolation effect.** Why could the control zone keep running when the camera zone was isolated? *Rubric:* 3 = zones separated; cameras not needed for control; 2 = partial; 1 = it stopped; 0 = none.
- **EX049 — Sharing exploits.** Why does this course refuse to share exploit code? *Rubric:* 3 = dual-use; could harm real sites; learning goal is defence; 2 = partial; 1 = no reason; 0 = none.
- **EX050 — Next course.** What does the next course in the curriculum cover? *Rubric:* 3 = critical infrastructure and sector security (course 023); 2 = vague; 1 = wrong; 0 = none.

### Synthesis

Good habits, a practised response, respect for safety and legal limits, and continued study protect OT sites.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Elmstead Solar and Battery Site, Jonah Park and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Operational technology is the hardware and software that monitors or controls physical devices and processes, such as inverters, pumps or production lines.

**EX002.** An IoT device senses or acts on the physical world — a camera, meter or sensor — and is usually small, single-purpose and connected to a network or cloud, whereas a laptop is a general-purpose computer for people.

**EX003.** A hospital infusion pump: software calculates and controls the dose delivered into a patient's vein, so a computing error becomes a physical effect.

**EX004.** It converts the direct current produced by the solar panels into alternating current suitable for the grid.

**EX005.** The temperature of the battery cells and their voltages.

**EX006.** Site controller SC-1, which follows the daily schedule and instructions from the grid operator.

**EX007.** Safety comes first, because an overheating battery can catch fire and endanger staff and neighbours.

**EX008.** It could discharge the battery at the wrong time, stressing cells, leaving no stored energy when the grid operator needs it, and pushing unexpected power into the grid.

**EX009.** That huge numbers of cameras, routers and similar devices could be taken over automatically by trying default usernames and passwords, then used together for attacks.

**EX010.** (a) IEC 62443; (b) ETSI EN 303 645; (c) MITRE ATT&CK for ICS.

**EX011.** CISA, the U.S. Cybersecurity and Infrastructure Security Agency, publishes them, often together with the product vendors.

**EX012.** Inverters INV-01 to INV-04, the BESS with its battery management system, site controller SC-1, the grid operator connection, and the cameras.

**EX013.** No. Logging into site equipment needs the owner's authorisation and a defined job; a course gives knowledge, not permission.

**EX014.** Every later control — patching, segmentation, monitoring, response — depends on knowing which devices exist, so anything missing from the inventory stays unprotected.

**EX015.** Device name, function, owner, firmware version and network address (plus location and cloud connection).

**EX016.** Default passwords are printed in public manuals, so anyone who can reach INV-02 over the network or portal could log in and change its settings.

**EX017.** INV-03 may be missing security fixes included in 5.1; check advisories for 4.7 and plan an update with the vendor.

**EX018.** `INV-04 cloud=no  old-fw 4.9` and `needs action: 3`.

**EX019.** The site owner's engineer, with the inverter vendor, changes it during a planned visit — not a trainee and not ad hoc.

**EX020.** The control zone (SC-1, inverters, battery management), the camera zone, the office zone and the DMZ.

**EX021.** A conduit is the controlled communication path that joins two zones, with defined rules about what may cross it.

**EX022.** Cameras are often weakly protected and linked to the internet; if one were compromised in the control zone, the attacker could reach SC-1 and the inverters directly.

**EX023.** T0883 Internet Accessible Device.

**EX024.** Vendors connect only through one site-owned gateway, using named accounts with multi-factor authentication. Accounts are enabled for each agreed job, sessions are logged, and access is switched off afterwards.

**EX025.** Can the portal send commands to equipment or only display data? Who holds accounts on it? Is multi-factor authentication required for every account?

**EX026.** He has no authorisation to do so, and scanning can upset fragile devices; records, network team data and walk-downs build the list safely.

**EX027.** SC-1 discharges the battery in the morning peak, charges it at midday when solar output is high, and discharges again in the evening, with every command coming from SC-1.

**EX028.** It came at 14:00, when the schedule says the battery should be charging, and it came from the vendor's remote portal instead of SC-1.

**EX029.** An unannounced vendor test; an operator or vendor mistake in the portal; or someone using stolen portal credentials.

**EX030.** `14:00 charge    from site-controller UNEXPECTED - report` — the schedule has no entry for hour 14, so `schedule.get("14")` is `None` and the check fails even though the source is SC-1.

**EX031.** T0831 Manipulation of Control.

**EX032.** T0886 Remote Services.

**EX033.** Rising battery temperatures with no load; inverter settings changed without a ticket; an unknown device on the network; screens disagreeing with local meters; silenced alarms.

**EX034.** What he saw (a discharge command from the portal), where (the BESS), when (14:00), what is happening now (battery discharging), and what he has done (nothing changed, log saved).

**EX035.** Rebooting the controller could interrupt the battery and grid schedule unsafely and would wipe information about what happened; the engineer decides any action.

**EX036.** Follow the site's fire and safety procedure and alert the on-call engineer at once; the security report can be finished afterwards.

**EX037.** It stopped anyone holding the old password from sending further commands, and made sure any future portal login requires a second factor as well as the password.

**EX038.** Cloud services often record times in UTC while the site uses local time, so without the zone the sequence of events could be misread by hours.

**EX039.** Use only scanned, site-issued USB drives; lock screens when away; keep passwords out of sight and out of chat; report lost badges and laptops quickly.

**EX040.** Leave it unplugged, note where and when it was found, and give it to the engineer or security contact.

**EX041.** Make safe; call the on-call engineer; preserve evidence; restore from verified backups; learn and improve.

**EX042.** Disconnect the vendor portal so no remote commands can reach SC-1, while the site keeps running on its local schedule.

**EX043.** "Does each unit have a unique password or force one at first use?" and "For how many years will you provide security updates?"

**EX044.** An update must be checked for compatibility with SC-1 and applied while the equipment can safely stop; applying it mid-operation could interrupt power flows.

**EX045.** On a protocol simulator or training equipment in a lab, never on Elmstead's live devices.

**EX046.** Refuse: battery protection is a safety system that is never disabled for testing; report the suggestion to the engineer.

**EX047.** Adding the camera vendor's support number to the wall card, so the on-call engineer can reach the right expert immediately instead of searching for it.

**EX048.** The cameras sit in a separate zone joined by a firewall, and SC-1, the inverters and the battery management system do not depend on them to operate.

**EX049.** Exploit code is dual-use: it could be used against real energy sites and endanger people, while the course's aim is to protect systems, which needs no attack tools.

**EX050.** Course 023: critical infrastructure and sector security.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- CISA. Cybersecurity advisories index (ICS advisories). <https://www.cisa.gov/news-events/cybersecurity-advisories>
- Antonakakis, M., et al. (2017). Understanding the Mirai Botnet. 26th USENIX Security Symposium. <https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- ISA/IEC 62443 series of standards (overview; zones and conduits from 62443-3-2, component requirements in 62443-4-2). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS: T0831 Manipulation of Control, T0836 Modify Parameter, T0883 Internet Accessible Device, T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
