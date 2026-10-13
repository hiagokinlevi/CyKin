# Information Security: Postgraduate Course

- Language: English (`en`); course 140, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: experienced IT practitioners building a risk-based information security programme for a multi-site healthcare organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs measure critical patch compliance per clinic on synthetic device data and flag lookalike sender domains by edit distance in a synthetic mail log. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one practitioner from governance, risk assessment and inventory through patching, access, phishing, recovery, incidents and board reporting to a ransomware-readiness capstone and its presentation. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Elena Petrova** | Postgraduate practitioner, IT and security manager | Invented |
| **Dr. Hamid Qureshi** | Tutor | Invented |
| **Thornbury Business School** | Fictional business school | Invented |
| **Moorfield Dental Group** | Fictional dental group, 22 clinics and about 600 staff | Invented |

### Core sources

ISO/IEC 27000:2026; ISO/IEC 27001:2022; ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; NIST CSWP 29 (CSF 2.0); Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — The practitioner and Moorfield Dental Group

### Learning outcomes

You will (1) describe the practitioner case; (2) identify what a postgraduate course adds to experience; (3) set learning goals linked to workplace problems.

### 1.1 The practitioner

Elena Petrova has worked in IT for twelve years and now manages IT and security for the fictional Moorfield Dental Group. She enrols in a two-year part-time postgraduate programme in information security at the fictional Thornbury Business School, taught by Dr. Hamid Qureshi. She brings practical skill but little formal training in governance, risk or measurement. Dr. Qureshi explains that the course aims to help experienced practitioners turn their experience into structured, defensible decisions that boards and auditors can follow and challenge.

### 1.2 The organisation

Moorfield runs twenty-two dental clinics with about six hundred staff and roughly five hundred and seventy computers, tablets and imaging devices. Clinics hold patient records, X-ray images, appointment diaries and payment details. Most clinics have no IT staff; three rely on a part-time local contact. A central team of four, led by Elena, supports everyone. Patients expect confidentiality, and clinics cannot treat patients if systems are unavailable, so both confidentiality and availability matter greatly. Elena's team also manages the central servers and the head office network.

### 1.3 What the course adds

Elena's experience tells her what usually breaks and how to fix it. The course adds frameworks for deciding what matters most, methods for measuring whether controls work and skills for explaining security to a board of dentists and investors. Dr. Qureshi asks each student to bring one workplace problem to every module. Elena chooses patch delays in small clinics, recurring phishing attempts and unclear recovery plans, which she suspects are connected through the same staffing gaps. She writes each problem at the top of her course notebook.

### 1.4 Learning goals

Elena writes three learning goals: build a risk-based security programme Moorfield's board can approve, measure the main controls with clear definitions and lead a credible capstone improvement project. Dr. Qureshi asks her to state how she will know each goal is met. She adds evidence for each: a board-approved programme document, a monthly measure set with definitions and a capstone report reviewed by the board. She learns that goals with evidence are easier to pursue and assess. Dr. Qureshi approves the goals and their evidence.

### Worked example

Elena enrols, describes Moorfield's twenty-two clinics and four-person team, links course content to three workplace problems and sets learning goals with evidence.

> **Synthetic case.** Elena, Moorfield and Thornbury are synthetic.

### Errors and limits

Experience without structured methods makes decisions hard to defend.

### Exercises

- **EX001 — Clinic count.** How many clinics does Moorfield run? *Rubric:* 3 = twenty-two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Central team.** How large is the central IT team? *Rubric:* 3 = four people;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX003 — Workplace problems.** Name one workplace problem Elena brings. *Rubric:* 3 = patch delays in small clinics;; 2 = one;; 1 = vague;; 0 = none.
- **EX004 — Course addition.** What does the course add to Elena's experience? *Rubric:* 3 = frameworks, measurement and board communication;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX005 — Goal evidence.** What evidence shows the programme goal is met? *Rubric:* 3 = a board-approved programme document;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 12)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Security governance and the management system

### Learning outcomes

You will (1) design a governance structure for security; (2) apply ISO/IEC 27001 management system concepts; (3) set risk appetite with a board.

### 2.1 Governance structure

Moorfield's board consists of three dentist partners and two investor representatives. Security decisions have been made informally by Elena and the operations director. Elena proposes a structure: the board approves policy and risk appetite each year, a security committee of Elena, the operations director and a clinical lead meets monthly and clinic managers are accountable for local controls. Dr. Qureshi notes that clear roles make it obvious who decides, who acts and who must be told. The board approves the structure at its next quarterly meeting.

### 2.2 Management system concepts

Elena studies ISO/IEC 27001:2022, which sets requirements for an information security management system. It asks the organisation to understand its context and interested parties, obtain leadership commitment, assess and treat risks, provide resources, operate controls, evaluate performance and improve. ISO/IEC 27000:2026 gives the overview of the family and its terms. Elena realises that Moorfield already does many of these activities but without records, so it cannot show they happen consistently. She lists Moorfield's existing activities against each clause and marks which have records, which have partial records and which have none at all.

### 2.3 Risk appetite

