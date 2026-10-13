# Security Governance, Risk and Compliance: Bachelor's Course

- Language: English (`en`); course 097, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; six offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students learning to build, run and evaluate a proportionate GRC programme in a small organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs query a SQLite risk register, compute Wilson intervals, patch medians, supplier tiers, matrix-versus-expected-loss rankings and a CSF gap summary on synthetic data. Risk figures are illustrations, standards are cited by edition and paraphrased, and nothing here is a real audit, attestation or legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one bachelor's student through four years centred on a housing association's GRC programme: foundations and data, identity and privacy, scope and theory, models and suppliers, risk methods and controls, laboratories, verification, failure analysis and operations, research, and a capstone that redesigns the access review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Reyes** | Bachelor's student | Invented |
| **Dr. Malik Haddad** | Tutor | Invented |
| **Brightwater College** | Fictional college | Invented |
| **Elmfield Housing Association** | Fictional social landlord, 300 staff, 4,000 homes | Invented |
| **Corbridge Community Trust** | Fictional comparison charity | Invented |

### Core sources

ISO 31000:2018; ISO/IEC 27001:2022 and 27002:2022; NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29), the [NIST Privacy Framework](https://doi.org/10.6028/NIST.CSWP.10) and [SP 800-55v1](https://doi.org/10.6028/NIST.SP.800-55v1); COBIT 2019; PCI DSS v4.0; AICPA trust services criteria; Cox (2008), [doi:10.1111/j.1539-6924.2008.01030.x](https://doi.org/10.1111/j.1539-6924.2008.01030.x); GAO-21-105263. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use proportions and rates to describe governance facts; (2) avoid common errors with percentages; (3) state claims precisely.

### 1.1 Numbers in governance

Sofia Reyes is a bachelor's student at the fictional Brightwater College. Her tutor, Dr. Malik Haddad, uses one running case across the course: the fictional Elmfield Housing Association, a social landlord with three hundred staff and four thousand homes, which holds personal data about tenants and takes rent payments online. Elmfield's managers often describe security with numbers: most staff have done training, few laptops lack encryption. Sofia learns to turn such phrases into precise proportions with a stated numerator and denominator. Sofia records this point in her course notebook so that later chapters can build on it.

### 1.2 Percentage traps

Sofia studies common traps. A rise from two incidents to four is a hundred percent increase but only two more incidents. A fall from ten percent to five percent of overdue reviews is five percentage points, not five percent. A share without its base can mislead: ninety percent of laptops encrypted means little if the count of laptops is unknown or if the ten percent unencrypted hold the most sensitive data. She practises rewriting misleading statements into honest ones that show counts and bases.

### 1.3 Precise claims

Dr. Haddad asks the class to write one precise claim about Elmfield. Sofia writes: on the first of October, two hundred and seventy of three hundred staff accounts had multi-factor authentication enabled, according to the identity system report. The claim names the date, the count, the base and the source. She learns that precise claims can be checked and challenged, while vague ones cannot, which is why auditors and boards prefer them and why governance writing should use them from the start. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### Worked example

Sofia rewrites vague statements as dated counts with bases and sources and avoids percentage traps.

> **Synthetic case.** Brightwater, Elmfield and all figures are synthetic.

### Errors and limits

Precise numbers can still be wrong. Sources can be out of date.

### Exercises

- **EX001 — Points versus percent.** A fall from ten percent to five percent is how large a change? *Rubric:* 3 = five percentage points;; 2 = points;; 1 = five percent;; 0 = none.
- **EX002 — Missing base.** Why can a ninety percent figure mislead? *Rubric:* 3 = the base and which items are missing are unknown;; 2 = base;; 1 = none;; 0 = none.
- **EX003 — Claim parts.** What four parts did Sofia's precise claim include? *Rubric:* 3 = date, count, base and source;; 2 = four;; 1 = none;; 0 = none.

### Synthesis

Precise proportions with bases and sources make governance claims checkable.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the components of an organisation's IT; (2) build a simple asset inventory; (3) see why inventories come first in governance.

### 2.1 Elmfield's systems

Sofia visits Elmfield and lists its computing systems: laptops for office staff, tablets for repairs operatives, a file server, a housing management system hosted by a supplier, cloud email, a rent payment page run by a payment provider and a small board portal. She learns that each system has hardware, software, data and people who use it. Understanding these parts helps her see where things could go wrong and who would need to act if they did. She notes the assumption behind it so that a reviewer can challenge it later.

### 2.2 The inventory

Sofia builds an asset inventory as a table: asset name, type, owner, location, data held and supplier. She finds that nobody owns the board portal and that eleven tablets are missing from the repairs team's list. ISO/IEC 27002:2022 includes guidance on inventories of information and associated assets, and NIST CSF 2.0 places asset management under its Identify function. She learns that an inventory is not paperwork but the map every later control depends on. The same reasoning will return when Elmfield's auditors visit next year.

### 2.3 Why first

Dr. Haddad explains why governance starts with inventory. Risk assessment needs to know what could be harmed. Access control needs to know which systems to control. Incident response needs to know what to restore. Without an inventory, each of these guesses. Sofia notes that inventories decay as staff buy new devices or adopt new services, so the inventory needs an owner and a review date. She recommends a quarterly check against purchase records and the identity system to catch missing items. She adds a short note to the shared course wiki for other students.

### Worked example

Sofia lists Elmfield's systems, builds an inventory with owners, finds an unowned portal and missing tablets and plans quarterly checks.

> **Synthetic case.** Elmfield's systems are synthetic; ISO/IEC 27002:2022 and CSF 2.0 are real.

### Errors and limits

Inventories miss shadow IT. Owners may be nominal.

### Exercises

- **EX004 — Inventory fields.** Which fields does Sofia's inventory hold? *Rubric:* 3 = name, type, owner, location, data held, supplier;; 2 = six fields;; 1 = none;; 0 = none.
- **EX005 — Inventory gaps.** What two gaps did the inventory reveal? *Rubric:* 3 = unowned board portal and eleven missing tablets;; 2 = two gaps;; 1 = none;; 0 = none.
- **EX006 — Decay check.** How does Sofia plan to keep the inventory current? *Rubric:* 3 = quarterly check against purchases and identity records;; 2 = quarterly;; 1 = none;; 0 = none.

### Synthesis

An owned, current inventory is the map on which all governance depends.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) read governance data with simple programs; (2) count and filter records; (3) write output that people can act on.

### 3.1 First script

Sofia writes her first Python program to read Elmfield's inventory from a CSV file. It prints how many assets exist and how many lack an owner. She learns basic structures: lists to hold records, loops to visit each one and conditions to test fields. Her lecturer stresses that even a simple count helps governance, because it replaces impressions with facts. The script also runs the same way every time, unlike manual counting, which may give different answers on different days. This makes the governance consequence visible to people outside the engineering team.

### 3.2 Filtering

Next Sofia filters the inventory to list assets that hold tenant personal data and lack an owner. Two appear: the board portal, which stores board papers containing tenant complaints, and a shared drive folder. She prints each with its location so someone can follow up. She learns that filtering by the combination of sensitivity and missing ownership points managers to the most urgent gaps first, rather than overwhelming them with a long undifferentiated list of problems. Sofia keeps a dated copy of her working so that the result can be traced.

### 3.3 Actionable output

Dr. Haddad reviews her output. A line saying two problems found is not useful; a line naming the asset, the problem and a suggested owner is. Sofia rewrites the output to include these fields and the date of the run. She learns to think of program output as a message to a busy manager. If the message needs explanation, it should be rewritten. This habit will matter throughout the course when scripts produce governance evidence. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### Worked example

Sofia counts inventory records, filters sensitive unowned assets and rewrites output to name asset, problem and suggested owner.

> **Synthetic case.** The inventory file is synthetic.

### Errors and limits

Scripts trust their input. Suggested owners need confirmation.

### Exercises

- **EX007 — Script benefit.** Why does a script count help governance? *Rubric:* 3 = it replaces impressions with repeatable facts;; 2 = facts;; 1 = none;; 0 = none.
- **EX008 — Filter combination.** Which combination did Sofia filter for? *Rubric:* 3 = tenant personal data and no owner;; 2 = sensitive unowned;; 1 = none;; 0 = none.
- **EX009 — Output rewrite.** What did each output line include after rewriting? *Rubric:* 3 = asset, problem, suggested owner and run date;; 2 = fields;; 1 = none;; 0 = none.

### Synthesis

Simple programs that count, filter and explain turn governance data into action.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write a short argument with evidence; (2) cite standards and sources correctly; (3) paraphrase rather than copy.

### 4.1 Argument structure

Sofia's first essay asks whether small organisations need formal security governance. She learns to structure an argument: a clear claim, reasons, evidence for each reason, a counterargument and a response. Her claim is that even small organisations need basic governance because they hold sensitive data and face the same threats as larger ones. Her counterargument is that formal frameworks cost too much for small teams. Her response proposes proportionate governance scaled to size and risk. She checks the idea against a second example before relying on it.

### 4.2 Citing sources

Sofia cites NIST CSF 2.0 and its small business resources, ISO/IEC 27001:2022 and a paper by Spears and Barki (2010) on user participation in security risk management. Dr. Haddad teaches her to cite standards with their edition and year, because requirements change between editions, and to give a DOI or official link where one exists. He warns never to invent references or identifiers and to check each one against the publisher's record before submission. The point seems small, but it changes how owners act on the result.

### 4.3 Paraphrase

Standards are copyrighted, and copying long passages is not allowed. Sofia learns to paraphrase in her own words and cite the source, quoting only short phrases where exact wording matters. She practises by summarising the idea of a risk treatment plan without copying any sentence. Paraphrasing also tests understanding: if she cannot explain an idea simply, she has not yet understood it. Her essay earns good marks for clear structure and accurate, honest citation. Elmfield's security manager later asks for a copy of this analysis.

### Worked example

Sofia structures an essay with claim, reasons, counterargument and response, cites sources by edition and paraphrases standards.

> **Synthetic case.** The essay is synthetic; CSF 2.0, ISO/IEC 27001:2022 and Spears and Barki (2010) are real.

### Errors and limits

Short essays oversimplify. Paraphrases can distort meaning.

### Exercises

- **EX010 — Counterargument.** What counterargument did Sofia address? *Rubric:* 3 = formal frameworks cost too much for small teams;; 2 = cost;; 1 = none;; 0 = none.
- **EX011 — Edition reason.** Why cite standards with edition and year? *Rubric:* 3 = requirements change between editions;; 2 = editions;; 1 = none;; 0 = none.
- **EX012 — Paraphrase test.** Why does paraphrasing test understanding? *Rubric:* 3 = if you cannot explain simply you have not understood;; 2 = understanding;; 1 = none;; 0 = none.

### Synthesis

Clear arguments, edition-specific citations and honest paraphrase are core academic skills for GRC.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain basic threats to a small organisation; (2) relate them to everyday controls; (3) communicate security without fear.

### 5.1 Common threats

Sofia learns the threats Elmfield faces most: emails that trick staff into giving passwords or paying fake invoices, ransomware that encrypts files, lost devices, mistakes such as sending tenant data to the wrong person and misuse of access by contractors. She notes that most incidents in small organisations come from ordinary failures, not sophisticated attacks. Understanding which threats are common helps Elmfield focus limited resources where they will prevent the most harm. She marks the open questions in red so that they are not forgotten.

### 5.2 Everyday controls

For each threat she lists everyday controls. Multi-factor authentication limits damage from stolen passwords. Backups kept offline allow recovery from ransomware. Encryption protects lost laptops. Checking recipient addresses and using secure sharing links reduce misdirected emails. Named contractor accounts with limited access reduce misuse. She learns that the NIST CSF 2.0 small business quick-start guidance stresses similar basics. Controls do not need to be complex to be effective, but they must be applied consistently. Writing the reasoning down also helps her spot a weak step in her argument.

### 5.3 Communicating well

Sofia prepares a short talk for Elmfield's housing officers. She avoids frightening language and blame. Instead she explains why each control helps tenants and staff, gives simple instructions and invites questions. She learns that fear may cause short bursts of caution but often leads to hiding mistakes. Encouraging staff to report errors quickly, such as a misdirected email, lets Elmfield limit harm. Good communication is itself a control, because it shapes how people behave when something goes wrong. Sofia discusses the trade-off with a classmate who works in finance.

### Worked example

Sofia identifies Elmfield's common threats, maps them to everyday controls and gives a blame-free talk encouraging quick reporting.

> **Synthetic case.** Threats and talk are synthetic; CSF 2.0 guidance is real.

### Errors and limits

Simple controls fail if inconsistent. Talks have short-lived effects.

### Exercises

- **EX013 — Common cause.** Where do most incidents in small organisations come from? *Rubric:* 3 = ordinary failures, not sophisticated attacks;; 2 = ordinary;; 1 = none;; 0 = none.
- **EX014 — Ransomware control.** Which control enables recovery from ransomware? *Rubric:* 3 = offline backups;; 2 = backups;; 1 = none;; 0 = none.
- **EX015 — Fear effect.** Why avoid fear in security talks? *Rubric:* 3 = it leads to hiding mistakes;; 2 = hiding;; 1 = none;; 0 = none.

### Synthesis

Security literacy links common threats to everyday controls and blame-free communication.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) represent roles and permissions as sets and relations; (2) find segregation of duties conflicts; (3) use graphs to trace dependencies.

### 6.1 Roles as sets

