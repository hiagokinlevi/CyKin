# Information Security: Bachelor's Course

- Language: English (`en`); course 094, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students learning how a small financial organisation protects member information through governance, technical controls, operations and measurement.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs review synthetic application access against HR status and role, measure synthetic vulnerability findings against remediation targets and hash synthetic passwords with salted PBKDF2 while checking them against a small breached list. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one bachelor's student from computing, networks, programming, statistics, writing, law and ethics through governance, risk, access and cryptography, then operational security, measurement and audit, to change management, a group project, a placement and a dissertation. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aisha Rahimi** | Bachelor's student | Invented |
| **Dr. Neil Carrow** | Personal tutor | Invented |
| **Pennick University** | Fictional university | Invented |
| **Ashfield Credit Union** | Fictional credit union, about 140 staff, four branches and 35,000 members | Invented |

### Core sources

Anderson (2020), [doi:10.1002/9781119644682](https://doi.org/10.1002/9781119644682); ISO/IEC 27000:2026; ISO/IEC 27001:2022; ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Shadish, Cook and Campbell (2002). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Studying information security at Pennick

### Learning outcomes

You will (1) describe what a bachelor's course in information security covers; (2) introduce the running case; (3) plan study habits for a four-year course.

### 1.1 The student and the course

Aisha Rahimi begins a four-year bachelor's degree in information security at the fictional Pennick University. Her personal tutor is Dr. Neil Carrow, who teaches the first-year foundations module. The course covers how organisations protect information: the technology involved, the people who use it, the rules that govern it and the ways security is measured. Dr. Carrow explains that security is not only a technical subject, and that graduates must explain risks clearly to managers who are not specialists. Aisha chose the course after a relative was defrauded online.

### 1.2 The case organisation

Throughout the course, Aisha works with the fictional Ashfield Credit Union, a member-owned savings and loans organisation with about 140 staff, four branches and roughly 35,000 members. Ashfield holds savings balances, loan records, identity documents and payment details. A breach would harm members directly and damage trust in a small organisation that depends on its local reputation. Dr. Carrow arranged the partnership so that students can see how each topic applies to a real type of organisation, using synthetic data in all exercises. Each module uses it.

### 1.3 How the course is organised

The first year builds foundations: computers, networks, programming, statistics, writing, law and ethics. The second year introduces security governance, risk, access control and cryptography. The third year covers operational security: vulnerabilities, configuration, monitoring, incidents, backups, suppliers and measurement. The final year includes change management, a group project, a placement, research methods and a dissertation. Aisha notes that each year builds on the last, so gaps left early become harder to fill later on. She prints the module map and pins it above her desk, marking which modules depend on which earlier ones.

### 1.4 Study habits

Dr. Carrow advises Aisha to keep a learning journal recording one security idea each week and how it applies to Ashfield. He also recommends reading primary sources, such as standards and well-known papers, rather than relying only on summaries. Aisha sets aside two hours each Friday for review. She learns that security changes quickly, so the habit of checking current sources and their editions matters as much as remembering any single fact. Her first journal entry describes why a small credit union is an attractive target for fraudsters who expect weaker defences than in large banks.

### Worked example

Aisha begins the course, meets the Ashfield case, maps the four years of study and sets a weekly review habit.

> **Synthetic case.** Pennick, Ashfield and all people are synthetic.

### Errors and limits

Treating security as purely technical ignores people, rules and measurement.

### Exercises

- **EX001 — Case size.** How many members does Ashfield have? *Rubric:* 3 = roughly 35,000;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX002 — Final year.** What does the final year include? *Rubric:* 3 = change management, group project, placement, research and dissertation;; 2 = most;; 1 = few;; 0 = none.
- **EX003 — Weekly habit.** What journal habit does Dr. Carrow advise? *Rubric:* 3 = one security idea each week applied to Ashfield;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — What information security is

### Learning outcomes

You will (1) define confidentiality, integrity and availability; (2) apply them to examples; (3) explain why security supports organisational goals.

### 2.1 Three objectives

Aisha learns the three objectives that define information security. FIPS 199, a United States federal standard, defines confidentiality as preserving authorised restrictions on access and disclosure, integrity as guarding against improper modification or destruction, and availability as ensuring timely and reliable access to and use of information. ISO/IEC 27000:2026 describes information security in the same three terms. Dr. Carrow notes that these objectives are widely used because they cover most ways information can be harmed. Aisha copies the three definitions into her journal and writes an Ashfield example beside each one.

### 2.2 Applying them

Aisha applies the objectives to Ashfield. Members' identity documents need confidentiality, because exposure could enable fraud. Account balances need integrity, because an altered balance would mean someone loses money. The online banking service needs availability, because members expect to see their money when they want. She notes that each piece of information usually needs all three to some degree, but one often matters most, which helps decide where effort goes. She records the most important objective for each item in a simple table, which she will reuse when the course reaches risk assessment in the second year.

### 2.3 Beyond the triad

Dr. Carrow introduces related properties. Authenticity means confirming that information or a person is genuine; accountability means actions can be traced to whoever performed them; non-repudiation means someone cannot credibly deny an action they took. At Ashfield, a loan approval must be traceable to the officer who approved it. Aisha learns that these properties extend the three objectives and often depend on good identity management and record keeping. She adds the three properties to her journal table, noting for each Ashfield record whether accountability or authenticity matters as much as the original three objectives.

### 2.4 Security and goals

Security exists to support Ashfield's purpose, not as an end in itself. A control that blocks members from accessing savings may protect confidentiality but damages availability and trust. Aisha learns that good security balances protection with usability and cost. Dr. Carrow asks her to remember that security professionals help organisations take sensible risks, not avoid all risk, because a credit union that refuses all risk could not lend money at all. Aisha writes a short paragraph in her journal describing a control at her own bank that she finds annoying, and asks whether its protection justifies the inconvenience.

### Worked example

Aisha defines the three objectives from FIPS 199, applies them to Ashfield's information, adds authenticity and accountability and links security to Ashfield's goals.

> **Synthetic case.** Examples are synthetic.

### Errors and limits

Maximising one objective can damage the others.

### Exercises

- **EX004 — Availability definition.** How does FIPS 199 define availability? *Rubric:* 3 = timely and reliable access and use;; 2 = correct;; 1 = vague;; 0 = none.
- **EX005 — Balance objective.** Which objective matters most for balances? *Rubric:* 3 = integrity;; 2 = correct;; 1 = other;; 0 = none.
- **EX006 — Loan traceability.** Which property makes loan approvals traceable? *Rubric:* 3 = accountability;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Information in organisations

### Learning outcomes

You will (1) identify the information an organisation holds; (2) trace how information flows; (3) recognise who is responsible for it.

### 3.1 What Ashfield holds

Aisha lists the information Ashfield holds: member identity details, savings and loan records, payment card data, staff records, board minutes and supplier contracts. Some is held in the core banking system, some in email and shared folders and some on paper in branches. Dr. Carrow points out that information on paper and in conversations also needs protection, and that many breaches involve information outside the main systems. She also notes paper application forms stored in branch cabinets, and loan files waiting for scanning in an unlocked tray, as examples of information outside any computer system.

### 3.2 Flows

Information moves. A new member's identity documents are scanned at a branch, uploaded to the core system and checked by a compliance officer. Loan applications pass from branch staff to lending officers to a credit committee. Aisha draws these flows and notes where information leaves Ashfield, for example to a credit reference agency and a card processor. She learns that each flow is a point where information could be intercepted, altered or lost. She labels each arrow on her diagram with the information it carries and the method used to send it.

### 3.3 Responsibility

Every type of information needs someone responsible for deciding how it is protected. At Ashfield, the head of lending is responsible for loan records and the compliance officer for identity documents. Aisha finds that nobody is clearly responsible for the shared folders, where staff save copies of reports. Dr. Carrow explains that unowned information tends to accumulate without controls, and that assigning ownership is often the first practical security step. Ashfield's chief executive later assigns the shared folders to the head of operations, who starts by asking teams to delete old copies.

### 3.4 Value and harm

Aisha estimates the harm if each type of information were exposed, altered or unavailable. Exposure of identity documents could enable fraud against members; altered loan records could hide bad loans; unavailable core banking stops all transactions. She ranks the information by potential harm. She learns that this ranking guides where to spend limited security effort, and that it must be reviewed when the organisation changes. She presents the ranking to her seminar group, who challenge two of her placements. After discussion she moves board minutes higher, because they contain confidential decisions about loan losses and staff.

### Worked example

Aisha lists Ashfield's information, draws flows including external ones, finds unowned shared folders and ranks information by potential harm.

> **Synthetic case.** Information types are synthetic.

### Errors and limits

Ignoring paper and shared folders leaves much information unprotected.

### Exercises

- **EX007 — External recipients.** Name one external recipient of Ashfield information. *Rubric:* 3 = credit reference agency;; 2 = one;; 1 = vague;; 0 = none.
- **EX008 — Unowned store.** Which store had no responsible person? *Rubric:* 3 = shared folders;; 2 = correct;; 1 = other;; 0 = none.
- **EX009 — Ranking purpose.** What does ranking by harm guide? *Rubric:* 3 = where to spend security effort;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Computers and operating systems

### Learning outcomes

You will (1) describe how computers run programs; (2) explain user accounts and permissions; (3) recognise why updates matter.

### 4.1 How computers run programs

Aisha learns that a computer runs programs under an operating system, which manages memory, files and devices. Each program runs as a process, and the operating system keeps processes apart so one cannot directly interfere with another. Ashfield's branch computers run a common desktop operating system, while its servers run another. Dr. Carrow explains that understanding these basics helps security staff see how attacks work and why certain controls are needed. Aisha installs a virtual machine on her laptop so she can explore an operating system safely without affecting her own files.

### 4.2 Accounts and permissions

Operating systems use accounts to decide who can do what. Standard accounts can run programs and use their own files; administrator accounts can install software and change settings. Aisha finds that some Ashfield branch staff use administrator accounts every day, because an old application once needed it. If one of these staff opens a malicious attachment, the malware gets administrator rights too. She recommends standard accounts for daily work. Ashfield's IT manager tests the old application with a standard account and finds it now works, so the daily administrator accounts can be removed.

### 4.3 Updates

Software contains flaws, and vendors publish updates to fix them. Attackers study updates to find what was fixed and then target systems not yet updated. Aisha checks a synthetic list of Ashfield computers and finds several weeks behind on updates because staff postpone restarts. She recommends automatic installation outside branch hours. Dr. Carrow notes that applying updates promptly is one of the most effective and least glamorous security practices. The IT manager agrees to schedule restarts at night, and Aisha suggests reporting the number of computers more than two weeks behind each month.

### 4.4 Malware basics

Malware is software designed to cause harm: stealing information, encrypting files for ransom or giving attackers remote control. It often arrives through email attachments, malicious websites or infected removable media. Aisha learns how antivirus and newer endpoint tools detect suspicious behaviour, and why they are not enough alone. She notes that standard accounts, prompt updates and careful email handling together reduce the chance malware succeeds. She writes a short journal entry comparing how each control would have stopped a ransomware infection described in a news article she read that week, which helps her remember why layers matter.

### Worked example

Aisha learns process separation, finds daily administrator use in branches, recommends automatic updates and connects malware defences to accounts and updates.

> **Synthetic case.** Computers are synthetic.

### Errors and limits

Daily use of administrator accounts gives malware administrator rights.

### Exercises

- **EX010 — Admin cause.** Why do some staff use administrator accounts? *Rubric:* 3 = an old application once needed it;; 2 = correct;; 1 = vague;; 0 = none.
- **EX011 — Update delay.** Why are some computers behind on updates? *Rubric:* 3 = staff postpone restarts;; 2 = correct;; 1 = vague;; 0 = none.
- **EX012 — Malware routes.** Name one way malware arrives. *Rubric:* 3 = email attachments;; 2 = one;; 1 = vague;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Networks and the internet

### Learning outcomes

You will (1) describe how networks connect computers; (2) explain firewalls and encryption in transit; (3) recognise common network threats.

### 5.1 How networks connect

Aisha learns that networks connect devices so they can exchange data. Ashfield's branches connect to its head office over encrypted links, and the head office connects to the internet and to the card processor. Each device has an address, and routers forward data between networks. Dr. Carrow draws the network on a whiteboard and asks students to mark where member data travel, which helps them see where protection is needed. Aisha redraws the diagram neatly at home and marks the card processor connection as the most sensitive external link.

### 5.2 Firewalls

A firewall controls which traffic can pass between networks. Ashfield's firewall allows web traffic to its online banking site and blocks most other incoming connections. Aisha learns that firewall rules accumulate over time and often include old exceptions nobody remembers. She reviews a synthetic rule list and finds a rule allowing remote desktop access from anywhere, created for a supplier years ago. She recommends removing it after checking with the supplier. The supplier confirms it now uses a secure remote access service instead, so the old rule is removed without disruption.

### 5.3 Encryption in transit

When data cross networks, others may be able to read them. Encryption in transit, such as the secure protocol used by websites, protects confidentiality and integrity along the way. Aisha checks that Ashfield's online banking uses it and that old, weak protocol versions are disabled. She learns that encryption protects data while moving, but not once they reach a compromised server, so other controls are still needed. She uses a free online checker against a test website to see which protocol versions it accepts, and records the results in her journal.

### 5.4 Network threats

Aisha studies common threats: attackers scanning for open services, intercepting traffic on unprotected wireless networks and overwhelming services with traffic to make them unavailable. Ashfield's branch wireless network for members is separate from staff networks, which limits risk. Dr. Carrow notes that separating networks by purpose is a simple but powerful control, because a problem in one network does not automatically reach the others. Aisha checks that the member wireless network cannot reach the staff printer, which confirms the separation works. She notes this test in her journal as an example of verifying a control rather than assuming it.

### Worked example

Aisha maps Ashfield's network, finds an old open remote desktop rule, checks encryption in transit and confirms member wireless is separated.

> **Synthetic case.** Networks are synthetic.

### Errors and limits

Old firewall exceptions often stay open long after their purpose ends.

### Exercises

- **EX013 — Old rule.** What old rule does Aisha find? *Rubric:* 3 = remote desktop access from anywhere;; 2 = correct;; 1 = other;; 0 = none.
- **EX014 — Transit limits.** What does encryption in transit not protect? *Rubric:* 3 = data on a compromised server;; 2 = correct;; 1 = vague;; 0 = none.
- **EX015 — Member wireless.** How is member wireless protected? *Rubric:* 3 = separated from staff networks;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Python for security checks

### Learning outcomes

You will (1) write simple Python scripts; (2) read and check data files; (3) produce clear results for others.

### 6.1 Getting started

Aisha writes her first Python scripts using only the standard library, so they run on any university or Ashfield computer without extra installation. Her first script reads a synthetic list of staff accounts from a text file and counts how many exist. Dr. Carrow explains that scripting lets security staff check thousands of records quickly and consistently, where manual checking would be slow and error-prone. She writes the script in a plain text editor, runs it from the command line and checks the count against the number of lines in the file. The two numbers match.

### 6.2 Checking data

Aisha's next script checks each account for a last login date. Accounts with no login for ninety days are listed for review. She uses the datetime module to compare dates. When a line has a missing date, the script records it separately instead of crashing. She learns that real data contain gaps and errors, and that a good checking script reports problems with its input as clearly as the results it was written to find. Three lines in the synthetic file lack dates.

### 6.3 Clear output

Dr. Carrow asks Aisha to make her output readable by managers. She prints a heading, the date of the check, the number of accounts checked, the number flagged and a list of flagged accounts with their last login dates. She also saves results to a CSV file using the csv module. She learns that the person reading a security report often decides what happens next, so clarity matters. Dr. Carrow marks the second version as clear and asks the class to use her layout as a model for later reports.

### 6.4 Keeping scripts safe

Aisha's scripts handle sensitive data. She keeps them and their outputs in a protected folder, never emails results containing account names to personal addresses and deletes temporary files after use. She also avoids writing passwords into scripts. Dr. Carrow notes that security tools can become security risks if their outputs leak, because a list of inactive accounts is useful to an attacker looking for unmonitored logins. She writes a short checklist for handling outputs and attaches it to every script folder, so classmates working with her follow the same rules.

### Worked example

Aisha writes standard-library scripts that count accounts, flag ninety-day inactivity, handle missing dates and produce readable reports and CSV files kept securely.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Leaked security reports can help attackers.

### Exercises

- **EX016 — Inactivity threshold.** Which accounts are flagged? *Rubric:* 3 = no login for ninety days;; 2 = correct;; 1 = vague;; 0 = none.
- **EX017 — Missing dates.** How does the script treat missing dates? *Rubric:* 3 = records them separately;; 2 = correct;; 1 = crash;; 0 = none.
- **EX018 — Leak risk.** Why could an inactive account list help attackers? *Rubric:* 3 = it shows unmonitored logins;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Statistics for security work

### Learning outcomes

You will (1) summarise security data with simple statistics; (2) interpret proportions and averages; (3) recognise misleading comparisons.

### 7.1 Counts and proportions

Aisha learns that many security measures are counts and proportions: the number of unpatched computers, the share of staff completing training, the proportion of phishing tests reported. She computes that 112 of 140 synthetic staff completed annual training, eighty percent. Dr. Carrow asks her to always report the denominator, because a count of 112 means little without knowing it is out of 140. She also reports the twenty-eight staff who had not completed it, listed by branch, so managers can follow up. Dr. Carrow notes that the same figure can be presented as completion or as a gap, and both views are useful.

### 7.2 Averages and spread

Aisha calculates how long Ashfield takes to close security findings. The mean is twenty-six days, but a few findings took over a hundred days. The median is fifteen days. She learns that the mean is pulled up by extreme values, so the median often describes a typical case better. She reports both, plus the longest cases, because those long-running findings may represent the greatest risk. She draws a simple chart of closure times, which shows most findings closing within a month and a long tail of slow ones.

### 7.3 Comparing groups

Ashfield's managers want to know which branch is most secure. Aisha notes that the largest branch has the most incidents but also the most staff and transactions. Comparing raw counts would unfairly blame it. She calculates incidents per hundred staff, which changes the ranking. Dr. Carrow explains that rates allow fair comparison between groups of different sizes. With rates, the largest branch moves from worst to second best, and the smallest branch, which had few incidents in total, turns out to have the highest rate. Ashfield's managers are surprised and ask her to repeat the analysis each quarter.

### 7.4 Uncertainty

With small numbers, differences can arise by chance. One branch had three phishing reports last month and seven this month. Aisha explains that this change may not mean anything, because counts this small vary naturally. She suggests looking at several months before drawing conclusions. She learns that security reports should avoid treating normal variation as meaningful change. She shows the managers twelve months of reports per branch in one chart, where the month-to-month ups and downs are clearly visible. The managers agree to review trends quarterly rather than reacting to single months, which reduces unnecessary worry.

### Worked example

Aisha reports training completion with its denominator, compares mean and median closure times, uses rates to compare branches and warns about chance variation.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Comparing raw counts between groups of different sizes misleads.

### Exercises

- **EX019 — Training rate.** What share of staff completed training? *Rubric:* 3 = 112 of 140, eighty percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX020 — Median closure.** What is the median closure time? *Rubric:* 3 = fifteen days;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX021 — Fair comparison.** How are branches compared fairly? *Rubric:* 3 = incidents per hundred staff;; 2 = correct;; 1 = raw;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Writing about security

### Learning outcomes

You will (1) write clear security reports; (2) adapt writing for different readers; (3) cite sources properly.

### 8.1 Clear writing

Aisha's first assignment is a one-page report on Ashfield's inactive accounts. Dr. Carrow returns her draft marked with questions: what is the problem, why does it matter, what should be done and by whom? She rewrites it with a short summary at the top, the evidence, the risk and a recommendation with an owner. She learns that busy readers often read only the first paragraph, so it must contain the key message. Dr. Carrow gives the rewritten report a strong mark and comments that it can be acted on immediately.

### 8.2 Different readers

Aisha writes two versions of the same finding. For Ashfield's board, she explains that former employees could still access member records and that the fix is a monthly check linked to leaving procedures. For the IT team, she lists the accounts and the exact steps to disable them. Dr. Carrow notes that the facts are the same, but readers need different detail to act. She checks both versions with a classmate playing each reader, who confirms they know what to do after reading. Dr. Carrow keeps both as examples.

### 8.3 Citing sources

Aisha learns to cite sources precisely. When she refers to a standard, she names its number, edition and year, such as ISO/IEC 27001:2022. When she cites a paper, she includes authors, year, title and a persistent identifier if one exists. Dr. Carrow warns that standards change, so citing the edition tells readers exactly which version she relied on, and that she should never cite a source she has not checked. She builds a reference list for her journal that includes each source's edition or identifier and the date she checked it.

### 8.4 Avoiding alarmism

Security writing can slip into alarm. Aisha's draft described an open firewall rule as catastrophic. Dr. Carrow asks what evidence supports that word. She rewrites it to state the rule, what an attacker could do and how likely that is. She learns that measured language builds credibility, and that readers who hear alarm too often stop listening. The revised finding states that the rule allowed connections from any address and that the remote desktop service had been patched recently, which lowers the immediate likelihood but does not remove the need to close it.

### Worked example

Aisha rewrites a report with a summary first, produces board and IT versions, cites standards by edition and replaces alarmist language with evidence.

> **Synthetic case.** Reports are synthetic.

### Errors and limits

Citing a standard without its edition leaves readers unsure which version applies.

### Exercises

- **EX022 — Report questions.** What four questions should a report answer? *Rubric:* 3 = problem, importance, action, owner;; 2 = all;; 1 = some;; 0 = none.
- **EX023 — Board version.** What does the board version emphasise? *Rubric:* 3 = former employees could access records;; 2 = correct;; 1 = vague;; 0 = none.
- **EX024 — Edition citation.** Why cite a standard's edition? *Rubric:* 3 = standards change;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Law and security

### Learning outcomes

You will (1) identify laws relevant to information security; (2) explain obligations to protect personal data; (3) recognise legal limits on security activities.

### 9.1 Why law matters

Aisha learns that laws shape information security in several ways. Data protection law requires organisations to protect personal data with appropriate security. Financial regulators expect institutions such as credit unions to manage operational risks, including cyber risks. Computer misuse laws make unauthorised access a crime. Dr. Carrow explains that the specific laws depend on the country, so the course teaches principles and asks students to check the law that applies where they work. Aisha makes a table listing each type of law and the Ashfield activity it affects.

### 9.2 Personal data

Ashfield holds personal data about members and staff. Data protection laws in many countries require security appropriate to the risk, limits on how long data are kept and notification of certain breaches to regulators and affected people. Aisha notes that these obligations make security a legal duty, not just good practice. She learns that a breach can lead to regulatory penalties and compensation claims, as well as lost trust. She notes that Ashfield's compliance officer is the person who would decide whether a breach must be reported, and that security staff must provide facts quickly.

### 9.3 Unauthorised access

Computer misuse laws make it a crime to access systems without permission. Aisha learns that this applies to security testing too: testing Ashfield's systems without written authorisation could be illegal, even if intended to help. Dr. Carrow explains that professional testers always work under signed agreements that define scope and timing. Students must never test real systems they do not own or have permission to test. Aisha signs the university's ethical testing agreement, which confirms that course exercises use only laboratory systems and synthetic data provided by the department.

### 9.4 Contracts

Ashfield's contracts with suppliers include security obligations, such as protecting member data and reporting incidents. Aisha reviews a synthetic contract with the card processor and finds clear incident reporting terms but no right for Ashfield to check the supplier's security. She recommends adding audit rights at renewal. She learns that contracts extend security obligations beyond an organisation's own walls. Ashfield's head of operations agrees and adds the change to the renewal checklist. Aisha also notes that contracts should say how quickly a supplier must report incidents, and finds this one requires notice within twenty-four hours.

### Worked example

Aisha identifies data protection, regulatory and misuse laws, links personal data obligations to security, insists on written authorisation for testing and finds a missing audit right in a contract.

> **Synthetic case.** Laws vary by country; the contract is synthetic.

### Errors and limits

Testing systems without written authorisation may be a crime.

### Exercises

- **EX025 — Law types.** Name one type of law shaping security. *Rubric:* 3 = data protection law;; 2 = one;; 1 = vague;; 0 = none.
- **EX026 — Testing rule.** What must testers always have? *Rubric:* 3 = signed authorisation defining scope;; 2 = correct;; 1 = vague;; 0 = none.
- **EX027 — Contract gap.** What did the card processor contract lack? *Rubric:* 3 = audit rights;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Ethics and security

### Learning outcomes

You will (1) apply ethical reasoning to security decisions; (2) balance monitoring and privacy; (3) handle discovered weaknesses responsibly.

### 10.1 Ethical reasoning

Security professionals often have access to sensitive information and powerful tools. Aisha discusses cases where staff misused access, such as reading a neighbour's records out of curiosity. Dr. Carrow explains that professional ethics requires using access only for authorised purposes, being honest about risks and respecting people affected by security decisions. Aisha notes that legal and ethical are not identical, and that some legal actions are still wrong. The class discusses a case in which an employee looked up a celebrity's account and was dismissed.

### 10.2 Monitoring and privacy

Ashfield monitors staff email for signs of fraud. Aisha considers how far monitoring should go. Monitoring protects members, but excessive monitoring treats staff as suspects and may intrude on private messages. She suggests clear notices, limiting monitoring to work systems, restricting who can view results and reviewing whether it remains necessary. She learns that proportionality is the key ethical test for monitoring. Ashfield's monitoring notice is reviewed by the compliance officer, who adds a sentence explaining that personal messages are not read unless fraud is suspected and approved by two managers.

### 10.3 Discovered weaknesses

During a class exercise using a public website, a classmate notices a weakness on a real organisation's site. Aisha's group discusses what to do. They agree not to explore further and to report it through the organisation's published contact for security issues, if one exists. Dr. Carrow explains coordinated disclosure: telling the organisation privately and giving time to fix before any public discussion. The group records what they saw, informs Dr. Carrow and drafts a short message to the organisation, which Dr. Carrow reviews before it is sent through the official channel.

### 10.4 Fairness

Security decisions affect people unequally. A rule blocking logins from abroad may stop fraud but also blocks members travelling or living overseas. Aisha suggests letting members register travel and offering alternative verification. She learns that fair security considers who bears the burden of controls, and that the people most affected should have a way to raise problems and be heard. Ashfield adopts the travel registration option, and member complaints about blocked logins fall over the next quarter. Aisha notes that the change also improved fraud detection, because unexpected foreign logins now stand out more clearly.

### Worked example

Aisha separates legal from ethical, applies proportionality to staff monitoring, follows coordinated disclosure for a found weakness and considers fairness of geographic login blocks.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Using authorised access for personal curiosity is a breach of trust.

### Exercises

- **EX028 — Monitoring test.** What is the key ethical test for monitoring? *Rubric:* 3 = proportionality;; 2 = correct;; 1 = other;; 0 = none.
- **EX029 — Disclosure approach.** How should the found weakness be handled? *Rubric:* 3 = report privately via published contact;; 2 = correct;; 1 = vague;; 0 = none.
- **EX030 — Blocked group.** Who is unfairly affected by foreign login blocks? *Rubric:* 3 = members abroad;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Security governance foundations

### Learning outcomes

You will (1) explain what security governance is; (2) describe how boards oversee security; (3) relate governance to frameworks.

### 11.1 What governance means

In her second year, Aisha studies security governance: how an organisation directs and oversees its security. Governance answers who decides how much risk is acceptable, who is accountable and how leaders know whether security is working. Dr. Carrow distinguishes governance from management. The board sets direction and asks questions; managers design and run controls. Aisha notes that at Ashfield the board approves the risk appetite and receives quarterly security reports, while the IT manager runs day-to-day controls and reports progress upward. She draws both.

### 11.2 The board's role

Ashfield's board includes volunteers elected by members, few of whom have technical backgrounds. Aisha considers what they need: a clear picture of the main risks, whether controls are working and what decisions require their approval. She reviews a synthetic board report filled with technical counts and suggests replacing it with five risk statements, each with a trend and an owner. Dr. Carrow notes that good governance depends on information leaders can understand and act on, not on volume. The board chair welcomes the change.

### 11.3 Frameworks

Aisha studies the NIST Cybersecurity Framework 2.0, which added a Govern function to Identify, Protect, Detect, Respond and Recover. The Govern function covers organisational context, risk management strategy, roles, policy and oversight. She maps Ashfield's current arrangements to these outcomes and finds that roles and policy exist but supply chain risk management is weak. Dr. Carrow explains that frameworks help organisations see gaps systematically, but that they describe outcomes rather than prescribing exact methods. She presents the mapping as a table with one row per outcome and a simple status for each.

### 11.4 Risk appetite

A risk appetite statement says how much risk an organisation will accept in pursuit of its goals. Ashfield's board states it will accept low risk to member data confidentiality but moderate risk of short service interruptions outside business hours. Aisha notes that this guides decisions: spending to prevent data exposure is justified more readily than spending to eliminate brief overnight outages. She learns that appetite statements turn vague values into practical guidance managers can apply. Aisha uses the statement to explain two past spending decisions to her seminar group.

### Worked example

Aisha separates governance from management, simplifies the board report into five risk statements, maps Ashfield to CSF 2.0 Govern outcomes and applies the risk appetite to spending.

> **Synthetic case.** Board arrangements are synthetic.

### Errors and limits

Board reports full of technical counts rarely support decisions.

### Exercises

- **EX031 — Board approves.** What does Ashfield's board approve? *Rubric:* 3 = the risk appetite;; 2 = correct;; 1 = other;; 0 = none.
- **EX032 — Govern gap.** Which Govern outcome is weak at Ashfield? *Rubric:* 3 = supply chain risk management;; 2 = correct;; 1 = other;; 0 = none.
- **EX033 — Appetite effect.** Which spending is justified more readily? *Rubric:* 3 = preventing data exposure;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Roles and accountability

### Learning outcomes

You will (1) define key security roles; (2) assign accountability for information and controls; (3) separate duties to reduce fraud and error.

### 12.1 Key roles

Aisha lists security roles at Ashfield. The board holds ultimate accountability. The chief executive ensures resources. The IT manager leads security operations, as Ashfield is too small for a dedicated security officer. Information owners, such as the head of lending, decide how their information is protected. All staff follow policies and report incidents. Dr. Carrow notes that small organisations often combine roles, which is acceptable if responsibilities are written down and conflicts are managed openly. Aisha writes each role's main duties in a single sentence for the staff handbook.

### 12.2 Accountability

Accountability means a named person answers for an outcome. Aisha finds that several controls at Ashfield have no named owner: the firewall review, supplier security checks and backup testing. Each was assumed to be someone else's job. She drafts a responsibility table listing each control, its owner and how often it runs. The chief executive approves it. She learns that unowned controls tend to stop without anyone noticing, which is why naming owners matters. Within a month, all three controls have run at least once under their new owners.

### 12.3 Separation of duties

Separation of duties splits sensitive tasks so no single person can complete them alone. At Ashfield, one person enters a payment and another approves it. Aisha finds that the IT manager can both create user accounts and approve their access, so an unauthorised account could be created without anyone else knowing. She recommends that access approvals come from information owners. Dr. Carrow links this to Saltzer and Schroeder's principle of separation of privilege. The head of lending and the head of finance agree to approve access for their own teams.

### 12.4 Small-organisation limits

Strict separation is hard in small teams. Ashfield has only two IT staff, so when one is on holiday, the other must do everything. Aisha suggests compensating controls: logging all administrator actions and having the head of operations review the log weekly. She learns that when separation is impossible, detection and review can partly replace it, and that documenting the compromise shows it was a deliberate decision rather than an oversight. The head of operations performs the first weekly review with Aisha watching, and finds every logged action explained by a ticket.

### Worked example

Aisha lists roles, names owners for unowned controls, finds that one person creates and approves accounts and proposes logging and review where separation is impossible.

> **Synthetic case.** Roles are synthetic.

### Errors and limits

Controls that nobody owns tend to stop without anyone noticing.

### Exercises

- **EX034 — Unowned controls.** Name one control that had no owner. *Rubric:* 3 = firewall review;; 2 = one;; 1 = vague;; 0 = none.
- **EX035 — Access conflict.** What conflict does the IT manager have? *Rubric:* 3 = creates and approves accounts;; 2 = correct;; 1 = vague;; 0 = none.
- **EX036 — Compensating control.** What compensates for limited separation? *Rubric:* 3 = logging admin actions with weekly review;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Policies and standards

### Learning outcomes

You will (1) distinguish policies, standards and procedures; (2) write a short security policy; (3) relate organisational policy to international standards.

### 13.1 Document types

Aisha learns to distinguish document types. A policy states what the organisation intends and requires, at a high level, such as all access to member data must be authorised. A standard sets specific mandatory requirements, such as passwords must be at least fourteen characters. A procedure describes step-by-step how to do something. Dr. Carrow explains that mixing these types produces documents that are too detailed to approve and too vague to follow, a common problem in small organisations. She sorts Ashfield's documents into the three types.

### 13.2 Writing a policy

Aisha drafts an access control policy for Ashfield. It states the purpose, scope, principles of least privilege and need to know, roles responsible and how compliance is checked. She keeps it to one page so staff will read it. Dr. Carrow reviews it and asks her to remove technical detail about password length, which belongs in a standard that can be updated without board approval. The final policy is short and clear. The board approves the policy at its next meeting without changes.

### 13.3 International standards

Aisha studies how organisations use ISO/IEC standards. ISO/IEC 27001:2022 sets requirements for an information security management system, including that top management establishes an information security policy. ISO/IEC 27002:2022 gives guidance on controls, including topic-specific policies such as access control. ISO/IEC 27000:2026 provides the overview of the family. She learns that Ashfield need not seek certification to benefit from using these standards as guidance. Aisha prepares a short table showing which Ashfield documents correspond to each of the main ISO/IEC 27002 control themes, and notes where Ashfield has nothing yet, such as supplier security.

### 13.4 Keeping policies alive

Policies go out of date. Aisha finds Ashfield's acceptable use policy refers to fax machines and makes no mention of cloud storage. She recommends an annual review with named owners and a change log. She also suggests a short quiz in annual training to check that staff understand key requirements. She learns that a policy nobody reads or updates provides little protection, regardless of how well it was written originally. The compliance officer takes ownership of the review schedule and adds each policy's review date to the board calendar.

### Worked example

Aisha distinguishes policy, standard and procedure, writes a one-page access policy, relates it to ISO/IEC 27001 and 27002 and recommends annual review.

> **Synthetic case.** Policies are synthetic; standards are paraphrased.

### Errors and limits

Putting technical detail in policies forces board approval for routine changes.

### Exercises

- **EX037 — Standard example.** Which is an example of a standard? *Rubric:* 3 = passwords at least fourteen characters;; 2 = correct;; 1 = other;; 0 = none.
- **EX038 — Removed detail.** What detail is removed from the policy? *Rubric:* 3 = password length;; 2 = correct;; 1 = other;; 0 = none.
- **EX039 — Outdated policy.** What did the acceptable use policy omit? *Rubric:* 3 = cloud storage;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Risk assessment

### Learning outcomes

You will (1) identify threats and vulnerabilities; (2) estimate likelihood and impact; (3) produce a prioritised risk register.

### 14.1 Risk components

Aisha learns that risk combines the likelihood of a harmful event with its impact. NIST SP 800-30 Revision 1 describes risk assessment as identifying threat sources and events, vulnerabilities, likelihood and impact. She identifies threats to Ashfield, such as criminals sending fake payment requests, and vulnerabilities, such as staff unable to verify requests easily. Dr. Carrow explains that risk exists only when a threat can exploit a vulnerability to cause harm to something valued. She writes one example threat and vulnerability for each of Ashfield's main systems.

### 14.2 Estimating

Aisha uses a simple scale of low, medium and high for likelihood and impact. Fake payment requests are likely, because fraudsters target small financial organisations, and impact is high, because money could be lost. A fire at the head office is unlikely but high impact. She records her reasoning for each rating so others can challenge it. She learns that ratings are judgements, and that writing down the reasoning makes them reviewable. Her seminar group challenges two ratings, and she changes one after hearing their reasoning.

### 14.3 The register

Aisha builds a risk register for Ashfield with ten entries, each with description, owner, likelihood, impact, current controls and planned actions. She sorts it by combined rating. Fake payment requests, ransomware and staff misuse of member data rank highest. The IT manager and chief executive review the register and agree owners. Dr. Carrow notes that a register is useful only if owners act and it is updated when circumstances change. The register is stored in a shared folder, and the IT manager adds a review of it to each quarterly board report.

### 14.4 Treating risks

For each risk, Ashfield chooses a treatment: reduce it with controls, transfer it through insurance or contracts, avoid it by stopping an activity or accept it within appetite. Aisha recommends reducing fake payment risk by requiring call-back verification to known numbers. She notes that cyber insurance transfers some financial loss but not reputational harm. She learns that treatment choices should be recorded with reasons and approved by the risk owner. The chief executive approves the call-back rule, and finance staff receive a printed list of verified supplier phone numbers.

### Worked example

Aisha identifies threats and vulnerabilities, rates likelihood and impact with reasons, builds a ten-entry register and chooses treatments including call-back verification.

> **Synthetic case.** The register is synthetic.

### Errors and limits

Insurance transfers some financial loss but not reputational harm.

### Exercises

- **EX040 — Assessment source.** Which publication guides the risk assessment? *Rubric:* 3 = NIST SP 800-30 Revision 1;; 2 = correct;; 1 = other;; 0 = none.
- **EX041 — Top risks.** Name one of the top three risks. *Rubric:* 3 = fake payment requests;; 2 = one;; 1 = vague;; 0 = none.
- **EX042 — Payment treatment.** How is fake payment risk reduced? *Rubric:* 3 = call-back verification to known numbers;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Asset management

### Learning outcomes

You will (1) build an inventory of information assets; (2) classify assets by sensitivity; (3) keep the inventory current.

### 15.1 Building an inventory

Aisha helps Ashfield build an inventory of information assets: hardware, software, data stores and services. She starts from purchase records and the IT manager's spreadsheet, then walks through each branch. She finds a forgotten network storage device in a branch cupboard holding old scanned documents. Dr. Carrow notes that inventories often miss such devices, and that walking around physically still finds things records miss, especially in small organisations. Her final inventory lists hardware, software, data stores and external services, with one row per asset and its location.

### 15.2 Classification

Aisha proposes a simple classification scheme: public, internal, confidential and restricted. Member identity documents and payment card data are restricted; loan records are confidential; staff newsletters are internal; branch opening hours are public. Each class has handling rules, such as encryption for restricted data on laptops. She keeps the scheme to four levels so staff can remember it. Dr. Carrow notes that complex schemes are often ignored in practice. She prints a one-page guide with examples for each class and the handling rules that apply.

### 15.3 Owners and handling

Each asset in the inventory gets an owner and a classification. The forgotten storage device is assigned to the head of operations, who decides the documents should be moved to the core system and the device securely wiped. Aisha records the decision. She learns that inventory, ownership and classification together make it possible to apply the right controls, because nobody can protect an asset appropriately without knowing what it holds. The wiping is done by a certified supplier, which provides a certificate for the record.

### 15.4 Keeping it current

Aisha recommends that new purchases be added to the inventory before use and that disposals be recorded with evidence of data destruction. She suggests a twice-yearly check comparing the inventory with devices seen on the network. She learns that an inventory decays quickly without routine updates, and that linking it to purchasing and disposal processes keeps it accurate with little extra effort. The IT manager agrees to add an inventory step to the purchasing form, so nothing new reaches the network without being recorded first.

### Worked example

Aisha builds an inventory that finds a forgotten storage device, proposes four classification levels, assigns owners and links the inventory to purchasing and disposal.

> **Synthetic case.** Assets are synthetic.

### Errors and limits

Complex classification schemes are often ignored.

### Exercises

- **EX043 — Forgotten device.** What forgotten asset does Aisha find? *Rubric:* 3 = a network storage device in a cupboard;; 2 = correct;; 1 = vague;; 0 = none.
- **EX044 — Restricted class.** Which data are restricted? *Rubric:* 3 = identity documents and payment card data;; 2 = correct;; 1 = other;; 0 = none.
- **EX045 — Inventory upkeep.** How is the inventory kept current? *Rubric:* 3 = link to purchasing and disposal, twice-yearly check;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Access control

### Learning outcomes

You will (1) apply least privilege and need to know; (2) design role-based access; (3) manage joiners, movers and leavers.

### 16.1 Principles

Aisha learns two principles for access control. Least privilege means each person or program has only the access needed for their task. Need to know means access to information is limited to those who need it for their work. Saltzer and Schroeder listed least privilege among their 1975 design principles. At Ashfield, tellers need to view member balances but not approve loans; lending officers need loan records but not ledger entries. She writes a short example for each role showing what it can and cannot see in the core system.

### 16.2 Role-based access

Aisha designs roles for Ashfield: teller, lending officer, finance and IT. Each role has a defined set of application permissions. New staff receive their role's permissions rather than copying a colleague's, which often brings extra rights. She documents each role's permissions in a table approved by information owners. Dr. Carrow notes that roles make access easier to review, because reviewers can compare people with their role instead of judging each permission individually. The information owners sign the table, and IT uses it for every new account.

### 16.3 Joiners, movers and leavers

Access changes when people join, change roles or leave. Aisha maps Ashfield's process. Joiners are set up by IT after a request from human resources. Movers often keep old access because nobody removes it. Leavers' accounts are disabled when IT is told, which sometimes happens days later. She recommends that human resources trigger all three events automatically and that movers' old access be removed by default. Human resources agrees to send a notice to IT on the same day for each event. Aisha drafts the notice template.

### 16.4 Privileged access

Administrator accounts can change systems and access all data. Aisha recommends separate administrator accounts used only for administration, protected by multi-factor authentication and logged. Daily work uses normal accounts. She finds that one shared administrator account is used by both IT staff and a supplier. She recommends individual accounts so actions can be traced. Dr. Carrow notes that privileged accounts are the main target for attackers after initial entry. The supplier receives its own named account, which is enabled only when it has an approved support request open.

### Worked example

Aisha applies least privilege and need to know, designs four roles, maps joiner, mover and leaver gaps and separates privileged accounts.

> **Synthetic case.** Roles are synthetic.

### Errors and limits

Copying a colleague's access often grants unneeded rights.

### Exercises

- **EX046 — Teller access.** What do tellers need? *Rubric:* 3 = view balances, not approve loans;; 2 = correct;; 1 = vague;; 0 = none.
- **EX047 — Mover problem.** What happens to movers' old access? *Rubric:* 3 = it is often kept;; 2 = correct;; 1 = vague;; 0 = none.
- **EX048 — Shared admin.** Who shares the administrator account? *Rubric:* 3 = IT staff and a supplier;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Authentication

### Learning outcomes

You will (1) compare authentication factors; (2) explain multi-factor authentication; (3) recognise attacks on authentication.

### 17.1 Factors

Authentication confirms that someone is who they claim to be. Aisha learns three factor types: something you know, such as a password; something you have, such as a phone or hardware key; and something you are, such as a fingerprint. Each has weaknesses. Passwords can be guessed or stolen; phones can be lost; fingerprints cannot be changed if copied. Dr. Carrow explains that combining factors of different types makes attacks much harder. She lists which factors Ashfield already uses for members and staff.

### 17.2 Multi-factor authentication

Ashfield's online banking uses passwords plus a code sent by text message. Aisha learns that text message codes are better than passwords alone but can be intercepted through mobile number takeover. App-based codes and hardware keys are stronger. For staff remote access, she recommends app-based codes, and for IT administrators, hardware keys. She notes that member convenience matters, so changes for members need careful communication and support. She drafts a member leaflet explaining why app codes are safer, and the marketing team agrees to include it with annual statements.

### 17.3 Attacks

Aisha studies attacks on authentication. Phishing tricks people into entering credentials on fake sites. Credential stuffing tries usernames and passwords leaked from other services. Password guessing tries common passwords against many accounts. Prompt bombing sends repeated approval requests hoping a tired user accepts one. She learns that multi-factor authentication stops many of these, but phishing-resistant methods such as hardware keys are needed against the most capable attackers. She writes a short summary of each attack for the awareness programme, using plain language and an example message staff might see.

### 17.4 Account recovery

Attackers often target account recovery instead of login. If a member can reset a password by answering easily discovered questions, strong login controls are bypassed. Aisha reviews Ashfield's synthetic recovery process and finds that branch staff reset passwords after members state their date of birth and address, information often available publicly. She recommends identity documents in branch or verification through the registered phone. Dr. Carrow notes that recovery is often the weakest point. The branch managers agree to the change after a short trial.

### Worked example

Aisha compares factor types, recommends app codes and hardware keys, studies phishing, stuffing and prompt bombing and strengthens weak member password recovery.

> **Synthetic case.** Processes are synthetic.

### Errors and limits

Strong login controls are bypassed if account recovery is weak.

### Exercises

- **EX049 — Fingerprint weakness.** What is the weakness of fingerprints? *Rubric:* 3 = cannot be changed if copied;; 2 = correct;; 1 = vague;; 0 = none.
- **EX050 — Text code risk.** How can text message codes be stolen? *Rubric:* 3 = mobile number takeover;; 2 = correct;; 1 = other;; 0 = none.
- **EX051 — Recovery weakness.** What weak recovery check did branches use? *Rubric:* 3 = date of birth and address;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Reviewing access

### Learning outcomes

You will (1) run an access review against authoritative records; (2) find leavers and excess rights; (3) report and fix review findings.

### 18.1 Purpose of reviews

Access drifts over time as people move, leave and receive temporary rights that are never removed. Periodic access reviews compare who has access with who should. Aisha plans a review of Ashfield's core banking access using two authoritative sources: the human resources list showing who works there and in which role, and the role table approved by information owners. Dr. Carrow emphasises that reviews must use authoritative data, not a manager's memory. She schedules the review for the first week of the quarter.

### 18.2 The access lab

The lab builds a synthetic list of 140 Ashfield accounts with roles, employment status and application access. It finds ten accounts belonging to people who have left but remain active. Among current staff, thirteen hold access beyond their role, and six of those have administrator access they should not. Aisha notes that the leavers are the most urgent, because nobody monitors their activity and their former colleagues would not notice misuse. She shares the three lists with the IT manager and the information owners within an hour, so each owner can confirm or reject the findings in their area.

### Lab — Reviewing synthetic application access against HR status and role

```python
"""Review synthetic application access against HR status and role (stdlib only)."""
import random
random.seed(3)
roles = {"teller": {"core"}, "lending": {"core", "loans"}, "finance": {"core", "ledger"}, "it": {"core", "admin"}}
staff = []
for i in range(140):
    role = random.choice(["teller"] * 5 + ["lending"] * 3 + ["finance"] * 2 + ["it"])
    left = random.random() < 0.1
    apps = set(roles[role])
    if random.random() < 0.08:
        apps.add(random.choice(["loans", "ledger", "admin"]))
    staff.append((f"s{i:03d}", role, left, apps))
leavers_active = [s for s in staff if s[2]]
excess = [s for s in staff if not s[2] and s[3] - roles[s[1]]]
admin_excess = [s for s in excess if "admin" in s[3] - roles[s[1]]]
print(f"accounts {len(staff)}; leavers still active {len(leavers_active)}")
print(f"current staff with access beyond role {len(excess)}; of which admin {len(admin_excess)}")
```

Run with `python3 lab_access.py`. Verified output:

```text
accounts 140; leavers still active 10
current staff with access beyond role 13; of which admin 6
```

### 18.3 Investigating findings

Aisha checks the ten leaver accounts with the IT manager. Most belong to staff who left during a busy period when leaving forms were delayed. Two belong to temporary staff whose contracts ended without notice to IT. For the thirteen excess cases, information owners confirm that most are left over from earlier roles, while two were granted temporarily for a project. She learns that understanding causes points to process fixes, not just account fixes. She writes each cause beside the account in her review notes.

### 18.4 Fixing and repeating

The ten leaver accounts are disabled the same day. Excess rights are removed after owners confirm, except one justified temporary grant recorded with an end date. Aisha recommends quarterly reviews and the automated leaver process proposed earlier. Dr. Carrow notes that the second review usually finds far fewer issues, which itself is evidence that process changes worked. She plans to compare results after the next review. She records each fix with the date and the person who confirmed it, so the next review can check that nothing has returned since.

### Worked example

Aisha reviews 140 synthetic accounts, finds 10 active leavers and 13 staff with excess access (6 with admin), traces causes and sets quarterly reviews.

> **Synthetic case.** Accounts are synthetic; outputs come from lab_access.py.

### Errors and limits

Reviews based on managers' memory miss leavers and leftover rights.

### Exercises

- **EX052 — Active leavers.** How many leavers still had active accounts? *Rubric:* 3 = ten;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX053 — Excess access.** How many current staff had access beyond their role? *Rubric:* 3 = thirteen;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX054 — Excess admin.** How many of them held administrator access? *Rubric:* 3 = six;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Cryptography basics

### Learning outcomes

You will (1) explain symmetric and public-key encryption; (2) describe hashing and digital signatures; (3) recognise common cryptographic mistakes.

### 19.1 Encryption

Encryption transforms readable data into unreadable form using a key. Aisha learns that symmetric encryption uses one shared key for both encryption and decryption, and is fast, so it protects stored data and network traffic. Public-key encryption uses a pair: a public key anyone can use to encrypt and a private key only the owner holds to decrypt. Dr. Carrow explains that websites use both together: public keys to agree on a shared key, then symmetric encryption for speed. She tries both in the laboratory.

### 19.2 Hashing

A hash function produces a fixed-length fingerprint of data. Changing one bit of the input changes the fingerprint completely, and it is impractical to find another input with the same fingerprint. Aisha uses Python's hashlib module to compute SHA-256 fingerprints of synthetic files and confirms that a small change produces a different result. She learns that hashes verify integrity, such as checking that a downloaded file is genuine. She records the two fingerprints in her journal to show the difference, and explains the idea to her seminar group with a printed example.

### 19.3 Digital signatures

A digital signature uses a private key to sign data and the matching public key to verify it. Anyone can check the signature, but only the key holder could have produced it. Aisha learns that software updates are signed so computers can reject tampered versions. At Ashfield, signed emails could help members recognise genuine messages. Dr. Carrow notes that signatures provide authenticity and integrity, but depend on keeping private keys secure. She checks that Ashfield's computers verify signed updates before installing them.

### 19.4 Common mistakes

Aisha studies common mistakes: inventing new algorithms, using outdated ones, storing keys beside encrypted data and failing to renew certificates. She finds that Ashfield's backup files are encrypted, but the key is stored in the same folder. She recommends separate key storage. She learns that most cryptographic failures come from how keys are handled and systems configured, not from breaking the mathematics. The IT manager moves the key to a separate protected store the same week. Aisha then confirms that a test restore still works with the key retrieved from its new location.

### Worked example

Aisha compares symmetric and public-key encryption, computes SHA-256 fingerprints, explains signed updates and finds backup keys stored beside backups.

> **Synthetic case.** Examples are synthetic.

### Errors and limits

Storing keys beside encrypted data defeats the encryption.

### Exercises

- **EX055 — Symmetric use.** Why is symmetric encryption used for bulk data? *Rubric:* 3 = it is fast;; 2 = correct;; 1 = vague;; 0 = none.
- **EX056 — Hash property.** What happens when one input bit changes? *Rubric:* 3 = the fingerprint changes completely;; 2 = correct;; 1 = vague;; 0 = none.
- **EX057 — Backup key.** Where was the backup key stored? *Rubric:* 3 = in the same folder as backups;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Security awareness

### Learning outcomes

You will (1) design awareness activities for staff; (2) encourage reporting; (3) measure awareness outcomes.

### 20.1 Why awareness

Many incidents begin with a person: clicking a phishing link, sending data to the wrong recipient or sharing a password. Aisha learns that awareness programmes help staff recognise and respond to threats. ISO/IEC 27002:2022 includes awareness, education and training among its people controls. Dr. Carrow warns that awareness is not about blaming staff, and that systems should be designed so that a single mistake does not cause serious harm. She reads examples of awareness programmes that improved reporting without blaming those who clicked.

### 20.2 Designing activities

Aisha designs a programme for Ashfield: a short annual course, monthly two-minute tips by email, simulated phishing exercises and branch discussions of real fraud attempts with personal details removed. She tailors content to roles. Tellers learn to spot social engineering by phone; finance staff learn about fake payment requests. She keeps sessions short, because long annual sessions are quickly forgotten. She tests the first monthly tip with five staff members, who say it is clear and takes under two minutes to read. The IT manager approves the programme for the coming year.

### 20.3 Encouraging reporting

Reporting matters more than never clicking. Aisha recommends a report button in email and a simple phone number for branch staff. Every report receives a thank-you, even if the message was harmless. When one teller reports a suspicious call, the IT manager discovers several branches received the same call. Dr. Carrow explains that staff who fear blame stop reporting, which removes one of the organisation's best detection sources. The IT manager blocks the caller's number and warns all branches within the hour.

### 20.4 Measuring outcomes

Aisha proposes measures: training completion, the share of simulated phishing emails reported and the time to first report of real suspicious emails. She avoids using click rates alone, because they depend on how hard each simulation is. She plans to track trends over a year. She learns that awareness outcomes are best measured by behaviour, especially reporting, rather than by attendance alone. She sets up a simple spreadsheet to track the three measures monthly, and the IT manager agrees to include the results in the quarterly board report.

### Worked example

Aisha designs role-based awareness with short sessions, makes reporting easy and thanked, uses a reported call to detect a wider campaign and measures behaviour.

> **Synthetic case.** The programme is synthetic.

### Errors and limits

Blaming staff for clicks discourages the reporting that detects attacks.

### Exercises

- **EX058 — Teller topic.** What do tellers learn to spot? *Rubric:* 3 = social engineering by phone;; 2 = correct;; 1 = other;; 0 = none.
- **EX059 — Report value.** What did one teller's report reveal? *Rubric:* 3 = several branches received the same call;; 2 = correct;; 1 = vague;; 0 = none.
- **EX060 — Click caution.** Why avoid click rates alone? *Rubric:* 3 = they depend on simulation difficulty;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Vulnerability management

### Learning outcomes

You will (1) describe the vulnerability management cycle; (2) measure findings against remediation targets; (3) prioritise fixes by severity and exposure.

### 21.1 The cycle

In her third year, Aisha studies vulnerability management: finding weaknesses, assessing them, fixing them and checking the fixes. Ashfield runs a monthly scan of its computers and servers, which produces a list of findings with severity ratings. Its standard sets remediation targets: critical findings within fourteen days, high within thirty and medium within ninety. Dr. Carrow explains that scanning without fixing achieves nothing, so the cycle must be measured at the fixing stage, not only at the finding stage. Aisha reviews the latest scan.

### 21.2 The vulnerability lab

The lab builds a synthetic list of 400 open findings with severity and age in days. Of 29 critical findings, five are older than fourteen days, 17.2 percent. Of 103 high findings, 27 are overdue against thirty days, 26.2 percent. Of 268 medium findings, 57 are overdue against ninety days, 21.3 percent. Overall, 89 of 400 findings are overdue. Aisha notes that the five overdue critical findings deserve attention first, even though high findings have the largest overdue share. She shows the IT manager a table of overdue findings by severity, with the five critical items listed by system and age, so he can assign them to staff the same day.

### Lab — Overdue vulnerability findings against remediation targets

```python
"""Find vulnerability findings overdue against remediation targets (stdlib only)."""
import random
from collections import Counter
random.seed(21)
target = {"critical": 14, "high": 30, "medium": 90}
finds = []
for _ in range(400):
    sev = random.choices(["critical", "high", "medium"], [1, 4, 10])[0]
    finds.append((sev, int(random.expovariate(1 / (target[sev] * 0.7)))))
total = Counter(s for s, _ in finds)
over = Counter(s for s, a in finds if a > target[s])
for s in target:
    print(f"{s}: {total[s]} open, {over[s]} overdue ({over[s]/total[s]:.1%}) against {target[s]} days")
print(f"all: {len(finds)} open, {sum(over.values())} overdue")
```

Run with `python3 lab_vulns.py`. Verified output:

```text
critical: 29 open, 5 overdue (17.2%) against 14 days
high: 103 open, 27 overdue (26.2%) against 30 days
medium: 268 open, 57 overdue (21.3%) against 90 days
all: 400 open, 89 overdue
```

### 21.3 Prioritising

Severity alone is not enough. Aisha adds exposure: whether the system is reachable from the internet and whether the vulnerability is known to be exploited in real attacks. Two of the five overdue critical findings are on the online banking server, which faces the internet, so they come first. The others are on internal systems. She learns that combining severity, exposure and evidence of real-world exploitation gives a better order of work than severity ratings alone. She records the order and her reasons in a short note for the IT manager.

### 21.4 Causes of delay

Aisha asks why findings become overdue. Some need a supplier update not yet released; some require downtime that branches resist; some were simply forgotten. For supplier delays, she recommends temporary measures such as restricting access to the affected service. For downtime, she proposes a monthly maintenance window agreed with branch managers. For forgotten items, she suggests a weekly overdue list sent to each owner. Dr. Carrow notes that each cause needs its own remedy. Branch managers accept the maintenance window after seeing the overdue critical findings.

### Worked example

Aisha measures 400 synthetic findings against targets, finds 89 overdue including 5 critical, prioritises internet-facing systems and addresses causes of delay.

> **Synthetic case.** Findings are synthetic; outputs come from lab_vulns.py.

### Errors and limits

Prioritising by severity alone ignores exposure and active exploitation.

### Exercises

- **EX061 — Overdue critical.** How many critical findings are overdue? *Rubric:* 3 = five, 17.2 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX062 — Overdue high.** What share of high findings is overdue? *Rubric:* 3 = 26.2 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX063 — Total overdue.** How many findings are overdue overall? *Rubric:* 3 = 89 of 400;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Secure configuration

### Learning outcomes

You will (1) explain why default settings are risky; (2) apply configuration baselines; (3) check configurations regularly.

### 22.1 Default risks

Systems arrive configured for convenience. Default passwords, unnecessary services and permissive settings help installation but also help attackers. Aisha finds that a synthetic Ashfield branch router still uses its factory administrator password, which is published in the manufacturer's manual. Anyone on the branch network could log in and change its settings. She recommends changing all default passwords during installation as a standard step, recorded in the installation checklist so it cannot be skipped. The IT manager changes the router password the same afternoon and checks the other branch routers.

### 22.2 Baselines

A configuration baseline lists the secure settings every system of a type should have. Aisha drafts a baseline for Ashfield's desktop computers: automatic updates on, disk encryption enabled, screen lock after five minutes, standard user accounts for staff and unnecessary software removed. She bases it on published guidance and adapts it to Ashfield's needs. Dr. Carrow notes that baselines turn security knowledge into repeatable settings that do not depend on each technician's memory. The IT manager reviews the draft and approves it for all new desktop installations.

### 22.3 Checking

Settings drift as people change them for convenience or troubleshooting. Aisha writes a small script that reads synthetic configuration exports and reports which computers differ from the baseline. She finds a handful with screen lock disabled, mostly at one branch where staff found it annoying during busy periods. She discusses this with the branch manager, who agrees to a longer timeout rather than none. She learns that understanding why settings drift helps fix the cause. The script runs monthly and emails the IT manager a short list.

### 22.4 Change control

Configuration changes should be planned, approved and recorded. Aisha finds that Ashfield's IT staff make firewall changes without records, so nobody can later explain why a rule exists. She proposes a simple change log: what changed, why, who approved it and how to reverse it. Dr. Carrow explains that change records also help during incidents, because investigators can quickly see whether a recent change caused a problem or opened a gap. The IT manager adopts the change log the following week and records the reason for each existing rule he can still explain.

### Worked example

Aisha finds a default router password, drafts a desktop baseline, checks drift with a script and introduces a change log for firewall changes.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Default passwords published in manuals give attackers easy access.

### Exercises

- **EX064 — Router problem.** What was wrong with the branch router? *Rubric:* 3 = factory default password;; 2 = correct;; 1 = vague;; 0 = none.
- **EX065 — Baseline item.** Name one desktop baseline setting. *Rubric:* 3 = disk encryption enabled;; 2 = one;; 1 = vague;; 0 = none.
- **EX066 — Screen lock fix.** What compromise is agreed for screen lock? *Rubric:* 3 = a longer timeout;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Logging and monitoring

### Learning outcomes

You will (1) choose which events to log; (2) review logs for suspicious activity; (3) protect logs from tampering.

### 23.1 What to log

Logs record events: logins, failed logins, changes to accounts, access to sensitive records and system errors. Aisha helps Ashfield decide what to log. She asks what questions an investigator would need answered, such as who viewed this member's record last week or who created this account. Each question points to events that must be logged. Dr. Carrow notes that logging everything produces too much to review, while logging too little leaves investigators blind. She lists six investigation questions and the events each requires in a table.

### 23.2 Reviewing logs

Logs only help if someone looks at them. Ashfield is too small for a full-time monitoring team, so Aisha proposes automated alerts for a few high-value events: administrator logins outside working hours, many failed logins on one account and bulk viewing of member records by one staff member. The IT manager reviews alerts each morning. She learns that a short list of meaningful alerts is more effective than a long list nobody reads. The review takes about ten minutes each morning and is recorded in a short log.

### 23.3 A real pattern

In a synthetic review, Aisha finds that one staff account viewed over three hundred member records in an afternoon, far more than usual. Investigation shows the staff member was preparing a legitimate mailing list for an annual meeting, approved by a manager. The alert worked correctly but the activity was authorised. She recommends that bulk tasks be notified in advance, so alerts can be checked quickly and genuine misuse stands out. The operations manager agrees to email IT before any approved bulk task, which takes only a minute and saves investigation time.

### 23.4 Protecting logs

Attackers who gain control often delete logs to hide their actions. Aisha recommends sending logs to a separate system that ordinary administrators cannot alter, and keeping them for a defined period agreed with the compliance officer. She also recommends that clocks on all systems be synchronised, so events from different systems can be put in order. Dr. Carrow notes that logs are evidence, and evidence must be trustworthy. The compliance officer sets a twelve-month retention period, after which the central system deletes old logs automatically, and the IT manager confirms clocks are synchronised.

### Worked example

Aisha chooses events from investigation questions, sets three automated alerts, investigates a bulk-viewing alert that proves authorised and protects logs centrally with synchronised clocks.

> **Synthetic case.** Logs are synthetic.

### Errors and limits

Logs kept only where administrators can alter them are weak evidence.

### Exercises

- **EX067 — Alert events.** Name one automated alert event. *Rubric:* 3 = admin logins outside working hours;; 2 = one;; 1 = vague;; 0 = none.
- **EX068 — Bulk viewing.** Why did one account view many records? *Rubric:* 3 = preparing an approved mailing list;; 2 = correct;; 1 = vague;; 0 = none.
- **EX069 — Clock sync.** Why synchronise clocks? *Rubric:* 3 = to order events across systems;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Incident response

### Learning outcomes

You will (1) describe incident response phases; (2) prepare a response plan; (3) practise response with an exercise.

### 24.1 Phases

Aisha studies incident response phases: preparation, detection and analysis, containment, eradication, recovery and lessons learned. NIST's Cybersecurity Framework 2.0 groups related outcomes under its Respond and Recover functions. At Ashfield, an incident might be a phishing compromise, ransomware, a lost laptop or a staff member misusing access. Dr. Carrow explains that the phases give structure under pressure, when people otherwise act inconsistently or forget important steps. She writes one Ashfield example for each phase in her journal, which helps her see how a phishing compromise would move through detection, containment, recovery and lessons learned.

### 24.2 The plan

Aisha drafts an incident response plan for Ashfield. It defines what counts as an incident, who leads the response, how to contact key people out of hours, when to inform the board, regulators, members and the insurer, and where to find technical procedures. She keeps the main plan to four pages with contact details on the first page. Dr. Carrow notes that plans are used under stress, so brevity and clarity matter. The chief executive approves the plan, and a printed copy is kept at every branch.

### 24.3 Containment decisions

Containment limits damage but can disrupt business. If ransomware is found on a branch computer, disconnecting the branch network stops spread but halts member services there. Aisha writes decision guidance: isolate the affected computer first, then the branch if spread is detected, with the chief executive informed of any branch-level isolation. She learns that agreeing decision rules in advance prevents delay and argument during an incident. She adds a simple flowchart to the plan showing each decision point and who makes it, so the person on duty can follow it quickly even without technical knowledge.

### 24.4 Exercise

Aisha runs a tabletop exercise with Ashfield's managers. The scenario: a finance officer reports an email from the chief executive asking for an urgent payment to a new supplier. Managers discuss their actions. They realise the plan does not say who decides whether to contact the bank to stop a payment. Aisha adds this to the plan. Dr. Carrow notes that exercises find gaps cheaply, before a real incident does. The managers agree to repeat the exercise every year with a different scenario chosen by the IT manager.

### Worked example

Aisha learns response phases, drafts a four-page plan, writes containment decision rules and runs an exercise revealing a missing payment-stop decision.

> **Synthetic case.** Plans and exercises are synthetic.

### Errors and limits

An incident plan that is never exercised usually contains gaps.

### Exercises

- **EX070 — Plan length.** How long is the main plan? *Rubric:* 3 = four pages;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX071 — First containment.** What is isolated first for ransomware? *Rubric:* 3 = the affected computer;; 2 = correct;; 1 = branch;; 0 = none.
- **EX072 — Exercise gap.** What gap did the exercise reveal? *Rubric:* 3 = who decides to contact the bank to stop a payment;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Backup and recovery

### Learning outcomes

You will (1) design backups for different threats; (2) test restores; (3) set recovery objectives with business owners.

### 25.1 Backup design

Backups protect against hardware failure, mistakes and ransomware, but each threat needs different design. Hardware failure needs a copy elsewhere; mistakes need older versions; ransomware needs copies attackers cannot reach or alter. Aisha reviews Ashfield's backups: nightly copies to a storage device in the head office, reachable from the network. She recommends an additional offline or immutable copy, kept away from the head office, so one event cannot destroy everything. The chief executive approves the cost of an additional copy stored with a specialist provider in another town.

### 25.2 Testing restores

A backup is only useful if it can be restored. Aisha asks when Ashfield last restored a full system from backup. Nobody remembers. She organises a test restore of the shared folders to a separate computer and compares file fingerprints with the originals using hashlib. A few files fail because they were open during backup. She recommends scheduling backups when files are closed and testing restores every quarter. The IT manager adds the quarterly restore test to the calendar and records each result with the number of files checked and verified.

### 25.3 Recovery objectives

Aisha works with managers to set recovery objectives. For core banking, they accept losing at most fifteen minutes of transactions and need service back within four hours. For shared folders, losing a day is acceptable and recovery within two days is fine. She learns that objectives come from business needs, not technical preferences, and that they decide backup frequency and the recovery methods needed. The managers sign the agreed objectives, and Aisha checks that current backups can meet them. Core banking backups currently run hourly, so she recommends more frequent copies.

### 25.4 Recovery plan

Aisha writes a recovery plan listing the order of systems to restore, the steps for each and the people responsible. Core banking comes first because members depend on it, followed by email and then shared folders. She notes dependencies: core banking needs the directory service for logins, so that must be restored before it. Dr. Carrow notes that recovery order is often discovered only during a real crisis if not planned. The IT manager walks through the plan with her and adds two missing steps.

### Worked example

Aisha adds an offline copy, tests a restore with fingerprints and finds open-file failures, sets objectives with managers and writes a dependency-aware recovery order.

> **Synthetic case.** Backups are synthetic.

### Errors and limits

Backups reachable from the network can be destroyed by ransomware.

### Exercises

- **EX073 — Missing copy.** What extra backup copy does Aisha recommend? *Rubric:* 3 = offline or immutable copy away from head office;; 2 = correct;; 1 = vague;; 0 = none.
- **EX074 — Restore failures.** Why did some files fail to restore? *Rubric:* 3 = they were open during backup;; 2 = correct;; 1 = vague;; 0 = none.
- **EX075 — Core objectives.** What are core banking's objectives? *Rubric:* 3 = fifteen minutes of data, four hours to restore;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Passwords in practice

### Learning outcomes

You will (1) store passwords safely with salted hashing; (2) check passwords against breached lists; (3) set practical password rules.

### 26.1 Storing passwords

Systems should never store passwords in readable form. Instead, they store a hash produced by a slow function with a random salt, a value unique to each password. Aisha learns that slowness makes guessing expensive for attackers who steal the hashes, and that salts stop attackers from comparing hashes across accounts. Python's hashlib module provides PBKDF2, a standard slow hashing function, which she uses in the laboratory with synthetic passwords. She confirms with the online banking supplier that member passwords are stored as salted hashes.

### 26.2 The password lab

The lab hashes the same password with two different salts and confirms the results differ, which is why identical passwords cannot be spotted from stored hashes. It then checks 300 synthetic member passwords against a small list of known breached passwords and finds six matches, 2.0 percent. The lab uses only a thousand hashing iterations to run quickly in class. Aisha notes that real systems use far more iterations, following current guidance. She explains the results to her seminar group with a printed example of the two hashes.

### Lab — Salted PBKDF2 hashing and a breached-password check on synthetic data

```python
"""Salted PBKDF2 password hashing and a breached-password check on synthetic data (stdlib only)."""
import hashlib, random
random.seed(9)
ITER = 1000  # kept low for a classroom run; real systems use far more iterations
breached = {"password1", "letmein", "qwerty123", "summer2024", "creditunion"}
pool = [f"word{n}-{n*7}" for n in range(1000)] + sorted(breached)
members = [random.choice(pool) if random.random() < 0.97 else random.choice(sorted(breached)) for _ in range(300)]
def h(pw, salt): return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, ITER).hex()
s1, s2 = bytes(16), bytes([1]) + bytes(15)
print("same password, different salts give different hashes:", h("letmein", s1) != h("letmein", s2))
hit = sum(pw in breached for pw in members)
print(f"members {len(members)}; passwords found in breached list {hit} ({hit/len(members):.1%})")
```

Run with `python3 lab_passwords.py`. Verified output:

```text
same password, different salts give different hashes: True
members 300; passwords found in breached list 6 (2.0%)
```

### 26.3 Breached passwords

Passwords that appear in breach lists are the first ones attackers try. Aisha recommends that Ashfield's online banking check new passwords against a breached list and refuse matches, with a clear message explaining why. She notes that checks must happen when passwords are set, because the system cannot read stored passwords later. For the six synthetic matches, she suggests prompting members to change their password at next login. The online banking supplier confirms its system can perform such checks, and Ashfield asks for the feature to be enabled at the next update.

### 26.4 Practical rules

Aisha reviews Ashfield's password rules, which require frequent changes and complex characters. She learns that frequent forced changes often lead to predictable patterns, such as adding a number each time. She recommends longer passphrases, breached-password checks, multi-factor authentication and changes only when compromise is suspected. Dr. Carrow notes that good password rules consider how people actually behave, which links to the principle of psychological acceptability. The IT manager updates Ashfield's password standard accordingly, and the change is announced to staff with a short explanation of why longer passphrases are easier and safer.

### Worked example

Aisha hashes passwords with salted PBKDF2, shows different salts give different hashes, finds 6 of 300 synthetic passwords in a breached list and recommends practical rules.

> **Synthetic case.** Passwords are synthetic; outputs come from lab_passwords.py.

### Errors and limits

Storing passwords without salt lets attackers spot identical passwords.

### Exercises

- **EX076 — Salt purpose.** Why use a unique salt? *Rubric:* 3 = stops comparing hashes across accounts;; 2 = correct;; 1 = vague;; 0 = none.
- **EX077 — Breached matches.** How many synthetic passwords were breached? *Rubric:* 3 = six, 2.0 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX078 — Forced changes.** Why avoid frequent forced changes? *Rubric:* 3 = they lead to predictable patterns;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Suppliers and third parties

### Learning outcomes

You will (1) identify supplier security risks; (2) assess suppliers proportionately; (3) manage supplier access and contracts.

### 27.1 Supplier risk

Ashfield relies on suppliers: a core banking provider, a card processor, an IT support company and a cloud email service. Each has access to Ashfield's data or systems, so their security affects Ashfield's. Aisha lists suppliers with the data they handle and the access they hold. She finds the IT support company has permanent remote access to all servers. Dr. Carrow notes that many breaches begin at a supplier with weaker security than its customer. She records each supplier's access and data in a shared register.

### 27.2 Proportionate assessment

Aisha cannot assess every supplier in depth, so she groups them by risk. Suppliers with access to member data or systems receive a questionnaire and requests for evidence such as certifications. Low-risk suppliers, such as the office cleaning company, receive basic contract terms only. She learns that ISO/IEC 27001 certification can be useful evidence, but only if the certificate's scope covers the services Ashfield uses. She sends questionnaires to the four highest-risk suppliers and records their answers and evidence in the supplier register, noting any gaps for follow-up.

### 27.3 Managing access

Aisha recommends that the IT support company's permanent access be replaced by access enabled only when a support request is approved, logged and disabled afterwards. The company agrees after a short discussion. She also recommends that supplier accounts be reviewed in the quarterly access review alongside staff accounts. She learns that supplier access is often forgotten because suppliers are not on the staff list. The new arrangement is tested during the next support request, which proceeds without delay, and the supplier's account is disabled again when the work is complete.

### 27.4 Contracts and exit

Aisha reviews supplier contracts for security terms: protection of data, incident notification, right to audit and return or deletion of data when the contract ends. Two contracts lack deletion terms. She recommends adding them at renewal. She notes that planning exit matters, because changing suppliers without retrieving and deleting data leaves copies in places Ashfield no longer controls. The head of operations adds deletion terms to the renewal checklist. Aisha also suggests that, when a contract ends, Ashfield should request written confirmation that its data have been deleted.

### Worked example

Aisha lists supplier access, tiers assessments by risk, replaces permanent support access with approved sessions and adds missing deletion terms.

> **Synthetic case.** Suppliers are synthetic.

### Errors and limits

Certification evidence is useful only if its scope covers the services used.

### Exercises

- **EX079 — Permanent access.** Which supplier had permanent remote access? *Rubric:* 3 = the IT support company;; 2 = correct;; 1 = other;; 0 = none.
- **EX080 — Certificate caution.** When is ISO/IEC 27001 certification useful evidence? *Rubric:* 3 = when its scope covers the services used;; 2 = correct;; 1 = vague;; 0 = none.
- **EX081 — Missing terms.** What did two contracts lack? *Rubric:* 3 = data deletion terms;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Physical security

### Learning outcomes

You will (1) protect premises and equipment; (2) secure paper and removable media; (3) consider environmental threats.

### 28.1 Premises

Physical security protects buildings, rooms and equipment. Aisha walks through a synthetic Ashfield branch. The public area is separated from the staff area by a locked door, but the door is propped open on busy days. The server cupboard has a lock, but the key hangs beside it. She recommends a self-closing door and a key safe. Dr. Carrow notes that physical weaknesses often defeat technical controls, because an attacker with physical access can bypass much of the network protection. The branch manager agrees.

### 28.2 Paper and media

Ashfield still handles paper: loan applications, identity copies and printed reports. Aisha finds printed member lists left on a printer overnight. She recommends secure printing, where documents release only when the user is at the printer, and locked confidential waste bins. She also finds unencrypted memory sticks used to move files between branches and recommends encrypted devices or secure file transfer instead. The IT manager orders encrypted memory sticks for the branches and sets the printers to secure release. Staff adjust within a week, and the confidential waste bins are emptied by a certified shredding company.

### 28.3 Equipment

Laptops leave the building. Aisha recommends full-disk encryption, screen locks and a register of who holds each laptop. When a synthetic laptop is reported lost on a train, the IT manager confirms it was encrypted and disables its accounts remotely, so no member data are exposed. She learns that encryption turns a potential data breach into a simple equipment loss, which matters for both members and regulators. The laptop register is updated each time a laptop is issued or returned, and the IT manager checks it every month.

### 28.4 Environment

Physical threats include fire, flood, power loss and overheating. The head office server room sits in a basement. Aisha checks flood risk and finds the building has flooded once in twenty years. She recommends raising equipment off the floor and keeping backups at another site. Dr. Carrow notes that environmental threats are usually low likelihood but high impact, so cheap preventive measures are often worthwhile. The IT manager arranges for the equipment to be moved onto raised racks during the next maintenance window and adds a water sensor to the room.

### Worked example

Aisha finds a propped door and a hanging key, recommends secure printing and encrypted media, shows encryption limits a lost laptop's impact and raises basement equipment.

> **Synthetic case.** Premises are synthetic.

### Errors and limits

A key hanging beside its lock offers no protection.

### Exercises

- **EX082 — Door problem.** What weakens the staff-area door? *Rubric:* 3 = propped open on busy days;; 2 = correct;; 1 = vague;; 0 = none.
- **EX083 — Lost laptop.** Why were no data exposed from the lost laptop? *Rubric:* 3 = it was encrypted;; 2 = correct;; 1 = vague;; 0 = none.
- **EX084 — Basement measure.** What is recommended for basement equipment? *Rubric:* 3 = raise it off the floor;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Measuring security

### Learning outcomes

You will (1) choose meaningful security measures; (2) avoid misleading metrics; (3) report trends to leaders.

### 29.1 Choosing measures

Aisha helps Ashfield choose security measures for the board. She selects measures linked to the top risks: share of critical vulnerabilities fixed within target, leavers removed within one day, staff reporting simulated phishing, backups restored successfully in tests and incidents by type. Each measure has a definition, data source, owner and target. Dr. Carrow notes that measures should help decisions, so each must connect to a risk or objective the board cares about. The board approves the five measures for quarterly reporting.

### 29.2 Misleading metrics

Some metrics mislead. Counting blocked attacks at the firewall produces large numbers that look impressive but say little about risk. Counting training completions shows attendance, not behaviour. Aisha explains these limits to the IT manager and replaces them with measures linked to outcomes. She learns that metrics which always look good or always rise without meaning should be treated with suspicion. The IT manager agrees and removes the firewall count from the board report, keeping it only as an internal operational figure for his team where it still has some value.

### 29.3 Using lab results

Aisha includes results from her earlier labs as baselines: ten active leaver accounts found in the access review, 89 of 400 vulnerability findings overdue and 2.0 percent of synthetic member passwords found in a breached list. She sets targets for each and plans to measure again in six months. She notes that baselines make improvement visible, and that without them nobody can tell whether security is getting better. The IT manager agrees with the targets and assigns each measure an owner who will report progress at the quarterly security meeting.

### 29.4 Reporting trends

Aisha designs a one-page quarterly report for the board: each measure with its current value, target, trend arrow and a short comment. Measures off target include a planned action and owner. The board can see at a glance which risks are improving. Dr. Carrow notes that trends matter more than single values, because a single quarter can be unusual while a trend shows direction. The board chair says the new report takes five minutes to read and gives a clearer picture than the old twelve-page report did.

### Worked example

Aisha links measures to top risks, replaces vanity metrics, uses lab results as baselines and designs a one-page trend report.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Counting blocked attacks looks impressive but says little about risk.

### Exercises

- **EX085 — Vanity metric.** Which metric says little about risk? *Rubric:* 3 = blocked attacks at the firewall;; 2 = correct;; 1 = other;; 0 = none.
- **EX086 — Leaver baseline.** What is the leaver baseline? *Rubric:* 3 = ten active leaver accounts;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX087 — Report format.** What does the board report show for each measure? *Rubric:* 3 = value, target, trend and comment;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Management systems and audit

### Learning outcomes

You will (1) describe an information security management system; (2) prepare for an internal audit; (3) handle audit findings.

### 30.1 Management system

Aisha learns that ISO/IEC 27001:2022 describes an information security management system: a set of policies, processes and responsibilities that an organisation uses to manage information security risks and improve over time. It requires understanding context, leadership commitment, risk assessment and treatment, support, operation, performance evaluation and improvement. Ashfield is not seeking certification, but its board wants to use the structure to organise its work. Aisha maps Ashfield's existing documents to the main clauses and finds that performance evaluation and improvement are the weakest areas.

### 30.2 Internal audit

Aisha joins Ashfield's first internal audit of security, led by an external accountant who audits other areas. They check whether policies are followed, using samples. For access control, they select ten leavers and check whether accounts were disabled within one day. Eight were; two took a week. Dr. Carrow notes that audits test whether practice matches policy, which is different from checking whether a policy exists. The accountant records the result with the names of the two leavers and the dates their accounts were disabled.

### 30.3 Findings

The audit produces four findings: late leaver removal, missing change records, untested recovery for one system and no review of supplier access. Each finding states the requirement, evidence and risk. Aisha helps managers write action plans with owners and dates. She learns that findings are opportunities to improve, and that defensive responses waste time better spent fixing the issues identified. The board reviews the findings and action plans at its next meeting and asks the IT manager to report progress each quarter until all four findings are closed.

### 30.4 Continual improvement

The management system includes continual improvement: lessons from audits, incidents and measures feed back into policies and controls. Aisha suggests a quarterly security meeting where the IT manager, compliance officer and head of operations review measures, findings and incidents, and decide actions. Dr. Carrow explains that this cycle, plan, do, check and act, keeps security responsive to change rather than frozen at the moment policies were written. The first meeting takes an hour and produces five actions, each with an owner and date.

### Worked example

Aisha studies ISO/IEC 27001's management system structure, joins an internal audit finding late leaver removal, helps plan actions and sets a quarterly review meeting.

> **Synthetic case.** The audit is synthetic.

### Errors and limits

Checking that a policy exists is not the same as checking it is followed.

### Exercises

- **EX088 — Sample result.** How many sampled leavers were removed within a day? *Rubric:* 3 = eight of ten;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX089 — Audit finding.** Name one audit finding. *Rubric:* 3 = no review of supplier access;; 2 = one;; 1 = vague;; 0 = none.
- **EX090 — Improvement cycle.** What cycle keeps security responsive? *Rubric:* 3 = plan, do, check, act;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-31"></a>

## Chapter 31 — Change management

### Learning outcomes

You will (1) plan security changes that affect people; (2) communicate and support change; (3) measure adoption.

### 31.1 Security changes affect people

In her final year, Aisha studies how security changes succeed or fail. Ashfield plans to introduce app-based multi-factor authentication for all staff remote access. Technically simple, the change affects how every staff member works from home. Dr. Carrow explains that many security projects fail not because the technology is wrong but because people were surprised, unsupported or unconvinced. Aisha's task is to plan the change so staff understand it, can use it and do not look for workarounds. She starts by interviewing five staff.

### 31.2 Planning communication

Aisha plans communication in stages. First, the chief executive explains why the change matters, using a real example of a credit union whose staff accounts were compromised. Then staff receive step-by-step guides with screenshots and a date for enrolment. Branch champions, one per branch, help colleagues set up their phones. She learns that messages from leaders carry weight, while help from colleagues builds confidence in using the new method. She writes the guides herself and tests them with two staff members who have never used an authenticator app, revising unclear steps.

### 31.3 Supporting people

Some staff do not have smartphones or do not want work apps on personal devices. Aisha recommends hardware tokens for them, provided by Ashfield. She also arranges drop-in sessions in each branch during the enrolment week. The IT manager prepares answers to common questions. She learns that offering alternatives prevents a minority from being excluded and reduces resistance, because staff who feel forced into something often find ways around it. The IT manager orders twenty tokens, and seven staff choose them during enrolment, mostly older staff and two who prefer to keep work off personal phones.

### 31.4 Measuring adoption

Aisha tracks enrolment daily during the rollout. After two weeks, most staff are enrolled, but one branch lags. She discovers the branch champion was on holiday. Another staff member steps in, and enrolment completes the next week. On the switch-over date, remote access without a second factor stops. Support calls peak on the first day and fall quickly. She learns that measuring adoption reveals local problems early. She plots enrolment by branch each day on a simple chart shared with branch managers, which makes the lagging branch obvious and encourages friendly competition between the others.

### Worked example

Aisha plans a multi-factor change with leader messages, guides and branch champions, provides hardware tokens as an alternative and tracks enrolment to find a lagging branch.

> **Synthetic case.** The rollout is synthetic.

### Errors and limits

Changes that surprise staff often produce workarounds.

### Exercises

- **EX091 — Leader message.** Who explains why the change matters? *Rubric:* 3 = the chief executive;; 2 = correct;; 1 = other;; 0 = none.
- **EX092 — Alternative method.** What is offered to staff without suitable phones? *Rubric:* 3 = hardware tokens;; 2 = correct;; 1 = other;; 0 = none.
- **EX093 — Lagging branch.** Why did one branch lag? *Rubric:* 3 = its champion was on holiday;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-32"></a>

## Chapter 32 — Business case

### Learning outcomes

You will (1) build a business case for a security investment; (2) estimate costs and benefits; (3) present options to decision-makers.

### 32.1 The need

Ashfield's board asks whether it should buy a managed detection service, which monitors systems around the clock. Aisha prepares a business case. She starts with the problem: the IT manager reviews alerts only on weekday mornings, so an attack beginning on Friday evening could run unnoticed until Monday. She uses the risk register to show that ransomware and account compromise are top risks, both of which spread quickly when unnoticed. She also lists two weekend incidents from the previous year that were found only on Monday mornings.

### 32.2 Costs and benefits

Aisha estimates costs: the annual service fee, setup work and staff time to respond to alerts. For benefits, she estimates how much faster attacks would be detected and what damage that might prevent, using the impact ratings from the risk register. She is careful to present benefits as ranges with stated assumptions, not as precise savings. Dr. Carrow notes that security benefits are uncertain, so honesty about assumptions builds trust. She shows the board a simple table with low, middle and high estimates, and lists the assumptions beneath it in plain language.

### 32.3 Options

Aisha presents three options: do nothing, extend the IT manager's hours with an on-call rota, or buy the managed service. Doing nothing costs least but leaves weekends unmonitored. The on-call rota is cheaper than the service but would exhaust two IT staff. The managed service costs most but provides continuous monitoring and specialist analysts. She recommends the managed service with a one-year trial and clear performance measures. She sets measures for the trial, such as time from alert to Ashfield being notified, and a monthly report from the provider to the IT manager.

### 32.4 Presenting

Aisha presents the business case to the board in fifteen minutes. She leads with the problem and the recommendation, then shows options, costs and risks. A board member asks what happens if the provider misses an attack. She explains the contract terms and the monthly review of alerts and responses. The board approves a one-year trial. She learns that business cases succeed when they connect security to outcomes the board values. After the meeting, the chair asks her to present the trial results to the board in a year.

### Worked example

Aisha builds a business case for managed detection, estimates costs and ranged benefits, compares three options and wins approval for a one-year trial.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Presenting uncertain benefits as precise savings damages credibility.

### Exercises

- **EX094 — Weekend gap.** Why could weekend attacks go unnoticed? *Rubric:* 3 = alerts reviewed only weekday mornings;; 2 = correct;; 1 = vague;; 0 = none.
- **EX095 — Rota drawback.** What is the drawback of the on-call rota? *Rubric:* 3 = it would exhaust two IT staff;; 2 = correct;; 1 = vague;; 0 = none.
- **EX096 — Board decision.** What does the board approve? *Rubric:* 3 = a one-year trial;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-33"></a>

## Chapter 33 — Group project I: plan

### Learning outcomes

You will (1) plan a team security project; (2) divide work fairly; (3) manage risks to the project.

### 33.1 The project

Aisha's group project, with three classmates, is to design a security awareness campaign for Ashfield's members, focused on avoiding fraud. The client, Ashfield's marketing manager, wants members to recognise scam calls and messages claiming to be from Ashfield. The group must deliver campaign materials, a delivery plan and a way to measure impact within ten weeks. Dr. Carrow supervises and meets the group fortnightly. The group meets the marketing manager in the first week to agree the scope, the deliverables and how often they will report progress, and records the agreement in a one-page project charter.

### 33.2 Understanding members

The group starts by understanding members. Using synthetic data, they find that many members are older, many use online banking but some rely on branch visits and phone calls. Fraud reports show scammers impersonating Ashfield staff by phone, asking for one-time codes. The group decides the core message: Ashfield will never ask for your code. They choose formats suited to different members: posters, leaflets, emails and short branch conversations. They also interview six members in a branch, who confirm that scam calls sound convincing and that members feel embarrassed to report being fooled.

### 33.3 Dividing work

The group divides work by strength: one member designs materials, one plans delivery, one designs measurement and Aisha coordinates and writes the final report. They agree weekly check-ins and a shared task list. Dr. Carrow warns that coordination roles can become invisible, so Aisha also takes on the member interviews. The group writes a short agreement on deadlines and how to raise problems. The agreement also states what happens if someone misses a deadline: the group discusses it at the next check-in, and if it repeats, they raise it with Dr. Carrow together.

### 33.4 Project risks

The group lists project risks: the client may be slow to approve materials, members may not respond to interview requests and one teammate has a part-time job limiting availability. They plan responses: early drafts sent to the client, interviews arranged through branch staff and work scheduled around the teammate's shifts. Aisha learns that projects need their own risk management, just like the systems they protect. They record each risk with its owner and response in their shared task list, and review the list at every weekly check-in to see whether any has become more likely.

### Worked example

Aisha's group plans a member fraud awareness campaign, finds code-request scams, sets the core message, divides work and plans for project risks.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Coordination work can become invisible in group projects.

### Exercises

- **EX097 — Core message.** What is the campaign's core message? *Rubric:* 3 = Ashfield will never ask for your code;; 2 = correct;; 1 = vague;; 0 = none.
- **EX098 — Scam method.** How do scammers impersonate Ashfield? *Rubric:* 3 = by phone asking for one-time codes;; 2 = correct;; 1 = vague;; 0 = none.
- **EX099 — Aisha's roles.** What roles does Aisha take? *Rubric:* 3 = coordination, report and member interviews;; 2 = correct;; 1 = some;; 0 = none.

<a id="ch-34"></a>

## Chapter 34 — Group project II: deliver

### Learning outcomes

You will (1) deliver a project to a client; (2) measure campaign impact; (3) reflect on teamwork.

### 34.1 Delivering

The group delivers materials: a poster for branches, a leaflet included with statements, an email to online members and a script for staff to use at counters. The marketing manager approves them after one round of changes, simplifying wording for clarity. The campaign runs for four weeks. Aisha coordinates timing so all formats appear in the same week, reinforcing the message. Branch staff practise the counter script in a short session before the campaign starts, and they report that members respond well when staff mention the message during ordinary conversations about their accounts.

### 34.2 Measuring impact

The measurement plan compares synthetic figures for the four weeks before and after the campaign: member calls to Ashfield reporting suspicious contacts, and fraud losses from code-sharing scams. Reports of suspicious calls rise noticeably, suggesting members recognise scams more often. Losses fall, but the numbers are small. Aisha reports that the evidence is encouraging but cannot prove the campaign caused the change, because scam activity also varies. The group presents both figures with their weeks shown side by side, so the client can see the size of the changes and how small the loss numbers are.

### 34.3 Client feedback

The marketing manager says the campaign was clear and practical, and asks the group to recommend how to repeat it. They suggest an annual campaign with refreshed examples and including the message on the online banking login page permanently. Aisha notes that the client valued the measurement plan most, because it showed a way to judge future campaigns. The group also writes a short guide explaining how Ashfield can repeat the measurement itself next year, using the same weeks and the same definitions, so the results can be compared fairly between campaigns.

### 34.4 Teamwork reflection

Aisha reflects on teamwork. The weekly check-ins kept work on track, but one deadline slipped when the client was ill. The group adjusted by moving the delivery plan earlier. The teammate with a part-time job contributed strongly through flexible scheduling. Dr. Carrow asks each member to write an individual reflection. Aisha notes that clear agreements at the start made later problems easier to solve without conflict. Her reflection also notes that she could have delegated more of the report writing, and she plans to practise this in future teams.

### Worked example

Aisha's group delivers four campaign formats, measures a rise in suspicious-call reports and a small fall in losses, reports limits and reflects on teamwork.

> **Synthetic case.** Results are synthetic.

### Errors and limits

A before-and-after comparison cannot by itself prove a campaign caused a change.

### Exercises

- **EX100 — Campaign formats.** Name one campaign format. *Rubric:* 3 = branch poster;; 2 = one;; 1 = vague;; 0 = none.
- **EX101 — Impact limit.** Why can't the group prove causation? *Rubric:* 3 = scam activity also varies;; 2 = correct;; 1 = vague;; 0 = none.
- **EX102 — Client value.** What did the client value most? *Rubric:* 3 = the measurement plan;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-35"></a>

## Chapter 35 — Placement

### Learning outcomes

You will (1) apply learning in a workplace; (2) handle confidential information; (3) reflect on professional development.

### 35.1 The placement

Aisha spends twelve weeks working in Ashfield's IT team. She helps with daily alert reviews, the quarterly access review and preparation for the managed detection trial. She sees how much of security work involves communication: explaining requests to branch staff, coordinating with suppliers and writing reports. Dr. Carrow visits mid-placement and asks what surprised her. She answers that technical problems were easier than persuading people to change routines. She keeps a weekly diary of tasks and lessons, which she later uses to write her placement reflection.

### 35.2 Confidentiality

During the placement, Aisha sees real member information and real security weaknesses. She signs a confidentiality agreement and keeps her course work based only on synthetic data. When a friend asks about Ashfield's security, she declines to discuss it. She learns that trust in security staff depends on discretion, and that sharing even general weaknesses could help attackers target the organisation. At the end of the placement, she returns her access badge, confirms her accounts are disabled and deletes any work notes stored on her personal devices, as the agreement requires.

### 35.3 Contributions

Aisha contributes a simplified access review procedure, reducing the time the IT manager spends on quarterly reviews by organising data before meetings with owners. She also writes a guide for branch staff on reporting suspicious calls. The IT manager adopts both. She learns that small, practical improvements are often valued more than ambitious proposals that require major investment. The access review procedure cuts the IT manager's preparation time noticeably, because owners receive sorted lists in advance and can confirm most entries before the meeting rather than during it. The reporting guide is pinned in every branch staff room.

### 35.4 Reflection

Aisha's placement reflection notes three lessons: security depends on relationships across the organisation, documentation saves time later and small organisations need simple controls they can sustain. She also notes skills to develop: confidence in presenting to senior managers and deeper knowledge of cloud services. Dr. Carrow suggests she choose a dissertation topic connected to her placement experience. She also writes about a moment when she disagreed with the IT manager about prioritising a finding, and how listening to his reasons about branch workloads changed her view. Dr. Carrow says this kind of reflection shows professional maturity.

### Worked example

Aisha works in Ashfield's IT team, keeps real details confidential, contributes a simpler access review procedure and a reporting guide and reflects on lessons and skills.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Sharing an employer's weaknesses, even casually, can help attackers.

### Exercises

- **EX103 — Placement surprise.** What surprised Aisha most? *Rubric:* 3 = persuading people was harder than technical problems;; 2 = correct;; 1 = vague;; 0 = none.
- **EX104 — Placement contribution.** Name one contribution Aisha made. *Rubric:* 3 = simplified access review procedure;; 2 = one;; 1 = vague;; 0 = none.
- **EX105 — Skill to develop.** Name one skill Aisha wants to develop. *Rubric:* 3 = presenting to senior managers;; 2 = one;; 1 = vague;; 0 = none.

<a id="ch-36"></a>

## Chapter 36 — Research methods

### Learning outcomes

You will (1) frame a research question; (2) choose a suitable design; (3) plan ethical data collection.

### 36.1 Research questions

Aisha learns to frame research questions that can be answered with evidence. Her first idea, whether Ashfield's security is good, is too broad. She narrows it: did introducing an automated leaver process shorten the time leavers' accounts stay active? The question names an intervention, an outcome and a comparison. Dr. Carrow notes that narrow questions produce clear answers, while broad ones produce opinions. She writes the question at the top of every planning document, so each later decision about data and analysis can be checked against it. Dr. Carrow approves the wording.

### 36.2 Designs

Aisha considers designs. A randomised trial is impossible, because the leaver process applies to everyone. A before-and-after comparison is possible: account removal times for leavers in the year before the automated process and the year after. She learns from Shadish, Cook and Campbell's work on quasi-experiments that such comparisons are vulnerable to other changes happening at the same time, such as fewer leavers or a new IT staff member. She lists each rival explanation she can think of and plans a way to check it with available data.

### 36.3 Data and measures

Aisha defines her measure: days between a leaver's last working day, from human resources records, and account disabling, from system logs. She plans to use anonymised records, with Ashfield removing names before sharing. She will report median days and the share disabled within one day. She learns that defining measures precisely before collecting data prevents changing definitions later to get a preferred answer. She also decides how to treat leavers whose last working day is missing from the records: they will be excluded and counted separately, so readers know how many there were.

### 36.4 Ethics

The university ethics committee reviews her plan. Because records concern former staff, it requires anonymisation by Ashfield, storage on university systems only and reporting in aggregate. Aisha agrees. Dr. Carrow notes that even apparently harmless security data can relate to identifiable people, so ethics review protects both participants and researchers. The committee also asks her to explain how she will handle any evidence of misuse she discovers in the logs. She agrees to report it only to Ashfield's IT manager and not to include it in the dissertation, since investigating misuse is not her research purpose. The committee approves the plan with these conditions recorded.

### Worked example

Aisha narrows her question to leaver removal time, chooses a before-and-after design while noting rival changes, defines the measure and gains ethics approval with anonymised data.

> **Synthetic case.** The plan is synthetic.

### Errors and limits

Changing measure definitions after seeing data biases results.

### Exercises

- **EX106 — Research question.** What is Aisha's narrowed question? *Rubric:* 3 = did the automated leaver process shorten removal time;; 2 = correct;; 1 = vague;; 0 = none.
- **EX107 — Design weakness.** What weakens a before-and-after design? *Rubric:* 3 = other changes at the same time;; 2 = correct;; 1 = vague;; 0 = none.
- **EX108 — Ethics condition.** Name one ethics condition. *Rubric:* 3 = anonymisation by Ashfield;; 2 = one;; 1 = vague;; 0 = none.

<a id="ch-37"></a>

## Chapter 37 — Dissertation I: proposal

### Learning outcomes

You will (1) write a dissertation proposal; (2) review relevant literature; (3) plan analysis and timeline.

### 37.1 Proposal structure

Aisha writes her proposal with an introduction stating the problem, a literature review, the research question, design, measures, ethics, analysis plan and timeline. She keeps it to eight pages. Dr. Carrow reviews it and asks her to explain why leaver removal matters, so readers outside security understand the stakes. She adds a paragraph explaining that former staff accounts can be misused by the former employee or by attackers who find them unmonitored. Dr. Carrow approves the proposal after one round of comments.

### 37.2 Literature

Aisha reviews literature on access management. Standards such as ISO/IEC 27002:2022 give guidance on managing access rights, including removal when employment ends. NIST SP 800-53 Revision 5 includes account management controls requiring timely disabling. She finds few published studies measuring removal times in small organisations, which gives her dissertation a modest but real contribution. Dr. Carrow reminds her to cite standards by edition. She also reads Anderson's Security Engineering, which discusses how organisations often struggle to keep access rights aligned with people's current roles. She notes the passage in her literature review as context for why removal delays occur in practice.

### 37.3 Analysis plan

Aisha plans her analysis: compare median days to disable before and after, compare the share disabled within one day and examine any leavers with long delays individually. She will also check for rival explanations, such as changes in leaver numbers or IT staffing. She writes the plan before receiving data, and Dr. Carrow signs it. She learns that a written plan protects her from choosing analyses after seeing results. She stores the signed plan with her ethics approval, so examiners can see it predates the data.

### 37.4 Timeline

Aisha's timeline allocates four weeks for data collection, four for analysis, six for writing and two for revision. She builds in a two-week buffer for delays. Dr. Carrow notes that data access often takes longer than expected in real organisations. She sends the data request to Ashfield early, with the ethics approval attached. Ashfield responds within a week, and the IT manager agrees to provide the anonymised records within a month. Aisha records the request date and the promised delivery date in her project log, so any delay can be explained in the dissertation if needed.

### Worked example

Aisha writes an eight-page proposal, reviews ISO/IEC 27002 and SP 800-53 guidance on access removal, writes an analysis plan before data and builds a timeline with a buffer.

> **Synthetic case.** The proposal is synthetic.

### Errors and limits

Choosing analyses after seeing results invites bias.

### Exercises

- **EX109 — Stakes paragraph.** Why does leaver removal matter? *Rubric:* 3 = former accounts can be misused;; 2 = correct;; 1 = vague;; 0 = none.
- **EX110 — Literature gap.** What gap does Aisha find? *Rubric:* 3 = few studies measuring removal times in small organisations;; 2 = correct;; 1 = vague;; 0 = none.
- **EX111 — Buffer.** How long is the timeline buffer? *Rubric:* 3 = two weeks;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-38"></a>

## Chapter 38 — Dissertation II: findings

### Learning outcomes

You will (1) analyse data according to plan; (2) check rival explanations; (3) report findings with appropriate caution.

### 38.1 Results

Aisha receives anonymised synthetic records for leavers in the year before and after the automated process. Before, the median time to disable was five days, and a quarter of accounts were disabled within one day. After, the median was zero days, with most accounts disabled on the last working day. A few accounts in the after period still took longer, which she examines individually. She presents the results in a table showing medians, the share disabled within one day and the number of leavers in each year, alongside a simple chart of removal times.

### 38.2 Long delays

Aisha investigates the after-period delays. Most involve temporary staff whose end dates were not entered in the human resources system, so the automated process did not trigger. This is a gap in the process, not a failure of automation. She recommends that temporary contracts always include an end date in the system. Dr. Carrow praises her for examining exceptions rather than reporting only the median. She counts the temporary staff cases and lists them by month, which shows they were spread across the year rather than concentrated in one busy period.

### 38.3 Rival explanations

Aisha checks rivals. Leaver numbers were similar in both years. A new IT staff member joined during the after period, which could have improved manual removals too. She examines the removal logs and finds that almost all after-period removals were performed automatically, not manually, which makes the staffing explanation less likely. She reports this check and its limits openly. She also checks whether the type of leavers changed between years, for example more temporary staff in one year, and finds the mix broadly similar. She reports each check in a short table so examiners can see what was examined and what was found.

### 38.4 Cautious conclusions

Aisha concludes that, at Ashfield, introducing the automated leaver process was followed by much faster account removal, with remaining delays concentrated among temporary staff. She does not claim the result applies to all organisations. She notes that one organisation over two years is a small evidence base. Dr. Carrow notes that cautious, well-supported conclusions are worth more than bold claims. She writes the conclusion in a single paragraph and checks that every sentence is supported by a result or a check reported earlier. She removes one sentence that suggested the process would work equally well in larger organisations.

### Worked example

Aisha finds median removal fell from five days to zero, traces remaining delays to missing temporary-staff end dates, checks rival explanations using logs and concludes cautiously.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Reporting only the median hides exceptions that reveal process gaps.

### Exercises

- **EX112 — Median before.** What was the median removal time before? *Rubric:* 3 = five days;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX113 — Delay cause.** What caused most after-period delays? *Rubric:* 3 = missing end dates for temporary staff;; 2 = correct;; 1 = vague;; 0 = none.
- **EX114 — Staffing rival.** How is the staffing rival weakened? *Rubric:* 3 = removals were performed automatically;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-39"></a>

## Chapter 39 — Dissertation III: writing

### Learning outcomes

You will (1) structure a dissertation clearly; (2) write limitations honestly; (3) revise from feedback.

### 39.1 Structure

Aisha structures her dissertation: introduction, literature review, method, results, discussion, limitations, recommendations and conclusion. Each chapter opens with its purpose and closes with a summary. She places her research question on the first page. Dr. Carrow reads a draft and suggests moving the investigation of temporary staff delays into results, since it is a finding, not just discussion. She also adds a short list of abbreviations at the start, because examiners from outside security may not know terms such as multi-factor authentication or access review. A classmate from another subject reads the introduction and confirms it is clear.

### 39.2 Limitations

Aisha writes her limitations specifically: one organisation, a before-and-after design without a comparison group, possible effects of the new IT staff member, and human resources dates that may themselves be late. For each, she explains how it might affect her conclusions. Dr. Carrow notes that specific limitations help readers judge findings, while vague statements such as more research is needed add little. She places the limitations section before the recommendations, so readers consider the limits before reading what she suggests Ashfield should do next.

### 39.3 Recommendations

Aisha separates findings from recommendations. Her recommendations for Ashfield are: require end dates for temporary contracts, review the automated process yearly and include contractor accounts in the same process. For other small organisations, she suggests measuring removal times before and after changes. She labels recommendations as judgements based on evidence, so readers can weigh them. She discusses the recommendations with the IT manager before submission, who confirms they are practical for Ashfield. She records his comments in an appendix, noting that one recommendation, including contractor accounts, will need agreement with suppliers.

### 39.4 Revision

Aisha revises her draft three times. A classmate's review points out unclear terms, and Dr. Carrow's feedback improves the structure. She checks every citation against its source, confirming editions and identifiers. She reads the final version aloud to catch awkward sentences. She learns that revision often improves a dissertation more than additional analysis would. She keeps a revision log listing each change and its reason, which helps her explain decisions in the viva. Dr. Carrow reads the final draft and confirms it is ready for submission, noting that the citations are accurate and complete.

### Worked example

Aisha structures the dissertation, writes four specific limitations, separates recommendations from findings and revises three times, checking every citation.

> **Synthetic case.** The dissertation is synthetic.

### Errors and limits

Vague limitations such as more research is needed add little.

### Exercises

- **EX115 — Moved section.** What is moved into results? *Rubric:* 3 = temporary staff delay investigation;; 2 = correct;; 1 = vague;; 0 = none.
- **EX116 — HR limitation.** What limitation concerns HR dates? *Rubric:* 3 = they may themselves be late;; 2 = correct;; 1 = vague;; 0 = none.
- **EX117 — Revision count.** How many times does Aisha revise? *Rubric:* 3 = three;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-40"></a>

## Chapter 40 — Presentation and viva

### Learning outcomes

You will (1) present research clearly; (2) answer examiner questions; (3) plan next steps after graduation.

### 40.1 Presentation

Aisha prepares a fifteen-minute presentation: problem, question, method, findings, limits and recommendations. She uses simple charts showing removal times before and after. She rehearses with classmates and times each section. Dr. Carrow advises her to state findings exactly as written in the dissertation, avoiding stronger claims under pressure. She keeps each chart simple, with clear labels and the number of leavers shown beside each bar. She prepares answers to likely questions about the design and the temporary staff finding, and practises them aloud with Dr. Carrow, who plays a demanding examiner and asks follow-up questions.

### 40.2 Viva

In the viva, an examiner asks whether the automated process could create new risks. Aisha explains that wrongly entered end dates could disable current staff accounts, and that Ashfield added a confirmation step for early disabling. Another asks why she did not use a comparison organisation. She explains that none was available and that she discusses this limit. The examiners appreciate her clear, honest answers. They also ask how she would extend the study, and she suggests comparing several small organisations over a longer period.

### 40.3 Outcome

Aisha passes with a strong mark. The examiners praise the clear measure, the investigation of exceptions and the honest limitations. Ashfield's IT manager adopts her recommendation on temporary contract end dates. Aisha reflects that her four years connected technical knowledge with governance, communication and research in one practice. Ashfield's chief executive writes to thank her for the work, noting that the recommendation has already been put into practice. Dr. Carrow invites her to speak to next year's students about her dissertation and placement. She agrees and prepares a short talk on choosing a focused question.

### 40.4 Next steps

Aisha accepts a junior security analyst role at a regional building society. She plans to keep learning through professional certifications and to keep a journal as she did at Pennick. Dr. Carrow reminds her that standards change; ISO/IEC 27000, for example, was revised in 2026. The next course in this area, data governance, examines how decisions about data quality and use are made, which complements her security knowledge. She also plans to stay in touch with Dr. Carrow and the Ashfield IT team, who invite her back to see the next access review.

### Worked example

Aisha presents findings, answers viva questions on new risks and comparison groups, passes with a strong mark and plans continued learning.

> **Synthetic case.** The viva is synthetic.

### Errors and limits

Overstating findings under questioning damages credibility.

### Exercises

- **EX118 — New risk.** What new risk could automation create? *Rubric:* 3 = wrong end dates disabling current staff;; 2 = correct;; 1 = vague;; 0 = none.
- **EX119 — Comparison answer.** Why was there no comparison organisation? *Rubric:* 3 = none was available;; 2 = correct;; 1 = vague;; 0 = none.
- **EX120 — Adopted recommendation.** Which recommendation does Ashfield adopt? *Rubric:* 3 = temporary contract end dates;; 2 = correct;; 1 = other;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Aisha Rahimi, Dr. Neil Carrow, Pennick University, Ashfield Credit Union and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Roughly 35,000 members.

**EX002.** Change management, a group project, a placement, research methods and a dissertation.

**EX003.** Recording one security idea each week and its application to Ashfield.

**EX004.** Ensuring timely and reliable access to and use of information.

**EX005.** Integrity.

**EX006.** Accountability.

**EX007.** A credit reference agency.

**EX008.** The shared folders.

**EX009.** Where to spend limited security effort.

**EX010.** An old application once needed it.

**EX011.** Staff postpone restarts.

**EX012.** Through email attachments.

**EX013.** A rule allowing remote desktop access from anywhere.

**EX014.** Data once they reach a compromised server.

**EX015.** It is separated from staff networks.

**EX016.** Accounts with no login for ninety days.

**EX017.** It records them separately instead of crashing.

**EX018.** It points to logins nobody is watching.

**EX019.** 112 of 140 staff, eighty percent.

**EX020.** Fifteen days.

**EX021.** Using incidents per hundred staff.

**EX022.** What the problem is, why it matters, what to do and by whom.

**EX023.** That former employees could still access member records.

**EX024.** Because standards change between editions.

**EX025.** Data protection law.

**EX026.** Signed agreements defining scope and timing.

**EX027.** A right for Ashfield to check the supplier's security.

**EX028.** Proportionality.

**EX029.** Report it privately through the organisation's security contact.

**EX030.** Members travelling or living overseas.

**EX031.** The risk appetite.

**EX032.** Supply chain risk management.

**EX033.** Spending to prevent member data exposure.

**EX034.** The firewall review.

**EX035.** He can both create accounts and approve their access.

**EX036.** Logging administrator actions with a weekly review.

**EX037.** Passwords must be at least fourteen characters.

**EX038.** The password length requirement.

**EX039.** Any mention of cloud storage.

**EX040.** NIST SP 800-30 Revision 1.

**EX041.** Fake payment requests.

**EX042.** Call-back verification to known numbers.

**EX043.** A network storage device in a branch cupboard.

**EX044.** Member identity documents and payment card data.

**EX045.** By linking it to purchasing and disposal with a twice-yearly check.

**EX046.** To view member balances but not approve loans.

**EX047.** It often remains because nobody removes it.

**EX048.** Both IT staff and a supplier.

**EX049.** They cannot be changed if copied.

**EX050.** Through mobile number takeover.

**EX051.** Members stating their date of birth and address.

**EX052.** Ten leaver accounts.

**EX053.** Thirteen current staff.

**EX054.** Six held administrator access.

**EX055.** Because it is fast.

**EX056.** The fingerprint changes completely.

**EX057.** In the same folder as the encrypted backups.

**EX058.** Social engineering by phone.

**EX059.** Several branches received the same suspicious call.

**EX060.** They depend on how hard each simulation is.

**EX061.** Five of 29, 17.2 percent.

**EX062.** 27 of 103, 26.2 percent.

**EX063.** 89 of 400 findings.

**EX064.** It still used its factory administrator password.

**EX065.** Disk encryption enabled.

**EX066.** A longer timeout rather than none.

**EX067.** Administrator logins outside working hours.

**EX068.** The staff member was preparing an approved mailing list.

**EX069.** So events from different systems can be put in order.

**EX070.** Four pages, with contacts on page one.

**EX071.** The affected computer.

**EX072.** Who decides whether to contact the bank to stop a payment.

**EX073.** An offline or immutable copy kept away from head office.

**EX074.** They were open during backup.

**EX075.** At most fifteen minutes of data loss and four hours to restore.

**EX076.** It stops attackers comparing hashes across accounts.

**EX077.** Six of 300, 2.0 percent.

**EX078.** They lead to predictable patterns.

**EX079.** The IT support company.

**EX080.** When its scope covers the services Ashfield uses.

**EX081.** Terms for deleting data at contract end.

**EX082.** It is propped open on busy days.

**EX083.** It was encrypted and its accounts were disabled.

**EX084.** Raising it off the floor and keeping backups elsewhere.

**EX085.** Counting blocked attacks at the firewall.

**EX086.** Ten active leaver accounts.

**EX087.** Current value, target, trend arrow and a comment.

**EX088.** Eight of ten.

**EX089.** No review of supplier access.

**EX090.** Plan, do, check and act.

**EX091.** The chief executive.

**EX092.** Hardware tokens provided by Ashfield.

**EX093.** Its branch champion was on holiday.

**EX094.** Alerts are reviewed only on weekday mornings.

**EX095.** It would exhaust the two IT staff.

**EX096.** A one-year trial of the managed service.

**EX097.** Ashfield will never ask for your code.

**EX098.** By phone, asking for one-time codes.

**EX099.** Coordination, the final report and member interviews.

**EX100.** A branch poster.

**EX101.** Because scam activity also varies over time.

**EX102.** The measurement plan.

**EX103.** Persuading people to change routines was harder than technical problems.

**EX104.** A simplified access review procedure.

**EX105.** Confidence presenting to senior managers.

**EX106.** Whether the automated leaver process shortened the time leavers' accounts stay active.

**EX107.** Other changes happening at the same time.

**EX108.** Anonymisation of records by Ashfield.

**EX109.** Former staff accounts can be misused by ex-employees or attackers.

**EX110.** Few studies measure removal times in small organisations.

**EX111.** Two weeks.

**EX112.** Five days.

**EX113.** Temporary staff without end dates in the HR system.

**EX114.** Logs show almost all removals were automatic.

**EX115.** The investigation of temporary staff delays.

**EX116.** HR dates may themselves be recorded late.

**EX117.** Three times.

**EX118.** Wrongly entered end dates disabling current staff accounts.

**EX119.** None was available.

**EX120.** Requiring end dates for temporary contracts.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. https://doi.org/10.1002/9781119644682
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- National Institute of Standards and Technology. (2004). *Standards for security categorization of federal information and information systems* (FIPS 199). https://doi.org/10.6028/NIST.FIPS.199
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.
