# Identity and Access Management: Bachelor's Degree

- Language: English (`en`); course 102, Bachelor's degree (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduates learning to measure and improve identity and access management in a small organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only identity systems and accounts you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic accounts, entitlements, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one bachelor's student helping a fictional housing association, from mathematical reasoning, systems, programming and writing through identity theory, system models, data and dependencies, lifecycle methods, controls, laboratories, verification, failure analysis and operations, to a comparative project, a capstone proposal, field practice, an evidence seminar, capstone delivery and evaluation, and the thesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Elena Petrova** | Bachelor's student | Invented |
| **Dr Kwame Asante** | Supervisor | Invented |
| **Westmere University** | Fictional university | Invented |
| **Greenhill Community Housing** | Fictional partner (about 140 staff) | Invented |

### Core sources

NIST [SP 800-63-4](https://doi.org/10.6028/NIST.SP.800-63-4), [SP 800-63B-4](https://doi.org/10.6028/NIST.SP.800-63B-4), [SP 800-162](https://doi.org/10.6028/NIST.SP.800-162), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); IETF [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700); [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html); W3C [WebAuthn Level 2](https://www.w3.org/TR/webauthn-2/); OASIS [SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf). Full list in [References](#references).

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

You will (1) reason with percentages and ratios about accounts; (2) read simple tables of identity data; (3) avoid common numerical mistakes.

### 1.1 The case

Elena Petrova is a bachelor's student at the fictional Westmere University, supervised by Dr Kwame Asante. Her four-year project is with the fictional Greenhill Community Housing, a housing association with about 140 staff who use a cloud office suite, a housing management system and a finance system. Greenhill's small IT team worries that some former staff still have accounts, that not everyone uses multi-factor authentication and that a few accounts are shared between colleagues. Elena's job over the degree is to understand these problems, measure them carefully and help fix them, using only synthetic data in this book.

### 1.2 Percentages and ratios

Identity work is full of percentages: the share of staff with multi-factor authentication, the share of leavers disabled on time, the share of accounts never used. A percentage is only meaningful with its base. Saying ninety percent of administrators use multi-factor sounds good, but if there are ten administrators, the one without it may hold the most powerful account in the organisation. Elena learns to always report the count and the base alongside the percentage, such as nine of ten, so readers can judge both the proportion and its real-world size.

### 1.3 Common mistakes

Two mistakes appear often. The first is comparing percentages with different bases: a rise from 50 to 60 percent in a team of ten is one person, while the same rise across 140 staff is fourteen people. The second is confusing percentage points with percent: going from 50 to 60 percent is a rise of ten percentage points but a twenty percent relative increase. Elena writes both clearly in her reports, because managers make decisions from these numbers and an ambiguous figure can lead to the wrong priority.

### Worked example

Of 140 synthetic staff, 108 use multi-factor authentication: 77.1 percent. Elena reports it as 108 of 140 (77.1%) and notes that the 32 without it are concentrated in one team.

> **Synthetic case.** Elena Petrova, Westmere University, Greenhill Community Housing and all figures are synthetic.

### Errors and limits

Reporting a percentage without its base hides whether a gap affects one person or many.

### Exercises

- **EX001 — Base matters.** Why report nine of ten instead of only ninety percent? *Rubric:* 3 = base shows the one missing may be critical;; 2 = base;; 1 = style;; 0 = none.
- **EX002 — Points versus percent.** A rise from 50 to 60 percent is how many points and what relative increase? *Rubric:* 3 = ten points, twenty percent;; 2 = ten points;; 1 = ten percent;; 0 = none.
- **EX003 — Greenhill size.** About how many staff does Greenhill have? *Rubric:* 3 = about 140;; 2 = 140;; 1 = 1,400;; 0 = none.

### Synthesis

Percentages with their bases, and clear use of points versus percent, make identity figures honest and useful.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the systems Greenhill staff use; (2) explain where accounts live; (3) identify which systems hold sensitive data.

### 2.1 Systems at Greenhill

Elena starts by listing the systems staff use. The cloud office suite provides email, documents and calendars, and holds most staff accounts. The housing management system stores tenant records, rent accounts and repair requests. The finance system handles payments and payroll. Smaller tools include a repairs scheduling app used by operatives in vans and a website content tool. For each system she records who supplies it, who looks after it at Greenhill and how staff sign in, because each sign-in method is a place where identity problems can start.

### 2.2 Where accounts live

Some systems use the office suite's accounts directly, so staff sign in once and are recognised everywhere that is connected. Others, such as the older finance system, keep their own separate list of usernames and passwords. Separate account lists are a common source of trouble: when someone leaves, IT may disable their office suite account but forget the finance account. Elena marks each system as connected or separate, and notes this as the first clue to why former staff might still have access to some systems after they leave.

### 2.3 Sensitive data

Not all systems carry the same risk. The housing system holds personal details about tenants, some of them vulnerable, and the finance system can move money. The website tool holds only public content. Elena ranks systems by the harm that misuse could cause, so that later effort goes first to the most sensitive ones. This simple ranking will guide everything from which accounts to review first to where multi-factor authentication matters most, because a small team cannot fix everything at once and must choose carefully.

### Worked example

Elena lists six systems: three connected to the office suite, three with separate accounts; housing and finance are ranked most sensitive.

> **Synthetic case.** Systems and suppliers are synthetic.

### Errors and limits

Assuming every system uses the main office suite account misses separate account lists where leavers remain.

### Exercises

- **EX004 — Separate account risk.** Why are separate account lists risky when staff leave? *Rubric:* 3 = IT may disable the main account but forget separate ones;; 2 = forgotten;; 1 = none;; 0 = none.
- **EX005 — Most sensitive systems.** Which two systems does Elena rank most sensitive? *Rubric:* 3 = housing and finance;; 2 = one;; 1 = website;; 0 = none.
- **EX006 — Connected meaning.** What does connected mean for a system here? *Rubric:* 3 = uses office suite accounts directly;; 2 = shared sign-in;; 1 = networked;; 0 = none.

### Synthesis

Knowing which systems exist, where their accounts live and what data they hold is the start of identity work.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write a simple script to count accounts; (2) read a CSV export; (3) print a clear summary.

### 3.1 Why program

Greenhill's office suite can export a list of accounts as a CSV file, a plain text table with one line per account. Counting by hand in a spreadsheet works once, but the check needs repeating every month. Elena writes a short Python script that reads the export, counts accounts by status and department and prints a summary. Using only the standard library means it runs on any Greenhill laptop without installing anything. Repeating the same script each month gives comparable results, which hand counting rarely does.

### 3.2 Reading data carefully

Real exports contain surprises: blank lines, names with commas, departments typed differently such as Housing and housing. Elena's script trims spaces, treats department names case-insensitively and reports any line it cannot read rather than silently skipping it. She tests the script on a small synthetic file where she knows the right answer before using the real export. If the script and her hand count disagree on the test file, she fixes the script, because a check that gives wrong answers is worse than no check at all.

### 3.3 Clear output

A good summary is easy to read and hard to misread. Elena prints a header with the export date, then a table of departments with total accounts, enabled accounts and accounts with multi-factor authentication, each as a count and a percentage of its base. She saves each month's output with its date so trends can be compared. The script is short, commented and stored in Greenhill's shared IT folder, so another member of the team can run it while Elena is away at university.

### Worked example

Elena's script reads a synthetic export of 152 accounts, reports 140 enabled and 12 disabled, and lists departments with counts and percentages.

> **Synthetic case.** Exports and counts are synthetic.

### Errors and limits

A script that silently skips unreadable lines may undercount exactly the accounts that need attention.

### Exercises

- **EX007 — CSV meaning.** What is a CSV export? *Rubric:* 3 = plain text table, one line per account;; 2 = text table;; 1 = database;; 0 = none.
- **EX008 — Department case issue.** How does Elena handle Housing versus housing? *Rubric:* 3 = compares department names case-insensitively;; 2 = case-insensitive;; 1 = ignores;; 0 = none.
- **EX009 — Enabled count.** How many enabled accounts does the synthetic export show? *Rubric:* 3 = 140 of 152;; 2 = 140;; 1 = 152;; 0 = none.

### Synthesis

A small, tested script makes monthly account checks repeatable and comparable.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear, evidence-based paragraphs; (2) cite sources correctly; (3) separate findings from opinions.

### 4.1 Writing with evidence

Academic writing makes claims and supports them with evidence. Elena practises paragraphs that state one point, give the evidence and explain what it means. For example: thirty-two of 140 Greenhill staff do not use multi-factor authentication, according to the March export; most are in the repairs team, who mainly sign in on shared tablets; this suggests the barrier is the device setup rather than staff reluctance. Each sentence has a job, and the reader can see where each claim comes from and how strong it is.

### 4.2 Citing sources

When Elena uses published guidance she cites it so readers can check it. She refers to NIST SP 800-63B-4, which sets out current guidance on authenticators, rather than to a blog summary of it. Each citation in her text matches a full entry in the reference list, with authors, year, title and a working link or DOI. She checks that the source actually says what she claims, because citing a document for a point it does not make is a serious academic error and also misleads practitioners.

### 4.3 Findings versus opinions

Elena separates what she observed from what she thinks it means. Findings are counts, dates and quotations from interviews; interpretations are her explanations, which may be wrong. She marks interpretations with words such as suggests or may, and offers alternatives where they exist. Recommendations come last and follow from the findings. This structure helps her supervisor and Greenhill's managers trust her reports, because they can agree with the facts even if they weigh the interpretation differently. Her supervisor checks this separation in every draft she submits.

### Worked example

Elena rewrites a vague paragraph claiming staff dislike multi-factor into one citing the March export, locating the gap in the repairs team and suggesting a device explanation.

> **Synthetic case.** Paragraphs and exports are synthetic; NIST SP 800-63B-4 is a real source.

### Errors and limits

Citing a summary instead of the original guidance risks repeating someone else's misreading.

### Exercises

- **EX010 — Paragraph parts.** What three things does a good evidence paragraph contain? *Rubric:* 3 = point, evidence, meaning;; 2 = two;; 1 = one;; 0 = none.
- **EX011 — Original source.** Which original source does Elena cite on authenticators? *Rubric:* 3 = NIST SP 800-63B-4;; 2 = NIST;; 1 = a blog;; 0 = none.
- **EX012 — Interpretation words.** How does Elena mark interpretations? *Rubric:* 3 = words like suggests or may;; 2 = hedging;; 1 = bold;; 0 = none.

### Synthesis

Clear evidence-based paragraphs, correct citations and separating findings from opinions make writing trustworthy.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain what identity and access management protects; (2) describe common identity threats; (3) recognise good basic practice.

### 5.1 What IAM protects

Identity and access management decides who people are when they sign in and what they are allowed to do. At Greenhill, it protects tenant records from people who should not see them, money in the finance system from misuse and staff email from being taken over. Good IAM means the right people get the right access at the right time, and lose it when they no longer need it. Elena explains this to Greenhill staff using everyday comparisons, such as building keys returned when someone leaves.

### 5.2 Common threats

The most common identity threats are simple. Passwords are guessed, reused from other websites or captured by fake sign-in pages. Accounts of former staff stay active and can be misused. Shared accounts make it impossible to know who did what. And people sometimes have far more access than their job needs, so a mistake or a compromised account causes more harm. Elena keeps her explanations defensive: she describes what can go wrong and how to prevent it, not how anyone would carry out an attack.

### 5.3 Good basic practice

Basic good practice covers a lot of risk. Multi-factor authentication makes a stolen password much less useful. Disabling accounts promptly when people leave closes a common gap. Giving everyone their own account keeps actions traceable. Granting access by job and reviewing it regularly limits harm. Using a password manager helps staff create long, unique passwords. NIST SP 800-63B-4 also advises against forcing regular password changes without reason, because they push people towards predictable patterns, which surprises some Greenhill managers. Each practice is explained with a short reason staff can remember.

### Worked example

Elena's one-page explainer lists four common identity threats at Greenhill and five basic practices, each in plain language with a building-key comparison.

> **Synthetic case.** The explainer and examples are synthetic.

### Errors and limits

Explaining threats by describing attack steps rather than prevention is unnecessary for defenders and unsafe to share.

### Exercises

- **EX013 — IAM definition.** What does IAM decide? *Rubric:* 3 = who people are and what they may do;; 2 = identity and access;; 1 = passwords only;; 0 = none.
- **EX014 — Shared account harm.** Why are shared accounts a problem? *Rubric:* 3 = cannot tell who did what;; 2 = traceability;; 1 = speed;; 0 = none.
- **EX015 — Forced changes advice.** What does NIST advise about regular forced password changes? *Rubric:* 3 = avoid them without reason, they encourage predictable patterns;; 2 = avoid;; 1 = require;; 0 = none.

### Synthesis

IAM protects people, data and money by giving the right access at the right time and removing it when no longer needed.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) describe users, groups and permissions as sets; (2) use set operations to compare lists; (3) draw relations as tables.

### 6.1 Sets of accounts

A set is a collection of distinct items. Greenhill's current staff from HR form one set; enabled accounts in the office suite form another. Comparing the two sets answers practical questions. Accounts in the second set but not the first belong to nobody currently employed, which may mean leavers. Staff in the first set but not the second may be new starters waiting for an account. Elena uses set difference, a basic operation, to turn a vague worry about leftover accounts into a precise list to check.

### 6.2 Groups and permissions

Access is often given through groups: everyone in the housing-officers group can open tenant records. Each group is a set of users, and each permission is linked to groups. A person's access is the union of the permissions of all their groups. When someone is in several groups, their combined access can be more than anyone intended. Elena writes groups and their permissions as a simple table, then computes each person's combined access so it can be compared with what their job requires.

### 6.3 Relations as tables