Sofia represents Elmfield's finance roles as sets of permissions. The payments clerk can enter supplier invoices and record payments. The finance manager can approve payments and add new suppliers. She lists which staff hold which roles and computes each person's combined permissions. One person covering for a colleague holds both roles, giving permission to add a supplier and approve payment to it. Sets make this conflict visible immediately rather than relying on someone noticing. The class compares answers and finds that most differences come from unstated assumptions.

### 6.2 Segregation of duties

Segregation of duties prevents one person from completing a sensitive process alone. Sofia writes rules as forbidden pairs of permissions, such as add supplier with approve payment. She checks each person's permission set against the rules and finds the one conflict. She recommends that cover arrangements use temporary access with a second approver and an end date. She learns that this simple logic underlies many fraud controls and that it can be checked automatically each month. Sofia records this point in her course notebook so that later chapters can build on it.

### 6.3 Dependency graphs

Sofia draws a graph where nodes are systems and edges show dependencies. The housing management system depends on cloud identity, which depends on email. If cloud identity fails, staff cannot reach housing records. The graph shows that identity is a single point of failure for most services. She learns that graphs reveal hidden concentrations of risk that inventories alone do not show, and that resilience planning should focus on nodes with many dependents. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### Worked example

Sofia finds a segregation of duties conflict through set operations and identifies cloud identity as a single point of failure with a graph.

> **Synthetic case.** Roles, staff and systems are synthetic.

### Errors and limits

Permission data may be incomplete. Graphs miss informal dependencies.

### Exercises

- **EX016 — Conflict found.** What conflict did Sofia find? *Rubric:* 3 = one person could add a supplier and approve payment;; 2 = SoD;; 1 = none;; 0 = none.
- **EX017 — Cover fix.** How should cover arrangements work? *Rubric:* 3 = temporary access with second approver and end date;; 2 = temporary;; 1 = none;; 0 = none.
- **EX018 — Single point.** Which system is a single point of failure? *Rubric:* 3 = cloud identity;; 2 = identity;; 1 = email;; 0 = none.

### Synthesis

Sets, relations and graphs make access conflicts and dependency risks visible.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) describe Elmfield's network and its external connections; (2) identify where data leave the organisation; (3) relate network design to risk.

### 7.1 The network

Elmfield's office network connects laptops and the file server, with internet access through a firewall. Most services now run in the cloud, reached over the internet. Repairs tablets connect through mobile networks. Sofia learns that the old idea of a trusted internal network no longer fits, because staff and data are spread across many places. Governance must therefore focus on identity, devices and data protection wherever they are, not only on the office firewall. She notes the assumption behind it so that a reviewer can challenge it later.

### 7.2 Data leaving

Sofia traces where tenant data leave Elmfield: email to contractors, the housing system supplier's servers, the payment provider and the payroll bureau. Each flow needs a reason, a contract and protection in transit. She finds that repairs contractors receive full tenant records when they need only a name, address and phone number. She recommends sending only the necessary fields, applying the principle of data minimisation, which reduces harm if a contractor's systems are compromised. The same reasoning will return when Elmfield's auditors visit next year.

### 7.3 Network risk

Sofia lists network risks: an exposed remote desktop service on the file server, a guest Wi-Fi network sharing the office network and no logging at the firewall. She ranks them by potential harm and ease of fixing. Closing the remote desktop exposure ranks first because attackers routinely scan for it. She learns that small fixes can remove large risks and that a network review is a quick way for a small organisation to find serious problems. She adds a short note to the shared course wiki for other students.

### Worked example

Sofia maps Elmfield's network and data flows, applies minimisation to contractor data and ranks three network risks.

> **Synthetic case.** Elmfield's network is synthetic.

### Errors and limits

Data flows change. Rankings depend on judgement.

### Exercises

- **EX019 — Trusted network.** Why does the trusted internal network idea no longer fit? *Rubric:* 3 = staff and data are spread across many places;; 2 = cloud and mobile;; 1 = none;; 0 = none.
- **EX020 — Minimisation fix.** What should contractors receive instead of full records? *Rubric:* 3 = name, address and phone only;; 2 = minimum fields;; 1 = full records;; 0 = none.
- **EX021 — Top network risk.** Which network risk ranked first? *Rubric:* 3 = exposed remote desktop on the file server;; 2 = RDP;; 1 = none;; 0 = none.

### Synthesis

Network and data-flow maps show where protection and minimisation matter most.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure governance scripts into functions with tests; (2) read several data sources; (3) cross-check sources to find discrepancies.

### 8.1 Functions and tests

Sofia restructures her scripts into functions, each doing one job: reading a file, checking a rule or printing a report. She writes small tests with known answers. For example, a test gives the owner check a record with an empty owner and expects it to be flagged. Tests catch mistakes when she changes code later. She learns that governance scripts need tests because their output may be used as evidence, and wrong evidence can mislead managers and auditors. This makes the governance consequence visible to people outside the engineering team.

### 8.2 Several sources

Real checks combine sources. Sofia reads the inventory, the identity system's account export and the human resources leaver list. Each uses different names for the same thing; the identity system uses email addresses, while human resources uses staff numbers. She writes a mapping table to join them. She learns that much governance work is reconciling sources that were never designed to match, and that documenting the mapping is essential so others can repeat the check. Sofia keeps a dated copy of her working so that the result can be traced.

### 8.3 Discrepancies

Cross-checking reveals discrepancies: four accounts belong to staff on the leaver list, two laptops in the inventory are assigned to leavers and one active account matches no staff member. Sofia prints each discrepancy with both sources' details. Dr. Haddad notes that discrepancies are where risk hides, because each system looks fine on its own. Reconciliation turns separate records into a single picture, which is the basis for access reviews and asset audits. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### Worked example

Sofia writes tested functions, joins three sources with a mapping table and finds leaver accounts, leaver laptops and an orphan account.

> **Synthetic case.** Sources and discrepancies are synthetic.

### Errors and limits

Mapping errors cause false alarms. Sources may share the same mistake.

### Exercises

- **EX022 — Test purpose.** Why do governance scripts need tests? *Rubric:* 3 = their output may be used as evidence;; 2 = evidence;; 1 = none;; 0 = none.
- **EX023 — Join problem.** Why did Sofia need a mapping table? *Rubric:* 3 = sources use different identifiers;; 2 = identifiers;; 1 = none;; 0 = none.
- **EX024 — Orphan account.** What is an orphan account in this check? *Rubric:* 3 = an active account matching no staff member;; 2 = orphan;; 1 = none;; 0 = none.

### Synthesis

Tested scripts that reconcile several sources reveal risks hidden between systems.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) store a risk register in a database; (2) query it for priorities and gaps; (3) understand why structure improves governance data.

### 9.1 Register in a database

Elmfield's risk register is a spreadsheet with merged cells and free text. Sofia moves a sample of six risks into a small SQLite database with defined columns: identifier, title, owner, likelihood from one to five and impact from one to five. Defined columns let her run queries that would be slow and error-prone by hand. She learns that structure is what turns a register from a document into data that can answer questions. She checks the idea against a second example before relying on it.

### 9.2 Queries

The lab runs two queries. The first ranks risks by score, likelihood times impact. Tenant data emailed to the wrong person and a lost laptop with case notes tie at twelve, followed by ransomware on the file server at ten. The second lists risks without an owner: the repairs contractor account misuse risk and the weak board portal passwords risk. Sofia notes that ties show the limits of a five-point scale, which cannot separate risks that may differ greatly in real consequences. The point seems small, but it changes how owners act on the result.

### Lab — Querying a synthetic risk register

```python
"""A synthetic Elmfield risk register in SQLite: top risks and unowned entries."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("create table risk(id text, title text, owner text, likelihood int, impact int)")
db.executemany("insert into risk values (?,?,?,?,?)", [
    ("R1", "tenant data emailed to wrong person", "Housing", 4, 3), ("R2", "ransomware on file server", "IT", 2, 5),
    ("R3", "repairs contractor account misuse", None, 3, 3), ("R4", "rent payment page outage", "Finance", 3, 2),
    ("R5", "lost laptop with case notes", "Housing", 3, 4), ("R6", "weak passwords on board portal", None, 2, 2)])
for row in db.execute("select id, title, likelihood*impact s from risk order by s desc limit 3"):
    print("top", *row)
print("unowned:", [r[0] for r in db.execute("select id from risk where owner is null")])
```

Run with `python3 lab_sqlite.py`. Verified output:

```text
top R1 tenant data emailed to wrong person 12
top R5 lost laptop with case notes 12
top R2 ransomware on file server 10
unowned: ['R3', 'R6']
```

### 9.3 Why structure helps

With structured data, Elmfield can track how scores change over time, check that every risk has an owner and produce board reports automatically. Sofia also adds a constraint so that likelihood and impact must be between one and five, preventing typing errors. Dr. Haddad notes that databases do not make risk judgements better by themselves, but they make the judgements visible, consistent and easy to review, which improves governance by exposing gaps. Elmfield's security manager later asks for a copy of this analysis. She marks the open questions in red so that they are not forgotten.

### Worked example

Sofia loads six risks into SQLite, finds two tied at twelve and two unowned risks and adds range constraints.

> **Synthetic case.** The register is synthetic.

### Errors and limits

Structured data can still hold poor judgements. Scales cause ties.

### Exercises

- **EX025 — Score formula.** How is the risk score computed? *Rubric:* 3 = likelihood times impact;; 2 = product;; 1 = sum;; 0 = none.
- **EX026 — Tied risks.** Which two risks tied at the top? *Rubric:* 3 = misdirected tenant data and lost laptop, both 12;; 2 = tie;; 1 = ransomware;; 0 = none.
- **EX027 — Unowned list.** Which risks had no owner? *Rubric:* 3 = R3 contractor misuse and R6 board portal passwords;; 2 = two;; 1 = none;; 0 = none.

### Synthesis

Storing a register as structured data makes priorities and gaps easy to see.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) work only within authorised scope; (2) handle personal data ethically during governance work; (3) report findings responsibly.

### 10.1 Authorisation

Sofia's work at Elmfield needs written authorisation. Dr. Haddad explains that even well-meant checks, such as testing whether a password is weak, can break rules or laws if done without permission. Elmfield's director signs a letter defining what Sofia may do: read inventory and account exports, interview staff and review documents. Active testing of systems is excluded. She learns that a clear scope protects her, the organisation and the people whose data she may see. Writing the reasoning down also helps her spot a weak step in her argument.

### 10.2 Personal data

Account exports and leaver lists contain personal data. Sofia stores them only on Elmfield's encrypted laptop provided for her placement, removes names when sharing results with her tutor and deletes copies at the end. She learns that governance work must follow the same data protection principles it promotes: use the minimum data needed, keep it secure and keep it only as long as necessary. Doing otherwise would undermine her credibility and could harm tenants and staff. Sofia discusses the trade-off with a classmate who works in finance.

### 10.3 Responsible reporting

When Sofia finds the exposed remote desktop service, she reports it immediately to Elmfield's IT lead rather than waiting for her final report, because attackers could exploit it at any time. She describes it factually, without blaming the person who set it up. She learns that urgent findings need fast, private reporting through agreed channels, while lower risks can wait for the written report. Responsible reporting balances speed, accuracy and respect for colleagues. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Sofia works under a signed scope, protects personal data in her own work and reports an urgent finding promptly and without blame.

> **Synthetic case.** The scope letter and findings are synthetic.

### Errors and limits

Scopes can be ambiguous. Urgency judgements vary.

### Exercises

- **EX028 — Excluded activity.** Which activity was excluded from Sofia's scope? *Rubric:* 3 = active testing of systems;; 2 = testing;; 1 = none;; 0 = none.
- **EX029 — Data handling.** How did Sofia handle personal data from exports? *Rubric:* 3 = encrypted laptop, names removed when sharing, deleted at end;; 2 = minimise;; 1 = none;; 0 = none.
- **EX030 — Urgent report.** Why report the remote desktop exposure immediately? *Rubric:* 3 = attackers could exploit it at any time;; 2 = urgency;; 1 = none;; 0 = none.

### Synthesis

Authorised scope, careful data handling and responsible reporting are the ethics of GRC work.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) relate operating system settings to policy; (2) check laptops against a simple baseline; (3) plan updates as a governed process.

### 11.1 Settings and policy

Elmfield's policy says laptops must be encrypted, lock after a few minutes idle, receive updates automatically and give staff no administrator rights. Sofia learns that each statement corresponds to operating system settings. Encryption is a disk setting, screen lock is a power and security setting, updates are managed by the update service and administrator rights depend on group membership. Linking policy statements to settings is what makes a policy enforceable and checkable rather than a wish. Sofia records this point in her course notebook so that later chapters can build on it.

### 11.2 Baseline check

Sofia uses the device management console to export settings for one hundred and twenty laptops and compares them with the policy baseline. Most comply, but nine lack encryption, all repairs team laptops bought locally, and fourteen users still have administrator rights granted for old software. She lists each with its owner. She learns that baseline checks reveal not only technical gaps but process gaps, such as devices bought outside the normal route, which explain why the technical gaps arose. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### 11.3 Updates as a process

Updates fix vulnerabilities but can break software. Elmfield needs a governed process: test updates on a few devices, deploy to everyone within a set time and track exceptions. Sofia drafts the process with the IT lead, setting thirty days for critical updates. She learns that update policy is a balance between speed and stability, and that writing down the target and measuring against it lets Elmfield see whether its practice matches its intention. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Sofia links policy to settings, finds nine unencrypted laptops and fourteen administrators and drafts an update process.

