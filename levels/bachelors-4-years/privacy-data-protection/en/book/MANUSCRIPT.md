# Privacy and Data Protection: Bachelor's Course

- Language: English (`en`); course 096, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; six offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students learning to protect children's and families' data in a multi-school education trust.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs query a SQLite app register, compute Wilson intervals for a parent survey, summarise access-request times, score classroom apps, suppress small cells and match photographs against consent records, all on synthetic data. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one bachelor's student through four years centred on a schools trust: foundations, systems and programming, writing and security literacy, data and ethics, identity and privacy foundations, measurement, architecture and research, scope and cases, models and dependencies, disclosure control and controls, laboratories, consent, verification, failure analysis and operations, hard cases, interdisciplinary work, research, comparison, community practice and a capstone parent portal. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Elena Rossi** | Bachelor's student | Invented |
| **Dr. Kwame Asante** | Tutor | Invented |
| **Fairhaven College** | Fictional college | Invented |
| **Brindle Valley Schools Trust** | Fictional trust of 12 primary schools, about 6,000 pupils | Invented |
| **Harrow Lane Academy** | Fictional comparison school | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR), including Recital 38 and Articles 7, 8, 28, 30 and 33; Lei 13.709/2018 (LGPD), including Article 14; EDPB Guidelines 05/2020, 07/2020, 01/2022 and 9/2022; WP248 rev.01; NIST SP 800-188; Sweeney (2002); Narayanan and Shmatikov (2008); Solove (2006); Nissenbaum (2004); Acquisti et al. (2015); Warren and Brandeis (1890). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use logic to state privacy rules precisely; (2) spot hidden assumptions in arguments about data; (3) reason about proportions and base rates.

### 1.1 A course built around schools

Elena Rossi begins a four-year bachelor's course at the fictional Fairhaven College, tutored by Dr. Kwame Asante. Her placement partner is the fictional Brindle Valley Schools Trust, which runs twelve primary schools with about 6,000 pupils. Schools hold names, addresses, health notes, special educational needs records and photographs of children. Dr. Asante explains that privacy and data protection will be Elena's main subject and that every foundation course will be read through the trust's work, starting with mathematical reasoning. Her first task is counting pupils per school.

### 1.2 Rules as logic

Privacy rules are often written loosely. The trust's policy says staff may share pupil data with apps if it is necessary and parents agree. Elena rewrites the rule as a logical statement: sharing is permitted only if necessity holds and a lawful basis exists. She notices that "parents agree" is not the only possible basis; a school may rely on a public task for teaching. Writing the rule precisely exposes the confusion. She learns that logic is a tool for making policies testable before they are applied to real children.

### 1.3 Hidden assumptions

Elena examines an argument from a teacher: the reading app is safe because it is popular with schools. The hidden assumption is that popularity implies careful data handling. She lists other hidden assumptions she meets: that a vendor's privacy page reflects its practice, that anonymised data cannot identify children, and that parents read consent forms. Each assumption can be checked. Dr. Asante asks the class to underline assumptions in every argument they read, a habit that will help them evaluate vendors and policies throughout the course.

### 1.4 Base rates

Elena studies base rates. If one in a hundred apps mishandles data and a vetting check catches nine in ten bad apps but wrongly flags five in a hundred good ones, most flagged apps are actually fine. She works through the arithmetic: of 1,000 apps, ten are bad and nine are flagged; of 990 good apps, about fifty are flagged. So only about one flagged app in six is bad. The lesson is that checks must be designed with base rates in mind, or staff will lose trust in them.

### Worked example

Elena rewrites a sharing rule as logic, exposes hidden assumptions about popular apps and shows that a vetting check flags mostly good apps when bad ones are rare.

> **Synthetic case.** Fairhaven, Brindle Valley and all figures are synthetic.

### Errors and limits

Base-rate figures here are illustrative; real rates must be estimated.

### Exercises

- **EX001 — Necessity and basis.** How does Elena rewrite the sharing rule? *Rubric:* 3 = sharing permitted only if necessary and a lawful basis exists;; 2 = mentions necessity;; 1 = keeps original;; 0 = none.
- **EX002 — Popular app assumption.** What hidden assumption lies in "the app is popular, so it is safe"? *Rubric:* 3 = popularity implies careful data handling;; 2 = names an assumption;; 1 = none;; 0 = none.
- **EX003 — Flagged apps.** Roughly what share of flagged apps is actually bad in Elena's example? *Rubric:* 3 = about one in six;; 2 = a minority;; 1 = most;; 0 = none.

### Synthesis

Chapter 1 sharpens reasoning. Chapter 2 looks at computing systems.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) map where pupil data live in school systems; (2) distinguish local, cloud and vendor storage; (3) relate system design to data protection duties.

### 2.1 Where data live

Elena maps the trust's systems. The management information system holds pupil records; a cloud office suite holds documents and email; classroom apps hold learning data; a payment system holds lunch accounts; and shared drives hold photographs. Some data sit on servers in schools, some in the cloud and some with vendors. She draws a simple diagram and finds that nobody in the trust has a complete view. Her map becomes the first version of the inventory that Article 30 of the GDPR requires.

### 2.2 Local and cloud

Local servers give the trust direct control but need maintenance, which small schools struggle to provide. Cloud services are maintained by providers but move data to another organisation, which becomes a processor under the GDPR. Elena lists responsibilities for each model. She notes that cloud is not automatically less private: a well-configured cloud service may be safer than an unpatched school server. The decision should follow the risks and the contracts in place, not a general preference for one model. Contracts decide much.

### 2.3 Devices

Pupils use shared tablets and teachers use laptops. Elena checks what data remain on devices: cached documents, saved passwords and photographs. A lost teacher laptop without encryption could expose many children's records. She recommends full-disk encryption on staff laptops and automatic sign-out on shared tablets. She learns that devices are part of the computing system and often its weakest point, because they leave the school and are used by many people with different levels of care. Pupil laptops go home each night, often shared with siblings.

### 2.4 Duties follow design

Elena concludes that system design shapes data protection duties. If data are spread across many vendors, the trust needs many contracts and must handle rights requests across all of them. If they are centralised, one system holds everything and must be well protected. Dr. Asante points out that Article 25 of the GDPR asks controllers to consider data protection when choosing the means of processing, which includes choosing and configuring systems, not only writing policies after the systems are installed. This is Article 25 in practice.

### Worked example

Elena maps five systems holding pupil data, compares local and cloud responsibilities, recommends encryption and auto sign-out on devices and links system choice to Article 25.

> **Synthetic case.** The trust's systems are synthetic; GDPR Articles 25 and 30 are real.

### Errors and limits

A first map misses shadow systems such as personal spreadsheets; revisit it.

### Exercises

- **EX004 — Missing view.** What did Elena's system map reveal? *Rubric:* 3 = nobody had a complete view of where pupil data live;; 2 = mentions gaps;; 1 = none;; 0 = none.
- **EX005 — Cloud not automatic.** Why is cloud storage not automatically less private? *Rubric:* 3 = a well-configured cloud may be safer than an unpatched school server;; 2 = mentions configuration;; 1 = says cloud is worse;; 0 = none.
- **EX006 — Device controls.** Which device controls does Elena recommend? *Rubric:* 3 = full-disk encryption on laptops and auto sign-out on shared tablets;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Chapter 2 maps systems. Chapter 3 starts programming.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small programs that process pupil data safely; (2) avoid exposing data in outputs; (3) use synthetic data for practice.

### 3.1 Synthetic first

Elena's first programs calculate attendance percentages. Dr. Asante insists that all practice uses synthetic pupils generated by a script, never real exports from the trust. Elena writes a generator that produces names, classes and attendance marks with realistic patterns. She learns that synthetic data let her make mistakes safely, share code with classmates and publish examples. The rule protects children and also teaches a habit that professional developers should keep, because real data in practice environments are a frequent source of leaks.

### 3.2 Outputs and exposure

Her attendance program prints a list of pupils below ninety per cent attendance. Elena realises that if the list were printed and left on a staffroom table, it would reveal sensitive information about families. She changes the program to print counts by class for general use and produce the named list only for the attendance officer, saved to a protected folder. Deciding who sees which output is a programming decision as well as a policy one, and the code can enforce it.

### 3.3 Input checks

The program reads a spreadsheet. Elena adds checks that reject unexpected columns, such as a health notes column accidentally included in an export. If the column appears, the program stops and explains why. This prevents the program from processing data it does not need. She explains that input checks implement data minimisation at the point where data enter a program, and that failing loudly is better than silently processing sensitive data that should never have been there. Her script rejects unexpected columns.

### 3.4 Comments that explain why

Elena writes comments that explain privacy decisions, such as why the named list is saved only to a protected folder. A classmate who reviews her code understands the reason and does not change it. Dr. Asante points out that comments explaining why are more valuable than comments explaining what, because the code already shows what it does. Privacy reasoning is easily lost when code changes hands, and short explanations keep it attached to the code that enforces it. Her comments name the purpose.

### Worked example

Elena practises with generated pupils, prints class counts for general use and named lists only for the attendance officer, rejects unexpected health columns and documents her reasons in comments.

> **Synthetic case.** Programs and pupils are synthetic.

### Errors and limits

Synthetic data may lack real edge cases; add them deliberately.

### Exercises

- **EX007 — Synthetic practice.** Why must practice use synthetic pupils? *Rubric:* 3 = mistakes and sharing are safe and real data stay protected;; 2 = mentions safety;; 1 = real is fine;; 0 = none.
- **EX008 — Two outputs.** How does Elena change the attendance output? *Rubric:* 3 = counts by class generally; named list only for the attendance officer;; 2 = one part;; 1 = prints names;; 0 = none.
- **EX009 — Unexpected column.** What does the program do with an unexpected health column? *Rubric:* 3 = stops and explains;; 2 = warns;; 1 = processes it;; 0 = none.

### Synthesis

Chapter 3 programs safely. Chapter 4 develops academic writing.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write an argued essay on a privacy question; (2) cite legal and academic sources properly; (3) distinguish description from argument.

### 4.1 The essay question

Elena's first essay asks: should schools publish photographs of pupils on public websites? She must take a position and support it. She researches the GDPR provisions on lawful basis and consent, including Article 8 on children's consent for online services, and reads academic work on children's privacy. She decides to argue that schools may publish photographs only with clear, specific consent from parents and, as children grow older, from the children themselves, and only where the purpose is meaningful. Her thesis states this in one sentence.

### 4.2 Citing properly

Dr. Asante teaches citation. Laws are cited by article and number, such as Regulation (EU) 2016/679, Article 6. Academic works are cited with author, year and title, and a reference list gives full details. Elena checks every citation against the original source rather than copying from secondary summaries. She finds that one blog misquotes the GDPR, saying that consent is always required for photographs. Citing the original text lets her avoid repeating the error and strengthens her argument. The source was a school blog.

### 4.3 Description and argument

Elena's first draft describes the law at length but argues little. Dr. Asante marks paragraphs that only describe. She revises so that each paragraph makes a claim, gives evidence and explains how the evidence supports the claim. For example, she argues that consent for photographs is meaningful only if refusal has no consequences, because the EDPB consent guidelines say consent must be freely given. The revised essay is shorter but more persuasive. Her first draft listed rules; the second explains why each one protects pupils.

### 4.4 Counter-arguments

A strong essay addresses objections. Elena considers the argument that photographs celebrate achievements and build community. She accepts the value but argues that internal newsletters and password-protected pages can achieve the same purpose with less exposure. She also considers that older pupils may want their achievements shown. She concludes that children's own views should carry growing weight with age. Addressing counter-arguments, she learns, shows the reader that the position survives scrutiny rather than ignoring it. One counter-argument concerns school traditions. Her reply cites the law.

### Worked example

Elena argues that school photographs need clear, specific consent with growing weight for children's views, cites the GDPR and EDPB guidance directly and answers community-building objections.

> **Synthetic case.** The essay is synthetic; GDPR Articles 6 and 8 and EDPB Guidelines 05/2020 are real.

### Errors and limits

Consent is one lawful basis among several; schools may rely on others for some processing.

### Exercises

- **EX010 — Original sources.** Why check citations against the original legal text? *Rubric:* 3 = secondary sources can misquote, as a blog did on photo consent;; 2 = mentions accuracy;; 1 = trusts blogs;; 0 = none.
- **EX011 — Paragraph structure.** What should each argued paragraph contain? *Rubric:* 3 = a claim, evidence and an explanation linking them;; 2 = two;; 1 = description;; 0 = none.
- **EX012 — Answering objections.** How does Elena answer the community-building objection? *Rubric:* 3 = internal or protected channels can achieve the purpose with less exposure;; 2 = mentions alternatives;; 1 = ignores;; 0 = none.

### Synthesis

Chapter 4 builds argument. Chapter 5 develops security literacy.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) recognise common threats to school data; (2) explain basic protections to staff; (3) relate security incidents to data protection.

### 5.1 Threats to schools

Elena studies threats that schools face: phishing emails pretending to be from parents or suppliers, ransomware that encrypts records, lost devices and misdirected emails. She reads that schools are attractive targets because they hold valuable data and often have limited security staff. She lists the trust's most likely incidents and finds that misdirected emails, such as sending one family's report to another, are the most frequent, even though ransomware gets more attention in the news. Her incident log review supports this ranking clearly.

### 5.2 Explaining protections

Elena prepares a short session for teachers. She explains strong passwords with a password manager, multi-factor authentication for email, checking recipients before sending and locking screens. She uses examples from schools rather than banks. She avoids blaming staff for mistakes, explaining that systems should make the safe choice easy, for instance by warning when an email is sent to an external address. Teachers respond better to practical advice than to warnings about hackers. One example: confirm attachments before sending externally. Teachers adopt them quickly.

### 5.3 Incidents are data protection events

Elena learns that a security incident involving personal data may be a personal data breach under the GDPR. Sending a pupil's report to the wrong parent is a breach, even if accidental. The trust must assess the risk and, unless the breach is unlikely to result in a risk to individuals, notify the supervisory authority within 72 hours under Article 33. She notes that many staff think breaches are only about hackers, so training must cover everyday mistakes. A wrong email can be a breach.

### 5.4 Culture

Elena reflects on security culture. Staff who fear punishment hide mistakes, which delays response. She recommends a reporting process that thanks staff for reporting quickly and focuses on fixing problems. Dr. Asante agrees, noting that fast reporting is essential when the 72-hour clock applies. Elena writes a one-page guide titled What to do if you send something to the wrong person, which tells staff to report immediately to the data protection lead and not to try to fix it alone. Speed matters most.

### Worked example

Elena identifies misdirected emails as the most frequent threat, trains teachers with school examples, explains that accidental disclosures are breaches under Article 33 and promotes a no-blame reporting culture.

> **Synthetic case.** Incidents are synthetic; GDPR Article 33 is real.

### Errors and limits

No-blame does not mean no accountability; repeated careless behaviour still needs management.

### Exercises

- **EX013 — Most frequent incident.** Which incident is most frequent for the trust? *Rubric:* 3 = misdirected emails;; 2 = mentions email;; 1 = ransomware;; 0 = none.
- **EX014 — Accidental breach.** Is sending a report to the wrong parent a breach? *Rubric:* 3 = yes; accidental disclosure counts;; 2 = yes;; 1 = no;; 0 = none.
- **EX015 — Reporting culture.** Why thank staff for reporting mistakes quickly? *Rubric:* 3 = fear delays reporting, and the 72-hour clock needs speed;; 2 = mentions speed;; 1 = punish;; 0 = none.

### Synthesis

Chapter 5 builds security literacy. Chapter 6 introduces discrete structures.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use sets and relations to model data sharing; (2) count combinations that identify pupils; (3) use graphs to trace data flows.

### 6.1 Sets of data

Elena models the trust's data as sets: all personal data, special category data such as health and religion, and data about children with special educational needs. She notes that some data belong to several sets. A list of pupils with dietary requirements may reveal religion or health. Set thinking helps her see that data which look ordinary can fall into sensitive categories, which GDPR Article 9 protects with stricter conditions. She uses Venn diagrams in her report to the trust. Health data are one example.

### 6.2 Counting identities

