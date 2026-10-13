# Security Operations and Blue Team: Bachelor's Course

- Language: English (`en`); course 107, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Eight offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduates who will analyse security data, triage and investigate alerts, and improve detections in a supervised SOC.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the foundation chapters apply mathematics, computing, writing and ethics to security operations, and the specialist chapters follow one university SOC from a phishing campaign that compromised student accounts to a tested capstone detection package. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucas Moreau** | Bachelor's student and student analyst | Invented |
| **Dr. Hana Kim** | Information security manager and SOC supervisor | Invented |
| **Riverton University** | Fictional university with a student-staffed SOC | Invented |
| **Eastbank Youth Centre** | Fictional community placement | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

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

You will (1) use ratios, rates and percentages correctly in security reporting; (2) compare groups of different sizes fairly; (3) recognise misleading numbers; (4) state calculations so others can check them.

### 1.1 Why numbers matter in a SOC

Security teams report numbers constantly: how many phishing emails were reported, how many people clicked, how many accounts were compromised. Decisions about training, filtering and staffing follow from these numbers, so they must be computed and explained correctly.

In the library-fines campaign, Dr. Kim had to decide whether to spend her small training budget on students or staff. A raw count of reports pointed one way and a rate pointed the other, so the choice depended on Lucas computing the right figure and explaining it in a sentence she could repeat to the university's leadership.

### 1.2 The course case

**Lucas Moreau** studies for a bachelor's degree at the fictional **Riverton University** and works part-time in its student-staffed campus security operations centre, supervised by the university's information security manager **Dr. Hana Kim**. In week three of term, a phishing email titled "Library fines overdue" reaches thousands of students and staff.

The campaign runs through the whole book. Early chapters use it to practise counting, programming and writing; later ones follow the same incident through detection, containment and review. Every person, account and figure in it is synthetic, so students can examine it freely without touching anyone's real mail or sign-in records.

### 1.3 Counts versus rates

Students reported 54 emails and staff 41. Raw counts suggest students were more alert, but there are 18,000 students and only 3,200 staff. Rates per 1,000 people make groups of different sizes comparable.

Here that gives 54 ÷ 18,000 × 1,000 for students and 41 ÷ 3,200 × 1,000 for staff. Lucas also checks that both groups received the email at all, since a rate based on the whole population would mislead if the campaign had reached only some faculties. The denominator should be the people who could have reported, which here was everyone, since the email went to the whole university.

### Lab — rates per group

```python
"""Rates and percentages for Riverton campus phishing reports (synthetic)."""
users = {"students": 18000, "staff": 3200}
reported = {"students": 54, "staff": 41}
clicked = {"students": 27, "staff": 6}
for g in users:
    print(f"{g:8} report rate={1000*reported[g]/users[g]:.1f} per 1,000  click rate={1000*clicked[g]/users[g]:.1f} per 1,000  clicks per report={clicked[g]/reported[g]:.2f}")
```

Run with `python3 lab_rates.py`. Verified output:

```text
students report rate=3.0 per 1,000  click rate=1.5 per 1,000  clicks per report=0.50
staff    report rate=12.8 per 1,000  click rate=1.9 per 1,000  clicks per report=0.15
```

### 1.4 Reading the result

Staff reported at 12.8 per 1,000, more than four times the student rate of 3.0. Click rates were similar (1.9 per 1,000 for staff and 1.5 for students), but for every staff report there were only 0.15 clicks, against 0.50 for students. Students clicked about as often but reported much less.

Those ratios come from 27 student clicks against 54 student reports, and 6 staff clicks against 41 staff reports. Together the 33 clickers match the set of clicking accounts analysed in later chapters. Lucas's conclusion for Dr. Kim was that training should encourage students to report, since they already click no more often than staff.

### 1.5 Misleading numbers

Percentages of tiny groups, missing denominators and changing definitions mislead. Always state what was counted, out of how many, over what period.

A department of eight people where two clicked has a 25% click rate, which sounds alarming next to the campus figure but rests on two people. Lucas reports such cases as counts with the group size beside them. If the definition of a "report" changes, for example to include phone calls, he marks the change so trends are not misread.

### 1.6 Showing your working

Lucas writes the formula beside each figure — reports ÷ users × 1,000 — so Dr. Kim can check it in seconds.

Writing the formula also exposes mistakes. In his first draft Lucas divided staff reports by the student population, which produced an implausibly small rate; seeing the formula beside the figure, Dr. Kim spotted it at once. A number with its working can be checked and corrected, while a bare number has to be trusted. Lucas now keeps the formula in the report itself, not only in his notes.

### Worked example

Lucas drafts: "Students reported more phishing than staff (54 vs 41)." Dr. Kim asks him to rewrite with rates. His revision: "Staff reported phishing at 12.8 per 1,000 people versus 3.0 for students; click rates were similar, so student reporting is the gap to address."

> **Synthetic case.** Riverton University, its SOC and all people are invented; figures come from the lab script.

### Errors and limits

Rates from small groups jump around; a department of 20 people with one click has a rate of 50 per 1,000, which says little.

### Exercises

- **EX001 — Fair comparison.** Why compare rates per 1,000 rather than raw counts? *Rubric:* 3 = groups differ in size; rates make them comparable; 2 = partial; 1 = counts fine; 0 = none.
- **EX002 — Lab rates.** Give report and click rates for both groups. *Rubric:* 3 = students 3.0 and 1.5; staff 12.8 and 1.9 per 1,000; 2 = two; 1 = one; 0 = none.
- **EX003 — The real gap.** What does the clicks-per-report ratio reveal? *Rubric:* 3 = students click about as much but report far less (0.50 vs 0.15); 2 = partial; 1 = vague; 0 = none.

### Synthesis

Use rates with clear denominators, show working and question numbers that compare unequal groups.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the hardware and software layers of a computing system; (2) explain how users, applications and services interact; (3) identify where security events are produced; (4) map a campus service end to end.

### 2.1 Layers

A computing system has hardware, firmware, an operating system, applications and the people using them. Security events can arise at each layer, and SOC analysts need to know which layer produced a record to interpret it.

In the phishing case, the fake sign-in page lived on an attacker's server, the stolen password was used at the identity provider, and the mailbox rules were created in the mail service's application layer. Each layer kept different records, so Lucas had to know which one would hold evidence of each step before he could look for it.

### 2.2 Clients and servers

When a student opens webmail, a browser on their laptop (client) talks to a mail service (server) run by a cloud provider. Sign-in is handled by the university's identity provider, which checks the password and, if enabled, a second factor.

This matters for the case because the attacker never touched a victim's laptop. Once the password was stolen, the attacker's own browser became the client, and the identity provider and mail service saw an ordinary sign-in from a different address. The evidence therefore sits on the servers' side, in sign-in and mailbox logs.

### 2.3 Services as chains

One action passes through many systems: laptop, campus Wi-Fi, internet, identity provider, mail service. Each keeps its own logs with its own clock and format.

For the phishing campaign this means a single click can leave traces in the browser, a campus DNS resolver, the identity provider and the mail service, each timestamped by its own clock. Lucas learns early that matching events across these records requires converting them to one time zone and allowing for small clock differences between systems run by different teams.

### 2.4 Where events come from

The identity provider records sign-ins; the mail service records sent messages and rule changes; Wi-Fi controllers record device connections; laptops record local events if managed.

Each source answers a different question. Sign-in logs show who authenticated, from where and whether a second factor was used. Mail logs show rules created and messages sent, which reveal what an attacker did with an account. Wi-Fi logs would show whether a device was on campus, which matters when judging whether a sign-in is unusual.

### 2.5 Managed and unmanaged devices

Staff laptops are university-managed and send logs to the SOC. Student laptops are personal and do not; the SOC sees students only through university services.

In the case, this meant the SOC could not check whether a student's laptop had been infected after clicking; it could only examine the student's university account. For staff, the managed laptop's logs could confirm or rule out anything happening on the device itself. The difference shapes what each investigation can conclude, and Lucas states it in his notes.

### 2.6 Mapping a service

Lucas maps webmail from end to end, listing each component, its owner and its logs.

His map lists the student's browser and laptop as unmanaged with no logs, campus Wi-Fi as owned by the network team with controller logs, the identity provider owned by the identity team with sign-in logs, and the mail service owned by the cloud provider with message and rule logs. Gaps are marked in red. The map fits on one page and is updated when a service changes.

### 2.7 Why maps help

When the phishing campaign begins, the map tells analysts which logs to check for each question.

For example, when asked whether a suspicious sign-in came from campus, Lucas's map pointed him straight to the Wi-Fi controller logs, and also showed that those logs were not forwarded to the SOC. That gap explained why the question could not be answered quickly, and it became one of the improvements recorded after the incident, with the network team as owner and a target date.

### Clocks across systems

Each system stamps events with its own clock. The SOC converts all times to UTC so events from laptops, identity and mail line up.

### Worked example

Lucas's map shows that the SOC receives identity-provider and mail-service logs but not Wi-Fi controller logs. Dr. Kim notes that without Wi-Fi logs, the SOC cannot tell whether a suspicious sign-in came from campus. Forwarding them becomes a backlog item.

> **Synthetic case.** Systems and maps are invented.

### Errors and limits

Maps simplify; cloud services may change internal components without notice.

### Exercises

- **EX004 — Event sources.** Name three campus systems that produce security events. *Rubric:* 3 = identity provider, mail service, Wi-Fi controllers, managed laptops (three); 2 = two; 1 = one; 0 = none.
- **EX005 — Student devices.** Why can the SOC see students only through university services? *Rubric:* 3 = personal unmanaged laptops send no logs; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Map gap.** What gap did Lucas's map reveal? *Rubric:* 3 = Wi-Fi logs not forwarded; cannot tell campus origin; 2 = partial; 1 = none; 0 = none.

### Synthesis

Understanding layers and service chains tells analysts where events originate and which are missing.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write short programs that read and count records; (2) use loops, conditions and dictionaries; (3) test programs on small known inputs; (4) write readable, commented code.

### 3.1 Why program

Analysts often ask questions no dashboard answers: "How many students received the phishing email per faculty?" A short program answers it reliably and can be rerun.

The recipient export for the library-fines email listed every delivery attempt, so counting rows would have overstated the number of people reached. Lucas's program de-duplicated by recipient and found 6,980 unique accounts. The same script ran again unchanged when a second export arrived the next day, which a manual count in a spreadsheet would not easily allow.

### 3.2 Basic constructs

Variables hold values; loops visit each record; conditions test fields; dictionaries map keys such as faculty names to counts. These four ideas solve most counting tasks.

Lucas's per-faculty counter uses all four: a dictionary called faculty_counts starts empty, a loop reads each recipient row, a condition checks whether the faculty field is present, and the matching count is increased by one. The whole program is under twenty lines, short enough for Dr. Kim to read before trusting its output.

### 3.3 Reading files

Exports arrive as CSV files. Python's csv module reads them into dictionaries keyed by column name, avoiding fragile string splitting.

The mail service's export quoted some faculty names because they contained commas, such as "Arts, Humanities". Splitting each line on commas would have broken those names into two fields and shifted every column after them. The csv module handles the quoting, so Lucas's counts were correct without any special code for awkward names. He also reads the file with an explicit encoding, since some names contain accented letters.

### 3.4 Testing

Before running on the real export, Lucas writes a five-line test file where he knows the answer: two students in Law, three in Engineering. If the program prints anything else, the program is wrong.

His first run on the test file printed three for Law, because the program counted the header row as a student. Fixing that took one line. Had he run the untested program on the real export, the error would have been hidden among thousands of rows and might never have been noticed.

### 3.5 Readability

Clear variable names (faculty_counts, not fc) and a comment stating intent help Dr. Kim and other students review his code.

When a fellow student analyst picked up the script during a later shift, the names and a one-line comment saying "count unique recipients per faculty" were enough for them to use and adapt it without asking Lucas. Code that only its author can understand becomes useless as soon as that person is off duty or graduates at the end of the year.

### 3.6 Handling errors

Some rows lack a faculty field. Lucas counts them under "unknown" instead of crashing, and prints how many there were.

In the phishing export, 112 rows had no faculty, mostly shared mailboxes and recent staff hires. Reporting that number told Dr. Kim how much of the data the faculty breakdown did not cover. A program that silently skipped those rows would have produced totals that did not add up to 6,980, without explaining why. Unknowns are a finding, not a nuisance, and they shrink as records improve.

### 3.7 Keeping code

Scripts are stored in the SOC's shared repository with a short description.

The description states what the script does, what input it expects and its known limits, such as treating shared mailboxes as unknown. Storing it in the shared repository means the next campaign can reuse it, and any change is recorded with the author and date. Scripts kept only on a student's laptop are lost when the student graduates, and nobody can check how an old figure was produced.

### Rerunning analyses

Because the script is saved, Lucas reruns it the next morning on a fresh export and sees 1,140 additional recipients from a second wave of the campaign. A manual count would have needed repeating from scratch; the script took seconds and its earlier output stayed as a record.

### Worked example

Lucas's first version counts 7,412 recipients. His test file passes, but the total seems high. He discovers duplicates: the export lists one row per delivery attempt. He de-duplicates by recipient address and gets 6,980 unique recipients.

> **Synthetic case.** Code and counts are invented.

### Errors and limits

A program that passes a small test can still mishandle unusual real data; check totals for plausibility.

### Exercises

- **EX007 — Four constructs.** Name the four basic constructs used for counting tasks. *Rubric:* 3 = variables, loops, conditions, dictionaries; 2 = three; 1 = one; 0 = none.
- **EX008 — Missing fields.** How should missing faculty fields be handled? *Rubric:* 3 = count as unknown, report how many, do not crash; 2 = partial; 1 = crash; 0 = none.
- **EX009 — Duplicate count.** Why was the first total too high, and what fixed it? *Rubric:* 3 = one row per delivery attempt; de-duplicate by recipient; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Small, tested, readable programs answer questions dashboards cannot, as long as results are checked for plausibility.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear academic and technical prose; (2) structure arguments with claims and evidence; (3) cite sources correctly; (4) avoid plagiarism and overclaiming.

### 4.1 Purpose

University assignments and SOC reports share a need: a reader must follow the argument and check the evidence. Academic writing makes claims explicit and supports each with sources or data.

When Lucas wrote his first incident summary, Dr. Kim needed to forward it to the university's data protection officer, who had not seen the logs. Every claim, such as "two accounts were compromised", had to point to the evidence behind it, so the officer could judge it without asking Lucas to explain each step in person.

### 4.2 Structure

A paragraph opens with its claim, gives evidence, explains how the evidence supports the claim and notes limits. Reports and essays follow the same pattern at larger scale.

A paragraph from Lucas's summary followed this shape: claim, two accounts were compromised; evidence, both clicked the link and signed in from an unusual country shortly afterwards; reasoning, the combination is a strong indicator; limit, other accounts may have been compromised without an unusual-country sign-in. The limit tells readers what is still uncertain.

### 4.3 Citing

Every borrowed idea or figure is cited. Lucas cites NIST SP 800-61r3 for incident response phases and Alahmadi, Axon and Martinovic (2022) for analysts' views of alarms, using the referencing style his course requires.

Citing the incident response guide lets readers check that the phases Lucas describes match the source rather than his memory of it. When he summarised findings about alarm fatigue, the citation showed the claim came from a study of analysts, not from his own opinion, which made Dr. Kim more willing to use it in a budget request.

### 4.4 Paraphrase and quotation

Paraphrasing restates ideas in new words and still needs a citation; quotation uses exact words in quotation marks. Copying without either is plagiarism.

Lucas uses quotation sparingly, mostly for precise definitions where exact wording matters, such as a phase name in the response guide. For most material he paraphrases, which shows he understood the idea, and adds the citation. When unsure whether a sentence is too close to the original, he rewrites it after closing the source, then compares the two.

### 4.5 Hedging

Claims should match evidence. "The phishing campaign compromised two accounts" is supported; "the campaign was run by a criminal group" is not, unless evidence shows it.

