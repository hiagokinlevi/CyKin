# Information Security: Technologist Course

- Language: English (`en`); course 071, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students learning to configure, check and maintain information security controls for a multi-site leisure charity.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs check synthetic workstations against a four-item baseline, review a synthetic firewall rule list for broad, shadowed and unused rules and parse a synthetic authentication log to rank sources of failed logins. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technologist student from operating systems, networks, scripting and logs through hardening, patching and scanning, then accounts, authentication, secrets, firewalls, wireless, endpoints, email, backups, encryption and physical security, to monitoring, incidents, suppliers, procedures, automation, handover, a placement and an applied project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Jamal Haddad** | Technologist student | Invented |
| **Ms. Fiona Grant** | Tutor | Invented |
| **Northgate College of Technology** | Fictional college | Invented |
| **Riverbend Leisure Trust** | Fictional leisure charity, nine centres, about 350 staff and 210 workstations | Invented |

### Core sources

ISO/IEC 27000:2026; ISO/IEC 27001:2022; ISO/IEC 27002:2022; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Starting at Northgate

### Learning outcomes

You will (1) describe the technologist role in information security; (2) meet the running case; (3) plan practical learning over three years.

### 1.1 The student and the role

Jamal Haddad begins a three-year technologist programme in information security at the fictional Northgate College of Technology. His tutor is Ms. Fiona Grant, who worked for ten years as a systems administrator before teaching. She explains that technologists are the people who configure, check and maintain security controls every day: they set up accounts, apply updates, review logs and respond to alerts. The programme is practical, with laboratory work every week and a placement in the final year. Jamal enjoys practical problems.

### 1.2 The case organisation

Jamal's placement partner is the fictional Riverbend Leisure Trust, a charity running nine leisure centres with swimming pools, gyms and cafés. It employs about 350 staff and uses around 210 workstations, a membership and booking system, card payment tills and closed-circuit cameras. Members' personal details, payment data and health questionnaires for gym inductions all need protection. Ms. Grant notes that leisure organisations are often targeted because they hold payment data but have small IT teams. The IT team consists of an IT manager and one technician who travels between centres.

### 1.3 How the programme runs

The first year covers operating systems, networks, scripting, logs and core security concepts, ending with hardening, patching and vulnerability scanning. The second year covers accounts, authentication, secrets, firewalls, wireless, endpoints, email, backups, encryption and physical security. The third year covers monitoring, incident handling, suppliers, procedures, awareness, automation, documentation, the placement and an applied project. Jamal notes that each topic connects to something Riverbend's two-person IT team does every week. He copies the module list into the front of his notebook and marks each module with the Riverbend task he expects it to help with, so he can check later whether the link held.

### 1.4 Learning habits

Ms. Grant asks students to keep a laboratory notebook recording every command they run, what it did and what they learned. She explains that technologists must be able to repeat work exactly and explain it to others, especially after an incident. Jamal also sets up a small home laboratory using virtual machines, so he can practise without touching any real system. He notes that practising safely in a laboratory is the first professional habit the course teaches. Ms. Grant checks the notebooks every fortnight.

### Worked example

Jamal starts the programme, meets Riverbend's nine centres and two-person IT team, maps the three years and starts a notebook and home laboratory.

> **Synthetic case.** Northgate, Riverbend and all people are synthetic.

### Errors and limits

Practising on real systems without permission is unsafe and may be illegal.

### Exercises

- **EX001 — Technologist work.** What do technologists do daily? *Rubric:* 3 = configure, check and maintain controls;; 2 = correct;; 1 = none;; 0 = none.
- **EX002 — Riverbend size.** How many staff does Riverbend employ? *Rubric:* 3 = about 350;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX003 — Notebook purpose.** Why keep a laboratory notebook? *Rubric:* 3 = to repeat and explain work;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Information at a leisure trust

### Learning outcomes

You will (1) identify information a leisure trust holds; (2) rate its sensitivity; (3) trace where it is stored and who uses it.

### 2.1 What Riverbend holds

Jamal lists Riverbend's information: member names, addresses and contact details; payment card data processed at tills and online; direct debit bank details; gym health questionnaires; staff records and rotas; children's swimming lesson registers; and camera footage. Ms. Grant asks him to note who uses each type. Receptionists use member details, instructors use health questionnaires and finance staff use bank details. He learns that knowing who needs information is the starting point for deciding who should access it. He records each type in a table with its users.

### 2.2 Sensitivity

Jamal rates sensitivity using three questions from the security objectives: what harm if disclosed, altered or unavailable? Health questionnaires and children's registers are highly sensitive if disclosed. Bank details are sensitive to alteration, because changed details could divert payments. The booking system matters most for availability, since centres cannot admit members without it. FIPS 199 describes this approach of rating confidentiality, integrity and availability impact separately, and Jamal finds it useful for small organisations too. He adds a column to his table showing the most important objective for each type.

### 2.3 Where it lives

Jamal traces storage. Member data live in a cloud-hosted booking system. Health questionnaires are on paper in each gym office, then scanned to a shared drive. Swimming registers are printed daily. Camera footage is stored on recorders in each centre. He finds scanned questionnaires in a folder all staff can open. He reports this to Riverbend's IT manager, who restricts it to instructors and managers the same day. He adds a storage column to his table, noting for each type whether it is held in the cloud, on a shared drive, on paper or on a local device in a centre.

### 2.4 Paper and people

Not all information is digital. Printed registers left at poolside can be read by anyone passing. Jamal suggests clipboards with covers and collecting registers at the end of each session for secure disposal. Ms. Grant explains that information security covers paper and conversations too. Reception staff reading a member's details aloud in a queue can disclose information as easily as a hacked database. The centre manager tries the covered clipboards for a month and keeps them. Jamal also suggests that receptionists ask members to check details on a screen rather than reading them aloud, and two centres adopt this practice.

### Worked example

Jamal lists Riverbend's information and users, rates sensitivity by objective, finds an over-shared questionnaire folder and suggests covering printed registers.

> **Synthetic case.** Information types are synthetic.

### Errors and limits

Scanned sensitive forms often end up in folders everyone can open.

### Exercises

- **EX004 — Health users.** Who uses health questionnaires? *Rubric:* 3 = instructors;; 2 = correct;; 1 = other;; 0 = none.
- **EX005 — Bank details risk.** Which objective matters most for bank details? *Rubric:* 3 = integrity;; 2 = correct;; 1 = other;; 0 = none.
- **EX006 — Folder fix.** What happens to the questionnaire folder? *Rubric:* 3 = restricted to instructors and managers;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Operating system administration

### Learning outcomes

You will (1) manage users and permissions on common operating systems; (2) control services and startup items; (3) read system information safely.

### 3.1 Users and groups

In the laboratory, Jamal creates user accounts and groups on both a Windows-style and a Linux virtual machine. He learns that permissions are best assigned to groups, such as reception or finance, rather than to individuals, because people change roles. Ms. Grant shows how a single misconfigured group can give many people access they should not have. At Riverbend, he finds that most staff belong to a group with access to all shared folders. He proposes four groups based on job roles and lists the folders each should reach.

### 3.2 Administrator rights

Jamal learns the difference between standard and administrator accounts. Administrators can install software, change security settings and read all files. He finds that Riverbend's reception computers log in automatically with an administrator account so staff can install printer drivers. Any malware run from these computers would gain full control. He recommends standard accounts with a printer driver package pre-installed, and the IT manager agrees to change one centre as a trial. After a month, the trial centre reports no problems, and the IT manager plans the change for the other eight centres over the following term.

### 3.3 Services

Operating systems run background services, and each running service is a possible entry point. Jamal lists services on a laboratory machine and identifies those not needed, such as remote registry access and file sharing on a computer that shares nothing. He disables them and confirms the machine still works. Ms. Grant explains that reducing running services shrinks the attack surface, a basic hardening principle. He records each disabled service in his notebook with the reason, and later uses the list to build a short service checklist for new Riverbend computers, which the IT manager adopts for every new installation.

### 3.4 Safe investigation

Jamal learns to gather information safely: listing logged-in users, running processes, open network connections and recent log entries without changing anything. He writes these commands in his notebook. Ms. Grant explains that during an incident, careless commands can destroy evidence, so technologists need a standard, read-only set of checks they can run calmly. He tests the checklist on a laboratory machine and confirms that none of the commands changes files, settings or logs. Ms. Grant asks him to add a step recording the date and time of each command, so later readers know exactly when information was collected and in what order.

### Worked example

Jamal manages users by group, finds automatic administrator logins at reception, disables unneeded services and builds a read-only investigation checklist.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Automatic administrator logins give any malware full control.

### Exercises

- **EX007 — Group permissions.** Why assign permissions to groups? *Rubric:* 3 = people change roles;; 2 = correct;; 1 = none;; 0 = none.
- **EX008 — Reception risk.** What risk do reception computers have? *Rubric:* 3 = automatic administrator login;; 2 = correct;; 1 = none;; 0 = none.
- **EX009 — Service reduction.** What does disabling unneeded services do? *Rubric:* 3 = shrinks the attack surface;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Networks in practice

### Learning outcomes

You will (1) map a small organisation's network; (2) identify devices and services; (3) separate networks by purpose.

### 4.1 Mapping

Jamal maps the network of one Riverbend centre with the IT manager's permission. It has a router connecting to the internet, a switch, reception computers, office computers, card tills, camera recorders, a guest wireless network and a staff wireless network. He draws each device and connection. Ms. Grant asks him to label which devices handle payment data, because those need the strongest protection and separation. He checks the drawing against the switch's list of connected devices and finds two devices he had missed: a printer in the manager's office and a small wireless access point installed by the café supplier.

### 4.2 Addresses and services

Jamal records each device's network address and the services it offers. He uses an authorised scan in the laboratory network first to learn the tools, then runs a limited scan at the centre during closed hours with written permission. He finds a camera recorder offering a web interface with a default password. He reports it, and the IT manager changes the password and restricts access. He also confirms that the guest wireless network cannot reach staff computers, by trying to connect from a laptop on the guest network in the laboratory copy of the setup. The test fails as intended, and he records the result.

### 4.3 Separation

At the centre, card tills, staff computers and camera recorders share one network. If a staff computer were infected, malware could reach the tills. Jamal proposes separate network segments: one for tills, one for staff, one for cameras and one for guests, with firewall rules allowing only necessary traffic. Ms. Grant explains that payment card industry standards treat separating card systems from other networks as a way to limit which systems must meet their strictest requirements. The IT manager agrees to start with the tills, because payment data carry the highest risk, and to separate cameras next. Jamal drafts the firewall rules needed for the tills to reach the payment provider and nothing else.

### 4.4 Documentation

Jamal produces a network diagram and device list for the centre, stored in Riverbend's IT documentation. He notes the date and who checked it. Ms. Grant points out that network documentation becomes outdated quickly and should be reviewed whenever devices are added. The IT manager asks Jamal to repeat the mapping for two more centres during his placement. He sets a reminder to review the diagram every six months and whenever a new device is installed. The IT manager says the diagram is the first accurate record of the centre's network he has had, and asks Jamal to use the same format for the other centres.

### Worked example