> **Synthetic case.** Laptop counts are synthetic.

### Errors and limits

Console exports miss unmanaged devices. Update targets need exceptions.

### Exercises

- **EX031 — Policy to setting.** Which setting enforces the no-admin rule? *Rubric:* 3 = group membership;; 2 = groups;; 1 = none;; 0 = none.
- **EX032 — Root cause.** Why did nine laptops lack encryption? *Rubric:* 3 = bought locally outside the normal route;; 2 = procurement;; 1 = none;; 0 = none.
- **EX033 — Update target.** What target did Sofia set for critical updates? *Rubric:* 3 = thirty days;; 2 = 30;; 1 = none;; 0 = none.

### Synthesis

Policies become enforceable when linked to operating system settings and measured processes.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) estimate a proportion with an interval; (2) compare teams fairly despite different sizes; (3) avoid over-reading small samples.

### 12.1 Proportions with intervals

Elmfield asks each team to acknowledge its updated information handling policy. Sofia learns that a proportion from a sample or small team should come with an interval showing uncertainty. She uses the Wilson interval, which behaves well for small counts and proportions near zero or one. The interval tells managers the range of values consistent with the data, which is more honest than a single percentage and helps prevent decisions based on chance differences. The same reasoning will return when Elmfield's auditors visit next year.

### 12.2 Comparing teams

The lab computes acknowledgement rates. Housing has fifty-two of sixty, eighty-seven percent, with an interval from seventy-six to ninety-three percent. Repairs has eighteen of thirty, sixty percent, with an interval from forty-two to seventy-five percent. Finance has fourteen of fifteen, ninety-three percent, but its interval runs from seventy to ninety-nine percent because the team is small. Repairs is clearly lower than housing, since their intervals barely touch. Finance and housing cannot be distinguished. She adds a short note to the shared course wiki for other students.

### Lab — Wilson intervals for policy acknowledgement

```python
"""Wilson 95% interval for a proportion (policy acknowledgement), stdlib only."""
from math import sqrt
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n; c = (p + z*z/(2*n))/d; h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h
for team, k, n in [("housing", 52, 60), ("repairs", 18, 30), ("finance", 14, 15)]:
    lo, hi = wilson(k, n); print(f"{team}: {k}/{n} = {k/n:.0%}, 95% interval {lo:.0%} to {hi:.0%}")
```

Run with `python3 lab_wilson.py`. Verified output:

```text
housing: 52/60 = 87%, 95% interval 76% to 93%
repairs: 18/30 = 60%, 95% interval 42% to 75%
finance: 14/15 = 93%, 95% interval 70% to 99%
```

### 12.3 Small samples

Sofia notes that finance's high percentage looks impressive but rests on fifteen people; one more or one fewer acknowledgement would move it several points. She recommends that Elmfield focus support on repairs, where the gap is clear, and asks why repairs staff find acknowledgement harder. She discovers that they rarely use laptops and the policy was sent by email. Statistics revealed the gap; talking to staff revealed the cause and a simple fix: acknowledgement on tablets during team meetings. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Sofia computes Wilson intervals, finds repairs clearly lower than housing and traces the cause to email delivery.

> **Synthetic case.** Acknowledgement counts are synthetic.

### Errors and limits

Acknowledgement does not mean understanding. Intervals assume independence.

### Exercises

- **EX034 — Wilson reason.** Why use the Wilson interval? *Rubric:* 3 = behaves well for small counts and extreme proportions;; 2 = small samples;; 1 = none;; 0 = none.
- **EX035 — Repairs interval.** What is the repairs team's interval? *Rubric:* 3 = 42% to 75%;; 2 = wide;; 1 = none;; 0 = none.
- **EX036 — Repairs cause.** Why did repairs staff acknowledge less? *Rubric:* 3 = they rarely use laptops and the policy came by email;; 2 = channel;; 1 = none;; 0 = none.

### Synthesis

Intervals show which differences are real and point to where conversations reveal causes.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) manage identities through joiners, movers and leavers; (2) apply least privilege; (3) run a simple access review.

### 13.1 Life cycle

Sofia maps Elmfield's identity life cycle. Human resources tells IT when someone joins, and accounts are created. When staff move teams, they ask for new access but rarely lose old access. When staff leave, accounts should be disabled on their last day, but the leaver list reaches IT late. She finds four active accounts belonging to leavers. She proposes that HR send leaver notices automatically before the last day and that IT confirm each disablement in a ticket. Sofia keeps a dated copy of her working so that the result can be traced.

### 13.2 Least privilege

Least privilege means each person has only the access their role needs. Sofia reviews the housing management system and finds that all housing officers can see every tenant's full record, including support needs and safeguarding notes. Only the specialist support team needs those notes. She recommends role-based access that restricts sensitive fields. ISO/IEC 27002:2022 includes guidance on access control and access rights that supports this, and Elmfield's tenants have a strong interest in it. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 13.3 Access review

Sofia runs Elmfield's first access review for the finance system. She sends each manager a list of their staff's access and asks them to confirm or remove each item. Most respond within a week; two need reminders. Seven access rights are removed. She records the date, reviewer and changes as evidence. She learns that reviews work best when lists are short, clear and sent to people who actually know what their staff do. She checks the idea against a second example before relying on it.

### Worked example

Sofia fixes the leaver process, restricts sensitive tenant notes by role and runs a finance access review removing seven rights.

> **Synthetic case.** Accounts and reviews are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Managers may approve without checking. Role design takes time.

### Exercises

- **EX037 — Leaver fix.** How did Sofia fix late leaver notices? *Rubric:* 3 = automatic HR notices before last day with ticket confirmation;; 2 = automation;; 1 = none;; 0 = none.
- **EX038 — Sensitive fields.** Who should see safeguarding notes? *Rubric:* 3 = only the specialist support team;; 2 = support team;; 1 = all officers;; 0 = none.
- **EX039 — Review outcome.** How many access rights did the review remove? *Rubric:* 3 = seven;; 2 = 7;; 1 = none;; 0 = none.

### Synthesis

Identity governance manages life-cycle transitions, least privilege and periodic review.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) apply data protection principles to tenant data; (2) map personal data processing; (3) link privacy and security governance.

### 14.1 Principles

Sofia studies data protection principles common to modern privacy laws: lawful and fair processing, purpose limitation, data minimisation, accuracy, storage limitation, security and accountability. She applies them to Elmfield. Tenant data are collected to manage tenancies and repairs, so using them for unrelated marketing would breach purpose limitation. Old records of former tenants kept for decades breach storage limitation. She notes that these principles overlap with security but also cover fairness and individuals' rights. The point seems small, but it changes how owners act on the result.

### 14.2 Processing map

Sofia builds a record of processing activities: what personal data Elmfield holds, why, where they come from, who receives them and how long they are kept. She finds that repairs contractors receive too much data, that support needs are stored in two systems and that nobody knows how long call recordings are kept. The NIST Privacy Framework offers a structure for managing privacy risk that she uses to organise her findings alongside security ones. Elmfield's security manager later asks for a copy of this analysis.

### 14.3 Joining privacy and security

Sofia recommends that Elmfield run privacy and security governance together, with one risk register and shared owners. A misdirected email is both a security incident and a personal data breach that may need reporting. Retention rules reduce the data an attacker could steal. She learns that privacy and security are distinct but strongly linked, and that separate programmes often duplicate effort and miss risks that sit between them, such as excessive data sharing with suppliers. She marks the open questions in red so that they are not forgotten.

### Worked example

Sofia applies privacy principles, maps processing with three gaps and recommends joint privacy and security governance.

> **Synthetic case.** Elmfield's processing is synthetic; the NIST Privacy Framework is real.

### Errors and limits

Laws differ by country. Mappings go out of date.

### Exercises

- **EX040 — Purpose breach.** Which use of tenant data would breach purpose limitation? *Rubric:* 3 = unrelated marketing;; 2 = marketing;; 1 = repairs;; 0 = none.
- **EX041 — Processing gaps.** Name two gaps found in the processing map. *Rubric:* 3 = excess contractor data and unknown call recording retention;; 2 = gaps;; 1 = none;; 0 = none.
- **EX042 — Joint example.** Why is a misdirected email both a security and privacy matter? *Rubric:* 3 = it is a security incident and a personal data breach;; 2 = both;; 1 = none;; 0 = none.

### Synthesis

Privacy principles and security governance work best as one programme with shared owners.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) choose measures that reflect control performance; (2) use medians and thresholds for skewed data; (3) present measures honestly.

### 15.1 Choosing measures

Elmfield wants to know whether its update process works. Sofia chooses two measures: the median number of days to apply critical updates and the share applied within the thirty-day target. She learns that measures should relate to the control's purpose, which is to shorten the time vulnerabilities remain open. Counting updates installed would be an activity measure; time to install is a performance measure closer to what matters for risk. Writing the reasoning down also helps her spot a weak step in her argument.

### 15.2 Skewed data

The lab examines fifteen critical updates. The median is twenty-one days and ten of fifteen, sixty-seven percent, were applied within thirty days. The three slowest took forty-eight, sixty-two and ninety days. Sofia notes that the mean would be pulled up by these long delays, so the median better describes a typical update while the slowest cases deserve separate attention. Most slow updates affected the file server, which staff avoid restarting during working hours. Sofia discusses the trade-off with a classmate who works in finance.

### Lab — Days to patch: median and share within target

```python
"""Days to patch for 15 synthetic critical updates: median and share within 30 days."""
from statistics import median
days = [3, 5, 7, 8, 12, 14, 15, 21, 25, 29, 33, 41, 48, 62, 90]
print(f"updates {len(days)}; median {median(days)} days")
w = sum(d <= 30 for d in days); print(f"within 30 days {w}/{len(days)} = {w/len(days):.0%}")
print(f"slowest three {days[-3:]}")
```

Run with `python3 lab_patch.py`. Verified output:

```text
updates 15; median 21 days
within 30 days 10/15 = 67%
slowest three [48, 62, 90]
```

### 15.3 Honest presentation

Sofia presents both measures with the list of slow updates and their cause. She avoids saying that most updates are on time without adding that a third are not. She recommends a monthly maintenance window for the file server. Dr. Haddad notes that NIST SP 800-55v1 discusses selecting and using measures for information security, and that good measures prompt decisions rather than decorate reports. Sofia's measure leads directly to the maintenance window decision. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Sofia measures a median of twenty-one days with sixty-seven percent on target and traces slow updates to the file server.

> **Synthetic case.** Update data are synthetic; NIST SP 800-55v1 is real.

### Errors and limits

Small samples vary. Medians hide the slowest cases.

### Exercises

- **EX043 — Performance measure.** Why is time to install a better measure than updates installed? *Rubric:* 3 = it relates to how long vulnerabilities stay open;; 2 = performance;; 1 = activity;; 0 = none.
- **EX044 — Patch results.** What median and on-target share did the lab report? *Rubric:* 3 = 21 days, 67%;; 2 = median 21;; 1 = none;; 0 = none.
- **EX045 — Slow cause.** Why were the slowest updates late? *Rubric:* 3 = the file server was not restarted during working hours;; 2 = server;; 1 = none;; 0 = none.

### Synthesis

Good measures reflect purpose, handle skew and lead to decisions.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe a simple security architecture for a small organisation; (2) apply layered defence; (3) document design choices.

### 16.1 A simple architecture

Sofia sketches Elmfield's target architecture. Identity is central: all staff sign in once with multi-factor authentication to reach cloud email, the housing system and files. Devices are managed and encrypted. Sensitive data live in a few well-controlled places. Backups are kept separately and tested. The office network is no longer trusted by default. She learns that small organisations can achieve strong security through a few well-chosen design decisions rather than many complex tools. Sofia records this point in her course notebook so that later chapters can build on it.

### 16.2 Layers

Sofia applies layered defence to ransomware. Email filtering blocks many malicious messages. Multi-factor authentication limits stolen passwords. Device controls block unknown programs. Limited administrator rights reduce spread. Offline backups allow recovery. No single layer is perfect, but together they reduce the chance that one failure causes disaster. She notes that layers sharing a weakness, such as one administrator account controlling all of them, would weaken this protection considerably. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on. She notes the assumption behind it so that a reviewer can challenge it later.

### 16.3 Documenting choices

Sofia writes short decision notes for each major choice: why cloud identity was chosen, why the file server will move to a cloud service and why backups remain offline. Each note records the alternatives and accepted risks. She learns that documented decisions help future staff understand the architecture and help auditors see that risk was considered. Elmfield's director appreciates the notes because they explain technical decisions in language the board can follow. The same reasoning will return when Elmfield's auditors visit next year. She adds a short note to the shared course wiki for other students.

### Worked example

Sofia sketches an identity-centred architecture, layers ransomware defences and documents major decisions.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Layers can share weaknesses. Cloud moves bring supplier risk.

### Exercises

- **EX046 — Central element.** What is central to Elmfield's target architecture? *Rubric:* 3 = identity with multi-factor authentication;; 2 = identity;; 1 = network;; 0 = none.
- **EX047 — Shared weakness.** What could weaken layered defence? *Rubric:* 3 = one administrator account controlling all layers;; 2 = shared admin;; 1 = none;; 0 = none.
- **EX048 — Decision notes.** What do Sofia's decision notes record? *Rubric:* 3 = alternatives and accepted risks;; 2 = alternatives;; 1 = none;; 0 = none.

### Synthesis

Small organisations gain strong security from a few well-documented architecture decisions.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain what encryption and hashing protect; (2) relate them to policy decisions; (3) manage keys and certificates as governed items.

