# Security Operations and Blue Team: Technical Course

- Language: English (`en`); course 061, Technical course (18 months).
- Editorial state: **published**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students preparing for entry-level analyst roles in a security operations centre.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one trainee analyst at a local council from a password-guessing alert through logs, triage, response, detection, tuning, metrics and maturity. Run each lab where it appears, attempt the four exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Carlos Mendes** | Trainee SOC analyst | Invented |
| **Aisha Rahman** | SOC lead | Invented |
| **Northgate Borough Council** | Fictional local council | Invented |
| **parks01** | Shared parks-department account | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — What a security operations centre does

### Learning outcomes

You will (1) describe the purpose of a SOC; (2) name the main SOC functions; (3) explain how the SOC relates to IT and management; (4) use the case that runs through the book.

### 1.1 The case

Carlos Mendes has just joined the small security operations centre at the fictional Northgate Borough Council as a trainee analyst. His lead is Aisha Rahman. On his second morning, at 09:04, the monitoring system shows 46 failed logons from one internet address, 203.0.113.80, against the council's remote-access portal, followed at 09:09 by a successful logon to "parks01", a shared account used by the parks department. This book follows Carlos as he learns to handle events like this one. The 46 failures and the single success, five minutes apart, become the thread that later chapters keep returning to.

### 1.2 Purpose

A SOC watches an organisation's systems for signs of attack or misuse, decides which signs matter, and coordinates the response. Zimmerman's "Ten Strategies of a World-Class Cybersecurity Operations Center" (MITRE, 2014) and its successor "11 Strategies" by Knerler, Parker and Zimmerman (MITRE, 2022) describe the SOC as a team with a clear mission, authority and resources rather than a room full of screens. At Northgate, mission and authority are written down: the SOC may disable accounts and block addresses on its own, but isolating servers needs the IT manager. That split shapes what Carlos can do at 09:09 without waiting for anyone else to approve the first containment step.

### 1.3 Functions

Typical functions are monitoring and triage, incident response, threat intelligence, detection engineering, vulnerability awareness and tool maintenance. At Northgate, four analysts cover all of these with help from the IT team. With four analysts, nobody specialises fully, so Carlos meets every function in his first weeks. Monitoring raised the 09:04 alert, triage and response handled parks01, and threat intelligence checked whether other councils had seen 203.0.113.80. Detection engineering later wrote the rule that would catch the same pattern faster next time. Small size means the same analyst may triage an alert and then write the rule that tunes it.

### 1.4 Relationships

The SOC does not own most systems. It needs IT to change firewall rules, reset passwords or rebuild machines, and it needs management to accept risks and approve major actions. Good relationships are part of the job. In the parks01 case Carlos could disable the account himself, but IT had to create named accounts for the gardeners and the IT manager owned the MFA change on the portal. Without good working relationships, each of those steps would have waited in someone else's queue while the parks team could not log timesheets.

### 1.5 Frameworks

NIST Cybersecurity Framework 2.0 (CSWP 29, 2024) groups security outcomes into Govern, Identify, Protect, Detect, Respond and Recover. Most SOC work sits in Detect and Respond but depends on the others. The parks01 case touches far more than two of the six CSF functions. Govern sets who may disable an account, Identify lists the shared account in the asset records, and Protect is where MFA on the portal belongs. Detect and Respond cover the morning itself, and Recover covers named accounts for the gardeners. Seeing the whole framework stops the SOC treating every problem as a detection problem when the fix belongs elsewhere.

### Worked example

Aisha asks Carlos to map the morning's event to SOC functions. Monitoring raised the alert; triage must decide if the parks01 logon was the attacker; incident response may disable the account; IT must reset it; threat intelligence may check the address; detection engineering may tune the rule that fired.

> **Synthetic case.** Northgate Borough Council, its staff and events are invented.

### Errors and limits

SOCs differ widely in size and scope; Northgate's is small and generalist.

### Exercises

- **EX001 — SOC purpose.** In one sentence, what is a SOC for? *Rubric:* 3 = watch, decide what matters, coordinate response; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Morning event.** Summarise the 09:04–09:09 events. *Rubric:* 3 = 46 failures from 203.0.113.80, then parks01 success at 09:09; 2 = partial; 1 = wrong; 0 = none.
- **EX003 — Who changes systems.** Why does the SOC depend on IT? *Rubric:* 3 = SOC does not own most systems; IT makes changes; 2 = partial; 1 = vague; 0 = none.
- **EX004 — CSF functions.** Which two CSF 2.0 functions hold most SOC work? *Rubric:* 3 = Detect and Respond; 2 = one; 1 = vague; 0 = none.

### Synthesis

A SOC watches, decides and coordinates; it relies on IT, management and clear frameworks.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Logs and telemetry

### Learning outcomes

You will (1) explain what logs and telemetry are; (2) list key log sources for a SOC; (3) describe what a useful log entry contains; (4) explain log retention and time synchronisation.

### 2.1 What logs are

A log is a record written by a system when something happens: a logon, a file change, a network connection. Telemetry is the broader stream of such data sent to the SOC. NIST SP 800-92 (Kent and Souppaya, 2006) is the classic guide to log management. For the parks01 case, the portal's authentication log recorded each attempt, the domain controller recorded the account check, and the file share's audit log recorded what was opened. None of these systems was set up for the SOC, so each log answers only the questions its owner chose to record.

### 2.2 Key sources

For Northgate: the remote-access portal, domain controllers, endpoint agents, the email gateway, the web proxy and the firewall. The 09:04 alert came from the portal's authentication log. Each source answers a different question in the council's cases. The portal and domain controllers show who signed in, the endpoint agents show what ran on a PC, and the email gateway shows who received a message. The proxy shows who clicked, as in the finance case, and the firewall shows traffic that bypassed the proxy.

### 2.3 Useful entries

A useful entry has a time, source, user, action and outcome. The portal entry "09:09 OK 203.0.113.80 parks01" has all five. Entries missing the user or source are much harder to use. The parks01 entry tells Carlos when it happened (09:09), from where (203.0.113.80), as whom (parks01), what was attempted (a logon) and how it ended (OK). A line with no source address could not have been linked to the 46 failures, and the case would have looked like an ordinary morning logon by a gardener.

### 2.4 Time

All systems must agree on time; Northgate uses a central time server. If the portal clock were five minutes slow, the logon would seem to come before the guessing, confusing the story. Carlos confirmed the order by comparing two independent sources: the portal and the domain controller both recorded 09:09. If one clock had drifted, the domain controller line would have appeared minutes away from the portal line, and he would have had to correct for the offset before building the timeline.

### 2.5 Retention

Logs are kept for a set period, here 90 days searchable and one year archived, as agreed with the records manager. Without retention, past activity cannot be checked. Ninety searchable days cover most investigations, including checking whether 203.0.113.80 had tried the portal before Monday. The one-year archive matters for slower questions, such as when the parks01 password was last changed. Agreeing retention with the records manager keeps it lawful as well as useful, since logs contain staff activity. The retention period is written into the logging standard so every new system follows it from the day it is connected.

### 2.6 Collection

Logs flow into a central security information and event management (SIEM) system where analysts search and correlate them. Having all sources in one SIEM is what lets Carlos see the portal failures, the parks01 logon and the domain controller check side by side. Without central collection he would have had to sign in to each system separately and line up times by hand, which is slow and easy to get wrong during a live case. Normalising fields on arrival is what makes a single search across all six sources possible.

### Normalisation

Different systems name the same thing differently: one says user, another account, another principal. The SIEM maps them to common field names when logs arrive, so one search finds a person's activity across all sources.

### Worked example

Carlos checks the portal and domain controller logs. The portal shows parks01 logged in at 09:09; the domain controller shows parks01 authenticated at 09:09 from the portal server. Times agree, so he can trust the sequence.

> **Synthetic case.** Log entries are synthetic.

### Errors and limits

More logs cost money to store and search; collect what supports decisions.

### Exercises

- **EX005 — Five fields.** Name five fields of a useful log entry. *Rubric:* 3 = time, source, user, action, outcome; 2 = four; 1 = two; 0 = none.
- **EX006 — Time agreement.** Why must clocks agree? *Rubric:* 3 = otherwise event order is wrong; 2 = partial; 1 = vague; 0 = none.
- **EX007 — Log sources.** List four Northgate log sources. *Rubric:* 3 = portal, DCs, endpoint agents, email, proxy, firewall (four); 2 = two; 1 = one; 0 = none.
- **EX008 — Retention purpose.** Why keep logs for a set period? *Rubric:* 3 = to check past activity; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Logs with complete fields, agreed time and suitable retention are the raw material of the SOC.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — The SIEM and alerting

### Learning outcomes

You will (1) explain what a SIEM does; (2) describe how rules produce alerts; (3) distinguish events, alerts and incidents; (4) explain alert severity.

### 3.1 What a SIEM does

A SIEM collects logs, normalises their fields, stores them for search and runs rules that raise alerts. Northgate's SIEM receives about four million events a day. Four million events a day is far beyond what analysts can read, so rules decide which few deserve a person's attention. On the Monday of the parks01 case, two of those millions became alerts, at 09:04 and 09:09, and both reached Carlos's queue within minutes of the activity. The rest stay searchable, which is how Carlos later checks the domain controller and share logs for parks01.

### 3.2 Rules

A rule describes a pattern, such as "20 or more failed logons from one source in 10 minutes". When the pattern matches, the SIEM raises an alert. Sigma (SigmaHQ) is an open, vendor-neutral format for sharing such rules. At 09:04 the 46 failures from 203.0.113.80 crossed this threshold of 20 within ten minutes, so the rule fired. Writing the idea in Sigma's format makes it easier to share with other councils or move to a different SIEM later. The detection engineering chapter uses the same structure for Carlos's new rule.

### 3.3 Events, alerts, incidents

An event is anything logged. An alert is an event or group that a rule flagged. An incident is a confirmed situation that harms or threatens security, as defined in NIST SP 800-61r3 (Nelson et al., 2025). Most alerts are not incidents. The parks01 case passes through all three stages in a single Monday morning. Every failed logon was an event; the 09:04 and 09:09 rule matches were alerts; only after Carlos confirmed the tablet was idle did the case become INC-0417, an incident. Keeping the terms apart stops every alert being reported as an incident to managers.

### 3.4 Severity

Each rule has a severity. The failed-logon rule is medium; a success after guessing raises it to high. Severity tells the analyst how much harm the matched pattern could mean if it is real. Failures alone are an attempt, while a success after them suggests a compromised account, which is why the 09:09 alert outranked the 09:04 one. Triage later combines this severity with how important the affected system is. Severity is set when the rule is written and reviewed during tuning, so it reflects what the SOC has learned from real alerts.

### 3.5 Alert queue

