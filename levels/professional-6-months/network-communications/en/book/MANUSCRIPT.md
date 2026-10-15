# Network and Communications Security: Professional Course

- Language: English (`en`); course 034, Professional course (6 months).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working IT professionals moving into network security who need practical, supervised skills in review, triage, investigation and reporting.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one IT support professional, mentored by a senior engineer, reviewing the network security of a three-office law firm, from foundations, context and authorised evidence handling through design and rule review, alert triage, operational workflow, change review, a supervised investigation, reporting, troubleshooting, a baseline lab and a final portfolio. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Grace Whitfield** | Professional learner | Invented |
| **Sam Adeyemi** | Mentor | Invented |
| **Northgate Professional Academy** | Fictional academy | Invented |
| **Oakline Legal** | Fictional partner (three offices) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) state core security goals in practice; (2) describe the practitioner's role; (3) set up a working approach for the course.

### 1.1 The practitioner setting

Grace Whitfield has worked for eight years in IT support and joins a six-month professional course at the fictional Northgate Professional Academy to move into network security. Her mentor is Sam Adeyemi, a senior network engineer. The course uses a running case: the fictional Oakline Legal, a law firm with three offices, 140 staff, client case files that must stay confidential and a small IT team that has asked for help reviewing its network security. Grace's work is supervised and uses synthetic data in labs, with any real-system activity approved in advance.

### 1.2 Goals in practice

Confidentiality, integrity and availability take concrete forms at a law firm. Confidentiality means case files are seen only by the lawyers working on them and never by guests or other clients. Integrity means documents and emails are not altered, since altered evidence or instructions could harm a case. Availability means lawyers can reach files and email before court deadlines. Grace learns to express every security task in these terms, because managers and partners understand business consequences more readily than technical descriptions of protocols and ports.

### 1.3 What practitioners do

Network security practitioners review designs and rule changes, monitor alerts and logs, investigate unusual activity, maintain secure configurations and explain risks to others. Much of the work is routine: checking that changes are safe, that certificates are current and that alerts are handled. Some is reactive, such as investigating a suspicious login. Grace notes that her support background helps: she already understands users, tickets and the cost of disruption, which are central to doing security work that people accept. She records which tasks are routine and which reactive.

### 1.4 Working approach

Sam sets out a working approach for the course. Every task starts by confirming scope and authorisation, uses evidence rather than assumptions, makes the smallest effective change, verifies the result and records what was done. Grace keeps a practice log of tasks, decisions and lessons, which becomes part of her final portfolio. The approach is simple, but following it consistently prevents most of the mistakes that cause security work to disrupt services or miss real problems. Sam checks her log weekly and comments on each decision, which keeps the approach honest.

### 1.5 Sources of guidance

Practitioners rely on trusted guidance rather than opinion. Grace's reference list includes NIST SP 800-41r1 for firewall policy, SP 800-94 for intrusion detection, SP 800-77r1 for IPsec VPNs, SP 800-52r2 for TLS, SP 800-153 for wireless and the CIS Controls for prioritised safeguards. She learns to cite the specific guidance behind a recommendation, which makes recommendations easier to accept and to check, and protects her from appearing to impose personal preferences on an experienced IT team. She keeps the documents in a shared folder for quick reference.

### Worked example

Grace's first log entry records the Oakline scope, her approach and the five guidance documents she will use.

> **Synthetic case.** Oakline Legal and all data are synthetic.

### Errors and limits

Describing risks only in technical terms makes it harder for managers to act.

### Exercises

- **EX001 — Law firm integrity.** Give an integrity concern specific to a law firm. *Rubric:* 3 = altered documents or instructions harming a case;; 2 = altered files;; 1 = generic;; 0 = none.
- **EX002 — Approach steps.** List the five steps of Sam's working approach. *Rubric:* 3 = scope, evidence, smallest change, verify, record;; 2 = four;; 1 = fewer;; 0 = none.
- **EX003 — Support background value.** How does Grace's support background help? *Rubric:* 3 = understands users, tickets and disruption cost;; 2 = users;; 1 = vague;; 0 = none.
- **EX004 — Citing guidance.** Why cite specific guidance for recommendations? *Rubric:* 3 = easier to accept and check, not personal preference;; 2 = credibility;; 1 = required;; 0 = none.
- **EX005 — Availability example.** Give an availability need at Oakline. *Rubric:* 3 = reaching files and email before court deadlines;; 2 = deadlines;; 1 = generic;; 0 = none.

### Synthesis

Practitioners translate security goals into business terms and follow a consistent, evidence-based approach.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Network and communications security: service and stakeholder context

### Learning outcomes

You will (1) map Oakline's services and users; (2) identify stakeholders and their concerns; (3) prioritise risks in context.

### 2.1 Services and users

Grace maps Oakline's services with the IT team: a document management system holding case files, email in the cloud, a practice management system for billing, printing and scanning, guest wireless in reception and meeting rooms, and a VPN for lawyers working from home or court. Each office has a firewall, and the offices connect by site-to-site VPN. She lists which user groups use each service: lawyers, support staff, finance, IT and guests. This map becomes the basis for every later check.

### 2.2 Stakeholders

Different people care about different things. Partners care about client confidentiality and reputation. Lawyers care about fast access, especially near deadlines. The finance director cares about billing systems and cost. The IT manager, Priyanka Shah, cares about workload and reliability. The compliance officer cares about regulatory obligations and evidence. Grace meets each briefly, asking what would be the worst outcome for them. Their answers shape her priorities and help her explain recommendations in terms each stakeholder values. She records each answer in her practice log.

### 2.3 Client confidentiality

Law firms hold information that clients trust them to protect, and some matters are highly sensitive. Oakline already restricts some case files to named lawyers inside the document system. Grace checks whether the network supports this: can guest devices reach the document system, can any office device reach its management interface, and are connections encrypted? She finds that guest wireless at one office shares a network with printers that are also used for confidential documents, a gap she records for review.

### 2.4 Prioritising in context

Grace ranks risks by likelihood and impact in Oakline's context. Guest access near confidential printing is likely and serious, so it ranks high. Weak VPN authentication for lawyers working remotely ranks high because remote access is a common target. Outdated printer firmware ranks medium. She discusses the ranking with Priyanka, who adds that the firm's insurer has asked about multi-factor authentication, raising its priority further. Context changes priorities, so rankings must be agreed with people who know the business. The agreed ranking is dated and filed.