Lucas's draft said the sender was "clearly a criminal group"; the logs showed only the sending infrastructure and the fake page. Dr. Kim asked him to replace it with what was known: the campaign used a newly registered domain and a page copying Riverton's sign-in screen. Claims about who was behind it were left to those with evidence.

### 4.6 Revision

First drafts are for thinking; later drafts for readers. Lucas reads his work aloud to find unclear sentences.

His first draft of the incident summary was a timeline in the order he had discovered things. The revised version led with the outcome, two compromised accounts contained, and followed with the evidence, which suited readers who needed the result first. Reading aloud caught a sentence that used "they" for both the attacker and the victims, which confused the order of events.

### 4.7 Feedback

Dr. Kim comments on drafts; Lucas keeps a list of recurring issues to avoid them next time.

After three assignments, Lucas's list included missing denominators, vague claims about attackers and unexplained abbreviations such as IdP. He checked each new draft against the list before submitting it. By the end of term, Dr. Kim's comments had shifted from these basics to questions about evidence and reasoning, which was the point of keeping the list. The list itself became shorter each month.

### Writing for SOC readers

SOC reports use the same discipline but shorter forms: a summary first, then evidence in tables with sources, then limits. Lucas practises both styles so he can switch between essays and incident notes without losing precision about what is known and what is inferred.

### Worked example

Lucas's draft sentence: "Most security alerts are useless." Dr. Kim asks for evidence. He revises: "In interviews, SOC practitioners described most alarms as benign triggers — legitimate activity matching a rule (Alahmadi et al., 2022)." The revision is narrower, sourced and accurate.

> **Synthetic case.** The drafts are invented.

### Errors and limits

Good writing cannot rescue weak evidence; gather evidence first.

### Exercises

- **EX010 — Paragraph pattern.** Describe the claim–evidence paragraph pattern. *Rubric:* 3 = claim, evidence, explanation, limits; 2 = three; 1 = one; 0 = none.
- **EX011 — Plagiarism.** Does paraphrasing need a citation? *Rubric:* 3 = yes; ideas borrowed must be cited; 2 = yes only; 1 = no; 0 = none.
- **EX012 — Revised claim.** Why is Lucas's revision better than "most alerts are useless"? *Rubric:* 3 = narrower, sourced, accurate wording; 2 = partial; 1 = same; 0 = none.

### Synthesis

Academic writing pairs every claim with evidence, cites honestly and keeps claims within what evidence supports.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain common threats to universities; (2) describe phishing and account compromise from the defender's view; (3) explain the role of a SOC; (4) recognise everyday security behaviours that help defenders.

### 5.1 Universities as targets

Universities hold personal data, research and payment systems, and have open networks and many users. Common incidents include phishing, account compromise, ransomware and misuse of research computing.

Riverton's case shows why: thousands of students change every year, staff share accounts across departments, and many people use the same email address for teaching, research and administration. A single compromised account can reach many others because messages from a university address look legitimate to colleagues and students alike. Open networks for visitors add further exposure.

### 5.2 Phishing

Phishing emails imitate trusted senders to trick people into revealing passwords or opening harmful files. The "Library fines overdue" email linked to a fake sign-in page styled like Riverton's.

The email's subject played on a common worry, and the fake page used Riverton's logo and colours. The domain resembled the library's real address but was registered only days before the campaign. Students who entered their password were redirected to the real library site, so many did not realise anything had happened.

### 5.3 Account compromise

With a stolen password, an attacker signs in as the victim, reads mail, creates rules to hide replies or forward mail, and sends more phishing to contacts. Compromised accounts spread campaigns because messages come from a trusted sender.

In the case, the attacker used s2047 to create a rule moving replies to a hidden folder and then sent the library-fines email to the account's contacts. Recipients saw a message from a classmate's real address, which made them more likely to click. This is how one stolen password can extend a campaign.

### 5.4 What a SOC does

A SOC monitors logs and alerts, investigates suspicious activity, coordinates response and helps improve defences. Riverton's SOC is small: two staff and six student analysts.

With so few people, Riverton's SOC relies on clear priorities. During the campaign, one staff member coordinated with the identity team while student analysts handled reports and searched logs. Monitoring continued for other alerts throughout, because a large phishing campaign can hide a quieter attack happening at the same time, and student analysts are trained to escalate anything unrelated.

### 5.5 Helpful behaviours

Reporting suspicious emails, using multi-factor authentication and not reusing passwords make defenders' work easier. Reports often arrive before technical detection.

In the library-fines campaign, the first report arrived from a staff member several minutes before any filter flagged the message. Accounts with multi-factor authentication were much harder to misuse even after a password was entered on the fake page, because the attacker also needed the second factor. Unique passwords kept the stolen ones from opening other services, such as library and payment accounts.

### 5.6 Reporting culture

People report more when they are thanked, not blamed. The SOC replies to every report.

During the campaign, one student who had clicked and entered her password reported it herself. The SOC reset her password, signed out her sessions, checked for new mail rules and thanked her. Treating her as a helpful reporter rather than a careless user encourages others to come forward quickly, which is when response is easiest. The reply also told her what to watch for afterwards, such as unexpected sign-in prompts.

### 5.7 Case

Within an hour of the campaign, 95 reports reach the SOC's phishing mailbox — the first signal of the incident.

Lucas sorts the first reports by arrival time and finds that they all quote the same subject and sender, which confirms a single campaign rather than several unrelated ones. The earliest report gives the time the campaign started, which later becomes the starting point for searching sign-in logs for suspicious activity. He also notes that the campaign's subject line is reusable in a mail search, which shows how many mailboxes received it and lets the mail team remove the message from those that have not yet opened it.

### Multi-factor authentication

MFA asks for a second proof, such as an app approval. Riverton requires it for staff but only recommends it for students, which matters later in the case.

### Worked example

A student reports that she entered her password before noticing the fake address. The SOC resets her password, signs out her sessions, checks for new mail rules and thanks her. Her quick report prevented the account being used.

> **Synthetic case.** The campaign and reports are invented.

### Errors and limits

Awareness reduces but never removes clicks; technical controls must assume some will happen.

### Exercises

- **EX013 — Compromise actions.** What might an attacker do with a stolen campus mail account? *Rubric:* 3 = read mail, create rules to hide/forward, send more phishing; 2 = two; 1 = one; 0 = none.
- **EX014 — Report value.** Why are user reports valuable to a SOC? *Rubric:* 3 = often arrive before technical detection; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Reporter response.** How did the SOC handle the student who entered her password? *Rubric:* 3 = reset, sign out sessions, check rules, thank her; 2 = three; 1 = one; 0 = none.

### Synthesis

Security literacy lets everyone recognise threats and helps the SOC by reporting early.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use sets, relations and graphs to describe accounts and messages; (2) express detection conditions in logic; (3) reason about counting and combinations; (4) apply graph ideas to the spread of phishing.

### 6.1 Sets of accounts

Let R be the accounts that received the phishing email, C those that clicked the link, and S those that later signed in from an unusual country. C ∩ S identifies accounts that both clicked and showed suspicious sign-ins — the strongest candidates for compromise.

Writing the sets out makes the steps clear. R holds the 6,980 recipients, C the 33 who clicked, and S the accounts with unusual-country sign-ins in the following days. An account in S but not C might be compromised by another route, or might be genuine travel, so it is reviewed separately.

### 6.2 Logic for detections

A detection condition is a logical formula: "sign-in from a new country AND mailbox rule created within 60 minutes". Writing it in logic makes it precise enough to test and review.

Written precisely, the rule can be checked against cases. For s2047, a sign-in from a new country was followed within minutes by a rule hiding replies, so the rule fires. A student who travels home and signs in from there, but creates no rule, does not trigger it. Each part of the condition removes a source of false alarms.

### 6.3 Relations

"Account a sent mail to account b" is a relation. Together these relations form a directed graph of who emails whom.

The relation is built from the mail service's message log: each row gives a sender and a recipient. Lucas stores it as a dictionary mapping each sender to the set of recipients they have mailed in the previous month. Comparing that history with mail sent after a suspected compromise shows which recipients are new, and therefore suspicious enough to review.

### 6.4 Graphs and spread

When s2047 was compromised, the attacker sent phishing to its contacts. In the graph, the campaign spreads along edges from compromised nodes. Finding nodes with many new outgoing edges finds spreading accounts.

For s2047, the account had mailed about twenty people in the previous month, but sent the library-fines email to more than two hundred in under an hour after compromise. That jump in new outgoing edges stood out clearly against normal student behaviour, and the same check later helped confirm whether s3310 had been used to spread the campaign further.

### 6.5 Counting

With 6,980 recipients and 33 clickers, the number of possible clicker pairs is 33 × 32 ÷ 2 = 528. Counting helps estimate the effort of manual checks before starting them.

In practice, the SOC does not need to compare clicker pairs at all; the count shows why it should not try. Instead, it checks each clicker against sign-in logs, which takes 33 lookups. Choosing a method whose effort grows with the number of accounts, not the number of pairs, keeps the work manageable for a small team of two staff and six students.

### 6.6 Precision of definitions

Discrete thinking turns "many emails" into "more than 50 recipients outside the user's usual contacts in one hour".

With a precise definition, two analysts reviewing the same mailbox reach the same answer, and a program can apply it to every account. A vague one leaves each analyst to decide what "many" means, so results vary between shifts. Lucas tests his definition against s2047, which it flags, and a busy lecturer, which it does not. Both tests are kept with the rule.

### 6.7 Case use

Lucas computes C ∩ S from exported lists and finds two accounts: s2047 and s3310.

Both accounts were then examined in detail. s2047 had two successful unusual-country sign-ins and s3310 had one. Starting from the intersection meant Lucas reviewed two accounts first rather than all 33 clickers, though the remaining clickers were still checked afterwards, since a compromise might not show an unusual-country sign-in, for example if the attacker used a server in the same country. For each of the other 31, Lucas checked sign-ins, new mail rules and sent mail, and recorded the result in the case notes.

### Paths

A path in the graph from s2047 to s3310 would show whether the second compromise came from the first account's phishing.

### Worked example

Lucas draws a small graph of s2047's outgoing mail on the day: before 02:14, edges go to 3 regular contacts; after 02:14, 212 new edges appear in two hours. The graph view makes the spread obvious in a way a list of messages did not.

> **Synthetic case.** Accounts and counts are invented.

### Errors and limits

Sets are only as complete as the logs that build them; missing click data shrinks C.

### Exercises

- **EX016 — Set intersection.** What does C ∩ S represent? *Rubric:* 3 = clicked and had suspicious sign-ins: strongest compromise candidates; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Graph spread.** How does a mail graph reveal a spreading account? *Rubric:* 3 = many new outgoing edges after compromise time; 2 = partial; 1 = none; 0 = none.
- **EX018 — Pair count.** How many clicker pairs exist among 33 clickers? *Rubric:* 3 = 528 with formula; 2 = number only; 1 = wrong; 0 = none.

### Synthesis

Sets, logic and graphs give precise meaning to compromise candidates and campaign spread.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain IP addressing, DNS, HTTP and email protocols; (2) read sign-in and mail logs at the protocol level; (3) reason about geolocation and its limits; (4) recognise network evidence of phishing.

### 7.1 Addresses and locations

Every connection has a source IP address. Identity providers often add a geolocation (country) guessed from the address. Geolocation is approximate: VPNs, mobile networks and cloud services can place users in the wrong country.

### 7.2 DNS

DNS translates names such as riverton.example.ac.uk into addresses. The phishing page used riverton-library.example.net, a look-alike name. DNS logs from campus resolvers show which devices looked it up.

### 7.3 HTTP and HTTPS

Web pages use HTTP over TLS. The fake sign-in page received passwords by HTTPS POST; network sensors see only the destination name, not the password.

### 7.4 Email protocols

Mail travels between servers by SMTP. Message headers record each server hop. Authentication results — SPF, DKIM and DMARC — show whether the sending domain authorised the message; the phishing email failed DMARC for its claimed sender.

### 7.5 Reading sign-in logs

A sign-in record shows time, user, IP, country, client application and result. s2047's 02:14 sign-in came from an address geolocated to the Netherlands using a desktop mail protocol.

### 7.6 DNS as evidence

Campus DNS logs show 41 lookups of the look-alike name from university Wi-Fi, a lower bound on clicks from campus.

### 7.7 Limits

Network evidence shows connections, not intentions; it needs context from other logs.

### Ports and services

Services listen on ports: 443 for HTTPS, 25 for server-to-server mail. Unusual ports in connection logs prompt questions.

### Worked example

Lucas checks whether the Netherlands address could be a student's VPN. The address belongs to a hosting provider, and s2047's owner confirms she was asleep in Riverton. Combined with the click and the new mailbox rule, the evidence supports compromise.

> **Synthetic case.** Addresses, names and counts are invented.

### Errors and limits

Geolocation errors are common; never base a decision on country alone.

### Exercises

- **EX019 — Geolocation limits.** Why is sign-in country unreliable on its own? *Rubric:* 3 = VPNs, mobile, cloud can misplace users; 2 = partial; 1 = reliable; 0 = none.
- **EX020 — DMARC.** What does a DMARC failure tell analysts? *Rubric:* 3 = claimed sending domain did not authorise the message; 2 = partial; 1 = vague; 0 = none.
- **EX021 — DNS lower bound.** Why are 41 DNS lookups a lower bound on campus clicks? *Rubric:* 3 = only campus resolvers; caching and off-campus clicks missed; 2 = partial; 1 = exact; 0 = none.

### Synthesis

Protocol knowledge turns network logs into evidence, provided geolocation and visibility limits are respected.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure larger analysis programs into functions and modules; (2) use the standard library for dates, CSV and JSON; (3) write unit tests for analysis logic; (4) handle large inputs efficiently.

### 8.1 From scripts to tools

Lucas's counting scripts grow into a small tool that reads sign-in and mail exports, joins them by user and time, and prints suspicious combinations. Functions separate reading, analysis and output.

### 8.2 Dates and times

The datetime module parses timestamps and converts zones. Mixing local and UTC times is the most common bug in SOC scripts.

### 8.3 JSON

Cloud services export JSON. The json module reads nested records; Lucas writes small functions to extract the fields he needs.

### 8.4 Unit tests

unittest checks functions with known inputs: "a rule created 59 minutes after a risky sign-in should match; 61 minutes should not".

### 8.5 Efficiency

Reading files line by line and using dictionaries for lookups keeps memory small and speed high on large exports.

### 8.6 Errors

The tool logs records it cannot parse and continues; at the end it prints totals read, skipped and matched.

### 8.7 Sharing

A README explains inputs, outputs and limits, so other student analysts can run it.

### Configuration

Thresholds such as the 60-minute window live in a small configuration file, not inside the code. Changing a threshold then needs no code change, and the configuration is reviewed like code. Lucas records which configuration produced each result so findings can be reproduced later.

### Peer review of tools

Another student analyst runs the tool on a test export before it is used in a case.

### Worked example

A unit test fails: a rule created at 02:59 after a sign-in at 02:00 is not matched. Lucas finds he compared minutes only, ignoring hours. He switches to datetime objects and the test passes. Without the test, the bug would have hidden matches spanning an hour boundary.

> **Synthetic case.** Code and data are synthetic.

### Errors and limits

Tests cover the cases you imagine; add new tests when real data surprises you.

### Exercises

- **EX022 — Time bug.** What caused the failed test, and what fixed it? *Rubric:* 3 = compared minutes ignoring hours; use datetime objects; 2 = partial; 1 = unknown; 0 = none.
- **EX023 — Totals output.** Why print totals read, skipped and matched? *Rubric:* 3 = makes data loss and coverage visible; 2 = partial; 1 = habit; 0 = none.
- **EX024 — README contents.** What should the tool's README explain? *Rubric:* 3 = inputs, outputs, limits; 2 = two; 1 = one; 0 = none.

### Synthesis

