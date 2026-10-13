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
- **EX006 — Map gap.** What gap did Lucas's map reveal? *Rubric:* 3 = Wi-Fi logs not forwarded; cannot tell campus origin; 2 = partial; 1 = vague; 0 = none.

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

In the case, the attacker used s2047 to create a rule forwarding its mail to an external address and then sent the library-fines email to the account's contacts. Recipients saw a message from a classmate's real address, which made them more likely to click. This is how one stolen password can extend a campaign.

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

Written precisely, the rule can be checked against cases. For s2047, a sign-in from a new country was followed six minutes later by a rule forwarding mail to an external address, so the rule fires. A student who travels home and signs in from there, but creates no rule, does not trigger it. Each part of the condition removes a source of false alarms.

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
- **EX017 — Graph spread.** How does a mail graph reveal a spreading account? *Rubric:* 3 = many new outgoing edges after compromise time; 2 = partial; 1 = vague; 0 = none.
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

In the case, a student who signed in from home over a mobile network appeared to be in another country for a few minutes, because the operator routed traffic through a gateway abroad. Lucas therefore treats a single odd country as a lead, not a conclusion, and looks for supporting signs such as a new mailbox rule or an unusual client application.

### 7.2 DNS

DNS translates names such as riverton.example.ac.uk into addresses. The phishing page used riverton-library.example.net, a look-alike name. DNS logs from campus resolvers show which devices looked it up.

The look-alike domain was chosen to pass a quick glance: it contained the university's name and the word library, but sat under a different parent domain that Riverton did not own. Lucas checks a suspicious name by reading it from the right, since the part just before the final suffix shows who actually controls it. Here, that was not Riverton.

### 7.3 HTTP and HTTPS

Web pages use HTTP over TLS. The fake sign-in page received passwords by HTTPS POST; network sensors see only the destination name, not the password.

For the SOC, this means network sensors cannot confirm which students typed their passwords; they can only show that a device connected to the fake page. Confirmation came from the other end, when a stolen password was used at the identity provider. The fake page itself had a valid certificate, so a padlock in the browser proved nothing about the site's honesty.

### 7.4 Email protocols

Mail travels between servers by SMTP. Message headers record each server hop. Authentication results — SPF, DKIM and DMARC — show whether the sending domain authorised the message; the phishing email failed DMARC for its claimed sender.

Lucas reads the headers from the bottom up, since each server adds its line at the top. The lowest received line showed the message entering from a hosting provider unrelated to Riverton or the library. The failed DMARC result confirmed the sender's address was forged, which helped the mail team write a filter blocking the remaining copies.

### 7.5 Reading sign-in logs

A sign-in record shows time, user, IP, country, client application and result. s2047's 02:14 sign-in came from an address geolocated to the Netherlands using a desktop mail protocol.

Two details made this record stand out. The country was unusual for a student who had only ever signed in from the United Kingdom, and the client was a desktop mail protocol rather than the web browser s2047 normally used. Older mail protocols often skip the second factor, which is one reason attackers prefer them after stealing a password.

### 7.6 DNS as evidence

Campus DNS logs show 41 lookups of the look-alike name from university Wi-Fi, a lower bound on clicks from campus.

It is a lower bound for two reasons noted in the worked results: lookups made off campus are not logged, and a device that looked the name up once may have clicked several times without repeating the query because of caching. Lucas reports the figure with both caveats, so nobody reads it as the total number of clicks. It still shows the campaign reached many devices on campus.

### 7.7 Limits

Network evidence shows connections, not intentions; it needs context from other logs.

A DNS lookup of the fake domain could come from a curious analyst checking the link, not a victim; a sign-in from the Netherlands could be a student on exchange. Lucas pairs each network record with account evidence, such as a rule change or a burst of sent mail, before calling an account compromised. Network data narrows the search; account data confirms it. Each conclusion in his notes names both.

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

The separation meant that when the mail service changed its export format halfway through term, only the reading function needed changing; the analysis and output parts stayed the same. Lucas also added a command-line option for the time window, so analysts could rerun the tool for a different period without editing the code itself.

### 8.2 Dates and times

The datetime module parses timestamps and converts zones. Mixing local and UTC times is the most common bug in SOC scripts.

When sign-in and mail records come from different services, one may record UTC and the other local time, and during British Summer Time the two differ by an hour. A rule that links events within sixty minutes would then match the wrong pairs or none. Lucas converts every timestamp to a timezone-aware datetime in UTC as it is read, so comparisons later in the tool never need to think about zones.

### 8.3 JSON

Cloud services export JSON. The json module reads nested records; Lucas writes small functions to extract the fields he needs.

The mail service's rule export nested the rule's conditions and actions several levels deep, and some rules lacked fields others had. Lucas's extract function returns a default when a field is missing, rather than raising an error, and his tests include a rule with no forwarding address so that case is checked. Fields he does not need are ignored, which keeps the function short and makes later format changes less likely to break it.

### 8.4 Unit tests

unittest checks functions with known inputs: "a rule created 59 minutes after a risky sign-in should match; 61 minutes should not".

Boundary cases like these catch the mistakes most likely to slip through: a comparison written as less-than instead of less-than-or-equal would pass ordinary examples and fail only at exactly sixty minutes. Lucas added a test for that boundary too. When a classmate later refactored the matching function, the tests showed within seconds that the behaviour had not changed. Tests also document intent for the next reader.

### 8.5 Efficiency

Reading files line by line and using dictionaries for lookups keeps memory small and speed high on large exports.

Lucas's first version loaded every sign-in into a list and searched it for each rule, which took minutes on a month's export. Building a dictionary keyed by user once, then looking up each rule's user, cut the run to a few seconds. The change mattered during the incident, when analysts needed to rerun the tool repeatedly as new data arrived during the day.

### 8.6 Errors

The tool logs records it cannot parse and continues; at the end it prints totals read, skipped and matched.

During the phishing incident, the tool reported that a few hundred of several hundred thousand sign-in records were skipped, all with a malformed timestamp from one legacy application. Because the count was printed, Lucas could check that none of the skipped records belonged to s2047 or s3310 before trusting the result. Silent skipping would have hidden that question entirely, along with the faulty application.

### 8.7 Sharing

A README explains inputs, outputs and limits, so other student analysts can run it.

The README lists the expected export files, the command to run, an example of the output and known limits, such as treating unknown time zones as UTC. When a student analyst on the night shift used the tool for the first time during the incident, the README was enough; nobody had to wake Lucas to ask how it worked. The README is updated in the same change as the code.

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

Riverton's SOC loads each day's sign-in export into a database table with those columns plus the client application. During the phishing incident, analysts queried a month of data, several million rows, to find every sign-in by the clicking accounts. The same questions in a spreadsheet would have been slow and error-prone, and harder to repeat exactly.

### 9.2 SQL basics

SELECT chooses columns, WHERE filters rows, GROUP BY aggregates and ORDER BY sorts. A query such as "successful sign-ins outside the usual country, grouped by user" answers an investigation question in one statement.

Lucas's query selected user, time, country and result from the sign-in table, filtered to successful sign-ins where the country was not GB, grouped by user and counted them. Writing the question as a query also documents it: Dr. Kim could read the statement and confirm it asked what she intended before relying on its answer.

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

The pair of records for s3310 matters for the timeline: the failure eleven minutes before the success shows the attacker tried the account more than once. Lucas notes it as consistent with a stolen password, while recognising that it could also mean the attacker mistyped. Either way, the success at 02:31 is when the account was compromised.

### 9.4 Joins

Joining the sign-in table with the mailbox-rule table on user shows which risky sign-ins were followed by rule changes.

The join found that s2047's unusual-country sign-in was followed six minutes later by a rule forwarding mail to an external address. For s3310, the join returned a deletion rule too, but created more than two hours after the risky sign-in. Lucas recorded both, since a join on user alone shows that a rule exists, while the time difference decides whether the two events are likely to be connected. That difference matters again when the correlation rule is built and tested in the first laboratory.

### 9.5 Quality

Missing countries, duplicated rows and inconsistent user formats (s2047 versus S2047) distort results. Normalising at load time prevents errors.

In Riverton's data, the identity provider wrote usernames in lower case while one mail export used capitals. Without normalising, a join would have treated s2047 and S2047 as different users and missed the link between sign-in and rule. Lucas converts usernames to lower case and removes duplicate rows as the data is loaded, and records how many were changed in a load report.

### 9.6 Privacy

Databases with personal data need access control and retention limits. The SOC database keeps sign-in details for 90 days.

Access to the database is limited to SOC staff and the student analysts on shift, and queries are logged. Ninety days covers most investigations, which usually begin within days of an incident. Records needed for an open case, such as s2047's sign-ins, are copied into the case file before deletion, so retention does not destroy evidence still needed for an open case.

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

During the phishing incident, Lucas was assigned the alerts for s2047 and s3310 and searched only their records. When a classmate asked him whether her own account had been affected, he directed her to the SOC's reporting address rather than looking it up himself, since checking an unassigned account would have gone beyond his authority.

### 10.2 Privacy

Students and staff expect privacy. The SOC looks at metadata (sign-ins, rule changes, message counts) by default and reads message content only with case approval from Dr. Kim.

For the phishing case, metadata was enough to confirm both compromises: unusual sign-ins, a new rule and a burst of sent mail. Dr. Kim approved one limited content check, the subjects of the messages s2047's rule had forwarded, to see what the attacker had received. Message bodies were never opened, and the approval was recorded in the case file.

### 10.3 Conflicts of interest

If an alert involves a friend, classmate or lecturer, a student analyst passes it to another analyst. Lucas declares when an alert involves someone in his course.

In week five, an alert involved a lecturer who taught one of Lucas's modules. He declared the connection to the shift lead and the alert went to another analyst. Declaring a conflict is not an admission of wrongdoing; it protects both the person involved and the credibility of the investigation if the case is later reviewed.

### 10.4 Confidentiality

Analysts sign a confidentiality agreement. Discussing cases outside the SOC, even anonymously, is not allowed.

Lucas found this hard during the phishing campaign, when classmates asked what had happened. He could repeat the university's public notice about the email but nothing about which accounts were affected. Even a vague remark, such as "someone in our year got hacked", could identify a person in a small cohort. Lucas found it easiest to say that he could not discuss SOC work at all, which classmates soon accepted. The same rule applies after the case is closed and after he leaves the SOC.

### 10.5 Authorised testing

Phishing simulations and other tests are approved in writing by Dr. Kim and communicated in policy; analysts never run their own tests on university systems.

When Lucas wanted to see how many students would report a mock phishing email, he wrote a proposal rather than sending one. Dr. Kim approved a simulation for the following term with a defined audience, a harmless landing page and a notice in the security policy. Running it without approval could have caused alarm and harmed trust in genuine warnings.

### 10.6 Proportionality

Responses match the risk: resetting a compromised account is proportionate; suspending a student's network access without evidence is not.

For s2047, the evidence of an external forwarding rule and mass sending justified an immediate reset and session revocation. For a student whose only sign was a single sign-in through a foreign mobile gateway, the proportionate step was to check other signals and, if needed, ask the student, not to lock the account while they were away and depending on it.

### 10.7 Reporting misconduct

If an analyst sees misuse of SOC access, they report it to Dr. Kim.

Reports go directly to Dr. Kim rather than through other students, so nobody has to confront a peer. Queries in the SOC database are logged, which allows a report to be checked against the record. Dr. Kim treats reports confidentially and protects the person who made them from retaliation, because the SOC's access is only acceptable if misuse is caught and dealt with promptly and fairly.

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

On Riverton's managed laptops, logging of logons and process creation is enabled by policy; on research servers, settings depend on whoever installed them. That difference matters later in the case, because a server set up with default settings recorded far less than the SOC needed. Knowing what is logged comes before writing any detection that depends on it.

### 11.2 Windows and Linux

University staff laptops run Windows; research servers mostly run Linux. Windows records events in event logs; Linux uses system logs and, where configured, the audit subsystem. Both can forward logs to the SOC.

For the SOC, the two need different parsing. A Windows event has a numeric identifier and structured fields, while a Linux authentication log line is text that must be split carefully. Lucas's tool handles both by converting each record into the same small set of fields, such as time, host, user and action, before analysis.

### 11.3 Users and privileges

Administrators can install software and change settings. Adding a user to an administrators group or to Linux's sudo group is a privilege change worth alerting on.

Such changes are rare and powerful, so they make good alerts: on Riverton's servers, administrator groups change only a few times a year. Each change should match a ticket or a known administrator's action. A change with no matching request, especially at night, suggests that someone has gained access and is securing their foothold.

### 11.4 Research servers

Research groups often run their own servers with local accounts. The research GPU server in the physics department was set up by a postdoc and forwarded no logs to the SOC until this year.

The GPU server held datasets and expensive computing time, which made it attractive to attackers who mine cryptocurrency. Because it forwarded no logs until recently, the SOC had little history to compare against when the alert arrived. The postdoc who set it up had since moved to another group, so nobody owned it day to day.