Elena counts how many pupils share combinations of attributes in a small school: year group, sex and first language. In a school of two hundred, some combinations contain one child. Publishing a table of results by these attributes could identify that child. She connects this to Sweeney's (2002) work on how combinations of ordinary attributes identify individuals. The counting exercise shows her why statistics about small schools need special care before publication. In a school with one pupil of a given age and ethnicity, the counts identify that child.

### 6.3 Relations

A relation pairs elements from two sets. Elena models which staff roles can access which data categories as a relation. Teachers access learning records; office staff access contact details; the special needs coordinator accesses support plans. She checks the relation against the principle of least privilege and finds that office staff can also access support plans, which they do not need. The model makes the problem visible in a way that a list of permissions in a software menu did not. Removing it narrows access.

### 6.4 Graphs of flows

Elena draws the trust's data flows as a directed graph: from parents to schools, from schools to apps, from apps to vendors' subprocessors. She finds paths that leave the trust through several steps, such as a reading app passing data to an analytics provider. A path, she notes, is only as protected as its weakest link. The graph prepares her for later chapters, where she will check each edge for a lawful basis and a contract. Each edge is a flow.

### Worked example

Elena models data categories as sets, counts identifying combinations in small schools, models role access as a relation (finding office access to support plans) and traces multi-step flows as a graph.

> **Synthetic case.** Models are synthetic; GDPR Article 9 and Sweeney (2002) are real.

### Errors and limits

Models simplify; real access often has exceptions not captured in role tables.

### Exercises

- **EX016 — Ordinary but sensitive.** Give an example of ordinary-looking data that may be special category. *Rubric:* 3 = dietary requirements revealing religion or health;; 2 = example given;; 1 = none;; 0 = none.
- **EX017 — Access relation finding.** What did the access relation reveal? *Rubric:* 3 = office staff could access support plans they do not need;; 2 = mentions office;; 1 = none;; 0 = none.
- **EX018 — Weakest link path.** Why is a multi-step data path only as protected as its weakest link? *Rubric:* 3 = data can leak at any step, such as a subprocessor;; 2 = mentions steps;; 1 = strongest;; 0 = none.

### Synthesis

Chapter 6 models data. Chapter 7 covers networks.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) identify what school network traffic reveals; (2) understand filtering and monitoring; (3) balance safeguarding with privacy.

### 7.1 School networks

Elena studies the trust's network. Pupils' devices connect through school Wi-Fi, which passes through a web filter. The filter logs every website a device visits. Encryption protects content but the filter sees domain names. Elena realises that the logs reveal sensitive information, such as searches for health or family problems, and that they relate to identifiable children when devices are assigned to pupils. Network design therefore creates a significant body of personal data that many staff do not even know exists. Logs are personal data.

### 7.2 Filtering and monitoring

Schools often have safeguarding duties to protect children from harmful content. Elena learns that filtering and monitoring can support those duties but must be proportionate. She reviews the filter settings and finds logs kept for three years and accessible to all IT staff. She recommends shorter retention, access limited to designated safeguarding staff and clear information to pupils and parents about what is monitored. She notes that transparency is part of fairness, even when monitoring is justified. Pupils see a notice at login.

### 7.3 Encryption in transit

Elena checks that the management information system and apps use encrypted connections. One legacy app used by a school sends pupil names without encryption on the local network. She raises it with the IT team, who replace it. She explains to teachers that encrypted connections prevent others on the same network from reading data, which matters in schools where many devices share networks. She checks the management information system and the parent portal and finds both encrypted, but a legacy printing service sends class lists in plain text across the network, which IT replaces during the next holiday.

### 7.4 Balancing duties

Elena discusses with Dr. Asante how to balance safeguarding and privacy. Both aim to protect children. Over-monitoring may discourage pupils from seeking help online about sensitive issues, while under-monitoring may miss serious risks. She writes that the trust should state the purpose of monitoring clearly, limit it to that purpose and review it regularly. The discussion shows her that privacy is not opposed to safety but must be weighed with it carefully and openly. Monitoring logs are kept for one term.

### Worked example

Elena finds web filter logs revealing sensitive searches kept for three years, recommends shorter retention and safeguarding-only access, replaces an unencrypted app and frames monitoring as a balance of duties.

> **Synthetic case.** The network and filter are synthetic.

### Errors and limits

Safeguarding requirements vary by country; check local guidance.

### Exercises

- **EX019 — Filter logs.** Why are web filter logs sensitive? *Rubric:* 3 = they reveal children's searches on health or family issues;; 2 = mentions searches;; 1 = not personal;; 0 = none.
- **EX020 — Filter retention.** What did Elena recommend for filter logs? *Rubric:* 3 = shorter retention, safeguarding-only access and transparency;; 2 = two;; 1 = none;; 0 = none.
- **EX021 — Over-monitoring harm.** How can over-monitoring harm children? *Rubric:* 3 = it may discourage seeking help online about sensitive issues;; 2 = mentions chilling;; 1 = none;; 0 = none.

### Synthesis

Chapter 7 examines networks. Chapter 8 advances programming.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) implement access checks; (2) pseudonymise data for analysis; (3) test privacy behaviour.

### 8.1 Access checks

Elena writes a small application for viewing pupil information. Before showing any record, it checks the user's role and the purpose. A teacher can see learning records for pupils in their classes; the special needs coordinator can see support plans. Requests without a valid role are refused and logged. She learns that writing checks into the code ensures the rules are applied consistently, rather than relying on staff remembering which data they should look at. Each request checks the class list.

### 8.2 Pseudonymised analysis

The trust wants to analyse reading progress across schools. Elena writes code that replaces pupil identifiers with pseudonyms using a keyed hash before data reach the analyst. The key is held by the data protection lead. She explains that the analyst can study progress without knowing which child is which, but that the data remain personal data under the GDPR because the key could re-identify pupils. Pseudonymisation reduces risk but does not remove legal duties. The key is stored separately from the data.

### 8.3 Testing

Elena writes tests that check privacy behaviour: a teacher cannot see a pupil from another class, the analysis export contains no names, and logs record each access. One test fails because a teacher who left a class still has access. She adds a rule to remove access when class assignments change. Testing privacy properties automatically finds problems that manual review would miss and keeps working as the code changes. A failing test blocks the change from being deployed. Tests run on every change, using synthetic classes only.

### 8.4 Code review

Elena's code is reviewed by a classmate who asks why the export includes date of birth. Elena realises it is not needed for reading progress and removes it. Dr. Asante points out that reviewers should ask what data are needed as well as whether the code works. Code review becomes a minimisation check as well as a quality check, and small removals like this add up across many programs. In one review she removes a date-of-birth field from an export. Reviewers ask why each field exists.

### Worked example

Elena implements role- and class-based access checks, pseudonymises reading data with a keyed hash, finds stale class access through tests and removes date of birth after review.

> **Synthetic case.** Code and pupils are synthetic.

### Errors and limits

Keyed pseudonyms can be reversed by anyone holding the key; protect it.

### Exercises

- **EX022 — Class-based access.** How does Elena's application decide whether a teacher sees a record? *Rubric:* 3 = role and purpose checks plus class membership;; 2 = mentions role;; 1 = shows all;; 0 = none.
- **EX023 — Pseudonymised still personal.** Why is the pseudonymised reading dataset still personal data? *Rubric:* 3 = the key can re-identify pupils;; 2 = mentions key;; 1 = anonymous;; 0 = none.
- **EX024 — Stale access.** What failed test did Elena fix? *Rubric:* 3 = teachers keeping access after leaving a class;; 2 = mentions access;; 1 = none;; 0 = none.

### Synthesis

Chapter 8 implements controls. Chapter 9 studies data and databases.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) query a database to find sharing risks; (2) relate contracts to data flows; (3) recommend actions from query results.

### 9.1 A sharing database

Elena builds a small SQLite database of classroom apps and the pupil data each receives, based on a synthetic version of the trust's records. Each app has a vendor, a region and a flag showing whether a data processing agreement is signed. Article 28 of the GDPR requires a contract with processors. The database lets her ask questions that a spreadsheet makes hard, such as which apps receive data without an agreement and how many pupils they affect. It uses only stdlib sqlite3.

### 9.2 The query

The lab joins apps with shared fields and filters apps without agreements. Three apps appear. ClassChat, based in the EEA, receives names and email addresses for 3,100 pupils. ReadAlong, based in the US, receives names, reading levels and a special educational needs flag for up to 1,800 pupils. QuizBlitz, in the US, receives names for 900 pupils. In total there are 5,800 pupil-app shares without an agreement, counting a pupil once per app. The query joins the apps table with the agreements table and counts pupils per app.

### 9.3 Reading the result

Elena notes that ReadAlong is the most serious case. It receives a special educational needs flag, which may be health data, sends data outside the EEA and has no agreement. ClassChat affects the most pupils but holds less sensitive data. She ranks the apps by sensitivity, transfer and scale rather than scale alone. She explains that a database query gives facts, but judgement is needed to decide which facts matter most for children. QuizBlitz needs attention too despite smaller numbers, because its data leave Europe.

### 9.4 Recommendations

Elena recommends suspending ReadAlong until an agreement and a transfer mechanism are in place and the special needs flag is removed; obtaining an agreement for ClassChat; and reviewing whether QuizBlitz is needed at all. She also recommends that the trust keep the database updated as apps change, turning it into a living register. Dr. Asante notes that a register queried regularly is more useful than a one-off audit spreadsheet. Each new app is added before teachers start using it. Teachers can query it themselves.

### Lab — Classroom apps receiving pupil data without an agreement

```python
# SQLite: which classroom apps receive pupil data without a signed data processing agreement?
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE app(name TEXT, vendor TEXT, dpa INTEGER, region TEXT);
CREATE TABLE share(app TEXT, field TEXT, pupils INTEGER);
INSERT INTO app VALUES ('MathsQuest','Qbit Ltd',1,'EEA'),('ReadAlong','Fable Inc',0,'US'),('ClassChat','Talko',0,'EEA'),
 ('Timetabler','Sched AB',1,'EEA'),('QuizBlitz','Blitz LLC',0,'US'),('LunchPay','Payfair',1,'EEA');
INSERT INTO share VALUES ('MathsQuest','name',2400),('MathsQuest','year_group',2400),('ReadAlong','name',1800),('ReadAlong','reading_level',1800),
 ('ReadAlong','sen_flag',140),('ClassChat','name',3100),('ClassChat','email',3100),('Timetabler','name',6000),('QuizBlitz','name',900),
 ('LunchPay','name',6000),('LunchPay','free_meals',1150);
""")
q = """SELECT a.name, a.region, GROUP_CONCAT(s.field), MAX(s.pupils) FROM app a JOIN share s ON s.app=a.name
       WHERE a.dpa=0 GROUP BY a.name ORDER BY MAX(s.pupils) DESC"""
for n, reg, f, p in db.execute(q): print(f"{n:10s} {reg:4s} fields={f:28s} pupils={p}")
print("pupil-app shares without a DPA (a pupil may count in several apps):", db.execute("SELECT SUM(m) FROM (SELECT MAX(s.pupils) m FROM app a JOIN share s ON s.app=a.name WHERE a.dpa=0 GROUP BY a.name)").fetchone()[0])
```

Run with `python3 lab_sqlite.py`. Verified output:

```text
ClassChat  EEA  fields=email,name                   pupils=3100
ReadAlong  US   fields=name,reading_level,sen_flag  pupils=1800
QuizBlitz  US   fields=name                         pupils=900
pupil-app shares without a DPA (a pupil may count in several apps): 5800
```

### Worked example

Elena's query finds three apps without agreements (5,800 pupil-app shares), ranks ReadAlong first because of the special needs flag and US transfer, and recommends suspension, agreements and a living register.

> **Synthetic case.** Apps and counts are synthetic; GDPR Article 28 is real.

### Errors and limits

Counting pupils per app double-counts children using several apps.

### Exercises

- **EX025 — Apps without agreements.** Which apps lack a data processing agreement? *Rubric:* 3 = ClassChat, ReadAlong, QuizBlitz;; 2 = two;; 1 = one;; 0 = none.
- **EX026 — Most serious.** Why is ReadAlong the most serious case? *Rubric:* 3 = special needs flag, US transfer and no agreement;; 2 = two reasons;; 1 = scale;; 0 = none.
- **EX027 — Living register.** Why keep the database as a living register? *Rubric:* 3 = apps change, so regular queries catch new gaps;; 2 = mentions updates;; 1 = one-off audit;; 0 = none.

### Synthesis

Chapter 9 queries data. Chapter 10 discusses ethics and authorised practice.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) apply ethical principles to work with children's data; (2) define the limits of authorised practice; (3) handle requests outside one's authority.

### 10.1 Children's interests

Elena studies ethics for work with children's data. Children may be less aware of risks and less able to exercise rights. Recital 38 of the GDPR says children merit specific protection, and Article 14 of the LGPD requires processing of children's data to be in their best interest. She writes that her work at the trust should always ask what is best for the children, not only what is lawful or convenient for adults. This becomes her working test for every decision. Lawful is not enough.

### 10.2 Authorised practice

During her placement Elena has access to synthetic data and to real system configurations, but not to real pupil records. Dr. Asante explains that authorised practice means doing only what her placement agreement allows. When a teacher offers to show her a real spreadsheet to help her understand a problem, she politely declines and asks for a synthetic example instead. She records the offer and her response in her placement log. The supervisor approves her response and supplies the synthetic data.

### 10.3 Requests outside authority

A head teacher asks Elena to check whether a parent's complaint about a data breach is justified by looking at email logs. Elena explains that investigating a complaint requires authority from the data protection lead and access she does not have. She refers the request to the lead. She learns that good intentions do not create authority, and that stepping outside her role could harm the people she wants to help and undermine trust in the investigation. She refers the request onwards.

### 10.4 Professional values

Elena reflects on values: respect for children and families, honesty about risks, and humility about her own limits. She writes a short personal code for her placement. Dr. Asante encourages her to revisit it each year. He explains that professional codes in computing and data protection share these values, and that the habit of reflecting on them prepares students for difficult decisions that rules alone cannot resolve. Her reflective log records one dilemma each week, with what she decided and why.

### Worked example

Elena centres children's best interests, declines a real spreadsheet, refers a complaint investigation to the data protection lead and writes a personal code of values.

> **Synthetic case.** Placement events are synthetic; GDPR Recital 38 and LGPD Article 14 are real.

### Errors and limits

Personal codes can be vague; tie each value to a concrete behaviour.

### Exercises

- **EX028 — Children's protection.** Which provisions emphasise special protection for children's data? *Rubric:* 3 = GDPR Recital 38 and LGPD Article 14;; 2 = one;; 1 = none;; 0 = none.
- **EX029 — Declining real data.** Why does Elena decline the real spreadsheet? *Rubric:* 3 = her placement authorises only synthetic data;; 2 = mentions authority;; 1 = accepts;; 0 = none.
- **EX030 — Complaint referral.** Why refer the complaint investigation to the data protection lead? *Rubric:* 3 = it needs authority and access she lacks;; 2 = mentions role;; 1 = investigates;; 0 = none.

### Synthesis

Chapter 10 sets ethical limits. Chapter 11 studies operating systems.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) configure accounts and permissions for school devices; (2) manage logs and temporary files; (3) plan secure disposal of devices.

### 11.1 Accounts on shared devices

Elena studies how operating systems manage accounts. On shared classroom computers, pupils log in with individual accounts so that work and browsing are separated. She finds that one school uses a single shared account for all pupils, which means files and browser histories are visible to everyone. She recommends individual accounts with automatic clean-up of temporary files at logout. She explains to the school's technician that operating system settings are the first line of privacy on shared devices, before any application is opened.

### 11.2 Permissions and shares

Teachers save documents to network shares. Elena checks permissions and finds a folder of safeguarding notes readable by all staff. She works with the technician to restrict it to safeguarding leads. She also turns on auditing for the folder so that access can be reviewed. The episode shows that sensitive information often sits in ordinary file shares rather than in protected systems, and that permissions drift over years as staff change roles without anyone reviewing who can still open which folders. Reviews fix this.

### 11.3 Logs