### 17.1 What cryptography protects

Sofia learns that encryption keeps data confidential from those without the key, while hashing produces a fingerprint that changes if data change, supporting integrity checks. Digital signatures combine both ideas to show who created something and that it was not altered. At Elmfield, laptop encryption protects lost devices, secure connections protect data in transit and hashes can show that evidence files were not changed after collection. This makes the governance consequence visible to people outside the engineering team. Sofia keeps a dated copy of her working so that the result can be traced.

### 17.2 Policy decisions

Cryptography requires policy decisions: which data must be encrypted, where and with what approved methods. Sofia drafts a short cryptography standard for Elmfield referencing its data classification: tenant personal data encrypted at rest on devices and in transit; board papers encrypted when shared outside the portal. She learns that ISO/IEC 27002:2022 expects rules on the use of cryptography and on key management, and that simple, clear rules work better than long technical documents nobody reads. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 17.3 Keys and certificates

Sofia lists Elmfield's certificates and recovery keys. The website certificate renews automatically, but laptop recovery keys are stored only in the device console, which one person administers. If that person left, recovery could fail. She recommends a second administrator and a documented recovery procedure. She learns that most cryptographic failures in small organisations are management failures, such as expired certificates or lost keys, not broken algorithms. She checks the idea against a second example before relying on it. The point seems small, but it changes how owners act on the result.

### Worked example

Sofia explains encryption and hashing, drafts a short cryptography standard and fixes a single-administrator key risk.

> **Synthetic case.** Elmfield's keys are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Encryption does not stop authorised misuse. Key procedures need testing.

### Exercises

- **EX049 — Hash role.** What does hashing support? *Rubric:* 3 = integrity checks;; 2 = integrity;; 1 = confidentiality;; 0 = none.
- **EX050 — Board papers rule.** When must board papers be encrypted under the draft standard? *Rubric:* 3 = when shared outside the portal;; 2 = outside portal;; 1 = never;; 0 = none.
- **EX051 — Key risk.** What was the risk with laptop recovery keys? *Rubric:* 3 = one administrator controlled the only store;; 2 = single admin;; 1 = none;; 0 = none.

### Synthesis

Cryptography protects data only when policy and key management are governed well.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) form a researchable question about governance; (2) choose interviews or surveys appropriately; (3) plan ethical data collection.

### 18.1 A research question

Sofia's first research project asks why some Elmfield teams complete security tasks on time and others do not. She narrows it to the quarterly access review: what helps or hinders managers in completing it? She learns that good questions are specific, answerable with available data and useful to someone. Asking whether security culture is good would be too vague; asking what helps managers complete a defined task can lead to practical improvements. Elmfield's security manager later asks for a copy of this analysis. She marks the open questions in red so that they are not forgotten.

### 18.2 Choosing methods

With only twelve managers, a survey would give little statistical power. Sofia chooses semi-structured interviews, which let managers explain their reasons in their own words. She writes an interview guide with open questions and prompts, pilots it with one manager and revises two confusing questions. She learns that interviews suit small groups and why questions, while surveys suit large groups and how-many questions, and that the choice should follow the question rather than habit. Writing the reasoning down also helps her spot a weak step in her argument.

### 18.3 Ethics

Sofia submits a short ethics application to Brightwater College. Participation is voluntary, interviews are recorded only with consent, transcripts remove names and Elmfield's director will see only themes, not who said what. She learns that even low-risk research about workplaces needs care, because managers might fear criticism. Protecting their identity encourages honest answers. Her ethics approval arrives within two weeks, and she begins interviews with clear information sheets for each participant. Sofia discusses the trade-off with a classmate who works in finance. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Sofia frames a specific question about access review completion, chooses interviews for twelve managers and secures ethics approval.

> **Synthetic case.** The study is synthetic.

### Errors and limits

Interviews reflect what people say, not always what they do. Small groups limit generality.

### Exercises

- **EX052 — Narrowed question.** What did Sofia's question narrow to? *Rubric:* 3 = what helps or hinders managers completing the access review;; 2 = specific;; 1 = culture;; 0 = none.
- **EX053 — Method choice.** Why interviews rather than a survey? *Rubric:* 3 = only twelve managers and a why question;; 2 = small group;; 1 = none;; 0 = none.
- **EX054 — Director access.** What will Elmfield's director see? *Rubric:* 3 = only themes, not who said what;; 2 = themes;; 1 = transcripts;; 0 = none.

### Synthesis

Specific questions, fitting methods and careful ethics make governance research useful.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Security governance, risk and compliance: scope and theory

### Learning outcomes

You will (1) define governance, risk management and compliance; (2) set the scope of a GRC programme; (3) explain key theory behind risk management.

### 19.1 Definitions

Sofia now begins the GRC courses. Governance means direction and oversight: who decides what level of risk is acceptable and how performance is checked. Risk management means identifying, analysing, evaluating and treating risks, a process ISO 31000:2018 describes in general terms for any organisation. Compliance means meeting obligations from law, contracts and adopted standards. She learns that the three support each other: governance sets direction, risk management informs decisions and compliance confirms obligations are met. Sofia records this point in her course notebook so that later chapters can build on it.

### 19.2 Scope

Elmfield must decide what its programme covers. Sofia proposes a scope including all staff, devices, cloud services and suppliers that handle tenant data, plus the board portal. Excluded items, such as tenants' own devices, are listed with reasons. ISO/IEC 27001:2022 requires a defined scope for the management system, and she learns that clear scope prevents both gaps and wasted effort. A scope that is too narrow misses risks; one too broad cannot be managed with Elmfield's resources. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### 19.3 Theory

Sofia reads about risk theory. Risk combines uncertainty about events with their consequences for objectives. Treatment options include avoiding, reducing, sharing and accepting risk. Cox (2008) shows that simple matrices can rank risks poorly, while Hubbard and Seiersen (2016) argue for quantitative estimates even with limited data. She learns that theory warns against false precision and false simplicity alike, and that small organisations should choose methods they can apply consistently and explain to their boards. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Sofia defines the three disciplines, proposes Elmfield's scope with exclusions and reviews core risk theory and treatment options.

> **Synthetic case.** Elmfield's scope is synthetic; ISO 31000:2018, ISO/IEC 27001:2022, Cox (2008) and Hubbard and Seiersen (2016) are real.

### Errors and limits

Definitions vary by source. Scope decisions need review.

### Exercises

- **EX055 — Discipline roles.** How do the three disciplines support each other? *Rubric:* 3 = governance sets direction, risk informs decisions, compliance confirms obligations;; 2 = roles;; 1 = none;; 0 = none.
- **EX056 — Excluded item.** What item was excluded from scope? *Rubric:* 3 = tenants' own devices;; 2 = tenant devices;; 1 = none;; 0 = none.
- **EX057 — Treatment options.** List the four treatment options. *Rubric:* 3 = avoid, reduce, share, accept;; 2 = four;; 1 = none;; 0 = none.

### Synthesis

Clear definitions, scope and theory form the foundation of a GRC programme.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security governance, risk and compliance: foundational cases

### Learning outcomes

You will (1) analyse published governance cases; (2) extract lessons for a small organisation; (3) distinguish root causes from symptoms.

### 20.1 Reading cases

Sofia studies governance lessons from public reports. GAO-21-105263, a 2021 testimony by the United States Government Accountability Office, describes weaknesses in the federal oversight of pipeline security after the ransomware attack on Colonial Pipeline's business systems, including risk assessments that lacked cybersecurity information and an incident protocol not updated since 2010. She reads such reports for patterns rather than blame: incomplete risk information, stale response plans and slow follow-up on recommendations recur. Public audit reports are valuable teaching material because they rest on evidence, though their settings may differ from Elmfield's.

### 20.2 Lessons for Elmfield

From the cases, Sofia draws lessons scaled for Elmfield: name one person accountable for the security programme, write a short risk appetite statement approved by the board, keep a register reviewed quarterly and report progress to the board twice a year. She avoids copying large-organisation structures that Elmfield could not sustain. She learns that good lessons are about principles, such as clear accountability, rather than specific committees or tools. This makes the governance consequence visible to people outside the engineering team. Sofia keeps a dated copy of her working so that the result can be traced.

### 20.3 Root causes

Sofia practises separating symptoms from causes. In a synthetic Elmfield incident, a contractor's account was used after the contract ended. The symptom was an active account. The root cause was that no one owned contractor offboarding, since contracts were managed by the repairs team while accounts were managed by IT. She recommends assigning ownership and linking contract end dates to account expiry. Fixing causes prevents repeats; fixing symptoms alone does not. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### Worked example

Sofia reads public audit cases for patterns, draws proportionate lessons for Elmfield and traces a contractor account incident to missing ownership.

> **Synthetic case.** The Elmfield incident is synthetic; GAO-21-105263 is real.

### Errors and limits

Cases from large organisations may not transfer. Root cause analysis can stop too early.

### Exercises

- **EX058 — GAO weaknesses.** Which two weaknesses did GAO-21-105263 describe? *Rubric:* 3 = risk assessments lacking cyber information and an outdated incident protocol;; 2 = two;; 1 = none;; 0 = none.
- **EX059 — Board reporting.** How often should progress be reported to Elmfield's board? *Rubric:* 3 = twice a year;; 2 = twice;; 1 = none;; 0 = none.
- **EX060 — Contractor root cause.** What was the root cause of the contractor account incident? *Rubric:* 3 = no one owned contractor offboarding;; 2 = ownership;; 1 = active account;; 0 = none.

### Synthesis

Cases teach principles; root causes, not symptoms, must be fixed.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security governance, risk and compliance: system models

### Learning outcomes

You will (1) model Elmfield's governance system as roles, processes and information flows; (2) identify accountability gaps; (3) use a RACI chart.

### 21.1 Roles and processes

Sofia models Elmfield's governance as a system of roles and processes. The board approves risk appetite and receives reports. The director is accountable for the programme. The IT lead runs technical controls. Team managers own risks in their areas. A part-time data protection lead handles privacy. Processes link them: risk review, policy approval, incident handling and access review. Drawing the model shows who passes information to whom and where decisions are made. Sofia records this point in her course notebook so that later chapters can build on it.

### 21.2 RACI

Sofia builds a responsibility chart listing who is responsible, accountable, consulted and informed for each process. For access review, managers are responsible, the director is accountable, IT is consulted and the board is informed. She finds two problems. No one is accountable for supplier security, and incident handling has three people marked accountable, which means in practice no one is. COBIT 2019 uses similar responsibility mapping to clarify governance and management roles. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### 21.3 Fixing gaps

Sofia proposes that the director be accountable for supplier security, with the finance manager responsible for contracts and the IT lead consulted. For incidents, the IT lead becomes accountable, with the data protection lead responsible for breach notifications. The board approves the chart. She learns that accountability must rest with one role per process, and that charts are only useful if people know about them and they are reviewed when roles change. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Sofia models Elmfield's governance roles and processes, finds two accountability gaps with a RACI chart and fixes them.

> **Synthetic case.** Roles and chart are synthetic; COBIT 2019 is real.

### Errors and limits

Charts describe intended roles, not behaviour. Small teams blur roles.

### Exercises

- **EX061 — RACI letters.** What do the four RACI letters mean? *Rubric:* 3 = responsible, accountable, consulted, informed;; 2 = four;; 1 = none;; 0 = none.
- **EX062 — Incident problem.** What was wrong with incident handling? *Rubric:* 3 = three people accountable meant no one was;; 2 = too many;; 1 = none;; 0 = none.
- **EX063 — Accountability rule.** How many roles should be accountable per process? *Rubric:* 3 = one;; 2 = single;; 1 = several;; 0 = none.

### Synthesis

System models and RACI charts make accountability clear and reveal gaps.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security governance, risk and compliance: data and dependencies

### Learning outcomes

You will (1) map dependencies on suppliers; (2) tier suppliers by risk; (3) set proportionate supplier controls.

### 22.1 Supplier dependencies

Elmfield depends on suppliers for its housing system, email, payroll, repairs and printing. Sofia maps what each supplier accesses: data, systems or premises. She learns that NIST CSF 2.0 includes cybersecurity supply chain risk management in its Govern function, and that ISO/IEC 27002:2022 covers information security in supplier relationships. Small organisations depend heavily on suppliers, so their security often depends on suppliers' controls as much as their own. The same reasoning will return when Elmfield's auditors visit next year. She adds a short note to the shared course wiki for other students.

### 22.2 Tiering

Sofia scores five suppliers from zero to two on three factors: access to personal data, criticality to services and remote access to systems. The lab adds the scores and assigns tiers. The repairs contractor and cloud email score five, high tier. The payroll bureau scores four, also high. The printing firm scores one and the cleaning company zero, both low. Tiering lets Elmfield focus scrutiny on the three high-tier suppliers rather than treating all suppliers alike. This makes the governance consequence visible to people outside the engineering team.

### Lab — Supplier tiering by data, criticality and remote access

```python
"""Supplier tiering: data access, criticality and remote access scored 0-2 (synthetic)."""
sup = {"repairs contractor": (1, 2, 2), "payroll bureau": (2, 2, 0), "cloud email": (2, 2, 1),
       "printing firm": (1, 0, 0), "cleaning company": (0, 0, 0)}
for s, (d, c, r) in sup.items():
    t = d + c + r; tier = "high" if t >= 4 else "medium" if t >= 2 else "low"
    print(f"{s}: score {t} tier {tier}")
```

Run with `python3 lab_tier.py`. Verified output:

```text
repairs contractor: score 5 tier high
payroll bureau: score 4 tier high
cloud email: score 5 tier high
printing firm: score 1 tier low
cleaning company: score 0 tier low
```

### 22.3 Proportionate controls

For high-tier suppliers, Sofia recommends security questions before contracts, contract clauses on breach notification and data return, and an annual review of their assurance reports or certifications. For low-tier suppliers, a short confidentiality clause suffices. She notes that the repairs contractor's remote access needs particular attention, since its staff connect to the housing system from their own offices. She learns that proportionate supplier governance saves effort while focusing on real risk. Sofia keeps a dated copy of her working so that the result can be traced.

### Worked example

Sofia maps supplier access, tiers five suppliers with three high-tier and sets proportionate controls.

> **Synthetic case.** Suppliers and scores are synthetic; CSF 2.0 and ISO/IEC 27002:2022 are real.

### Errors and limits

Simple scores miss nuance. Supplier assurance reports vary in scope.

### Exercises

- **EX064 — Tiering factors.** Which three factors are scored? *Rubric:* 3 = personal data access, criticality, remote access;; 2 = three;; 1 = none;; 0 = none.
- **EX065 — High tier.** Which suppliers are high tier? *Rubric:* 3 = repairs contractor, cloud email, payroll bureau;; 2 = three;; 1 = printing;; 0 = none.
- **EX066 — High-tier controls.** Name two controls for high-tier suppliers. *Rubric:* 3 = pre-contract questions and breach notification clauses;; 2 = controls;; 1 = none;; 0 = none.

### Synthesis

Tiering suppliers focuses scrutiny where dependencies carry real risk.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security governance, risk and compliance: methods I

### Learning outcomes

You will (1) score risks on a 5x5 matrix; (2) compare matrix scores with expected loss; (3) understand when the two disagree.

### 23.1 Matrix scoring

Elmfield scores risks on a five-by-five matrix: likelihood and impact each from one to five, multiplied for a score. Sofia scores five risks with managers. Misdirected tenant data scores twelve, the lost laptop twelve, ransomware ten, contractor misuse nine and payment page outage six. The matrix is quick and familiar, which is why many organisations use it. Sofia also asks managers for an annual probability and a typical loss for each risk, to compare methods. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 23.2 Expected loss

The lab computes expected loss as probability times loss. Ransomware, with a one-in-ten chance and a loss of two hundred and fifty thousand, has the highest expected loss at twenty-five thousand. Misdirected data follows at twelve thousand and the lost laptop at ten thousand. The matrix ranks misdirected data first, tied with the laptop, while expected loss ranks ransomware first. The disagreement arises because the matrix compresses a very large impact into a score of five. She checks the idea against a second example before relying on it.

### Lab — Matrix scores versus expected loss

```python
"""5x5 scores vs expected loss (thousands) for five Elmfield risks."""
risks = [("tenant data misdirected", 4, 3, 0.8, 15), ("ransomware", 2, 5, 0.1, 250),
         ("lost laptop", 3, 4, 0.5, 20), ("payment page outage", 3, 2, 0.6, 8), ("contractor misuse", 3, 3, 0.2, 40)]
for n, l, i, p, loss in risks: print(f"{n}: score {l*i}, expected loss {p*loss:.1f}k")
print("top by score:", max(risks, key=lambda r: r[1]*r[2])[0]); print("top by expected loss:", max(risks, key=lambda r: r[3]*r[4])[0])
```

Run with `python3 lab_score.py`. Verified output:

```text
tenant data misdirected: score 12, expected loss 12.0k
ransomware: score 10, expected loss 25.0k
lost laptop: score 12, expected loss 10.0k
payment page outage: score 6, expected loss 4.8k
contractor misuse: score 9, expected loss 8.0k
top by score: tenant data misdirected
top by expected loss: ransomware
```

### 23.3 When they disagree

Sofia reads Cox (2008), who shows that risk matrices can assign higher ratings to quantitatively smaller risks and can produce ties between very different risks. Her lab illustrates both problems. She does not conclude that matrices are useless: they help start conversations and are easy for non-specialists. She recommends that Elmfield keep the matrix for initial screening but add rough expected loss estimates for its top risks, so that rare but severe risks like ransomware are not underestimated. The point seems small, but it changes how owners act on the result.

### Worked example

Sofia finds the matrix ranks misdirected data first while expected loss ranks ransomware first, and recommends combining both.

> **Synthetic case.** Scores and estimates are synthetic; Cox (2008) is real.

### Errors and limits

Expected loss needs uncertain inputs. Matrices compress severity.

### Exercises

- **EX067 — Matrix top.** Which risk tops the matrix ranking? *Rubric:* 3 = misdirected tenant data, tied with the laptop at 12;; 2 = tie;; 1 = ransomware;; 0 = none.
- **EX068 — Expected-loss top.** Which risk tops by expected loss? *Rubric:* 3 = ransomware at 25k;; 2 = ransomware;; 1 = laptop;; 0 = none.
- **EX069 — Disagreement cause.** Why do the methods disagree on ransomware? *Rubric:* 3 = the matrix compresses very large impacts into a score of five;; 2 = compression;; 1 = none;; 0 = none.

### Synthesis

Matrices aid screening, but expected loss reveals severe risks they understate.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security governance, risk and compliance: controls

### Learning outcomes

You will (1) select controls for Elmfield's top risks; (2) write a statement of applicability; (3) assign control owners.

### 24.1 Selecting controls

For each top risk, Sofia selects controls from ISO/IEC 27002:2022. For misdirected data: secure sharing links, recipient checks and training. For lost laptops: encryption and remote wipe. For ransomware: offline backups, multi-factor authentication and limited administrator rights. For contractor misuse: named accounts and access reviews. She learns that selecting from a recognised catalogue makes choices easier to explain and helps ensure nothing obvious is missed. Elmfield's security manager later asks for a copy of this analysis. She marks the open questions in red so that they are not forgotten.

### 24.2 Statement of applicability

ISO/IEC 27001:2022 requires a statement of applicability listing reference controls, whether each is included and why. Sofia drafts one for Elmfield. Most controls are included. Some are excluded with reasons: secure development controls are excluded because Elmfield builds no software, though supplier controls cover its housing system. She learns that exclusions must be justified by scope and risk, not by convenience, and that the statement becomes a key document for auditors. Writing the reasoning down also helps her spot a weak step in her argument.

### 24.3 Owners

Each control needs an owner who ensures it operates. Sofia assigns owners: IT lead for backups and encryption, managers for access reviews, data protection lead for sharing rules and the finance manager for supplier contracts. She writes a one-line description of each control's operation. She learns that owners must have both authority and time; assigning everything to the IT lead would overload one person and leave controls unperformed when that person is absent. Sofia discusses the trade-off with a classmate who works in finance.

### Worked example

Sofia selects controls for four risks, drafts a statement of applicability with justified exclusions and spreads ownership.

> **Synthetic case.** Elmfield's controls are synthetic; ISO/IEC 27001:2022 and 27002:2022 are real.

### Errors and limits

Catalogue controls need tailoring. Owners change roles.

### Exercises

- **EX070 — Laptop controls.** Which controls address lost laptops? *Rubric:* 3 = encryption and remote wipe;; 2 = two;; 1 = none;; 0 = none.
- **EX071 — Justified exclusion.** Why are secure development controls excluded? *Rubric:* 3 = Elmfield builds no software;; 2 = no development;; 1 = none;; 0 = none.
- **EX072 — Owner spread.** Why not assign all controls to the IT lead? *Rubric:* 3 = it would overload one person;; 2 = overload;; 1 = none;; 0 = none.

### Synthesis

Catalogue-based selection, a justified statement of applicability and spread ownership make controls real.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) test a control in a safe environment; (2) record evidence properly; (3) compare results with expectations.

### 25.1 Planning the test

In the first laboratory, Sofia tests Elmfield's backup control using a test copy of the file share provided by the IT lead. The test checks that a backup exists for each day of the last week, that it is stored offline and that a sample of files can be restored. She writes the steps, expected results and evidence to collect before starting. Testing in a copy ensures that nothing in live use is disturbed. The class compares answers and finds that most differences come from unstated assumptions.

### 25.2 Running and recording

Sofia restores twenty files chosen at random from different folders and dates. Nineteen restore correctly. One, a large spreadsheet, fails because the backup excluded files above a size limit. She records the date, steps, results, screenshots and file list. She stores the evidence in a folder that only she and the IT lead can change. She learns that evidence must allow someone else to understand what was tested and see the result for themselves. Sofia records this point in her course notebook so that later chapters can build on it.

### 25.3 Comparing with expectations

The control description said all files are backed up nightly; the test shows large files are excluded. Sofia reports the gap with its likely impact: large spreadsheets include rent arrears records. The IT lead changes the setting and asks her to retest, which passes. She learns that testing reveals the difference between what a control is believed to do and what it does, and that this difference is often caused by a forgotten configuration choice. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### Worked example

Sofia tests backups in a copy, restores nineteen of twenty files, finds a size exclusion and confirms the fix with a retest.

> **Synthetic case.** The test is synthetic.

### Errors and limits

Small samples miss rare failures. Test copies may differ from live systems.

### Exercises

- **EX073 — Restore result.** How many sampled files restored correctly? *Rubric:* 3 = nineteen of twenty;; 2 = 19;; 1 = 20;; 0 = none.
- **EX074 — Failure cause.** Why did one file fail to restore? *Rubric:* 3 = backup excluded files above a size limit;; 2 = size limit;; 1 = none;; 0 = none.
- **EX075 — Belief versus reality.** What did the test reveal about the control? *Rubric:* 3 = it did less than believed because of a forgotten setting;; 2 = gap;; 1 = none;; 0 = none.

### Synthesis

Laboratory testing shows what controls really do and produces evidence for fixes.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security governance, risk and compliance: methods II

### Learning outcomes

You will (1) run a gap assessment against NIST CSF 2.0; (2) summarise results by function; (3) prioritise improvements.

### 26.1 Gap assessment

Sofia runs a gap assessment using a sample of outcomes from each NIST CSF 2.0 function: Govern, Identify, Protect, Detect, Respond and Recover. With the IT lead and director, she rates each sampled outcome as achieved or not achieved, based on evidence rather than opinion. For example, an outcome about backups counts as achieved only because of the laboratory test. She records the evidence for each rating so that later reassessments can compare like with like. She notes the assumption behind it so that a reviewer can challenge it later.

### 26.2 Results

The lab summarises twenty-eight rated outcomes. Protect is strongest at five of six, eighty-three percent. Identify reaches sixty percent. Govern and Respond reach fifty percent. Recover reaches thirty-three percent and Detect is weakest at one of four, twenty-five percent. Overall, fifteen of twenty-eight outcomes are achieved, fifty-four percent. Sofia notes that Elmfield invested in protection but has little ability to notice or recover from incidents, a common pattern in small organisations. The same reasoning will return when Elmfield's auditors visit next year. She adds a short note to the shared course wiki for other students.

### Lab — Achieved CSF 2.0 outcomes by function

```python
"""Gap assessment: share of sampled CSF 2.0 outcomes achieved per function (synthetic ratings)."""
ratings = {"Govern": [1,0,0,1,0,1], "Identify": [1,1,0,1,0], "Protect": [1,1,1,0,1,1],
           "Detect": [0,1,0,0], "Respond": [1,0,0,1], "Recover": [0,0,1]}
for f, r in ratings.items(): print(f"{f}: {sum(r)}/{len(r)} = {sum(r)/len(r):.0%}")
t = sum(sum(r) for r in ratings.values()); n = sum(len(r) for r in ratings.values())
print(f"overall {t}/{n} = {t/n:.0%}; weakest {min(ratings, key=lambda f: sum(ratings[f])/len(ratings[f]))}")
```

Run with `python3 lab_gap.py`. Verified output:

```text
Govern: 3/6 = 50%
Identify: 3/5 = 60%
Protect: 5/6 = 83%
Detect: 1/4 = 25%
Respond: 2/4 = 50%
Recover: 1/3 = 33%
overall 15/28 = 54%; weakest Detect
```

### 26.3 Priorities

Sofia proposes priorities based on the gaps and on risk. Detection comes first: enabling alerts in cloud email and identity services and assigning someone to review them. Recovery comes second: documenting and testing a restore plan for the housing system. Governance improvements, such as approving a risk appetite, follow. She warns that percentages from small samples are rough, so they should guide priorities rather than become targets. The board approves the plan for the coming year. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Sofia rates twenty-eight CSF outcomes, finds Detect weakest at twenty-five percent and prioritises detection and recovery.

> **Synthetic case.** Ratings are synthetic; CSF 2.0 is real.

### Errors and limits

Sampled outcomes are not the whole framework. Binary ratings lose nuance.

### Exercises

- **EX076 — Rating basis.** On what basis are outcomes rated achieved? *Rubric:* 3 = evidence rather than opinion;; 2 = evidence;; 1 = opinion;; 0 = none.
- **EX077 — Weakest function.** Which function is weakest and at what level? *Rubric:* 3 = Detect, 1/4 = 25%;; 2 = Detect;; 1 = Protect;; 0 = none.
- **EX078 — Overall result.** What share of outcomes is achieved overall? *Rubric:* 3 = 15/28 = 54%;; 2 = 54%;; 1 = none;; 0 = none.

### Synthesis

Evidence-based gap assessments show where investment is unbalanced and guide priorities.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security governance, risk and compliance: verification

### Learning outcomes

You will (1) verify controls through inspection, observation and re-performance; (2) choose suitable tests; (3) document verification results.