### 11.5 SSH

Linux servers accept remote logins over SSH. Authentication logs show successes and failures with source addresses. Key-based login without passwords reduces guessing risk.

On the physics server, password login was still enabled for some accounts, and the authentication log showed thousands of failed attempts from internet addresses every day. Most were automated guessing. The SOC's concern was the rare success from an unknown address, which, combined with the sudo alert, became the starting point of the week-five investigation of the GPU server.

### 11.6 Configuration matters

A rule for "new administrator added" works only if the server logs group changes and forwards them.

Forwarding to the SOC had been enabled on the physics server only a few weeks before the alert. Had it been left at its old setting, the sudo change would have stayed in a local file nobody read. Lucas's lesson was that each detection rule needs a check that its source is still logging and forwarding. The SOC now alerts when a server stops sending logs for a day.

### 11.7 Case

In week five, an alert reports a new sudo user on the physics GPU server.

The alert arrived at 23:40 on a weeknight, with no matching change request. Lucas checked the authentication log first, to see who had signed in shortly before the change and from where. That question, rather than the sudo change itself, determines whether the event is an administrator's late-night fix or an intruder's. He also checked who normally administers the server, so he knew whom to ask before taking any action that might disrupt running research jobs.

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

For s2047, a student who sent a few messages a day, 212 in a day was obviously strange; for the library account, 40 was routine. A single threshold across all accounts would either miss the student or constantly flag the library. Comparing each account with its own history removes most of that problem, though not all.

### 12.2 Mean and standard deviation

The mean is the typical value; the standard deviation measures spread. A z-score — (today − mean) ÷ standard deviation — shows how many spreads today's value lies from typical.

Lucas computes both from the previous seven days for each account. For an account that sends between two and three messages a day, the standard deviation is small, so a large jump produces a very high z-score. For an account with wide daily swings, the same jump produces a modest score, which is what we want.

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

The size of s2047's score reflects how steady its history was: with only small daily variation, even a modest rise would score highly, and 212 messages score enormously. The two near-threshold accounts show the opposite case, small rises on accounts whose activity already varies, which is why they are not flagged.

### 12.4 Thresholds

Lucas flags z above 4. With hundreds of thousands of accounts, a threshold of 2 would flag thousands every day; base rates matter, as Axelsson (2000) showed for intrusion detection.

At four, Riverton's daily screening flags a handful of accounts, which two staff and six students can review. Lucas checked that s2047 would have been flagged at any threshold up to two hundred, so the choice did not affect this case. A lower threshold would have buried it among routine variation and tired the analysts.

### 12.5 Limits of z-scores

Seven days is a short history; z-scores assume roughly symmetric variation, which counts rarely have. They are a screening tool, not proof.

New accounts have no history at all, and the start of term changes everyone's behaviour at once. A student who sends coursework to a whole class on one day can produce a high score innocently. Lucas treats a flag as a reason to look at an account, combined with other signs, never as a finding on its own.

### 12.6 Reporting

Lucas reports values with history length and threshold so readers know how the flag was made.

His summary line for s2047 reads: 212 messages today against a seven-day mean of about 2.4, z about 215, threshold 4. A reader can see at once how extreme the value is and how short the history was. Without those details, a flag would be impossible to compare with flags produced by other rules or other analysts. Dr. Kim asked for the same format in every screening report, so trends across weeks could be compared directly.

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

At Riverton, the student records system feeds the identity provider: enrolment creates an account, a change of course updates group memberships, and graduation starts the alumni period. When that feed fails, accounts drift from reality. Lucas's quarterly check compares active accounts with current enrolment and staff lists, and every account matching neither is sent to its owning team for a decision.

### 13.2 Authentication and authorisation

Authentication proves identity; authorisation decides what the identity may access. A compromised student account can access that student's mail, files and learning platform.

That is why a student account matters even though it has no administrative rights. With s2047's password, the attacker could read the student's mail, set up forwarding and send phishing that classmates trusted. Authorisation limited the damage to what one student could reach, but that still included other students' marks sent by email, as the privacy chapter shows.

### 13.3 Multi-factor authentication

MFA requires a second proof. Riverton requires it for staff; for students it is optional. Neither s2047 nor s3310 had enrolled.

Had either student enrolled, the stolen passwords alone would not have been enough at the web sign-in page, since the attacker would also need the second factor from the student's phone. MFA was optional for students because of concerns about support calls and students without smartphones, concerns the university later addressed when it made enrolment compulsory, offering hardware tokens to students without a suitable phone.

### 13.4 Identity signals

New country or device, impossible travel (two distant locations too close in time), legacy protocols that bypass MFA, and MFA method changes are common signals.

In the campaign, s2047 showed two of them at once: a new country and a legacy protocol. The country was new against a history that contained only the United Kingdom. Each signal alone produces false alarms, such as students on holiday, but combinations are much rarer among genuine users and are worth an analyst's time.

### 13.5 Legacy protocols

s2047's attacker used a desktop mail protocol that does not support MFA. Even enrolled users could be exposed while such protocols remain enabled.

These protocols send the password directly and have no way to ask for a second factor, so the identity provider either accepts the password alone or blocks the protocol entirely. That is why disabling them was paired with requiring MFA in the case decision: without the first change, the second could be bypassed by any attacker who chose an older mail client.

### 13.6 Controls

Require MFA for all, disable legacy protocols, and alert on MFA changes and risky sign-ins.

Each control addresses a step in the campaign. MFA stops a stolen password from being enough; disabling legacy protocols removes the route around MFA; alerts on MFA changes catch an attacker who registers their own device; and risky sign-in alerts catch what slips through. Together they make the s2047 sequence much harder to repeat. No single one is enough: MFA without legacy blocking leaves a bypass, and alerts without prevention leave analysts racing an attacker who already has the account.

### 13.7 Case decision

After the campaign, the university decides to require student MFA and disable legacy mail protocols from next term.

Lucas's worked example on legacy protocol use, described below, informed how the change was rolled out, and the service desk prepared guides for setting up MFA on common phones. Announcing the change a full term ahead gave students time to update old mail apps, and kept the cut-over from coinciding with exam weeks, when support calls would be hardest to handle and students least able to wait.

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
- **EX039 — Controls adopted.** What identity controls did Riverton adopt? *Rubric:* 3 = student MFA required, legacy protocols disabled; 2 = one; 1 = vague; 0 = none.

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

For Riverton's SOC, lawfulness and transparency mean the monitoring notice described below; purpose limitation means security logs serve security; minimisation means metadata by default; accuracy means correcting a wrong attribution, such as a sign-in linked to the wrong user; storage limitation means fixed retention periods; and security means the SOC's own systems are protected and access-logged.

### 14.2 Purpose limitation

Logs collected for security may not be reused for unrelated purposes, such as checking attendance. Riverton's monitoring notice states security as the purpose.

Lucas met this in practice when a lecturer asked whether Wi-Fi logs could show which students had attended a lecture. The answer was no: the logs were collected for security under the monitoring notice, and using them for attendance would be a different purpose that students had not been told about. Dr. Kim replied to the lecturer explaining why.

### 14.3 Minimisation

The SOC collects metadata needed for detection, not message content. When content is needed, access is approved per case and limited to what answers the question.

In the phishing case, sign-in records, rule details and message counts were enough to confirm both compromises. Content was needed only to judge what s2047's forward rule had exposed, and even then the approval covered subjects of the forwarded messages, not their bodies. Each step in the case notes shows why a piece of data was needed.

### 14.4 Retention

Sign-in logs are kept 90 days, mail metadata 180 days. Longer retention needs justification.

The periods reflect how investigations work: most compromises are found within days, while some mail-based fraud is noticed weeks later, which is why mail metadata is kept longer. Data needed for an open case is copied into the case file with a note of why it is kept, and the case file has its own review date. When the case closes, the copies are deleted unless the disciplinary process or the DPO needs them, and the reason for any extension is written down.

### 14.5 Individuals' rights

Students can ask what data is held about them. The SOC's records must be retrievable for such requests, with redaction where other people's data appears.

If s2047's owner asked what the SOC held about her, the response would include her sign-in records and the case notes about her account. The forwarded messages' subjects, which mentioned other students' marks, would be redacted, since disclosing them would expose other people's data. Keeping case files organised by account makes such requests answerable within the deadline.

### 14.6 Breach assessment

If personal data was exposed — for example, mail forwarded to an attacker — the data protection officer assesses whether to notify regulators and affected people.

The SOC's role is to supply what the DPO needs to decide: what data was exposed, how many people were affected, whether the attacker could have used it, and when. In the s2047 case, that meant the list of forwarded messages and which ones mentioned other students. The decision to notify belonged to the DPO, who weighed the sensitivity of the marks and the attacker's likely use.

### 14.7 Working with the DPO

The SOC informs the data protection officer early and provides facts, not legal conclusions.

For s2047, Lucas sent the DPO a short note on the morning of the incident: the forwarding rule existed, how many messages had gone out, and that subjects were being reviewed under approval. He did not speculate on whether notification was required. Early contact gave the DPO time to prepare, since some notification deadlines run from discovery. Lucas followed up with each new fact the same day.

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

In the phishing case, Lucas's evidence included the sign-in export, the rule export, a screenshot of the rule's settings, the original phishing message and a short statement from s2047's owner confirming she had entered her password on the fake page. Each item received a reference such as E-3 so case notes could cite it precisely.

### 15.2 Preservation

Exports are saved read-only with a hash (a digital fingerprint). If a file changes, its hash changes. Case notes record who exported what, when and from where.

Lucas computes a SHA-256 hash of each export as soon as it is saved and writes it in the case notes. If anyone later questions whether the sign-in export was edited, recomputing the hash and comparing it with the recorded value answers the question in seconds. Working copies are made for analysis so the original is never opened for editing.

### 15.3 Observation and inference

"Sign-in from 198.51.100.x at 02:14" is an observation. "The account was compromised" is an inference. Case notes keep them separate and show the reasoning.

Keeping them apart lets a reader challenge the reasoning without disputing the facts. If someone suggests s2047's owner was simply travelling, the observations stay the same, a sign-in from a Dutch hosting address and an external forwarding rule six minutes later, and the discussion focuses on whether the inference still holds. Here, the owner's statement settled it.

### 15.4 Measurement

Consistent measures — time to acknowledge, time to contain, number of accounts affected — let the SOC compare incidents and improve. Definitions must be fixed: does "contain" mean password reset or all sessions revoked?

Riverton defines containment as both a password reset and revocation of all sessions, since a reset alone leaves an attacker's existing session working. Under that definition, s2047 was contained at 08:41 and s3310 at 11:20. Recording the definition beside each figure prevents a later report from comparing times measured in different ways.

### 15.5 Units and clocks

All times in UTC; durations in minutes. Mixed units cause errors.

The campaign shows why: delivery at 01:50, the first compromise at 02:14 and containment of s3310 at 11:20 come from different systems, and a report mixing local and UTC times would misstate how long the attacker had access. Writing durations in minutes, such as the gap between sign-in and rule, avoids confusion between hours and minutes. The worked results show the bug this prevents: a comparison of minutes that ignored hours broke matches across an hour boundary. Lucas's tools now parse every timestamp into a full datetime in UTC before doing any arithmetic, and reports state the zone beside each time.

### 15.6 Error and uncertainty

Some measures are uncertain: the number of people who clicked is estimated from DNS lookups and reports. Lucas reports a range and its basis.

For the number of people who clicked, the 41 campus DNS lookups give a lower bound, since off-campus clicks are not logged. Reports and sign-in evidence give other partial views. Lucas's case note states a range with its basis rather than a single figure, and explains that the true number is likely to be higher than any one source suggests.

### 15.7 Case notes

Each step in the campaign response is recorded as it happens, not reconstructed afterwards.

Notes written during the response captured details that would have been lost later, such as the exact time the forward rule was removed and who removed it. When the review chapter builds a timeline of the campaign, it relies on these entries. Reconstructing from memory would have produced plausible but uncertain times that could not be checked against any source. Lucas keeps his notes in the case system, which timestamps each entry automatically.

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

Each zone suits different controls. Student Wi-Fi serves thousands of personal devices the university does not manage, so it is isolated from internal systems. Research networks host specialised servers run by academic groups, often outside central IT. Cloud mail and identity serve everyone and hold the most valuable logs, which is why the phishing case was investigated mainly through them.

### 16.2 Trust boundaries

Boundaries separate zones: student Wi-Fi should not reach administrative servers; research servers should be reachable only by their groups. Firewalls enforce boundaries and log crossings.

Firewall logs at these boundaries help the SOC see attempts to cross them. If a device on student Wi-Fi tried to connect to an administrative server, the log would show a blocked connection from that address. A successful crossing between zones that should not talk is a strong signal, since it means either a misconfiguration or an attacker who has found a way through.

### 16.3 Cloud-first services