A relation connects items from two sets, such as which users belong to which groups. Writing it as a table, with users as rows and groups as columns and a mark where a user belongs, makes patterns easy to see. A row with many marks may be a person who has collected access over years. A column with very few marks may be a group nobody uses. Elena finds such tables easier to discuss with managers than lists, because managers can quickly spot what looks wrong for their team.

### Worked example

In a January export, set difference between 140 synthetic HR staff and 147 enabled accounts finds seven accounts with no current employee and none missing.

> **Synthetic case.** Staff, accounts and groups are synthetic.

### Errors and limits

Reviewing group names without computing each person's combined access misses access gathered through several groups.

### Exercises

- **EX016 — Leftover accounts.** Which set operation finds accounts with no current employee? *Rubric:* 3 = enabled accounts minus HR staff;; 2 = difference;; 1 = union;; 0 = none.
- **EX017 — Combined access.** How is a person's access computed from groups? *Rubric:* 3 = union of their groups' permissions;; 2 = union;; 1 = intersection;; 0 = none.
- **EX018 — Leftover count.** How many accounts with no current employee does the worked example find? *Rubric:* 3 = seven;; 2 = 7;; 1 = none;; 0 = none.

### Synthesis

Sets, unions and relation tables turn account and group lists into clear questions about access.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain how sign-in travels over the internet; (2) describe HTTPS and why it matters; (3) recognise fake sign-in pages.

### 7.1 Signing in over the internet

When a Greenhill employee signs in to the office suite, the browser sends their username and authentication to the provider's servers across the internet. HTTPS protects this traffic using TLS, which encrypts it and confirms the server's identity through a certificate. Without HTTPS, anyone on the same network, such as public Wi-Fi in a café, could read passwords. Elena checks that every system Greenhill uses for sign-in uses HTTPS, and finds that all do, including the older finance system after a recent upgrade.

### 7.2 Single sign-on

Some Greenhill systems trust the office suite to sign staff in. The browser is sent to the office suite's sign-in page, the user signs in there and is sent back to the system with a signed message saying who they are. Standards such as SAML 2.0 and OpenID Connect describe how these messages work. The benefit for Greenhill is one place to sign in, enforce multi-factor authentication and disable access, rather than a separate password for each system that must be managed and removed separately.

### 7.3 Fake sign-in pages

Attackers create pages that look like the real sign-in page to capture what people type. Staff are taught to check the address bar, but that is unreliable under pressure. Stronger protection comes from authenticators that only work with the real site, such as passkeys based on the W3C WebAuthn standard, which will not respond to a look-alike address. Elena explains this to Greenhill managers as the reason to prefer passkeys or security keys over codes typed from a phone, especially for finance and administrator accounts.

### Worked example

Elena confirms HTTPS on all six systems and identifies three that could use the office suite for single sign-on, reducing separate passwords.

> **Synthetic case.** Systems and findings are synthetic; SAML 2.0, OpenID Connect and WebAuthn are real standards.

### Errors and limits

Relying only on staff spotting fake addresses ignores how convincing look-alike pages can be under time pressure.

### Exercises

- **EX019 — HTTPS role.** What does HTTPS do for sign-in? *Rubric:* 3 = encrypts traffic and confirms server identity;; 2 = encrypts;; 1 = speeds up;; 0 = none.
- **EX020 — SSO benefit.** What is Greenhill's main benefit from single sign-on? *Rubric:* 3 = one place to sign in, enforce MFA and disable access;; 2 = central control;; 1 = none;; 0 = none.
- **EX021 — Fake page defence.** Which authenticators resist fake sign-in pages? *Rubric:* 3 = site-bound passkeys or security keys (WebAuthn);; 2 = passkeys;; 1 = SMS codes;; 0 = none.

### Synthesis

HTTPS protects sign-in traffic, single sign-on centralises control, and site-bound authenticators resist fake pages.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) build a larger script with functions and tests; (2) combine two data sources; (3) produce a monthly identity report.

### 8.1 Combining sources

Elena's second-year script combines the HR staff list with the office suite export. Each source names people differently: HR uses employee numbers, the office suite uses email addresses. She writes a function to match them using a mapping table maintained by HR, and reports any person who cannot be matched. Combining sources is where many identity checks go wrong, because a mismatch in naming can make a current employee look like a leaver or hide a real leaver behind a slightly different spelling.

### 8.2 Functions and tests

The script is organised into functions: read HR, read accounts, match, analyse and report. Each has tests using small synthetic files where Elena knows the right answer, including awkward cases such as a person who changed surname and an account with capital letters in the email. Tests run before each monthly use. When Greenhill changes its export format, a failing test warns Elena immediately, instead of the report quietly producing wrong numbers that someone might act on. New awkward cases are added as tests whenever they appear in real data.

### 8.3 The monthly report

The report lists accounts without a current employee, staff without multi-factor authentication by team, accounts unused for ninety days and administrator accounts. Each list includes counts and percentages with bases, and the report header gives export dates and script version. Elena sends it to the IT lead, who decides actions. She avoids changing accounts herself: her role is to provide accurate evidence. The report becomes the baseline against which later improvements are measured during her capstone. Each month's report is stored with the previous ones for comparison.

### Worked example

The combined script matches 138 of 140 staff automatically; two unmatched names are resolved with HR, one a surname change and one a typo.

> **Synthetic case.** Sources, names and counts are synthetic.

### Errors and limits

Matching people by display name instead of a stable identifier mistakes surname changes for leavers.

### Exercises

- **EX022 — Matching key.** How does Elena match HR records to accounts? *Rubric:* 3 = mapping table from employee number to email;; 2 = mapping;; 1 = names;; 0 = none.
- **EX023 — Unmatched causes.** What caused the two unmatched names? *Rubric:* 3 = surname change and a typo;; 2 = two causes;; 1 = leavers;; 0 = none.
- **EX024 — Elena's role.** Why does Elena not change accounts herself? *Rubric:* 3 = her role is evidence; IT lead decides actions;; 2 = evidence only;; 1 = no time;; 0 = none.

### Synthesis

Carefully matched sources, tested functions and a clear monthly report make identity evidence dependable.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) store identity data in a simple database; (2) write queries for common questions; (3) protect personal data in the store.

### 9.1 A simple database

Monthly CSV files become hard to compare over time, so Elena loads them into a small SQLite database, which Python's standard library supports. Tables hold staff, accounts, group memberships and monthly snapshots, each with a date. Storing snapshots allows questions such as how many leavers were disabled within a day in each month. The structure is documented with a short description of every table and column, so anyone at Greenhill can understand what is stored and why. Each snapshot records the export file it came from.

### 9.2 Queries

Queries answer questions directly. Which enabled accounts have not signed in for ninety days? Which staff are in more than five groups? How many leavers in March were disabled after their leaving date? Elena writes each query with a clear time window, checks its results against a small sample by hand and saves it with a description. Saved queries mean the same question gets the same method every month, which makes trends trustworthy rather than an artefact of how someone happened to ask.

### 9.3 Protecting the data

The database contains names, departments and sign-in dates, which is personal data. Elena stores it on an encrypted Greenhill drive with access limited to the IT team, keeps only the fields her checks need and deletes snapshots older than two years, as agreed with Greenhill's data protection lead. She never copies it to her personal devices. Handling identity data carefully is part of being trusted to work with it, and it is also a legal duty under data protection law.

### Worked example

The SQLite store holds twelve monthly snapshots; a saved query finds nine synthetic enabled accounts unused for ninety days.

> **Synthetic case.** Tables, snapshots and counts are synthetic.

### Errors and limits

Keeping every field from every export forever creates a growing store of personal data with no purpose.

### Exercises

- **EX025 — Snapshot value.** Why store dated snapshots? *Rubric:* 3 = compare months and measure trends;; 2 = trends;; 1 = backup;; 0 = none.
- **EX026 — Unused query result.** How many enabled accounts are unused for ninety days in the worked example? *Rubric:* 3 = nine;; 2 = 9;; 1 = none;; 0 = none.
- **EX027 — Retention agreed.** How long are snapshots kept? *Rubric:* 3 = two years, agreed with data protection lead;; 2 = two years;; 1 = forever;; 0 = none.

### Synthesis

A documented database, saved queries and careful data protection make identity trends reliable and lawful.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) work only within written permission; (2) handle colleagues' data respectfully; (3) raise concerns appropriately.

### 10.1 Written permission

Before any identity work at Greenhill, Elena receives a written agreement from the chief executive and IT lead stating what she may do: receive exports, analyse them, interview staff and recommend changes. It excludes signing in to systems as an administrator, testing passwords or trying to get around any control. If a task seems to need more, she stops and asks. Working only within written permission protects Greenhill, protects Elena legally and keeps the trust that makes the placement possible.

### 10.2 Respect for colleagues

Identity data is about colleagues: when they work, what they can access and sometimes mistakes they made. Elena uses it only for agreed purposes. She does not comment on individuals' sign-in times or share findings about named people beyond those who need to act. When she finds a manager with excessive access, she reports it to the IT lead factually, without blame, because most excess access builds up through ordinary job changes rather than bad intent. She also avoids discussing findings about named people outside agreed meetings.

### 10.3 Raising concerns

Sometimes Elena finds something serious, such as a former employee's account that signed in after they left. Her agreement sets out what to do: report immediately to the IT lead and her supervisor, preserve the evidence and take no further action herself. She does not investigate on her own or confront anyone. Clear escalation routes mean serious issues reach the right people quickly, and students are protected from situations beyond their role and authority. Her supervisor reviews the escalation steps with her at the start of the placement.

### Worked example

Elena finds a synthetic leaver account with a sign-in after the leaving date, reports it to the IT lead and supervisor the same day and preserves the export.

> **Synthetic case.** The agreement, findings and people are synthetic.

### Errors and limits

Investigating a suspicious sign-in alone, beyond the agreed role, can damage evidence and exceed authority.

### Exercises

- **EX028 — Excluded actions.** Name two actions Elena's agreement excludes. *Rubric:* 3 = admin sign-in, password testing, bypass attempts (two);; 2 = one;; 1 = none;; 0 = none.
- **EX029 — Excess access tone.** How does Elena report a manager's excess access? *Rubric:* 3 = factually, without blame;; 2 = neutral;; 1 = publicly;; 0 = none.
- **EX030 — Suspicious sign-in steps.** What should Elena do about a leaver's post-departure sign-in? *Rubric:* 3 = report to IT lead and supervisor, preserve evidence, act no further;; 2 = report;; 1 = investigate;; 0 = none.

### Synthesis

Written permission, respect for colleagues and clear escalation keep identity work ethical and safe.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain user and administrator accounts on laptops; (2) describe local accounts and device sign-in; (3) reduce unnecessary admin rights.

### 11.1 Users and administrators

Operating systems separate standard users from administrators. Administrators can install software and change security settings; standard users cannot. If a member of staff works all day as an administrator, any harmful file they open gets administrator power too. At Greenhill, Elena finds that about a third of laptops let their main user act as an administrator, mostly for historical reasons. She recommends standard accounts for daily work, with a simple request process when someone genuinely needs software installed. Requests are logged and reviewed monthly.

### 11.2 Device sign-in

Greenhill laptops are joined to the office suite's device management, so staff sign in with their work accounts. This means disabling a leaver's account stops them signing in to any managed laptop. Elena checks for laptops not enrolled in device management, finding four older machines with only local accounts. Those machines would let a leaver keep signing in if they still had one. She lists them for the IT lead to enrol or retire, closing a gap that account disabling alone cannot reach.

### 11.3 Local administrator passwords

Each laptop also has a built-in local administrator account for emergencies. If every laptop uses the same local password, knowing it on one machine opens all of them. Elena recommends a tool built into the device management service that gives each laptop a unique, automatically rotated local administrator password, stored centrally and logged when viewed. This is a small configuration change with a large effect, and it shows how operating system settings are part of identity and access management. The IT lead approves the change.

### Worked example

Elena finds 46 of 140 laptops with daily administrator rights and four unenrolled laptops, and recommends standard accounts, enrolment and unique local administrator passwords.

> **Synthetic case.** Laptops and counts are synthetic.

### Errors and limits

Disabling a leaver's cloud account does not stop sign-in on laptops that use only local accounts.

### Exercises

- **EX031 — Admin daily risk.** Why is working daily as administrator risky? *Rubric:* 3 = harmful files get admin power;; 2 = power;; 1 = slow;; 0 = none.
- **EX032 — Unenrolled laptops.** How many unenrolled laptops did Elena find? *Rubric:* 3 = four;; 2 = 4;; 1 = none;; 0 = none.
- **EX033 — Local password fix.** What fixes shared local administrator passwords? *Rubric:* 3 = unique, rotated, centrally stored and logged passwords;; 2 = unique;; 1 = none;; 0 = none.

### Synthesis

Standard daily accounts, managed device sign-in and unique local administrator passwords extend IAM to laptops.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) summarise identity measurements with medians and ranges; (2) reason about chance in small samples; (3) avoid overreading trends.

### 12.1 Summaries

Elena measures how many days pass between a leaver's last day and their account being disabled. The values vary widely: many are zero or one day, a few are weeks. The mean is pulled up by the long delays, so she reports the median as the typical case and the maximum to show the worst. She also counts how many exceed Greenhill's target of one day. Choosing summaries that match the shape of the data prevents a misleading single number from hiding the problem cases.

### 12.2 Small samples

Greenhill has about ten leavers a month, so monthly figures jump around by chance. If six were disabled on time one month and eight the next, that may not mean improvement. Elena groups three months together before comparing, and reports counts rather than only percentages. She explains to managers that with small numbers, a single slow case changes the percentage a lot, so they should look for patterns over several months rather than reacting to every change. She also shows the actual counts on every chart.