Alerts wait in a queue sorted by severity and time. Analysts take the top one, investigate and record a decision. Taking the top alert rather than the most interesting one keeps the most serious work first. Recording a decision for each alert means nothing is left half-handled when a shift ends. In the parks01 case, the linked 09:04 and 09:09 alerts sat together in one case, so the next analyst saw the whole story. The queue also shows how long each alert has waited, which feeds the acknowledge times measured later in the metrics chapter.

### 3.6 Noise

Rules that fire often without real problems create noise that hides important alerts. Alahmadi et al. (2022) found analysts widely frustrated by false positives. At Northgate, the 'admin tool used' rule shows the cost: it fired 220 times in a month with only two real cases. Analysts who see hundreds of harmless alerts begin to skim, and a real case can slip past. Tuning that rule is one of Carlos's tasks later in the book. Every noisy rule therefore has a cost in attention as well as in time.

### Correlation

Some rules look across sources. A correlation rule might link a portal logon with a domain controller authentication and a file-share access in the same minutes. Correlation turns separate small signals into one meaningful alert, but it only works when time and user fields agree across systems, which is why chapter 2 stressed them.

### Worked example

The SIEM raised two alerts at 09:04 and 09:09. Carlos sees they share a source address and links them in one case, so the next analyst sees the whole story.

> **Synthetic case.** Volumes and alerts are invented.

### Errors and limits

SIEM rules only see what is logged; gaps in collection are blind spots.

### Exercises

- **EX009 — Three terms.** Distinguish event, alert and incident. *Rubric:* 3 = logged thing; rule-flagged; confirmed harm/threat; 2 = partial; 1 = confused; 0 = none.
- **EX010 — Rule example.** Give the failed-logon rule in words. *Rubric:* 3 = 20+ failures from one source in 10 min; 2 = partial; 1 = vague; 0 = none.
- **EX011 — Sigma.** What is Sigma? *Rubric:* 3 = open vendor-neutral rule format; 2 = partial; 1 = tool; 0 = none.
- **EX012 — Linking alerts.** Why link the two alerts in one case? *Rubric:* 3 = shared source; whole story visible; 2 = partial; 1 = vague; 0 = none.

### Synthesis

The SIEM turns logs into alerts through rules; analysts turn alerts into decisions.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Reading authentication logs

### Learning outcomes

You will (1) read authentication log entries; (2) count failures per source; (3) spot success after many failures; (4) explain why shared accounts are risky.

### 4.1 Authentication events

Logon attempts record user, source, time and result. Patterns in failures reveal guessing. In the portal log, each line carries the time, result, source address and username. Counting failures by source shows whether many attempts came from one place, while counting usernames shows whether one person mistyped or many names were tried. Both counts mattered when Carlos decided how to treat the parks01 case. The lab below performs the first count on synthetic data, using the threshold of 20 failures from the council's rule. It prints an ALERT line for any source at or above it.

### Lab — counting failures

```python
"""Count failed logons per source address in a synthetic log (threshold 20 in 10 minutes)."""
from collections import Counter
log = (["09:01 FAIL 198.51.100.7 jsmith"] * 3 + ["09:04 FAIL 203.0.113.80 admin"] * 46
       + ["09:05 FAIL 192.0.2.15 mbrown"] * 2 + ["09:09 OK 203.0.113.80 parks01"])
fails = Counter(line.split()[2] for line in log if line.split()[1] == "FAIL")
for src, n in fails.most_common():
    print(f"{src:15} failures={n:3} {'ALERT' if n >= 20 else 'ok'}")
ok_after = [l for l in log if l.split()[1] == "OK" and fails[l.split()[2]] >= 20]
print("success from alerting source:", ok_after)
```

Run with `python3 lab_failed.py`. Verified output:

```text
203.0.113.80    failures= 46 ALERT
198.51.100.7    failures=  3 ok
192.0.2.15      failures=  2 ok
success from alerting source: ['09:09 OK 203.0.113.80 parks01']
```

### 4.2 Lab result

The lab counts 46 failures from 203.0.113.80, above the threshold of 20, while two other sources had 3 and 2 failures, which looks like normal typing mistakes. It also finds the 09:09 success for parks01 from the alerting source. For brevity the lab writes every one of the 46 failures against the name admin; the real portal search showed 31 different usernames, which Carlos checks separately in the SIEM. The lab's success line is what turns a failed attack into a possible compromise. Both counts, by source and by username, go into the INC-0417 case note.

### 4.3 Success after failure

A success from the same source after many failures is a strong sign the guessing worked. It moves the case from "attempt" to "possible compromise". A success alone is ordinary, and many failures alone are an attempt, but together from one source they suggest the attacker found a working password. For parks01 that sequence, 46 failures then a success five minutes later from 203.0.113.80, is what moved the case into confirming compromise. Carlos then checks the tablet and the session to be sure.

### 4.4 Shared accounts

parks01 is used by several gardeners on a shared tablet. No one person is responsible for its password, which had not changed in three years. Shared accounts are easy to guess and hard to investigate because you cannot tell which person used them. The shared account also made the investigation slower and less certain for Carlos. Carlos could not ask one person whether they had logged in at 09:09; he had to check the shared tablet instead and found it idle in the depot. Named accounts for each gardener, agreed in the lessons, remove both the guessing risk and this ambiguity.

### 4.5 ATT&CK

MITRE ATT&CK (Strom et al., 2018) describes adversary behaviour; the pattern here matches its brute-force technique under Credential Access. Tagging the case with the brute-force technique lets Northgate count how often it appears and check whether a rule covers it. The coverage map later shows credential guessing well covered, partly because of the rule written after INC-0417. The tag also links the case to the sharing group's warning about guessing against council portals. ATT&CK names the behaviour without saying who was behind it, which is all the SOC needs here.

### Username patterns

Carlos also looks at which usernames were tried. The 46 failures used 31 different names, many of them common words such as admin, test and reception. Guessing many names with a few passwords each is a sign of automated guessing rather than a forgetful person. A single user mistyping their own password produces failures on one name only, usually spread over a few minutes. This pattern check takes seconds in the SIEM and helps decide whether the case is an attack or a help-desk call.

### Worked example

Carlos records: "46 failures from 203.0.113.80 against multiple usernames 09:04, success as parks01 09:09 from same source. Likely password guessing succeeded. Recommend disable parks01 and check its activity since 09:09."

> **Synthetic case.** The log is synthetic and created by the lab.

### Errors and limits

Some sources are shared by many users (for example a mobile carrier); check before blaming one address.

### Exercises

- **EX013 — Lab counts.** What did the lab report? *Rubric:* 3 = 46 from .80 ALERT; 3 and 2 ok; success parks01; 2 = partial; 1 = one; 0 = none.
- **EX014 — Why success matters.** Why does a later success matter? *Rubric:* 3 = guessing may have worked; possible compromise; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Shared account risk.** Give two risks of shared accounts. *Rubric:* 3 = easy to guess/old password; cannot tell who used it; 2 = one; 1 = vague; 0 = none.
- **EX016 — Recommended action.** What did Carlos recommend? *Rubric:* 3 = disable parks01; check activity since 09:09; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Count failures, look for success after failure and treat shared accounts with extra care.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Triage and prioritisation

### Learning outcomes

You will (1) explain what triage means in a SOC; (2) rank alerts by severity and asset importance; (3) decide when to escalate; (4) record triage decisions clearly.

### 5.1 What triage is

Triage is the quick first look at an alert to decide what it is and how urgent it is. The aim is not to finish the investigation but to put each alert in the right place: close it, investigate it now, or escalate it. Most alerts in Northgate's queue need only a few minutes to place correctly. A2, the new payroll admin, was closed quickly once Carlos found the approved change ticket. A4 went to a closer look in the proxy logs. Getting each into the right place frees time for the few that become incidents.

### 5.2 Two inputs

Urgency depends on how serious the activity is (severity) and how important the affected system is (asset criticality). A new admin on a payroll server matters more than failed logons on a library kiosk, even if both rules are "medium". The payroll server handles staff pay, so a new admin there could affect every employee, while a kiosk in the library holds no personal data. The asset list supplies the criticality value, and the rule supplies severity, so the analyst does not have to judge both from memory under pressure.

### Lab — ranking alerts

```python
"""Rank synthetic alerts by severity x asset criticality (1-3 each)."""
alerts = [("A1", "Malware blocked on laptop", 2, 1), ("A2", "New admin on payroll server", 3, 3),
          ("A3", "Failed logons on library kiosk", 1, 1), ("A4", "Outbound to new domain from finance PC", 2, 3),
          ("A5", "Disabled AV on reception PC", 2, 2)]
for aid, text, sev, crit in sorted(alerts, key=lambda a: -a[2] * a[3]):
    score = sev * crit
    pri = "P1" if score >= 9 else "P2" if score >= 6 else "P3" if score >= 3 else "P4"
    print(f"{aid} score={score} {pri} {text}")
```

Run with `python3 lab_triage.py`. Verified output:

```text
A2 score=9 P1 New admin on payroll server
A4 score=6 P2 Outbound to new domain from finance PC
A5 score=4 P3 Disabled AV on reception PC
A1 score=2 P4 Malware blocked on laptop
A3 score=1 P4 Failed logons on library kiosk
```

### 5.3 Lab result

Multiplying severity by criticality (each 1–3) puts the new admin on the payroll server first (score 9, P1), outbound traffic from a finance PC to a new domain second (6, P2), disabled antivirus on a reception PC third (4, P3), and the blocked malware and kiosk failures last (P4). The blocked malware is low because the protection worked, but it is still checked later. The score is a guide to order, not a decision about what the alert means. Carlos follows the scores unless he records a reason to depart from them.

### 5.4 Escalation

Carlos escalates to Aisha when an alert is P1, when he is unsure, or when an action would affect services. Escalating is not failure; guessing is. In the parks01 case, Carlos could disable the account without escalating, because the playbook allows it and it affects only the shared account. When the gardeners needed accounts for timesheets, he involved IT. Escalating when unsure costs Aisha a few minutes; a wrong guess on a P1 alert could cost much more. His escalations are logged with the reason, so Aisha can see the pattern over time.

### 5.5 Recording

Each triage note states what was seen, what was checked, the decision and the reason. "Closed — benign" with no reason helps no one. Carlos's note for A2 shows the pattern: a new admin account on the payroll server, checked against the change system, matched an approved change ticket for the payroll upgrade, closed as benign with the ticket number. A reviewer can verify that in seconds, while 'closed — benign' alone would force them to repeat the work. Good notes also give Carlos's later tuning work the real and benign counts it depends on.

### 5.6 Asset list