### 2.5 Recording context

Grace writes a two-page context summary: services, users, stakeholders, constraints and the top five risks. Constraints include a small IT team, busy periods before court dates and a requirement that changes avoid working hours. The summary is reviewed by Priyanka and Sam. Writing context down keeps later work focused and lets others check that recommendations fit the firm. It also helps when new people join the work, because they can understand the setting quickly. The summary is updated whenever services, stakeholders or constraints change during the engagement.

### Worked example

The context summary lists six services, five stakeholder groups, three constraints and five ranked risks.

> **Synthetic case.** The firm and people are synthetic.

### Errors and limits

Ranking risks without the business's input misses factors such as insurer requirements.

### Exercises

- **EX006 — Worst outcome question.** What did Grace ask each stakeholder? *Rubric:* 3 = the worst outcome for them;; 2 = worst case;; 1 = their job;; 0 = none.
- **EX007 — Printer gap.** What gap did Grace find at one office? *Rubric:* 3 = guest wireless shares network with confidential printers;; 2 = guest-printer;; 1 = vague;; 0 = none.
- **EX008 — Insurer effect.** How did the insurer affect priorities? *Rubric:* 3 = asked about MFA, raising its priority;; 2 = MFA up;; 1 = vague;; 0 = none.
- **EX009 — Change constraint.** Name one constraint on changes at Oakline. *Rubric:* 3 = avoid working hours or busy court periods;; 2 = one;; 1 = vague;; 0 = none.
- **EX010 — Context summary purpose.** Why write the context summary down? *Rubric:* 3 = focus, checking fit, onboarding others;; 2 = focus;; 1 = formality;; 0 = none.

### Synthesis

Understanding services, stakeholders and constraints grounds network security work in the organisation's needs.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) work within written authorisation; (2) handle evidence and confidential data; (3) maintain chain of custody.

### 3.1 Written authorisation

Before reviewing anything at Oakline, Grace receives a written authorisation from the IT manager and a partner. It lists what she may review (firewall and VPN configurations, logs and wireless settings, all exported by the IT team), what she may not do (access case files, test live systems or contact clients) and the reporting route for findings. If a task needs anything outside the authorisation, she stops and asks. Written authorisation protects the firm, the academy and Grace from misunderstandings.

### 3.2 Confidential data

Logs and configurations at a law firm can reveal client names, matter numbers and lawyers' movements. Grace receives only sanitised exports where possible, with client identifiers removed by the IT team. Files are stored on the academy's encrypted storage, accessed only by Grace and Sam, and deleted at the end of the engagement. She never copies files to personal devices or shares them in chat tools. These measures meet both the firm's confidentiality duties and data protection obligations. Sam confirms these arrangements before files arrive.

### 3.3 Handling evidence

When Grace finds something important, such as an unusual login pattern, she preserves the evidence: the original log extract, the time she obtained it, who provided it and a SHA-256 digest of the file so any later change can be detected. She works on copies, leaving originals untouched. This discipline matters if a finding later becomes part of an incident investigation or a disciplinary matter, where the reliability of evidence may be questioned. Copies are clearly labelled as working copies, and the originals are stored read-only with their digests alongside.

### 3.4 Chain of custody

A chain of custody records who held evidence, when and why, from collection to final use. Grace keeps a simple custody log for each evidence item: received from whom, stored where, accessed by whom and transferred to whom. For most review work, this is light-touch, but the habit means she is ready if a matter escalates. Courts and regulators place weight on evidence whose handling can be shown, and a law firm, of all organisations, values such care. Entries are dated and signed off by Sam.

### 3.5 Reporting findings

Findings go through the agreed route: to Priyanka first, with urgent issues reported by phone the same day. Grace states facts, evidence and recommended actions, and avoids speculation about who might be responsible. If she accidentally sees confidential client data, she reports that too. Honest, prompt, discreet reporting is a core professional behaviour; it lets the firm act quickly and preserves trust in the person doing the review. Each report is logged with its date, recipient and the response received, so follow-up actions can be tracked until they are closed.

### Worked example

Grace's evidence log for one unusual login includes source, time, digest and two custody entries.

> **Synthetic case.** Evidence is synthetic.

### Errors and limits

Working on original evidence files risks altering them and weakening their reliability.

### Exercises

- **EX011 — Not permitted.** Name two activities outside Grace's authorisation. *Rubric:* 3 = access case files, test live systems, contact clients;; 2 = two;; 1 = one;; 0 = none.
- **EX012 — Digest purpose.** Why record a digest of an evidence file? *Rubric:* 3 = detect later changes;; 2 = integrity;; 1 = encryption;; 0 = none.
- **EX013 — Custody log contents.** What does the custody log record? *Rubric:* 3 = who held evidence, when, where, why;; 2 = holders;; 1 = vague;; 0 = none.
- **EX014 — Urgent finding route.** How are urgent findings reported? *Rubric:* 3 = phone to IT manager same day;; 2 = phone;; 1 = email later;; 0 = none.
- **EX015 — Accidental exposure.** What should Grace do if she sees client data by accident? *Rubric:* 3 = report it;; 2 = report;; 1 = ignore;; 0 = none.

### Synthesis

Authorisation, careful data handling and documented custody make practitioner work trustworthy.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Network and communications security: core methods

### Learning outcomes

You will (1) review a network design; (2) check rules against needed flows; (3) assess remote access.

### 4.1 Design review

Grace reviews Oakline's network design. Each office has staff, printers, servers (main office only), guest and management networks, separated by the office firewall. The design is sound in principle, but she checks details: whether guest networks are truly isolated, whether management interfaces are reachable only from IT workstations and whether rules between networks match needs. Reviews compare the design with good practice and with what is actually configured, since the two often differ over time. She also asks the IT team which parts of the design they find hardest to run, since operational difficulty often predicts future drift.

### 4.2 Needed flows

Grace and Priyanka list the flows Oakline needs between networks: staff to document and practice management systems, staff to printers, remote lawyers to the same systems via VPN, servers to update services and IT workstations to management interfaces. Anything else between internal networks should be denied, following the default-deny approach in NIST SP 800-41r1. The list is short, and each entry has an owner. This list is the yardstick for reviewing the rules. Priyanka confirms each owner, and any flow without a willing owner is questioned before it is allowed to stay.