Elena drafts a risk appetite statement for the board. Moorfield will accept very low risk to patient record confidentiality, low risk of clinical systems being unavailable during opening hours and moderate risk for administrative systems such as marketing. The board debates the wording and adds that no clinic should be unable to treat patients for more than half a day. Dr. Qureshi notes that appetite statements turn values into rules for prioritising work. The final statement fits on one page and is signed by the board chair.

### 2.4 Scope

Elena defines the scope of Moorfield's management system: all clinics, the head office, the patient record system, imaging systems and payment processing. The dental laboratory, run by a separate company, is excluded but treated as a supplier. She writes the scope in one paragraph with a diagram. Dr. Qureshi warns that unclear scope causes confusion later, especially when an auditor or insurer asks what the programme actually covers. The board approves the scope, and Elena adds it to the front of the security programme document so everyone reading the programme knows what it covers.

### Worked example

Elena designs a board, committee and clinic-manager structure, maps Moorfield to ISO/IEC 27001 concepts, drafts a risk appetite with a half-day clinical limit and defines scope.

> **Synthetic case.** Board arrangements are synthetic; standards are paraphrased.

### Errors and limits

Activities without records cannot show they happen consistently.

### Exercises

- **EX006 — Committee members.** Who sits on the security committee? *Rubric:* 3 = Elena, operations director, clinical lead;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX007 — Missing records.** What does Moorfield lack despite doing activities? *Rubric:* 3 = records;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX008 — Board addition.** What limit does the board add? *Rubric:* 3 = no clinic unable to treat patients over half a day;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX009 — Excluded party.** What is excluded from scope? *Rubric:* 3 = the dental laboratory;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX010 — Overview standard.** Which standard gives the family overview? *Rubric:* 3 = ISO/IEC 27000:2026;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 12)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Risk assessment for a clinic network

### Learning outcomes

You will (1) conduct a structured risk assessment; (2) rate likelihood and impact consistently; (3) select treatments aligned with appetite.

### 3.1 Method

Elena follows the approach in NIST SP 800-30 Revision 1: identify threat sources and events, vulnerabilities and predisposing conditions, then judge likelihood and impact. She runs workshops with clinic managers, the clinical lead and finance. The workshops identify ransomware, phishing leading to account compromise, lost or stolen tablets, supplier failure and staff misuse of patient records as the main threats. Dr. Qureshi advises involving people who run the work, because they know where processes really break. Each workshop lasts two hours and produces a list of threats with examples.

### 3.2 Consistent ratings

Ratings vary between people. Elena defines five-point scales with examples: impact five means a clinic cannot treat patients for over a day or many patient records are exposed; likelihood five means expected within a year. She asks two colleagues to rate ten risks independently and compares results. Where they differ by more than one point, they discuss and agree. Dr. Qureshi notes that calibration exercises make ratings more consistent and defensible. Three of the ten risks needed discussion, and the agreed ratings are recorded with the reasons.

### 3.3 Results

Ransomware and phishing-led compromise rate highest, followed by patching delays in clinics without IT staff and weak recovery testing. Staff misuse of patient records rates moderate likelihood and high impact. Elena records each risk with an owner, current controls and planned treatment. She notes that patch delays and weak recovery both make ransomware more damaging, so treating them reduces several risks at once. She presents the register to the security committee as a one-page heat map with the top five risks listed beneath it, each with its owner and the next planned action.

### 3.4 Treatment

Elena selects treatments aligned with appetite. For ransomware, she plans faster patching, immutable backups and tested recovery. For phishing, she plans multi-factor authentication and mail filtering improvements. For misuse, she plans access reviews and alerts on unusual record viewing. Cyber insurance transfers some financial loss. The board approves the plan, accepting moderate residual risk for administrative systems. Dr. Qureshi notes that recording accepted risks protects everyone later. Elena records the board's decision and the accepted residual risks in the minutes, with a review date set for the following year.

### Worked example

Elena runs workshops following SP 800-30 Revision 1, calibrates five-point scales, ranks ransomware and phishing highest and selects treatments approved by the board.

> **Synthetic case.** Assessments are synthetic.

### Errors and limits

Uncalibrated ratings vary widely between assessors.

### Exercises

- **EX011 — Threat example.** Name one main threat identified. *Rubric:* 3 = ransomware;; 2 = one;; 1 = vague;; 0 = none.
- **EX012 — Calibration rule.** When do raters discuss differences? *Rubric:* 3 = when they differ by more than one point;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX013 — Linked risks.** Which two risks worsen ransomware damage? *Rubric:* 3 = patch delays and weak recovery;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Misuse treatment.** How is staff misuse treated? *Rubric:* 3 = access reviews and alerts on unusual viewing;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX015 — Transfer method.** What transfers some financial loss? *Rubric:* 3 = cyber insurance;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 12)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Asset and supplier inventory

### Learning outcomes

You will (1) build a reliable asset inventory across sites; (2) identify suppliers with access to data; (3) assign owners and classifications.

### 4.1 Assets across sites