Jamal maps a centre's network, finds a camera recorder with a default password through an authorised scan, proposes four segments and documents the network.

> **Synthetic case.** Networks are synthetic.

### Errors and limits

Scanning without written permission is unacceptable, even on a friendly network.

### Exercises

- **EX010 — Payment label.** Which devices must be labelled specially? *Rubric:* 3 = those handling payment data;; 2 = correct;; 1 = none;; 0 = none.
- **EX011 — Camera finding.** What did the scan find on the camera recorder? *Rubric:* 3 = a default password;; 2 = correct;; 1 = none;; 0 = none.
- **EX012 — Proposed segments.** Name the four proposed segments. *Rubric:* 3 = tills, staff, cameras, guests;; 2 = all;; 1 = some;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Python scripting basics

### Learning outcomes

You will (1) write simple Python scripts for security tasks; (2) read CSV and text files; (3) produce clear, repeatable output.

### 5.1 First scripts

Jamal learns Python using only the standard library, so scripts run on any machine. His first script reads a list of Riverbend user accounts from a CSV file and counts accounts per group. His second lists accounts that have not logged in for sixty days. Ms. Grant explains that scripting turns slow manual checks into fast, repeatable ones, which is essential for small IT teams responsible for hundreds of devices. He runs both scripts weekly in the laboratory and compares the results with manual counts to confirm they are correct.

### 5.2 Reading files

Jamal learns to read text and CSV files with the csv module and to handle problems: empty lines, missing columns and unexpected values. His script skips bad lines and reports them, so data problems are visible rather than hidden. He tests it with a file containing deliberate errors. He learns that security scripts must fail loudly, because a script that silently ignores half its input gives false reassurance. His test file contains ten deliberate errors, and the script reports all ten with their line numbers, which gives him confidence that it will not hide problems in real data.

### 5.3 Clear output

Jamal formats output for people: a heading, the date, totals and a list of items needing action, sorted by importance. He also writes results to a CSV file for the IT manager's records. Ms. Grant asks him to include the script version and input file name in each report, so anyone can trace a result back to exactly what produced it. The IT manager says the reports are easy to read and asks Jamal to use the same format for every script he writes during the placement. Ms. Grant uses one of his reports as an example in class.

### 5.4 Safe habits

Jamal stores scripts in a version-controlled folder, never writes passwords into them and keeps outputs containing personal data in a restricted folder. He adds comments explaining why each check exists. Ms. Grant notes that scripts often outlive their authors, so clear comments and safe handling of data are part of writing good security tools. He also writes a short README file for each script explaining what it checks, what input it needs and what its output means. Ms. Grant notes that these files make it possible for the IT manager to run the scripts after Jamal leaves.

### Worked example

Jamal writes standard-library scripts that count accounts and flag inactivity, handles bad input loudly, formats traceable output and keeps scripts safe.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Scripts that silently skip bad input give false reassurance.

### Exercises

- **EX013 — Inactivity script.** Which accounts does the second script list? *Rubric:* 3 = no login for sixty days;; 2 = correct;; 1 = none;; 0 = none.
- **EX014 — Bad lines.** How does the script handle bad lines? *Rubric:* 3 = skips and reports them;; 2 = correct;; 1 = ignore;; 0 = none.
- **EX015 — Traceability.** What does each report include for tracing? *Rubric:* 3 = script version and input file name;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Logs and log formats

### Learning outcomes

You will (1) read common log formats; (2) extract fields with patterns; (3) understand time zones and clocks in logs.

### 6.1 Why logs matter

Logs record what systems did: logins, failures, changes and errors. Jamal learns that logs are how technologists find out what happened after a problem. Riverbend's systems produce logs in different formats: the booking system exports CSV, servers write text lines and the firewall uses its own format. Ms. Grant explains that being able to read any format is a core technologist skill. He collects one example line from each format and annotates the fields in his notebook, which helps him recognise each format quickly later. The IT manager confirms that these are the logs he checks most often when something goes wrong at a centre.

### 6.2 Extracting fields

Jamal learns regular expressions with Python's re module to extract fields from text lines, such as the time, username and source address from a login record. He practises on synthetic logs and checks his pattern against unusual lines, such as usernames with dots or addresses in different formats. He learns that a pattern which works on the first hundred lines may fail on the thousandth, so testing with varied data matters. He keeps a test file of unusual lines and runs every new pattern against it before use.

### 6.3 Time and clocks

Log times only help if clocks are correct. Jamal finds that one centre's camera recorder clock is eleven minutes slow, which would confuse any investigation comparing footage with till records. He also learns that some systems log in local time and others in universal time. He recommends synchronising all clocks to a reliable time source and recording time zones explicitly. Ms. Grant notes that mismatched clocks have undermined many investigations. The IT manager configures all recorders and servers to use the same time source, and Jamal checks a week later that every clock matches.

### 6.4 Keeping logs

Jamal learns that logs must be kept long enough to investigate problems, protected from alteration and stored where attackers cannot delete them. Riverbend keeps server logs for only seven days on each server. He recommends forwarding them to a central store kept for ninety days, with access limited to IT staff. He notes that logs containing personal data must also follow retention rules. The IT manager sets up the central store using existing server space. Jamal checks after a week that logs from every server are arriving, and finds one server that was not forwarding because of a typing error in its configuration.

### Worked example

Jamal reads several log formats, extracts fields with tested patterns, finds an eleven-minute camera clock error and recommends central log storage for ninety days.

> **Synthetic case.** Logs are synthetic.

### Errors and limits

Unsynchronised clocks make events from different systems impossible to order.

### Exercises

- **EX016 — Pattern module.** Which module extracts fields? *Rubric:* 3 = re;; 2 = correct;; 1 = other;; 0 = none.
- **EX017 — Clock error.** How slow is the camera recorder clock? *Rubric:* 3 = eleven minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX018 — Log retention.** How long should central logs be kept? *Rubric:* 3 = ninety days;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Security concepts in practice

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to daily tasks; (2) use least privilege and defence in depth; (3) relate controls to risks.

### 7.1 Objectives in daily work

Jamal connects the three security objectives to his daily tasks. Restricting the questionnaire folder protected confidentiality. Checking backups protects integrity and availability. Keeping the booking system patched protects all three. ISO/IEC 27000:2026, the overview of the ISO/IEC 27000 family, describes information security in these terms. Ms. Grant asks him to label each task in his notebook with the objective it serves, which helps him explain why the task matters. After a month, he finds that most of his tasks protect availability, which matches the centres' need to keep admitting members.

### 7.2 Least privilege

Saltzer and Schroeder's 1975 paper describes least privilege: give each user and program only the access needed. Jamal applies it at Riverbend: receptionists need booking access but not finance folders; instructors need questionnaires but not payment data. He notes that least privilege also limits the damage when an account is compromised, because the attacker inherits only that account's limited rights. He reviews the access of five sample accounts against their roles and finds two receptionists who can open finance folders. The IT manager removes the access the same day, and Jamal notes the result in his notebook.

### 7.3 Defence in depth

No single control is perfect, so security uses layers. Jamal lists layers protecting Riverbend's tills: network separation, up-to-date software, restricted accounts, payment terminal encryption and monitoring. If one fails, others still protect. Ms. Grant explains that layered defence is especially important in small organisations, where any single control may be maintained by one busy person. He draws the layers as rings around the tills in his notebook. Ms. Grant asks him which ring would fail first if the IT technician were on holiday for a month, and he identifies software updates, which leads him to suggest an automatic update setting for the tills supplier to confirm.

### 7.4 Controls and risks

Jamal learns that controls exist to reduce specific risks. Before adding a control, he asks what risk it reduces and whether that risk matters. He questions a proposal to block all USB storage devices at reception, finding that staff need them for printing posters. He suggests allowing only encrypted, Riverbend-issued devices instead. Ms. Grant praises him for matching controls to real needs. The IT manager orders encrypted memory sticks for each reception desk, and staff report that the change causes no difficulty. Jamal records the decision with the risk it addresses and the reason the original proposal was changed.

### Worked example

Jamal labels tasks by objective, applies least privilege to roles, lists layered controls for tills and adapts a USB control to real needs.

> **Synthetic case.** Examples are synthetic.

### Errors and limits

Controls that ignore real work needs get bypassed.

### Exercises

- **EX019 — Overview standard.** Which standard gives the family overview? *Rubric:* 3 = ISO/IEC 27000:2026;; 2 = correct;; 1 = other;; 0 = none.
- **EX020 — Compromise limit.** How does least privilege limit compromise? *Rubric:* 3 = attacker inherits limited rights;; 2 = correct;; 1 = none;; 0 = none.
- **EX021 — USB alternative.** What USB alternative does Jamal suggest? *Rubric:* 3 = Riverbend-issued encrypted devices only;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Hardening workstations

### Learning outcomes

You will (1) define a workstation baseline; (2) check workstations against it automatically; (3) prioritise fixes.

### 8.1 The baseline

Jamal and the IT manager agree a four-item baseline for Riverbend workstations: the local firewall on, disk encryption enabled, a screen lock after a few minutes and automatic updates on. Each item addresses a clear risk: network attacks, theft of a laptop, unattended screens at reception and unpatched software. Ms. Grant advises starting with a short baseline that can be checked reliably, then adding items later. He writes each item as a check that a script can perform automatically, with a clear pass or fail result and the setting it reads.

### 8.2 The workstation lab

The lab checks 210 synthetic workstations. The firewall is on for 201, 95.7 percent; disk encryption for 164, 78.1 percent; screen lock for 187, 89.0 percent; and automatic updates for 196, 93.3 percent. Only 129 workstations, 61.4 percent, meet all four items. Jamal notes that disk encryption is the weakest item and that the combined figure shows almost two in five workstations fail at least one check. He presents the results by item and combined in a short table, and the IT manager says the combined figure is much lower than he expected. They agree that encryption should be the first focus, because it has the lowest pass rate and protects against theft.

### Lab — Checking synthetic workstation settings against a four-item baseline

```python
"""Check synthetic workstation settings against a four-item baseline (stdlib only)."""
import random
random.seed(44)
items = ["firewall_on", "disk_encrypted", "screen_lock", "auto_updates"]
fail_p = {"firewall_on": 0.03, "disk_encrypted": 0.12, "screen_lock": 0.09, "auto_updates": 0.05}
ws = [{k: random.random() >= fail_p[k] for k in items} for _ in range(210)]
for k in items:
    ok = sum(w[k] for w in ws)
    print(f"{k}: {ok}/{len(ws)} ({ok/len(ws):.1%})")
allok = sum(all(w.values()) for w in ws)
print(f"all four: {allok}/{len(ws)} ({allok/len(ws):.1%})")
```

Run with `python3 lab_workstations.py`. Verified output:

```text
firewall_on: 201/210 (95.7%)
disk_encrypted: 164/210 (78.1%)
screen_lock: 187/210 (89.0%)
auto_updates: 196/210 (93.3%)
all four: 129/210 (61.4%)
```

### 8.3 Prioritising

