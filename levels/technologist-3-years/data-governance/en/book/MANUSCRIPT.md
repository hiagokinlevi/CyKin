# Data Governance: Technologist Course

- Language: English (`en`); course 072, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students who will build and run the checks, scripts, dictionaries and reports that make data governance work day to day.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs validate priority codes and date order in synthetic repair jobs, pseudonymise tenant identifiers with keyed hashes and measure emergency repairs completed within twenty-four hours for two synthetic contractors. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technologist student from files, SQL, Python and data formats through quality checks, source fixes, reference codes, dictionaries, lineage, access, pseudonymisation, privacy requests, retention and contractor data to dashboards, returns, incidents, automation, a placement and an applied project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Ravi Desai** | Technologist student | Invented |
| **Ms. Hannah Moreau** | Instructor | Invented |
| **Eastgate Institute of Technology** | Fictional institute | Invented |
| **Calder Valley Housing Association** | Fictional landlord, about 9,000 homes and 30,000 repair jobs a year | Invented |

### Core sources

DAMA-DMBOK2 (2017); ISO 8000-8:2015; Wang and Strong (1996); NIST SP 800-188; GDPR. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Starting at Eastgate

### Learning outcomes

You will (1) describe the technologist route and its case; (2) explain the applied focus of the course; (3) set up a working environment.

### 1.1 The student

Ravi Desai starts a three-year technologist diploma in data management at the fictional Eastgate Institute of Technology. His instructor, Ms. Hannah Moreau, explains that the course prepares technologists who build and run the tools, checks and reports that make data governance work day to day. Throughout the course, Ravi works with a fictional partner organisation, Calder Valley Housing Association, which owns about nine thousand homes and handles around thirty thousand repair jobs a year. All data used in labs are synthetic. Ravi is keen.

### 1.2 Applied focus

Ms. Moreau explains the difference between this course and a degree. Ravi will spend most of his time doing: writing queries, scripts and validation checks, building dashboards, maintaining dictionaries and supporting stewards. Theory appears where it helps practice. Each chapter has a practical task linked to Calder Valley. She notes that technologists are often the people who notice data problems first, so they need enough governance understanding to raise them with the right people and explain their effects clearly. Ravi welcomes the practical emphasis.

### 1.3 Working environment

Ravi sets up his environment: a Python installation using only the standard library, a text editor, a small SQLite database of synthetic Calder Valley data and a version control repository for his scripts. Ms. Moreau insists that every script be saved in the repository with a short description. She explains that this habit matters in practice, where scripts written for one-off checks often become essential processes that nobody can find or explain after their author leaves. Ravi writes his first repository description that afternoon.

### 1.4 Calder Valley's needs

Calder Valley's data manager, a fictional figure named Mrs. Okonjo, meets the class. She explains that the association must report repair performance to its regulator, respond to tenants' requests about their data and manage contractors who carry out most repairs. Data come from a housing management system, contractor portals and spreadsheets. She asks students to help with practical problems, starting with the quality of repair job records, which feed every performance report. The class agrees to begin with a survey of repair job fields and their uses.

### Worked example

Ravi begins the technologist diploma, learns its applied focus, sets up a standard-library Python environment with version control and meets Calder Valley's data manager, who describes repair reporting needs.

> **Synthetic case.** Eastgate, Calder Valley and all people are synthetic.

### Errors and limits

Scripts kept outside version control become unexplainable processes.

### Exercises

- **EX001 — Partner size.** How many homes does Calder Valley own? *Rubric:* 3 = about nine thousand;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Technologist role.** What do technologists build and run? *Rubric:* 3 = tools, checks and reports for governance;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX003 — First problem.** Which problem does Mrs. Okonjo ask students to start with? *Rubric:* 3 = quality of repair job records;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Data at a housing association

### Learning outcomes

You will (1) identify the main data sets in a housing association; (2) map how repair data flow; (3) recognise who depends on them.

### 2.1 Main data sets

Ravi lists Calder Valley's main data sets: properties with addresses, types and components such as boilers; tenants and tenancies; repair jobs with priority, dates and contractor; rent accounts; complaints; and safety inspections such as gas checks. Each is held in the housing management system, except contractor job updates, which arrive through a portal. He notes that properties link everything, because repairs, tenancies and inspections all refer to a property identifier. Ravi records each data set in a simple list with its system, its owner if known and the property link.

### 2.2 Following a repair

Ravi traces a repair. A tenant reports a leak by phone. A call handler creates a job with a priority code and assigns a contractor. The contractor attends, updates the portal with completion details and the portal sends data back to the housing system each night. Reports draw on completed jobs. He finds three handoffs where data are typed or transferred, each a point where errors can enter, and marks them on a diagram. Mrs. Okonjo confirms that his diagram matches how repairs actually work.

### 2.3 Who depends on repair data

Many people rely on repair data: tenants waiting for repairs, call handlers answering queries, managers monitoring contractors, finance paying invoices and the regulator assessing performance. Ravi notes that an error in a completion date can make a late repair look on time, misleading the regulator, or make an on-time repair look late, leading to an unfair penalty for a contractor. Understanding dependents explains why quality matters beyond the data team. Ravi adds each group of dependents to his diagram, so the effect of errors at each handoff can be seen at a glance.

### 2.4 Safety data

Some data affect tenant safety directly. Gas safety checks must be carried out every year, and records must show when each check happened. Ms. Moreau stresses that errors in such data are serious: a missing record might mean a check was missed. Ravi learns that data supporting legal safety duties need the strictest controls, and that technologists should flag any doubt about such records immediately rather than waiting for routine reports. Ravi notes that the gas check records are owned by the compliance manager, who must be told of any doubt.

### Worked example

Ravi lists Calder Valley's data sets with property as the link, traces a repair through three handoffs, identifies dependents from tenants to the regulator and learns that safety data need the strictest controls.

> **Synthetic case.** Data sets are synthetic.

### Errors and limits

Treating safety records like routine data delays urgent action.

### Exercises

- **EX004 — Linking entity.** What links most data sets? *Rubric:* 3 = the property identifier;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX005 — Handoff count.** How many handoffs did Ravi find in a repair? *Rubric:* 3 = three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX006 — Gas check frequency.** How often must gas checks happen? *Rubric:* 3 = every year;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Spreadsheet and file hygiene

### Learning outcomes

You will (1) organise shared files; (2) apply naming and versioning conventions; (3) reduce risks in spreadsheet processes.

### 3.1 Shared drives

Calder Valley's shared drive contains thousands of files with names such as final, final2 and use this one. Ravi surveys one folder and finds four versions of the contractor rates list, with no way to tell which is current. He proposes a structure with folders by function, a naming convention including date and version and an archive folder for old versions. Owners for each top-level folder approve the structure and agree to keep it tidy. The archive keeps old versions available without confusing current users.

### 3.2 Naming conventions

Ravi's convention uses the date in year-month-day order, a short subject and a version number, such as 2026-02-14 contractor rates v3. Dates in that order sort correctly. He explains that conventions only work if everyone follows them, so he writes a one-page guide with examples and asks team leaders to remind staff. After a month, he checks a sample of new files and finds most follow the convention. The few files that do not follow it are renamed by their owners after a friendly reminder from their team leaders, and the sample is repeated a month later.

### 3.3 Spreadsheet risks

The repair performance spreadsheet copies data from a housing system export, applies formulas and produces figures for managers. Ravi finds a formula referencing a fixed row range that misses new rows and a manual adjustment cell without any note. He adds a check comparing row counts with the export, protects formula cells and adds a notes column explaining manual adjustments. He also records who prepares the spreadsheet each month. The monthly preparer now signs a short checklist confirming that the row count check passed before the figures are sent to managers.

### 3.4 Personal data in files

Ravi searches the shared drive for files containing tenant names and phone numbers. He finds several old call lists in folders accessible to all staff. He reports them to Mrs. Okonjo, who has owners review and delete unnecessary files and move the rest to restricted folders. Ms. Moreau explains that unmanaged files are a common source of data breaches and over-retention, and that technologists can find them with simple searches. The search is repeated every quarter, and the number of exposed files falls steadily as owners clean up.

### Worked example

Ravi reorganises a shared folder with four rate list versions, writes a dated naming convention guide, adds row count checks to a spreadsheet and finds old tenant call lists in open folders.

> **Synthetic case.** Files are synthetic.

### Errors and limits

Conventions without guidance and checks are ignored.

### Exercises

- **EX007 — Rate list versions.** How many versions of the rate list did Ravi find? *Rubric:* 3 = four;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX008 — Date order.** Why use year-month-day dates? *Rubric:* 3 = they sort correctly;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX009 — Call lists.** What did Ravi find in open folders? *Rubric:* 3 = old call lists with tenant names and phone numbers;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — SQL for governance checks

### Learning outcomes

You will (1) write SQL queries to check data; (2) find orphans and duplicates; (3) save queries as reusable checks.

### 4.1 Basic queries

Using SQLite, Ravi writes queries against synthetic Calder Valley tables. He counts jobs by priority, finds jobs with missing contractors and lists properties without a recorded gas check in the past year. Each query answers one governance question. Ms. Moreau asks him to write the question as a comment above each query, so others understand its purpose. He notes that SQL is often the quickest way to answer quality questions in systems built on relational databases. The comments make his queries easy to review.

### 4.2 Orphans

An orphan is a record referring to something that does not exist, such as a job referring to a property identifier not in the property table. Ravi uses a left join to find jobs whose property is missing. He finds a handful, created when properties were sold and removed from the system while open jobs remained. He reports them to the repairs steward, who closes the jobs and asks IT to prevent property deletion while jobs are open. IT applies the restriction within a month.

### 4.3 Duplicates

Ravi looks for duplicate jobs: the same property, the same problem description and dates within two days. He uses a self-join and finds pairs where tenants reported a problem twice and call handlers created two jobs. Duplicates inflate job counts and may send two contractors. He shares examples with the call centre manager, who adds a step to check for open jobs at the property before creating a new one. The number of duplicate jobs falls in the following month, and contractors report fewer wasted visits to properties.

### 4.4 Reusable checks

Ravi saves useful queries in the repository with a name, purpose, owner and expected result. He builds a small Python script using sqlite3 that runs all saved checks and writes results to a table with the date. Ms. Moreau notes that turning queries into a check library makes them repeatable and reviewable, and that this is how many organisations build their first data quality monitoring before buying any specialised tool. The steward reviews the results table each morning and raises an issue when a check result changes unexpectedly.

### Worked example