Triage depends on knowing which systems matter. Northgate keeps an asset list with a criticality value for each server and group of PCs, maintained with IT. The scores in the triage lab depend entirely on this list. If the payroll server were missing or marked as low criticality, A2 would have dropped to the bottom of the queue. Maintaining the list with IT means new servers, such as those added for the payroll upgrade, get a value before alerts arrive.

### Worked example

At 10:30, five alerts are waiting. Carlos uses the scores, takes A2 first, finds that IT created the admin account for a planned payroll upgrade with an approved change ticket, and closes it with the ticket number. He then takes A4, the finance PC, which needs a closer look and links to chapter 8.

> **Synthetic case.** Alerts and scores are synthetic.

### Errors and limits

A simple score can mislead; an analyst's judgement can override it with a recorded reason.

### Exercises

- **EX017 — Triage aim.** What is the aim of triage? *Rubric:* 3 = place alert: close, investigate, escalate; 2 = partial; 1 = finish; 0 = none.
- **EX018 — Lab order.** Give the top two alerts from the lab and their scores. *Rubric:* 3 = A2 9 P1; A4 6 P2; 2 = partial; 1 = wrong; 0 = none.
- **EX019 — When to escalate.** When does Carlos escalate? *Rubric:* 3 = P1, unsure, service-affecting action; 2 = two; 1 = one; 0 = none.
- **EX020 — A2 outcome.** How was A2 resolved? *Rubric:* 3 = approved change ticket; closed with ticket number; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Triage combines severity and asset importance, escalates when needed and records clear reasons.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Endpoint telemetry

### Learning outcomes

You will (1) describe what endpoint agents record; (2) read process and account events; (3) use endpoint data to confirm or rule out compromise; (4) explain isolation as a containment option.

### 6.1 Endpoint agents

Endpoint detection and response (EDR) agents on laptops and servers record processes started, files changed, network connections and account changes, and can isolate a machine from the network on command. At Northgate the agents answer questions the portal log cannot, such as what ran on a PC after a click. In the second proxy case, the agent on the planning-office PC showed no new processes after the blocked download, which was enough to close it. Isolation is the agent's strongest action, so it needs the right authority and a recorded reason.

### 6.2 Process events

A process event shows which program ran, who ran it, what started it and the command line. Unusual parents, such as a word processor starting a command shell, are worth a look. For the finance PC that visited invoice-portal.example, Carlos would look for processes started by the browser shortly after the visit. A browser starting a script interpreter would be worth a closer look, while a browser opening a new tab is normal. The parent process and the command line are what separate those two cases.

### 6.3 Account events

Windows records account creation, group changes and logons with event IDs; the SIEM labels them so analysts need not memorise numbers. When Carlos checked the payroll admin in A2, the SIEM showed the account creation and the group change by label rather than by number. He could then match the creator and time against the approved change ticket. Labels also reduce mistakes when analysts move between Windows, the portal and other systems. The SIEM keeps the original event ID alongside its label for anyone checking raw logs.

### 6.4 Confirming compromise

For the parks01 case, Carlos checks the remote-access portal session: after logging in, parks01 opened the council's internal file share and listed folders for 6 minutes, then disconnected. No files were downloaded according to the share's audit log. The six minutes of folder listing fit the timeline: logon at 09:09, browsing ends at 09:15. The share's audit log showing no downloads is what keeps INC-0417 at minor severity, with one account and no data taken. Carlos still records that listing folders revealed their names to the outsider.

### 6.5 Isolation

Isolating cuts a machine off from the network except from the EDR console. It stops spread but also stops the user working, so it needs the right authority and a reason. For parks01, isolation was not needed, because the depot tablet was idle and not involved. Disabling the account stopped the outsider's access without stopping any device. Under the playbook, isolating a server would need the IT manager, so Carlos considers the smaller action first and records why isolation was unnecessary.

### 6.6 Health of agents

Missing agents mean missing data. Northgate's console lists PCs whose agents have not reported in 24 hours; IT fixes them weekly. A PC without a working agent is invisible to the SOC, so an attacker there would leave no endpoint trace. The 24-hour list turns this into a weekly task for IT. The same idea appears later at server level, when Carlos finds 18 servers not sending logs during the maturity assessment. Carlos checks the list when a case involves a PC, because a silent agent changes what the absence of evidence means.

### Timeline building

Carlos lists every event in time order across portal, share and EDR, which makes gaps and links obvious to reviewers.

### Worked example

Carlos finds the gardeners' shared tablet did not log in at 09:09; it was in the depot, idle. The session came only through the portal from 203.0.113.80. This confirms the logon was not a gardener, so the account is disabled and the case becomes an incident.

> **Synthetic case.** Sessions and events are synthetic.

### Errors and limits

EDR records what the agent can see; it misses machines without agents and actions on network devices.

### Exercises

- **EX021 — EDR records.** List four kinds of event an EDR records. *Rubric:* 3 = processes, files, network, accounts; 2 = three; 1 = one; 0 = none.
- **EX022 — Suspicious parent.** Give an example of an unusual parent process. *Rubric:* 3 = word processor starting a shell; 2 = partial; 1 = vague; 0 = none.
- **EX023 — parks01 activity.** What did parks01 do after logging in? *Rubric:* 3 = listed file share folders 6 min; no downloads; 2 = partial; 1 = vague; 0 = none.
- **EX024 — Isolation trade-off.** What is the trade-off of isolating a machine? *Rubric:* 3 = stops spread but stops user working; needs authority; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Endpoint and access data confirm or rule out compromise; isolation is powerful and needs authority.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Email and phishing alerts

### Learning outcomes

You will (1) explain why email is a common entry point; (2) read email gateway alerts; (3) handle user-reported phishing; (4) coordinate message removal and user follow-up.

### 7.1 Why email

Phishing emails try to trick people into opening attachments, entering passwords on fake sites or approving payments. They are one of the most common starting points of incidents. At Northgate, the finance case followed this pattern: an 'Overdue invoice' email with a link to invoice-portal.example, sent to thirteen staff. One finance officer, at the PC 10.2.0.31, entered her password on the page. Phishing aims at people rather than systems, so the gateway, user reports and proxy logs each play a part in catching it. The rest of this chapter follows that case step by step.

### 7.2 Gateway alerts

The email gateway scans messages and flags suspicious senders, links and attachments. It blocks many but not all. The 'Overdue invoice' email got through because its domain was newly registered and had no bad reputation yet. Gateway alerts are still useful for catching known senders and attachments, but the SOC cannot assume that a delivered message was checked and judged safe. User reports through the button fill some of the gap the gateway leaves. Carlos records which gateway checks the message passed, so the email team can judge whether a rule change is needed.

### 7.3 User reports

Northgate staff have a "report phishing" button. Reports go to the SOC queue. Each report gets a reply, even if the message was harmless, so people keep reporting. The finance case started with exactly such a report from a finance officer. Without the button, the email would have stayed in thirteen mailboxes and nobody would have searched the proxy for clicks. Replying to every report, even harmless ones, keeps staff reporting, which is how the SOC learns about messages the gateway missed. The SOC answers each report within the working day so that staff see their effort noticed.

### 7.4 The finance case

On Carlos's third day, a finance officer reports an email titled "Overdue invoice" with a link to invoice-portal.example. The gateway had let it through. Twelve other staff received it. The thirteen recipients define the search: Carlos needs to know which of them clicked and whether anyone entered a password. The gateway console shows the sender, route and link target as text, so he can triage without visiting invoice-portal.example. The headers show a newly registered domain, not the real supplier.

### 7.5 Removal

With approval, the email team removes the message from all twelve mailboxes and blocks the sender and domain. Removing the message stops further clicks, but it does not undo clicks that already happened, which is why the proxy search follows. Blocking the domain also protects staff who might receive a forwarded copy. Approval is required because removing mail from mailboxes touches staff's accounts. The email team records how many copies were removed, so the count of thirteen recipients can be checked against the gateway's own figures.

### 7.6 Follow-up

Carlos checks proxy logs (chapter 8) for anyone who clicked, and asks those users whether they entered a password. The proxy search runs from the email's arrival until its removal, so visits outside that window are not wrongly linked to it. Asking users is still needed, because the proxy shows a visit but not whether a password was typed. The finance officer at 10.2.0.31 confirmed she had entered hers. Users are asked politely and without blame, since honest answers depend on staff not fearing trouble for clicking.

### 7.7 Training link

The council's awareness team uses the anonymised example in next month's staff bulletin. Using the case in training makes the example real for staff without naming the finance officer. The bulletin can show the 'Overdue invoice' subject and the look of the link, so staff recognise the next one. The example is anonymised, consistent with the no-blame approach in the rest of the response. The bulletin also reminds staff where the report button is and thanks those who used it in the finance case.

### Checking the message safely

Carlos never opens suspicious links on his own PC. He views the message headers in the gateway console, where sender, route and link targets are shown as text. Headers revealed the message came from a newly registered domain, not the supplier it claimed to be from. These checks are enough for triage without visiting the site.

### Worked example

Of the 13 recipients, one finance PC, 10.2.0.31, visited the link twice. The user admits entering her password. Carlos asks IT to reset it and checks her account's sign-ins: none from new locations since. The case is contained within an hour.

> **Synthetic case.** Emails, users and addresses are synthetic.

### Errors and limits

Users may not admit clicking; logs fill the gap but never fully.

### Exercises

- **EX025 — Why reply.** Why reply to every report? *Rubric:* 3 = keeps people reporting; 2 = partial; 1 = vague; 0 = none.
- **EX026 — Recipients.** How many staff received the email? *Rubric:* 3 = 13 (reporter plus 12); 2 = partial; 1 = wrong; 0 = none.
- **EX027 — Removal steps.** What two actions followed approval? *Rubric:* 3 = removed from mailboxes; blocked sender and domain; 2 = one; 1 = vague; 0 = none.
- **EX028 — Password entered.** What was done for the user who entered her password? *Rubric:* 3 = reset; sign-ins checked; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Treat phishing reports quickly, remove and block, find clickers and reset credentials.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Network and proxy logs

### Learning outcomes

You will (1) read web proxy logs; (2) match traffic against indicators; (3) identify which hosts need checking; (4) understand limits of network data.

### 8.1 Proxy logs

A web proxy records which internal host visited which domain and when. It is ideal for answering "who clicked?". In the finance case, the proxy log showed that only one of thirteen recipients, the finance PC at 10.2.0.31, visited invoice-portal.example, and it did so twice. That narrowed the password reset to one user rather than all thirteen recipients. The lab below repeats this search on a small synthetic sample with a list of indicators. The time window for that search runs from the email's arrival to its removal.

### Lab — matching indicators