Jamal sorts failures by risk. Laptops without encryption come first, because they leave buildings and can be stolen. Reception computers without screen lock come next, because members pass them constantly. Desktop computers in locked offices without encryption come later. He discusses the order with the IT manager, who agrees and schedules encryption for laptops in the first week. He creates a simple task list with the failing workstations grouped by centre and priority, so the technician can fix several machines at each visit rather than travelling repeatedly between centres.

### 8.4 Repeating the check

Jamal schedules the check to run monthly and report results by centre. After two months, the share meeting all four items rises substantially, with remaining failures mostly old desktops due for replacement. He records these as exceptions with replacement dates. Ms. Grant notes that repeated checks turn a baseline from a document into a working control. He adds the monthly results to a chart that the IT manager shows at the quarterly management meeting. Ms. Grant asks him to record the exceptions with the reason and replacement date, so the baseline remains honest about what has not yet been fixed.

### Worked example

Jamal defines a four-item baseline, finds 129 of 210 synthetic workstations (61.4 percent) meet all four, prioritises laptop encryption and schedules monthly checks.

> **Synthetic case.** Workstations are synthetic; outputs come from lab_workstations.py.

### Errors and limits

Reporting each item separately can hide how many machines fail at least one.

### Exercises

- **EX022 — Encryption rate.** What share has disk encryption? *Rubric:* 3 = 164 of 210, 78.1 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX023 — Combined rate.** How many meet all four items? *Rubric:* 3 = 129, 61.4 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX024 — First priority.** Which failures come first? *Rubric:* 3 = laptops without encryption;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Patch management

### Learning outcomes

You will (1) run a patch cycle; (2) test updates before wide deployment; (3) handle systems that cannot be patched quickly.

### 9.1 The cycle

Jamal learns the patch cycle: learn about new updates, assess their importance, test them, deploy them and confirm installation. Riverbend's IT manager receives vendor notices and checks a public catalogue of known exploited vulnerabilities. Updates for actively exploited flaws get priority. Ms. Grant explains that a reliable, routine cycle protects better than occasional bursts of effort after news stories. He writes the cycle as a monthly checklist with dates for each stage and the person responsible, so the IT manager and technician know exactly what to do and when. The checklist includes a step for checking the exploited vulnerabilities catalogue every week.

### 9.2 Testing

Updates can break things. Jamal sets up a test group of five workstations, one from each type of role, that receive updates first. After two days without problems, updates go to all workstations. When an update breaks a reception printer driver, the test group catches it before it reaches every centre. He records the problem and the fix in the IT log. Ms. Grant notes that test groups should include the most unusual machines, such as reception computers with printers, because those are most likely to break. Jamal adds two more machines to the group for this reason.

### 9.3 Servers and cloud

Riverbend's booking system is cloud-hosted, so its supplier handles server patching. Jamal checks the contract and finds the supplier commits to patching critical issues within fourteen days. Riverbend still patches its own file server and camera recorders. Camera recorder updates are rare and must be downloaded manually, so he adds a quarterly check to the calendar. He also asks the supplier for a summary of its recent patching performance, which the supplier provides. It shows critical issues patched within the committed time over the past year. Jamal files the summary with the contract and sets a reminder to request it annually.

### 9.4 Systems that lag

Some systems cannot be patched quickly. An old pool chemical controller runs software the supplier no longer updates. Jamal recommends isolating it on its own network segment, blocking internet access and asking the supplier about replacement. Ms. Grant notes that isolation reduces risk when patching is impossible, but should be recorded as a temporary exception with a review date. The supplier offers a replacement controller at a reduced price, and the centre manager includes it in next year's budget. Jamal records the exception with its controls and review date in the IT log, and checks that the isolation works by testing from a staff computer.

### Worked example

Jamal follows the patch cycle, uses a five-machine test group that catches a printer problem, checks the cloud supplier's commitment and isolates an unpatchable pool controller.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Deploying untested updates everywhere at once can break every centre.

### Exercises

- **EX025 — Priority updates.** Which updates get priority? *Rubric:* 3 = those for actively exploited flaws;; 2 = correct;; 1 = none;; 0 = none.
- **EX026 — Test group.** How many workstations are in the test group? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX027 — Pool controller.** How is the pool controller protected? *Rubric:* 3 = isolated segment without internet;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Vulnerability scanning

### Learning outcomes

You will (1) run authorised vulnerability scans; (2) interpret scan results; (3) verify fixes.

### 10.1 Authorised scanning

Vulnerability scanners check systems for known weaknesses. Jamal learns that scanning must be authorised in writing, scheduled to avoid busy times and limited to agreed systems. Riverbend's IT manager approves a monthly scan of the head office and one centre, outside opening hours. Ms. Grant reminds students that scanning someone else's system without permission is illegal in many countries. Jamal keeps a copy of the signed approval with the scan results. He runs the first scan with the IT manager watching, so any unexpected effect on the centre's systems can be handled immediately.

### 10.2 Reading results

The scan produces a long list of findings with severity ratings. Jamal learns that scanners produce false positives, reporting a weakness that is not present, and that severity ratings do not account for local context. A finding on an internal printer rated high may matter less than a medium finding on an internet-facing system. He sorts findings by severity and exposure and checks the top items manually. He confirms two false positives by checking the software versions directly and records them so they can be ignored in future scans.

### 10.3 Fixing

Jamal works with the IT manager to fix the top findings: an outdated remote access tool on the file server, a weak encryption setting on an internal website and the camera recorder's old firmware. Each fix is recorded with the date and the person responsible. He learns that clear records help when auditors or insurers ask whether known weaknesses were addressed. The IT manager updates the remote access tool and applies the new encryption setting, while Jamal downloads and installs the camera recorder firmware during a closed period. Each change is tested before the centre reopens.

### 10.4 Verifying

After fixing, Jamal reruns the scan on the affected systems to confirm the findings have gone. One remains, because the remote access tool had two installations. He removes the second and rescans successfully. Ms. Grant notes that verification is essential, because assuming a fix worked without checking is a common source of lingering weaknesses. Jamal adds a rescan step to the monthly checklist, so every fix is confirmed before the finding is closed. He also records the second installation in his notebook as a lesson: inventories of installed software should be checked before assuming a single fix is complete.

### Worked example

Jamal runs authorised monthly scans, sorts findings by severity and exposure, fixes three top findings and verifies by rescanning, catching a second installation.

> **Synthetic case.** Scans are synthetic.

### Errors and limits

Assuming a fix worked without rescanning leaves weaknesses in place.

### Exercises

- **EX028 — Scan approval.** Who approves the scan? *Rubric:* 3 = the IT manager, in writing;; 2 = correct;; 1 = none;; 0 = none.
- **EX029 — False positive.** What is a false positive? *Rubric:* 3 = a reported weakness that is not present;; 2 = correct;; 1 = none;; 0 = none.
- **EX030 — Remaining finding.** Why did one finding remain after fixing? *Rubric:* 3 = a second installation of the tool;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Account administration

### Learning outcomes

You will (1) run joiner, mover and leaver processes; (2) handle shared and service accounts; (3) review accounts regularly.

### 11.1 Joiners

In his second year, Jamal helps Riverbend's IT manager with account administration. Seasonal lifeguards and swimming teachers join in large numbers before summer. Each needs an account for the booking system and staff rota, but nothing else. Jamal creates a template for each role so new accounts receive exactly the right access. Ms. Grant explains that templates prevent the common mistake of copying an existing colleague's account, which carries extra rights the new person does not need. Templates also make setup faster during busy periods.

### 11.2 Movers and leavers

When staff change roles, old access should be removed. Jamal finds a former receptionist, now an instructor, who still has reception access to member payment screens. When staff leave, accounts should be disabled on their last day. Riverbend relies on centre managers emailing IT, which often happens late. Jamal proposes a weekly report from the payroll system listing leavers, which IT checks against active accounts. The IT manager agrees to try it for a term and record how many late removals it finds.

### 11.3 Shared and service accounts

Shared accounts make it impossible to know who did what. Each centre's reception uses one shared login. Jamal proposes individual logins with a quick badge sign-in, so actions are traceable without slowing reception. Service accounts, used by software rather than people, need named owners and strong passwords stored securely. He lists Riverbend's service accounts and finds one used by an old backup tool that no longer runs. He disables it after confirming with the IT manager. The badge sign-in is trialled at one centre first.

### 11.4 Reviews

Jamal runs a quarterly account review: compare active accounts with the staff list, check each account's access against its role template and list accounts unused for sixty days. His first review finds several seasonal staff from last summer still active and two accounts with unexplained finance access. All are fixed within a week. Ms. Grant notes that regular reviews catch what processes miss, and that the second review is usually much cleaner, which is itself evidence of improvement. He records each review's findings and fixes.

### Worked example

Jamal builds role templates for seasonal joiners, finds a mover with old access, proposes a payroll leaver report, replaces shared reception logins and runs a quarterly review.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Copying a colleague's account to create a new one spreads unneeded access.

### Exercises

- **EX031 — Seasonal access.** What access do seasonal staff need? *Rubric:* 3 = booking system and rota only;; 2 = correct;; 1 = none;; 0 = none.
- **EX032 — Leaver report.** What source lists leavers weekly? *Rubric:* 3 = the payroll system;; 2 = correct;; 1 = other;; 0 = none.
- **EX033 — Old service account.** Which service account is disabled? *Rubric:* 3 = one used by an old backup tool;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Multi-factor authentication

### Learning outcomes

You will (1) choose second factors for different users; (2) deploy multi-factor authentication in stages; (3) support users and handle lost devices.

### 12.1 Choosing factors

Jamal compares second factors for Riverbend. App-based codes suit office staff with smartphones. Hardware keys suit the two IT staff, whose accounts are the most powerful and most targeted. Text message codes are weaker but may suit casual staff who do not want apps on personal phones. Ms. Grant explains that the choice balances protection, cost and practicality, and that phishing-resistant methods such as hardware keys give the strongest protection against fake login pages. He summarises the options in a table with cost, strength and ease of use for each group.

### 12.2 Staged rollout

Jamal plans the rollout in stages: IT staff first, then managers, then office staff, then all remaining staff. Each stage has a date, a guide and a support session. He starts with the email system, because compromised email accounts are commonly used to send fraudulent invoices. The IT manager approves the plan. Jamal learns that staging lets the team fix problems with a small group before they affect everyone. He writes a short message for each stage explaining why the change matters, and the IT manager sends it two weeks before the stage begins.

### 12.3 Supporting users

Some staff struggle with setup. Jamal writes a one-page guide with screenshots and runs drop-in sessions at each centre. He finds that older phones cannot install the authenticator app, so he provides text message codes as an alternative for those staff. Support requests peak in the first week and then fall. Ms. Grant notes that good support reduces resistance and stops staff looking for ways around the new control. He records each support request with its cause, and the most common one, a phone clock set incorrectly, is added to the guide.

### 12.4 Lost devices

Phones get lost. Jamal writes a procedure: staff report the loss to IT, IT removes the lost device from the account after confirming identity through a known phone number or in person, and the staff member registers a new device. He sets up backup codes for IT staff, stored securely. He learns that recovery procedures must be as secure as the login itself, because attackers often target recovery rather than the main login. He tests the procedure with a colleague who pretends to have lost a phone.

### Worked example