Ravi writes commented SQL checks, finds orphan jobs from sold properties, finds duplicate jobs from repeat reports and builds a script that runs saved checks and records results.

> **Synthetic case.** Tables are synthetic.

### Errors and limits

Uncommented queries lose their purpose; state the question.

### Exercises

- **EX010 — Orphan cause.** Why did orphan jobs exist? *Rubric:* 3 = properties sold and removed with open jobs;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX011 — Duplicate rule.** How did Ravi define a duplicate job? *Rubric:* 3 = same property and problem within two days;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX012 — Call centre fix.** What step did the call centre add? *Rubric:* 3 = check for open jobs at the property first;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Python scripting basics

### Learning outcomes

You will (1) write Python scripts for data tasks; (2) handle files and errors; (3) structure scripts for reuse.

### 5.1 First scripts

Ravi writes Python scripts that read contractor portal exports in CSV format using the csv module, count rows and summarise jobs by status. He uses functions for each step: reading, checking and summarising. Ms. Moreau reviews his code and asks for clearer names, such as count_jobs_by_status instead of f2. She explains that clear names make scripts readable months later, when the author has forgotten details and a colleague needs to understand them quickly. Ravi renames every function in his scripts that week.

### 5.2 Handling errors

Contractor exports sometimes arrive with missing columns or extra blank lines. Ravi's first script crashes on such files. He adds checks that confirm expected columns are present and skip blank lines, with clear messages explaining any problem. When a column is missing, the script stops and reports which one, rather than producing wrong results silently. He learns that stopping loudly is better than continuing quietly with bad data. He adds a small set of broken test files to his repository so that these behaviours can be checked whenever the script changes.

### 5.3 Dates and numbers

Repair data contain dates in several formats, because contractors use different systems. Ravi uses the datetime module to parse each expected format and records any value that matches none. He also converts costs from text to numbers carefully, handling currency symbols and commas. He finds that one contractor uses day-month order while another uses month-day, which had caused completion dates to be misread in earlier reports. Ravi reports this to the steward, who asks both contractors to confirm their formats, and earlier reports are corrected with a note explaining the change.

### 5.4 Structure for reuse

Ravi organises his scripts into a module with shared functions for reading files, parsing dates and writing results, and separate small scripts for each task. He writes simple tests for the date parser using examples from each contractor. Ms. Moreau notes that reusable functions mean a fix, such as a new date format, needs making in one place, reducing the chance that different scripts treat the same data differently. When a third contractor joins later, Ravi adds its date format to the shared parser and every script handles it correctly at once.

### Worked example

Ravi writes function-based scripts with clear names, stops loudly on missing columns, finds day-month and month-day date confusion between contractors and organises shared functions with tests.

> **Synthetic case.** Exports are synthetic.

### Errors and limits

Scripts that continue quietly on bad input produce wrong results.

### Exercises

- **EX013 — Naming advice.** What naming advice did Ms. Moreau give? *Rubric:* 3 = use descriptive names like count_jobs_by_status;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Missing column behaviour.** What does the script do when a column is missing? *Rubric:* 3 = stops and reports which one;; 2 = partly correct;; 1 = continues;; 0 = none.
- **EX015 — Date confusion.** What date problem did Ravi find? *Rubric:* 3 = contractors used day-month and month-day order;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Data formats and exchange

### Learning outcomes

You will (1) compare common data formats; (2) define exchange specifications; (3) validate incoming files.

### 6.1 Common formats

Ravi compares formats used at Calder Valley: CSV for contractor exports, JSON from the tenant portal, fixed-width files from the old rent system and spreadsheets from managers. CSV is simple but has no types; JSON carries structure but can vary between records; fixed-width files need exact column positions. He uses Python's csv and json modules to read each, noting the specific problems each format tends to create. He writes a short note for each format describing its typical problems and how his scripts handle them, so that colleagues can reuse the approach.

### 6.2 Exchange specifications

To reduce problems, Ravi helps write an exchange specification for contractor files: file name pattern, encoding, delimiter, column names and order, data types, date format in year-month-day order, allowed values for status and priority and what to do when a job is cancelled. The repairs steward approves it and sends it to all contractors. He notes that a specification turns assumptions into agreements, making it possible to reject files that do not comply. The specification is published with an example file that contractors can test against.

### 6.3 Validating files

Ravi writes a validator that checks each incoming contractor file against the specification before loading it. Files passing all checks load automatically; files failing are held and the contractor is emailed a report listing problems. In the first month, two contractors send non-compliant files, both fixed within days. He notes that automated validation shifts the burden of fixing errors to the source, where they can be fixed properly. Contractors begin to test their files against the specification before sending them, and held files become rare after the first two months.

### 6.4 Version changes

When a contractor upgrades its system, a new column appears. The validator holds the file. Ravi checks with the steward, who agrees the column is harmless and updates the specification to version two, allowing an optional extra column. Ms. Moreau notes that specifications need version control like code, so everyone knows which version applies and changes are deliberate rather than accidental, with a record of who approved each change. The specification history is kept in the repository next to the validator code, so each version can be matched to the validator that enforced it.

### Worked example

Ravi compares CSV, JSON, fixed-width and spreadsheet formats, helps write a contractor exchange specification, builds a validator that holds non-compliant files and manages a specification version change.

> **Synthetic case.** Files and specifications are synthetic.

### Errors and limits

Accepting files without validation moves source errors into reports.

### Exercises

- **EX016 — CSV weakness.** What is CSV's main weakness? *Rubric:* 3 = no data types;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX017 — Failed file handling.** What happens to files failing validation? *Rubric:* 3 = held and contractor emailed a report;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX018 — Version two change.** What did version two of the specification allow? *Rubric:* 3 = an optional extra column;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Data quality concepts

### Learning outcomes

You will (1) apply quality dimensions to repair data; (2) choose measures for each; (3) relate quality to uses.

### 7.1 Dimensions

Ms. Moreau introduces quality dimensions from Wang and Strong's research: accuracy, completeness, consistency, timeliness and validity, among others. Ravi applies them to repair jobs. Completeness means jobs have priority, dates and contractor. Validity means codes and dates follow rules. Accuracy means completion dates reflect when work actually finished. Timeliness means updates arrive soon after work. Consistency means the housing system and contractor portal agree about the same job. Ravi writes a short example of a failure for each dimension using Calder Valley's repair jobs, which helps classmates and stewards understand them quickly.

### 7.2 Measures

For each dimension Ravi writes a measure. Completeness is the share of jobs with all required fields. Validity is the share passing code and date rules. Consistency is the share of jobs where status matches between systems. Timeliness is the share of completions updated within one day. Accuracy is checked by sampling jobs and comparing completion dates with tenant confirmations. He records each measure with its formula so results can be reproduced. The steward reviews the formulas and agrees the targets for each measure.

### 7.3 Quality and use

Ravi learns that quality depends on use. For paying contractors, cost accuracy matters most. For regulator reports, completion dates and priorities matter most. For tenant communication, contact details matter most. He builds a table linking uses to the dimensions they depend on, which helps Mrs. Okonjo explain to managers why some quality problems need urgent attention while others can wait. ISO 8000-8 supports stating how each quality claim was measured. Mrs. Okonjo uses the table in her next meeting with managers, who agree to prioritise completion date accuracy for the coming quarter.

### 7.4 Quality as a habit

Ms. Moreau explains that quality is not a project with an end date but a habit built into daily work. Technologists support this by running checks automatically, making results visible and helping people fix causes. Ravi notes in his journal that the best quality improvements he has seen so far came from small process changes at the source, such as the call centre checking for open jobs, rather than large clean-up exercises. Ms. Moreau asks the class to collect such examples throughout the course.

### Worked example

Ravi applies quality dimensions to repair jobs, writes a formula for each, links uses to the dimensions they depend on and notes that small source changes improve quality most.

> **Synthetic case.** Measures are synthetic; Wang and Strong (1996) and ISO 8000-8:2015 are real.

### Errors and limits

One quality score for all uses hides what matters for each.

### Exercises

- **EX019 — Consistency measure.** How is consistency measured? *Rubric:* 3 = share of jobs with matching status between systems;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Regulator focus.** Which dimensions matter for regulator reports? *Rubric:* 3 = completion dates and priorities;; 2 = both;; 1 = one;; 0 = none.
- **EX021 — Best improvements.** Where did the best improvements come from? *Rubric:* 3 = small process changes at the source;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Validating repair jobs

### Learning outcomes

You will (1) validate job records against two rules; (2) combine rule results; (3) report findings to the steward.

### 8.1 The rules

Ravi validates repair jobs with two rules agreed with the repairs steward. The priority code must be one of E for emergency, U for urgent, R for routine or P for planned. The completion date must not be earlier than the date the job was raised. Both rules matter for regulatory reporting, because priority determines the target time and dates determine whether the target was met. He writes each rule as a small function with a clear name. The steward approves both functions.

### Lab — Priority code and date order checks on 6,000 synthetic repair jobs

```python
"""Validate 6,000 synthetic repair job records: priority code and date order (stdlib only)."""
import random, datetime as dt
random.seed(21)
codes = ["E", "U", "R", "P"]
bad_code = bad_date = both = 0
for i in range(6000):
    c = random.choice(codes) if random.random() > 0.03 else random.choice(["", "X", "e"])
    raised = dt.date(2026, 1, 1) + dt.timedelta(days=random.randint(0, 180))
    done = raised + dt.timedelta(days=random.randint(0, 30) if random.random() > 0.02 else -random.randint(1, 10))
    bc, bd = c not in codes, done < raised
    bad_code += bc; bad_date += bd; both += bc and bd
print(f"jobs 6000; invalid priority {bad_code}; completed before raised {bad_date}; both {both}")
print(f"valid on both rules {6000 - bad_code - bad_date + both} ({100*(6000 - bad_code - bad_date + both)/6000:.1f}%)")
```

Run with `python3 lab_jobs.py`. Verified output:

```text
jobs 6000; invalid priority 167; completed before raised 122; both 8
valid on both rules 5719 (95.3%)
```

### 8.2 Results

The lab checks six thousand synthetic jobs. One hundred and sixty-seven have an invalid priority, such as a blank, an unknown letter or a lowercase e. One hundred and twenty-two were completed before they were raised. Eight fail both rules. In total, 5,719 jobs, 95.3 percent, pass both rules. Ravi notes that jobs failing both rules are counted once in the total, which is why the failures do not simply add up. Ravi presents the results in a small table with the combined figure shown first, followed by each rule's failure count.

### 8.3 Causes