Operating systems log logins and file access. Elena explains that logs help investigate incidents but also contain personal data about staff and pupils. She recommends keeping logs long enough for investigations, such as six months, restricting access to IT security staff and telling staff in the acceptable use policy that activity is logged. Transparency, she notes, is required by GDPR Articles 13 and 14 for staff as well as for pupils, and staff are entitled to know what is recorded about them. Staff can request them.

### 11.4 Disposal

Old laptops and tablets are sold or recycled. Elena finds that devices are wiped by deleting user accounts, which may leave data recoverable. She recommends using built-in secure erase functions or full-disk encryption with key destruction, and keeping a disposal record for each device. She learns that disposal is part of the data life cycle and that many breaches in the sector have involved devices sold without proper wiping, which is an avoidable and embarrassing way to lose children's data. Certificates prove wiping.

### Worked example

Elena replaces a shared pupil account with individual accounts, restricts and audits a safeguarding folder, sets log retention with transparency to staff and introduces secure erase and disposal records.

> **Synthetic case.** Devices and folders are synthetic; GDPR Articles 13 and 14 are real.

### Errors and limits

Secure erase methods differ by device; verify that the method works on each model.

### Exercises

- **EX031 — Shared account risk.** What is wrong with one shared pupil account? *Rubric:* 3 = files and histories are visible to every pupil;; 2 = mentions sharing;; 1 = fine;; 0 = none.
- **EX032 — Safeguarding folder.** How was the safeguarding folder fixed? *Rubric:* 3 = access restricted to safeguarding leads with auditing;; 2 = one part;; 1 = none;; 0 = none.
- **EX033 — Device disposal.** Why is deleting user accounts not enough before selling a laptop? *Rubric:* 3 = data may remain recoverable on disk;; 2 = mentions recovery;; 1 = enough;; 0 = none.

### Synthesis

Chapter 11 secures systems. Chapter 12 uses probability and statistics.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) estimate a proportion from a survey with uncertainty; (2) compare groups carefully; (3) report survey results without identifying respondents.

### 12.1 The parent survey

The trust surveys parents about privacy awareness. One question asks whether parents know which apps receive their child's data. Elena analyses the synthetic results. Across twelve schools, 131 of 520 respondents say yes, 25%. She computes a Wilson 95% interval, which behaves well for proportions near zero or one and for small samples, and finds 22% to 29%. She reports the interval because a single percentage hides how uncertain the estimate is, especially for individual schools. The Wilson interval works well for proportions near zero or with small samples.

### 12.2 Comparing schools

Elena compares two schools. At Ashby Primary 9 of 40 parents say yes, 22%, with an interval from 12% to 38%. At Kelso Primary 22 of 48 say yes, 46%, with an interval from 33% to 60%. The intervals barely overlap, suggesting a real difference. She investigates and finds that Kelso sends parents a yearly letter listing apps. She cautions that the survey cannot prove the letter caused the difference, but the pattern supports trying the letter elsewhere. Other differences between schools could also explain the gap. Only an experiment could show causation.

### 12.3 Response bias

Not all parents respond. Elena notes that parents interested in privacy may be more likely to answer, which could make awareness look higher than it is. She reports the response rate for each school and recommends caution in interpreting low-response schools. She explains that statistics about people depend on who is counted, and that a careful analyst always asks who is missing from the data before drawing conclusions about everyone. Parents who answer surveys may differ from those who do not.

### 12.4 Protecting respondents

The survey includes a free-text comment field. Some comments mention children's names and conditions. Elena removes identifying details before sharing comments with the trust's leadership and reports school-level figures only where at least twenty parents responded. She explains that a survey about privacy must itself protect privacy, and that small groups and free text are the most common ways survey reports accidentally identify people. She suppresses results for groups smaller than ten and removes free-text answers that mention children's names or classes.

### Lab — Parent awareness with Wilson intervals

```python
# Wilson 95% intervals for a synthetic parent survey: "I know which apps receive my child's data".
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h
for school, k, n in [("Ashby Primary", 9, 40), ("Kelso Primary", 22, 48), ("all 12 schools", 131, 520)]:
    lo, hi = wilson(k, n); print(f"{school:15s} {k}/{n} = {k/n:.0%}  95% CI {lo:.0%}-{hi:.0%}")
```

Run with `python3 lab_wilson.py`. Verified output:

```text
Ashby Primary   9/40 = 22%  95% CI 12%-38%
Kelso Primary   22/48 = 46%  95% CI 33%-60%
all 12 schools  131/520 = 25%  95% CI 22%-29%
```

### Worked example

Elena estimates trust-wide awareness at 25% (95% interval 22% to 29%), finds Ashby 22% versus Kelso 46% with barely overlapping intervals, notes response bias and redacts comments.

> **Synthetic case.** Survey data are synthetic.

### Errors and limits

Barely overlapping intervals are suggestive, not a formal test; a test of difference would be more precise.

### Exercises

- **EX034 — Trust-wide interval.** What is the 95% interval for trust-wide awareness? *Rubric:* 3 = 22% to 29%;; 2 = approximately right;; 1 = wrong;; 0 = none.
- **EX035 — Kelso difference.** What might explain Kelso's higher awareness? *Rubric:* 3 = a yearly letter listing apps, though causation is not proven;; 2 = mentions letter;; 1 = none;; 0 = none.
- **EX036 — Respondent protection.** How does Elena protect survey respondents? *Rubric:* 3 = redacts free text and reports schools only with at least twenty responses;; 2 = one part;; 1 = none;; 0 = none.

### Synthesis

Chapter 12 measures awareness. Chapter 13 covers identity and access.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) design role-based access for school systems; (2) manage joiners, movers and leavers; (3) review access regularly.

### 13.1 Roles

Elena designs roles for the trust's management information system: class teacher, head of year, special needs coordinator, office administrator, safeguarding lead and head teacher. Each role has defined access. She documents the purpose of each permission. For example, office administrators need contact details to send letters but not assessment results. Role design turns the principle of least privilege into something staff and auditors can understand and check. The office role, for example, can update contact details but cannot see reading levels.

### 13.2 Joiners, movers and leavers

Staff change roles often. Elena finds that a former special needs coordinator, now a class teacher, still has access to all support plans. Another teacher who left the trust six months ago still has an active account. She proposes a process linked to the human resources system: when someone joins, moves or leaves, their access changes automatically, with a manager confirming the new role. She notes that stale access is one of the most common access control failures in organisations of every size.

### 13.3 Access reviews

Elena sets up termly access reviews. Each head teacher receives a list of staff and their roles and confirms or corrects them. In the first review, eleven of 340 accounts need changes. She records the results and repeats the review the next term, when only three changes are needed. Regular reviews, she explains, catch errors that automated processes miss and provide evidence of accountability under Article 5(2) of the GDPR. Each head teacher confirms their school's list every term. Corrections are logged with dates and reasons.

### 13.4 Authentication

Elena recommends multi-factor authentication for staff accessing pupil records from outside school. She also recommends that pupils use simple but individual logins appropriate to their age. Very young pupils may use picture passwords on classroom devices, while older pupils use passwords. She explains that authentication must suit the people using it, and that security that young children cannot manage will be bypassed by well-meaning teachers sharing logins. Younger pupils use picture passwords on shared tablets, and teachers no longer need to share their own logins.

### Worked example

Elena defines six roles with documented purposes, links access changes to HR, runs termly reviews (eleven changes falling to three) and adapts authentication to staff and pupils' ages.

> **Synthetic case.** Accounts and roles are synthetic; GDPR Article 5(2) is real.

### Errors and limits

HR integration fails if HR records are late; reviews remain necessary.

### Exercises

- **EX037 — Stale access cases.** Name the two stale access cases Elena found. *Rubric:* 3 = former SEN coordinator keeping support plans; departed teacher with active account;; 2 = one;; 1 = none;; 0 = none.
- **EX038 — Review results.** How many accounts needed changes in the first and second reviews? *Rubric:* 3 = eleven, then three;; 2 = one figure;; 1 = wrong;; 0 = none.
- **EX039 — Age-appropriate login.** Why use picture passwords for very young pupils? *Rubric:* 3 = security they cannot manage will be bypassed;; 2 = mentions usability;; 1 = none;; 0 = none.

### Synthesis

Chapter 13 manages access. Chapter 14 lays privacy foundations.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) explain theories of privacy; (2) apply data protection principles; (3) identify lawful bases for school processing.

### 14.1 Theories

Elena studies privacy theory. Warren and Brandeis (1890) argued for a right to be let alone. Solove (2006) describes privacy as a family of problems, such as surveillance, aggregation and disclosure. Nissenbaum's contextual integrity holds that information flows should respect the norms of their context. Elena applies contextual integrity to schools: information shared by parents with a teacher about a family situation should not flow to other parents or to app vendors, even if technically possible. Nissenbaum calls this contextual integrity. Norms travel with information.

### 14.2 Principles

She studies the GDPR principles in Article 5 and finds equivalents in LGPD Article 6, which lists principles such as purpose, adequacy, necessity, transparency, security and prevention. She maps each principle to a school example: purpose limitation means attendance data collected for safeguarding should not be used to rank teachers; minimisation means a lunch app does not need reading levels. The examples make abstract principles concrete for staff training. Purpose limitation prevents attendance data being used for staff performance. Each example comes from trust practice.

### 14.3 Lawful bases

Elena learns that processing needs a lawful basis under GDPR Article 6. Schools often rely on legal obligation for records required by education law, public task for teaching, and consent for optional activities such as photographs in newsletters. She explains that consent is not always the right basis: if a school needs data to teach, asking for consent suggests that parents could refuse without consequence, which may not be true. Choosing the correct basis makes processing more honest. Public task fits most pupil data.

### 14.4 Special categories

Health data, religious beliefs and ethnic origin are special categories under Article 9. Schools process them for medical care, dietary needs and equality monitoring. Each needs a condition under Article 9 as well as a basis under Article 6. Elena builds a table of the trust's special category processing with both bases. She finds that equality monitoring data are kept with names when aggregated analysis would suffice, and recommends separating them. Separation reduces exposure without reducing the usefulness of the equality reports. The lead agrees.

### Worked example

Elena applies contextual integrity to family information, maps GDPR and LGPD principles to school examples, explains why consent is not always the right basis and finds equality data kept with names.

> **Synthetic case.** The trust's processing is synthetic; Warren and Brandeis (1890), Solove (2006), Nissenbaum (2004), GDPR Articles 5, 6 and 9 and LGPD Article 6 are real.

### Errors and limits

Lawful basis choices depend on national education law; check locally.

### Exercises

- **EX040 — Contextual flow.** How does contextual integrity apply to family information shared with a teacher? *Rubric:* 3 = it should not flow to other parents or vendors;; 2 = mentions norms;; 1 = free to share;; 0 = none.
- **EX041 — Consent misuse.** Why is consent wrong for data needed to teach? *Rubric:* 3 = parents cannot really refuse without consequence;; 2 = mentions choice;; 1 = consent always;; 0 = none.
- **EX042 — Equality data.** What did Elena find about equality monitoring data? *Rubric:* 3 = kept with names when aggregate analysis would suffice;; 2 = mentions names;; 1 = none;; 0 = none.

### Synthesis

Chapter 14 lays foundations. Chapter 15 measures evidence.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) measure performance on rights requests; (2) identify causes of delay; (3) set targets and monitoring.

### 15.1 Access requests from parents

Parents can request access to their child's data, and children can make requests themselves when mature enough. Elena collects synthetic data on twenty requests from the past year. The median response time is 26 days and the mean 26.8. Six of the twenty, 30%, took longer than thirty days, the approximate one-month limit in GDPR Article 12(3). The longest took 61 days. The figures give the trust its first factual picture of how it handles requests. Several took over a month. Most were answered on time, but delays clustered around holidays.

### 15.2 Causes

Elena looks at the late requests. All four requests received just before school holidays were late, because staff were away. She also finds that requests went to individual schools rather than a central point, so handling varied. She explains that the GDPR deadline continues during holidays, although Article 12(3) allows extension by two months for complex or numerous requests if the requester is told within the first month. Holidays alone do not justify an extension. Most delays came from school holidays. Planning can fix this.

### 15.3 Targets and process

Elena proposes a central request inbox managed by the data protection lead, a holiday cover rota and a target of answering all requests within twenty-five days to leave a margin. She also proposes a template letter for extensions where genuinely needed. EDPB Guidelines 01/2022 on the right of access help her design the identity check and the content of responses. She presents the plan to the trust's leadership with the measured baseline. The plan sets a twenty-day internal target. Each request is logged centrally from day one.

### 15.4 Monitoring

Elena sets up a simple monthly report: requests received, open requests, median time and late requests. She explains that measuring regularly turns a one-off review into a feedback loop. Dr. Asante points out that small numbers make percentages jumpy, so she reports counts alongside percentages. Six months later, after the new process starts, no requests are late. She reports the improvement with the caution that the sample is small. With so few requests, one late case changes the percentage sharply. Counts are shown too.

### Lab — Response times for parents' access requests

```python
# Subject access requests from parents over one year: days to respond, one-month (30-day) target.
import statistics
days = [12, 25, 31, 8, 44, 19, 27, 30, 52, 15, 22, 35, 9, 28, 61, 17, 24, 29, 33, 14]
print(f"requests {len(days)}; median {statistics.median(days)} days; mean {statistics.mean(days):.1f}")
late = [d for d in days if d > 30]
print(f"late (>30 days): {len(late)} of {len(days)} ({len(late)/len(days):.0%}); longest {max(days)} days")
print("holiday-period requests late:", sum(1 for d in [44, 52, 61, 35] if d > 30), "of 4")
```

Run with `python3 lab_sar.py`. Verified output:

```text
requests 20; median 26.0 days; mean 26.8
late (>30 days): 6 of 20 (30%); longest 61 days
holiday-period requests late: 4 of 4
```

### Worked example

Elena measures a median of 26 days with 6 of 20 requests late (all four holiday-period requests), centralises handling with holiday cover and monitors monthly.

> **Synthetic case.** Requests are synthetic; GDPR Article 12(3) and EDPB Guidelines 01/2022 are real.

### Errors and limits

Twenty requests are few; one late case changes the percentage a lot.

### Exercises

- **EX043 — Late share.** What share of requests was late? *Rubric:* 3 = 6 of 20, 30%;; 2 = about a third;; 1 = wrong;; 0 = none.
- **EX044 — Holiday extension.** Do school holidays justify extending the deadline? *Rubric:* 3 = no; extension is for complexity or volume, with notice;; 2 = no;; 1 = yes;; 0 = none.
- **EX045 — Counts with percentages.** Why report counts alongside percentages? *Rubric:* 3 = small numbers make percentages jumpy;; 2 = mentions size;; 1 = not needed;; 0 = none.

### Synthesis

Chapter 15 measures rights handling. Chapter 16 studies security architecture.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) design a secure architecture for a multi-school trust; (2) separate sensitive data; (3) plan backup and recovery.

### 16.1 Trust architecture

Elena designs an architecture for the trust. A central management information system serves all twelve schools. Each school's staff see only their pupils. Safeguarding records sit in a separate, more restricted system. Classroom apps connect through single sign-on, which lets the trust control access centrally and remove it quickly. She draws the design with zones and explains why sensitive records are separated from everyday systems used by many staff. Sensitive safeguarding records sit in their own zone with separate access. Zones are documented.

### 16.2 Separation

Separation limits damage. If a teacher's account is compromised, the attacker can reach learning records but not safeguarding notes. Elena also separates pupil data from staff data, since different roles need each. She explains that the GDPR requires security appropriate to the risk under Article 32, and that separation is a cost-effective measure for a trust with limited security staff, because it reduces how much any single failure can expose. A compromised classroom laptop cannot reach safeguarding records directly. Rules are simple and testable.

### 16.3 Backup and recovery

Schools have suffered ransomware attacks. Elena designs backups that are encrypted, stored separately and tested. She sets recovery objectives: the management system restored within one day, safeguarding records within four hours, since safeguarding staff may need them urgently. She plans a restore test each term. She notes that backups also hold personal data and must follow retention rules, so old backups expire. In the first restore test, a term's attendance records are recovered in under an hour, and the restored copy is deleted afterwards so that no duplicate remains.