Jamal chooses factors by user group, stages a rollout starting with email, supports staff with guides and alternatives and writes a secure lost-device procedure.

> **Synthetic case.** The rollout is synthetic.

### Errors and limits

A weak recovery procedure lets attackers bypass multi-factor authentication.

### Exercises

- **EX034 — IT factor.** Which factor suits IT staff? *Rubric:* 3 = hardware keys;; 2 = correct;; 1 = other;; 0 = none.
- **EX035 — First system.** Which system gets multi-factor authentication first? *Rubric:* 3 = email;; 2 = correct;; 1 = other;; 0 = none.
- **EX036 — Old phones.** What alternative suits staff with old phones? *Rubric:* 3 = text message codes;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Passwords and secrets

### Learning outcomes

You will (1) set practical password rules; (2) manage shared secrets with a password manager; (3) remove secrets from scripts and documents.

### 13.1 Password rules

Riverbend's old rules forced password changes every month, leading staff to add a number to the same word each time. Jamal recommends longer passphrases, checks against lists of breached passwords, multi-factor authentication and changes only when compromise is suspected. Ms. Grant explains that rules which ignore human behaviour produce predictable passwords. The IT manager adopts the new rules after Jamal shows examples of the predictable patterns staff had been using. He also suggests that the booking system for members adopt the same breached-password check, which the supplier agrees to enable.

### 13.2 Password managers

IT staff manage many passwords for routers, camera recorders, supplier portals and service accounts. These were kept in a spreadsheet on the file server. Jamal recommends a password manager with individual accounts for each IT staff member, sharing only the entries each needs, and an access log. He moves the entries and deletes the spreadsheet. He learns that password managers make strong, unique passwords practical, because nobody has to remember them. Each IT staff member can see only the entries needed for their work, and the log shows who opened each entry.

### 13.3 Secrets in scripts

Jamal finds a backup script with a service account password written inside it. Anyone who can read the script can use the password. He rewrites the script to read the password from a protected configuration file readable only by the service account, and asks the IT manager to change the exposed password. Ms. Grant notes that secrets in scripts often spread through copies, backups and shared folders. He searches the other scripts on the server for similar passwords and finds two more, which he fixes in the same way.

### 13.4 Secrets in documents

Jamal searches Riverbend's shared drive, with permission, for documents containing the word password. He finds a setup guide for camera recorders listing current passwords and an old handover note with router credentials. He removes the passwords from both documents, replacing them with a reference to the password manager, and has the affected passwords changed. He learns that searching for exposed secrets periodically is a simple, valuable check. He adds the search to his monthly checklist, so new exposures are found quickly rather than lingering for years in shared folders.

### Worked example

Jamal replaces forced monthly changes with passphrases and breach checks, moves IT passwords into a password manager and removes secrets from a script and documents.

> **Synthetic case.** Secrets are synthetic.

### Errors and limits

A password written in a script is exposed to anyone who can read it.

### Exercises

- **EX037 — Old rule effect.** What did monthly forced changes cause? *Rubric:* 3 = adding a number to the same word;; 2 = correct;; 1 = none;; 0 = none.
- **EX038 — Spreadsheet replacement.** What replaces the password spreadsheet? *Rubric:* 3 = a password manager;; 2 = correct;; 1 = other;; 0 = none.
- **EX039 — Document findings.** What did the document search find? *Rubric:* 3 = camera passwords and router credentials;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Firewalls and segmentation

### Learning outcomes

You will (1) review firewall rules systematically; (2) find overly broad, shadowed and unused rules; (3) clean up rules safely.

### 14.1 Why review rules

Firewall rules accumulate over years as suppliers and staff request access. Old rules are rarely removed, because nobody remembers why they exist and everyone fears breaking something. Jamal is asked to review the rule list for Riverbend's head office firewall. Ms. Grant explains three common problems: rules that allow too much, rules that can never take effect because an earlier rule already matches the same traffic, and rules that have not been used for a long time. He exports the rule list with ninety days of hit counts.

### 14.2 The firewall lab

The lab reviews a synthetic list of twelve rules with hit counts for ninety days. Rule 11 allows any traffic from anywhere to anywhere. Because the firewall applies the first matching rule, rule 11 makes the final deny rule, rule 12, unreachable, and it has zero hits. Rule 9 duplicates rule 1 and is shadowed by it. Rules 6, 9, 10 and 12 have zero hits, including rule 6, which allows a supplier remote desktop access to the tills. He presents the findings to the IT manager in a short table listing each rule, its hits and the problem found, if any, with a proposed action for each.

### Lab — Reviewing a synthetic firewall rule list for broad, shadowed and unused rules

```python
"""Review a synthetic firewall rule list for any-any rules, shadowed rules and unused rules (stdlib only)."""
rules = [
 (1, "allow", "staff", "internet", "443", 51234), (2, "allow", "staff", "internet", "80", 20877),
 (3, "allow", "staff", "booking", "443", 9411), (4, "allow", "guest", "internet", "443", 40210),
 (5, "deny", "guest", "staff", "any", 1876), (6, "allow", "supplier", "tills", "3389", 0),
 (7, "allow", "staff", "tills", "443", 2210), (8, "allow", "cctv", "internet", "any", 1530),
 (9, "allow", "staff", "internet", "443", 0), (10, "allow", "mgmt", "switches", "22", 0),
 (11, "allow", "any", "any", "any", 312), (12, "deny", "any", "any", "any", 0),
]
anyany = [r[0] for r in rules if r[2] == "any" and r[3] == "any" and r[4] == "any" and r[1] == "allow"]
def shadowed(rs):
    out = []
    for i, r in enumerate(rs):
        for p in rs[:i]:
            if p[2] in ("any", r[2]) and p[3] in ("any", r[3]) and p[4] in ("any", r[4]):
                out.append((r[0], p[0])); break
    return out
unused = [r[0] for r in rules if r[5] == 0]
print(f"rules {len(rules)}; allow any-any: {anyany}")
print(f"shadowed (rule, by): {shadowed(rules)}")
print(f"zero hits in 90 days: {unused}")
print(f"after removing rule 11, shadowed: {shadowed([r for r in rules if r[0] != 11])}")
```

Run with `python3 lab_firewall.py`. Verified output:

```text
rules 12; allow any-any: [11]
shadowed (rule, by): [(9, 1), (12, 11)]
zero hits in 90 days: [6, 9, 10, 12]
after removing rule 11, shadowed: [(9, 1)]
```

### 14.3 Interpreting

The any-to-any rule is the most serious finding, because it means the firewall effectively allows anything not matched earlier, and the deny rule meant to block everything else never applies. Jamal asks the IT manager about it; it was added during a network problem two years ago as a temporary fix. The unused supplier remote desktop rule is also concerning, because remote desktop to tills is a common ransomware entry route. Rule 10, for managing switches, is unused but legitimate. He records each finding's history.

### 14.4 Safe clean-up

Jamal proposes changes: remove rule 11, so the final deny takes effect; remove the duplicate rule 9; remove the supplier rule 6 after confirming with the supplier; and keep rule 10 with a note explaining its purpose. The lab shows that after removing rule 11, only rule 9 remains shadowed. The IT manager makes the changes during a quiet period with a rollback plan, monitors for problems for a week and records each change. The supplier confirms it no longer needs rule 6. After a week without problems, Jamal schedules a review of the rule list every six months.

### Worked example

Jamal reviews twelve synthetic rules, finds an any-to-any rule making the final deny unreachable, a duplicate and an unused supplier remote desktop rule, and cleans up safely.

> **Synthetic case.** Rules are synthetic; outputs come from lab_firewall.py.

### Errors and limits

An allow-any rule above the final deny makes the deny useless.

### Exercises

- **EX040 — Broad rule.** Which rule allows any traffic? *Rubric:* 3 = rule 11;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX041 — Unreachable deny.** Why does rule 12 have zero hits? *Rubric:* 3 = rule 11 matches first;; 2 = correct;; 1 = none;; 0 = none.
- **EX042 — Supplier rule.** What does unused rule 6 allow? *Rubric:* 3 = supplier remote desktop to tills;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Wireless security

### Learning outcomes

You will (1) configure secure wireless networks; (2) separate guest and staff wireless; (3) find unauthorised access points.

### 15.1 Staff wireless

Riverbend's staff wireless uses a single password shared by everyone and unchanged for years, known to many former staff. Jamal recommends individual sign-in for staff wireless using their normal accounts, so leavers lose wireless access when their account is disabled. Where devices cannot support this, such as some tablets used for class registers, he recommends a separate network with a strong password changed every term. The IT manager configures individual sign-in at one centre as a trial and extends it to all centres after a month. The register tablets move to their own network with a new password.

### 15.2 Guest wireless

Members use guest wireless in cafés and lounges. Jamal checks that the guest network is separated from staff and till networks and that guests cannot see each other's devices. He also checks the guest welcome page, which asks for an email address. He suggests explaining how the address is used and offering access without it. Ms. Grant notes that guest networks must be isolated, because Riverbend cannot control what devices guests bring. The marketing manager agrees to update the welcome page wording within a month.

### 15.3 Unauthorised access points

Jamal walks through two centres with a laptop listing nearby wireless networks. He finds an access point named like a staff network but not installed by IT. It turns out the café supplier installed it for their card terminal. It connects to the staff network directly. He reports it, and the IT manager arranges for the supplier's terminal to use a proper separated connection. Jamal learns that unauthorised access points often come from suppliers solving their own problems. He adds a wireless check to his visits.

### 15.4 Settings

Jamal checks wireless settings: modern encryption enabled, old protocol versions disabled, management interfaces not reachable from guest networks and firmware updated. One centre's access point still allows an old, weak encryption mode for compatibility with an old printer. He moves the printer to a wired connection and disables the weak mode. Ms. Grant notes that compatibility settings often keep weaknesses alive long after they are needed. He records the settings for each access point in the network documentation, so the IT manager can check them after any change or firmware update.

### Worked example

Jamal replaces a shared staff wireless password with individual sign-in, checks guest isolation, finds a supplier access point bridging to the staff network and removes a weak encryption mode.

> **Synthetic case.** Networks are synthetic.

### Errors and limits

Shared wireless passwords remain known to former staff.

### Exercises

- **EX043 — Shared password problem.** Why is the shared staff wireless password a problem? *Rubric:* 3 = known to former staff;; 2 = correct;; 1 = none;; 0 = none.
- **EX044 — Rogue access point.** Who installed the unauthorised access point? *Rubric:* 3 = the café supplier;; 2 = correct;; 1 = other;; 0 = none.
- **EX045 — Weak mode.** Why was a weak encryption mode enabled? *Rubric:* 3 = for an old printer;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Endpoint protection

### Learning outcomes

You will (1) deploy endpoint protection tools; (2) respond to endpoint alerts; (3) control software installation.

### 16.1 Endpoint tools

Endpoint protection software detects and blocks malware and suspicious behaviour on computers. Riverbend uses one product, but Jamal finds it installed on only most workstations, with several reception computers missing it after a reinstallation. He compares the product's console list with the inventory and installs it on the missing machines. Ms. Grant notes that coverage gaps are common, and that checking coverage against the inventory should be a routine monthly task. He adds a monthly coverage comparison to his checklist and sends the IT manager the list of any missing machines.