```python
"""Match synthetic proxy-log domains against a synthetic indicator list."""
iocs = {"invoice-portal.example", "update-check.example", "cdn-files.example"}
proxy = [("10.2.0.14", "council.example"), ("10.2.0.31", "invoice-portal.example"), ("10.2.0.31", "invoice-portal.example"),
         ("10.2.0.52", "news.example"), ("10.2.0.77", "cdn-files.example"), ("10.2.0.14", "mail.example")]
hits = {}
for host, dom in proxy:
    if dom in iocs:
        hits.setdefault(host, set()).add(dom)
for host in sorted(hits):
    print(host, sorted(hits[host]))
print("hosts to check:", len(hits), "of", len({h for h, _ in proxy}))
```

Run with `python3 lab_ioc.py`. Verified output:

```text
10.2.0.31 ['invoice-portal.example']
10.2.0.77 ['cdn-files.example']
hosts to check: 2 of 4
```

### 8.2 Lab result

Of four hosts in the sample, two contacted domains on the indicator list: 10.2.0.31 visited invoice-portal.example twice (the finance PC from chapter 7), and 10.2.0.77 visited cdn-files.example. The second hit came from an indicator unrelated to the phishing email, which is why it needed its own check. 10.2.0.77 matched cdn-files.example, which came from the national alert, not the email. Carlos therefore treats it as a separate question and opens its own case rather than adding it to the phishing incident. The lab counts four distinct hosts in the sample, so two of four needed checking.

### 8.3 The second host

10.2.0.77 was not in the phishing case. Carlos checks: it is a planning-office PC; cdn-files.example came from a separate list of indicators from a national alert. The visit was a single download blocked by the proxy. Opening a separate case keeps the finance incident record clean and lets each case close on its own evidence. The block at the proxy meant the file never arrived, and the endpoint agent showing no new processes confirmed nothing ran. The national alert was the source of the indicator, rated reliable.

### 8.4 Firewall logs

Firewalls record allowed and blocked connections by address and port; they help when traffic bypasses the proxy. If an attacker's tool connected to an address directly, bypassing the proxy, only the firewall would record it. In Northgate's cases the proxy answered most questions, but the firewall log is the check that the finance PC made no other unexpected outbound connections after its two visits to invoice-portal.example. Carlos checks the firewall logs for the same time window as the proxy search, from the email's arrival to its removal.

### 8.5 Encryption

Most web traffic is encrypted; proxies see domains but often not full addresses or content. For the finance case, seeing the domain was enough: invoice-portal.example appeared twice for 10.2.0.31. The proxy could not show what the officer typed on the page, so confirming the password entry needed her own account. When content matters, other sources such as the endpoint agent must fill the gap. The proxy's limits are written into the case note so readers do not assume it saw more than domains.

### 8.6 Indicators expire

Domains on indicator lists get reused or cleaned up; old indicators cause false alarms. invoice-portal.example may be abandoned or taken over by someone else within months. An old indicator then flags innocent visits and wastes analysts' time, which is why Northgate sets review dates on indicators and drops those no longer reported. The blog list rated unknown is never used for automatic blocking. Each indicator in Northgate's list carries the date it was added and its source rating, so stale entries are easy to find.

### Time windows

Carlos searches the proxy logs from the time the phishing email arrived until it was removed. Visits before arrival cannot be linked to the email, and visits after removal suggest another source of the link, such as a forwarded copy on a personal device. Bounding the search by time keeps the result small and relevant, and it makes the reasoning easy to explain to reviewers.

### Recording the search

Carlos saves the exact proxy query in the case so others can repeat it.

### Worked example

Carlos opens a second, low-priority case for 10.2.0.77, confirms the endpoint agent shows no new processes after the blocked download, and closes it with evidence. The finance case is linked to the phishing incident.

> **Synthetic case.** Hosts and domains are synthetic and use reserved example names.

### Errors and limits

Matching indicators finds known bad things only; new domains will not match.

### Exercises

- **EX029 — Lab hits.** Which hosts matched and what domains? *Rubric:* 3 = 10.2.0.31 invoice-portal; 10.2.0.77 cdn-files; 2 = partial; 1 = one; 0 = none.
- **EX030 — Second host outcome.** What was found on 10.2.0.77? *Rubric:* 3 = planning PC; download blocked; no new processes; closed; 2 = partial; 1 = vague; 0 = none.
- **EX031 — Encryption limit.** What can proxies see in encrypted traffic? *Rubric:* 3 = domains, often not content; 2 = partial; 1 = all; 0 = none.
- **EX032 — Indicator limits.** Give one limit of indicator matching. *Rubric:* 3 = only known bad; old indicators false alarms; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Proxy and firewall logs show who went where; indicators help but expire and miss new threats.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Threat intelligence basics

### Learning outcomes

You will (1) explain what threat intelligence is; (2) distinguish indicators from behaviours; (3) judge source reliability; (4) use intelligence to guide monitoring.

### 9.1 What it is

Threat intelligence is information about threats that helps you decide what to do. Useful intelligence is timely, relevant to your organisation and actionable. For Northgate, the sharing group's warning about guessing against council portals met all three tests. It arrived within days of the parks01 case, it concerned exactly the kind of portal the council runs, and it pointed to an action, MFA. A report about mobile banking apps would fail the relevance test for the council. Carlos checks each new report against these three tests before spending time on it.

### 9.2 Indicators and behaviours

Indicators are specific values such as domains and addresses; they change quickly. Behaviours, described in MITRE ATT&CK, change slowly. The pyramid of pain idea says behaviours are harder for attackers to change. 203.0.113.80 is an indicator; the attacker can switch to another address tomorrow. The behaviour, many failures followed by a success from one source, stays the same whatever address is used. That is why Carlos's new rule detects the behaviour itself rather than simply blocking the single address seen on Monday.

### 9.3 Sources

Northgate receives a national government alert feed, a local-government sharing group and vendor reports. Each is rated for reliability based on past accuracy. The national feed supplied cdn-files.example, which matched the planning-office PC, and the sharing group supplied the warning about portal guessing. Rating each source helps Carlos decide how far to trust an item. A reliable source's indicator can be searched at once; an unknown one waits for a low-priority check. The ratings are reviewed twice a year from the count of indicators that led to real findings.

### 9.4 Relevance

A report about attacks on councils' remote-access portals is highly relevant after the parks01 case; a report about a mobile banking app is not. Relevance depends on what Northgate runs and has just experienced. The parks01 case proved the portal was a target, so reports about portal attacks moved up in priority. Reading every report equally would waste the small team's time on threats the council does not face. Relevance is reassessed after each incident, since a new case can make an old report suddenly important.

### 9.5 Acting on intelligence

The sharing group warns that password guessing against council portals has increased. Aisha asks IT to require multi-factor authentication on the portal for all accounts, including shared ones. This is intelligence turning into a control that IT can actually configure. The warning combined with Northgate's own case justified the cost of MFA, including for shared accounts that were later replaced. The guessing attempt against a councillor's account in the rule's first live month was stopped because MFA had been enabled by then. The MFA change also covered shared accounts until they were replaced with named ones.

### 9.6 Sharing back

Northgate shares its own anonymised indicators (203.0.113.80 and the invoice domain) with the group. Sharing back is what makes the group useful to everyone. Other councils can search their portal logs for 203.0.113.80 and the invoice domain. Anonymising removes parks01, the finance officer and any details that would identify staff, while keeping the indicators and times that others need. Carlos removes staff names and internal host addresses before anything leaves the council. Aisha approves each item, because sharing is an external disclosure even when anonymised. The sharing group's own handling rules then decide which member councils may see it.

### Rating reliability

Northgate rates each source on past accuracy: reliable, usually reliable or unknown. The national feed and sharing group are reliable; a free blog list is unknown and its indicators are used only for low-priority searches, never automatic blocking. Ratings are reviewed twice a year when Carlos and Aisha count how many indicators from each source led to real findings.

### Keeping it short

Notes stay to one paragraph so busy managers actually read them.

### Worked example

Carlos writes a one-paragraph intelligence note: "Password guessing against council portals rising (sharing group, reliable). Northgate affected 09:04 Monday; parks01 compromised. Recommend MFA on portal; monitor for success after failures; share indicators." Aisha forwards it to the IT manager.

> **Synthetic case.** Feeds and reports are invented.

### Errors and limits

Intelligence can be wrong or late; combine it with your own data.

### Exercises

- **EX033 — Useful intelligence.** Give three qualities of useful intelligence. *Rubric:* 3 = timely, relevant, actionable; 2 = two; 1 = one; 0 = none.
- **EX034 — Indicators vs behaviours.** Why focus on behaviours? *Rubric:* 3 = change slowly; harder for attackers to change; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Action taken.** What action followed the sharing-group warning? *Rubric:* 3 = MFA on portal for all accounts; 2 = partial; 1 = vague; 0 = none.
- **EX036 — Sharing back.** What did Northgate share? *Rubric:* 3 = 203.0.113.80 and invoice domain, anonymised; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Intelligence guides action when it is relevant and trusted; share back to help others.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — The incident response process

### Learning outcomes

You will (1) describe the incident response life cycle in NIST SP 800-61r3; (2) explain roles during an incident; (3) open, run and close an incident record; (4) link response to CSF 2.0.

### 10.1 The life cycle

NIST SP 800-61 Revision 3 (Nelson et al., 2025) places incident response within CSF 2.0: preparation through Govern, Identify and Protect; detection and analysis through Detect; response through Respond; and recovery through Recover, with lessons feeding improvement. For INC-0417, preparation had gaps, such as no MFA on the portal and a shared account. Detection and analysis covered 09:04 to 09:40, response the 09:52 account disable, and recovery the named accounts created for the gardeners that day. The lessons then fed back into preparation through the MFA plan and the new detection rule.

### 10.2 Roles

An incident lead coordinates, analysts investigate, IT acts on systems, communications handles messages and a manager approves big decisions. In a small SOC one person may hold several roles, but each must be named. In INC-0417 Carlos was analyst and, for a minor incident, effectively lead, while IT created named accounts and the IT manager approved the MFA plan. Naming each role in the record, even when one person holds several, stops tasks being assumed by everyone and done by no one.

### 10.3 The record

The incident record holds a timeline, decisions, evidence references, actions and owners. Carlos opened INC-0417 for the parks01 compromise. INC-0417's record holds the timeline from 09:04 to 10:30, the decision to disable parks01 at 09:52, references to the portal and share logs, and the owners of each lesson. Anyone picking it up later can see what happened and why each step was taken. Evidence references point to copies saved in the case folder with time stamps, not to searches in the SIEM alone.

### 10.4 Severity levels

Northgate uses three levels: minor (one account, no data), significant (data exposure or several systems) and major (service disruption). INC-0417 is minor. INC-0417 is minor because one shared account was affected and the share's audit log shows no downloads. Had files been downloaded, it would have become significant, since data exposure triggers that level. The level decides who is told and how quickly, including the data protection officer. The level is reviewed whenever new evidence appears, so it can rise or fall during the case.