Ravi samples failing jobs and discusses them with the steward. Lowercase e comes from a contractor portal that does not convert case. Blanks come from jobs created in a hurry during storms. Completion before raising usually means a call handler created the job after the contractor had already fixed an emergency, entering the raised date as the call date. Each cause suggests a different fix, from case conversion to clearer guidance for emergencies. Ravi records each cause with an example job number in his notes.

### 8.4 Reporting

Ravi reports to the steward with counts, the combined pass rate, examples with tenant details removed, likely causes and suggested fixes. The steward accepts the case conversion fix and asks call handlers to record the original report time for emergencies. Ravi adds both rules to the check library to run nightly. Ms. Moreau notes that reporting causes alongside counts helps the steward act rather than simply worry about a number. The steward presents Ravi's report at the monthly repairs meeting, where managers agree to monitor the pass rate each month from then on.

### Worked example

Ravi validates 6,000 jobs, finding 167 invalid priorities, 122 completed before raised and 8 both, with 5,719 (95.3 percent) valid, traces causes and adds the rules to nightly checks.

> **Synthetic case.** Jobs are synthetic; outputs come from lab_jobs.py.

### Errors and limits

Adding failure counts double-counts records failing several rules.

### Exercises

- **EX022 — Valid share.** What share of jobs pass both rules? *Rubric:* 3 = 95.3% (5,719);; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Lowercase cause.** Where does lowercase e come from? *Rubric:* 3 = a portal that does not convert case;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX024 — Date cause.** Why were some jobs completed before being raised? *Rubric:* 3 = emergency jobs created after the fix;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Fixing problems at the source

### Learning outcomes

You will (1) distinguish source fixes from downstream cleaning; (2) implement source controls; (3) measure the effect.

### 9.1 Cleaning versus fixing

Ravi could correct invalid priorities each night with a script, converting lowercase letters and guessing blanks. Ms. Moreau asks what would happen next month: the same errors would arrive again, and guesses might be wrong. She explains that cleaning downstream treats symptoms, while fixing at the source prevents errors. Cleaning may be needed temporarily, but it should be paired with a source fix and recorded so that reports can show what was changed. Ravi agrees to pursue source fixes first, with temporary cleaning recorded.

### 9.2 Source controls

Ravi works with the contractor portal team to convert priority codes to uppercase and reject blanks before submission. In the housing system, call handlers now select priority from a drop-down rather than typing. For emergencies, a new field records the time the tenant first reported the problem, so jobs created later keep a correct raised time. Each change is tested with synthetic jobs before release to confirm it behaves as intended. The portal team and IT release the changes together after the tests pass, with the steward's approval.

### 9.3 Measuring effect

After the changes, Ravi reruns the validation on a new month of synthetic jobs designed to match the new process. Invalid priorities fall sharply, and completion-before-raised errors fall as call handlers use the new field. He reports the before-and-after comparison to the steward, noting that the new month's synthetic data reflect his assumptions about the changes and that real monitoring will confirm whether the improvement holds. He schedules a check on real monitoring results three months after the changes, with the steward responsible for reviewing them and reporting to the repairs manager.

### 9.4 Remaining cleaning

Some old records still contain errors. Ravi and the steward decide to correct historical priorities where the correct value can be confirmed from job descriptions, marking each correction with a reason code, and to leave others flagged as unknown. He notes that corrections must be traceable, so that anyone reviewing past reports can see which values were changed, when and why, and that guessing silently would damage trust in reports. The flagged records are listed in a separate report, so managers know which past figures carry uncertainty.

### Worked example

Ravi chooses source fixes over nightly cleaning, adds uppercase conversion, blank rejection, drop-downs and a first-report time field, measures the effect and corrects old records only with traceable reason codes.

> **Synthetic case.** Changes are synthetic.

### Errors and limits

Silent downstream corrections hide recurring source errors.

### Exercises

- **EX025 — Cleaning problem.** Why is nightly cleaning not enough? *Rubric:* 3 = the same errors recur and guesses may be wrong;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX026 — Emergency field.** What new field supports emergency jobs? *Rubric:* 3 = time the tenant first reported the problem;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX027 — Historical corrections.** How are historical corrections marked? *Rubric:* 3 = with a reason code;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Reference codes and lookups

### Learning outcomes

You will (1) manage reference code lists; (2) keep lookups consistent across systems; (3) handle code changes over time.

### 10.1 Code lists

Calder Valley uses many code lists: priorities, job types, property types, contractor identifiers and complaint categories. Ravi finds job type lists differ between the housing system and the contractor portal, with some codes in one but not the other. He creates a master list in a reference table, owned by the repairs steward, and a mapping table linking portal codes to master codes. Unmapped codes are flagged when files load. The steward approves the master list and the mapping after checking each code with the call centre and contractors.

### 10.2 Consistency

Ravi writes a nightly check comparing code lists in each system with the master list. Differences appear in a short report to the steward. When a new job type is needed, the steward adds it to the master list first, then IT and the portal team add it to their systems. He notes that this order prevents systems drifting apart, which had caused reports to drop jobs with codes not recognised by the reporting tool. The report is usually empty, which shows the process works.

### 10.3 Changes over time

Codes change. Calder Valley merges two job types, plaster repair and wall repair, into one. Ravi adds start and end dates to the master list, so historical reports still show the old types for past periods while new jobs use the merged code. He creates a mapping for trend reports that need consistent categories across time. He explains that deleting old codes would break historical reports. The steward approves the end dates and the mapping, and Ravi tests the trend reports to confirm that past periods still show the expected categories.

### 10.4 Documentation

Each code has a description, examples and the date it became valid. Ravi publishes the master list on the intranet so call handlers can check meanings. A call handler notices that two codes have nearly identical descriptions and asks which to use. The steward clarifies the difference and updates descriptions. Ms. Moreau notes that publishing code lists invites useful questions, which improves consistency more than keeping lists hidden in system tables. Call handlers now consult the published list regularly, and the number of jobs recorded under the wrong type falls.

### Worked example

Ravi creates a master job type list with portal mappings, runs nightly consistency checks, adds start and end dates for a merged code and publishes descriptions that prompt a useful clarification.

> **Synthetic case.** Code lists are synthetic.

### Errors and limits

Deleting old codes breaks historical reports; end-date them.

### Exercises

- **EX028 — Master list owner.** Who owns the master job type list? *Rubric:* 3 = the repairs steward;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Change order.** What order is followed for new job types? *Rubric:* 3 = master list first, then systems;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX030 — Merged types.** Which job types were merged? *Rubric:* 3 = plaster repair and wall repair;; 2 = both;; 1 = one;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Tenant records and duplicates

### Learning outcomes

You will (1) find duplicate tenant records; (2) apply matching rules with review; (3) prevent new duplicates.

### 11.1 Why duplicates appear

Tenant records duplicate when someone moves between Calder Valley homes and a new record is created instead of updating the old one, or when names are spelled differently by different staff. Ravi finds tenants with two records, each holding part of their history. Duplicates cause repeated letters, split rent accounts and incomplete records when tenants request their data. He explains that duplicates matter both for service quality and for meeting legal duties. Ravi counts the likely duplicates in the synthetic data before proposing any rules.

### 11.2 Matching rules

Ravi writes matching rules: exact match on date of birth plus a similar surname and first initial, or exact match on national insurance number where recorded. He normalises names by removing spaces and converting to lowercase before comparing. Matches are classified as certain or possible. Certain matches go to the tenancy steward for quick confirmation; possible matches need careful review, because merging two different people would mix their personal data and rent accounts. The tenancy steward approves the rules after testing them on known cases.

### 11.3 Review and merging

The steward reviews possible matches using additional information such as previous addresses. Confirmed duplicates are merged in the housing system following a documented procedure that keeps the history from both records and records who merged them. Ravi tracks the number reviewed, confirmed and rejected. About a fifth of possible matches turn out to be different people, such as relatives with similar names, which justifies the manual review step for that group. Ravi reports these figures to the steward each month so the rules can be tuned if needed.

### 11.4 Prevention

To prevent new duplicates, Ravi suggests that staff search for existing tenants by date of birth and surname before creating a record, with the housing system showing likely matches. The system supplier configures this. He also adds a monthly duplicate check to the library. Ms. Moreau notes that prevention again proves cheaper than repeated clean-ups, and that matching rules should be reviewed whenever duplicates slip through, since every miss reveals a gap in the rules. The supplier's change goes live within two months.

### Worked example

Ravi explains why tenant duplicates appear, writes normalised matching rules with certain and possible classes, has the steward review merges and finds a fifth of possible matches are different people, and adds search-before-create prevention.

> **Synthetic case.** Records are synthetic.

### Errors and limits

Merging without review can combine different people's data.

### Exercises

- **EX031 — Duplicate effects.** Name one effect of tenant duplicates. *Rubric:* 3 = repeated letters, split rent accounts or incomplete data requests;; 2 = one;; 1 = vague;; 0 = none.
- **EX032 — Normalisation steps.** How are names normalised? *Rubric:* 3 = remove spaces and lowercase;; 2 = both;; 1 = one;; 0 = none.
- **EX033 — Rejected share.** What share of possible matches were different people? *Rubric:* 3 = about a fifth;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Metadata and data dictionaries

### Learning outcomes

You will (1) build a data dictionary; (2) keep it current; (3) use it to answer questions.

### 12.1 Building a dictionary

Ravi builds a data dictionary for the repair jobs table. For each field he records the name, plain-language meaning, data type, allowed values or format, whether it is required, the source and the owner. He gathers meanings from the steward and system documentation. Some fields have no documented meaning; he asks staff who use them and records their answers, flagging any where answers differ, such as two meanings for a field named completed flag. The steward reviews each entry before it is published.

### 12.2 Resolving meanings

The completed flag is set by contractors when work is finished, but call handlers believe it means the tenant has confirmed satisfaction. Reports counting completed jobs mix both interpretations. Ravi brings the question to the steward, who confirms the contractor meaning and asks IT to add a separate field for tenant confirmation. The dictionary records the decision. He notes that dictionaries surface ambiguity that otherwise causes silent errors in reports. Reports are updated to use the contractor meaning, and the new field is added to the dictionary when created.

### 12.3 Keeping it current

Ravi links the dictionary to the database schema with a script that lists fields in the database and compares them with dictionary entries, flagging fields missing from the dictionary and entries for fields that no longer exist. The script runs weekly. When IT adds a field, the report prompts the steward to document it. He explains that automated comparison prevents dictionaries from drifting out of date, a common reason they are ignored. The steward documents new fields within a week of each report, and missing entries become rare.