### 4.3 Rule review

Comparing rules with the list, Grace finds three issues. A rule allows any staff device to reach the server management network, added once for a project. A rule allows guest wireless at one office to reach printers, explaining the gap seen earlier. A temporary rule for a supplier, added a year ago, has no expiry. She recommends removing the first two and setting an expiry or removing the third after asking its owner. Each issue is tied to evidence from the exported configuration.

### 4.4 Remote access

Lawyers work from home, client sites and court. Grace reviews the VPN: it uses IKEv2 with certificates for the site-to-site links, but remote access uses passwords only, without a second factor. She recommends multi-factor authentication for remote access, consistent with the insurer's request and widely recommended practice, and restricting remote users to the systems they need. She also checks that the VPN gateway's TLS settings for its web portal follow SP 800-52r2. She also checks that remote sessions time out after inactivity, so unattended laptops at court do not stay connected.

### 4.5 Presenting the review

Grace presents her review as a short table: finding, evidence, risk, recommendation and owner. She leads with the two highest risks: guest access to printers and remote access without a second factor. She acknowledges strengths, such as the sound zone structure and certificate-based site links. Balanced reviews are easier to accept than lists of faults, and they show the IT team that the reviewer understands what they have done well. She sends the table to Priyanka a day before the meeting, so questions can be prepared and the meeting spent on decisions rather than reading.

### Worked example

The review finds three rule issues and one remote access gap, each with evidence and an owner.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Reviewing only the design document without the actual configuration misses drift.

### Exercises

- **EX016 — Review comparison.** What two things does a design review compare? *Rubric:* 3 = design with good practice and with actual configuration;; 2 = both;; 1 = one;; 0 = none.
- **EX017 — Rule issues.** List the three rule issues found. *Rubric:* 3 = staff to server management, guest to printers, supplier rule without expiry;; 2 = two;; 1 = one;; 0 = none.
- **EX018 — Remote access gap.** What remote access gap did Grace find? *Rubric:* 3 = passwords only, no second factor;; 2 = no MFA;; 1 = vague;; 0 = none.
- **EX019 — Review table columns.** List the review table's columns. *Rubric:* 3 = finding, evidence, risk, recommendation, owner;; 2 = four;; 1 = fewer;; 0 = none.
- **EX020 — Acknowledging strengths.** Why include strengths in the review? *Rubric:* 3 = easier acceptance, shows understanding;; 2 = balance;; 1 = politeness;; 0 = none.

### Synthesis

Comparing design, configuration and needed flows finds real gaps and supports balanced recommendations.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Network and communications security: tools and interpretation

### Learning outcomes

You will (1) interpret alerts and logs; (2) prioritise alerts by severity and asset value; (3) avoid common misreadings.

### 5.1 Reading alerts

Oakline's firewalls and email service produce alerts. Each alert has a type, severity, affected asset and time. Grace learns that severity set by a tool reflects the type of event, not the importance of the asset involved. A medium-severity alert on the document system may matter more than a high-severity alert on a guest phone. Interpreting alerts means combining the tool's view with knowledge of the organisation, which is exactly the judgement practitioners add. She writes down, for each alert type, which assets make it urgent and which make it routine.

### 5.2 Asset criticality

Grace and Priyanka rate assets by how much harm their compromise would cause: case files and email high, laptops medium, guest wireless and printers low. Combining severity with criticality gives a simple priority score. NIST SP 800-94 notes that intrusion detection outputs need tuning and context to be useful. A score is not a perfect measure, but it gives consistent ordering, so the most important alerts are looked at first when there are more alerts than time. The ratings are reviewed with Priyanka every six months.

### Lab — Alert triage

```python
"""Rank synthetic alerts by severity times asset criticality (stdlib only)."""
crit = {"case-files": 3, "email": 3, "laptop": 2, "guest-wifi": 1, "printer": 1}
alerts = [("A1", "laptop", 2, "malware callback blocked"), ("A2", "guest-wifi", 3, "port sweep from guest"),
          ("A3", "case-files", 3, "admin login from new country"), ("A4", "printer", 1, "firmware outdated"),
          ("A5", "email", 2, "mass forwarding rule created"), ("A6", "laptop", 1, "VPN login failure")]
ranked = sorted(alerts, key=lambda a: (-a[2] * crit[a[1]], a[0]))
for aid, asset, sev, txt in ranked: print(f"{aid} score {sev*crit[asset]}  {asset:11}{txt}")
```

Run with `python3 lab_triage.py`. Verified output:

```text
A3 score 9  case-files admin login from new country
A5 score 6  email      mass forwarding rule created
A1 score 4  laptop     malware callback blocked
A2 score 3  guest-wifi port sweep from guest
A6 score 2  laptop     VPN login failure
A4 score 1  printer    firmware outdated
```

### 5.3 Reading the ranking

The synthetic ranking puts an administrator login from a new country on the case files system first, with score nine, and a new mass email forwarding rule second, with score six. Both suggest possible account compromise affecting confidential data, so they deserve immediate attention. A blocked malware callback on a laptop scores four: important, but the block suggests the firewall did its job, and the laptop should be checked. The guest port sweep, VPN failure and printer firmware rank lower and can wait for routine review.

### 5.4 Common misreadings

Grace notes misreadings to avoid. Treating a blocked event as harmless ignores the infected device behind it. Treating every alert from a high-value system as an incident creates panic. Assuming an alert is false because it was false last time misses the one time it is real. And reading times in different time zones without converting causes confusion about sequence. She adds these to her practice log as a checklist for future triage sessions. She converts all times to UTC before comparing events from different systems, and notes the conversion.

### Worked example

The triage ranks six alerts; the top two indicate possible account compromise on high-value systems.

> **Synthetic case.** Alerts are synthetic.

### Errors and limits

Ranking alerts by tool severity alone overweights low-value assets.

### Exercises