### 10.5 Closure

An incident closes when containment is confirmed, systems are restored and lessons are recorded. For INC-0417, containment was confirmed when parks01 was disabled and no further logons came from 203.0.113.80. Restoring service meant named accounts for the gardeners, and lessons were recorded with the IT manager as owner. Closing before all three would leave loose ends that nobody tracks. Aisha checks all three conditions before INC-0417 is marked closed. The INC-0417 record shows the date on which each of the three conditions was met.

### 10.6 Lessons

A short review asks what happened, what went well, what to change, with owners and dates. INC-0417's review produced two changes, named accounts and MFA within two weeks, each with an owner. The review asks what went well too, such as linking the 09:04 and 09:09 alerts quickly. Without owners and dates, lessons tend to stay as notes rather than become changes. The INC-0417 review is held within a week of closure, while details are still fresh in everyone's memory and notes.

### Evidence handling

Logs and screenshots used in an incident are saved to a case folder with time stamps and who saved them, so findings can be checked later. Original logs are left in the SIEM; copies go to the folder. If an incident might lead to disciplinary or legal action, the information governance lead is told early so evidence is kept properly from the start.

### Worked example

INC-0417 timeline: 09:04 guessing; 09:09 parks01 logon; 09:15 file-share browsing ends; 09:40 Carlos confirms tablet idle; 09:52 account disabled; 10:30 MFA plan agreed. Lessons: replace shared accounts with named accounts for gardeners; MFA on portal within two weeks; owner: IT manager.

> **Synthetic case.** The incident record is invented.

### Errors and limits

Real incidents rarely follow the stages in order; the cycle is a guide.

### Exercises

- **EX037 — Life cycle link.** How does SP 800-61r3 relate to CSF 2.0? *Rubric:* 3 = maps response to CSF functions; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Five roles.** Name the roles in an incident. *Rubric:* 3 = lead, analysts, IT, communications, manager; 2 = four; 1 = two; 0 = none.
- **EX039 — Severity.** Why is INC-0417 minor? *Rubric:* 3 = one account, no data taken; 2 = partial; 1 = vague; 0 = none.
- **EX040 — Lessons.** Name two lessons from INC-0417. *Rubric:* 3 = named accounts for gardeners; MFA on portal; 2 = one; 1 = vague; 0 = none.

### Synthesis

A clear process, named roles and a good record carry an incident from alert to lessons.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Containment and communication

### Learning outcomes

You will (1) choose containment actions proportionate to risk; (2) get the right approvals; (3) communicate with users, managers and partners; (4) avoid spreading alarm.

### 11.1 Options

Disable an account, reset a password, block an address, isolate a machine or remove an email. Each has a cost to the business. For parks01, the options were disabling the account, resetting its password, blocking 203.0.113.80 or isolating the depot tablet. Each stops a different part of the harm and costs something different: the gardeners lose their login, or a device stops working. Carlos chose by asking what the outsider was actually using. The playbook lists each option with who may approve it.

### 11.2 Proportion

Choose the smallest action that stops the harm. For parks01, disabling the account was enough; isolating the depot tablet was not needed because it was not involved. The outsider used only the parks01 account through the portal, so disabling it removed their access completely. Isolating the tablet would have stopped the gardeners working without affecting the outsider at all. Proportion keeps the council running while still stopping the harm. Carlos records why isolation was not used, so a reviewer sees it was considered.

### 11.3 Approvals

Northgate's playbook lets analysts disable accounts and block addresses alone; isolating servers needs the IT manager. These rules let Carlos act at 09:52 without waiting for anyone, because disabling an account is pre-approved. Isolating a server affects many users and services, so the IT manager decides. Knowing the boundary in advance avoids delays during an incident and prevents analysts overstepping. Any action outside these limits waits for approval, even during a busy incident. The approval is recorded in the incident record with its time.

### 11.4 Talking to users

The parks supervisor is told: "Your team's shared login was used by someone outside the council this morning. We have disabled it. IT will set up individual logins today." Plain words, no blame. The message tells the supervisor what happened, what was done and what comes next, without technical terms. It does not suggest that any gardener caused the problem by choosing a weak password. Saying 'IT will set up individual logins today' answers the supervisor's real concern, which is whether the team can keep working.

### 11.5 Managers

A short email to the head of IT and the information governance lead sets out facts, actions and next steps. Managers need enough to decide and to answer questions from above. For INC-0417 the email stated the outsider's logon, the six minutes of folder listing, the disabled account and the MFA plan. The information governance lead receives it because staff accounts and possible data were involved. The email goes out the same morning, after Aisha checks the wording for accuracy and tone.

### 11.6 Data protection

If personal data might have been exposed, the data protection officer must be told early; for parks01 no personal data was accessed. The share's audit log showed only folder listing, with no files opened or downloaded, which is why no personal data was considered accessed. Had the finance officer's account been used after her password was entered, the same check would apply to her mailbox. Telling the officer early leaves time for any legal deadlines. The data protection officer is still told about the finance officer's password case.

### External partners

Sometimes containment involves others: the remote-access vendor, the internet provider or a national cyber centre. Northgate keeps a contact list with phone numbers and what each partner can do. In INC-0417, Carlos reports 203.0.113.80 to the national centre through its online form after Aisha's approval, adding the times and the type of activity seen. The centre may link it with reports from other councils and issue a warning, which is how the sharing system improves defences for everyone.

### Worked example

The gardeners need to log timesheets by Friday. Carlos asks IT to create named accounts the same day, so the containment does not stop payroll for the parks team.

> **Synthetic case.** Communications are invented.

### Errors and limits

Over-containment can cause more harm than the attack; under-containment lets it continue.

### Exercises

- **EX041 — Proportion.** Why was the tablet not isolated? *Rubric:* 3 = not involved; smallest action enough; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Approval rule.** Which action needed the IT manager? *Rubric:* 3 = isolating servers; 2 = partial; 1 = vague; 0 = none.
- **EX043 — User message.** What made the supervisor message good? *Rubric:* 3 = plain, facts, action, no blame; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Business impact.** How was payroll protected? *Rubric:* 3 = named accounts created same day; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Contain proportionately, with the right approval, and communicate plainly to everyone affected.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Detection engineering basics

### Learning outcomes

You will (1) explain the detection engineering cycle; (2) write a detection idea in plain language and Sigma-style structure; (3) test rules with synthetic events; (4) document rules for analysts.

### 12.1 The cycle

Detection engineering turns knowledge about threats into rules: pick a behaviour, find the data that shows it, write the rule, test it, deploy it, then measure and tune. It is a loop, not a one-off task. For Carlos the cycle starts from INC-0417, a behaviour the SOC has now seen. The loop matters because the first version of a rule is rarely right; the live month later shows one benign and one real firing, and measuring those is what tells him whether to tune.

### 12.2 Choosing a behaviour

After INC-0417, Aisha asks Carlos to write a rule for "successful logon from a source that had many failures shortly before". The behaviour matches ATT&CK's brute-force technique and is visible in portal logs. Choosing a behaviour seen in a real case gives the rule a known test: it must fire on the Monday log. Portal logs already hold the needed fields, source, user, result and time, so no new data collection is required before writing the rule. The rule's documentation page links back to INC-0417 so reviewers can see the original pattern.

### 12.3 Structure

Sigma rules have a title, description, log source, detection condition, false-positive notes and level. Writing the idea in this structure, even for a SIEM that uses its own language, forces clarity: Carlos writes log source "remote-access portal authentication", condition "success where same source had 20 or more failures in previous 15 minutes", level high. The 15-minute window is wider than the original failure rule's ten minutes, so a slower guesser is still linked to the success. The structure also records expected false positives before the rule goes live.

### 12.4 Testing

Carlos replays the synthetic Monday log in a test index. The rule fires once, at 09:09, for parks01. He also replays a week of normal logs: it does not fire. Testing the rule both ways, against attack and normal logs, matters. Firing on the Monday log shows the rule catches what it was built for, while staying silent on a normal week shows it will not flood the queue. A rule tested only on the attack would give no idea of its false positives. Both replays are saved with the rule as its test record.

### 12.5 Documentation

Each rule gets a short page: what it detects, why, data needed, expected false positives and first triage steps. The page lets an analyst who has never seen the rule handle its first alert. In the first live month, the forgotten-password case was closed in two minutes because the triage steps said to check whether the user could be reached and confirm. Without documentation, the same alert might take a new analyst much longer to close. The page is linked from the alert itself, so the triage steps are one click away.

### 12.6 Review

Another analyst reviews logic and documentation before deployment. A second reader catches mistakes such as a window set to 15 seconds instead of minutes, or a condition that never matches. The review also checks the documentation is clear to someone who did not write the rule. Carlos's rule passed this review before going live on the council's SIEM. The reviewer's name and the review date are both recorded on the rule's page. Changes after review need the same check again before deployment.

### Rule naming

Rules use clear names that state the behaviour so analysts recognise them in a busy queue.

### Worked example

In the first month live, the rule fires twice: once for a staff member who forgot a new password 25 times from home and then got it right (benign, closed in two minutes thanks to the triage steps) and once for a real guessing attempt against a councillor's account, stopped because MFA had since been enabled.

> **Synthetic case.** Rules and events are synthetic.

### Errors and limits

A rule tested on one replay may still miss variations, such as guessing spread across many sources.

### Exercises

- **EX045 — Cycle steps.** List the steps of the detection cycle. *Rubric:* 3 = behaviour, data, write, test, deploy, measure/tune; 2 = four; 1 = two; 0 = none.
- **EX046 — Sigma fields.** Name four fields of a Sigma rule. *Rubric:* 3 = title, description, log source, detection, false positives, level (four); 2 = two; 1 = one; 0 = none.
- **EX047 — Test results.** What did testing show? *Rubric:* 3 = fired once at 09:09; not on normal week; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Live firings.** Describe the two live firings. *Rubric:* 3 = forgotten password benign; real guessing on councillor stopped by MFA; 2 = partial; 1 = one; 0 = none.

### Synthesis

Detection engineering is a tested, documented, reviewed loop.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Tuning and false positives

### Learning outcomes

You will (1) define false positives and false negatives; (2) measure a rule's usefulness; (3) tune rules without hiding real threats; (4) record tuning decisions.

### 13.1 Definitions

A false positive is an alert that is not a real problem; a false negative is a real problem that raised no alert. Axelsson (2000) showed that when real attacks are rare, even accurate detectors produce mostly false alarms; this is the base-rate problem. At Northgate, most alerts on most days are false positives, even from well-written rules, because real attacks are rare. The 'admin tool used' rule shows this: 220 alerts and two real cases. A false negative is harder to see, because nothing appears in the queue to count.