### 27.1 Test types

Sofia learns three ways to verify a control. Inspection examines documents or records, such as access review sign-offs. Observation watches a control being performed, such as a manager reviewing access. Re-performance repeats the control independently, such as Sofia comparing the leaver list with active accounts herself. Re-performance gives the strongest evidence because it does not rely on the owner's records, but it takes the most time and access. Sofia keeps a dated copy of her working so that the result can be traced. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 27.2 Choosing tests

For each key control Sofia chooses a test. For access reviews, she inspects sign-offs and re-performs a sample. For encryption, she inspects the device console report. For incident handling, she observes a tabletop exercise. She learns that the choice depends on the control's importance and the evidence available. Important controls deserve stronger tests. She also notes that relying only on inspection risks accepting records that look complete but describe controls nobody actually performed. She checks the idea against a second example before relying on it.

### 27.3 Documenting results

Sofia documents each test with its objective, method, sample, results and conclusion. Re-performing the leaver check reveals one account that the access review missed, so she concludes the review control operates with an exception. She recommends adding the leaver list to reviewers' materials. She learns that verification results should state clearly whether a control operated effectively, operated with exceptions or failed, so that management knows how much to rely on it. The point seems small, but it changes how owners act on the result.

### Worked example

Sofia uses inspection, observation and re-performance, finds an access review exception and states conclusions clearly.

> **Synthetic case.** Tests and results are synthetic.

### Errors and limits

Observation can change behaviour. Re-performance needs access.

### Exercises

- **EX079 — Strongest test.** Which test type gives the strongest evidence? *Rubric:* 3 = re-performance;; 2 = re-perform;; 1 = inspection;; 0 = none.
- **EX080 — Inspection risk.** What is the risk of relying only on inspection? *Rubric:* 3 = records may describe controls nobody performed;; 2 = false records;; 1 = none;; 0 = none.
- **EX081 — Conclusion categories.** What three conclusions can a verification reach? *Rubric:* 3 = effective, effective with exceptions, failed;; 2 = three;; 1 = none;; 0 = none.

### Synthesis

Verification chooses fitting tests and states clearly how far controls can be relied on.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security governance, risk and compliance: failure analysis

### Learning outcomes

You will (1) analyse an incident for control failures; (2) run a blameless review; (3) turn lessons into control changes.

### 28.1 The incident

A synthetic incident occurs: a housing officer emails a spreadsheet with tenants' arrears details to an external address with a similar name to a council contact. The recipient reports it, and the file is deleted. Sofia helps the data protection lead assess whether the breach must be reported to the regulator and whether tenants should be told, following Elmfield's procedure. The assessment considers the sensitivity of the data and the recipient's confirmation of deletion. Elmfield's security manager later asks for a copy of this analysis.

### 28.2 Blameless review

Sofia facilitates a blameless review. The aim is to understand how the system allowed the error, not to punish the officer. They find that email auto-completed the wrong address, that spreadsheets with arrears data were routinely emailed rather than shared through the housing system and that no warning appeared for external recipients. Sofia learns that blameless reviews encourage honest accounts, which reveal design problems. Blaming individuals tends to hide information and leaves the same conditions in place. She marks the open questions in red so that they are not forgotten.

### 28.3 Control changes

The review leads to changes: an external recipient warning in email, a rule that arrears data are shared through secure links with expiry, and a short reminder in team meetings. Sofia updates the risk register, raising the likelihood estimate for misdirected data and recording the new controls. She learns that incidents are evidence about control effectiveness and should feed back into risk assessment, closing the loop between operations and governance. Writing the reasoning down also helps her spot a weak step in her argument.

### Worked example

Sofia supports breach assessment, runs a blameless review finding three system causes and feeds changes into the register.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Blameless reviews still need accountability for repeated negligence. Warnings cause fatigue.

### Exercises

- **EX082 — Review aim.** What is the aim of a blameless review? *Rubric:* 3 = understand how the system allowed the error;; 2 = system;; 1 = punishment;; 0 = none.
- **EX083 — System causes.** Name two system causes found. *Rubric:* 3 = auto-complete and routine emailing of arrears spreadsheets;; 2 = causes;; 1 = none;; 0 = none.
- **EX084 — Register update.** How did Sofia update the register? *Rubric:* 3 = raised likelihood for misdirected data and recorded new controls;; 2 = update;; 1 = none;; 0 = none.

### Synthesis

Blameless failure analysis turns incidents into better controls and better risk estimates.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security governance, risk and compliance: operations

### Learning outcomes

You will (1) run a governance calendar; (2) track actions to completion; (3) report to the board.

### 29.1 Governance calendar

Sofia helps Elmfield set a governance calendar. Monthly: review security alerts and incidents. Quarterly: access reviews, risk register review and supplier checks. Twice a year: board report. Annually: policy review, backup restore test and gap reassessment. Each activity has an owner and a reminder in the shared calendar. She learns that a calendar turns good intentions into routine, and that small organisations benefit from predictable rhythms because staff can plan around them. Sofia discusses the trade-off with a classmate who works in finance. The class compares answers and finds that most differences come from unstated assumptions.

### 29.2 Tracking actions

Every finding and improvement becomes an action with an owner and a due date in a simple tracker. Sofia reviews the tracker monthly with the director. Overdue actions are discussed, not hidden. After three months, eighteen of twenty-four actions are complete. She learns that tracking is most useful when it prompts conversations about obstacles, such as an owner lacking time or budget, rather than simply listing overdue items. Sofia records this point in her course notebook so that later chapters can build on it.

### 29.3 Board reporting

Sofia drafts Elmfield's first board security report. It covers top risks and changes, gap assessment progress, incidents and lessons, overdue actions and decisions requested. It is three pages with plain language. The board asks good questions, especially about supplier risk. Sofia learns that boards engage when reports are short, honest and ask for decisions. A report that only reassures gives the board nothing to govern, which undermines the purpose of oversight. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### Worked example

Sofia sets a governance calendar, tracks twenty-four actions with eighteen complete and drafts a three-page board report.

> **Synthetic case.** Actions and reports are synthetic.

### Errors and limits

Calendars slip under pressure. Board attention varies.

### Exercises

- **EX085 — Quarterly items.** Which activities are quarterly? *Rubric:* 3 = access reviews, register review, supplier checks;; 2 = three;; 1 = none;; 0 = none.
- **EX086 — Action progress.** How many actions were complete after three months? *Rubric:* 3 = eighteen of twenty-four;; 2 = 18/24;; 1 = none;; 0 = none.
- **EX087 — Reassurance problem.** Why is a report that only reassures a problem? *Rubric:* 3 = it gives the board nothing to govern;; 2 = no decisions;; 1 = none;; 0 = none.

### Synthesis

A governance calendar, action tracking and decision-focused reports keep the programme running.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) run a tabletop exercise; (2) evaluate response against the plan; (3) record improvements.

### 30.1 Exercise design

In the second laboratory, Sofia designs a tabletop exercise for Elmfield's managers: ransomware has encrypted the file server on a Monday morning. The scenario unfolds in stages, with new information at each stage. Participants decide what to do using the incident plan. The exercise is announced, uses no real systems and lasts ninety minutes. Sofia prepares injects, such as a call from a journalist and a tenant asking about their data. She notes the assumption behind it so that a reviewer can challenge it later.

### 30.2 Observations

Sofia and a colleague observe. Managers quickly isolate the server but are unsure who decides whether to contact the police and the regulator. The backup restore plan exists but nobody knows where it is stored. Communication with tenants is improvised. The housing system, being a cloud service, keeps running, which reassures everyone. She records each observation with the time and compares actions with the incident plan. The same reasoning will return when Elmfield's auditors visit next year. She adds a short note to the shared course wiki for other students.

### 30.3 Improvements

After the exercise, the group agrees improvements: name the director as decision maker for external notifications, store the restore plan in two places including paper, and prepare template messages for tenants. Sofia records these as actions in the tracker. She learns that tabletop exercises are cheap and safe ways to test plans, and that they often reveal simple gaps, such as a plan nobody can find, that matter enormously in a real incident. This makes the governance consequence visible to people outside the engineering team.

### Worked example

Sofia runs a ransomware tabletop, observes three gaps and records agreed improvements as tracked actions.

> **Synthetic case.** The exercise is synthetic and used no real systems.

### Errors and limits

Tabletops do not test technical recovery. Participants may perform for observers.

### Exercises

- **EX088 — Exercise safety.** Why does the tabletop use no real systems? *Rubric:* 3 = to stay safe and avoid disruption;; 2 = safety;; 1 = none;; 0 = none.
- **EX089 — Missing plan.** What gap concerned the restore plan? *Rubric:* 3 = nobody knew where it was stored;; 2 = location;; 1 = none;; 0 = none.
- **EX090 — Notification decision.** Who will decide on external notifications? *Rubric:* 3 = the director;; 2 = director;; 1 = IT lead;; 0 = none.

### Synthesis

Tabletop exercises safely reveal simple gaps that matter greatly in real incidents.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security governance, risk and compliance: advanced cases

### Learning outcomes

You will (1) analyse governance in payment and certification contexts; (2) understand scope reduction; (3) compare assurance types.

### 31.1 Payments

Elmfield takes rent payments by card through a hosted payment page run by a provider. Sofia learns that PCI DSS v4.0 applies to organisations that store, process or transmit cardholder data or could affect its security. By using a hosted page, Elmfield keeps card data off its own systems, greatly reducing its obligations, though it must still protect the website that links to the payment page and confirm the provider's compliance. She learns that architecture choices can shrink compliance scope substantially. Sofia records this point in her course notebook so that later chapters can build on it.

### 31.2 Certification

Elmfield's board asks whether it should seek ISO/IEC 27001:2022 certification. Sofia lists benefits: tenders from councils increasingly ask for it, and it would discipline the programme. Costs include audit fees, staff time and ongoing surveillance audits. She suggests first operating the management system for a year and measuring progress against the gap assessment, then deciding. She learns that certification is a means, not an end, and should be chosen for clear reasons. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### 31.3 Assurance types

Sofia compares assurance types Elmfield receives from suppliers. Certification shows a management system met a standard at audit. SOC 2 reports, based on the AICPA trust services criteria, describe controls and, in a type two report, test their operation over a period. Questionnaires record what suppliers claim. She learns that each type provides different strength of evidence and that reading the scope and exceptions in a report matters more than its title. She notes the assumption behind it so that a reviewer can challenge it later.

### Worked example

Sofia explains how a hosted payment page reduces PCI DSS scope, weighs certification and compares assurance types.

> **Synthetic case.** Elmfield's choices are synthetic; PCI DSS v4.0, ISO/IEC 27001:2022 and AICPA TSC are real.

### Errors and limits

Scope reduction does not remove all duties. Reports vary in scope.

### Exercises

- **EX091 — Hosted page effect.** How does a hosted payment page affect PCI DSS obligations? *Rubric:* 3 = keeps card data off Elmfield's systems, reducing scope;; 2 = scope;; 1 = none;; 0 = none.
- **EX092 — Certification advice.** What did Sofia suggest before deciding on certification? *Rubric:* 3 = operate the system for a year and measure progress;; 2 = wait;; 1 = none;; 0 = none.
- **EX093 — Type two report.** What does a SOC 2 type two report add? *Rubric:* 3 = tests of control operation over a period;; 2 = operation;; 1 = none;; 0 = none.

### Synthesis

Architecture, certification and assurance choices shape compliance effort and evidence strength.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security governance, risk and compliance: interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, finance and HR on governance; (2) translate between professional languages; (3) handle conflicting priorities.

### 32.1 Legal

Sofia works with Elmfield's external solicitor on data sharing agreements with councils. The solicitor focuses on lawful basis and liability; Sofia focuses on security controls and evidence. They agree a template that covers both. She learns that GRC staff should not give legal advice but must understand legal requirements well enough to ask the right questions and translate them into controls. The boundary between legal and security roles needs to be clear and respected. The same reasoning will return when Elmfield's auditors visit next year.

### 32.2 Finance and HR

Finance cares about cost, insurance and fraud; HR cares about fair treatment of staff and accurate records. Sofia learns to frame security in their terms. For finance, she presents controls as reducing expected loss and insurance premiums. For HR, she presents the leaver process as protecting former staff from misuse of their accounts as well as protecting tenants. Framing in each discipline's language increases cooperation without changing the substance of the controls. She adds a short note to the shared course wiki for other students.

### 32.3 Conflicting priorities

Conflicts arise. Housing managers want staff to work quickly from anywhere; IT wants tighter device controls. Sofia facilitates a meeting where each side explains its concerns. They agree that managed devices may work from anywhere, while personal devices get access to email only. She learns that conflicts are best resolved by understanding underlying needs and agreeing a documented compromise, which the director approves as a risk decision with a review date. This makes the governance consequence visible to people outside the engineering team. Sofia keeps a dated copy of her working so that the result can be traced.

### Worked example

Sofia co-writes a data sharing template with legal, frames controls for finance and HR and mediates a device conflict.

> **Synthetic case.** The collaborations are synthetic.

### Errors and limits

Translation can oversimplify. Compromises may drift.

### Exercises

- **EX094 — Legal boundary.** What should GRC staff not do in legal matters? *Rubric:* 3 = give legal advice;; 2 = advice;; 1 = none;; 0 = none.
- **EX095 — HR framing.** How did Sofia frame the leaver process for HR? *Rubric:* 3 = protecting former staff from account misuse;; 2 = fairness;; 1 = none;; 0 = none.
- **EX096 — Device compromise.** What compromise was agreed for devices? *Rubric:* 3 = managed devices anywhere, personal devices email only;; 2 = compromise;; 1 = none;; 0 = none.