- **EX021 — Top alert.** Which alert ranks first, and why? *Rubric:* 3 = admin login from new country on case files, score 9;; 2 = A3;; 1 = A2;; 0 = none.
- **EX022 — Forwarding rule.** Why is a mass email forwarding rule concerning? *Rubric:* 3 = possible compromise leaking email;; 2 = compromise;; 1 = vague;; 0 = none.
- **EX023 — Blocked event.** Why does a blocked malware callback still need action? *Rubric:* 3 = infected device remains;; 2 = infection;; 1 = vague;; 0 = none.
- **EX024 — Severity limit.** Why is tool severity not enough to prioritise? *Rubric:* 3 = ignores asset importance;; 2 = context;; 1 = accurate;; 0 = none.
- **EX025 — Time zone misreading.** What misreading do time zones cause? *Rubric:* 3 = confused event sequence;; 2 = order;; 1 = vague;; 0 = none.

### Synthesis

Combining severity with asset criticality and careful reading focuses attention where harm would be greatest.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Network and communications security: operational workflow

### Learning outcomes

You will (1) run daily and weekly security routines; (2) manage tickets; (3) escalate appropriately.

### 6.1 Daily routine

Grace drafts a daily routine for Oakline's IT team: review overnight high-priority alerts, check that VPN tunnels between offices are up, confirm logs arrived from each firewall and glance at the help desk queue for access problems that might signal blocked needs or misuse. The routine takes about fifteen minutes. A short, fixed routine ensures important signals are seen every day, even when the team is busy with other work. Anything unusual becomes a ticket so it is tracked to completion rather than remembered informally.

### 6.2 Weekly routine

Weekly tasks include reviewing denied connections by network pair, checking certificates expiring within sixty days, reviewing temporary rules approaching expiry, and checking accounts for leavers. Grace builds a checklist with expected times and a place to record results. Records show that checks happened and make trends visible over weeks. A weekly routine catches slower problems, such as gradually rising denies, that daily glances miss. The checklist is kept in the ticket system so that missed weeks are visible to Priyanka, and results from previous weeks can be compared easily.

### 6.3 Ticket workflow

Security work at Oakline flows through the help desk system. Grace defines ticket categories: alert investigation, rule change request, access request and security question. Each category has a target response time and an owner. Alert investigations record what was checked, the conclusion and any follow-up. Using the existing ticket system rather than a separate tool keeps work visible to the whole IT team and fits how they already work. Priyanka reviews overdue security tickets every Friday, so investigations do not quietly stall.

### 6.4 Escalation

Some situations need more than routine handling. Grace writes escalation criteria: suspected compromise of an account with access to case files, evidence of data leaving the firm, or loss of service affecting court deadlines. Escalation goes to the IT manager and, for confidentiality incidents, the compliance officer, who decides on client and regulatory notifications. Clear criteria prevent both delay, when people hesitate to escalate, and panic, when everything is treated as an emergency. The criteria are printed beside the IT team's desks and included in the daily routine.

### 6.5 Handover between shifts

Oakline's IT team works staggered hours. Grace adds a short handover note at the end of each day: open investigations, changes made and anything to watch. Handover notes prevent issues falling between people and reduce repeated work. They are kept in the ticket system so they remain searchable. Small habits like handover notes make a team's security work reliable without adding significant effort. Grace provides a three-line template: open items, changes made today and things to watch tomorrow. The template keeps notes short enough that people actually write them.

### Worked example

The daily routine takes fifteen minutes; the weekly checklist has four items; three escalation criteria are agreed.

> **Synthetic case.** Routines are synthetic.

### Errors and limits

Without escalation criteria, serious events wait in the routine queue.

### Exercises

- **EX026 — Daily checks.** List three daily routine checks. *Rubric:* 3 = alerts, tunnels, log arrival or help desk queue;; 2 = two;; 1 = one;; 0 = none.
- **EX027 — Weekly value.** What do weekly checks catch that daily ones miss? *Rubric:* 3 = slow trends like rising denies;; 2 = trends;; 1 = vague;; 0 = none.
- **EX028 — Ticket system reuse.** Why use the existing ticket system? *Rubric:* 3 = keeps work visible and fits current practice;; 2 = visibility;; 1 = cheaper;; 0 = none.
- **EX029 — Escalation criterion.** Give one escalation criterion. *Rubric:* 3 = suspected compromise of case-file account, data leaving, deadline outage;; 2 = one;; 1 = vague;; 0 = none.
- **EX030 — Compliance role.** Who decides on client and regulatory notifications? *Rubric:* 3 = compliance officer;; 2 = compliance;; 1 = IT;; 0 = none.

### Synthesis

Short routines, a clear ticket workflow and defined escalation make security operations dependable.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Network and communications security: controls and verification

### Learning outcomes

You will (1) review firewall change requests; (2) apply review criteria; (3) verify implemented changes.

### 7.1 Why review changes

Most firewall weaknesses come from changes made over time rather than the original design. A rule added for a project, a supplier or an urgent problem can widen access far beyond its need. Grace proposes that every rule change request is reviewed against simple criteria before approval. Wool's 2004 study of firewall configurations found errors common and increasing with rule base complexity, which supports reviewing each change rather than relying on occasional audits. Reviewing each change also spreads knowledge of the rule base across the team.

### 7.2 Review criteria

Grace's criteria are: the rule is specific, naming source, destination and service rather than "any"; it has a named owner; temporary rules have an expiry date; guest networks never reach internal systems; and the rule matches a documented need. These criteria are simple enough for the IT team to apply quickly and catch the most common problems. She writes them as a short checklist attached to the change request form. A request failing any criterion is returned with a short note explaining what to fix, which teaches requesters over time.

### Lab — Change review

```python
"""Check synthetic firewall change requests against simple review rules (stdlib only)."""
reqs = [{"id": "CR1", "src": "staff", "dst": "case-files", "port": 445, "owner": "IT", "temp": False, "expiry": None},
        {"id": "CR2", "src": "any", "dst": "any", "port": None, "owner": "vendor", "temp": True, "expiry": None},
        {"id": "CR3", "src": "partners-vpn", "dst": "case-files", "port": 443, "owner": None, "temp": False, "expiry": None},
        {"id": "CR4", "src": "staff", "dst": "print", "port": 631, "owner": "Facilities", "temp": True, "expiry": "2026-05-01"},
        {"id": "CR5", "src": "guest", "dst": "case-files", "port": 443, "owner": "Reception", "temp": False, "expiry": None}]
def issues(r):
    out = []
    if "any" in (r["src"], r["dst"]) or r["port"] is None: out.append("too broad")
    if not r["owner"]: out.append("no owner")
    if r["temp"] and not r["expiry"]: out.append("temporary without expiry")
    if r["src"] == "guest" and r["dst"] != "internet": out.append("guest to internal")
    return out
for r in reqs: print(r["id"], "; ".join(issues(r)) or "ok")
print("approve as submitted:", [r["id"] for r in reqs if not issues(r)])
```