Structured, tested tools built on the standard library make SOC analysis repeatable and shareable.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) model security data as tables; (2) write SQL queries with filters, grouping and joins; (3) use a database to answer investigation questions; (4) consider data quality and privacy in stored data.

### 9.1 Tables

Security logs fit naturally into tables: one row per event, columns for time, user, address, country and result. Databases answer questions over millions of rows quickly.

### 9.2 SQL basics

SELECT chooses columns, WHERE filters rows, GROUP BY aggregates and ORDER BY sorts. A query such as "successful sign-ins outside the usual country, grouped by user" answers an investigation question in one statement.

### Lab — querying sign-ins

```python
"""Query synthetic sign-in records with the standard-library sqlite3 module."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table signin(ts text, user text, country text, result text)")
rows = [("09:01","s1001","GB","ok"),("09:03","s1002","GB","ok"),("09:05","s1001","GB","ok"),
        ("02:14","s2047","NL","ok"),("02:15","s2047","NL","ok"),("02:20","s3310","NL","fail"),
        ("10:12","s2047","GB","ok"),("02:31","s3310","NL","ok")]
db.executemany("insert into signin values (?,?,?,?)", rows)
q = "select user, count(*) from signin where country != 'GB' and result = 'ok' group by user order by user"
for user, n in db.execute(q): print(user, "successful sign-ins outside GB:", n)
```

Run with `python3 lab_sqlite.py`. Verified output:

```text
s2047 successful sign-ins outside GB: 2
s3310 successful sign-ins outside GB: 1
```

### 9.3 Reading the result

Two accounts had successful sign-ins outside GB: s2047 twice and s3310 once. s3310's success at 02:31 followed a failure at 02:20, suggesting the attacker had its password after a mistake or second attempt.

### 9.4 Joins

Joining the sign-in table with the mailbox-rule table on user shows which risky sign-ins were followed by rule changes.

### 9.5 Quality

Missing countries, duplicated rows and inconsistent user formats (s2047 versus S2047) distort results. Normalising at load time prevents errors.

### 9.6 Privacy

Databases with personal data need access control and retention limits. The SOC database keeps sign-in details for 90 days.

### Indexes

Queries filtering by user or time run faster when those columns are indexed. Lucas adds indexes on user and timestamp after a query over a month of data takes minutes, and it then returns in under a second. Indexes cost storage and slow inserts slightly, a trade-off worth making for fields used in most investigations.

### Worked example

Lucas extends the query to compare each user's sign-in countries with their previous 30 days. s2047 had only GB before; s3310 had GB and FR (a semester abroad). The NL sign-in is new for both, but s3310's history reminds him that travel is normal for some students.

> **Synthetic case.** Records come from the lab script and invented history.

### Errors and limits

SQL answers what was stored; events never logged cannot be queried.

### Exercises

- **EX025 — Lab result.** Which accounts had successful sign-ins outside GB? *Rubric:* 3 = s2047 (2), s3310 (1); 2 = one; 1 = wrong; 0 = none.
- **EX026 — Failure then success.** What does s3310's 02:20 failure followed by 02:31 success suggest? *Rubric:* 3 = attacker obtained/retried password successfully; 2 = partial; 1 = nothing; 0 = none.
- **EX027 — User history.** Why compare with the previous 30 days? *Rubric:* 3 = shows what is normal for each user (e.g. travel); 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Tables and SQL answer investigation questions quickly when data is clean and handled under privacy rules.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) apply ethical principles to SOC work at a university; (2) act within authorisation and policy; (3) protect privacy of students and staff; (4) handle conflicts of interest and peer data.

### 10.1 Authority

The SOC acts under the university's information security policy, approved by its governing body. Student analysts may view logs only for assigned alerts and may not search for people they know.

### 10.2 Privacy

Students and staff expect privacy. The SOC looks at metadata (sign-ins, rule changes, message counts) by default and reads message content only with case approval from Dr. Kim.

### 10.3 Conflicts of interest

If an alert involves a friend, classmate or lecturer, a student analyst passes it to another analyst. Lucas declares when an alert involves someone in his course.

### 10.4 Confidentiality

Analysts sign a confidentiality agreement. Discussing cases outside the SOC, even anonymously, is not allowed.

### 10.5 Authorised testing

Phishing simulations and other tests are approved in writing by Dr. Kim and communicated in policy; analysts never run their own tests on university systems.

### 10.6 Proportionality

Responses match the risk: resetting a compromised account is proportionate; suspending a student's network access without evidence is not.

### 10.7 Reporting misconduct

If an analyst sees misuse of SOC access, they report it to Dr. Kim.

### Records of access

Every log search by an analyst is recorded by the SIEM. Dr. Kim reviews a sample monthly, so misuse would be noticed and analysts know their access is accountable.

### Worked example

During the campaign, another student analyst suggests reading s2047's inbox to see what the attacker read. Lucas points out that metadata (rule creation, sent counts) answers the immediate questions and that content access needs Dr. Kim's approval. She approves a limited review of the forwarded messages' subjects only.

> **Synthetic case.** Policies and events are invented.

### Errors and limits

Policies cannot foresee every case; ask when unsure.

### Exercises

- **EX028 — Content access.** When may student analysts read message content? *Rubric:* 3 = only with case approval from Dr. Kim; 2 = partial; 1 = any time; 0 = none.
- **EX029 — Conflict of interest.** What should Lucas do if an alert involves a classmate? *Rubric:* 3 = declare and pass to another analyst; 2 = partial; 1 = handle it; 0 = none.
- **EX030 — Limited review.** What did Dr. Kim approve during the campaign? *Rubric:* 3 = review of forwarded messages' subjects only; 2 = partial; 1 = full inbox; 0 = none.

### Synthesis

Ethical SOC practice means acting within authority, protecting privacy, declaring conflicts and keeping responses proportionate.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain processes, users, permissions and logging in Windows and Linux; (2) locate security-relevant events on servers; (3) relate OS configuration to what a SOC can see; (4) recognise privilege changes as signals.

### 11.1 What operating systems record

Operating systems control processes, files and users, and can log logons, process creation, privilege changes and service installation. Logging is configurable: unconfigured systems record little.

### 11.2 Windows and Linux

University staff laptops run Windows; research servers mostly run Linux. Windows records events in event logs; Linux uses system logs and, where configured, the audit subsystem. Both can forward logs to the SOC.

### 11.3 Users and privileges

Administrators can install software and change settings. Adding a user to an administrators group or to Linux's sudo group is a privilege change worth alerting on.

### 11.4 Research servers

Research groups often run their own servers with local accounts. The research GPU server in the physics department was set up by a postdoc and forwarded no logs to the SOC until this year.

### 11.5 SSH

Linux servers accept remote logins over SSH. Authentication logs show successes and failures with source addresses. Key-based login without passwords reduces guessing risk.

### 11.6 Configuration matters

A rule for "new administrator added" works only if the server logs group changes and forwards them.

### 11.7 Case

In week five, an alert reports a new sudo user on the physics GPU server.

### Worked example

Lucas checks the server's authentication log: the new user was created by the server's administrator account at 14:02 from a university IP address belonging to the physics building. He contacts the research group, who confirm a new PhD student was added. He closes the alert as authorised and suggests the group record such changes in a ticket first.

> **Synthetic case.** Servers and events are invented.

### Errors and limits

Local accounts on research servers may not match central identity records, complicating investigation.

### Exercises

- **EX031 — Privilege signal.** Why is adding a user to sudo or administrators a useful signal? *Rubric:* 3 = grants admin rights attackers seek; 2 = partial; 1 = noise; 0 = none.
- **EX032 — Rule dependency.** When does a "new administrator" rule work? *Rubric:* 3 = server logs group changes and forwards them; 2 = partial; 1 = always; 0 = none.
- **EX033 — GPU alert outcome.** How was the sudo alert resolved? *Rubric:* 3 = created by admin from physics building; confirmed new PhD student; closed authorised; ticket suggested; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Operating systems produce useful security events only when configured and forwarded; privilege changes deserve attention.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) describe distributions of user activity; (2) use means, standard deviations and z-scores to find unusual behaviour; (3) understand base rates and false alarms; (4) report uncertainty.

### 12.1 Normal behaviour varies

Each user sends a different number of emails per day. A library staff account sends about 40; most students send a handful. Unusual means unusual for that account.

### 12.2 Mean and standard deviation

The mean is the typical value; the standard deviation measures spread. A z-score — (today − mean) ÷ standard deviation — shows how many spreads today's value lies from typical.

### Lab — unusual outbound mail

```python
"""Flag accounts whose outbound mail today is far above their own history (synthetic)."""
import statistics
history = {"s1001": [4, 6, 5, 3, 7, 5, 4], "s2047": [2, 3, 1, 2, 4, 2, 3], "staff_lib": [40, 38, 45, 42, 39, 41, 44]}
today = {"s1001": 8, "s2047": 212, "staff_lib": 47}
for u, h in history.items():
    m, s = statistics.mean(h), statistics.stdev(h)
    z = (today[u] - m) / s
    print(f"{u:9} mean={m:5.1f} sd={s:4.1f} today={today[u]:4} z={z:7.1f} {'FLAG' if z > 4 else ''}")
```

Run with `python3 lab_zscore.py`. Verified output:

```text
s1001     mean=  4.9 sd= 1.3 today=   8 z=    2.3 
s2047     mean=  2.4 sd= 1.0 today= 212 z=  214.7 FLAG
staff_lib mean= 41.3 sd= 2.6 today=  47 z=    2.2
```

### 12.3 Reading the result

s2047 normally sends about 2.4 messages a day; today it sent 212, a z-score of about 215 — far beyond any normal variation. s1001 (z = 2.3) and the library account (z = 2.2) are slightly above typical but well within ordinary days.

### 12.4 Thresholds

Lucas flags z above 4. With hundreds of thousands of accounts, a threshold of 2 would flag thousands every day; base rates matter, as Axelsson (2000) showed for intrusion detection.

### 12.5 Limits of z-scores

Seven days is a short history; z-scores assume roughly symmetric variation, which counts rarely have. They are a screening tool, not proof.

### 12.6 Reporting

Lucas reports values with history length and threshold so readers know how the flag was made.

### Seasonality

Activity changes with the academic calendar: exam weeks, holidays and term starts. A history that spans a holiday understates normal term-time activity. Lucas compares like with like where possible, using the same week type in previous terms.

### Worked example

Dr. Kim asks whether s2047 could be a legitimate bulk send, such as a society newsletter. Lucas checks recipients: 212 different addresses, none in the student's past contacts, all with the same "Library fines" subject. Combined with the risky sign-in, he classifies it as compromise.

> **Synthetic case.** Values come from the lab script.

### Errors and limits

Accounts with no history cannot be scored; new users need a different approach.

### Exercises

- **EX034 — z-score meaning.** Define a z-score in this context. *Rubric:* 3 = (today − mean) ÷ sd: spreads from typical; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Lab flags.** Which account was flagged and why were others not? *Rubric:* 3 = s2047 z≈215; others z≈2.3, 2.2 below threshold 4; 2 = partial; 1 = wrong; 0 = none.
- **EX036 — Threshold reasoning.** Why not flag at z above 2? *Rubric:* 3 = many accounts → thousands of daily false flags (base rate); 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Statistics compare behaviour with each account's own normal; thresholds must respect base rates and short histories.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) explain identity lifecycle, authentication and authorisation; (2) describe multi-factor authentication and its signals; (3) analyse identity logs for compromise; (4) recommend identity controls.

### 13.1 Identity lifecycle

Accounts are created when people join, changed when roles change and removed when they leave. Universities have heavy churn each term; stale accounts of graduates are a risk if not disabled.

### 13.2 Authentication and authorisation

Authentication proves identity; authorisation decides what the identity may access. A compromised student account can access that student's mail, files and learning platform.

### 13.3 Multi-factor authentication

MFA requires a second proof. Riverton requires it for staff; for students it is optional. Neither s2047 nor s3310 had enrolled.

### 13.4 Identity signals

New country or device, impossible travel (two distant locations too close in time), legacy protocols that bypass MFA, and MFA method changes are common signals.

### 13.5 Legacy protocols

s2047's attacker used a desktop mail protocol that does not support MFA. Even enrolled users could be exposed while such protocols remain enabled.

### 13.6 Controls

Require MFA for all, disable legacy protocols, and alert on MFA changes and risky sign-ins.

### 13.7 Case decision

After the campaign, the university decides to require student MFA and disable legacy mail protocols from next term.

### Graduates and leavers

At the end of each year thousands of students graduate. Their accounts move to a short alumni period and are then disabled. Stale accounts that still work are attractive to attackers because nobody watches them, so the SOC alerts on sign-ins to accounts past their end date.

### Worked example

Lucas checks how many students used legacy protocols in the past month: 318 accounts, mostly older mail apps. The service desk contacts them before the change, and the cut-over happens with only 14 support calls.

> **Synthetic case.** Figures and decisions are invented.

### Errors and limits

MFA reduces password-only compromise but attackers adapt, for example by tricking users into approving prompts.

### Exercises

- **EX037 — Identity signals.** List three identity compromise signals. *Rubric:* 3 = new country/device, impossible travel, legacy protocol, MFA change (three); 2 = two; 1 = one; 0 = none.
- **EX038 — Legacy risk.** Why do legacy protocols matter even for MFA users? *Rubric:* 3 = they do not support MFA, so password alone suffices; 2 = partial; 1 = irrelevant; 0 = none.
- **EX039 — Controls adopted.** What identity controls did Riverton adopt? *Rubric:* 3 = student MFA required, legacy protocols disabled; 2 = one; 1 = none; 0 = none.

### Synthesis

Identity is central to campus security; lifecycle, MFA and identity signals shape both detection and prevention.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) explain privacy principles relevant to monitoring; (2) apply data minimisation and purpose limitation; (3) handle personal data in investigations; (4) communicate with data protection staff.

### 14.1 Principles

Common privacy principles include lawfulness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, and security. They apply to SOC monitoring as to any processing of personal data.

### 14.2 Purpose limitation

Logs collected for security may not be reused for unrelated purposes, such as checking attendance. Riverton's monitoring notice states security as the purpose.

### 14.3 Minimisation

The SOC collects metadata needed for detection, not message content. When content is needed, access is approved per case and limited to what answers the question.

### 14.4 Retention

Sign-in logs are kept 90 days, mail metadata 180 days. Longer retention needs justification.

### 14.5 Individuals' rights

Students can ask what data is held about them. The SOC's records must be retrievable for such requests, with redaction where other people's data appears.

### 14.6 Breach assessment

If personal data was exposed — for example, mail forwarded to an attacker — the data protection officer assesses whether to notify regulators and affected people.

### 14.7 Working with the DPO

The SOC informs the data protection officer early and provides facts, not legal conclusions.

### Transparency

The monitoring notice is published on the university intranet and linked from the sign-in page. It explains what is logged, why, for how long and who can see it. People who understand monitoring are more likely to trust and report to the SOC.

### Third parties

Cloud providers process logs on the university's behalf under contracts setting security and location terms.

### Worked example

For s2047, the forward rule sent 37 messages to an external address. Lucas lists their subjects with Dr. Kim's approval; three contained other students' marks. The DPO decides that those three students must be informed, and the SOC provides the exact message list.

> **Synthetic case.** The case and decisions are invented.

### Errors and limits

Privacy law varies by country; follow your institution's legal advice.

### Exercises

- **EX040 — Purpose limitation.** Give an example of a purpose-limitation breach. *Rubric:* 3 = using security logs to check attendance; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Minimisation.** How does the SOC apply minimisation? *Rubric:* 3 = metadata by default; content only per approved case; 2 = partial; 1 = collect all; 0 = none.
- **EX042 — Breach outcome.** What did the DPO decide for s2047's forwarded mail? *Rubric:* 3 = three students with exposed marks informed; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Privacy principles shape what a SOC collects, how long it keeps it and how it handles exposure of personal data.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) preserve digital evidence with integrity; (2) measure SOC activities consistently; (3) distinguish observation, inference and conclusion; (4) record evidence in case notes.