### 16.2 Alerts

Jamal learns to review endpoint alerts. Most are low risk: blocked advertising software or suspicious downloads stopped automatically. One alert shows a script trying to run from a downloaded invoice attachment on a finance computer. The tool blocked it. Jamal checks whether anything else happened, finds nothing, and reports the attempt so the IT manager can warn staff. He learns to treat blocked attacks as signs that someone is targeting the organisation. The IT manager sends a short warning to finance staff describing the invoice email.

### 16.3 Software control

Staff sometimes install free tools, some of which carry unwanted software. Jamal recommends that only IT can install software, with a simple request form and a list of approved applications. He also recommends allowing only approved applications to run on till computers, which do one job. Ms. Grant explains that allow-listing is very effective on single-purpose machines, though harder on general office computers. The IT manager approves the request form and the approved list. On the tills, allow-listing is trialled at one centre and then rolled out to all nine without problems reported by staff.

### 16.4 Removable media

Malware can spread through memory sticks. Jamal configures endpoint protection to scan removable media automatically and blocks automatic running of programs from them. Combined with the earlier decision to issue encrypted Riverbend memory sticks, this reduces risk while keeping work possible. He documents the settings so they are applied to new computers. He tests the settings with a harmless test file on a memory stick in the laboratory and confirms that automatic running is blocked and the scan runs. The IT manager approves applying the settings to all Riverbend computers through the device management system, and Jamal checks a sample of computers a week later to confirm the settings arrived.

### Worked example

Jamal fixes endpoint coverage gaps, investigates a blocked invoice script, restricts software installation, allow-lists till applications and scans removable media.

> **Synthetic case.** Alerts are synthetic.

### Errors and limits

Endpoint protection protects only the machines it is installed on.

### Exercises

- **EX046 — Coverage gap.** Where was endpoint protection missing? *Rubric:* 3 = reception computers after reinstallation;; 2 = correct;; 1 = none;; 0 = none.
- **EX047 — Finance alert.** What did the finance alert show? *Rubric:* 3 = a script from an invoice attachment;; 2 = correct;; 1 = none;; 0 = none.
- **EX048 — Allow-listing.** Where is allow-listing most effective? *Rubric:* 3 = single-purpose machines like tills;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Email security

### Learning outcomes

You will (1) configure email filtering and authentication; (2) handle reported phishing; (3) protect against payment fraud.

### 17.1 Filtering

Riverbend's email provider filters spam and malware. Jamal reviews the settings and enables additional protections: warnings on external emails, blocking of risky attachment types and checking links when clicked. He tests the settings with harmless test messages in the laboratory. Ms. Grant explains that filtering catches most attacks, but the remainder reach staff, so other controls are needed as well. He measures the effect over a month and finds that the number of suspicious emails reaching staff falls noticeably. He records the settings in the documentation, so they can be checked after any change made by the email provider.

### 17.2 Domain authentication

Jamal learns how email authentication records let receiving systems check whether a message claiming to come from Riverbend really did. He finds that Riverbend's records are incomplete, so fake messages using its domain may be delivered to members. He works with the IT manager to complete the records, starting in monitoring mode and moving to rejection once legitimate sending services are all listed. He lists every service that sends email for Riverbend, including the booking system and a newsletter service, before moving to rejection. This prevents genuine messages being blocked.

### 17.3 Reported phishing

Jamal sets up a report button so staff can forward suspicious emails easily. He reviews reports each morning, removes confirmed phishing from all mailboxes and thanks reporters. In one week, a receptionist reports a message asking for gift card purchases, apparently from a centre manager. Jamal finds the same message sent to five centres and removes it everywhere. He learns that one report can protect many staff. He records each report, its outcome and how quickly it was handled, and shares a monthly summary with the IT manager.

### 17.4 Payment fraud

Fraudsters often impersonate suppliers to change bank details. Jamal helps finance write a rule: any bank detail change must be confirmed by phone using a number already on file, never one from the email. He also adds a warning in the finance system when bank details change. Ms. Grant notes that process controls are essential against fraud, because a well-crafted fraudulent email may pass every technical filter. The finance manager adds the rule to the finance procedures and briefs her team. Within a month, a fake supplier request is caught by the call-back.

### Worked example

Jamal tightens filtering, completes email authentication records, runs a report button that stops a gift card scam across five centres and adds a bank detail call-back rule.

> **Synthetic case.** Messages are synthetic.

### Errors and limits

Technical filters alone cannot stop well-crafted payment fraud.

### Exercises

- **EX049 — Incomplete records.** What risk did incomplete authentication records create? *Rubric:* 3 = fake messages using Riverbend's domain delivered;; 2 = correct;; 1 = none;; 0 = none.
- **EX050 — Gift card scam.** How many centres received the gift card message? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX051 — Bank change rule.** How must bank detail changes be confirmed? *Rubric:* 3 = by phone using a number on file;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Backups in practice

### Learning outcomes

You will (1) check backup coverage; (2) test restores; (3) protect backups from ransomware.

### 18.1 Coverage

Jamal lists what Riverbend backs up: the file server nightly and the booking system by its cloud supplier. Camera footage and the finance computer's local files are not backed up. He discusses each with the IT manager. Camera footage is kept for thirty days on recorders and is acceptable without backup. Finance local files should move to the file server. Ms. Grant notes that knowing what is not backed up matters as much as knowing what is. He records the decisions in the backup plan.

### 18.2 Restore tests

Jamal tests restores monthly. He restores a sample of files to a separate folder and compares their fingerprints with the originals using Python's hashlib module. In one test, a folder fails to restore because the backup job excluded it after a folder rename. He fixes the job and retests. He learns that backup jobs can report success while silently missing data, so restores are the only proof. He records each test in a log with the files checked, the result and any fix, so the IT manager can show insurers that restores are tested.

### 18.3 Ransomware protection

The file server backups are stored on a device reachable from the network with the same administrator password. Ransomware could encrypt both. Jamal recommends a second copy with a cloud backup service that keeps versions for thirty days and cannot be deleted by Riverbend's normal administrator accounts. The IT manager arranges it. Ms. Grant notes that backups must assume attackers will look for them. He also separates the backup device's administrator password from the main administrator account and stores it in the password manager with restricted access.

### 18.4 Cloud supplier backups

Jamal checks the booking system contract for backup terms. The supplier backs up daily and keeps copies for fourteen days, but Riverbend has never requested a restore. Jamal asks the supplier to demonstrate a restore of a test record. The supplier does so within a day. He records the result and adds a yearly demonstration request to the calendar. He also asks how long a full restore of the booking system would take, and the supplier estimates several hours. The IT manager shares this with centre managers, who agree that paper sign-in sheets would be used meanwhile.

### Worked example

Jamal lists backup coverage and gaps, finds a renamed folder excluded through monthly restore tests, adds an undeletable cloud copy and asks the booking supplier to demonstrate a restore.

> **Synthetic case.** Backups are synthetic.

### Errors and limits

A backup job that reports success may still be missing data.

### Exercises

- **EX052 — Moved files.** What should happen to finance local files? *Rubric:* 3 = move to the file server;; 2 = correct;; 1 = none;; 0 = none.
- **EX053 — Restore failure.** Why did a folder fail to restore? *Rubric:* 3 = excluded after a rename;; 2 = correct;; 1 = none;; 0 = none.
- **EX054 — Supplier retention.** How long does the booking supplier keep backups? *Rubric:* 3 = fourteen days;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Encryption in practice

### Learning outcomes

You will (1) enable encryption for devices and data; (2) manage certificates for websites; (3) handle keys and recovery.

### 19.1 Device encryption

Jamal enables full-disk encryption on Riverbend laptops and checks it on desktops. He stores recovery keys in the device management system, so IT can recover a laptop if its owner forgets a password, but nobody else can read the disk. When a laptop is stolen from a car, the IT manager confirms it was encrypted and disables the user's accounts. No member data are exposed. He records the theft and the confirmation of encryption in the incident log. Ms. Grant uses the case in class as an example of how encryption limits harm.

### 19.2 Data in transit

Jamal checks that the booking website and staff webmail use encrypted connections with current protocol versions. He finds an internal reporting page served without encryption on the staff network. Though internal, it shows member names. He asks the IT manager to add encryption. Ms. Grant notes that internal networks are not automatically safe, especially when guest or supplier devices could reach them. The IT manager installs a certificate on the reporting page within a week, and Jamal confirms that the page now loads only over an encrypted connection.

### 19.3 Certificates

Websites use certificates to prove their identity. Riverbend's public website certificate expired last year, causing browser warnings that frightened members. Jamal lists all certificates with expiry dates and owners and sets up automatic renewal where possible. For certificates that cannot renew automatically, he sets reminders thirty days before expiry. He learns that certificate management is a routine task that causes outages when forgotten. The list contains eleven certificates. Two are due to expire within a month, and the IT manager renews them immediately while the automatic process is set up.

### 19.4 Keys and recovery

Encryption depends on keys. Jamal learns that losing keys can make data unrecoverable, while exposing them makes encryption useless. He checks that backup encryption keys are stored separately from backups and that two people know how to retrieve them. Ms. Grant explains that key management is the hard part of encryption, and that recovery should be tested before it is needed. He tests key retrieval with the IT manager, timing how long it takes to recover a backup encryption key from its separate store and restore a test file with it.

### Worked example

Jamal enables laptop encryption with escrowed recovery keys, adds encryption to an internal page showing member names, sets up certificate renewal and checks key storage.

> **Synthetic case.** Devices are synthetic.

### Errors and limits

Losing encryption keys can make data unrecoverable.

### Exercises

- **EX055 — Stolen laptop.** Why were no data exposed from the stolen laptop? *Rubric:* 3 = it was encrypted;; 2 = correct;; 1 = none;; 0 = none.
- **EX056 — Internal page.** What did the unencrypted internal page show? *Rubric:* 3 = member names;; 2 = correct;; 1 = other;; 0 = none.
- **EX057 — Renewal reminder.** When are manual renewal reminders set? *Rubric:* 3 = thirty days before expiry;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Physical and device security

### Learning outcomes

You will (1) secure equipment rooms and devices; (2) protect tills and cameras physically; (3) dispose of equipment safely.

### 20.1 Equipment rooms

Jamal visits network cupboards at three centres. One is unlocked and used to store cleaning supplies. Another has the key hanging on a hook beside it. He recommends locks with keys held by the centre manager and IT, and removal of other items. Ms. Grant explains that someone with physical access to network equipment can bypass many controls, for example by plugging in their own device. The centre managers agree, and the cleaning supplies are moved. Jamal checks the cupboards again a month later and finds all three locked.

### 20.2 Tills and terminals

Card terminals can be tampered with by criminals who add devices to capture card details. Jamal helps write a simple daily check: reception staff compare each terminal with a photo, check seals and report anything unusual. He also checks that terminals are fixed to counters. Ms. Grant notes that daily checks by the people who use equipment are often the best detection for physical tampering. He prepares the photos and a one-page checklist for each centre. Reception staff complete the check at opening time and initial a sheet.