Run with `python3 lab_review.py`. Verified output:

```text
CR1 ok
CR2 too broad; temporary without expiry
CR3 no owner
CR4 ok
CR5 guest to internal
approve as submitted: ['CR1', 'CR4']
```

### 7.3 Reading the review

Of five synthetic requests, two can be approved as submitted: staff access to case files on the file-sharing port, and a temporary printing rule with an expiry. CR2, a vendor's request for any-to-any access without expiry, fails two criteria and should be rejected and rewritten as specific flows with an end date. CR3, partner VPN access to case files, has no owner, so it waits until one is named. CR5, guest access to case files, breaks the guest rule and is refused outright regardless of who requests it.

### 7.4 Verifying implemented changes

Approval is not the end. After implementation, Grace checks that the configured rule matches the approved request exactly and tests it: the permitted flow works and a neighbouring flow is still denied. She records the result in the change ticket. Verification catches typos, such as a wrong address range, that reviews of the request cannot. Over time, verified changes keep the rule base aligned with documented needs. If verification fails, the change is rolled back and the request returned. Verification takes about five minutes per change, a small cost compared with discovering a mistake months later.

### Worked example

Two of five requests are approved; one is refused, one needs an owner and one must be rewritten.

> **Synthetic case.** Requests are synthetic.

### Errors and limits

Approving broad vendor rules to save time creates long-lived exposure.

### Exercises

- **EX031 — Approved requests.** Which requests are approved as submitted? *Rubric:* 3 = CR1 and CR4;; 2 = two;; 1 = all;; 0 = none.
- **EX032 — Vendor request.** What should happen to CR2? *Rubric:* 3 = reject, rewrite as specific flows with expiry;; 2 = rewrite;; 1 = approve;; 0 = none.
- **EX033 — Guest request.** Why is CR5 refused outright? *Rubric:* 3 = guests never reach internal systems;; 2 = guest rule;; 1 = no owner;; 0 = none.
- **EX034 — Verification test.** Describe post-change verification. *Rubric:* 3 = config matches request, permitted flow works, neighbour denied;; 2 = test;; 1 = vague;; 0 = none.
- **EX035 — Review evidence.** Which study supports reviewing each change? *Rubric:* 3 = Wool 2004 on firewall errors;; 2 = Wool;; 1 = vague;; 0 = none.

### Synthesis

Simple review criteria and post-change verification keep firewall rules specific and justified.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Network and communications security: supervised case analysis

### Learning outcomes

You will (1) investigate a security event under supervision; (2) build a timeline; (3) recommend actions.

### 8.1 The event

One morning, the triage list shows an administrator login to the document system from an unfamiliar country, followed by a new email forwarding rule on a lawyer's mailbox. Under Sam's supervision and with Priyanka's approval, Grace investigates. The aim is to establish what happened, whether confidential data was exposed and what to do next. She follows the escalation criteria: this is a suspected compromise of an account with case-file access, so Priyanka and the compliance officer are informed immediately. She notes the time each step began.

### 8.2 Building a timeline

Grace collects VPN, email and document system logs for the relevant period and builds a timeline in UTC. The lawyer's password was entered on a fake login page the previous evening, according to a phishing report from another staff member. Shortly after, a login from abroad succeeded because the email service did not require a second factor. A forwarding rule was created. The document system login came from the same address but used a separate administrator account, which was denied by multi-factor authentication.

### 8.3 Containment

With the timeline, Priyanka resets the lawyer's password, removes the forwarding rule, revokes active sessions and blocks the foreign address at the email service. The administrator account's denial shows multi-factor authentication worked where it was enabled. Grace checks which emails were forwarded during the window: twelve, three containing client material. The compliance officer assesses whether client notification is required under the firm's obligations. All actions are logged with times and the person who performed them. Grace confirms afterwards that no further logins came from the foreign address and that the forwarding rule did not reappear.

### 8.4 Root causes

Grace identifies causes: the phishing email reached the user; the email service lacked multi-factor authentication for ordinary accounts; and forwarding to external addresses was permitted without review. She avoids blaming the lawyer, noting that phishing is designed to deceive and that the system should not depend on every person spotting every fake. Root causes point to fixes in controls, not just in individual behaviour. She also checks whether other mailboxes received the same phishing email and whether any of those users entered their passwords, since attackers rarely target one person only.

### 8.5 Recommendations

Grace recommends enabling multi-factor authentication for all email accounts, blocking automatic forwarding to external addresses except by approved exception, adding an alert for new forwarding rules and continuing staff phishing awareness. Each recommendation has an owner and a date. Sam reviews her report and asks her to separate confirmed facts from inferences more clearly, which she does. The firm adopts all four recommendations within a month. Progress is tracked in the ticket system, and Grace checks after a month that the forwarding alert actually fires on a test rule created by the IT team.

### Worked example

The investigation finds twelve emails forwarded, three with client material; four recommendations are adopted.

> **Synthetic case.** The event is synthetic.

### Errors and limits

Blaming individuals for phishing distracts from control gaps that allowed harm.

### Exercises

- **EX036 — Escalation reason.** Why was the event escalated immediately? *Rubric:* 3 = suspected compromise of case-file account;; 2 = criterion;; 1 = severity;; 0 = none.
- **EX037 — MFA evidence.** What showed multi-factor authentication working? *Rubric:* 3 = admin login denied by MFA;; 2 = admin denied;; 1 = vague;; 0 = none.
- **EX038 — Forwarded emails.** How many forwarded emails contained client material? *Rubric:* 3 = three of twelve;; 2 = three;; 1 = twelve;; 0 = none.
- **EX039 — Root cause list.** List the three root causes. *Rubric:* 3 = phishing reached user, no MFA on email, external forwarding allowed;; 2 = two;; 1 = one;; 0 = none.
- **EX040 — Facts versus inferences.** What did Sam ask Grace to improve? *Rubric:* 3 = separate confirmed facts from inferences;; 2 = clarity;; 1 = vague;; 0 = none.