### 12.4 Using the dictionary

Analysts, call handlers and auditors begin using the dictionary to answer questions. When the regulator asks how Calder Valley defines a completed emergency repair, Mrs. Okonjo answers from the dictionary within minutes. Ravi adds a page explaining how to read entries. Ms. Moreau notes that metadata proves its value when people can answer real questions quickly, and that this practical benefit is what keeps owners willing to maintain it. The regulator's reviewer later notes the clarity of the answer, which encourages owners to keep entries up to date.

### Worked example

Ravi builds a repair jobs dictionary, resolves conflicting meanings of the completed flag, automates comparison with the schema and sees the dictionary answer a regulator question quickly.

> **Synthetic case.** The dictionary is synthetic.

### Errors and limits

Dictionaries without automated checks drift and lose trust.

### Exercises

- **EX034 — Completed flag meanings.** What two meanings did the completed flag have? *Rubric:* 3 = contractor finished work versus tenant satisfaction;; 2 = both;; 1 = one;; 0 = none.
- **EX035 — Drift check.** How does Ravi keep the dictionary current? *Rubric:* 3 = a weekly script comparing schema and entries;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX036 — Regulator answer.** What did the dictionary help answer? *Rubric:* 3 = the definition of a completed emergency repair;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Lineage for reports

### Learning outcomes

You will (1) trace report figures back to sources; (2) document transformations; (3) use lineage to investigate discrepancies.

### 13.1 Tracing a figure

The monthly report shows the percentage of emergency repairs completed within twenty-four hours. Ravi traces it: the report reads a summary table, which is built by a script from the jobs table, which receives contractor updates from the portal and call handler entries. He records each step, including filters and calculations, in a lineage note. He finds that the script excludes cancelled jobs, which is correct, but also excludes jobs without a completion time, which is not documented. He reports this to the steward.

### 13.2 Transformations

Ravi documents each transformation: which records are included, how times are calculated and what happens to missing values. He finds that the calculation uses the date only, not the time, so a job raised at eleven at night and completed at nine the next morning appears as one day, while a job raised at one in the morning and completed at eleven at night the same day appears as zero days. He recommends using full timestamps. The steward agrees, and the script is changed after testing.

### 13.3 Investigating discrepancies

The repairs manager's own spreadsheet shows a different emergency figure from the report. Using lineage, Ravi compares steps and finds that the spreadsheet includes jobs without completion times as late, while the report excludes them. Neither approach is documented. The steward decides that jobs without completion times should be reported separately as unknown. Both the report and spreadsheet are updated to match, ending months of disagreement. Ravi records the agreed approach in the lineage note, and the repairs manager retires his spreadsheet in favour of the corrected report a month later.

### 13.4 Keeping lineage

Ravi stores lineage notes next to each report in the repository and adds a rule that changes to report scripts must update the notes. He also adds a short lineage summary to each report's footer. Ms. Moreau explains that lineage helps people trust figures and resolve disagreements quickly, and that technologists are well placed to maintain it because they understand both the scripts and the business questions behind them. Report readers begin to consult the footer when figures surprise them, which reduces the number of questions sent to the data team.

### Worked example

Ravi traces the emergency repair figure, finds undocumented exclusion of missing completion times and date-only calculations, resolves a disagreement with the manager's spreadsheet and stores lineage notes with each report.

> **Synthetic case.** Reports are synthetic.

### Errors and limits

Date-only calculations distort time-based targets.

### Exercises

- **EX037 — Undocumented exclusion.** What was excluded without documentation? *Rubric:* 3 = jobs without a completion time;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Timestamp issue.** Why should full timestamps be used? *Rubric:* 3 = date-only calculations misstate elapsed time;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX039 — Unknown handling.** How are jobs without completion times reported now? *Rubric:* 3 = separately as unknown;; 2 = partly correct;; 1 = late;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Roles in practice

### Learning outcomes

You will (1) describe how technologists support owners and stewards; (2) handle requests that need decisions; (3) work within agreed authority.

### 14.1 The technologist's role

Ravi learns where technologists fit. Owners such as the head of repairs decide policies and priorities for their data. Stewards maintain definitions, rules and issues. Technologists build checks, scripts, dictionaries and reports, and raise problems. Ms. Moreau explains that technologists should not make policy decisions themselves, even when they have the technical ability, because decisions about data meaning and use belong to those accountable for the business outcome. Ravi writes this distinction at the front of his journal, because he expects to be asked to make such decisions in his placement.

### 14.2 Requests needing decisions

A manager asks Ravi to change the emergency report to exclude jobs where tenants were not home, which would improve the figure. Ravi recognises that this changes the meaning of a regulated measure. He explains that he cannot make the change without the steward's and owner's agreement and refers the request. The owner checks the regulator's guidance, which does not allow the exclusion, and declines. Ravi records the request and decision. The manager accepts the decision once he sees the regulator's guidance.

### 14.3 Working with stewards

Ravi meets the repairs steward weekly to review check results, new issues and planned changes. He prepares short summaries with examples. The steward decides priorities, and Ravi carries out technical work. When the steward is on leave, decisions wait for the deputy rather than being made by Ravi. He notes that clear authority makes his work easier, because he does not have to defend decisions he did not make. The weekly meeting rarely takes more than half an hour, which suits both of them.

### 14.4 Raising concerns

Ravi notices that gas safety records for some properties show checks completed on dates when the contractor's portal shows no visit. He raises this immediately with the compliance steward, providing examples, rather than waiting for the weekly meeting, because safety data are involved. The steward investigates and finds data entry errors rather than missed checks. Ms. Moreau praises Ravi for escalating promptly and for presenting evidence rather than accusations. The steward arranges correction of the records and adds a check comparing gas records with portal visits.

### Worked example

Ravi learns that technologists build and raise but do not decide policy, refers a request to exclude no-access jobs that the owner declines, works weekly with the steward and escalates a gas record concern promptly.

> **Synthetic case.** Roles and events are synthetic.

### Errors and limits

Technologists making policy changes alone bypass accountability.

### Exercises

- **EX040 — Declined request.** What change did the owner decline? *Rubric:* 3 = excluding no-access jobs from the emergency report;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX041 — Leave cover.** Who decides when the steward is on leave? *Rubric:* 3 = the deputy;; 2 = partly correct;; 1 = technologist;; 0 = none.
- **EX042 — Gas finding.** What did the gas record investigation find? *Rubric:* 3 = data entry errors, not missed checks;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Policies and procedures

### Learning outcomes

You will (1) read and apply data policies; (2) write clear procedures; (3) test procedures with users.

### 15.1 Reading policies

Calder Valley has a data policy setting principles: data have owners, quality is measured, personal data are protected and retention follows the schedule. Ravi reads it and lists what it requires of technologists, such as logging access to tenant data in scripts and following the retention schedule in extracts. He notes that policies are written broadly, so technologists must translate them into specific technical practices and check with stewards when unsure. He shares his list with the steward, who confirms each item.

### 15.2 Writing procedures

Ravi writes a procedure for loading contractor files: receive the file, run the validator, load if valid, hold and notify if not, record the outcome. Each step names who does it and what to do if something goes wrong. He uses numbered steps and plain words. Ms. Moreau reviews it and asks him to add what happens if the validator itself fails, which he had not considered. He adds a step telling staff to contact the data team and hold all files until the validator is fixed and tested.

### 15.3 Testing with users

Ravi asks a colleague who has never loaded contractor files to follow the procedure. She gets stuck at step four, because it assumes knowledge of where held files are stored. Ravi adds the folder location and a screenshot description. A second colleague completes the procedure without help. He learns that procedures written by experts often skip steps that seem obvious to them, and that testing with newcomers reveals these gaps. The procedure is then published on the intranet with a version number and a date of approval.

### 15.4 Keeping procedures current

Ravi adds a review date and owner to each procedure and stores them on the intranet. When the validator changes, he updates the procedure and notes the version. He also suggests that staff report problems with procedures through the issue log. Ms. Moreau notes that procedures are living documents, and that outdated procedures can be more harmful than none, because staff follow them confidently into errors. The first problems reported through the issue log lead to two small corrections within a month, which shows that the channel works.

### Worked example

Ravi translates the policy into technical practices, writes a contractor file procedure including validator failure, tests it with a newcomer who gets stuck and keeps procedures current with owners and review dates.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Procedures written by experts skip steps newcomers need.

### Exercises

- **EX043 — Missing case.** What case did Ms. Moreau ask Ravi to add? *Rubric:* 3 = what happens if the validator fails;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Stuck step.** Where did the tester get stuck? *Rubric:* 3 = step four, held file location;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX045 — Outdated risk.** Why can outdated procedures be harmful? *Rubric:* 3 = staff follow them confidently into errors;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Access control in practice

### Learning outcomes

You will (1) implement role-based access for data; (2) run access reviews; (3) log access to sensitive data.

### 16.1 Roles and permissions

Ravi helps implement role-based access in Calder Valley's reporting database. Roles include repairs analyst, call handler, finance officer and data team. Each role has permissions to specific tables or views. Repairs analysts see jobs and properties but tenant names only through a view that masks them. The tenancy owner approves which roles see tenant details. Ravi documents each role in the dictionary and creates views rather than granting access to raw tables. The views are tested by each role before access is switched on.

### 16.2 Access reviews

Every quarter, Ravi produces a list of accounts with their roles and last login for each owner to review. Owners confirm, change or remove access. In the first review, the tenancy owner removes access for staff who moved departments and an external consultant whose contract ended. Ravi records the review and changes. He notes that reviews are only effective if owners actually examine lists rather than approving them automatically, so he highlights unusual entries. The tenancy owner thanks Ravi for the highlights.

### 16.3 Logging

For tables with tenant details, Ravi turns on logging of queries, recording who accessed what and when. Logs are kept for a year and reviewed monthly for unusual patterns, such as large exports or access outside working hours. He writes a simple script that summarises logs for the data protection officer. He explains that logs deter misuse and allow investigation, and that reviewing them regularly is what turns logging into a control. The first monthly summary shows no unusual patterns, which reassures the officer.

### 16.4 Least privilege

Ravi learns the principle of least privilege: people should have the minimum access needed for their work. A finance officer asks for full access to the jobs table to reconcile invoices. Ravi checks with the repairs owner, who approves a view containing job identifiers, contractors and costs without tenant details. The finance officer can do the reconciliation. Ms. Moreau notes that tailored views often satisfy requests without granting broad access. Ravi adds the finance view to the dictionary, so that similar requests can be handled quickly in future.