### 16.4 Vendor architecture

Many functions are provided by vendors. Elena includes vendors in the architecture diagram with their data flows and contracts. She notes that single sign-on lets the trust disable access to all apps quickly when a pupil leaves. She also sets a rule that new apps must connect through single sign-on and pass vetting. Architecture, she explains, includes rules about how new components join, not only the current components. New apps must use the trust's single sign-on. Each app joins only after vetting and appears on the architecture diagram.

### Worked example

Elena designs a central system with per-school access, a separate safeguarding system, single sign-on for apps, encrypted tested backups and an onboarding rule for new apps.

> **Synthetic case.** The architecture is synthetic; GDPR Article 32 is real.

### Errors and limits

Central systems concentrate risk; protect and monitor them closely.

### Exercises

- **EX046 — Safeguarding separation.** Why keep safeguarding records in a separate system? *Rubric:* 3 = a compromised teacher account cannot reach them;; 2 = mentions sensitivity;; 1 = same system;; 0 = none.
- **EX047 — Single sign-on benefit.** What does single sign-on give the trust? *Rubric:* 3 = central control and quick removal of access to all apps;; 2 = mentions control;; 1 = none;; 0 = none.
- **EX048 — Backup retention.** Why must backups follow retention rules? *Rubric:* 3 = backups hold personal data too;; 2 = mentions data;; 1 = exempt;; 0 = none.

### Synthesis

Chapter 16 designs architecture. Chapter 17 covers cryptography concepts.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain encryption at rest and in transit; (2) understand hashing and pseudonymisation; (3) manage keys appropriately.

### 17.1 Encryption

Elena learns the difference between encryption in transit, which protects data moving across networks, and encryption at rest, which protects stored data. Both protect children's records from different threats. She checks that the trust's systems use both and finds that exported reports saved to USB drives are not encrypted. She recommends encrypted USB drives or, better, stopping exports to removable media and using secure sharing instead. Her audit finds that these drives are mostly used for moving reports home to mark.

### 17.2 Hashing and pseudonyms

Hashing turns data into a fixed-length value that cannot easily be reversed. Elena explains that hashing a pupil identifier alone is weak, because the set of identifiers is small and an attacker can hash them all. A keyed hash with a secret key is stronger. She uses keyed hashes for the reading analysis in Chapter 8. She stresses that pseudonymisation reduces risk but the data remain personal under GDPR Article 4(5). Keys stay with the data protection lead. The key is rotated yearly by the lead.

### 17.3 Keys

Encryption depends on keys. Elena asks who holds the keys for the trust's backups. The answer is a single IT technician. If he leaves or loses the key, backups become unusable. She recommends storing keys in a managed key service with two authorised custodians and documented recovery. She explains that key management is often the hardest part of cryptography in practice, and that small organisations need simple, well-documented arrangements. The trust keeps a two-page key register. It names holders and locations for each key.

### 17.4 Limits

Elena notes that encryption does not protect against authorised users misusing data or against data being collected unnecessarily. A teacher with legitimate access can still share a report inappropriately. Encryption is one measure among many. She writes in her notes that cryptography protects confidentiality against outsiders, while access control, training and minimisation address insiders and over-collection. A teacher with legitimate access can still misuse decrypted reports, so encryption alone would not have prevented the misdirected email she studied earlier in the course.

### Worked example

Elena stops unencrypted USB exports, uses keyed hashes for pseudonyms, moves backup keys to a managed service with two custodians and states the limits of encryption.

> **Synthetic case.** Systems are synthetic; GDPR Article 4(5) is real.

### Errors and limits

Encrypted data are still personal data; encryption reduces risk, not obligations.

### Exercises

- **EX049 — USB exports.** What did Elena recommend for exports on USB drives? *Rubric:* 3 = encrypted drives or replace with secure sharing;; 2 = one option;; 1 = none;; 0 = none.
- **EX050 — Single key holder.** What was the risk of one technician holding backup keys? *Rubric:* 3 = backups unusable if he leaves or loses the key;; 2 = mentions loss;; 1 = none;; 0 = none.
- **EX051 — Encryption limits.** What does encryption not protect against? *Rubric:* 3 = authorised users misusing data and over-collection;; 2 = one;; 1 = everything;; 0 = none.

### Synthesis

Chapter 17 explains cryptography. Chapter 18 introduces research methods.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) frame a research question about privacy practice; (2) choose methods suited to schools; (3) plan ethical research with children's data.

### 18.1 Question

Elena's research methods course asks her to plan a small study. She asks: why do teachers adopt classroom apps without checking their data practices? The question matters because unchecked apps create most of the trust's sharing risks found in Chapter 9. She frames it as an exploratory question, suitable for interviews, rather than a hypothesis to test, because little is known about teachers' reasoning in this setting. Her question asks why teachers adopt apps without vetting. She expects varied reasons and wants to hear them in teachers' own words.

### 18.2 Methods

Elena plans semi-structured interviews with ten teachers across four schools. She writes an interview guide with open questions about how they find apps, what they check and what they would need to check more. She plans to analyse transcripts thematically, coding recurring reasons. She also plans to compare interview themes with the app register, to see whether stated practices match actual sharing. Interviews last about thirty minutes and use the same core questions for every teacher. Answers are compared with the app register.

### 18.3 Ethics

Elena's study involves adults, not children, but discussions may mention pupils. She plans to tell participants not to name children, to delete any names that appear in transcripts and to store recordings securely and delete them after transcription. She obtains ethics approval from Fairhaven and permission from the trust. Participants give informed consent and may withdraw. She notes that research about privacy must model good privacy practice. Recordings are deleted after transcription. Teachers are asked not to name pupils, and any names mentioned are removed from transcripts.

### 18.4 Limits

Elena notes limits: ten teachers cannot represent all teachers; participants may present themselves favourably; and her placement role may influence what they say. She plans to state these limits in her report and to ask a colleague who is not part of the placement to conduct two interviews as a check. Dr. Asante reminds her that acknowledging limits is part of good research, not a weakness. Her placement role might make teachers less candid. A colleague conducts two interviews to check for this effect.

### Worked example

Elena frames an exploratory question on teachers' app adoption, plans ten interviews with thematic analysis, sets ethics safeguards against naming children and lists limits.

> **Synthetic case.** The study plan is synthetic.

### Errors and limits

Interviews capture reported behaviour; compare with records where possible.

### Exercises

- **EX052 — Exploratory framing.** Why frame the question as exploratory? *Rubric:* 3 = little is known about teachers' reasoning, so interviews suit it;; 2 = mentions novelty;; 1 = hypothesis;; 0 = none.
- **EX053 — Children in transcripts.** How does Elena handle mentions of children in interviews? *Rubric:* 3 = asks participants not to name children and deletes names from transcripts;; 2 = one part;; 1 = keeps;; 0 = none.
- **EX054 — Placement influence.** Why might Elena's placement role affect answers? *Rubric:* 3 = teachers may tell her what they think the trust wants to hear;; 2 = mentions bias;; 1 = no effect;; 0 = none.

### Synthesis

Chapter 18 plans research. Chapter 19 sets the scope and theory of data protection.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Privacy and data protection: scope and theory

### Learning outcomes

You will (1) define the scope of data protection law; (2) relate theory to legal concepts; (3) understand where law ends and ethics continues.

### 19.1 Scope of the law

Elena studies the scope of the GDPR. It applies to processing of personal data by automated means or in filing systems, with exceptions such as purely household activities. Personal data means any information relating to an identified or identifiable natural person. The LGPD has a similar definition. Elena notes that pupil data clearly fall within scope, as do photographs and voice recordings in which children can be recognised. Article 4(1) defines personal data broadly. It covers any information relating to an identifiable person, including indirect identifiers.

### 19.2 Identifiability

Recital 26 explains that identifiability depends on the means reasonably likely to be used. Elena applies this to a published table of exam results for a small school. If a table shows that one pupil with free school meals achieved a certain grade, readers may identify the child. The data are therefore personal even though no name appears. She links this to the counting exercise in Chapter 6 and to Sweeney's research. Recital 26 sets the test. It asks what means are reasonably likely to be used to identify someone.

### 19.3 Theory and law

Elena compares legal concepts with privacy theory. The law's purpose limitation resembles contextual integrity's concern with flows matching contexts. Solove's harms, such as exclusion and secondary use, correspond to rights of access and purpose limitation. She notes that theory often explains why a legal rule exists, which helps staff understand and follow it rather than seeing it as arbitrary. Contextual integrity, for instance, explains why data shared with a teacher should not reach app advertisers, which matches the purpose limitation rule.

### 19.4 Beyond the law

Some practices may be lawful but still harmful. A school might lawfully share class photographs with parents, but a photograph showing a child in a distressing moment could cause harm. Elena writes that the trust should consider children's dignity and feelings, not only legal permissions. Dr. Asante agrees and notes that ethics continues where law is silent, especially for children who cannot easily speak for themselves. She adds an ethics question to vetting. Is this fair to the child? She asks it every time.

### Worked example

Elena defines the GDPR's scope, shows how a small school's results table can identify a pupil, maps theory to legal rules and adds dignity as a consideration beyond the law.

> **Synthetic case.** Examples are synthetic; GDPR Recital 26, the LGPD, Solove (2006), Nissenbaum (2004) and Sweeney (2002) are real.

### Errors and limits

Identifiability is contextual; the same table may be safe for a large school.

### Exercises

- **EX055 — Personal data definition.** What does personal data mean under the GDPR? *Rubric:* 3 = information relating to an identified or identifiable natural person;; 2 = close;; 1 = wrong;; 0 = none.
- **EX056 — Nameless table.** How can a results table without names be personal data? *Rubric:* 3 = small cells let readers identify a child;; 2 = mentions small numbers;; 1 = never;; 0 = none.
- **EX057 — Lawful but harmful.** Give an example of lawful but harmful processing from the chapter. *Rubric:* 3 = sharing a photo showing a child in distress;; 2 = example;; 1 = none;; 0 = none.

### Synthesis

Chapter 19 sets scope. Chapter 20 studies foundational cases.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Privacy and data protection: foundational cases

### Learning outcomes

You will (1) learn from published privacy research cases; (2) identify the lesson each case teaches; (3) apply lessons to schools.

### 20.1 Re-identification

Elena studies Sweeney's (2002) demonstration that a few attributes such as postcode, birth date and sex could re-identify people in supposedly anonymous health records. The lesson is that removing names does not make data anonymous. For the trust, this means that releasing pupil-level data to researchers without names but with birth date and school could still identify children, and must be treated as personal data with proper safeguards. Sweeney showed how few attributes identify people. Birth date and school can be enough for small schools.

### 20.2 Sparse data

Narayanan and Shmatikov (2008) showed that a dataset of film ratings could be linked to public reviews using a few known ratings. The lesson is that detailed behavioural data are highly identifying. Elena applies it to learning apps, which record detailed activity such as answers and timing. Such data could reveal individual children even without names, which strengthens her concern about apps sharing activity logs with third parties. App logs record each click and its time. A few timestamps can single out one child.

### 20.3 Behaviour and choices

Acquisti, Brandimarte and Loewenstein (2015) review evidence that people's privacy choices are uncertain, context-dependent and malleable. The lesson for the trust is that parents' consent depends heavily on how choices are presented. Elena recommends neutral consent forms that do not pre-tick options or use pressure, consistent with the EDPB consent guidelines. She notes that research on behaviour helps design fairer choices. Acquisti and colleagues show that people's privacy choices are easily shaped by design and context, so the trust's forms present choices neutrally.

### 20.4 Applying lessons

Elena writes a short guide for the trust: never treat nameless data as anonymous without analysis; treat learning activity data as identifying; and design consent choices neutrally. Each lesson is linked to a published case. Dr. Asante notes that grounding guidance in evidence makes it more persuasive to busy head teachers than general warnings, because the evidence shows that the risks are real rather than theoretical. Her slides cite each study. Each slide pairs one study with one school example, so head teachers can see why the research matters locally.

### Worked example

Elena draws three lessons from Sweeney (2002), Narayanan and Shmatikov (2008) and Acquisti et al. (2015) and turns them into a guide for the trust.

> **Synthetic case.** The guide is synthetic; the cited works and EDPB Guidelines 05/2020 are real.

### Errors and limits

Lessons from other domains need care when transferred to children's data.

### Exercises

- **EX058 — Sweeney lesson.** What lesson does Sweeney's work teach? *Rubric:* 3 = removing names does not make data anonymous;; 2 = close;; 1 = names enough;; 0 = none.
- **EX059 — Activity logs.** Why are learning app activity logs identifying? *Rubric:* 3 = detailed behavioural data can link to individuals like sparse ratings;; 2 = mentions detail;; 1 = not identifying;; 0 = none.
- **EX060 — Neutral consent.** What consent design follows from behavioural research? *Rubric:* 3 = neutral forms without pre-ticked boxes or pressure;; 2 = mentions design;; 1 = pre-tick;; 0 = none.

### Synthesis

Chapter 20 learns from cases. Chapter 21 builds system models.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Privacy and data protection: system models

### Learning outcomes

You will (1) model the trust's processing as a system; (2) build a record of processing activities; (3) identify controllers and processors.

### 21.1 Processing as a system

In the third year Elena models the trust's processing as a system of activities, each with a purpose, data categories, people affected, recipients and retention. Admissions, attendance, teaching, special educational needs support, safeguarding, catering and communications are separate activities. Modelling activities rather than systems helps her see that one system may serve several purposes, and that one purpose may use several systems. Purpose, she learns, is the organising concept that the law uses, so her model follows it. Admissions is one purpose.

### 21.2 Record of processing

Article 30 of the GDPR requires a record of processing activities. Elena builds one with a row per activity. For catering, the purpose is providing meals; data include names, dietary needs and free meal eligibility; recipients include the catering contractor; retention is the school year plus one. Building the record reveals gaps, such as no defined retention for communications. She presents the record to the data protection lead as a living document that should be updated whenever processing changes. It lists each purpose.

### 21.3 Roles

Elena identifies roles using EDPB Guidelines 07/2020. The trust is controller for its schools' processing. The catering contractor and most app vendors are processors acting on the trust's instructions. A local authority receiving census data is a separate controller with its own legal duties. She notes that roles matter because they determine who answers rights requests, who notifies breaches and what contracts are needed, and that the role depends on what an organisation actually does rather than on what a contract calls it.

### 21.4 Model checks

Elena checks the model against reality by asking staff to walk through a typical day. A teacher describes sending photographs to a parent messaging app not in the model. The app becomes a new row in the record, with a vetting review. She explains that models are useful only when checked against practice, and that conversations with staff reveal processing that no system diagram shows because it happens through informal tools chosen for convenience. She finds one class using a messaging app.

### Worked example

Elena models seven processing activities, builds an Article 30 record, assigns controller and processor roles and adds an unrecorded messaging app found by walking through a teacher's day.

> **Synthetic case.** Activities are synthetic; GDPR Article 30 and EDPB Guidelines 07/2020 are real.

### Errors and limits

Records go stale quickly; tie updates to procurement and project processes.

### Exercises

- **EX061 — Purpose-based model.** Why model activities by purpose rather than system? *Rubric:* 3 = the law organises duties around purposes; one system may serve several;; 2 = mentions purpose;; 1 = by system;; 0 = none.
- **EX062 — Census recipient.** What role does a local authority receiving census data have? *Rubric:* 3 = a separate controller;; 2 = controller;; 1 = processor;; 0 = none.
- **EX063 — Walkthrough finding.** What did the teacher walkthrough reveal? *Rubric:* 3 = an unrecorded parent messaging app used for photographs;; 2 = mentions app;; 1 = none;; 0 = none.

### Synthesis

Chapter 21 models processing. Chapter 22 examines data and dependencies.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Privacy and data protection: data and dependencies

### Learning outcomes

You will (1) vet classroom apps against criteria; (2) score dependencies consistently; (3) decide on approval or rejection.

### 22.1 Why vet apps

The trust depends on many classroom apps chosen by teachers. Each app is a dependency that receives pupil data. Elena develops a vetting scheme with five criteria worth two points each: a signed data processing agreement; data kept in the EEA or protected by transfer safeguards; no advertising or profiling of children; deletion on request; and collection of minimal fields. Apps scoring eight or more of ten are approved. The scheme gives teachers clear expectations and the trust a consistent decision rule.