### Synthesis

Supervised investigation with a timeline, containment and root causes leads to lasting control improvements.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write clear reports for different audiences; (2) handle sensitive findings ethically; (3) communicate uncertainty.

### 9.1 Audiences

Grace's investigation needs reports for different readers. Partners need a one-page summary: what happened, impact on clients, actions taken and decisions needed. The IT team needs technical detail: timeline, logs, configuration changes. The compliance officer needs facts relevant to obligations: what data, which clients, when discovered. Grace writes each from the same facts. Tailoring reports to their readers increases the chance they are read and acted upon, without changing the underlying truth. She checks each version against the facts list so no report contradicts another.

### 9.2 Plain language

Grace avoids jargon in summaries. Instead of "credential compromise via adversary-in-the-middle phishing", she writes "a lawyer entered their password on a fake login page, and someone used it to read and forward email". She defines unavoidable terms once. She also avoids alarming language. Plain, calm writing helps non-technical readers understand and decide, and it reduces the risk of overreaction or of dismissing the issue because it sounds too technical. She asks a non-technical colleague to read the summary and explain it back, which shows whether it is clear.

### 9.3 Communicating uncertainty

Some questions cannot be answered fully. Logs show twelve forwarded emails, but cannot show whether the recipient read or shared them. Grace states what is known, what is not and how confident she is. She uses phrases such as "logs show" and "we have no evidence of" rather than "nothing else happened". Honest statements of uncertainty let decision makers judge risk properly and protect the firm if more information emerges later. She also states what further evidence could reduce uncertainty, such as asking the recipient's provider for information.

### 9.4 Ethics of sensitive findings

Investigations can reveal sensitive information about colleagues, such as personal emails or mistakes. Grace includes only what is necessary for the security purpose and shares it only with those who need it. She does not discuss the case outside the agreed group. She treats the lawyer who was phished with respect, recognising that anyone can be deceived. Ethical handling maintains trust and encourages staff to report problems quickly in future. Notes about individuals are kept separate from technical findings and deleted when no longer needed.

### 9.5 Review before release

Before reports are released, Sam and Priyanka review them for accuracy, tone and sensitive content. The compliance officer reviews the partner summary. Reviews catch errors and phrasing that could be misread. Grace keeps a version history so changes are traceable. Releasing reports without review, especially about incidents, risks spreading inaccuracies that are hard to correct once partners or clients have read them. Each reviewer signs off a specific version, and only the signed version is distributed. If facts change later, a dated correction is issued rather than silently editing the released report.

### Worked example

Three reports are produced from one set of facts and reviewed before release.

> **Synthetic case.** Reports are synthetic.

### Errors and limits

Stating "nothing else happened" when logs cannot show it overstates certainty.

### Exercises

- **EX041 — Partner summary contents.** What does the partner summary contain? *Rubric:* 3 = what happened, client impact, actions, decisions needed;; 2 = three;; 1 = fewer;; 0 = none.
- **EX042 — Plain language rewrite.** Rewrite "credential compromise via phishing" plainly. *Rubric:* 3 = lawyer entered password on fake page, used by someone else;; 2 = plain;; 1 = jargon;; 0 = none.
- **EX043 — Uncertainty phrase.** How should Grace describe events logs cannot show? *Rubric:* 3 = "we have no evidence of", not "did not happen";; 2 = hedged;; 1 = certain;; 0 = none.
- **EX044 — Sensitive content.** How is sensitive colleague information handled? *Rubric:* 3 = include only what is necessary, need-to-know;; 2 = minimal;; 1 = full;; 0 = none.
- **EX045 — Report reviewers.** Who reviews the reports before release? *Rubric:* 3 = Sam, Priyanka and compliance officer;; 2 = reviewers;; 1 = vague;; 0 = none.

### Synthesis

Audience-specific, plain, honest and ethically handled reports support good decisions.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Network and communications security: quality and troubleshooting

### Learning outcomes

You will (1) troubleshoot security-related service problems; (2) maintain quality of controls; (3) learn from errors.

### 10.1 Security changes and service problems

After the firm enables multi-factor authentication for email and blocks external forwarding, some users report problems. A partner cannot sign in on an old tablet; a support team's shared mailbox stops forwarding to a court filing service. Grace approaches each as a troubleshooting task: precise description, evidence from logs, hypothesis, test and narrow fix. The goal is to restore legitimate service without weakening the new controls. She also tracks how many users report problems in the first week, which shows whether the rollout communications were clear enough.

### 10.2 The tablet

Logs show the tablet uses an old mail app that does not support modern sign-in with a second factor. Options are to replace the app, replace the tablet or exempt the account. Exempting the account would leave a partner's mailbox without multi-factor authentication, which is not acceptable. Grace recommends installing the supported mail app, which takes ten minutes. Narrow fixes like this preserve the control for everyone while solving the user's real problem. She adds the old app to a list of unsupported software for the help desk.

### 10.3 The court filing forwarding

The shared mailbox legitimately forwards certain messages to a court filing service. Grace confirms the destination with the support team lead, and Priyanka adds an approved exception for that mailbox and that destination only, with an owner and a review date. The exception is documented in the change log. Approved, narrow exceptions are part of a mature control; a block that cannot accommodate legitimate needs will eventually be removed entirely under pressure. The court filing destination is also added to the email service's monitoring, so unusual volumes are noticed.

### 10.4 Quality checks

Grace adds quality checks to the weekly routine: count of accounts without multi-factor authentication, which should be zero; count and age of forwarding exceptions; and any new rules without owners. She also proposes a quarterly sample review of closed alert tickets, checking that conclusions were supported by evidence. Quality checks catch slow decay, such as exceptions accumulating or alerts being closed without investigation. The results are shown as a short table in the weekly report, with any non-zero values highlighted, so Priyanka can see at a glance whether controls are holding.

### 10.5 Learning from errors

During the rollout, a configuration error briefly blocked forwarding for an approved exception because the destination was mistyped. Grace records it in a lessons log: what happened, effect, cause and change made. The change is to copy addresses from the original request rather than retyping them. Small, recorded lessons accumulate into better practice. Teams that record errors openly improve faster than those that fix them quietly and forget. The lessons log is reviewed monthly by the IT team, and recurring causes are turned into checklist items or small process changes.

### Worked example