### 13.2 Measuring

For each rule Carlos counts alerts in a month and how many were real. The "admin tool used" rule fired 220 times; 2 were real. Two real cases out of 220 means about 1 in 110 alerts mattered, so analysts spent most effort on harmless activity. The analysts' marks on closed alerts, real, benign or unclear, supply these numbers. Without them, Carlos could not tell which rules need tuning first. Analysts who mark alerts carefully make this measurement possible, which is why marking is part of triage.

### 13.3 Tuning options

Exclude known safe sources, raise thresholds, add context such as time of day, or combine with another signal. Each option risks missing something. Excluding a source narrows what the rule sees, raising a threshold can let slow attacks through, and time-of-day context can miss an attacker working office hours. Carlos picks the option that removes the most noise while keeping the real cases, and records the risk he accepted. No option is free, so each tuning change states which kind of miss it accepts. Carlos discusses each trade-off with Aisha before applying a tuning change to a live rule.

### 13.4 The admin-tool rule

Most firings were IT staff using the tool from their own machines. Carlos excludes the IT admin workstations by name, keeping alerts for the tool used anywhere else. The real cases came from machines outside the IT admin workstations, so excluding those named machines removed the noise without losing them. Excluding all IT staff accounts instead would have been broader and could hide an attacker using a stolen IT account on another machine. The named workstations are listed in the tuning note, so a departed admin's machine can be spotted and removed.

### 13.5 Recording

The tuning note states the change, reason, expected effect and review date. For the admin-tool rule, the note says IT admin workstations were excluded by name because they produced most firings. It expects alerts to fall sharply while keeping cases from other machines, and it sets a quarterly review date. Anyone questioning the rule later can see why it changed. The tuning note is stored with the rule's documentation page in the SOC's knowledge base. Anyone reviewing the admin-tool rule months later can therefore find the reason for the exclusion quickly. The review date is also added to the team's calendar.

### 13.6 Watching after

In the next month the rule fires 14 times, 2 real. The exclusion list is reviewed quarterly so departed staff's machines are removed. Alerts fell from 220 to 14 a month, while the two real cases were still caught. Precision rose from about 1 in 110 to 1 in 7. The quarterly review of the exclusion list keeps it from growing stale as staff and machines change. The analysts' marks confirm the two real cases each month. Carlos keeps the monthly counts with the tuning note, so the next review starts from them.

### 13.7 Research context

Sommer and Paxson (2010) warned that detection systems which seem accurate in testing often struggle in real environments; local tuning is how SOCs cope. Northgate's experience fits this warning: the admin-tool rule looked reasonable on paper but produced 220 alerts in a real month. Only local measurement and tuning, based on the analysts' marks, made it useful. Rules shared through Sigma still need the same local tuning before they suit the council. The paper's point is that testing alone cannot guarantee real-world performance.

### Feedback from analysts

Analysts mark each closed alert as real, benign or unclear. These marks give Carlos the numbers he needs for tuning, so marking honestly is part of every triage.

### Review dates

Every tuning change gets a review date, and Carlos checks the rule's real-case count again on that date before keeping it.

### Worked example

An analyst asks to silence the rule entirely. Carlos shows the two real cases came from outside the IT workstations, so the exclusion keeps them. Silencing would have missed both.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

Every exclusion is a place an attacker could hide; keep them narrow and reviewed.

### Exercises

- **EX049 — Base rate.** What is the base-rate problem? *Rubric:* 3 = rare attacks mean mostly false alarms; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Tuning change.** How was the admin-tool rule tuned? *Rubric:* 3 = excluded named IT admin workstations; 2 = partial; 1 = vague; 0 = none.
- **EX051 — Result.** What changed after tuning? *Rubric:* 3 = 220 to 14 alerts; 2 real still caught; 2 = partial; 1 = vague; 0 = none.
- **EX052 — Why not silence.** Why not silence the rule? *Rubric:* 3 = would miss the 2 real cases; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Tune narrowly, record why, and check real cases are still caught.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Coverage with ATT&CK and D3FEND

### Learning outcomes

You will (1) map detections to ATT&CK techniques; (2) identify gaps in coverage; (3) use D3FEND to describe defensive techniques; (4) prioritise new detection work.

### 14.1 Mapping

Each rule is tagged with the ATT&CK techniques it detects. A coverage map shows which techniques have rules and which do not. For Carlos's new rule, the tag is the brute-force technique, matching the parks01 case. Each tag lets the map show that this technique now has a tested rule. Tags also help when intelligence warns about a technique, since the SOC can quickly see whether any rule covers it. Rules without a tag are listed separately so they are not forgotten.

### 14.2 Gaps

Northgate's map shows good coverage of initial access by phishing and credential guessing, but little for data moved to cloud storage. Good coverage of phishing and guessing reflects the cases Northgate has handled, including the finance phishing and parks01. The gap around cloud storage means data could be copied out without any alert. Seeing the gap on a map makes it easier to explain to managers why new data sources are needed. The map is updated whenever a rule is added, changed or retired. Gaps are listed with the data source each one would need.

### 14.3 Prioritising

Gaps are ranked by how likely the technique is against councils (from intelligence) and how damaging. Data exfiltration from file shares ranks high. Exfiltration from file shares ranks high partly because the parks01 outsider spent six minutes listing share folders. Had they downloaded files, no rule would have flagged the volume. Ranking by likelihood and damage helps a four-analyst team choose which gaps to close first. The ranking is reviewed each quarter, when new intelligence from the sharing group may move a technique up or down.

### 14.4 D3FEND

MITRE D3FEND (Kaloroumakis and Smith, 2021) is a knowledge graph of defensive techniques, linked to ATT&CK. It helps describe what a control does, such as "user behaviour analysis" or "network traffic analysis". Using D3FEND terms lets Carlos describe the new detections consistently, for example mass file reads as user behaviour analysis. Managers and other councils can then compare controls without reading each rule's logic. D3FEND describes what a control does in general, not whether it actually works at Northgate.

### 14.5 Coverage is not quality

A tagged rule may be noisy, untested or blind on some systems. Northgate marks each mapping as tested or untested. A technique tag shows what a rule is meant to catch, not proof that it does. Marking each mapping as tested shows which rules have been checked against data, as Carlos's rule was with the Monday log. An untested rule may never fire, and a coverage map that hides this would give false comfort to the risk committee. Untested mappings are scheduled for testing in the quarterly rule review. Until then they are shown in a different colour on the table.

### 14.6 Data first

Some gaps exist because data is missing; the cloud storage gap needs proxy logs with upload sizes. Without upload sizes, no rule can tell a large upload to personal cloud storage from ordinary browsing. Collecting that data comes before writing the rule, so the first approved detection depends on a proxy change. Carlos records this data dependency on the coverage table beside the cloud storage gap. IT owns the proxy change, and Carlos tracks it as a dependency for the new rule. Until it is done, the cloud storage gap stays open on the map.

### Presenting coverage

Carlos shows the map as a table rather than a colourful heat map, listing for each technique the rule names, whether they were tested, and the data sources used. Managers find the table harder to misread: a green cell on a heat map can suggest full protection when the only rule is untested. The table also makes clear which gaps are due to missing data and which need new rules.

### Worked example

Carlos proposes three new detections: large uploads to personal cloud storage, mass file reads on the file share by one account, and new mail forwarding rules. Aisha approves the first two for this quarter.

> **Synthetic case.** Coverage values are invented.

### Errors and limits

ATT&CK coverage maps can look reassuring while hiding untested rules.

### Exercises

- **EX053 — Gap found.** What gap did the map show? *Rubric:* 3 = data moved to cloud storage; 2 = partial; 1 = vague; 0 = none.
- **EX054 — Ranking gaps.** How are gaps ranked? *Rubric:* 3 = likelihood against councils and damage; 2 = partial; 1 = vague; 0 = none.
- **EX055 — D3FEND.** What is D3FEND? *Rubric:* 3 = knowledge graph of defensive techniques linked to ATT&CK; 2 = partial; 1 = vague; 0 = none.
- **EX056 — Approved rules.** Which two detections were approved? *Rubric:* 3 = large uploads to personal cloud; mass file reads; 2 = one; 1 = vague; 0 = none.

### Synthesis

Map coverage honestly, find gaps, and fix data before rules.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — SOC metrics

### Learning outcomes

You will (1) choose meaningful SOC metrics; (2) compute median times; (3) avoid metrics that drive bad behaviour; (4) present metrics to managers.

### 15.1 Why measure

Metrics show whether the SOC is improving and where to invest. For Northgate, measurement shows whether changes such as the shift overlap or the playbook change actually helped. Without numbers, the team relies on impressions, which tend to remember dramatic cases and forget routine ones. The lab below measures acknowledge and contain times for six incidents to show what a small set can and cannot say. The same metrics are reported to the council's risk committee each quarter on one page.

### Lab — response times

```python
"""Median minutes to acknowledge and to contain for synthetic incidents."""
from statistics import median
inc = [("I1", 4, 35), ("I2", 12, 60), ("I3", 3, 22), ("I4", 25, 140), ("I5", 6, 41), ("I6", 8, 50)]
ack = [a for _, a, _ in inc]; con = [c for _, _, c in inc]
print("median acknowledge:", median(ack), "min")
print("median contain:", median(con), "min")
print("acknowledged within 10 min:", sum(a <= 10 for a in ack), "of", len(ack))
```

Run with `python3 lab_mttr.py`. Verified output:

```text
median acknowledge: 7.0 min
median contain: 45.5 min
acknowledged within 10 min: 4 of 6
```

### 15.2 Lab result

For six incidents, the median time to acknowledge is 7 minutes and the median time to contain is 45.5 minutes; four of six were acknowledged within 10 minutes. I4, acknowledged after 25 minutes and contained after 140, happened during a shift change. The outlier is why the medians are reported rather than averages. I4 is still reported as its own line, because it shows a process problem worth fixing. Carlos checks whether other slow cases also fell at shift change before recommending the overlap. With six cases, he treats the pattern as a lead rather than proof.

### 15.3 Medians

Medians resist one very long case dragging the average. In the lab, I4's 140 minutes to contain would pull the mean up to 58 minutes, while the median stays at 45.5. The median describes a typical incident better when one case is unusual. The outlier is still reported separately, since it shows the shift-change problem. With only six incidents, one extreme case would move the mean noticeably. Carlos reports both the median and the outlier, so readers see the typical case and the exception.

### 15.4 Bad metrics

Counting closed alerts per analyst encourages closing quickly without care. Northgate avoids it. An analyst rewarded for closures might close the parks01 alerts without checking the tablet or linking the alerts. The measure would look good while the work got worse. Northgate prefers measures that reward care, such as the share of alerts with clear notes. Measures are chosen in the monthly meeting, so analysts can say when one creates the wrong incentive. Aisha drops any measure that the team finds is being gamed.