### 22.2 Scoring

The lab scores five apps. MathsQuest meets every criterion and scores 10. Timetabler scores 8, missing only minimal fields, and is approved with a request to reduce fields. ClassChat scores 6, lacking an agreement and deletion on request. ReadAlong scores 4, lacking an agreement, transfer safeguards and minimal fields. QuizBlitz scores 4, lacking an agreement, transfer safeguards and a ban on advertising. Three apps are rejected until vendors address the gaps. Each criterion carries points. The scores cover agreements, transfers, data collected, advertising and deletion support for each app.

### 22.3 Children's profiling

Elena pays special attention to advertising and profiling. Recital 38 of the GDPR notes that children merit specific protection, in particular regarding marketing and profiling. QuizBlitz shows adverts to pupils and builds interest profiles. Even if a contract were signed, she recommends against it, because profiling children for advertising conflicts with the trust's duty of care. She explains that some criteria are not just points but red lines, and she adds a rule that advertising to pupils is an automatic rejection. No exceptions apply.

### 22.4 Living with decisions

Rejecting apps upsets some teachers who rely on them. Elena works with them to find approved alternatives with similar features and asks vendors of rejected apps to fix gaps. Two weeks later ClassChat signs an agreement and adds deletion, raising its score to 10. Dr. Asante notes that vetting works best as a conversation with teachers and vendors rather than a gate that only says no, because the aim is safer teaching, not fewer tools. Two rejected apps later return compliant. Teachers welcome that.

### Lab — Vetting classroom apps against five criteria

```python
# Vetting score for classroom apps: 2 points per criterion met, 0 otherwise; approve at >= 8 of 10.
crit = ["DPA signed", "data stays in EEA or safeguards", "no ads or profiling", "deletion on request", "minimal fields"]
apps = {"MathsQuest": [1, 1, 1, 1, 1], "ReadAlong": [0, 0, 1, 1, 0], "ClassChat": [0, 1, 1, 0, 1],
        "QuizBlitz": [0, 0, 0, 1, 1], "Timetabler": [1, 1, 1, 1, 0]}
for a, m in apps.items():
    s = 2 * sum(m); miss = [c for c, x in zip(crit, m) if not x]
    print(f"{a:10s} score {s:2d}/10 {'APPROVE' if s >= 8 else 'REJECT '} missing: {', '.join(miss) or '-'}")
```

Run with `python3 lab_vet.py`. Verified output:

```text
MathsQuest score 10/10 APPROVE missing: -
ReadAlong  score  4/10 REJECT  missing: DPA signed, data stays in EEA or safeguards, minimal fields
ClassChat  score  6/10 REJECT  missing: DPA signed, deletion on request
QuizBlitz  score  4/10 REJECT  missing: DPA signed, data stays in EEA or safeguards, no ads or profiling
Timetabler score  8/10 APPROVE missing: minimal fields
```

### Worked example

Elena's vetting approves MathsQuest (10) and Timetabler (8), rejects ClassChat (6), ReadAlong (4) and QuizBlitz (4), makes advertising to pupils a red line and sees ClassChat fixed to 10.

> **Synthetic case.** Apps and scores are synthetic; GDPR Recital 38 is real.

### Errors and limits

Equal weights treat criteria as equally important; red lines correct the worst cases.

### Exercises

- **EX064 — Approved apps.** Which apps are approved and with what scores? *Rubric:* 3 = MathsQuest 10 and Timetabler 8;; 2 = one;; 1 = wrong;; 0 = none.
- **EX065 — Red line.** Why make advertising to pupils an automatic rejection? *Rubric:* 3 = profiling children for marketing conflicts with their special protection;; 2 = mentions children;; 1 = points only;; 0 = none.
- **EX066 — ClassChat fix.** What changed ClassChat's score to 10? *Rubric:* 3 = it signed an agreement and added deletion on request;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Chapter 22 vets dependencies. Chapter 23 applies statistical disclosure methods.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Privacy and data protection: methods I

### Learning outcomes

You will (1) apply small-cell suppression to published tables; (2) use complementary suppression; (3) judge when tables are safe.

### 23.1 Publishing results

Schools publish exam results by group, such as pupils eligible for free school meals. Elena knows from Chapter 19 that small cells can identify children. She applies a common rule: suppress any cell with fewer than five pupils. If a school has three free-meal pupils, publishing their results would reveal much about each. Suppression hides that cell. The rule is simple, but she learns that applying it alone is not enough when totals are also published. Totals let readers subtract. Differencing attacks are a real risk.

### 23.2 Complementary suppression

If a school's total and the other-group count are published, a reader can subtract to recover the suppressed cell. Elena therefore also suppresses a complementary cell in the same school. The lab applies both rules to eight cells across four schools. Ashby has three free-meal pupils and Moor has two; both are suppressed, with their complements. Four of eight cells are suppressed: two primary and two complementary. Kelso and Penn are published in full because their smallest cells contain twelve and seven pupils.

### 23.3 Information loss

Suppression hides useful information. Readers of the table cannot compare free-meal outcomes at Ashby and Moor. Elena discusses alternatives: combining small schools into a group, reporting over three years, or publishing rounded figures. NIST SP 800-188 describes such approaches for government statistics. She recommends combining Ashby and Moor for this table, which keeps useful comparisons while protecting individuals, and she shows the trust how the table would look. Combining two small schools loses some detail but keeps trust-wide trends visible. Governors accept the table.

### 23.4 Judgement

Elena notes that thresholds such as five are conventions, not guarantees. A cell of six pupils may still reveal something if readers know who they are. For sensitive groups, such as pupils with special educational needs, she recommends a higher threshold. She explains that disclosure control combines rules with judgement about who might read the table and what they already know, which connects to the identifiability test in Recital 26. Local readers know many families. Small villages make identification easy. Context decides suppression.

### Lab — Suppressing small cells in a results table

```python
# Published exam results by school and group: suppress any cell with fewer than 5 pupils (and its complement).
table = {("Ashby", "free meals"): 3, ("Ashby", "other"): 41, ("Kelso", "free meals"): 12, ("Kelso", "other"): 36,
         ("Moor", "free meals"): 2, ("Moor", "other"): 18, ("Penn", "free meals"): 7, ("Penn", "other"): 29}
sup = set()
for (s, g), n in table.items():
    if n < 5:
        sup.add((s, g)); sup.add((s, "other" if g == "free meals" else "free meals"))
for (s, g), n in table.items():
    print(f"{s:6s} {g:11s} {'*' if (s, g) in sup else n}")
print(f"suppressed cells: {len(sup)} of {len(table)} (2 primary + 2 complementary)")
```

Run with `python3 lab_cells.py`. Verified output:

```text
Ashby  free meals  *
Ashby  other       *
Kelso  free meals  12
Kelso  other       36
Moor   free meals  *
Moor   other       *
Penn   free meals  7
Penn   other       29
suppressed cells: 4 of 8 (2 primary + 2 complementary)
```

### Worked example

Elena suppresses four of eight cells (Ashby and Moor free-meal cells and their complements), discusses information loss and recommends combining small schools and higher thresholds for sensitive groups.

> **Synthetic case.** Tables are synthetic; NIST SP 800-188 and GDPR Recital 26 are real.

### Errors and limits

Suppression across several published tables can still be undone by combining them.

### Exercises

- **EX067 — Complementary reason.** Why suppress a complementary cell? *Rubric:* 3 = otherwise subtraction from totals recovers the suppressed cell;; 2 = mentions totals;; 1 = not needed;; 0 = none.
- **EX068 — Suppressed count.** How many cells were suppressed and why? *Rubric:* 3 = four: two primary below five and two complementary;; 2 = number only;; 1 = wrong;; 0 = none.
- **EX069 — Higher threshold.** When does Elena recommend a higher threshold? *Rubric:* 3 = for sensitive groups such as special needs pupils;; 2 = mentions sensitivity;; 1 = never;; 0 = none.

### Synthesis

Chapter 23 controls disclosure. Chapter 24 designs controls.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Privacy and data protection: controls

### Learning outcomes

You will (1) design organisational and technical controls for a school trust; (2) link controls to risks; (3) assign ownership.

### 24.1 Control set

Elena designs a control set for the trust. Organisational controls include the app vetting scheme, staff training, a records retention schedule and the central request inbox. Technical controls include role-based access, single sign-on, encryption, backups and small-cell suppression. She links each control to the risks it reduces and the principles it supports. The link makes it possible to explain to governors why each control exists and what would happen if it were removed. Each control lists its risk. The list fits on two pages.

### 24.2 Retention schedule

Elena drafts a retention schedule. Pupil records follow education law requirements; safeguarding records are kept according to statutory guidance; photographs for newsletters are kept for the current year; app data are deleted when a pupil leaves. She explains that retention schedules implement storage limitation and reduce what could be exposed in a breach. She notes that some periods are set by law and must be confirmed with the trust's legal adviser. The schedule covers every record type. Legal advice confirms them.

### 24.3 Training

Training is a control. Elena designs short sessions for different roles: teachers learn about app vetting and misdirected email; office staff learn about identity checks for requests; safeguarding leads learn about secure records. Each session uses school examples and ends with a short quiz. She measures completion and quiz scores. She notes that training changes behaviour only when combined with systems that support the right choices. Quiz scores rose, but incident counts tell a more useful story about behaviour. Incidents matter most.

### 24.4 Owners

Each control needs an owner. The data protection lead owns the record of processing and request inbox; the IT manager owns access, encryption and backups; head teachers own training completion in their schools. Elena writes a one-page description for each control. Dr. Asante points out that controls without owners decay quietly, and that ownership is the difference between a policy document and a working control. Each owner has a named deputy and a review date in the operations calendar. Reviews are termly.

### Worked example

Elena designs organisational and technical controls linked to risks, drafts a retention schedule, creates role-based training with quizzes and assigns owners with one-page descriptions.

> **Synthetic case.** Controls are synthetic.

### Errors and limits

Training metrics measure attendance more than behaviour; combine with incident data.

### Exercises

- **EX070 — Linking controls.** Why link each control to risks and principles? *Rubric:* 3 = to explain why it exists and what removing it would cause;; 2 = mentions justification;; 1 = not needed;; 0 = none.
- **EX071 — Photo retention.** How long are newsletter photographs kept in the schedule? *Rubric:* 3 = the current year;; 2 = approximately;; 1 = indefinitely;; 0 = none.
- **EX072 — Owners matter.** Why does every control need an owner? *Rubric:* 3 = controls without owners decay quietly;; 2 = mentions maintenance;; 1 = optional;; 0 = none.

### Synthesis

Chapter 24 designs controls. Chapter 25 is the first laboratory.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) test controls in a safe laboratory; (2) simulate common incidents; (3) record results as evidence.

### 25.1 Lab setup

In Laboratory I Elena builds a test environment with synthetic pupils, a copy of the access configuration and test accounts for each role. No real data are used. She plans tests for access control, retention and misdirected email warnings. Dr. Asante insists on writing expected results before running tests. Elena learns that a laboratory is a place to discover failures safely, so that they can be fixed before they affect real children. All test accounts are synthetic. The lab mirrors the real configuration.

### 25.2 Access tests

Elena logs in as each role and attempts to view records. Teachers cannot see pupils from other classes; office staff cannot see support plans after her earlier fix. But a head of year can see safeguarding notes, which the role design did not intend. She traces the problem to an old permission group and removes it. She records the test, the failure and the fix with dates. One test showed a teaching assistant seeing support plans. It came from an old group.

### 25.3 Incident simulation

Elena simulates a misdirected email by sending a synthetic report to an external test address. The email system warns about an external recipient, as designed. She then simulates a lost tablet and checks that remote wipe works and that the tablet held no cached pupil data. Both succeed. She also simulates a parent's access request through the central inbox and checks that it is logged and assigned within one day. She times each step of the response. Both steps finish on time.

### 25.4 Evidence

Elena compiles results into a laboratory report: tests, expected results, actual results, failures and fixes. She notes that the report is evidence for accountability and should be kept with the trust's data protection records. She also notes what she did not test, such as vendor deletion. Dr. Asante reminds her that a test report is as valuable for what it shows is untested as for what it shows works. Untested areas are listed explicitly in the report. Vendor deletion is tested later.

### Worked example

Elena tests access, retention and incident responses on synthetic data, finds and removes a head-of-year safeguarding permission, confirms email warnings and remote wipe, and records evidence including untested areas.

> **Synthetic case.** The laboratory is synthetic.

### Errors and limits

Laboratory configurations can drift from production; compare them regularly.

### Exercises

- **EX073 — Unexpected access.** What unexpected access did testing reveal? *Rubric:* 3 = a head of year could see safeguarding notes;; 2 = mentions safeguarding;; 1 = none;; 0 = none.
- **EX074 — Lost tablet test.** What did the lost-tablet simulation check? *Rubric:* 3 = remote wipe works and no cached pupil data on the device;; 2 = one;; 1 = none;; 0 = none.
- **EX075 — Untested areas.** Why record what was not tested? *Rubric:* 3 = it shows where assurance is missing, e.g. vendor deletion;; 2 = mentions gaps;; 1 = unnecessary;; 0 = none.

### Synthesis

Chapter 25 tests controls. Chapter 26 applies further methods.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Privacy and data protection: methods II

### Learning outcomes

You will (1) match uses of data against consent records; (2) handle missing or refused consent; (3) design consent processes for children.

### 26.1 Photo consent

The trust asks parents for consent before using photographs in newsletters. Elena builds a check that matches pupils tagged in planned photographs against the consent register. A pupil is cleared only if consent is recorded as given; refusal or missing records mean the photograph must be held. Consent is one of the clearest cases where the law requires a record, because Article 7(1) of the GDPR requires the controller to be able to demonstrate that consent was given. Records are kept centrally.

### 26.2 Matching

The lab checks three planned photographs. The science fair photograph is cleared. The sports day photograph includes P02, whose parents refused. The choir photograph includes P05, whose parents refused, and P08, who has no record at all. Two of three photographs need action. Elena explains that a missing record is treated like a refusal, because consent cannot be assumed. The newsletter editor crops or replaces the two photographs. Her lab matched photographs against consent records for every pupil shown. Two photographs lacked records.

### 26.3 Withdrawal

Consent can be withdrawn at any time, as Article 7(3) states, and withdrawal must be as easy as giving consent. Elena designs a form on the parent portal for withdrawal and a process to remove photographs from future publications. Past printed newsletters cannot be recalled, which she explains honestly to parents in the consent form. She notes that being clear about what withdrawal can and cannot do is part of informed consent. Printed newsletters cannot be recalled. Online copies are removed within days.

### 26.4 Children's voice

Older pupils may have their own views. Elena recommends asking pupils aged around twelve and above whether they are happy for photographs to be used, alongside parental consent, and respecting their objection. She notes that GDPR Article 8 concerns consent for online services and sets age thresholds, but that the broader principle of respecting children's views as they mature applies more widely. Dr. Asante agrees that listening to children improves both fairness and trust. Older pupils now sign alongside parents. Their views are recorded.

### Lab — Matching photographs against consent records

```python
# Match pupils tagged in planned newsletter photos against the photo-consent register.
consent = {"P01": True, "P02": False, "P03": True, "P04": True, "P05": False, "P06": True, "P07": True, "P08": None}
photos = {"sports day": ["P01", "P02", "P03"], "science fair": ["P04", "P06", "P07"], "choir": ["P05", "P08", "P01"]}
for ev, kids in photos.items():
    bad = [k for k in kids if consent.get(k) is not True]
    print(f"{ev:12s} {'OK' if not bad else 'HOLD: ' + ', '.join(f'{k} ({consent[k]})' for k in bad)}")
print("photos needing action:", sum(1 for ks in photos.values() if any(consent.get(k) is not True for k in ks)), "of", len(photos))
```

Run with `python3 lab_photo.py`. Verified output:

```text
sports day   HOLD: P02 (False)
science fair OK
choir        HOLD: P05 (False), P08 (None)
photos needing action: 2 of 3
```

### Worked example