Two service problems are resolved without weakening controls; weekly checks show zero accounts without MFA.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Exempting users from controls to fix device problems leaves the most exposed accounts unprotected.

### Exercises

- **EX046 — Tablet fix.** How was the partner's tablet problem fixed? *Rubric:* 3 = install supported mail app;; 2 = new app;; 1 = exemption;; 0 = none.
- **EX047 — Exception scope.** What does the forwarding exception cover? *Rubric:* 3 = one mailbox to one destination, owner, review date;; 2 = narrow;; 1 = all;; 0 = none.
- **EX048 — Quality check.** Give one weekly quality check. *Rubric:* 3 = accounts without MFA, exceptions, rules without owners;; 2 = one;; 1 = vague;; 0 = none.
- **EX049 — Mistyped lesson.** What changed after the mistyped destination? *Rubric:* 3 = copy addresses from request, not retype;; 2 = copy;; 1 = vague;; 0 = none.
- **EX050 — Exception necessity.** Why are narrow approved exceptions necessary? *Rubric:* 3 = otherwise control removed under pressure;; 2 = usability;; 1 = weakness;; 0 = none.

### Synthesis

Careful troubleshooting, narrow exceptions and quality checks keep controls effective and usable.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) establish a baseline for denied connections; (2) detect unusual weeks; (3) investigate in a lab setting.

### 11.1 Why baselines

An alert threshold is easier to set if one knows what normal looks like. Grace builds a baseline of weekly denied connections at Oakline's main office from eight weeks of synthetic data. A baseline captures the usual level and its variation. Weeks far above it may signal a new device, a misconfiguration or an infection. Baselines must be rebuilt when the network changes, since a new office or service changes what normal means. Grace documents the period used so the baseline can be rebuilt consistently later.

### 11.2 Choosing a threshold

A common simple threshold is the mean plus two standard deviations. In roughly normal data, values above it occur by chance only a few percent of the time. Grace notes that network data may not be normal, so the threshold is a starting point to be tested against experience. She also notes that a threshold catches only sharp rises; slow increases need a trend check, which she adds to the monthly review. She records the threshold method and its date in the lab notebook before applying it.

### Lab — Baseline check

```python
"""Flag weeks whose denied-connection count is above baseline mean + 2 standard deviations (stdlib only)."""
import statistics
base = [410, 385, 430, 402, 395, 420, 415, 398]
weeks = {"W9": 405, "W10": 512, "W11": 418, "W12": 389, "W13": 470}
m, s = statistics.mean(base), statistics.stdev(base); limit = m + 2 * s
print(f"baseline mean {m:.1f} sd {s:.1f} limit {limit:.1f}")
for w, v in weeks.items(): print(f"{w:4}{v:5} {'ABOVE' if v > limit else 'normal'}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
baseline mean 406.9 sd 14.7 limit 436.2
W9    405 normal
W10   512 ABOVE
W11   418 normal
W12   389 normal
W13   470 ABOVE
```

### 11.3 Reading the baseline

The eight baseline weeks average 406.9 denies with a standard deviation of 14.7, giving a threshold of 436.2. Weeks 10 and 13 exceed it, with 512 and 470 denies. In the lab scenario, week 10 matches the installation of new meeting room displays that tried to reach a cloud service not on the allowed list, and week 13 matches a guest who connected a laptop with malware that kept trying to reach internal addresses. Both are investigated and resolved: one by adding a needed flow, the other by guest isolation already blocking the attempts.

### 11.4 Lab discipline

Grace works in an isolated lab using synthetic data, documenting each step and keeping results reproducible. She writes down the threshold method before looking at the weeks, so she cannot adjust it to produce a preferred result. Sam reviews her notebook and asks her to explain why two weeks above threshold in thirteen is plausible. She explains that real events caused both, rather than chance alone. Disciplined lab work builds habits that carry into real investigations. Her notebook is kept with the lab files.

### Worked example

The baseline threshold is 436.2; weeks 10 and 13 exceed it and are explained by a missing flow and a guest infection.

> **Synthetic case.** Data and events are synthetic.

### Errors and limits

Adjusting thresholds after seeing results can hide or invent anomalies.

### Exercises

- **EX051 — Threshold value.** What threshold does the lab compute? *Rubric:* 3 = 436.2 from mean 406.9 plus 2 × 14.7;; 2 = 436.2;; 1 = 406.9;; 0 = none.
- **EX052 — Flagged weeks.** Which weeks exceed the threshold? *Rubric:* 3 = W10 512 and W13 470;; 2 = two;; 1 = one;; 0 = none.
- **EX053 — Week 10 cause.** What caused week 10's rise? *Rubric:* 3 = new displays reaching unlisted cloud service;; 2 = displays;; 1 = attack;; 0 = none.
- **EX054 — Slow increase.** How are slow increases detected? *Rubric:* 3 = monthly trend check;; 2 = trend;; 1 = threshold;; 0 = none.
- **EX055 — Rebuild trigger.** When must the baseline be rebuilt? *Rubric:* 3 = network changes, such as new office or service;; 2 = changes;; 1 = never;; 0 = none.

### Synthesis

Baselines and simple thresholds turn raw counts into signals worth investigating.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a practice portfolio; (2) demonstrate competence; (3) plan continuing development.

### 12.1 The portfolio

Grace's portfolio collects evidence of her work: the context summary, the network review, the change review checklist, the investigation report, the troubleshooting cases, the baseline lab and her practice log. Each item has a short cover note stating what it shows and which course outcome it supports. All client-identifying details are removed, and Oakline approves the portfolio for assessment. A portfolio shows what a practitioner can actually do, which matters more to employers than course completion alone. Sam reviews each item before submission.

### 12.2 Demonstrating competence

In the final review, an assessor asks Grace to walk through one piece of work in depth. She chooses the investigation: how she followed authorisation and escalation, built the timeline, separated facts from inferences and turned root causes into control changes. The assessor asks what she would do differently. She says she would have checked mailbox forwarding rules across the firm sooner, since one compromised account suggests others may have been targeted. Reflection on improvements shows mature judgement. The assessor notes this answer.

### 12.3 Outcomes for Oakline