### 12.3 Trends and causes

When figures improve after a change, it is tempting to credit the change. Elena checks for other explanations: fewer leavers that month, a different person processing them or a holiday period. She marks when changes were made on her charts and compares periods of similar length. Where she cannot rule out alternatives, she says the improvement coincided with the change rather than claiming it was caused by it. Careful wording keeps her reports honest and her later capstone evaluation credible.

### Worked example

Over a quarter of 30 synthetic leavers, median delay is 1 day, maximum 31 days, and 14 exceed the one-day target.

> **Synthetic case.** Leavers and delays are synthetic.

### Errors and limits

Reacting to one month's change in a small team treats chance variation as a real trend.

### Exercises

- **EX034 — Median choice.** Why report the median leaver delay rather than the mean? *Rubric:* 3 = long delays pull the mean up;; 2 = skew;; 1 = simpler;; 0 = none.
- **EX035 — Grouping months.** Why group three months together? *Rubric:* 3 = small monthly numbers vary by chance;; 2 = chance;; 1 = tidier;; 0 = none.
- **EX036 — Cautious wording.** What wording does Elena use when alternatives cannot be ruled out? *Rubric:* 3 = improvement coincided with the change;; 2 = coincided;; 1 = caused;; 0 = none.

### Synthesis

Medians, maximums, grouped periods and careful causal wording make small identity datasets meaningful.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) explain identification, authentication and authorisation; (2) describe account lifecycle; (3) relate them to Greenhill's systems.

### 13.1 Three steps

Identity and access involve three steps. Identification is claiming to be someone, such as typing a username. Authentication is proving the claim, with a password, passkey or security key. Authorisation is deciding what that person may do once proven. Problems can occur at each step: a shared username breaks identification, a weak password weakens authentication, and excessive group membership breaks authorisation. Elena uses these three words carefully in her reports, because mixing them up leads to fixing the wrong thing.

### 13.2 Authenticators

NIST SP 800-63B-4 describes kinds of authenticators: something you know, such as a password; something you have, such as a phone or security key; and something you are, such as a fingerprint, used to unlock a device. Multi-factor authentication combines different kinds. Some methods resist phishing better than others: a security key or passkey checks the website it is talking to, while a code typed from a text message can be passed on to a fake site. Elena uses this to rank Greenhill's options.

### 13.3 Lifecycle

Every account has a lifecycle: created when someone joins, changed when they move role and removed when they leave. HR knows about these events first, so good lifecycle processes start from HR records. At Greenhill, joiners are handled well because people chase IT for access, but movers keep old access and leavers rely on an email from HR that sometimes arrives late. Elena maps the current process step by step, noting who does what and where delays happen, as the basis for later improvements.

### Worked example

Elena maps Greenhill's lifecycle: joiners take two days, movers keep old access indefinitely and leavers depend on a late-arriving HR email.

> **Synthetic case.** Processes and timings are synthetic.

### Errors and limits

Calling a weak password an authorisation problem leads to fixing permissions instead of authentication.

### Exercises

- **EX037 — Three steps names.** Name the three steps of identity and access. *Rubric:* 3 = identification, authentication, authorisation;; 2 = two;; 1 = one;; 0 = none.
- **EX038 — Phishing-resistant choice.** Why is a security key more phishing-resistant than a text code? *Rubric:* 3 = key checks the website; code can be passed on;; 2 = checks site;; 1 = cheaper;; 0 = none.
- **EX039 — Mover problem.** What goes wrong for movers at Greenhill? *Rubric:* 3 = they keep old access indefinitely;; 2 = old access;; 1 = nothing;; 0 = none.

### Synthesis

Clear use of identification, authentication and authorisation, and a mapped lifecycle, show where identity problems lie.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) identify personal data in identity systems; (2) apply minimisation and purpose limitation; (3) respect staff privacy in monitoring.

### 14.1 Personal data in identity

Identity systems hold personal data: names, job titles, phone numbers for multi-factor authentication, sign-in times and locations. Logs can reveal when someone works, where they travel and how often they make mistakes. Elena lists the personal data each identity system holds and why. She discovers that the old finance system stores staff home addresses it no longer needs, which becomes a recommendation for removal, since holding data without purpose adds risk without benefit. The list is shared with Greenhill's data protection lead for review and kept up to date.

### 14.2 Minimisation and purpose

Two privacy principles guide her work. Minimisation means collecting only what a purpose needs; purpose limitation means using data only for the purpose it was collected for. Sign-in logs are collected for security; using them to judge staff productivity would be a different purpose and would breach staff trust. Elena writes a short statement, agreed with HR and staff representatives, saying identity logs are used for security and troubleshooting only, which reassures staff worried about being watched. The statement is published on the staff intranet.

### 14.3 Privacy in multi-factor setup

Some multi-factor methods require a personal phone. Not all staff want to use their own phone for work, and some do not have a suitable one. Elena recommends offering alternatives, such as a security key provided by Greenhill, so nobody is forced to use personal devices. This respects privacy and also helps adoption: in her data, the repairs team's low multi-factor rate partly reflects operatives without work phones, a problem a provided key solves. Keys are issued and recorded by IT, and lost keys are reported and replaced quickly.

### Worked example

Elena lists personal data in six systems, finds unneeded home addresses in finance, and drafts a log-use statement agreed with HR and staff representatives.

> **Synthetic case.** Data fields and agreements are synthetic.

### Errors and limits

Using security logs to judge productivity breaks purpose limitation and staff trust.

### Exercises

- **EX040 — Unneeded data.** What unneeded personal data did Elena find? *Rubric:* 3 = staff home addresses in finance;; 2 = addresses;; 1 = none;; 0 = none.
- **EX041 — Purpose example.** Why not use sign-in logs to judge productivity? *Rubric:* 3 = different purpose, breaks purpose limitation and trust;; 2 = purpose;; 1 = allowed;; 0 = none.
- **EX042 — Phone alternative.** What alternative to personal phones does Elena recommend? *Rubric:* 3 = Greenhill-provided security keys;; 2 = keys;; 1 = none;; 0 = none.

### Synthesis

Minimisation, purpose limitation and alternatives to personal phones make identity systems respectful of staff privacy.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) define identity measures precisely; (2) collect them consistently; (3) present them clearly to decision-makers.

### 15.1 Defining measures

A measure must be defined so that anyone would count it the same way. Elena defines multi-factor coverage as enabled staff accounts with at least one registered second factor, divided by all enabled staff accounts, excluding service accounts, on the first day of each month. Each part of the definition matters: including disabled accounts or service accounts would change the result. She writes definitions in a short table with the data source and known weaknesses, so the measure can be repeated by someone else.

### Lab — Coverage by team

```python
"""Multi-factor coverage by staff group from a synthetic account export (stdlib only)."""
from collections import defaultdict
rows = [("housing", 1)]*38 + [("housing", 0)]*7 + [("repairs", 1)]*22 + [("repairs", 0)]*18 + [("finance", 1)]*14 + [("finance", 0)]*1 \
     + [("office", 1)]*30 + [("office", 0)]*5 + [("admin", 1)]*4 + [("admin", 0)]*1
g = defaultdict(lambda: [0, 0])
for grp, m in rows: g[grp][0] += m; g[grp][1] += 1
for grp, (m, n) in sorted(g.items(), key=lambda x: x[1][0]/x[1][1]):
    print(f"{grp:8} {m:3}/{n:<3} {100*m/n:5.1f}%")
tm = sum(v[0] for v in g.values()); tn = sum(v[1] for v in g.values()); print(f"overall  {tm}/{tn} {100*tm/tn:.1f}%")
```

Run with `python3 lab_mfa.py`. Verified output:

```text
repairs   22/40   55.0%
admin      4/5    80.0%
housing   38/45   84.4%
office    30/35   85.7%
finance   14/15   93.3%
overall  108/140 77.1%
```

### 15.2 Reading coverage

The synthetic export shows overall coverage of 108 of 140, or 77.1 percent. Teams differ sharply: finance is at 93.3 percent, office and housing in the mid-eighties, administrators at 80 percent and repairs at 55 percent. The one administrator without multi-factor is the most urgent single gap, because administrator accounts can change everything. The repairs gap is the largest in number. Elena presents both, explaining that priority depends on harm as well as size, so the IT lead can plan which to tackle first.

Fixing the one administrator account takes minutes, while the repairs gap needs devices and training, so the two fixes run on different timescales.

### 15.3 Presenting measures

Elena presents measures with their definition, the current value with count and base, the previous value and a short comment. She uses a simple bar chart sorted by value so the lowest team stands out. She avoids decorative charts and unnecessary decimals. Each figure is dated and linked to the export it came from. Clear, consistent presentation lets managers compare months quickly and builds trust that changes in the numbers reflect real changes at Greenhill. Each chart has a short caption explaining what changed.

### Worked example

Coverage is 77.1 percent overall; one of five administrators and 18 of 40 repairs staff lack multi-factor, giving one urgent and one large gap.

> **Synthetic case.** Teams, counts and coverage are synthetic.

### Errors and limits

Including disabled or service accounts in coverage makes the measure inconsistent between months.

### Exercises

- **EX043 — Overall coverage.** What is overall multi-factor coverage in the lab? *Rubric:* 3 = 108 of 140, 77.1%;; 2 = 77.1%;; 1 = 100%;; 0 = none.
- **EX044 — Lowest team.** Which team has the lowest coverage, and at what level? *Rubric:* 3 = repairs, 55.0%;; 2 = repairs;; 1 = finance;; 0 = none.
- **EX045 — Urgent gap.** Why is the administrator gap most urgent? *Rubric:* 3 = admin accounts can change everything;; 2 = power;; 1 = size;; 0 = none.

### Synthesis

Precise definitions, consistent collection and clear presentation turn identity data into usable evidence.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe a target identity architecture for a small organisation; (2) place controls sensibly; (3) keep the design simple.

### 16.1 One identity provider

Elena's target architecture for Greenhill uses the office suite as the single identity provider. Systems that can, sign staff in through it with single sign-on; those that cannot are listed for replacement or careful separate management. Multi-factor authentication is enforced at the provider, so every connected system benefits. HR records drive account creation and removal. This arrangement follows a common pattern in which identity becomes the central control point, an idea also found in NIST SP 800-207's description of zero trust.

### 16.2 Placing controls

Controls sit where they work best. Strong sign-in is enforced at the provider. Detailed permissions, such as which tenant records a housing officer can see, stay in the housing system, which understands its own data. Administrator accounts are separate from everyday accounts and need security keys. Logging collects sign-in events from the provider. Elena draws these on a simple diagram, labelling each control with what it protects, so Greenhill's managers can see why each one is there. The diagram is updated whenever a control moves.

### 16.3 Keeping it simple

A small team needs a simple design. Elena avoids adding a second identity system, complex rules for every situation or many special exceptions. She proposes a few clear policies: everyone uses multi-factor, administrators use security keys, leavers are disabled on their last day, and access is granted by team groups. Simple designs are easier to explain, check and keep working after Elena leaves, which matters more at Greenhill than adopting every advanced feature available. Any new exception must be justified in writing and reviewed yearly.

### Worked example

Elena's architecture diagram shows one provider, three single sign-on systems, three systems for replacement or separate management, and four simple policies.

> **Synthetic case.** The architecture and systems are synthetic; NIST SP 800-207 is a real source.

### Errors and limits

Adding complex rules and exceptions a small team cannot maintain lets the design decay quickly.

### Exercises

- **EX046 — Provider choice.** What serves as Greenhill's identity provider? *Rubric:* 3 = the office suite;; 2 = office suite;; 1 = finance;; 0 = none.
- **EX047 — Permission placement.** Where do detailed tenant-record permissions stay? *Rubric:* 3 = in the housing system;; 2 = application;; 1 = provider;; 0 = none.
- **EX048 — Four policies.** List Elena's four simple policies. *Rubric:* 3 = MFA for all, admin keys, leaver same-day disable, team groups;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

One identity provider, sensibly placed controls and a few clear policies suit a small organisation.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain hashing and why passwords are stored hashed; (2) describe public-key signatures in passkeys; (3) understand certificates in sign-in.

### 17.1 Hashing passwords

Systems should never store passwords as plain text. Instead they store a hash, the output of a one-way function, often with a random salt and a deliberately slow algorithm. When someone signs in, the system hashes what they typed and compares. If the stored hashes leak, attackers cannot simply read the passwords, though weak passwords may still be guessed. Elena asks Greenhill's finance system supplier how passwords are stored and records the answer, because older systems sometimes fall short. Answers are kept in the system inventory.

### 17.2 Signatures in passkeys

Passkeys use public-key cryptography. When a passkey is created, the device makes a pair of keys: a private key that stays on the device and a public key given to the website. To sign in, the website sends a challenge and the device signs it with the private key. The website checks the signature with the public key. No secret travels that a fake site could reuse, and the website stores nothing that would let an attacker sign in if it leaked.

### 17.3 Certificates

When a browser connects to a sign-in page over HTTPS, the site presents a certificate showing that a trusted authority has confirmed it controls that name. The browser checks it automatically. Certificates also sign the messages identity providers send to connected systems. Each certificate expires, and an expired signing certificate can stop single sign-on for every connected system at once. Elena adds certificate expiry dates for Greenhill's single sign-on connections to the IT team's calendar. A named person owns each renewal, and a colleague is listed as backup.

### Worked example

Elena records how each system stores passwords and adds three single sign-on certificate expiry dates to the IT calendar with reminders thirty days ahead.

> **Synthetic case.** Systems and dates are synthetic.

### Errors and limits

Assuming every supplier hashes passwords properly without asking leaves older systems unchecked.

### Exercises