### 15.5 Better metrics

Time to contain, share of alerts with clear notes, rule precision and percentage of assets sending logs. Each of these measures links to something the SOC itself can change. Time to contain is the measure the playbook change aims at; note quality improves triage handovers; rule precision rose from 1 in 110 to 1 in 7 after tuning; and log coverage tracks the 18 servers found not sending logs. Each one is measured the same way every month, so the trends shown to managers are fair.

### 15.6 Presenting

One page, trends over months, with explanation of outliers. Trends over months show whether changes worked, which one month cannot. Explaining outliers, such as I4 at shift change, stops readers drawing wrong conclusions from one bad case. Keeping it to one page means the risk committee actually reads it. Carlos writes the page and Aisha checks it before it goes to the committee. The page shows six months of trend data where available, and states clearly when a sample, such as six incidents, is too small.

### Data quality for metrics

Metrics are only as good as the times recorded. Carlos finds two incidents where the acknowledge time was entered by hand an hour after the event. Northgate changes the case tool so acknowledge time is captured automatically when an analyst opens the alert, and containment time is captured when the containment action is logged. He also notes that metrics should be compared over the same kinds of cases, since phishing cases are naturally faster to contain than server compromises.

### Using metrics for learning

Metrics are discussed in a monthly team meeting, not used to rank people. The team looks at the slowest cases and asks what made them slow: missing information, unclear ownership, or waiting for approvals. In one meeting, the team discovers that containment waited 30 minutes for a manager's approval to isolate an ordinary PC three times; the playbook is changed so analysts can isolate PCs alone, while disabling accounts was already theirs and servers still need the IT manager.

### Worked example

Carlos's report notes the I4 outlier came at shift change and recommends an overlap of 15 minutes between shifts. Aisha adopts it.

> **Synthetic case.** Incident times are synthetic.

### Errors and limits

Six cases are too few for strong conclusions.

### Exercises

- **EX057 — Lab medians.** Give the two lab medians. *Rubric:* 3 = acknowledge 7; contain 45.5; 2 = one; 1 = vague; 0 = none.
- **EX058 — Why medians.** Why use medians? *Rubric:* 3 = resist long outliers; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Bad metric.** Name a metric that drives bad behaviour. *Rubric:* 3 = closed alerts per analyst; 2 = partial; 1 = vague; 0 = none.
- **EX060 — I4 fix.** What change followed the I4 outlier? *Rubric:* 3 = 15-min shift overlap; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Measure what matters, use medians, avoid perverse metrics and explain outliers.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Shifts, handover and wellbeing

### Learning outcomes

You will (1) organise SOC shifts; (2) write effective handovers; (3) recognise alert fatigue and burnout; (4) support healthy working.

### 16.1 Shifts

Northgate monitors 07:00–19:00 on weekdays with on-call cover at night and weekends. Twelve hours of daytime cover suit a council whose staff mostly work office hours. At night and weekends, alerts go to the on-call analyst, which is why the night checklist and the P1-only rule matter. The parks01 case at 09:04 on a Monday fell well inside staffed hours. The on-call duty rotates weekly among the four analysts, so each covers roughly one week in four. Each analyst knows in advance which weeks they cover, which lets them plan rest around it.

### 16.2 Handover

Each shift ends with a written note: open cases, promised calls, alerts being watched. After the parks01 morning, a handover note would list INC-0417 as open, the promise to call the parks supervisor once named accounts were ready, and the 203.0.113.80 address being watched. The next shift can continue without asking Carlos, who may be off duty. The note is written in the case tool, not on paper, so it is searchable. The incoming analyst reads it before taking new alerts from the queue.

### 16.3 On-call

The on-call analyst carries a phone for P1 alerts only, so sleep is not broken for minor things. Limiting calls to P1 means the on-call analyst can rest and still respond when it matters. A P1 such as a new admin on the payroll server would wake them; a blocked malware alert would wait. The triage scores from the asset list make the line between them clear. The on-call phone receives only P1 alerts from the SIEM. Lower alerts wait in the queue for the morning shift.

### 16.4 Fatigue

Repetitive alerts cause fatigue; analysts start skipping checks. Alahmadi et al. (2022) interviewed and surveyed SOC practitioners and found that floods of false alarms frustrate analysts and erode trust in their tools; fatigue and turnover follow when this goes unaddressed. The I4 outlier and Carlos's skimming of phishing reports late in the shift both fit this pattern. Fatigue is not a personal weakness but a predictable result of repetitive alerts. Tuning noisy rules, such as the admin-tool rule, is therefore also a wellbeing measure.

### 16.5 Support

Rotating tasks, time for projects and learning, and managers who listen. At Northgate this means Carlos rotates to detection work in the afternoons, has four hours a week for learning and can raise problems with Aisha. Each of these measures reduces the repetitive load that leads analysts to skim. A small team cannot do everything, but it can share the dull tasks fairly. Aisha reviews workload with each analyst monthly, during the same meetings she uses for mentoring. Changes such as Carlos's afternoon rotation are agreed with the analyst rather than imposed.

### 16.6 Mistakes

A just culture treats honest mistakes as learning chances. When the case tool showed acknowledge times entered by hand an hour late, the fix was to capture them automatically, not to blame the analysts. Treating mistakes as process problems keeps people reporting them openly to Aisha. Hiding errors would make metrics and incident records less trustworthy. Mistakes are discussed in the monthly meeting, not in front of others during a shift. The discussion focuses on what to change in tools or process, not on who slipped.

### Night cover

On-call analysts have a short checklist for night alerts: confirm the alert, check the asset criticality, take any pre-approved action, and decide whether to wake the incident lead. Everything else waits for the morning shift, with a note. The checklist means a tired person at 03:00 follows the same steps a rested person would, and the morning team picks up the case without confusion.

### Learning time

Each analyst gets four hours a week for learning: a course, a lab exercise or reading. Carlos uses his to practise log searches on synthetic data. Aisha argues that learning time is not a luxury, because the threats and tools change constantly and analysts who stop learning soon struggle with new alerts. Protected learning time also makes the job more attractive, helping a small SOC keep its staff.

### Speaking up

Analysts are encouraged to say when they are tired or overloaded, early.

### Worked example

Carlos notices he skims phishing reports late in the shift. He tells Aisha, who rotates him to detection work in the afternoons.

> **Synthetic case.** Shifts are invented.

### Errors and limits

Small teams have less room to rotate.

### Exercises

- **EX061 — On-call scope.** Why page on-call for P1 only? *Rubric:* 3 = protect sleep; 2 = partial; 1 = vague; 0 = none.
- **EX062 — Handover contents.** What goes in a handover? *Rubric:* 3 = open cases, promised calls, watched alerts; 2 = two; 1 = one; 0 = none.
- **EX063 — Burnout factors.** What did Alahmadi et al. (2022) find about false alarms and analysts? *Rubric:* 3 = frustration and eroded trust in tools; 2 = one of these; 1 = vague; 0 = none.
- **EX064 — Carlos's change.** What change helped Carlos? *Rubric:* 3 = afternoon detection work rotation; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Clear shifts and handovers protect the service; wellbeing protects the people.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Continuous monitoring and SOC maturity

### Learning outcomes

You will (1) explain continuous monitoring per SP 800-137; (2) assess SOC maturity with SOC-CMM; (3) plan improvements; (4) report to governance.

### 17.1 Continuous monitoring

NIST SP 800-137 (Dempsey et al., 2011) describes information security continuous monitoring: ongoing awareness of security, vulnerabilities and threats to support risk decisions. For Northgate, continuous monitoring means knowing at any time which servers send logs, which rules are tested and which threats are rising. The risk committee uses this to decide what to fund. The 18 servers not sending logs are exactly the kind of gap it is meant to reveal. Continuous monitoring covers the SOC's own tools as well as the council's systems. Gaps in either, such as silent agents or servers without logs, are reported to the risk committee.

### 17.2 SOC-CMM

The SOC Capability Maturity Model (van Os, 2016) assesses business, people, process, technology and services domains. Northgate uses the model to see where it is strong and weak across all five domains, not only technology. An honest score in each domain gives a baseline that the next assessment, a year later and using the same method, can be compared against fairly. The five domains deliberately cover much more than the SOC's technology alone. Northgate's assessment is scored from evidence such as logs and records, not from opinion. Carlos's part was collecting evidence for the technology domain, which is how he found the 18 silent servers.

### 17.3 Northgate's assessment

Strong on process documentation, weak on technology coverage and people development. The assessment's findings match what the earlier chapters of this book have shown. Playbooks and procedures were written down, but 18 servers sent no logs and the coverage map showed gaps such as cloud storage. People development was weak, with no training budget per analyst before the plan. The assessment's evidence is kept so the next one can check whether each weakness improved. Results were shared with the whole team, not only managers.

### 17.4 Improvement plan

Three items: log coverage to 95% of servers, training budget per analyst, quarterly rule reviews. Each item addresses a weak area: log coverage for technology, training budget for people, and rule reviews to keep detections tested. The 95% target follows from the 18 servers found missing, 15 of which IT fixed within a month. Each item has a named owner and a measure reported to the risk committee. Progress on all three items is reported to the council's risk committee each quarter. Any item that slips behind its date is explained in a short note beside the table.

### 17.5 Governance

Results go to the council's risk committee each quarter, tying SOC work to CSF 2.0 Govern. Reporting to the risk committee puts SOC gaps alongside other council risks, so spending can be compared. It also makes the SOC accountable for progress on its plan. Linking to Govern shows the SOC's work as part of how the council manages risk. The committee can ask for more detail on any item. The committee also approves the training budget that the people-development item depends on.

### 17.6 Research

Vielberth et al. (2020) surveyed SOCs and found people, process and technology must be balanced. Northgate's assessment shows the same lesson: strong process documentation could not make up for weak technology coverage and people development. The improvement plan balances all three with one item each. A SOC with excellent tools but untrained staff would still miss cases like parks01. The paper supports Aisha's choice to spread the plan across all three areas. Northgate's improvement plan accordingly has one item for each of the three areas.

### Measuring progress

Each improvement item has a measure and a date. Log coverage is measured weekly from the SIEM's list of reporting servers; training is measured by courses completed; rule reviews by the number reviewed per quarter. Progress is shown to the risk committee as a simple table of target, current value and trend, with a short note on any item that slipped and why.

### Assessment honesty

Maturity scores are only useful if honest. Aisha insists the team rate what is actually done, not what is written in documents. A process that exists on paper but is not followed scores low. The first honest assessment looked worse than expected, but it gave a clear baseline; the following year's assessment showed real progress that the risk committee could trust because the starting point had not been inflated.