### Worked example

Ravi implements roles with masked views, runs quarterly owner reviews that remove stale access, logs and summarises access to tenant data and satisfies a finance request with a tailored view.

> **Synthetic case.** Roles are synthetic.

### Errors and limits

Owners approving lists without examining them makes reviews meaningless.

### Exercises

- **EX046 — Masked access.** How do repairs analysts see tenant names? *Rubric:* 3 = through a masking view;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX047 — Log patterns.** What unusual patterns are reviewed? *Rubric:* 3 = large exports or out-of-hours access;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX048 — Finance view.** What did the finance view contain? *Rubric:* 3 = job identifiers, contractors and costs;; 2 = partly correct;; 1 = partial;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Pseudonymisation for extracts

### Learning outcomes

You will (1) pseudonymise identifiers with keyed hashes; (2) preserve linkage for analysis; (3) explain the limits of pseudonymisation.

### 17.1 The need

An analyst wants to study whether some tenants report the same problem repeatedly, which could indicate poor repairs. The study needs to link jobs for the same tenant but not to know who the tenant is. Ravi proposes replacing tenant identifiers with pseudonyms in the extract. He explains that pseudonymisation reduces risk if the extract is lost or misused, while still allowing the analyst to count jobs per tenant and look for patterns. The tenancy owner approves the extract with pseudonyms in place.

### Lab — Keyed-hash pseudonyms for tenant identifiers in a synthetic extract

```python
"""Mask tenant identifiers in a synthetic extract with keyed hashes and check linkage (stdlib only)."""
import hmac, hashlib
key = b"synthetic-teaching-key"
def p(t): return hmac.new(key, t.encode(), hashlib.sha256).hexdigest()[:12]
rows = [("T1001", "leak"), ("T1002", "boiler"), ("T1001", "damp"), ("T1003", "lock"), ("T1001", "leak")]
masked = [(p(t), j) for t, j in rows]
print(f"rows {len(rows)}; distinct tenants {len({t for t,_ in rows})}; distinct pseudonyms {len({t for t,_ in masked})}")
print(f"T1001 pseudonym {p('T1001')}; jobs linked {sum(1 for t,_ in masked if t == p('T1001'))}")
```

Run with `python3 lab_mask.py`. Verified output:

```text
rows 5; distinct tenants 3; distinct pseudonyms 3
T1001 pseudonym 083752155d81; jobs linked 3
```

### 17.2 How it works

The lab uses Python's hmac and hashlib modules to create a keyed hash of each tenant identifier with a secret key held by the data team. In a five-row synthetic extract with three distinct tenants, the result has three distinct pseudonyms. Tenant T1001 becomes 083752155d81, and all three of that tenant's jobs share the same pseudonym, so the analyst can see that one tenant had three jobs, including two leaks, without knowing the identifier. The analyst confirms that the linkage meets the study's needs.

### 17.3 Protecting the key

The key is what makes pseudonyms hard to reverse. Without the key, someone with a list of tenant identifiers cannot recompute pseudonyms. Ravi stores the key in the data team's restricted vault, not in the script, and limits access to two people. He sets a rule that the same key is used only for one project, so pseudonyms from different extracts cannot be linked by others. Each use of the key is recorded. Access to the vault is reviewed every quarter by the owner.

### 17.4 Limits

Ravi explains that pseudonymised data remain personal data under the GDPR, because the data team can re-identify tenants with the key and because other details, such as a rare repair at a specific property, might identify someone. The extract therefore still needs access controls and a retention date. Ms. Moreau notes that pseudonymisation is a valuable safeguard but not anonymisation, and that NIST SP 800-188 discusses why de-identification must consider all fields together. The extract is given a deletion date at the end of the analyst's study.

### Worked example

Ravi pseudonymises tenant identifiers with keyed hashes, keeps three tenants as three pseudonyms with T1001's three jobs linked, protects the key in a vault per project and explains that the extract remains personal data.

> **Synthetic case.** The extract and key are synthetic; outputs come from lab_mask.py; the GDPR and NIST SP 800-188 are real.

### Errors and limits

Plain hashes without a key can be reversed by hashing known identifiers.

### Exercises

- **EX049 — T1001 pseudonym.** What pseudonym did T1001 receive? *Rubric:* 3 = 083752155d81;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX050 — Key storage.** Where is the key stored? *Rubric:* 3 = the data team's restricted vault;; 2 = partly correct;; 1 = script;; 0 = none.
- **EX051 — Legal status.** Are pseudonymised extracts still personal data? *Rubric:* 3 = yes;; 2 = partly correct;; 1 = no;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Privacy requests

### Learning outcomes

You will (1) support subject access requests technically; (2) find a person's data across systems; (3) handle correction and erasure requests.

### 18.1 Access requests

A tenant asks Calder Valley for a copy of all personal data held about them. The data protection officer coordinates, and Ravi helps find data. He uses the dictionary and inventory to list systems holding tenant data: housing system, contractor portal, complaints, call recordings index and shared drive files. He writes queries for each structured system using the tenant's identifiers. He notes that a good inventory turns a stressful search into a routine task. The officer welcomes the list of systems warmly.

### 18.2 Finding everything

The duplicate tenant records from earlier chapters matter here: the tenant has two records, and the second holds old repair history. Ravi finds it through the matching rules. He also searches the shared drive for the tenant's name, finding a spreadsheet of complaint notes. He compiles results for the officer, who reviews them, removes information about other people and sends the response within the legal deadline. Ravi records the search steps in a short guide, so that the next request can be handled faster and more consistently by any member of the data team.

### 18.3 Corrections

Another tenant reports that their phone number is wrong. The correction must be made in the housing system and also in the contractor portal, which holds a copy for appointment calls. Ravi documents which systems hold copies of each tenant field, so corrections reach all of them. He notes that copies are where corrections often fail, leaving outdated data in some systems while the main record is correct. Corrections now include a check of each copy listed, and the officer confirms that the tenant's number has been updated everywhere.

### 18.4 Erasure

A former tenant asks for erasure. The officer decides which data can be erased and which must be kept, such as rent records needed for financial obligations. Ravi carries out deletion in the systems where data can be erased and records what was removed and what was retained, with reasons. Ms. Moreau notes that technologists need clear instructions from the officer, because erasure decisions involve legal judgement that technical staff should not make alone. Ravi's record is filed with the original request.

### Worked example

Ravi lists systems holding tenant data for an access request, finds a duplicate record and a complaint spreadsheet, maps copies of fields for corrections and carries out erasure under the officer's instructions.

> **Synthetic case.** Requests are synthetic; the GDPR is real. This is not legal advice.

### Errors and limits

Corrections made only in the main system leave outdated copies elsewhere.

### Exercises

- **EX052 — Hidden data.** What hidden data did Ravi find for the access request? *Rubric:* 3 = a duplicate record and a complaint spreadsheet;; 2 = both;; 1 = one;; 0 = none.
- **EX053 — Phone copy.** Where was a copy of the phone number? *Rubric:* 3 = the contractor portal;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX054 — Retained records.** Which records were kept despite erasure? *Rubric:* 3 = rent records for financial obligations;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Retention and disposal

### Learning outcomes

You will (1) apply a retention schedule technically; (2) automate disposal; (3) record disposal as evidence.

### 19.1 The schedule

Calder Valley's retention schedule says repair job records are kept for six years after completion, tenant records for six years after the tenancy ends and call recordings for six months. Ravi translates each rule into a query that finds records past their retention date. He checks the rules with the records officer, who confirms exceptions, such as records involved in legal claims, which must be kept until the claim ends. Ravi adds a legal hold flag to the jobs table so that such records can be excluded automatically.

### 19.2 Automating disposal

Ravi writes a monthly script that lists records due for disposal, excludes those flagged for legal hold and produces a report for the owner to approve. After approval, the script deletes or anonymises the records, depending on the schedule. For repair jobs, the property and job type are kept for long-term analysis, but tenant links are removed. He tests the script on synthetic data first and runs it with logging enabled. The first run removes tenant links from thousands of old synthetic jobs.

### 19.3 Evidence

Each disposal run produces a record: date, rule applied, number of records, approval and any errors. Ravi stores these in a disposal log. When the regulator asks how Calder Valley ensures it does not keep data longer than needed, Mrs. Okonjo shows the schedule, the script, the approvals and the log. Ravi notes that evidence of disposal is as important as the disposal itself for demonstrating compliance. The regulator's reviewer accepts the evidence and notes Calder Valley's disposal practice as a strength in the review report.

### 19.4 Backups and copies

Disposal in live systems does not remove data from backups and extracts. Ravi confirms with IT that backups expire after ninety days, so disposed records disappear from backups within that time. He also checks the shared drive for extracts older than the schedule allows and asks owners to delete them. Ms. Moreau explains that retention must cover every copy, and that extracts are the hardest to control because they are created informally. Owners delete most of the old extracts, and the rest are given deletion dates.

### Worked example

Ravi turns retention rules into queries with legal hold exceptions, automates approved monthly disposal that keeps property and job type but removes tenant links, logs disposal as evidence and checks backups and extracts.

> **Synthetic case.** The schedule is synthetic.

### Errors and limits

Disposal limited to live systems leaves data in extracts and backups.

### Exercises

- **EX055 — Recording retention.** How long are call recordings kept? *Rubric:* 3 = six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX056 — Kept fields.** What is kept after repair job disposal? *Rubric:* 3 = property and job type;; 2 = both;; 1 = one;; 0 = none.
- **EX057 — Backup expiry.** When do backups expire? *Rubric:* 3 = after ninety days;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Contractor data

### Learning outcomes

You will (1) govern data exchanged with contractors; (2) monitor contractor data quality; (3) handle contractor changes.

### 20.1 Data flows

Contractors receive job details, property addresses and tenant contact information to arrange visits, and return completion updates, costs and photographs. Ravi lists each flow with fields, frequency and purpose. He checks the contract and finds data protection terms but no data quality requirements. He suggests adding the exchange specification and timeliness targets to the contract at renewal, so contractors have clear obligations for the data they return. The repairs owner agrees, and the terms are added to the renewal plan for each contractor's agreement.

### 20.2 Monitoring quality

Ravi builds a monthly contractor data scorecard: share of files passing validation, share of jobs updated within a day of completion and share of completion records with photographs. He shares each contractor's scorecard with them and with the repairs manager. One contractor's photograph rate is low; it explains that its app crashes when uploading large images. Calder Valley's portal team raises the upload limit, and the rate improves. Ravi adds a short note to each scorecard explaining any change from the previous month, which helps contractors understand their results.