Mail and identity live in the cloud, so the most important logs come from cloud providers rather than campus networks. The SOC's architecture must collect cloud logs reliably.

For the phishing campaign, almost every key event, including the sign-ins, the forward rule and the deletion rule, happened in cloud services rather than on campus. If those cloud logs had not been collected, the SOC would have seen only DNS lookups and reports. Lucas checks weekly that cloud log feeds are arriving, since a silent failure would leave the SOC blind.

### 16.4 Monitoring placement

The SOC monitors identity sign-ins (all users), mail events, firewall logs at zone boundaries and endpoint logs from managed devices. Student devices are visible only through services.

This placement means the SOC sees every sign-in and mailbox change wherever it happens, and crossings between campus zones, but not activity inside a student's laptop. In the phishing case, that was enough, because the attack ran entirely through cloud services. A malware infection on a student's own device would be visible only through its effects on university accounts.

### 16.5 Research network

Research servers are diverse and loosely managed. A boundary that limits inbound access to university addresses and requires SSH keys reduces exposure.

The physics GPU server shows the risk: it accepted SSH from the whole internet with passwords enabled for some accounts, and it forwarded no logs until recently. Applying both controls would have removed most of the automated guessing in its logs. Neither control needs new hardware. The worked example below describes how the restriction was agreed with the research group.

### 16.6 Defence in depth

Several layers — mail filtering, MFA, legacy protocol blocking, monitoring of mailbox rules — mean one failure does not lead to widespread compromise.

In the phishing campaign, mail filtering missed the message and only marked it with a banner, but the next layers helped: MFA would have stopped the stolen passwords had the students enrolled, and the z-score screening flagged s2047's burst of sending. Where layers were missing, compromise followed, and s3310's quieter compromise went unflagged for hours. The case decision added MFA and legacy blocking, and later chapters add an alert for suspicious mailbox rules.

### 16.7 Mapping to frameworks

Lucas maps controls to NIST CSF 2.0 functions to show coverage across Protect, Detect and Respond.

His table lists each control with its function: mail filtering and MFA under Protect, the z-score screening and rule alerts under Detect, password resets and rule removal under Respond. The table showed few controls under Recover, which led to a question about restoring deleted mail that appears again in the case's later chapters. A map with an empty column is useful precisely because it points to work nobody had planned.

### Administrative systems

Finance, HR and student records sit in a restricted zone reachable only from staff networks through a gateway that requires MFA. Logs from the gateway show every session, giving the SOC a narrow, high-value view of access to the most sensitive data.

### Worked example

Lucas's architecture review notes that research servers accept SSH from anywhere on the internet. He proposes restricting inbound SSH to the university VPN and campus networks. The physics group agrees after a trial week shows their remote collaborators can use the VPN.

> **Synthetic case.** Networks and reviews are invented.

### Errors and limits

Universities value openness; controls must fit research and teaching needs.

### Exercises

- **EX046 — Cloud logs.** Why are cloud provider logs central to Riverton's SOC? *Rubric:* 3 = mail and identity are in the cloud; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Research boundary.** What change was proposed for research servers? *Rubric:* 3 = restrict inbound SSH to VPN and campus; SSH keys; 2 = partial; 1 = vague; 0 = none.
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

Lucas uses SHA-256 for both purposes. For evidence, the hash recorded at export time proves the file is unchanged. For identification, a hash of a malicious attachment can be searched across mailboxes to find every exact copy. The worked example below shows the limit of the second use: changing a single character produces a completely different hash.

### 17.2 Encryption

Encryption makes data unreadable without a key. TLS encrypts web and mail traffic in transit; disk encryption protects lost laptops.

For the SOC, encryption in transit protects students' passwords on campus Wi-Fi from eavesdroppers, but it also protected the phishing page's traffic, so network sensors could not see what victims typed. Disk encryption on staff laptops means a stolen laptop is a lost device rather than a data breach, which changes how the SOC and the DPO respond to the loss.

### 17.3 Signatures

A digital signature proves who created data and that it has not changed. Email DKIM signatures let receiving servers verify that a message came from the claimed domain.

In the phishing case, the message claimed to come from the library but had no valid DKIM signature for the library's domain, because the attacker did not hold the library's signing key. Receiving servers could therefore tell the message was not genuine. The filter's response, a banner rather than rejection, determined whether students actually saw that warning.

### 17.4 Passwords

Passwords should be stored as slow, salted hashes so that a stolen database cannot be easily reversed.

Riverton's identity provider stores passwords this way, so a breach of its database would not hand over usable passwords quickly. But the phishing campaign shows the limit: the attacker never needed the database, because victims typed their passwords directly into the fake page. Strong storage protects against one kind of attack and does nothing against another, which is why MFA matters as a second barrier.

### 17.5 Monitoring and encryption

Encryption hides content from network sensors. The SOC relies on endpoint and service logs that see data before encryption or after decryption.

For mail and identity, the cloud services decrypt traffic as part of their work, so their logs show sign-ins and rules in full. For student devices, the SOC has no such view. This is why the architecture chapter places most monitoring at services, where data is visible, rather than on campus network links where it is encrypted end to end.

### 17.6 Keys and trust

Cryptography is only as safe as its keys. Compromised signing keys let attackers sign malicious content.

If the library's DKIM signing key had been stolen, the attacker could have sent messages that passed authentication checks, and filters would have treated them as genuine. Riverton keeps signing keys in the mail provider's managed service and rotates them on a schedule. The SOC alerts on any change to the domain's DNS records that publish those keys, since a swapped record would let an attacker's key pass.

### 17.7 Case

The phishing email failed DKIM for the domain it pretended to come from; receiving filters marked it suspicious, but the banner was easy to ignore.

The banner said the sender could not be verified, in small text above the message. Many students who clicked later said they had not noticed it. Lucas recorded a question for the incident review: whether messages failing authentication for Riverton's own domains should be quarantined rather than delivered with a warning. A banner that most readers overlook protects little, however accurate it is.

### Certificates

Websites prove their identity with certificates signed by trusted authorities. The phishing page had a valid certificate for its look-alike name, so the browser padlock showed; a padlock proves encryption, not honesty.

### Worked example

Lucas exports the phishing message and computes its SHA-256 hash for the case record. Later, a second copy reported by staff has a different hash: the attacker added the recipient's name to each message. Lucas notes that hashes identify exact copies, not campaigns; subjects and links group variants.

> **Synthetic case.** Messages and hashes are invented.

### Errors and limits

Cryptography protects data in specific ways; it does not make a system secure by itself.

### Exercises

- **EX049 — Hash uses.** Name two SOC uses of hashes. *Rubric:* 3 = identify files, check evidence integrity; 2 = one; 1 = vague; 0 = none.
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

The question focuses on reasons, which logs cannot show, and on Riverton students, which keeps the study manageable. It avoids assuming students are careless; perhaps they did not know how to report, or assumed someone else would. A good question leaves room for answers the researcher did not expect, and that openness shapes the methods chosen next.

### 18.2 Choosing a method

Surveys reach many people with fixed questions; interviews explore reasons in depth with fewer people; log analysis shows behaviour but not reasons. Lucas combines a short survey with five interviews.

The survey gives a sense of how common each reason is, while the interviews explain reasons the survey's options might miss. Log analysis would add little here, since chapter 1's rates already show the behaviour. Combining methods lets each cover the other's weakness, which the embedded SOC studies cited below also recommend.

### 18.3 Sampling

A survey of volunteers may over-represent security-interested students. Lucas recruits through several channels and reports who responded.

Lucas posts the survey on the student portal, in two faculty newsletters and through a residence-hall mailing list, rather than only on the security society's channel. He reports how many responded from each faculty, so readers can see whether some groups dominate. A sample of mostly computing students would describe them well and the rest of campus poorly. He also compares respondents' year of study with enrolment figures.

### 18.4 Ethics

Research with people needs ethics approval, informed consent, anonymity and the right to withdraw. No SOC data about individuals is used.

Lucas applies to the university's ethics committee with his questions, consent form and data plan. Separating the study from SOC data is important: his position as an analyst gives him access to logs, but using them for research would breach the purpose limitation described in the privacy chapter. Respondents are told he works in the SOC, and that nothing they say will be passed to it.

### 18.5 Designing questions

Neutral wording ("How do you usually handle suspicious emails?") avoids leading answers ("Why don't you report phishing?").

The leading version assumes students do not report and invites them to justify themselves, which may produce defensive or invented reasons. The neutral version lets them describe what they actually do, including reporting. Lucas also avoids technical terms such as DMARC, since students who do not know them may guess or skip the question. Each question asks about one thing only, and the pilot described below tests whether readers understand them as intended.

### 18.6 Analysis

Survey answers are counted; interview transcripts are coded into themes, with a second student coding a sample to check consistency.

For the interviews, Lucas codes themes such as not knowing how to report, assuming IT already knows and fear of looking foolish. A second student codes two of the five transcripts independently, and they compare results. Where they disagree, they discuss and refine the theme definitions, then recode, so the final themes are not just one person's reading of the transcripts.

### 18.7 Literature

Sundaramurthy et al. (2014) show how researchers embedded in SOCs revealed practice that surveys missed, encouraging mixed methods.

Their finding matters for Lucas's design: analysts in those studies described their work differently in surveys than researchers observed in practice. Students may likewise say they would report suspicious mail while their behaviour in the campaign suggested otherwise. Combining interviews with chapter 1's measured rates lets him compare what students say with what they did, which neither source could show alone or settle.

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

At Riverton, "continuously" is limited by staffing: student analysts cover daytime shifts and an engineer is on call overnight. The phishing campaign shows what that means in practice, since the first compromise happened at 02:14 and nobody looked until morning. Understanding the gap between the ideal of continuous operations and the actual rota is part of the theory too.

### 19.2 SOC functions

Knerler, Parker and Zimmerman (2022) group SOC functions into areas such as real-time monitoring and triage, incident analysis and response, threat intelligence, tooling and engineering, and expanded services like hunting.

Riverton's small SOC covers some of these well and others thinly. Monitoring and triage are done by student analysts, incident response by the two staff engineers with the service desk, and tooling by the same engineers in their spare time. Threat intelligence is mostly reading public advisories. Naming the functions shows where a single person is covering several roles.

### 19.3 Incident response framework

NIST SP 800-61r3 places incident response within cybersecurity risk management, aligned to CSF 2.0 functions: preparation sits in Govern, Identify and Protect; detection and response in Detect and Respond; recovery in Recover.

The alignment helps Riverton see that much of incident response happens before an incident. Requiring student MFA, for example, is preparation under Protect, and assigning the DPO's role in breach decisions is part of Govern. Without that preparation, detection and response start from a weaker position, as the phishing campaign showed when neither compromised student had enrolled.

### 19.4 Continuous monitoring

NIST SP 800-137 describes continuous monitoring as an ongoing programme tied to risk.

Tied to risk means monitoring effort follows what matters most: at Riverton, cloud sign-ins and mailbox changes receive the closest watch because the phishing campaign and similar attacks run through them. The programme also checks itself, as the source-health report in the data chapter does, so that a silent gap in collection is noticed rather than assumed away. Lucas's weekly check of cloud feeds is one small piece of that self-checking, and it found two short outages in its first term.

### 19.5 SOC models

SOCs may be internal, outsourced or hybrid. Riverton's is internal and small, using student analysts as a teaching programme.

The teaching programme shapes how the SOC works. Shifts follow the academic timetable, procedures are written for newcomers who change every year, and the two staff engineers spend part of their time training. Outsourcing overnight monitoring was considered after the campaign, but the cost and the loss of local knowledge led Dr. Kim to trial an on-call arrangement instead. The trial is reviewed after one term.

### 19.6 Maturity

The SOC-CMM (van Os, 2016) assesses maturity across business, people, process, technology and services. Riverton scores higher in technology than in process documentation.

The gap showed during the campaign: tools collected the right logs, but there was no written procedure for when to page the on-call engineer overnight. Students who saw early reports were unsure whether to wake anyone. Writing that procedure, with clear thresholds, became one of the first improvements, and the next assessment will show whether the process score rises.

### 19.7 Theory and practice

Vielberth et al. (2020) note that SOC research is fragmented; much practice relies on experience, so the course pairs theory with case work.

For Lucas, this means checking published ideas against Riverton's own data before relying on them. A finding from a large commercial SOC about alert volumes may not hold for a university with seasonal traffic and student analysts. The case work tests theory in a particular setting, and the setting sometimes shows where the theory needs qualifying. Lucas notes such qualifications in his reports.

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

Each case adds something the others lack. The phishing campaign has real timings and decisions from Riverton's own systems. The ransomware exercise covers a kind of attack Riverton has not suffered. The published studies show patterns across many SOCs, which helps Lucas judge whether Riverton's experience is typical or unusual. Using all three guards against generalising from one event.

### 20.2 Riverton's campaign

Detection came first from user reports, then from the z-score flag on s2047. Containment took about six hours for s2047 because the flag ran only in a morning batch.