### Next assessment

The next SOC-CMM assessment is booked a year later, using the same scoring method so results compare fairly.

### Worked example

Carlos helps collect evidence for the SOC-CMM technology domain and finds 18 servers not sending logs; IT fixes 15 within a month.

> **Synthetic case.** Scores are invented.

### Errors and limits

Maturity models describe capability, not effectiveness against real attacks.

### Exercises

- **EX065 — SP 800-137 aim.** What does continuous monitoring support? *Rubric:* 3 = risk decisions with ongoing awareness; 2 = partial; 1 = vague; 0 = none.
- **EX066 — SOC-CMM domains.** Name the five SOC-CMM domains. *Rubric:* 3 = business, people, process, technology, services; 2 = four; 1 = two; 0 = none.
- **EX067 — Weak areas.** Where was Northgate weak? *Rubric:* 3 = technology coverage, people development; 2 = one; 1 = vague; 0 = none.
- **EX068 — Log gap.** How many servers lacked logs and how many were fixed? *Rubric:* 3 = 18; 15; 2 = one; 1 = vague; 0 = none.

### Synthesis

Monitoring continuously and assessing maturity guide steady improvement.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Review and next steps

### Learning outcomes

You will (1) review the whole SOC journey; (2) connect each skill to the case; (3) plan personal development; (4) prepare for further study.

### 18.1 Looking back

From Monday's 46 failures to a tuned, tested rule and MFA on the portal, Carlos has seen the full loop. The loop runs from 46 failures to a rule tested on the Monday log, MFA on the portal and named accounts for the gardeners. Each step taught a different skill, and each depended on the one before. Carlos can now explain to a new trainee why every step was needed. The same chain of steps would apply to any new case he handles at the council.

### 18.2 Skills

Logs, triage, endpoint and network analysis, intelligence, response, detection, tuning, metrics, wellbeing and maturity. Each skill appears in a case: logs and triage in parks01, network analysis in the finance phishing, tuning in the admin-tool rule, metrics in the shift-change outlier. Wellbeing and maturity apply across all of these cases rather than belonging to any single one. The list maps to the eighteen chapters of the course. Carlos's six-month review lists the cases and records that show evidence for each skill.

### 18.3 Development

Carlos plans a certificate course and a lab project on file-share monitoring. The file-share monitoring project follows from the coverage gap and from parks01's six minutes of folder listing, which no rule would have flagged if files had been taken. A certificate course adds structured study to the learning time he already uses. Aisha reviews both plans with him at their next monthly meeting. Both plans include target dates and a concrete way to show results to Aisha and the team.

### 18.4 Mentoring

Aisha meets him monthly to review cases. Monthly reviews let Aisha check Carlos's notes and decisions on real cases and suggest improvements. They also give Carlos a regular place to raise problems early, such as fatigue. Mentoring continues the support he had in his first weeks, now focused on judgement rather than basics. The meetings are booked in advance so busy weeks do not push them out. Each meeting reviews at least one of Carlos's recent cases in detail, including his notes.

### 18.5 Ethics

SOC access to staff activity is powerful; it must be used only for security purposes, under policy. In the finance case, Carlos read only the logs needed to see who clicked, not staff's browsing in general. The SIEM gives access to much more than any case needs, so policy and purpose set the limit. Misusing it would damage trust between the SOC and staff. Any search beyond what a case needs requires a reason recorded in that case's notes for Aisha to see.

### 18.6 Next course

The next stop covers incident response and cyber resilience in depth. The parks01 and finance cases were minor, but larger incidents need deeper response skills, such as handling significant or major incidents with service disruption. The next course builds on the incident process and containment chapters here. It also covers recovery and resilience in more detail than a SOC course can. Carlos's notes from the cases here will be useful material there. The six-month review lists those cases, including INC-0417 and the finance phishing incident.

### What the case taught

The parks01 case shows that a small event touches every part of the SOC. A weak shared password let in an outsider; logs showed the attempt; a rule raised an alert; triage linked the alerts; endpoint and share logs confirmed what happened; a proportionate action stopped it; plain communication kept the parks team working; lessons led to MFA and named accounts; a new detection and better metrics followed. Each chapter of this book covered one link in that chain, and a weakness in any link would have let the outsider stay longer.

### Continuing practice

Skills fade without use. Carlos keeps a personal lab with synthetic logs where he rebuilds detections and practises searches, and he joins the local-government sharing group's monthly call to hear what other councils are seeing. He also volunteers to update one runbook a month, which keeps his knowledge of procedures fresh and improves the documents for everyone on the team.

### Worked example

Carlos's six-month review lists 120 alerts triaged, three incidents led, two rules written and one metric changed.

> **Synthetic case.** Review contents are invented.

### Errors and limits

A technical course covers foundations; deeper study needs practice.

### Exercises

- **EX069 — Full loop.** Summarise the INC-0417 loop. *Rubric:* 3 = alert, triage, contain, lessons, rule, MFA; 2 = partial; 1 = one; 0 = none.
- **EX070 — Ethics.** Why must SOC access be limited? *Rubric:* 3 = powerful; security purposes under policy; 2 = partial; 1 = vague; 0 = none.
- **EX071 — Review numbers.** What did the six-month review list? *Rubric:* 3 = 120 alerts, 3 incidents, 2 rules, 1 metric; 2 = partial; 1 = vague; 0 = none.
- **EX072 — Plan.** Name one development step. *Rubric:* 3 = certificate course or file-share monitoring project; 2 = partial; 1 = vague; 0 = none.

### Synthesis

The SOC is a loop of seeing, deciding, acting and learning.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Carlos Mendes, Aisha Rahman, Northgate Borough Council, parks01 and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** To watch systems for signs of attack or misuse, decide which matter and coordinate the response.

**EX002.** Forty-six failed logons from 203.0.113.80 against the remote-access portal, then a successful parks01 logon at 09:09.

**EX003.** Because the SOC does not own most systems, IT must make changes such as password resets and firewall rules.

**EX004.** Detect and Respond.

**EX005.** Time, source, user, action and outcome.

**EX006.** Because otherwise events appear in the wrong order and the story is confused.

**EX007.** The remote-access portal, domain controllers, endpoint agents and the web proxy.

**EX008.** So past activity can be checked during investigations.

**EX009.** An event is anything logged, an alert is what a rule flagged, and an incident is a confirmed harm or threat.

**EX010.** Twenty or more failed logons from one source within ten minutes.

**EX011.** An open, vendor-neutral format for writing and sharing detection rules.

**EX012.** They share a source, so linking shows the whole story to anyone who picks up the case.

**EX013.** 203.0.113.80 had 46 failures (alert), others 3 and 2; then parks01 succeeded from that source.

**EX014.** It suggests the guessing worked, moving the case to possible compromise.

**EX015.** Passwords are rarely changed and you cannot tell which person used the account.

**EX016.** Disable parks01 and check what it did after 09:09.

**EX017.** To decide quickly whether to close, investigate now or escalate, not to finish the investigation.

**EX018.** A2 (new admin on payroll server, 9, P1) and A4 (finance PC outbound, 6, P2).

**EX019.** For P1 alerts, when unsure, or when an action would affect services.

**EX020.** IT had created the account for a planned upgrade under an approved change; Carlos closed it citing the ticket.

**EX021.** Processes started, files changed, network connections and account changes.

**EX022.** A word processor starting a command shell.

**EX023.** It listed folders on the internal file share for six minutes and downloaded nothing, according to the audit log.

**EX024.** It stops spread but also stops the user working, so it needs authority and a reason.

**EX025.** So staff keep reporting suspicious emails.

**EX026.** Thirteen: the reporter and twelve others.

**EX027.** The message was removed from all mailboxes and the sender and domain were blocked.

**EX028.** Her password was reset and her sign-ins checked for unusual locations.

**EX029.** 10.2.0.31 visited invoice-portal.example and 10.2.0.77 visited cdn-files.example.

**EX030.** A planning-office PC whose single download was blocked; no new processes followed, so the case was closed.

**EX031.** Usually the domain, but not full content.

**EX032.** It finds only known bad domains, and old indicators can cause false alarms.

**EX033.** Timely, relevant and actionable.

**EX034.** Because behaviours change slowly and are harder for attackers to change than indicators.

**EX035.** Requiring multi-factor authentication on the portal for all accounts.

**EX036.** Its anonymised indicators: 203.0.113.80 and the invoice domain.

**EX037.** It places incident response activities within the CSF 2.0 functions.

**EX038.** Incident lead, analysts, IT, communications and an approving manager.

**EX039.** One account was affected and no data was taken.

**EX040.** Replace the shared account with named accounts and add MFA to the portal.

**EX041.** It was not involved; disabling the account was the smallest effective action.

**EX042.** Isolating servers.

**EX043.** It was plain, stated facts and actions, and blamed no one.

**EX044.** IT created named accounts the same day so timesheets could be logged.

**EX045.** Choose a behaviour, find the data, write, test, deploy, then measure and tune.

**EX046.** Title, log source, detection condition and level.

**EX047.** It fired once at 09:09 for parks01 and not at all on a normal week of logs.

**EX048.** One benign forgotten-password case and one real guessing attempt stopped by MFA.

**EX049.** When attacks are rare, even accurate detectors produce mostly false alarms.

**EX050.** By excluding the named IT admin workstations only.

**EX051.** Alerts fell from 220 to 14 a month, and both real cases were still caught.

**EX052.** Because it would have missed the two real cases.

**EX053.** Little coverage for data being moved to cloud storage.

**EX054.** By likelihood against councils and how damaging the technique would be.

**EX055.** A knowledge graph of defensive techniques linked to ATT&CK.

**EX056.** Large uploads to personal cloud storage and mass file reads by one account.

**EX057.** Median acknowledge 7 minutes; median contain 45.5 minutes.

**EX058.** They are not dragged by one very long case.

**EX059.** Counting closed alerts per analyst.

**EX060.** A 15-minute overlap between shifts.

**EX061.** To avoid breaking sleep for minor issues.

**EX062.** Open cases, promised calls and alerts being watched.

**EX063.** Floods of false alarms frustrate analysts and erode their trust in tools.

**EX064.** Rotating to detection work in the afternoons.

**EX065.** Ongoing awareness to support risk decisions.

**EX066.** Business, people, process, technology and services.

**EX067.** Technology coverage and people development.

**EX068.** Eighteen, of which fifteen were fixed within a month.

**EX069.** Alert, triage, containment, lessons, a new rule and MFA on the portal.

**EX070.** Because it is powerful and must only be used for security purposes under policy.

**EX071.** 120 alerts triaged, three incidents led, two rules written and one metric changed.

**EX072.** A lab project on file-share monitoring.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