Elena's check clears the science fair photograph and holds two others (P02 refused; P05 refused and P08 with no record), designs easy withdrawal and adds older pupils' own views.

> **Synthetic case.** Pupils and records are synthetic; GDPR Articles 7 and 8 are real.

### Errors and limits

Tagging must be accurate; untagged pupils in photographs escape the check.

### Exercises

- **EX076 — Missing record.** How is a pupil with no consent record treated? *Rubric:* 3 = as not consented; the photograph is held;; 2 = as refusal;; 1 = as consent;; 0 = none.
- **EX077 — Held photos.** Which photographs need action? *Rubric:* 3 = sports day (P02) and choir (P05, P08);; 2 = one;; 1 = none;; 0 = none.
- **EX078 — Withdrawal honesty.** What must parents be told about withdrawal? *Rubric:* 3 = it stops future use but cannot recall printed copies;; 2 = mentions limits;; 1 = everything removed;; 0 = none.

### Synthesis

Chapter 26 manages consent. Chapter 27 verifies controls.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Privacy and data protection: verification

### Learning outcomes

You will (1) verify controls against requirements; (2) sample records for compliance; (3) report verification honestly.

### 27.1 Verification plan

Elena plans verification of the trust's controls. For each control she defines a requirement and a test. Access control: staff can see only what their role allows, tested by sampling accounts. Retention: records past their period are deleted, tested by querying the system. App vetting: no unapproved app receives data, tested by comparing the app register with network traffic. She follows a principle that every important control should be tested with evidence, not assumed. Each control gets one test. Tests follow the risk ranking.

### 27.2 Sampling

Elena samples twenty staff accounts across schools and compares each account's permissions with its role. Eighteen match; two have extra permissions left from previous roles. She reports the error rate and fixes the accounts. She explains that a sample does not prove all accounts are correct, but it gives an estimate and shows whether the joiners-movers-leavers process works. She recommends repeating the sample each term. The twenty sampled accounts come from every school, and each is checked against current staff lists.

### 27.3 Network comparison

Elena works with the IT manager to list domains that school devices contact and compares them with approved apps. Two unapproved apps appear: a free quiz site and a drawing app. Both receive pupil names through login. She contacts the teachers involved, who were unaware of the process, and helps them find approved alternatives. She notes that technical verification finds practices that policies and surveys miss. Traffic showed several apps never vetted. Two unapproved apps were found this way, both used by a single class for homework quizzes.

### 27.4 Honest reporting

Elena writes a verification report showing passes and failures. Governors ask whether the trust is compliant. She explains that the trust has improved and has evidence for many controls, but that failures remain and verification must continue. She avoids claiming full compliance, which no evidence could support. Dr. Asante notes that honest reporting builds trust with governors and regulators better than optimistic claims that later prove wrong. Her report states clearly which controls failed testing and what will be done about each one.

### Worked example

Elena verifies controls with tests, finds two of twenty sampled accounts with excess permissions, discovers two unapproved apps through network comparison and reports results without claiming full compliance.

> **Synthetic case.** Samples and findings are synthetic.

### Errors and limits

Network comparison misses apps used on home devices.

### Exercises

- **EX079 — Sample result.** What did the account sample find? *Rubric:* 3 = two of twenty accounts with extra permissions;; 2 = number only;; 1 = none;; 0 = none.
- **EX080 — Unapproved apps.** How were unapproved apps found? *Rubric:* 3 = comparing contacted domains with the approved list;; 2 = mentions network;; 1 = survey;; 0 = none.
- **EX081 — Compliance claim.** Why does Elena avoid claiming full compliance? *Rubric:* 3 = evidence cannot support it and failures remain;; 2 = mentions evidence;; 1 = claims it;; 0 = none.

### Synthesis

Chapter 27 verifies. Chapter 28 analyses failures.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Privacy and data protection: failure analysis

### Learning outcomes

You will (1) analyse a privacy incident to find root causes; (2) distinguish individual error from system failure; (3) recommend lasting fixes.

### 28.1 The incident

A synthetic incident: a teacher emails a spreadsheet of pupils' reading levels and special needs flags to all parents in a class instead of a single colleague. Elena leads the failure analysis. She gathers facts: the email client auto-completed the parent group, the spreadsheet contained more columns than needed, and there was no warning for external recipients with attachments. The breach is reported to the data protection lead within an hour. A teacher emailed a spreadsheet to all parents. Every family in the class received it.

### 28.2 Root causes

Elena asks why repeatedly. Why did the email go to parents? Auto-complete suggested the parent group. Why did the spreadsheet contain special needs flags? It was exported from the system with default columns. Why was there no warning? The warning covered external domains, but parents' addresses were in a school-managed group. She identifies three system causes, not just the teacher's error, and explains that blaming the teacher would leave the causes in place. The export included unneeded columns. Email groups were unmanaged.

### 28.3 Response

The trust assesses the risk. The spreadsheet included special needs information, which may be health data, so the risk to pupils is likely, and the trust notifies the supervisory authority within 72 hours under Article 33. It contacts parents to ask them to delete the email and informs affected families. EDPB Guidelines 9/2022 help assess the severity. Elena records the timeline and decisions. Within the first day, the trust asks each recipient to confirm deletion, and the data protection lead decides whether the authority must be notified under Article 33.

### 28.4 Lasting fixes

Elena recommends three fixes: disable auto-complete for parent groups, change export defaults to minimal columns, and extend warnings to any message with attachments sent to large groups. She also recommends sharing reports through a secure system rather than email. After the fixes, she runs a laboratory test to confirm them. Dr. Asante notes that good failure analysis produces fixes that make the same mistake hard to repeat for anyone. External attachments now trigger a warning before sending. Exports now default to minimal columns.

### Worked example

Elena analyses a misdirected spreadsheet, finds three system causes, supports notification within 72 hours and recommends disabling auto-complete, minimal export defaults, broader warnings and secure sharing.

> **Synthetic case.** The incident is synthetic; GDPR Article 33 and EDPB Guidelines 9/2022 are real.

### Errors and limits

Root cause analysis can stop too early; keep asking why until a system cause appears.

### Exercises

- **EX082 — System causes.** Name the three system causes of the incident. *Rubric:* 3 = auto-complete of parent group, default export columns, warnings limited to external domains;; 2 = two;; 1 = blame teacher;; 0 = none.
- **EX083 — Notification reason.** Why did the trust notify the supervisory authority? *Rubric:* 3 = special needs data made risk to pupils likely;; 2 = mentions sensitivity;; 1 = not needed;; 0 = none.
- **EX084 — Lasting fix.** Give one lasting fix Elena recommends. *Rubric:* 3 = e.g. minimal export columns by default;; 2 = example;; 1 = retrain only;; 0 = none.

### Synthesis

Chapter 28 learns from failure. Chapter 29 runs operations.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Privacy and data protection: operations

### Learning outcomes

You will (1) run day-to-day data protection operations; (2) handle rights requests and incidents; (3) report to leadership.

### 29.1 Operations calendar

Elena helps the data protection lead create an operations calendar. Weekly: review the request inbox and incident log. Monthly: report metrics and review new apps. Termly: access reviews, training checks and restore tests. Yearly: update the record of processing and retention schedule. The calendar turns many separate tasks into a predictable routine, which is important in schools where staff time is limited and priorities change quickly. Each month lists due tasks and owners, such as access reviews in September and retention deletion in July.

### 29.2 Requests and incidents

With the central inbox, requests are logged and assigned on arrival. Elena handles a request from a parent who wants all data about their child, including emails mentioning the child. She works with the data protection lead to search email systems and redact information about other pupils. She learns that access requests often involve judgement about third-party information, and that EDPB Guidelines 01/2022 discuss how to balance rights of others. Redaction protects other pupils. Other pupils' details are removed before any record is released.

### 29.3 Metrics

Elena reports monthly metrics to leadership: requests received and on time, incidents and time to report, apps vetted and rejected, access review completion and training completion. She presents trends with brief explanations. Leadership asks for fewer numbers and more meaning, so she adds a short paragraph on what changed and what needs attention. She learns that metrics are useful only when someone acts on them. Her monthly page shows five figures with a comment on each. Five figures fit on one page.

### 29.4 Sustaining

Elena notes that operations depend on the data protection lead, a single person. If the lead is ill, tasks stop. She recommends a deputy and documented procedures. She also recommends that each school name a privacy champion who handles local questions and escalates issues. Dr. Asante points out that resilience applies to people as well as systems, and that small organisations are especially vulnerable to losing key individuals. Each role now has a written procedure and a trained deputy. Cover is now planned.

### Worked example

Elena creates an operations calendar, handles an access request involving redaction of other pupils, reports monthly metrics with commentary and recommends a deputy and school privacy champions.

> **Synthetic case.** Operations are synthetic; EDPB Guidelines 01/2022 are real.

### Errors and limits

Champions need time and training; naming them is not enough.

### Exercises

- **EX085 — Calendar purpose.** What does the operations calendar achieve? *Rubric:* 3 = turns separate tasks into a predictable routine;; 2 = mentions routine;; 1 = none;; 0 = none.
- **EX086 — Redaction.** Why redact parts of emails in an access request? *Rubric:* 3 = they contain information about other pupils;; 2 = mentions others;; 1 = send all;; 0 = none.
- **EX087 — Single point.** What single point of failure does Elena identify? *Rubric:* 3 = the data protection lead as the only person running operations;; 2 = mentions lead;; 1 = none;; 0 = none.

### Synthesis

Chapter 29 runs operations. Chapter 30 is the second laboratory.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) test end-to-end processes; (2) test vendor deletion; (3) improve processes from test results.

### 30.1 End-to-end test

In Laboratory II Elena tests the full life of a synthetic pupil: admission, class assignment, app accounts, photographs with consent, an access request and leaving the trust. She checks that each step creates, uses and deletes data as designed. When the pupil leaves, the management system marks them as left, single sign-on removes app access, and the retention schedule sets deletion dates. The test confirms that the main systems work together. A synthetic pupil leaves the trust. Each system is checked for the pupil's record.

### 30.2 Vendor deletion

The untested area from Laboratory I was vendor deletion. Elena asks three approved app vendors to delete the synthetic pupil's data and confirm. Two confirm within a week with deletion records. One replies that data are retained for a year for analytics. That contradicts the trust's agreement, which requires deletion on request. Elena escalates to the data protection lead, who contacts the vendor to enforce the contract. The vendor kept the record. The app's support page claimed records are kept for three years after leaving.

### 30.3 Process improvements

Elena recommends adding vendor deletion confirmation to the leaver process, with a reminder if no confirmation arrives in two weeks. She also recommends including deletion testing in yearly vendor reviews. She notes that contracts are only as strong as the trust's ability to check them, and that a simple test with a synthetic pupil revealed a real gap that paperwork had hidden. Vendor deletion is now confirmed in writing, and the synthetic pupil test is repeated each summer. The contract now has a deletion clause.

### 30.4 Reflection

Elena reflects on the two laboratories. The first tested controls in isolation; the second tested processes across systems and vendors. The second found more serious gaps, because failures often occur at boundaries. Dr. Asante notes that end-to-end testing with synthetic subjects is one of the most effective tools in data protection practice, and that it should become a routine part of the trust's operations rather than a one-off exercise. The test took one afternoon. It found what audits missed for years.

### Worked example

Elena tests a synthetic pupil's life cycle end to end, finds a vendor retaining data for a year against its contract, and adds deletion confirmations to the leaver process.

> **Synthetic case.** The pupil and vendors are synthetic.

### Errors and limits

Vendors may confirm deletion without verifying it; request evidence where possible.

### Exercises

- **EX088 — Vendor gap.** What did the vendor deletion test reveal? *Rubric:* 3 = one vendor kept data for a year contrary to its contract;; 2 = mentions retention;; 1 = none;; 0 = none.
- **EX089 — Leaver process.** What did Elena add to the leaver process? *Rubric:* 3 = vendor deletion confirmation with a two-week reminder;; 2 = mentions confirmation;; 1 = none;; 0 = none.
- **EX090 — Boundaries.** Why did the second laboratory find more serious gaps? *Rubric:* 3 = failures often occur at boundaries between systems and vendors;; 2 = mentions boundaries;; 1 = luck;; 0 = none.

### Synthesis

Chapter 30 tests processes. Chapter 31 examines advanced cases.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Privacy and data protection: advanced cases

### Learning outcomes

You will (1) analyse difficult cases involving children's data; (2) weigh competing rights; (3) document reasoning for contested decisions.

### 31.1 Separated parents

A father who does not live with his child asks for the child's school records. The mother objects. Elena studies the case with the data protection lead. Parental rights to educational information may come from education law, while access to personal data comes from data protection law. A court order may restrict one parent's access. She learns that such cases need careful checks of legal status and that the child's safety must be considered, especially where there are safeguarding concerns about one parent.

### 31.2 Pupil's own request

A fourteen-year-old pupil asks to see what the school holds about her, without telling her parents. Elena learns that children can exercise their own rights when they understand them, and that the school should usually respond to the child directly. EDPB Guidelines 01/2022 address requests by and on behalf of children. The case shows that children are rights-holders in their own name, not only through their parents. A fourteen-year-old can usually exercise the right of access herself, depending on maturity. Her parents are informed.

### 31.3 Police request

Police ask a school for a pupil's attendance records in an investigation. Elena learns that disclosure to authorities may be lawful under specific provisions but must be checked: the request should be in writing, state the purpose and the legal basis, and be limited to what is necessary. The data protection lead decides, documents the decision and discloses only the attendance dates requested. She notes that urgency does not remove the need for a record of what was shared and why. A record is kept.

### 31.4 Documenting contested decisions

In each case Elena helps write a decision record: facts, legal basis, rights considered, decision and reviewer. She explains that contested decisions may be challenged later by a parent, a regulator or a court, and that a clear record shows the trust acted carefully. Dr. Asante notes that good records protect children and staff alike, because they show that decisions were made thoughtfully rather than under pressure. Each record names the decision, the reasons and who agreed it. Records are kept for review.

### Worked example

Elena works through a separated parent's request, a pupil's own access request and a police request, and writes decision records for each contested case.

> **Synthetic case.** Cases are synthetic; EDPB Guidelines 01/2022 are real.

### Errors and limits

Family and police disclosure rules vary by jurisdiction; always confirm local law.

### Exercises

- **EX091 — Pupil requester.** How should the school respond to a mature pupil's own access request? *Rubric:* 3 = usually directly to the pupil, as a rights-holder;; 2 = mentions pupil;; 1 = parents only;; 0 = none.
- **EX092 — Police checks.** What should a police request include before disclosure? *Rubric:* 3 = written request with purpose and legal basis, limited to necessary data;; 2 = two;; 1 = disclose all;; 0 = none.
- **EX093 — Decision records.** Why keep decision records for contested cases? *Rubric:* 3 = decisions may be challenged later and records show careful reasoning;; 2 = mentions challenge;; 1 = optional;; 0 = none.

### Synthesis

Chapter 31 handles hard cases. Chapter 32 explores interdisciplinary interfaces.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Privacy and data protection: interdisciplinary interfaces

### Learning outcomes

You will (1) work with education, safeguarding and legal professionals; (2) translate between disciplines; (3) resolve conflicts between professional goals.

### 32.1 Working with educators

Teachers want tools that help children learn. Elena learns to frame privacy as part of good teaching: an app that profiles children for advertising undermines the trust between school and family. She works with a curriculum lead to include privacy questions in the process for choosing resources. Translating privacy into educational language, she finds, gains more support than presenting it as a legal requirement imposed from outside. Teachers respond to classroom examples such as a reading app. They want examples, not rules.

### 32.2 Working with safeguarding

Safeguarding leads must share information to protect children, sometimes quickly. Elena learns that data protection law does not prevent sharing to protect a child at risk, and that fear of breaking privacy rules should never delay necessary safeguarding. She helps write guidance stating that safeguarding information may be shared when needed to protect a child, recorded afterwards, and limited to what is necessary. The guidance reduces hesitation without abandoning care. Staff now share concerns faster. Clear guidance on lawful sharing gives staff confidence to act.

### 32.3 Working with lawyers