Elena's inventory exists in a spreadsheet updated when devices are bought. She compares it with the device management system and network records. Several clinics have imaging computers bought directly by dentists and never registered. These run old operating systems because imaging software suppliers have not certified newer versions. Dr. Qureshi notes that unregistered devices often carry the highest risk, because they are excluded from patching, monitoring and backup by default. She finds eleven unregistered imaging computers and adds them to the inventory with their clinic, supplier and operating system version.

### 4.2 Classifying information

Elena classifies information: patient clinical records and images as restricted, payment data as restricted, staff records as confidential, appointment diaries as confidential and marketing materials as internal. Each class has handling rules, such as encryption on portable devices for restricted data. She keeps the scheme to four levels. ISO/IEC 27002:2022 includes guidance on classifying and labelling information, which she uses as a reference without copying its text. She prints a one-page guide for clinics with examples of each class and the handling rules, and clinic managers display it in staff rooms.

### 4.3 Suppliers

Moorfield uses suppliers for the patient record system, imaging software, payments, email and IT support at the three clinics with part-time contacts. Elena lists each supplier's access and data. The imaging supplier connects remotely to clinic computers using a shared password known to its support staff. Elena recommends individual accounts, multi-factor authentication and access enabled only during approved support sessions. The imaging supplier agrees after Elena explains Moorfield's insurance requirements, and the change is completed over two months. She records supplier access in a register reviewed each quarter by the security committee.

### 4.4 Ownership

Each asset and supplier relationship needs an owner. Elena assigns clinic managers as owners of local devices, the clinical lead as owner of patient records and herself as owner of central systems. Supplier relationships are owned by the person who manages each contract. She records owners in the inventory. Dr. Qureshi notes that ownership makes accountability concrete, especially in organisations with many sites. Clinic managers receive a short briefing explaining what ownership means in practice: knowing which devices are in their clinic, reporting changes and confirming access lists during each quarterly review.

### Worked example

Elena reconciles inventory with device and network records, finds unregistered imaging computers, classifies information, tightens imaging supplier access and assigns owners.

> **Synthetic case.** Inventories are synthetic.

### Errors and limits

Devices bought outside central purchasing often escape patching and backup.

### Exercises

- **EX016 — Unregistered devices.** What unregistered devices does Elena find? *Rubric:* 3 = imaging computers bought by dentists;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX017 — Old systems.** Why do imaging computers run old systems? *Rubric:* 3 = suppliers have not certified newer versions;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX018 — Restricted data.** Which information is restricted? *Rubric:* 3 = clinical records, images and payment data;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX019 — Supplier fix.** What does Elena recommend for imaging supplier access? *Rubric:* 3 = individual accounts, MFA, session-only access;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Records owner.** Who owns patient records? *Rubric:* 3 = the clinical lead;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 12)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Patch and vulnerability management

### Learning outcomes

You will (1) measure patch compliance across sites; (2) find sites that need support; (3) design remediation for constrained systems.

### 5.1 Measuring compliance

Elena defines her measure: the share of devices with critical security updates installed within fourteen days of release, by clinic. She extracts synthetic data from the device management system. Dr. Qureshi asks her to report both the overall figure and the spread between clinics, because a good average can hide clinics with serious gaps, and attackers need only one weak point to enter a connected network. She writes the definition in the measure handbook with the data source, the owner and the reporting frequency, so the same figure can be produced each month.

### 5.2 The patch lab

The lab covers 566 synthetic devices across twenty-two clinics. Overall, 513 devices, 90.6 percent, received critical updates within fourteen days. The three lowest clinics are C19 with 10 of 20 devices, 50.0 percent; C15 with 20 of 28, 71.4 percent; and C07 with 22 of 30, 73.3 percent. All three are the clinics relying on a part-time local IT contact. Elena notes that the overall figure would have hidden these clinics completely. She presents the clinic-level results to the security committee with a short chart, and the committee agrees that the three clinics should receive extra support immediately rather than waiting for the next quarterly review.

### Lab — Critical patch compliance per clinic on synthetic device data

```python
"""Critical patch compliance per clinic on synthetic device data (stdlib only)."""
import random
random.seed(14)
rows = []
for c in range(1, 23):
    late_p = 0.06 if c not in (7, 15, 19) else 0.30          # three clinics with a part-time IT contact
    for d in range(random.randint(20, 34)):
        rows.append((f"C{c:02d}", random.random() >= late_p))
by = {}
for clinic, ok in rows:
    t = by.setdefault(clinic, [0, 0]); t[0] += ok; t[1] += 1
total_ok = sum(ok for _, ok in rows)
print(f"devices {len(rows)}; patched within 14 days {total_ok} ({total_ok/len(rows):.1%})")
worst = sorted(by.items(), key=lambda kv: kv[1][0] / kv[1][1])[:3]
for c, (ok, n) in worst:
    print(f"{c}: {ok}/{n} ({ok/n:.1%})")
```

Run with `python3 lab_patch.py`. Verified output:

```text
devices 566; patched within 14 days 513 (90.6%)
C19: 10/20 (50.0%)
C15: 20/28 (71.4%)
C07: 22/30 (73.3%)
```

### 5.3 Causes and support