### Synthesis

GRC work depends on translating between disciplines and documenting compromises.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse interview data thematically; (2) check reliability of coding; (3) report qualitative findings honestly.

### 33.1 Thematic analysis

Sofia returns to her interviews with twelve managers about access reviews. She reads transcripts several times, codes passages with short labels and groups codes into themes. Three themes emerge: lists were too long and used system jargon, managers did not know what their staff actually needed and reviews arrived at busy times. She learns that thematic analysis is systematic, not impressionistic, and requires a clear record of how codes became themes. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 33.2 Reliability

To check her coding, a classmate independently codes four transcripts with Sofia's codebook. They agree on most passages, and discussion of disagreements refines two code definitions. She reports agreement using Cohen's kappa as discussed by Landis and Koch (1977) for interpreting agreement levels, while noting that qualitative research also values reflexivity: being aware of how her own role at Elmfield might shape what managers told her and what she noticed. She checks the idea against a second example before relying on it. The point seems small, but it changes how owners act on the result.

### 33.3 Reporting

Sofia reports themes with illustrative anonymised quotes, counts of how many managers raised each and the contrary views she found. Two managers liked the reviews and found them easy. She recommends shorter lists with plain descriptions, a short guide on role needs and scheduling reviews outside month-end. She learns that qualitative findings are most persuasive when they show their evidence, include dissent and lead to concrete changes that can later be tested. Elmfield's security manager later asks for a copy of this analysis. She marks the open questions in red so that they are not forgotten.

### Worked example

Sofia finds three themes, checks coding with a classmate and reports anonymised findings including dissent.

> **Synthetic case.** Interviews are synthetic; Landis and Koch (1977) is real.

### Errors and limits

Themes reflect the analyst's lens. Twelve interviews limit generality.

### Exercises

- **EX097 — Three themes.** Name the three themes. *Rubric:* 3 = long jargon-filled lists, unknown staff needs, busy timing;; 2 = three;; 1 = none;; 0 = none.
- **EX098 — Reflexivity.** What is reflexivity in this study? *Rubric:* 3 = awareness of how Sofia's role shapes data;; 2 = self-awareness;; 1 = none;; 0 = none.
- **EX099 — Dissent.** Why report the two managers who liked reviews? *Rubric:* 3 = including dissent makes findings more credible;; 2 = balance;; 1 = none;; 0 = none.

### Synthesis

Systematic coding, reliability checks and honest reporting make qualitative GRC research useful.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare governance approaches across organisations; (2) choose fair comparison criteria; (3) avoid misleading league tables.

### 34.1 Two organisations

Sofia compares Elmfield with a second fictional organisation, Corbridge Community Trust, a charity of similar size. Both agree to share anonymised summaries of their governance practices. Corbridge uses a managed service provider for IT and security, while Elmfield has an in-house IT lead. Sofia wants to understand how the different models affect governance: who owns risks, how evidence is gathered and how boards are informed. Writing the reasoning down also helps her spot a weak step in her argument. Sofia discusses the trade-off with a classmate who works in finance.

### 34.2 Fair criteria

Sofia chooses criteria that make sense for both: existence of an approved risk appetite, register review frequency, access review completion, backup testing and board reporting. She avoids comparing raw incident counts, because reporting cultures differ: a higher count may reflect better reporting rather than worse security. She learns that comparisons must account for context and measurement differences, or they will mislead the very people they aim to inform. The class compares answers and finds that most differences come from unstated assumptions. Sofia records this point in her course notebook so that later chapters can build on it.

### 34.3 Findings

Corbridge has stronger technical monitoring through its provider but weaker ownership, since staff assume the provider handles everything. Elmfield has clearer ownership but less monitoring. Sofia presents these as complementary lessons rather than a ranking. She recommends that Elmfield consider buying monitoring services while keeping in-house ownership, and that Corbridge clarify which risks remain its own. Both organisations find the comparison useful because it avoided judging one as better. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### Worked example

Sofia compares two organisations on five fair criteria, avoids raw incident counts and presents complementary lessons.

> **Synthetic case.** Both organisations are synthetic.

### Errors and limits

Two cases cannot generalise. Shared summaries may be optimistic.

### Exercises

- **EX100 — Model difference.** How do the two organisations' IT models differ? *Rubric:* 3 = managed service provider versus in-house IT lead;; 2 = models;; 1 = none;; 0 = none.
- **EX101 — Incident counts.** Why avoid comparing raw incident counts? *Rubric:* 3 = reporting cultures differ;; 2 = culture;; 1 = none;; 0 = none.
- **EX102 — Corbridge weakness.** What weakness did Corbridge show? *Rubric:* 3 = weak ownership because staff assume the provider handles everything;; 2 = ownership;; 1 = none;; 0 = none.

### Synthesis

Fair comparisons use context-aware criteria and yield lessons rather than rankings.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone that improves a governance control; (2) define measurable outcomes; (3) plan ethics and risks.

### 35.1 The proposal

For her capstone, Sofia proposes redesigning Elmfield's quarterly access review using her research findings: shorter lists with plain descriptions, a role guide, scheduling outside month-end and the leaver list included. She will measure whether completion time, completion rate and the number of excess rights found change compared with the previous two quarters. She writes the proposal with background, aims, methods, timeline, ethics and risks, in ten pages. She notes the assumption behind it so that a reviewer can challenge it later. The same reasoning will return when Elmfield's auditors visit next year.

### 35.2 Outcomes

Sofia defines outcomes before starting: completion rate by the deadline, median days to complete, rights removed per hundred reviewed and manager satisfaction on a short survey. She notes that rights removed might fall because earlier reviews already cleaned up access, not because the new design is worse, and records this as an interpretation risk. She learns that defining outcomes and their limits in advance prevents choosing flattering measures after results arrive. She adds a short note to the shared course wiki for other students.

### 35.3 Ethics and risks

The capstone involves managers' work but not personal data beyond what reviews already use. Sofia obtains Dr. Haddad's approval and Elmfield's agreement. Risks include a busy quarter, manager turnover and her own limited time. She plans responses, such as a fallback schedule. She also commits to keep the old process available if the new one fails, so that Elmfield's control is never weaker because of her project. This makes the governance consequence visible to people outside the engineering team. Sofia keeps a dated copy of her working so that the result can be traced.

### Worked example

Sofia proposes a redesigned access review with four predefined outcomes, interpretation risks and a fallback.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

Before-after comparisons confound time. Surveys measure perception.

### Exercises

- **EX103 — Design elements.** What four changes does the redesign include? *Rubric:* 3 = shorter plain lists, role guide, better timing, leaver list;; 2 = four;; 1 = none;; 0 = none.
- **EX104 — Interpretation risk.** Why might rights removed fall for reasons unrelated to the design? *Rubric:* 3 = earlier reviews already cleaned up access;; 2 = prior cleanup;; 1 = none;; 0 = none.
- **EX105 — Safety commitment.** What safeguards Elmfield's control during the project? *Rubric:* 3 = keeping the old process available if the new one fails;; 2 = fallback;; 1 = none;; 0 = none.

### Synthesis

A good capstone proposal fixes outcomes and safeguards in advance.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply GRC skills in a community setting; (2) adapt guidance for very small organisations; (3) respect the limits of volunteer help.

### 36.1 Community placement

Sofia volunteers with a local tenants' association linked to Elmfield. It has a committee of eight volunteers, a laptop, a shared email account and a spreadsheet of member contacts. Its needs are small but real: it holds personal data and handles small amounts of money. Sofia learns that frameworks designed for organisations with staff and budgets must be adapted heavily for groups like this, focusing on a handful of high-value actions. Her lecturer reminds the class that clear reasoning matters more than a polished answer.

### 36.2 Simple guidance

Sofia writes a one-page guide: give each committee member their own account instead of sharing one, turn on multi-factor authentication, keep the member list in one place with access for two people, back it up monthly and delete contacts of people who have left. She draws on the NIST CSF 2.0 small business quick-start materials but simplifies further. The committee adopts four of the five steps immediately and agrees to revisit the fifth. She checks the idea against a second example before relying on it.

### 36.3 Limits

Sofia is careful about limits. She does not access members' personal data herself, does not set up accounts using her own credentials and does not promise ongoing support she cannot provide. Instead she teaches two committee members to do each step. She learns that volunteer help should build the group's own capacity rather than create dependence, and that good intentions must be matched by clear boundaries and handover. The point seems small, but it changes how owners act on the result. Elmfield's security manager later asks for a copy of this analysis.

### Worked example

Sofia writes a five-step guide for a tenants' association, sees four steps adopted and builds the committee's own capacity.

> **Synthetic case.** The association is synthetic; CSF 2.0 resources are real.

### Errors and limits

Volunteers change often. Simple guidance omits risks.

### Exercises

- **EX106 — Shared account fix.** What replaced the shared email account? *Rubric:* 3 = individual accounts for each member;; 2 = own accounts;; 1 = none;; 0 = none.
- **EX107 — Steps adopted.** How many guide steps were adopted immediately? *Rubric:* 3 = four of five;; 2 = 4;; 1 = 5;; 0 = none.
- **EX108 — Volunteer boundary.** Why did Sofia teach members instead of doing the work herself? *Rubric:* 3 = to build capacity, not dependence;; 2 = capacity;; 1 = none;; 0 = none.

### Synthesis

Community GRC work adapts guidance to tiny organisations and builds their own capacity.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critique governance evidence presented by peers; (2) judge evidence strength; (3) give constructive feedback.

### 37.1 The seminar

In the evidence review seminar, each student presents the evidence behind one governance claim from their placement. Sofia presents the claim that Elmfield's backups work, supported by the laboratory restore test, the retest after the fix and the monthly backup job reports. A classmate presents a claim that phishing risk fell, supported only by fewer reported suspicious emails. The class discusses which claims are well supported and why. She marks the open questions in red so that they are not forgotten. Writing the reasoning down also helps her spot a weak step in her argument.

### 37.2 Judging strength

The group ranks evidence types. Independent re-performance and tests rank highest. System-generated reports rank next. Owner statements and questionnaires rank lowest. They note that fewer reported emails could mean less phishing, better filtering or less reporting, so the classmate's claim is weak. Sofia's claim is strong for the files tested but cannot prove every system is backed up. She learns that judging evidence means asking what else could explain it and how much it covers. Sofia discusses the trade-off with a classmate who works in finance.

### 37.3 Constructive feedback

Dr. Haddad asks students to give feedback that helps. Sofia suggests her classmate add data on filtered emails and a short survey of reporting habits. She receives feedback that her claim should state its scope: the file share only, not the housing system, which the supplier backs up. She revises the claim. She learns that peer review improves claims when feedback is specific, respectful and focused on evidence rather than on the person. The class compares answers and finds that most differences come from unstated assumptions.

### Worked example

Sofia ranks evidence types, spots alternative explanations in a peer's claim and narrows her own claim's scope after feedback.

> **Synthetic case.** The seminar and claims are synthetic.

### Errors and limits

Rankings are general guides. Feedback can be too polite to help.

### Exercises

- **EX109 — Weakest evidence.** Which evidence types rank lowest? *Rubric:* 3 = owner statements and questionnaires;; 2 = statements;; 1 = tests;; 0 = none.
- **EX110 — Phishing alternatives.** What else could explain fewer reported suspicious emails? *Rubric:* 3 = better filtering or less reporting;; 2 = alternatives;; 1 = none;; 0 = none.
- **EX111 — Scope correction.** How did Sofia revise her backup claim? *Rubric:* 3 = limited it to the file share;; 2 = scope;; 1 = none;; 0 = none.

### Synthesis

Evidence review asks what else could explain a claim and how much it covers.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement a redesigned governance process; (2) monitor it as it runs; (3) adjust without losing comparability.

### 38.1 Implementation

Sofia implements the redesigned access review for one quarter. She prepares shorter lists with plain descriptions of each permission, writes a two-page role guide with the data protection lead, schedules the review for the second week of the month and adds the leaver list. She briefs managers in a short meeting and offers help sessions. She keeps a log of every question managers ask, because questions reveal where the design is still unclear. Sofia records this point in her course notebook so that later chapters can build on it.

### 38.2 Monitoring

During the review, Sofia tracks completion daily. Most managers finish within a week. Two ask what a permission called case escalation means, so she clarifies its description for everyone. One manager is on leave, and a deputy completes the review. She records these events. She learns that monitoring a new process as it runs allows small fixes, but each change must be logged so that the evaluation can account for it later. Dr. Haddad asks her to explain the idea aloud to a classmate before moving on.

### 38.3 Comparability

Sofia is tempted to change the measurement method when she notices the old completion data used different dates. Instead, she records completion using both the old and new definitions, so results can be compared fairly with previous quarters. She learns that improving a process and evaluating it are different tasks, and that keeping measurement consistent is essential if Elmfield is to learn whether the redesign actually helped. She notes the assumption behind it so that a reviewer can challenge it later. The same reasoning will return when Elmfield's auditors visit next year.

### Worked example

Sofia runs the redesigned review, logs questions and fixes, and keeps both old and new measurement definitions for fair comparison.

> **Synthetic case.** The implementation is synthetic.

### Errors and limits

Mid-course fixes complicate evaluation. One quarter is a short trial.

### Exercises