### 20.3 Minimising shared data

Ravi reviews what contractors receive and finds they get tenants' full dates of birth, which they do not need. He removes the field from the export after checking with the tenancy owner. Contractors receive only name, address, phone and access notes needed for visits. He notes that minimising shared data reduces the harm if a contractor suffers a breach, and that exports often include fields simply because they were in the source table. Ravi checks the other exports for similar unneeded fields.

### 20.4 Contractor changes

When a contractor's contract ends, Ravi follows an exit checklist: stop exports, disable portal accounts, request confirmation that Calder Valley data have been deleted and record the confirmation. He also checks that open jobs have been reassigned. Ms. Moreau notes that exits are often rushed, and that a checklist ensures data obligations are not forgotten when attention focuses on handing over work. Ravi uses the checklist for the first time when a small contractor leaves, and every step is completed within two weeks, with the deletion confirmation filed in the contractor's record.

### Worked example

Ravi lists contractor flows and suggests quality terms, builds a monthly scorecard that reveals photo upload failures, removes unnecessary dates of birth from exports and follows an exit checklist when a contract ends.

> **Synthetic case.** Contractors are synthetic.

### Errors and limits

Exporting whole tables sends contractors fields they do not need.

### Exercises

- **EX058 — Contract gap.** What was missing from contractor contracts? *Rubric:* 3 = data quality requirements;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX059 — Photo cause.** Why was one contractor's photo rate low? *Rubric:* 3 = its app crashed on large images;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX060 — Removed field.** Which field did Ravi remove from exports? *Rubric:* 3 = full date of birth;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Measuring contractor performance

### Learning outcomes

You will (1) compute performance against a time target; (2) compare contractors with medians and shares; (3) present results fairly.

### 21.1 The target

Calder Valley requires emergency repairs to be completed within twenty-four hours of the tenant's first report. Two contractors carry out emergencies: one in the north of the area and one in the south. Ravi measures each contractor's performance using full timestamps, following the lineage fixes from chapter 13, and the first-report time field added in chapter 9. He calculates the share completed within twenty-four hours and the median time, which shows a typical job rather than being distorted by a few very long ones.

### Lab — Emergency repairs within twenty-four hours for two synthetic contractors

```python
"""Share of synthetic emergency repairs completed within 24 hours, by contractor (stdlib only)."""
import random
random.seed(4)
for name, mean in [("North contractor", 10), ("South contractor", 17)]:
    h = [random.expovariate(1/mean) for _ in range(800)]
    print(f"{name}: within 24h {100*sum(x <= 24 for x in h)/len(h):.1f}%; median {sorted(h)[400]:.1f}h")
```

Run with `python3 lab_emergency.py`. Verified output:

```text
North contractor: within 24h 89.1%; median 7.2h
South contractor: within 24h 74.2%; median 12.5h
```

### 21.2 Results

The lab simulates eight hundred emergency jobs for each contractor. The north contractor completes 89.1 percent within twenty-four hours, with a median of 7.2 hours. The south contractor completes 74.2 percent, with a median of 12.5 hours. Ravi notes that the gap is clear in both measures, so it is unlikely to come from a handful of unusual jobs. He presents both measures together, because a share alone hides how far from the target late jobs fall. He shows the two contractors side by side in a short table for the manager.

### 21.3 Fair comparison

Before presenting, Ravi asks whether the comparison is fair. The south area is more rural, with longer travel distances, which could explain some of the difference. He checks whether job types differ between areas in the synthetic data and finds a similar mix. He includes the travel caveat in his report and suggests comparing jobs within similar distances in a follow-up. Ms. Moreau notes that technologists should anticipate fairness questions rather than leaving managers to discover them later. The manager welcomes the caveat.

### 21.4 Using the results

The repairs manager meets the south contractor with Ravi's results. The contractor explains that it has only one emergency team overnight. Calder Valley and the contractor agree to add a second overnight team for a trial period, with monthly measurement using the same script. Ravi documents the measurement method in the dictionary so both parties trust future figures. He notes that agreed measurement methods turn performance discussions from arguments about numbers into discussions about improvement. The trial begins the following month, with results reviewed jointly.

### Worked example

Ravi measures emergency repairs with full timestamps, finding north 89.1 percent and median 7.2 hours versus south 74.2 percent and 12.5 hours, considers rural travel and supports a trial second overnight team.

> **Synthetic case.** Jobs are synthetic; outputs come from lab_emergency.py.

### Errors and limits

Reporting only a share hides how late the late jobs are.

### Exercises

- **EX061 — South share.** What share did the south contractor complete within twenty-four hours? *Rubric:* 3 = 74.2%;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX062 — North median.** What was the north contractor's median time? *Rubric:* 3 = 7.2 hours;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX063 — Overnight cause.** What did the south contractor reveal? *Rubric:* 3 = only one emergency team overnight;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Dashboards and reporting

### Learning outcomes

You will (1) design dashboards for different users; (2) show data quality alongside figures; (3) avoid misleading displays.

### 22.1 Users and needs

Ravi designs dashboards for three groups. The repairs manager wants daily open jobs by priority and contractor. Contractors want their own performance against targets. The board wants monthly trends against regulatory targets. Each dashboard shows only what its users need. He sketches layouts on paper and asks each group for feedback before building. He notes that dashboards built without asking users often show many figures that nobody uses. The feedback removes several figures from Ravi's first sketches and adds one that he had missed, a count of jobs awaiting parts.

### 22.2 Quality alongside figures

Each dashboard shows a small quality indicator: the share of jobs with complete and valid data and the date of the latest load. If quality falls below the threshold, the indicator turns amber and explains why. When a contractor's file is held one day, the manager's dashboard shows that the contractor's figures are incomplete. Ravi explains that showing quality helps users judge how much to trust a figure before acting on it. The repairs manager says the indicator stopped him chasing a contractor unfairly.

### 22.3 Honest displays

Ravi follows display rules: bar charts start at zero, time series use consistent intervals, colours are explained and targets are shown as lines. He avoids three-dimensional charts and unnecessary decorations. For the board, he shows twelve months of trends rather than only the latest month, so that a single unusual month does not dominate. Ms. Moreau notes that honest displays are part of data governance, because misleading charts produce poor decisions from accurate data. Ravi writes these rules into a short style guide for the team.

### 22.4 Maintaining dashboards

Dashboards need owners and maintenance. Ravi records each dashboard in the catalogue with its owner, data sources, refresh schedule and users. He sets up a check that alerts him if a dashboard has not refreshed. Every six months he asks owners whether dashboards are still used, and retires two unused ones. He notes that unused dashboards waste effort and can mislead anyone who finds them without knowing they are out of date. Owners confirm the remaining dashboards and agree to tell him when needs change.

### Worked example

Ravi designs dashboards for managers, contractors and the board with user feedback, adds quality indicators and load dates, follows honest display rules and catalogues and retires dashboards.

> **Synthetic case.** Dashboards are synthetic.

### Errors and limits

Dashboards without quality indicators invite overconfidence in incomplete figures.

### Exercises

- **EX064 — Board view.** What does the board dashboard show? *Rubric:* 3 = twelve months of trends against targets;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX065 — Amber indicator.** When does the quality indicator turn amber? *Rubric:* 3 = quality below threshold;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX066 — Retired count.** How many unused dashboards were retired? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Regulatory returns

### Learning outcomes

You will (1) prepare data for regulatory returns; (2) document calculations and checks; (3) support sign-off by owners.

### 23.1 The return

Calder Valley submits an annual return to its regulator including repair performance, safety compliance and tenant satisfaction. Ravi helps prepare the repair figures. He reads the regulator's definitions carefully and compares them with Calder Valley's own measures. He finds that the regulator counts repairs by the date of completion within the year, while Calder Valley's internal reports count by the date raised. He adjusts the calculation for the return to match the regulator's definition. He records the reason for the difference in the calculation note.

### 23.2 Documenting calculations

Ravi writes a calculation note for each figure in the return: the definition, the source tables, filters, the script used, the result and the checks performed. He saves the script version used in the repository with a tag for the return year. He explains that documentation lets the owner and auditors verify the figures, and allows next year's preparer to repeat the method consistently even if Ravi has moved on. The owner reads every note before the return is prepared, and asks two questions that lead to clearer wording.

### 23.3 Checks

Before sign-off, Ravi runs checks: totals reconcile with monthly reports adjusted for the definition difference, no jobs are counted twice and figures are within expected ranges compared with last year. One figure differs substantially from last year. Investigation shows that a contractor's jobs were missing from last year's return because of a loading failure. The owner decides to note the error in this year's return rather than ignore it. The regulator's guidance allows corrections of this kind, and the owner explains the cause and the fix in a short covering note.

### 23.4 Sign-off

The head of repairs, as owner, signs off the figures after reviewing the calculation notes and check results. Ravi prepares a short summary of any judgements made, such as how unknown completion times were treated. Ms. Moreau notes that the owner signs because they are accountable, and that technologists support sign-off by making evidence clear rather than asking owners simply to trust the numbers they are given. The owner signs the return after a meeting in which Ravi walks through each note, and the signed copy is filed with the evidence for future reference.

### Worked example

Ravi aligns the return with the regulator's completion-date definition, documents calculations with tagged scripts, finds last year's missing contractor jobs during checks and supports owner sign-off with clear evidence.

> **Synthetic case.** The return is synthetic.

### Errors and limits

Using internal definitions for regulatory figures misreports performance.

### Exercises

- **EX067 — Definition difference.** How did definitions differ? *Rubric:* 3 = completion date versus date raised;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX068 — Year difference cause.** What explained the change from last year? *Rubric:* 3 = a contractor's jobs missing from last year;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX069 — Signing owner.** Who signs off the repair figures? *Rubric:* 3 = the head of repairs;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Issue logs and root causes

### Learning outcomes

You will (1) run an issue log; (2) use root cause techniques; (3) track issues to closure.

### 24.1 The log

Ravi maintains the data issue log for repairs. Each issue records description, reporter, date, data affected, impact, priority, owner, status and resolution. Anyone can submit issues through a form. The steward triages weekly. Ravi adds a link to supporting evidence, such as check results. He explains that a log gives the organisation a memory of problems and their fixes, which prevents the same investigation being repeated when a problem returns. The log is reviewed at the monthly repairs meeting, where the most serious open issues are discussed.

### 24.2 Root causes