Elena visits the three clinics. Devices are often switched off overnight, when updates are scheduled, and the part-time contacts lack time to chase them. She changes update scheduling to lunchtime with automatic restarts outside appointments and asks the device management system to alert her when a device misses two cycles. She also arranges a monthly remote check by the central team. Dr. Qureshi notes that the fix addresses causes rather than blaming local staff. After two months, all three clinics exceed ninety percent.

### 5.4 Constrained systems

Imaging computers cannot always receive operating system updates because suppliers restrict them. Elena isolates them on a separate network segment, blocks internet access except to the supplier's update service and restricts which devices can connect to them. She records each as an exception with an expiry date and a request to the supplier for a supported version. She learns that when patching is impossible, reducing exposure is the next best control. The supplier promises a supported version within the year, and Elena tracks the commitment in the risk register.

### Worked example

Elena measures 90.6 percent compliance overall, finds three clinics at 50.0 to 73.3 percent, fixes scheduling causes and isolates unpatchable imaging computers.

> **Synthetic case.** Devices are synthetic; outputs come from lab_patch.py.

### Errors and limits

An overall compliance figure can hide clinics with serious gaps.

### Exercises

- **EX021 — Overall compliance.** What is overall patch compliance? *Rubric:* 3 = 513 of 566, 90.6 percent;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX022 — Lowest clinic.** Which clinic is lowest? *Rubric:* 3 = C19 at 50.0 percent;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Common factor.** What do the three lowest clinics share? *Rubric:* 3 = a part-time local IT contact;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX024 — Schedule fix.** How is update scheduling changed? *Rubric:* 3 = lunchtime with restarts outside appointments;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX025 — Imaging control.** How are unpatchable imaging computers protected? *Rubric:* 3 = isolated segment and restricted access;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 12)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Identity and access

### Learning outcomes

You will (1) design role-based access for clinical systems; (2) review access across sites; (3) protect privileged and remote access.

### 6.1 Roles

Elena designs roles for the patient record system: dentist, hygienist, dental nurse, receptionist, clinic manager and central administrator. Each role has defined permissions. Receptionists see appointments and contact details but not clinical notes; nurses see clinical notes for patients at their clinic. Previously, many staff had broad access copied from colleagues. Dr. Qureshi notes that clinical environments need quick access in emergencies, so roles must be designed with clinicians, not imposed on them. She runs two workshops with clinicians to test the roles.

### 6.2 Emergency access

Clinicians sometimes need records from another clinic, for example when a patient attends an unfamiliar site. Elena designs break-glass access: staff can open such a record after stating a reason, the action is logged and the clinical lead reviews a weekly report. Most uses are legitimate. Dr. Qureshi explains that break-glass access balances patient care with privacy, provided reviews actually happen and staff know they do. The clinical lead reviews the first month's report and finds every use explained, which reassures staff and patients' representatives. Elena records the review in the security committee minutes.

### 6.3 Access reviews

Elena runs quarterly reviews comparing system accounts with the staff list from human resources. The first review finds former staff with active accounts, mostly locum dentists whose contracts ended. She adds locum end dates to the human resources system so accounts expire automatically. She learns that temporary staff are a common source of leftover access in clinical settings. The first review takes two days; she expects later reviews to be faster as leftover accounts are cleared. The second review, three months later, finds only one former staff account, which belonged to a locum whose end date had been entered incorrectly.

### 6.4 Privileged and remote access

Central administrators and suppliers hold powerful access. Elena requires separate administrator accounts with hardware security keys, and supplier access only through a managed gateway with multi-factor authentication and recorded sessions. She removes shared administrator passwords. She notes that Saltzer and Schroeder's principle of least privilege and NIST SP 800-53 Revision 5 access control guidance both support these measures. Dr. Qureshi asks her to measure enrolment. Within a month, all central administrators use hardware keys, and the three suppliers with remote access use the gateway. She reports the enrolment figures to the security committee.

### Worked example

Elena designs six clinical roles with clinicians, adds logged break-glass access, links locum end dates to account expiry and protects privileged and supplier access.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Copying colleagues' access spreads excess rights across clinics.

### Exercises

- **EX026 — Receptionist view.** What can receptionists see? *Rubric:* 3 = appointments and contact details;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX027 — Break-glass review.** Who reviews break-glass use? *Rubric:* 3 = the clinical lead weekly;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX028 — Leftover access.** Which staff most often kept access? *Rubric:* 3 = locum dentists;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Admin factor.** What protects administrator accounts? *Rubric:* 3 = hardware security keys;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX030 — Supplier gateway.** How do suppliers connect? *Rubric:* 3 = managed gateway with MFA and recorded sessions;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 12)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Phishing and email security

### Learning outcomes

You will (1) analyse phishing patterns in mail data; (2) detect lookalike sender domains; (3) combine technical and human controls against phishing.

### 7.1 The problem

Moorfield's clinics receive frequent phishing emails, some pretending to come from head office or suppliers asking for payment or login details. Last year, a clinic manager entered her password on a fake login page, and the account sent phishing to patients before it was locked. Elena wants to understand the patterns. Dr. Qureshi suggests starting with sender domains, because many attacks use domains that look almost identical to genuine ones, which busy staff rarely notice. She asks the email provider for a three-month log export.