### 15.1 What counts as evidence

In a SOC, evidence includes exported logs, alert records, screenshots of configuration and statements. Evidence must be preserved so its integrity can be shown later.

### 15.2 Preservation

Exports are saved read-only with a hash (a digital fingerprint). If a file changes, its hash changes. Case notes record who exported what, when and from where.

### 15.3 Observation and inference

"Sign-in from 198.51.100.x at 02:14" is an observation. "The account was compromised" is an inference. Case notes keep them separate and show the reasoning.

### 15.4 Measurement

Consistent measures — time to acknowledge, time to contain, number of accounts affected — let the SOC compare incidents and improve. Definitions must be fixed: does "contain" mean password reset or all sessions revoked?

### 15.5 Units and clocks

All times in UTC; durations in minutes. Mixed units cause errors.

### 15.6 Error and uncertainty

Some measures are uncertain: the number of people who clicked is estimated from DNS lookups and reports. Lucas reports a range and its basis.

### 15.7 Case notes

Each step in the campaign response is recorded as it happens, not reconstructed afterwards.

### Chain of custody

When evidence may be needed by the university's disciplinary process or by police, a chain-of-custody record lists every transfer of the evidence with time and person. Without it, the evidence may be challenged even if it is accurate.

### Timeliness

Notes written hours later lose detail; Lucas writes them while working.

### Worked example

Lucas's case note: "02:14 UTC sign-in s2047 from NL hosting address (observation, export E-3, hash recorded). 02:20 rule created forwarding to external address (observation, E-5). Inference: account compromised (supported by E-3, E-5, owner statement). Contained 08:41 (password reset and sessions revoked)."

> **Synthetic case.** Notes and exports are invented.

### Errors and limits

Preserved evidence shows what logs recorded, not everything that happened.

### Exercises

- **EX043 — Observation versus inference.** Classify "the account was compromised". *Rubric:* 3 = inference, supported by observations; 2 = inference only; 1 = observation; 0 = none.
- **EX044 — Containment definition.** Why must "contained" be defined precisely? *Rubric:* 3 = different actions mean different times; consistent comparison; 2 = partial; 1 = no reason; 0 = none.
- **EX045 — Click estimate.** How should the click count be reported? *Rubric:* 3 = range with basis (DNS lookups, reports); 2 = partial; 1 = exact number; 0 = none.

### Synthesis

Preserve evidence with integrity, measure consistently and keep observations separate from inferences.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe how a university's networks and services are arranged for security; (2) identify trust boundaries and where monitoring belongs; (3) evaluate architecture against campus threats; (4) propose improvements with reasons.

### 16.1 Campus architecture

Riverton runs a student Wi-Fi network, a staff network, a research network, data-centre servers and cloud services for mail and identity. Each has different users and risks.

### 16.2 Trust boundaries

Boundaries separate zones: student Wi-Fi should not reach administrative servers; research servers should be reachable only by their groups. Firewalls enforce boundaries and log crossings.

### 16.3 Cloud-first services

Mail and identity live in the cloud, so the most important logs come from cloud providers rather than campus networks. The SOC's architecture must collect cloud logs reliably.

### 16.4 Monitoring placement

The SOC monitors identity sign-ins (all users), mail events, firewall logs at zone boundaries and endpoint logs from managed devices. Student devices are visible only through services.

### 16.5 Research network

Research servers are diverse and loosely managed. A boundary that limits inbound access to university addresses and requires SSH keys reduces exposure.

### 16.6 Defence in depth

Several layers — mail filtering, MFA, legacy protocol blocking, monitoring of mailbox rules — mean one failure does not lead to widespread compromise.

### 16.7 Mapping to frameworks

Lucas maps controls to NIST CSF 2.0 functions to show coverage across Protect, Detect and Respond.

### Administrative systems

Finance, HR and student records sit in a restricted zone reachable only from staff networks through a gateway that requires MFA. Logs from the gateway show every session, giving the SOC a narrow, high-value view of access to the most sensitive data.

### Worked example

Lucas's architecture review notes that research servers accept SSH from anywhere on the internet. He proposes restricting inbound SSH to the university VPN and campus networks. The physics group agrees after a trial week shows their remote collaborators can use the VPN.

> **Synthetic case.** Networks and reviews are invented.

### Errors and limits

Universities value openness; controls must fit research and teaching needs.

### Exercises

- **EX046 — Cloud logs.** Why are cloud provider logs central to Riverton's SOC? *Rubric:* 3 = mail and identity are in the cloud; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Research boundary.** What change was proposed for research servers? *Rubric:* 3 = restrict inbound SSH to VPN and campus; SSH keys; 2 = partial; 1 = none; 0 = none.
- **EX048 — Defence in depth.** Give three layers protecting campus mail accounts. *Rubric:* 3 = filtering, MFA, legacy blocking, rule monitoring (three); 2 = two; 1 = one; 0 = none.

### Synthesis

Architecture defines zones and boundaries; monitoring belongs where trust changes and where important services live.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain hashing, encryption and digital signatures; (2) relate cryptography to authentication and email security; (3) use hashes for evidence integrity; (4) recognise cryptographic limits in monitoring.

### 17.1 Hashes

A cryptographic hash turns any data into a fixed-size fingerprint. It is practically impossible to find two inputs with the same hash. SOCs use hashes to identify files and to check that evidence has not changed.

### 17.2 Encryption

Encryption makes data unreadable without a key. TLS encrypts web and mail traffic in transit; disk encryption protects lost laptops.

### 17.3 Signatures

A digital signature proves who created data and that it has not changed. Email DKIM signatures let receiving servers verify that a message came from the claimed domain.

### 17.4 Passwords

Passwords should be stored as slow, salted hashes so that a stolen database cannot be easily reversed.

### 17.5 Monitoring and encryption

Encryption hides content from network sensors. The SOC relies on endpoint and service logs that see data before encryption or after decryption.

### 17.6 Keys and trust

Cryptography is only as safe as its keys. Compromised signing keys let attackers sign malicious content.

### 17.7 Case

The phishing email failed DKIM for the domain it pretended to come from; receiving filters marked it suspicious, but the banner was easy to ignore.

### Certificates

Websites prove their identity with certificates signed by trusted authorities. The phishing page had a valid certificate for its look-alike name, so the browser padlock showed; a padlock proves encryption, not honesty.

### Worked example

Lucas exports the phishing message and computes its SHA-256 hash for the case record. Later, a second copy reported by staff has a different hash: the attacker added the recipient's name to each message. Lucas notes that hashes identify exact copies, not campaigns; subjects and links group variants.

> **Synthetic case.** Messages and hashes are invented.

### Errors and limits

Cryptography protects data in specific ways; it does not make a system secure by itself.

### Exercises

- **EX049 — Hash uses.** Name two SOC uses of hashes. *Rubric:* 3 = identify files, check evidence integrity; 2 = one; 1 = none; 0 = none.
- **EX050 — DKIM.** What does a DKIM signature let receivers check? *Rubric:* 3 = message came from claimed domain unchanged; 2 = partial; 1 = encryption; 0 = none.
- **EX051 — Variant hashes.** Why did two copies of the phishing email have different hashes? *Rubric:* 3 = personalised content changes hash; group by subject/link; 2 = partial; 1 = error; 0 = none.

### Synthesis

Cryptography underpins authentication, email trust and evidence integrity, but it hides content from monitoring and depends on key safety.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) formulate a research question about SOC practice; (2) choose methods such as surveys, interviews and log analysis; (3) consider ethics in research with people and data; (4) plan a small study.

### 18.1 From curiosity to question

Lucas wonders why students report phishing less than staff (chapter 1). A research question: "What reasons do Riverton students give for not reporting suspicious emails?"

### 18.2 Choosing a method

Surveys reach many people with fixed questions; interviews explore reasons in depth with fewer people; log analysis shows behaviour but not reasons. Lucas combines a short survey with five interviews.

### 18.3 Sampling

A survey of volunteers may over-represent security-interested students. Lucas recruits through several channels and reports who responded.

### 18.4 Ethics

Research with people needs ethics approval, informed consent, anonymity and the right to withdraw. No SOC data about individuals is used.

### 18.5 Designing questions

Neutral wording ("How do you usually handle suspicious emails?") avoids leading answers ("Why don't you report phishing?").

### 18.6 Analysis

Survey answers are counted; interview transcripts are coded into themes, with a second student coding a sample to check consistency.

### 18.7 Literature

Sundaramurthy et al. (2014) show how researchers embedded in SOCs revealed practice that surveys missed, encouraging mixed methods.

### Analysis plan

Before collecting responses, Lucas writes down how he will analyse them: which questions are counted, how themes will be coded and how disagreements between coders will be resolved. Writing the plan first prevents him from searching the data for whatever looks interesting and presenting it as if it had been the question all along.

### Worked example

Lucas's pilot survey with ten classmates shows the question "Do you know how to report phishing?" was misread as "Do you know what phishing is?" He rewrites it: "If you received a suspicious email at Riverton, what would you do with it?" with open text.

> **Synthetic case.** The study is invented.

### Errors and limits

Small studies at one university show local reasons; others may differ.

### Exercises

- **EX052 — Method mix.** Why combine a survey with interviews? *Rubric:* 3 = survey breadth plus interview depth on reasons; 2 = partial; 1 = one enough; 0 = none.
- **EX053 — Leading questions.** Rewrite a leading question neutrally. *Rubric:* 3 = e.g. "How do you usually handle suspicious emails?"; 2 = partial; 1 = unchanged; 0 = none.
- **EX054 — Pilot finding.** What did the pilot reveal and how was it fixed? *Rubric:* 3 = question misread; rewritten as open scenario; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Research methods turn SOC puzzles into questions, chosen methods and ethical, piloted studies.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Security operations and blue team: scope and theory

### Learning outcomes

You will (1) define security operations and blue-team work; (2) explain SOC functions and services; (3) relate SOC work to incident response frameworks; (4) describe SOC models and maturity.

### 19.1 What security operations are

Security operations monitor, detect, analyse and respond to threats continuously. The blue team is the defending side, contrasted with red teams that simulate attackers under authorisation.

### 19.2 SOC functions

Knerler, Parker and Zimmerman (2022) group SOC functions into areas such as real-time monitoring and triage, incident analysis and response, threat intelligence, tooling and engineering, and expanded services like hunting.

### 19.3 Incident response framework

NIST SP 800-61r3 places incident response within cybersecurity risk management, aligned to CSF 2.0 functions: preparation sits in Govern, Identify and Protect; detection and response in Detect and Respond; recovery in Recover.

### 19.4 Continuous monitoring

NIST SP 800-137 describes continuous monitoring as an ongoing programme tied to risk.

### 19.5 SOC models

SOCs may be internal, outsourced or hybrid. Riverton's is internal and small, using student analysts as a teaching programme.

### 19.6 Maturity

The SOC-CMM (van Os, 2016) assesses maturity across business, people, process, technology and services. Riverton scores higher in technology than in process documentation.

### 19.7 Theory and practice

Vielberth et al. (2020) note that SOC research is fragmented; much practice relies on experience, so the course pairs theory with case work.

### Red, blue and purple

Red teams simulate attackers under written authorisation; blue teams defend; purple exercises bring both together so defenders learn which simulated actions they saw. Riverton runs a small purple exercise each year with an external firm.

### Worked example

Lucas maps the phishing response onto CSF 2.0: Detect (user reports, z-score flag), Respond (resets, rule removal, notifications), Recover (restoring deleted mail for s3310), and Govern (decision to require student MFA).

> **Synthetic case.** The mapping is invented.

### Errors and limits

Frameworks describe what to achieve, not how a particular SOC should be staffed.

### Exercises

- **EX055 — Blue team.** Define the blue team. *Rubric:* 3 = defenders who monitor, detect and respond; 2 = partial; 1 = attackers; 0 = none.
- **EX056 — CSF mapping.** Map two response actions to CSF functions. *Rubric:* 3 = e.g. resets → Respond; MFA decision → Govern; 2 = one; 1 = wrong; 0 = none.
- **EX057 — Maturity result.** What did Riverton's SOC-CMM view show? *Rubric:* 3 = stronger technology than process documentation; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Security operations theory frames SOC functions, frameworks and maturity, which the following chapters apply to the campus case.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security operations and blue team: foundational cases

### Learning outcomes

You will (1) analyse published and synthetic SOC cases; (2) identify detection, triage and response decisions in each; (3) extract lessons that generalise; (4) compare cases with Riverton's campaign.

### 20.1 Learning from cases

Cases show how principles play out under pressure. Lucas studies three: Riverton's phishing campaign, a synthetic ransomware case from a teaching exercise, and the findings of published SOC studies.

### 20.2 Riverton's campaign

Detection came first from user reports, then from the z-score flag on s2047. Containment took about six hours for s2047 because the flag ran only in a morning batch.

### 20.3 Synthetic ransomware exercise

In the course's tabletop exercise, a file server's files are encrypted. Detection comes from users reporting unreadable files; response hinges on isolating the server and restoring from backups. The exercise shows that tested backups decide recovery time.

### 20.4 Published studies

Alahmadi et al. (2022) describe analysts overwhelmed by benign triggers; Kokulu et al. (2019) describe mismatched SOC priorities between managers and analysts. Both explain why Riverton's student analysts sometimes ignore low-severity alerts.

### 20.5 Decision points

In each case Lucas lists decision points: when to escalate, when to contain, whom to inform. Delays often come from unclear authority, not missing tools.

### 20.6 Generalising

Lessons that recur — user reports matter, batch detection is slow, unclear authority delays action — are candidates for SOC improvement.

### 20.7 Limits

Cases are selected and simplified; they illustrate, they do not prove.

### Using cases in training

New student analysts read the case write-ups in their first week, with names removed, and discuss what they would have done at each decision point.

### Worked example

Lucas's comparison table shows that in both the phishing and ransomware cases, the first signal came from people, not tools. He recommends making user reporting faster (a report button in mail) and running the z-score check hourly rather than daily.

> **Synthetic case.** Cases are invented except the cited studies.

### Errors and limits

Synthetic exercises may miss real-world friction.

### Exercises

- **EX058 — Containment delay.** Why did s2047's containment take about six hours? *Rubric:* 3 = z-score check ran in morning batch; 2 = partial; 1 = unknown; 0 = none.
- **EX059 — Recurring lesson.** What lesson recurred across cases? *Rubric:* 3 = first signal from people, not tools; 2 = partial; 1 = none; 0 = none.
- **EX060 — Delay source.** What often causes response delays according to Lucas's analysis? *Rubric:* 3 = unclear authority rather than missing tools; 2 = partial; 1 = tools; 0 = none.

### Synthesis

Cases reveal recurring decision points and delays; their lessons guide improvements when generalised carefully.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security operations and blue team: system models

### Learning outcomes

You will (1) model the SOC as a set of connected components and roles; (2) trace an alert from source to closure; (3) identify where delays and errors arise; (4) use models to plan improvements.

### 21.1 The SOC as a system

Riverton's SOC links log sources, a SIEM, detection rules, a case-management system, analysts and responders in IT. An alert is a message that passes through this chain; every link can delay or distort it.

### 21.2 Tracing an alert

For the s2047 flag: the mail service logged outbound messages; logs arrived in the SIEM within 10 minutes; the z-score job ran at 07:00; the alert entered the case queue; a student analyst picked it up at 08:05; the service desk reset the password at 08:41.

### 21.3 Delays

The largest delay was the gap between activity (from 02:30) and the batch job (07:00). The second was queue time before an analyst picked up the alert, because the morning shift starts at 08:00.

### 21.4 Roles

Student analysts triage; Dr. Kim's two staff engineers maintain tools and handle escalations; the service desk performs resets; the data protection officer handles personal data exposure.

### 21.5 Interfaces

Each hand-off — SIEM to case system, analyst to service desk — has a format and an expected time. Missing expectations cause waits.

### 21.6 Using the model

Lucas annotates the model with measured times from the campaign to show where improvements would matter most.