The batch timing explains most of that delay: the account began sending at about 02:30, but the check that flagged it did not run until 07:00. Earlier user reports pointed to the campaign but not to which account had been compromised. The lesson Lucas draws is that detection speed depends on schedule as much as on rule quality.

### 20.3 Synthetic ransomware exercise

In the course's tabletop exercise, a file server's files are encrypted. Detection comes from users reporting unreadable files; response hinges on isolating the server and restoring from backups. The exercise shows that tested backups decide recovery time.

In the exercise, the team discovered that the most recent backup restore test had been a year earlier, and nobody knew how long a full restore would take. Participants estimated anywhere from four hours to two days. The exercise led to a scheduled restore test, which is cheaper to learn from than a real outage.

### 20.4 Published studies

Alahmadi et al. (2022) describe analysts overwhelmed by benign triggers; Kokulu et al. (2019) describe mismatched SOC priorities between managers and analysts. Both explain why Riverton's student analysts sometimes ignore low-severity alerts.

At Riverton, low-severity alerts such as antivirus quarantines on student laptops are numerous and almost always harmless. Students learn to skim them, which is the overload these studies describe. The risk is that a rare important one is skimmed too, so the triage lab teaches ordering by score and judgement rather than by habit.

### 20.5 Decision points

In each case Lucas lists decision points: when to escalate, when to contain, whom to inform. Delays often come from unclear authority, not missing tools.

In the phishing campaign, the key decision was whether to wake the on-call engineer when early reports arrived overnight. Nobody was sure who could make that call, so nobody did. The improvement was not a new tool but a written rule naming who decides and on what evidence, which the student analysts could follow without hesitation.

### 20.6 Generalising

Lessons that recur — user reports matter, batch detection is slow, unclear authority delays action — are candidates for SOC improvement.

Lucas checks each lesson against the cases before recommending a change. User reports mattered in both the phishing and ransomware cases. Batch detection mattered only in phishing, so the evidence is narrower, but the timings were measured precisely. Unclear authority appeared in both and in the published studies, which makes it the strongest candidate. Lucas ranks the lessons by how much evidence supports each, and presents that ranking to Dr. Kim with the cases listed beside every lesson.

### 20.7 Limits

Cases are selected and simplified; they illustrate, they do not prove.

The ransomware exercise left out the stress of a real outage, angry users and incomplete information; the phishing case was written up after the fact, when the right answers were known. Lucas uses the cases to suggest what to look at, and the measured improvements in later chapters to check whether each change actually helped. A lesson drawn from a case is a hypothesis about Riverton's SOC, and it stays one until the measurements in later chapters confirm or reject it. Lucas marks each lesson in his notes with its status.

### Using cases in training

New student analysts read the case write-ups in their first week, with names removed, and discuss what they would have done at each decision point.

### Worked example

Lucas's comparison table shows that in both the phishing and ransomware cases, the first signal came from people, not tools. He recommends making user reporting faster (a report button in mail) and running the z-score check hourly rather than daily.

> **Synthetic case.** Cases are invented except the cited studies.

### Errors and limits

Synthetic exercises may miss real-world friction.

### Exercises

- **EX058 — Containment delay.** Why did s2047's containment take about six hours? *Rubric:* 3 = z-score check ran in morning batch; 2 = partial; 1 = unknown; 0 = none.
- **EX059 — Recurring lesson.** What lesson recurred across cases? *Rubric:* 3 = first signal from people, not tools; 2 = partial; 1 = vague; 0 = none.
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

Thinking of the SOC this way shifts attention from individual mistakes to the design of the chain. A late alert may not be any analyst's fault; it may come from a log source that arrives slowly, a job that runs once a day or a queue that nobody watches overnight. Each link can be measured and improved.

### 21.2 Tracing an alert

For the s2047 flag: the mail service logged outbound messages; logs arrived in the SIEM within 10 minutes; the z-score job ran at 07:00; the alert entered the case queue; a student analyst picked it up at 08:05; the service desk reset the password at 08:41.

Each step leaves a timestamp in a different system, so the trace was built from the mail service, the SIEM, the case system and the service desk's ticket. Putting them on one timeline showed for the first time how long each step took, which the next part of this chapter uses to find where time was lost.

### 21.3 Delays

The largest delay was the gap between activity (from 02:30) and the batch job (07:00). The second was queue time before an analyst picked up the alert, because the morning shift starts at 08:00.

Neither delay came from slow analysis: once the alert was picked up, the password was reset within about forty minutes. Improving analysts' speed would have saved little; changing when the job runs and who watches the queue overnight would save hours. The model makes that difference visible, which is its main purpose.

### 21.4 Roles

Student analysts triage; Dr. Kim's two staff engineers maintain tools and handle escalations; the service desk performs resets; the data protection officer handles personal data exposure.

Each role holds a different power. Student analysts can examine logs but cannot reset passwords; the service desk can reset but does not investigate. This separation protects against misuse but adds hand-offs, and the phishing case shows that hand-offs are where time is lost if the next person is not expecting the request. Clear roles reduce that risk.

### 21.5 Interfaces

Each hand-off — SIEM to case system, analyst to service desk — has a format and an expected time. Missing expectations cause waits.

After the campaign, Riverton defined the analyst-to-service-desk hand-off: a ticket with the account, the evidence reference and the action requested, with a target of thirty minutes during working hours. Before that, requests arrived by phone or chat with varying detail, and the service desk sometimes had to call back to ask what was needed. The new format removed those calls and made each request traceable in the ticket system.

### 21.6 Using the model

Lucas annotates the model with measured times from the campaign to show where improvements would matter most.

With times attached, the model turns opinions into comparisons. Faster triage had been suggested, but measured triage time was small; the batch gap was large. Lucas's annotations let Dr. Kim choose the changes that would save the most time for the effort, which is the decision described in the worked example below. The same annotated model is reused after each later incident, so the effect of the changes can be measured against the campaign's original times.

### 21.7 Feedback loops

Analyst closure reasons feed back to engineers, who tune rules; without this loop, the same noise repeats.

At Riverton, analysts close each alert with a reason such as benign travel, shared address or confirmed compromise. Engineers review the reasons monthly. When many spray alerts closed as library computers, the engineers added the library's addresses to the shared-address list, and those false alerts stopped appearing in the queue. Without the closure reasons, the engineers would not have known which addresses to add. The loop works only if analysts choose reasons carefully rather than picking the first option.

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

The rule column proved the most useful. It showed that the outbound-mail check depended on mail events alone, and that no rule used the mailbox audit source at all, even though it recorded the forwarding and deletion rules in the campaign. That gap later led to the correlation rule tested in the first laboratory.

### 22.2 Quality

Some sources have gaps: DNS logs miss queries from devices using external resolvers; research servers forward inconsistently. Quality problems limit what detections can promise.

Lucas records each gap beside the detections it affects. A rule that counts lookups of a look-alike domain, for instance, can promise only a lower bound because of the DNS gap. Stating this in the rule's description stops analysts from treating a low count as proof that few people clicked. Research server rules carry a similar note about inconsistent forwarding.

### 22.3 Latency

Cloud mail audit events arrive up to 30 minutes late; sign-ins within 5. Detections that combine them must allow for the slower source.

A rule that looks for a mailbox rule within sixty minutes of a risky sign-in must therefore wait at least thirty minutes after the window closes before deciding nothing happened. Running it too early would miss matches whose audit events had not yet arrived, and an analyst would wrongly conclude the sign-in was harmless. Lucas schedules the correlation to run with this delay built in.

### 22.4 Retention

Cloud audit logs are kept by the provider for 90 days on Riverton's licence; the SOC copies key events to its own store for longer.

The difference matters for slow attacks. A compromise noticed after three months would find the provider's logs already deleted. The SOC therefore copies sign-ins, rule changes and forwarding events to its own store, which follows the retention rules in the privacy chapter, so key evidence survives longer than the licence allows. The copied events are hashed on arrival, like other evidence.

### 22.5 External dependencies

The SOC depends on the cloud provider's logging, the identity provider's API and the university network team. A change in any can break collection silently.

The firewall replacement in the worked example below is one such change. Others include a provider renaming a field in its export, which can make a rule stop matching without any error, or an expired API credential. Lucas's inventory lists who to contact for each dependency and how a failure would show itself. Each entry was confirmed with its owner.

### 22.6 Source health

A daily report shows events received per source compared with the usual range. A sudden drop prompts investigation.

The report compares each source's daily count with the range of the previous four weeks. A drop to zero is obvious, but a fall by half may mean a partial failure, such as one building's controller no longer forwarding. The report goes to the morning shift, which checks any flagged source before relying on it. In its first month, the report caught the firewall gap described below.

### 22.7 Ownership

Each source has a named owner outside the SOC who is told when problems appear.

Owners are outside the SOC because they control the systems that produce the data. When the research firewall stopped forwarding, the SOC could not fix it; the network team could. Naming the owner in the inventory meant Lucas knew whom to contact within minutes rather than asking around the IT department. Owners also receive the monthly source-health summary, so they can see their system's role in detection and plan changes such as replacements with forwarding in mind. That reduced surprises like the firewall gap.

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

Lockout limits explain the difference. Riverton locks an account after several failures in a short period, so brute force against one account soon stops working, while a spray that tries each account only once or twice never triggers a lock. Spraying succeeds when some users choose common passwords, which is why it targets many accounts.

### 23.2 Grouping matters

Grouping failures by source and counting distinct users and attempts per user separates the patterns: spraying shows many users and few attempts each; brute force shows one user and many attempts.

Without grouping, both patterns are just failures in a long list, and the spray's forty failures look much like the day's background of mistyped passwords. Grouping by source address turns them into two clear profiles. The lab below applies exactly this grouping to synthetic records. The grouping is cheap to compute, even on a busy day.

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

Only the first thirty of the spray's forty attempts fall inside the thirty-minute window, which is why the lab reports thirty users rather than forty. The window choice matters: a slower spray spread over hours would show fewer users per window and could fall below the threshold. Lucas notes this limit in the rule's description, so analysts know that a quiet result does not rule out a slow spray.

### 23.4 Responses differ

Spraying threatens many weak passwords; the response is to check whether any targeted account later signed in successfully and to block the source. Brute force against one account may be a user who forgot a password, or a targeted attack; the response is to contact the account holder.

In the lab, the different responses produced different outcomes, as the worked example below shows: the spray was checked for later successful sign-ins and its source blocked, while the brute-force pattern turned out to be a forgotten saved password. Treating both the same way would either alarm s1001's owner needlessly or under-react to the spray.

### 23.5 Thresholds

The lab uses 20 users and 2 attempts per user. Lower thresholds catch slower sprays but raise false alerts from shared campus addresses, such as library computers.

Lucas tested lower values on a week of real failure records. At ten users and two attempts, the rule flagged three library and lab addresses each day, all benign. At twenty, it flagged none of them. He kept twenty for general addresses and documented the trade-off, so slower sprays are a known limit rather than a surprise.

### 23.6 Shared addresses

Campus NAT means many students share one public address; a real spray must be distinguished from a busy lab. The rule excludes known campus egress addresses and handles them with separate thresholds.

For campus egress addresses, the rule uses higher thresholds and also looks at the share of failures, since a busy computer lab produces many successes alongside its failures. A spray from a shared address would show unusually many failures across many users with few successes, a pattern a lab full of students seldom produces.

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

In the campaign, prevention was weak, since filtering only added a banner, and detection was slow, so response had to clean up more than it should have. Strengthening prevention reduces what detection has to catch, and faster detection reduces what response has to undo. The control changes below address all three. Lucas's control table has a column for each.

### 24.2 After the campaign

The campaign response produced four control changes: required student MFA, disabled legacy mail protocols, blocked automatic external forwarding by default, and added a report button in the mail client.

Each change maps to a step in the attack. MFA and legacy blocking address the use of stolen passwords. The forwarding block stops the exfiltration seen in s2047's mailbox. The report button speeds up the first signal, which came from people in both cases studied. Together they target the points where the campaign succeeded.

### 24.3 Side effects

Blocking external forwarding affects staff who forward mail to personal accounts. The university publishes an exception process requiring manager approval and a business reason.

Lucas counted existing forwarding rules before the block was applied: a small number of staff had them, mostly to personal accounts. Each was contacted with instructions for the exception process. Doing this before the change avoided a wave of complaints and missed mail on the day the block took effect. The exception list is reviewed each term.

### 24.4 D3FEND naming

MITRE D3FEND names defensive techniques precisely, such as multi-factor authentication and user behaviour analysis. Naming controls this way helps compare them with other organisations and spot gaps.

Using D3FEND's terms, Lucas's control table names MFA and behaviour analysis precisely, rather than writing vague entries such as "better login security". When Riverton compared notes with another university, both could see that the other monitored mailbox rules but neither had user behaviour analysis for research servers, a shared gap. Precise names made the gap visible.

### 24.5 Control ownership