### 7.2 The lookalike lab

The lab reads a synthetic log of 5,823 inbound messages from 68 distinct sender domains. It compares each domain with Moorfield's own domain using edit distance, the number of single-character changes needed to turn one into the other. Four domains are within two changes, such as a digit one replacing a letter l or a hyphen inserted, and 23 messages came from them. Elena notes that all four would pass a quick glance. She shows the four domains to the security committee side by side with the genuine one, and none of the members spots every difference without help.

### Lab — Flagging lookalike sender domains by edit distance in a synthetic mail log

```python
"""Flag lookalike sender domains by edit distance in a synthetic mail log (stdlib only)."""
import random
random.seed(30)
OWN = "moorfielddental.example"
def dist(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
fakes = ["moorfie1ddental.example", "moorfielddentai.example", "moorfield-dental.example", "moorfielddental.examp1e"]
normal = [f"supplier{i}.example" for i in range(60)] + ["labwork.example", "dentalsupply.example", "bank.example"]
log = [random.choice(normal) for _ in range(5000)] + [OWN] * 800 + [random.choice(fakes) for _ in range(23)]
flag = {d for d in set(log) if d != OWN and dist(d, OWN) <= 2}
n_flag = sum(d in flag for d in log)
print(f"messages {len(log)}; distinct sender domains {len(set(log))}")
print(f"lookalike domains (distance <= 2): {sorted(flag)}; messages from them {n_flag}")
```

Run with `python3 lab_lookalike.py`. Verified output:

```text
messages 5823; distinct sender domains 68
lookalike domains (distance <= 2): ['moorfie1ddental.example', 'moorfield-dental.example', 'moorfielddentai.example', 'moorfielddental.examp1e']; messages from them 23
```

### 7.3 Technical controls

Elena asks the email provider to quarantine messages from domains within two edits of Moorfield's and of key suppliers' domains, and to mark all external messages with a visible banner. She publishes email authentication records for Moorfield's domain, so receiving systems can reject messages falsely claiming to come from it. She also enables multi-factor authentication for all mailboxes, so a stolen password alone no longer opens an account. After a month, the quarantine catches several new lookalike messages, and the email provider confirms that messages falsely using Moorfield's own domain are now rejected.

### 7.4 Human controls

Technical controls miss some attacks. Elena introduces a simple rule for payment and bank detail changes: always confirm by calling a known number, never one given in the email. She adds a report button and thanks every reporter. Short monthly examples show real lookalike domains with the differences highlighted. Dr. Qureshi notes that people and technology together give better protection than either alone. Clinic managers say the monthly examples are useful because staff discuss them in team meetings. Within three months, reports of suspicious emails double, and the central team finds two campaigns earlier than before.

### Worked example

Elena analyses 5,823 synthetic messages, finds four lookalike domains sending 23 messages, quarantines near-matches, adds email authentication and MFA and sets a call-back rule.

> **Synthetic case.** Mail data are synthetic; outputs come from lab_lookalike.py.

### Errors and limits

Lookalike domains pass a quick glance, so relying on staff spotting them fails.

### Exercises

- **EX031 — Message count.** How many messages does the log contain? *Rubric:* 3 = 5,823;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX032 — Lookalike count.** How many lookalike domains are flagged? *Rubric:* 3 = four;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX033 — Lookalike messages.** How many messages came from lookalike domains? *Rubric:* 3 = 23;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX034 — Edit distance.** What does edit distance count? *Rubric:* 3 = single-character changes between strings;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX035 — Payment rule.** What is the payment change rule? *Rubric:* 3 = confirm by calling a known number;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 12)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Backup, ransomware and recovery

### Learning outcomes

You will (1) design backups resistant to ransomware; (2) test recovery against objectives; (3) plan clinic continuity.

### 8.1 Backup design

Moorfield backs up the patient record system nightly to a server in head office, reachable from the same network. Elena recognises that ransomware could encrypt both. She adds immutable copies held by a backup provider for thirty days, which cannot be deleted even by Moorfield administrators. She also separates backup administration credentials from everyday administrator accounts. Dr. Qureshi notes that ransomware groups often target backups first, so backups must be designed against deliberate attack, not just accidents. The board approves the provider's annual cost.

### 8.2 Recovery objectives

Elena agrees objectives with the clinical lead and operations director, consistent with the board's appetite. The patient record system must return within four hours and lose no more than one hour of data. Imaging must return within one day; clinics can continue with paper notes meanwhile. Email can wait a day. She learns that objectives must be agreed with those who bear the consequences, because technical teams alone tend to underestimate or overestimate the urgency. The objectives are recorded in the recovery plan and signed by both managers.

### 8.3 Testing

Elena tests a full restore of the patient record system into an isolated environment. The restore succeeds but takes six hours, missing the four-hour objective, mostly because the database is copied slowly from the provider. She arranges a faster recovery option: a recent snapshot kept locally on immutable storage. A second test completes in three hours. She learns that only timed tests reveal whether objectives are achievable. She records both test timelines step by step and adds the local snapshot procedure to the recovery runbook, so any member of the central team can follow it.

### 8.4 Clinic continuity