- **EX049 — Hash meaning.** What is a password hash? *Rubric:* 3 = one-way function output stored instead of password;; 2 = one-way;; 1 = encryption;; 0 = none.
- **EX050 — Passkey private key.** Where does a passkey's private key stay? *Rubric:* 3 = on the device;; 2 = device;; 1 = website;; 0 = none.
- **EX051 — Certificate expiry risk.** What can an expired single sign-on certificate cause? *Rubric:* 3 = sign-in failure for every connected system;; 2 = outage;; 1 = nothing;; 0 = none.

### Synthesis

Hashing, public-key signatures and managed certificates are the cryptographic foundations of safe sign-in.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) form a clear research question; (2) choose a suitable method; (3) plan data collection ethically.

### 18.1 A research question

Elena's first research exercise asks: why is multi-factor coverage low in the repairs team? A good question is specific, answerable with available evidence and useful to Greenhill. She avoids broad questions such as how to improve security, which cannot be answered in one study. She writes her question, what would count as an answer and how the answer would help, and agrees it with her supervisor and the repairs manager before collecting anything. The agreed question is written at the top of her research notes.

### 18.2 Choosing a method

Numbers show where coverage is low but not why. Elena chooses short interviews with eight repairs operatives and the repairs manager, combined with observation of how operatives sign in on their tablets at the start of a shift. Interviews reveal reasons people give; observation shows what actually happens. Using both helps her spot differences, such as operatives saying they have multi-factor set up when the tablet actually stays signed in under a shared account. She notes where the two sources agree and where they differ.

### 18.3 Ethical data collection

Participants are told the purpose, that taking part is voluntary and that their names will not appear in reports. Elena gets consent in writing, records notes rather than audio, stores them securely and deletes them after analysis. Her university's ethics process reviews the plan first. She takes care not to make anyone feel blamed for low coverage, because the aim is to understand barriers, and people who feel judged rarely explain them honestly. Participants receive a short summary of findings once the study is complete.

### Worked example

Interviews and observation reveal that repairs tablets stay signed in under shared accounts and that operatives lack work phones, explaining much of the low coverage.

> **Synthetic case.** Interviews, operatives and findings are synthetic.

### Errors and limits

Relying only on what people say can miss practices, such as shared tablet accounts, that observation would show.

### Exercises

- **EX052 — Specific question.** Why avoid a question like how to improve security? *Rubric:* 3 = too broad to answer in one study;; 2 = broad;; 1 = boring;; 0 = none.
- **EX053 — Observation value.** What did observation add to interviews? *Rubric:* 3 = showed shared tablet accounts despite claims;; 2 = practice;; 1 = nothing;; 0 = none.
- **EX054 — Consent elements.** Name two things participants are told. *Rubric:* 3 = purpose, voluntary, anonymity (two);; 2 = one;; 1 = none;; 0 = none.

### Synthesis

A specific question, mixed methods and ethical collection give clear, trustworthy explanations.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and access management: scope and theory

### Learning outcomes

You will (1) define the scope of IAM; (2) explain least privilege and separation of duties; (3) relate access control models to Greenhill.

### 19.1 Scope of IAM

Identity and access management covers how identities are created, verified and removed; how access is granted, reviewed and revoked; and how actions are logged and checked. It includes people, such as staff and contractors, and non-human identities, such as service accounts used by systems. At Greenhill, Elena's scope covers staff and contractors across six systems, plus two service accounts used by the finance system to send payment files. Stating scope prevents her from drifting into unrelated areas such as network firewalls.

### 19.2 Least privilege and separation of duties

Saltzer and Schroeder (1975) described least privilege: each person or program should have only the access needed for its job. Separation of duties adds that no single person should complete a sensitive task alone, such as setting up a new supplier and paying them. In Greenhill's finance system, Elena finds one officer who can do both. She reports it, and the finance manager agrees that a second person will approve new suppliers, a small change that removes a serious risk.

The same check is worth repeating whenever finance staff change roles, since a mover can quietly end up holding both permissions.

### 19.3 Access control models

Role-based access control gives access through roles linked to jobs, as described by Sandhu and colleagues (1996). It suits Greenhill, where most staff in a team need the same access. Attribute-based access control, described in NIST SP 800-162, decides using attributes such as department or location, which suits finer rules. Elena recommends roles for Greenhill, implemented as team groups, with a short list of documented exceptions, because a small organisation benefits from the simplest model that works. Exceptions are reviewed each quarter.

### Worked example

Elena's scope covers staff, contractors and two service accounts across six systems; she finds one finance officer able to create and pay suppliers, fixed by adding second approval.

> **Synthetic case.** Systems, officers and accounts are synthetic; the cited papers and NIST SP 800-162 are real.

### Errors and limits

Ignoring service accounts leaves powerful non-human identities unmanaged.

### Exercises

- **EX055 — Non-human identity.** Give an example of a non-human identity at Greenhill. *Rubric:* 3 = finance service account sending payment files;; 2 = service account;; 1 = tenant;; 0 = none.
- **EX056 — Supplier conflict.** What separation-of-duties problem did Elena find? *Rubric:* 3 = one officer could set up and pay suppliers;; 2 = create and pay;; 1 = none;; 0 = none.
- **EX057 — Model choice.** Which access model does Elena recommend for Greenhill? *Rubric:* 3 = role-based via team groups, few exceptions;; 2 = roles;; 1 = attributes;; 0 = none.

### Synthesis

Clear scope, least privilege, separation of duties and a simple role model form the theory behind Greenhill's IAM.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Identity and access management: foundational cases

### Learning outcomes

You will (1) study well-known identity failure patterns; (2) relate them to Greenhill; (3) draw defensive lessons.

### 20.1 The forgotten leaver

A common pattern in organisations of all sizes is the leaver whose access is never fully removed. Weeks later, their account is used, either by them or by someone who obtained their password. The lesson is not about villains but about process: removal depends on someone remembering, across several systems. Elena relates this to Greenhill's late HR emails and separate finance accounts, and concludes that leaver removal must be triggered automatically from HR records and checked against every system. She records this as a priority.

### 20.2 The shared account

Another pattern is the shared account: a reception login used by whoever is on shift, or a team account for a scheduling app. When something goes wrong, nobody can tell who did it, and the password is known to everyone who ever worked there, including leavers. Elena's data shows two likely shared accounts at Greenhill. The lesson is to give each person their own account, using features such as shared mailboxes that allow team access without sharing a password. Each case is discussed with its team.

### 20.3 The overpowered helper

A third pattern is the helpful employee who gathers access over years, covering for colleagues and moving between teams, until they hold far more than any job needs. If their account is misused, the harm is wide. Regular access reviews and removing old access when people move address this. Elena finds two long-serving Greenhill staff with access from three previous roles and recommends a review, framed as tidying rather than blame. Both staff members agree that the review is reasonable, and unused access is removed with their managers' approval.

### Worked example

Elena maps three foundational patterns, the forgotten leaver, the shared account and the overpowered helper, to specific Greenhill findings and preventive actions.

> **Synthetic case.** Patterns are general; Greenhill findings are synthetic.

### Errors and limits

Treating identity failures as stories about bad people distracts from the process gaps that allow them.

### Exercises

- **EX058 — Leaver lesson.** What is the main lesson of the forgotten leaver? *Rubric:* 3 = removal must be automatic from HR and checked everywhere;; 2 = automate;; 1 = villains;; 0 = none.
- **EX059 — Shared account alternative.** What allows team access without sharing a password? *Rubric:* 3 = features such as shared mailboxes with individual accounts;; 2 = shared mailbox;; 1 = none;; 0 = none.
- **EX060 — Overpowered fix.** What addresses the overpowered helper? *Rubric:* 3 = regular reviews and removing old access on moves;; 2 = reviews;; 1 = nothing;; 0 = none.

### Synthesis

Common failure patterns teach that process, individual accounts and regular reviews prevent most identity harm.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Identity and access management: system models

### Learning outcomes

You will (1) model Greenhill's identity system as components and flows; (2) describe joiner, mover and leaver flows; (3) find weak points in the model.

### 21.1 Components

Elena models Greenhill's identity system as components: HR records, the office suite identity provider, the housing system, the finance system, the repairs app, the IT team and line managers. Arrows show information moving between them, such as HR telling IT about a leaver or the provider telling the housing system who has signed in. Drawing the model on one page helps everyone see the whole system at once. It also shows that much of identity management depends on people passing messages, not only on technology.

### 21.2 Lifecycle flows

Using the model, Elena traces three flows. A joiner flow starts when HR enters a new starter, IT creates an account and the manager requests team access. A mover flow should remove old access when someone changes team, but currently only adds new access. A leaver flow starts with an HR email to IT, who disable the office suite account and then email system owners about other accounts. Each step is marked with who performs it, how long it usually takes and what happens if it is missed.

### 21.3 Weak points

The model shows weak points clearly. The leaver flow depends on two emails, either of which can be delayed or lost. The mover flow has no removal step at all. The finance system is outside single sign-on, so its accounts are not disabled when the office suite account is. The repairs app uses a shared account. Elena marks each weak point on the diagram with a number and lists it in a table with its likely effect, which becomes the starting point for designing controls in later chapters.

### Worked example

Elena's one-page model shows seven components, three lifecycle flows and four numbered weak points, from email-dependent leavers to the shared repairs account.

> **Synthetic case.** Components, flows and weak points are synthetic.

### Errors and limits

Modelling only technical systems and leaving out managers and HR misses where most lifecycle delays occur.

### Exercises

- **EX061 — Mover flow gap.** What step is missing from the mover flow? *Rubric:* 3 = removal of old access;; 2 = removal;; 1 = creation;; 0 = none.
- **EX062 — Leaver dependency.** What does the leaver flow depend on? *Rubric:* 3 = two emails that can be delayed or lost;; 2 = emails;; 1 = automation;; 0 = none.
- **EX063 — People in model.** Why include managers and HR in the model? *Rubric:* 3 = much identity work is messages between people;; 2 = people;; 1 = style;; 0 = none.

### Synthesis

A simple component and flow model exposes where identity processes break.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Identity and access management: data and dependencies

### Learning outcomes

You will (1) identify data sources for identity checks; (2) detect possible shared accounts from sign-in records; (3) map dependencies between systems.

### 22.1 Data sources

Elena's checks rely on several sources: HR's staff list, the office suite account export, its sign-in logs, the finance system's user list and the repairs app's account list. Each has an owner, an update frequency and quirks, such as the finance list using initials rather than full names. She records these details so that combining sources is done carefully, and she agrees with each owner how often she may receive exports and how they will be handled, in line with her written permission.

### Lab — Possible shared accounts

```python
"""Flag accounts signed in from two distant sites within ten minutes in synthetic logs - a sign of sharing (stdlib only)."""
log = [("reception", "09:00", "HQ"), ("reception", "09:04", "Depot"), ("jsmith", "09:02", "HQ"), ("repairs1", "08:10", "Depot"),
       ("repairs1", "08:15", "Van-7"), ("repairs1", "08:16", "Depot"), ("akhan", "10:00", "HQ"), ("akhan", "13:00", "Depot"), ("reception", "12:30", "HQ")]
def mins(t): h, m = t.split(":"); return int(h)*60 + int(m)
flag = set()
by = {}
for a, t, s in sorted(log, key=lambda r: (r[0], mins(r[1]))):
    if a in by and by[a][1] != s and mins(t) - by[a][0] <= 10: flag.add(a)
    by[a] = (mins(t), s)
print("accounts:", len(by), " flagged as possibly shared:", sorted(flag))
```

Run with `python3 lab_shared.py`. Verified output:

```text
accounts: 4  flagged as possibly shared: ['reception', 'repairs1']
```

### 22.2 Reading the result

The synthetic sign-in sample shows four accounts. Two are flagged: reception signed in at headquarters and at the depot four minutes apart, and repairs1 signed in at the depot, then from van 7 and back at the depot within six minutes. One person cannot be in two places that quickly, so these accounts are probably shared. Accounts like akhan, signing in at different sites hours apart, are normal. Elena treats the flags as leads to check with managers, not as proof, because location records can be imprecise.

### 22.3 Dependencies

Systems depend on each other. If the office suite provider is unavailable, staff cannot reach the connected systems either. The finance system sends payment files using a service account whose password is stored on one server; if that password expires, payments stop. The repairs app depends on tablets staying signed in. Elena maps these dependencies so that changes, such as enforcing multi-factor or rotating a service account password, are planned with their knock-on effects in mind and do not interrupt essential services such as paying suppliers.

### Worked example

The sign-in check flags reception and repairs1 as possibly shared; managers confirm both are used by several people per shift.

> **Synthetic case.** Accounts, sites and times are synthetic.

### Errors and limits

Treating location-based flags as proof of sharing ignores imprecise location records.

### Exercises

- **EX064 — Flagged accounts.** Which accounts does the lab flag as possibly shared? *Rubric:* 3 = reception and repairs1;; 2 = two;; 1 = akhan;; 0 = none.
- **EX065 — Normal pattern.** Why is akhan not flagged? *Rubric:* 3 = different sites hours apart is normal;; 2 = time gap;; 1 = error;; 0 = none.
- **EX066 — Service account dependency.** What stops if the finance service account password expires? *Rubric:* 3 = supplier payments;; 2 = payments;; 1 = email;; 0 = none.

### Synthesis

Understanding data sources, checking sign-in patterns and mapping dependencies make identity changes safe.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Identity and access management: methods I

### Learning outcomes

You will (1) design an HR-driven leaver process; (2) plan individual accounts to replace shared ones; (3) involve owners in each method.

### 23.1 HR-driven leavers