Each control has an owner: identity team for MFA, mail team for forwarding, SOC for monitoring rules.

Ownership matters when a control fails or causes trouble. When the forwarding block stopped a research mailing list, the mail team owned the fix and used the exception process. Without a named owner, the SOC might have been asked to change a mail setting it did not control, and the fix would have been delayed. Owners also decide on exceptions to their control.

### 24.6 Testing controls

After deployment, the SOC tests each control: a test account tries to create an external forwarding rule; the block works and an alert fires.

Testing showed one gap: the block applied to new rules created in the web interface but, at first, not to rules created through an older mail client. The mail team extended the policy, and the test was repeated through both routes. Deploying a control without such a test would have left the gap open. The test is now repeated after every mail-system update.

### 24.7 Cost and benefit

Lucas estimates time saved: forwarding blocks would have prevented the 37 messages leaving s2047's mailbox.

Those 37 messages included the three containing other students' marks, which led to the DPO's notification decision. Preventing them would have avoided the notification, the work to identify affected students and the worry it caused. Against that, the forwarding block's cost was an exception process and one brief disruption, described below under rollback. Lucas's estimate was rough, but it made the trade-off clear enough for the university to accept the block. He also noted that the block would not have stopped the s3310 deletion rule.

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
- **EX072 — MFA trend caveat.** What caveat did Lucas attach to the MFA results? *Rubric:* 3 = attackers may shift to MFA fatigue prompts; 2 = partial; 1 = vague; 0 = none.

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

Using synthetic alerts lets students practise mistakes safely. A student who closes a real compromise as benign could leave an attacker in an account; in the lab, the same mistake becomes a lesson in the debrief. The lab copy also lets Dr. Kim design alerts that teach specific points, such as ties in the score. No alert in the lab names a real person.

### 25.2 Prioritisation

Not all alerts are equal. A simple score multiplies alert severity (1–3) by asset criticality (1–3); ties are broken by age so older alerts are not forgotten.

Multiplying rather than adding means a high-severity alert on a low-value asset scores the same as a low-severity alert on a critical one, which reflects that both factors matter. Breaking ties by age keeps an alert from waiting indefinitely behind newer ones with the same score, which a queue sorted by score alone would allow.

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

A3 deserves first place: a new administrator on the GPU server could mean an attacker securing access, as in the week-five case. A4 comes last despite being the oldest, because antivirus already quarantined the file and the laptop is personal. The ordering matches what an experienced analyst would choose most of the time.

### 25.4 Triage notes

For each alert, the lab sheet records the decision (benign, suspicious, malicious), evidence checked and next action.

A note for A1 might read: decision suspicious; evidence checked, thirty accounts each targeted once from one external address, no later successful sign-ins; next action, block the source address and close. Recording evidence checked lets a reviewer see that the decision was based on the right questions, not only on the outcome. Notes are written before the next alert is opened, while details are fresh. In the debrief, Dr. Kim compares notes across students to see whether they checked the same evidence.

### 25.5 Errors

In the first run, Lucas spends ten minutes on A4 because it is oldest, delaying A3. Ordering by score first prevents this.

Lucas's mistake was natural, since the oldest item in a queue feels most urgent. In a real shift, ten minutes on a harmless quarantine while a server gained an unexpected administrator could let an intruder settle in. The debrief turned the mistake into a rule in the triage guide: read the score first. Lucas added a line to his own checklist as well.

### 25.6 Reflection

Scores support but do not replace judgement: an analyst who knows the mail rule matches the s2047 pattern may escalate A2 ahead of A1.

In the lab, A2's pattern matched s2047 exactly: an external forwarding rule six minutes after a sign-in from a new country. Escalating it ahead of the equally scored spray was justified because the spray had produced no successful sign-ins, while A2 indicated an account already in an attacker's hands. Dr. Kim's comment on his sheet confirms this reasoning, and the triage guide now notes that pattern matches can override equal scores.

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

In the campaign, s2047's sign-in from the Netherlands alone might have been a student abroad, and its forwarding rule alone might have been a student copying mail to a personal account. The two together, six minutes apart, left little doubt. Correlation lets the SOC alert on that combination without alerting on every trip or every new rule.

### 26.2 Designing the correlation

Lucas's rule: a sign-in flagged as new-country, followed within a time window by mailbox-rule creation for the same user. The window must allow for mail audit delay (up to 30 minutes) and for attacker behaviour.

Lucas writes the rule in plain logic before implementing it: for each new-country sign-in, look for a rule created by the same user within the window; if found, alert with both events. Writing it this way let Dr. Kim check the logic before any code existed, and made the test cases in the laboratory easy to derive.

### 26.3 Choosing the window

Too short a window misses slow attackers; too long a window links unrelated events. Lucas starts with 60 minutes and evaluates it on known cases from the campaign in Laboratory II.

Sixty minutes was chosen because s2047's rule appeared six minutes after sign-in, and Lucas assumed attackers act quickly once inside an account. That assumption is exactly what the laboratory tests. Starting with a stated window and a stated reason makes it easy to see, later, which assumption failed when a case is missed.

### 26.4 Delayed sources

Because mail audit events can arrive late, the rule waits 30 minutes after a risky sign-in before deciding no rule followed.

Without this wait, a sign-in at 02:14 followed by a rule at 02:20 whose audit event arrived at 02:45 could be judged at 02:30 as having no rule, and the alert would never fire. The wait adds half an hour to detection time, a cost Lucas accepts because a missed alert is worse. The rule's documentation records the delay and its reason, so a later engineer does not remove it as an apparent inefficiency and quietly reintroduce missed alerts.

### 26.5 Noise

Students travelling abroad who also tidy their inbox will match. Requiring the rule to forward externally or delete messages by keyword reduces this.

The restriction reflects what attackers in the campaign actually did: s2047's rule forwarded externally and s3310's deleted by keyword. Ordinary students' rules usually move newsletters into folders. Narrowing the rule types removes most benign matches while keeping the behaviour that indicates compromise, as the worked example's test on last month's data shows. Benign forwarding remains possible, but the forwarding block now limits it to approved exceptions.

### 26.6 Rule documentation

The rule records its purpose, logic, window, known benign matches and response steps.

For the correlation, the known benign matches include staff travelling abroad who forward mail to a personal account under an approved exception. The response steps name the service desk ticket to raise and the evidence to export first. A student analyst meeting the alert for the first time at night can follow the documentation without calling anyone. When the window later changed after the laboratory, the documentation was updated in the same change, with the reason and the date, so readers never see a rule that behaves differently from its description.

### 26.7 ATT&CK reference

Mailbox rules used to hide or forward mail relate to email collection and hiding techniques in ATT&CK; referencing them helps coverage tracking.

Lucas tags the correlation with email collection, since forwarding rules collect mail for the attacker, and with the hiding technique for deletion rules like s3310's. These tags feed the coverage count in the verification chapter, where an untested rule under a technique does not count as coverage until it has been shown to fire. Tags also help when comparing with other universities.

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

For the correlation rule, verification means a test account signs in from a test address flagged as a new country, creates a forwarding rule, and the SOC confirms an alert appears with both events. A second test creates an ordinary folder rule after the same sign-in and confirms no alert appears.

### 27.2 Coverage honestly measured

Coverage is the share of priority ATT&CK techniques with a tested detection. A rule that exists but has never been tested is not counted as coverage, because it may silently fail.

Counting untested rules would have hidden the broken email collection rule found in the worked example below: it existed, appeared on the coverage chart and had not matched anything for months, because the field it relied on had been renamed. Honest counting turned a reassuring number into a list of work.

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

The figures describe Riverton's SOC fairly: the techniques seen in the phishing campaign and the ransomware exercise have tested detections, while those involving research servers and DNS have none. The gaps reflect where the SOC's data sources are weakest, as the data chapter showed, rather than where attackers are least likely to go.

### 27.4 Planning

Untested rules are tested first because it is cheap. The two gaps need data sources: remote-service logons on research servers and DNS-based exfiltration detection using resolver logs.

Testing the two untested rules needed only a test account and an afternoon. Filling the gaps needs more: research servers must forward remote-service logons reliably, and DNS exfiltration detection needs resolver logs with enough detail to spot unusually long or frequent queries. Lucas's plan lists the owner and the first step for each.

### 27.5 Test design

Each test states input, expected result and pass criteria. For mailbox rules, a test account creates a forwarding rule after a simulated risky sign-in from a test address.

For the mailbox test, the pass criterion is an alert within the window plus the audit delay, naming the test account and listing the rule. A test that produced an alert without the rule details would fail, since analysts need both events to triage quickly. Stating criteria in advance prevents a partial result from being counted as a pass.

### 27.6 Recording

Results are stored with date, rule version and tester, and repeated each term.

Repeating each term catches silent breakage like the renamed field. Storing the rule version with each result shows which version passed, so if a later change breaks the rule, the last working version can be found. The record also shows the next tester exactly what was done before. For the correlation rule, the first record lists the test account, the sign-in address, the rule created, the alert time and the tester's name. The second, a term later, repeated the same steps after the window change and confirmed the new version still fired.

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

Riverton's review was held a week after the campaign, when containment was complete but memories were still fresh. It included student analysts, the duty engineers, the service desk and the DPO. Its terms stated that the aim was to improve systems, not to assign fault, which shaped how openly people described their decisions that night.

### 28.2 Timeline

The review builds a timeline from email delivery (01:50) to last containment (s3310 at 11:20). Each entry cites its source.

Building it required matching times from the mail service, identity provider, SIEM, case system and service desk tickets, all converted to UTC. Lucas's case notes from the day supplied the analyst actions. Each entry cites its source so that anyone questioning a time can check it against the original export. The finished timeline showed the long quiet stretch between s3310's sign-in at 02:31 and any SOC action, which became the review's central question. A timeline built from memory would have blurred that gap.

### 28.3 What failed

s3310 was compromised at 02:31 but not contained until 11:20. Its attacker created a rule deleting messages containing "phishing" — hiding warnings — but no alert fired, because the correlation window had not yet existed and the z-score did not flag s3310 (it sent few messages).

The gap of almost nine hours for s3310 matters because its deletion rule was removing warnings, including a classmate's question, while the attacker could keep sending mail from the account. Detection had been built around the s2047 pattern of heavy sending, and an attacker who behaved more quietly fell through.

### 28.4 Contributing factors

No MFA for students; legacy protocol enabled; batch detection; no rule for keyword-deletion rules; only one analyst on the early shift.

None of these factors alone explains the outcome. Without MFA, stolen passwords worked; with legacy protocols, MFA could have been bypassed even if enrolled; batch detection delayed s2047's alert; the missing deletion-rule alert left s3310 unseen; and a single early analyst could not handle reports and alerts together. Each factor became an action. Listing them separately also shows which were already fixed.

### 28.5 Blameless approach

The review focuses on systems and decisions, not individuals. People speak openly when they are not blamed.

In the review, the analyst on the early shift explained that she had seen several phishing reports but had not linked them to compromised accounts, because the reports described the email rather than any account. Without blame, that insight was recorded: reports and account alerts lived in different queues, which made the connection hard to see. The action list later added a link between the two queues.

### 28.6 Actions

Each factor becomes an action with owner and date: MFA requirement, legacy shutdown, 15-minute checks, correlation rule, an extra early shift during campaigns.

The extra early shift during campaigns responds directly to the single-analyst factor. The fifteen-minute checks replace the morning batch that delayed s2047's alert. Each action names who will do it and by when, and the review report lists them in a table so their progress can be checked. Owners report progress at the monthly review, and an action whose date passes without completion is raised with Dr. Kim rather than silently extended.

### 28.7 Follow-up

Actions are tracked until closed and checked in the next exercise.

Dr. Kim reviews open actions monthly. The next purple exercise included a slow mailbox-rule attacker similar to s3310, to check that the new keyword-deletion alert fired. It did, and the action was closed with a reference to the exercise report. Actions closed without such a check are reopened. The MFA requirement was followed up differently: Lucas compared risky sign-in alerts before and after, as the controls chapter showed, and the falling count of foreign sign-ins without MFA was recorded as evidence that the action had worked.

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

The staffed hours explain the campaign's timeline: it began at 01:50, outside them, and the first analyst arrived at 08:00. Overnight, only the on-call engineer could act, and only if paged. The trial paging for high scores, described in the system models chapter, is meant to narrow that gap without staffing nights. Student shifts are timed around lectures, so cover is thinnest at the start of the day, when overnight activity is first seen.

### 29.2 Handovers

Each shift ends with a handover note: open alerts, cases in progress, system issues and expected events, such as a planned phishing simulation.

A handover note from the campaign's evening might read: s2047 contained, s3310 under investigation, external forwarding block deployed, campus notice sent, expect more reports overnight. The next shift starts knowing what matters, rather than rediscovering it from the queue. Notes are kept with the case records. A good note is brief enough to read in two minutes and specific enough that nothing important depends on memory. The incoming analyst confirms they have read it before the outgoing one leaves.