### 21.7 Feedback loops

Analyst closure reasons feed back to engineers, who tune rules; without this loop, the same noise repeats.

### Worked example

Lucas's annotated model shows 4.5 hours lost to batch timing and 1 hour to queueing. He proposes running the outbound-mail check every 15 minutes and paging the on-call engineer overnight for scores above 50. Dr. Kim approves the first and limits the second to a trial.

> **Synthetic case.** Times and roles are invented.

### Errors and limits

Models simplify; real alerts sometimes skip or repeat stages.

### Exercises

- **EX061 — Alert trace.** Trace the s2047 alert from log to reset with times. *Rubric:* 3 = logged, SIEM in 10 min, 07:00 job, 08:05 pickup, 08:41 reset; 2 = most; 1 = few; 0 = none.
- **EX062 — Main delay.** Where was the largest delay, and why? *Rubric:* 3 = batch job gap from 02:30 to 07:00; 2 = partial; 1 = analyst; 0 = none.
- **EX063 — Proposals.** What two changes did Lucas propose and what was decided? *Rubric:* 3 = 15-minute checks approved; overnight paging trial only; 2 = partial; 1 = one; 0 = none.

### Synthesis

Modelling the SOC as a system shows where time is lost and which changes matter most.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security operations and blue team: data and dependencies

### Learning outcomes

You will (1) inventory the SOC's data sources and their owners; (2) assess data quality, latency and retention; (3) identify dependencies on external services; (4) plan for source failures.

### 22.1 Data inventory

Lucas lists every source: identity sign-ins, mail events, mailbox audit, firewall logs, DNS resolver logs, endpoint logs from staff devices, research server logs (partial), and the phishing report mailbox. For each, he records owner, format, latency, retention and which rules use it.

### 22.2 Quality

Some sources have gaps: DNS logs miss queries from devices using external resolvers; research servers forward inconsistently. Quality problems limit what detections can promise.

### 22.3 Latency

Cloud mail audit events arrive up to 30 minutes late; sign-ins within 5. Detections that combine them must allow for the slower source.

### 22.4 Retention

Cloud audit logs are kept by the provider for 90 days on Riverton's licence; the SOC copies key events to its own store for longer.

### 22.5 External dependencies

The SOC depends on the cloud provider's logging, the identity provider's API and the university network team. A change in any can break collection silently.

### 22.6 Source health

A daily report shows events received per source compared with the usual range. A sudden drop prompts investigation.

### 22.7 Ownership

Each source has a named owner outside the SOC who is told when problems appear.

### Cost of sources

Each source costs licence, storage and analyst attention. Lucas adds a column for the number of alerts each source produced last term, so low-value, high-cost sources can be reviewed.

### Worked example

Lucas's health report shows the research network firewall sent no logs for two days. The network team had replaced the firewall and not re-enabled forwarding. They fix it within an hour; the gap is recorded so analysts know research traffic for those days is unmonitored.

> **Synthetic case.** Sources and figures are invented.

### Errors and limits

Inventories go out of date quickly; review them each term.

### Exercises

- **EX064 — Inventory fields.** What does Lucas record for each source? *Rubric:* 3 = owner, format, latency, retention, rules using it; 2 = three; 1 = one; 0 = none.
- **EX065 — Latency effect.** Why must detections combining mail audit and sign-ins allow for delay? *Rubric:* 3 = mail audit up to 30 min late; 2 = partial; 1 = no reason; 0 = none.
- **EX066 — Firewall gap.** What caused the research firewall gap, and how was it handled? *Rubric:* 3 = replacement without forwarding; fixed, gap recorded; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Know every source, its quality and dependencies, and watch source health so gaps are found quickly.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security operations and blue team: methods I

### Learning outcomes

You will (1) design detections for password guessing patterns; (2) distinguish spraying from single-account brute force; (3) evaluate thresholds on synthetic data; (4) decide alert routing by pattern.

### 23.1 Two guessing patterns

Brute force tries many passwords against one account. Password spraying tries one or two common passwords against many accounts, staying under per-account lockout limits. Both appear in identity logs as failures, but they look different when grouped.

### 23.2 Grouping matters

Grouping failures by source and counting distinct users and attempts per user separates the patterns: spraying shows many users and few attempts each; brute force shows one user and many attempts.

### Lab — spray versus brute force

```python
"""Password-spray pattern: one source, many users, few attempts each, within 30 minutes (synthetic)."""
from collections import defaultdict
fails = [("198.51.100.77", f"s{n}", t) for n, t in zip(range(3000, 3040), range(0, 40))] + \
        [("192.0.2.5", "s1001", t) for t in (1, 2, 3, 4, 5, 6)]
by_src = defaultdict(lambda: defaultdict(int))
for src, user, minute in fails:
    if minute < 30: by_src[src][user] += 1
for src, users in by_src.items():
    per_user = max(users.values())
    kind = "SPRAY" if len(users) >= 20 and per_user <= 2 else ("BRUTE-FORCE ONE USER" if len(users) == 1 and per_user >= 5 else "-")
    print(f"{src:14} users={len(users):3} max attempts/user={per_user} {kind}")
```

Run with `python3 lab_spray.py`. Verified output:

```text
198.51.100.77  users= 30 max attempts/user=1 SPRAY
192.0.2.5      users=  1 max attempts/user=6 BRUTE-FORCE ONE USER
```

### 23.3 Reading the result

In 30 minutes, 198.51.100.77 failed against 30 accounts with at most one attempt each — a spray. 192.0.2.5 failed six times against s1001 only — a brute-force pattern on one account.

### 23.4 Responses differ

Spraying threatens many weak passwords; the response is to check whether any targeted account later signed in successfully and to block the source. Brute force against one account may be a user who forgot a password, or a targeted attack; the response is to contact the account holder.

### 23.5 Thresholds

The lab uses 20 users and 2 attempts per user. Lower thresholds catch slower sprays but raise false alerts from shared campus addresses, such as library computers.

### 23.6 Shared addresses

Campus NAT means many students share one public address; a real spray must be distinguished from a busy lab. The rule excludes known campus egress addresses and handles them with separate thresholds.

### Worked example

Lucas checks whether any of the 30 sprayed accounts signed in successfully afterwards: none did. For 192.0.2.5, s1001's owner says he had changed his password and his old laptop kept retrying. The SOC closes it as benign and suggests he update the saved password.

> **Synthetic case.** Sources and accounts come from the lab script.

### Errors and limits

Attackers can spread sprays across many addresses and long periods; per-source grouping then misses them.

### Exercises

- **EX067 — Pattern difference.** How do spraying and brute force differ in grouped logs? *Rubric:* 3 = spray: many users, few attempts; brute: one user, many attempts; 2 = partial; 1 = same; 0 = none.
- **EX068 — Lab classification.** Classify the two sources in the lab. *Rubric:* 3 = 198.51.100.77 spray (30 users, 1 each); 192.0.2.5 brute force on s1001 (6); 2 = one; 1 = wrong; 0 = none.
- **EX069 — Shared addresses.** Why are campus egress addresses handled separately? *Rubric:* 3 = many users share them; would trigger false sprays; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Group identity failures to reveal patterns, choose responses by pattern, and adapt thresholds to shared campus addresses.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security operations and blue team: controls

### Learning outcomes

You will (1) relate SOC detections to preventive and responsive controls; (2) recommend controls after incidents; (3) evaluate controls for side effects; (4) map controls using D3FEND names.

### 24.1 Controls around detection

Detection works best alongside prevention and response. For phishing: mail filtering and DMARC enforcement prevent; mailbox-rule monitoring detects; password resets and session revocation respond.

### 24.2 After the campaign

The campaign response produced four control changes: required student MFA, disabled legacy mail protocols, blocked automatic external forwarding by default, and added a report button in the mail client.

### 24.3 Side effects

Blocking external forwarding affects staff who forward mail to personal accounts. The university publishes an exception process requiring manager approval and a business reason.

### 24.4 D3FEND naming

MITRE D3FEND names defensive techniques precisely, such as multi-factor authentication and user behaviour analysis. Naming controls this way helps compare them with other organisations and spot gaps.

### 24.5 Control ownership

Each control has an owner: identity team for MFA, mail team for forwarding, SOC for monitoring rules.

### 24.6 Testing controls

After deployment, the SOC tests each control: a test account tries to create an external forwarding rule; the block works and an alert fires.

### 24.7 Cost and benefit

Lucas estimates time saved: forwarding blocks would have prevented the 37 messages leaving s2047's mailbox.

### Rollback

Every control change has a way back. When the forwarding block briefly stopped an automated research mailing list, the mail team added an exception within an hour using the documented process.

### Worked example

Three weeks after the MFA requirement, Lucas compares risky sign-in alerts: successful foreign sign-ins without MFA fall from 14 per week to 2, both from accounts not yet enrolled during a grace period. He reports the trend with the caveat that attackers may shift to MFA fatigue prompts.

> **Synthetic case.** Controls and figures are invented.

### Errors and limits

Controls change behaviour; attackers adapt, so monitoring must follow.

### Exercises

- **EX070 — Control changes.** List the four controls adopted after the campaign. *Rubric:* 3 = student MFA, legacy disabled, forwarding blocked, report button; 2 = three; 1 = one; 0 = none.
- **EX071 — Forwarding side effect.** How was the forwarding block's side effect handled? *Rubric:* 3 = exception process with manager approval and reason; 2 = partial; 1 = ignored; 0 = none.
- **EX072 — MFA trend caveat.** What caveat did Lucas attach to the MFA results? *Rubric:* 3 = attackers may shift to MFA fatigue prompts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Pair detections with preventive and responsive controls, test them, and watch for side effects and attacker adaptation.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) practise triage in a contained lab with synthetic alerts; (2) prioritise a queue by severity and asset criticality; (3) document triage decisions; (4) reflect on prioritisation errors.

### 25.1 The lab

The SOC's training lab contains a copy of the case system loaded with synthetic alerts. No real student or staff data is present.

### 25.2 Prioritisation

Not all alerts are equal. A simple score multiplies alert severity (1–3) by asset criticality (1–3); ties are broken by age so older alerts are not forgotten.

### Lab — ordering a queue

```python
"""Order a triage queue by severity x asset criticality, then age (synthetic alerts)."""
alerts = [("A1","spray detected","medium","idp",3,25), ("A2","mail rule to external","high","mailbox",2,10),
          ("A3","new admin on lab server","high","research-gpu",3,4), ("A4","AV quarantine","low","student-laptop",1,40),
          ("A5","impossible travel","medium","mailbox",2,15)]
sev = {"low":1,"medium":2,"high":3}
for a in sorted(alerts, key=lambda a: (-(sev[a[2]] * a[4]), -a[5])):
    print(f"{a[0]} score={sev[a[2]]*a[4]} age={a[5]:2}m {a[1]} ({a[3]})")
```

Run with `python3 lab_queue_order.py`. Verified output:

```text
A3 score=9 age= 4m new admin on lab server (research-gpu)
A1 score=6 age=25m spray detected (idp)
A2 score=6 age=10m mail rule to external (mailbox)
A5 score=4 age=15m impossible travel (mailbox)
A4 score=1 age=40m AV quarantine (student-laptop)
```

### 25.3 Reading the result

A3 (new administrator on the research GPU server, high severity on a critical asset) scores 9 and comes first. A1 (spray against the identity provider) and A2 (external mail rule) both score 6; A1 is older so comes first. A5 scores 4 and A4, an antivirus quarantine on a student laptop, scores 1.

### 25.4 Triage notes

For each alert, the lab sheet records the decision (benign, suspicious, malicious), evidence checked and next action.

### 25.5 Errors

In the first run, Lucas spends ten minutes on A4 because it is oldest, delaying A3. Ordering by score first prevents this.

### 25.6 Reflection

Scores support but do not replace judgement: an analyst who knows the mail rule matches the s2047 pattern may escalate A2 ahead of A1.

### Lab debrief

After each lab session, student analysts compare their decisions in a short debrief. Disagreements are discussed with evidence, not settled by seniority. Recurring confusion becomes a new note in the triage guide, so the next cohort benefits.

### Worked example

Lucas's lab sheet for A2: "Rule forwards to external address; created 6 minutes after a sign-in from a new country; same pattern as s2047. Decision: malicious (likely). Action: escalate to service desk for reset; disable rule after export." Dr. Kim notes that this judgement correctly overrode the score order.

> **Synthetic case.** Alerts come from the lab script.

### Errors and limits

Simple scores ignore context such as campaign patterns; analysts must think beyond them.

### Exercises

- **EX073 — Score formula.** How is the triage score calculated, and how are ties broken? *Rubric:* 3 = severity × criticality; age breaks ties; 2 = partial; 1 = vague; 0 = none.
- **EX074 — Queue order.** Give the queue order from the lab. *Rubric:* 3 = A3, A1, A2, A5, A4; 2 = most; 1 = wrong; 0 = none.
- **EX075 — Overriding the score.** Why did Lucas escalate A2 ahead of A1? *Rubric:* 3 = matched known s2047 compromise pattern; 2 = partial; 1 = score; 0 = none.

### Synthesis

Scored queues keep triage orderly; documented judgement handles what the score cannot see.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security operations and blue team: methods II

### Learning outcomes

You will (1) build correlation detections across sources; (2) choose time windows using evidence; (3) handle delayed sources; (4) evaluate correlations for misses and noise.

### 26.1 Why correlate

Single events are often ambiguous: a sign-in from abroad may be travel; a new mailbox rule may be routine. Together, a risky sign-in followed soon by a forwarding or deleting rule is much stronger evidence of compromise.

### 26.2 Designing the correlation

Lucas's rule: a sign-in flagged as new-country, followed within a time window by mailbox-rule creation for the same user. The window must allow for mail audit delay (up to 30 minutes) and for attacker behaviour.

### 26.3 Choosing the window

Too short a window misses slow attackers; too long a window links unrelated events. Lucas starts with 60 minutes and evaluates it on known cases from the campaign in Laboratory II.

### 26.4 Delayed sources

Because mail audit events can arrive late, the rule waits 30 minutes after a risky sign-in before deciding no rule followed.

### 26.5 Noise

Students travelling abroad who also tidy their inbox will match. Requiring the rule to forward externally or delete messages by keyword reduces this.

### 26.6 Rule documentation

The rule records its purpose, logic, window, known benign matches and response steps.

### 26.7 ATT&CK reference

Mailbox rules used to hide or forward mail relate to email collection and hiding techniques in ATT&CK; referencing them helps coverage tracking.

### Suppressing duplicates

One compromise can create several matching rules. The rule groups matches per user per day so analysts get one alert with all rules listed, not five.

### Worked example

Lucas tests the correlation on last month's data. It matches s2047 and two travelling staff members who created ordinary folder rules. After restricting rule types to forwarding and keyword deletion, only s2047 remains — but chapter 30 will show the window still misses s3310.

> **Synthetic case.** Rules and data are invented.

### Errors and limits

Correlations multiply dependencies; a broken source silences the whole rule.

### Exercises

- **EX076 — Why correlation.** Why is a risky sign-in plus rule creation stronger than either alone? *Rubric:* 3 = each ambiguous alone; together strong evidence; 2 = partial; 1 = same; 0 = none.
- **EX077 — Delay handling.** How does the rule handle delayed mail audit events? *Rubric:* 3 = waits 30 minutes before deciding no rule followed; 2 = partial; 1 = ignores; 0 = none.
- **EX078 — Noise reduction.** How were travelling staff matches removed? *Rubric:* 3 = restrict to forwarding/keyword-deletion rules; 2 = partial; 1 = removed staff; 0 = none.

### Synthesis

Correlation combines weak signals into strong ones, but windows, delays and dependencies need careful design.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security operations and blue team: verification

### Learning outcomes

You will (1) verify that detections work as specified; (2) measure ATT&CK coverage honestly; (3) distinguish tested from untested rules; (4) plan verification for gaps.

### 27.1 What verification checks

Verification checks that each rule fires on the behaviour it targets and stays quiet otherwise. It uses safe synthetic events in a test environment or approved test accounts in production.