- **EX112 — Question log.** Why does Sofia log managers' questions? *Rubric:* 3 = they reveal unclear parts of the design;; 2 = clarity;; 1 = none;; 0 = none.
- **EX113 — Clarified permission.** Which permission description was clarified? *Rubric:* 3 = case escalation;; 2 = case escalation;; 1 = none;; 0 = none.
- **EX114 — Dual definitions.** Why record completion under both definitions? *Rubric:* 3 = to compare fairly with previous quarters;; 2 = comparability;; 1 = none;; 0 = none.

### Synthesis

Implementing a redesign well means monitoring, logging changes and keeping measurement consistent.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate a redesigned process against predefined outcomes; (2) interpret results cautiously; (3) recommend next steps.

### 39.1 Results

Sofia compares the redesigned quarter with the previous two. Completion by the deadline rose from eight of twelve managers to eleven of twelve. Median days to complete fell from fourteen to six. Rights removed per hundred reviewed fell slightly, from four to three. The manager survey shows most found the lists clearer. She presents each result with the counts behind it, avoiding percentages that would exaggerate small numbers. She adds a short note to the shared course wiki for other students. This makes the governance consequence visible to people outside the engineering team.

### 39.2 Interpretation

Sofia interprets cautiously. Completion and speed improved clearly, consistent with the redesign helping. The small fall in removals matches her predefined interpretation risk: earlier reviews had already cleaned up much excess access. Other explanations exist; the quarter was quieter than usual and managers knew they were being studied. With twelve managers and one quarter, she cannot rule these out. She states the evidence supports the redesign without proving it caused the improvement. Sofia keeps a dated copy of her working so that the result can be traced.

### 39.3 Next steps

Sofia recommends that Elmfield keep the redesign, continue measuring for three more quarters and extend the approach to the housing system review. She suggests adding a check that approved removals actually happen. Elmfield's director accepts the recommendations. Sofia learns that evaluation is valuable even when results cannot prove cause, because it tells the organisation whether to continue, adjust or stop and what to watch for next. Her lecturer reminds the class that clear reasoning matters more than a polished answer. She checks the idea against a second example before relying on it.

### Worked example

Sofia finds completion rose to eleven of twelve and median time fell to six days, interprets cautiously and recommends continued measurement.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Small samples and observation effects limit conclusions. Surveys are subjective.

### Exercises

- **EX115 — Completion change.** How did completion by the deadline change? *Rubric:* 3 = from eight of twelve to eleven of twelve;; 2 = improved;; 1 = none;; 0 = none.
- **EX116 — Median change.** How did median days to complete change? *Rubric:* 3 = from fourteen to six;; 2 = faster;; 1 = none;; 0 = none.
- **EX117 — Cause caution.** Why can Sofia not claim the redesign caused the improvement? *Rubric:* 3 = quieter quarter and observation effects;; 2 = alternatives;; 1 = none;; 0 = none.

### Synthesis

Careful evaluation guides decisions even when it cannot prove cause.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis on a governance improvement; (2) present to academic and practitioner audiences; (3) reflect on learning.

### 40.1 The thesis

Sofia writes her thesis on improving access review in a small social landlord. It covers the problem, literature and standards, her interview study, the redesign, implementation, evaluation and conclusions. She cites ISO/IEC 27002:2022 on access rights, NIST CSF 2.0 and the research on user participation by Spears and Barki (2010). Each claim links to evidence, and limitations are stated plainly. Appendices hold the interview guide, codebook, role guide and measurement definitions. The point seems small, but it changes how owners act on the result. Elmfield's security manager later asks for a copy of this analysis.

### 40.2 Presentations

Sofia presents twice. To examiners at Brightwater she focuses on methods, evidence and limits. To Elmfield's board she focuses on what changed, what it cost and what the board should decide. Examiners ask how she avoided bias given her placement role; she explains her reflexive notes and the second coder. The board asks whether the approach could work for repairs contractors; she suggests a pilot. Both audiences value clear evidence presented in their own terms. She marks the open questions in red so that they are not forgotten.

### 40.3 Reflection

Sofia reflects on her four years. She began counting laptops and ended redesigning a governance process with evidence. She learned that governance is mainly about people, clarity and follow-through, supported by data and standards. She also learned to state limits honestly and to give credit to the managers whose interviews shaped her work. Dr. Haddad notes that her habits of precise claims and fair evidence will serve her in any GRC role. Writing the reasoning down also helps her spot a weak step in her argument.

### Worked example

Sofia writes and presents her thesis to two audiences, answers questions on bias and reflects on her learning.

> **Synthetic case.** The thesis is synthetic; cited sources are real.

### Errors and limits

Reflection can be selective. One organisation limits generality.

### Exercises

- **EX118 — Thesis sources.** Which research paper on participation does Sofia cite? *Rubric:* 3 = Spears and Barki (2010);; 2 = Spears;; 1 = none;; 0 = none.
- **EX119 — Bias answer.** How did Sofia answer the examiners on bias? *Rubric:* 3 = reflexive notes and a second coder;; 2 = reflexivity;; 1 = none;; 0 = none.
- **EX120 — Board suggestion.** What did Sofia suggest for repairs contractors? *Rubric:* 3 = a pilot of the approach;; 2 = pilot;; 1 = none;; 0 = none.

### Synthesis

A bachelor's thesis joins research, practice and honest limits into usable governance knowledge.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Sofia Reyes, Dr. Malik Haddad, Brightwater College, Elmfield Housing Association, Corbridge Community Trust and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Five percentage points (a halving in relative terms).

**EX002.** Because without the count and knowing which items are missing, the share hides important detail.

**EX003.** The date, the count, the base and the source.

**EX004.** Asset name, type, owner, location, data held and supplier.

**EX005.** The board portal had no owner and eleven tablets were missing from the repairs list.

**EX006.** A quarterly check against purchase records and the identity system.

**EX007.** It replaces impressions with facts and gives the same answer each run.

**EX008.** Assets holding tenant personal data that lacked an owner.

**EX009.** The asset, the problem, a suggested owner and the date of the run.

**EX010.** That formal frameworks cost too much for small teams.

**EX011.** Because requirements change between editions.

**EX012.** Because if you cannot explain an idea in your own words, you have not yet understood it.

**EX013.** Ordinary failures and mistakes rather than sophisticated attacks.

**EX014.** Backups kept offline.

**EX015.** Because fear often leads staff to hide mistakes rather than report them.

**EX016.** One person covering for a colleague could both add a supplier and approve payment to it.

**EX017.** With temporary access, a second approver and an end date.

**EX018.** Cloud identity, on which most services depend.

**EX019.** Because staff and data are spread across cloud services, mobile devices and offices.

**EX020.** Only the name, address and phone number they need.

**EX021.** The exposed remote desktop service on the file server.

**EX022.** Because their output may be used as evidence, and wrong evidence misleads.

**EX023.** Because the identity system uses email addresses and HR uses staff numbers.

**EX024.** An active account that matches no staff member.

**EX025.** Likelihood multiplied by impact.

**EX026.** Tenant data emailed to the wrong person and the lost laptop with case notes, both scoring 12.

**EX027.** R3, repairs contractor account misuse, and R6, weak passwords on the board portal.

**EX028.** Active testing of systems.

**EX029.** She kept it on an encrypted Elmfield laptop, removed names when sharing and deleted copies at the end.

**EX030.** Because attackers could exploit it at any time, so waiting would leave harm possible.

**EX031.** Administrator group membership on each laptop.

**EX032.** They were repairs laptops bought locally outside the normal purchasing route.

**EX033.** Thirty days.

**EX034.** Because it behaves well for small counts and proportions near zero or one.

**EX035.** 42% to 75%.

**EX036.** Because they rarely use laptops and the policy was sent by email.

**EX037.** HR sends leaver notices automatically before the last day and IT confirms each disablement in a ticket.

**EX038.** Only the specialist support team.

**EX039.** Seven.

**EX040.** Using tenancy and repairs data for unrelated marketing.

**EX041.** Repairs contractors receive too much data and call recording retention is unknown (also support needs stored twice).

**EX042.** Because it is a security incident and a personal data breach that may need reporting.

**EX043.** Because it measures how long vulnerabilities remain open, which is the control's purpose.

**EX044.** A median of 21 days, with 10 of 15 (67%) within 30 days.

**EX045.** They affected the file server, which staff avoid restarting during working hours.

**EX046.** Identity, with single sign-on and multi-factor authentication.

**EX047.** A shared weakness, such as one administrator account controlling all layers.

**EX048.** The choice, its alternatives and the risks accepted.

**EX049.** Integrity checks, because the fingerprint changes if data change.

**EX050.** When shared outside the board portal.

**EX051.** Only one person administered the console holding them, so recovery could fail if they left.

**EX052.** What helps or hinders managers in completing the quarterly access review.

**EX053.** Because there are only twelve managers and the question asks why.

**EX054.** Only themes, not who said what.

**EX055.** Governance sets direction, risk management informs decisions and compliance confirms obligations are met.

**EX056.** Tenants' own devices, with reasons recorded.

**EX057.** Avoid, reduce, share and accept.

**EX058.** Risk assessments lacking cybersecurity information and an incident response protocol not updated since 2010.

**EX059.** Twice a year.

**EX060.** No one owned contractor offboarding between the repairs team and IT.

**EX061.** Responsible, accountable, consulted and informed.

**EX062.** Three people were marked accountable, which in practice means no one is.

**EX063.** One.

**EX064.** Access to personal data, criticality to services and remote access to systems.

**EX065.** The repairs contractor (5), cloud email (5) and the payroll bureau (4).

**EX066.** For example, security questions before contracts and breach notification clauses (also annual assurance review).

**EX067.** Misdirected tenant data, tied with the lost laptop at 12.

**EX068.** Ransomware, at 25 thousand.

**EX069.** Because the matrix compresses a very large impact into a maximum score of five.

**EX070.** Encryption and remote wipe.

**EX071.** Because Elmfield builds no software itself; supplier controls cover its housing system.

**EX072.** Because it would overload one person and leave controls unperformed when they are absent.

**EX073.** Nineteen of twenty.

**EX074.** The backup excluded files above a size limit.

**EX075.** That it did less than the description claimed, because of a forgotten configuration choice.

**EX076.** On evidence, such as a test result, rather than opinion.

**EX077.** Detect, at one of four outcomes (25%).

**EX078.** Fifteen of twenty-eight, 54%.

**EX079.** Re-performance, because it does not rely on the owner's records.

**EX080.** Accepting records that look complete but describe controls nobody performed.

**EX081.** Operated effectively, operated with exceptions, or failed.

**EX082.** To understand how the system allowed the error, not to punish the person.

**EX083.** For example, email auto-completed the wrong address and arrears spreadsheets were routinely emailed (also no external warning).

**EX084.** She raised the likelihood estimate for misdirected data and recorded the new controls.

**EX085.** Access reviews, risk register review and supplier checks.

**EX086.** Eighteen of twenty-four.

**EX087.** Because it gives the board nothing to govern or decide.

**EX088.** So the exercise is safe and nothing live is disrupted.

**EX089.** Nobody knew where the restore plan was stored.

**EX090.** The director.

**EX091.** It keeps card data off Elmfield's systems, greatly reducing its obligations, though some remain.

**EX092.** Operate the management system for a year and measure progress first.

**EX093.** Testing of how controls operated over a period.

**EX094.** Give legal advice; they should understand requirements and ask the right questions.

**EX095.** As protecting former staff from misuse of their accounts as well as protecting tenants.

**EX096.** Managed devices may work from anywhere; personal devices get email only.

**EX097.** Lists too long with jargon, managers not knowing staff needs and reviews arriving at busy times.

**EX098.** Awareness of how her own role at Elmfield might shape what managers said and what she noticed.

**EX099.** Because showing contrary views makes qualitative findings more honest and persuasive.

**EX100.** Corbridge uses a managed service provider; Elmfield has an in-house IT lead.

**EX101.** Because a higher count may reflect better reporting rather than worse security.

**EX102.** Weaker ownership, since staff assume the provider handles everything.

**EX103.** Shorter plain-language lists, a role guide, scheduling outside month-end and inclusion of the leaver list.

**EX104.** Because earlier reviews may already have removed most excess access.

**EX105.** Keeping the old process available as a fallback.

**EX106.** Individual accounts for each committee member.

**EX107.** Four of five.

**EX108.** To build the group's own capacity rather than create dependence on her.

**EX109.** Owner statements and questionnaires.

**EX110.** Better filtering or less reporting, not necessarily less phishing.

**EX111.** She limited it to the file share, since the supplier backs up the housing system.

**EX112.** Because questions show where the design is still unclear.

**EX113.** The permission called case escalation.

**EX114.** So results can be compared fairly with previous quarters.

**EX115.** From eight of twelve managers to eleven of twelve.

**EX116.** From fourteen days to six.

**EX117.** Because a quieter quarter and managers knowing they were studied could also explain it, with only twelve managers and one quarter.

**EX118.** Spears and Barki (2010).

**EX119.** By explaining her reflexive notes and the use of a second coder.

**EX120.** A pilot of the redesigned approach.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Schroeder, K., Trinh, H., & Pillitteri, V. (2024). *Measurement guide for information security: Volume 1 — Identifying and selecting measures* (NIST SP 800-55v1). <https://doi.org/10.6028/NIST.SP.800-55v1>
- U.S. Government Accountability Office. (2021). *Critical infrastructure protection: TSA is taking steps to address some pipeline security program weaknesses* (GAO-21-105263). <https://www.gao.gov/products/gao-21-105263>