### 20.3 Cameras

Cameras protect people and property but also record members, including children at pools. Jamal checks that camera recorders are in locked rooms, footage is kept for a defined period and access to footage is limited and logged. He finds that one centre's recorder screen is visible from reception. He recommends moving it. He learns that physical security and privacy often meet in camera systems. The centre manager moves the screen into the office, and Jamal adds footage access logging to the monthly checks for each centre.

### 20.4 Disposal

Old computers and recorders contain data. Jamal finds three old reception computers in a storeroom awaiting disposal. He recommends wiping drives with a recognised method or using a certified disposal company that provides certificates. He records each disposed device in the inventory. Ms. Grant notes that disposal failures have caused many data exposures, because discarded devices often still hold readable data. The IT manager chooses a certified company, which collects the computers and provides a certificate for each drive. Jamal files the certificates with the inventory records.

### Worked example

Jamal secures network cupboards, writes a daily terminal tampering check, limits camera footage access and arranges certified disposal of old computers.

> **Synthetic case.** Sites are synthetic.

### Errors and limits

Discarded devices often still hold readable data.

### Exercises

- **EX058 — Cupboard misuse.** How was one network cupboard misused? *Rubric:* 3 = storing cleaning supplies;; 2 = correct;; 1 = none;; 0 = none.
- **EX059 — Terminal check.** How do staff check terminals daily? *Rubric:* 3 = compare with a photo and check seals;; 2 = correct;; 1 = none;; 0 = none.
- **EX060 — Recorder screen.** What problem did one recorder screen have? *Rubric:* 3 = visible from reception;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Log monitoring

### Learning outcomes

You will (1) parse authentication logs with scripts; (2) separate internal mistakes from external attacks; (3) act on what the logs show.

### 21.1 The question

In his third year, Jamal is asked to look at authentication logs from Riverbend's file transfer server, which the booking supplier uses to send nightly reports. The IT manager has noticed the server running slowly. Jamal decides to count failed logins by source address, because a large number of failures from a few addresses usually means password guessing. Ms. Grant reminds him to check that he is authorised to read the logs and to note his question before looking, so he does not go hunting aimlessly.

### 21.2 The log lab

The lab parses a synthetic log of 3,271 lines with a regular expression and finds 838 failed logins. The top three sources are 203.0.113.45 with 412 failures, 198.51.100.7 with 198 and 203.0.113.88 with 61. All three are external addresses, together responsible for 671 failures, 80.1 percent of the total. The remaining failures come from internal staff addresses and look like ordinary mistyping spread across many accounts. The external failures target names such as root, admin and test. Jamal notes that the addresses belong to ranges reserved for documentation, used here as placeholders for real external addresses, and that a real analysis would check address ownership before drawing conclusions.

### Lab — Parsing a synthetic authentication log and ranking sources of failed logins

```python
"""Parse a synthetic SSH-style authentication log and rank sources of failed logins (stdlib only)."""
import random, re
from collections import Counter
random.seed(77)
lines = []
for _ in range(2600):
    ip = f"10.4.{random.randint(1,3)}.{random.randint(2,60)}"
    ok = random.random() < 0.93
    lines.append(f"sshd: {'Accepted' if ok else 'Failed'} password for staff{random.randint(1,40)} from {ip}")
for ip, n in [("203.0.113.45", 412), ("198.51.100.7", 198), ("203.0.113.88", 61)]:
    for _ in range(n):
        lines.append(f"sshd: Failed password for {random.choice(['root','admin','test','staff3'])} from {ip}")
random.shuffle(lines)
pat = re.compile(r"(Accepted|Failed) password for (\S+) from (\S+)")
fails = Counter(); total_fail = 0
for l in lines:
    m = pat.search(l)
    if m and m.group(1) == "Failed":
        total_fail += 1; fails[m.group(3)] += 1
ext = {ip: n for ip, n in fails.items() if not ip.startswith("10.")}
print(f"lines {len(lines)}; failed logins {total_fail}")
print(f"top sources: {fails.most_common(3)}")
print(f"external sources {len(ext)} with {sum(ext.values())} failures ({sum(ext.values())/total_fail:.1%} of all failures)")
```

Run with `python3 lab_authlog.py`. Verified output:

```text
lines 3271; failed logins 838
top sources: [('203.0.113.45', 412), ('198.51.100.7', 198), ('203.0.113.88', 61)]
external sources 3 with 671 failures (80.1% of all failures)
```

### 21.3 What it means

The results show that the file transfer server accepts password logins from the internet, and automated tools are guessing common account names. Jamal checks whether any external login succeeded and finds none in the log. He reports to the IT manager that the server is exposed more widely than needed: only the booking supplier should connect, from known addresses. Ms. Grant notes that log analysis often reveals configuration problems rather than successful attacks. He records the finding and the check for successful logins in his notebook.

### 21.4 Acting

The IT manager restricts the server to the supplier's addresses at the firewall and switches the supplier's account from password to key-based authentication. Jamal reruns his script on the following week's logs and finds external failures have stopped. The server performance returns to normal. He adds the script to a weekly schedule with an alert if external failures appear again. He learns that monitoring is most useful when it leads to a change and then confirms the change worked. The IT manager thanks him.

### Worked example

Jamal parses 3,271 synthetic log lines, finds 838 failures with 80.1 percent from three external addresses, finds no successful external login, restricts the server and confirms the fix.

> **Synthetic case.** Logs and addresses are synthetic documentation addresses; outputs come from lab_authlog.py.

### Errors and limits

Ranking failures without separating internal and external sources mixes mistyping with attacks.

### Exercises

- **EX061 — Failed count.** How many failed logins does the log contain? *Rubric:* 3 = 838;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX062 — Top source.** Which address has the most failures? *Rubric:* 3 = 203.0.113.45 with 412;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX063 — External share.** What share of failures came from external sources? *Rubric:* 3 = 80.1 percent;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Incident handling

### Learning outcomes

You will (1) follow an incident procedure; (2) preserve evidence; (3) communicate during and after an incident.

### 22.1 The procedure

Riverbend has a short incident procedure written by the IT manager with Jamal's help: report, assess, contain, investigate, recover and review. It is based on the Respond and Recover functions of the NIST Cybersecurity Framework 2.0. Each step names who acts and how to contact them out of hours. Ms. Grant explains that technologists are often first on the scene, so they must know the procedure well enough to follow it calmly under pressure. Jamal keeps a printed copy in his bag during centre visits.

### 22.2 A real incident

A centre manager reports that her email account sent messages she did not write. Jamal follows the procedure. He resets her password, signs out all sessions, checks for forwarding rules and finds one sending copies of her mail to an external address. He removes it and confirms multi-factor authentication is enabled. The account had been one of the last waiting for enrolment. He records every step with times in the incident log. He also checks the sent folder to see which recipients received the messages, so they can be warned.

### 22.3 Evidence

Before removing the forwarding rule, Jamal takes a screenshot and exports the sign-in logs showing a login from an unfamiliar country. He stores them in a restricted folder with the date and his name. Ms. Grant explains that evidence collected carefully helps understand what happened and may be needed by insurers or regulators. Changing things before recording them can destroy the evidence needed to know what the attacker accessed. He records the time zone of each log entry, because the sign-in logs use universal time while the centre manager reported local times.

### 22.4 Communication

The IT manager tells the centre manager what happened and what was done, informs the data protection lead because member emails were forwarded, and warns other staff about the phishing message used. A short review afterwards identifies the cause: delayed enrolment in multi-factor authentication. The remaining enrolments are completed within a week. Jamal learns that clear communication reduces worry and that reviews turn incidents into improvements. The data protection lead reviews which member emails were forwarded and decides, with the IT manager, how to inform the affected members. Jamal adds the incident and its lessons to the monthly report.

### Worked example

Jamal follows the procedure for a compromised mailbox, removes an external forwarding rule after capturing evidence, involves the data protection lead and helps close the enrolment gap.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Changing settings before recording them can destroy evidence.

### Exercises

- **EX064 — Procedure basis.** Which CSF 2.0 functions shape the procedure? *Rubric:* 3 = Respond and Recover;; 2 = correct;; 1 = other;; 0 = none.
- **EX065 — Forwarding rule.** What did Jamal find in the mailbox? *Rubric:* 3 = a rule forwarding mail externally;; 2 = correct;; 1 = none;; 0 = none.
- **EX066 — Root cause.** What caused the incident? *Rubric:* 3 = delayed MFA enrolment;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Supplier and cloud services

### Learning outcomes

You will (1) list suppliers and their access; (2) check supplier security commitments; (3) manage supplier accounts.

### 23.1 Supplier list

Jamal lists Riverbend's suppliers with access to its systems or data: the booking system provider, the payment processor, the email provider, the café supplier, the camera maintenance company and the pool controller supplier. For each, he records what data they hold, how they connect and who manages the relationship. Ms. Grant explains that suppliers extend an organisation's attack surface, so knowing them is as important as knowing internal systems. He stores the list with the contracts and asks each relationship manager to confirm the details are correct and complete.

### 23.2 Security commitments

Jamal reviews contracts for security terms: data protection, incident notification, access control and data return at the end of the contract. The booking provider's contract is strong and refers to an ISO/IEC 27001 certificate covering its hosting service. The camera maintenance company's contract has no security terms. He recommends adding basic terms at renewal. He notes that a certificate is useful evidence only when its scope covers the service Riverbend uses. The IT manager adds the recommendation to the renewal checklist and asks the camera company for its current security practices in writing.

### 23.3 Supplier accounts

Several suppliers have accounts on Riverbend systems. Jamal finds the camera maintenance company has an always-on remote access account with a shared password. He recommends disabling it between visits, enabling it only for scheduled work and using individual accounts with multi-factor authentication. The IT manager agrees. He also adds supplier accounts to the quarterly account review, which had previously covered only staff. The camera company agrees to the new arrangement after a short discussion, and Jamal tests it during the next scheduled maintenance visit. The account is enabled at the start and disabled at the end, with both steps recorded in the IT log.

### 23.4 Cloud responsibilities

For cloud services, Jamal learns that responsibilities are shared. The provider secures its infrastructure, but Riverbend manages its own users, settings and data. He checks the email service settings and finds that external sharing of files is allowed by default. He restricts it to approved partners. Ms. Grant notes that many cloud exposures come from customer settings, not provider failures. He documents the change and checks the other sharing settings in the service, finding two more that allowed anonymous links. He restricts them as well and records all three settings in the documentation for future reviews.

### Worked example

Jamal lists six suppliers, checks contract terms and certificate scope, disables always-on supplier access and restricts default cloud file sharing.

> **Synthetic case.** Suppliers are synthetic.

### Errors and limits

A supplier certificate is useful evidence only if its scope covers the service used.

### Exercises

- **EX067 — Missing terms.** Which contract has no security terms? *Rubric:* 3 = camera maintenance company;; 2 = correct;; 1 = other;; 0 = none.
- **EX068 — Supplier access fix.** How is the camera company's access changed? *Rubric:* 3 = enabled only for scheduled work;; 2 = correct;; 1 = none;; 0 = none.
- **EX069 — Cloud setting.** What default cloud setting is restricted? *Rubric:* 3 = external file sharing;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Policies and procedures