### 27.2 Coverage honestly measured

Coverage is the share of priority ATT&CK techniques with a tested detection. A rule that exists but has never been tested is not counted as coverage, because it may silently fail.

### Lab — coverage status

```python
"""ATT&CK technique coverage for the campus SOC (synthetic status per technique)."""
status = {"T1566 Phishing": "tested", "T1078 Valid Accounts": "tested", "T1110 Brute Force": "tested",
          "T1114 Email Collection": "rule-untested", "T1098 Account Manipulation": "rule-untested",
          "T1021 Remote Services": "none", "T1486 Data Encrypted for Impact": "tested", "T1048 Exfiltration Over Alternative Protocol": "none"}
n = len(status)
for k in ("tested", "rule-untested", "none"):
    items = [t for t, s in status.items() if s == k]
    print(f"{k:13} {len(items)}/{n} = {len(items)/n:.0%}")
print("gaps:", [t.split()[0] for t, s in status.items() if s == "none"])
```

Run with `python3 lab_coverage.py`. Verified output:

```text
tested        4/8 = 50%
rule-untested 2/8 = 25%
none          2/8 = 25%
gaps: ['T1021', 'T1048']
```

### 27.3 Reading the result

Of eight priority techniques, four (50%) have tested detections, two (25%) have rules not yet tested, and two (25%) — remote services (T1021) and exfiltration over alternative protocols (T1048) — have nothing.

### 27.4 Planning

Untested rules are tested first because it is cheap. The two gaps need data sources: remote-service logons on research servers and DNS-based exfiltration detection using resolver logs.

### 27.5 Test design

Each test states input, expected result and pass criteria. For mailbox rules, a test account creates a forwarding rule after a simulated risky sign-in from a test address.

### 27.6 Recording

Results are stored with date, rule version and tester, and repeated each term.

### Who tests

Rules are tested by someone other than their author where possible. An author may unconsciously build a test that matches their own assumptions; a second person tests what the rule claims to detect.

### Worked example

Testing the two untested rules finds one working (account manipulation alert) and one broken: the email collection rule referenced a field renamed by the cloud provider months earlier. After fixing, coverage rises to 6 of 8 tested (75%).

> **Synthetic case.** Statuses come from the lab script; test results are invented.

### Errors and limits

Coverage percentages hide depth: one rule per technique may cover only one way of doing it.

### Exercises

- **EX079 — Honest coverage.** Why are untested rules excluded from coverage? *Rubric:* 3 = may silently fail; not proven; 2 = partial; 1 = included; 0 = none.
- **EX080 — Lab coverage.** Report the coverage figures and gaps. *Rubric:* 3 = 4/8 tested 50%, 2 untested, 2 none: T1021, T1048; 2 = partial; 1 = wrong; 0 = none.
- **EX081 — Broken rule.** Why was the email collection rule broken? *Rubric:* 3 = referenced field renamed by provider; 2 = partial; 1 = unknown; 0 = none.

### Synthesis

Verify each rule with safe tests and count only tested rules as coverage.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security operations and blue team: failure analysis

### Learning outcomes

You will (1) analyse why detections or responses failed; (2) use timelines and contributing factors; (3) avoid blame in reviews; (4) turn findings into actions.

### 28.1 Post-incident review

After the campaign, Riverton holds a review. Its aim is learning: what happened, why defences and response worked or failed, and what to change. NIST SP 800-61r3 treats such lessons as part of continuous improvement.

### 28.2 Timeline

The review builds a timeline from email delivery (01:50) to last containment (s3310 at 11:20). Each entry cites its source.

### 28.3 What failed

s3310 was compromised at 02:31 but not contained until 11:20. Its attacker created a rule deleting messages containing "phishing" — hiding warnings — but no alert fired, because the correlation window had not yet existed and the z-score did not flag s3310 (it sent few messages).

### 28.4 Contributing factors

No MFA for students; legacy protocol enabled; batch detection; no rule for keyword-deletion rules; only one analyst on the early shift.

### 28.5 Blameless approach

The review focuses on systems and decisions, not individuals. People speak openly when they are not blamed.

### 28.6 Actions

Each factor becomes an action with owner and date: MFA requirement, legacy shutdown, 15-minute checks, correlation rule, an extra early shift during campaigns.

### 28.7 Follow-up

Actions are tracked until closed and checked in the next exercise.

### Writing the review

The review report is short: timeline, what went well, what did not, contributing factors and actions. It is shared with IT, the service desk and the data protection officer, and a version without personal details is used in training.

### Worked example

The review asks why s3310 was found at all. Answer: a classmate replied to s3310's phishing email asking if it was real; s3310 never saw the reply (deleted by the rule) but the classmate also reported it. The finding reinforces the value of reporting and of alerting on deletion rules.

> **Synthetic case.** The review is invented.

### Errors and limits

Reviews depend on available logs; unknowns are recorded as such.

### Exercises

- **EX082 — s3310 delay.** Why was s3310 not contained until 11:20? *Rubric:* 3 = deletion rule hid warnings; no alert; low send volume missed by z-score; 2 = partial; 1 = unknown; 0 = none.
- **EX083 — Contributing factors.** List four contributing factors. *Rubric:* 3 = no MFA, legacy protocol, batch detection, no deletion-rule alert, one analyst (four); 2 = three; 1 = one; 0 = none.
- **EX084 — How found.** How was s3310 eventually found? *Rubric:* 3 = classmate's report; 2 = partial; 1 = tools; 0 = none.

### Synthesis

Blameless failure analysis turns timelines and contributing factors into owned actions.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security operations and blue team: operations

### Learning outcomes

You will (1) run shifts and handovers in a student-staffed SOC; (2) manage queues and escalation; (3) support analyst learning and wellbeing; (4) communicate with the university community.

### 29.1 Shifts

Riverton's SOC runs staffed hours from 08:00 to 20:00 on weekdays, with on-call engineers outside them. Student analysts work four-hour shifts around classes.

### 29.2 Handovers

Each shift ends with a handover note: open alerts, cases in progress, system issues and expected events, such as a planned phishing simulation.

### 29.3 Escalation

Student analysts escalate to the duty engineer for anything involving staff accounts, research systems or personal data exposure. Escalation is encouraged; nobody is criticised for escalating in good faith.

### 29.4 Queues

The queue is ordered by the scoring from Laboratory I. During campaigns, the duty engineer may assign alerts directly.

### 29.5 Learning

Student analysts follow a training path: shadowing, supervised triage, then independent triage of low-severity alerts.

### 29.6 Wellbeing

Studies such as Alahmadi et al. (2022) link alert overload to burnout. Shifts are short; analysts rotate between alert types; exam periods have reduced rosters.

### 29.7 Communication

The SOC sends campus notices during campaigns: what the email looks like, what to do if you clicked, and how to report.

### Shift metrics

Each shift records alerts handled, escalations and time to first look. Patterns over a term show when extra cover is needed, such as Monday mornings after weekend campaigns, and help plan rosters before problems arise rather than after.

### Quiet periods

On quiet shifts, analysts review closed alerts for quality.

### Worked example

During exam week, a second campaign arrives with only two analysts on shift. The duty engineer pauses low-severity alerts, sends a campus notice within an hour, and asks staff from IT to help with password resets. Reports peak at 140 in two hours; all compromised accounts are contained the same day.

> **Synthetic case.** Rosters and events are invented.

### Errors and limits

Student availability varies with term; plan staffing around the academic calendar.

### Exercises

- **EX085 — Escalation triggers.** When must student analysts escalate? *Rubric:* 3 = staff accounts, research systems, personal data exposure; 2 = two; 1 = one; 0 = none.
- **EX086 — Wellbeing measures.** Name three measures protecting analyst wellbeing. *Rubric:* 3 = short shifts, rotation, reduced exam rosters; 2 = two; 1 = one; 0 = none.
- **EX087 — Exam-week response.** How did the SOC cope with the exam-week campaign? *Rubric:* 3 = paused low alerts, notice in an hour, IT helped resets, contained same day; 2 = partial; 1 = vague; 0 = none.

### Synthesis

SOC operations combine clear shifts, encouraged escalation, learning paths and attention to wellbeing.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) test a correlation detection against known cases; (2) analyse why a known case was missed; (3) adjust and re-test the rule; (4) document limits after adjustment.

### 30.1 Purpose

Laboratory II tests the correlation rule from chapter 26 against the synthetic reconstruction of the campaign, where the right answers are known.

### 30.2 Setup

The lab contains synthetic sign-ins and mailbox-rule events for s2047, s3310 and s1001, with times in minutes since midnight.

### Lab — correlation against known cases

```python
"""Correlate risky sign-ins with mailbox-rule creation within 60 minutes (synthetic)."""
signins = [("s2047", 134, "NL", "new-country"), ("s3310", 151, "NL", "new-country"), ("s1001", 545, "GB", "normal")]
rules = [("s2047", 140, "forward to external"), ("s1001", 600, "move newsletters"), ("s3310", 300, "delete if 'phishing'")]
for user, t_sign, country, risk in signins:
    if risk == "normal": continue
    for u, t_rule, desc in rules:
        if u == user and 0 <= t_rule - t_sign <= 60:
            print(f"ALERT {user}: risky sign-in {country} at minute {t_sign} then rule '{desc}' at minute {t_rule}")
        elif u == user:
            print(f"no match {user}: rule '{desc}' {t_rule - t_sign} min after sign-in (outside window)")
```

Run with `python3 lab_correlate.py`. Verified output:

```text
ALERT s2047: risky sign-in NL at minute 134 then rule 'forward to external' at minute 140
no match s3310: rule 'delete if 'phishing'' 149 min after sign-in (outside window)
```

### 30.3 Reading the result

The rule alerts on s2047: a risky sign-in at minute 134 (02:14) followed by an external forwarding rule six minutes later. It misses s3310: the deletion rule came 149 minutes after the risky sign-in, outside the 60-minute window.

### 30.4 Analysing the miss

s3310's attacker waited over two hours before hiding warnings, perhaps after seeing replies. Attackers do not follow the defender's assumptions about timing.

### 30.5 Adjusting

Extending the window to 6 hours catches s3310 but risks linking unrelated events. Lucas adds a second, separate rule: any keyword-deletion rule matching words like "phishing" or "hacked" alerts on its own, regardless of sign-in, because such rules are rare and suspicious in themselves.

### 30.6 Re-test

With the 6-hour window plus the keyword rule, both compromised accounts alert and s1001's ordinary folder rule does not.

### Monitoring after change

For a month after the change, Lucas reviews every match of both rules each Friday and records whether it was correct. If false alerts exceed two per week, he will revisit the window.

### Worked example

Lucas's lab report: "60-minute correlation missed s3310 (rule after 149 minutes). Changes: window 6 hours; new stand-alone alert for deletion rules containing warning keywords. Re-test: 2 of 2 compromised accounts detected, 0 false alerts on test data. Limit: test data is small; monitor false alerts for one month."

> **Synthetic case.** Events come from the lab script.

### Errors and limits

Known cases test only what happened before; new attacker timings may still be missed.

### Exercises

- **EX088 — Lab outcome.** Which account was detected and which missed, and why? *Rubric:* 3 = s2047 detected (6 min); s3310 missed (149 min outside 60); 2 = partial; 1 = wrong; 0 = none.
- **EX089 — Two fixes.** What two changes were made? *Rubric:* 3 = 6-hour window; stand-alone keyword-deletion rule; 2 = one; 1 = none; 0 = none.
- **EX090 — Stand-alone logic.** Why can a keyword-deletion rule alert on its own? *Rubric:* 3 = such rules are rare and suspicious regardless of sign-in; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Testing against known cases exposes timing assumptions; fix them and record the limits that remain.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security operations and blue team: advanced cases

### Learning outcomes

You will (1) analyse complex cases involving several systems and teams; (2) handle uncertainty and incomplete data; (3) coordinate response across organisational units; (4) extract lessons from difficult cases.

### 31.1 A harder case

In spring term, the SOC sees unusual SSH logins to a research server from a collaborator's university at night, followed by large outbound transfers. The research group says the collaborator is legitimate; the transfers are larger than usual.

### 31.2 Competing explanations

Possibilities: the collaborator is working late on a big dataset; the collaborator's account at the partner university was compromised; or someone in the group shared credentials. Each predicts different evidence.

### 31.3 Gathering evidence

Lucas checks: login times compared with the collaborator's usual pattern; files transferred (names and sizes from server logs); whether the partner university's SOC sees anything unusual. Contacting the partner goes through Dr. Kim.

### 31.4 Findings

The partner SOC reports that the collaborator's account signed in from an unusual country that night, and the collaborator confirms they were not working. The transfers were of a shared dataset, not personal data.

### 31.5 Coordinated response

The research group disables the collaborator's server access; the partner resets the account; Riverton reviews which data left and informs the data owner.

### 31.6 Uncertainty

Some questions stay open: whether the attacker targeted the research or simply used any access found. The report states this.

### 31.7 Lessons

Research collaborations need shared contacts between SOCs and a way to verify unusual access quickly.

### Time pressure

Large transfers might have continued while questions were asked, so the group paused the collaborator's access within the hour as a precaution.

### Worked example