Elena works with clinic managers on continuity plans for system outages: printed appointment lists each evening, paper clinical notes with later entry and emergency contact details for patients with appointments. A clinic trials the plan during a planned system upgrade and identifies that paper consent forms were missing. The forms are added. Dr. Qureshi notes that continuity planning keeps patient care going while technical recovery happens. Each clinic keeps a small continuity box containing printed forms, the latest appointment list and contact numbers, and clinic managers check its contents every month.

### Worked example

Elena adds thirty-day immutable backups and separate credentials, agrees recovery objectives, improves a six-hour restore to three hours and trials clinic paper fallbacks.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

Backups reachable with everyday administrator credentials can be destroyed by ransomware.

### Exercises

- **EX036 — Immutable period.** How long are immutable copies held? *Rubric:* 3 = thirty days;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX037 — Record objectives.** What are the patient record objectives? *Rubric:* 3 = four hours, one hour of data;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — First test.** How long did the first restore take? *Rubric:* 3 = six hours;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX039 — Second test.** How long did the second test take? *Rubric:* 3 = three hours;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX040 — Missing forms.** What was missing in the continuity trial? *Rubric:* 3 = paper consent forms;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 12)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Incident response and notification

### Learning outcomes

You will (1) build an incident response process for a multi-site organisation; (2) meet notification obligations; (3) learn from incidents.

### 9.1 Process

Elena writes Moorfield's incident process. Any staff member can report through a single phone number or email address. The central team assesses severity using a short table. Serious incidents trigger an incident lead, a communications contact and notification to the operations director. The process covers containment, investigation, recovery and closure. She aligns it with the Respond and Recover functions of the NIST Cybersecurity Framework 2.0. Dr. Qureshi advises keeping the process short enough to use under pressure. The process fits on two pages with a severity table.

### 9.2 Notification

Health data breaches may require notification to regulators and patients within strict deadlines under data protection law, which varies by country. Elena works with Moorfield's data protection officer to define who decides whether notification is needed and how evidence is collected quickly. Cyber insurance also requires prompt notice. She adds a checklist so these obligations are considered early, rather than discovered after deadlines have passed. The data protection officer approves the checklist, and Elena prints it on the back of the incident process so both are always together. The insurer's notification number is added to the first page.

### 9.3 Exercise

Elena runs an exercise: a clinic receptionist reports that patients are receiving texts asking for payment to an unfamiliar account, apparently from Moorfield. Participants trace the cause to a compromised account at the text messaging supplier. They discover Moorfield's contract does not require the supplier to notify incidents promptly. Elena adds this to the supplier review. Dr. Qureshi notes that exercises often reveal supplier gaps, because suppliers are rarely included in planning. The operations director contacts the supplier the following week to agree new terms.

### 9.4 Learning

After each real incident, Elena holds a short blameless review: what happened, why controls did not stop it, what worked and what will change. She tracks actions to completion. Over a year, reviews lead to improvements in mail filtering, supplier contracts and locum account expiry. She learns that incidents are expensive lessons, and that recording and acting on them is how an organisation gets value from the cost. She keeps a log of reviews and actions, and the security committee checks progress on open actions at every monthly meeting.

### Worked example

Elena writes a short multi-site incident process aligned with CSF 2.0 Respond and Recover, adds a notification checklist, runs a supplier-related exercise and holds blameless reviews.

> **Synthetic case.** Incidents are synthetic; notification rules vary by country.

### Errors and limits

Discovering notification deadlines late can turn an incident into a regulatory breach.

### Exercises

- **EX041 — Report channel.** How do staff report incidents? *Rubric:* 3 = a single phone number or email address;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX042 — CSF alignment.** Which CSF 2.0 functions guide the process? *Rubric:* 3 = Respond and Recover;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX043 — Notification partner.** Who helps decide on notification? *Rubric:* 3 = the data protection officer;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX044 — Exercise gap.** What gap did the exercise reveal? *Rubric:* 3 = supplier not required to notify promptly;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX045 — Review outcome.** Name one improvement from reviews. *Rubric:* 3 = locum account expiry;; 2 = one;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 12)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Metrics, reporting and the board

### Learning outcomes

You will (1) choose measures linked to risks; (2) report to a non-specialist board; (3) use measures to drive decisions.

### 10.1 Measures

Elena selects six measures linked to top risks: critical patch compliance by clinic, multi-factor enrolment, quarantined lookalike messages, timed recovery test results, former-staff accounts found in reviews and incidents by type. Each has a definition, source, owner and target. She avoids counts that only look impressive, such as blocked connections. Dr. Qureshi notes that each measure should answer a question the board would ask. She writes each definition in the measure handbook, and the central team tests that the figures can be produced from existing systems each month without manual effort.

### 10.2 Baselines

Elena uses her course work as baselines: patch compliance of 90.6 percent with three clinics far lower, four lookalike domains in the synthetic mail sample, a six-hour first restore and several former staff accounts in the first review. She shows improvement since: clinic patch compliance above ninety percent, quarantining in place and a three-hour restore. Baselines make progress visible to the board. She shows both the baseline and the latest value for each measure in a simple table, so the board can see where progress has been made and where work remains, including the imaging exceptions still open.