The trust's legal adviser interprets law; Elena explains systems. In a discussion about retention, the adviser explains statutory periods and Elena explains which systems can enforce them automatically. Together they produce a retention schedule that is both lawful and implementable. She learns that lawyers and technologists each have half of the answer, and that projects go wrong when either side assumes the other has handled their part. The lawyer drafts terms while Elena checks the technical facts behind them. Both review drafts.

### 32.4 Resolving conflicts

Conflicts arise. The curriculum lead wants learning analytics that track every click; Elena prefers coarse data. They agree on weekly summaries per pupil, kept for the school year, which give teachers what they need without detailed tracking. Dr. Asante notes that interdisciplinary work succeeds when each side states its real goal rather than its preferred solution, because goals can often be met in more than one way. Stating goals first turned a stalemate about a homework app into a shared solution.

### Worked example

Elena frames privacy in educational terms, writes guidance that safeguarding sharing must not be delayed by privacy fears, co-designs an implementable retention schedule with the legal adviser and negotiates weekly analytics summaries.

> **Synthetic case.** Colleagues and decisions are synthetic.

### Errors and limits

Translating across disciplines can oversimplify; check meanings with each professional.

### Exercises

- **EX094 — Safeguarding guidance.** What does the safeguarding guidance say about privacy? *Rubric:* 3 = sharing to protect a child at risk is allowed, recorded and limited to what is necessary;; 2 = mentions sharing;; 1 = forbids;; 0 = none.
- **EX095 — Lawyers and engineers.** What does Elena learn from working with the legal adviser? *Rubric:* 3 = each discipline holds half of the answer;; 2 = mentions cooperation;; 1 = lawyers decide all;; 0 = none.
- **EX096 — Analytics compromise.** What analytics compromise was agreed? *Rubric:* 3 = weekly summaries per pupil kept for the school year;; 2 = mentions summaries;; 1 = click tracking;; 0 = none.

### Synthesis

Chapter 32 works across disciplines. Chapter 33 advances research methods.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse qualitative interview data; (2) combine qualitative and quantitative evidence; (3) report findings with limits.

### 33.1 Analysing interviews

Elena conducts the ten teacher interviews planned in Chapter 18. She transcribes them, removes any names and codes recurring reasons for adopting apps without checks. Four themes emerge: time pressure, trust in popularity, lack of knowledge about the vetting process and belief that free apps are harmless. She counts how many teachers mention each theme and keeps illustrative quotations without identifying details. Time pressure is mentioned most often, usually when a teacher starts a new topic at short notice. Coding is checked twice.

### 33.2 Combining evidence

Elena compares themes with the app register. Teachers who mentioned not knowing the process taught in schools with the most unapproved apps. The combination of qualitative and quantitative evidence strengthens her interpretation: lack of awareness, not resistance, drives most unchecked adoption. She notes that mixed methods allow each source to check the other and give a fuller picture than either alone. Interview themes match the register's gaps. The register shows many unvetted apps in exactly the subjects where teachers described the heaviest time pressure, so the two sources agree.

### 33.3 Recommendations

Based on findings, Elena recommends a two-minute guide to vetting in staff induction, an approved app catalogue on the intranet and a fast-track review for requested apps within five school days. She links each recommendation to a theme. She also recommends explaining why free apps may cost children their data, addressing the fourth theme directly with examples from the vetting scores. Faster vetting comes first, with a target of five days for simple apps. Clear contact details for the vetting team follow.

### 33.4 Limits

Elena reports limits: ten teachers, possible desire to please, and her placement role. Two interviews conducted by a colleague produced similar themes, which offers some reassurance. She avoids claiming the findings apply to all schools. Dr. Asante praises the clear link from evidence to recommendations and the honest limits, noting that small studies are useful when they inform specific decisions. Ten interviews from one trust cannot represent all teachers, but they explain this trust's patterns well enough to guide its next steps.

### Worked example

Elena finds four themes (time pressure, popularity, unawareness, free means harmless), links unawareness to unapproved apps in the register and recommends induction guidance, a catalogue and fast-track reviews.

> **Synthetic case.** Interviews and themes are synthetic.

### Errors and limits

Theme counts depend on coding; a second coder improves reliability.

### Exercises

- **EX097 — Main driver.** What drives most unchecked adoption according to the combined evidence? *Rubric:* 3 = lack of awareness of the process;; 2 = mentions awareness;; 1 = resistance;; 0 = none.
- **EX098 — Fast-track.** What fast-track did Elena recommend? *Rubric:* 3 = review of requested apps within five school days;; 2 = mentions speed;; 1 = none;; 0 = none.
- **EX099 — Second interviewer.** Why did a colleague conduct two interviews? *Rubric:* 3 = to check whether her role influenced answers;; 2 = mentions bias;; 1 = none;; 0 = none.

### Synthesis

Chapter 33 analyses evidence. Chapter 34 runs a comparative project.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare privacy practice across two organisations; (2) use consistent criteria; (3) learn from differences without ranking unfairly.

### 34.1 The comparison

Elena compares Brindle Valley with the fictional Harrow Lane Academy, a single large secondary school. She uses consistent criteria: record of processing, app vetting, rights handling, retention and training. She gathers evidence through documents and interviews with each organisation's data protection lead. The comparison aims to learn what works, not to rank schools publicly, which both organisations agree to before participating. Both organisations share policies and evidence openly with each other. The partner is a similar-sized trust in another region, chosen because its data protection lead volunteered.

### 34.2 Findings

Harrow Lane has a stronger retention process, with automatic deletion in its management system, while Brindle Valley has stronger app vetting after Elena's work. Harrow Lane answers rights requests faster because one office handles them, but its training is limited to an annual video. Each organisation has something to learn from the other. Elena presents the findings as a table with evidence for each rating. The partner automates retention, while Brindle Valley trains staff more often. Each rating cites evidence. Both learn something.

### 34.3 Context

Elena notes that context explains differences. A single secondary school has older pupils, more staff in one place and a dedicated administrator. A trust of primary schools has younger pupils and staff spread across sites. Practices must suit context. She avoids recommending that one organisation simply copy the other, instead identifying principles behind good practices, such as automation of retention, that can be adapted. Sizes and budgets differ greatly. The partner trust has a full-time lead, while Brindle Valley shares one between many schools.

### 34.4 Sharing

Both organisations receive the report and agree to share practices. Harrow Lane adopts Brindle Valley's vetting criteria; Brindle Valley explores automated retention. Elena reflects that comparison works best with consent and collaboration, and that respecting context avoids unfair judgements. Dr. Asante notes that sector learning is valuable because small organisations rarely have time to develop every practice themselves. The findings are shared anonymously at a regional meeting of school data protection leads, where other trusts recognise the same patterns and ask for the comparison template.

### Worked example

Elena compares the trust with Harrow Lane Academy using five criteria, finds complementary strengths, explains differences by context and helps both organisations share practices.

> **Synthetic case.** Both organisations are synthetic.

### Errors and limits

Document-based comparison can miss practice; interviews reduce but do not remove this gap.

### Exercises

- **EX100 — Harrow Lane strength.** What does Harrow Lane do better? *Rubric:* 3 = automatic retention and faster rights handling;; 2 = one;; 1 = none;; 0 = none.
- **EX101 — Context matters.** Why should one organisation not simply copy the other? *Rubric:* 3 = context differs, so principles must be adapted;; 2 = mentions context;; 1 = copy;; 0 = none.
- **EX102 — Comparison ethics.** What did both organisations agree before participating? *Rubric:* 3 = the aim is learning, not public ranking;; 2 = mentions consent;; 1 = none;; 0 = none.

### Synthesis

Chapter 34 compares practice. Chapter 35 proposes the capstone.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone that improves practice; (2) define success criteria; (3) plan risks and ethics.

### 35.1 Proposal

Elena proposes a capstone: a privacy-aware parent communication system for the trust, replacing email for sensitive reports. Reports would be shared through a secure portal with authentication, so that misdirected emails like the incident in Chapter 28 become impossible for those documents. She defines the scope: reports and letters about individual pupils, not general newsletters. She explains the problem with evidence from the incident log and the failure analysis. A secure parent portal would replace emailed reports. Parents would log in to read reports, and staff would upload them once rather than emailing each family separately with attachments.

### 35.2 Criteria

Success criteria: no sensitive reports sent by email after rollout; at least 85% of parents able to access the portal within a term; requests from parents without internet access handled through alternatives; and staff time not increased. She defines how each will be measured. She notes that the third criterion protects fairness, because some families have limited digital access and must not be excluded from information about their children. Four criteria are set before building. Each is measurable. Activation, errors, staff time and access equity are measured.

### 35.3 Risks

Elena lists risks: parents unable to log in, a portal breach exposing many reports, staff reverting to email under time pressure, and vendor dependence. Controls include support for parents, strong security and monitoring, making the portal faster than email for staff, and contract terms. She plans a DPIA because the portal processes children's data at scale, following WP248 criteria. The DPIA records children's data at scale. Risks include wrong parent links, weak passwords, vendor access and exclusion of families without devices.

### 35.4 Ethics and approval

The capstone involves real processes but Elena tests with synthetic data until the trust's data protection lead approves the DPIA. Parents are informed before rollout. Dr. Asante approves the proposal with the condition that Elena measures outcomes honestly, including if the portal fails some criteria. She notes the condition in her plan, recognising that a capstone is an experiment as well as a project. The trust approves on condition of honest reporting. Governors review the plan before any real family data are used.

### Worked example

Elena proposes a secure parent portal for sensitive reports with four success criteria including fairness for families without internet, lists risks and plans a DPIA under WP248 criteria.

> **Synthetic case.** The proposal is synthetic; WP248 rev.01 is real.

### Errors and limits

Portals can shift risk rather than remove it; a breach could expose many reports at once.

### Exercises

- **EX103 — Portal purpose.** What problem does the portal solve? *Rubric:* 3 = misdirected emails of sensitive reports;; 2 = mentions email;; 1 = none;; 0 = none.
- **EX104 — Fairness criterion.** Why include alternatives for parents without internet? *Rubric:* 3 = so families with limited digital access are not excluded;; 2 = mentions fairness;; 1 = ignore;; 0 = none.
- **EX105 — DPIA need.** Why plan a DPIA for the portal? *Rubric:* 3 = it processes children's data at scale, meeting WP248 criteria;; 2 = mentions children;; 1 = unnecessary;; 0 = none.

### Synthesis

Chapter 35 proposes the capstone. Chapter 36 is field practice.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) support a community organisation's data protection; (2) adapt advice to limited resources; (3) reflect on service.

### 36.1 Community placement

Elena spends a term volunteering with a fictional parents' association that runs holiday clubs. It keeps children's names, ages, allergies and emergency contacts in a shared spreadsheet. Volunteers change often. Elena helps the association understand its duties as a controller, even as a small volunteer group, and adapts advice to its limited time and money. The association runs a weekend football club for local children, with volunteer coaches and a parent committee. Its records were kept on coaches' phones. Phones get lost.

### 36.2 Practical steps

Elena recommends a few steps: a short form with only needed fields, a password-protected shared folder instead of email attachments, a list of who can access the spreadsheet, deletion of children's details at the end of each holiday unless parents ask otherwise, and a one-page privacy notice. She avoids recommending expensive tools. The association adopts the steps in a single meeting. Cost is nearly zero. The steps include a shared password-protected spreadsheet instead of phones, deletion of old lists and consent for photographs.

### 36.3 Allergies and safety

Allergy information is health data, but it is essential for children's safety. Elena explains that the association needs it and that keeping it accurate and available to volunteers on duty is part of data protection, not opposed to it. She helps design a printed allergy card kept securely during sessions and shredded afterwards. The example shows that protecting data includes making sure the right people can use it when needed. Coaches can see allergies quickly. Safety needs access. Coaches carry the card.

### 36.4 Reflection

Elena reflects that small organisations need simple, proportionate advice. Complex frameworks would overwhelm volunteers. She learns to prioritise the few steps that reduce most risk. Dr. Asante notes that service to community groups builds understanding of how data protection works for people without specialists, and that proportionality is a principle of the law as well as of good advice. Small groups need simple, proportionate advice that volunteers can follow without legal training. The committee thanked her warmly. Proportionate advice gets adopted.

### Worked example

Elena helps a parents' association minimise fields, secure its spreadsheet, delete data after holidays, publish a notice and handle allergy data with printed cards shredded after sessions.

> **Synthetic case.** The association is synthetic.

### Errors and limits

Volunteer turnover undoes practices; keep instructions short and repeated.

### Exercises

- **EX106 — Small controller.** Does a volunteer parents' association have data protection duties? *Rubric:* 3 = yes; it is a controller of children's data;; 2 = yes;; 1 = no;; 0 = none.
- **EX107 — Allergy balance.** How is allergy data handled at sessions? *Rubric:* 3 = printed card kept securely and shredded afterwards;; 2 = one part;; 1 = email;; 0 = none.
- **EX108 — Proportionate advice.** Why avoid complex frameworks for the association? *Rubric:* 3 = volunteers lack time; a few steps reduce most risk;; 2 = mentions simplicity;; 1 = full framework;; 0 = none.

### Synthesis

Chapter 36 serves the community. Chapter 37 reviews evidence.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) review evidence for privacy interventions; (2) judge strength of evidence; (3) present a balanced review.

### 37.1 The question

In the evidence review seminar Elena asks: what evidence supports privacy training for staff in reducing incidents? She searches for studies and finds that many evaluate knowledge after training, fewer measure behaviour and very few measure incidents. She categorises studies by outcome measured. She learns that the outcome that matters most, fewer incidents, is the hardest to measure and the least studied. Most studies measure knowledge only. Few studies measured incidents directly, and those that did often lacked comparison groups. Measurement is hard.

### 37.2 Strength of evidence

Elena judges studies by design, sample size and outcome. A randomised study with incident outcomes would be strong; a survey of satisfaction with training is weak. Most of what she finds is in between. She applies the judgement to her trust's data: training completion rose while misdirected emails fell after technical changes, so training alone cannot be credited. She writes that the evidence supports training as part of a set of measures, not alone. Evidence remains weak. Confounders abound. Context matters greatly.

### 37.3 Balanced presentation

Elena presents her review to the seminar, giving the strongest evidence first and stating uncertainties clearly. A classmate argues that training is legally expected under accountability regardless of evidence. Elena agrees that it may be expected but says evidence should shape how training is designed. The discussion shows the difference between justifying an activity and designing it well. She presents what the studies show, what they cannot show and what the trust should therefore measure itself. Training remains worthwhile. Design matters most.

### 37.4 Using the review

Elena recommends that the trust measure incidents before and after future training changes and combine training with technical measures. She also suggests sharing anonymised results with other trusts to build evidence. Dr. Asante notes that practitioners can contribute evidence by measuring carefully, and that the field needs more such contributions to move beyond assumptions. She recommends that the trust records incidents before and after each training change, so that in two years it has evidence of its own rather than borrowed assumptions.

### Worked example

Elena finds little evidence linking training to fewer incidents, judges studies by design and outcome, notes that her trust's email reduction followed technical changes and recommends measuring future changes.

> **Synthetic case.** The review is synthetic.

### Errors and limits

A short review may miss studies; record search methods.

### Exercises

- **EX109 — Least studied outcome.** Which outcome is least studied in training research? *Rubric:* 3 = reduction in incidents;; 2 = mentions incidents;; 1 = knowledge;; 0 = none.
- **EX110 — Credit for improvement.** Why can training not be credited for fewer misdirected emails? *Rubric:* 3 = technical changes happened at the same time;; 2 = mentions confounding;; 1 = full credit;; 0 = none.
- **EX111 — Justify versus design.** What is the difference between justifying and designing training? *Rubric:* 3 = it may be expected anyway, but evidence should shape its design;; 2 = mentions evidence;; 1 = same;; 0 = none.

### Synthesis

Chapter 37 reviews evidence. Chapter 38 implements the capstone.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement the parent portal with privacy controls; (2) roll out in stages; (3) handle problems during rollout.

### 38.1 Building