Lucas's case summary separates facts (logins, transfers, partner findings), inferences (the collaborator's account was compromised) and unknowns (attacker's aim). It recommends listing external collaborators with server access and reviewing them each term.

> **Synthetic case.** The case is invented.

### Errors and limits

Cross-organisation cases depend on others' logs and willingness to share.

### Exercises

- **EX091 — Three explanations.** List three explanations for the night-time SSH activity. *Rubric:* 3 = legitimate late work, partner account compromised, shared credentials; 2 = two; 1 = one; 0 = none.
- **EX092 — Deciding evidence.** What evidence decided the case? *Rubric:* 3 = partner SOC saw unusual country sign-in; collaborator denied working; 2 = partial; 1 = transfer size; 0 = none.
- **EX093 — Collaboration lesson.** What lesson concerns research collaborations? *Rubric:* 3 = shared SOC contacts; verify unusual access quickly; list external collaborators; 2 = partial; 1 = none; 0 = none.

### Synthesis

Complex cases need competing explanations, cross-team evidence and honest reporting of what remains unknown.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security operations and blue team: interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, privacy, HR, communications and academic staff; (2) translate technical findings for non-technical colleagues; (3) respect different professional duties; (4) agree joint procedures.

### 32.1 Many disciplines

SOC incidents touch law (data protection, evidence), HR (staff misconduct), student affairs (student discipline), communications (public statements) and academic departments (research data). Each has its own duties and language.

### 32.2 Legal and privacy

The data protection officer decides on breach notifications; the SOC supplies facts. Legal staff advise when evidence may be needed in proceedings.

### 32.3 HR and student affairs

If an incident suggests misconduct by staff or students, the SOC passes facts to HR or student affairs and does not investigate the person beyond the security question.

### 32.4 Communications

Public statements are written by the communications office with SOC facts; analysts do not speak to journalists.

### 32.5 Academics

Researchers value openness; security requirements must be explained in terms of protecting their work and participants.

### 32.6 Translating

Lucas practises explaining "risky sign-in followed by forwarding rule" as "someone else logged in as the student and set the mailbox to copy their mail elsewhere".

### 32.7 Joint procedures

A shared procedure lists who is informed for each incident type, within what time and through which channel.

### Regular contact

The SOC meets each partner office once a term, not only during incidents. Knowing people beforehand makes urgent calls easier and faster, and lets each side explain its constraints when nothing is on fire.

### Worked example

For the research server case, Lucas prepares two summaries: a technical one for the research group's IT contact and a plain one for the professor and the data owner. The professor's main question is whether participants' data left the server; Lucas answers directly: no, only the shared public dataset was transferred.

> **Synthetic case.** Procedures and summaries are invented.

### Errors and limits

Different disciplines may disagree; escalate disagreements to Dr. Kim rather than deciding alone.

### Exercises

- **EX094 — Staff misconduct.** What does the SOC do if an incident suggests staff misconduct? *Rubric:* 3 = pass facts to HR; do not investigate person beyond security question; 2 = partial; 1 = investigate; 0 = none.
- **EX095 — Translation.** Translate "risky sign-in followed by forwarding rule" for a non-technical reader. *Rubric:* 3 = someone else logged in and set mail to copy elsewhere; 2 = partial; 1 = jargon; 0 = none.
- **EX096 — Professor's question.** What did the professor most want to know, and what was the answer? *Rubric:* 3 = whether participant data left; no, only public dataset; 2 = partial; 1 = vague; 0 = none.

### Synthesis

SOC work succeeds through other disciplines; translate findings, respect their duties and agree procedures in advance.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse quantitative and qualitative data from a SOC study; (2) use appropriate statistics and coding; (3) assess validity and reliability; (4) report findings with limits.

### 33.1 Returning to the study

Lucas's survey on student reporting (chapter 18) received 412 responses, and he conducted five interviews.

### 33.2 Quantitative analysis

61% of respondents said they would delete a suspicious email without reporting; 24% would report; 15% were unsure. With 412 responses, the margin of error is roughly ±5 percentage points, assuming responses are representative.

### 33.3 Qualitative coding

Interview transcripts are coded into themes: "didn't know how to report" (four of five), "thought IT already knew" (three), "worried about looking foolish" (two). A second student codes two transcripts independently; they agree on most codes and discuss differences.

### 33.4 Validity

Volunteers may be more security-aware than average, so true reporting may be even lower. Self-reported intentions may differ from actual behaviour; log data on actual reports helps triangulate.

### 33.5 Reliability

Clear code definitions and double coding make qualitative results more reliable.

### 33.6 Triangulation

Actual reporting rates from chapter 1 (3.0 per 1,000 students) are consistent with low reporting intentions.

### 33.7 Reporting

The report gives numbers with uncertainty, quotes that illustrate themes, and limits.

### Ethical reporting

Quotes are chosen to illustrate themes without identifying speakers: course names, years and unusual details are removed. Participants were told how quotes would be used before they agreed to take part. Lucas also shares a short summary of findings with participants, as promised in the consent form, before the full report is submitted.

### Sharing the instrument

The questionnaire is published as an appendix so others can repeat the survey.

### Worked example

Lucas's main finding: "Most students who received suspicious email would delete it without reporting (61%, ±5 points); interviews suggest the main barrier is not knowing how to report." This supports the report button introduced in chapter 24 and suggests adding a one-line explanation in the student newsletter.

> **Synthetic case.** The survey data are invented.

### Errors and limits

One university's survey cannot represent students elsewhere.

### Exercises

- **EX097 — Survey results.** Report the three response shares and the margin of error. *Rubric:* 3 = 61% delete, 24% report, 15% unsure; ±5 points; 2 = partial; 1 = one; 0 = none.
- **EX098 — Main theme.** What was the most common interview theme? *Rubric:* 3 = did not know how to report (4 of 5); 2 = partial; 1 = other; 0 = none.
- **EX099 — Validity threat.** Name one validity threat and its likely direction. *Rubric:* 3 = volunteers more aware → true reporting even lower; or intentions ≠ behaviour; 2 = partial; 1 = none; 0 = none.

### Synthesis

Analyse mixed data carefully, triangulate with logs and report findings with honest limits.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare SOC practices across organisations or approaches; (2) choose fair criteria; (3) gather comparable evidence; (4) draw balanced conclusions.

### 34.1 The project

Lucas and two classmates compare how three universities' SOCs handle phishing reports: Riverton (internal student-staffed), a partner university using a managed provider, and a third with a regional shared SOC.

### 34.2 Criteria

They compare time from report to acknowledgement, whether reporters get feedback, automation of mailbox searches, and staffing model, using the same definitions for each.

### 34.3 Evidence

Each SOC shares anonymised figures for one term and a description of its process. No personal data is exchanged.

### 34.4 Findings

The managed provider acknowledges fastest (median 6 minutes) but rarely gives reporters feedback; Riverton is slower (median 22 minutes in staffed hours) but replies to every reporter; the regional SOC automates mailbox purges best.

### 34.5 Balanced conclusions

No model is best on all criteria. Feedback to reporters, which Riverton does well, encourages reporting; speed and automation, which others do well, reduce exposure.

### 34.6 Fairness

Differences in size and threat exposure limit comparison; the project states these.

### 34.7 Recommendations

Riverton adopts automated purges of reported phishing from all mailboxes, with feedback kept.

### Process of the project

The team agreed definitions with all three SOCs before collecting figures, met them online twice and sent each a draft of its own section for factual correction. This avoided misreporting another organisation's practice and built goodwill for future sharing. Each SOC approved its section before the report was submitted.

### Limits of anonymised figures

Anonymised medians hide spread: a median of 6 minutes may include some reports waiting hours. The team asks each SOC for 90th percentiles too.

### Worked example

The team's comparison table lists each criterion with values and sources. Their conclusion: "Riverton should keep personal feedback to reporters and adopt automated purges; a managed provider might improve night-time speed but would need a feedback agreement."

> **Synthetic case.** Universities and figures are invented.

### Errors and limits

Three cases cannot establish general rules.

### Exercises

- **EX100 — Comparison criteria.** List the four comparison criteria. *Rubric:* 3 = acknowledgement time, reporter feedback, purge automation, staffing; 2 = three; 1 = one; 0 = none.
- **EX101 — Trade-off finding.** What trade-off did the comparison reveal? *Rubric:* 3 = speed vs feedback; no model best everywhere; 2 = partial; 1 = one best; 0 = none.
- **EX102 — Adopted change.** What did Riverton adopt from the comparison? *Rubric:* 3 = automated purges, keeping feedback; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fair comparisons use shared criteria and comparable evidence, and lead to balanced, specific improvements.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone project addressing a real SOC need; (2) define aims, requirements and evaluation; (3) plan ethics, data and risks; (4) obtain approval.

### 35.1 Choosing the need

From the campaign review and coverage work, Lucas chooses: "Improve detection of compromised student mail accounts, measured against authorised test scenarios."

### 35.2 Aims

Aim 1: combine the correlation and keyword-deletion rules into a tested detection package. Aim 2: add detection of mass internal mailing by newly risky accounts. Aim 3: measure detection rate before and after on a set of 20 authorised test scenarios.

### 35.3 Requirements

Detect at least 80% of test scenarios; no more than three false alerts per week in production; alerts within 30 minutes of the triggering activity.

### 35.4 Test scenarios

Twenty scenarios are designed with Dr. Kim: each uses university test accounts and benign actions, such as a test sign-in from a test address and creation of a forwarding rule to a test mailbox. No real accounts are touched.

### 35.5 Ethics and data

The project uses SOC data under existing policy; personal data is not taken off university systems; the report uses aggregates only.

### 35.6 Risks

Test scenarios may not resemble real attacks; mitigated by basing them on the campaign's actual behaviours. False alerts may disturb analysts; mitigated by monitor-only mode first.

### 35.7 Approval

Dr. Kim and Lucas's academic supervisor sign the proposal.

### Timeline

Weeks 1–3: package rules and write tests. Weeks 4–5: design mass-mailing detection. Week 6: run before-scenarios. Weeks 7–8: monitor-only deployment. Week 9: run after-scenarios. Weeks 10–12: analysis and report.

### Supervision

Lucas meets his academic supervisor fortnightly and Dr. Kim weekly. Each meeting ends with agreed next steps recorded in a shared log, so slippage is visible early.

### Worked example

Lucas's evaluation plan: run the 20 scenarios against the existing rules (before) and against the new package (after), report detection proportions with confidence intervals, and record false alerts in production for four weeks.

> **Synthetic case.** The proposal is invented.

### Errors and limits

Proposals change; record changes with reasons.

### Exercises

- **EX103 — Three aims.** State the three capstone aims. *Rubric:* 3 = package rules, add mass-mailing detection, measure before/after on 20 scenarios; 2 = two; 1 = one; 0 = none.
- **EX104 — Test safety.** How are test scenarios kept safe? *Rubric:* 3 = university test accounts, benign actions, no real accounts; 2 = partial; 1 = none; 0 = none.
- **EX105 — Requirements.** List the three requirements. *Rubric:* 3 = ≥80% detection, ≤3 false/week, within 30 min; 2 = two; 1 = one; 0 = none.

### Synthesis

A capstone proposal links a real need to measurable aims, safe tests and approved plans.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply SOC skills in a community setting; (2) adapt advice to small organisations; (3) teach basic security practices; (4) reflect on community engagement.

### 36.1 The placement

As part of the degree, Lucas spends four weeks helping a local charity, the fictional **Eastbank Youth Centre**, which has twelve staff, a cloud mail service and no IT team.

### 36.2 Understanding the setting

The charity cannot run a SOC. Its risks are similar to Riverton's on a small scale: phishing, account compromise and lost devices.

### 36.3 Practical improvements

With the manager's permission, Lucas helps enable MFA for all staff, turns on the mail service's built-in alerts for suspicious sign-ins and forwarding rules, and sets alerts to go to two named staff members.

### 36.4 Teaching

He runs a 30-minute session on recognising phishing and how to report it, using examples adapted from Riverton's campaign with all identifying details removed.

### 36.5 Simple procedures

A one-page "what to do if" sheet covers clicked links, lost phones and strange emails, with contact numbers.

### 36.6 Boundaries

Lucas does not access staff mailboxes or personal data; he configures settings with the manager present and leaves documentation.

### 36.7 Reflection

Advice must fit the organisation's capacity; a perfect plan the charity cannot maintain is worse than a simple one it can.

### Handing over

Before leaving, Lucas walks the two named staff through the alert emails and the one-page sheet, and arranges a check-in call a month later.

### Worked example

Two weeks after the session, a staff member reports a suspicious email using the new sheet; the built-in alert also fires for a forwarding rule created on her account after she entered her password. The manager follows the sheet: resets the password and removes the rule. No data left the account.

> **Synthetic case.** The charity and events are invented.

### Errors and limits

Community help is limited by time; leave documentation and contacts so improvements last.

### Exercises

- **EX106 — Built-in alerts.** Which built-in alerts were enabled? *Rubric:* 3 = suspicious sign-ins and forwarding rules; 2 = one; 1 = none; 0 = none.
- **EX107 — Boundaries.** What boundaries did Lucas keep? *Rubric:* 3 = no mailbox or personal data access; configure with manager present; documentation; 2 = partial; 1 = none; 0 = none.
- **EX108 — Capacity principle.** Why must advice fit the charity's capacity? *Rubric:* 3 = unmaintainable perfect plan worse than simple maintainable one; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Community practice adapts SOC thinking to small organisations through simple controls, teaching and lasting documentation.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) present evidence from projects for peer review; (2) critique others' evidence constructively; (3) identify weak inferences and missing data; (4) improve evidence before final reports.

### 37.1 The seminar

Final-year students present their capstone evidence so far. Each presentation shows claims, the evidence behind them and open questions.

### 37.2 Lucas's evidence

He shows before-scenario results (11 of 20 detected), monitor-only false alerts (four in two weeks) and the design of the mass-mailing detection.

### 37.3 Peer critique

A classmate asks whether the 20 scenarios include slow attackers like s3310. Another asks whether four false alerts in two weeks meets the "three per week" requirement or whether two weeks is too short to judge.

### 37.4 Weak inferences

Dr. Kim notes Lucas's slide says "the package will detect most compromises"; the evidence supports only "detects most test scenarios".

### 37.5 Missing data

Lucas has not yet recorded how long each detection took; the 30-minute requirement cannot be assessed.

### 37.6 Responding

Lucas adds two slow-attacker scenarios (replacing two duplicates), starts recording detection times, and changes the wording.

### 37.7 Critiquing others

He questions a classmate's claim that a new dashboard "reduced workload" when the only evidence was analysts' impressions; he suggests counting alerts handled per shift.

### Preparing for critique

Before the seminar, each student writes the three questions they most fear being asked and brings the evidence they have for each. Lucas's list included false-alert rates, which turned out to be exactly what a classmate asked about. Preparing this way makes critique a working session rather than a defence.

### Recording

Notes from the seminar are added to the project log.

### Worked example

Lucas's revised claim: "In authorised test scenarios, the existing rules detected 11 of 20; after the package, we expect to report detection with a confidence interval and detection times for each scenario." The wording now matches what the evidence can show.

> **Synthetic case.** The seminar is invented.

### Errors and limits

Peer review improves evidence but cannot replace testing.

### Exercises

- **EX109 — Peer questions.** What two peer questions challenged Lucas's evidence? *Rubric:* 3 = slow attackers in scenarios; two weeks too short for false-alert rate; 2 = one; 1 = none; 0 = none.
- **EX110 — Weak claim.** What overclaim did Dr. Kim identify? *Rubric:* 3 = "will detect most compromises" vs "detects most test scenarios"; 2 = partial; 1 = none; 0 = none.
- **EX111 — Changes made.** What did Lucas change after the seminar? *Rubric:* 3 = added slow scenarios, recorded detection times, reworded; 2 = two; 1 = one; 0 = none.

### Synthesis

Evidence review seminars sharpen claims, expose gaps and improve projects before final reporting.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement the capstone detection package; (2) follow change control and testing; (3) deploy in stages; (4) record implementation evidence.

### 38.1 Building the package

The package contains the 6-hour correlation rule, the keyword-deletion rule and a new mass-mailing rule: alert when an account that had a risky sign-in in the past day sends to more than 50 internal recipients it has never mailed before.

### 38.2 Tests

Each rule has unit tests in the SOC's test harness and a set of synthetic events. Tests run before each change.

### 38.3 Change control

Lucas submits each rule through the SOC's change process with a description, test results and rollback steps. Dr. Kim approves.

### 38.4 Staged deployment

Rules run in monitor-only mode for two weeks, recording matches without alerting analysts. Lucas reviews every match.

### 38.5 Monitor-only findings

The mass-mailing rule matches a student society officer who emailed new members after signing in from abroad on holiday. Lucas adds a check: alert only if the messages share a subject with messages already reported as phishing, or if links point to domains first seen that week.

### 38.6 Going live

After a clean second week, the package moves to alerting for analysts.

### 38.7 Evidence

Commits, test outputs, change tickets and monitor-only reviews are filed for the capstone dossier.

### Documentation for maintainers

Each rule in the package has a page: purpose, logic, thresholds and why they were chosen, known benign matches, tests and owner. The student analysts who maintain the rules after Lucas graduates can change them without guessing his intentions.

### Worked example

In the first live week, the package alerts once: a compromised account sends 120 messages with a link to a domain registered four days earlier. The account is contained within 25 minutes of the first message, inside the 30-minute requirement.

> **Synthetic case.** Rules and events are invented.

### Errors and limits

A week of live data shows early behaviour only.

### Exercises

- **EX112 — Mass-mailing rule.** State the mass-mailing rule. *Rubric:* 3 = risky sign-in in past day + >50 new internal recipients; 2 = partial; 1 = vague; 0 = none.
- **EX113 — Society officer.** How was the society officer match handled? *Rubric:* 3 = added check for reported subjects or new domains; 2 = partial; 1 = ignored; 0 = none.
- **EX114 — Live result.** What happened in the first live week? *Rubric:* 3 = one alert; 120 messages, new domain; contained in 25 min; 2 = partial; 1 = none; 0 = none.

### Synthesis

Implement with tests, change control and monitor-only stages, adjusting rules from observed matches.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against its requirements; (2) compute detection rates with confidence intervals; (3) analyse false alerts and detection times; (4) state limitations.

### 39.1 Evaluation design

The 20 authorised scenarios are run before (existing rules) and after (new package). Each scenario is scored detected or missed, with detection time.

### Lab — detection rates with intervals

```python
"""Wilson 95% interval for the capstone detection rate on authorised test scenarios (synthetic)."""
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for label, k, n in (("before", 11, 20), ("after", 18, 20)):
    lo, hi = wilson(k, n)
    print(f"{label:6} detected {k}/{n} = {k/n:.2f}  95% CI [{lo:.2f}, {hi:.2f}]")
```

Run with `python3 lab_wilson.py`. Verified output:

```text
before detected 11/20 = 0.55  95% CI [0.34, 0.74]
after  detected 18/20 = 0.90  95% CI [0.70, 0.97]
```

### 39.2 Reading the result

Before: 11 of 20 detected (0.55, 95% interval 0.34–0.74). After: 18 of 20 (0.90, interval 0.70–0.97). The intervals overlap only slightly; with 20 scenarios, uncertainty is large, but the improvement is consistent with the design.

### 39.3 Misses

The two missed scenarios used a forwarding rule to an internal account that then forwarded externally — a pattern none of the rules covered. They become future work.

### 39.4 Detection times

Median detection time was 14 minutes; the slowest was 27 minutes, within the 30-minute requirement.

### 39.5 False alerts

Over four weeks live, false alerts averaged 1.5 per week, below the three-per-week requirement.

### 39.6 Requirements summary

Detection ≥80%: met (90%, though the interval's lower bound is 70%). False alerts ≤3/week: met. Within 30 minutes: met.

### Analyst feedback

Lucas asks the six student analysts whether the new alerts were clear. Five say the alert text, which lists the risky sign-in, the rule created and the recipients, let them decide quickly; one asks for a link to the user's sign-in history, which he adds. Analysts' experience is part of evaluation: a rule that detects but confuses slows response.

### Comparison with the baseline period

In the four weeks before the package, two real compromises were found by user reports after several hours. In the four weeks after, one real compromise was detected by the package in 25 minutes.

### Worked example

Lucas writes: "The package met all three requirements on test scenarios and four weeks of operation. Because the lower confidence bound for detection is 0.70, below the 0.80 target, we cannot claim the target is met with confidence; more scenarios are needed."

> **Synthetic case.** Results come from the lab script and invented operation data.

### Errors and limits

Test scenarios approximate attacks; operational detection rates may differ.

### Exercises

- **EX115 — Lab intervals.** Report before and after detection with intervals. *Rubric:* 3 = 0.55 [0.34, 0.74]; 0.90 [0.70, 0.97]; 2 = one; 1 = wrong; 0 = none.
- **EX116 — Missed pattern.** What pattern did the missed scenarios use? *Rubric:* 3 = internal forward then external; 2 = partial; 1 = unknown; 0 = none.
- **EX117 — Confidence caveat.** Why can Lucas not claim the 80% target is met with confidence? *Rubric:* 3 = lower bound 0.70 below 0.80; more scenarios needed; 2 = partial; 1 = he can; 0 = none.

### Synthesis

Evaluate against each requirement with intervals and honest caveats, and turn misses into future work.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis on the capstone; (2) present findings to academic and SOC audiences; (3) reflect on learning across the degree; (4) plan next steps.

### 40.1 Thesis structure

Introduction; background (campus threats, SOC practice, literature); the campaign and review; method (rules, tests, scenarios); implementation; evaluation; discussion; limitations; conclusions; references; appendices.

### 40.2 Literature in the thesis

Lucas draws on Alahmadi et al. (2022) for alarm quality, Axelsson (2000) for base rates, Sundaramurthy et al. (2014) for SOC practice, NIST SP 800-61r3 for response and SigmaHQ conventions for rule documentation.

### 40.3 Discussion

The package improved detection of test scenarios and fit analyst capacity; reporting by people remained crucial; attackers' timing defeated early assumptions.

### 40.4 Limitations

One university; 20 scenarios; four weeks; scenarios designed by defenders; student population specific.

### 40.5 Presentation

A 15-minute talk to the department and a separate 10-minute briefing to the SOC team focusing on how to maintain the package.

### 40.6 Reflection

From mathematical reasoning in chapter 1 to the evaluation, the degree built habits: measure fairly, write precisely, act within authority, test assumptions.

### 40.7 Next steps

Lucas plans to apply for a junior analyst role and to keep contributing rule improvements to the SOC's repository as an alumnus volunteer under supervision.

### Archiving

The final rules, tests, scenarios (without personal data) and analysis scripts are stored in the SOC repository with a README, so the evaluation can be repeated next year with new scenarios and compared directly with Lucas's results.

### Acknowledgements

The thesis thanks the student analysts and Dr. Kim, and states that no personal data appears in it.

### Worked example

At the presentation, a lecturer asks what Lucas would do with more time. He answers: "Expand scenarios to 60 to narrow the interval, cover internal-then-external forwarding, and measure whether the report button increased student reporting rates."

> **Synthetic case.** The thesis and presentation are invented.

### Errors and limits

A thesis records one project; the SOC must keep improving after the student leaves.

### Exercises

- **EX118 — Thesis sections.** List the main thesis sections in order. *Rubric:* 3 = introduction to appendices in order; 2 = most; 1 = few; 0 = none.
- **EX119 — Two audiences.** How did the two presentations differ? *Rubric:* 3 = department talk on findings; SOC briefing on maintenance; 2 = partial; 1 = same; 0 = none.
- **EX120 — More time.** What would Lucas do with more time? *Rubric:* 3 = 60 scenarios, internal-external forwarding, measure report-button effect; 2 = two; 1 = one; 0 = none.

### Synthesis

The thesis and presentations close the degree by showing measured improvement, honest limits and habits that carry into practice.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Lucas Moreau, Dr. Hana Kim, Riverton University, Eastbank Youth Centre and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Students outnumber staff more than five to one, so only rates show which group reported proportionally more.

**EX002.** Students reported 3.0 and clicked 1.5 per 1,000; staff reported 12.8 and clicked 1.9 per 1,000.

**EX003.** Students click about as often as staff but report much less: 0.50 clicks per report against 0.15.

**EX004.** The identity provider, the mail service and the Wi-Fi controllers.

**EX005.** Students use personal, unmanaged laptops that send no logs, so only university services record their activity.

**EX006.** Wi-Fi controller logs were not forwarded, so the SOC could not tell whether sign-ins came from campus.

**EX007.** Variables, loops, conditions and dictionaries.

**EX008.** Count them under "unknown" and report how many, rather than crashing.

**EX009.** The export listed each delivery attempt; de-duplicating by recipient gave 6,980 unique recipients.

**EX010.** State the claim, give evidence, explain how it supports the claim, and note limits.

**EX011.** Yes; a paraphrase still uses someone else's idea and must be cited.

**EX012.** It narrows the claim to what the study found, cites it and uses accurate terms.

**EX013.** Read mail, create rules that hide or forward messages, and send further phishing to the victim's contacts.

**EX014.** They often arrive before any technical detection and point analysts to the campaign.

**EX015.** It reset her password, signed out her sessions, checked for new mail rules and thanked her.

**EX016.** Accounts that clicked the link and later signed in from an unusual country — the most likely compromised accounts.

**EX017.** The account suddenly gains many new outgoing edges to people it never mailed before.

**EX018.** 33 × 32 ÷ 2 = 528 pairs.

**EX019.** Because VPNs, mobile networks and cloud services can make addresses appear in the wrong country.

**EX020.** That the sender's claimed domain had not authorised the message, a sign of spoofing.

**EX021.** Only campus resolvers are logged, and caching or off-campus clicks are not counted, so the real number may be higher.

**EX022.** Comparing minutes without hours broke matches across hour boundaries; using datetime objects fixed it.

**EX023.** So anyone can see how much data was processed and how much was skipped.

**EX024.** Its inputs, outputs and known limits.

**EX025.** s2047 with two successful sign-ins and s3310 with one.

**EX026.** That someone failed and then succeeded, consistent with an attacker trying the stolen password again.

**EX027.** It shows each user's normal countries, so genuine travel is not mistaken for compromise.

**EX028.** Only with case-specific approval from Dr. Kim.

**EX029.** Declare the connection and pass the alert to another analyst.

**EX030.** A limited review of the subjects of forwarded messages only.

**EX031.** Because it grants administrative power, which attackers try to obtain.

**EX032.** Only if the server records group changes and forwards those logs to the SOC.

**EX033.** The change came from the server administrator in the physics building for a new PhD student, so it was closed as authorised with a suggestion to ticket such changes.

**EX034.** It is today's value minus the account's mean, divided by its standard deviation — how many typical spreads away today is.

**EX035.** s2047 with z about 215; s1001 and the library account had z near 2, below the threshold of 4.

**EX036.** With so many accounts, a low threshold would flag thousands of normal days, overwhelming analysts.

**EX037.** A sign-in from a new country or device, impossible travel, and use of legacy protocols that bypass MFA.

**EX038.** They do not support MFA, so a stolen password alone still grants access through them.

**EX039.** Mandatory MFA for students and disabling legacy mail protocols.

**EX040.** Using security sign-in logs to check whether students attend lectures.

**EX041.** It collects metadata by default and accesses content only with case approval and only as needed.

**EX042.** That the three students whose marks were in forwarded messages must be informed.

**EX043.** It is an inference drawn from observations such as the foreign sign-in and the new rule.

**EX044.** Because different actions (password reset versus all sessions revoked) give different times, making comparisons unreliable.

**EX045.** As a range explained by its sources, such as DNS lookups and user reports.

**EX046.** Because mail and identity, the main targets, run in the cloud and are visible mainly through provider logs.

**EX047.** Limit inbound SSH to the university VPN and campus networks, with key-based login.

**EX048.** Mail filtering, multi-factor authentication and monitoring of mailbox rule changes.

**EX049.** Identifying exact files and confirming that preserved evidence has not changed.

**EX050.** That the message was signed by the claimed domain and not changed in transit.

**EX051.** Each copy included the recipient's name, so contents differed; campaigns are grouped by subject and link instead.

**EX052.** The survey shows how common views are, while interviews explain the reasons in depth.

**EX053.** "How do you usually handle suspicious emails?" instead of "Why don't you report phishing?"

**EX054.** Students misread the reporting question as asking about phishing knowledge; it became an open scenario question.

**EX055.** The defending side that monitors, detects and responds to threats.

**EX056.** Password resets belong to Respond, and the decision to require student MFA belongs to Govern.

**EX057.** Technology was more mature than process documentation.

**EX058.** The anomaly check ran only once each morning, so the flag came hours after the activity.

**EX059.** In both cases the first signal came from people reporting problems, not from tools.

**EX060.** Unclear authority over who decides, more than a lack of tools.

**EX061.** Outbound mail was logged and reached the SIEM within 10 minutes; the 07:00 job flagged it; an analyst picked it up at 08:05; the reset happened at 08:41.

**EX062.** Between the activity starting around 02:30 and the 07:00 batch job, because detection ran only once a day.

**EX063.** Running the check every 15 minutes, approved, and overnight paging for very high scores, approved only as a trial.

**EX064.** Owner, format, latency, retention and which rules depend on it.

**EX065.** Because mail audit events can arrive up to 30 minutes after sign-ins, so a combined rule must wait for them.

**EX066.** A replaced firewall had not been set to forward logs; it was fixed and the two-day gap recorded.

**EX067.** Spraying shows many users with one or two attempts each; brute force shows one user with many attempts.

**EX068.** 198.51.100.77 is a spray against 30 accounts; 192.0.2.5 is repeated guessing against s1001 alone.

**EX069.** Many students share those addresses, so normal mistakes could look like a spray.

**EX070.** Mandatory student MFA, disabling legacy mail protocols, blocking automatic external forwarding and adding a report button.

**EX071.** Through an exception process requiring manager approval and a business reason.

**EX072.** That attackers may switch to bombarding users with MFA prompts, so monitoring must adapt.

**EX073.** Severity multiplied by asset criticality, with older alerts first when scores tie.

**EX074.** A3, then A1, A2, A5 and A4.

**EX075.** Because A2 matched the pattern of the known compromise, making it more urgent than its score suggested.

**EX076.** Each alone has innocent explanations, but together they strongly indicate compromise.

**EX077.** It waits 30 minutes after a risky sign-in before concluding that no rule was created.

**EX078.** By restricting matching rules to external forwarding or deletion by keyword.

**EX079.** Because they might not work; only tested rules are proven to detect.

**EX080.** Four of eight tested (50%), two untested (25%), two with nothing (25%): T1021 and T1048.

**EX081.** It used a field name the cloud provider had renamed months before.

**EX082.** Its attacker's deletion rule hid warnings, no rule covered such deletion, and its low sending volume did not trigger the z-score check.

**EX083.** No student MFA, legacy protocols enabled, once-daily detection and no alert for keyword-deletion rules.

**EX084.** A classmate who received its phishing email reported it.

**EX085.** For anything involving staff accounts, research systems or exposure of personal data.

**EX086.** Short shifts, rotation between alert types and reduced rosters during exams.

**EX087.** It paused low-severity alerts, issued a campus notice within an hour, borrowed IT staff for resets and contained all accounts the same day.

**EX088.** s2047 was detected because its rule came six minutes after sign-in; s3310 was missed because its rule came 149 minutes later.

**EX089.** The window was extended to six hours and a separate alert for deletion rules with warning keywords was added.

**EX090.** Because rules deleting messages containing words like "phishing" are rare and suspicious in themselves.

**EX091.** The collaborator working late, the collaborator's partner-university account being compromised, or credentials shared within the group.

**EX092.** The partner SOC saw an unusual sign-in for the collaborator's account and the collaborator confirmed they were not working.

**EX093.** Collaborations need SOC-to-SOC contacts and a regularly reviewed list of external people with server access.

**EX094.** It gives the facts to HR and does not investigate the person beyond the security question.

**EX095.** Someone else logged in as the user and set their mailbox to send copies of their mail somewhere else.

**EX096.** Whether participants' data had left the server; it had not, only a shared public dataset.

**EX097.** 61% would delete, 24% would report and 15% were unsure, with a margin of about ±5 percentage points.

**EX098.** Not knowing how to report, mentioned in four of five interviews.

**EX099.** Volunteers may be more security-aware than average, so true reporting is probably even lower.

**EX100.** Time to acknowledgement, feedback to reporters, automation of mailbox searches and staffing model.

**EX101.** The fastest SOC gave little feedback to reporters while Riverton was slower but replied to everyone; no model won on every criterion.

**EX102.** Automated removal of reported phishing from all mailboxes, while keeping personal feedback.

**EX103.** Package the correlation and deletion rules with tests, add detection of mass internal mailing by risky accounts, and measure detection before and after on 20 scenarios.

**EX104.** They use university test accounts and harmless actions only, never real people's accounts.

**EX105.** At least 80% of scenarios detected, at most three false alerts a week, and alerts within 30 minutes.

**EX106.** Alerts for suspicious sign-ins and for forwarding rules.

**EX107.** He did not access mailboxes or personal data, made changes with the manager present and left documentation.

**EX108.** Because a perfect plan they cannot maintain helps less than a simple one they can keep running.

**EX109.** Whether the scenarios included slow attackers, and whether two weeks was enough to judge the false-alert rate.

**EX110.** Saying the package "will detect most compromises" when evidence covered only test scenarios.

**EX111.** He added two slow-attacker scenarios, began recording detection times and narrowed his wording.

**EX112.** Alert when an account with a risky sign-in in the past day sends to over 50 internal recipients it has never mailed before.

**EX113.** A check was added requiring a subject already reported as phishing or links to domains first seen that week.

**EX114.** One alert for an account sending 120 messages linking to a new domain, contained within 25 minutes.

**EX115.** Before 11/20 = 0.55 (0.34–0.74); after 18/20 = 0.90 (0.70–0.97).

**EX116.** A forwarding rule to an internal account that then forwarded externally.

**EX117.** Because the interval's lower bound is 0.70, under the target, so more scenarios are needed.

**EX118.** Introduction, background, campaign and review, method, implementation, evaluation, discussion, limitations, conclusions, references and appendices.

**EX119.** The department talk covered findings; the SOC briefing focused on maintaining the package.

**EX120.** Run 60 scenarios, cover internal-then-external forwarding and measure whether the report button raised student reporting.

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