### 29.3 Escalation

Student analysts escalate to the duty engineer for anything involving staff accounts, research systems or personal data exposure. Escalation is encouraged; nobody is criticised for escalating in good faith.

The rule is broad on purpose: student analysts are learning, and a missed escalation costs more than an unnecessary one. In the research server case later in the book, the student who saw the night logins escalated at once because it involved a research system, which brought the duty engineer in early.

### 29.4 Queues

The queue is ordered by the scoring from Laboratory I. During campaigns, the duty engineer may assign alerts directly.

Direct assignment during campaigns prevents several analysts from working the same report while others are untouched. In the exam-week campaign, the duty engineer assigned one analyst to reports and one to account alerts, which addressed the review's finding that the two queues had been hard to connect. Scores still guide each analyst within their assigned work. After the campaign, the engineer returns the queue to normal ordering, and the assignments are recorded in the shift log for later review.

### 29.5 Learning

Student analysts follow a training path: shadowing, supervised triage, then independent triage of low-severity alerts.

Each stage has a checklist. Shadowing ends when the student can explain the triage guide; supervised triage ends when a senior analyst agrees with most of their decisions over several shifts. Independent work starts with low-severity alerts and moves to higher ones as confidence grows. Lucas followed this path in his first term. Progress is recorded so the next supervisor knows where each student stands, and students who struggle with a stage repeat it rather than being rushed forward.

### 29.6 Wellbeing

Studies such as Alahmadi et al. (2022) link alert overload to burnout. Shifts are short; analysts rotate between alert types; exam periods have reduced rosters.

Riverton's four-hour shifts limit continuous alert exposure, and rotating between phishing reports and identity alerts reduces monotony. During exams, the reduced roster shifts more work to staff engineers. These choices accept slightly slower triage in exchange for students who stay alert and remain in the programme. Analysts can also ask to step away from a distressing case, such as one involving harassment, without explaining why.

### 29.7 Communication

The SOC sends campus notices during campaigns: what the email looks like, what to do if you clicked, and how to report.

Notices are short and practical. During the exam-week campaign, the notice showed the subject line, said what to do if you had clicked, and linked to the report button. It went out within an hour, and reports then rose sharply, which helped the SOC find compromised accounts more quickly. Notices avoid blame and technical terms, and the SOC sends a short follow-up when the campaign is over, so people know the danger has passed.

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

Known answers make the test meaningful: s2047 and s3310 were both compromised, and s1001 was not. A correct rule must alert on both and stay quiet on s1001. Testing on these cases before deploying shows whether the rule would have helped during the campaign itself. A rule that fails on these known cases would certainly fail on new ones. Passing them is only a first step, since real attackers will vary their timing, which is why the lab also asks what the rule would miss.

### 30.2 Setup

The lab contains synthetic sign-ins and mailbox-rule events for s2047, s3310 and s1001, with times in minutes since midnight.

The times match the campaign: minute 134 is 02:14, when s2047 signed in, and minute 151 is 02:31, s3310's successful sign-in. Using minutes since midnight keeps the lab simple, though the real rule uses full timestamps in UTC, as the time-handling chapters require. The data contain only these three accounts and four events, which is small enough to check every result by hand. Lucas computes the expected output on paper before running the script, so any difference points to a mistake in either the rule or his understanding of it.

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

The s1001 events produce no output because its sign-in was normal and the loop skips it. That silence is correct: the newsletter rule should not alert. The lab therefore shows one true positive, one false negative and one true negative. A false negative on a real compromise is the most important finding.

### 30.4 Analysing the miss

s3310's attacker waited over two hours before hiding warnings, perhaps after seeing replies. Attackers do not follow the defender's assumptions about timing.

Lucas's original window assumed attackers act fast, which s2047's did. s3310's attacker created the deletion rule at minute 300, about 05:00, perhaps after seeing replies questioning the email. The gap shows that a rule built from one case risks matching only that case. Lucas also asked what other timings attackers might use. An attacker who waits a day before acting would escape even a six-hour window, which is one reason the separate keyword rule does not depend on timing at all.

### 30.5 Adjusting

Extending the window to 6 hours catches s3310 but risks linking unrelated events. Lucas adds a second, separate rule: any keyword-deletion rule matching words like "phishing" or "hacked" alerts on its own, regardless of sign-in, because such rules are rare and suspicious in themselves.

The two changes work differently. The longer window still depends on a risky sign-in, so it catches s3310 only because its sign-in was flagged. The keyword rule needs no sign-in at all, so it would also catch an attacker whose sign-in looked normal. Together they cover both timing and the absence of a sign-in signal.

### 30.6 Re-test

With the 6-hour window plus the keyword rule, both compromised accounts alert and s1001's ordinary folder rule does not.

Rerunning the same three accounts confirms the expected outcomes, but the dataset is tiny. Lucas notes that a longer window could match more ordinary rules in real traffic, which is why the monitoring described below follows. A pass on three synthetic accounts is necessary but not sufficient. The next real test is a month of live traffic. Lucas sets a threshold for acceptable false alerts before that month starts, so he cannot decide afterwards that whatever happened was acceptable.

### Monitoring after change

For a month after the change, Lucas reviews every match of both rules each Friday and records whether it was correct. If false alerts exceed two per week, he will revisit the window.

### Worked example

Lucas's lab report: "60-minute correlation missed s3310 (rule after 149 minutes). Changes: window 6 hours; new stand-alone alert for deletion rules containing warning keywords. Re-test: 2 of 2 compromised accounts detected, 0 false alerts on test data. Limit: test data is small; monitor false alerts for one month."

> **Synthetic case.** Events come from the lab script.

### Errors and limits

Known cases test only what happened before; new attacker timings may still be missed.

### Exercises

- **EX088 — Lab outcome.** Which account was detected and which missed, and why? *Rubric:* 3 = s2047 detected (6 min); s3310 missed (149 min outside 60); 2 = partial; 1 = wrong; 0 = none.
- **EX089 — Two fixes.** What two changes were made? *Rubric:* 3 = 6-hour window; stand-alone keyword-deletion rule; 2 = one; 1 = vague; 0 = none.
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

Unlike the phishing campaign, nothing here is clearly malicious on its own: collaborators do log in, sometimes late, and research groups do move data. The difficulty is deciding whether the same activity is legitimate this time. The case tests the skills from earlier chapters under real uncertainty.

### 31.2 Competing explanations

Possibilities: the collaborator is working late on a big dataset; the collaborator's account at the partner university was compromised; or someone in the group shared credentials. Each predicts different evidence.

Late work predicts the collaborator will confirm the activity; a compromised partner account predicts an unusual sign-in at the partner university; shared credentials predict logins from a Riverton group member's usual location. Listing predictions first tells Lucas what to look for, rather than gathering everything and hoping a pattern emerges.

### 31.3 Gathering evidence

Lucas checks: login times compared with the collaborator's usual pattern; files transferred (names and sizes from server logs); whether the partner university's SOC sees anything unusual. Contacting the partner goes through Dr. Kim.

Going through Dr. Kim matters because contacting another university's SOC involves sharing information about a person and a research project. She knows the partner's contacts and can agree what may be shared. Lucas prepares the questions and the evidence, but the formal request comes from her. File names alone answer much.

### 31.4 Findings

The partner SOC reports that the collaborator's account signed in from an unusual country that night, and the collaborator confirms they were not working. The transfers were of a shared dataset, not personal data.

The evidence fits the second explanation and rules out the first: the collaborator was not working, and their partner account showed an unusual country. Nothing suggested shared credentials. Lucas records which predictions were confirmed and which were not, so the conclusion can be traced back to the evidence.

### 31.5 Coordinated response

The research group disables the collaborator's server access; the partner resets the account; Riverton reviews which data left and informs the data owner.

Each organisation acts on what it controls. Riverton cannot reset the partner account, and the partner cannot disable access to Riverton's server. Clear division of tasks, agreed on a call between the two SOCs, avoided duplicated work and gaps. Informing the data owner let them judge whether the shared dataset's release mattered. Both SOCs kept notes of the call.

### 31.6 Uncertainty

Some questions stay open: whether the attacker targeted the research or simply used any access found. The report states this.

Lucas's report states that the evidence cannot distinguish a targeted attack on the research from opportunistic use of any access found. It explains what would help: logs from the partner showing the attacker's other activity. Stating the unknown prevents readers from assuming either answer. The report also notes that the partner's logs may never be shared in full, since they concern the partner's own users and systems. Lucas's recommendation therefore does not depend on resolving that question.

### 31.7 Lessons

Research collaborations need shared contacts between SOCs and a way to verify unusual access quickly.

Before this case, nobody at Riverton knew whom to call at the partner's SOC. The lessons led to a list of contacts for each university with research collaborations, and an agreement that unusual access by a collaborator can be checked with a phone call rather than a formal letter. The termly review of external collaborators with server access, recommended in the worked example, makes it easier to answer the first question in any future case quickly: should this person have access at all, and who at their home institution vouches for them?

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
- **EX093 — Collaboration lesson.** What lesson concerns research collaborations? *Rubric:* 3 = shared SOC contacts; verify unusual access quickly; list external collaborators; 2 = partial; 1 = vague; 0 = none.

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

The s2047 case alone involved the DPO for the exposed marks; the research server case involved a professor and a data owner. Each office asks different questions: the DPO asks what personal data left, the professor asks whether participants are affected. The SOC must answer each in the right terms. Lucas notes each office's questions.

### 32.2 Legal and privacy

The data protection officer decides on breach notifications; the SOC supplies facts. Legal staff advise when evidence may be needed in proceedings.

In the s2047 case, Lucas supplied the list of forwarded messages and their subjects; the DPO decided that three students must be informed. Legal staff would have been involved if the evidence had been needed for disciplinary proceedings, which would have required the chain-of-custody record from the evidence chapter. Lucas never offers an opinion on whether notification is legally required, even when asked informally. Doing so could mislead people who later rely on the DPO's actual decision.

### 32.3 HR and student affairs

If an incident suggests misconduct by staff or students, the SOC passes facts to HR or student affairs and does not investigate the person beyond the security question.

The limit protects people's rights. If logs suggested a student had shared their password with a friend, the SOC's question would be whether the account is secure; whether the student broke rules is for student affairs. The SOC reports facts and stops there. In such a referral, Lucas's note states only what the logs show and when, without conclusions about intent. Student affairs may ask further questions through Dr. Kim, never directly to an analyst.

### 32.4 Communications

Public statements are written by the communications office with SOC facts; analysts do not speak to journalists.

During the exam-week campaign, the communications office published the campus notice using facts from the SOC: the subject line, what to do and how to report. When a student newspaper asked about the campaign, the query went to the communications office, which answered without naming any affected account. Lucas forwarded the newspaper's query without replying, as the procedure requires. Analysts who speak informally to reporters may reveal details that identify victims or tell attackers what the SOC knows, so even friendly questions are passed on.

### 32.5 Academics

Researchers value openness; security requirements must be explained in terms of protecting their work and participants.

For the physics group, restricting SSH was presented as protecting their GPU time and datasets from misuse, not as a rule from central IT. The trial week, during which remote collaborators used the VPN, showed the change would not stop their work, which made agreement easy. Lucas also met the group's postdocs, who ran most of the jobs, to explain the change in person. Their questions about connecting from conferences abroad led to clear VPN instructions being added to the group's wiki before the restriction took effect.

### 32.6 Translating

Lucas practises explaining "risky sign-in followed by forwarding rule" as "someone else logged in as the student and set the mailbox to copy their mail elsewhere".

The plain version avoids "sign-in", "forwarding rule" and "compromise" without losing accuracy. Lucas tests it on a friend outside computing. If she can repeat the meaning, the translation works. He keeps a short glossary of such translations for common alert types. Translation also works in reverse: when the professor asked whether "the data got out", Lucas confirmed which data, to where and when, before answering, so his reply addressed the real question.

### 32.7 Joint procedures

A shared procedure lists who is informed for each incident type, within what time and through which channel.

For a personal data exposure, Riverton's procedure says the SOC informs the DPO within four hours by phone and follows up in writing. For a research system incident, the group's head and the data owner are told the same day. Agreeing these in advance removes guesswork during an incident. The procedure is reviewed at the termly meetings with partner offices, and changes are dated. During an incident, nobody has to remember who should be called; they read the table and act.

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

The responses came through the several channels planned in chapter 18, and Lucas recorded which faculty each respondent studied in. Five interviews are few, but they were meant to explain reasons rather than measure how common they are, which the survey does. Each interview lasted about twenty minutes and was transcribed with identifying details removed. Interviewees were recruited from survey respondents who left an address for follow-up, chosen from different faculties so that the five conversations would not all reflect one department's habits or one course's teaching about phishing.

### 33.2 Quantitative analysis

61% of respondents said they would delete a suspicious email without reporting; 24% would report; 15% were unsure. With 412 responses, the margin of error is roughly ±5 percentage points, assuming responses are representative.