Elena designs a leaver method that starts from HR rather than email. When HR records a leaving date in its system, a scheduled job compares HR with the office suite each evening and disables accounts whose leaving date has passed. A report lists the person's accounts in other systems, such as finance, for their owners to disable the next morning, with a reminder if not done. This turns a process relying on memory into one triggered by data, while keeping owners responsible for systems outside single sign-on.

### 23.2 Replacing shared accounts

For reception, Elena proposes individual accounts for each receptionist, with access to a shared reception mailbox and calendar through group membership. For the repairs app, she works with the supplier to enable sign-in with office suite accounts and gives each operative a security key that works on the tablets. Each change is tested with two volunteers before rolling out. Replacing shared accounts takes effort, but it restores traceability and means leavers lose access automatically when their own account is disabled.

### 23.3 Involving owners

Each method affects people who own systems or processes. HR must keep leaving dates accurate and timely; system owners must act on reports; managers must request access through groups. Elena meets each owner, explains the reason, listens to concerns and adjusts. The finance manager worries about disabling accounts before final payroll tasks, so leavers in finance are disabled at the end of their last day rather than at midnight before. Methods agreed with owners are far more likely to be followed than ones imposed by IT.

### Worked example

The HR-driven method disables office suite accounts each evening and reports other accounts to owners; shared reception and repairs logins are replaced with individual accounts and security keys.

> **Synthetic case.** Methods, owners and systems are synthetic.

### Errors and limits

Designing a leaver process without HR's commitment to timely dates makes automation act on wrong data.

### Exercises

- **EX067 — Leaver trigger.** What triggers leaver disabling in the new method? *Rubric:* 3 = HR leaving date checked nightly;; 2 = HR date;; 1 = email;; 0 = none.
- **EX068 — Repairs fix.** How are repairs operatives given individual sign-in? *Rubric:* 3 = office suite accounts with security keys on tablets;; 2 = keys;; 1 = shared;; 0 = none.
- **EX069 — Finance timing.** When are finance leavers disabled, and why? *Rubric:* 3 = end of last day, for final payroll tasks;; 2 = end of day;; 1 = midnight;; 0 = none.

### Synthesis

HR-triggered leavers, individual accounts and owner involvement are the first core methods.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Identity and access management: controls

### Learning outcomes

You will (1) specify multi-factor, administrator and access-group controls; (2) choose authenticators by role; (3) define review controls.

### 24.1 Multi-factor control

The control states that every staff account must have multi-factor authentication registered, enforced at the office suite provider for all sign-ins. Elena chooses authenticators by role, following NIST SP 800-63B-4: administrators and finance staff use security keys or passkeys, which resist fake sign-in pages; other staff may use an authenticator app or passkey; repairs operatives use provided security keys. Text message codes are phased out because they can be intercepted or passed to fake sites more easily. Coverage is checked monthly against this rule using the identity report.

### 24.2 Administrator controls

Administrator access is the most powerful at Greenhill. Elena specifies separate administrator accounts not used for email or browsing, security keys only, and a list of administrators reviewed monthly. She recommends reducing the nine administrator accounts found earlier to those actually needed, with roles limited to specific tasks, such as password resets for the service desk, rather than full control. Every administrator action is logged by the provider and reviewed when anything unusual happens. The IT lead approves any new administrator account in writing, with a stated reason and review date.

### 24.3 Groups and reviews

Access to systems is given through team groups owned by managers. Joining a group needs the group owner's approval; leaving a team removes membership automatically when HR records the move. Every six months, managers review their groups, confirming each member still needs access. Elena keeps the review short, showing each person's name, groups and last sign-in, so managers can decide quickly. Group-based access with regular reviews keeps least privilege practical for a small organisation. Reviews that are not completed on time are escalated to the manager's director.

### Worked example

The control set requires multi-factor for all, security keys for administrators and finance, separate administrator accounts reduced from nine to four, and six-monthly manager reviews of team groups.

> **Synthetic case.** Controls and counts are synthetic; NIST SP 800-63B-4 is a real source.

### Errors and limits

Using everyday accounts for administration exposes powerful rights to email and browsing risks.

### Exercises

- **EX070 — Text code phase-out.** Why are text message codes phased out? *Rubric:* 3 = interceptable and easily passed to fake sites;; 2 = weaker;; 1 = cost;; 0 = none.
- **EX071 — Admin reduction.** How many administrator accounts remain after reduction? *Rubric:* 3 = four, from nine;; 2 = four;; 1 = nine;; 0 = none.
- **EX072 — Review content.** What does a manager see in a group review? *Rubric:* 3 = name, groups and last sign-in per person;; 2 = names;; 1 = passwords;; 0 = none.

### Synthesis

Role-appropriate authenticators, tightly controlled administrators and owned, reviewed groups form Greenhill's core controls.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) set up a safe test environment; (2) test controls with synthetic accounts; (3) record results as evidence.

### 25.1 A safe test environment

Elena tests controls in a separate trial tenant of the office suite, which the supplier provides for testing, with synthetic users and groups. Nothing in the trial tenant can affect real staff. She mirrors Greenhill's planned settings: multi-factor enforcement, administrator restrictions and group-based access to a sample application. Using a test environment means mistakes, such as a rule that locks out everyone, are discovered safely before anything changes for real users. The trial tenant is reset before each round of tests, so earlier experiments cannot affect new results, and its settings are kept in a dated file.

### 25.2 Test cases

Each test states the control, the synthetic input and the expected result. A synthetic user without multi-factor tries to sign in and should be asked to register. A synthetic administrator using an everyday account tries an administrator task and should be refused. A synthetic leaver marked in a test HR file should be disabled by the evening job. A synthetic user added to a group should reach the sample application, and one removed should not. Expected results are written before running, so outcomes are judged honestly.

### 25.3 Recording evidence

For each test, Elena records the date, the settings version, the input, what happened and pass or fail, with a screenshot or log extract. Of twenty tests, eighteen pass. One failure shows that the evening job ignored leavers whose leaving date had been entered with a time; another shows a group owner could add members without approval. Both are fixed and retested. The evidence log becomes part of her capstone and lets the IT lead see exactly what was tested.

### Worked example

Eighteen of twenty trial-tenant tests pass; failures in date handling and group approval are fixed and retested.

> **Synthetic case.** The tenant, tests and failures are synthetic.

### Errors and limits

Testing new controls directly on real staff accounts risks locking people out of work.

### Exercises

- **EX073 — Trial tenant purpose.** Why use a trial tenant? *Rubric:* 3 = mistakes cannot affect real staff;; 2 = safety;; 1 = cost;; 0 = none.
- **EX074 — Lab I result.** How many tests passed in Laboratory I? *Rubric:* 3 = 18 of 20;; 2 = 18;; 1 = 20;; 0 = none.
- **EX075 — Date bug.** What was the leaver date bug? *Rubric:* 3 = evening job ignored dates entered with a time;; 2 = date format;; 1 = none;; 0 = none.

### Synthesis

A safe test environment, written test cases and recorded evidence make control changes trustworthy.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Identity and access management: methods II

### Learning outcomes

You will (1) measure leaver timeliness; (2) analyse delays; (3) improve the mover process.

### 26.1 Measuring leavers

With the HR-driven process designed, Elena first measures the old process to have a fair baseline. For each recent leaver she records the HR leaving date and the date their office suite account was disabled, then counts days between. Greenhill's target is disabling within one day. She uses the same definition for every leaver and notes any she cannot measure, such as a leaver whose date was changed after they left, so the baseline is honest and comparable with later results.

### Lab — Leaver delays

```python
"""Days from HR leaving date to account disable for synthetic leavers; count breaches of a one-day target (stdlib only)."""
import statistics as st
days = {"L01": 0, "L02": 3, "L03": 1, "L04": 14, "L05": 0, "L06": 2, "L07": 31, "L08": 1, "L09": 0, "L10": 6}
v = list(days.values())
print(f"leavers={len(v)} median_days={st.median(v)} max_days={max(v)} over_1_day={sum(d > 1 for d in v)}")
print("worst:", sorted(days, key=days.get, reverse=True)[:3])
```

Run with `python3 lab_offboard.py`. Verified output:

```text
leavers=10 median_days=1.5 max_days=31 over_1_day=5
worst: ['L07', 'L04', 'L10']
```

### 26.2 Reading the delays

The synthetic baseline of ten leavers shows a median of 1.5 days, but a maximum of 31 days, and five of ten miss the one-day target. The worst cases, L07 at 31 days, L04 at 14 and L10 at 6, all left during holiday periods, when HR's email waited in an absent colleague's inbox. This confirms the weak point found in the model: email-based handover fails when people are away. Elena uses these cases to explain to managers why the evening HR comparison matters.

Five of ten missing the target shows that the median of 1.5 days hides a process that fails half the time.

### 26.3 Improving movers

The mover process currently adds access but never removes it. Elena designs a change: when HR records a team move, the person keeps old team groups for two weeks to finish handover, then the old groups are removed automatically, with a reminder to the old manager a few days before. Exceptions require the new manager's approval and an end date. This small change will gradually reduce the access build-up she found in long-serving staff, without disrupting handover work. HR confirms each move date before it takes effect.

### Worked example

The baseline shows five of ten leavers over target with a 31-day maximum, all slow cases in holidays; movers keep old groups for two weeks before automatic removal.

> **Synthetic case.** Leavers, delays and processes are synthetic.

### Errors and limits

Reporting only the median leaver delay hides the long holiday delays that create real risk.

### Exercises

- **EX076 — Leaver baseline.** What does the lab baseline show? *Rubric:* 3 = median 1.5 days, max 31, five of ten over target;; 2 = five over;; 1 = all fine;; 0 = none.
- **EX077 — Slow cause.** What caused the slowest leaver delays? *Rubric:* 3 = holiday periods, emails waiting in absent inbox;; 2 = holidays;; 1 = IT;; 0 = none.
- **EX078 — Mover grace.** How long do movers keep old groups? *Rubric:* 3 = two weeks, then automatic removal;; 2 = two weeks;; 1 = forever;; 0 = none.

### Synthesis

A measured baseline explains delays and justifies automated leaver and mover methods.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Identity and access management: verification

### Learning outcomes

You will (1) verify that controls work in production; (2) sample real outcomes; (3) distinguish configured from effective.

### 27.1 Configured versus effective

A control can be configured correctly yet fail in practice. Multi-factor may be enforced, but an old email app that does not support it might still be allowed by an exception. Elena distinguishes configured, meaning the setting exists, from effective, meaning real sign-ins actually use it. She checks effectiveness by sampling sign-in logs and confirming that each successful sign-in included a second factor, finding a few from an old app exception that is then removed. Both views are reported side by side each month for every key control.

### 27.2 Sampling outcomes

Verifying every event is impractical, so Elena samples. Each month she takes twenty random sign-ins, all leavers and all administrator actions, and checks each against the controls. Random samples avoid her unconsciously picking easy cases. For leavers, she checks every case because there are few and each matters. Sampling results are recorded with the selection method, so another person could repeat the check and get comparable results. Samples are drawn by a short script using a recorded random seed, and results are kept with the monthly evidence so trends in control effectiveness become visible over time.

### 27.3 Independent checking

Elena asks Greenhill's external auditor to review her verification method and a sample of evidence. The auditor suggests adding checks for accounts created outside the HR process, such as test accounts set up by suppliers. Elena adds a monthly query for accounts with no HR match created in the last month. Independent checking catches blind spots and adds weight to her conclusions, because the people who design controls are not always best placed to judge whether they work. The auditor's comments are filed with her evidence.

### Worked example

Sampling finds three sign-ins without a second factor via an old app exception, which is removed; the auditor's suggestion adds a check for accounts created outside HR.

> **Synthetic case.** Samples, findings and the auditor are synthetic.

### Errors and limits

Checking only that a control is configured, not that it is effective, misses exceptions that bypass it.

### Exercises

- **EX079 — Configured versus effective.** What is the difference between configured and effective? *Rubric:* 3 = setting exists vs real sign-ins use it;; 2 = exists vs works;; 1 = same;; 0 = none.
- **EX080 — Random sampling reason.** Why sample sign-ins randomly? *Rubric:* 3 = avoids picking easy cases;; 2 = bias;; 1 = speed;; 0 = none.
- **EX081 — Auditor addition.** What check did the auditor suggest? *Rubric:* 3 = accounts created outside HR, such as supplier test accounts;; 2 = outside HR;; 1 = none;; 0 = none.

### Synthesis

Verification checks real outcomes by sampling and benefits from independent review.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Identity and access management: failure analysis

### Learning outcomes

You will (1) analyse what happens when identity controls fail; (2) plan for lost keys and outages; (3) learn from near misses.

### 28.1 Lost and broken keys

Security keys get lost. If an operative loses a key and cannot sign in, work stops. Elena designs a recovery process: the operative calls the service desk, who verify identity by calling back the manager on a known number, issue a spare key and revoke the lost one. Each operative also registers a second key kept at the depot. NIST SP 800-63B-4 treats loss and recovery as part of authenticator management, and a weak recovery step would undo the protection keys provide.

### 28.2 Provider outages

If the office suite provider is unavailable, staff cannot sign in to connected systems. Elena checks the provider's published service status history and finds rare but real outages. She plans what Greenhill does: emergency tenant contact numbers are kept on paper at reception, the repairs team has a printed list of the day's jobs each morning, and one emergency administrator account with a key in the safe can be used if the IT lead's normal access fails. These simple steps limit harm without adding complexity.

### 28.3 Near misses

A near miss is a failure that almost caused harm. During rollout, a group rule briefly removed housing officers from the housing system for twenty minutes because a group was renamed. Nobody was hurt, but tenant calls were delayed. Elena records the near miss without blame, identifies the cause, a rename not tested first, and adds a test for group renames. Learning from near misses is cheaper than learning from real incidents and builds a culture where people report problems early.

### Worked example