### 10.3 Board report

Elena designs a two-page quarterly report. Page one shows the six measures with trend arrows and a sentence on each. Page two lists top risks, changes since last quarter and decisions needed. The board asks fewer technical questions and more about priorities and resources. One partner asks why imaging computers remain exceptions, prompting a decision to pressure the supplier jointly with other dental groups. The board decides to contact two other dental groups that use the same imaging software and send a joint request to the supplier for an updated, supported version.

### 10.4 Driving decisions

Measures matter when they change decisions. Elena shows how the clinic patch measure led to support for three clinics and how the restore test led to the local snapshot. She proposes stopping a measure that never changes decisions. Dr. Qureshi notes that measurement systems should be pruned as well as grown, so attention stays on what matters. The committee agrees to stop reporting the number of quarantined messages to the board, keeping it as an internal measure for the central team, because it rose and fell with attacker activity rather than with anything Moorfield controlled.

### Worked example

Elena links six measures to risks, uses course results as baselines, writes a two-page board report and shows how measures changed decisions.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Measures that never change decisions waste attention.

### Exercises

- **EX046 — Measure count.** How many measures does Elena select? *Rubric:* 3 = six;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX047 — Avoided count.** Which count does Elena avoid? *Rubric:* 3 = blocked connections;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX048 — Report length.** How long is the board report? *Rubric:* 3 = two pages;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX049 — Imaging decision.** What decision follows the imaging question? *Rubric:* 3 = pressure the supplier jointly with other groups;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX050 — Pruning.** What does Elena propose for unused measures? *Rubric:* 3 = stop them;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 12)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Capstone project

### Learning outcomes

You will (1) define a capstone improvement project; (2) deliver it with evidence; (3) evaluate results against goals.

### 11.1 Choosing the project

Elena's capstone addresses the risk the board ranked highest: ransomware. Her project combines three improvements already started: clinic patching support, immutable backups with faster recovery and multi-factor authentication for all accounts. The goal is that Moorfield can show, with evidence, that a ransomware attack would be harder to start, slower to spread and faster to recover from. Dr. Qureshi approves the project and asks for clear success criteria. She writes a one-page project charter with scope, timeline and criteria, approved by the operations director.

### 11.2 Success criteria

Elena sets criteria: critical patch compliance at least ninety-five percent overall and ninety percent in every clinic; multi-factor authentication for every account with documented exceptions; immutable backups for all critical systems; and a timed recovery of the patient record system within four hours. Each criterion has a measure and evidence source. She learns that clear criteria make capstone evaluation straightforward and honest. She lists the criteria in a table with the measure, the data source and the date by which each will be checked. The operations director and the clinical lead sign the table.

### 11.3 Delivery

Over four months, Elena delivers the improvements. Patch compliance rises above ninety-five percent overall, though one clinic remains at ninety-two percent because of an imaging exception. Multi-factor enrolment reaches all staff accounts, with two service account exceptions documented. Immutable backups cover all critical systems. A final timed recovery completes in three hours and ten minutes. She records evidence for each. She keeps a project log recording the date each milestone was reached and the evidence stored for it. The log, with links to evidence, forms an appendix to her capstone report.

### 11.4 Evaluation

Elena evaluates honestly. Three criteria are met; the per-clinic patch criterion is narrowly missed in one clinic, with a clear reason and plan. She notes that the project shows improvement in preparation, but cannot prove Moorfield would withstand a real attack. She recommends an independent test of incident response within the next year. Dr. Qureshi praises the honest evaluation as the most important part. She presents the evaluation in a table showing each criterion, the result and whether it was met, with the reason for the missed criterion stated beside it.

### Worked example

Elena defines a ransomware capstone with four criteria, delivers patching, MFA, immutable backups and a three-hour ten-minute recovery and evaluates one criterion as narrowly missed.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Claiming a project proves resilience against real attacks overstates evidence.

### Exercises

- **EX051 — Capstone risk.** Which risk does the capstone address? *Rubric:* 3 = ransomware;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX052 — Clinic criterion.** What is the per-clinic patch criterion? *Rubric:* 3 = at least ninety percent in every clinic;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX053 — Missed criterion.** Which criterion is narrowly missed? *Rubric:* 3 = per-clinic patch compliance;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX054 — Final recovery.** How long did the final recovery take? *Rubric:* 3 = three hours ten minutes;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX055 — Next step.** What does Elena recommend next? *Rubric:* 3 = an independent incident response test;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 12)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Capstone presentation and next steps

### Learning outcomes

You will (1) present a capstone to examiners and a board; (2) answer challenges; (3) plan continued improvement.

### 12.1 Presentation

Elena presents her capstone to Dr. Qureshi, an external examiner and Moorfield's board. She covers the risk, criteria, delivery, evidence and evaluation in twenty minutes, with backup slides showing data. She uses the board's language: clinics able to treat patients and patient records protected. Dr. Qureshi had advised her to lead with the business outcome and keep technical detail for questions. She rehearses twice with colleagues from the course, who ask her to shorten the introduction and move one chart forward. She also prepares a one-page handout summarising the criteria and results for board members.