### Learning outcomes

You will (1) distinguish policies from procedures; (2) write clear procedures for technical tasks; (3) keep documents current.

### 24.1 Policies and procedures

Jamal learns that a policy states what must happen, such as all staff accounts must use multi-factor authentication, while a procedure explains how to do it step by step. Riverbend's policies are written by the IT manager and approved by the chief executive. ISO/IEC 27002:2022 provides guidance on policies for information security, which Riverbend uses as a reference. Ms. Grant notes that technologists mostly write and follow procedures, so clear procedures are part of their craft. He reads the current policies before writing anything.

### 24.2 Writing procedures

Jamal writes procedures for tasks he performs: creating accounts from templates, running the monthly workstation check and handling a lost phone. Each lists purpose, when to use it, steps, expected results and what to do if something goes wrong. He tests each procedure by asking the technician to follow it without help. Two steps are unclear and he rewrites them. He learns that a procedure is good only if someone else can follow it. The technician says the revised versions are clear enough to use alone.

### 24.3 Version control

Jamal stores procedures in a shared folder with version numbers, dates and owners. Old versions are archived, not deleted, so the team can see what changed. He adds a review date to each. Ms. Grant explains that procedures referring to old screens or settings cause mistakes, so regular review is necessary. He sets reminders for six-monthly reviews. He also adds a short change note at the top of each document explaining what changed in the latest version and why, so readers do not have to compare versions themselves. The IT manager approves the structure and asks that all IT documents follow it.

### 24.4 Linking to policy

Each procedure refers to the policy it supports, so readers understand why the task matters. Jamal notices that the password policy still mentions monthly changes, though practice has changed. He asks the IT manager to update the policy so practice and policy agree. Ms. Grant notes that auditors check whether practice matches policy, and that outdated policies create avoidable findings. The IT manager updates the policy the following month and the chief executive approves the change. Jamal checks the other policies against current practice and finds no further contradictions.

### Worked example

Jamal distinguishes policy from procedure, writes and tests three procedures, adds versions and review dates and gets an outdated password policy updated.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Policies that contradict practice create avoidable audit findings.

### Exercises

- **EX070 — Procedure test.** How does Jamal test his procedures? *Rubric:* 3 = the technician follows them without help;; 2 = correct;; 1 = none;; 0 = none.
- **EX071 — Archive rule.** What happens to old procedure versions? *Rubric:* 3 = archived, not deleted;; 2 = correct;; 1 = deleted;; 0 = none.
- **EX072 — Outdated policy.** Which policy is outdated? *Rubric:* 3 = the password policy;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Security awareness support

### Learning outcomes

You will (1) support awareness activities as a technologist; (2) use real examples safely; (3) encourage reporting.

### 25.1 The technologist's part

Awareness at Riverbend is led by the human resources manager, but Jamal supports it with technical knowledge. He provides real examples from phishing reports, with personal details removed, for monthly staff tips. He also explains how the report button works. Ms. Grant notes that technologists see attacks first-hand, so their examples make awareness more concrete and relevant than generic training materials. He agrees a simple process with the human resources manager: each month he sends two anonymised examples with a short explanation, and she includes them in the staff newsletter with a reminder about the report button.

### 25.2 Short sessions

Jamal helps run ten-minute sessions at staff meetings in each centre. He shows two real phishing messages and points out clues: a sender address slightly different from the real one, urgent wording and a link that does not match the claimed site. Staff practise spotting clues on printed examples. He keeps sessions short because centre staff work shifts and cannot attend long training. After each session he asks staff which clue they found hardest to spot, and most say mismatched links. He adds a short guide to checking links on a phone.

### 25.3 Reporting culture

Jamal makes sure every report receives a thank-you within a day, even when the message was harmless. When a lifeguard reports a suspicious text message claiming to be from Riverbend payroll, Jamal confirms it was a scam and warns all staff. The lifeguard is thanked publicly at the next staff meeting. Ms. Grant explains that recognition encourages reporting, which helps detect attacks early. He keeps a log of reports and thank-you messages, and the human resources manager mentions reporting in the staff newsletter each month to keep the habit visible.

### 25.4 Measuring

Jamal tracks the number of reports per month and the time from first report to removal of phishing from mailboxes. Reports rise after the sessions. He avoids measuring individual click rates, which could discourage reporting. Ms. Grant notes that awareness measures should focus on helpful behaviour, such as reporting, rather than on catching people making mistakes. He presents the figures quarterly to the IT manager and the human resources manager in a short chart. They agree to keep the focus on reporting and to repeat the sessions each year with new examples.

### Worked example

Jamal supplies anonymised real examples, runs ten-minute centre sessions, thanks every reporter and measures reports and removal time rather than individual clicks.

> **Synthetic case.** Messages are synthetic.

### Errors and limits

Measuring individual click rates can discourage reporting.

### Exercises

- **EX073 — Session length.** How long are the sessions? *Rubric:* 3 = ten minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX074 — Phishing clue.** Name one phishing clue Jamal shows. *Rubric:* 3 = slightly different sender address;; 2 = one;; 1 = none;; 0 = none.
- **EX075 — Lifeguard report.** What did the lifeguard report? *Rubric:* 3 = a scam text claiming to be from payroll;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Automation and scheduling

### Learning outcomes

You will (1) automate routine security checks; (2) schedule and monitor scripts; (3) handle failures of automation.

### 26.1 What to automate

Jamal has written several scripts: the inactive account check, workstation baseline check, failed login analysis and restore verification. Running them by hand takes time and is easily forgotten. He selects those that run on a fixed schedule with predictable inputs and automates them. Ms. Grant advises automating stable tasks first and keeping a person involved for decisions, such as disabling accounts. He lists each candidate script with how often it runs, what input it needs and whether its output requires a decision, and chooses four for automation in the first month.

### 26.2 Scheduling

Jamal schedules the scripts on a server using the operating system's task scheduler. Each runs under a dedicated service account with only the access it needs. Results go to a shared folder and a summary email to the IT manager. He documents each schedule with its purpose, owner and timing. He learns that scheduled tasks also need inventory and ownership, just like systems. He tests each scheduled task for a week, checking that outputs arrive and that the service accounts cannot access anything beyond what each script needs.

### 26.3 Monitoring the automation

Automated checks can fail silently. Jamal adds a simple heartbeat: each script writes a line to a log when it finishes, and a separate check alerts if any script has not run on time. In the first month, the alert catches the baseline check failing after a password change on its service account. He fixes it the same day. Ms. Grant notes that unmonitored automation can give false confidence for months. He adds the heartbeat check itself to the scheduling documentation with its owner.

### 26.4 Keeping humans involved

Jamal designs the inactive account script to list accounts for review rather than disabling them automatically. The IT manager reviews the list weekly and disables accounts after checking with managers. One account belongs to a member of staff on long-term sick leave, who should not be disabled. Jamal learns that automation should support judgement where context matters, rather than replacing it. He adds a note field to the review list so the IT manager can record why any flagged account was kept, which helps later reviews avoid asking the same questions again.

### Worked example

Jamal automates four stable checks under dedicated service accounts, adds a heartbeat that catches a failing job and keeps human review for disabling accounts.

> **Synthetic case.** Schedules are synthetic.

### Errors and limits

Automation that fails silently gives false confidence.

### Exercises

- **EX076 — Automation choice.** Which tasks are automated first? *Rubric:* 3 = stable tasks with predictable inputs;; 2 = correct;; 1 = none;; 0 = none.
- **EX077 — Heartbeat catch.** What did the heartbeat catch? *Rubric:* 3 = baseline check failing after a password change;; 2 = correct;; 1 = none;; 0 = none.
- **EX078 — Sick leave.** Why should one inactive account stay enabled? *Rubric:* 3 = staff on long-term sick leave;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Documentation and handover

### Learning outcomes

You will (1) document systems and controls for others; (2) prepare a handover; (3) check documentation by use.

### 27.1 What to document

Jamal documents what he has built and changed: network diagrams, account templates, procedures, scripts with instructions, schedules and the supplier list. Each document names an owner and a review date. Ms. Grant explains that small IT teams depend on documentation, because when one person is absent the other must manage alone. Jamal stores everything in one structured folder with an index. He asks the IT manager to review the index and confirm that nothing important is missing. The IT manager adds one item: the procedure for renewing the website certificate.

### 27.2 Handover plan

As his placement nears its end, Jamal prepares a handover. He lists every task he performs, how often, which document explains it and who will take it over. The technician will take most tasks; the IT manager will review results. He schedules sessions where the technician performs each task with Jamal watching, then alone. Ms. Grant notes that handover is a security control, because tasks left without owners stop. He keeps a checklist showing each task, the date it was handed over and the technician's signature.

### 27.3 Testing by use

During handover, the technician follows the restore test procedure and gets stuck where a server name has changed. Jamal updates the document. The technician also finds the script instructions assume knowledge he does not have. Jamal adds a short explanation. He learns that documentation is tested by the people who must use it, not by its author. After the changes, the technician follows each procedure again without help. Jamal records the date each document was tested and by whom, so later readers know it has been checked by a real user.

### 27.4 Final check

Jamal checks that all accounts he used are disabled or transferred, all passwords he knew are changed and his access to Riverbend systems is removed on his last day. He confirms this with the IT manager. Ms. Grant notes that departing staff and students are leavers too, and that following the leaver process for oneself sets a good example. He also returns his building access card and confirms that his name is removed from the out-of-hours contact list. The IT manager signs the leaver checklist, and Jamal keeps a copy in his notebook.

### Worked example

Jamal documents his work in an indexed folder, plans a supervised handover, fixes documents after the technician tests them and confirms his own access is removed.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Documentation tested only by its author often fails other users.

### Exercises

- **EX079 — Handover recipient.** Who takes over most tasks? *Rubric:* 3 = the technician;; 2 = correct;; 1 = other;; 0 = none.
- **EX080 — Restore document fix.** What was wrong in the restore procedure? *Rubric:* 3 = a changed server name;; 2 = correct;; 1 = none;; 0 = none.
- **EX081 — Own access.** What happens to Jamal's access? *Rubric:* 3 = removed on his last day;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Work placement

### Learning outcomes

You will (1) apply skills in a workplace; (2) work within professional boundaries; (3) reflect on learning.

### 28.1 The placement

Jamal's final-year placement runs for a full term at Riverbend's head office, with visits to centres. He works on account reviews, monitoring, patching support and the applied project. The IT manager meets him weekly to review progress. Ms. Grant visits twice. He finds that real work involves frequent interruptions, such as urgent requests from centres, so planning and prioritising are as important as technical skill. He keeps a daily task list and reviews it with the IT manager each week to agree priorities for the next week.

### 28.2 Boundaries

Jamal has access to member data and systems. He follows Riverbend's policies, uses only the access needed for his tasks and asks before investigating anything outside his remit. When he notices a member's details displayed on a public notice board at one centre, he reports it to the centre manager rather than removing it himself. Ms. Grant notes that knowing when to act and when to report is part of professional judgement. The centre manager removes the notice the same day and thanks him.

### 28.3 Learning