The margin applies to each percentage separately and assumes a random sample, which a volunteer survey is not. Lucas therefore presents it as a rough guide to precision, not a guarantee. The three answers add to 100%, which confirms that every respondent chose exactly one option and none were lost in coding.

### 33.3 Qualitative coding

Interview transcripts are coded into themes: "didn't know how to report" (four of five), "thought IT already knew" (three), "worried about looking foolish" (two). A second student codes two transcripts independently; they agree on most codes and discuss differences.

Counts such as four of five show how often a theme came up among interviewees, not how common it is among all students; the survey does that job. Where the two coders disagreed, it was usually about whether "I wasn't sure who to tell" meant not knowing how to report, and they settled on including it.

### 33.4 Validity

Volunteers may be more security-aware than average, so true reporting may be even lower. Self-reported intentions may differ from actual behaviour; log data on actual reports helps triangulate.

Lucas compares the survey's faculty mix with enrolment: computing students were over-represented, which supports the concern that respondents were more aware than average. Rather than weighting the results, which needs assumptions he cannot check, he reports the imbalance and the direction in which it probably pushes the findings. Self-report is the second concern, and the log comparison below addresses it as far as the data allow.

### 33.5 Reliability

Clear code definitions and double coding make qualitative results more reliable.

Lucas's codebook defines each theme with an example quote and a counter-example, so the second coder knew what to exclude. After their discussion, they rewrote one definition and recoded the two shared transcripts, reaching agreement on all codes. A reader can repeat the coding using the codebook in the appendix. Reliability is not the same as validity: two coders can agree consistently on a theme that does not reflect what interviewees meant. Lucas guarded against that by checking each theme against the full transcripts, not only the coded extracts.

### 33.6 Triangulation

Actual reporting rates from chapter 1 (3.0 per 1,000 students) are consistent with low reporting intentions.

The two sources measure different things, intentions and actual behaviour, and both point the same way. Neither alone would be convincing: intentions may not match action, and the reporting rate does not explain why. Together, they support the conclusion that low reporting reflects not knowing how, which the interviews suggested. Lucas is careful not to overstate the match. The survey asked about intentions in general, while the reporting rate comes from one campaign, so the comparison shows consistency rather than proof of cause.

### 33.7 Reporting

The report gives numbers with uncertainty, quotes that illustrate themes, and limits.

Lucas's report presents each percentage with its margin, gives one anonymised quote per theme and lists limits first in a short paragraph rather than burying them at the end. Readers in the SOC wanted to know whether to trust the numbers before reading them, so putting limits early helped them judge. The appendix holds the full questionnaire and codebook. Lucas also gives the number of respondents who skipped each question, since skipped answers can change percentages and readers deserve to see how many responses each figure rests on.

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
- **EX099 — Validity threat.** Name one validity threat and its likely direction. *Rubric:* 3 = volunteers more aware → true reporting even lower; or intentions ≠ behaviour; 2 = partial; 1 = vague; 0 = none.

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

Each of the three models is common among universities, which made the comparison useful to others. The team chose phishing reports because all three SOCs handle them and because Riverton's campaign gave them a detailed understanding of what good handling should achieve. Contacts at the other two came through Dr. Kim.

### 34.2 Criteria

They compare time from report to acknowledgement, whether reporters get feedback, automation of mailbox searches, and staffing model, using the same definitions for each.

Agreeing definitions mattered: one SOC counted acknowledgement as an automatic reply, another as a person reading the report. The team chose a person's first action, and each SOC recalculated its figure on that basis. Without the shared definition, the fastest SOC might simply have been the one with an automatic reply. Feedback was defined as a personal reply telling the reporter what happened, so an automatic acknowledgement did not count. Automation was judged by whether a reported message could be searched and removed from all mailboxes without manual steps.

### 34.3 Evidence

Each SOC shares anonymised figures for one term and a description of its process. No personal data is exchanged.

Each SOC provided counts and medians rather than individual reports, so no reporter or recipient could be identified. Process descriptions were checked against a short questionnaire the team wrote, which asked the same questions of each SOC in the same order. That kept answers comparable. The team also asked each SOC to describe one recent phishing report from start to finish, which brought the process descriptions to life and revealed steps the questionnaire had missed, such as manual approval before a purge at the regional SOC.

### 34.4 Findings

The managed provider acknowledges fastest (median 6 minutes) but rarely gives reporters feedback; Riverton is slower (median 22 minutes in staffed hours) but replies to every reporter; the regional SOC automates mailbox purges best.

Riverton's slower median reflects staffed hours: reports that arrive overnight wait until the morning, while the managed provider staffs nights. The regional SOC's purges remove reported phishing from every mailbox within minutes, which Riverton did by hand during the campaign. Each strength has a cost the team recorded alongside it.

### 34.5 Balanced conclusions

No model is best on all criteria. Feedback to reporters, which Riverton does well, encourages reporting; speed and automation, which others do well, reduce exposure.

The interviews in Lucas's study connect these: students said they did not know how to report or assumed IT already knew. Personal feedback addresses both by teaching reporters that reports matter. Speed and purges limit how many people click. Both matter, so a balanced conclusion recommends keeping one and adding the other. The team avoided ranking the three overall.

### 34.6 Fairness

Differences in size and threat exposure limit comparison; the project states these.

The managed provider serves a university twice Riverton's size, and the regional SOC serves several institutions, so their volumes and staff differ. The team reported medians and percentages rather than raw counts, and stated the differences in size beside each figure so readers could judge comparability themselves. Threat exposure also differs: the regional SOC's members include a medical school that receives targeted phishing more often. The team could not adjust for that, so they described it and advised readers to compare processes more than raw speeds.

### 34.7 Recommendations

Riverton adopts automated purges of reported phishing from all mailboxes, with feedback kept.

Riverton tested automated purges on a simulated phishing message in a test mailbox group before enabling them. The change keeps the personal reply to each reporter, which the team found was Riverton's distinctive strength. The purge removes copies that recipients have not yet opened, reducing exposure in the next campaign. Feedback to reporters remains a person's reply, written by the analyst who handled the report. The team also suggested that Riverton ask the managed provider's university how it handles feedback at night, since that was the one gap all three shared.

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
- **EX102 — Adopted change.** What did Riverton adopt from the comparison? *Rubric:* 3 = automated purges, keeping feedback; 2 = partial; 1 = vague; 0 = none.

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

The choice follows the evidence: the review showed s3310 went undetected for nearly nine hours, and coverage work found gaps in mail-related detection. Measuring against authorised scenarios means the project can show improvement without waiting for a real attack, and without touching real students' accounts. The need was confirmed with Dr. Kim, who agreed it was the SOC's top detection priority for the coming year. A capstone that matches a real priority is more likely to be used once the student has graduated.

### 35.2 Aims

Aim 1: combine the correlation and keyword-deletion rules into a tested detection package. Aim 2: add detection of mass internal mailing by newly risky accounts. Aim 3: measure detection rate before and after on a set of 20 authorised test scenarios.

Aim 2 addresses the behaviour that made s2047 dangerous: sending phishing to contacts from a trusted address. Aim 3 provides the evidence for the other two. Each aim can be judged separately, so a partial success, such as a good package with a weak new rule, would still be clear in the evaluation.

### 35.3 Requirements

Detect at least 80% of test scenarios; no more than three false alerts per week in production; alerts within 30 minutes of the triggering activity.

Each requirement has a reason. Eighty percent reflects that no rule set catches everything; three false alerts a week is what six student analysts can absorb without ignoring alerts; thirty minutes would have saved s2047 hours of sending. Stating reasons lets the evaluation discuss a near miss intelligently. Each requirement can be checked with a number at the end of the project, which is what makes it a requirement rather than a hope.

### 35.4 Test scenarios

Twenty scenarios are designed with Dr. Kim: each uses university test accounts and benign actions, such as a test sign-in from a test address and creation of a forwarding rule to a test mailbox. No real accounts are touched.

The scenarios vary in timing, rule type and sending volume. Dr. Kim's involvement ensures they are realistic and authorised; test accounts are clearly labelled so analysts and the service desk do not respond to them as real incidents. Each scenario is written down in advance with its expected detection.

### 35.5 Ethics and data

The project uses SOC data under existing policy; personal data is not taken off university systems; the report uses aggregates only.

Because Lucas is both an analyst and a researcher, the proposal states that capstone analysis uses only data the SOC already holds for security, under the same access rules. The university's ethics office confirmed that no further approval was needed since no new data about people is collected. Lucas's dual role is stated in the proposal so that the supervisor can watch for conflicts, for instance if Lucas were tempted to look at accounts beyond the scenarios to improve his results.

### 35.6 Risks

Test scenarios may not resemble real attacks; mitigated by basing them on the campaign's actual behaviours. False alerts may disturb analysts; mitigated by monitor-only mode first.

Other risks include delays in change approval and Lucas's exam period. The timeline below leaves weeks for analysis and report writing, so a delay in deployment would shorten the margin rather than the evaluation. Each risk names who watches for it. A risk register at the end of the proposal lists each risk, its likelihood, its effect on the project and the mitigation. Lucas reviews it at each fortnightly supervision meeting and records any changes.

### 35.7 Approval

Dr. Kim and Lucas's academic supervisor sign the proposal.

The two signatures cover different concerns. Dr. Kim approves the operational work, including tests in production and rule changes. The academic supervisor approves the project as assessed work, including the evaluation plan. Both receive later changes through the shared log described under supervision. Signing both before work begins also protects Lucas: if anyone later questions why test accounts were signing in from unusual addresses or creating forwarding rules, the signed proposal shows the activity was planned and authorised. Copies are stored with the capstone log and in the SOC's change records.

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
- **EX104 — Test safety.** How are test scenarios kept safe? *Rubric:* 3 = university test accounts, benign actions, no real accounts; 2 = partial; 1 = vague; 0 = none.
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

Eastbank's situation is common among small charities: cloud services set up by a volunteer years ago, shared passwords and no one whose job includes security. Four weeks is short, so Lucas agreed with the manager on three goals at the start: stronger sign-in, alerts that someone reads and staff who know what to do.

### 36.2 Understanding the setting

The charity cannot run a SOC. Its risks are similar to Riverton's on a small scale: phishing, account compromise and lost devices.

Lucas spent his first days asking staff how they work: who uses which devices, who has administrator rights and how they share files. Several staff used personal phones for mail. That shaped his advice, since rules requiring managed devices would be impossible for a charity with no IT budget. He also learned that the manager shared her administrator password with a volunteer, which became the first thing they changed together.

### 36.3 Practical improvements

With the manager's permission, Lucas helps enable MFA for all staff, turns on the mail service's built-in alerts for suspicious sign-ins and forwarding rules, and sets alerts to go to two named staff members.

These three changes reuse what the mail service already offers, so they cost nothing and need no ongoing technical work. Two named staff receive alerts so one absence does not leave them unread. Lucas tested each alert with the manager's own account before leaving, so they knew what a real one looked like.

### 36.4 Teaching

He runs a 30-minute session on recognising phishing and how to report it, using examples adapted from Riverton's campaign with all identifying details removed.

Adapting Riverton's campaign gave staff a realistic example: an urgent-sounding message, a look-alike link and a fake sign-in page. Lucas explained what to look for and, more importantly, that reporting quickly matters more than never clicking. Staff practised forwarding a sample email to the reporting address. Staff asked practical questions, such as what to do if they were unsure, and Lucas's answer was always to report and let someone else decide.

### 36.5 Simple procedures

A one-page "what to do if" sheet covers clicked links, lost phones and strange emails, with contact numbers.

The sheet is written in plain language and pinned in the office as well as shared by email. For a clicked link, it says to change the password, tell the manager and check for strange forwarding rules, with screenshots showing where to look. Lucas tested the sheet by asking a staff member to follow it. The staff member found one step confusing, which Lucas rewrote.

### 36.6 Boundaries

Lucas does not access staff mailboxes or personal data; he configures settings with the manager present and leaves documentation.

Working with the manager present means every change is understood by someone who stays. Lucas's documentation lists each setting changed and how to reverse it. He did not keep any administrator access after the placement, which the manager confirmed by removing his temporary account. When a staff member asked him to look into a strange email in her inbox, he talked her through checking it herself rather than opening her mailbox. That kept him within the agreed limits and left her more confident.

### 36.7 Reflection

Advice must fit the organisation's capacity; a perfect plan the charity cannot maintain is worse than a simple one it can.

Lucas initially drafted a ten-page security plan, then realised nobody at Eastbank would read or maintain it. The final version, three settings and one sheet, was used within two weeks. Matching advice to capacity is a skill that applies equally inside larger organisations. He also notes that the charity's staff taught him things about their work that changed his advice, such as the need to email families from personal phones during evening activities. Listening first made his recommendations usable.

### Handing over

Before leaving, Lucas walks the two named staff through the alert emails and the one-page sheet, and arranges a check-in call a month later.

### Worked example