A twenty-minute housing access near miss from an untested group rename leads to a new test; lost-key recovery uses manager call-back and spare keys.

> **Synthetic case.** Events and processes are synthetic; NIST SP 800-63B-4 is a real source.

### Errors and limits

Recovering lost keys with weak checks, such as a caller simply giving their name, undoes the protection keys provide.

### Exercises

- **EX082 — Lost key verification.** How does the desk verify an operative who lost a key? *Rubric:* 3 = call back the manager on a known number;; 2 = call-back;; 1 = name only;; 0 = none.
- **EX083 — Outage preparation.** Name one outage arrangement Elena plans. *Rubric:* 3 = paper emergency contacts, printed job lists, safe-stored emergency admin key (one);; 2 = one;; 1 = none;; 0 = none.
- **EX084 — Near miss cause.** What caused the housing access near miss? *Rubric:* 3 = an untested group rename;; 2 = rename;; 1 = attack;; 0 = none.

### Synthesis

Planned recovery, outage arrangements and learning from near misses make identity controls resilient.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Identity and access management: operations

### Learning outcomes

You will (1) run monthly identity routines; (2) handle access requests; (3) report to managers.

### 29.1 Monthly routines

Elena writes a monthly routine for Greenhill's IT team: run the identity report, check leavers against all systems, review administrator accounts, check multi-factor coverage by team and look at accounts unused for ninety days. Each task has a checklist and expected time, so the routine takes about two hours. Writing routines down means they continue when someone is on holiday or leaves, which is exactly when undocumented habits tend to stop. The routine is reviewed every six months and updated when systems change, so it always matches how Greenhill actually works.

### 29.2 Access requests

Staff request access through a simple form naming the system, the reason and the group needed. The group owner approves or declines. IT then adds the person to the group, never granting individual permissions directly. Requests and decisions are kept so later reviews can see why access was given. This replaces informal emails and corridor requests, which left no record and made it impossible to know whether access had ever been approved by anyone responsible. Declined requests are kept too, with the owner's reason recorded.

### 29.3 Reporting

Each month, a one-page summary goes to the senior management team: multi-factor coverage, leavers disabled within one day, administrator count, shared accounts remaining and open actions. Each figure shows this month, last month and target. Elena keeps it short so managers actually read it. When figures worsen, the summary explains why, such as a new team not yet enrolled, so managers understand and support the work rather than losing confidence. Open actions list an owner and a due date. Managers can ask for more detail, which Elena provides in a short appendix rather than crowding the main page.

### Worked example

The monthly routine takes about two hours; the first summary shows coverage at 90 percent and all leavers that month disabled within a day.

> **Synthetic case.** Routines, figures and reports are synthetic.

### Errors and limits

Undocumented routines stop when the person who knows them is away.

### Exercises

- **EX085 — Routine tasks.** Name three monthly routine tasks. *Rubric:* 3 = identity report, leaver check, admin review, MFA coverage, unused accounts (three);; 2 = two;; 1 = one;; 0 = none.
- **EX086 — Direct permissions rule.** How does IT grant access after approval? *Rubric:* 3 = adds to a group, never individual permissions;; 2 = groups;; 1 = direct;; 0 = none.
- **EX087 — Summary contents.** What does each summary figure show? *Rubric:* 3 = this month, last month and target;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Written routines, recorded requests and short monthly summaries keep identity management running.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) test the full lifecycle end to end; (2) test recovery and failure handling; (3) compare with Laboratory I.

### 30.1 End-to-end lifecycle

Laboratory II tests the whole lifecycle in the trial tenant: a synthetic joiner is created from a test HR record and gains team access; they move team and lose old groups after the grace period; they leave and are disabled the same evening, with a report listing their finance account. Elena checks each step's timing and result. End-to-end tests catch problems that single-control tests miss, such as a mover whose grace period never ended because of a date format. Each run is recorded with its timings.

### 30.2 Recovery and failure tests

Elena also tests what happens when things go wrong. A synthetic operative loses a security key: the recovery steps are followed and the lost key is revoked. The HR test file is missing one night: the evening job must stop and alert rather than treat everyone as leavers. A synthetic administrator account is used outside working hours: an alert must reach the IT lead. Testing failure handling is essential, because these paths are rarely used and therefore often broken. Each result is logged as evidence.

### 30.3 Comparing with Laboratory I

Laboratory II runs thirty tests, twenty-nine of which pass. The single failure is the missing HR file test: the job stopped but sent no alert. It is fixed and retested. Compared with Laboratory I, more tests cover failure paths and end-to-end flows, and the earlier failures stay fixed, confirmed by rerunning them. Elena records results in the same evidence format, showing steady progress and giving the IT lead confidence before the capstone changes go live. The IT lead signs off the results before go-live.

### Worked example

Twenty-nine of thirty Laboratory II tests pass; the missing-HR-file job stopped safely but sent no alert, which is fixed and retested.

> **Synthetic case.** Tests and failures are synthetic.

### Errors and limits

A job that treats a missing HR file as everyone leaving would disable every account at once.

### Exercises

- **EX088 — Lab II result.** How many Laboratory II tests passed? *Rubric:* 3 = 29 of 30;; 2 = 29;; 1 = 30;; 0 = none.
- **EX089 — Missing file behaviour.** What must the evening job do if the HR file is missing? *Rubric:* 3 = stop and alert, not disable everyone;; 2 = stop;; 1 = disable;; 0 = none.
- **EX090 — Rerun purpose.** Why rerun Laboratory I tests? *Rubric:* 3 = confirm earlier fixes stay fixed;; 2 = regression;; 1 = none;; 0 = none.

### Synthesis

End-to-end and failure-path tests show the lifecycle works and fails safely.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Identity and access management: advanced cases

### Learning outcomes

You will (1) handle contractors and volunteers; (2) manage service accounts; (3) consider tenants' identities in online services.

### 31.1 Contractors and volunteers

Greenhill uses contractors for repairs and volunteers for community events. They need some access but are not in HR. Elena designs a sponsor model: each contractor or volunteer has a named Greenhill sponsor, an account with an end date and access only to what their work needs. Sponsors confirm continued need every three months. Accounts expire automatically on the end date. This keeps people outside HR inside the lifecycle, rather than creating accounts that nobody remembers to remove. The sponsor list is reviewed every quarter.

### 31.2 Service accounts

The finance system's two service accounts send payment files and receive bank statements. They have passwords that never change and broad permissions. Elena recommends documenting each service account's owner, purpose and permissions; reducing permissions to what the task needs; storing credentials in a protected vault rather than a file; and rotating them on a schedule agreed with the supplier. Service accounts are often forgotten in reviews, yet their access can be as powerful as any administrator's. Each change is agreed with the finance supplier in advance.

### 31.3 Tenant identities

Greenhill plans an online portal where tenants can report repairs and pay rent. Tenants are a very different population: some are elderly, some have no smartphone, and many share devices with family. Elena notes that tenant identity needs separate thinking from staff identity: simple sign-in options, accessible recovery and protection against someone else in the household acting for a tenant without consent. She records this as future work, outside her current scope, so it is not forgotten. The note is shared with the portal project team.

### Worked example

Twelve contractors and volunteers move to sponsored, expiring accounts; two finance service accounts are documented, reduced and moved to a vault.

> **Synthetic case.** People, accounts and plans are synthetic.

### Errors and limits

Creating contractor accounts outside any lifecycle leaves access long after work ends.

### Exercises

- **EX091 — Sponsor role.** What does a contractor's sponsor do? *Rubric:* 3 = confirms need every three months;; 2 = confirms need;; 1 = pays;; 0 = none.
- **EX092 — Service account steps.** Name two service account improvements. *Rubric:* 3 = document owner, reduce permissions, vault storage, rotation (two);; 2 = one;; 1 = none;; 0 = none.
- **EX093 — Tenant concern.** Name one tenant identity concern. *Rubric:* 3 = no smartphone, shared devices, accessible recovery, household consent (one);; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Sponsors, managed service accounts and separate thinking for tenants extend IAM beyond employees.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Identity and access management: interdisciplinary interfaces

### Learning outcomes

You will (1) work with HR, finance and legal colleagues; (2) align identity with data protection duties; (3) communicate across disciplines.

### 32.1 Working with HR

HR is the source of truth for joiners, movers and leavers, so Elena works closely with the HR officer. She explains why timely, accurate dates matter and agrees simple rules: leaving dates are entered as soon as resignation is accepted, team moves are entered before the move date, and corrections are flagged. HR in turn asks for a monthly list of accounts without HR matches, which helps them find records they forgot to update. Each discipline benefits from the other's information.

### 32.2 Finance and legal

Finance cares about separation of duties and audit evidence; legal cares about data protection and contracts with suppliers. Elena meets both. Finance agrees the second approval for new suppliers and asks for a yearly list of finance access for auditors. Legal reviews her data handling and confirms that sign-in logs may be kept for a year for security purposes, documented in Greenhill's records of processing. Each discussion is recorded with decisions and owners. Follow-up meetings are scheduled every six months to keep the arrangements current and to review any new systems.

### 32.3 Speaking across disciplines

Each discipline uses different words. HR says starters and leavers; IT says provisioning and deprovisioning; finance says segregation of duties. Elena keeps a short glossary and uses the listener's terms. She frames identity work in each group's concerns: for HR, fewer chases from IT; for finance, cleaner audits; for legal, demonstrable compliance. Speaking others' language turns identity from an IT project into shared work that colleagues support. She also checks understanding by asking colleagues to explain decisions back in their own words, which quickly reveals misunderstandings before they cause problems in practice.

### Worked example

HR agrees timely date rules, finance agrees second supplier approval and yearly access lists, and legal confirms one-year log retention.

> **Synthetic case.** Colleagues and agreements are synthetic.

### Errors and limits

Treating identity as purely an IT project leaves HR, finance and legal unaware of their part.

### Exercises

- **EX094 — HR benefit.** What does HR receive from the identity work? *Rubric:* 3 = monthly list of accounts without HR match;; 2 = list;; 1 = nothing;; 0 = none.
- **EX095 — Legal decision.** What did legal confirm about logs? *Rubric:* 3 = one-year retention for security, documented;; 2 = one year;; 1 = forever;; 0 = none.
- **EX096 — Glossary purpose.** Why does Elena keep a glossary? *Rubric:* 3 = different disciplines use different terms;; 2 = terms;; 1 = exam;; 0 = none.

### Synthesis

Working with HR, finance and legal, and speaking their language, makes identity a shared responsibility.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) design a before-and-after evaluation; (2) choose measures and comparison; (3) plan analysis in advance.

### 33.1 Evaluation design

For her capstone, Elena plans to evaluate whether the new identity processes improved Greenhill's position. She uses a before-and-after design: measure key indicators for three months before changes and three months after. Because there is no separate comparison group at a small organisation, she records other events that could affect results, such as staff turnover or a new system, so she can discuss alternative explanations honestly rather than assuming every improvement came from her changes. The plan is agreed with her supervisor before any change is made.

### 33.2 Choosing measures

Elena chooses five measures already defined in earlier chapters: multi-factor coverage, leavers disabled within one day, shared accounts, administrator accounts and unused paid licences. Each has a definition, a data source and a target. She avoids adding new measures after seeing results, which would let her pick whichever looked best. She also decides in advance how she will treat missing data, such as a month when an export failed, so that choices are not made to favour a particular outcome.

### 33.3 Analysis plan

The analysis plan states that for each measure she will report before and after values with counts, the change and whether the target was met. With small numbers, she will not use statistical tests that need large samples; instead she will describe changes carefully and discuss possible alternative explanations. Her supervisor approves the plan before the after period begins. Writing it down first is what makes the evaluation trustworthy, because the method was fixed before the answer was known. The approved plan is stored with her evidence.

### Worked example

Elena's plan fixes five measures, three-month periods before and after, a record of other events and a descriptive analysis approved before changes go live.

> **Synthetic case.** Measures, periods and plans are synthetic.

### Errors and limits

Choosing measures after seeing results lets an evaluation report whichever looks best.

### Exercises

- **EX097 — Comparison limit.** Why does Elena record other events during the evaluation? *Rubric:* 3 = no comparison group, so alternatives must be discussed;; 2 = alternatives;; 1 = habit;; 0 = none.
- **EX098 — Five measures.** List the five evaluation measures. *Rubric:* 3 = MFA coverage, leavers within a day, shared accounts, admin accounts, unused licences;; 2 = four;; 1 = two;; 0 = none.
- **EX099 — Statistical caution.** Why avoid tests needing large samples? *Rubric:* 3 = numbers are small;; 2 = small n;; 1 = cost;; 0 = none.

### Synthesis

A planned before-and-after evaluation with fixed measures and honest discussion of alternatives gives credible results.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two approaches to a problem; (2) use clear criteria; (3) recommend with evidence.

### 34.1 The problem

Greenhill must decide how repairs operatives sign in on shared tablets. Elena compares two approaches. Option one gives each operative a security key that works with the tablets, signing in at the start of each job. Option two gives each operative a work phone with a passkey and the repairs app, retiring shared tablets. Both remove the shared account. The comparison helps Greenhill choose wisely rather than adopting whichever idea was suggested first. Repairs managers, operatives and IT all take part in the comparison from the start.

### 34.2 Criteria and evidence

Elena agrees criteria with the repairs manager: security, cost over three years, ease of use with gloves and in vans, effect on job speed and support effort. She gathers evidence through a two-week trial of each option with three volunteers, supplier prices and IT estimates. Keys are cheaper and quick to use but easy to leave in vans; phones cost more but combine sign-in, job details and photos of completed work. Each score is recorded with its evidence. Volunteers' comments are recorded verbatim.

### 34.3 Recommendation