Jamal keeps his notebook throughout the placement. He records not only technical tasks but conversations: explaining to a centre manager why her old computer could not stay on the network, or negotiating a maintenance window with the café supplier. He notes that communication takes as much of his time as technical work, and that staff respond better when they understand reasons. Ms. Grant reads extracts from his notebook during her visits and comments that his records of conversations show growing confidence in explaining technical decisions to people without technical backgrounds.

### 28.4 Feedback

At the end of the placement, the IT manager gives written feedback. Strengths include reliable scripting, clear documentation and calm handling of the mailbox incident. Areas to develop include estimating how long tasks take and speaking up earlier when blocked. Jamal discusses the feedback with Ms. Grant and sets goals for his applied project. Jamal sets two goals: to estimate each project task before starting and compare the estimate with the actual time, and to raise blockers within a day. Ms. Grant agrees that these goals are specific and measurable, and asks him to report on them at the end of the project.

### Worked example

Jamal completes a term-long placement, respects boundaries by reporting rather than acting on a notice board exposure, records communication lessons and receives balanced feedback.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Investigating outside one's remit without asking oversteps professional boundaries.

### Exercises

- **EX082 — Placement interruptions.** What makes planning important on placement? *Rubric:* 3 = frequent urgent interruptions;; 2 = correct;; 1 = none;; 0 = none.
- **EX083 — Notice board.** What does Jamal do about the notice board? *Rubric:* 3 = reports it to the centre manager;; 2 = correct;; 1 = remove;; 0 = none.
- **EX084 — Development area.** Name one area to develop. *Rubric:* 3 = estimating task time;; 2 = one;; 1 = none;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Applied project

### Learning outcomes

You will (1) define a practical security project with a client; (2) deliver it with evidence; (3) measure the result.

### 29.1 Defining the project

For his applied project, Jamal chooses remote access to Riverbend systems. The firewall review and log analysis showed services exposed to the internet more than necessary. The project goal is that every remote access path is known, restricted to the people and suppliers who need it and protected by multi-factor authentication. The IT manager agrees and sets a deadline of eight weeks. Ms. Grant approves the plan and success criteria. He writes the goal, criteria and deadline on a one-page plan signed by the IT manager.

### 29.2 Finding every path

Jamal lists remote access paths: the staff remote desktop gateway, the file transfer server, the camera company's remote account, the pool controller supplier's connection and the email service. He uses the firewall rules, the supplier list and an authorised external scan of Riverbend's internet addresses. The scan finds one more path: an old web management page for a router, reachable from the internet. He records each path in a table with its purpose, the people or suppliers who use it, how it is protected and the evidence he used to find it. The table becomes the project's main working document.

### 29.3 Delivering

Jamal works through each path. The gateway already uses multi-factor authentication. The file transfer server was restricted earlier. The camera account is disabled between visits. The pool controller connection moves behind the gateway. The router management page is closed to the internet. He records each change, the date and the evidence: configuration screenshots and a repeat external scan. He tests each change from outside Riverbend's network using an authorised laptop and confirms that the closed paths are no longer reachable. For the pool controller, he confirms with the supplier that their engineers can still connect through the gateway.

### 29.4 Measuring

Jamal measures the result: five known paths and one newly found, all six now restricted or closed, and all remaining paths protected by multi-factor authentication. The repeat scan shows no unexpected services. Weekly failed login analysis shows no external guessing. He notes the limits: the scan sees only what is reachable at the time, so it must be repeated regularly. He presents the measures in a short table with the evidence linked, and the IT manager schedules a repeat external scan every quarter. Jamal estimated six weeks for the project and finished in seven, which he records against his feedback goal.

### Worked example

Jamal defines a remote access project, finds six paths including an exposed router page, restricts or closes all of them with evidence and measures the result with a repeat scan.

> **Synthetic case.** The project is synthetic.

### Errors and limits

A single external scan shows only what was reachable at that moment.

### Exercises

- **EX085 — Project goal.** What is the project goal? *Rubric:* 3 = every remote path known, restricted and MFA-protected;; 2 = correct;; 1 = none;; 0 = none.
- **EX086 — Extra path.** What extra path did the scan find? *Rubric:* 3 = an old router management page;; 2 = correct;; 1 = none;; 0 = none.
- **EX087 — Path total.** How many paths were restricted or closed? *Rubric:* 3 = six;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Project review and next steps

### Learning outcomes

You will (1) present a project to a client and tutor; (2) answer questions about evidence; (3) plan continued development.

### 30.1 Presentation

Jamal presents his project to the IT manager, the chief executive and Ms. Grant. He explains the problem in plain language: ways into Riverbend's systems from the internet that were not all known or protected. He shows the six paths, the changes and the evidence. The chief executive asks how Riverbend will know if a new path appears. Jamal explains the scheduled scans and the firewall review every six months. He brings printed copies of the path table and the scan results for each person present.

### 30.2 Questions

Ms. Grant asks why he did not remove remote desktop entirely. Jamal explains that some staff work from home and need it, so the gateway with multi-factor authentication balances need and risk. The IT manager asks about cost; Jamal shows that every change used existing tools. Both answers rely on evidence from his records. He learns that clear records make questions easy to answer. Ms. Grant also asks what he would do differently, and he answers that he would have run the external scan first, because it found a path the internal records missed.

### 30.3 Outcome

The project is accepted, and Riverbend adopts the six-monthly remote access review as a standing task. Jamal receives a strong mark. He reflects that the three years taught him to configure, check and document controls, and that the most valuable habit was confirming that each change worked. Ms. Grant notes that his notebook shows steady growth from following instructions to making careful judgements. The chief executive thanks him for making a technical subject understandable, and the IT manager asks him to present the project to centre managers at their next meeting.

### 30.4 Next steps

Jamal accepts a junior technician role at Riverbend after graduating. He plans to study for a professional certification and to deepen his knowledge of cloud services. Ms. Grant reminds him that standards change; ISO/IEC 27000 was revised in 2026, and he should check editions when citing them. The next course in this area, data governance, looks at how decisions about data quality and use are made, which complements the controls he has learned to run. He also plans to mentor next year's placement student.

### Worked example

Jamal presents his remote access project, answers questions on remote desktop and cost with evidence, has the review adopted as a standing task and plans further study.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Answers without records to support them weaken a project review.

### Exercises

- **EX088 — New path detection.** How will new paths be detected? *Rubric:* 3 = scheduled scans and six-monthly firewall review;; 2 = correct;; 1 = none;; 0 = none.
- **EX089 — Remote desktop kept.** Why keep remote desktop? *Rubric:* 3 = staff work from home;; 2 = correct;; 1 = none;; 0 = none.
- **EX090 — Standing task.** What becomes a standing task? *Rubric:* 3 = the six-monthly remote access review;; 2 = correct;; 1 = other;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Jamal Haddad, Ms. Fiona Grant, Northgate College of Technology, Riverbend Leisure Trust and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Configure, check and maintain security controls.

**EX002.** About 350 staff.

**EX003.** So work can be repeated exactly and explained to others.

**EX004.** Instructors.

**EX005.** Integrity, because changed details could divert payments.

**EX006.** It is restricted to instructors and managers.

**EX007.** Because people change roles.

**EX008.** They log in automatically as administrator.

**EX009.** It shrinks the attack surface.

**EX010.** Devices handling payment data.

**EX011.** A web interface with a default password.

**EX012.** Tills, staff, cameras and guests.

**EX013.** Accounts with no login for sixty days.

**EX014.** It skips and reports them.

**EX015.** The script version and input file name.

**EX016.** The re module.

**EX017.** Eleven minutes.

**EX018.** Ninety days.

**EX019.** ISO/IEC 27000:2026, the family overview.

**EX020.** The attacker inherits only that account's limited rights.

**EX021.** Allowing only encrypted, Riverbend-issued devices.

**EX022.** 164 of 210, 78.1 percent.

**EX023.** 129 workstations, 61.4 percent.

**EX024.** Laptops without encryption.

**EX025.** Updates for actively exploited flaws.

**EX026.** Five workstations.

**EX027.** By isolating it on its own segment without internet access.

**EX028.** Riverbend's IT manager, in writing.

**EX029.** A reported weakness that is not actually present.

**EX030.** The remote access tool had a second installation.

**EX031.** Only the booking system and staff rota.

**EX032.** A weekly report from the payroll system.

**EX033.** The account used by an old backup tool.

**EX034.** Hardware keys.

**EX035.** The email system.

**EX036.** Text message codes.

**EX037.** Staff adding a number to the same word each time.

**EX038.** A password manager with individual accounts.

**EX039.** Camera recorder passwords and router credentials.

**EX040.** Rule 11.

**EX041.** Rule 11 matches all traffic first.

**EX042.** Supplier remote desktop access to the tills.

**EX043.** It is known to many former staff.

**EX044.** The café supplier.

**EX045.** For compatibility with an old printer.

**EX046.** On several reception computers after reinstallation.

**EX047.** A script trying to run from a downloaded invoice attachment.

**EX048.** On single-purpose machines such as tills.

**EX049.** Fake messages using Riverbend's domain could reach members.

**EX050.** Five centres.

**EX051.** By phone using a number already on file.

**EX052.** They should move to the file server.

**EX053.** The backup job excluded it after a folder rename.

**EX054.** Fourteen days.

**EX055.** The laptop was encrypted.

**EX056.** Member names.

**EX057.** Thirty days before expiry.

**EX058.** It was used to store cleaning supplies.

**EX059.** By comparing each terminal with a photo and checking seals.

**EX060.** It was visible from reception.

**EX061.** 838 failed logins.

**EX062.** 203.0.113.45, with 412 failures.

**EX063.** 671 failures, 80.1 percent.

**EX064.** The Respond and Recover functions.

**EX065.** A rule forwarding copies of mail to an external address.

**EX066.** Delayed enrolment in multi-factor authentication.

**EX067.** The camera maintenance company's contract.

**EX068.** Enabled only for scheduled work with individual accounts.

**EX069.** External sharing of files.

**EX070.** By asking the technician to follow them without help.

**EX071.** They are archived, not deleted.

**EX072.** The password policy, still mentioning monthly changes.

**EX073.** Ten minutes.

**EX074.** A slightly different sender address.

**EX075.** A scam text message claiming to be from Riverbend payroll.

**EX076.** Stable tasks with fixed schedules and predictable inputs.

**EX077.** The baseline check failing after a service account password change.

**EX078.** It belongs to staff on long-term sick leave.

**EX079.** The technician.

**EX080.** A server name had changed.

**EX081.** It is removed on his last day.

**EX082.** Frequent urgent requests from centres.

**EX083.** He reports it to the centre manager.

**EX084.** Estimating how long tasks take.

**EX085.** Every remote access path known, restricted and protected by MFA.

**EX086.** An old router management page reachable from the internet.

**EX087.** Six paths.

**EX088.** Through scheduled scans and a six-monthly firewall review.

**EX089.** Some staff work from home and need it.

**EX090.** The six-monthly remote access review.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- National Institute of Standards and Technology. (2004). *Standards for security categorization of federal information and information systems* (FIPS 199). https://doi.org/10.6028/NIST.FIPS.199
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