Two weeks after the session, a staff member reports a suspicious email using the new sheet; the built-in alert also fires for a forwarding rule created on her account after she entered her password. The manager follows the sheet: resets the password and removes the rule. No data left the account.

> **Synthetic case.** The charity and events are invented.

### Errors and limits

Community help is limited by time; leave documentation and contacts so improvements last.

### Exercises

- **EX106 — Built-in alerts.** Which built-in alerts were enabled? *Rubric:* 3 = suspicious sign-ins and forwarding rules; 2 = one; 1 = vague; 0 = none.
- **EX107 — Boundaries.** What boundaries did Lucas keep? *Rubric:* 3 = no mailbox or personal data access; configure with manager present; documentation; 2 = partial; 1 = vague; 0 = none.
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

Students present to classmates, Dr. Kim and an academic supervisor. Questions focus on whether claims match evidence, not on how much work was done. Presenting before the final evaluation means criticism can still change the project, which is more useful than receiving it in the final examination. Each presenter receives written comments from two assigned peers in addition to spoken questions, so quieter classmates contribute too and the presenter has a record to work from afterwards.

### 37.2 Lucas's evidence

He shows before-scenario results (11 of 20 detected), monitor-only false alerts (four in two weeks) and the design of the mass-mailing detection.

The before result shows that existing rules caught just over half the scenarios. Four false alerts in two weeks is a rate of two a week, under the three-per-week requirement, but over a short period. The mass-mailing design was presented as a plan, since it had not yet been built. He presented each figure with its source in the project log, so peers could see which numbers were measured and which were still plans.

### 37.3 Peer critique

A classmate asks whether the 20 scenarios include slow attackers like s3310. Another asks whether four false alerts in two weeks meets the "three per week" requirement or whether two weeks is too short to judge.

Both questions were fair. The scenarios had been based mainly on s2047's fast behaviour, so slow attackers were under-represented. Two weeks of monitor-only data gives only a rough sense of the false-alert rate. Lucas had not considered either point carefully until classmates raised them.

### 37.4 Weak inferences

Dr. Kim notes Lucas's slide says "the package will detect most compromises"; the evidence supports only "detects most test scenarios".

The difference matters because test scenarios are designed by defenders and may be easier than real attacks. Claiming the package will detect most compromises would invite readers to rely on it more than the evidence warrants. Precise wording protects both the reader and the project's credibility. Lucas rewrote the slide during the seminar break, and Dr. Kim asked him to apply the same check to every claim in his draft report before submitting it.

### 37.5 Missing data

Lucas has not yet recorded how long each detection took; the 30-minute requirement cannot be assessed.

Detection time had been in the requirements from the start but was not being captured, because the test harness recorded only whether each scenario alerted. Lucas changed the harness to log the time of the triggering action and the alert, so the before and after runs would both have times. He also realised that the before run had to be repeated to collect times, since comparing times from only the after run would have nothing to compare against.

### 37.6 Responding

Lucas adds two slow-attacker scenarios (replacing two duplicates), starts recording detection times, and changes the wording.

Replacing duplicates rather than adding scenarios kept the total at twenty, so the before and after runs remain comparable. The before run was repeated with the new scenarios to keep the comparison fair. Each change was recorded in the project log with the seminar as its source. The wording change was applied across his draft report as well as the slides. He sent a short note to both classmates thanking them and listing what had changed, which also documented the response for his supervisor.

### 37.7 Critiquing others

He questions a classmate's claim that a new dashboard "reduced workload" when the only evidence was analysts' impressions; he suggests counting alerts handled per shift.

Lucas framed his comment as a suggestion with a method attached, not as a dismissal. The classmate agreed that impressions might reflect novelty rather than real change, and added a count of alerts handled per shift before and after the dashboard. Good critique gives the presenter something to do. Lucas also noted something the classmate had done well: the dashboard's design was based on interviews with analysts.

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

- **EX109 — Peer questions.** What two peer questions challenged Lucas's evidence? *Rubric:* 3 = slow attackers in scenarios; two weeks too short for false-alert rate; 2 = one; 1 = vague; 0 = none.
- **EX110 — Weak claim.** What overclaim did Dr. Kim identify? *Rubric:* 3 = "will detect most compromises" vs "detects most test scenarios"; 2 = partial; 1 = vague; 0 = none.
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

The mass-mailing rule's threshold of fifty new recipients comes from the campaign: s2047 mailed far more than that, while ordinary students rarely mail more than a handful of new people in a day. Restricting it to accounts with a recent risky sign-in keeps it focused on likely compromise rather than busy organisers.

### 38.2 Tests

Each rule has unit tests in the SOC's test harness and a set of synthetic events. Tests run before each change.

Unit tests check each rule's logic with small inputs, including boundary cases such as exactly fifty recipients. The synthetic events replay realistic sequences, such as s3310's slow deletion rule. Running both before each change catches mistakes before they reach the monitor-only stage. The harness reports pass or fail for each test and stops a change from being submitted if any fails. Lucas added tests for the two slow-attacker scenarios as soon as they were written, so they were checked throughout development.

### 38.3 Change control

Lucas submits each rule through the SOC's change process with a description, test results and rollback steps. Dr. Kim approves.

Rollback steps state how to disable each rule quickly if it floods analysts. Dr. Kim's approval confirms that the tests passed and the change fits the SOC's capacity. The change record also links to the capstone log, so assessors can see the operational approval for each part of the project. The process added a day or two to each change, which Lucas planned for in his timeline.

### 38.4 Staged deployment

Rules run in monitor-only mode for two weeks, recording matches without alerting analysts. Lucas reviews every match.

Monitor-only mode shows how rules behave on real traffic without adding work for analysts. Lucas reviewed each match against the account's activity to decide whether it was a true or false alert. The review let him adjust rules before they affected anyone, as the next finding shows. He recorded his decision for every match in a table with the account, the rule, the reason for the match and whether it was a true or false alert. The table became part of the dossier and later fed the false-alert evaluation.

### 38.5 Monitor-only findings

The mass-mailing rule matches a student society officer who emailed new members after signing in from abroad on holiday. Lucas adds a check: alert only if the messages share a subject with messages already reported as phishing, or if links point to domains first seen that week.

The added check uses signals specific to phishing: a subject already reported, or links to newly seen domains. The society officer's message had neither, so the revised rule stayed quiet. Lucas reran the synthetic tests after the change to confirm that the campaign-like scenarios still alerted.

### 38.6 Going live

After a clean second week, the package moves to alerting for analysts.

A clean week means no false alerts from the revised rules. Lucas told the student analysts about the new alerts before they appeared, with a short guide to each. Going live on a Monday, rather than before a weekend, ensured the staffed SOC could react to any early problems. Lucas stayed available during the first live week to answer analysts' questions, and recorded each question as a possible improvement to the alert text or the rule documentation.

### 38.7 Evidence

Commits, test outputs, change tickets and monitor-only reviews are filed for the capstone dossier.

Filing as he went meant the dossier was complete when the evaluation began. Each item is named by date and rule, and the dossier index links each requirement to the evidence for it. An assessor can follow any claim back to commits and tests without asking Lucas. Lucas also kept a short diary of decisions and their reasons. When writing the thesis months later, the diary explained choices that the commits alone did not, such as why the recipient threshold was set where it was.

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
- **EX114 — Live result.** What happened in the first live week? *Rubric:* 3 = one alert; 120 messages, new domain; contained in 25 min; 2 = partial; 1 = vague; 0 = none.

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

Running the same twenty scenarios twice, before and after, means differences come from the rules, not the scenarios. The scenarios include the two slow attackers added after the seminar. Detection time is measured from the triggering action to the alert, as the requirement states, using the harness timestamps added earlier. Lucas ran both sets on the same day with the same test accounts.

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

The slight overlap means the evidence for improvement is good but not overwhelming. With twenty scenarios, each one moves the rate by five points. Lucas states the improvement as seven more scenarios detected, which is concrete, and leaves the intervals to show how precise the rates are. He also reports which individual scenarios changed from missed to detected.

### 39.3 Misses

The two missed scenarios used a forwarding rule to an internal account that then forwarded externally — a pattern none of the rules covered. They become future work.

The pattern is a two-step chain: the attacker forwards to an internal account it also controls, which then forwards outside. No single rule sees an external forward from the compromised account. Lucas describes how a future rule could follow such chains through the mailbox audit log. He does not adjust the package to catch them before the evaluation ends, since that would mean tuning to the test.

### 39.4 Detection times

Median detection time was 14 minutes; the slowest was 27 minutes, within the 30-minute requirement.

Times came from the harness, so they are exact for test scenarios. The slowest included the deliberate wait for delayed mail audit events. Live times may differ, since real activity arrives with variable delays, which the single live detection in twenty-five minutes illustrates. Lucas reports the full list of times in an appendix rather than only the median and the maximum, so readers can see whether most detections clustered near the median or were spread across the window. Times for the slow-attacker scenarios are marked.

### 39.5 False alerts

Over four weeks live, false alerts averaged 1.5 per week, below the three-per-week requirement.

Each false alert was reviewed: most were staff with approved forwarding exceptions who signed in from abroad. Lucas added those exceptions to the rule's known benign matches. The rate is an average over four weeks, so a busy week could still exceed three, which the SOC will watch. Lucas reports the average as one and a half per week alongside the weekly counts, so the spread is visible. Analysts confirmed in the feedback described below that this level did not distract them from other work.

### 39.6 Requirements summary

Detection ≥80%: met (90%, though the interval's lower bound is 70%). False alerts ≤3/week: met. Within 30 minutes: met.

The detection line states both the result and the caveat, as the worked example below explains. False alerts and timing are met clearly. Presenting the caveat beside the claim, rather than in a footnote, lets readers see in one place what was met and how confidently. Lucas also lists the requirement on detection time with the median and the slowest value. A summary table with one row per requirement, the result and a brief caveat lets a reader see the outcome in seconds.

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

Placing the campaign and review before the method shows readers why the work was needed. The appendices contain the rule pages, test scenarios without personal data and the analysis scripts. Lucas's supervisor reviewed the outline before he wrote, which avoided reorganising later. Each chapter opens with the question it answers and ends with what it found, so a reader can skim the thesis by reading only those paragraphs.

### 40.2 Literature in the thesis

Lucas draws on Alahmadi et al. (2022) for alarm quality, Axelsson (2000) for base rates, Sundaramurthy et al. (2014) for SOC practice, NIST SP 800-61r3 for response and SigmaHQ conventions for rule documentation.

Each source supports a specific part of the thesis. Base rates justify the attention to false alerts; alarm quality studies explain why analysts' trust matters; SOC practice studies support mixed methods. Lucas cites only what he uses, so the reference list stays short and relevant. He checked each citation against the original source.

### 40.3 Discussion

The package improved detection of test scenarios and fit analyst capacity; reporting by people remained crucial; attackers' timing defeated early assumptions.

The discussion connects results to the campaign: the package would have detected s3310's deletion rule, which went unseen for hours. It also notes what the package does not change. People reporting suspicious mail remained the first signal in the live period, which supports keeping the report button. The discussion also states what surprised him: the slow attacker, which no early design anticipated, became the most important case in the whole project.

### 40.4 Limitations

One university; 20 scenarios; four weeks; scenarios designed by defenders; student population specific.

Each limitation is linked to what it affects. Twenty scenarios limit precision; four weeks limit what the false-alert rate shows; defender-designed scenarios may be easier than real attacks. Stating these lets the SOC decide how far to rely on the package and what to test next. He also lists what would reduce each limitation: more scenarios, a longer live period and scenarios written by someone outside the SOC, such as the external firm that runs Riverton's purple exercise. That turns each limitation into a concrete next step the SOC can choose to fund.

### 40.5 Presentation

A 15-minute talk to the department and a separate 10-minute briefing to the SOC team focusing on how to maintain the package.

The two audiences need different things. The department wants the question, method, results and limits. The SOC team wants to know what each rule does, how to tell a false alert, and how to change thresholds safely. Lucas prepared separate slides for each rather than one talk for both. Both talks end with the same one-sentence result, so the message is consistent.

### 40.6 Reflection

From mathematical reasoning in chapter 1 to the evaluation, the degree built habits: measure fairly, write precisely, act within authority, test assumptions.

Lucas's reflection connects the first chapter's rates to the evaluation's intervals: both are about not overstating what numbers show. He also notes the habit of asking authority before acting, which shaped his work at Eastbank and in the research server case. He writes that the most useful habit was keeping observations separate from inferences, which made every later report easier to check and defend.

### 40.7 Next steps

Lucas plans to apply for a junior analyst role and to keep contributing rule improvements to the SOC's repository as an alumnus volunteer under supervision.

Volunteering under supervision keeps the rules maintained by someone who knows them while the next cohort learns. Lucas's access as an alumnus will be limited to the rule repository, not live logs, which Dr. Kim set as a condition. The archive described below makes his work usable without him. He also agreed to mentor next year's first student analysts during their shadowing stage.

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