Elena recommends security keys now, because they solve the shared account quickly and cheaply, with a key holder on each operative's lanyard to reduce losses. She suggests reconsidering work phones when tablets are due for replacement in two years, since phones then offer extra benefits. The recommendation states its reasons, its weaknesses and what would change it. The repairs manager agrees, and the decision is recorded so the later review can check whether the reasoning held. The cost difference is shown over three years.

### Worked example

The comparison scores keys higher on cost and speed and phones higher on extra features; Elena recommends keys now and a phone review at tablet replacement.

> **Synthetic case.** Options, trials and prices are synthetic.

### Errors and limits

Choosing the first suggested option without comparison can miss a cheaper or better alternative.

### Exercises

- **EX100 — Two options.** What two options are compared? *Rubric:* 3 = security keys on tablets vs work phones with passkeys;; 2 = both;; 1 = one;; 0 = none.
- **EX101 — Key weakness.** What is the main weakness of keys in the trial? *Rubric:* 3 = easily left in vans;; 2 = lost;; 1 = cost;; 0 = none.
- **EX102 — Phone review timing.** When should work phones be reconsidered? *Rubric:* 3 = when tablets are replaced in two years;; 2 = later;; 1 = never;; 0 = none.

### Synthesis

Comparing options against agreed criteria with trial evidence leads to clear, revisitable decisions.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) define the capstone scope and objectives; (2) plan tasks, risks and evidence; (3) obtain approval.

### 35.1 Scope and objectives

Elena's capstone aims to improve Greenhill's identity hygiene in one cycle: raise multi-factor coverage above 95 percent, disable all leavers within one day, remove both shared accounts, reduce administrator accounts to four and remove unused paid licences. Each objective is linked to a measure from her evaluation plan. The scope covers staff, contractors and the two service accounts across six systems, and excludes the future tenant portal, which she has recorded as later work. Each objective has a named owner at Greenhill and a target date within the year.

### 35.2 Tasks and risks

Tasks include enrolling the repairs team with security keys, launching the HR-driven leaver job, replacing reception's shared login, reducing administrators and reviewing licences. Each task has an owner, a date and a test from her laboratories. Risks include operatives losing keys, HR dates being late and a supplier delay for repairs app sign-in. Each risk has a response, such as spare keys at the depot. The plan is realistic for her final year alongside other studies. The plan is reviewed with her supervisor every fortnight.

### 35.3 Approval

Elena presents the proposal to Dr Asante and Greenhill's IT lead and chief executive. They ask about disruption to repairs work and agree that enrolment will happen at the depot before shifts start. Approval is recorded in writing, together with her permission letter, now updated to cover supervised production changes made by the IT team. Formal approval protects everyone and ensures that the capstone's changes are Greenhill's decisions, carried out with Elena's support. Copies of the approval are kept by Greenhill, the university and Elena, and any later change in scope requires the same approval again.

### Worked example

The approved proposal sets five measurable objectives, eleven tasks with owners and tests, and four risks with responses.

> **Synthetic case.** Objectives, tasks and approvals are synthetic.

### Errors and limits

Starting production changes without written approval blurs who decided and who is responsible.

### Exercises

- **EX103 — Coverage objective.** What multi-factor coverage does the capstone target? *Rubric:* 3 = above 95 percent;; 2 = 95%;; 1 = 100%;; 0 = none.
- **EX104 — Excluded item.** What does the capstone scope exclude? *Rubric:* 3 = future tenant portal;; 2 = tenants;; 1 = finance;; 0 = none.
- **EX105 — Approval update.** What changed in Elena's permission letter? *Rubric:* 3 = covers supervised production changes by IT;; 2 = production;; 1 = nothing;; 0 = none.

### Synthesis

A scoped, measurable, risk-aware and approved proposal sets up the capstone for success.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) support real users during change; (2) run enrolment sessions; (3) gather feedback respectfully.

### 36.1 Enrolment sessions

Elena and the IT team run enrolment sessions at the depot before shifts start. Each operative receives a security key, registers it with their account and practises signing in to the repairs app on a tablet. Sessions are short, practical and friendly. Elena brings printed one-page guides with pictures. Doing enrolment in person, where people work, solves problems on the spot, such as gloves, and is far more successful than sending instructions by email. Attendance is recorded, and anyone who misses a session is offered another slot within the same week.

### 36.2 Supporting users

Some operatives are nervous about technology or worried about being blamed for losing keys. Elena reassures them that losses happen, explains the simple recovery process and gives each a key holder for their lanyard. She notes every question and problem in a log, such as one tablet with a faulty port, which IT replaces. Supporting users respectfully builds trust, and trust is what makes new security habits stick after the project team leaves. The log is reviewed after each session, and recurring problems are fixed before the next one.

### 36.3 Gathering feedback

A week after enrolment, Elena asks operatives three short questions: is signing in easier or harder, has anything gone wrong and what would help. Most say signing in is quicker than the old shared password once they are used to it; two mention forgetting keys in vans. She feeds this back to the repairs manager, who adds a key check to the van checklist. Gathering feedback shows people their views matter and quickly finds practical improvements. Responses are anonymous unless people choose otherwise.

### Worked example

Thirty-eight of forty operatives enrol in two depot sessions; feedback finds sign-in quicker for most and leads to a van key check.

> **Synthetic case.** Sessions, operatives and feedback are synthetic.

### Errors and limits

Sending enrolment instructions by email to staff who rarely use it leads to low uptake.

### Exercises

- **EX106 — Enrolment place.** Where are enrolment sessions held, and when? *Rubric:* 3 = at the depot before shifts;; 2 = depot;; 1 = online;; 0 = none.
- **EX107 — Enrolment count.** How many operatives enrol in the sessions? *Rubric:* 3 = 38 of 40;; 2 = 38;; 1 = 40;; 0 = none.
- **EX108 — Feedback action.** What action came from feedback about forgotten keys? *Rubric:* 3 = key check added to van checklist;; 2 = checklist;; 1 = none;; 0 = none.

### Synthesis

In-person enrolment, respectful support and quick feedback make security changes work for real people.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) present evidence to peers; (2) respond to challenge; (3) improve the evaluation.

### 37.1 Presenting evidence

In a university seminar, Elena presents her capstone evidence to classmates and two lecturers. She shows her measures, data sources, test results and early after-period figures, and explains her limitations. The aim is not to impress but to find weaknesses before her final evaluation. She prepares by checking every number against its source and making sure each chart shows counts as well as percentages, so the audience can judge the evidence themselves. She also brings copies of her evaluation plan, so the audience can check that the analysis follows what was agreed in advance.

### 37.2 Challenges

A classmate asks whether multi-factor coverage rose simply because twelve unused accounts were disabled, shrinking the base. A lecturer asks whether one quiet month for leavers proves anything. Both are fair. Elena checks: disabling unused accounts raised coverage by about two points, so most of the rise came from enrolment. On leavers, she agrees one month is too little and extends her after period to three full months, as her plan required. She thanks both questioners and writes down each challenge in her project log before responding with evidence.

### 37.3 Improving the evaluation

The seminar improves her evaluation. She adds a note separating coverage changes due to enrolment from those due to account clean-up, reports leavers over the full three months and adds a short section on alternative explanations, such as a new IT staff member joining. She thanks participants and records changes in her project log. Welcoming challenge, rather than defending every point, is a sign of mature evidence work. Her supervisor reviews the changes and confirms that they follow the original plan rather than altering it after results were seen, which protects the credibility of the final evaluation.

### Worked example

Seminar challenges lead Elena to separate enrolment from clean-up effects on coverage (about two points from clean-up) and to report leavers over three full months.

> **Synthetic case.** Seminar participants and figures are synthetic.

### Errors and limits

Ignoring changes in a measure's base can credit an intervention with an improvement that came from clean-up.

### Exercises

- **EX109 — Base challenge.** What did the classmate's question concern? *Rubric:* 3 = coverage rising because unused accounts shrank the base;; 2 = base;; 1 = cost;; 0 = none.
- **EX110 — Clean-up effect.** How much of the coverage rise came from clean-up? *Rubric:* 3 = about two points;; 2 = small;; 1 = all;; 0 = none.
- **EX111 — Leaver period.** How was the leaver evaluation period fixed? *Rubric:* 3 = extended to three full months;; 2 = longer;; 1 = one month;; 0 = none.

### Synthesis

Presenting evidence to challenge and responding openly makes the final evaluation stronger.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) deliver capstone changes safely; (2) track progress against the plan; (3) handle problems openly.

### 38.1 Delivering changes

With approval, the IT team makes the capstone changes in planned order, with Elena supporting and recording. The HR-driven leaver job goes live first, after a final test. Repairs enrolment follows, then reception's individual accounts, then administrator reduction and licence clean-up. Each change happens at a quiet time with a rollback plan, and each is checked afterwards against its test. Doing one change at a time means any problem can be traced to its cause quickly. Each change is announced to staff beforehand.

### 38.2 Tracking progress

Elena tracks each task on a simple board: planned, in progress, done and verified. A task counts as done only when its test passes in production. She reports weekly to the IT lead and her supervisor. By the end of the second month, nine of eleven tasks are verified. The remaining two are the repairs app single sign-on, waiting on the supplier, and the final service account rotation, scheduled with the finance supplier. Delays are explained in the weekly report, with new dates agreed with the owners concerned.

### 38.3 Handling problems

Two problems arise. The leaver job disables a contractor whose end date was entered wrongly; the sponsor notices within an hour and access is restored, and the sponsor process now asks for date confirmation. The repairs supplier delays single sign-on by a month; meanwhile operatives use individual app accounts with their security keys through the provider. Elena records both openly in the project log, with causes and fixes, because hiding problems would make the evaluation untrustworthy. Both are reviewed at the next weekly meeting.

### Worked example

Nine of eleven tasks are verified by month two; a wrongly dated contractor is restored within an hour and a supplier delay is handled with an interim arrangement.

> **Synthetic case.** Tasks, problems and dates are synthetic.

### Errors and limits

Marking tasks done before verifying them in production overstates progress.

### Exercises

- **EX112 — Done definition.** When does a task count as done? *Rubric:* 3 = its test passes in production;; 2 = verified;; 1 = deployed;; 0 = none.
- **EX113 — Remaining tasks.** Which two tasks remain after month two? *Rubric:* 3 = repairs app SSO and service account rotation;; 2 = two;; 1 = none;; 0 = none.
- **EX114 — Contractor fix.** What process change followed the wrongly disabled contractor? *Rubric:* 3 = sponsor confirms end dates;; 2 = date confirmation;; 1 = none;; 0 = none.

### Synthesis

One change at a time, verified progress and openly handled problems deliver the capstone safely.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) compare before and after measures; (2) judge each against its target; (3) discuss alternative explanations.

### 39.1 Collecting results

After three months, Elena collects the after-period values using exactly the same definitions and queries as the before period. She checks each against its source and records the export dates. Where data is missing, she follows her plan. She also gathers her log of other events during the period, such as two new starters and one system update, so she can discuss them when interpreting results. She stores the after-period exports alongside the before-period files in the same folder structure, and records the script version used for each calculation, so anyone can repeat the comparison exactly.

### Lab — Before and after

```python
"""Before/after evaluation of synthetic access-hygiene measures for the capstone (stdlib only)."""
m = [("MFA coverage %", 77.1, 97.9, "up"), ("Leavers disabled within 1 day %", 50.0, 100.0, "up"),
     ("Shared accounts", 2, 0, "down"), ("Admin accounts", 9, 4, "down"), ("Unused licences", 23, 6, "down")]
for name, b, a, d in m:
    ok = (a > b) if d == "up" else (a < b)
    print(f"{name:34} before={b:<6} after={a:<6} {'improved' if ok else 'not improved'}")
```

Run with `python3 lab_eval.py`. Verified output:

```text
MFA coverage %                     before=77.1   after=97.9   improved
Leavers disabled within 1 day %    before=50.0   after=100.0  improved
Shared accounts                    before=2      after=0      improved
Admin accounts                     before=9      after=4      improved
Unused licences                    before=23     after=6      improved
```

### 39.2 Reading the results

All five measures improved. Multi-factor coverage rose from 77.1 to 97.9 percent, above the 95 percent target, with about two points from clean-up. Leavers disabled within one day rose from 50 to 100 percent over the after period. Both shared accounts were removed. Administrator accounts fell from nine to four. Unused paid licences fell from 23 to 6, saving money that helps justify the work. Elena reports these with counts and notes that small numbers, especially for leavers, mean results should be confirmed over a longer period.

### 39.3 Alternative explanations

Could anything else explain the improvements? The leaver result could partly reflect fewer leavers in the after period, so she reports counts: nine before and seven after. Coverage gains could reflect clean-up, which she has separated. The new IT staff member may have helped with administrator reduction, which she acknowledges. None of these explains the overall pattern, which matches the timing of each change. She concludes the changes very likely caused most of the improvement, with stated uncertainty. Her supervisor agrees with this reading.

### Worked example

All five measures improve, including coverage from 77.1 to 97.9 percent and leavers within a day from 50 to 100 percent; alternatives are discussed with counts.

> **Synthetic case.** Measures, counts and events are synthetic.

### Errors and limits

Claiming every improvement was caused by the project without discussing alternatives overstates the evidence.

### Exercises

- **EX115 — Coverage change.** How did multi-factor coverage change in the lab? *Rubric:* 3 = 77.1% to 97.9%, above target;; 2 = rose;; 1 = fell;; 0 = none.
- **EX116 — Licence saving.** How did unused licences change? *Rubric:* 3 = 23 to 6;; 2 = fell;; 1 = rose;; 0 = none.
- **EX117 — Leaver counts.** How many leavers were in each period? *Rubric:* 3 = nine before, seven after;; 2 = counts;; 1 = none;; 0 = none.