Ravi uses the five whys technique on an issue where tenant phone numbers are often wrong. Why? Because they are entered incorrectly. Why? Because call handlers type them from memory after calls. Why? Because the screen to edit numbers is not open during calls. Why? Because opening it takes several clicks. Why? Because the system layout was never reviewed. The fix is to show the phone field on the main call screen. The supplier makes the change, and call handlers welcome the simpler screen.

### 24.3 Tracking closure

Issues close only with evidence. For the phone number issue, Ravi measures the share of numbers confirmed correct in a sample before and after the screen change and records the improvement. He also confirms with call handlers that the new layout works. Issues closed without evidence are reopened. He notes that the reopening rate itself is a useful measure of whether fixes really work. In the first quarter, two issues are reopened because their fixes did not hold, and both are then fixed properly after a second root cause investigation by the steward and Ravi.

### 24.4 Patterns

After six months, Ravi groups issues by cause: manual entry, system design, partner data, unclear definitions and process gaps. Manual entry and partner data cause most issues. He presents the patterns to Mrs. Okonjo, who prioritises validation at entry and contractor specifications for the next year. Ms. Moreau explains that issue logs become strategic tools when their patterns guide investment, rather than serving only as lists of individual tasks. The patterns are repeated every six months, and Ravi adds a chart showing how the mix of causes changes over time.

### Worked example

Ravi runs a repairs issue log with evidence links, traces wrong phone numbers through five whys to screen layout, closes issues with measured evidence and groups six months of causes to guide priorities.

> **Synthetic case.** Issues are synthetic.

### Errors and limits

Fixing symptoms without root causes lets issues recur.

### Exercises

- **EX070 — Phone root cause.** What was the root cause of wrong phone numbers? *Rubric:* 3 = the system layout hid the phone field during calls;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX071 — Reopening measure.** What does the reopening rate show? *Rubric:* 3 = whether fixes really work;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX072 — Top causes.** Which causes produced most issues? *Rubric:* 3 = manual entry and partner data;; 2 = both;; 1 = one;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Data incidents

### Learning outcomes

You will (1) recognise data incidents; (2) follow an incident procedure; (3) learn from incidents.

### 25.1 What counts

A data incident is an event that harms data confidentiality, integrity or availability, such as a lost laptop with tenant data, a wrong file sent to a contractor or a failed load leaving reports incomplete. Ravi learns Calder Valley's incident procedure: report immediately to the data protection officer or data manager, contain the problem, assess impact, notify if required and review lessons. He notes that speed matters, because legal notification deadlines may apply. Ravi keeps a printed copy of the procedure beside his desk.

### 25.2 An incident

Ravi notices that a contractor export sent overnight contained tenants from another contractor's area. He reports it at once. The contractor is asked to delete the file and confirm. Ravi traces the cause to a filter in the export script that used a postcode list which had not been updated after an area boundary change. The data protection officer assesses the risk to tenants and decides whether notification is required under the GDPR. Ravi records each step and its time in the incident log.

### 25.3 Containment and fix

While the officer assesses, Ravi pauses the export, corrects the filter to use the contractor allocation field rather than postcodes, tests it with synthetic data and resumes exports after the steward approves. He checks the previous week's exports and finds the error began three days earlier. Those contractors are also asked to delete affected files. Each action is recorded with times in the incident log. The officer uses the log to complete the assessment, and the decision on notification is recorded together with its reasons and the date it was made.

### 25.4 Lessons

The incident review finds that boundary changes were not communicated to the data team. The fix is to add the data team to the change process for contractor areas, and to add an export check comparing each contractor's tenants with its allocation. Ms. Moreau notes that blameless reviews focus on how systems allowed an error rather than on who made it, which encourages people to report incidents quickly in future. Both changes are made within a month, and the export check has caught no further errors since it was added.

### Worked example

Ravi reports a misdirected contractor export, traces it to an outdated postcode filter, pauses and fixes the export, finds three earlier affected days and supports a review that adds the data team to boundary changes.

> **Synthetic case.** The incident is synthetic; the GDPR is real.

### Errors and limits

Delaying incident reports can miss legal deadlines.

### Exercises

- **EX073 — Export cause.** What caused the misdirected export? *Rubric:* 3 = an outdated postcode list after a boundary change;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX074 — Filter fix.** What did Ravi filter on instead? *Rubric:* 3 = the contractor allocation field;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX075 — Review style.** What do blameless reviews focus on? *Rubric:* 3 = how systems allowed the error;; 2 = partly correct;; 1 = who;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Automation and scheduling

### Learning outcomes

You will (1) schedule data checks and loads; (2) handle dependencies and failures; (3) monitor automated jobs.

### 26.1 Scheduling

Ravi's checks, loads and reports now run on a schedule. Contractor files load at two in the morning, checks run at three, summary tables at four and dashboards refresh at five. He documents the schedule in a table with each job, its time, dependencies and owner. He notes that schedules make governance routine, but also create dependencies: if the load fails, every later job may run on incomplete data. The table is published with the dictionary so that users know when each report is refreshed each morning.

### 26.2 Dependencies

Ravi adds dependency checks: each job confirms that the previous job finished successfully and produced expected row counts before starting. If not, it stops and sends an alert. One night, a contractor file is late, and the load waits. The checks hold the summary job, and the dashboard shows an amber indicator rather than incomplete figures. He explains that controlled failure is better than silent success on bad data. The contractor's file arrives later that morning, and the jobs run in sequence once the load completes successfully.

### 26.3 Monitoring

Ravi creates a job monitoring summary each morning: which jobs ran, how long they took, records processed and any failures. Run times are tracked over time; when the check job slows down as data grow, he notices before it misses its window. He adds an index to the jobs table, which restores speed. Ms. Moreau notes that monitoring the governance machinery itself prevents gradual failures from going unnoticed until they cause problems. He records the change and the run times before and after it in the change log.

### 26.4 Change control

Changes to scheduled jobs follow a simple process: test on synthetic data, review by a colleague, record in the change log and deploy at a quiet time. When Ravi changes the export filter after the incident, he follows this process even under pressure. He notes that skipping change control during emergencies is tempting but often causes new problems, and that a quick but disciplined process serves better than shortcuts. The change log shows each change with its test result, reviewer and the time it was deployed.

### Worked example

Ravi schedules loads, checks, summaries and dashboards with documented dependencies, stops jobs on failed predecessors, monitors run times and adds an index, and applies change control even during the incident.

> **Synthetic case.** Jobs are synthetic.

### Errors and limits

Jobs that run regardless of failed predecessors publish incomplete figures.

### Exercises

- **EX076 — Check time.** When do checks run? *Rubric:* 3 = three in the morning;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX077 — Slowdown fix.** How did Ravi fix the slowing check job? *Rubric:* 3 = added an index;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX078 — Change steps.** Name the change control steps. *Rubric:* 3 = test, review, log and deploy at a quiet time;; 2 = most;; 1 = few;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Documentation and handover

### Learning outcomes

You will (1) document technical governance work; (2) prepare handover for colleagues; (3) reduce dependence on individuals.

### 27.1 What to document

Ravi lists what others would need if he left: the repository with scripts and tests, the check library with purposes, the schedule, procedures, dictionary, lineage notes, dashboards and their owners, and known issues. He writes a short overview page linking to each item. Ms. Moreau explains that documentation is a governance control, because organisations depend on technical work that nobody can maintain if only one person understands it. Mrs. Okonjo asks him to present the overview to the whole data team, so that everyone knows where to find it.

### 27.2 Handover practice

To test documentation, Ravi takes a week of leave while a classmate on placement at Calder Valley covers his work using only the documentation. She manages most tasks but struggles with a held contractor file, because the procedure does not explain how to release a file after the contractor resends it. Ravi adds the missing steps when he returns. He notes that real handover tests reveal gaps that self-review misses. His classmate also suggests an index of common tasks, which he adds to the overview page.

### 27.3 Reducing dependence

Ravi pairs with a colleague on monthly tasks, such as disposal runs and access reviews, so that two people can do each. He also records short screen recordings showing complex steps. Mrs. Okonjo adds technical governance tasks to the team's skills matrix to track who can do what. He notes that dependence on one person is a risk that governance should manage, like any other risk to data. By the end of the placement, every monthly task has at least two people who can carry it out.

### 27.4 Keeping documentation alive

Documentation decays as systems change. Ravi links each document to the scripts or processes it describes and adds a reminder to update documentation as part of every change. He schedules a quarterly review where the team checks a sample of documents against reality. Ms. Moreau notes that small, regular updates keep documentation useful, whereas large rewrites happen rarely and leave documents outdated for long periods between them. The first quarterly review finds three documents that need small changes, which are made the same week.

### Worked example

Ravi documents his work with an overview page, tests it through a week's handover that exposes a missing release step, pairs on monthly tasks and keeps documentation current through change reminders and quarterly reviews.

> **Synthetic case.** Documentation is synthetic.

### Errors and limits

Untested documentation hides gaps until someone needs it urgently.

### Exercises

- **EX079 — Handover gap.** What gap did the handover reveal? *Rubric:* 3 = how to release a held file after resend;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX080 — Skills tracking.** How does Mrs. Okonjo track who can do tasks? *Rubric:* 3 = a skills matrix;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX081 — Documentation review.** How often is a sample of documents checked? *Rubric:* 3 = quarterly;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Work placement

### Learning outcomes

You will (1) apply skills in a work placement; (2) work within an organisation's processes; (3) reflect on professional practice.

### 28.1 The placement

In year three, Ravi spends a term on placement in Calder Valley's data team. All examples in this book remain synthetic. He supports stewards, maintains checks and joins incident and change processes. He finds that real work involves more communication than he expected: explaining check results to managers, negotiating file formats with contractors and helping call handlers understand codes. Technical skills matter, but so does explaining clearly. He keeps a weekly log of the communication tasks that took most of his time and what he learned from them.

### 28.2 Organisational processes

Ravi learns Calder Valley's processes: change requests need approval from IT, data releases need owner approval and incidents follow the procedure. At first he finds these slow. After seeing a colleague's untested change break a report, he appreciates their purpose. He learns to plan work around approval times and to prepare requests with clear evidence so that approvals happen quickly rather than being delayed by questions. His requests are approved faster as a result, and his supervisor notes the improvement in his mid-placement review.

### 28.3 Professional conduct

A manager asks Ravi to send him a full tenant list to his personal email so he can work at home. Ravi explains that this would breach policy and suggests using the approved remote access system. The manager accepts. Ravi reports the request to his supervisor, not as a complaint but so that the data team can remind staff about remote access options. He reflects that saying no politely with an alternative is a key professional skill. The reminder goes out that week.