The firm's position has improved during the course: guest wireless no longer reaches printers, remote access and email require multi-factor authentication, external forwarding needs approval, rule changes are reviewed against criteria, and the IT team has daily and weekly routines. Grace lists these outcomes with evidence, careful not to claim credit for work the IT team did. Accurate attribution maintains good relationships and credibility. Each outcome is linked to a ticket, change record or report showing when it was completed and by whom. Priyanka confirms the list is accurate before it goes into the portfolio.

### 12.4 Continuing development

Grace writes a development plan for the next year: deepen knowledge of cloud email security, practise packet-level troubleshooting in labs, read the full text of SP 800-94 and SP 800-207, and join a local practitioners' group. Sam agrees to continue mentoring monthly. Network security changes constantly, so a plan for continued learning is part of professional competence, not an optional extra. Each item has a target date and a way to show it was done, such as a lab write-up or a short summary of what she read. Sam reviews progress at their monthly meetings and suggests adjustments as her new role develops.

### 12.5 Closing reflection

Grace reflects that her support background was an advantage: she understood users and service, so her security work was practical and accepted. The main new skills were evidence handling, structured review and communicating risk to partners. She completes the course and takes a junior network security role at a managed service provider, where she will apply the same approach across several client organisations. She notes that the habits of scope, evidence, smallest change, verification and recording will matter even more when she works across many clients, each with different systems and expectations.

### Worked example

The portfolio contains seven items with cover notes; the assessor passes Grace with commendation for her investigation.

> **Synthetic case.** The portfolio and review are synthetic.

### Errors and limits

Portfolios that claim credit for others' work undermine trust.

### Exercises

- **EX056 — Portfolio cover note.** What does each cover note state? *Rubric:* 3 = what it shows and which outcome;; 2 = purpose;; 1 = title;; 0 = none.
- **EX057 — Improvement named.** What would Grace do differently in the investigation? *Rubric:* 3 = check forwarding rules firm-wide sooner;; 2 = check others;; 1 = vague;; 0 = none.
- **EX058 — Outcome list.** Name three improvements at Oakline. *Rubric:* 3 = guest isolation, MFA, forwarding approval, change review, routines;; 2 = two;; 1 = one;; 0 = none.
- **EX059 — Attribution.** Why avoid claiming credit for the IT team's work? *Rubric:* 3 = accuracy, relationships, credibility;; 2 = honesty;; 1 = modesty;; 0 = none.
- **EX060 — Development item.** Name one item in Grace's development plan. *Rubric:* 3 = cloud email security, labs, reading, practitioners' group;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

A practice portfolio, honest reflection and a development plan complete the professional course.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Grace Whitfield, Sam Adeyemi, Northgate Professional Academy, Oakline Legal and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Altered documents or emailed instructions could harm a client's case.

**EX002.** Confirm scope, use evidence, make the smallest change, verify and record.

**EX003.** She understands users, tickets and the cost of disruption.

**EX004.** It makes recommendations easier to accept and check.

**EX005.** Lawyers must reach files and email before court deadlines.

**EX006.** What the worst outcome would be for them.

**EX007.** Guest wireless shares a network with printers used for confidential documents.

**EX008.** Its question about multi-factor authentication raised that priority.

**EX009.** Changes must avoid working hours.

**EX010.** It keeps work focused and lets others check recommendations fit the firm.

**EX011.** Accessing case files and testing live systems.

**EX012.** To detect any later change to the file.

**EX013.** Who held each item, when, where it was stored and why it moved.

**EX014.** By phone to the IT manager the same day.

**EX015.** Report it through the agreed route.

**EX016.** The design against good practice and against the actual configuration.

**EX017.** Staff access to server management, guest access to printers and a supplier rule without expiry.

**EX018.** Remote access used passwords without a second factor.

**EX019.** Finding, evidence, risk, recommendation and owner.

**EX020.** It makes the review easier to accept and shows understanding of the team's work.

**EX021.** The administrator login from a new country on case files, score nine.

**EX022.** It may indicate a compromised account forwarding confidential email.

**EX023.** The laptop behind it may still be infected.

**EX024.** It reflects event type, not the importance of the affected asset.

**EX025.** Confusion about the order of events.

**EX026.** Overnight high-priority alerts, tunnel status and log arrival.

**EX027.** Slow trends such as gradually rising denies.

**EX028.** It keeps work visible to the team and fits how they already work.

**EX029.** Suspected compromise of an account with case-file access.

**EX030.** The compliance officer.

**EX031.** CR1 and CR4.

**EX032.** Reject it and rewrite as specific flows with an end date.

**EX033.** Guest networks must never reach internal systems.

**EX034.** Check the rule matches, the permitted flow works and a neighbouring flow is denied.

**EX035.** Wool's 2004 study of firewall configuration errors.

**EX036.** It met the criterion of suspected compromise of an account with case-file access.

**EX037.** The administrator account's login was denied by multi-factor authentication.

**EX038.** Three of the twelve forwarded emails.

**EX039.** Phishing reached the user, email lacked MFA and external forwarding was allowed.

**EX040.** To separate confirmed facts from inferences more clearly.

**EX041.** What happened, client impact, actions taken and decisions needed.

**EX042.** A lawyer entered their password on a fake login page and someone used it.

**EX043.** With phrases such as "we have no evidence of" rather than claiming it did not happen.

**EX044.** Only what is necessary is included, shared only with those who need it.

**EX045.** Sam, Priyanka and, for the partner summary, the compliance officer.

**EX046.** By installing a mail app that supports modern sign-in.

**EX047.** One mailbox forwarding to one destination, with an owner and review date.

**EX048.** Counting accounts without multi-factor authentication.

**EX049.** Addresses are copied from the original request rather than retyped.

**EX050.** Without them, blocks that stop legitimate work are eventually removed entirely.

**EX051.** 436.2, the mean of 406.9 plus two standard deviations of 14.7.

**EX052.** Weeks 10 and 13.

**EX053.** New meeting room displays trying to reach an unlisted cloud service.

**EX054.** With a monthly trend check, since the threshold catches only sharp rises.

**EX055.** When the network changes, such as a new office or service.

**EX056.** What the item shows and which course outcome it supports.

**EX057.** Check mailbox forwarding rules across the firm sooner.

**EX058.** Guest isolation from printers, MFA for email and remote access, and change review.

**EX059.** Accurate attribution maintains relationships and credibility.

**EX060.** Deepening knowledge of cloud email security.

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