### Synthesis

Consistent measurement, targets and honest discussion of alternatives make the capstone evaluation credible.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write the bachelor's thesis; (2) present findings clearly; (3) reflect on learning and next steps.

### 40.1 The thesis

Elena's thesis tells the story of her project: Greenhill's situation, the problems found, the methods designed, the tests, the capstone changes and the evaluation. Each chapter has a clear purpose and links to evidence in appendices. She states findings plainly, discusses limits honestly and makes recommendations for Greenhill's next steps, including the tenant portal and work phones at tablet replacement. Her supervisor reviews drafts, and she revises them in response to comments. Appendices hold test evidence, scripts, the evaluation plan and anonymised feedback summaries, so examiners can check her claims.

### 40.2 The presentation

Elena presents to examiners and Greenhill's managers in fifteen minutes. She starts with the problem in plain words, shows the five measures before and after with one simple chart, explains what made the biggest difference and states what remains. She answers questions with evidence, such as the leaver counts when asked about small samples. Managers appreciate that she explains both successes and limits, and the IT lead asks to keep using her monthly routine. Slides are shared with attendees afterwards.

### 40.3 Reflection

In her reflection, Elena notes that the hardest parts were not technical but human: getting timely HR dates, supporting nervous operatives and agreeing changes with finance. She learned to measure before acting, to test safely and to report honestly. Her next step is a job in an IT team, where she plans to apply the same habits. She leaves Greenhill with documentation, routines and evidence, so the improvements continue after her placement ends. She thanks the Greenhill staff who helped, and offers to answer questions during the first months after she leaves.

### Worked example

Elena's thesis and fifteen-minute presentation report five improved measures, limits and recommendations; Greenhill adopts her monthly routine.

> **Synthetic case.** The thesis, presentation and outcomes are synthetic.

### Errors and limits

Presenting only successes without limits reduces trust from managers and examiners.

### Exercises

- **EX118 — Presentation chart.** What does Elena's one simple chart show? *Rubric:* 3 = five measures before and after;; 2 = measures;; 1 = costs;; 0 = none.
- **EX119 — Hardest parts.** What did Elena find hardest? *Rubric:* 3 = human parts: HR dates, nervous users, agreeing with finance;; 2 = people;; 1 = coding;; 0 = none.
- **EX120 — Lasting asset.** What did Greenhill ask to keep using? *Rubric:* 3 = Elena's monthly routine;; 2 = routine;; 1 = laptop;; 0 = none.

### Synthesis

A clear thesis, honest presentation and thoughtful reflection complete the bachelor's journey.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Elena Petrova, Dr Kwame Asante, Westmere University, Greenhill Community Housing and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Because the base shows the real size of the gap, and the one missing administrator may be critical.

**EX002.** Ten percentage points, a twenty percent relative increase.

**EX003.** About 140 staff.

**EX004.** Because IT may disable the main account but forget the separate ones.

**EX005.** The housing management system and the finance system.

**EX006.** It uses the office suite's accounts directly, so staff sign in once.

**EX007.** A plain text table with one line per record.

**EX008.** By treating department names case-insensitively.

**EX009.** 140 enabled of 152 accounts.

**EX010.** A point, the evidence for it and an explanation of what it means.

**EX011.** NIST SP 800-63B-4.

**EX012.** With words such as suggests or may.

**EX013.** Who people are when they sign in and what they are allowed to do.

**EX014.** Nobody can tell which person performed an action.

**EX015.** Avoid them unless there is a reason, because they push people towards predictable patterns.

**EX016.** Set difference: enabled accounts minus current HR staff.

**EX017.** As the union of the permissions of all their groups.

**EX018.** Seven.

**EX019.** It encrypts traffic and confirms the server's identity.

**EX020.** One place to sign in, enforce multi-factor and disable access.

**EX021.** Passkeys or security keys based on WebAuthn, which only work with the real site.

**EX022.** With an HR-maintained mapping table from employee number to email address.

**EX023.** A surname change and a typo.

**EX024.** Her role is to provide accurate evidence; the IT lead decides actions.

**EX025.** To compare months and measure trends such as leaver timeliness.

**EX026.** Nine.

**EX027.** Two years, as agreed with the data protection lead.

**EX028.** Signing in as an administrator and testing passwords (also bypass attempts).

**EX029.** Factually to the IT lead, without blame.

**EX030.** Report it immediately, preserve the evidence and take no further action herself.

**EX031.** Any harmful file the user opens gets administrator power too.

**EX032.** Four.

**EX033.** Unique, automatically rotated local passwords stored centrally with views logged.

**EX034.** Because a few long delays pull the mean up and hide the typical case.

**EX035.** Because about ten leavers a month makes monthly figures vary a lot by chance.

**EX036.** That the improvement coincided with the change, not that it caused it.

**EX037.** Identification, authentication and authorisation.

**EX038.** The key checks the website it talks to; a typed code can be passed to a fake site.

**EX039.** They keep their old access indefinitely.

**EX040.** Staff home addresses in the old finance system.

**EX041.** It is a different purpose from security and breaks purpose limitation and trust.

**EX042.** Security keys provided by Greenhill.

**EX043.** 108 of 140, or 77.1 percent.

**EX044.** Repairs, at 55.0 percent (22 of 40).

**EX045.** Because administrator accounts can change everything, so one gap there carries high harm.

**EX046.** The cloud office suite.

**EX047.** In the housing management system, which understands its own data.

**EX048.** Multi-factor for everyone, security keys for administrators, leavers disabled on their last day and access by team groups.

**EX049.** The output of a one-way function, stored instead of the password itself.

**EX050.** On the user's device.

**EX051.** Sign-in failure for every connected system at once.

**EX052.** It is too broad to answer with one study.

**EX053.** It showed tablets staying signed in under shared accounts, which interviews missed.

**EX054.** The purpose and that taking part is voluntary (also anonymity).

**EX055.** A finance system service account that sends payment files.

**EX056.** One finance officer could both set up new suppliers and pay them.

**EX057.** Role-based access through team groups with a short list of documented exceptions.

**EX058.** Removal must be triggered automatically from HR and checked across every system.

**EX059.** Features such as shared mailboxes, used with individual accounts.

**EX060.** Regular access reviews and removing old access when people move.

**EX061.** Removal of the person's old access.

**EX062.** Two emails, either of which can be delayed or lost.

**EX063.** Because much identity management depends on people passing messages, not only technology.

**EX064.** reception and repairs1.

**EX065.** Its sign-ins at different sites are hours apart, which is normal.

**EX066.** Payment files to suppliers stop.

**EX067.** The HR leaving date, compared with accounts each evening.

**EX068.** Office suite accounts on the repairs app, with security keys on the tablets.

**EX069.** At the end of their last day, so final payroll tasks can be completed.

**EX070.** They can be intercepted or passed to fake sites more easily.

**EX071.** Four, reduced from nine.

**EX072.** Each person's name, groups and last sign-in.

**EX073.** So mistakes cannot affect real staff.

**EX074.** 18 of 20.

**EX075.** The evening job ignored leaving dates entered with a time.

**EX076.** Median 1.5 days, maximum 31 days, and five of ten over the one-day target.

**EX077.** Holiday periods, when HR's email waited in an absent colleague's inbox.

**EX078.** Two weeks, then old groups are removed automatically.

**EX079.** Configured means the setting exists; effective means real sign-ins actually use it.

**EX080.** To avoid unconsciously picking easy cases.

**EX081.** Checks for accounts created outside the HR process, such as supplier test accounts.

**EX082.** By calling back the operative's manager on a known number.

**EX083.** Paper emergency tenant contacts at reception (also printed job lists or an emergency admin key).

**EX084.** A group rename that was not tested first.

**EX085.** Running the identity report, checking leavers and reviewing administrators (also coverage and unused accounts).

**EX086.** By adding the person to a group, never granting individual permissions directly.

**EX087.** This month, last month and the target.

**EX088.** 29 of 30.

**EX089.** Stop and send an alert, not treat everyone as leavers.

**EX090.** To confirm the earlier failures remain fixed.

**EX091.** Confirms the contractor's continued need every three months.

**EX092.** Reduce permissions and store credentials in a vault (also document owner and rotate).

**EX093.** Many tenants share devices with family (also no smartphone or accessible recovery).

**EX094.** A monthly list of accounts without an HR match, to find unupdated records.

**EX095.** That sign-in logs may be kept for one year for security, documented in processing records.

**EX096.** Because HR, IT and finance use different words for the same things.

**EX097.** Because there is no comparison group, so other explanations must be considered.

**EX098.** Multi-factor coverage, leavers disabled within a day, shared accounts, administrator accounts and unused licences.

**EX099.** Because Greenhill's numbers are small.

**EX100.** Security keys on shared tablets versus work phones with passkeys.

**EX101.** They are easily left in vans.

**EX102.** When tablets are due for replacement in two years.

**EX103.** Above 95 percent.

**EX104.** The future tenant portal.

**EX105.** It now covers supervised production changes made by the IT team.

**EX106.** At the depot before shifts start.

**EX107.** 38 of 40.

**EX108.** A key check was added to the van checklist.

**EX109.** Whether coverage rose because disabling unused accounts shrank the base.

**EX110.** About two percentage points.

**EX111.** It was extended to three full months as planned.

**EX112.** Only when its test passes in production.

**EX113.** Repairs app single sign-on and the final service account rotation.

**EX114.** The sponsor process now asks for confirmation of end dates.

**EX115.** From 77.1 to 97.9 percent, above the 95 percent target.

**EX116.** From 23 to 6.

**EX117.** Nine before and seven after.

**EX118.** The five measures before and after.

**EX119.** The human parts: timely HR dates, supporting operatives and agreeing changes with finance.

**EX120.** Her monthly identity routine.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Bonneau, J., Herley, C., van Oorschot, P. C., & Stajano, F. (2012). The quest to replace passwords: A framework for comparative evaluation of web authentication schemes. *2012 IEEE Symposium on Security and Privacy*, 553–567. <https://doi.org/10.1109/SP.2012.44>
- Ferraiolo, D. F., Sandhu, R., Gavrila, S., Kuhn, D. R., & Chandramouli, R. (2001). Proposed NIST standard for role-based access control. *ACM Transactions on Information and System Security*, 4(3), 224–274. <https://doi.org/10.1145/501978.501980>
- Florêncio, D., & Herley, C. (2007). A large-scale study of web password habits. *Proceedings of the 16th International Conference on World Wide Web*, 657–666. <https://doi.org/10.1145/1242572.1242661>
- Hardt, D. (Ed.). (2012). *The OAuth 2.0 authorization framework* (RFC 6749). IETF. <https://www.rfc-editor.org/rfc/rfc6749>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Hu, V. C., Ferraiolo, D., Kuhn, R., Schnitzer, A., Sandlin, K., Miller, R., & Scarfone, K. (2014). *Guide to attribute based access control (ABAC) definition and considerations* (NIST SP 800-162). NIST. <https://doi.org/10.6028/NIST.SP.800-162>
- Hunt, P. (Ed.), Grizzle, K., Ansari, M., Wahlstroem, E., & Mortimore, C. (2015). *System for Cross-domain Identity Management: Protocol* (RFC 7644). IETF. <https://www.rfc-editor.org/rfc/rfc7644>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Jones, M., Bradley, J., & Sakimura, N. (2015). *JSON Web Token (JWT)* (RFC 7519). IETF. <https://www.rfc-editor.org/rfc/rfc7519>
- Kuhn, D. R., Coyne, E. J., & Weil, T. R. (2010). Adding attributes to role-based access control. *Computer*, 43(6), 79–81. <https://doi.org/10.1109/MC.2010.155>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lodderstedt, T., Bradley, J., Labunets, A., & Fett, D. (2025). *Best current practice for OAuth 2.0 security* (RFC 9700, BCP 240). IETF. <https://www.rfc-editor.org/rfc/rfc9700>
- Molloy, I., Chen, H., Li, T., Wang, Q., Li, N., Bertino, E., Calo, S., & Lobo, J. (2008). Mining roles with semantic meanings. *Proceedings of the 13th ACM Symposium on Access Control Models and Technologies*, 21–30. <https://doi.org/10.1145/1377836.1377840>
- OASIS. (2005). *Assertions and protocols for the OASIS Security Assertion Markup Language (SAML) V2.0*. OASIS Standard. <https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Sakimura, N., Bradley, J., & Agarwal, N. (2015). *Proof Key for Code Exchange by OAuth public clients* (RFC 7636). IETF. <https://www.rfc-editor.org/rfc/rfc7636>
- Sakimura, N., Bradley, J., Jones, M., de Medeiros, B., & Mortimore, C. (2014). *OpenID Connect Core 1.0*. OpenID Foundation. <https://openid.net/specs/openid-connect-core-1_0.html>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. *Computer*, 29(2), 38–47. <https://doi.org/10.1109/2.485845>
- Temoshok, D., Proud-Madruga, D., Choong, Y.-Y., Galluzzo, R., Gupta, S., LaSalle, C., Lefkovitz, N., & Regenscheid, A. (2025). *Digital identity guidelines* (NIST SP 800-63-4). NIST. <https://doi.org/10.6028/NIST.SP.800-63-4>
- Temoshok, D., Fenton, J. L., Choong, Y.-Y., Lefkovitz, N., Regenscheid, A., Galluzzo, R., & Richer, J. P. (2025). *Digital identity guidelines: Authentication and authenticator management* (NIST SP 800-63B-4). NIST. <https://doi.org/10.6028/NIST.SP.800-63B-4>
- W3C. (2021). *Web Authentication: An API for accessing public key credentials, Level 2*. W3C Recommendation. <https://www.w3.org/TR/webauthn-2/>