### 28.4 Reflection

Ravi's placement report describes his work, what he learned and how course content applied. He notes that the most valuable contributions were often small: a clearer procedure, a check that caught an error early or a dictionary entry that settled a dispute. He identifies a topic for his applied project: reducing the time between repair completion and system update, which affects many reports. Ms. Moreau approves the topic. He includes examples of each small contribution in the report, with the effect each had on the work of others.

### Worked example

Ravi finds placement work communication-heavy, learns to value approval processes after seeing an untested change fail, declines a personal email request with an alternative and chooses completion update delay as his project topic.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Sending data to personal accounts bypasses security controls.

### Exercises

- **EX082 — Process lesson.** What made Ravi appreciate approval processes? *Rubric:* 3 = a colleague's untested change broke a report;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX083 — Personal email response.** What did Ravi suggest instead of personal email? *Rubric:* 3 = the approved remote access system;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX084 — Project topic.** What is Ravi's applied project topic? *Rubric:* 3 = reducing delay between completion and system update;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Applied project

### Learning outcomes

You will (1) plan and deliver an applied improvement project; (2) measure results against a baseline; (3) document the solution for handover.

### 29.1 Problem and baseline

Ravi's project addresses delay between repair completion and the update appearing in the housing system. Delays make reports show jobs as open when they are finished and cause tenants to receive unnecessary calls. Using synthetic data that mirror his placement observations, he measures a baseline: the share of completions updated within one day and the median delay. He agrees a target with the repairs steward and a plan with milestones. The baseline figures are recorded in the project log before any changes begin.

### 29.2 Causes

Ravi investigates causes. Some contractors update the portal only at the end of each day; others batch updates weekly. The portal sends updates to the housing system once nightly, adding up to a day more. Some updates fail validation and wait for correction. He ranks causes by their contribution to delay and finds weekly batching by one contractor and the nightly transfer to be the largest contributors. He shares the ranking with the steward, who agrees to tackle the two largest causes first and leave the smaller ones for later.

### 29.3 Changes

With the steward's approval, Ravi works with the portal team to send updates every hour instead of nightly. The contractor that batches weekly agrees to daily updates after seeing its scorecard. Ravi improves validation messages so contractors fix failed updates faster. He tests each change on synthetic data and follows change control. He keeps a project log recording decisions, tests and results for his assessment. The changes go live one at a time, so that the effect of each can be seen separately in the monitoring results.

### 29.4 Results and handover

After changes, synthetic data designed to match the new process show the share updated within one day rising and the median delay falling. Ravi notes that real monitoring must confirm this. He hands the monitoring script, documentation and scorecard updates to the steward, with a monthly check scheduled. Ms. Moreau notes that projects succeed when they leave behind working processes and owners, not only a report describing what was done. The steward confirms that the handover pack is complete and that she can run the monitoring alone.

### Worked example

Ravi baselines completion update delay, traces it to weekly batching and nightly transfers, introduces hourly transfers, daily contractor updates and clearer validation messages and hands over monitoring to the steward.

> **Synthetic case.** The project data are synthetic.

### Errors and limits

Projects that end without handover leave improvements unsupported.

### Exercises

- **EX085 — Largest causes.** Which causes contributed most delay? *Rubric:* 3 = weekly batching by a contractor and the nightly transfer;; 2 = both;; 1 = one;; 0 = none.
- **EX086 — Transfer change.** How often does the portal now send updates? *Rubric:* 3 = hourly;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX087 — Handover recipient.** Who receives the monitoring script? *Rubric:* 3 = the repairs steward;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Project review and next steps

### Learning outcomes

You will (1) present an applied project for assessment; (2) reflect on learning across the course; (3) plan a technologist career.

### 30.1 Presentation

Ravi presents his project to Ms. Moreau, an external assessor and Mrs. Okonjo. He shows the problem, baseline, causes, changes, results and handover. The assessor asks how he knows the improvement came from his changes rather than seasonal variation. Ravi explains that his synthetic data cannot answer that, and that the steward's monthly monitoring over a year will. The assessor appreciates his honesty about what the project can claim. Mrs. Okonjo confirms that monitoring is already scheduled and that the first results will be shared with Eastgate.

### 30.2 Feedback

The assessors praise his clear causes analysis and practical handover. They suggest that he could have involved contractors earlier in designing changes, as one contractor initially resisted. Ravi agrees and notes it for future projects. Mrs. Okonjo says the hourly transfer has already reduced unnecessary tenant calls, according to call handlers, though she agrees that measured evidence will follow from the monitoring. Ravi thanks the assessors for their comments and records them in his journal, together with a note on how he would involve contractors in the design of his next project.

### 30.3 Reflection

Ravi reflects on three years: from scripts and SQL to validation, lineage, access control, pseudonymisation, retention, incidents and projects. He values the habits of asking who owns a decision, checking data at the source and documenting work so others can continue it. He notes that governance became concrete through practical tasks, and that technical work gained purpose once he understood whom it served. He also notes that his confidence in explaining technical issues to managers grew most during the placement, and that this skill will matter in his future work.

### 30.4 Next steps

Ravi accepts a job as a data technologist at Calder Valley. Ms. Moreau encourages him to keep learning, perhaps later taking a bachelor's degree part-time. She reminds him that his role will often involve noticing problems first and raising them with evidence. The next course in this area turns to privacy and data protection, where governed data meet the rights of the people they describe. Ravi thanks Ms. Moreau and Mrs. Okonjo, and starts his new role the following month with a plan to extend the check library to rent data.

### Worked example

Ravi presents his project honestly about seasonality, accepts feedback to involve contractors earlier, reflects on three years of practical governance and joins Calder Valley as a data technologist.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Claiming effects synthetic data cannot show undermines credibility.

### Exercises

- **EX088 — Seasonality answer.** How will seasonality be addressed? *Rubric:* 3 = the steward's monthly monitoring over a year;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX089 — Assessor suggestion.** What did assessors suggest? *Rubric:* 3 = involve contractors earlier;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX090 — Ravi's job.** What job does Ravi accept? *Rubric:* 3 = data technologist at Calder Valley;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Ravi Desai, Ms. Hannah Moreau, Eastgate Institute of Technology, Calder Valley Housing Association and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About nine thousand.

**EX002.** The tools, checks and reports that make governance work.

**EX003.** The quality of repair job records.

**EX004.** The property identifier.

**EX005.** Three.

**EX006.** Every year.

**EX007.** Four.

**EX008.** They sort correctly.

**EX009.** Old call lists containing tenant names and phone numbers.

**EX010.** Properties were removed while jobs were still open.

**EX011.** Same property, same description, dates within two days.

**EX012.** Checking for open jobs at the property before creating one.

**EX013.** Use descriptive names such as count_jobs_by_status.

**EX014.** Stops and reports which column is missing.

**EX015.** One contractor used day-month order and another month-day.

**EX016.** It carries no data types.

**EX017.** They are held, and the contractor receives a problem report.

**EX018.** An optional extra column.

**EX019.** The share of jobs whose status matches between systems.

**EX020.** Accuracy of completion dates and priorities.

**EX021.** Small process changes at the source.

**EX022.** 95.3 percent, 5,719 jobs.

**EX023.** A contractor portal that does not convert case.

**EX024.** Call handlers created emergency jobs after contractors had already fixed them.

**EX025.** Errors keep arriving and guesses may be wrong.

**EX026.** The time the tenant first reported the problem.

**EX027.** With a reason code.

**EX028.** The repairs steward.

**EX029.** Add to the master list first, then to each system.

**EX030.** Plaster repair and wall repair.

**EX031.** Split rent accounts.

**EX032.** By removing spaces and converting to lowercase.

**EX033.** About a fifth.

**EX034.** Work finished by the contractor, or tenant confirmed satisfaction.

**EX035.** A weekly script comparing the schema with dictionary entries.

**EX036.** How Calder Valley defines a completed emergency repair.

**EX037.** Jobs without a completion time.

**EX038.** Date-only calculations misstate how long jobs took.

**EX039.** Separately, as unknown.

**EX040.** Excluding jobs where tenants were not home.

**EX041.** The deputy steward.

**EX042.** Data entry errors rather than missed checks.

**EX043.** What to do if the validator itself fails.

**EX044.** At step four, not knowing where held files are stored.

**EX045.** Staff follow them confidently into errors.

**EX046.** Only through a view that masks them.

**EX047.** Large exports or access outside working hours.

**EX048.** Job identifiers, contractors and costs, without tenant details.

**EX049.** 083752155d81.

**EX050.** In the data team's restricted vault.

**EX051.** Yes, they remain personal data.

**EX052.** A second tenant record and a complaint notes spreadsheet.

**EX053.** In the contractor portal.

**EX054.** Rent records needed for financial obligations.

**EX055.** Six months.

**EX056.** Property and job type, without tenant links.

**EX057.** After ninety days.

**EX058.** Data quality requirements.

**EX059.** Its app crashed when uploading large images.

**EX060.** Tenants' full dates of birth.

**EX061.** 74.2 percent.

**EX062.** 7.2 hours.

**EX063.** It had only one emergency team overnight.

**EX064.** Twelve months of trends against regulatory targets.

**EX065.** When data quality falls below the threshold.

**EX066.** Two.

**EX067.** The regulator counts by completion date; internal reports by date raised.

**EX068.** Last year's return missed a contractor's jobs.

**EX069.** The head of repairs.

**EX070.** The edit screen was not on the main call screen.

**EX071.** Whether fixes actually work.

**EX072.** Manual entry and partner data.

**EX073.** A postcode filter not updated after an area boundary change.

**EX074.** The contractor allocation field.

**EX075.** How systems allowed the error, not who made it.

**EX076.** At three in the morning.

**EX077.** By adding an index to the jobs table.

**EX078.** Test, review, record and deploy at a quiet time.

**EX079.** How to release a held contractor file after it is resent.

**EX080.** With the team's skills matrix.

**EX081.** Every quarter.

**EX082.** Seeing an untested change break a report.

**EX083.** Using the approved remote access system.

**EX084.** Reducing the delay between repair completion and system update.

**EX085.** One contractor's weekly batching and the nightly transfer.

**EX086.** Every hour.

**EX087.** The repairs steward, who receives the handover pack.

**EX088.** Through the steward's monthly monitoring over a year.

**EX089.** Involving contractors earlier in designing changes.

**EX090.** Data technologist at Calder Valley.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