### 12.2 Challenges

The external examiner asks whether patch compliance measures exposure accurately when imaging computers are excluded by exception. Elena explains the isolation controls and shows exception records, accepting that exposure remains. A partner asks about cost; she shows that most improvements used existing licences and staff time, with the backup provider as the main new cost. Both answers are clear and evidence-based. The examiner also asks how she would know if the improvements decayed over time, and she points to the quarterly measures and the yearly recovery test.

### 12.3 Outcome

Elena passes the capstone with distinction. The board adopts her measures as standing quarterly reporting and approves an independent incident response test. Elena reflects that the course gave her frameworks to organise what she already knew and the confidence to present security as a business matter. She notes that her relationships with clinic managers improved as they saw problems solved rather than blamed. Clinic managers send a short message thanking the central team for the patching support. Dr. Qureshi asks her permission to use the capstone as an example for future students.

### 12.4 Next steps

Elena plans next steps: the independent test, a review of the risk assessment in a year and preparing for possible ISO/IEC 27001 certification, which large insurers have begun to request. She also plans to mentor a junior team member through the same methods. The next course in this area, data governance, examines how decisions about data ownership, quality and use are made, which complements the security programme she has built. The board asks her to present a certification readiness plan within six months.

### Worked example

Elena presents her capstone in business terms, answers challenges on imaging exceptions and cost, passes with distinction and plans certification readiness.

> **Synthetic case.** The presentation is synthetic.

### Errors and limits

Leading with technical detail loses a board audience.

### Exercises

- **EX056 — Board language.** What language does Elena use for the board? *Rubric:* 3 = clinics able to treat patients;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX057 — Main new cost.** What was the main new cost? *Rubric:* 3 = the backup provider;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX058 — Capstone result.** What result does Elena achieve? *Rubric:* 3 = distinction;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX059 — Board adoption.** What does the board adopt? *Rubric:* 3 = Elena's measures as quarterly reporting;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX060 — Certification driver.** Why consider ISO/IEC 27001 certification? *Rubric:* 3 = insurers have begun to request it;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 12)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Elena Petrova, Dr. Hamid Qureshi, Thornbury Business School, Moorfield Dental Group and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Twenty-two clinics.

**EX002.** Four people, led by Elena.

**EX003.** Patch delays in small clinics.

**EX004.** Frameworks, measurement methods and board communication skills.

**EX005.** A board-approved programme document.

**EX006.** Elena, the operations director and a clinical lead.

**EX007.** Records showing the activities happen consistently.

**EX008.** No clinic unable to treat patients for more than half a day.

**EX009.** The dental laboratory, treated as a supplier.

**EX010.** ISO/IEC 27000:2026.

**EX011.** Ransomware.

**EX012.** When ratings differ by more than one point.

**EX013.** Patch delays and weak recovery testing.

**EX014.** Access reviews and alerts on unusual record viewing.

**EX015.** Cyber insurance.

**EX016.** Imaging computers bought directly by dentists.

**EX017.** Imaging suppliers have not certified newer versions.

**EX018.** Patient clinical records, images and payment data.

**EX019.** Individual accounts, multi-factor authentication and session-only access.

**EX020.** The clinical lead.

**EX021.** 513 of 566 devices, 90.6 percent.

**EX022.** C19, with 10 of 20 devices, 50.0 percent.

**EX023.** They rely on a part-time local IT contact.

**EX024.** To lunchtime with automatic restarts outside appointments.

**EX025.** By isolating them on a separate segment with restricted access.

**EX026.** Appointments and contact details, not clinical notes.

**EX027.** The clinical lead, through a weekly report.

**EX028.** Locum dentists whose contracts ended.

**EX029.** Hardware security keys.

**EX030.** Through a managed gateway with multi-factor authentication and recorded sessions.

**EX031.** 5,823 messages.

**EX032.** Four domains.

**EX033.** 23 messages.

**EX034.** The single-character changes needed to turn one domain into another.

**EX035.** Always confirm by calling a known number.

**EX036.** Thirty days.

**EX037.** Return within four hours and lose no more than one hour of data.

**EX038.** Six hours.

**EX039.** Three hours.

**EX040.** Paper consent forms.

**EX041.** Through a single phone number or email address.

**EX042.** Respond and Recover.

**EX043.** The data protection officer.

**EX044.** The supplier contract did not require prompt incident notification.

**EX045.** Locum account expiry.

**EX046.** Six measures.

**EX047.** Blocked connections.

**EX048.** Two pages.

**EX049.** To pressure the supplier jointly with other dental groups.

**EX050.** Stopping measures that never change decisions.

**EX051.** Ransomware, the board's highest-ranked risk.

**EX052.** At least ninety percent in every clinic.

**EX053.** The per-clinic patch compliance criterion.

**EX054.** Three hours and ten minutes.

**EX055.** An independent test of incident response.

**EX056.** Clinics able to treat patients and patient records protected.

**EX057.** The backup provider.

**EX058.** A pass with distinction.

**EX059.** Her measures as standing quarterly reporting.

**EX060.** Large insurers have begun to request it.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