Elena works with the trust's IT manager and a vendor to configure the parent portal. Parents authenticate with an account linked to their child; reports are uploaded by staff and visible only to linked parents. Access is logged. Documents expire after the school year. She configures the system with synthetic families first and tests each role. The DPIA is approved before any real data are used. Each role is tested first. Staff accounts use single sign-on. Roles mirror school staff structures.

### 38.2 Linking parents

Linking parents to children is the hardest part. Errors could show one family's report to another. Elena designs a process: the school office verifies identity and sends a one-time code by post to the address on record. Separated parents are linked according to the legal information held by the school. She tests the process with synthetic cases including complex family situations, which reveal two edge cases she fixes. Each link is checked against school records. Separated parents are handled carefully. Errors are rare.

### 38.3 Staged rollout

Elena rolls out to two schools first. In the first month 78% of parents activate accounts. Staff report that uploading is faster than emailing. Three parents without internet receive printed copies. One linking error is caught before any report is shared because the parent notices an unfamiliar child name and reports it. Elena traces the error to a typing mistake and adds a confirmation step for office staff. One school starts first. Feedback shapes the next school. One error is caught early.

### 38.4 Expanding

After fixes, the portal rolls out to all twelve schools. Elena monitors activation, support requests and any emails of reports still being sent. She finds a few staff still emailing reports and contacts them to understand why: they did not know how to upload large files. She arranges help. She learns that implementation is mostly about people and processes, with technology as the easier part. Staff guides help the most. Help desks run at drop-off times. Staff ask good questions.

### Worked example

Elena configures the portal, designs postal-code linking for parents, rolls out to two schools (78% activation, one linking error caught and fixed) and expands to all twelve schools.

> **Synthetic case.** The portal and rollout are synthetic.

### Errors and limits

Postal codes delay activation; balance security with convenience.

### Exercises

- **EX112 — Linking process.** How are parents linked to children? *Rubric:* 3 = office identity check and a one-time code posted to the recorded address;; 2 = one part;; 1 = self-registration;; 0 = none.
- **EX113 — Linking error.** How was the linking error caught and fixed? *Rubric:* 3 = a parent saw an unfamiliar name; a confirmation step was added;; 2 = one part;; 1 = none;; 0 = none.
- **EX114 — Remaining emails.** Why did some staff still email reports? *Rubric:* 3 = they did not know how to upload large files;; 2 = mentions training;; 1 = refused;; 0 = none.

### Synthesis

Chapter 38 implements the portal. Chapter 39 evaluates it.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against criteria; (2) report unmet criteria honestly; (3) recommend next steps.

### 39.1 Results

Elena evaluates the portal after one term. Sensitive reports by email fall from about forty a month to three. Parent activation reaches 83%, below the 85% target. Families without internet receive printed reports. Staff time spent on sending reports decreases slightly. Three of four criteria are met. Elena reports the activation shortfall clearly rather than rounding it up. Parent activation reached only part of its target, while misdirected report emails dropped to zero in the participating schools during the evaluation term. Activation stays low.

### 39.2 Understanding the shortfall

Elena investigates low activation. Most non-activated accounts belong to families who did not receive the posted code or speak languages other than English. She recommends translated instructions and an option to collect codes at school. She notes that the shortfall is an equity issue, not only a technical one, because families who cannot access the portal lose timely information about their children. Families without home internet or with language barriers activated least, and the trust offers help in school offices. Support helps.

### 39.3 Remaining emails

Three reports a month are still emailed. Elena finds they relate to external professionals, such as therapists, who are not on the portal. She recommends a secure sharing method for professionals. She notes that the original scope did not include them and that the evaluation identified a new need. Good evaluation, she learns, finds what the project did not anticipate. Some messages still go by email. Messages from clubs and trips still use email because the portal was scoped for reports only.

### 39.4 Next steps

Elena recommends translated materials, school collection of codes, a professional sharing route and continued monitoring. She presents the evaluation to the trust's leadership, who approve the steps. Dr. Asante praises the honest reporting of the unmet criterion and its equity dimension, noting that evaluations which hide shortfalls deny organisations the chance to improve. The trust funds assisted activation sessions in each school and will measure activation again after one term, using the same criteria as the original evaluation. Results go to governors.

### Worked example

Elena finds emailed reports fell from about forty to three a month and activation reached 83% against an 85% target, traces the gap to posted codes and language, and recommends translations and school collection.

> **Synthetic case.** Evaluation figures are synthetic.

### Errors and limits

One term is short; effects may change as novelty fades.

### Exercises

- **EX115 — Unmet criterion.** Which criterion was not met? *Rubric:* 3 = parent activation: 83% against 85%;; 2 = mentions activation;; 1 = all met;; 0 = none.
- **EX116 — Equity issue.** Why is low activation an equity issue? *Rubric:* 3 = families who cannot access the portal lose timely information;; 2 = mentions fairness;; 1 = technical only;; 0 = none.
- **EX117 — New need.** What new need did evaluation reveal? *Rubric:* 3 = secure sharing with external professionals;; 2 = mentions professionals;; 1 = none;; 0 = none.

### Synthesis

Chapter 39 evaluates honestly. Chapter 40 presents the thesis.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis on applied data protection; (2) present findings to an audience; (3) reflect on learning.

### 40.1 Thesis

Elena writes her thesis on improving data protection in a primary school trust. It covers the app register, vetting, consent checking, disclosure control, failure analysis, the parent portal and its evaluation. Each chapter presents evidence and limits. She argues that most risks in the trust came from ordinary processes, such as email and apps, and that practical controls combined with honest measurement reduced them. Her thesis follows one trust. It uses evidence from each placement chapter. Measurement anchors every claim made.

### 40.2 Presentation

Elena presents to a panel of tutors and the trust's data protection lead. She uses figures from her labs: apps without agreements, vetting scores, suppressed cells, photographs held and portal results. Questions focus on sustainability: who will maintain the register and portal? She answers with the owners and calendar established in operations. The panel asks about children's voices, and she describes asking older pupils about photographs. Her slides use evidence tables. Each claim cites a lab result. Governors attend the session.

### 40.3 Assessment

The panel commends the thesis for linking evidence to action and for honesty about shortfalls. They suggest that future work could involve pupils more directly in designing privacy information. Elena agrees and notes it as a recommendation. Dr. Asante notes that the thesis shows a full cycle from problem to evaluated improvement. The panel suggests involving pupils earlier in design decisions, such as asking them how the portal should present their own reports and photographs. She accepts this. The panel passes her thesis.

### 40.4 Reflection

Elena reflects on four years. She learned that privacy protects real people, here children who cannot easily protect themselves. She learned that law, technology and people must work together. She learned to measure and report honestly. She plans to work in data protection for schools and to keep studying children's rights. The trust offers her a part-time role as a privacy officer, which she accepts. She remains grateful to Dr. Asante. She thanks the teachers. She starts the role in September.

### Worked example

Elena writes a thesis linking evidence to action, presents lab figures and sustainability plans, receives commendation and a suggestion to involve pupils, and reflects on protecting children.

> **Synthetic case.** The thesis and job offer are synthetic.

### Errors and limits

A single trust's experience may not generalise; state context clearly.

### Exercises

- **EX118 — Thesis argument.** What is Elena's main thesis argument? *Rubric:* 3 = most risks came from ordinary processes, reduced by practical controls and measurement;; 2 = mentions processes;; 1 = technology only;; 0 = none.
- **EX119 — Sustainability answer.** How does Elena answer the sustainability question? *Rubric:* 3 = owners and an operations calendar maintain register and portal;; 2 = mentions owners;; 1 = none;; 0 = none.
- **EX120 — Future work.** What future work did the panel suggest? *Rubric:* 3 = involving pupils in designing privacy information;; 2 = mentions pupils;; 1 = none;; 0 = none.

### Synthesis

Chapter 40 completes the bachelor's route. The worked results follow, then the references.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Elena Rossi, Dr. Kwame Asante, Fairhaven College, Brindle Valley Schools Trust, Harrow Lane Academy and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Sharing is allowed only when necessity holds and there is a lawful basis, which need not be parental consent.

**EX002.** That widespread use means the vendor handles children's data properly.

**EX003.** About one in six: 9 of roughly 59 flagged apps.

**EX004.** That no one in the trust had a full picture of where pupil data were held.

**EX005.** Security depends on configuration and maintenance, so a managed cloud service can be safer than a neglected local server.

**EX006.** Full-disk encryption for staff laptops and automatic sign-out on shared tablets.

**EX007.** Synthetic data allow safe mistakes and sharing without exposing children.

**EX008.** General users get class counts; only the attendance officer gets the protected named list.

**EX009.** It refuses to run and explains that the column is not needed.

**EX010.** Because summaries may be wrong, as one blog misstated consent rules for photographs.

**EX011.** A claim, supporting evidence and an explanation of how the evidence supports it.

**EX012.** Protected newsletters and pages can celebrate pupils with less exposure.

**EX013.** Misdirected emails, such as one family's report sent to another.

**EX014.** Yes, it is a personal data breach even though accidental.

**EX015.** Fear makes people hide mistakes; quick reporting is needed for timely assessment and notification.

**EX016.** A dietary list can reveal religion or health conditions.

**EX017.** Office staff had access to special needs support plans without need.

**EX018.** Exposure at any edge, such as an analytics subprocessor, exposes the data on that path.

**EX019.** They record sites visited by identifiable pupils, including sensitive searches.

**EX020.** Shorter retention, access only for designated safeguarding staff and clear information to families.

**EX021.** Pupils may avoid seeking help for sensitive problems if they feel watched.

**EX022.** It checks the teacher's role and whether the pupil is in their classes.

**EX023.** The data protection lead's key could link pseudonyms back to pupils.

**EX024.** Teachers retained access to pupils after class changes; access now updates automatically.

**EX025.** ClassChat, ReadAlong and QuizBlitz.

**EX026.** It receives a special educational needs flag, sends data outside the EEA and has no agreement.

**EX027.** Apps and sharing change, and a regularly queried register finds new gaps.

**EX028.** GDPR Recital 38 and LGPD Article 14.

**EX029.** Her agreement allows only synthetic data, so viewing real records would exceed her authority.

**EX030.** Investigating requires authority and access that only the lead can grant.

**EX031.** Every pupil can see others' files and browsing history.

**EX032.** Access was limited to safeguarding leads and auditing switched on.

**EX033.** Deleted accounts can leave recoverable data; secure erase or key destruction is needed.

**EX034.** From 22% to 29%.

**EX035.** Kelso sends an annual letter listing apps; this may explain the difference but is not proven.

**EX036.** She removes identifying details from comments and reports school figures only where twenty or more responded.

**EX037.** A former special needs coordinator with support plan access and a teacher who left with an active account.

**EX038.** Eleven of 340 in the first review, three in the second.

**EX039.** Young children cannot manage complex passwords, which leads to shared logins.

**EX040.** Information shared in confidence with a teacher should stay within that context.

**EX041.** Because refusal is not genuinely free when the data are necessary for teaching.

**EX042.** They were stored with names although aggregated analysis would meet the purpose.

**EX043.** 6 of 20 (30%).

**EX044.** No. Extensions are allowed for complex or numerous requests with notice, not for holidays.

**EX045.** With few requests, percentages swing widely, so counts give context.

**EX046.** Separation means a compromise of ordinary accounts does not expose safeguarding notes.

**EX047.** Central control of access and the ability to remove access to every app at once.

**EX048.** Backups contain personal data, so they must expire like the originals.

**EX049.** Use encrypted drives or, better, stop exports to removable media.

**EX050.** If he leaves or loses it, backups cannot be restored.

**EX051.** Misuse by authorised users and collecting more data than needed.

**EX052.** Little prior knowledge exists, so open exploration fits better than testing a hypothesis.

**EX053.** Participants are asked not to name pupils, and any names are deleted.

**EX054.** Teachers may present themselves favourably to someone linked to the trust.

**EX055.** Any information relating to an identified or identifiable natural person.

**EX056.** In small schools, a cell describing one pupil can identify that child.

**EX057.** Sharing a lawful class photograph that shows a child in a distressing moment.

**EX058.** Removing names leaves data identifiable through other attributes.

**EX059.** Detailed activity patterns are distinctive, like film ratings in Narayanan and Shmatikov's study.

**EX060.** Neutral forms without pre-ticked options or pressure.

**EX061.** Because legal duties attach to purposes, and systems and purposes do not map one to one.

**EX062.** It is a separate controller with its own duties.

**EX063.** A parent messaging app used to send photographs that the record did not include.

**EX064.** MathsQuest with 10 and Timetabler with 8.

**EX065.** Recital 38 highlights children's protection from marketing and profiling, so it cannot be offset by other points.

**EX066.** Signing a data processing agreement and adding deletion on request.

**EX067.** Because readers could subtract the other group from the total to find the hidden value.

**EX068.** Four: the Ashby and Moor free-meal cells and their complements.

**EX069.** For sensitive groups like pupils with special educational needs.

**EX070.** So governors can see why each control matters and the effect of removing it.

**EX071.** For the current school year.

**EX072.** Without an owner, nobody maintains a control and it decays unnoticed.

**EX073.** Heads of year could view safeguarding notes through an old permission group.

**EX074.** That remote wipe works and that the tablet stored no pupil data.

**EX075.** It identifies gaps in assurance, such as vendor deletion.

**EX076.** As without consent, so the photo is held.

**EX077.** Sports day because of P02 and choir because of P05 and P08.

**EX078.** Withdrawal stops future use, but past printed newsletters cannot be recalled.

**EX079.** Two of twenty sampled accounts had leftover permissions.

**EX080.** By comparing domains contacted by school devices with approved apps.

**EX081.** Because evidence shows remaining failures and cannot prove full compliance.

**EX082.** Auto-complete suggested the parent group, exports included unnecessary columns and warnings did not cover managed parent groups.

**EX083.** Because the disclosed special needs information made a risk to pupils likely.

**EX084.** Making exports contain only minimal columns by default.

**EX085.** It organises recurring tasks into a predictable schedule.

**EX086.** To protect the rights of other pupils mentioned in the emails.

**EX087.** Reliance on one data protection lead with no deputy.

**EX088.** One vendor retained data for analytics for a year, breaching its agreement.

**EX089.** A requirement for vendor confirmation of deletion, with a reminder after two weeks.

**EX090.** Because problems tend to appear where systems and organisations meet.

**EX091.** Usually directly to the pupil, who holds the right in her own name.

**EX092.** A written request stating purpose and legal basis, with disclosure limited to what is necessary.

**EX093.** Records show how and why decisions were made if they are challenged.

**EX094.** Necessary sharing to protect a child is permitted; it should be recorded and limited.

**EX095.** Lawful and implementable rules require both legal interpretation and system knowledge.

**EX096.** Weekly per-pupil summaries retained for the school year.

**EX097.** Lack of awareness of the vetting process rather than resistance.

**EX098.** Reviewing requested apps within five school days.

**EX099.** To see whether themes changed without her placement role influencing participants.

**EX100.** It deletes records automatically and answers rights requests faster.

**EX101.** Differences in size, age of pupils and structure mean practices need adapting.

**EX102.** That the comparison is for learning, not public ranking.

**EX103.** It prevents sensitive reports being misdirected by email.

**EX104.** To ensure families with limited digital access still receive information.

**EX105.** Large-scale processing of children's data meets several high-risk criteria.

**EX106.** Yes, it controls children's personal data and must follow the law proportionately.

**EX107.** On a secure printed card available during sessions and shredded afterwards.

**EX108.** Because small volunteer groups need simple steps that address the main risks.

**EX109.** Actual reduction in incidents.

**EX110.** Because technical fixes were introduced in the same period.

**EX111.** Training may be expected for accountability, while evidence should determine how it is done.

**EX112.** The office verifies identity and posts a one-time code to the address on record.

**EX113.** A parent reported an unfamiliar child; Elena added a confirmation step for office staff.

**EX114.** They were unsure how to upload large files.

**EX115.** Parent activation, at 83% against the 85% target.

**EX116.** Families affected, often with language barriers, lose timely information about their children.

**EX117.** A secure route for sharing reports with external professionals.

**EX118.** That ordinary processes created most risks, and practical, measured controls reduced them.

**EX119.** Named owners and the operations calendar keep the register and portal maintained.

**EX120.** Involving pupils directly in designing privacy information.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
